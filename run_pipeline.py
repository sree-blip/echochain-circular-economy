import os
import subprocess
import sys
import time

def run_stage(stage_name, script_path):
    """
    Executes a single pipeline stage script as a subprocess.
    """
    print("=" * 60)
    print(f"RUNNING STAGE: {stage_name}")
    print(f"Script: {script_path}")
    print("=" * 60)
    
    start_time = time.time()
    
    # Run the script using the same Python interpreter
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False, # Print standard output directly to the console
        text=True
    )
    
    duration = time.time() - start_time
    
    if result.returncode == 0:
        print(f"\nSUCCESS: Stage '{stage_name}' completed in {duration:.2f} seconds.\n")
        return True, duration
    else:
        print(f"\nERROR: Stage '{stage_name}' failed with exit code {result.returncode}.\n")
        return False, duration

def main():
    print("*" * 60)
    print("         ECHOCHAIN ETL PIPELINE RUNNER        ")
    print("*" * 60)
    
    project_root = os.path.dirname(os.path.abspath(__file__))
    pyspark_dir = os.path.join(project_root, "pyspark")
    
    # Define pipeline stages in execution order
    stages = [
        ("1. Data Cleaning", os.path.join(pyspark_dir, "data_cleaning.py")),
        ("2. Data Transformation", os.path.join(pyspark_dir, "transformation.py")),
        ("3. SKU Extraction", os.path.join(pyspark_dir, "sku_extraction.py")),
        ("4. Fuzzy Matching", os.path.join(pyspark_dir, "fuzzy_matching.py")),
        ("5. Gold Layer Aggregation", os.path.join(pyspark_dir, "aggregate_listings.py"))
    ]
    
    overall_start = time.time()
    durations = {}
    
    for stage_name, script_path in stages:
        if not os.path.exists(script_path):
            print(f"Error: Script not found at {script_path}")
            sys.exit(1)
            
        success, duration = run_stage(stage_name, script_path)
        durations[stage_name] = duration
        
        if not success:
            print("Pipeline aborted due to step failure.")
            sys.exit(1)
            
    overall_duration = time.time() - overall_start
    
    print("*" * 60)
    print("            ETL PIPELINE EXECUTION SUMMARY                   ")
    print("*" * 60)
    for stage, dur in durations.items():
        print(f" - {stage:<25}: {dur:.2f} seconds")
    print("-" * 60)
    print(f"Total Pipeline Runtime     : {overall_duration:.2f} seconds")
    print("*" * 60 + "\n")

if __name__ == "__main__":
    main()
