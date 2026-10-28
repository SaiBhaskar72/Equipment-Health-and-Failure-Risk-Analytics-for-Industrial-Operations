"""Compare three approaches to classifying equipment failures."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
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
    """Display results and return one row for the comparison table."""

    accuracy = accuracy_score(actual, predicted)
    precision = precision_score(actual, predicted, zero_division=0)
    recall = recall_score(actual, predicted, zero_division=0)
    f1 = f1_score(actual, predicted, zero_division=0)

    # Rows = actual outcomes; columns = predicted outcomes.
    matrix = confusion_matrix(actual, predicted, labels=[0, 1])
    tn, fp, fn, tp = matrix.ravel()

    print(f"\n{name}")
    print("-" * 45)
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Failure precision: {precision:.2%}")
    print(f"Failure recall: {recall:.2%}")
    print(f"Failure F1: {f1:.2%}")

    print("\nConfusion matrix:")
    print(matrix)

    print("Correctly identified non-failures:", tn)
    print("False alarms:", fp)
    print("Missed failures:", fn)
    print("Detected failures:", tp)

    return {
        "Model": name,
        "Accuracy (%)": accuracy * 100,
        "Precision (%)": precision * 100,
        "Recall (%)": recall * 100,
        "F1 (%)": f1 * 100,
        "Detected failures": int(tp),
        "Missed failures": int(fn),
        "False alarms": int(fp),
    }


def main():
    # ---------------------------------------------------------
    # 1. Load data and select inputs and target
    # ---------------------------------------------------------
    df = pd.read_csv(DATA_PATH)

    numeric_features = [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
    ]

    categorical_features = ["Type"]

    # Exclude identifiers and failure-mode labels from inputs.
    X = df[categorical_features + numeric_features]
    y = df["Machine failure"]

    # ---------------------------------------------------------
    # 2. Keep the same 80/20 split for all three models
    # ---------------------------------------------------------
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

    results = []

    # ---------------------------------------------------------
    # Model 1: always predict no failure
    # ---------------------------------------------------------
    baseline = DummyClassifier(
        strategy="constant",
        constant=0,
    )

    baseline.fit(X_train, y_train)

    results.append(
        evaluate_model(
            "Always no failure",
            y_test,
            baseline.predict(X_test),
        )
    )

    # ---------------------------------------------------------
    # Model 2: logistic regression
    # ---------------------------------------------------------
    # Learn scaling and category encoding from training data.
    logistic_preprocessing = ColumnTransformer(
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

    logistic_model = Pipeline(
        steps=[
            ("preprocessing", logistic_preprocessing),
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

    logistic_model.fit(X_train, y_train)

    results.append(
        evaluate_model(
            "Logistic regression",
            y_test,
            logistic_model.predict(X_test),
        )
    )

    # ---------------------------------------------------------
    # Model 3: random forest
    # ---------------------------------------------------------
    # Trees do not require numeric scaling.
    forest_preprocessing = ColumnTransformer(
        transformers=[
            (
                "numeric",
                "passthrough",
                numeric_features,
            ),
            (
                "category",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
        ]
    )

    forest_model = Pipeline(
        steps=[
            ("preprocessing", forest_preprocessing),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    min_samples_leaf=2,
                    class_weight="balanced",
                    random_state=42,
                    n_jobs=-1,
                ),
            ),
        ]
    )

    forest_model.fit(X_train, y_train)

    results.append(
        evaluate_model(
            "Random forest",
            y_test,
            forest_model.predict(X_test),
        )
    )

    # ---------------------------------------------------------
    # 3. Display the comparison
    # ---------------------------------------------------------
    comparison = pd.DataFrame(results)

    print("\nMODEL COMPARISON")
    print(comparison.round(2).to_string(index=False))

    print(
        "\nNote: precision is reported as 0 by convention "
        "when a model predicts no failures."
    )


if __name__ == "__main__":
    main()