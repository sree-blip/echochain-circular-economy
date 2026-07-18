
# EchoChain Project Progress

## Day 1

### Completed

- Created repository structure
- Download Microsoft Power BI
- Explored Power BI





# Day 2 – Connect Power BI to Databricks

## Objective

Prepare and configure the connection between Power BI Desktop and Databricks for the EchoChain project.

---

## Tasks Completed

- Opened Power BI Desktop.
- Explored the **Get Data** option.
- Selected the **Azure Databricks** connector.
- Studied the connection requirements:
  - Server Hostname
  - HTTP Path
  - Authentication credentials
- Reviewed the workflow for connecting Power BI to Databricks.
- Prepared the environment for data import.

---


## Connection Steps

1. Open Power BI Desktop.
2. Select *Home → Get Data*.
3. Search for *Azure Databricks*.
4. Enter the *Server Hostname*.
5. Enter the *HTTP Path*.
6. Sign in using the required authentication method.
   


---

## Status

- Connection setup prepared.
- Explored the Azure Databricks connector.
- Waiting for the Databricks SQL Warehouse details to establish the live connection.

---

## Next Step

- Import project datasets into Power BI.
- Validate imported tables.


# Day 3 – Import Datasets into Power BI

## Objective

Import the required datasets from Databricks into Power BI for data modeling and dashboard development.

## Tasks Completed

- Connected Power BI to the Databricks SQL Warehouse.
- Opened the Navigator window.
- Selected the required project tables.
- Imported the datasets into Power BI.
- Verified that all imported tables were loaded successfully.

## Datasets Imported

- Scraper_data
- warrant_details
- circularity_score
- SKU_Master
- BOM_details


## Next Step
- Create relationships between imported tables.
- Build the Power BI data model.


# Day 4 – Power BI Data Modeling & Table Relationships

## Objective

Create relationships between the imported EchoChain datasets to build a structured Power BI data model for analysis and reporting.

---

## Tasks Completed

- Opened the Model View in Power BI Desktop.
- Identified common columns (**SKU** and **Product_ID**) across the datasets.
- Created relationships between the imported tables.
- Configured the correct relationship cardinality.
- Verified active relationships using the Manage Relationships window.
- Organized the data model for better readability.

- Saved the updated Power BI project.

---
## Relationships Created

- SKU_Master_updated[product_id] → circularity_score_updated[product_id]
- SKU_Master_updated[product_id] → scraper_data_[product_id]
- SKU_Master_updated[sku_id] → BOM_details_updated[sku_id]
- SKU_Master_updated[sku_id] → warrant_details_updated[sku_id]
- Cardinality: One to Many (1:*)




---

## Next Step

Build the first Power BI report by creating KPI Cards, charts, slicers, and other visuals using the connected data model.

#  Day 4 – Build First Basic Report

##  Objective
Create the first interactive Power BI dashboard using the EchoChain dataset.

##  Tasks Completed
- Created KPI Cards:
  - Total Products
  - Average Circularity Score
  - Warranty Records
  - Total Components (BOM)
- Built a Product by Category bar chart.
- Built a Product by Brand pie chart.
- Built an Average Circularity Score by Category column chart.
- Added a Product Details table.
- Added Brand and Category slicers.
- Applied dashboard formatting with titles and alignment.
- Tested interactions between slicers and visuals.

##  Visuals Created
- KPI Cards (4)
- Clustered Bar Chart
- Pie Chart
- Clustered Column Chart
- Table Visual
- Brand Slicer
- Category Slicer

##  Tools Used
- Power BI Desktop
- CSV Dataset
- Data Modeling
- Basic Power BI Visualizations

## Next Step

Continue with **Week 2** by creating a **Product Overview Dashboard**. Add KPI cards, improve the dashboard layout, apply consistent formatting, and enhance interactivity using slicers and filters to provide better insights into the EchoChain datasets.

# Day 6 – Product Overview Dashboard

## Objective

Build the first Power BI dashboard to provide an overview of the EchoChain Circular Economy dataset using KPI cards, charts, slicers, and a data table.

---

## Tasks Completed

- Created a new dashboard page named **Product Overview Dashboard**.
- Added KPI cards for Total Products, Average Circularity Score, Warranty Records, and Total Components.
- Built a Product by Category bar chart.
- Created a Product by Brand pie chart.
- Added an Average Circularity Score by Category column chart.
- Inserted a Brand slicer for interactive filtering.
- Added a product details table for detailed analysis.
- Formatted visuals with consistent colors, borders, and titles.
- Verified that all visuals interact correctly with the data model.
- Saved the updated Power BI dashboard.

---

# Day 6 – Product Overview Dashboard

## Objective

Build the first Power BI dashboard to provide an overview of the EchoChain Circular Economy dataset using KPI cards, charts, slicers, and a data table.

---

## Tasks Completed

- Created a new dashboard page named **Product Overview Dashboard**.
- Added KPI cards for Total Products, Average Circularity Score, Warranty Records, and Total Components.
- Built a Product by Category bar chart.
- Created a Product by Brand pie chart.
- Added an Average Circularity Score by Category column chart.
- Inserted a Brand slicer for interactive filtering.
- Added a product details table for detailed analysis.
- Formatted visuals with consistent colors, borders, and titles.
- Verified that all visuals interact correctly with the data model.
- Saved the updated Power BI dashboard.

---

## Dashboard Visuals

- KPI Cards
- Bar Chart
- Pie Chart
- Column Chart
- Brand Slicer
- Product Details Table

---

## Next Step

Create KPI visuals with trend analysis and enhance the dashboard with additional interactive charts.

# Day 7 – Create KPI Cards

## Objective

Create KPI Cards to display key business metrics for the EchoChain dashboard.

---

## Tasks Completed

- Created KPI cards for Total Products.
- Added Average Circularity Score card.
- Added Warranty Records card.
- Added Total Components (BOM) card.
- Added Average Recyclability Percentage card.
- Added Average Repairability Score card.
- Formatted KPI cards with consistent colors and layout.
- Saved the updated Power BI dashboard.

---

## KPI Cards Created

- Total Products
- Average Circularity Score
- Warranty Records
- Total Components (BOM)
- Average Recyclability %

---

## Next Step

Create charts and graphs to analyze product categories, brands, and circularity performance.

