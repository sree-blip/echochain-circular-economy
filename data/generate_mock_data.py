import os
import csv
import random

def generate_mock_data():
    # Ensure test mock data directory exists
    output_dir = "tests/mock_data"
    os.makedirs(output_dir, exist_ok=True)

    # Replicable random data generation
    brands = ["Lenovo", "Apple", "Dell", "Samsung", "HP"]
    categories = ["Laptop", "Mobile", "Accessories"]
    conditions = ["Used", "Refurbished", "New", "Good", "Like New"]
    locations = ["Hyderabad", "Vijayawada", "Bangalore", "New York", "Los Angeles"]
    components = ["Motherboard", "Battery", "Screen", "Keyboard"]
    suppliers = ["Tech Components", "ABC Ltd", "XYZ Pvt Ltd"]
    claim_statuses = ["Active", "Expired"]
    circularity_categories = ["Excellent", "Good", "Poor", "Fair"]
    recommendations = ["Recycle", "Reuse", "Refurbish"]

    # 1. Generate scraper_data_.csv (100 rows)
    scraper_file = os.path.join(output_dir, "scraper_data_.csv")
    scraper_headers = [
        "product_id", "marketplace_name", "product_name", "brand", "category",
        "condition", "resale_price", "seller_name", "seller_rating", "location",
        "listing_date", "product_url", "availability_status", "scraped_date"
    ]
    scraper_rows = []
    for i in range(1, 101):
        brand = brands[i % len(brands)]
        cat = categories[i % len(categories)]
        cond = conditions[i % len(conditions)]
        loc = locations[i % len(locations)]
        price = float(150.0 + (i * 12.5) % 1500)
        rating = round(3.0 + (i * 0.17) % 2.0, 1)
        scraper_rows.append([
            f"{float(i)}",
            "OLX" if i % 2 == 0 else "eBay",
            f"{brand} {cat} model {i}",
            brand,
            cat,
            cond,
            f"{price}",
            f"Seller_{i}",
            f"{rating}",
            loc,
            f"2024-03-{10 + (i % 20):02d}",
            f"https://example.com/product/{i}",
            "Sold" if i % 3 == 0 else "Available",
            "2025-01-29"
        ])
    with open(scraper_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(scraper_headers)
        writer.writerows(scraper_rows)

    # 2. Generate warrant_details_.csv (100 rows)
    warranty_file = os.path.join(output_dir, "warrant_details_.csv")
    warranty_headers = [
        "warranty_id", "sku_id", "product_id", "warranty_period_months", "warranty_start_date",
        "warranty_end_date", "warranty_type", "coverage_details", "service_center_available",
        "claim_status", "last_service_date"
    ]
    warranty_rows = []
    for i in range(1, 101):
        period = 12 if i % 3 == 0 else (24 if i % 3 == 1 else 36)
        warranty_rows.append([
            f"WAR{i:04d}",
            f"SKU{i:04d}",
            f"{float(i)}",
            f"{period}",
            f"2022-{1 + (i % 12):02d}-15",
            f"2024-{1 + (i % 12):02d}-15",
            "Manufacturer" if i % 2 == 0 else "Seller",
            "Parts and Service" if i % 2 == 0 else "Parts only",
            "Yes" if i % 4 != 0 else "No",
            claim_statuses[i % len(claim_statuses)],
            f"2024-{1 + (i % 11):02d}-20"
        ])
    with open(warranty_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(warranty_headers)
        writer.writerows(warranty_rows)

    # 3. Generate BOM_details_.csv (100 rows)
    bom_file = os.path.join(output_dir, "BOM_details_.csv")
    bom_headers = [
        "bom_id", "sku_id", "product_id", "component_name", "component_weight",
        "recyclable", "recycled_content_percentage", "supplier_name", "cost_per_component",
        "hazardous_material_flag"
    ]
    bom_rows = []
    for i in range(1, 101):
        weight = 100 + (i * 17) % 800
        recycled_pct = (i * 13) % 100
        cost = 50.0 + (i * 22.5) % 800
        bom_rows.append([
            f"BOM{i:04d}",
            f"SKU{i:04d}",
            f"{float(i)}",
            components[i % len(components)],
            f"{weight}",
            "Yes" if i % 5 != 0 else "No",
            f"{float(recycled_pct)}",
            suppliers[i % len(suppliers)],
            f"{round(cost, 2)}",
            "Yes" if i % 7 == 0 else "No"
        ])
    with open(bom_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(bom_headers)
        writer.writerows(bom_rows)

    # 4. Generate SKU_Master_.csv (100 rows)
    sku_file = os.path.join(output_dir, "SKU_Master_.csv")
    sku_headers = [
        "sku_id", "product_id", "product_name", "brand", "category", "model_number",
        "original_price", "manufacturing_date", "launch_year", "product_type",
        "material_type", "weight", "dimensions", "country_of_origin", "expected_life_span",
        "repairability_score"
    ]
    sku_rows = []
    countries = ["China", "India", "Taiwan", "USA", "Vietnam"]
    for i in range(1, 101):
        brand = brands[i % len(brands)]
        cat = categories[i % len(categories)]
        price = 500.0 + (i * 35.0) % 2000
        sku_rows.append([
            f"SKU{i:04d}",
            f"{float(i)}",
            f"{brand} {cat} model {i}",
            brand,
            cat,
            f"MOD-{i:04d}",
            f"{price}",
            f"2021-05-{1 + (i % 28):02d}",
            f"{2018 + (i % 7)}",
            "Electronics",
            "Aluminum" if i % 2 == 0 else "Plastic",
            f"{round(1.0 + (i * 0.05) % 2.5, 2)}",
            f"{30 + i%5}x{20 + i%5}x{1.5 + (i%5)*0.1}",
            countries[i % len(countries)],
            f"{3 + (i % 6)}",
            f"{round(4.0 + (i * 0.13) % 5.0, 1)}"
        ])
    with open(sku_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(sku_headers)
        writer.writerows(sku_rows)

    # 5. Generate circularity_score_.csv (100 rows)
    circ_file = os.path.join(output_dir, "circularity_score_.csv")
    circ_headers = [
        "product_id", "sku_id", "recyclability_score", "reusability_score",
        "material_sustainability_score", "warranty_score", "overall_circularity_score",
        "circularity_category", "recommendation"
    ]
    circ_rows = []
    for i in range(1, 101):
        overall = float(30.0 + (i * 1.7) % 70.0)
        circ_rows.append([
            f"{float(i)}",
            f"SKU{i:04d}",
            f"{float(1 + (i % 10))}",
            f"{float(1 + ((i+2) % 10))}",
            f"{float(1 + ((i+4) % 10))}",
            f"{float(1 + ((i+6) % 10))}",
            f"{round(overall, 1)}",
            circularity_categories[i % len(circularity_categories)],
            recommendations[i % len(recommendations)]
        ])
    with open(circ_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(circ_headers)
        writer.writerows(circ_rows)

    print(f"Successfully generated all mock datasets (100 rows each) in {output_dir}")

if __name__ == "__main__":
    generate_mock_data()
