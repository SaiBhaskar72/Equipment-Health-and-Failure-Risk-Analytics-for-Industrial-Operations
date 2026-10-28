# Equipment Health and Failure-Risk Analytics for Industrial Operations

**An educational research project connecting Mechanical Engineering and Data Analytics.**

## Overview

I developed this project to explore how engineering knowledge and data analytics can work together to investigate equipment health and failure patterns.

Drawing on my Mechanical Engineering background and studies in Data Analytics, I examined operating measurements such as temperature, rotational speed, torque and tool wear. The project follows an analytical workflow from data understanding and quality checks to SQL analysis, machine-learning classification and dashboard development.

My objective was to investigate the evidence rather than confirm a predetermined conclusion. The study considers both findings that support the initial hypotheses and results that reveal limitations or suggest further questions.

## Research Objective

**Which recorded operating conditions are associated with equipment failure, and how effectively can classification models distinguish failure observations from non-failure observations?**

The investigation focuses on:

- Understanding the dataset and the engineering meaning of its variables.
- Identifying data-quality issues and documenting how they are handled.
- Exploring relationships between operating conditions and failure outcomes.
- Comparing machine-learning models through their predictions and errors.
- Communicating findings clearly while distinguishing evidence from assumptions.

## Technical Approach

| Area | Tools and Methods | Application |
|---|---|---|
| Data understanding and preparation | Python, pandas | Inspect data types, missing values, identifiers, categories and label consistency |
| Exploratory analysis | pandas, Matplotlib | Compare operating conditions, distributions and failure rates |
| SQL analysis | MySQL | Answer operational questions using aggregation, grouping and conditional filtering |
| Machine learning | scikit-learn | Compare an always-no-failure baseline, logistic regression and random forest |
| Model preparation | Train/test splitting, pipelines, one-hot encoding, standardization | Prepare inputs consistently and fit preprocessing on training data |
| Model evaluation | Precision, recall, F1, accuracy and confusion matrices | Assess detected failures, missed failures and false alarms |
| Visualization | Tableau | Present equipment-health summaries through calculated measures, charts and a dashboard |
| Version control | Git, GitHub | Maintain incremental commits, development branches and pull requests |

## Project Workflow

1. **Understand the data** — define the observation, column meanings and analytical questions.
2. **Check data quality** — investigate missing values, repeated identifiers, measurement ranges and conflicting labels.
3. **Explore operating patterns** — compare failure and non-failure observations and examine the research hypotheses.
4. **Analyze with SQL** — reproduce selected summaries and answer operational questions.
5. **Build the dashboard** — communicate recorded operating conditions and failure outcomes in Tableau.
6. **Evaluate models** — compare a simple baseline with learned classifiers using the same data split.
7. **Document the study** — explain findings, unexpected outcomes, limitations and potential next steps.

Data issues are investigated before changes are made. Where the correct value cannot be established, the uncertainty is documented rather than silently corrected.

## Repository Structure

```text
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── data-dictionary.md
├── notebooks/
│   ├── 01_data_understanding.py
│   ├── 02_data_quality_checks.py
│   ├── 03_exploratory_analysis.py
│   ├── 04_baseline_models.py
│   └── SQL/
│       └── 01_failure_analysis.sql
├── sql/
│   └── README.md
├── Tableau/
│   ├── equipment_health_failure_risk_dashboard.twb
│   └── EQUIPMENT HEALTH & FAILURE RISK ANALYTICS.png
├── dashboard/
│   └── README.md
└── reports/
    └── findings.md
```

Downloaded data, generated outputs and private learning notes are maintained locally and excluded from Git.

## Getting Started

Download the dataset using the instructions in [data/README.md](data/README.md) and place `ai4i2020.csv` inside `data/raw/`.

From the repository root, install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the analysis scripts in order:

```powershell
python notebooks/01_data_understanding.py
python notebooks/02_data_quality_checks.py
python notebooks/03_exploratory_analysis.py
python notebooks/04_baseline_models.py
```

The exploratory script saves charts to the local `outputs/` folder. The modeling script prints evaluation metrics and confusion matrices.

For the other project components, follow the [SQL setup instructions](sql/README.md) and [Tableau workbook instructions](dashboard/README.md).

## Results and Documentation

The detailed results are kept separate from this overview:

- **[Findings and conclusions](reports/findings.md)** — research hypotheses, observed results, model comparisons, interpretation and limitations.
- **[Data dictionary](data/data-dictionary.md)** — variable definitions and intended roles.
- **[Dataset documentation](data/README.md)** — source attribution and local setup.
- **[SQL documentation](sql/README.md)** — analysis queries and database instructions.
- **[Tableau documentation](dashboard/README.md)** — dashboard measures, screenshot and workbook setup.

## Research Context and Limitations

This is an **educational research and portfolio project**, not a deployed industrial maintenance system.

The study uses the **AI4I 2020 Predictive Maintenance Dataset**, a **synthetic dataset** distributed through the UCI Machine Learning Repository. Its observations were generated to represent industrial operating conditions; they were not collected from a real factory for this project.

The analysis explores associations and evaluates classification models. It does not establish causal relationships, a defined warning period before breakdown, or measurable maintenance savings.

Applying the approach in industry would require validation using real equipment histories, measurements available before failure, and assessment of the resulting alerts by maintenance engineers.

## Dataset Attribution

AI4I 2020 Predictive Maintenance Dataset. UCI Machine Learning Repository.

- **Source:** [Dataset DOI](https://doi.org/10.24432/C5HS5C)
- **Dataset license:** Creative Commons Attribution 4.0 International — CC BY 4.0

## Author

**Sai Bhaskar Chundru**  
Mechanical Engineering background | Data Analytics  
[GitHub](https://github.com/SaiBhaskar72)