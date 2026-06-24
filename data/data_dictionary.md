# Mutual Fund Analytics Data Dictionary

## Fund Master

amfi_code
- Type: Integer
- Description: Unique AMFI Scheme Code

fund_house
- Type: Text
- Description: Fund House Name

scheme_name
- Type: Text
- Description: Mutual Fund Scheme Name

category
- Type: Text
- Description: Fund Category

sub_category
- Type: Text
- Description: Fund Sub Category

risk_category
- Type: Text
- Description: Risk Grade

---

## NAV History

amfi_code
- Type: Integer

date
- Type: Date

nav
- Type: Decimal
- Description: Net Asset Value

---

## Investor Transactions

investor_id
transaction_date
transaction_type
amount_inr
state
city
kyc_status

Description:
Investor transaction records.

---

## Scheme Performance

return_1yr_pct
return_3yr_pct
return_5yr_pct
expense_ratio_pct

Description:
Performance metrics of mutual fund schemes.