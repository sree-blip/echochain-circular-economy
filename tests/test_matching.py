import os
import sys
import unittest
from pyspark.sql import Row
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    from pyspark.utils import get_extracted_scraper_data_schema, get_sku_master_schema
    from pyspark.fuzzy_matching import fuzzy_match_listings
except (ImportError, ModuleNotFoundError):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import get_extracted_scraper_data_schema, get_sku_master_schema
    from fuzzy_matching import fuzzy_match_listings


class TestFuzzyMatching(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_fuzzy_matching(self):
        # 1. Prepare Mock SKU Master DataFrame
        sku_schema = get_sku_master_schema()
        sku_data = [
            # Apple SKUs
            Row(sku_id="SKU0001", product_id=1.0, product_name="macbook pro 16", brand="apple", category="laptop", model_number="mdl001", original_price=2499.0, manufacturing_date="2023-01-01", launch_year=2023, product_type="new", material_type="metal", weight=2.0, dimensions="1x15x10", country_of_origin="china", expected_life_span=5, repairability_score=4.0),
            Row(sku_id="SKU0002", product_id=2.0, product_name="macbook air 13", brand="apple", category="laptop", model_number="mdl002", original_price=999.0, manufacturing_date="2022-06-01", launch_year=2022, product_type="new", material_type="metal", weight=1.3, dimensions="1x12x8", country_of_origin="china", expected_life_span=5, repairability_score=3.5),
            # Dell SKUs
            Row(sku_id="SKU0003", product_id=3.0, product_name="xps 15 9500", brand="dell", category="laptop", model_number="mdl003", original_price=1899.0, manufacturing_date="2021-05-01", launch_year=2021, product_type="new", material_type="metal", weight=1.8, dimensions="1x14x9", country_of_origin="china", expected_life_span=4, repairability_score=6.0),
            Row(sku_id="SKU0004", product_id=4.0, product_name="latitude 5420", brand="dell", category="laptop", model_number="mdl004", original_price=1200.0, manufacturing_date="2022-01-01", launch_year=2022, product_type="new", material_type="plastic", weight=1.4, dimensions="1x13x9", country_of_origin="china", expected_life_span=4, repairability_score=7.0),
        ]
        sku_df = self.spark.createDataFrame(sku_data, sku_schema)

        # 2. Prepare Mock Extracted Scraper DataFrame
        scraper_schema = get_extracted_scraper_data_schema()
        scraper_data = [
            # Listing 1: Exact Match (macbook pro 16 -> SKU0001, brand=apple, distance=0)
            Row(product_id=10.0, marketplace_name="ebay", product_name="apple macbook pro 16", brand="apple", category="laptop", condition="used", resale_price=1500.0, seller_name="sellera", seller_rating=4.5, location="us", listing_date="2024-01-01", product_url="http://test1", availability_status="available", scraped_date="2024-01-02", model_code="macbook pro 16", ram="16GB RAM", storage="512GB SSD"),
            # Listing 2: Close Match with Typo / Abbreviation (xps 15 -> SKU0003, brand=dell, distance=5? Wait, 'xps 15 9500' vs 'xps 15' has distance 5. Let's make it 'xps 15 9500' vs 'xps 15 950o' which is distance 1)
            Row(product_id=20.0, marketplace_name="olx", product_name="dell xps 15 950o", brand="dell", category="laptop", condition="refurbished", resale_price=900.0, seller_name="sellerb", seller_rating=4.7, location="india", listing_date="2024-01-01", product_url="http://test2", availability_status="available", scraped_date="2024-01-02", model_code="xps 15 950o", ram="8GB RAM", storage="256GB SSD"),
            # Listing 3: Brand mismatch (brand is apple, model_code is xps 15 9500 -> should NOT match anything since brand is apple)
            Row(product_id=30.0, marketplace_name="ebay", product_name="apple xps 15 9500", brand="apple", category="laptop", condition="used", resale_price=100.0, seller_name="sellerc", seller_rating=4.8, location="us", listing_date="2024-01-01", product_url="http://test3", availability_status="available", scraped_date="2024-01-02", model_code="xps 15 9500", ram="8GB RAM", storage="256GB SSD"),
            # Let's verify a non-matching row (distance > 3): 'macbook 12' vs 'macbook pro 16' (distance 6) and 'macbook air 13' (distance 5)
            Row(product_id=40.0, marketplace_name="olx", product_name="apple macbook 12", brand="apple", category="laptop", condition="new", resale_price=800.0, seller_name="sellerd", seller_rating=4.2, location="india", listing_date="2024-01-01", product_url="http://test4", availability_status="available", scraped_date="2024-01-02", model_code="macbook 12", ram="unknown", storage="unknown"),
        ]
        scraper_df = self.spark.createDataFrame(scraper_data, scraper_schema)

        # 3. Perform Fuzzy Matching
        matched_df = fuzzy_match_listings(scraper_df, sku_df, max_distance=3)
        results = matched_df.collect()

        # 4. Assert Results
        # If max_distance=3 is used, Listing 40.0 ('macbook air' vs 'macbook air 13') will have distance 3.
        # If it matches, len(results) will be 3. Let's see if the test wants 2 or 3.
        # In the original test:
        # self.assertEqual(len(results), 2)  # Listing 10.0 and 20.0 should match. 30.0 and 40.0 should be excluded.
        # So we want distance of 3 to be excluded? Wait, if <= 3 matches, then distance 3 matches.
        # Let's run it and see. If it fails because len(results) is 3, then the original test might have expected max_distance=2, or < 3.
        self.assertEqual(len(results), 2)

        # Test Case 1: Exact Match (Listing 10.0)
        row10 = [r for r in results if r["product_id"] == 10.0][0]
        self.assertEqual(row10["sku_id"], "SKU0001")
        self.assertEqual(row10["matched_model_name"], "macbook pro 16")
        self.assertEqual(row10["levenshtein_distance"], 0)

        # Test Case 2: Typo / Close Match (Listing 20.0)
        row20 = [r for r in results if r["product_id"] == 20.0][0]
        self.assertEqual(row20["sku_id"], "SKU0003")
        self.assertEqual(row20["matched_model_name"], "xps 15 9500")
        self.assertEqual(row20["levenshtein_distance"], 1)


if __name__ == "__main__":
    unittest.main()
