from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count
from utils import setup_logger
import pandas as pd

logger = setup_logger()

try:
    # Create Spark Session
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("CustomerOrderAnalytics") \
        .config("spark.hadoop.io.native.lib.available", "false") \
        .getOrCreate()

    logger.info("Spark Session Created")

    # Read CSV File
    orders_df = spark.read.csv(
        "data/raw/customer_orders.csv",
        header=True,
        inferSchema=True
    )

    logger.info("CSV Loaded Successfully")

    # Remove Null Values
    orders_df = orders_df.dropna()

    # Convert amount column
    orders_df = orders_df.withColumn(
        "amount",
        col("amount").cast("double")
    )

    # City Sales Analytics
    sales_by_city = orders_df.groupBy("city").agg(
        sum("amount").alias("total_sales"),
        avg("amount").alias("average_sales"),
        count("*").alias("total_orders")
    )

    # Product Analytics
    product_sales = orders_df.groupBy("product").agg(
        sum("amount").alias("product_sales")
    )

    # Save Reports as JSON
    sales_by_city.toPandas().to_json(
        "data/processed/city_sales_report.json",
        orient="records",
        indent=4
    )

    product_sales.toPandas().to_json(
        "data/processed/product_sales_report.json",
        orient="records",
        indent=4
    )

    print("DATA SAVED SUCCESSFULLY")

    logger.info("Reports Generated Successfully")

    spark.stop()

    logger.info("Pipeline Completed Successfully")

    print("ETL PIPELINE COMPLETED SUCCESSFULLY")

except Exception as e:
    logger.error(f"Pipeline Failed: {str(e)}")
    print(f"ERROR: {str(e)}")