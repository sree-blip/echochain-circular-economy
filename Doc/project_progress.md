
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

# Day 8 – Build Charts

## Objective

Build interactive Power BI charts to analyze product categories, brands, circularity scores, warranty performance, and recyclability for the EchoChain Circular Economy dashboard.

---

## Tasks Completed

- Created a Clustered Column Chart to compare Circularity Score by Brand.
- Added a Bar Chart to display Total Products by Category.
- Built a Donut Chart showing Product Distribution by Brand.
- Created a Line Chart to visualize product launches by Year.
- Added a Column Chart for Average Recyclability Score by Category.
- Added a Bar Chart for Average Repairability Score by Brand.
- Applied consistent color themes and data labels.
- Enabled cross-filtering between charts and slicers.
- Verified all visuals display correct values after applying filters.
- Saved the updated Power BI dashboard.

---

## Dashboard Visuals

- Clustered Column Chart
- Bar Chart
- Donut Chart
- Line Chart
- Column Chart
- Brand Slicer
- Category Slicer
- Launch Year Slicer

---

## Charts Created

- Circularity Score by Brand
- Total Products by Category
- Product Distribution by Brand
- Products by Launch Year
- Average Recyclability Score by Category
- Average Repairability Score by Brand

---

## Next Step

Improve dashboard usability by adding advanced formatting, conditional formatting, tooltips, and interactive features.

# Day 9 – Improve Dashboard Layout

## Objective

Enhance the overall dashboard appearance by improving layout, formatting, alignment, and user experience.

---

## Tasks Completed

- Improved the alignment of KPI cards and charts.
- Applied a consistent color theme across all report pages.
- Added a professional dashboard title.
- Formatted KPI cards with uniform fonts and sizes.
- Improved chart titles, legends, and axis labels.
- Added rounded corners and subtle shadows to visuals.
- Arranged slicers neatly for better usability.
- Optimized spacing between visuals.
- Verified cross-filtering and slicer interactions.
- Reviewed dashboard design for consistency.
- Saved the enhanced Power BI dashboard.

---

## Dashboard Improvements

- Professional Layout
- Consistent Theme
- Better KPI Card Design
- Enhanced Chart Formatting
- Improved Navigation
- Optimized User Experience

---

## Next Step

Perform final testing, update project documentation.

# Day 10 – Mid-Project Review Dashboard

## Objective

Review the progress of the EchoChain Power BI dashboard, validate all implemented features, ensure data accuracy, and prepare the dashboard for the next development phase.

---

## Tasks Completed

- Reviewed all dashboard pages and report layouts.
- Verified relationships between all imported tables.
- Validated DAX measures and KPI calculations.
- Checked the accuracy of charts and visualizations.
- Tested Brand, Category, and Launch Year slicers.
- Verified cross-filtering and visual interactions.
- Improved dashboard formatting and alignment.
- Fixed minor formatting and layout issues.
- Updated project documentation with the latest progress.
- Saved the reviewed Power BI dashboard.

---

## Dashboard Review

- KPI Dashboard ✓
- Product Overview Dashboard ✓
- Interactive Charts ✓
- Slicers & Filters ✓
- Data Model Validation ✓
- DAX Measure Validation ✓
- Dashboard Formatting ✓
- Visual Interaction Testing ✓

---



## Next Step

- Create advanced DAX measures.
- Implement Circularity Score calculations.
- Build Executive Dashboard.
- Add advanced analytics and business insights

# Day 11 – Create DAX Measures

## Objective

Create reusable DAX measures to calculate key business metrics for the EchoChain Circular Economy Dashboard.

---

## Tasks Completed

- Created DAX measures for Total Products.
- Created Average Circularity Score measure.
- Created Average Repairability Score measure.
- Created Average Recyclability Score measure.
- Created Average Warranty Score measure.
- Created Total BOM Components measure.
- Created Circularity Target measure.
- Verified all DAX measures return correct values.
- Updated KPI cards using the new measures.
- Saved the Power BI dashboard.

---

## DAX Measures Created

- Total Products
- Average Circularity Score
- Average Repairability Score
- Average Recyclability Score
- Average Warranty Score
- Total BOM Components
- Circularity Target

---

## Next Step

Create advanced calculations and business insights using additional DAX measures.



