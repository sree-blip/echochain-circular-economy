# EchoChain Project Structure

## Overview

The project follows the Medallion Architecture.

Raw Data
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer

## Bronze Layer
Stores raw data collected from web scraping and source files.

## Silver Layer
Contains cleaned, validated, and standardized datasets.

## Gold Layer
Stores business-ready datasets optimized for analytics and reporting.

## Responsibilities

- Manage Databricks environment
- Create Bronze, Silver, and Gold layers
- Configure Delta Lake
- Manage data ingestion
- Optimize data pipeline


## Data Architecture

The EchoChain project is designed using the Medallion Architecture.

### Bronze Layer (Planned)

Stores raw data collected from the original source.

### Silver Layer (Planned)

Stores cleaned and validated data.

### Gold Layer (Planned)

Stores analytics-ready datasets for reporting and dashboards.

---

## Planned Data Flow

Raw Data

↓

Bronze

↓

Silver

↓

Gold

↓

Power BI Dashboard

---

## Current Status

- Repository initialized
- Databricks environment explored
- Architecture documented
- Data ingestion is planned for the next phase


## Current Implementation Status

### Bronze Layer ✅

- Testing dataset uploaded successfully.
- Bronze managed table created.
- Raw marketplace data stored without transformation.

### Silver Layer ⏳

Planned for data cleaning and transformation.

### Gold Layer ⏳

Planned for analytics-ready datasets.
