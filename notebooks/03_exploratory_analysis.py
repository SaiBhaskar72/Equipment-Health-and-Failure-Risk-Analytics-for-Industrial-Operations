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

    print("\nTool wear by failure outcome:")
    print(
        df.groupby("Machine failure")["Tool wear [min]"].agg(
            observations="size",
            median_wear="median",
        )
    )

    # Compare tool-wear distributions using the same ranges.
    fig, axes = plt.subplots(
        2, 1, figsize=(8, 6), sharex=True, sharey=True
    )

    bins = list(range(0, 276, 25))

    for ax, outcome, label in zip(
        axes, [0, 1], ["No failure", "Failure"]
    ):
        wear = df.loc[
            df["Machine failure"] == outcome,
            "Tool wear [min]",
        ]

        weights = [100 / len(wear)] * len(wear)

        ax.hist(
            wear,
            bins=bins,
            weights=weights,
            edgecolor="white",
        )

        ax.set_title(f"{label} — {len(wear):,} observations")
        ax.set_ylabel("Group share (%)")

    axes[-1].set_xlabel("Accumulated tool-use time (minutes)")
    fig.suptitle("Tool wear by recorded failure outcome")
    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "tool_wear_by_failure.png",
        dpi=150,
    )
    plt.close(fig)

    print("\nTorque and speed by failure outcome:")

    print(
        df.groupby("Machine failure")[
            ["Torque [Nm]", "Rotational speed [rpm]"]
        ].median()
    )

    # Compare torque and rotational speed by failure outcome.
    fig, ax = plt.subplots(figsize=(8, 6))

    for outcome, label in [(0, "No failure"), (1, "Failure")]:
        subset = df[df["Machine failure"] == outcome]

        ax.scatter(
            subset["Rotational speed [rpm]"],
            subset["Torque [Nm]"],
            label=label,
            alpha=0.5,
        )

    ax.set_title("Torque vs rotational speed by failure outcome")
    ax.set_xlabel("Rotational speed (rpm)")
    ax.set_ylabel("Torque (Nm)")
    ax.legend()

    fig.tight_layout()
    fig.savefig(
        OUTPUT_DIR / "torque_vs_speed_by_failure.png",
        dpi=150,
    )
    plt.close(fig)

    # Compare failure rates across simple torque-speed operating groups.
    median_torque = df["Torque [Nm]"].median()
    median_speed = df["Rotational speed [rpm]"].median()

    df["Torque group"] = df["Torque [Nm]"].apply(
        lambda x: "High torque" if x >= median_torque else "Low torque"
    )

    df["Speed group"] = df["Rotational speed [rpm]"].apply(
        lambda x: "High speed" if x >= median_speed else "Low speed"
    )

    operating_summary = (
        df.groupby(["Speed group", "Torque group"])["Machine failure"]
        .agg(
            observations="size",
            failures="sum",
            failure_rate="mean",
        )
    )

    operating_summary["failure_rate_percent"] = (
        operating_summary["failure_rate"] * 100
    )

    print("\nTorque-speed operating groups:")
    print(
        operating_summary[
            ["observations", "failures", "failure_rate_percent"]
        ].round(2)
    )


if __name__ == "__main__":
    main()