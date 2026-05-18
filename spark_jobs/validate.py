from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Validation") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

df = pd.read_json(
    "data/processed/city_sales_report.json"
)

print("VALIDATED DATA")
print(df)

if df.empty:
    raise Exception("Validation Failed")

print("VALIDATION SUCCESSFUL")

spark.stop()