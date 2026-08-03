import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://127.0.0.1:5000"

with open("day11_products.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total records to verify: {len(rows)}")

mismatch_count = 0

for row in rows:
    url = BASE_URL + row["product_url"]
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")

        page_text = soup.get_text()

        # Check if product name exists on the live page
        if row["product_name"] not in page_text:
            print(f"MISMATCH: '{row['product_name']}' not found on {url}")
            mismatch_count += 1

        # Check if price exists on the live page
        price_clean = row["resale_price"].replace("₹", "").strip()
        if price_clean not in page_text:
            print(f"PRICE MISMATCH: {row['product_name']} -> CSV has {row['resale_price']}, not found on page")
            mismatch_count += 1

    except Exception as e:
        print(f"ERROR fetching {url}: {e}")
        mismatch_count += 1

print(f"\nVerification complete. Mismatches found: {mismatch_count}")