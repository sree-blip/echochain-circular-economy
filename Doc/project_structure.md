# EchoChain Project Structure

---

## Overview

The Power BI solution is designed to transform processed data into interactive dashboards and business insights.

Data Source → Power Query → Data Model → DAX Measures → Power BI Dashboards

---

## Data Source

Stores data imported from Databricks, CSV files, or SQL databases.

---

## Power Query

Performs data cleaning, transformation, and preparation before loading the data model.

---

## Data Model

Creates relationships between tables and builds a star schema for efficient reporting.

---

## DAX Measures

Contains calculated columns, measures, KPIs, and business metrics for dashboard analysis.

---

## Responsibilities

- Import data from Databricks SQL Endpoint
- Clean and transform data using Power Query
- Create relationships between tables
- Develop DAX Measures and KPIs
- Build interactive Power BI dashboards
- Publish and maintain Power BI reports

---

## Dashboard Architecture

The EchoChain dashboard consists of multiple reporting pages.

### Product Overview Dashboard

Displays product details, inventory, sales, and lifecycle metrics.

### Circularity Score Dashboard

Displays Circularity Score, sustainability KPIs, and recycling insights.

### Executive Dashboard

Provides high-level business KPIs, trends, and performance summaries.

---

## Planned Data Flow

Raw Data

↓

Databricks SQL Endpoint

↓

Power Query

↓

Data Model

↓

DAX Measures

↓

Power BI Dashboards

---

## Current Status

- Repository initialized
- Power BI environment configured
- Dataset connection planned
- Dashboard design in progress
- KPI planning completed
