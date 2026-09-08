"""Check the dataset before exploratory analysis."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    # Check group sizes and failure rates.
    print("Product type summary:")

    type_summary = df.groupby("Type")["Machine failure"].agg(
        observations="size",
        failures="sum",
        failure_rate="mean",
    )

    type_summary["failure_rate_percent"] = (
        type_summary["failure_rate"] * 100
    )

    print(
        type_summary[
            ["observations", "failures", "failure_rate_percent"]
        ].round(2)
    )

    # Compare the overall label with the failure-mode flags.
    failure_modes = ["TWF", "HDF", "PWF", "OSF", "RNF"]

    any_mode_failure = df[failure_modes].eq(1).any(axis=1)
    overall_failure = df["Machine failure"].eq(1)

    print("\nOverall failure versus failure-mode flags:")
    print(
        pd.crosstab(
            overall_failure,
            any_mode_failure,
            rownames=["Overall failure"],
            colnames=["Any failure mode"],
        )
    )

    disagreement = overall_failure != any_mode_failure
    print("\nRecords with disagreeing labels:", disagreement.sum())

    print("\nRecords to investigate:")
    print(
        df.loc[
            disagreement,
            ["UDI", "Machine failure"] + failure_modes,
        ].to_string(index=False)
    )


    # Check whether any row identifier appears more than once.
    duplicate_ids = df["UDI"].duplicated()

    print("\nRepeated UDI values:", duplicate_ids.sum())

    print("\nProduct types present:")
    print(df["Type"].unique())

    print("\nValues present in failure-label columns:")
    for column in ["Machine failure"] + failure_modes:
        print(column, ":", df[column].unique())


        measurements = [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
    ]

    print("\nMeasurement ranges:")
    print(df[measurements].agg(["min", "max"]))

if __name__ == "__main__":
    main()