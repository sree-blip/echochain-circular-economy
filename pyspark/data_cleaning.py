import os
import sys
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import (
    get_scraper_data_schema,
    get_warranty_data_schema,
    get_bom_data_schema,
    get_sku_master_schema,
    get_circularity_score_schema,
    load_csv
)

def clean_scraper_data(df):
    """
    Cleans Scraper Data:
    - Drops rows where product_id is null
    - Fills optional string column nulls with 'Unknown'
    - Fills price/rating nulls with 0.0
    """
    # Drop rows with null primary keys
    df_clean = df.dropna(subset=["product_id"])
    
    # Fill defaults for string columns
    string_cols = ["marketplace_name", "product_name", "brand", "category", 
                   "condition", "seller_name", "location", "product_url", 
                   "availability_status", "listing_date", "scraped_date"]
    for c in string_cols:
        df_clean = df_clean.fillna({c: "Unknown"})
        
    # Fill defaults for numeric columns
    df_clean = df_clean.fillna({"resale_price": 0.0, "seller_rating": 0.0})
    
    return df_clean

def clean_warranty_details(df):
    """
    Cleans Warranty Details:
    - Drops rows where key identifiers (warranty_id, sku_id, product_id) are null
    - Fills optional string column nulls with 'Unknown'
    """
    df_clean = df.dropna(subset=["warranty_id", "sku_id", "product_id"])
    
    string_cols = ["warranty_type", "coverage_details", "service_center_available", 
                   "claim_status", "warranty_start_date", "warranty_end_date", "last_service_date"]
    for c in string_cols:
        df_clean = df_clean.fillna({c: "Unknown"})
        
    return df_clean

def clean_bom_details(df):
    """
    Cleans BOM Details:
    - Drops rows where identifiers (bom_id, sku_id, product_id) are null
    - Fills optional string column nulls with 'Unknown'
    - Fills numeric column nulls with 0.0
    """
    df_clean = df.dropna(subset=["bom_id", "sku_id", "product_id"])
    
    string_cols = ["component_name", "recyclable", "supplier_name", "hazardous_material_flag"]
    for c in string_cols:
        df_clean = df_clean.fillna({c: "Unknown"})
        
    df_clean = df_clean.fillna({
        "component_weight": 0.0,
        "recycled_content_percentage": 0.0,
        "cost_per_component": 0.0
    })
    
    return df_clean

def clean_sku_master(df):
    """
    Cleans SKU Master Data:
    - Drops rows where key identifiers (sku_id, product_id) are null
    - Fills optional string column nulls with 'Unknown'
    - Fills numeric column nulls with 0.0/0
    """
    df_clean = df.dropna(subset=["sku_id", "product_id"])
    
    string_cols = ["product_name", "brand", "category", "model_number", 
                   "product_type", "material_type", "dimensions", "country_of_origin",
                   "manufacturing_date"]
    for c in string_cols:
        df_clean = df_clean.fillna({c: "Unknown"})
        
    df_clean = df_clean.fillna({
        "original_price": 0.0,
        "launch_year": 0,
        "weight": 0.0,
        "expected_life_span": 0,
        "repairability_score": 0.0
    })
    
    return df_clean

def clean_circularity_score(df):
    """
    Cleans Circularity Score Data:
    - Drops rows where identifiers (product_id, sku_id) are null
    - Fills optional string columns with 'Unknown'
    - Fills scores with 0.0
    """
    df_clean = df.dropna(subset=["product_id", "sku_id"])
    
    string_cols = ["circularity_category", "recommendation"]
    for c in string_cols:
        df_clean = df_clean.fillna({c: "Unknown"})
        
    score_cols = ["recyclability_score", "reusability_score", 
                  "material_sustainability_score", "warranty_score", 
                  "overall_circularity_score"]
    for c in score_cols:
        df_clean = df_clean.fillna({c: 0.0})
        
    return df_clean

def main():
    print("============================================================")
    # Initialize Spark Session
    spark = create_spark_session()
    print("Spark Session initialized successfully.")
    
    # Ensure Silver Directory exists
    silver_dir = "data/silver"
    os.makedirs(silver_dir, exist_ok=True)
    
    datasets = [
        {
            "name": "Scraper Data",
            "path": "data/bronze/scraper_data_.csv",
            "schema": get_scraper_data_schema(),
            "clean_func": clean_scraper_data,
            "out_name": "scraper_data"
        },
        {
            "name": "Warranty Details",
            "path": "data/bronze/warrant_details_.csv",
            "schema": get_warranty_data_schema(),
            "clean_func": clean_warranty_details,
            "out_name": "warrant_details"
        },
        {
            "name": "BOM Details",
            "path": "data/bronze/BOM_details_.csv",
            "schema": get_bom_data_schema(),
            "clean_func": clean_bom_details,
            "out_name": "BOM_details"
        },
        {
            "name": "SKU Master",
            "path": "data/bronze/SKU_Master_.csv",
            "schema": get_sku_master_schema(),
            "clean_func": clean_sku_master,
            "out_name": "SKU_Master"
        },
        {
            "name": "Circularity Score",
            "path": "data/bronze/circularity_score_.csv",
            "schema": get_circularity_score_schema(),
            "clean_func": clean_circularity_score,
            "out_name": "circularity_score"
        }
    ]
    
    print("\nStarting Day 6 Data Cleaning (Removing Nulls)...")
    for ds in datasets:
        print(f"\nProcessing {ds['name']}:")
        
        # Load raw data
        raw_df = load_csv(spark, ds["path"], ds["schema"])
        initial_count = raw_df.count()
        print(f"  Raw count: {initial_count}")
        
        # Apply cleaning
        clean_df = ds["clean_func"](raw_df)
        final_count = clean_df.count()
        print(f"  Clean count: {final_count}")
        print(f"  Removed: {initial_count - final_count} null/empty rows")
        
        # Write to Silver layer by converting to Pandas to bypass Windows winutils write limitations
        out_file = os.path.join(silver_dir, f"{ds['out_name']}.csv")
        clean_df.toPandas().to_csv(out_file, index=False)
        print(f"  Saved cleaned data to: {out_file}")
        
    # Stop Spark Session
    spark.stop()
    print("\nDay 6 Data Cleaning completed successfully.")
    print("============================================================")

if __name__ == "__main__":
    main()