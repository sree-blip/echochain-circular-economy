import os
import sys
import unittest
from pyspark.sql import Row
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    from pyspark.utils import get_matched_scraper_data_schema, get_sku_master_schema
    from pyspark.aggregate_listings import aggregate_product_data
except (ImportError, ModuleNotFoundError):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import get_matched_scraper_data_schema, get_sku_master_schema
    from aggregate_listings import aggregate_product_data


class TestProductAggregation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_aggregation_metrics(self):
        # 1. Prepare Mock SKU Master
        sku_schema = get_sku_master_schema()
        sku_data = [
            Row(sku_id="SKU001", product_id=1.0, product_name="macbook pro 16", brand="apple", category="laptop", model_number="mdl001", original_price=1000.0, manufacturing_date="2023-01-01", launch_year=2023, product_type="new", material_type="metal", weight=2.0, dimensions="1x15x10", country_of_origin="china", expected_life_span=5, repairability_score=4.0),
            Row(sku_id="SKU002", product_id=2.0, product_name="latitude 5420", brand="dell", category="laptop", model_number="mdl002", original_price=500.0, manufacturing_date="2022-01-01", launch_year=2022, product_type="new", material_type="plastic", weight=1.4, dimensions="1x13x9", country_of_origin="china", expected_life_span=4, repairability_score=7.0),
        ]
        sku_df = self.spark.createDataFrame(sku_data, sku_schema)

        # 2. Prepare Mock Matched Listings
        matched_schema = get_matched_scraper_data_schema()
        matched_data = [
            # Group A: Apple laptops, condition="good"
            Row(product_id=101.0, marketplace_name="olx", product_name="macbook pro 16", brand="apple", category="laptop", condition="good", resale_price=800.0, seller_name="s1", seller_rating=4.5, location="vizag", listing_date="2024-01-01", product_url="url", availability_status="available", scraped_date="2024-01-02", model_code="macbook pro 16", ram="16gb", storage="512gb", sku_id="SKU001", matched_model_name="macbook pro 16", levenshtein_distance=0),
            Row(product_id=102.0, marketplace_name="olx", product_name="macbook pro 16", brand="apple", category="laptop", condition="good", resale_price=600.0, seller_name="s2", seller_rating=4.0, location="vizag", listing_date="2024-01-02", product_url="url", availability_status="available", scraped_date="2024-01-03", model_code="macbook pro 16", ram="16gb", storage="512gb", sku_id="SKU001", matched_model_name="macbook pro 16", levenshtein_distance=0),
            
            # Group B: Dell laptops, condition="new"
            Row(product_id=103.0, marketplace_name="olx", product_name="latitude 5420", brand="dell", category="laptop", condition="new", resale_price=400.0, seller_name="s3", seller_rating=4.2, location="vizag", listing_date="2024-01-03", product_url="url", availability_status="available", scraped_date="2024-01-04", model_code="latitude 5420", ram="8gb", storage="256gb", sku_id="SKU002", matched_model_name="latitude 5420", levenshtein_distance=0),
        ]
        matched_df = self.spark.createDataFrame(matched_data, matched_schema)

        # 3. Execute Aggregation
        result_df = aggregate_product_data(matched_df, sku_df)
        results = result_df.collect()

        # 4. Verify results
        # We expect 2 groups:
        # Group 1: apple, laptop, macbook pro 16, good
        #   - listing_count = 2
        #   - avg_original_price = 1000.0
        #   - avg_resale_price = 700.0 (average of 800 and 600)
        #   - avg_depreciation_pct = 30.0% (depreciation of 101.0 is 20%, of 102.0 is 40%)
        # Group 2: dell, laptop, latitude 5420, new
        #   - listing_count = 1
        #   - avg_original_price = 500.0
        #   - avg_resale_price = 400.0
        #   - avg_depreciation_pct = 20.0% (depreciation of 103.0 is 20%)

        self.assertEqual(len(results), 2)
        
        apple_group = [r for r in results if r["brand"] == "apple"][0]
        self.assertEqual(apple_group["listing_count"], 2)
        self.assertEqual(apple_group["avg_original_price"], 1000.0)
        self.assertEqual(apple_group["avg_resale_price"], 700.0)
        self.assertEqual(apple_group["avg_depreciation_pct"], 30.0)

        dell_group = [r for r in results if r["brand"] == "dell"][0]
        self.assertEqual(dell_group["listing_count"], 1)
        self.assertEqual(dell_group["avg_original_price"], 500.0)
        self.assertEqual(dell_group["avg_resale_price"], 400.0)
        self.assertEqual(dell_group["avg_depreciation_pct"], 20.0)


if __name__ == "__main__":
    unittest.main()
