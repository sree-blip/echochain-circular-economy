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


## Day 5

### Completed

- Validated all Bronze tables.
- Exported Bronze datasets.
- Prepared Bronze handoff package.
- Completed documentation for Silver layer transition.

### Status

Ready for Silver Layer implementation.


## Day 6

### Completed

- Received Silver datasets from PySpark Engineer.
- Uploaded Silver CSV files.
- Created 5 Silver Delta tables.
- Validated schemas and row counts.
- Completed Silver layer implementation.

### Status

Ready for Gold Layer.


## Day 7

### Completed

- Validated Silver tables
- Exported Silver datasets
- Prepared Silver handoff package
- Completed documentation

### Status

Ready for BI Engineer.

## Day 8

### Work Completed

- Repository documentation updated
- Data Dictionary created
- Dataset Inventory created
- Repository structure reviewed
- Silver handoff documentation finalized

### Status

Project documentation completed.
