from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Reporting") \
    .getOrCreate()

# Read Processed Report
city_df = spark.read.csv(
    "data/processed/city_sales_report",
    header=True,
    inferSchema=True
)
print("FINAL ANALYTICS REPORT")

city_df.show()

spark.stop()