import os
import csv

def generate_mock_data():
    # Ensure input directory exists
    os.makedirs("data/input", exist_ok=True)

    # 1. Generate scraper_data.csv
    scraper_file = "data/input/mock_scraper_data.csv"
    scraper_headers = [
        "product_id", "marketplace_name", "product_name", "brand", "category",
        "condition", "resale_price", "seller_name", "seller_rating", "location",
        "listing_date", "product_url", "availability_status", "scraped_date"
    ]
    scraper_rows = [
        ["1.0", "eBay", "Lenovo ThinkPad T490 16GB RAM 512GB SSD", "Lenovo", "Laptop", "Used", "320.0", "Refurb_King", "4.8", "New York", "2024-03-07", "https://ebay.com/1", "Available", "2025-01-29"],
        ["2.0", "eBay", "Apple MacBook Pro M1 8GB 256GB", "Apple", "Laptop", "Refurbished", "750.0", "Mac_Power", "4.9", "Los Angeles", "2024-06-19", "https://ebay.com/2", "Available", "2025-01-29"],
        ["3.0", "eBay", "Dell XPS 13 9310 Core i7", "Dell", "Laptop", "Good", "600.0", "PC_Deals", "4.2", "Chicago", "2024-08-03", "https://ebay.com/3", "Available", "2025-01-29"],
        ["4.0", "eBay", "Gently Used Lenovo T490 Laptop", "Lenovo", "Laptop", "Used", "290.0", "Tech_Recycle", "4.5", "Houston", "2024-11-21", "https://ebay.com/4", "Available", "2025-01-29"],
        ["5.0", "eBay", "Dell XPS13 9310 laptop", "Dell", "Laptop", "Used", "550.0", "ByteSize", "4.0", "San Jose", "2024-12-01", "https://ebay.com/5", "Available", "2025-01-29"],
        ["6.0", "eBay", "Broken Lenovo T490 parts", "Lenovo", "Laptop", "For Parts", "100.0", "Tech_Scrap", "3.8", "Austin", "2024-12-15", "https://ebay.com/6", "Available", "2025-01-29"],
    ]

    with open(scraper_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(scraper_headers)
        writer.writerows(scraper_rows)
    print(f"Generated {scraper_file}")

    # 2. Generate warrant_details.csv
    warranty_file = "data/input/mock_warrant_details.csv"
    warranty_headers = [
        "warranty_id", "sku_id", "product_id", "warranty_period_months", "warranty_start_date",
        "warranty_end_date", "warranty_type", "coverage_details", "service_center_available",
        "claim_status", "last_service_date"
    ]
    warranty_rows = [
        ["WAR0001", "SKU_T490", "1.0", "24", "2022-11-27", "2024-11-27", "Manufacturer", "Parts and Service", "Yes", "Expired", "2024-02-13"],
        ["WAR0002", "SKU_MBP_M1", "2.0", "12", "2024-01-15", "2025-01-15", "Manufacturer", "Parts and Service", "Yes", "Active", "2024-08-17"],
        ["WAR0003", "SKU_XPS13", "3.0", "36", "2022-10-04", "2025-10-04", "Manufacturer", "Parts and Service", "Yes", "Active", "2024-08-26"],
        ["WAR0004", "SKU_T490", "4.0", "24", "2023-05-22", "2025-05-22", "Manufacturer", "Parts and Service", "No", "Active", "2024-06-28"],
        ["WAR0005", "SKU_XPS13", "5.0", "36", "2023-01-10", "2026-01-10", "Manufacturer", "Parts and Service", "Yes", "Active", "2024-09-02"],
        ["WAR0006", "SKU_T490", "6.0", "24", "2022-09-12", "2024-09-12", "Manufacturer", "Parts and Service", "No", "Expired", "2024-03-01"],
    ]

    with open(warranty_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(warranty_headers)
        writer.writerows(warranty_rows)
    print(f"Generated {warranty_file}")

    # 3. Generate internal_bom.csv
    bom_file = "data/input/mock_internal_bom.csv"
    bom_headers = ["model_id", "model_name", "brand", "component", "original_retail_price"]
    bom_rows = [
        ["SKU_T490", "ThinkPad T490", "Lenovo", "Motherboard", "450.0"],
        ["SKU_T490", "ThinkPad T490", "Lenovo", "Display Panel", "200.0"],
        ["SKU_T490", "ThinkPad T490", "Lenovo", "Battery", "80.0"],
        ["SKU_MBP_M1", "MacBook Pro M1", "Apple", "Logic Board", "600.0"],
        ["SKU_MBP_M1", "MacBook Pro M1", "Apple", "Retina Display", "350.0"],
        ["SKU_MBP_M1", "MacBook Pro M1", "Apple", "Battery", "120.0"],
        ["SKU_XPS13", "XPS 13 9310", "Dell", "Motherboard", "500.0"],
        ["SKU_XPS13", "XPS 13 9310", "Dell", "Display Panel", "250.0"],
        ["SKU_XPS13", "XPS 13 9310", "Dell", "Battery", "90.0"],
    ]

    with open(bom_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(bom_headers)
        writer.writerows(bom_rows)
    print(f"Generated {bom_file}")

if __name__ == "__main__":
    generate_mock_data()
