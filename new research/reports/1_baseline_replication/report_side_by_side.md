# Side-by-Side Comparison: CGM (GMI) vs HbA1c

This report compares multivariable models adjusting for GMI alongside models adjusting for HbA1c to predict cognitive impairment.

## Understanding This Terminology
- **Adj Mean**: Adjusted Mean. This is the estimated average MoCA score after mathematically leveling the playing field for age, BMI, education, and other medical conditions.
- **OR (Odds Ratio)**: A measure of association. An OR > 1 means higher odds of having cognitive impairment compared to the healthy control group. For example, an OR of 1.63 means 63% higher odds.
- **95% CI**: 95% Confidence Interval. We are 95% confident the true Odds Ratio falls within this range.
- **Control**: Healthy Controls (No Diabetes)
- **Pre-diab**: Pre-diabetes
- **Med-Ctrl**: Medication-controlled Diabetes
- **Insulin**: Insulin-dependent Diabetes

## Table 2: Adjusted MoCA Total and Domain Scores (GMI vs HbA1c)

| Cognitive Domain | Unadjusted Mean | Adj Mean (GMI) | p-value (GMI) | Adj Mean (HbA1c) | p-value (HbA1c) |
| --- | --- | --- | --- | --- | --- |
| Total Score | Control: 26.1, Pre-diab: 25.9, Med-Ctrl: 25.4, Insulin: 24.2 | Control: 31.6, Pre-diab: 31.5, Med-Ctrl: 31.3, Insulin: 30.6 | **0.019** ⭐ | Control: 29.3, Pre-diab: 29.2, Med-Ctrl: 28.9, Insulin: 28.0 | **<0.001** ⭐ |
| Memory | Control: 12.7, Pre-diab: 12.7, Med-Ctrl: 12.4, Insulin: 11.9 | Control: 18.0, Pre-diab: 18.1, Med-Ctrl: 18.2, Insulin: 18.0 | 0.925 | Control: 16.5, Pre-diab: 16.5, Med-Ctrl: 16.5, Insulin: 16.3 | 0.888 |
| Orientation | Control: 5.9, Pre-diab: 5.9, Med-Ctrl: 5.9, Insulin: 5.8 | Control: 6.1, Pre-diab: 6.1, Med-Ctrl: 6.1, Insulin: 6.1 | 0.507 | Control: 6.1, Pre-diab: 6.2, Med-Ctrl: 6.2, Insulin: 6.1 | 0.616 |
| Abstraction | Control: 1.9, Pre-diab: 1.9, Med-Ctrl: 1.9, Insulin: 1.8 | Control: 1.8, Pre-diab: 1.8, Med-Ctrl: 1.8, Insulin: 1.7 | 0.061 | Control: 1.9, Pre-diab: 1.9, Med-Ctrl: 1.8, Insulin: 1.8 | 0.086 |

## Table 3: Association with Cognitive Impairment (MoCA < 26) - Multivariable OR

| Glycaemic Status | OR (GMI) (95% CI) | p-value (GMI) | OR (HbA1c) (95% CI) | p-value (HbA1c) |
| --- | --- | --- | --- | --- |
| 2_Pre-diabetes | 1.04 (0.80 - 1.36) | 0.754 | 1.07 (0.82 - 1.40) | 0.617 |
| 3_Medication-controlled | 1.18 (0.88 - 1.57) | 0.271 | 1.32 (0.98 - 1.78) | 0.065 |
| 4_Insulin-dependent | 1.63 (1.04 - 2.55) | **0.032** ⭐ | 1.95 (1.24 - 3.08) | **0.004** ⭐ |