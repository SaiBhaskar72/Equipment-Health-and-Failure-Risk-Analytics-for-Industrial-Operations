## Tableau Dashboard Results

The dashboard brings together the recorded failure outcomes and operating conditions from the full dataset. It supports exploration of the observations; it does not display machine-learning predictions or forecast future breakdowns.

![Equipment Health and Failure-Risk Dashboard](../Tableau/EQUIPMENT%20HEALTH%20%26%20FAILURE%20RISK%20ANALYTICS.png)

### Overall Failure Frequency

The dashboard reports **10,000 observations, 339 recorded failures and a 3.39% failure rate**.

Failures represent a small proportion of the dataset. This imbalance influenced the modeling stage: a high overall accuracy could conceal poor failure detection, so evaluation also considered precision, recall, F1 and confusion matrices.

### Failure Rates by Product Type

| Product type | Observations | Recorded failures | Failure rate |
|---|---:|---:|---:|
| L — Low quality variant | 6,000 | 235 | 3.92% |
| M — Medium quality variant | 2,997 | 83 | 2.77% |
| H — High quality variant | 1,003 | 21 | 2.09% |

Type L had the highest observed failure rate. Comparing rates rather than counts accounts for the unequal group sizes.

This supports a descriptive difference between product categories. It does not establish that product quality caused the failures, because operating conditions may also differ between groups.

### Torque and Rotational Speed

The scatter plot displays torque against rotational speed, with observations colored by recorded failure status.

Failure observations appear in several operating regions, including higher-torque, lower-speed conditions. Python summaries help quantify this visual pattern: failure observations had a median torque of **53.7 Nm** and median speed of **1,365 rpm**, compared with **39.9 Nm** and **1,507 rpm** for non-failure observations.

The overlap between outcomes matters. The chart suggests that operating measurements should be examined together, but it does not establish a boundary that reliably separates every failure from normal operation.

### Tool Wear by Failure Status

Median accumulated tool-use time was **165 minutes for failure observations**, compared with **107 minutes for non-failure observations**—a difference of 58 minutes.

This is consistent with greater tool wear being associated with failure in the dataset. However, the supporting Python distributions showed overlap: failures occurred at lower wear levels, and non-failures also occurred at higher wear levels.

The median is a group summary. It is not a replacement threshold, an estimate of remaining tool life or a prediction that failure occurs after 165 minutes.

### Failure-Mode Counts

| Failure-mode flag | Flagged observations |
|---|---:|
| Heat dissipation failure — HDF | 115 |
| Overstrain failure — OSF | 98 |
| Power failure — PWF | 95 |
| Tool wear failure — TWF | 46 |
| Random failure — RNF | 19 |

Heat dissipation was the most frequently flagged mode. These counts describe the supplied labels, not mutually exclusive failure events.

The counts should not be added and interpreted as unique failures: modes can overlap, and the quality checks identified 27 disagreements between the overall failure label and the combined mode flags. The original labels were retained and the uncertainty documented.

### What the Dashboard Contributes

The dashboard connects overall failure frequency with product categories, operating measurements and failure-mode labels. It makes the descriptive findings accessible and provides context for the later model comparison.

The study found useful associations, but it did not produce a single operating threshold that explains every failure. This informed the decision to evaluate several inputs together through classification models.

The dashboard's practical contribution is to demonstrate how an analyst can organize evidence and identify questions for further investigation. Applying those findings to maintenance decisions would require validation using real equipment histories and review by maintenance engineers.