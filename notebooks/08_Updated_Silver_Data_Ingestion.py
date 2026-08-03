# Databricks notebook source
# MAGIC %md
# MAGIC # Day 14 - Updated Silver Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Create the Updated Silver Layer by loading the transformed datasets received from the PySpark Engineer.
# MAGIC
# MAGIC The datasets will be validated and stored as Delta tables inside the Silver schema.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Input Files
# MAGIC
# MAGIC - BOM_details (1).csv
# MAGIC - SKU_Master (1).csv
# MAGIC - scraper_matched.csv
# MAGIC - warrant_details (1).csv
# MAGIC - circularity_score (1).csv
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Output Tables
# MAGIC
# MAGIC - silver_updated_bom_details
# MAGIC - silver_updated_sku_master
# MAGIC - silver_updated_scraper_data
# MAGIC - silver_updated_warranty_details
# MAGIC - silver_updated_circularity_score

# COMMAND ----------

datasets = {
    "BOM_details (1).csv": "dbacademy.silver.silver_updated_bom_details",
    "SKU_Master (1).csv": "dbacademy.silver.silver_updated_sku_master",
    "scraper_matched.csv": "dbacademy.silver.silver_updated_scraper_data",
    "warrant_details (1).csv": "dbacademy.silver.silver_updated_warranty_details",
    "circularity_score (1).csv": "dbacademy.silver.silver_updated_circularity_score"
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

    print("\nSchema")
    df.printSchema()

    print("\nSample Data")
    display(df.limit(5))

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(table_name)
    )

    print(f"\n✅ {table_name} created successfully.\n")

# COMMAND ----------

volume_path = "/Volumes/dbacademy/default/tutorials"

# COMMAND ----------

print(volume_path)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/Volumes/dbacademy/default/tutorials"))

# COMMAND ----------

datasets = {
    "BOM_details (1).csv": "dbacademy.silver.silver_updated_bom_details",
    "SKU_Master (1).csv": "dbacademy.silver.silver_updated_sku_master",
    "scraper_matched.csv": "dbacademy.silver.silver_updated_scraper_data",
    "warrant_details (1).csv": "dbacademy.silver.silver_updated_warranty_details",
    "circularity_score (1).csv": "dbacademy.silver.silver_updated_circularity_score"
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

    print(f"✅ {table_name} created successfully\n")

# COMMAND ----------

tables = [
    "dbacademy.silver.silver_updated_bom_details",
    "dbacademy.silver.silver_updated_sku_master",
    "dbacademy.silver.silver_updated_scraper_data",
    "dbacademy.silver.silver_updated_warranty_details",
    "dbacademy.silver.silver_updated_circularity_score"
]

for table in tables:
    print("=" * 70)
    print(table)
    print("Rows :", spark.table(table).count())

# COMMAND ----------

