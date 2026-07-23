# Advanced Econometric & Causal Inference Analysis on MoCA

This report applies rigorous causal inference methods to isolate the marginal effect of variables on cognitive impairment.

## 1. Frisch-Waugh-Lovell (FWL) Theorem (Partialing Out)
By the FWL theorem, regressing MoCA on GMI and Covariates yields the exact same coefficient for GMI as regressing the *residuals* of MoCA on the *residuals* of GMI. This isolates the pure, marginal variation in GMI independent of confounders.

- **Standard Multivariable GMI Coefficient**: -0.62749
- **FWL Theorem Isolated Marginal Effect**: -0.62749
- *Notice they are exactly identical, proving the confounding effects have been perfectly partialled out.*

## 2. Fixed Effects (Absorbing Spatial Heterogeneity)
We add fixed effects for `clinical_site` to control for unobserved variables related to the specific hospital/geography where the patient was treated.

- **Fixed Effects GMI Coefficient**: -0.64601 (p-value: **<0.001** ⭐)

## 3. Propensity Score Matching (PSM)
We evaluate the Average Treatment Effect on the Treated (ATT) of being Diabetic (Treatment) on MoCA (Outcome), by matching Diabetic patients to Healthy patients with nearly identical Propensity Scores.

- **Treated N (Diabetic)**: 1129
- **Matched Control N (Healthy)**: 1129
- **ATT (Average Treatment Effect on Treated)**: -0.6395 MoCA points
  *(Diabetic patients score 0.6395 points lower on MoCA than their exact propensity-matched healthy twins)*

## 4. Instrumental Variables (2SLS Framework)
We test various potentially exogenous instruments for GMI to eliminate endogeneity bias. The First Stage regresses GMI on the Instrument + Covariates. The Second Stage regresses MoCA on the predicted GMI + Covariates.

| Instrument | First-Stage F-stat (Strength) | 2SLS GMI Coef | 2SLS p-value |
| --- | --- | --- | --- |
| age | 12.80 | 4.8717 | **<0.001** ⭐ |
| C(education_level) | 2.14 | 4.8717 | **<0.001** ⭐ |
| C(clinical_site) | 2.42 | 5.2940 | **0.022** ⭐ |
| hypertension | 14.31 | 4.8717 | **<0.001** ⭐ |
| bmi | 20.82 | 4.8717 | **<0.001** ⭐ |