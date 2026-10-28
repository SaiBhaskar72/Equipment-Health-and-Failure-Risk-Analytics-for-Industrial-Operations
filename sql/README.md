# SQL analysis

The analysis is in [01_failure_analysis.sql](../notebooks/SQL/01_failure_analysis.sql). It uses MySQL syntax and answers nine questions: record totals, outcome counts, overall rate, rates by type, mean operating conditions, mean temperatures, mode counts, disagreement count and disagreement records.

## Setup

1. Open a local MySQL connection in MySQL Workbench.
2. Create a schema named `predictive_maintenance`.
3. Import local `data/raw/ai4i2020.csv` with the Table Data Import Wizard as `equipment_data`, retaining the CSV column names. Use text for Product ID/Type, numeric decimal types for temperatures/torque, and integers for identifiers, speed, wear and failure flags.
4. Run the linked analysis script; it selects the schema using USE.

The repository contains analysis queries, not a database backup or automated loading pipeline. MySQL is a separate installation. Raw data stays local.

## Expected results

10,000 observations; 339 failures; overall rate 3.39%; 27 label disagreements. Type rates: L 3.92%, M 2.77%, H 2.09%.

SQL operating summaries use means; Python/Tableau report selected medians. Compare equivalent measures only.

The final documentation review inspected queries and Python/dashboard reference figures; it did not rerun a live MySQL server. See the [findings report](../reports/findings.md).