---

# Day 12 – Circularity Score Calculation

## Objective

Calculate and analyze the Circularity Score of products using Power BI and DAX
to evaluate the circular economy performance of products.

---

## Tasks Completed

- Reviewed the Circularity Score dataset.
- Verified the available circularity-related fields.
- Connected Circularity Score data with product information.
- Created the Average Circularity Score measure.
- Created the Circularity Target measure.
- Created the Circularity Gap measure.
- Created the Circularity Status measure.
- Tested the Circularity Score calculations.
- Added Circularity Score KPIs to the dashboard.
- Added Brand and Category slicers.
- Created Circularity Score visualizations.
- Verified that the visuals respond correctly to filters.
- Saved the updated Power BI dashboard.

---

## DAX Measures Created

- Average Circularity Score
- Circularity Target
- Circularity Gap
- Circularity Status

---

## Dashboard Visuals

- Average Circularity Score KPI
- Circularity Target KPI
- Circularity Gap KPI
- Average Circularity Score by Brand
- Average Circularity Score by Category
- Overall Circularity Score Gauge
- Brand and Category Slicers

---

## Next Step

Perform depreciation analysis using original price and resale price data.

---

# Day 13 – Depreciation Analysis

## Objective

Analyze product depreciation by comparing original prices and resale prices
to understand product value retention in the secondary market.

---

## Tasks Completed

- Reviewed marketplace and aggregated product data.
- Verified Original Price and Resale Price fields.
- Calculated Average Original Price.
- Calculated Average Resale Price.
- Created the Average Depreciation % measure.
- Created the Price Retention % measure.
- Compared depreciation percentages across brands.
- Analyzed depreciation across product categories.
- Created Original Price vs Resale Price visualizations.
- Created Depreciation % by Brand visualization.
- Created a Price vs Resale Price scatter chart.
- Added depreciation KPIs to the dashboard.
- Created a detailed product summary table.
- Tested the depreciation calculations.
- Verified dashboard filtering and interactions.
- Saved the updated Power BI dashboard.

---

## DAX Measures Created

- Average Original Price
- Average Resale Price
- Average Depreciation %
- Price Retention %

---

## Dashboard Visuals

- Average Original Price KPI
- Average Resale Price KPI
- Average Depreciation % KPI
- Original Price vs Resale Price by Brand
- Average Depreciation % by Brand
- Original Price vs Resale Price Scatter Chart
- Detailed Product Summary Table

---

## Analysis Outcome

- Identified differences between original and resale prices.
- Compared depreciation levels between different brands.
- Analyzed product value retention in the secondary market.
- Identified products and brands with relatively higher depreciation.
- Prepared depreciation insights for the Executive Dashboard.

---

## Next Step

Finalize the dashboard design and prepare the Executive Dashboard
with key business insights.

---

# Day 14 – Executive Dashboard Design

## Objective

Design and organize the Executive Dashboard to present important
business KPIs, circularity metrics, depreciation analysis, and
product insights in a clear and professional format.

---

## Tasks Completed

- Reviewed the existing Power BI dashboard pages.
- Finalized the Executive Dashboard layout.
- Organized important KPI cards.
- Added Circularity Score KPIs.
- Added depreciation-related KPIs.
- Added relevant charts and tables.
- Added Brand, Category, and Launch Year slicers.
- Improved visual alignment and spacing.
- Applied consistent formatting across visuals.
- Selected a professional dashboard theme.
- Added dashboard title and section headings.
- Verified interactions between slicers and visuals.
- Saved the updated Power BI dashboard.

---

## Dashboard Components

- Total Products KPI
- Average Circularity Score KPI
- Circularity Target KPI
- Circularity Gap KPI
- Average Original Price KPI
- Average Resale Price KPI
- Average Depreciation % KPI
- Circularity Score Gauge
- Circularity Score by Brand
- Circularity Score by Category
- Depreciation Analysis
- Product Summary Table
- Brand and Category Slicers

---

## Outcome

Created the initial Executive Dashboard structure with important
business metrics and analytical visuals.

---

## Next Step

Review the complete dashboard and validate all visuals, measures,
filters, and interactions.

---

# Day 15 – Dashboard Review

## Objective

Review the Power BI dashboard and verify that all calculations,
visuals, filters, and layouts are working correctly.

