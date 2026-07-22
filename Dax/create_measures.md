





# DAX Measures



# KPI Measures

## Total Products

```DAX
Total Products =
DISTINCTCOUNT('SKU_Master_final'[product_id])
```

## Total BOM Components

```DAX
Total BOM Components =
COUNTROWS('BOM_details_updated')
```

## Average Circularity Score

```DAX
Average Circularity Score =
AVERAGE('circularity_score_updated'[overall_circularity_score])
```

## Average Repairability Score

```DAX
Average Repairability Score =
AVERAGE('SKU_Master_final'[repairability_score])
```

## Average Recyclability Score

```DAX
Average Recyclability Score =
AVERAGE('circularity_score_updated'[recyclability_score])
```

## Average Warranty Score

```DAX
Average Warranty Score =
AVERAGE('circularity_score_updated'[warranty_score])
```
