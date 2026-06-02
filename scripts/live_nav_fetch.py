import pandas as pd
import requests
from pathlib import Path

scheme_codes = [
    125497,  # HDFC Top 100
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

output_dir = Path("data/raw/live_nav")
output_dir.mkdir(parents=True, exist_ok=True)

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(output_dir / f"{code}.csv", index=False)

        print(f"Saved {code}.csv")
    else:
        print(f"Failed for {code}")