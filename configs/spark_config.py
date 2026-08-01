import os
import sys
from pyspark.sql import SparkSession

# Set dummy HADOOP_HOME on Windows if not configured to suppress shell warnings
if sys.platform.startswith("win"):
    if not os.environ.get("HADOOP_HOME"):
        os.environ["HADOOP_HOME"] = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def create_spark_session():
    """
    Create and return a configured SparkSession for local development.
    """
    try:
        builder = (
            SparkSession.builder
            .master("local[*]")
            .appName("PySpark_Project")
            .config("spark.sql.shuffle.partitions", "8")
            .config("spark.driver.memory", "2g")
            .config("spark.executor.memory", "2g")
        )

        # Force RawLocalFileSystem on Windows to resolve missing winutils binary write crashes
        if sys.platform.startswith("win"):
            builder = builder.config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem")

        spark = builder.getOrCreate()

        # Reduce unnecessary Spark log messages
        spark.sparkContext.setLogLevel("WARN")

        return spark

    except Exception as e:
        print(f"Error creating Spark session: {e}")
        raise


if __name__ == "__main__":
    spark = create_spark_session()

    print("Spark Configuration Successful")
    print("Application Name:", spark.sparkContext.appName)
    print("Master:", spark.sparkContext.master)
    print("Spark Version:", spark.version)

    spark.stop()
    print("Spark Session Stopped Successfully")
