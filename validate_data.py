import pandas as pd

# Read cleaned data
df = pd.read_csv("clean_scraper_data.csv")

print("Total Records:", len(df))

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna(subset=["product_name"])
df = df.dropna(subset=["brand"])
df = df.dropna(subset=["resale_price"])

# Remove invalid prices
df = df[df["resale_price"] > 0]

# Save validated data
df.to_csv("validated_scraper_data.csv", index=False)

print("\nValidation completed successfully!")
print("Final Records:", len(df))