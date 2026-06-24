-- 1. Top 5 Funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3. Total Transactions
SELECT COUNT(*)
FROM fact_transactions;

-- 4. Total Investment Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 5. Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 6. SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- 7. Redemption Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='REDEMPTION';

-- 8. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 9. Average 3 Year Return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 10. Highest Return Fund
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 1;