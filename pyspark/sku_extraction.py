import os
import sys
from pyspark.sql.functions import col, regexp_extract, when, lit, concat, upper, trim

# Add project root and pyspark directories to paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.spark_config import create_spark_session
from utils import get_scraper_data_schema, load_csv

def extract_specs(df):
    """
    Extracts brand, model_code, ram, and storage specifications from the product_name column.
    
    Parameters:
    df (DataFrame): Spark DataFrame containing cleaned scraper data.
    
    Returns:
    DataFrame: Updated Spark DataFrame with model_code, ram, storage columns and updated brand.
    """
    # 1. Brand Extraction
    # Search for common brand names in the lowercase product_name.
    # If a brand is found, use it; otherwise fallback to the existing brand column.
    brand_pattern = r"\b(lenovo|apple|dell|samsung|hp|asus|acer|toshiba|microsoft)\b"
    extracted_brand = regexp_extract(col("product_name"), brand_pattern, 1)
    df = df.withColumn(
        "brand",
        when(extracted_brand != "", trim(extracted_brand)).otherwise(col("brand"))
    )
    
    # 2. Model Code Extraction
    # Matches patterns like 'model 1', 'product 1', 'mdl001', 'mod-001', 't490', 'xps15', etc.
    model_pattern = r"\b(model\s+\d+|product\s+\d+|mdl\d+|mod-\d+|t-?\d+|xps\s*\d+|m1)\b"
    extracted_model = regexp_extract(col("product_name"), model_pattern, 1)
    df = df.withColumn(
        "model_code",
        when(extracted_model != "", trim(extracted_model)).otherwise(lit("unknown"))
    )
    
    # 3. RAM Extraction
    # Matches '16gb ram', '16 gb ram', '8gb', etc. (differentiating from storage by typical sizes if no suffix)
    ram_pattern = r"\b(\d+\s*(?:gb|mb)\s*ram|\b(?:4|8|12|16|24|32|64)\s*(?:gb|mb)\b)"
    raw_ram = regexp_extract(col("product_name"), ram_pattern, 1)
    
    ram_num = regexp_extract(raw_ram, r"(\d+)", 1)
    ram_unit = regexp_extract(raw_ram, r"(gb|mb)", 1)
    
    df = df.withColumn(
        "ram",
        when(raw_ram != "", concat(upper(ram_num), upper(ram_unit), lit(" RAM"))).otherwise(lit("unknown"))
    )
    
    # 4. Storage Extraction
    # Matches '512gb ssd', '1tb hdd', '256gb', etc.
    storage_pattern = r"\b(\d+\s*(?:gb|tb|mb)\s*(?:ssd|hdd|storage)|\b(?:128|256|512|1024)\s*gb\b|\b(?:1|2)\s*tb\b)"
    raw_storage = regexp_extract(col("product_name"), storage_pattern, 1)
    
    storage_num = regexp_extract(raw_storage, r"(\d+)", 1)
    storage_unit = regexp_extract(raw_storage, r"(gb|tb|mb)", 1)
    storage_type = regexp_extract(raw_storage, r"(ssd|hdd)", 1)
    
    storage_type_norm = when(storage_type != "", upper(storage_type)).otherwise(lit("SSD"))
    
    df = df.withColumn(
        "storage",
        when(raw_storage != "", concat(upper(storage_num), upper(storage_unit), lit(" "), storage_type_norm)).otherwise(lit("unknown"))
    )
    
    return df

def main():
    print("============================================================")
    print("Starting SKU and Specs Extraction Stage...")
    
    # Initialize Spark Session
    spark = create_spark_session()
    print("Spark Session initialized successfully.")
    
    input_path = "data/silver/scraper_data.csv"
    output_path = "data/silver/scraper_data.csv"
    
    if not os.path.exists(input_path):
        print(f"Error: Silver scraper data not found at {input_path}")
        spark.stop()
        sys.exit(1)
        
    print(f"Loading silver scraper data from {input_path}...")
    df = load_csv(spark, input_path, get_scraper_data_schema())
    initial_count = df.count()
    print(f"Loaded {initial_count} rows.")
    
    print("Extracting specifications (brand, model, RAM, storage)...")
    extracted_df = extract_specs(df)
    
    # Let's count some stats
    print("\nExtraction Summary:")
    extracted_df.cache()
    
    brand_stats = extracted_df.filter(col("brand") != "unknown").count()
    model_stats = extracted_df.filter(col("model_code") != "unknown").count()
    ram_stats = extracted_df.filter(col("ram") != "unknown").count()
    storage_stats = extracted_df.filter(col("storage") != "unknown").count()
    
    print(f"  Total records: {initial_count}")
    print(f"  Resolved brand: {brand_stats} ({brand_stats / initial_count * 100:.2f}%)")
    print(f"  Resolved model code: {model_stats} ({model_stats / initial_count * 100:.2f}%)")
    print(f"  Resolved RAM: {ram_stats} ({ram_stats / initial_count * 100:.2f}%)")
    print(f"  Resolved storage: {storage_stats} ({storage_stats / initial_count * 100:.2f}%)")
    
    # Save the output
    print(f"\nSaving extracted data to {output_path}...")
    # Convert to Pandas to handle Windows write limitations
    extracted_df.toPandas().to_csv(output_path, index=False)
    print(f"Successfully saved to {output_path}")
    
    spark.stop()
    print("SKU and Specs Extraction completed successfully.")
    print("============================================================")

if __name__ == "__main__":
    main()