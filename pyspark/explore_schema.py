import sys
import os

# Add the project root and the local pyspark directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from configs.spark_config import create_spark_session
from utils import (
    get_scraper_data_schema,
    get_warranty_data_schema,
    get_bom_data_schema,
    get_sku_master_schema,
    get_circularity_score_schema,
    load_csv
)

def explore_schemas():
    print("=" * 60)
    print("INITIALIZING SPARK SESSION FOR BRONZE DATA PROFILING")
    print("=" * 60)
    spark = create_spark_session()
    
    try:
        # Define files to explore with their paths and schemas
        datasets = [
            {
                "name": "SCRAPER DATA",
                "path": "data/bronze/scraper_data_.csv",
                "schema_func": get_scraper_data_schema
            },
            {
                "name": "WARRANTY DETAILS",
                "path": "data/bronze/warrant_details_.csv",
                "schema_func": get_warranty_data_schema
            },
            {
                "name": "BOM DETAILS",
                "path": "data/bronze/BOM_details_.csv",
                "schema_func": get_bom_data_schema
            },
            {
                "name": "SKU MASTER",
                "path": "data/bronze/SKU_Master_.csv",
                "schema_func": get_sku_master_schema
            },
            {
                "name": "CIRCULARITY SCORE",
                "path": "data/bronze/circularity_score_.csv",
                "schema_func": get_circularity_score_schema
            }
        ]

        for ds in datasets:
            print("\n" + "=" * 60)
            print(f"LOADING & EXPLORING {ds['name']}")
            print("=" * 60)
            
            # Load DataFrame
            df = load_csv(spark, ds["path"], ds["schema_func"]())
            
            # Profile row count
            row_count = df.count()
            print(f"File Path: {ds['path']}")
            print(f"Row count: {row_count}")
            
            # Print schema
            print("\nSchema:")
            df.printSchema()
            
            # Show preview
            print("\nSample Data (Top 3 rows):")
            df.show(3, truncate=True)

    except Exception as e:
        print(f"An error occurred during schema exploration: {e}")
    finally:
        print("\n" + "=" * 60)
        print("STOPPING SPARK SESSION")
        print("=" * 60)
        spark.stop()

if __name__ == "__main__":
    explore_schemas()
