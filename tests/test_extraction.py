import os
import sys
import unittest
from pyspark.sql import Row
from pyspark.sql.functions import col

# Add project root and pyspark directories to paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    from pyspark.utils import get_scraper_data_schema
    from pyspark.sku_extraction import extract_specs
except (ImportError, ModuleNotFoundError):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import get_scraper_data_schema
    from sku_extraction import extract_specs

class TestSKUExtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_extract_specs(self):
        # Create a schema and dummy data for testing various titles
        schema = get_scraper_data_schema()
        data = [
            # 1. Standard messy Thinkpad listing
            Row(product_id=1.0, marketplace_name="ebay", product_name="gently used thinkpad t-490 laptop 16gb", brand="unknown", category="laptop", condition="used", resale_price=350.0, seller_name="sellera", seller_rating=4.5, location="us", listing_date="2024-01-01", product_url="http://test1", availability_status="available", scraped_date="2024-01-02"),
            # 2. Dell XPS with RAM and Storage SSD
            Row(product_id=2.0, marketplace_name="olx", product_name="dell xps15 8gb ram 256gb ssd", brand="dell", category="laptop", condition="refurbished", resale_price=600.0, seller_name="sellerb", seller_rating=4.7, location="india", listing_date="2024-01-01", product_url="http://test2", availability_status="available", scraped_date="2024-01-02"),
            # 3. Apple Macbook Air M1 with RAM and Storage (no ssd suffix, but large size)
            Row(product_id=3.0, marketplace_name="ebay", product_name="macbook air m1 16gb 512gb", brand="apple", category="laptop", condition="good", resale_price=750.0, seller_name="sellerc", seller_rating=4.8, location="us", listing_date="2024-01-01", product_url="http://test3", availability_status="available", scraped_date="2024-01-02"),
            # 4. Standard mock row format "samsung laptop model 3"
            Row(product_id=4.0, marketplace_name="olx", product_name="samsung laptop model 3", brand="samsung", category="laptop", condition="new", resale_price=500.0, seller_name="sellerd", seller_rating=4.2, location="india", listing_date="2024-01-01", product_url="http://test4", availability_status="available", scraped_date="2024-01-02"),
            # 5. Cleaned real row format "product 1" (which should extract product 1 as model and keep brand lenovo)
            Row(product_id=5.0, marketplace_name="olx", product_name="product 1", brand="lenovo", category="mobile", condition="refurbished", resale_price=300.0, seller_name="sellere", seller_rating=4.1, location="india", listing_date="2024-01-01", product_url="http://test5", availability_status="available", scraped_date="2024-01-02"),
            # 6. Row with no matchable specifications
            Row(product_id=6.0, marketplace_name="olx", product_name="unknown cheap device", brand="unknown", category="electronics", condition="used", resale_price=20.0, seller_name="sellerf", seller_rating=3.5, location="india", listing_date="2024-01-01", product_url="http://test6", availability_status="available", scraped_date="2024-01-02")
        ]
        df = self.spark.createDataFrame(data, schema)
        df_extracted = extract_specs(df)
        
        # Collect results
        results = df_extracted.collect()
        
        # Test Case 1: "gently used thinkpad t-490 laptop 16gb"
        # brand fallback is kept if no brand found
        row1 = [r for r in results if r["product_id"] == 1.0][0]
        self.assertEqual(row1["brand"], "unknown")
        self.assertEqual(row1["model_code"], "t-490")
        self.assertEqual(row1["ram"], "16GB RAM")
        self.assertEqual(row1["storage"], "unknown")
        
        # Test Case 2: "dell xps15 8gb ram 256gb ssd"
        # brand: 'dell', model: 'xps15', RAM: '8GB RAM', storage: '256GB SSD'
        row2 = [r for r in results if r["product_id"] == 2.0][0]
        self.assertEqual(row2["brand"], "dell")
        self.assertEqual(row2["model_code"], "xps15")
        self.assertEqual(row2["ram"], "8GB RAM")
        self.assertEqual(row2["storage"], "256GB SSD")
        
        # Test Case 3: "macbook air m1 16gb 512gb"
        # brand: 'apple', model: 'm1', RAM: '16GB RAM', storage: '512GB SSD' (default SSD for 512gb)
        row3 = [r for r in results if r["product_id"] == 3.0][0]
        self.assertEqual(row3["brand"], "apple")
        self.assertEqual(row3["model_code"], "m1")
        self.assertEqual(row3["ram"], "16GB RAM")
        self.assertEqual(row3["storage"], "512GB SSD")
        
        # Test Case 4: "samsung laptop model 3"
        # brand: 'samsung', model: 'model 3', RAM: 'unknown', storage: 'unknown'
        row4 = [r for r in results if r["product_id"] == 4.0][0]
        self.assertEqual(row4["brand"], "samsung")
        self.assertEqual(row4["model_code"], "model 3")
        self.assertEqual(row4["ram"], "unknown")
        self.assertEqual(row4["storage"], "unknown")
        
        # Test Case 5: "product 1"
        # brand: 'lenovo', model: 'product 1', RAM: 'unknown', storage: 'unknown'
        row5 = [r for r in results if r["product_id"] == 5.0][0]
        self.assertEqual(row5["brand"], "lenovo")
        self.assertEqual(row5["model_code"], "product 1")
        self.assertEqual(row5["ram"], "unknown")
        self.assertEqual(row5["storage"], "unknown")
        
        # Test Case 6: "unknown cheap device"
        # All columns should fallback to defaults
        row6 = [r for r in results if r["product_id"] == 6.0][0]
        self.assertEqual(row6["brand"], "unknown")
        self.assertEqual(row6["model_code"], "unknown")
        self.assertEqual(row6["ram"], "unknown")
        self.assertEqual(row6["storage"], "unknown")

if __name__ == "__main__":
    unittest.main()
