# PySpark Setup Documentation
## Overview
   This document explains how to set up a local PySpark development environment.
## Software Requirements
- Python 3.12.10
- Java JDK 17
- PySpark 4.1.2
## Installation Steps

### 1. Install Python
Download Python from:
https://www.python.org/downloads/

Verify:
```bash
python --version
```

### 2. Install Java JDK 17
Download Java from:
https://adoptium.net/temurin/releases/?version=17

Verify:
```bash
java -version
javac -version
```
Expected output:
java version "17.x.x"

### 3. Install PySpark
```bash
python -m pip install pyspark
```
## Test PySpark Installation

This test confirms that Spark is working correctly.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Test") \
    .getOrCreate()

print("Spark Version:", spark.version)

spark.stop()
```
Verify:
```
python -c "import pyspark; print(pyspark.__version__)"
```
