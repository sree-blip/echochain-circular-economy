from pyspark.sql import SparkSession


def create_spark_session():
    """
    Create and return a configured SparkSession for local development.
    """
    try:
        spark = (
            SparkSession.builder
            .master("local[*]")
            .appName("PySpark_Project")
            .config("spark.sql.shuffle.partitions", "8")
            .config("spark.driver.memory", "2g")
            .config("spark.executor.memory", "2g")
            .getOrCreate()
        )

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
