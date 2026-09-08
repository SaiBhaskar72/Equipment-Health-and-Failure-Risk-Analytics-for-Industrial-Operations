"""Create basic charts for equipment failure analysis."""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def main():
    df = pd.read_csv(DATA_PATH)

    # Calculate the percentage of failures within each product type.
    failure_rates = (
        df.groupby("Type")["Machine failure"].mean() * 100
    ).reindex(["H", "M", "L"])

    # Create the chart.
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(failure_rates.index, failure_rates.values)

    ax.set_title("Observed failure rate by product type")
    ax.set_xlabel("Product type")
    ax.set_ylabel("Failure rate (%)")
    ax.set_ylim(0, failure_rates.max() + 1)

    ax.bar_label(bars, fmt="%.2f%%", padding=3)

    fig.tight_layout()

    # Save the chart in the local, Git-ignored outputs folder.
    OUTPUT_DIR.mkdir(exist_ok=True)
    chart_path = OUTPUT_DIR / "failure_rate_by_product_type.png"
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)

    print("Chart saved to:", chart_path)


if __name__ == "__main__":
    main()