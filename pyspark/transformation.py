import os
import sys
from pyspark.sql.functions import col, to_date, when, trim, upper, lower
from pyspark.sql.types import DateType, DoubleType, IntegerType

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import (
    get_extracted_scraper_data_schema,
    get_warranty_data_schema,
    get_bom_data_schema,
    get_sku_master_schema,
    get_circularity_score_schema,
    load_csv
)

def transform_scraper_data(df):
    """
    Transforms Scraper Data:
    - Casts date columns (listing_date, scraped_date) to DateType.
    - Ensures product_id is DoubleType.
    """
    df_trans = df.withColumn("product_id", col("product_id").cast(DoubleType()))
    df_trans = df_trans.withColumn("listing_date", to_date(col("listing_date"), "yyyy-MM-dd"))
    df_trans = df_trans.withColumn("scraped_date", to_date(col("scraped_date"), "yyyy-MM-dd"))
    return df_trans

def transform_warranty_details(df):
    """
    Transforms Warranty Details:
    - Casts date columns to DateType.
    - Fixes logical date mismatches: if start date > end date, swap them.
    - Standardizes ID columns.
    """
    # 1. Cast dates to DateType
    df_trans = df.withColumn("warranty_start_date", to_date(col("warranty_start_date"), "yyyy-MM-dd"))
    df_trans = df_trans.withColumn("warranty_end_date", to_date(col("warranty_end_date"), "yyyy-MM-dd"))
    df_trans = df_trans.withColumn("last_service_date", to_date(col("last_service_date"), "yyyy-MM-dd"))
    
    # 2. Fix date logic: swap if start > end
    df_trans = df_trans.withColumn(
        "actual_start",
        when(col("warranty_start_date") > col("warranty_end_date"), col("warranty_end_date"))
        .otherwise(col("warranty_start_date"))
    ).withColumn(
        "actual_end",
        when(col("warranty_start_date") > col("warranty_end_date"), col("warranty_start_date"))
        .otherwise(col("warranty_end_date"))
    )
    
    # Drop intermediate columns and rename to original names
    df_trans = df_trans.drop("warranty_start_date", "warranty_end_date") \
                       .withColumnRenamed("actual_start", "warranty_start_date") \
                       .withColumnRenamed("actual_end", "warranty_end_date")
    
    # 3. Standardize and cast
    df_trans = df_trans.withColumn("product_id", col("product_id").cast(DoubleType()))
    df_trans = df_trans.withColumn("sku_id", upper(trim(col("sku_id"))))
    df_trans = df_trans.withColumn("warranty_id", upper(trim(col("warranty_id"))))
    df_trans = df_trans.withColumn("warranty_period_months", col("warranty_period_months").cast(IntegerType()))
    
    original_cols = ["warranty_id", "sku_id", "product_id", "warranty_period_months", 
                     "warranty_start_date", "warranty_end_date", "warranty_type", 
                     "coverage_details", "service_center_available", "claim_status", 
                     "last_service_date"]
    return df_trans.select(*original_cols)

def transform_sku_master(df):
    """
    Transforms SKU Master:
    - Casts manufacturing_date to DateType.
    - Standardizes columns.
    """
    df_trans = df.withColumn("product_id", col("product_id").cast(DoubleType()))
    df_trans = df_trans.withColumn("sku_id", upper(trim(col("sku_id"))))
    df_trans = df_trans.withColumn("manufacturing_date", to_date(col("manufacturing_date"), "yyyy-MM-dd"))
    df_trans = df_trans.withColumn("original_price", col("original_price").cast(DoubleType()))
    df_trans = df_trans.withColumn("launch_year", col("launch_year").cast(IntegerType()))
    df_trans = df_trans.withColumn("expected_life_span", col("expected_life_span").cast(IntegerType()))
    df_trans = df_trans.withColumn("repairability_score", col("repairability_score").cast(DoubleType()))
    return df_trans

