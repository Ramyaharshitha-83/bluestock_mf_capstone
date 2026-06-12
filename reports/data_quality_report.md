# Data Quality Report

This report summarizes the raw dataset quality checks for all 10 source CSV files in `data/raw`.

Each dataset was evaluated for:
- Rows
- Columns
- Missing Values
- Duplicate Records

## Dataset Summaries

### 01_fund_master.csv
- Rows: 40
- Columns: 15
- Missing values: 0
- Duplicates: 0
- Observations: Dataset is complete with no missing values or duplicate rows.

### 02_nav_history.csv
- Rows: 46,000
- Columns: 3
- Missing values: 0
- Duplicates: 0
- Observations: NAV history is complete and contains no duplicate rows.

### 03_aum_by_fund_house.csv
- Rows: 90
- Columns: 5
- Missing values: 0
- Duplicates: 0
- Observations: AUM by fund house dataset is clean with no missing or duplicate records.

### 04_monthly_sip_inflows.csv
- Rows: 48
- Columns: 6
- Missing values: 12
- Duplicates: 0
- Observations: This dataset contains 12 missing values; review the affected rows/columns before analysis.

### 05_category_inflows.csv
- Rows: 144
- Columns: 3
- Missing values: 0
- Duplicates: 0
- Observations: Category inflows dataset is complete with no missing values or duplicate rows.

### 06_industry_folio_count.csv
- Rows: 21
- Columns: 6
- Missing values: 0
- Duplicates: 0
- Observations: Industry folio count data is complete and clean.

### 07_scheme_performance.csv
- Rows: 40
- Columns: 19
- Missing values: 0
- Duplicates: 0
- Observations: Scheme performance dataset has no missing values or duplicate records.

### 08_investor_transactions.csv
- Rows: 32,778
- Columns: 13
- Missing values: 0
- Duplicates: 0
- Observations: Investor transaction history appears clean and complete.

### 09_portfolio_holdings.csv
- Rows: 322
- Columns: 8
- Missing values: 0
- Duplicates: 0
- Observations: Portfolio holdings data is complete with no missing or duplicate records.

### 10_benchmark_indices.csv
- Rows: 8,050
- Columns: 3
- Missing values: 0
- Duplicates: 0
- Observations: Benchmark indices dataset is complete and clean.

## Overall Observations
- 9 of the 10 datasets have no missing values.
- No duplicate rows were found in any dataset.
- `04_monthly_sip_inflows.csv` is the only dataset with missing values and should be inspected further to determine whether those gaps can be filled or require handling.

- AMFI code validation passed: all `amfi_code` values in `01_fund_master.csv` were found in `02_nav_history.csv`, with no missing scheme codes detected.

#EDA of Datsets

1. Most transactions are SIPs.
2. High-risk funds show higher returns.
3. Certain states dominate investments.
4. Sharpe ratio strongly correlates with returns.
5. Top funds consistently outperform benchmarks.

## Advanced Insights

1. Funds with the highest VaR show the greatest downside risk.
2. CVaR reveals the average loss during extreme market declines.
3. Recent investor cohorts contribute the highest investment amounts.
4. Investors with SIP gaps above 35 days are more likely to discontinue investing.
5. Funds with high Sharpe ratios and low HHI provide better risk-adjusted diversification.
