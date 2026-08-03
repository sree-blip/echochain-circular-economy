# Databricks notebook source
# MAGIC %md
# MAGIC # EchoChain
# MAGIC
# MAGIC ## Day 3 - Bronze Layer Data Ingestion
# MAGIC
# MAGIC ### Objective
# MAGIC Import the marketplace dataset into Databricks and prepare the Bronze layer.
# MAGIC
# MAGIC ### Dataset
# MAGIC scraped_marketplace_data.csv
# MAGIC
# MAGIC ### Layer
# MAGIC Bronze
# MAGIC
# MAGIC ### Status
# MAGIC In Progress
# MAGIC
# MAGIC # Day 4 – Bronze Layer Validation & Data Profiling
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Validate the Bronze layer created using the testing dataset and assess its readiness for Silver layer transformation.
# MAGIC
# MAGIC > Note: This validation is performed on a testing dataset. The final scraped dataset will be ingested once received from the Web Scraping Engineer.

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/dbacademy/default/tutorials/scraped_marketplace_data.csv")

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

print("Total Rows:", df.count())
print("Total Columns:", len(df.columns))

# COMMAND ----------

df.show(5, truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col, count, when

display(
    df.select([
        count(when(col(c).isNull(), c)).alias(c)
        for c in df.columns
    ])
)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("bronze_marketplace_data")

# COMMAND ----------

spark.sql("SHOW TABLES").show()

# COMMAND ----------

bronze_df = spark.table("bronze_marketplace_data")

display(bronze_df)

# COMMAND ----------

spark.sql("DESCRIBE TABLE bronze_marketplace_data").show(truncate=False)

# COMMAND ----------

spark.sql("SELECT * FROM bronze_marketplace_data LIMIT 10").show(truncate=False)

# COMMAND ----------

bronze_df = spark.table("bronze_marketplace_data")

display(bronze_df)

# COMMAND ----------

print("Total Records:", bronze_df.count())

# COMMAND ----------

print("Total Columns:", len(bronze_df.columns))

# COMMAND ----------

bronze_df.printSchema()

# COMMAND ----------

duplicates = bronze_df.count() - bronze_df.dropDuplicates().count()
print("Duplicate Records:", duplicates)

# COMMAND ----------

from pyspark.sql.functions import col, count, when

display(
    bronze_df.select([
        count(when(col(c).isNull(), c)).alias(c)
        for c in bronze_df.columns
    ])
)

# COMMAND ----------

display(
    bronze_df.groupBy("Marketplace").count()
)

# COMMAND ----------

display(
    bronze_df.groupBy("Category").count()
)

# COMMAND ----------

display(
    bronze_df.groupBy("Brand").count()
)

# COMMAND ----------

display(
    bronze_df.describe("Original_MRP_INR", "Selling_Price_INR")
)

# COMMAND ----------

display(
    bronze_df.describe("Original_MRP_INR", "Selling_Price_INR")
)

# COMMAND ----------

# MAGIC %md
# MAGIC # Conclusion
# MAGIC
# MAGIC The Bronze layer has been successfully validated using the testing dataset.
# MAGIC
# MAGIC Completed validations:
# MAGIC - Dataset accessibility
# MAGIC - Schema verification
# MAGIC - Duplicate record check
# MAGIC - Missing value check
# MAGIC - Basic data profiling
# MAGIC
# MAGIC The notebook is ready to process the final scraped dataset once it is received.

# COMMAND ----------

