# EchoChain - Daily Project Progress

This document tracks the daily progress and contributions for the PySpark data engineering role on the EchoChain Circular Economy project.

---

### Day 1
- Created the initial PySpark setup documentation (`docs/pyspark_setup.md`).
- Documented system dependency requirements for Python 3.12.10, JDK 17, and PySpark 4.1.2.
- Provided command-line verification scripts to verify local Python and Java versions.
- Drafted a local PySpark validation script to test session initialization.

### Day 2
- Completed PySpark setup guide with Windows-specific troubleshooting for `winutils.exe` warnings.
- Implemented the Spark Session configuration script (`configs/spark_config.py`).
- Configured local Spark settings, including memory allocations and reduced partition sizes.

### Day 3
- Established core project directory structure (`configs/`, `data/`, `docs/`, `pyspark/`, `tests/`).
- Defined Bronze, Silver, and Gold layer target schemas for listings, BOMs, and warranties.
- Documented PySpark transformation phases (cleaning, SKU matching) in `docs/workflow.md`.

### Day 4
- Implemented baseline StructType schemas and a reusable CSV data loader in `pyspark/utils.py`.
- Developed the data verification script (`pyspark/explore_schema.py`) to inspect column structures.
- Verified successful local schema validation, row counts, and data previews.

### Day 5
- Ingested the 5 real datasets into `data/bronze/` and aligned directory names with teammate.
- Refactored PySpark StructType schemas for all 5 raw datasets in `pyspark/utils.py`.
- Profiled the 5 real datasets (50,000 rows each) and wrote `docs/data_profiling.md`.
- Expanded the mock generator to create 100 mock rows per dataset inside `tests/mock_data/`.
- Authored the unit test suite (`tests/test_utils.py`) and verified a successful test execution.
- Updated `.gitignore` rules to track test code while excluding large raw CSV datasets.

### Day 6
- Created the core cleaning logic in `pyspark/data_cleaning.py` to remove nulls and assign default values.
- Successfully generated and saved the clean initial Silver Layer datasets in `data/silver/`.
- Authored the unit test suite (`tests/test_cleaning.py`) to verify null-handling and verified a successful execution.

### Day 7
- Implemented product name and text standardization logic in `pyspark/data_cleaning.py` (casing, whitespace trimming, and underscore replacement).
- Standardized join keys (such as `sku_id`, `bom_id`, and `warranty_id`) to uppercase across all datasets.
- Updated and executed the unit test suite (`tests/test_cleaning.py`) to verify the new standardization rules.

### Day 8
- Developed the regex-based SKU extraction module (`pyspark/sku_extraction.py`) to parse and standardize brand, model, RAM, and storage specifications.
- Verified the logic via unit tests (`tests/test_extraction.py`) and executed the pipeline to append these attributes to the Silver scraper data.

### Day 9
- Developed `pyspark/transformation.py` to standardize datatypes and cast date columns to DateType.
- Resolved logical date mismatches in the warranty dataset by swapping inverted start/end dates.
- Enforced original schema column ordering on disk to prevent downstream positional mismatches.
- Verified all transformation functions via unit tests in `tests/test_transformation.py`.

### Day 10
- Implemented `pyspark/validate_silver.py` to verify Silver dataset schemas, datatypes, and key relationships.
- Confirmed date formats (yyyy-MM-dd) and timeline logic are consistent across all 5 Silver datasets.
- Tested and verified 100.00% foreign key join compatibility on sku_id.
