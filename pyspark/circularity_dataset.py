import os
import sys

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import (
    get_matched_scraper_data_schema,
    get_warranty_data_schema,
    get_bom_data_schema,
    get_circularity_score_schema,
    load_csv
)

def create_circularity_dataset(matched_df, bom_df, warranty_df, circularity_df):
    """
    Consolidates the matched scraper data, BOM details, warranty details, and circularity scores.
    """
    # 1. Clean clashing columns from internal tables (drop product_id to avoid name collision)
    bom_clean = bom_df.drop("product_id")
    warranty_clean = warranty_df.drop("product_id")
    circularity_clean = circularity_df.drop("product_id")
    
    # 2. Perform LEFT JOINs from scraper matches to the internal dimensions on sku_id
    joined = matched_df.join(bom_clean, on="sku_id", how="left")
    joined = joined.join(warranty_clean, on="sku_id", how="left")
    joined = joined.join(circularity_clean, on="sku_id", how="left")
    
    return joined

def main():
    spark = create_spark_session()
    
    try:
        silver_dir = "data/silver"
        processed_dir = "data/processed"
        os.makedirs(processed_dir, exist_ok=True)
        
        print("\n" + "="*60)
        print("STARTING CIRCULARITY DATASET GENERATION STAGE")
        print("="*60)
        
        # Load datasets
        print("Loading Silver datasets...")
        matched_df = load_csv(spark, os.path.join(silver_dir, "scraper_matched.csv"), get_matched_scraper_data_schema())
        bom_df = load_csv(spark, os.path.join(silver_dir, "BOM_details.csv"), get_bom_data_schema())
        warranty_df = load_csv(spark, os.path.join(silver_dir, "warrant_details.csv"), get_warranty_data_schema())
        circularity_df = load_csv(spark, os.path.join(silver_dir, "circularity_score.csv"), get_circularity_score_schema())
        
        # Run joins
        print("Merging datasets on sku_id...")
        circularity_dataset = create_circularity_dataset(matched_df, bom_df, warranty_df, circularity_df)
        
        # Save output in Parquet format by converting to Pandas to bypass the winutils.exe write limitation on Windows
        out_dir = os.path.join(processed_dir, "circularity_dataset")
        os.makedirs(out_dir, exist_ok=True)
        
        out_file = os.path.join(out_dir, "part-0.parquet")
        print(f"Saving merged Circularity Dataset to {out_file} as Parquet...")
        
        # Convert Spark DataFrame to Pandas and export as Parquet
        pandas_df = circularity_dataset.toPandas()
        
        # Drop columns 'ram' and 'storage' as they are currently unpopulated in scraper data
        cols_to_drop = [col for col in ["ram", "storage"] if col in pandas_df.columns]
        if cols_to_drop:
            print(f"Dropping unpopulated columns for final output: {cols_to_drop}")
            pandas_df = pandas_df.drop(columns=cols_to_drop)
            
        pandas_df.to_parquet(out_file, index=False)
        
        # Also save the full 50,000 rows as CSV for the BI / upload compatibility
        out_file_csv = os.path.join(processed_dir, "circularity_dataset.csv")
        print(f"Saving merged Circularity Dataset to {out_file_csv} as CSV...")
        pandas_df.to_csv(out_file_csv, index=False)
        
        print("Circularity Dataset successfully saved in both Parquet and CSV formats.")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"Error during Circularity Dataset generation: {e}")
        sys.exit(1)
    finally:
        spark.stop()

if __name__ == "__main__":
    main()