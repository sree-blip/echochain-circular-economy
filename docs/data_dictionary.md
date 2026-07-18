# Data Dictionary

## Project
EchoChain - Circular Economy

## Layer
Silver Layer

## Prepared By
chirag – Data Engineer

## Description

This document describes the schema and purpose of each Silver Layer dataset used in the EchoChain Circular Economy project.

---

# 1. silver_scraper_data

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| Listing_ID | String | Unique marketplace listing identifier |
| SKU | String | Product SKU identifier |
| Product_Name | String | Product name |
| Brand | String | Product brand |
| Model | String | Product model |
| Category | String | Product category |
| Marketplace | String | Marketplace source |
| Condition | String | Product condition |
| Original_MRP_INR | Integer | Original product price |
| Selling_Price_INR | Integer | Marketplace selling price |
| Seller_City | String | Seller location |
| Seller_Rating | Double | Seller rating |
| Posted_Date | Date | Listing date |
| Listing_URL | String | Marketplace listing URL |

---

# 2. silver_sku_master

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| SKU | String | Unique SKU identifier |
| Product_Name | String | Product name |
| Brand | String | Product brand |
| Category | String | Product category |
| Product_Type | String | Product type |
| Launch_Year | Integer | Product launch year |
| Manufacturer | String | Manufacturer name |

---

# 3. silver_bom_details

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| SKU | String | Product SKU |
| Component_Name | String | Component used in product |
| Material | String | Material type |
| Weight_Grams | Double | Component weight |
| Recyclable | String | Recyclability status |
| Supplier | String | Supplier name |

---

# 4. silver_warranty_details

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| SKU | String | Product SKU |
| Warranty_Months | Integer | Warranty duration |
| Warranty_Type | String | Warranty category |
| Service_Center | String | Authorized service center |
| Replacement_Available | String | Replacement availability |

---

# 5. silver_circularity_score

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| SKU | String | Product SKU |
| Recyclability_Score | Double | Product recyclability score |
| Repairability_Score | Double | Product repairability score |
| Reusability_Score | Double | Product reusability score |
| Circularity_Score | Double | Overall circularity score |
| Sustainability_Level | String | Sustainability category |

---

# Summary

| Layer | Total Tables |
|--------|--------------|
| Silver | 5 |

## Status

✅ Data Dictionary Completed

Prepared for:
- BI Engineer
- Dashboard Development
- Gold Layer Integration
