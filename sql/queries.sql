-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Highest Sharpe Ratio
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 4. Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Total investment amount by state
SELECT state, SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- 7. Average income by age group
SELECT age_group, AVG(annual_income_lakh)
FROM fact_transactions
GROUP BY age_group;

-- 8. Top funds by 3-year return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- 9. Risk grade distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- 10. Gender-wise investment amount
SELECT gender, SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;