def transform_bom_details(df):
    """
    Transforms BOM Details:
    - Standardizes ID columns.
    - Casts numeric fields.
    """
    df_trans = df.withColumn("product_id", col("product_id").cast(DoubleType()))
    df_trans = df_trans.withColumn("sku_id", upper(trim(col("sku_id"))))
    df_trans = df_trans.withColumn("bom_id", upper(trim(col("bom_id"))))
    df_trans = df_trans.withColumn("component_weight", col("component_weight").cast(DoubleType()))
    df_trans = df_trans.withColumn("recycled_content_percentage", col("recycled_content_percentage").cast(DoubleType()))
    df_trans = df_trans.withColumn("cost_per_component", col("cost_per_component").cast(DoubleType()))
    return df_trans

def transform_circularity_score(df):
    """
    Transforms Circularity Score:
    - Standardizes ID columns.
    - Casts score columns.
    """
    df_trans = df.withColumn("product_id", col("product_id").cast(DoubleType()))
    df_trans = df_trans.withColumn("sku_id", upper(trim(col("sku_id"))))
    df_trans = df_trans.withColumn("recyclability_score", col("recyclability_score").cast(DoubleType()))
    df_trans = df_trans.withColumn("reusability_score", col("reusability_score").cast(DoubleType()))
    df_trans = df_trans.withColumn("material_sustainability_score", col("material_sustainability_score").cast(DoubleType()))
    df_trans = df_trans.withColumn("warranty_score", col("warranty_score").cast(DoubleType()))
    df_trans = df_trans.withColumn("overall_circularity_score", col("overall_circularity_score").cast(DoubleType()))
    return df_trans

def main():
    print("============================================================")
    print("Starting Transformed Dataset Preparation Stage...")
    
    # Initialize Spark Session
    spark = create_spark_session()
    print("Spark Session initialized successfully.")
    
    silver_dir = "data/silver"
    
    # We load scraper_data.csv using the extracted schema because Day 8 has run and added model columns.
    datasets = [
        {
            "name": "Scraper Data",
            "path": os.path.join(silver_dir, "scraper_data.csv"),
            "schema": get_extracted_scraper_data_schema(),
            "transform_func": transform_scraper_data,
            "out_name": "scraper_data"
        },
        {
            "name": "Warranty Details",
            "path": os.path.join(silver_dir, "warrant_details.csv"),
            "schema": get_warranty_data_schema(),
            "transform_func": transform_warranty_details,
            "out_name": "warrant_details"
        },
        {
            "name": "BOM Details",
            "path": os.path.join(silver_dir, "BOM_details.csv"),
            "schema": get_bom_data_schema(),
            "transform_func": transform_bom_details,
            "out_name": "BOM_details"
        },
        {
            "name": "SKU Master",
            "path": os.path.join(silver_dir, "SKU_Master.csv"),
            "schema": get_sku_master_schema(),
            "transform_func": transform_sku_master,
            "out_name": "SKU_Master"
        },
        {
            "name": "Circularity Score",
            "path": os.path.join(silver_dir, "circularity_score.csv"),
            "schema": get_circularity_score_schema(),
            "transform_func": transform_circularity_score,
            "out_name": "circularity_score"
        }
    ]
    
    print("\nExecuting type casting and logical transformations...")
    for ds in datasets:
        print(f"\nProcessing {ds['name']}:")
        if not os.path.exists(ds["path"]):
            print(f"  Error: File not found at {ds['path']}")
            continue
            
        df = load_csv(spark, ds["path"], ds["schema"])
        trans_df = ds["transform_func"](df)
        
        # Save back to Silver layer, overwriting the clean CSV files with standard datatypes
        out_file = ds["path"]
        # Convert to Pandas to handle Windows write limitations
        trans_df.toPandas().to_csv(out_file, index=False)
        print(f"  Successfully transformed and updated: {out_file}")
        
    spark.stop()
    print("\nTransformed Dataset Preparation Stage completed successfully.")
    print("============================================================")

if __name__ == "__main__":
    main()