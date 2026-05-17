from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Validation") \
    .getOrCreate()

# Read Processed Data
df = spark.read.parquet(
    "data/processed/city_sales_report"
)

print("VALIDATED DATA")
df.show()

# Validation Check
if df.count() == 0:
    raise Exception("Validation Failed")

print("VALIDATION SUCCESSFUL")

spark.stop()