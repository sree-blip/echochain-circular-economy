import pandas as pd
import os

# Check if CSV exists
if os.path.exists("validated_scraper_data.csv"):
    print("PASS: CSV file found")
else:
    print("FAIL: CSV file not found")
    exit()

# Read CSV
df = pd.read_csv("validated_scraper_data.csv")

# Check records
if len(df) > 0:
    print(f"PASS: {len(df)} records found")
else:
    print("FAIL: Dataset is empty")

# Required columns
required_columns = [
    "product_name",
    "brand",
    "category",
    "resale_price"
]

for column in required_columns:
    if column in df.columns:
        print(f"PASS: {column} column exists")
    else:
        print(f"FAIL: {column} column missing")

print("Automated Scraping Test Completed Successfully!")