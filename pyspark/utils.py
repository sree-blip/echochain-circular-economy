from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType
)

def get_scraper_data_schema() -> StructType:
    """
    Returns the schema for the scraped marketplace listings.
    """
    return StructType([
        StructField("product_id", DoubleType(), True),
        StructField("marketplace_name", StringType(), True),
        StructField("product_name", StringType(), True),
        StructField("brand", StringType(), True),
        StructField("category", StringType(), True),
        StructField("condition", StringType(), True),
        StructField("resale_price", DoubleType(), True),
        StructField("seller_name", StringType(), True),
        StructField("seller_rating", DoubleType(), True),
        StructField("location", StringType(), True),
        StructField("listing_date", StringType(), True),
        StructField("product_url", StringType(), True),
        StructField("availability_status", StringType(), True),
        StructField("scraped_date", StringType(), True)
    ])

def get_warranty_data_schema() -> StructType:
    """
    Returns the schema for the warranty and repair claims database.
    """
    return StructType([
        StructField("warranty_id", StringType(), True),
        StructField("sku_id", StringType(), True),
        StructField("product_id", DoubleType(), True),
        StructField("warranty_period_months", IntegerType(), True),
        StructField("warranty_start_date", StringType(), True),
        StructField("warranty_end_date", StringType(), True),
        StructField("warranty_type", StringType(), True),
        StructField("coverage_details", StringType(), True),
        StructField("service_center_available", StringType(), True),
        StructField("claim_status", StringType(), True),
        StructField("last_service_date", StringType(), True)
    ])

def get_bom_data_schema() -> StructType:
    """
    Returns the schema for the internal Bill of Materials (BOM) catalog.
    """
    return StructType([
        StructField("model_id", StringType(), True),
        StructField("model_name", StringType(), True),
        StructField("brand", StringType(), True),
        StructField("component", StringType(), True),
        StructField("original_retail_price", DoubleType(), True)
    ])

def load_csv(spark, path: str, schema: StructType):
    """
    General helper to load a CSV file into a PySpark DataFrame with a specified schema.
    """
    return (
        spark.read
        .format("csv")
        .option("header", "true")
        .schema(schema)
        .load(path)
    )