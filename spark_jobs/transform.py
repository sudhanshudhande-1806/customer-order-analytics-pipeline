from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count

# Create Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("CustomerOrderAnalytics") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

print("SPARK SESSION CREATED")

# Read CSV File
orders_df = spark.read.csv(
    "data/raw/customer_orders.csv",
    header=True,
    inferSchema=True
)

print("RAW DATA")
orders_df.show()

# Remove Null Values
orders_df = orders_df.dropna()

# Convert amount column
orders_df = orders_df.withColumn(
    "amount",
    col("amount").cast("double")
)

print("CLEANED DATA")
orders_df.show()

# City Sales Analytics
sales_by_city = orders_df.groupBy("city").agg(
    sum("amount").alias("total_sales"),
    avg("amount").alias("average_sales"),
    count("*").alias("total_orders")
)

print("CITY SALES REPORT")
sales_by_city.show()

# Product Analytics
product_sales = orders_df.groupBy("product").agg(
    sum("amount").alias("product_sales")
)

print("PRODUCT SALES REPORT")
product_sales.show()

# Save Processed Data
sales_by_city.write.mode("overwrite").parquet(
    "data/processed/city_sales_report"
)

product_sales.write.mode("overwrite").parquet(
    "data/processed/product_sales_report"
)

print("DATA SAVED SUCCESSFULLY")

spark.stop()

print("ETL PIPELINE COMPLETED SUCCESSFULLY")