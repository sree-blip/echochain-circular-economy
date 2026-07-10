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
    load_csv
)

def explore_schemas():
    print("=" * 60)
    print("INITIALIZING SPARK SESSION FOR SCHEMA EXPLORATION")
    print("=" * 60)
    spark = create_spark_session()
    
    try:
        # Define file paths
        scraper_path = "data/input/mock_scraper_data.csv"
        warranty_path = "data/input/mock_warrant_details.csv"
        bom_path = "data/input/mock_internal_bom.csv"

        print("\n" + "=" * 60)
        print("1. LOADING & EXPLORING SCRAPER DATA")
        print("=" * 60)
        scraper_df = load_csv(spark, scraper_path, get_scraper_data_schema())
        print(f"Row count: {scraper_df.count()}")
        print("\nSchema:")
        scraper_df.printSchema()
        print("\nSample Data:")
        scraper_df.show(3, truncate=False)

        print("\n" + "=" * 60)
        print("2. LOADING & EXPLORING WARRANTY DATA")
        print("=" * 60)
        warranty_df = load_csv(spark, warranty_path, get_warranty_data_schema())
        print(f"Row count: {warranty_df.count()}")
        print("\nSchema:")
        warranty_df.printSchema()
        print("\nSample Data:")
        warranty_df.show(3, truncate=False)

        print("\n" + "=" * 60)
        print("3. LOADING & EXPLORING BOM DATA")
        print("=" * 60)
        bom_df = load_csv(spark, bom_path, get_bom_data_schema())
        print(f"Row count: {bom_df.count()}")
        print("\nSchema:")
        bom_df.printSchema()
        print("\nSample Data:")
        bom_df.show(3, truncate=False)

    except Exception as e:
        print(f"An error occurred during schema exploration: {e}")
    finally:
        print("\n" + "=" * 60)
        print("STOPPING SPARK SESSION")
        print("=" * 60)
        spark.stop()

if __name__ == "__main__":
    explore_schemas()
