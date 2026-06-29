import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("="*50)
print("Cleaning NAV History")
print("="*50)

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav = nav.drop_duplicates()

nav.to_csv(
    "data/processed/cleaned_nav_history.csv",
    index=False
)

print("NAV rows:", len(nav))


print("="*50)
print("Cleaning Investor Transactions")
print("="*50)

tx = pd.read_csv("data/raw/08_investor_transactions.csv")

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

tx["amount_inr"] = pd.to_numeric(
    tx["amount_inr"],
    errors="coerce"
)

tx = tx[tx["amount_inr"] > 0]

print("\nUnique Transaction Types:")
print(tx["transaction_type"].unique())

print("\nUnique KYC Status:")
print(tx["kyc_status"].unique())

tx.to_csv(
    "data/processed/cleaned_investor_transactions.csv",
    index=False
)

print("Transaction rows:", len(tx))


print("="*50)
print("Cleaning Scheme Performance")
print("="*50)

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(perf.columns)

perf.to_csv(
    "data/processed/cleaned_scheme_performance.csv",
    index=False
)
# Other files save to processed folder

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_csv(
    "data/processed/cleaned_fund_master.csv",
    index=False
)

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_csv(
    "data/processed/cleaned_aum_by_fund_house.csv",
    index=False
)

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
sip.to_csv(
    "data/processed/cleaned_monthly_sip_inflows.csv",
    index=False
)

category = pd.read_csv("data/raw/05_category_inflows.csv")
category.to_csv(
    "data/processed/cleaned_category_inflows.csv",
    index=False
)

folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
folio.to_csv(
    "data/processed/cleaned_industry_folio_count.csv",
    index=False
)

holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
holdings.to_csv(
    "data/processed/cleaned_portfolio_holdings.csv",
    index=False
)

benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")
benchmark.to_csv(
    "data/processed/cleaned_benchmark_indices.csv",
    index=False
)

print("Done")