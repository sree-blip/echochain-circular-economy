# Databricks notebook source
# MAGIC %md
# MAGIC # Day 5 - Bronze Layer Validation & Handoff

# COMMAND ----------

tables = [
    "bronze_scraper_data",
    "bronze_sku_master",
    "bronze_bom_details",
    "bronze_warranty_details",
    "bronze_circularity_score"
]

for table in tables:
    print("=" * 60)
    print(f"Table: {table}")
    spark.sql(f"SELECT COUNT(*) AS total_records FROM {table}").show()

# COMMAND ----------

for table in tables:
    print("=" * 60)
    print(f"Schema: {table}")
    spark.sql(f"DESCRIBE TABLE {table}").show(truncate=False)

# COMMAND ----------

for table in tables:
    print("=" * 60)
    print(f"Preview: {table}")
    display(spark.table(table).limit(5))

# COMMAND ----------

(spark.table("bronze_scraper_data")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/exports/bronze_scraper_data"))

# COMMAND ----------

(spark.table("bronze_sku_master")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/exports/bronze_sku_master"))

# COMMAND ----------

(spark.table("bronze_bom_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/exports/bronze_bom_details"))

# COMMAND ----------

(spark.table("bronze_warranty_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/exports/bronze_warranty_details"))

# COMMAND ----------

(spark.table("bronze_circularity_score")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/exports/bronze_circularity_score"))

# COMMAND ----------

