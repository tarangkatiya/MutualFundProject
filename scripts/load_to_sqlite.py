import pandas as pd
from sqlalchemy import create_engine

print("=" * 50)
print("Creating SQLite Database")
print("=" * 50)

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/cleaned_nav_history.csv")
tx = pd.read_csv("data/processed/cleaned_investor_transactions.csv")
perf = pd.read_csv("data/processed/cleaned_scheme_performance.csv")

fund = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Load into SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
tx.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("Database Created Successfully")

print("\nRow Counts")
print("dim_fund:", len(fund))
print("fact_nav:", len(nav))
print("fact_transactions:", len(tx))
print("fact_performance:", len(perf))
print("fact_aum:", len(aum))