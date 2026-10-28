"""Compare a no-failure baseline with logistic regression."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def evaluate_model(name, actual, predicted):
    """Print performance and explain the prediction counts."""
    print(f"\n{name}")
    print("-" * 40)

    print(f"Accuracy: {accuracy_score(actual, predicted):.2%}")
    print(
        f"Failure precision: "
        f"{precision_score(actual, predicted, zero_division=0):.2%}"
    )
    print(
        f"Failure recall: "
        f"{recall_score(actual, predicted, zero_division=0):.2%}"
    )
    print(
        f"Failure F1: "
        f"{f1_score(actual, predicted, zero_division=0):.2%}"
    )

    matrix = confusion_matrix(actual, predicted, labels=[0, 1])
    tn, fp, fn, tp = matrix.ravel()

    print("\nConfusion matrix:")
    print(matrix)
    print("Correctly identified non-failures:", tn)
    print("False alarms:", fp)
    print("Missed failures:", fn)
    print("Detected failures:", tp)


def main():
    df = pd.read_csv(DATA_PATH)

    numeric_features = [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
    ]

    categorical_features = ["Type"]

    X = df[categorical_features + numeric_features]
    y = df["Machine failure"]

    # Keep the same split as our previous baseline.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("Training observations:", len(X_train))
    print("Test observations:", len(X_test))
    print("Training failures:", y_train.sum())
    print("Test failures:", y_test.sum())

    # Model 1: always predict no failure.
    baseline = DummyClassifier(
        strategy="constant",
        constant=0,
    )

    baseline.fit(X_train, y_train)

    evaluate_model(
        "Always-no-failure baseline",
        y_test,
        baseline.predict(X_test),
    )

    # Prepare inputs for logistic regression.
    preprocessing = ColumnTransformer(
        transformers=[
            (
                "numeric",
                StandardScaler(),
                numeric_features,
            ),
            (
                "category",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
        ]
    )

    # Keep preprocessing and the model together.
    logistic_model = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )

    # Learn preprocessing and model parameters from training data only.
    logistic_model.fit(X_train, y_train)

    evaluate_model(
        "Logistic regression — balanced class weights",
        y_test,
        logistic_model.predict(X_test),
    )


if __name__ == "__main__":
    main()