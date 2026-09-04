"""First exploration of the AI4I predictive-maintenance dataset.

Run from the project root:
python notebooks/01_data_understanding.py
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def main() -> None:
    """Load the source data and print the first data-quality checks."""
    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)
    print("\nColumn data types:\n", df.dtypes)
    print("\nMissing values by column:\n", df.isna().sum())

    failure_rate = df["Machine failure"].mean()
    print(f"\nOverall machine-failure rate: {failure_rate:.2%}")

    print("\nMachine failure counts:\n", df["Machine failure"].value_counts())
    print("\nFailure counts by mode:\n", df[["TWF", "HDF", "PWF", "OSF", "RNF"]].sum())
    print("\nFailure rate by product type:\n", df.groupby("Type")["Machine failure"].mean())


if __name__ == "__main__":
    main()
