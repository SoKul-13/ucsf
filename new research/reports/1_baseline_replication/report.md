# Statistical Analysis Replication: Cognitive Impairment and CGM Metrics

This report replicates the findings of the AI-READI paper using CGM metrics (GMI) instead of HbA1c.

## Table 1: Participant Characteristics

| Characteristic | 1_Controls | 2_Pre-diabetes | 3_Medication-controlled | 4_Insulin-dependent | p-value |
| --- | --- | --- | --- | --- | --- |
| N | 607 | 457 | 525 | 147 | - |
| Age (years) | 60.4 (11.7) | 60.9 (11.1) | 62.7 (10.3) | 62.1 (11.1) | **0.005** ⭐ |
| BMI | 28.0 (6.9) | 29.4 (6.9) | 30.8 (6.7) | 33.9 (8.2) | **<0.001** ⭐ |
| GMI (%) | 6.2 (0.3) | 6.3 (0.4) | 6.8 (0.6) | 7.1 (0.7) | **<0.001** ⭐ |
| Mean Glucose (mg/dL) | 119.2 (13.7) | 125.6 (17.7) | 144.2 (25.7) | 157.9 (27.7) | **<0.001** ⭐ |
| Time in Range (%) | 97.0 (4.9) | 94.7 (9.1) | 83.3 (18.4) | 71.7 (20.9) | **<0.001** ⭐ |
| Hypertension (%) | 32.3% | 46.2% | 65.3% | 70.1% | **<0.001** ⭐ |
| High Cholesterol (%) | 40.0% | 47.9% | 63.6% | 59.2% | **<0.001** ⭐ |
| Kidney Disease (%) | 4.8% | 10.5% | 12.8% | 28.6% | **<0.001** ⭐ |
| Circulatory Problems (%) | 12.5% | 11.8% | 17.1% | 30.6% | **<0.001** ⭐ |
| Neurodegenerative (%) | 10.4% | 10.1% | 16.6% | 31.3% | **<0.001** ⭐ |

## Table 2: MoCA Total and Domain Scores

| Cognitive Domain | Unadjusted Mean | p-value (Unadj) | Adjusted Mean (approx) | p-value (Adj) |
| --- | --- | --- | --- | --- |
| Total Score | 1_C: 26.1, 2_P: 25.9, 3_M: 25.4, 4_I: 24.2 | **<0.001** ⭐ | Cont: 31.6, 2_P: 31.5, 3_M: 31.3, 4_I: 30.6 | **0.019** ⭐ |
| Memory | 1_C: 12.7, 2_P: 12.7, 3_M: 12.4, 4_I: 11.9 | **0.008** ⭐ | Cont: 18.0, 2_P: 18.1, 3_M: 18.2, 4_I: 18.0 | 0.925 |
| Orientation | 1_C: 5.9, 2_P: 5.9, 3_M: 5.9, 4_I: 5.8 | 0.133 | Cont: 6.1, 2_P: 6.1, 3_M: 6.1, 4_I: 6.1 | 0.507 |
| Abstraction | 1_C: 1.9, 2_P: 1.9, 3_M: 1.9, 4_I: 1.8 | **0.001** ⭐ | Cont: 1.8, 2_P: 1.8, 3_M: 1.8, 4_I: 1.7 | 0.061 |

## Table 3: Association with Cognitive Impairment (MoCA < 26)

| Glycaemic Status | Univariable OR (95% CI) | p-value | Multivariable OR (95% CI) | p-value |
| --- | --- | --- | --- | --- |
| 2_Pre-diabetes | 1.09 (0.84 - 1.40) | 0.511 | 1.04 (0.80 - 1.36) | 0.754 |
| 3_Medication-controlled | 1.52 (1.20 - 1.93) | **<0.001** ⭐ | 1.18 (0.88 - 1.57) | 0.271 |
| 4_Insulin-dependent | 2.74 (1.90 - 3.96) | **<0.001** ⭐ | 1.63 (1.04 - 2.55) | **0.032** ⭐ |