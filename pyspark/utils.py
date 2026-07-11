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
        StructField("bom_id", StringType(), True),
        StructField("sku_id", StringType(), True),
        StructField("product_id", DoubleType(), True),
        StructField("component_name", StringType(), True),
        StructField("component_weight", DoubleType(), True),
        StructField("recyclable", StringType(), True),
        StructField("recycled_content_percentage", DoubleType(), True),
        StructField("supplier_name", StringType(), True),
        StructField("cost_per_component", DoubleType(), True),
        StructField("hazardous_material_flag", StringType(), True)
    ])

def get_sku_master_schema() -> StructType:
    """
    Returns the schema for the SKU master dataset.
    """
    return StructType([
        StructField("sku_id", StringType(), True),
        StructField("product_id", DoubleType(), True),
        StructField("product_name", StringType(), True),
        StructField("brand", StringType(), True),
        StructField("category", StringType(), True),
        StructField("model_number", StringType(), True),
        StructField("original_price", DoubleType(), True),
        StructField("manufacturing_date", StringType(), True),
        StructField("launch_year", IntegerType(), True),
        StructField("product_type", StringType(), True),
        StructField("material_type", StringType(), True),
        StructField("weight", DoubleType(), True),
        StructField("dimensions", StringType(), True),
        StructField("country_of_origin", StringType(), True),
        StructField("expected_life_span", IntegerType(), True),
        StructField("repairability_score", DoubleType(), True)
    ])

def get_circularity_score_schema() -> StructType:
    """
    Returns the schema for the baseline circularity scores.
    """
    return StructType([
        StructField("product_id", DoubleType(), True),
        StructField("sku_id", StringType(), True),
        StructField("recyclability_score", DoubleType(), True),
        StructField("reusability_score", DoubleType(), True),
        StructField("material_sustainability_score", DoubleType(), True),
        StructField("warranty_score", DoubleType(), True),
        StructField("overall_circularity_score", DoubleType(), True),
        StructField("circularity_category", StringType(), True),
        StructField("recommendation", StringType(), True)
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