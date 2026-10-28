"""Prepare a data split and evaluate a no-failure baseline."""

from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    recall_score,
)
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def main():
    # 1. Load the dataset.
    df = pd.read_csv(DATA_PATH)

    # 2. Select operating measurements as inputs.
    # Exclude identifiers and failure-mode labels.
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

    # 3. Split into 80% training and 20% test data.
    # Stratification preserves approximately the same failure rate.
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

    # 4. Create a baseline that always predicts no failure.
    baseline = DummyClassifier(
        strategy="constant",
        constant=0,
    )

    baseline.fit(X_train, y_train)
    predictions = baseline.predict(X_test)

    # 5. Evaluate the baseline on test observations.
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions, zero_division=0)

    print("\nAlways-no-failure baseline:")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Failure recall: {recall:.2%}")

    # Rows represent actual outcomes.
    # Columns represent predicted outcomes.
    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1],
    )

    print("\nConfusion matrix:")
    print(matrix)

    true_negatives, false_positives, false_negatives, true_positives = (
        matrix.ravel()
    )

    print("\nWhat the matrix means:")
    print("Correctly identified non-failures:", true_negatives)
    print("False alarms:", false_positives)
    print("Missed failures:", false_negatives)
    print("Detected failures:", true_positives)


if __name__ == "__main__":
    main()