---

## Tasks Completed

- Reviewed all dashboard pages.
- Verified relationships between imported tables.
- Validated DAX measures and KPI calculations.
- Checked Circularity Score calculations.
- Checked Depreciation calculations.
- Verified charts and visualizations.
- Tested Brand slicer.
- Tested Category slicer.
- Tested Launch Year slicer.
- Verified cross-filtering between visuals.
- Checked visual alignment and spacing.
- Fixed minor formatting issues.
- Reviewed dashboard titles and labels.
- Saved the reviewed Power BI dashboard.

---

## Dashboard Review

- KPI Dashboard ✓
- Circularity Score Dashboard ✓
- Depreciation Analysis ✓
- Interactive Charts ✓
- Slicers & Filters ✓
- Data Model Validation ✓
- DAX Measure Validation ✓
- Dashboard Formatting ✓
- Visual Interaction Testing ✓

---

## Outcome

Completed the first detailed review of the Power BI dashboard and
identified areas requiring improvement.

---

## Next Step

Improve the dashboard UI and visual presentation.

---

# Day 16 – Improve Dashboard UI

## Objective

Improve the visual design, usability, and professional appearance
of the Power BI dashboard.

---

## Tasks Completed

- Improved dashboard layout.
- Adjusted KPI card sizes.
- Aligned visuals properly.
- Improved spacing between visuals.
- Standardized font sizes.
- Updated chart titles.
- Improved slicer formatting.
- Applied consistent background formatting.
- Improved KPI card formatting.
- Updated visual borders and shadows where required.
- Improved dashboard navigation.
- Checked the dashboard in different screen sizes.
- Saved the updated dashboard.

---

## UI Improvements

- Professional dashboard theme
- Consistent fonts
- Consistent KPI card design
- Consistent chart formatting
- Improved slicers
- Improved spacing
- Improved alignment
- Improved navigation
- Improved readability

---

## Outcome

Improved the overall appearance and usability of the EchoChain
Power BI dashboard.

---

## Next Step

Create and configure Drill-Through pages for detailed analysis.

---

# Day 17 – Add Drill-Through Pages

## Objective

Create Drill-Through functionality so users can move from summary
visuals to detailed product or category information.

---

## Tasks Completed

- Created a Drill-Through page.
- Added Product/Brand fields to Drill-through filters.
- Added relevant product details.
- Added Circularity Score information.
- Added Depreciation information.
- Added Original Price information.
- Added Resale Price information.
- Added product-level summary tables.
- Added supporting charts.
- Added Back button for dashboard navigation.
- Tested Drill-Through functionality.
- Verified that filters are passed correctly.
- Saved the updated Power BI dashboard.

---

## Drill-Through Information

- Product Name
- Brand
- Category
- Condition
- Circularity Score
- Original Price
- Resale Price
- Depreciation %
- Warranty Information
- Repairability Information
- Recyclability Information

---

## Outcome

Created an interactive Drill-Through page for detailed product-level
analysis.

---

## Next Step

Perform final testing of all dashboard pages and interactions.

---

# Day 18 – Final Dashboard Testing

## Objective

Perform complete testing of the Power BI dashboard before final
submission and presentation.

---

## Tasks Completed

- Tested all dashboard pages.
- Tested all KPI cards.
- Tested all DAX measures.
- Tested all charts.
- Tested all slicers.
- Tested Brand filtering.
- Tested Category filtering.
- Tested Launch Year filtering.
- Tested Drill-Through functionality.
- Checked cross-filtering.
- Checked chart interactions.
- Checked data accuracy.
- Checked dashboard navigation.
- Checked visual formatting.
- Checked page titles.
- Checked table values.
- Verified Circularity Score calculations.
- Verified Depreciation calculations.
- Saved the final tested dashboard.

---

## Testing Checklist

- KPI calculations ✓
- DAX measures ✓
- Circularity Score ✓
- Depreciation Analysis ✓
- Slicers ✓
- Charts ✓
- Tables ✓
- Drill-Through ✓
- Navigation ✓
- Visual formatting ✓
- Data validation ✓

---

## Outcome

Completed functional and visual testing of the Power BI dashboard.

---

## Next Step

Fix the issues identified during final testing.

---

