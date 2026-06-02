import os
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')


def summarize_raw_csv_files(raw_dir: str = RAW_DIR) -> None:
    """Read all CSV files from the raw data folder and print summary statistics."""
    if not os.path.isdir(raw_dir):
        raise FileNotFoundError(f'Raw data directory not found: {raw_dir}')

    csv_files = sorted(
        f for f in os.listdir(raw_dir) if f.lower().endswith('.csv')
    )

    if not csv_files:
        print('No CSV files found in', raw_dir)
        return

    print(f'Found {len(csv_files)} CSV file(s) in {raw_dir}')

    for csv_file in csv_files:
        file_path = os.path.join(raw_dir, csv_file)
        print('\n' + '=' * 80)
        print(f'File: {csv_file}')

        try:
            df = pd.read_csv(file_path)
        except Exception as exc:
            print(f'Failed to read {csv_file}: {exc}')
            continue

        print('Shape:', df.shape)
        print('\nDtypes:')
        print(df.dtypes)
        print('\nHead:')
        print(df.head().to_string(index=False))


if __name__ == '__main__':
    summarize_raw_csv_files()
