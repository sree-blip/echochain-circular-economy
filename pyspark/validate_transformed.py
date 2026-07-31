import os
import sys
import pandas as pd

def validate_circularity_dataset(filepath, format_type="parquet"):
    """
    Validates logic, completeness, and schema integrity of the Circularity Dataset (Parquet/CSV).
    """
    errors = []
    print(f"\nValidating Circularity Dataset ({format_type.upper()})...")
    
    if not os.path.exists(filepath):
        errors.append(f"File not found: {filepath}")
        return errors

    try:
        if format_type == "parquet":
            df = pd.read_parquet(filepath)
        else:
            df = pd.read_csv(filepath)
        
        # 1. Row count validation (expecting 50,000 matches)
        row_count = len(df)
        print(f"  - Total rows: {row_count}")
        if row_count != 50000:
            errors.append(f"Row count mismatch! Expected 50000, found {row_count}")
            
        # 2. Critical column existence check
        critical_cols = [
            "sku_id", "product_id", "product_name", "resale_price", 
            "bom_id", "component_name", "overall_circularity_score", "circularity_category"
        ]
        for col in critical_cols:
            if col not in df.columns:
                errors.append(f"Missing critical column: {col}")
        
        # If columns are missing, return early since logical assertions will crash
        if errors:
            return errors
            
        # 3. Null values check in primary keys
        pks_with_nulls = df[df["sku_id"].isna() | df["product_id"].isna()]
        if len(pks_with_nulls) > 0:
            errors.append(f"Found {len(pks_with_nulls)} records with null sku_id or product_id.")
            
        # 4. Values business range validations
        invalid_prices = df[df["resale_price"] <= 0]
        if len(invalid_prices) > 0:
            errors.append(f"Found {len(invalid_prices)} records with invalid negative or zero resale prices.")
            
        # 5. Score ranges validation
        if "overall_circularity_score" in df.columns:
            invalid_scores = df[(df["overall_circularity_score"] < 0) | (df["overall_circularity_score"] > 100)]
            invalid_scores = invalid_scores.dropna(subset=["overall_circularity_score"])
            if len(invalid_scores) > 0:
                errors.append(f"Found {len(invalid_scores)} records where overall_circularity_score is outside [0-100].")
            
        print(f"  - Circularity Dataset ({format_type.upper()}) schema and logic checks completed.")
        
    except Exception as e:
        errors.append(f"Failed to read/validate {format_type.upper()} dataset: {e}")
        
    return errors


def validate_aggregated_data(filepath):
    """
    Validates logic, completeness, and schema integrity of the Aggregated layer (CSV).
    """
    errors = []
    print("\nValidating Aggregated Product Data (CSV)...")
    
    if not os.path.exists(filepath):
        errors.append(f"File not found: {filepath}")
        return errors

    try:
        df = pd.read_csv(filepath)
        row_count = len(df)
        print(f"  - Total rows: {row_count}")
        
        # 1. Non-empty check
        if row_count == 0:
            errors.append("Aggregated product data is empty.")
            
        # 2. Critical column existence check
        expected_cols = [
            "brand", "category", "matched_model_name", "condition", 
            "listing_count", "avg_original_price", "avg_resale_price", "avg_depreciation_pct"
        ]
        for col in expected_cols:
            if col not in df.columns:
                errors.append(f"Missing critical column: {col}")
                
        if errors:
            return errors
            
        # 3. Numeric logic rules
        invalid_counts = df[df["listing_count"] < 1]
        if len(invalid_counts) > 0:
            errors.append(f"Found {len(invalid_counts)} records with listing_count < 1.")
            
        invalid_averages = df[(df["avg_original_price"] <= 0) | (df["avg_resale_price"] <= 0)]
        if len(invalid_averages) > 0:
            errors.append(f"Found {len(invalid_averages)} records with invalid negative or zero price averages.")
            
        # Allowed range: depreciation can go negative (appreciation up to -300% in mock data), but max 100% price cut
        invalid_deprecations = df[(df["avg_depreciation_pct"] < -300) | (df["avg_depreciation_pct"] > 100)]
        if len(invalid_deprecations) > 0:
            errors.append(f"Found {len(invalid_deprecations)} records with average depreciation out of bounds [-300 to 100].")
            
        print("  - Aggregated product data schema and metrics checks completed.")
        
    except Exception as e:
        errors.append(f"Failed to read/validate CSV dataset: {e}")
        
    return errors


def main():
    print("="*60)
    print("                 DATASET VALIDATION ENGINE                   ")
    print("="*60)
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    circularity_file = os.path.join(project_root, "data", "processed", "circularity_dataset", "part-0.parquet")
    circularity_csv_file = os.path.join(project_root, "data", "processed", "circularity_dataset.csv")
    aggregated_file = os.path.join(project_root, "data", "gold", "aggregated_product_data.csv")
    
    circularity_errors = validate_circularity_dataset(circularity_file, "parquet")
    circularity_csv_errors = validate_circularity_dataset(circularity_csv_file, "csv")
    aggregated_errors = validate_aggregated_data(aggregated_file)
    
    all_errors = circularity_errors + circularity_csv_errors + aggregated_errors
    
    print("\n" + "*"*60)
    print("               VALIDATION REPORT SUMMARY                     ")
    print("*"*60)
    
    if not all_errors:
        print(" [PASS] All validation assertions passed successfully.")
        print(" [PASS] Data integrity and schemas are 100% clean.")
        print("*"*60 + "\n")
        sys.exit(0)
    else:
        print(f" [FAIL] Found {len(all_errors)} validation errors:")
        for error in all_errors:
            print(f"   - {error}")
        print("*"*60 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
