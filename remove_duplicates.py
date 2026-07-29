import pandas as pd

# Read CSV
df = pd.read_csv("scraper_data_final.csv")

print("Before removing duplicates:", len(df))

# Remove duplicate products
df = df.drop_duplicates(
    subset=["product_name", "brand", "resale_price"],
    keep="first"
)

print("After removing duplicates:", len(df))

# Save cleaned data
df.to_csv("clean_scraper_data.csv", index=False)

print("Duplicate products removed successfully!")