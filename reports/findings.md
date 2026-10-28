# Findings and interpretation

Final portfolio report, October 27, 2026.

## Expectations versus actual evidence

| Question | Expectation | Evidence | Conclusion |
|---|---|---|---|
| Tool wear | Greater wear accompanies failure | Median 165 minutes for failures versus 107 for non-failures; overlapping distributions | Descriptive support for association; wear alone is insufficient |
| Torque and speed | Joint operating conditions help distinguish outcomes | Failure medians: 53.7 Nm and 1,365 rpm; non-failure: 39.9 Nm and 1,507 rpm | Patterns support further investigation; incremental predictive benefit was not separately tested |
| Temperature gap | Smaller process-minus-air gap with lower speed accompanies more failures | Median gap 9.3 K for failures versus 9.8 K for non-failures | Directionally consistent; the specific gap-by-speed hypothesis was not fully tested |
| Product type | Failure rates differ | L 235/6,000 = 3.92%; M 83/2,997 = 2.77%; H 21/1,003 = 2.09% | Descriptive differences, not causation or established statistical significance |
| Modeling | Operating measurements improve detection over a no-failure rule | Logistic regression caught 56/68 failures; forest caught 39/68; baseline caught none | Better detection, with different false-alarm burdens; no universal winner |

These are exploratory hypotheses, partly informed by the synthetic generation rules. No formal significance tests were performed.

## Data quality

Each row is an operating observation, not necessarily a separate machine. The file has 10,000 rows, 14 columns, no missing values and no repeated UDI identifiers. Product types are H/M/L; failure flags contain 0/1. Range checks found no negative measurements but did not establish safety limits.

There are 27 disagreements: 18 observations have RNF = 1 with overall failure = 0 and no other flags; nine have overall failure = 1 with all modes zero. Their cause is unresolved. No labels were corrected and no rows were removed; the supplied overall target was retained.

Mode counts: HDF 115, OSF 98, PWF 95, TWF 46 and RNF 19. They are not disjoint event counts because modes may overlap and may disagree with the overall target.

## Operating conditions

Exploratory groups use whole-file median cutoffs: torque 40.1 Nm and speed 1,503 rpm. High means at or above the cutoff. These are descriptive cutoffs, not safety thresholds or model features.

| Speed | Torque | Observations | Failures | Failure rate |
|---|---|---:|---:|---:|
| High | High | 626 | 1 | 0.16% |
| High | Low | 4,388 | 59 | 1.34% |
| Low | High | 4,387 | 276 | 6.29% |
| Low | Low | 599 | 3 | 0.50% |

Failure-group median air and process temperatures were 301.6 K and 310.4 K, compared with 300.0 K and 310.0 K for non-failures. Median temperature gap is calculated per row, then summarized; it need not equal the difference between two group medians.

The wear histogram shows percentages within each outcome group. Its concentration around 200-225 minutes among failures is not the probability of failure in that wear range.

## SQL and Tableau

SQL uses COUNT, SUM, AVG, GROUP BY and conditional filters to calculate totals, rates, mean operating conditions and label disagreements. SQL means and Python/Tableau medians are different statistics.

The Tableau screenshot contains totals, type rates, torque versus speed, median wear and mode counts. Its displayed aggregates match the Python reference results. It describes observed labels across the full dataset, not future risk scores or model predictions. The original workbook needs a local CSV connection; setup instructions are in the dashboard documentation.

## Modeling method

Inputs: Type, air temperature, process temperature, rotational speed, torque and wear. Identifiers, failure-mode labels, derived temperature gap and EDA operating groups are excluded.

The same stratified 80/20 split uses seed 42. Training: 7,729 non-failures and 271 failures. Test: 1,932 non-failures and 68 failures.

- Baseline always predicts zero.
- Logistic regression: training-fitted numeric standardization and one-hot type encoding, balanced weights, max_iter=1000.
- Random forest: one-hot type encoding, unscaled numerics, 200 trees, min_samples_leaf=2, balanced weights, seed 42.
- Default classifier decision rules were used. No tuning against test results was performed.

| Model | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| No-failure baseline | 96.60% | 0%* | 0% | 0% | 1932 | 0 | 68 | 0 |
| Logistic regression | 82.45% | 14.18% | 82.35% | 24.19% | 1593 | 339 | 12 | 56 |
| Random forest | 98.05% | 79.59% | 57.35% | 66.67% | 1922 | 10 | 29 | 39 |

TN: correct non-failure; FP: false alarm; FN: missed failure; TP: detected failure. Precision = TP/(TP+FP); recall = TP/(TP+FN). *Undefined baseline precision is displayed as zero.

Logistic regression raised 395 alerts, 56 correct. Forest raised 49 alerts, 39 correct. Forest generated 329 fewer false alarms but missed 17 additional failures. Without inspection costs and failure consequences, neither is an established operational winner.

## Conclusion and learning

I expected operating measurements to provide useful failure signals. They did, but the analysis did not produce a simple wear threshold or a model that detects every failure without unnecessary alerts. The main lesson was to evaluate data consistency, operating conditions and prediction errors together.

Random forest had the strongest F1 of the tested models; logistic regression caught more failures. Reporting this tradeoff is more useful than presenting the highest accuracy as proof of success. This project demonstrates a repeatable analysis method to test with plant data, not instructions for replacing equipment at a particular measurement.

## Limitations and further work

Synthetic generation rules limit real-world generalization. There is no defined prediction lead time, measured intervention benefit or remaining-useful-life estimate. Evaluation uses one split with only 68 failures, and full-data exploration occurred before splitting. This is an educational holdout rather than independent confirmatory validation. Row-order dependence and transfer to other equipment were not tested.

Cross-validation, calibrated probabilities, average precision, confidence intervals and sensitivity to label disagreements remain future work. They are not claimed deliverables.

A practical extension would collect timestamped machine histories, define inputs available before failure, select models using training folds, evaluate on later observations and test alert usefulness with maintenance engineers in a supervised pilot.
