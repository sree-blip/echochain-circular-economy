# Data Profiling & Exploratory Data Analysis (EDA) Report

This document profiles the 5 raw bronze datasets ingested for the **EchoChain Circular Economy** pipeline. It documents row counts, schema structures, and actual sample records extracted from the Spark Session run.

---

## 📊 Summary of Ingested Datasets

| Dataset Name | File Path | Row Count | Key Identifier | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Scraper Data** | `data/bronze/scraper_data_.csv` | 50,001 | `product_id` | Scraped listings from secondary marketplaces (OLX, eBay, etc.) |
| **Warranty Details** | `data/bronze/warrant_details_.csv` | 50,000 | `warranty_id` | Historical warranty registrations and claim logs |
| **BOM Details** | `data/bronze/BOM_details_.csv` | 50,000 | `bom_id` | Bill of Materials specifying component weights, costs, and materials |
| **SKU Master** | `data/bronze/SKU_Master_.csv` | 50,000 | `sku_id` | Official manufacturer catalog and technical details |
| **Circularity Score** | `data/bronze/circularity_score_.csv` | 50,000 | `product_id` | Baseline circularity ratings and recommendations |

---

## 🔍 Detailed Schemas & Real Sample Data

### 1. Scraper Data (`scraper_data_.csv`)
*   **Row Count**: 50,001
*   **Schema Tree**:
    ```
    root
     |-- product_id: double (nullable = true)
     |-- marketplace_name: string (nullable = true)
     |-- product_name: string (nullable = true)
     |-- brand: string (nullable = true)
     |-- category: string (nullable = true)
     |-- condition: string (nullable = true)
     |-- resale_price: double (nullable = true)
     |-- seller_name: string (nullable = true)
     |-- seller_rating: double (nullable = true)
     |-- location: string (nullable = true)
     |-- listing_date: string (nullable = true)
     |-- product_url: string (nullable = true)
     |-- availability_status: string (nullable = true)
     |-- scraped_date: string (nullable = true)
    ```
*   **Real Data Preview (Top 3 rows)**:
    ```
    +----------+----------------+------------+------+-----------+-----------+------------+-----------+-------------+----------+------------+--------------------+-------------------+------------+
    |product_id|marketplace_name|product_name| brand|   category|  condition|resale_price|seller_name|seller_rating|  location|listing_date|         product_url|availability_status|scraped_date|
    +----------+----------------+------------+------+-----------+-----------+------------+-----------+-------------+----------+------------+--------------------+-------------------+------------+
    |       1.0|             OLX|   Product_1|Lenovo|     Mobile|Refurbished|     21134.0|   Seller_1|          4.8|Vijayawada|  2024-03-07|https://example.c...|               Sold|  2025-01-29|
    |       2.0|             OLX|   Product_2| Apple|Accessories|       Good|     12871.0|   Seller_2|          4.5| Hyderabad|  2024-06-19|https://example.c...|               Sold|  2022-03-06|
    |       3.0|             OLX|   Product_3| Apple|Accessories|        New|     26988.0|   Seller_3|          4.1| Hyderabad|  2025-01-22|https://example.c...|          Available|  2022-10-31|
    +----------+----------------+------------+------+-----------+-----------+------------+-----------+-------------+----------+------------+--------------------+-------------------+------------+
    ```

---

### 2. Warranty Details (`warrant_details_.csv`)
*   **Row Count**: 50,000
*   **Schema Tree**:
    ```
    root
     |-- warranty_id: string (nullable = true)
     |-- sku_id: string (nullable = true)
     |-- product_id: double (nullable = true)
     |-- warranty_period_months: integer (nullable = true)
     |-- warranty_start_date: string (nullable = true)
     |-- warranty_end_date: string (nullable = true)
     |-- warranty_type: string (nullable = true)
     |-- coverage_details: string (nullable = true)
     |-- service_center_available: string (nullable = true)
     |-- claim_status: string (nullable = true)
     |-- last_service_date: string (nullable = true)
    ```
*   **Real Data Preview (Top 3 rows)**:
    ```
    +-----------+-------+----------+----------------------+-------------------+-----------------+-------------+-----------------+------------------------+------------+-----------------+
    |warranty_id| sku_id|product_id|warranty_period_months|warranty_start_date|warranty_end_date|warranty_type| coverage_details|service_center_available|claim_status|last_service_date|
    +-----------+-------+----------+----------------------+-------------------+-----------------+-------------+-----------------+------------------------+------------+-----------------+
    |    WAR0001|SKU0001|       1.0|                    24|         2022-11-27|       2025-02-08|       Seller|Parts and Service|                      No|     Expired|       2024-02-13|
    |    WAR0002|SKU0002|       2.0|                     6|         2024-11-15|       2023-09-21| Manufacturer|Parts and Service|                      No|      Active|       2025-02-17|
    |    WAR0003|SKU0003|       3.0|                    12|         2024-10-28|       2022-04-10| Manufacturer|Parts and Service|                      No|      Active|       2024-08-26|
    +-----------+-------+----------+----------------------+-------------------+-----------------+-------------+-----------------+------------------------+------------+-----------------+
    ```

---

### 3. BOM Details (`BOM_details_.csv`)
*   **Row Count**: 50,000
*   **Schema Tree**:
    ```
    root
     |-- bom_id: string (nullable = true)
     |-- sku_id: string (nullable = true)
     |-- product_id: double (nullable = true)
     |-- component_name: string (nullable = true)
     |-- component_weight: double (nullable = true)
     |-- recyclable: string (nullable = true)
     |-- recycled_content_percentage: double (nullable = true)
     |-- supplier_name: string (nullable = true)
     |-- cost_per_component: double (nullable = true)
     |-- hazardous_material_flag: string (nullable = true)
    ```
