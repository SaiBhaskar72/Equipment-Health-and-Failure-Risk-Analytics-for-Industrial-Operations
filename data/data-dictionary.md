# Data dictionary

Source: AI4I 2020 Predictive Maintenance Dataset, UCI Machine Learning Repository. See [README.md](README.md) for attribution.

| Column | Type | Meaning | Use in this project |
| --- | --- | --- | --- |
| `UDI` | Integer | Unique record identifier | Traceability only; not a model feature |
| `Product ID` | Text | Product quality type plus serial number | Identifier; quality type is extracted from `Type` |
| `Type` | Category | Product quality variant: low, medium, or high | Operational segmentation and model feature |
| `Air temperature [K]` | Decimal | Ambient air temperature in Kelvin | Process-condition feature |
| `Process temperature [K]` | Decimal | Process temperature in Kelvin | Process-condition feature |
| `Rotational speed [rpm]` | Integer | Equipment rotational speed | Operating-condition feature |
| `Torque [Nm]` | Decimal | Applied torque in Newton-metres | Operating-condition feature |
| `Tool wear [min]` | Integer | Accumulated tool wear in minutes | Maintenance-condition feature |
| `Machine failure` | Binary | Overall failure indicator: 1 = failure, 0 = no failure | Primary classification target |
| `TWF` | Binary | Tool wear failure flag | Failure-mode analysis |
| `HDF` | Binary | Heat dissipation failure flag | Failure-mode analysis |
| `PWF` | Binary | Power failure flag | Failure-mode analysis |
| `OSF` | Binary | Overstrain failure flag | Failure-mode analysis |
| `RNF` | Binary | Random failure flag | Failure-mode analysis |

## Initial observations

- The dataset has 10,000 rows and 14 columns.
- The primary target is imbalanced: 339 records have `Machine failure = 1` (3.39%).
- Model evaluation should therefore use recall, precision, F1 score, and a confusion matrix rather than accuracy alone.
