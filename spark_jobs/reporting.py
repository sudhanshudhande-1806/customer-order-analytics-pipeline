import pandas as pd

# Read JSON report
df = pd.read_json(
    "data/processed/city_sales_report.json"
)

print("FINAL ANALYTICS REPORT")
print(df)