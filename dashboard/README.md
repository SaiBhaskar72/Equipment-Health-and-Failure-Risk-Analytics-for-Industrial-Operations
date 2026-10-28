# Tableau dashboard

View the [screenshot](../Tableau/EQUIPMENT%20HEALTH%20%26%20FAILURE%20RISK%20ANALYTICS.png) or open the [workbook](../Tableau/equipment_health_failure_risk_dashboard.twb).

## Setup

The workbook was authored in Tableau 2025.2.2. Download the CSV to `data/raw/ai4i2020.csv`, open the TWB, and edit its text-file connection to select your CSV. Its original Desktop path must be reconnected after a project move or on another computer. The TWB does not package the source CSV.

## Views and calculations

| View | Calculation/design |
|---|---|
| Total observations | COUNT(UDI) = 10,000 |
| Total failures | SUM(Machine failure) = 339 |
| Overall rate | AVG(Machine failure), formatted as 3.39% |
| Rate by type | AVG(Machine failure), grouped by Type |
| Wear by outcome | MEDIAN(Tool wear), grouped by 0/1 outcome |
| Torque versus speed | Observation-level scatter colored by outcome |
| Failure-mode counts | SUM of each mode flag using Measure Names/Values |

The screenshot uses the full dataset and observed labels, not model predictions. Mode counts may overlap; median wear is not a failure threshold.

The final review inspected the screenshot and workbook XML and checked displayed aggregates against Python. It did not launch Tableau or verify every interactive action. The original dashboard was preserved without adding or claiming model integration.
