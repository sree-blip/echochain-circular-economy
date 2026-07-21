import os
import sys
from pyspark.sql.functions import col, count, avg, round, when

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import (
    get_matched_scraper_data_schema,
    get_sku_master_schema,
    load_csv
)

def aggregate_product_data(matched_df, sku_df):
    """
    Joins matched listings with SKU Master on sku_id,
    and aggregates listing_count, avg_original_price, avg_resale_price,
    and avg_depreciation_pct grouped by brand, category, matched_model_name, and condition.
    """
    # 1. Join matched listings and SKU Master on sku_id
    joined = matched_df.alias("m").join(
        sku_df.alias("k"),
        "sku_id",
        "inner"
    )
    
    # 2. Calculate individual depreciation percentage for each row
    # Depreciation % = ((original_price - resale_price) / original_price) * 100
    # Use when() to safely avoid division by zero or null pricing values
    with_depreciation = joined.withColumn(
        "depreciation_pct",
        when(
            (col("k.original_price").isNotNull()) & (col("k.original_price") > 0),
            ((col("k.original_price") - col("m.resale_price")) / col("k.original_price")) * 100
        ).otherwise(0.0)
    )
    
    # 3. Group by brand, category, matched_model_name, and condition
    aggregated = with_depreciation.groupBy(
        col("m.brand").alias("brand"),
        col("m.category").alias("category"),
        col("m.matched_model_name").alias("matched_model_name"),
        col("m.condition").alias("condition")
    ).agg(
        count("m.product_id").alias("listing_count"),
        round(avg("k.original_price"), 2).alias("avg_original_price"),
        round(avg("m.resale_price"), 2).alias("avg_resale_price"),
        round(avg("depreciation_pct"), 2).alias("avg_depreciation_pct")
    )
    
    return aggregated

def main():
    print("="*60)
    print("PRODUCT DATA AGGREGATION")
    print("="*60)
    
    spark = create_spark_session()
    
    # Define file paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    silver_dir = os.path.join(base_dir, "data", "silver")
    gold_dir = os.path.join(base_dir, "data", "gold")
    
    # Create gold directory if it does not exist
    os.makedirs(gold_dir, exist_ok=True)
    
    matched_file = os.path.join(silver_dir, "scraper_matched.csv")
    sku_file = os.path.join(silver_dir, "SKU_Master.csv")
    
    # Load datasets
    print("Loading datasets...")
    matched_df = load_csv(spark, matched_file, get_matched_scraper_data_schema())
    sku_df = load_csv(spark, sku_file, get_sku_master_schema())
    
    # Aggregate data
    print("Aggregating product listings and calculating depreciation...")
    agg_df = aggregate_product_data(matched_df, sku_df)
    
    # Sort sequentially for a neat output layout
    sorted_agg_df = agg_df.orderBy("brand", "category", "matched_model_name", "condition")
    
    # Save output to gold directory
    out_file = os.path.join(gold_dir, "aggregated_product_data.csv")
    print(f"Saving aggregated dataset to {out_file}...")
    sorted_agg_df.toPandas().to_csv(out_file, index=False)
    
    print(f"Aggregation complete. Saved {sorted_agg_df.count()} records.")
    print("="*60 + "\n")
    
    spark.stop()

if __name__ == "__main__":
    main()
