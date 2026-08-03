# Databricks notebook source
# MAGIC %md
# MAGIC # Day 12 - Updated Bronze Layer Data Ingestion
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC The objective of this notebook is to ingest the updated project datasets into the Bronze Layer.
# MAGIC
# MAGIC The Bronze Layer stores raw data exactly as received from the source system without applying any business transformations.
# MAGIC
# MAGIC ## Input Datasets
# MAGIC
# MAGIC - BOM_details_updated.csv
# MAGIC - SKU_Master_final.csv
# MAGIC - clean_scraper_data.csv
# MAGIC - warrant_details_final.csv
# MAGIC - circularity_score_final.csv
# MAGIC
# MAGIC ## Output Bronze Tables
# MAGIC
# MAGIC - bronze_updated_bom_details
# MAGIC - bronze_updated_sku_master
# MAGIC - bronze_updated_scraper_data
# MAGIC - bronze_updated_warranty_details
# MAGIC - bronze_updated_circularity_score
# MAGIC
# MAGIC ## Validation
# MAGIC
# MAGIC - Schema Validation
# MAGIC - Row Count Validation
# MAGIC - Null Value Validation

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

volume_path = "/Volumes/dbacademy/default/tutorials"

# COMMAND ----------

df = spark.read.csv(
    f"{volume_path}/BOM_details_updated.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

datasets = {
    "BOM_details_updated.csv": "bronze_updated_bom_details",
    "SKU_Master_final.csv": "bronze_updated_sku_master",
    "clean_scraper_data.csv": "bronze_updated_scraper_data",
    "warranty_details_final.csv": "bronze_updated_warranty_details",
    "circularity_score_final.csv": "bronze_updated_circularity_score"
}

# COMMAND ----------

for file_name, table_name in datasets.items():

    print("=" * 80)
    print(f"Processing : {file_name}")
    print("=" * 80)

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(f"{volume_path}/{file_name}")
    )

    print(f"Rows : {df.count()}")
    print(f"Columns : {len(df.columns)}")

    df.printSchema()

    display(df.limit(5))

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(table_name)
    )

    print(f"{table_name} created successfully.\n")

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/dbacademy/default/tutorials"))

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/dbacademy/default/tutorials"))

# COMMAND ----------

datasets = {
    "BOM_details_updated.csv": "bronze_updated_bom_details",
    "SKU_Master_final.csv": "bronze_updated_sku_master",
    "clean_scraper_data.csv": "bronze_updated_scraper_data",
    "warrant_details_final.csv": "bronze_updated_warranty_details",
    "circularity_score_final.csv": "bronze_updated_circularity_score"
}

# COMMAND ----------

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/dbacademy/default/tutorials/BOM_details_updated.csv")
)

display(df)

# COMMAND ----------

datasets = {
    "BOM_details_updated.csv": "bronze_updated_bom_details",
    "SKU_Master_final.csv": "bronze_updated_sku_master",
    "clean_scraper_data.csv": "bronze_updated_scraper_data",
    "warrant_details_final.csv": "bronze_updated_warranty_details",
    "circularity_score_final.csv": "bronze_updated_circularity_score"
}

volume_path = "/Volumes/dbacademy/default/tutorials"

for file_name, table_name in datasets.items():

    print("=" * 80)
    print(f"Processing : {file_name}")
    print("=" * 80)

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(f"{volume_path}/{file_name}")
    )

    print(f"Rows : {df.count()}")
    print(f"Columns : {len(df.columns)}")

    df.printSchema()

    display(df.limit(5))

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(f"dbacademy.default.{table_name}")
    )

    print(f"✅ {table_name} created successfully.\n")

# COMMAND ----------

display(spark.table("dbacademy.default.bronze_updated_bom_details"))
display(spark.table("dbacademy.default.bronze_updated_sku_master"))
display(spark.table("dbacademy.default.bronze_updated_scraper_data"))
display(spark.table("dbacademy.default.bronze_updated_warranty_details"))
display(spark.table("dbacademy.default.bronze_updated_circularity_score"))

# COMMAND ----------

tables = [
    "bronze_updated_bom_details",
    "bronze_updated_sku_master",
    "bronze_updated_scraper_data",
    "bronze_updated_warranty_details",
    "bronze_updated_circularity_score"
]

for table in tables:
    count = spark.table(table).count()
    print(f"{table}: {count} rows")

# COMMAND ----------

tables = [
    "dbacademy.default.bronze_updated_bom_details",
    "dbacademy.default.bronze_updated_sku_master",
    "dbacademy.default.bronze_updated_scraper_data",
    "dbacademy.default.bronze_updated_warranty_details",
    "dbacademy.default.bronze_updated_circularity_score"
]

for table in tables:
    count = spark.table(table).count()
    print(f"{table}: {count} rows")

# COMMAND ----------

