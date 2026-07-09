# EchoChain Project Progress

## Day 1

### Completed
- Created repository structure
- Explored Databricks workspace
- Added project documentation

---

## Day 2

### Completed
- Explored Unity Catalog
- Created Medallion Architecture planning notebook
- Explored SQL Editor
- Updated project documentation

---

## Next Step

Import the project dataset and implement the Bronze layer.

## Day 3

### Completed

- Received the initial marketplace dataset.
- Uploaded the dataset to Databricks Volume.
- Created the `03_Bronze_Data_Ingestion` notebook.
- Loaded the CSV dataset using PySpark.
- Verified the dataset schema and row count.
- Performed a basic null value validation.
- Created the Bronze table (`bronze_marketplace_data`).
- Verified the Bronze table by querying the stored data.

### Status

Bronze layer implementation completed successfully.


## Day 4

### Completed

- Uploaded all final project datasets to Databricks Volume.
- Read and validated all five CSV files using PySpark.
- Created separate Bronze tables for each dataset.
- Verified successful table creation and data availability.

### Bronze Tables

- bronze_bom_details
- bronze_sku_master
- bronze_scraper_data
- bronze_warranty_details
- bronze_circularity_score
