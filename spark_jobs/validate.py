import pandas as pd

df = pd.read_json(
    "data/processed/city_sales_report.json"
)

print("VALIDATED DATA")
print(df)

if df.empty:
    raise Exception("Validation Failed")

print("VALIDATION SUCCESSFUL")