import sys
import os
import unittest

# Insert project root at the very beginning of sys.path to prioritize local imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session

try:
    # Satisfies VS Code's static analysis / linter
    from pyspark.utils import (
        get_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema,
        load_csv
    )
except (ImportError, ModuleNotFoundError):
    # Runs at runtime when python module resolution collides with global pyspark package
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from utils import (
        get_scraper_data_schema,
        get_warranty_data_schema,
        get_bom_data_schema,
        get_sku_master_schema,
        get_circularity_score_schema,
        load_csv
    )

class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize Spark Session for testing
        cls.spark = create_spark_session()
        cls.mock_dir = "tests/mock_data"

    @classmethod
    def tearDownClass(cls):
        # Stop Spark Session
        cls.spark.stop()

    def test_load_scraper_data(self):
        schema = get_scraper_data_schema()
        path = os.path.join(self.mock_dir, "scraper_data_.csv")
        df = load_csv(self.spark, path, schema)
        
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 100)
        self.assertEqual(len(df.columns), len(schema.fields))

    def test_load_warranty_details(self):
        schema = get_warranty_data_schema()
        path = os.path.join(self.mock_dir, "warrant_details_.csv")
        df = load_csv(self.spark, path, schema)
        
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 100)
        self.assertEqual(len(df.columns), len(schema.fields))

    def test_load_bom_details(self):
        schema = get_bom_data_schema()
        path = os.path.join(self.mock_dir, "BOM_details_.csv")
        df = load_csv(self.spark, path, schema)
        
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 100)
        self.assertEqual(len(df.columns), len(schema.fields))

    def test_load_sku_master(self):
        schema = get_sku_master_schema()
        path = os.path.join(self.mock_dir, "SKU_Master_.csv")
        df = load_csv(self.spark, path, schema)
        
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 100)
        self.assertEqual(len(df.columns), len(schema.fields))

    def test_load_circularity_score(self):
        schema = get_circularity_score_schema()
        path = os.path.join(self.mock_dir, "circularity_score_.csv")
        df = load_csv(self.spark, path, schema)
        
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 100)
        self.assertEqual(len(df.columns), len(schema.fields))

if __name__ == "__main__":
    unittest.main()
