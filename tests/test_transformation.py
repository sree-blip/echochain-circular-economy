import os
import sys
import unittest
from datetime import date
from pyspark.sql import Row
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    from pyspark.utils import (
        get_extracted_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema
    )
    from pyspark.transformation import (
        transform_scraper_data,
        transform_warranty_details,
        transform_sku_master,
        transform_bom_details,
        transform_circularity_score
    )
except (ImportError, ModuleNotFoundError):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import (
        get_extracted_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema
    )
    from transformation import (
        transform_scraper_data,
        transform_warranty_details,
        transform_sku_master,
        transform_bom_details,
        transform_circularity_score
    )

class TestDataTransformation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_transform_scraper_data(self):
        schema = get_extracted_scraper_data_schema()
        data = [
            Row(product_id=1.0, marketplace_name="ebay", product_name="test", brand="dell", category="laptop", condition="new", resale_price=1000.0, seller_name="seller", seller_rating=4.5, location="us", listing_date="2024-03-07", product_url="http://test", availability_status="available", scraped_date="2025-01-29", model_code="t490", ram="16GB RAM", storage="512GB SSD")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_trans = transform_scraper_data(df)
        
        row = df_trans.collect()[0]
        self.assertEqual(row["listing_date"], date(2024, 3, 7))
        self.assertEqual(row["scraped_date"], date(2025, 1, 29))
        self.assertEqual(row["product_id"], 1.0)

    def test_transform_warranty_details_date_swap(self):
        schema = get_warranty_data_schema()
        data = [
            # Row 1: Normal dates
            Row(warranty_id="war0001", sku_id="sku0001", product_id=1.0, warranty_period_months=24, warranty_start_date="2022-11-27", warranty_end_date="2025-02-08", warranty_type="seller", coverage_details="parts", service_center_available="no", claim_status="expired", last_service_date="2024-02-13"),
            # Row 2: Swapped dates (start date is after end date)
            Row(warranty_id="war0002", sku_id="sku0002", product_id=2.0, warranty_period_months=6, warranty_start_date="2024-11-15", warranty_end_date="2023-09-21", warranty_type="manufacturer", coverage_details="parts", service_center_available="no", claim_status="active", last_service_date="2025-02-17")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_trans = transform_warranty_details(df)
        
        rows = df_trans.collect()
        row1 = [r for r in rows if r["warranty_id"] == "WAR0001"][0]
        row2 = [r for r in rows if r["warranty_id"] == "WAR0002"][0]
        
        # Row 1 check
        self.assertEqual(row1["warranty_start_date"], date(2022, 11, 27))
        self.assertEqual(row1["warranty_end_date"], date(2025, 2, 8))
        self.assertEqual(row1["sku_id"], "SKU0001")
        
        # Row 2 check (must be swapped!)
        self.assertEqual(row2["warranty_start_date"], date(2023, 9, 21))
        self.assertEqual(row2["warranty_end_date"], date(2024, 11, 15))
        self.assertEqual(row2["sku_id"], "SKU0002")

    def test_transform_sku_master(self):
        schema = get_sku_master_schema()
        data = [
            Row(sku_id="sku0001", product_id=1.0, product_name="product 1", brand="lenovo", category="mobile", model_number="mdl001", original_price=29442.0, manufacturing_date="2022-03-01", launch_year=2025, product_type="new", material_type="plastic", weight=7.0, dimensions="10x20x5", country_of_origin="india", expected_life_span=9, repairability_score=2.0)
        ]
        df = self.spark.createDataFrame(data, schema)
        df_trans = transform_sku_master(df)
        
        row = df_trans.collect()[0]
        self.assertEqual(row["manufacturing_date"], date(2022, 3, 1))
        self.assertEqual(row["sku_id"], "SKU0001")

if __name__ == "__main__":
    unittest.main()
