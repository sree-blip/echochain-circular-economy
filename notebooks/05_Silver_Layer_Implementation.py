# Databricks notebook source
# MAGIC %md
# MAGIC # EchoChain
# MAGIC
# MAGIC ## Day 6 - Silver Layer Implementation
# MAGIC
# MAGIC ### Objective
# MAGIC Load validated Silver datasets into Databricks and create Silver Delta tables.
# MAGIC
# MAGIC ### Input
# MAGIC Silver CSV datasets provided by PySpark Engineer.
# MAGIC
# MAGIC ### Output
# MAGIC Silver Delta Tables
# MAGIC
# MAGIC ### Status
# MAGIC In Progress

# COMMAND ----------

silver_scraper_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/dbacademy/default/tutorials/silver_scraper_data.csv")
)

# COMMAND ----------

silver_sku_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/dbacademy/default/tutorials/silver_SKU_Master.csv")
)

# COMMAND ----------

silver_bom_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/dbacademy/default/tutorials/silver_BOM_details.csv")
)

# COMMAND ----------

silver_warranty_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/dbacademy/default/tutorials/silver_warrant_details.csv")
)

# COMMAND ----------

silver_circularity_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/dbacademy/default/tutorials/silver_circularity_score.csv")
)

# COMMAND ----------

display(silver_scraper_df)

# COMMAND ----------

display(silver_sku_df)

# COMMAND ----------

display(silver_bom_df)

# COMMAND ----------

display(silver_warranty_df)

# COMMAND ----------

display(silver_circularity_df)

# COMMAND ----------

silver_scraper_df.write.mode("overwrite").saveAsTable("silver_scraper_data")

# COMMAND ----------

silver_sku_df.write.mode("overwrite").saveAsTable("silver_sku_master")

# COMMAND ----------

silver_bom_df.write.mode("overwrite").saveAsTable("silver_bom_details")

# COMMAND ----------

silver_warranty_df.write.mode("overwrite").saveAsTable("silver_warranty_details")

# COMMAND ----------

silver_circularity_df.write.mode("overwrite").saveAsTable("silver_circularity_score")

# COMMAND ----------

tables = [
    "silver_scraper_data",
    "silver_sku_master",
    "silver_bom_details",
    "silver_warranty_details",
    "silver_circularity_score"
]

for table in tables:
    print("=" * 60)
    print(table)
    spark.sql(f"SELECT COUNT(*) FROM {table}").show()

# COMMAND ----------

for table in tables:
    print("=" * 60)
    spark.sql(f"DESCRIBE TABLE {table}").show(truncate=False)

# COMMAND ----------

tables = [
    "silver_scraper_data",
    "silver_sku_master",
    "silver_bom_details",
    "silver_warranty_details",
    "silver_circularity_score"
]

for table in tables:
    print("=" * 60)
    print(f"Table: {table}")
    spark.sql(f"SELECT COUNT(*) AS total_records FROM {table}").show()

# COMMAND ----------

for table in tables:
    print("=" * 60)
    print(f"Schema of {table}")
    spark.sql(f"DESCRIBE TABLE {table}").show(truncate=False)

# COMMAND ----------

tables = [
    "silver_scraper_data",
    "silver_sku_master",
    "silver_bom_details",
    "silver_warranty_details",
    "silver_circularity_score"
]

for table in tables:
    print("="*60)
    print(table)
    spark.sql(f"SELECT COUNT(*) FROM {table}").show()

# COMMAND ----------

(spark.table("silver_scraper_data")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_scraper_data"))

# COMMAND ----------

(spark.table("silver_sku_master")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_scraper_data"))

# COMMAND ----------

(spark.table("silver_bom_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_scraper_data"))

# COMMAND ----------

(spark.table("silver_warranty_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_scraper_data"))

# COMMAND ----------

(spark.table("silver_circularity_score")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_scraper_data"))

# COMMAND ----------

(spark.table("silver_sku_master")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header","true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_sku_master"))

# COMMAND ----------

(spark.table("silver_sku_master")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_sku_master"))

# COMMAND ----------

(spark.table("silver_bom_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_bom_details"))

# COMMAND ----------

(spark.table("silver_warranty_details")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_warranty_details"))

# COMMAND ----------

(spark.table("silver_circularity_score")
 .coalesce(1)
 .write
 .mode("overwrite")
 .option("header", "true")
 .csv("/Volumes/dbacademy/default/tutorials/silver_exports/silver_circularity_score"))

# COMMAND ----------

