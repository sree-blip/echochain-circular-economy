import os
import sys
import unittest
from pyspark.sql import Row
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    # Satisfies VS Code's static analysis / linter
    from pyspark.utils import (
        get_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema
    )
    from pyspark.data_cleaning import (
        clean_scraper_data,
        clean_warranty_details,
        clean_bom_details,
        clean_sku_master,
        clean_circularity_score
    )
except (ImportError, ModuleNotFoundError):
    # Runtime fallback path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import (
        get_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema
    )
    from data_cleaning import (
        clean_scraper_data,
        clean_warranty_details,
        clean_bom_details,
        clean_sku_master,
        clean_circularity_score
    )

class TestDataCleaning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_clean_scraper_data(self):
        # Create mock data with a null product_id (should be dropped) and a null brand (should be replaced)
        schema = get_scraper_data_schema()
        data = [
            Row(product_id=1.0, marketplace_name="Amazon", product_name="Laptop", brand=None, category="Electronics", condition="New", resale_price=999.9, seller_name="SellerA", seller_rating=4.5, location="US", listing_date="2024-01-01", product_url="http://test", availability_status="In Stock", scraped_date="2024-01-02"),
            Row(product_id=None, marketplace_name="eBay", product_name="Phone", brand="Apple", category="Electronics", condition="Used", resale_price=499.9, seller_name="SellerB", seller_rating=4.8, location="UK", listing_date="2024-01-01", product_url="http://test", availability_status="In Stock", scraped_date="2024-01-02")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_clean = clean_scraper_data(df)
        
        # Verify null product_id is dropped
        self.assertEqual(df_clean.count(), 1)
        
        # Verify null brand is replaced with "Unknown"
        result = df_clean.collect()[0]
        self.assertEqual(result["brand"], "Unknown")
        self.assertEqual(result["product_id"], 1.0)

    def test_clean_warranty_details(self):
        schema = get_warranty_data_schema()
        data = [
            # Valid row
            Row(warranty_id="W1", sku_id="SKU1", product_id=1.0, warranty_period_months=12, warranty_start_date="2024-01-01", warranty_end_date="2025-01-01", warranty_type="Standard", coverage_details="1 Year", service_center_available="Yes", claim_status="Claimed", last_service_date="2024-06-01"),
            # Row with null key (should be dropped)
            Row(warranty_id="W2", sku_id=None, product_id=2.0, warranty_period_months=12, warranty_start_date="2024-01-01", warranty_end_date="2025-01-01", warranty_type="Standard", coverage_details="1 Year", service_center_available="Yes", claim_status="Claimed", last_service_date="2024-06-01"),
            # Row with null optional field (should be filled)
            Row(warranty_id="W3", sku_id="SKU3", product_id=3.0, warranty_period_months=12, warranty_start_date="2024-01-01", warranty_end_date="2025-01-01", warranty_type=None, coverage_details="1 Year", service_center_available="Yes", claim_status="Claimed", last_service_date="2024-06-01")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_clean = clean_warranty_details(df)
        
        # Verify null key row is dropped
        self.assertEqual(df_clean.count(), 2)
        
        # Verify null optional field is filled with "Unknown"
        rows = df_clean.filter(col("warranty_id") == "W3").collect()
        self.assertEqual(rows[0]["warranty_type"], "Unknown")

    def test_clean_bom_details(self):
        schema = get_bom_data_schema()
        data = [
            # Valid row
            Row(bom_id="B1", sku_id="SKU1", product_id=1.0, component_name="Screen", component_weight=0.5, recyclable="Yes", recycled_content_percentage=100.0, supplier_name="SupplierA", cost_per_component=95.0, hazardous_material_flag="No"),
            # Row with null key (should be dropped)
            Row(bom_id=None, sku_id="SKU2", product_id=2.0, component_name="Battery", component_weight=0.3, recyclable="No", recycled_content_percentage=80.0, supplier_name="SupplierB", cost_per_component=40.0, hazardous_material_flag="No"),
            # Row with null numeric and string fields (should be filled)
            Row(bom_id="B3", sku_id="SKU3", product_id=3.0, component_name=None, component_weight=None, recyclable="Yes", recycled_content_percentage=None, supplier_name="SupplierC", cost_per_component=25.0, hazardous_material_flag=None)
        ]
        df = self.spark.createDataFrame(data, schema)
        df_clean = clean_bom_details(df)
        
        self.assertEqual(df_clean.count(), 2)
        
        row_b3 = df_clean.filter(col("bom_id") == "B3").collect()[0]
        self.assertEqual(row_b3["component_name"], "Unknown")
        self.assertEqual(row_b3["component_weight"], 0.0)
        self.assertEqual(row_b3["recycled_content_percentage"], 0.0)
        self.assertEqual(row_b3["hazardous_material_flag"], "Unknown")

    def test_clean_sku_master(self):
        schema = get_sku_master_schema()
        data = [
            Row(sku_id="SKU1", product_id=1.0, product_name="Laptop", brand="BrandA", category="CategoryA", model_number="M1", original_price=999.0, manufacturing_date="2024-01-01", launch_year=2024, product_type="TypeA", material_type="Metal", weight=2.5, dimensions="10x5", country_of_origin="US", expected_life_span=5, repairability_score=8.5),
            # Null sku_id (dropped)
            Row(sku_id=None, product_id=2.0, product_name="Laptop", brand="BrandA", category="CategoryA", model_number="M2", original_price=999.0, manufacturing_date="2024-01-01", launch_year=2024, product_type="TypeA", material_type="Metal", weight=2.5, dimensions="10x5", country_of_origin="US", expected_life_span=5, repairability_score=8.5),
            # Null dimension and price (filled)
            Row(sku_id="SKU3", product_id=3.0, product_name="Laptop", brand="BrandA", category="CategoryA", model_number="M3", original_price=None, manufacturing_date="2024-01-01", launch_year=2024, product_type="TypeA", material_type="Metal", weight=2.5, dimensions=None, country_of_origin="US", expected_life_span=5, repairability_score=8.5)
        ]
        df = self.spark.createDataFrame(data, schema)
        df_clean = clean_sku_master(df)
        
        self.assertEqual(df_clean.count(), 2)
        row_sku3 = df_clean.filter(col("sku_id") == "SKU3").collect()[0]
        self.assertEqual(row_sku3["dimensions"], "Unknown")
        self.assertEqual(row_sku3["original_price"], 0.0)

    def test_clean_circularity_score(self):
        schema = get_circularity_score_schema()
        data = [
            Row(product_id=1.0, sku_id="SKU1", recyclability_score=8.0, reusability_score=7.0, material_sustainability_score=9.0, warranty_score=8.0, overall_circularity_score=80.0, circularity_category="Good", recommendation="Recycle"),
            # Null keys (dropped)
            Row(product_id=None, sku_id="SKU2", recyclability_score=8.0, reusability_score=7.0, material_sustainability_score=9.0, warranty_score=8.0, overall_circularity_score=80.0, circularity_category="Good", recommendation="Recycle"),
            # Null scores and category (filled)
            Row(product_id=3.0, sku_id="SKU3", recyclability_score=None, reusability_score=7.0, material_sustainability_score=9.0, warranty_score=8.0, overall_circularity_score=None, circularity_category=None, recommendation="Recycle")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_clean = clean_circularity_score(df)
        
        self.assertEqual(df_clean.count(), 2)
        row_sku3 = df_clean.filter(col("sku_id") == "SKU3").collect()[0]
        self.assertEqual(row_sku3["recyclability_score"], 0.0)
        self.assertEqual(row_sku3["overall_circularity_score"], 0.0)
        self.assertEqual(row_sku3["circularity_category"], "Unknown")

if __name__ == "__main__":
    unittest.main()
