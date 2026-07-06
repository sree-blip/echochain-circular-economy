# PySpark Setup Documentation
## Overview
   This document explains how to set up a local PySpark development environment.
## Software Requirements
Required:
- Python 3.12.10
- Java JDK 17
- PySpark 4.1.2

Recommended:
- VS Code (Visual Studio Code) 

## Installation Steps


### 1. Install Python
Download Python from:
https://www.python.org/downloads/

Verify:

In Command Prompt
```bash
python --version
```
Expected ouput:

Python 3.12.10


### 2. Install Java JDK 17
Download Java from:
https://adoptium.net/temurin/releases/?version=17

Verify:

In Command Prompt
```bash
java -version
```
Expected Output:

openjdk version "17.0.19" 2026-04-21

OpenJDK Runtime Environment Temurin-17.0.19+10 (build 17.0.19+10)

OpenJDK 64-Bit Server VM Temurin-17.0.19+10 (build 17.0.19+10, mixed mode, sharing)


```bash
javac -version
```
Expected output:

javac 17.0.19

### 3. Install Visual Studio Code (VS Code) (Recommended)

Download VS Code from: https://code.visualstudio.com/

### 4. Install PySpark
In Command Prompt
```bash
python -m pip install pyspark
```
Verify:

In Command Prompt
```
python -c "import pyspark; print(pyspark.__version__)"
```
Expected output:

4.1.2

### 5. Test PySpark Installation

1.Open VS Code.

2.Create a new file named test_pyspark.py.

3.Paste the following code:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Test") \
    .getOrCreate()

print("Spark Version:", spark.version)

spark.stop()
```

4.Save the file.

5.Open the VS Code terminal.

6.Run:

```bash
python test_pyspark.py
```

Expected Output:

Spark Version: 4.1.2


This test confirms that PySpark is installed correctly and that Spark is working properly on your system.


### Note:

- On Windows, Spark may display warnings such as "winutils.exe" or "NativeCodeLoader".

- These are expected for a local development setup and do not indicate a failed installation.


## Common Issues

### 1. python is not recognized

**Solution:** Ensure Python is installed and added to the system PATH.

### 2. Java not found

**Solution:** Ensure Java JDK 17 is installed and the `JAVA_HOME` environment variable is configured.

### 3. PySpark import error

**Solution:** Verify that PySpark is installed correctly. If the issue persists, reinstall PySpark by following the installation steps.

## References
Python: https://www.python.org/⁠�

Eclipse Temurin JDK: https://adoptium.net/⁠�

VS Code: https://code.visualstudio.com/⁠�
