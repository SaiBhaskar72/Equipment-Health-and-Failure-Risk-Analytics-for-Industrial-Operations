# Research Findings and Conclusions

This report explains the initial expectations, observed results and lessons from the equipment-health study. The analysis uses synthetic data and investigates associations and classification performance rather than causes of failure.

## 1. What I Expected and What the Evidence Showed

I began this study expecting operating measurements to reveal useful differences between failure and non-failure observations. The analysis supported some of these expectations, but also showed why an association does not automatically provide a reliable prediction rule.

Tool Wear

I expected greater accumulated tool-use time to be associated with failure.

Failure observations had a higher median wear value: 165 minutes compared with 107 minutes for non-failures. However, both groups contained observations at similar wear levels. This supported an association while showing that tool wear alone could not reliably distinguish the outcomes.

Torque and Rotational Speed

I expected the combination of torque and speed to reveal operating conditions associated with failure.

The exploratory low-speed, high-torque group had the highest observed failure rate. This suggested that examining measurements together was useful, but the analysis did not establish a causal relationship or separately measure how much this combination improved prediction.

Temperature Conditions

I expected a smaller difference between process and air temperature, particularly at lower rotational speed, to accompany failure.

The median temperature gap was smaller among failure observations: 9.3 K compared with 9.8 K. This was consistent with the expected direction. However, the specific interaction between temperature gap and speed was not fully tested, so the complete hypothesis remains unresolved.

Product Categories

I expected failure rates to differ across the L, M and H product categories.

The observed rates differed, with L highest, followed by M and H. This supported a descriptive difference between categories, but did not prove that product quality caused the difference. Operating conditions may also contribute.

Machine-Learning Models

I expected models using operating measurements to detect failures that an always-no-failure baseline would miss.

Both learned models did so. However, their errors revealed different priorities: logistic regression detected more failures but generated many false alarms, while random forest produced more precise alerts but missed more failures.

The result was not a model that solved every aspect of the problem. It was evidence that failure detection must be evaluated alongside the reliability and workload of its alerts.

These expectations were investigated through descriptive analysis and model evaluation, not formal statistical hypothesis tests. Some were also informed by the rules used to generate the synthetic dataset.

## 2. Data Quality and Analytical Decisions

The dataset contains **10,000 observations and 14 columns**. Each row represents an operating observation, not necessarily a separate machine.

The checks found:

- No missing values.
- No repeated UDI identifiers.
- Product categories limited to H, M and L.
- Failure-label values limited to 0 and 1.
- No negative values in the inspected operating measurements.

These checks establish basic consistency, not that every record is correct or that observed measurement ranges are safe operating limits.

### Conflicting Failure Labels

There were **27 disagreements** between the overall failure label and the combined failure-mode flags:

- **18 observations** had `RNF = 1`, but `Machine failure = 0`, with all other failure-mode flags zero.
- **9 observations** had `Machine failure = 1`, but all five failure-mode flags were zero.

The reason for these disagreements was not established. I retained the original records and consistently used the supplied `Machine failure` column as the classification target.

This was an important analytical decision: changing uncertain labels without supporting evidence would introduce an additional assumption into the study.

## 3. Operating Conditions and Recorded Failures

### Overall Failure Frequency

There were **339 recorded failures among 10,000 observations**, giving an overall failure rate of **3.39%**.

Because failures are uncommon, a model can achieve high accuracy simply by predicting non-failure. This motivated the use of precision, recall, F1 and confusion matrices alongside accuracy.

### Product Categories

| Product type | Observations | Recorded failures | Failure rate |
|---|---:|---:|---:|
| L | 6,000 | 235 | 3.92% |
| M | 2,997 | 83 | 2.77% |
| H | 1,003 | 21 | 2.09% |

Type L had the highest observed failure rate. Comparing rates accounts for the unequal category sizes, but does not account for every possible difference in operating conditions between categories.

### Tool Wear

Median accumulated tool-use time was:

- **107 minutes** for non-failure observations.
- **165 minutes** for failure observations.

The difference was **58 minutes**. However, the distributions overlapped: some failures occurred at low wear, while some non-failure observations had high wear.

The failure-group histogram showed a concentration around 200–225 minutes. This describes where failure observations were concentrated; it is not the probability of failure within that wear range.

Neither 165 minutes nor the 200–225-minute interval should be interpreted as a maintenance or replacement threshold.

### Torque and Rotational Speed

| Measurement | Non-failure median | Failure median |
|---|---:|---:|
| Torque | 39.9 Nm | 53.7 Nm |
| Rotational speed | 1,507 rpm | 1,365 rpm |

Failure observations had higher median torque and lower median speed. To explore their combination, I divided observations using the full-dataset medians: **40.1 Nm** for torque and **1,503 rpm** for speed.

“High” means at or above the relevant median; “low” means below it.

| Speed group | Torque group | Observations | Failures | Failure rate |
|---|---|---:|---:|---:|
| High | High | 626 | 1 | 0.16% |
| High | Low | 4,388 | 59 | 1.34% |
| Low | High | 4,387 | 276 | 6.29% |
| Low | Low | 599 | 3 | 0.50% |

The low-speed, high-torque group had the highest observed failure rate. These exploratory cutoffs are not engineering limits, and small failure counts in some groups make broad conclusions inappropriate.

### Temperature Conditions

| Measurement | Non-failure median | Failure median |
|---|---:|---:|
| Air temperature | 300.0 K | 301.6 K |
| Process temperature | 310.0 K | 310.4 K |
| Process-to-air temperature difference | 9.8 K | 9.3 K |

Temperature difference was calculated for each observation before taking the group median. Therefore, its median need not equal the difference between the two temperature medians.

The smaller gap among failure observations was consistent with the initial expectation. Further joint analysis with speed would be needed to investigate the complete hypothesis.

## 4. SQL and Tableau Contributions

## 4. Bringing the Findings Together Through SQL and Tableau

SQL queries were used to examine failure counts, rates by product type, average operating conditions and disagreements between failure labels. This provided another way to investigate the dataset and check selected summaries.

SQL operating comparisons use means, while selected Python and Tableau comparisons use medians. These measures describe different aspects of the data and should not be treated as interchangeable.

### Equipment Health Dashboard

The Tableau dashboard brings the descriptive analysis into one view. It connects overall failure frequency with product categories, operating conditions and failure-mode labels.

![Tableau dashboard showing equipment observations, failure frequency, torque and speed, product-type rates, median tool wear and failure-mode counts](../Tableau/EQUIPMENT%20HEALTH%20%26%20FAILURE%20RISK%20ANALYTICS.png)

*Figure 1. Equipment Health and Failure-Risk Analytics dashboard. The views summarize recorded outcomes across the full synthetic dataset; they do not show model predictions or forecast future breakdowns.*

### Reading the Dashboard

The summary measures establish how common recorded failures are. The product-type chart compares rates across categories rather than comparing raw failure counts alone.

The torque-versus-speed plot and tool-wear comparison show how operating conditions differ between outcomes. Their interpretation requires care: differences between groups do not establish a safe operating threshold or prove that a measurement caused failure.

The failure-mode chart identifies the most frequently flagged modes. Its counts may overlap and should not be added as though they represent separate failure events.

Together, these views provide context for the modeling stage. They show why several measurements may be useful while also explaining why no single chart supplies a complete failure-detection rule.

[Read the detailed chart-by-chart Tableau interpretation](tableau-results.md).

## 5. Machine-Learning Evaluation

### Inputs and Data Split

The models used six inputs:

- Product type.
- Air temperature.
- Process temperature.
- Rotational speed.
- Torque.
- Tool wear.

UDI, Product ID and failure-mode labels were excluded. Derived temperature difference and exploratory operating groups were not included in these baseline models.

All models used the same stratified 80/20 split with `random_state=42`:

| Dataset | Non-failures | Failures | Total |
|---|---:|---:|---:|
| Training | 7,729 | 271 | 8,000 |
| Test | 1,932 | 68 | 2,000 |

Preprocessing was fitted on training data only.

### Models Compared

- **Always-no-failure baseline:** predicts non-failure for every observation.
- **Logistic regression:** numeric standardization, one-hot encoding of product type, balanced class weights and `max_iter=1000`.
- **Random forest:** one-hot encoding, unscaled numeric inputs, 200 trees, `min_samples_leaf=2`, balanced class weights and seed 42.

Default classifier decision rules were used. Model settings and thresholds were not tuned against the test results.

### Performance

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Always no failure | 96.60% | 0%* | 0% | 0% |
| Logistic regression | 82.45% | 14.18% | 82.35% | 24.19% |
| Random forest | 98.05% | 79.59% | 57.35% | 66.67% |

*The baseline’s precision is undefined because it produces no failure alerts. The code reports zero by convention.*

| Model | Correct non-failures | False alarms | Missed failures | Detected failures |
|---|---:|---:|---:|---:|
| Always no failure | 1,932 | 0 | 68 | 0 |
| Logistic regression | 1,593 | 339 | 12 | 56 |
| Random forest | 1,922 | 10 | 29 | 39 |

### What the Comparison Means

The baseline achieved 96.60% accuracy while missing every test failure. It demonstrated why accuracy alone was insufficient for this problem.

Logistic regression detected **56 of 68 failures**, but produced **339 false alarms**. Of its 395 failure alerts, only 56 were correct.

Random forest detected **39 of 68 failures** and produced **10 false alarms**. Of its 49 alerts, 39 were correct.

Compared with logistic regression, random forest produced **329 fewer false alarms but missed 17 additional failures**. It had the highest F1 score in this comparison, while logistic regression had the highest recall.

The preferred model would depend on the consequences of missed failures, inspection costs and maintenance capacity. Those factors were not measured, so this study does not establish an operational winner.

## 6. What Differed From the Initial Expectations

The expectation that operating measurements would contain useful failure information was supported. However, useful associations did not translate into a simple rule that reliably identified every failure.

Higher tool wear was associated with failure, but overlap between groups prevented it from acting as a standalone threshold. Torque and speed revealed operating patterns, but the analysis did not establish that either measurement caused failure.

Both learned models improved detection over the no-failure baseline. Their results also exposed competing priorities: detecting more failures and producing more reliable alerts were not achieved equally well by the same model.

The temperature-gap result was directionally consistent with the expectation, but the complete gap-and-speed hypothesis remains unresolved. It would be inaccurate to describe every hypothesis as fully confirmed.

## 7. Overall Conclusion

This project showed how engineering questions can be investigated through data-quality checks, exploratory analysis, SQL, visualization and machine-learning evaluation.

The most important outcome was not a single prediction score. It was understanding how data consistency, overlapping operating conditions and different types of prediction error affect the conclusions we can draw.

I found evidence of associations between operating conditions and recorded failures, while also identifying limits to those relationships. The model comparison demonstrated that a classifier with more precise alerts can still miss more failures, and that high accuracy can conceal ineffective failure detection.

The project provides a documented analytical workflow that could be tested with real equipment data. It does not provide a validated maintenance threshold or a deployment-ready industrial system.

## 8. Limitations and Future Work

- **Synthetic data:** patterns may reflect generation rules and may not transfer to real equipment.
- **No defined warning period:** the study classifies recorded outcomes; it does not establish prediction hours or days before failure.
- **Limited evaluation:** results come from one split with 68 test failures. Full-data exploration preceded modeling, so this is an educational holdout rather than independent confirmatory validation.
- **Unresolved label disagreements:** the original labels were retained; their impact was not assessed through sensitivity analysis.
- **No causal or financial validation:** the study does not establish causes of failure, maintenance savings or reduced downtime.
- **Further model assessment:** cross-validation, calibrated probabilities, average precision, confidence intervals and validation of row-order dependence remain future work.

A practical extension would use timestamped equipment histories, define which measurements are available before failure, select models using training data, and evaluate on later observations. Maintenance engineers would then need to assess whether the alerts provide enough warning and are useful within real inspection capacity.