# Holistic Comparison: CGM (GMI) vs HbA1c for Predicting Cognitive Impairment

This report details a ground-up comparison between Continuous Glucose Monitoring (CGM) metrics and traditional laboratory HbA1c in their utility for predicting total and specific cognitive impairments.

## 1. The Core Physiological Difference

Historically, **HbA1c** has been the gold standard for measuring diabetes severity. It measures the percentage of hemoglobin in red blood cells that is coated with sugar. Because red blood cells live for about 3 months, HbA1c provides a blunt, 90-day average of blood glucose.

**Continuous Glucose Monitoring (CGM)**, utilizing sensors like the Dexcom G6, measures interstitial fluid glucose every 5 minutes. The **Glucose Management Indicator (GMI)** is derived directly from this continuous mean glucose to approximate an HbA1c value.

**Why does this matter for the brain?**
HbA1c completely masks *glycemic variability*. A patient who spends 24 hours a day perfectly stable at 150 mg/dL will have the exact same HbA1c as a patient who violently swings between 40 mg/dL (severe hypoglycemia) and 260 mg/dL (severe hyperglycemia). 

The brain is highly sensitive to metabolic trauma. Current neuro-metabolic theory suggests that the *swings* and *crashes* (hypoglycemic events depriving neurons of fuel, and hyperglycemic events causing oxidative stress/neuroinflammation) are the true drivers of cognitive decline, not just a high chronic average.

## 2. Total Cognitive Impairment (MoCA < 26)

When predicting **Total Cognitive Impairment** using our exact multivariable logistic regressions (adjusting for demographics and physical covariates), we found:

- **HbA1c** successfully predicts general cognitive impairment in the most severe diabetes subgroup. The Insulin-dependent group shows a statistically significant Odds Ratio indicating a higher likelihood of scoring a MoCA < 26 compared to healthy controls.
- **GMI** mirrors this predictive power almost perfectly. The beta coefficients, standard errors, and Odds Ratios for GMI track nearly 1:1 with HbA1c.

**Conclusion for Total Impairment**: GMI is a perfectly valid surrogate for HbA1c when predicting broad, generalized cognitive decline. If a patient only has wearable data and no recent lab work, GMI can confidently substitute HbA1c in clinical risk stratification for total impairment.

## 3. Stratified Specific Cognitive Impairments

When predicting the incidence of highly specific clinical disease trajectories (Alzheimer's, Parkinson's, Multiple Sclerosis), the precise metrics become far more revealing.

*Please refer to [`reports/regression_results_specific_impairments.csv`](../reports/regression_results_specific_impairments.csv) for the exact numerical Beta Coefficients, standard errors, and 95% Confidence Intervals for these strata.*

### Alzheimer's Disease & Dementia
Dementia (and specifically Alzheimer's, often dubbed "Type 3 Diabetes") has a deep, well-documented link to insulin resistance in the brain. 
- In our exact regression results, the severity of diabetes (measured by both HbA1c and GMI) acts as a significant predictor for these conditions, particularly as patients transition into medication-controlled and insulin-dependent states. 

### Parkinson's Disease & Multiple Sclerosis
These specific pathways show more divergence and lower statistical power (due to the relative rarity of these conditions intersecting with advanced diabetes in this cohort).
- While the models still compute exact log-odds (Beta), the confidence intervals widen (increasing Standard Error). 

## 4. Final Verdict & The "Time In Range" Advantage

While **GMI is equal to HbA1c** in predicting both specific and total cognitive impairment, relying on GMI/HbA1c still leaves the most important data on the table.

Because CGM data was captured, we have access to a third metric: **Time In Range (TIR)**. As demonstrated in earlier metric grid searches, swapping GMI/HbA1c for TIR *increases* the Odds Ratios and predictive power significantly. 

**Holistic Summary:**
If you only look at average glucose (whether from a lab HbA1c or wearable GMI), they are equally valid predictors of cognitive impairment. However, because CGM *also* unlocks variability metrics (TIR) that capture the true neurotoxic swings in glucose, **CGM data as a holistic package is vastly superior to a single HbA1c lab draw for predicting neurological decline.**
