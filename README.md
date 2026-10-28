# Equipment Health and Failure-Risk Analytics for Industrial Operations

A portfolio project by Sai Bhaskar Chundru connecting Mechanical Engineering and Data Analytics through Python, SQL, Tableau and machine learning.

## Question and conclusion

Which recorded operating conditions are associated with failure, and how well can simple models distinguish failure observations?

The data contained useful patterns, but no single measurement reliably separated failures from non-failures. Logistic regression caught more failures but produced many false alarms; random forest produced more precise alerts but missed more failures. The project demonstrates an investigation workflow, not a validated advance-warning system.

## Findings

- **10,000 observations; 339 failures (3.39%).** No missing values or repeated UDI identifiers were found.
- Failure rates: **L 3.92%, M 2.77%, H 2.09%**.
- Median tool wear: **165 minutes for failures versus 107 for non-failures**. Distributions overlap; these are not maintenance thresholds.
- Failure observations had higher median torque and lower median speed.
- **27 label disagreements** were documented; original labels were preserved.

## Model comparison

Same stratified 80/20 split, seed 42: 8,000 training observations and 2,000 test observations, including 68 test failures. Identifiers and mode labels were excluded; preprocessing was fitted on training data only.

| Model | Precision | Recall | F1 | Detected failures | Missed failures | False alarms |
|---|---:|---:|---:|---:|---:|---:|
| Always no failure | 0%* | 0% | 0% | 0 | 68 | 0 |
| Balanced logistic regression | 14.18% | 82.35% | 24.19% | 56 | 12 | 339 |
| Balanced random forest | 79.59% | 57.35% | 66.67% | 39 | 29 | 10 |

*Baseline precision is undefined without alerts; code displays zero by convention. Its 96.60% accuracy shows why accuracy alone is misleading. Random forest had the highest F1 here, but choosing an operational model requires costs for missed failures and unnecessary inspections.

See [findings and limitations](reports/findings.md), [SQL setup](sql/README.md) and [Tableau documentation](dashboard/README.md).

## Tableau

![Equipment health dashboard](Tableau/EQUIPMENT%20HEALTH%20%26%20FAILURE%20RISK%20ANALYTICS.png)

The [workbook](Tableau/equipment_health_failure_risk_dashboard.twb) summarizes observed outcomes, not model predictions. Reconnect it to your local CSV when opening it.

## Reproduce

Download the [UCI AI4I 2020 dataset](https://doi.org/10.24432/C5HS5C) into `data/raw/ai4i2020.csv`. From the repository root:

```powershell
python -m pip install -r requirements.txt
python notebooks/01_data_understanding.py
python notebooks/02_data_quality_checks.py
python notebooks/03_exploratory_analysis.py
python notebooks/04_baseline_models.py
```

EDA charts are saved to local `outputs/`; model results print to the terminal. Observed environment: Python 3.13.3, pandas 2.3.3, NumPy 2.4.2, matplotlib 3.10.8, scikit-learn 1.7.1. Requirements are not pinned; other versions may produce differences.

| Location | Purpose |
|---|---|
| `notebooks/` | Python checks, exploration and modeling |
| `notebooks/SQL/01_failure_analysis.sql` | MySQL business queries |
| `Tableau/` | Workbook and dashboard screenshot |
| `reports/findings.md` | Expectations, evidence, interpretation and future work |
| `data/`, `sql/`, `dashboard/` | Data dictionary, attribution and setup guidance |

## Scope

The portfolio implementation covers descriptive analysis and baseline classification. The data are synthetic and provide no defined pre-failure warning window. Full-data EDA preceded modeling; evaluation used one random split without external validation or formal hypothesis tests. No downtime reduction, cost saving or deployment readiness is claimed.

Raw data, generated outputs and private learning notes remain local and excluded from Git. Dataset: AI4I 2020 Predictive Maintenance Dataset (2020), UCI Machine Learning Repository, [DOI](https://doi.org/10.24432/C5HS5C), CC BY 4.0.
