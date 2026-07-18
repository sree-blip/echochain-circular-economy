import os
import sys
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import DateType

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

def validate_datasets(spark):
    silver_dir = "data/silver"
    errors = []
    
    print("\n" + "="*60)
    print("1. LOADING SILVER DATASETS & VERIFYING ROW COUNTS")
    print("="*60)
    
    # Load all 5 datasets
    datasets = {
        "scraper_data": {
            "df": load_csv(spark, os.path.join(silver_dir, "scraper_data.csv"), get_extracted_scraper_data_schema()),
            "dates": ["listing_date", "scraped_date"]
        },
        "warrant_details": {
            "df": load_csv(spark, os.path.join(silver_dir, "warrant_details.csv"), get_warranty_data_schema()),
            "dates": ["warranty_start_date", "warranty_end_date", "last_service_date"]
        },
        "BOM_details": {
            "df": load_csv(spark, os.path.join(silver_dir, "BOM_details.csv"), get_bom_data_schema()),
            "dates": []
        },
        "SKU_Master": {
            "df": load_csv(spark, os.path.join(silver_dir, "SKU_Master.csv"), get_sku_master_schema()),
            "dates": ["manufacturing_date"]
        },
        "circularity_score": {
            "df": load_csv(spark, os.path.join(silver_dir, "circularity_score.csv"), get_circularity_score_schema()),
            "dates": []
        }
    }
    
    for name, info in datasets.items():
        count = info["df"].count()
        print(f"  {name:20} -> Loaded {count} rows.")
        if count == 0:
            errors.append(f"Dataset '{name}' is empty.")
            
    print("\n" + "="*60)
    print("2. VERIFYING DATATYPE FORMATS (DATE FIELDS)")
    print("="*60)
    
    for name, info in datasets.items():
        df = info["df"]
        
        for date_col in info["dates"]:
            if date_col in df.columns:
                # Count records where string is not null but cannot be parsed as yyyy-MM-dd
                invalid_parse_count = df.filter(
                    to_date(col(date_col), "yyyy-MM-dd").isNull() & col(date_col).isNotNull()
                ).count()
                
                is_valid = (invalid_parse_count == 0)
                print(f"  {name:20} : {date_col:25} -> Valid Date Format (yyyy-MM-dd) [PASSED]" if is_valid else f"  {name:20} : {date_col:25} -> {invalid_parse_count} invalid values [FAILED]")
                if not is_valid:
                    errors.append(f"Column '{date_col}' in '{name}' has {invalid_parse_count} unparseable values.")
            else:
                errors.append(f"Date column '{date_col}' missing from '{name}' columns.")

    print("\n" + "="*60)
    print("3. VERIFYING DATE LOGIC (WARRANTY TIMELINE BOUNDS)")
    print("="*60)
    
    w_df = datasets["warrant_details"]["df"]
    # Check for records where start_date > end_date
    invalid_dates_df = w_df.filter(col("warranty_start_date") > col("warranty_end_date"))
    invalid_count = invalid_dates_df.count()
    
    if invalid_count == 0:
        print("  All warranty records satisfy logical bounds (start_date <= end_date). [PASSED]")
    else:
        print(f"  Found {invalid_count} records with invalid date ordering (start_date > end_date). [FAILED]")
        errors.append(f"Warranty dataset has {invalid_count} records with invalid start/end dates.")

    print("\n" + "="*60)
    print("4. TESTING FOREIGN KEY & JOIN COMPATIBILITY ON SKU_ID")
    print("="*60)
    
    sku_master_df = datasets["SKU_Master"]["df"]
    
    # Check join with BOM
    bom_df = datasets["BOM_details"]["df"]
    bom_joined = bom_df.join(sku_master_df, "sku_id", "inner")
    bom_match_rate = (bom_joined.count() / bom_df.count()) * 100 if bom_df.count() > 0 else 0
    print(f"  BOM Details joined with SKU Master: {bom_match_rate:.2f}% match rate.")
    if bom_match_rate < 90:
        errors.append(f"Low match rate ({bom_match_rate:.2f}%) between BOM and SKU Master on sku_id.")
        
    # Check join with Warranty
    warr_joined = w_df.join(sku_master_df, "sku_id", "inner")
    warr_match_rate = (warr_joined.count() / w_df.count()) * 100 if w_df.count() > 0 else 0
    print(f"  Warranty Details joined with SKU Master: {warr_match_rate:.2f}% match rate.")
    if warr_match_rate < 90:
        errors.append(f"Low match rate ({warr_match_rate:.2f}%) between Warranty and SKU Master on sku_id.")
        
    # Check join with Circularity Score
    circ_df = datasets["circularity_score"]["df"]
    circ_joined = circ_df.join(sku_master_df, "sku_id", "inner")
    circ_match_rate = (circ_joined.count() / circ_df.count()) * 100 if circ_df.count() > 0 else 0
    print(f"  Circularity Score joined with SKU Master: {circ_match_rate:.2f}% match rate.")
    if circ_match_rate < 90:
        errors.append(f"Low match rate ({circ_match_rate:.2f}%) between Circularity Score and SKU Master on sku_id.")

    print("\n" + "="*60)
    print("5. VALIDATION SUMMARY")
    print("="*60)
    
    if len(errors) == 0:
        print("\n  [SUCCESS] All Silver layer datasets are validated and compatible!")
    else:
        print(f"\n  [FAILURE] Found {len(errors)} validation errors:")
        for err in errors:
            print(f"            - {err}")
            
    print("="*60 + "\n")

def main():
    spark = create_spark_session()
    try:
        validate_datasets(spark)
    except Exception as e:
        print(f"Execution Error during validation script run: {e}")
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
