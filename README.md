# Predictive Maintenance Analytics for Industrial Equipment

An end-to-end portfolio project that uses operational equipment data to identify machine-failure risk and turn technical findings into practical maintenance insights.

## Why this project

This project connects my Mechanical Engineering background with data operations, SQL, Python, visualization, and machine learning. The goal is to show a complete analytics workflow rather than a model in isolation.

## Business question

How can operational data help maintenance teams identify elevated equipment-failure risk and prioritize inspection before a failure occurs?

## Planned workflow

1. Understand and clean the source data in Python.
2. Design a SQL analytics model and answer maintenance questions with SQL.
3. Explore trends and create failure-risk features in Python.
4. Train and compare baseline classification models.
5. Build a Tableau dashboard for operations and maintenance stakeholders.
6. Document findings, limitations, and recommended maintenance actions.

## Dataset

This project uses the AI4I 2020 Predictive Maintenance Dataset from the UCI Machine Learning Repository. It is a synthetic industrial dataset with 10,000 records and operational features including temperature, rotational speed, torque, tool wear, product quality type, and machine-failure labels.

The source dataset is downloaded locally and excluded from version control. See [data/README.md](data/README.md) for attribution and setup.

## Repository structure

```
data/        Dataset notes and local data folders
notebooks/   Exploration and model experiments
sql/         Relational model and analytical SQL queries
src/         Reusable Python code
dashboard/   Tableau workbook and dashboard documentation
```

## September project plan

| Stage | Outcome |
| --- | --- |
| Week 1 | Dataset understanding, data dictionary, Python exploration |
| Week 2 | SQL schema, data loading, and business analysis queries |
| Week 3 | Feature engineering and model comparison |
| Week 4 | Tableau dashboard, final findings, and portfolio documentation |

## Important note

This is an educational portfolio project based on synthetic data. It does not represent a deployed maintenance system or real operational recommendations.
