import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))

from configs.spark_config import create_spark_session
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, IntegerType
)
try:
    from pyspark.circularity_dataset import create_circularity_dataset
except (ImportError, ModuleNotFoundError):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../pyspark")))
    from circularity_dataset import create_circularity_dataset


class TestCircularityDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = create_spark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_joins_and_column_resolution(self):
        # 1. Create schemas
        matched_schema = StructType([
            StructField("product_id", DoubleType(), True),
            StructField("sku_id", StringType(), True),
            StructField("title", StringType(), True),
            StructField("matched_model_name", StringType(), True)
        ])
        
        bom_schema = StructType([
            StructField("bom_id", StringType(), True),
            StructField("sku_id", StringType(), True),
            StructField("product_id", DoubleType(), True),
            StructField("component_name", StringType(), True)
        ])
        
        warranty_schema = StructType([
            StructField("warranty_id", StringType(), True),
            StructField("sku_id", StringType(), True),
            StructField("product_id", DoubleType(), True),
            StructField("claim_status", StringType(), True)
        ])
        
        circularity_schema = StructType([
            StructField("sku_id", StringType(), True),
            StructField("product_id", DoubleType(), True),
            StructField("overall_circularity_score", DoubleType(), True)
        ])

        # 2. Create mock data
        matched_data = [(100.0, "SKU1", "Apple MacBook Air", "MacBook Air")]
        bom_data = [("BOM1", "SKU1", 200.0, "motherboard")]
        warrant_data = [("WARR1", "SKU1", 300.0, "claims_approved")]
        score_data = [("SKU1", 400.0, 85.5)]

        # 3. Create DataFrames
        matched_df = self.spark.createDataFrame(matched_data, matched_schema)
        bom_df = self.spark.createDataFrame(bom_data, bom_schema)
        warranty_df = self.spark.createDataFrame(warrant_data, warranty_schema)
        circularity_df = self.spark.createDataFrame(score_data, circularity_schema)

        # 4. Execute function
        result_df = create_circularity_dataset(matched_df, bom_df, warranty_df, circularity_df)
        
        # 5. Assertions
        cols = result_df.columns
        self.assertEqual(result_df.count(), 1)
        
        # Ensure name collisions on "product_id" were resolved (only one product_id column exists)
        self.assertEqual(cols.count("product_id"), 1)
        
        # Verify that columns from all tables exist in the final dataframe
        self.assertIn("sku_id", cols)
        self.assertIn("title", cols)
        self.assertIn("component_name", cols)
        self.assertIn("claim_status", cols)
        self.assertIn("overall_circularity_score", cols)

if __name__ == "__main__":
    unittest.main()
