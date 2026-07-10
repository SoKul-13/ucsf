# Grid Search and Metric Comparison: HbA1c vs CGM Metrics

## Statistical Significance (Logistic Regression)
Evaluates if the metric is independently associated with cognitive impairment after adjusting for covariates.
| Metric | Coefficient | p-value | Significant (p<0.05)? |
|--------|-------------|---------|------------------------|
| HBA1C | 0.0542 | 0.5222 | No |
| GMI | 0.2552 | 0.0175 | **Yes** ⭐ |
| MEAN_GLUCOSE | 0.0061 | 0.0175 | **Yes** ⭐ |
| TIR | -0.0022 | 0.5786 | No |

## Machine Learning Accuracy & AUC (5-fold CV)
Evaluates the predictive power of adding the metric to the base model.
| Metric | LogReg Accuracy | LogReg AUC | RandomForest Accuracy | RandomForest AUC |
|--------|-----------------|------------|-----------------------|------------------|
| GMI | 0.6464 | 0.6639 | 0.6157 | 0.6623 |
| MEAN_GLUCOSE | 0.6464 | 0.6639 | 0.6157 | 0.6623 |
| TIR | 0.6429 | 0.6600 | 0.6258 | 0.6558 |
| HBA1C | 0.6399 | 0.6593 | 0.6251 | 0.6531 |

## Ranking and Conclusion
Ranked by Random Forest AUC (predictive performance):
1. GMI (AUC: 0.6623)
2. MEAN_GLUCOSE (AUC: 0.6623)
3. TIR (AUC: 0.6558)
4. HBA1C (AUC: 0.6531)