"""Train and evaluate baseline failure classifiers."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    # Inputs: operating conditions only.
    features = [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
    ]

    X = df[features]
    y = df["Machine failure"]

    # Use 80% for training and 20% for evaluation.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("Training observations:", len(X_train))
    print("Test observations:", len(X_test))

    print("\nTraining failure counts:")
    print(y_train.value_counts().sort_index())

    print("\nTest failure counts:")
    print(y_test.value_counts().sort_index())


if __name__ == "__main__":
    main()