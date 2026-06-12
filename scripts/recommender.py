import pandas as pd

df = pd.read_csv(
    "../data/processed/clean_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

recommend = (
    df[df["risk_grade"]==risk]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    recommend[
        ["scheme_name",
         "sharpe_ratio",
         "risk_grade"]
    ]
)


hhi = (
    holdings.groupby("amfi_code")
    ["weight_pct"]
    .apply(
        lambda x:
        ((x/100)**2).sum()
    )
)

hhi = hhi.reset_index()

hhi.columns = [
    "amfi_code",
    "HHI"
]

hhi.head()