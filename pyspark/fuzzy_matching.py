import os
import sys
from pyspark.sql import Window
from pyspark.sql.functions import col, levenshtein, lower, trim, row_number, abs, length, lit

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import (
    get_extracted_scraper_data_schema,
    get_sku_master_schema,
    load_csv
)

def fuzzy_match_listings(scraper_df, sku_df, max_distance=3):
    """
    Fuzzy matches scraper listings with internal SKU Master using a tiered approach:
    1. Tier 1: Exact join on brand and model name (extremely fast).
    2. Tier 2: Levenshtein distance join for remaining unmatched listings (narrow search space).
    """
    s = scraper_df.alias("s")
    k = sku_df.alias("k")
    
    # --- TIER 1: EXACT MATCH ---
    exact_joined = s.join(
        k,
        (lower(trim(col("s.brand"))) == lower(trim(col("k.brand")))) &
        (lower(trim(col("s.model_code"))) == lower(trim(col("k.product_name")))),
        "inner"
    )
    
    exact_result_cols = [
        col(f"s.{c}") for c in scraper_df.columns
    ] + [
        col("k.sku_id"),
        col("k.product_name").alias("matched_model_name"),
        lit(0).alias("levenshtein_distance")
    ]
    exact_matches = exact_joined.select(*exact_result_cols)
    
    # --- TIER 2: FUZZY MATCH (Only for unmatched listings) ---
    unmatched_scraper = s.join(exact_matches, "product_id", "left_anti")
    
    # Join unmatched on brand
    fuzzy_joined = unmatched_scraper.join(
        k,
        lower(trim(col("s.brand"))) == lower(trim(col("k.brand"))),
        "inner"
    )
    
    # Filter candidates by length difference constraint
    optimized_candidates = fuzzy_joined.filter(
        abs(length(lower(trim(col("s.model_code")))) - length(lower(trim(col("k.product_name"))))) <= max_distance
    )
    
    # Calculate Levenshtein distance
    dist_expr = levenshtein(lower(trim(col("s.model_code"))), lower(trim(col("k.product_name"))))
    matched_fuzzy = optimized_candidates.withColumn("levenshtein_distance", dist_expr)
    matched_fuzzy = matched_fuzzy.filter(col("levenshtein_distance") <= max_distance)
    
    # Rank candidates to find the closest match
    window_spec = Window.partitionBy("s.product_id").orderBy(
        col("levenshtein_distance").asc(),
        col("k.sku_id").asc()
    )
    ranked_fuzzy = matched_fuzzy.withColumn("rank", row_number().over(window_spec))
    best_fuzzy_matches = ranked_fuzzy.filter(col("rank") == 1).drop("rank")
    
    fuzzy_result_cols = [
        col(f"s.{c}") for c in scraper_df.columns
    ] + [
        col("k.sku_id"),
        col("k.product_name").alias("matched_model_name"),
        col("levenshtein_distance")
    ]
    fuzzy_matches = best_fuzzy_matches.select(*fuzzy_result_cols)
    
    # --- COMBINE TIER 1 & TIER 2 ---
    return exact_matches.unionByName(fuzzy_matches)

def main():
    spark = create_spark_session()
    try:
        silver_dir = "data/silver"
        
        print("\n" + "="*60)
        print("STARTING FUZZY MATCHING STAGE")
        print("="*60)
        
        # Load datasets
        scraper_df = load_csv(spark, os.path.join(silver_dir, "scraper_data.csv"), get_extracted_scraper_data_schema())
        sku_df = load_csv(spark, os.path.join(silver_dir, "SKU_Master.csv"), get_sku_master_schema())
        
        print(f"Loaded {scraper_df.count()} scraper listings.")
        print(f"Loaded {sku_df.count()} SKU master models.")
        
        # Execute matching
        print("Matching listings against SKU Master...")
        matched_df = fuzzy_match_listings(scraper_df, sku_df, max_distance=3)
        
        # Sort sequentially by product_id for neat output
        ordered_df = matched_df.orderBy("product_id")
        
        # Save output using pandas to bypass winutils.exe write issue
        out_file = os.path.join(silver_dir, "scraper_matched.csv")
        print(f"Saving matched listings to {out_file}...")
        ordered_df.toPandas().to_csv(out_file, index=False)
        
        print(f"Fuzzy matching completed. Saved {matched_df.count()} matched records.")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"Error during fuzzy matching execution: {e}")
    finally:
        spark.stop()

if __name__ == "__main__":
    main()