*   **Real Data Preview (Top 3 rows)**:
    ```
    +-------+-------+----------+--------------+----------------+----------+---------------------------+-------------+------------------+-----------------------+
    | bom_id| sku_id|product_id|component_name|component_weight|recyclable|recycled_content_percentage|supplier_name|cost_per_component|hazardous_material_flag|
    +-------+-------+----------+--------------+----------------+----------+---------------------------+-------------+------------------+-----------------------+
    |BOM0001|SKU0001|       1.0|       Battery|           775.0|       Yes|                       84.0|      ABC Ltd|            1762.0|                     No|
    |BOM0002|SKU0002|       2.0|      Keyboard|           100.0|       Yes|                       50.0|  XYZ Pvt Ltd|            1418.0|                     No|
    |BOM0003|SKU0003|       3.0|       Battery|           235.0|        No|                       83.0|  XYZ Pvt Ltd|            3839.0|                    Yes|
    +-------+-------+----------+--------------+----------------+----------+---------------------------+-------------+------------------+-----------------------+
    ```

---

### 4. SKU Master (`SKU_Master_.csv`)
*   **Row Count**: 50,000
*   **Schema Tree**:
    ```
    root
     |-- sku_id: string (nullable = true)
     |-- product_id: double (nullable = true)
     |-- product_name: string (nullable = true)
     |-- brand: string (nullable = true)
     |-- category: string (nullable = true)
     |-- model_number: string (nullable = true)
     |-- original_price: double (nullable = true)
     |-- manufacturing_date: string (nullable = true)
     |-- launch_year: integer (nullable = true)
     |-- product_type: string (nullable = true)
     |-- material_type: string (nullable = true)
     |-- weight: double (nullable = true)
     |-- dimensions: string (nullable = true)
     |-- country_of_origin: string (nullable = true)
     |-- expected_life_span: integer (nullable = true)
     |-- repairability_score: double (nullable = true)
    ```
*   **Real Data Preview (Top 3 rows)**:
    ```
    +-------+----------+------------+------+-----------+------------+--------------+------------------+-----------+------------+-------------+------+----------+-----------------+------------------+-------------------+
    | sku_id|product_id|product_name| brand|   category|model_number|original_price|manufacturing_date|launch_year|product_type|material_type|weight|dimensions|country_of_origin|expected_life_span|repairability_score|
    +-------+----------+------------+------+-----------+------------+--------------+------------------+-----------+------------+-------------+------+----------+-----------------+------------------+-------------------+
    |SKU0001|       1.0|   Product_1|Lenovo|     Mobile|      MDL001|       29442.0|        2022-03-01|       2025|         New|      Plastic|   7.0|   10x20x5|            India|                 9|                2.0|
    |SKU0002|       2.0|   Product_2| Apple|Accessories|      MDL002|       24481.0|        2024-09-11|       2025|         New|        Metal|   9.0|   10x20x5|            India|                10|                8.0|
    |SKU0003|       3.0|   Product_3| Apple|Accessories|      MDL003|       33292.0|        2024-08-03|       2025|         New|      Plastic|   9.0|   10x20x5|            India|                 5|                5.0|
    +-------+----------+------------+------+-----------+------------+--------------+------------------+-----------+------------+-------------+------+----------+-----------------+------------------+-------------------+
    ```

---

### 5. Circularity Score (`circularity_score_.csv`)
*   **Row Count**: 50,000
*   **Schema Tree**:
    ```
    root
     |-- product_id: double (nullable = true)
     |-- sku_id: string (nullable = true)
     |-- recyclability_score: double (nullable = true)
     |-- reusability_score: double (nullable = true)
     |-- material_sustainability_score: double (nullable = true)
     |-- warranty_score: double (nullable = true)
     |-- overall_circularity_score: double (nullable = true)
     |-- circularity_category: string (nullable = true)
     |-- recommendation: string (nullable = true)
    ```
*   **Real Data Preview (Top 3 rows)**:
    ```
    +----------+-------+-------------------+-----------------+-----------------------------+--------------+-------------------------+--------------------+--------------+
    |product_id| sku_id|recyclability_score|reusability_score|material_sustainability_score|warranty_score|overall_circularity_score|circularity_category|recommendation|
    +----------+-------+-------------------+-----------------+-----------------------------+--------------+-------------------------+--------------------+--------------+
    |       1.0|SKU0001|                2.0|              7.0|                          1.0|           6.0|                     68.0|           Excellent|       Recycle|
    |       2.0|SKU0002|                4.0|              7.0|                          3.0|          10.0|                     50.0|                Poor|         Reuse|
    |       3.0|SKU0003|                6.0|              6.0|                          4.0|           3.0|                     76.0|                Poor|     Refurbish|
    +----------+-------+-------------------+-----------------+-----------------------------+--------------+-------------------------+--------------------+--------------+
    ```

---

## 📌 Technical Findings & Challenges for Cleaning (Silver Layer)
Looking at this actual data, we will need to address the following problems in tomorrow's cleaning stage (`pyspark/data_cleaning.py`):
1.  **Logical Date Mismatch**: In Warranty Details, row 2 has a start date of `2024-11-15` but an end date of `2023-09-21` (which is in the past). We must handle these date logic errors.
2.  **Date Format Casts**: Date fields are loaded as `StringType` and need to be cleaned and cast to standard PySpark `DateType`.
3.  **Standardization**: String fields like `brand`, `category`, and `condition` have different casings and trailing spaces that need to be trimmed and standardized.
