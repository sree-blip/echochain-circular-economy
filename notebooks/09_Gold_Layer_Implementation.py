# Databricks notebook source
# MAGIC %md
# MAGIC # Day 15 - Gold Layer Implementation
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Create the Gold Layer using the aggregated business dataset received from the PySpark Engineer.
# MAGIC
# MAGIC The Gold Layer contains business-ready data for reporting and dashboard development.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Input File
# MAGIC
# MAGIC - aggregated_product_data.csv
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Output Table
# MAGIC
# MAGIC - gold_product_summary

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

volume_path = "dbfs:/Volumes/dbacademy/default/tutorials"

# COMMAND ----------

gold_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{volume_path}/aggregated_product_data.csv")
)

# COMMAND ----------

print("=" * 80)
print("Gold Layer Validation")
print("=" * 80)

print("Rows :", gold_df.count())
print("Columns :", len(gold_df.columns))

gold_df.printSchema()

display(gold_df.limit(10))

# COMMAND ----------

(
    gold_df.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("dbacademy.gold.gold_product_summary")
)

print("✅ Gold table created successfully.")

# COMMAND ----------

spark.table("dbacademy.gold.gold_product_summary").count()

# COMMAND ----------

display(
    spark.table("dbacademy.gold.gold_product_summary")
)

# COMMAND ----------

from pyspark.sql.functions import col, count, when

gold_df = spark.table("dbacademy.gold.gold_product_summary")

gold_df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in gold_df.columns
]).display()

# COMMAND ----------

print("Total Rows :", gold_df.count())
print("Distinct Rows :", gold_df.distinct().count())

# COMMAND ----------

display(gold_df.describe())

# COMMAND ----------

