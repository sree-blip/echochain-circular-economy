# Databricks notebook source
# MAGIC %md
# MAGIC # Day 13 - Updated Silver Layer Preparation
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Prepare the environment for the Updated Silver Layer implementation.
# MAGIC
# MAGIC This notebook establishes the Silver Layer architecture, validates the project setup, and prepares the workflow for processing updated datasets received from the PySpark Engineer.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Medallion Architecture
# MAGIC
# MAGIC Bronze → Silver → Gold
# MAGIC
# MAGIC Bronze Layer : Raw validated datasets
# MAGIC
# MAGIC Silver Layer : Cleaned and transformed datasets
# MAGIC
# MAGIC Gold Layer : Business-ready analytical datasets

# COMMAND ----------

# MAGIC %md
# MAGIC ## Input Bronze Tables
# MAGIC
# MAGIC - bronze_updated_bom_details
# MAGIC - bronze_updated_sku_master
# MAGIC - bronze_updated_scraper_data
# MAGIC - bronze_updated_warranty_details
# MAGIC - bronze_updated_circularity_score
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Output Silver Tables
# MAGIC
# MAGIC - silver_updated_bom_details
# MAGIC - silver_updated_sku_master
# MAGIC - silver_updated_scraper_data
# MAGIC - silver_updated_warranty_details
# MAGIC - silver_updated_circularity_score

# COMMAND ----------

# Bronze Schema

bronze_schema = "dbacademy.bronze"

# Silver Schema

silver_schema = "dbacademy.silver"

# Gold Schema

gold_schema = "dbacademy.gold"

print("Bronze Schema :", bronze_schema)
print("Silver Schema :", silver_schema)
print("Gold Schema :", gold_schema)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bronze Layer Verification
# MAGIC
# MAGIC The Updated Bronze Layer has been successfully completed.
# MAGIC
# MAGIC The following validations were performed:
# MAGIC
# MAGIC - Dataset Upload Validation
# MAGIC - Schema Validation
# MAGIC - Row Count Validation
# MAGIC - Data Quality Verification
# MAGIC - Delta Table Creation
# MAGIC
# MAGIC The Bronze Layer is now ready for the Updated Silver Layer implementation.

# COMMAND ----------

tables = [
    "dbacademy.bronze.bronze_updated_bom_details",
    "dbacademy.bronze.bronze_updated_sku_master",
    "dbacademy.bronze.bronze_updated_scraper_data",
    "dbacademy.bronze.bronze_updated_warranty_details",
    "dbacademy.bronze.bronze_updated_circularity_score"
]

for table in tables:

    df = spark.table(table)

    print("="*80)
    print(table)
    print("="*80)

    print("Rows :", df.count())
    print("Columns :", len(df.columns))

    display(df.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Silver Layer Preparation
# MAGIC
# MAGIC The Updated Silver datasets will be received from the PySpark Engineer.
# MAGIC
# MAGIC Once received, the following activities will be performed:
# MAGIC
# MAGIC - Schema Validation
# MAGIC - Row Count Validation
# MAGIC - Duplicate Validation
# MAGIC - Null Value Validation
# MAGIC - Data Type Validation
# MAGIC - Silver Delta Table Creation

# COMMAND ----------

