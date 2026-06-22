import pandas as pd

# Load CSV
df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("FUND MASTER ANALYSIS")
print("="*60)

# Total Records
print("\nTotal Records:", len(df))

# Unique Fund Houses
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nTotal Fund Houses:", df["fund_house"].nunique())

# Categories
print("\nCategories:")
print(df["category"].unique())

print("\nTotal Categories:", df["category"].nunique())

# Sub Categories
print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nTotal Sub Categories:", df["sub_category"].nunique())

# Risk Categories
print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nTotal Risk Categories:", df["risk_category"].nunique())