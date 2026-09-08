# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 685; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0571**, F-statistic = **5.14** (p = **2.88e-07**), Residual SE = **4.445** on **674** df, AIC = **3998.7**, BIC = **4048.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.3977 | ±2.7953 | **+6.058** | **1.38e-09** | *** |
| Education: graduate level (vs college) | -0.3027 | 0.3685 | ±0.7371 | -0.821 | 0.4115 |  |
| Education: high school or below (vs college) | +0.4970 | 0.7603 | ±1.5206 | +0.654 | 0.5133 |  |
| Site: UCSD (vs UAB) | -0.5737 | 0.4671 | ±0.9343 | -1.228 | 0.2194 |  |
| Site: UW (vs UAB) | -0.2200 | 0.4629 | ±0.9257 | -0.475 | 0.6346 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0332 | **-5.059** | **4.21e-07** | *** |
| **BMI (kg/m2)** | **+0.0608** | 0.0282 | ±0.0563 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4795 | 0.3992 | ±0.7983 | +1.201 | 0.2296 |  |
| High cholesterol | +0.6697 | 0.3550 | ±0.7099 | +1.887 | 0.0592 | . |
| Kidney disease | +1.0134 | 0.8449 | ±1.6898 | +1.199 | 0.2303 |  |
| Circulatory disease | +0.7221 | 0.6050 | ±1.2100 | +1.194 | 0.2326 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.79e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.8277** | 3.0899 | ±6.1798 | **+2.857** | **0.0043** | ** |
| Education: graduate level (vs college) | -0.3017 | 0.3710 | ±0.7419 | -0.813 | 0.4160 |  |
| Education: high school or below (vs college) | +0.4975 | 0.7621 | ±1.5242 | +0.653 | 0.5139 |  |
| Site: UCSD (vs UAB) | -0.5737 | 0.4679 | ±0.9359 | -1.226 | 0.2202 |  |
| Site: UW (vs UAB) | -0.2191 | 0.4636 | ±0.9272 | -0.473 | 0.6365 |  |
| **Age (years)** | **-0.0839** | 0.0169 | ±0.0338 | **-4.959** | **7.09e-07** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0286 | ±0.0572 | **+2.145** | **0.0320** | * |
| Hypertension | +0.4839 | 0.4001 | ±0.8002 | +1.209 | 0.2265 |  |
| High cholesterol | +0.6743 | 0.3584 | ±0.7169 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0131 | 0.8486 | ±1.6972 | +1.194 | 0.2325 |  |
| Circulatory disease | +0.7206 | 0.6054 | ±1.2107 | +1.190 | 0.2339 |  |
| HbA1c (%) | -0.0706 | 0.5632 | ±1.1265 | -0.125 | 0.9003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0561**, F-statistic = **4.69** (p = **6.08e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.3659** | 2.2468 | ±4.4936 | **+4.168** | **3.07e-05** | *** |
| Education: graduate level (vs college) | -0.2901 | 0.3701 | ±0.7402 | -0.784 | 0.4332 |  |
| Education: high school or below (vs college) | +0.5071 | 0.7618 | ±1.5236 | +0.666 | 0.5056 |  |
| Site: UCSD (vs UAB) | -0.5830 | 0.4671 | ±0.9342 | -1.248 | 0.2120 |  |
| Site: UW (vs UAB) | -0.2037 | 0.4665 | ±0.9330 | -0.437 | 0.6624 |  |
| **Age (years)** | **-0.0837** | 0.0167 | ±0.0334 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.0623** | 0.0281 | ±0.0563 | **+2.215** | **0.0267** | * |
| Hypertension | +0.4924 | 0.4005 | ±0.8009 | +1.230 | 0.2189 |  |
| High cholesterol | +0.6687 | 0.3555 | ±0.7110 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0284 | 0.8432 | ±1.6864 | +1.220 | 0.2226 |  |
| Circulatory disease | +0.7407 | 0.6053 | ±1.2107 | +1.224 | 0.2211 |  |
| Mean glucose (mg/dL) | -0.0083 | 0.0162 | ±0.0325 | -0.510 | 0.6103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0561**, F-statistic = **4.69** (p = **6.08e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5107** | 4.2419 | ±8.4837 | **+2.478** | **0.0132** | * |
| Education: graduate level (vs college) | -0.2901 | 0.3701 | ±0.7402 | -0.784 | 0.4332 |  |
| Education: high school or below (vs college) | +0.5071 | 0.7618 | ±1.5236 | +0.666 | 0.5056 |  |
| Site: UCSD (vs UAB) | -0.5830 | 0.4671 | ±0.9342 | -1.248 | 0.2120 |  |
| Site: UW (vs UAB) | -0.2037 | 0.4665 | ±0.9330 | -0.437 | 0.6624 |  |
| **Age (years)** | **-0.0837** | 0.0167 | ±0.0334 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.0623** | 0.0281 | ±0.0563 | **+2.215** | **0.0267** | * |
| Hypertension | +0.4924 | 0.4005 | ±0.8009 | +1.230 | 0.2189 |  |
| High cholesterol | +0.6687 | 0.3555 | ±0.7110 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0284 | 0.8432 | ±1.6864 | +1.220 | 0.2226 |  |
| Circulatory disease | +0.7407 | 0.6053 | ±1.2107 | +1.224 | 0.2211 |  |
| GMI (%) | -0.3459 | 0.6787 | ±1.3574 | -0.510 | 0.6103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.75e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7343** | 2.1023 | ±4.2045 | **+4.155** | **3.26e-05** | *** |
| Education: graduate level (vs college) | -0.3001 | 0.3702 | ±0.7404 | -0.811 | 0.4175 |  |
| Education: high school or below (vs college) | +0.4995 | 0.7628 | ±1.5256 | +0.655 | 0.5126 |  |
| Site: UCSD (vs UAB) | -0.5736 | 0.4681 | ±0.9362 | -1.225 | 0.2204 |  |
| Site: UW (vs UAB) | -0.2144 | 0.4657 | ±0.9314 | -0.460 | 0.6453 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0332 | **-5.071** | **3.95e-07** | *** |
| **BMI (kg/m2)** | **+0.0619** | 0.0285 | ±0.0569 | **+2.174** | **0.0297** | * |
| Hypertension | +0.4817 | 0.3993 | ±0.7986 | +1.206 | 0.2277 |  |
| High cholesterol | +0.6721 | 0.3561 | ±0.7122 | +1.887 | 0.0591 | . |
| Kidney disease | +1.0160 | 0.8445 | ±1.6889 | +1.203 | 0.2289 |  |
| Circulatory disease | +0.7268 | 0.6062 | ±1.2123 | +1.199 | 0.2305 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0025 | 0.0149 | ±0.0298 | -0.168 | 0.8669 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.83e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5132** | 1.5724 | ±3.1449 | **+5.414** | **6.16e-08** | *** |
| Education: graduate level (vs college) | -0.3037 | 0.3687 | ±0.7374 | -0.824 | 0.4100 |  |
| Education: high school or below (vs college) | +0.4979 | 0.7612 | ±1.5225 | +0.654 | 0.5130 |  |
| Site: UCSD (vs UAB) | -0.5753 | 0.4684 | ±0.9368 | -1.228 | 0.2194 |  |
| Site: UW (vs UAB) | -0.2186 | 0.4650 | ±0.9299 | -0.470 | 0.6382 |  |
| **Age (years)** | **-0.0840** | 0.0168 | ±0.0336 | **-5.000** | **5.73e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0565 | **+2.158** | **0.0309** | * |
| Hypertension | +0.4809 | 0.4005 | ±0.8009 | +1.201 | 0.2298 |  |
| High cholesterol | +0.6699 | 0.3558 | ±0.7115 | +1.883 | 0.0597 | . |
| Kidney disease | +1.0147 | 0.8439 | ±1.6878 | +1.202 | 0.2292 |  |
| Circulatory disease | +0.7218 | 0.6054 | ±1.2107 | +1.192 | 0.2331 |  |
| Glucose SD, pooled (mg/dL) | -0.0029 | 0.0473 | ±0.0946 | -0.060 | 0.9519 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.49e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7090** | 1.5467 | ±3.0934 | **+5.631** | **1.80e-08** | *** |
| Education: graduate level (vs college) | -0.3062 | 0.3686 | ±0.7372 | -0.831 | 0.4061 |  |
| Education: high school or below (vs college) | +0.5030 | 0.7611 | ±1.5222 | +0.661 | 0.5087 |  |
| Site: UCSD (vs UAB) | -0.5845 | 0.4678 | ±0.9357 | -1.249 | 0.2116 |  |
| Site: UW (vs UAB) | -0.2123 | 0.4652 | ±0.9304 | -0.456 | 0.6481 |  |
| **Age (years)** | **-0.0835** | 0.0168 | ±0.0335 | **-4.983** | **6.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0614** | 0.0283 | ±0.0565 | **+2.172** | **0.0299** | * |
| Hypertension | +0.4864 | 0.4005 | ±0.8009 | +1.215 | 0.2245 |  |
| High cholesterol | +0.6699 | 0.3555 | ±0.7110 | +1.885 | 0.0595 | . |
| Kidney disease | +1.0232 | 0.8450 | ±1.6900 | +1.211 | 0.2259 |  |
| Circulatory disease | +0.7214 | 0.6051 | ±1.2102 | +1.192 | 0.2332 |  |
| Avg. daily SD (mg/dL) | -0.0166 | 0.0483 | ±0.0966 | -0.344 | 0.7306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.72e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2706** | 1.6603 | ±3.3207 | **+4.981** | **6.31e-07** | *** |
| Education: graduate level (vs college) | -0.2956 | 0.3692 | ±0.7385 | -0.801 | 0.4233 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7607 | ±1.5214 | +0.652 | 0.5144 |  |
| Site: UCSD (vs UAB) | -0.5693 | 0.4689 | ±0.9378 | -1.214 | 0.2247 |  |
| Site: UW (vs UAB) | -0.2217 | 0.4639 | ±0.9277 | -0.478 | 0.6326 |  |
| **Age (years)** | **-0.0844** | 0.0167 | ±0.0335 | **-5.043** | **4.59e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0564 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4766 | 0.3998 | ±0.7997 | +1.192 | 0.2333 |  |
| High cholesterol | +0.6693 | 0.3556 | ±0.7112 | +1.882 | 0.0598 | . |
| Kidney disease | +1.0112 | 0.8439 | ±1.6878 | +1.198 | 0.2308 |  |
| Circulatory disease | +0.7272 | 0.6046 | ±1.2092 | +1.203 | 0.2291 |  |
| CV (%) | +0.0129 | 0.0621 | ±0.1242 | +0.208 | 0.8356 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.76e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6388** | 1.7552 | ±3.5103 | **+4.922** | **8.57e-07** | *** |
| Education: graduate level (vs college) | -0.2967 | 0.3698 | ±0.7396 | -0.802 | 0.4224 |  |
| Education: high school or below (vs college) | +0.4955 | 0.7605 | ±1.5210 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5713 | 0.4683 | ±0.9366 | -1.220 | 0.2225 |  |
| Site: UW (vs UAB) | -0.2225 | 0.4641 | ±0.9282 | -0.479 | 0.6317 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0335 | **-5.036** | **4.76e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0564 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4769 | 0.3996 | ±0.7991 | +1.194 | 0.2327 |  |
| High cholesterol | +0.6698 | 0.3554 | ±0.7108 | +1.885 | 0.0595 | . |
| Kidney disease | +1.0115 | 0.8439 | ±1.6878 | +1.199 | 0.2307 |  |
| Circulatory disease | +0.7263 | 0.6047 | ±1.2094 | +1.201 | 0.2297 |  |
| Mean / SD ratio | -0.0256 | 0.1467 | ±0.2934 | -0.175 | 0.8615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.17e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9804** | 1.7540 | ±3.5079 | **+4.550** | **5.37e-06** | *** |
| Education: graduate level (vs college) | -0.3164 | 0.3690 | ±0.7381 | -0.857 | 0.3912 |  |
| Education: high school or below (vs college) | +0.5025 | 0.7608 | ±1.5216 | +0.660 | 0.5089 |  |
| Site: UCSD (vs UAB) | -0.5826 | 0.4678 | ±0.9356 | -1.246 | 0.2129 |  |
| Site: UW (vs UAB) | -0.2115 | 0.4645 | ±0.9290 | -0.455 | 0.6488 |  |
| **Age (years)** | **-0.0835** | 0.0167 | ±0.0334 | **-4.993** | **5.93e-07** | *** |
| **BMI (kg/m2)** | **+0.0611** | 0.0283 | ±0.0565 | **+2.163** | **0.0305** | * |
| Hypertension | +0.4828 | 0.3998 | ±0.7996 | +1.208 | 0.2272 |  |
| High cholesterol | +0.6673 | 0.3551 | ±0.7102 | +1.879 | 0.0603 | . |
| Kidney disease | +1.0221 | 0.8470 | ±1.6939 | +1.207 | 0.2275 |  |
| Circulatory disease | +0.7110 | 0.6033 | ±1.2066 | +1.178 | 0.2386 |  |
| Avg. daily mean/SD | +0.0615 | 0.1242 | ±0.2484 | +0.495 | 0.6206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.41e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0936** | 1.5453 | ±3.0906 | **+5.237** | **1.63e-07** | *** |
| Education: graduate level (vs college) | -0.3021 | 0.3689 | ±0.7378 | -0.819 | 0.4129 |  |
| Education: high school or below (vs college) | +0.4795 | 0.7676 | ±1.5352 | +0.625 | 0.5322 |  |
| Site: UCSD (vs UAB) | -0.5696 | 0.4677 | ±0.9354 | -1.218 | 0.2233 |  |
| Site: UW (vs UAB) | -0.2183 | 0.4633 | ±0.9267 | -0.471 | 0.6376 |  |
| **Age (years)** | **-0.0840** | 0.0166 | ±0.0333 | **-5.051** | **4.39e-07** | *** |
| **BMI (kg/m2)** | **+0.0610** | 0.0281 | ±0.0562 | **+2.171** | **0.0299** | * |
| Hypertension | +0.4861 | 0.3992 | ±0.7985 | +1.218 | 0.2234 |  |
| High cholesterol | +0.6715 | 0.3554 | ±0.7109 | +1.889 | 0.0589 | . |
| Kidney disease | +1.0035 | 0.8420 | ±1.6841 | +1.192 | 0.2333 |  |
| Circulatory disease | +0.7261 | 0.6068 | ±1.2135 | +1.197 | 0.2315 |  |
| MAG (mg/dL/h) | +0.0101 | 0.0244 | ±0.0487 | +0.413 | 0.6796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.56e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7471** | 1.6081 | ±3.2163 | **+5.439** | **5.35e-08** | *** |
| Education: graduate level (vs college) | -0.3022 | 0.3691 | ±0.7382 | -0.819 | 0.4129 |  |
| Education: high school or below (vs college) | +0.5061 | 0.7605 | ±1.5209 | +0.666 | 0.5057 |  |
| Site: UCSD (vs UAB) | -0.5791 | 0.4677 | ±0.9355 | -1.238 | 0.2157 |  |
| Site: UW (vs UAB) | -0.2135 | 0.4648 | ±0.9296 | -0.459 | 0.6460 |  |
| **Age (years)** | **-0.0837** | 0.0168 | ±0.0335 | **-4.995** | **5.89e-07** | *** |
| **BMI (kg/m2)** | **+0.0605** | 0.0283 | ±0.0565 | **+2.141** | **0.0323** | * |
| Hypertension | +0.4817 | 0.3998 | ±0.7996 | +1.205 | 0.2282 |  |
| High cholesterol | +0.6679 | 0.3549 | ±0.7099 | +1.882 | 0.0599 | . |
| Kidney disease | +1.0225 | 0.8441 | ±1.6881 | +1.211 | 0.2257 |  |
| Circulatory disease | +0.7241 | 0.6051 | ±1.2102 | +1.197 | 0.2314 |  |
| Avg. daily range (mg/dL) | -0.0034 | 0.0103 | ±0.0206 | -0.325 | 0.7452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.12e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2819** | 1.4109 | ±2.8218 | **+5.870** | **4.36e-09** | *** |
| Education: graduate level (vs college) | -0.3001 | 0.3688 | ±0.7376 | -0.814 | 0.4158 |  |
| Education: high school or below (vs college) | +0.4942 | 0.7625 | ±1.5250 | +0.648 | 0.5169 |  |
| Site: UCSD (vs UAB) | -0.5708 | 0.4684 | ±0.9369 | -1.218 | 0.2230 |  |
| Site: UW (vs UAB) | -0.2256 | 0.4639 | ±0.9277 | -0.486 | 0.6268 |  |
| **Age (years)** | **-0.0841** | 0.0167 | ±0.0333 | **-5.050** | **4.43e-07** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0284 | ±0.0567 | **+2.098** | **0.0359** | * |
| Hypertension | +0.4821 | 0.3996 | ±0.7991 | +1.207 | 0.2276 |  |
| High cholesterol | +0.6563 | 0.3591 | ±0.7181 | +1.828 | 0.0676 | . |
| Kidney disease | +1.0248 | 0.8493 | ±1.6987 | +1.207 | 0.2276 |  |
| Circulatory disease | +0.7196 | 0.6056 | ±1.2112 | +1.188 | 0.2347 |  |
| SD of daily means (mg/dL) | +0.0395 | 0.0743 | ±0.1486 | +0.532 | 0.5950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.50e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.7302 | 6.9089 | ±13.8177 | +1.553 | 0.1204 |  |
| Education: graduate level (vs college) | -0.3037 | 0.3691 | ±0.7382 | -0.823 | 0.4107 |  |
| Education: high school or below (vs college) | +0.4977 | 0.7611 | ±1.5223 | +0.654 | 0.5132 |  |
| Site: UCSD (vs UAB) | -0.5643 | 0.4690 | ±0.9379 | -1.203 | 0.2289 |  |
| Site: UW (vs UAB) | -0.2258 | 0.4637 | ±0.9273 | -0.487 | 0.6263 |  |
| **Age (years)** | **-0.0845** | 0.0167 | ±0.0334 | **-5.060** | **4.19e-07** | *** |
| **BMI (kg/m2)** | **+0.0605** | 0.0282 | ±0.0564 | **+2.146** | **0.0319** | * |
| Hypertension | +0.4774 | 0.4000 | ±0.7999 | +1.194 | 0.2327 |  |
| High cholesterol | +0.6630 | 0.3562 | ±0.7123 | +1.862 | 0.0627 | . |
| Kidney disease | +1.0068 | 0.8458 | ±1.6916 | +1.190 | 0.2339 |  |
| Circulatory disease | +0.7139 | 0.6066 | ±1.2131 | +1.177 | 0.2392 |  |
| Time in range 70-180, pooled (%) | -0.0227 | 0.0681 | ±0.1362 | -0.333 | 0.7389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.81e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +9.2087 | 7.1295 | ±14.2590 | +1.292 | 0.1965 |  |
| Education: graduate level (vs college) | -0.3030 | 0.3690 | ±0.7381 | -0.821 | 0.4116 |  |
| Education: high school or below (vs college) | +0.4976 | 0.7612 | ±1.5224 | +0.654 | 0.5133 |  |
| Site: UCSD (vs UAB) | -0.5706 | 0.4688 | ±0.9376 | -1.217 | 0.2235 |  |
| Site: UW (vs UAB) | -0.2216 | 0.4635 | ±0.9270 | -0.478 | 0.6326 |  |
| **Age (years)** | **-0.0842** | 0.0167 | ±0.0334 | **-5.049** | **4.44e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.154** | **0.0312** | * |
| Hypertension | +0.4791 | 0.3999 | ±0.7997 | +1.198 | 0.2309 |  |
| High cholesterol | +0.6675 | 0.3562 | ±0.7124 | +1.874 | 0.0609 | . |
| Kidney disease | +1.0110 | 0.8454 | ±1.6909 | +1.196 | 0.2318 |  |
| Circulatory disease | +0.7191 | 0.6066 | ±1.2133 | +1.185 | 0.2359 |  |
| Avg. daily time in range 70-180 (%) | -0.0074 | 0.0703 | ±0.1406 | -0.106 | 0.9158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.28e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5181** | 1.4025 | ±2.8051 | **+6.073** | **1.25e-09** | *** |
| Education: graduate level (vs college) | -0.3207 | 0.3727 | ±0.7454 | -0.860 | 0.3895 |  |
| Education: high school or below (vs college) | +0.4754 | 0.7628 | ±1.5256 | +0.623 | 0.5331 |  |
| Site: UCSD (vs UAB) | -0.5672 | 0.4667 | ±0.9335 | -1.215 | 0.2242 |  |
| Site: UW (vs UAB) | -0.2247 | 0.4630 | ±0.9260 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0333 | **-5.062** | **4.15e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4812 | 0.3999 | ±0.7997 | +1.203 | 0.2288 |  |
| High cholesterol | +0.6744 | 0.3553 | ±0.7106 | +1.898 | 0.0577 | . |
| Kidney disease | +1.0094 | 0.8476 | ±1.6952 | +1.191 | 0.2337 |  |
| Circulatory disease | +0.7118 | 0.6042 | ±1.2085 | +1.178 | 0.2388 |  |
| Time 54-69, pooled (%) | -0.1499 | 0.3294 | ±0.6588 | -0.455 | 0.6490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.37e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5082** | 1.4013 | ±2.8025 | **+6.072** | **1.26e-09** | *** |
| Education: graduate level (vs college) | -0.3196 | 0.3724 | ±0.7448 | -0.858 | 0.3907 |  |
| Education: high school or below (vs college) | +0.4762 | 0.7631 | ±1.5261 | +0.624 | 0.5326 |  |
| Site: UCSD (vs UAB) | -0.5649 | 0.4663 | ±0.9325 | -1.212 | 0.2257 |  |
| Site: UW (vs UAB) | -0.2234 | 0.4631 | ±0.9261 | -0.482 | 0.6295 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0333 | **-5.057** | **4.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4804 | 0.3998 | ±0.7996 | +1.202 | 0.2296 |  |
| High cholesterol | +0.6734 | 0.3555 | ±0.7109 | +1.894 | 0.0582 | . |
| Kidney disease | +1.0104 | 0.8471 | ±1.6942 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7106 | 0.6046 | ±1.2092 | +1.175 | 0.2399 |  |
| Avg. daily time 54-69 (%) | -0.1325 | 0.3334 | ±0.6667 | -0.398 | 0.6910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.28e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5181** | 1.4025 | ±2.8051 | **+6.073** | **1.25e-09** | *** |
| Education: graduate level (vs college) | -0.3207 | 0.3727 | ±0.7454 | -0.860 | 0.3895 |  |
| Education: high school or below (vs college) | +0.4754 | 0.7628 | ±1.5256 | +0.623 | 0.5331 |  |
| Site: UCSD (vs UAB) | -0.5672 | 0.4667 | ±0.9335 | -1.215 | 0.2242 |  |
| Site: UW (vs UAB) | -0.2247 | 0.4630 | ±0.9260 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0333 | **-5.062** | **4.15e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4812 | 0.3999 | ±0.7997 | +1.203 | 0.2288 |  |
| High cholesterol | +0.6744 | 0.3553 | ±0.7106 | +1.898 | 0.0577 | . |
| Kidney disease | +1.0094 | 0.8476 | ±1.6952 | +1.191 | 0.2337 |  |
| Circulatory disease | +0.7118 | 0.6042 | ±1.2085 | +1.178 | 0.2388 |  |
| Time < 70 (%) | -0.1499 | 0.3294 | ±0.6588 | -0.455 | 0.6490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.37e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5082** | 1.4013 | ±2.8025 | **+6.072** | **1.26e-09** | *** |
| Education: graduate level (vs college) | -0.3196 | 0.3724 | ±0.7448 | -0.858 | 0.3907 |  |
| Education: high school or below (vs college) | +0.4762 | 0.7631 | ±1.5261 | +0.624 | 0.5326 |  |
| Site: UCSD (vs UAB) | -0.5649 | 0.4663 | ±0.9325 | -1.212 | 0.2257 |  |
| Site: UW (vs UAB) | -0.2234 | 0.4631 | ±0.9261 | -0.482 | 0.6295 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0333 | **-5.057** | **4.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4804 | 0.3998 | ±0.7996 | +1.202 | 0.2296 |  |
| High cholesterol | +0.6734 | 0.3555 | ±0.7109 | +1.894 | 0.0582 | . |
| Kidney disease | +1.0104 | 0.8471 | ±1.6942 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7106 | 0.6046 | ±1.2092 | +1.175 | 0.2399 |  |
| Avg. daily time < 70 (%) | -0.1325 | 0.3334 | ±0.6667 | -0.398 | 0.6910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.32e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4686** | 1.4000 | ±2.7999 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.3073 | 0.3695 | ±0.7390 | -0.832 | 0.4057 |  |
| Education: high school or below (vs college) | +0.4939 | 0.7613 | ±1.5226 | +0.649 | 0.5165 |  |
| Site: UCSD (vs UAB) | -0.5608 | 0.4688 | ±0.9377 | -1.196 | 0.2316 |  |
| Site: UW (vs UAB) | -0.2280 | 0.4638 | ±0.9276 | -0.492 | 0.6230 |  |
| **Age (years)** | **-0.0846** | 0.0167 | ±0.0334 | **-5.066** | **4.06e-07** | *** |
| **BMI (kg/m2)** | **+0.0603** | 0.0282 | ±0.0564 | **+2.141** | **0.0322** | * |
| Hypertension | +0.4772 | 0.3999 | ±0.7998 | +1.193 | 0.2328 |  |
| High cholesterol | +0.6623 | 0.3561 | ±0.7122 | +1.860 | 0.0629 | . |
| Kidney disease | +1.0045 | 0.8464 | ±1.6928 | +1.187 | 0.2353 |  |
| Circulatory disease | +0.7100 | 0.6065 | ±1.2130 | +1.171 | 0.2417 |  |
| Time 181-250, pooled (%) | +0.0281 | 0.0674 | ±0.1349 | +0.416 | 0.6773 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.73e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4684** | 1.3992 | ±2.7985 | **+6.052** | **1.43e-09** | *** |
| Education: graduate level (vs college) | -0.3050 | 0.3695 | ±0.7389 | -0.825 | 0.4091 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7612 | ±1.5224 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5675 | 0.4687 | ±0.9374 | -1.211 | 0.2260 |  |
| Site: UW (vs UAB) | -0.2231 | 0.4637 | ±0.9274 | -0.481 | 0.6304 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0334 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.0606** | 0.0282 | ±0.0564 | **+2.149** | **0.0316** | * |
| Hypertension | +0.4789 | 0.3999 | ±0.7997 | +1.198 | 0.2311 |  |
| High cholesterol | +0.6662 | 0.3561 | ±0.7123 | +1.871 | 0.0614 | . |
| Kidney disease | +1.0089 | 0.8459 | ±1.6918 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7157 | 0.6068 | ±1.2135 | +1.179 | 0.2382 |  |
| Avg. daily time 181-250 (%) | +0.0129 | 0.0698 | ±0.1396 | +0.185 | 0.8532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.32e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4686** | 1.4000 | ±2.7999 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.3073 | 0.3695 | ±0.7390 | -0.832 | 0.4057 |  |
| Education: high school or below (vs college) | +0.4939 | 0.7613 | ±1.5226 | +0.649 | 0.5165 |  |
| Site: UCSD (vs UAB) | -0.5608 | 0.4688 | ±0.9377 | -1.196 | 0.2316 |  |
| Site: UW (vs UAB) | -0.2280 | 0.4638 | ±0.9276 | -0.492 | 0.6230 |  |
| **Age (years)** | **-0.0846** | 0.0167 | ±0.0334 | **-5.066** | **4.06e-07** | *** |
| **BMI (kg/m2)** | **+0.0603** | 0.0282 | ±0.0564 | **+2.141** | **0.0322** | * |
| Hypertension | +0.4772 | 0.3999 | ±0.7998 | +1.193 | 0.2328 |  |
| High cholesterol | +0.6623 | 0.3561 | ±0.7122 | +1.860 | 0.0629 | . |
| Kidney disease | +1.0045 | 0.8464 | ±1.6928 | +1.187 | 0.2353 |  |
| Circulatory disease | +0.7100 | 0.6065 | ±1.2130 | +1.171 | 0.2417 |  |
| Time > 180 (%) | +0.0281 | 0.0674 | ±0.1349 | +0.416 | 0.6773 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.73e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4684** | 1.3992 | ±2.7985 | **+6.052** | **1.43e-09** | *** |
| Education: graduate level (vs college) | -0.3050 | 0.3695 | ±0.7389 | -0.825 | 0.4091 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7612 | ±1.5224 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5675 | 0.4687 | ±0.9374 | -1.211 | 0.2260 |  |
| Site: UW (vs UAB) | -0.2231 | 0.4637 | ±0.9274 | -0.481 | 0.6304 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0334 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.0606** | 0.0282 | ±0.0564 | **+2.149** | **0.0316** | * |
| Hypertension | +0.4789 | 0.3999 | ±0.7997 | +1.198 | 0.2311 |  |
| High cholesterol | +0.6662 | 0.3561 | ±0.7123 | +1.871 | 0.0614 | . |
| Kidney disease | +1.0089 | 0.8459 | ±1.6918 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7157 | 0.6068 | ±1.2135 | +1.179 | 0.2382 |  |
| Avg. daily time > 180 (%) | +0.0129 | 0.0698 | ±0.1396 | +0.185 | 0.8532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0776**, Adj R² = **0.0626**, F-statistic = **5.15** (p = **8.59e-08**), Residual SE = **4.432** on **673** df, AIC = **3995.7**, BIC = **4050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5202** | 1.3918 | ±2.7836 | **+6.122** | **9.25e-10** | *** |
| Education: graduate level (vs college) | -0.2940 | 0.3678 | ±0.7356 | -0.799 | 0.4240 |  |
| Education: high school or below (vs college) | +0.4547 | 0.7618 | ±1.5236 | +0.597 | 0.5506 |  |
| Site: UCSD (vs UAB) | -0.5404 | 0.4681 | ±0.9362 | -1.154 | 0.2484 |  |
| Site: UW (vs UAB) | -0.2518 | 0.4624 | ±0.9247 | -0.545 | 0.5861 |  |
| **Age (years)** | **-0.0830** | 0.0167 | ±0.0334 | **-4.971** | **6.67e-07** | *** |
| BMI (kg/m2) | +0.0535 | 0.0279 | ±0.0557 | +1.920 | 0.0548 | . |
| Hypertension | +0.5028 | 0.3993 | ±0.7986 | +1.259 | 0.2080 |  |
| High cholesterol | +0.5881 | 0.3585 | ±0.7170 | +1.641 | 0.1009 |  |
| Kidney disease | +1.0234 | 0.8509 | ±1.7017 | +1.203 | 0.2291 |  |
| Circulatory disease | +0.7236 | 0.6008 | ±1.2015 | +1.204 | 0.2284 |  |
| **Nocturnal time > 180 (%)** | **+0.1253** | 0.0581 | ±0.1162 | **+2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 685; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **2.24e-06**), AUC = **0.6867**, AIC = **563.9**, BIC = **613.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0301 | 0.8467 | ±1.6934 | -0.036 | 0.9717 | 0.9704 |  |
| Education: graduate level (vs college) | -0.0419 | 0.2445 | ±0.4890 | -0.171 | 0.8639 | 0.9590 |  |
| Education: high school or below (vs college) | +0.3546 | 0.3670 | ±0.7339 | +0.966 | 0.3339 | 1.4256 |  |
| Site: UCSD (vs UAB) | -0.1112 | 0.3035 | ±0.6070 | -0.366 | 0.7141 | 0.8948 |  |
| Site: UW (vs UAB) | +0.1099 | 0.2842 | ±0.5683 | +0.387 | 0.6989 | 1.1162 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.124** | **0.0337** | 1.0330 | * |
| Hypertension | +0.2834 | 0.2488 | ±0.4975 | +1.139 | 0.2546 | 1.3277 |  |
| **High cholesterol** | **+0.5988** | 0.2327 | ±0.4654 | **+2.573** | **0.0101** | 1.8199 | * |
| Kidney disease | +0.6240 | 0.3920 | ±0.7841 | +1.592 | 0.1114 | 1.8664 |  |
| Circulatory disease | +0.4209 | 0.3481 | ±0.6961 | +1.209 | 0.2265 | 1.5234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **4.98e-06**), AUC = **0.6864**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1923 | 1.9544 | ±3.9088 | -0.098 | 0.9216 | 0.8250 |  |
| Education: graduate level (vs college) | -0.0415 | 0.2445 | ±0.4891 | -0.170 | 0.8653 | 0.9594 |  |
| Education: high school or below (vs college) | +0.3554 | 0.3670 | ±0.7341 | +0.968 | 0.3329 | 1.4268 |  |
| Site: UCSD (vs UAB) | -0.1104 | 0.3037 | ±0.6074 | -0.364 | 0.7162 | 0.8955 |  |
| Site: UW (vs UAB) | +0.1094 | 0.2843 | ±0.5685 | +0.385 | 0.7003 | 1.1156 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0222 | **-4.860** | **1.17e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0155 | ±0.0310 | **+2.085** | **0.0370** | 1.0328 | * |
| Hypertension | +0.2808 | 0.2504 | ±0.5007 | +1.122 | 0.2621 | 1.3242 |  |
| **High cholesterol** | **+0.5967** | 0.2338 | ±0.4676 | **+2.552** | **0.0107** | 1.8161 | * |
| Kidney disease | +0.6231 | 0.3921 | ±0.7843 | +1.589 | 0.1120 | 1.8648 |  |
| Circulatory disease | +0.4226 | 0.3485 | ±0.6969 | +1.213 | 0.2253 | 1.5259 |  |
| HbA1c (%) | +0.0314 | 0.3412 | ±0.6825 | +0.092 | 0.9266 | 1.0319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0770**, LLR χ² = **45.20** (p = **4.48e-06**), AUC = **0.6873**, AIC = **565.7**, BIC = **620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5885 | 1.3637 | ±2.7274 | -0.432 | 0.6660 | 0.5551 |  |
| Education: graduate level (vs college) | -0.0485 | 0.2450 | ±0.4901 | -0.198 | 0.8432 | 0.9527 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3668 | ±0.7335 | +0.954 | 0.3401 | 1.4189 |  |
| Site: UCSD (vs UAB) | -0.1045 | 0.3039 | ±0.6077 | -0.344 | 0.7310 | 0.9008 |  |
| Site: UW (vs UAB) | +0.0990 | 0.2849 | ±0.5697 | +0.348 | 0.7281 | 1.1041 |  |
| **Age (years)** | **-0.0541** | 0.0111 | ±0.0221 | **-4.891** | **1.01e-06** | 0.9473 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0154 | ±0.0309 | **+2.047** | **0.0407** | 1.0321 | * |
| Hypertension | +0.2785 | 0.2490 | ±0.4979 | +1.119 | 0.2632 | 1.3212 |  |
| **High cholesterol** | **+0.5952** | 0.2328 | ±0.4656 | **+2.557** | **0.0106** | 1.8134 | * |
| Kidney disease | +0.6094 | 0.3933 | ±0.7866 | +1.550 | 0.1213 | 1.8394 |  |
| Circulatory disease | +0.4113 | 0.3486 | ±0.6971 | +1.180 | 0.2380 | 1.5087 |  |
| Mean glucose (mg/dL) | +0.0051 | 0.0098 | ±0.0195 | +0.523 | 0.6009 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0770**, LLR χ² = **45.20** (p = **4.48e-06**), AUC = **0.6873**, AIC = **565.7**, BIC = **620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2960 | 2.5648 | ±5.1297 | -0.505 | 0.6133 | 0.2736 |  |
| Education: graduate level (vs college) | -0.0485 | 0.2450 | ±0.4901 | -0.198 | 0.8432 | 0.9527 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3668 | ±0.7335 | +0.954 | 0.3401 | 1.4189 |  |
| Site: UCSD (vs UAB) | -0.1045 | 0.3039 | ±0.6077 | -0.344 | 0.7310 | 0.9008 |  |
| Site: UW (vs UAB) | +0.0990 | 0.2849 | ±0.5697 | +0.348 | 0.7281 | 1.1041 |  |
| **Age (years)** | **-0.0541** | 0.0111 | ±0.0221 | **-4.891** | **1.01e-06** | 0.9473 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0154 | ±0.0309 | **+2.047** | **0.0407** | 1.0321 | * |
| Hypertension | +0.2785 | 0.2490 | ±0.4979 | +1.119 | 0.2632 | 1.3212 |  |
| **High cholesterol** | **+0.5952** | 0.2328 | ±0.4656 | **+2.557** | **0.0106** | 1.8134 | * |
| Kidney disease | +0.6094 | 0.3933 | ±0.7866 | +1.550 | 0.1213 | 1.8394 |  |
| Circulatory disease | +0.4113 | 0.3486 | ±0.6971 | +1.180 | 0.2380 | 1.5087 |  |
| GMI (%) | +0.2137 | 0.4086 | ±0.8172 | +0.523 | 0.6009 | 1.2383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0809**, LLR χ² = **47.48** (p = **1.77e-06**), AUC = **0.6930**, AIC = **563.4**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5266 | 1.2633 | ±2.5267 | -1.208 | 0.2269 | 0.2173 |  |
| Education: graduate level (vs college) | -0.0516 | 0.2455 | ±0.4910 | -0.210 | 0.8336 | 0.9497 |  |
| Education: high school or below (vs college) | +0.3460 | 0.3672 | ±0.7344 | +0.942 | 0.3460 | 1.4134 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3040 | ±0.6081 | -0.374 | 0.7087 | 0.8926 |  |
| Site: UW (vs UAB) | +0.0733 | 0.2852 | ±0.5704 | +0.257 | 0.7971 | 1.0761 |  |
| **Age (years)** | **-0.0533** | 0.0111 | ±0.0221 | **-4.816** | **1.47e-06** | 0.9481 | *** |
| BMI (kg/m2) | +0.0276 | 0.0160 | ±0.0319 | +1.731 | 0.0835 | 1.0280 | . |
| Hypertension | +0.2728 | 0.2489 | ±0.4979 | +1.096 | 0.2732 | 1.3136 |  |
| **High cholesterol** | **+0.5788** | 0.2334 | ±0.4668 | **+2.480** | **0.0131** | 1.7839 | * |
| Kidney disease | +0.6062 | 0.3934 | ±0.7867 | +1.541 | 0.1233 | 1.8335 |  |
| Circulatory disease | +0.4030 | 0.3484 | ±0.6969 | +1.157 | 0.2474 | 1.4964 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0137 | 0.0085 | ±0.0170 | +1.609 | 0.1076 | 1.0138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **4.99e-06**), AUC = **0.6868**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0691 | 0.9846 | ±1.9692 | -0.070 | 0.9440 | 0.9332 |  |
| Education: graduate level (vs college) | -0.0411 | 0.2447 | ±0.4895 | -0.168 | 0.8667 | 0.9597 |  |
| Education: high school or below (vs college) | +0.3539 | 0.3671 | ±0.7341 | +0.964 | 0.3350 | 1.4246 |  |
| Site: UCSD (vs UAB) | -0.1090 | 0.3049 | ±0.6097 | -0.358 | 0.7207 | 0.8967 |  |
| Site: UW (vs UAB) | +0.1097 | 0.2842 | ±0.5684 | +0.386 | 0.6994 | 1.1160 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0222 | **-4.859** | **1.18e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.120** | **0.0340** | 1.0330 | * |
| Hypertension | +0.2822 | 0.2493 | ±0.4986 | +1.132 | 0.2576 | 1.3260 |  |
| **High cholesterol** | **+0.5986** | 0.2327 | ±0.4655 | **+2.572** | **0.0101** | 1.8195 | * |
| Kidney disease | +0.6230 | 0.3922 | ±0.7845 | +1.588 | 0.1122 | 1.8645 |  |
| Circulatory disease | +0.4219 | 0.3482 | ±0.6965 | +1.211 | 0.2257 | 1.5248 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0297 | ±0.0594 | +0.078 | 0.9380 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **5.00e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0271 | 0.9616 | ±1.9233 | -0.028 | 0.9775 | 0.9732 |  |
| Education: graduate level (vs college) | -0.0419 | 0.2446 | ±0.4892 | -0.171 | 0.8639 | 0.9589 |  |
| Education: high school or below (vs college) | +0.3547 | 0.3671 | ±0.7342 | +0.966 | 0.3339 | 1.4257 |  |
| Site: UCSD (vs UAB) | -0.1114 | 0.3049 | ±0.6097 | -0.365 | 0.7148 | 0.8946 |  |
| Site: UW (vs UAB) | +0.1100 | 0.2842 | ±0.5684 | +0.387 | 0.6988 | 1.1162 |  |
| **Age (years)** | **-0.0538** | 0.0111 | ±0.0222 | **-4.849** | **1.24e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.122** | **0.0338** | 1.0330 | * |
| Hypertension | +0.2835 | 0.2492 | ±0.4984 | +1.138 | 0.2552 | 1.3278 |  |
| **High cholesterol** | **+0.5988** | 0.2327 | ±0.4654 | **+2.573** | **0.0101** | 1.8199 | * |
| Kidney disease | +0.6241 | 0.3926 | ±0.7851 | +1.590 | 0.1118 | 1.8666 |  |
| Circulatory disease | +0.4209 | 0.3482 | ±0.6964 | +1.209 | 0.2268 | 1.5233 |  |
| Avg. daily SD (mg/dL) | -0.0002 | 0.0303 | ±0.0606 | -0.006 | 0.9949 | 0.9998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.92e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0962 | 1.0594 | ±2.1188 | +0.091 | 0.9276 | 1.1010 |  |
| Education: graduate level (vs college) | -0.0459 | 0.2453 | ±0.4906 | -0.187 | 0.8516 | 0.9551 |  |
| Education: high school or below (vs college) | +0.3556 | 0.3670 | ±0.7341 | +0.969 | 0.3326 | 1.4271 |  |
| Site: UCSD (vs UAB) | -0.1164 | 0.3045 | ±0.6090 | -0.382 | 0.7023 | 0.8901 |  |
| Site: UW (vs UAB) | +0.1081 | 0.2842 | ±0.5684 | +0.380 | 0.7037 | 1.1142 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.843** | **1.28e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.118** | **0.0342** | 1.0330 | * |
| Hypertension | +0.2863 | 0.2492 | ±0.4983 | +1.149 | 0.2506 | 1.3314 |  |
| **High cholesterol** | **+0.5983** | 0.2327 | ±0.4655 | **+2.571** | **0.0101** | 1.8191 | * |
| Kidney disease | +0.6243 | 0.3921 | ±0.7843 | +1.592 | 0.1114 | 1.8669 |  |
| Circulatory disease | +0.4164 | 0.3488 | ±0.6977 | +1.194 | 0.2326 | 1.5165 |  |
| CV (%) | -0.0081 | 0.0407 | ±0.0815 | -0.198 | 0.8427 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6864**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1577 | 1.0692 | ±2.1383 | -0.147 | 0.8827 | 0.8541 |  |
| Education: graduate level (vs college) | -0.0461 | 0.2454 | ±0.4909 | -0.188 | 0.8509 | 0.9549 |  |
| Education: high school or below (vs college) | +0.3562 | 0.3671 | ±0.7341 | +0.971 | 0.3318 | 1.4280 |  |
| Site: UCSD (vs UAB) | -0.1147 | 0.3039 | ±0.6079 | -0.377 | 0.7059 | 0.8916 |  |
| Site: UW (vs UAB) | +0.1093 | 0.2841 | ±0.5682 | +0.385 | 0.7006 | 1.1154 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.848** | **1.25e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.118** | **0.0342** | 1.0330 | * |
| Hypertension | +0.2863 | 0.2492 | ±0.4984 | +1.149 | 0.2506 | 1.3315 |  |
| **High cholesterol** | **+0.5980** | 0.2328 | ±0.4655 | **+2.569** | **0.0102** | 1.8184 | * |
| Kidney disease | +0.6245 | 0.3921 | ±0.7842 | +1.593 | 0.1112 | 1.8673 |  |
| Circulatory disease | +0.4166 | 0.3488 | ±0.6976 | +1.194 | 0.2324 | 1.5167 |  |
| Mean / SD ratio | +0.0194 | 0.0993 | ±0.1986 | +0.196 | 0.8449 | 1.0196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0769**, LLR χ² = **45.10** (p = **4.65e-06**), AUC = **0.6866**, AIC = **565.8**, BIC = **620.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2953 | 1.0541 | ±2.1083 | -0.280 | 0.7794 | 0.7443 |  |
| Education: graduate level (vs college) | -0.0495 | 0.2452 | ±0.4904 | -0.202 | 0.8400 | 0.9517 |  |
| Education: high school or below (vs college) | +0.3580 | 0.3671 | ±0.7342 | +0.975 | 0.3294 | 1.4305 |  |
| Site: UCSD (vs UAB) | -0.1181 | 0.3038 | ±0.6076 | -0.389 | 0.6975 | 0.8886 |  |
| Site: UW (vs UAB) | +0.1102 | 0.2841 | ±0.5682 | +0.388 | 0.6981 | 1.1165 |  |
| **Age (years)** | **-0.0535** | 0.0111 | ±0.0222 | **-4.820** | **1.44e-06** | 0.9480 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.130** | **0.0331** | 1.0331 | * |
| Hypertension | +0.2865 | 0.2489 | ±0.4977 | +1.151 | 0.2497 | 1.3317 |  |
| **High cholesterol** | **+0.5948** | 0.2329 | ±0.4657 | **+2.554** | **0.0106** | 1.8127 | * |
| Kidney disease | +0.6276 | 0.3922 | ±0.7843 | +1.600 | 0.1095 | 1.8732 |  |
| Circulatory disease | +0.4116 | 0.3489 | ±0.6979 | +1.180 | 0.2381 | 1.5093 |  |
| Avg. daily mean/SD | +0.0338 | 0.0800 | ±0.1601 | +0.423 | 0.6725 | 1.0344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0767**, LLR χ² = **45.04** (p = **4.78e-06**), AUC = **0.6872**, AIC = **565.8**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2313 | 1.0375 | ±2.0750 | -0.223 | 0.8236 | 0.7935 |  |
| Education: graduate level (vs college) | -0.0395 | 0.2446 | ±0.4893 | -0.161 | 0.8718 | 0.9613 |  |
| Education: high school or below (vs college) | +0.3458 | 0.3681 | ±0.7361 | +0.939 | 0.3475 | 1.4131 |  |
| Site: UCSD (vs UAB) | -0.1091 | 0.3037 | ±0.6073 | -0.359 | 0.7195 | 0.8967 |  |
| Site: UW (vs UAB) | +0.1103 | 0.2841 | ±0.5682 | +0.388 | 0.6979 | 1.1166 |  |
| **Age (years)** | **-0.0538** | 0.0111 | ±0.0221 | **-4.872** | **1.11e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2868 | 0.2490 | ±0.4979 | +1.152 | 0.2494 | 1.3321 |  |
| **High cholesterol** | **+0.6012** | 0.2330 | ±0.4660 | **+2.581** | **0.0099** | 1.8244 | ** |
| Kidney disease | +0.6189 | 0.3924 | ±0.7848 | +1.577 | 0.1147 | 1.8569 |  |
| Circulatory disease | +0.4246 | 0.3482 | ±0.6964 | +1.219 | 0.2227 | 1.5290 |  |
| MAG (mg/dL/h) | +0.0054 | 0.0160 | ±0.0321 | +0.337 | 0.7363 | 1.0054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.95** (p = **4.95e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0630 | 1.0259 | ±2.0518 | +0.061 | 0.9511 | 1.0650 |  |
| Education: graduate level (vs college) | -0.0418 | 0.2445 | ±0.4889 | -0.171 | 0.8643 | 0.9591 |  |
| Education: high school or below (vs college) | +0.3577 | 0.3676 | ±0.7351 | +0.973 | 0.3304 | 1.4301 |  |
| Site: UCSD (vs UAB) | -0.1144 | 0.3041 | ±0.6082 | -0.376 | 0.7068 | 0.8919 |  |
| Site: UW (vs UAB) | +0.1107 | 0.2842 | ±0.5684 | +0.390 | 0.6968 | 1.1171 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.839** | **1.31e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.115** | **0.0344** | 1.0329 | * |
| Hypertension | +0.2843 | 0.2488 | ±0.4976 | +1.143 | 0.2532 | 1.3288 |  |
| **High cholesterol** | **+0.5979** | 0.2328 | ±0.4655 | **+2.569** | **0.0102** | 1.8183 | * |
| Kidney disease | +0.6282 | 0.3929 | ±0.7858 | +1.599 | 0.1098 | 1.8742 |  |
| Circulatory disease | +0.4208 | 0.3481 | ±0.6962 | +1.209 | 0.2267 | 1.5231 |  |
| Avg. daily range (mg/dL) | -0.0011 | 0.0070 | ±0.0140 | -0.161 | 0.8723 | 0.9989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0775**, LLR χ² = **45.51** (p = **3.95e-06**), AUC = **0.6886**, AIC = **565.4**, BIC = **619.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2354 | 0.8886 | ±1.7773 | -0.265 | 0.7911 | 0.7903 |  |
| Education: graduate level (vs college) | -0.0329 | 0.2452 | ±0.4905 | -0.134 | 0.8931 | 0.9676 |  |
| Education: high school or below (vs college) | +0.3550 | 0.3670 | ±0.7340 | +0.967 | 0.3334 | 1.4262 |  |
| Site: UCSD (vs UAB) | -0.1031 | 0.3043 | ±0.6086 | -0.339 | 0.7347 | 0.9020 |  |
| Site: UW (vs UAB) | +0.1116 | 0.2849 | ±0.5697 | +0.392 | 0.6951 | 1.1181 |  |
| **Age (years)** | **-0.0536** | 0.0110 | ±0.0221 | **-4.856** | **1.20e-06** | 0.9478 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0154 | ±0.0309 | **+2.043** | **0.0410** | 1.0320 | * |
| Hypertension | +0.2848 | 0.2487 | ±0.4975 | +1.145 | 0.2522 | 1.3295 |  |
| **High cholesterol** | **+0.5805** | 0.2337 | ±0.4675 | **+2.484** | **0.0130** | 1.7870 | * |
| Kidney disease | +0.6407 | 0.3920 | ±0.7840 | +1.635 | 0.1021 | 1.8979 |  |
| Circulatory disease | +0.4275 | 0.3480 | ±0.6960 | +1.229 | 0.2192 | 1.5334 |  |
| SD of daily means (mg/dL) | +0.0366 | 0.0475 | ±0.0950 | +0.770 | 0.4415 | 1.0372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0812**, LLR χ² = **47.64** (p = **1.65e-06**), AUC = **0.6881**, AIC = **563.2**, BIC = **617.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.9246 | 3.6450 | ±7.2900 | +1.625 | 0.1041 | 374.1250 |  |
| Education: graduate level (vs college) | -0.0589 | 0.2460 | ±0.4919 | -0.239 | 0.8107 | 0.9428 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3669 | ±0.7337 | +0.954 | 0.3402 | 1.4190 |  |
| Site: UCSD (vs UAB) | -0.0719 | 0.3051 | ±0.6102 | -0.236 | 0.8137 | 0.9306 |  |
| Site: UW (vs UAB) | +0.0981 | 0.2850 | ±0.5700 | +0.344 | 0.7307 | 1.1031 |  |
| **Age (years)** | **-0.0553** | 0.0111 | ±0.0223 | **-4.967** | **6.80e-07** | 0.9462 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0154 | ±0.0309 | **+2.037** | **0.0417** | 1.0319 | * |
| Hypertension | +0.2910 | 0.2495 | ±0.4991 | +1.166 | 0.2435 | 1.3377 |  |
| **High cholesterol** | **+0.5715** | 0.2337 | ±0.4673 | **+2.446** | **0.0145** | 1.7708 | * |
| Kidney disease | +0.6032 | 0.3930 | ±0.7859 | +1.535 | 0.1248 | 1.8280 |  |
| Circulatory disease | +0.4015 | 0.3494 | ±0.6988 | +1.149 | 0.2505 | 1.4941 |  |
| Time in range 70-180, pooled (%) | -0.0595 | 0.0354 | ±0.0707 | -1.682 | 0.0926 | 0.9423 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0808**, LLR χ² = **47.40** (p = **1.82e-06**), AUC = **0.6886**, AIC = **563.5**, BIC = **617.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.8341 | 3.7453 | ±7.4905 | +1.558 | 0.1193 | 341.7658 |  |
| Education: graduate level (vs college) | -0.0582 | 0.2459 | ±0.4919 | -0.237 | 0.8129 | 0.9435 |  |
| Education: high school or below (vs college) | +0.3549 | 0.3666 | ±0.7332 | +0.968 | 0.3331 | 1.4260 |  |
| Site: UCSD (vs UAB) | -0.0733 | 0.3050 | ±0.6100 | -0.240 | 0.8102 | 0.9294 |  |
| Site: UW (vs UAB) | +0.1002 | 0.2849 | ±0.5699 | +0.352 | 0.7251 | 1.1054 |  |
| **Age (years)** | **-0.0551** | 0.0111 | ±0.0222 | **-4.956** | **7.18e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0312** | 0.0155 | ±0.0309 | **+2.019** | **0.0435** | 1.0317 | * |
| Hypertension | +0.2910 | 0.2495 | ±0.4989 | +1.166 | 0.2434 | 1.3377 |  |
| **High cholesterol** | **+0.5719** | 0.2336 | ±0.4673 | **+2.448** | **0.0144** | 1.7716 | * |
| Kidney disease | +0.5987 | 0.3932 | ±0.7864 | +1.523 | 0.1279 | 1.8198 |  |
| Circulatory disease | +0.4000 | 0.3493 | ±0.6986 | +1.145 | 0.2522 | 1.4918 |  |
| Avg. daily time in range 70-180 (%) | -0.0585 | 0.0363 | ±0.0727 | -1.610 | 0.1074 | 0.9432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.94** (p = **4.98e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0380 | 0.8498 | ±1.6997 | -0.045 | 0.9643 | 0.9627 |  |
| Education: graduate level (vs college) | -0.0396 | 0.2454 | ±0.4909 | -0.161 | 0.8719 | 0.9612 |  |
| Education: high school or below (vs college) | +0.3578 | 0.3681 | ±0.7363 | +0.972 | 0.3311 | 1.4302 |  |
| Site: UCSD (vs UAB) | -0.1120 | 0.3036 | ±0.6072 | -0.369 | 0.7123 | 0.8941 |  |
| Site: UW (vs UAB) | +0.1111 | 0.2844 | ±0.5688 | +0.391 | 0.6961 | 1.1175 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2833 | 0.2488 | ±0.4976 | +1.139 | 0.2548 | 1.3275 |  |
| **High cholesterol** | **+0.5983** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8191 | * |
| Kidney disease | +0.6255 | 0.3923 | ±0.7845 | +1.594 | 0.1108 | 1.8691 |  |
| Circulatory disease | +0.4222 | 0.3482 | ±0.6965 | +1.212 | 0.2254 | 1.5253 |  |
| Time 54-69, pooled (%) | +0.0249 | 0.2235 | ±0.4470 | +0.112 | 0.9112 | 1.0252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0423 | 0.8493 | ±1.6986 | -0.050 | 0.9603 | 0.9586 |  |
| Education: graduate level (vs college) | -0.0377 | 0.2455 | ±0.4911 | -0.153 | 0.8780 | 0.9630 |  |
| Education: high school or below (vs college) | +0.3605 | 0.3683 | ±0.7366 | +0.979 | 0.3277 | 1.4340 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3038 | ±0.6076 | -0.374 | 0.7084 | 0.8926 |  |
| Site: UW (vs UAB) | +0.1117 | 0.2844 | ±0.5688 | +0.393 | 0.6946 | 1.1181 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.874** | **1.10e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.128** | **0.0333** | 1.0332 | * |
| Hypertension | +0.2834 | 0.2489 | ±0.4977 | +1.139 | 0.2547 | 1.3277 |  |
| **High cholesterol** | **+0.5982** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8189 | * |
| Kidney disease | +0.6265 | 0.3923 | ±0.7845 | +1.597 | 0.1102 | 1.8711 |  |
| Circulatory disease | +0.4240 | 0.3484 | ±0.6969 | +1.217 | 0.2236 | 1.5281 |  |
| Avg. daily time 54-69 (%) | +0.0423 | 0.2141 | ±0.4283 | +0.198 | 0.8432 | 1.0433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.94** (p = **4.98e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0380 | 0.8498 | ±1.6997 | -0.045 | 0.9643 | 0.9627 |  |
| Education: graduate level (vs college) | -0.0396 | 0.2454 | ±0.4909 | -0.161 | 0.8719 | 0.9612 |  |
| Education: high school or below (vs college) | +0.3578 | 0.3681 | ±0.7363 | +0.972 | 0.3311 | 1.4302 |  |
| Site: UCSD (vs UAB) | -0.1120 | 0.3036 | ±0.6072 | -0.369 | 0.7123 | 0.8941 |  |
| Site: UW (vs UAB) | +0.1111 | 0.2844 | ±0.5688 | +0.391 | 0.6961 | 1.1175 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2833 | 0.2488 | ±0.4976 | +1.139 | 0.2548 | 1.3275 |  |
| **High cholesterol** | **+0.5983** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8191 | * |
| Kidney disease | +0.6255 | 0.3923 | ±0.7845 | +1.594 | 0.1108 | 1.8691 |  |
| Circulatory disease | +0.4222 | 0.3482 | ±0.6965 | +1.212 | 0.2254 | 1.5253 |  |
| Time < 70 (%) | +0.0249 | 0.2235 | ±0.4470 | +0.112 | 0.9112 | 1.0252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0423 | 0.8493 | ±1.6986 | -0.050 | 0.9603 | 0.9586 |  |
| Education: graduate level (vs college) | -0.0377 | 0.2455 | ±0.4911 | -0.153 | 0.8780 | 0.9630 |  |
| Education: high school or below (vs college) | +0.3605 | 0.3683 | ±0.7366 | +0.979 | 0.3277 | 1.4340 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3038 | ±0.6076 | -0.374 | 0.7084 | 0.8926 |  |
| Site: UW (vs UAB) | +0.1117 | 0.2844 | ±0.5688 | +0.393 | 0.6946 | 1.1181 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.874** | **1.10e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.128** | **0.0333** | 1.0332 | * |
| Hypertension | +0.2834 | 0.2489 | ±0.4977 | +1.139 | 0.2547 | 1.3277 |  |
| **High cholesterol** | **+0.5982** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8189 | * |
| Kidney disease | +0.6265 | 0.3923 | ±0.7845 | +1.597 | 0.1102 | 1.8711 |  |
| Circulatory disease | +0.4240 | 0.3484 | ±0.6969 | +1.217 | 0.2236 | 1.5281 |  |
| Avg. daily time < 70 (%) | +0.0423 | 0.2141 | ±0.4283 | +0.198 | 0.8432 | 1.0433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0810**, LLR χ² = **47.54** (p = **1.72e-06**), AUC = **0.6875**, AIC = **563.3**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0048 | 0.8506 | ±1.7012 | -0.006 | 0.9955 | 0.9953 |  |
| Education: graduate level (vs college) | -0.0639 | 0.2461 | ±0.4922 | -0.259 | 0.7953 | 0.9381 |  |
| Education: high school or below (vs college) | +0.3428 | 0.3668 | ±0.7337 | +0.934 | 0.3501 | 1.4088 |  |
| Site: UCSD (vs UAB) | -0.0710 | 0.3052 | ±0.6104 | -0.233 | 0.8161 | 0.9315 |  |
| Site: UW (vs UAB) | +0.0957 | 0.2849 | ±0.5699 | +0.336 | 0.7368 | 1.1005 |  |
| **Age (years)** | **-0.0552** | 0.0111 | ±0.0223 | **-4.965** | **6.88e-07** | 0.9463 | *** |
| **BMI (kg/m2)** | **+0.0313** | 0.0154 | ±0.0309 | **+2.031** | **0.0423** | 1.0318 | * |
| Hypertension | +0.2910 | 0.2494 | ±0.4988 | +1.167 | 0.2433 | 1.3378 |  |
| **High cholesterol** | **+0.5730** | 0.2335 | ±0.4671 | **+2.454** | **0.0141** | 1.7737 | * |
| Kidney disease | +0.6003 | 0.3930 | ±0.7860 | +1.527 | 0.1266 | 1.8227 |  |
| Circulatory disease | +0.3990 | 0.3494 | ±0.6989 | +1.142 | 0.2535 | 1.4904 |  |
| Time 181-250, pooled (%) | +0.0580 | 0.0351 | ±0.0701 | +1.653 | 0.0983 | 1.0597 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0805**, LLR χ² = **47.27** (p = **1.93e-06**), AUC = **0.6881**, AIC = **563.6**, BIC = **617.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0031 | 0.8511 | ±1.7023 | -0.004 | 0.9971 | 0.9969 |  |
| Education: graduate level (vs college) | -0.0631 | 0.2461 | ±0.4921 | -0.256 | 0.7976 | 0.9388 |  |
| Education: high school or below (vs college) | +0.3472 | 0.3666 | ±0.7332 | +0.947 | 0.3436 | 1.4151 |  |
| Site: UCSD (vs UAB) | -0.0714 | 0.3052 | ±0.6104 | -0.234 | 0.8150 | 0.9311 |  |
| Site: UW (vs UAB) | +0.0982 | 0.2849 | ±0.5697 | +0.345 | 0.7302 | 1.1032 |  |
| **Age (years)** | **-0.0550** | 0.0111 | ±0.0222 | **-4.952** | **7.34e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0311** | 0.0154 | ±0.0309 | **+2.014** | **0.0440** | 1.0316 | * |
| Hypertension | +0.2907 | 0.2493 | ±0.4986 | +1.166 | 0.2436 | 1.3374 |  |
| **High cholesterol** | **+0.5735** | 0.2335 | ±0.4670 | **+2.456** | **0.0141** | 1.7744 | * |
| Kidney disease | +0.5963 | 0.3933 | ±0.7866 | +1.516 | 0.1294 | 1.8155 |  |
| Circulatory disease | +0.3966 | 0.3494 | ±0.6988 | +1.135 | 0.2563 | 1.4868 |  |
| Avg. daily time 181-250 (%) | +0.0565 | 0.0361 | ±0.0721 | +1.566 | 0.1173 | 1.0581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0810**, LLR χ² = **47.54** (p = **1.72e-06**), AUC = **0.6875**, AIC = **563.3**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0048 | 0.8506 | ±1.7012 | -0.006 | 0.9955 | 0.9953 |  |
| Education: graduate level (vs college) | -0.0639 | 0.2461 | ±0.4922 | -0.259 | 0.7953 | 0.9381 |  |
| Education: high school or below (vs college) | +0.3428 | 0.3668 | ±0.7337 | +0.934 | 0.3501 | 1.4088 |  |
| Site: UCSD (vs UAB) | -0.0710 | 0.3052 | ±0.6104 | -0.233 | 0.8161 | 0.9315 |  |
| Site: UW (vs UAB) | +0.0957 | 0.2849 | ±0.5699 | +0.336 | 0.7368 | 1.1005 |  |
| **Age (years)** | **-0.0552** | 0.0111 | ±0.0223 | **-4.965** | **6.88e-07** | 0.9463 | *** |
| **BMI (kg/m2)** | **+0.0313** | 0.0154 | ±0.0309 | **+2.031** | **0.0423** | 1.0318 | * |
| Hypertension | +0.2910 | 0.2494 | ±0.4988 | +1.167 | 0.2433 | 1.3378 |  |
| **High cholesterol** | **+0.5730** | 0.2335 | ±0.4671 | **+2.454** | **0.0141** | 1.7737 | * |
| Kidney disease | +0.6003 | 0.3930 | ±0.7860 | +1.527 | 0.1266 | 1.8227 |  |
| Circulatory disease | +0.3990 | 0.3494 | ±0.6989 | +1.142 | 0.2535 | 1.4904 |  |
| Time > 180 (%) | +0.0580 | 0.0351 | ±0.0701 | +1.653 | 0.0983 | 1.0597 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0805**, LLR χ² = **47.27** (p = **1.93e-06**), AUC = **0.6881**, AIC = **563.6**, BIC = **617.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0031 | 0.8511 | ±1.7023 | -0.004 | 0.9971 | 0.9969 |  |
| Education: graduate level (vs college) | -0.0631 | 0.2461 | ±0.4921 | -0.256 | 0.7976 | 0.9388 |  |
| Education: high school or below (vs college) | +0.3472 | 0.3666 | ±0.7332 | +0.947 | 0.3436 | 1.4151 |  |
| Site: UCSD (vs UAB) | -0.0714 | 0.3052 | ±0.6104 | -0.234 | 0.8150 | 0.9311 |  |
| Site: UW (vs UAB) | +0.0982 | 0.2849 | ±0.5697 | +0.345 | 0.7302 | 1.1032 |  |
| **Age (years)** | **-0.0550** | 0.0111 | ±0.0222 | **-4.952** | **7.34e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0311** | 0.0154 | ±0.0309 | **+2.014** | **0.0440** | 1.0316 | * |
| Hypertension | +0.2907 | 0.2493 | ±0.4986 | +1.166 | 0.2436 | 1.3374 |  |
| **High cholesterol** | **+0.5735** | 0.2335 | ±0.4670 | **+2.456** | **0.0141** | 1.7744 | * |
| Kidney disease | +0.5963 | 0.3933 | ±0.7866 | +1.516 | 0.1294 | 1.8155 |  |
| Circulatory disease | +0.3966 | 0.3494 | ±0.6988 | +1.135 | 0.2563 | 1.4868 |  |
| Avg. daily time > 180 (%) | +0.0565 | 0.0361 | ±0.0721 | +1.566 | 0.1173 | 1.0581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0939**, LLR χ² = **55.11** (p = **7.40e-08**), AUC = **0.6966**, AIC = **555.7**, BIC = **610.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0428 | 0.8658 | ±1.7316 | +0.049 | 0.9606 | 1.0437 |  |
| Education: graduate level (vs college) | -0.0364 | 0.2477 | ±0.4954 | -0.147 | 0.8832 | 0.9642 |  |
| Education: high school or below (vs college) | +0.3092 | 0.3712 | ±0.7424 | +0.833 | 0.4049 | 1.3623 |  |
| Site: UCSD (vs UAB) | -0.0861 | 0.3048 | ±0.6096 | -0.283 | 0.7774 | 0.9175 |  |
| Site: UW (vs UAB) | +0.0662 | 0.2871 | ±0.5741 | +0.231 | 0.8175 | 1.0685 |  |
| **Age (years)** | **-0.0536** | 0.0112 | ±0.0223 | **-4.803** | **1.56e-06** | 0.9478 | *** |
| BMI (kg/m2) | +0.0267 | 0.0159 | ±0.0318 | +1.684 | 0.0922 | 1.0271 | . |
| Hypertension | +0.3199 | 0.2510 | ±0.5021 | +1.274 | 0.2025 | 1.3771 |  |
| **High cholesterol** | **+0.5234** | 0.2360 | ±0.4720 | **+2.218** | **0.0266** | 1.6878 | * |
| Kidney disease | +0.6481 | 0.3926 | ±0.7853 | +1.651 | 0.0988 | 1.9119 | . |
| Circulatory disease | +0.4333 | 0.3512 | ±0.7025 | +1.234 | 0.2173 | 1.5424 |  |
| **Nocturnal time > 180 (%)** | **+0.0961** | 0.0338 | ±0.0676 | **+2.845** | **0.0044** | 1.1009 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 46 single-predictor tests; 2 with raw p < 0.05 (about 2 expected by chance); FDR rule applied to 46 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family and 0 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 685): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.033 vs 0.025 for covariates alone, gain +0.008; +0.384 per SD, p = 0.031, q = 0.323). No association survives FDR; nominal only: %>180 nocturnal (p = 0.031).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 685): best single predictor out of sample is **%>180 nocturnal** (CV AUC 0.653 vs 0.641 for covariates alone, gain +0.012; OR 1.34 per SD, p = 0.004, q = 0.102). No association survives FDR; nominal only: %>180 nocturnal (p = 0.004).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.012, via %>180 nocturnal); CES-D-10 depressive symptoms (0-30) (+0.008, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 180 (0 FDR-significant / 2 raw-significant of 6); HbA1c (0 FDR-significant / 0 raw-significant of 2); CGM level (0 FDR-significant / 0 raw-significant of 6).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%>180 nocturnal, ΔAIC -5.0); Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -10.2).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
