# Reproducing the project

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

## Other workflows

See [SQL setup](../sql/README.md), [Tableau instructions](../dashboard/README.md) and [findings and limitations](findings.md). Raw data, generated outputs and private notes stay local.
