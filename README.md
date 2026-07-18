# EchoChain - Circular Economy ♻️

## Overview

EchoChain is a cloud-based data engineering project that implements the **Medallion Architecture (Bronze → Silver → Gold)** using **Databricks** and **Apache Spark**.

The project focuses on processing circular economy datasets, transforming raw data into validated and analytics-ready datasets for business intelligence and reporting.

---

## Project Architecture

```
Raw Data
    │
    ▼
Bronze Layer
    │
    ▼
Silver Layer
    │
    ▼
Gold Layer
    │
    ▼
Power BI Dashboard
```

---

## Technologies Used

- Databricks
- Apache Spark (PySpark)
- Delta Tables
- SQL
- Git & GitHub
- Medallion Architecture

---

## Repository Structure

```
EchoChain
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docs/
│   ├── images/
│   ├── bronze_handoff.md
│   ├── silver_handoff.md
│   ├── data_dictionary.md
│   ├── dataset_inventory.md
│   ├── data_quality_report.md
│   ├── project_progress.md
│   ├── project_structure.md
│   └── databricks_setup.md
│
├── handoff/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── 01_workspace_exploration.md
│   ├── 02_Medallion_Architecture_planning.md
│   ├── 05_Silver_Layer_Implementation.md
│
└── README.md
```

---

# Project Progress

## Week 1

### Day 1
- Repository Setup
- Databricks Workspace Setup
- GitHub Project Structure

### Day 2
- Medallion Architecture Planning
- Documentation
- Catalog Configuration

### Day 3
- Bronze Layer Data Ingestion
- Initial Bronze Table Creation

### Day 4
- Multi-table Bronze Layer Implementation
- Bronze Delta Tables Created

### Day 5
- Bronze Layer Validation
- Bronze Dataset Export
- Bronze Layer Handoff

### Day 6
- Silver Layer Implementation
- Silver Delta Tables Created

### Day 7
- Silver Layer Validation
- Silver Dataset Export
- Silver Layer Handoff

### Day 8
- Repository Documentation
- Data Dictionary
- Dataset Inventory
- Project Documentation Updated

---

# Bronze Tables

- bronze_scraper_data
- bronze_sku_master
- bronze_bom_details
- bronze_warranty_details
- bronze_circularity_score

---

# Silver Tables

- silver_scraper_data
- silver_sku_master
- silver_bom_details
- silver_warranty_details
- silver_circularity_score

---

# Current Status

- Bronze Layer Completed
- Bronze Validation Completed
- Bronze Handoff Completed
- Silver Layer Completed
- Silver Validation Completed
- Silver Handoff Completed
- Documentation Updated

---

# Upcoming Work

- Gold Layer Integration
- Gold Layer Validation
- BI Dashboard Development
- Final Project Review

---

## Project Team

| Role | Responsibility |
|------|----------------|
| Sri Talmi | Data Collection |
| Chirag | Data Engineering |
| Miduna | PySpark Engineering |
| Shivaji | BI Engineering |

---

## Author

**Chirag Tarvekar**

Role: **Data Engineer**

---

## Status

**Project In Progress**