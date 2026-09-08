# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 550; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **550**, R² = **0.1453**, Adj R² = **0.1294**, F-statistic = **9.16** (p = **4.71e-14**), Residual SE = **4.879** on **539** df, AIC = **3315.2**, BIC = **3362.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.9379** | 1.8688 | ±3.7377 | **+6.388** | **1.68e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4384** | 0.4456 | ±0.8913 | **-3.228** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1599 | 0.6846 | ±1.3691 | +1.694 | 0.0902 | . |
| Site: UCSD (vs UAB) | +0.1170 | 0.5598 | ±1.1195 | +0.209 | 0.8345 |  |
| Site: UW (vs UAB) | -0.4161 | 0.4977 | ±0.9953 | -0.836 | 0.4031 |  |
| **Age (years)** | **-0.1219** | 0.0206 | ±0.0413 | **-5.906** | **3.50e-09** | *** |
| BMI (kg/m2) | +0.0378 | 0.0309 | ±0.0618 | +1.223 | 0.2215 |  |
| Hypertension | +0.2668 | 0.4644 | ±0.9288 | +0.574 | 0.5657 |  |
| High cholesterol | +0.3226 | 0.4621 | ±0.9242 | +0.698 | 0.4851 |  |
| Kidney disease | +0.8311 | 0.5671 | ±1.1342 | +1.466 | 0.1428 |  |
| **Circulatory disease** | **+1.9482** | 0.5868 | ±1.1737 | **+3.320** | **9.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **550**, R² = **0.1532**, Adj R² = **0.1359**, F-statistic = **8.85** (p = **1.52e-14**), Residual SE = **4.861** on **538** df, AIC = **3312.0**, BIC = **3363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4520** | 2.2750 | ±4.5500 | **+4.155** | **3.26e-05** | *** |
| **Education: graduate level (vs college)** | **-1.3727** | 0.4471 | ±0.8942 | **-3.070** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0124 | 0.6709 | ±1.3418 | +1.509 | 0.1313 |  |
| Site: UCSD (vs UAB) | +0.1882 | 0.5566 | ±1.1132 | +0.338 | 0.7353 |  |
| Site: UW (vs UAB) | -0.3283 | 0.4994 | ±0.9988 | -0.657 | 0.5109 |  |
| **Age (years)** | **-0.1187** | 0.0206 | ±0.0413 | **-5.752** | **8.81e-09** | *** |
| BMI (kg/m2) | +0.0296 | 0.0314 | ±0.0629 | +0.942 | 0.3463 |  |
| Hypertension | +0.2518 | 0.4652 | ±0.9304 | +0.541 | 0.5883 |  |
| High cholesterol | +0.3278 | 0.4603 | ±0.9206 | +0.712 | 0.4764 |  |
| Kidney disease | +0.8594 | 0.5692 | ±1.1385 | +1.510 | 0.1311 |  |
| **Circulatory disease** | **+1.9097** | 0.5870 | ±1.1741 | **+3.253** | **0.0011** | ** |
| HbA1c (%) | +0.3505 | 0.1791 | ±0.3581 | +1.957 | 0.0503 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **550**, R² = **0.1480**, Adj R² = **0.1306**, F-statistic = **8.50** (p = **6.76e-14**), Residual SE = **4.876** on **538** df, AIC = **3315.4**, BIC = **3367.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.7189** | 2.1383 | ±4.2767 | **+5.013** | **5.37e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4090** | 0.4473 | ±0.8947 | **-3.150** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0828 | 0.6801 | ±1.3602 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1743 | 0.5591 | ±1.1183 | +0.312 | 0.7553 |  |
| Site: UW (vs UAB) | -0.3685 | 0.5013 | ±1.0025 | -0.735 | 0.4623 |  |
| **Age (years)** | **-0.1200** | 0.0207 | ±0.0414 | **-5.802** | **6.57e-09** | *** |
| BMI (kg/m2) | +0.0344 | 0.0311 | ±0.0622 | +1.104 | 0.2694 |  |
| Hypertension | +0.2729 | 0.4630 | ±0.9260 | +0.589 | 0.5555 |  |
| High cholesterol | +0.3354 | 0.4618 | ±0.9237 | +0.726 | 0.4676 |  |
| Kidney disease | +0.8141 | 0.5739 | ±1.1477 | +1.419 | 0.1560 |  |
| **Circulatory disease** | **+1.9098** | 0.5864 | ±1.1728 | **+3.257** | **0.0011** | ** |
| Mean glucose (mg/dL) | +0.0069 | 0.0058 | ±0.0117 | +1.176 | 0.2397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **550**, R² = **0.1480**, Adj R² = **0.1306**, F-statistic = **8.50** (p = **6.76e-14**), Residual SE = **4.876** on **538** df, AIC = **3315.4**, BIC = **3367.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7706** | 2.6231 | ±5.2462 | **+3.725** | **1.95e-04** | *** |
| **Education: graduate level (vs college)** | **-1.4090** | 0.4473 | ±0.8947 | **-3.150** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0828 | 0.6801 | ±1.3602 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1743 | 0.5591 | ±1.1183 | +0.312 | 0.7553 |  |
| Site: UW (vs UAB) | -0.3685 | 0.5013 | ±1.0025 | -0.735 | 0.4623 |  |
| **Age (years)** | **-0.1200** | 0.0207 | ±0.0414 | **-5.802** | **6.57e-09** | *** |
| BMI (kg/m2) | +0.0344 | 0.0311 | ±0.0622 | +1.104 | 0.2694 |  |
| Hypertension | +0.2729 | 0.4630 | ±0.9260 | +0.589 | 0.5555 |  |
| High cholesterol | +0.3354 | 0.4618 | ±0.9237 | +0.726 | 0.4676 |  |
| Kidney disease | +0.8141 | 0.5739 | ±1.1477 | +1.419 | 0.1560 |  |
| **Circulatory disease** | **+1.9098** | 0.5864 | ±1.1728 | **+3.257** | **0.0011** | ** |
| GMI (%) | +0.2865 | 0.2437 | ±0.4874 | +1.176 | 0.2397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **550**, R² = **0.1491**, Adj R² = **0.1317**, F-statistic = **8.57** (p = **4.98e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.7**, BIC = **3366.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.6294** | 2.0896 | ±4.1793 | **+5.087** | **3.64e-07** | *** |
| **Education: graduate level (vs college)** | **-1.3919** | 0.4484 | ±0.8968 | **-3.104** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0838 | 0.6784 | ±1.3568 | +1.598 | 0.1101 |  |
| Site: UCSD (vs UAB) | +0.1902 | 0.5574 | ±1.1147 | +0.341 | 0.7330 |  |
| Site: UW (vs UAB) | -0.3855 | 0.4996 | ±0.9992 | -0.772 | 0.4403 |  |
| **Age (years)** | **-0.1184** | 0.0208 | ±0.0415 | **-5.705** | **1.16e-08** | *** |
| BMI (kg/m2) | +0.0318 | 0.0312 | ±0.0623 | +1.019 | 0.3080 |  |
| Hypertension | +0.2809 | 0.4627 | ±0.9253 | +0.607 | 0.5438 |  |
| High cholesterol | +0.3404 | 0.4612 | ±0.9225 | +0.738 | 0.4605 |  |
| Kidney disease | +0.8285 | 0.5721 | ±1.1442 | +1.448 | 0.1476 |  |
| **Circulatory disease** | **+1.9029** | 0.5860 | ±1.1721 | **+3.247** | **0.0012** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0076 | 0.0053 | ±0.0106 | +1.423 | 0.1548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1554**, Adj R² = **0.1381**, F-statistic = **9.00** (p = **8.13e-15**), Residual SE = **4.855** on **538** df, AIC = **3310.6**, BIC = **3362.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0737** | 2.0209 | ±4.0418 | **+4.985** | **6.21e-07** | *** |
| **Education: graduate level (vs college)** | **-1.3761** | 0.4464 | ±0.8929 | **-3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0166 | 0.6815 | ±1.3631 | +1.492 | 0.1358 |  |
| Site: UCSD (vs UAB) | +0.1974 | 0.5554 | ±1.1107 | +0.355 | 0.7222 |  |
| Site: UW (vs UAB) | -0.2598 | 0.5007 | ±1.0015 | -0.519 | 0.6039 |  |
| **Age (years)** | **-0.1196** | 0.0207 | ±0.0413 | **-5.788** | **7.13e-09** | *** |
| BMI (kg/m2) | +0.0337 | 0.0313 | ±0.0625 | +1.076 | 0.2818 |  |
| Hypertension | +0.2480 | 0.4609 | ±0.9219 | +0.538 | 0.5905 |  |
| High cholesterol | +0.3566 | 0.4582 | ±0.9164 | +0.778 | 0.4364 |  |
| Kidney disease | +0.6145 | 0.5853 | ±1.1705 | +1.050 | 0.2937 |  |
| **Circulatory disease** | **+1.8914** | 0.5897 | ±1.1795 | **+3.207** | **0.0013** | ** |
| **Glucose SD, pooled (mg/dL)** | **+0.0439** | 0.0177 | ±0.0354 | **+2.480** | **0.0131** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1508**, Adj R² = **0.1334**, F-statistic = **8.68** (p = **3.05e-14**), Residual SE = **4.868** on **538** df, AIC = **3313.6**, BIC = **3365.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4888** | 2.0165 | ±4.0331 | **+5.201** | **1.98e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4026** | 0.4466 | ±0.8932 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.0354 | 0.6879 | ±1.3758 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | +0.1763 | 0.5583 | ±1.1166 | +0.316 | 0.7521 |  |
| Site: UW (vs UAB) | -0.3138 | 0.5017 | ±1.0034 | -0.625 | 0.5317 |  |
| **Age (years)** | **-0.1208** | 0.0206 | ±0.0413 | **-5.852** | **4.86e-09** | *** |
| BMI (kg/m2) | +0.0374 | 0.0311 | ±0.0622 | +1.202 | 0.2293 |  |
| Hypertension | +0.2658 | 0.4623 | ±0.9246 | +0.575 | 0.5653 |  |
| High cholesterol | +0.3421 | 0.4605 | ±0.9211 | +0.743 | 0.4576 |  |
| Kidney disease | +0.6554 | 0.5878 | ±1.1755 | +1.115 | 0.2648 |  |
| **Circulatory disease** | **+1.9180** | 0.5899 | ±1.1798 | **+3.251** | **0.0011** | ** |
| Avg. daily SD (mg/dL) | +0.0371 | 0.0203 | ±0.0407 | +1.825 | 0.0681 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **550**, R² = **0.1499**, Adj R² = **0.1325**, F-statistic = **8.62** (p = **3.95e-14**), Residual SE = **4.870** on **538** df, AIC = **3314.2**, BIC = **3365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3490** | 2.1015 | ±4.2029 | **+4.925** | **8.45e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4202** | 0.4455 | ±0.8909 | **-3.188** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1221 | 0.6890 | ±1.3780 | +1.629 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.1306 | 0.5586 | ±1.1172 | +0.234 | 0.8151 |  |
| Site: UW (vs UAB) | -0.3328 | 0.4997 | ±0.9994 | -0.666 | 0.5054 |  |
| **Age (years)** | **-0.1223** | 0.0206 | ±0.0412 | **-5.936** | **2.93e-09** | *** |
| BMI (kg/m2) | +0.0384 | 0.0311 | ±0.0622 | +1.235 | 0.2168 |  |
| Hypertension | +0.2305 | 0.4648 | ±0.9296 | +0.496 | 0.6200 |  |
| High cholesterol | +0.3350 | 0.4610 | ±0.9220 | +0.727 | 0.4675 |  |
| Kidney disease | +0.6580 | 0.5764 | ±1.1529 | +1.142 | 0.2536 |  |
| **Circulatory disease** | **+1.9496** | 0.5909 | ±1.1817 | **+3.300** | **9.68e-04** | *** |
| CV (%) | +0.0659 | 0.0394 | ±0.0789 | +1.671 | 0.0946 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **550**, R² = **0.1510**, Adj R² = **0.1336**, F-statistic = **8.70** (p = **2.89e-14**), Residual SE = **4.867** on **538** df, AIC = **3313.5**, BIC = **3365.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.6857** | 2.0793 | ±4.1586 | **+6.582** | **4.64e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4132** | 0.4453 | ±0.8906 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1317 | 0.6880 | ±1.3761 | +1.645 | 0.1000 |  |
| Site: UCSD (vs UAB) | +0.1059 | 0.5579 | ±1.1159 | +0.190 | 0.8495 |  |
| Site: UW (vs UAB) | -0.3491 | 0.4988 | ±0.9976 | -0.700 | 0.4839 |  |
| **Age (years)** | **-0.1221** | 0.0206 | ±0.0412 | **-5.931** | **3.01e-09** | *** |
| BMI (kg/m2) | +0.0396 | 0.0310 | ±0.0620 | +1.276 | 0.2020 |  |
| Hypertension | +0.2420 | 0.4641 | ±0.9282 | +0.522 | 0.6020 |  |
| High cholesterol | +0.3104 | 0.4599 | ±0.9199 | +0.675 | 0.4998 |  |
| Kidney disease | +0.6749 | 0.5723 | ±1.1446 | +1.179 | 0.2383 |  |
| **Circulatory disease** | **+1.9295** | 0.5906 | ±1.1812 | **+3.267** | **0.0011** | ** |
| Mean / SD ratio | -0.4100 | 0.2226 | ±0.4452 | -1.842 | 0.0655 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1473**, Adj R² = **0.1298**, F-statistic = **8.45** (p = **8.39e-14**), Residual SE = **4.878** on **538** df, AIC = **3315.9**, BIC = **3367.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.8850** | 2.0675 | ±4.1351 | **+6.232** | **4.60e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4240** | 0.4459 | ±0.8918 | **-3.193** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1388 | 0.6894 | ±1.3788 | +1.652 | 0.0986 | . |
| Site: UCSD (vs UAB) | +0.1077 | 0.5593 | ±1.1187 | +0.193 | 0.8473 |  |
| Site: UW (vs UAB) | -0.3904 | 0.4989 | ±0.9979 | -0.783 | 0.4339 |  |
| **Age (years)** | **-0.1225** | 0.0206 | ±0.0412 | **-5.940** | **2.85e-09** | *** |
| BMI (kg/m2) | +0.0406 | 0.0309 | ±0.0618 | +1.314 | 0.1890 |  |
| Hypertension | +0.2583 | 0.4654 | ±0.9309 | +0.555 | 0.5790 |  |
| High cholesterol | +0.3200 | 0.4620 | ±0.9241 | +0.693 | 0.4886 |  |
| Kidney disease | +0.7465 | 0.5724 | ±1.1449 | +1.304 | 0.1922 |  |
| **Circulatory disease** | **+1.9499** | 0.5898 | ±1.1795 | **+3.306** | **9.45e-04** | *** |
| Avg. daily mean/SD | -0.1958 | 0.1767 | ±0.3535 | -1.108 | 0.2679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **550**, R² = **0.1589**, Adj R² = **0.1417**, F-statistic = **9.24** (p = **2.94e-15**), Residual SE = **4.845** on **538** df, AIC = **3308.4**, BIC = **3360.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3389** | 2.2862 | ±4.5725 | **+3.647** | **2.65e-04** | *** |
| **Education: graduate level (vs college)** | **-1.3462** | 0.4470 | ±0.8940 | **-3.012** | **0.0026** | ** |
| Education: high school or below (vs college) | +1.0510 | 0.6749 | ±1.3497 | +1.557 | 0.1194 |  |
| Site: UCSD (vs UAB) | +0.1943 | 0.5547 | ±1.1094 | +0.350 | 0.7261 |  |
| Site: UW (vs UAB) | -0.1853 | 0.5043 | ±1.0086 | -0.367 | 0.7133 |  |
| **Age (years)** | **-0.1136** | 0.0206 | ±0.0412 | **-5.515** | **3.49e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.0308 | ±0.0616 | +1.269 | 0.2045 |  |
| Hypertension | +0.2615 | 0.4597 | ±0.9194 | +0.569 | 0.5695 |  |
| High cholesterol | +0.3540 | 0.4556 | ±0.9112 | +0.777 | 0.4372 |  |
| Kidney disease | +0.6777 | 0.5772 | ±1.1543 | +1.174 | 0.2403 |  |
| **Circulatory disease** | **+1.9165** | 0.5923 | ±1.1846 | **+3.236** | **0.0012** | ** |
| **MAG (mg/dL/h)** | **+0.0640** | 0.0236 | ±0.0473 | **+2.709** | **0.0067** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **550**, R² = **0.1497**, Adj R² = **0.1324**, F-statistic = **8.61** (p = **4.13e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1422** | 2.1865 | ±4.3730 | **+4.639** | **3.51e-06** | *** |
| **Education: graduate level (vs college)** | **-1.4048** | 0.4465 | ±0.8930 | **-3.146** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.0464 | 0.6899 | ±1.3799 | +1.517 | 0.1293 |  |
| Site: UCSD (vs UAB) | +0.1751 | 0.5587 | ±1.1174 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | -0.3247 | 0.5023 | ±1.0046 | -0.646 | 0.5180 |  |
| **Age (years)** | **-0.1193** | 0.0207 | ±0.0415 | **-5.753** | **8.77e-09** | *** |
| BMI (kg/m2) | +0.0388 | 0.0311 | ±0.0622 | +1.247 | 0.2124 |  |
| Hypertension | +0.2835 | 0.4618 | ±0.9235 | +0.614 | 0.5392 |  |
| High cholesterol | +0.3235 | 0.4604 | ±0.9208 | +0.703 | 0.4823 |  |
| Kidney disease | +0.6634 | 0.5881 | ±1.1761 | +1.128 | 0.2593 |  |
| **Circulatory disease** | **+1.9111** | 0.5901 | ±1.1801 | **+3.239** | **0.0012** | ** |
| Avg. daily range (mg/dL) | +0.0099 | 0.0061 | ±0.0122 | +1.631 | 0.1028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **550**, R² = **0.1662**, Adj R² = **0.1492**, F-statistic = **9.75** (p = **3.35e-16**), Residual SE = **4.823** on **538** df, AIC = **3303.5**, BIC = **3355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4372** | 1.8811 | ±3.7622 | **+5.549** | **2.88e-08** | *** |
| **Education: graduate level (vs college)** | **-1.2881** | 0.4464 | ±0.8928 | **-2.885** | **0.0039** | ** |
| Education: high school or below (vs college) | +1.1060 | 0.6685 | ±1.3369 | +1.655 | 0.0980 | . |
| Site: UCSD (vs UAB) | +0.1919 | 0.5519 | ±1.1038 | +0.348 | 0.7280 |  |
| Site: UW (vs UAB) | -0.2243 | 0.4908 | ±0.9816 | -0.457 | 0.6476 |  |
| **Age (years)** | **-0.1136** | 0.0209 | ±0.0419 | **-5.423** | **5.86e-08** | *** |
| BMI (kg/m2) | +0.0258 | 0.0307 | ±0.0614 | +0.841 | 0.4004 |  |
| Hypertension | +0.1651 | 0.4630 | ±0.9260 | +0.357 | 0.7213 |  |
| High cholesterol | +0.3730 | 0.4545 | ±0.9090 | +0.821 | 0.4118 |  |
| Kidney disease | +0.7104 | 0.5714 | ±1.1427 | +1.243 | 0.2137 |  |
| **Circulatory disease** | **+1.7689** | 0.5828 | ±1.1656 | **+3.035** | **0.0024** | ** |
| **SD of daily means (mg/dL)** | **+0.0894** | 0.0249 | ±0.0497 | **+3.593** | **3.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **550**, R² = **0.1497**, Adj R² = **0.1323**, F-statistic = **8.61** (p = **4.19e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.8425** | 1.9632 | ±3.9264 | **+6.542** | **6.08e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4089** | 0.4466 | ±0.8932 | **-3.155** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0571 | 0.6814 | ±1.3629 | +1.551 | 0.1208 |  |
| Site: UCSD (vs UAB) | +0.2036 | 0.5594 | ±1.1188 | +0.364 | 0.7159 |  |
| Site: UW (vs UAB) | -0.3527 | 0.5005 | ±1.0009 | -0.705 | 0.4810 |  |
| **Age (years)** | **-0.1202** | 0.0207 | ±0.0414 | **-5.811** | **6.23e-09** | *** |
| BMI (kg/m2) | +0.0324 | 0.0311 | ±0.0622 | +1.041 | 0.2979 |  |
| Hypertension | +0.2844 | 0.4622 | ±0.9244 | +0.615 | 0.5383 |  |
| High cholesterol | +0.3582 | 0.4614 | ±0.9229 | +0.776 | 0.4376 |  |
| Kidney disease | +0.7917 | 0.5765 | ±1.1529 | +1.373 | 0.1696 |  |
| **Circulatory disease** | **+1.9006** | 0.5847 | ±1.1694 | **+3.251** | **0.0012** | ** |
| Time in range 70-180, pooled (%) | -0.0138 | 0.0087 | ±0.0174 | -1.586 | 0.1128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **550**, R² = **0.1492**, Adj R² = **0.1318**, F-statistic = **8.57** (p = **4.88e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.7**, BIC = **3366.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.7968** | 1.9724 | ±3.9449 | **+6.488** | **8.71e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4138** | 0.4465 | ±0.8931 | **-3.166** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.0591 | 0.6824 | ±1.3647 | +1.552 | 0.1206 |  |
| Site: UCSD (vs UAB) | +0.2021 | 0.5595 | ±1.1191 | +0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -0.3556 | 0.5002 | ±1.0005 | -0.711 | 0.4772 |  |
| **Age (years)** | **-0.1205** | 0.0207 | ±0.0414 | **-5.822** | **5.83e-09** | *** |
| BMI (kg/m2) | +0.0326 | 0.0312 | ±0.0624 | +1.044 | 0.2965 |  |
| Hypertension | +0.2848 | 0.4623 | ±0.9247 | +0.616 | 0.5379 |  |
| High cholesterol | +0.3551 | 0.4617 | ±0.9235 | +0.769 | 0.4419 |  |
| Kidney disease | +0.7890 | 0.5761 | ±1.1522 | +1.370 | 0.1708 |  |
| **Circulatory disease** | **+1.9034** | 0.5852 | ±1.1703 | **+3.253** | **0.0011** | ** |
| Avg. daily time in range 70-180 (%) | -0.0129 | 0.0087 | ±0.0174 | -1.480 | 0.1389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **550**, R² = **0.1498**, Adj R² = **0.1324**, F-statistic = **8.62** (p = **4.07e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5721** | 1.8761 | ±3.7521 | **+6.168** | **6.90e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4396** | 0.4450 | ±0.8901 | **-3.235** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1816 | 0.6827 | ±1.3655 | +1.731 | 0.0835 | . |
| Site: UCSD (vs UAB) | +0.1753 | 0.5552 | ±1.1105 | +0.316 | 0.7522 |  |
| Site: UW (vs UAB) | -0.3597 | 0.4979 | ±0.9958 | -0.722 | 0.4701 |  |
| **Age (years)** | **-0.1193** | 0.0209 | ±0.0418 | **-5.710** | **1.13e-08** | *** |
| BMI (kg/m2) | +0.0381 | 0.0307 | ±0.0614 | +1.240 | 0.2151 |  |
| Hypertension | +0.1884 | 0.4672 | ±0.9345 | +0.403 | 0.6867 |  |
| High cholesterol | +0.3781 | 0.4610 | ±0.9219 | +0.820 | 0.4121 |  |
| Kidney disease | +0.8130 | 0.5668 | ±1.1335 | +1.434 | 0.1514 |  |
| **Circulatory disease** | **+1.8946** | 0.5939 | ±1.1879 | **+3.190** | **0.0014** | ** |
| Any reading < 54 during wear (0/1) | +0.8680 | 0.5149 | ±1.0298 | +1.686 | 0.0918 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **550**, R² = **0.1464**, Adj R² = **0.1289**, F-statistic = **8.39** (p = **1.08e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.5**, BIC = **3368.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8741** | 1.8817 | ±3.7634 | **+6.310** | **2.78e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4249** | 0.4459 | ±0.8918 | **-3.196** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1814 | 0.6845 | ±1.3690 | +1.726 | 0.0844 | . |
| Site: UCSD (vs UAB) | +0.1550 | 0.5594 | ±1.1189 | +0.277 | 0.7817 |  |
| Site: UW (vs UAB) | -0.3680 | 0.5000 | ±0.9999 | -0.736 | 0.4617 |  |
| **Age (years)** | **-0.1221** | 0.0207 | ±0.0414 | **-5.898** | **3.67e-09** | *** |
| BMI (kg/m2) | +0.0378 | 0.0312 | ±0.0624 | +1.211 | 0.2259 |  |
| Hypertension | +0.2224 | 0.4686 | ±0.9372 | +0.475 | 0.6351 |  |
| High cholesterol | +0.3556 | 0.4646 | ±0.9293 | +0.765 | 0.4441 |  |
| Kidney disease | +0.8244 | 0.5690 | ±1.1381 | +1.449 | 0.1474 |  |
| **Circulatory disease** | **+1.9770** | 0.5873 | ±1.1745 | **+3.366** | **7.61e-04** | *** |
| Time < 54 (%) | +0.6991 | 0.9768 | ±1.9536 | +0.716 | 0.4742 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **550**, R² = **0.1475**, Adj R² = **0.1301**, F-statistic = **8.46** (p = **7.78e-14**), Residual SE = **4.877** on **538** df, AIC = **3315.7**, BIC = **3367.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8857** | 1.8780 | ±3.7560 | **+6.329** | **2.47e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4253** | 0.4459 | ±0.8918 | **-3.196** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1882 | 0.6849 | ±1.3697 | +1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | +0.1589 | 0.5600 | ±1.1200 | +0.284 | 0.7766 |  |
| Site: UW (vs UAB) | -0.3616 | 0.5000 | ±1.0001 | -0.723 | 0.4696 |  |
| **Age (years)** | **-0.1220** | 0.0207 | ±0.0414 | **-5.891** | **3.85e-09** | *** |
| BMI (kg/m2) | +0.0372 | 0.0311 | ±0.0622 | +1.194 | 0.2323 |  |
| Hypertension | +0.2238 | 0.4657 | ±0.9314 | +0.481 | 0.6308 |  |
| High cholesterol | +0.3631 | 0.4631 | ±0.9263 | +0.784 | 0.4330 |  |
| Kidney disease | +0.8127 | 0.5701 | ±1.1402 | +1.426 | 0.1540 |  |
| **Circulatory disease** | **+1.9754** | 0.5878 | ±1.1755 | **+3.361** | **7.77e-04** | *** |
| Avg. daily time < 54 (%) | +0.7242 | 0.9502 | ±1.9004 | +0.762 | 0.4459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **550**, R² = **0.1506**, Adj R² = **0.1332**, F-statistic = **8.67** (p = **3.21e-14**), Residual SE = **4.868** on **538** df, AIC = **3313.7**, BIC = **3365.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7333** | 1.8731 | ±3.7463 | **+6.264** | **3.75e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4183** | 0.4469 | ±0.8938 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1713 | 0.6855 | ±1.3711 | +1.709 | 0.0875 | . |
| Site: UCSD (vs UAB) | +0.2170 | 0.5592 | ±1.1184 | +0.388 | 0.6980 |  |
| Site: UW (vs UAB) | -0.3191 | 0.5024 | ±1.0049 | -0.635 | 0.5254 |  |
| **Age (years)** | **-0.1229** | 0.0207 | ±0.0414 | **-5.929** | **3.06e-09** | *** |
| BMI (kg/m2) | +0.0397 | 0.0311 | ±0.0622 | +1.277 | 0.2016 |  |
| Hypertension | +0.1879 | 0.4642 | ±0.9284 | +0.405 | 0.6856 |  |
| High cholesterol | +0.3981 | 0.4635 | ±0.9270 | +0.859 | 0.3904 |  |
| Kidney disease | +0.7841 | 0.5700 | ±1.1400 | +1.376 | 0.1689 |  |
| **Circulatory disease** | **+2.0010** | 0.5930 | ±1.1860 | **+3.374** | **7.40e-04** | *** |
| Time 54-69, pooled (%) | +0.4327 | 0.2659 | ±0.5317 | +1.627 | 0.1037 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **550**, R² = **0.1530**, Adj R² = **0.1357**, F-statistic = **8.83** (p = **1.62e-14**), Residual SE = **4.862** on **538** df, AIC = **3312.2**, BIC = **3363.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7656** | 1.8732 | ±3.7465 | **+6.281** | **3.37e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4047** | 0.4456 | ±0.8913 | **-3.152** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1832 | 0.6854 | ±1.3709 | +1.726 | 0.0843 | . |
| Site: UCSD (vs UAB) | +0.2363 | 0.5593 | ±1.1186 | +0.423 | 0.6726 |  |
| Site: UW (vs UAB) | -0.2869 | 0.5005 | ±1.0011 | -0.573 | 0.5665 |  |
| **Age (years)** | **-0.1235** | 0.0207 | ±0.0414 | **-5.960** | **2.52e-09** | *** |
| BMI (kg/m2) | +0.0388 | 0.0311 | ±0.0623 | +1.247 | 0.2122 |  |
| Hypertension | +0.1698 | 0.4635 | ±0.9270 | +0.366 | 0.7142 |  |
| High cholesterol | +0.4182 | 0.4613 | ±0.9225 | +0.907 | 0.3646 |  |
| Kidney disease | +0.7813 | 0.5678 | ±1.1357 | +1.376 | 0.1688 |  |
| **Circulatory disease** | **+2.0217** | 0.5914 | ±1.1828 | **+3.419** | **6.30e-04** | *** |
| **Avg. daily time 54-69 (%)** | **+0.4969** | 0.2172 | ±0.4343 | **+2.288** | **0.0221** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **550**, R² = **0.1501**, Adj R² = **0.1327**, F-statistic = **8.64** (p = **3.73e-14**), Residual SE = **4.870** on **538** df, AIC = **3314.1**, BIC = **3365.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7423** | 1.8775 | ±3.7550 | **+6.254** | **4.00e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4157** | 0.4464 | ±0.8928 | **-3.171** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1797 | 0.6854 | ±1.3708 | +1.721 | 0.0852 | . |
| Site: UCSD (vs UAB) | +0.2160 | 0.5589 | ±1.1179 | +0.386 | 0.6992 |  |
| Site: UW (vs UAB) | -0.3145 | 0.5017 | ±1.0033 | -0.627 | 0.5307 |  |
| **Age (years)** | **-0.1228** | 0.0207 | ±0.0414 | **-5.925** | **3.13e-09** | *** |
| BMI (kg/m2) | +0.0393 | 0.0312 | ±0.0624 | +1.261 | 0.2072 |  |
| Hypertension | +0.1816 | 0.4654 | ±0.9308 | +0.390 | 0.6964 |  |
| High cholesterol | +0.3995 | 0.4641 | ±0.9282 | +0.861 | 0.3894 |  |
| Kidney disease | +0.7901 | 0.5702 | ±1.1404 | +1.386 | 0.1658 |  |
| **Circulatory disease** | **+2.0048** | 0.5913 | ±1.1825 | **+3.391** | **6.97e-04** | *** |
| Time < 70 (%) | +0.3467 | 0.2163 | ±0.4325 | +1.603 | 0.1089 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **550**, R² = **0.1522**, Adj R² = **0.1349**, F-statistic = **8.78** (p = **2.01e-14**), Residual SE = **4.864** on **538** df, AIC = **3312.7**, BIC = **3364.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7814** | 1.8767 | ±3.7533 | **+6.278** | **3.43e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4063** | 0.4455 | ±0.8910 | **-3.157** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1920 | 0.6852 | ±1.3704 | +1.740 | 0.0819 | . |
| Site: UCSD (vs UAB) | +0.2284 | 0.5590 | ±1.1180 | +0.408 | 0.6829 |  |
| Site: UW (vs UAB) | -0.2908 | 0.5000 | ±0.9999 | -0.582 | 0.5608 |  |
| **Age (years)** | **-0.1232** | 0.0207 | ±0.0414 | **-5.945** | **2.77e-09** | *** |
| BMI (kg/m2) | +0.0383 | 0.0312 | ±0.0624 | +1.227 | 0.2199 |  |
| Hypertension | +0.1717 | 0.4641 | ±0.9283 | +0.370 | 0.7115 |  |
| High cholesterol | +0.4154 | 0.4622 | ±0.9244 | +0.899 | 0.3688 |  |
| Kidney disease | +0.7842 | 0.5684 | ±1.1368 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+2.0175** | 0.5902 | ±1.1805 | **+3.418** | **6.31e-04** | *** |
| **Avg. daily time < 70 (%)** | **+0.3737** | 0.1632 | ±0.3264 | **+2.290** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **550**, R² = **0.1496**, Adj R² = **0.1322**, F-statistic = **8.60** (p = **4.31e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.4**, BIC = **3366.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.4986** | 2.1956 | ±4.3911 | **+6.148** | **7.84e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3811** | 0.4474 | ±0.8948 | **-3.087** | **0.0020** | ** |
| Education: high school or below (vs college) | +1.0730 | 0.6790 | ±1.3579 | +1.580 | 0.1140 |  |
| Site: UCSD (vs UAB) | +0.1856 | 0.5580 | ±1.1159 | +0.333 | 0.7394 |  |
| Site: UW (vs UAB) | -0.3262 | 0.5051 | ±1.0102 | -0.646 | 0.5184 |  |
| **Age (years)** | **-0.1183** | 0.0208 | ±0.0415 | **-5.701** | **1.19e-08** | *** |
| BMI (kg/m2) | +0.0348 | 0.0313 | ±0.0627 | +1.111 | 0.2667 |  |
| Hypertension | +0.2409 | 0.4629 | ±0.9258 | +0.520 | 0.6028 |  |
| High cholesterol | +0.3422 | 0.4614 | ±0.9228 | +0.742 | 0.4582 |  |
| Kidney disease | +0.7919 | 0.5739 | ±1.1478 | +1.380 | 0.1676 |  |
| **Circulatory disease** | **+1.9147** | 0.5885 | ±1.1770 | **+3.253** | **0.0011** | ** |
| Time 54-250, pooled (%) | -0.0193 | 0.0142 | ±0.0284 | -1.361 | 0.1736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **550**, R² = **0.1488**, Adj R² = **0.1314**, F-statistic = **8.55** (p = **5.35e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.9**, BIC = **3366.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.3988** | 2.2272 | ±4.4543 | **+6.016** | **1.79e-09** | *** |
| **Education: graduate level (vs college)** | **-1.3866** | 0.4473 | ±0.8946 | **-3.100** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0813 | 0.6795 | ±1.3590 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +0.1804 | 0.5586 | ±1.1171 | +0.323 | 0.7467 |  |
| Site: UW (vs UAB) | -0.3369 | 0.5048 | ±1.0095 | -0.667 | 0.5045 |  |
| **Age (years)** | **-0.1190** | 0.0207 | ±0.0415 | **-5.739** | **9.50e-09** | *** |
| BMI (kg/m2) | +0.0350 | 0.0314 | ±0.0627 | +1.116 | 0.2644 |  |
| Hypertension | +0.2456 | 0.4632 | ±0.9264 | +0.530 | 0.5959 |  |
| High cholesterol | +0.3403 | 0.4619 | ±0.9238 | +0.737 | 0.4613 |  |
| Kidney disease | +0.7902 | 0.5738 | ±1.1475 | +1.377 | 0.1684 |  |
| **Circulatory disease** | **+1.9149** | 0.5888 | ±1.1775 | **+3.252** | **0.0011** | ** |
| Avg. daily time 54-250 (%) | -0.0177 | 0.0145 | ±0.0289 | -1.225 | 0.2204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **550**, R² = **0.1462**, Adj R² = **0.1287**, F-statistic = **8.37** (p = **1.14e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.6**, BIC = **3368.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7737** | 1.8828 | ±3.7657 | **+6.253** | **4.02e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4481** | 0.4464 | ±0.8929 | **-3.244** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1270 | 0.6884 | ±1.3767 | +1.637 | 0.1016 |  |
| Site: UCSD (vs UAB) | +0.1445 | 0.5623 | ±1.1245 | +0.257 | 0.7972 |  |
| Site: UW (vs UAB) | -0.4193 | 0.4979 | ±0.9959 | -0.842 | 0.3997 |  |
| **Age (years)** | **-0.1226** | 0.0207 | ±0.0414 | **-5.918** | **3.25e-09** | *** |
| BMI (kg/m2) | +0.0351 | 0.0310 | ±0.0620 | +1.133 | 0.2573 |  |
| Hypertension | +0.2978 | 0.4647 | ±0.9294 | +0.641 | 0.5217 |  |
| High cholesterol | +0.3380 | 0.4623 | ±0.9247 | +0.731 | 0.4648 |  |
| Kidney disease | +0.8232 | 0.5715 | ±1.1430 | +1.440 | 0.1498 |  |
| **Circulatory disease** | **+1.9280** | 0.5836 | ±1.1673 | **+3.303** | **9.55e-04** | *** |
| Time 181-250, pooled (%) | +0.0111 | 0.0141 | ±0.0282 | +0.785 | 0.4322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **550**, R² = **0.1462**, Adj R² = **0.1287**, F-statistic = **8.37** (p = **1.14e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.6**, BIC = **3368.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7720** | 1.8831 | ±3.7663 | **+6.251** | **4.07e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4501** | 0.4466 | ±0.8932 | **-3.247** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1226 | 0.6894 | ±1.3788 | +1.628 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.1472 | 0.5618 | ±1.1237 | +0.262 | 0.7933 |  |
| Site: UW (vs UAB) | -0.4164 | 0.4981 | ±0.9962 | -0.836 | 0.4032 |  |
| **Age (years)** | **-0.1225** | 0.0207 | ±0.0414 | **-5.913** | **3.35e-09** | *** |
| BMI (kg/m2) | +0.0350 | 0.0310 | ±0.0620 | +1.130 | 0.2587 |  |
| Hypertension | +0.2969 | 0.4639 | ±0.9279 | +0.640 | 0.5222 |  |
| High cholesterol | +0.3370 | 0.4623 | ±0.9247 | +0.729 | 0.4660 |  |
| Kidney disease | +0.8217 | 0.5716 | ±1.1432 | +1.438 | 0.1505 |  |
| **Circulatory disease** | **+1.9293** | 0.5842 | ±1.1684 | **+3.302** | **9.59e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0108 | 0.0139 | ±0.0277 | +0.780 | 0.4352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **550**, R² = **0.1492**, Adj R² = **0.1319**, F-statistic = **8.58** (p = **4.75e-14**), Residual SE = **4.872** on **538** df, AIC = **3314.6**, BIC = **3366.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4960** | 1.8913 | ±3.7827 | **+6.078** | **1.22e-09** | *** |
| **Education: graduate level (vs college)** | **-1.4115** | 0.4466 | ±0.8933 | **-3.160** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0623 | 0.6814 | ±1.3627 | +1.559 | 0.1190 |  |
| Site: UCSD (vs UAB) | +0.1949 | 0.5597 | ±1.1193 | +0.348 | 0.7277 |  |
| Site: UW (vs UAB) | -0.3602 | 0.5004 | ±1.0007 | -0.720 | 0.4717 |  |
| **Age (years)** | **-0.1203** | 0.0207 | ±0.0414 | **-5.815** | **6.05e-09** | *** |
| BMI (kg/m2) | +0.0326 | 0.0311 | ±0.0622 | +1.049 | 0.2940 |  |
| Hypertension | +0.2866 | 0.4624 | ±0.9249 | +0.620 | 0.5354 |  |
| High cholesterol | +0.3533 | 0.4615 | ±0.9230 | +0.766 | 0.4440 |  |
| Kidney disease | +0.7955 | 0.5759 | ±1.1518 | +1.381 | 0.1672 |  |
| **Circulatory disease** | **+1.9013** | 0.5846 | ±1.1693 | **+3.252** | **0.0011** | ** |
| Time > 180 (%) | +0.0130 | 0.0086 | ±0.0173 | +1.506 | 0.1320 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **550**, R² = **0.1486**, Adj R² = **0.1312**, F-statistic = **8.54** (p = **5.65e-14**), Residual SE = **4.874** on **538** df, AIC = **3315.0**, BIC = **3366.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5472** | 1.8896 | ±3.7792 | **+6.111** | **9.91e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4166** | 0.4466 | ±0.8932 | **-3.172** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.0655 | 0.6823 | ±1.3646 | +1.562 | 0.1184 |  |
| Site: UCSD (vs UAB) | +0.1923 | 0.5598 | ±1.1196 | +0.344 | 0.7312 |  |
| Site: UW (vs UAB) | -0.3641 | 0.5002 | ±1.0003 | -0.728 | 0.4667 |  |
| **Age (years)** | **-0.1205** | 0.0207 | ±0.0414 | **-5.826** | **5.66e-09** | *** |
| BMI (kg/m2) | +0.0329 | 0.0312 | ±0.0624 | +1.056 | 0.2910 |  |
| Hypertension | +0.2865 | 0.4626 | ±0.9252 | +0.619 | 0.5357 |  |
| High cholesterol | +0.3497 | 0.4619 | ±0.9237 | +0.757 | 0.4490 |  |
| Kidney disease | +0.7936 | 0.5755 | ±1.1510 | +1.379 | 0.1679 |  |
| **Circulatory disease** | **+1.9045** | 0.5851 | ±1.1702 | **+3.255** | **0.0011** | ** |
| Avg. daily time > 180 (%) | +0.0119 | 0.0086 | ±0.0173 | +1.381 | 0.1674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **550**, R² = **0.1504**, Adj R² = **0.1331**, F-statistic = **8.66** (p = **3.39e-14**), Residual SE = **4.869** on **538** df, AIC = **3313.8**, BIC = **3365.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5597** | 1.8788 | ±3.7577 | **+6.153** | **7.63e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3807** | 0.4479 | ±0.8958 | **-3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0689 | 0.6792 | ±1.3584 | +1.574 | 0.1155 |  |
| Site: UCSD (vs UAB) | +0.2176 | 0.5574 | ±1.1149 | +0.390 | 0.6963 |  |
| Site: UW (vs UAB) | -0.3729 | 0.4992 | ±0.9985 | -0.747 | 0.4551 |  |
| **Age (years)** | **-0.1187** | 0.0208 | ±0.0415 | **-5.718** | **1.08e-08** | *** |
| BMI (kg/m2) | +0.0294 | 0.0314 | ±0.0628 | +0.936 | 0.3493 |  |
| Hypertension | +0.2890 | 0.4619 | ±0.9239 | +0.626 | 0.5315 |  |
| High cholesterol | +0.3704 | 0.4608 | ±0.9217 | +0.804 | 0.4216 |  |
| Kidney disease | +0.7960 | 0.5745 | ±1.1491 | +1.386 | 0.1659 |  |
| **Circulatory disease** | **+1.8924** | 0.5846 | ±1.1693 | **+3.237** | **0.0012** | ** |
| Nocturnal time > 180 (%) | +0.0131 | 0.0075 | ±0.0150 | +1.742 | 0.0815 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **550**, R² = **0.1495**, Adj R² = **0.1321**, F-statistic = **8.60** (p = **4.39e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.4**, BIC = **3366.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5717** | 1.8961 | ±3.7923 | **+6.103** | **1.04e-09** | *** |
| **Education: graduate level (vs college)** | **-1.3819** | 0.4474 | ±0.8947 | **-3.089** | **0.0020** | ** |
| Education: high school or below (vs college) | +1.0731 | 0.6789 | ±1.3579 | +1.581 | 0.1140 |  |
| Site: UCSD (vs UAB) | +0.1840 | 0.5580 | ±1.1160 | +0.330 | 0.7416 |  |
| Site: UW (vs UAB) | -0.3282 | 0.5049 | ±1.0099 | -0.650 | 0.5157 |  |
| **Age (years)** | **-0.1183** | 0.0208 | ±0.0415 | **-5.702** | **1.18e-08** | *** |
| BMI (kg/m2) | +0.0348 | 0.0313 | ±0.0627 | +1.112 | 0.2663 |  |
| Hypertension | +0.2423 | 0.4629 | ±0.9258 | +0.523 | 0.6007 |  |
| High cholesterol | +0.3412 | 0.4614 | ±0.9227 | +0.739 | 0.4596 |  |
| Kidney disease | +0.7924 | 0.5738 | ±1.1476 | +1.381 | 0.1673 |  |
| **Circulatory disease** | **+1.9141** | 0.5885 | ±1.1771 | **+3.252** | **0.0011** | ** |
| Time > 250 (%) | +0.0192 | 0.0142 | ±0.0284 | +1.352 | 0.1765 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **550**, R² = **0.1487**, Adj R² = **0.1313**, F-statistic = **8.54** (p = **5.52e-14**), Residual SE = **4.874** on **538** df, AIC = **3314.9**, BIC = **3366.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6338** | 1.8932 | ±3.7864 | **+6.145** | **8.00e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3877** | 0.4473 | ±0.8946 | **-3.102** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0818 | 0.6795 | ±1.3590 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1784 | 0.5586 | ±1.1172 | +0.319 | 0.7494 |  |
| Site: UW (vs UAB) | -0.3395 | 0.5046 | ±1.0092 | -0.673 | 0.5011 |  |
| **Age (years)** | **-0.1190** | 0.0207 | ±0.0415 | **-5.742** | **9.35e-09** | *** |
| BMI (kg/m2) | +0.0351 | 0.0314 | ±0.0627 | +1.118 | 0.2635 |  |
| Hypertension | +0.2470 | 0.4632 | ±0.9265 | +0.533 | 0.5939 |  |
| High cholesterol | +0.3390 | 0.4619 | ±0.9238 | +0.734 | 0.4629 |  |
| Kidney disease | +0.7913 | 0.5736 | ±1.1472 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+1.9148** | 0.5888 | ±1.1776 | **+3.252** | **0.0011** | ** |
| Avg. daily time > 250 (%) | +0.0174 | 0.0144 | ±0.0289 | +1.208 | 0.2272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 550; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0836**, LLR χ² = **47.80** (p = **6.76e-07**), AUC = **0.6958**, AIC = **546.1**, BIC = **593.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3288 | 0.9419 | ±1.8838 | +0.349 | 0.7270 | 1.3893 |  |
| Education: graduate level (vs college) | -0.4556 | 0.2774 | ±0.5549 | -1.642 | 0.1005 | 0.6341 |  |
| Education: high school or below (vs college) | +0.1559 | 0.2820 | ±0.5640 | +0.553 | 0.5803 | 1.1688 |  |
| Site: UCSD (vs UAB) | -0.1128 | 0.2777 | ±0.5555 | -0.406 | 0.6847 | 0.8933 |  |
| Site: UW (vs UAB) | -0.1774 | 0.2676 | ±0.5353 | -0.663 | 0.5075 | 0.8375 |  |
| **Age (years)** | **-0.0454** | 0.0117 | ±0.0234 | **-3.882** | **1.04e-04** | 0.9556 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0294 | +1.639 | 0.1012 | 1.0243 |  |
| Hypertension | +0.2948 | 0.2627 | ±0.5254 | +1.122 | 0.2618 | 1.3428 |  |
| High cholesterol | +0.2010 | 0.2431 | ±0.4862 | +0.827 | 0.4084 | 1.2226 |  |
| Kidney disease | +0.3505 | 0.2689 | ±0.5379 | +1.303 | 0.1925 | 1.4198 |  |
| **Circulatory disease** | **+0.7290** | 0.2578 | ±0.5157 | **+2.827** | **0.0047** | 2.0729 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0931**, LLR χ² = **53.24** (p = **1.62e-07**), AUC = **0.7067**, AIC = **542.7**, BIC = **594.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9497 | 1.0962 | ±2.1924 | -0.866 | 0.3863 | 0.3869 |  |
| Education: graduate level (vs college) | -0.4142 | 0.2790 | ±0.5580 | -1.485 | 0.1376 | 0.6609 |  |
| Education: high school or below (vs college) | +0.0746 | 0.2878 | ±0.5757 | +0.259 | 0.7956 | 1.0774 |  |
| Site: UCSD (vs UAB) | -0.0649 | 0.2810 | ±0.5619 | -0.231 | 0.8174 | 0.9372 |  |
| Site: UW (vs UAB) | -0.1024 | 0.2713 | ±0.5426 | -0.377 | 0.7058 | 0.9027 |  |
| **Age (years)** | **-0.0431** | 0.0118 | ±0.0236 | **-3.658** | **2.54e-04** | 0.9578 | *** |
| BMI (kg/m2) | +0.0202 | 0.0149 | ±0.0297 | +1.362 | 0.1732 | 1.0204 |  |
| Hypertension | +0.2842 | 0.2650 | ±0.5300 | +1.073 | 0.2834 | 1.3288 |  |
| High cholesterol | +0.1986 | 0.2445 | ±0.4889 | +0.812 | 0.4165 | 1.2197 |  |
| Kidney disease | +0.3789 | 0.2706 | ±0.5412 | +1.400 | 0.1615 | 1.4607 |  |
| **Circulatory disease** | **+0.7218** | 0.2589 | ±0.5177 | **+2.788** | **0.0053** | 2.0581 | ** |
| **HbA1c (%)** | **+0.1702** | 0.0723 | ±0.1446 | **+2.355** | **0.0185** | 1.1856 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0869**, LLR χ² = **49.68** (p = **7.14e-07**), AUC = **0.7016**, AIC = **546.2**, BIC = **597.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3288 | 1.0572 | ±2.1144 | -0.311 | 0.7558 | 0.7198 |  |
| Education: graduate level (vs college) | -0.4295 | 0.2784 | ±0.5568 | -1.543 | 0.1229 | 0.6508 |  |
| Education: high school or below (vs college) | +0.1184 | 0.2846 | ±0.5691 | +0.416 | 0.6774 | 1.1257 |  |
| Site: UCSD (vs UAB) | -0.0778 | 0.2796 | ±0.5591 | -0.278 | 0.7809 | 0.9252 |  |
| Site: UW (vs UAB) | -0.1404 | 0.2696 | ±0.5392 | -0.521 | 0.6025 | 0.8690 |  |
| **Age (years)** | **-0.0439** | 0.0117 | ±0.0234 | **-3.746** | **1.80e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0227 | 0.0148 | ±0.0295 | +1.535 | 0.1248 | 1.0229 |  |
| Hypertension | +0.2929 | 0.2633 | ±0.5266 | +1.113 | 0.2659 | 1.3404 |  |
| High cholesterol | +0.2035 | 0.2435 | ±0.4870 | +0.836 | 0.4034 | 1.2256 |  |
| Kidney disease | +0.3483 | 0.2694 | ±0.5387 | +1.293 | 0.1959 | 1.4167 |  |
| **Circulatory disease** | **+0.7155** | 0.2579 | ±0.5159 | **+2.774** | **0.0055** | 2.0452 | ** |
| Mean glucose (mg/dL) | +0.0034 | 0.0025 | ±0.0049 | +1.382 | 0.1669 | 1.0034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0869**, LLR χ² = **49.68** (p = **7.14e-07**), AUC = **0.7016**, AIC = **546.2**, BIC = **597.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8010 | 1.2494 | ±2.4987 | -0.641 | 0.5214 | 0.4489 |  |
| Education: graduate level (vs college) | -0.4295 | 0.2784 | ±0.5568 | -1.543 | 0.1229 | 0.6508 |  |
| Education: high school or below (vs college) | +0.1184 | 0.2846 | ±0.5691 | +0.416 | 0.6774 | 1.1257 |  |
| Site: UCSD (vs UAB) | -0.0778 | 0.2796 | ±0.5591 | -0.278 | 0.7809 | 0.9252 |  |
| Site: UW (vs UAB) | -0.1404 | 0.2696 | ±0.5392 | -0.521 | 0.6025 | 0.8690 |  |
| **Age (years)** | **-0.0439** | 0.0117 | ±0.0234 | **-3.746** | **1.80e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0227 | 0.0148 | ±0.0295 | +1.535 | 0.1248 | 1.0229 |  |
| Hypertension | +0.2929 | 0.2633 | ±0.5266 | +1.113 | 0.2659 | 1.3404 |  |
| High cholesterol | +0.2035 | 0.2435 | ±0.4870 | +0.836 | 0.4034 | 1.2256 |  |
| Kidney disease | +0.3483 | 0.2694 | ±0.5387 | +1.293 | 0.1959 | 1.4167 |  |
| **Circulatory disease** | **+0.7155** | 0.2579 | ±0.5159 | **+2.774** | **0.0055** | 2.0452 | ** |
| GMI (%) | +0.1427 | 0.1032 | ±0.2064 | +1.382 | 0.1669 | 1.1533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0901**, LLR χ² = **51.53** (p = **3.31e-07**), AUC = **0.7067**, AIC = **544.4**, BIC = **596.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5122 | 1.0387 | ±2.0774 | -0.493 | 0.6219 | 0.5992 |  |
| Education: graduate level (vs college) | -0.4077 | 0.2792 | ±0.5585 | -1.460 | 0.1443 | 0.6652 |  |
| Education: high school or below (vs college) | +0.1152 | 0.2850 | ±0.5699 | +0.404 | 0.6861 | 1.1221 |  |
| Site: UCSD (vs UAB) | -0.0601 | 0.2804 | ±0.5607 | -0.214 | 0.8304 | 0.9417 |  |
| Site: UW (vs UAB) | -0.1462 | 0.2693 | ±0.5387 | -0.543 | 0.5873 | 0.8640 |  |
| **Age (years)** | **-0.0430** | 0.0117 | ±0.0235 | **-3.658** | **2.54e-04** | 0.9579 | *** |
| BMI (kg/m2) | +0.0211 | 0.0148 | ±0.0297 | +1.426 | 0.1540 | 1.0214 |  |
| Hypertension | +0.2986 | 0.2640 | ±0.5280 | +1.131 | 0.2580 | 1.3480 |  |
| High cholesterol | +0.2112 | 0.2443 | ±0.4887 | +0.865 | 0.3873 | 1.2352 |  |
| Kidney disease | +0.3606 | 0.2698 | ±0.5396 | +1.336 | 0.1814 | 1.4341 |  |
| **Circulatory disease** | **+0.7123** | 0.2582 | ±0.5164 | **+2.759** | **0.0058** | 2.0387 | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0045 | 0.0023 | ±0.0046 | +1.946 | 0.0516 | 1.0045 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0994**, LLR χ² = **56.85** (p = **3.55e-08**), AUC = **0.7135**, AIC = **539.1**, BIC = **590.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8584 | 1.0269 | ±2.0537 | -0.836 | 0.4032 | 0.4238 |  |
| Education: graduate level (vs college) | -0.4000 | 0.2804 | ±0.5608 | -1.427 | 0.1537 | 0.6703 |  |
| Education: high school or below (vs college) | +0.0679 | 0.2875 | ±0.5749 | +0.236 | 0.8133 | 1.0702 |  |
| Site: UCSD (vs UAB) | -0.0919 | 0.2812 | ±0.5623 | -0.327 | 0.7438 | 0.9122 |  |
| Site: UW (vs UAB) | -0.0738 | 0.2720 | ±0.5440 | -0.271 | 0.7861 | 0.9288 |  |
| **Age (years)** | **-0.0433** | 0.0117 | ±0.0234 | **-3.701** | **2.15e-04** | 0.9576 | *** |
| BMI (kg/m2) | +0.0218 | 0.0149 | ±0.0297 | +1.469 | 0.1419 | 1.0221 |  |
| Hypertension | +0.2837 | 0.2654 | ±0.5309 | +1.069 | 0.2852 | 1.3280 |  |
| High cholesterol | +0.2229 | 0.2455 | ±0.4911 | +0.908 | 0.3639 | 1.2497 |  |
| Kidney disease | +0.2061 | 0.2766 | ±0.5531 | +0.745 | 0.4561 | 1.2289 |  |
| **Circulatory disease** | **+0.7205** | 0.2600 | ±0.5201 | **+2.771** | **0.0056** | 2.0554 | ** |
| **Glucose SD, pooled (mg/dL)** | **+0.0261** | 0.0087 | ±0.0175 | **+2.995** | **0.0027** | 1.0265 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0923**, LLR χ² = **52.77** (p = **1.97e-07**), AUC = **0.7060**, AIC = **543.1**, BIC = **594.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5850 | 1.0310 | ±2.0619 | -0.567 | 0.5704 | 0.5571 |  |
| Education: graduate level (vs college) | -0.4192 | 0.2791 | ±0.5583 | -1.502 | 0.1332 | 0.6576 |  |
| Education: high school or below (vs college) | +0.0771 | 0.2865 | ±0.5730 | +0.269 | 0.7878 | 1.0802 |  |
| Site: UCSD (vs UAB) | -0.0990 | 0.2795 | ±0.5591 | -0.354 | 0.7234 | 0.9058 |  |
| Site: UW (vs UAB) | -0.1107 | 0.2705 | ±0.5410 | -0.409 | 0.6823 | 0.8952 |  |
| **Age (years)** | **-0.0442** | 0.0117 | ±0.0234 | **-3.775** | **1.60e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0239 | 0.0148 | ±0.0295 | +1.621 | 0.1050 | 1.0242 |  |
| Hypertension | +0.2948 | 0.2640 | ±0.5280 | +1.117 | 0.2642 | 1.3428 |  |
| High cholesterol | +0.2146 | 0.2444 | ±0.4887 | +0.878 | 0.3799 | 1.2394 |  |
| Kidney disease | +0.2317 | 0.2763 | ±0.5527 | +0.838 | 0.4018 | 1.2607 |  |
| **Circulatory disease** | **+0.7301** | 0.2590 | ±0.5179 | **+2.819** | **0.0048** | 2.0754 | ** |
| **Avg. daily SD (mg/dL)** | **+0.0222** | 0.0099 | ±0.0199 | **+2.234** | **0.0255** | 1.0224 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0908**, LLR χ² = **51.95** (p = **2.78e-07**), AUC = **0.7053**, AIC = **544.0**, BIC = **595.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6396 | 1.0546 | ±2.1091 | -0.606 | 0.5442 | 0.5275 |  |
| Education: graduate level (vs college) | -0.4459 | 0.2790 | ±0.5579 | -1.599 | 0.1099 | 0.6402 |  |
| Education: high school or below (vs college) | +0.1254 | 0.2839 | ±0.5678 | +0.442 | 0.6587 | 1.1336 |  |
| Site: UCSD (vs UAB) | -0.1322 | 0.2790 | ±0.5580 | -0.474 | 0.6355 | 0.8761 |  |
| Site: UW (vs UAB) | -0.1379 | 0.2695 | ±0.5390 | -0.512 | 0.6089 | 0.8712 |  |
| **Age (years)** | **-0.0457** | 0.0117 | ±0.0234 | **-3.902** | **9.54e-05** | 0.9553 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0295 | +1.638 | 0.1013 | 1.0244 |  |
| Hypertension | +0.2777 | 0.2637 | ±0.5274 | +1.053 | 0.2923 | 1.3201 |  |
| High cholesterol | +0.2134 | 0.2441 | ±0.4881 | +0.875 | 0.3818 | 1.2379 |  |
| Kidney disease | +0.2195 | 0.2790 | ±0.5579 | +0.787 | 0.4314 | 1.2454 |  |
| **Circulatory disease** | **+0.7435** | 0.2597 | ±0.5193 | **+2.863** | **0.0042** | 2.1033 | ** |
| **CV (%)** | **+0.0406** | 0.0199 | ±0.0398 | **+2.042** | **0.0411** | 1.0414 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0896**, LLR χ² = **51.26** (p = **3.71e-07**), AUC = **0.7028**, AIC = **544.6**, BIC = **596.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.2547 | 1.0758 | ±2.1515 | +1.166 | 0.2435 | 3.5067 |  |
| Education: graduate level (vs college) | -0.4428 | 0.2789 | ±0.5577 | -1.588 | 0.1123 | 0.6422 |  |
| Education: high school or below (vs college) | +0.1367 | 0.2835 | ±0.5670 | +0.482 | 0.6298 | 1.1465 |  |
| Site: UCSD (vs UAB) | -0.1409 | 0.2793 | ±0.5587 | -0.504 | 0.6140 | 0.8686 |  |
| Site: UW (vs UAB) | -0.1477 | 0.2692 | ±0.5384 | -0.549 | 0.5831 | 0.8626 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0235 | **-3.877** | **1.06e-04** | 0.9555 | *** |
| BMI (kg/m2) | +0.0246 | 0.0147 | ±0.0295 | +1.667 | 0.0956 | 1.0249 | . |
| Hypertension | +0.2916 | 0.2633 | ±0.5267 | +1.107 | 0.2682 | 1.3386 |  |
| High cholesterol | +0.1978 | 0.2438 | ±0.4875 | +0.811 | 0.4172 | 1.2187 |  |
| Kidney disease | +0.2511 | 0.2761 | ±0.5522 | +0.910 | 0.3631 | 1.2855 |  |
| **Circulatory disease** | **+0.7254** | 0.2595 | ±0.5190 | **+2.795** | **0.0052** | 2.0656 | ** |
| Mean / SD ratio | -0.2158 | 0.1187 | ±0.2373 | -1.818 | 0.0690 | 0.8059 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0848**, LLR χ² = **48.52** (p = **1.15e-06**), AUC = **0.6980**, AIC = **547.4**, BIC = **599.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7054 | 1.0442 | ±2.0883 | +0.676 | 0.4993 | 2.0246 |  |
| Education: graduate level (vs college) | -0.4484 | 0.2780 | ±0.5560 | -1.613 | 0.1067 | 0.6386 |  |
| Education: high school or below (vs college) | +0.1450 | 0.2826 | ±0.5652 | +0.513 | 0.6079 | 1.1560 |  |
| Site: UCSD (vs UAB) | -0.1273 | 0.2785 | ±0.5570 | -0.457 | 0.6476 | 0.8805 |  |
| Site: UW (vs UAB) | -0.1717 | 0.2680 | ±0.5359 | -0.641 | 0.5216 | 0.8422 |  |
| **Age (years)** | **-0.0456** | 0.0117 | ±0.0234 | **-3.892** | **9.94e-05** | 0.9554 | *** |
| BMI (kg/m2) | +0.0250 | 0.0147 | ±0.0295 | +1.697 | 0.0897 | 1.0253 | . |
| Hypertension | +0.2957 | 0.2627 | ±0.5254 | +1.126 | 0.2603 | 1.3441 |  |
| High cholesterol | +0.2013 | 0.2432 | ±0.4864 | +0.828 | 0.4079 | 1.2230 |  |
| Kidney disease | +0.3088 | 0.2740 | ±0.5480 | +1.127 | 0.2597 | 1.3618 |  |
| **Circulatory disease** | **+0.7311** | 0.2585 | ±0.5169 | **+2.829** | **0.0047** | 2.0774 | ** |
| Avg. daily mean/SD | -0.0773 | 0.0919 | ±0.1839 | -0.841 | 0.4003 | 0.9256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0941**, LLR χ² = **53.80** (p = **1.28e-07**), AUC = **0.7036**, AIC = **542.1**, BIC = **593.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1730 | 1.1312 | ±2.2624 | -1.037 | 0.2998 | 0.3094 |  |
| Education: graduate level (vs college) | -0.4064 | 0.2796 | ±0.5592 | -1.454 | 0.1460 | 0.6660 |  |
| Education: high school or below (vs college) | +0.0830 | 0.2877 | ±0.5755 | +0.288 | 0.7730 | 1.0866 |  |
| Site: UCSD (vs UAB) | -0.0979 | 0.2798 | ±0.5595 | -0.350 | 0.7263 | 0.9067 |  |
| Site: UW (vs UAB) | -0.0685 | 0.2727 | ±0.5453 | -0.251 | 0.8015 | 0.9337 |  |
| **Age (years)** | **-0.0418** | 0.0118 | ±0.0237 | **-3.533** | **4.11e-04** | 0.9590 | *** |
| BMI (kg/m2) | +0.0245 | 0.0148 | ±0.0297 | +1.651 | 0.0986 | 1.0248 | . |
| Hypertension | +0.2994 | 0.2655 | ±0.5310 | +1.127 | 0.2595 | 1.3490 |  |
| High cholesterol | +0.2070 | 0.2449 | ±0.4897 | +0.845 | 0.3980 | 1.2299 |  |
| Kidney disease | +0.2908 | 0.2723 | ±0.5445 | +1.068 | 0.2855 | 1.3375 |  |
| **Circulatory disease** | **+0.7248** | 0.2596 | ±0.5192 | **+2.792** | **0.0052** | 2.0644 | ** |
| **MAG (mg/dL/h)** | **+0.0264** | 0.0108 | ±0.0215 | **+2.455** | **0.0141** | 1.0267 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0919**, LLR χ² = **52.56** (p = **2.15e-07**), AUC = **0.7053**, AIC = **543.3**, BIC = **595.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8795 | 1.0976 | ±2.1951 | -0.801 | 0.4230 | 0.4150 |  |
| Education: graduate level (vs college) | -0.4153 | 0.2791 | ±0.5582 | -1.488 | 0.1367 | 0.6601 |  |
| Education: high school or below (vs college) | +0.0718 | 0.2870 | ±0.5740 | +0.250 | 0.8026 | 1.0744 |  |
| Site: UCSD (vs UAB) | -0.0955 | 0.2793 | ±0.5587 | -0.342 | 0.7326 | 0.9090 |  |
| Site: UW (vs UAB) | -0.1190 | 0.2702 | ±0.5403 | -0.440 | 0.6597 | 0.8878 |  |
| **Age (years)** | **-0.0434** | 0.0118 | ±0.0235 | **-3.691** | **2.23e-04** | 0.9575 | *** |
| BMI (kg/m2) | +0.0246 | 0.0148 | ±0.0295 | +1.669 | 0.0951 | 1.0249 | . |
| Hypertension | +0.3120 | 0.2643 | ±0.5287 | +1.180 | 0.2379 | 1.3661 |  |
| High cholesterol | +0.2001 | 0.2442 | ±0.4884 | +0.819 | 0.4126 | 1.2215 |  |
| Kidney disease | +0.2238 | 0.2774 | ±0.5548 | +0.807 | 0.4198 | 1.2509 |  |
| **Circulatory disease** | **+0.7224** | 0.2592 | ±0.5184 | **+2.787** | **0.0053** | 2.0594 | ** |
| **Avg. daily range (mg/dL)** | **+0.0065** | 0.0030 | ±0.0060 | **+2.186** | **0.0288** | 1.0065 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.1133**, LLR χ² = **64.82** (p = **1.16e-09**), AUC = **0.7327**, AIC = **531.1**, BIC = **582.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6676 | 0.9717 | ±1.9433 | -0.687 | 0.4920 | 0.5129 |  |
| Education: graduate level (vs college) | -0.3653 | 0.2831 | ±0.5661 | -1.290 | 0.1969 | 0.6940 |  |
| Education: high school or below (vs college) | +0.1373 | 0.2886 | ±0.5773 | +0.476 | 0.6342 | 1.1472 |  |
| Site: UCSD (vs UAB) | -0.0841 | 0.2849 | ±0.5699 | -0.295 | 0.7679 | 0.9193 |  |
| Site: UW (vs UAB) | -0.0441 | 0.2739 | ±0.5478 | -0.161 | 0.8721 | 0.9569 |  |
| **Age (years)** | **-0.0399** | 0.0116 | ±0.0233 | **-3.432** | **5.99e-04** | 0.9609 | *** |
| BMI (kg/m2) | +0.0193 | 0.0151 | ±0.0301 | +1.283 | 0.1996 | 1.0195 |  |
| Hypertension | +0.2392 | 0.2689 | ±0.5378 | +0.890 | 0.3736 | 1.2703 |  |
| High cholesterol | +0.2352 | 0.2487 | ±0.4975 | +0.946 | 0.3444 | 1.2652 |  |
| Kidney disease | +0.2859 | 0.2758 | ±0.5515 | +1.037 | 0.2999 | 1.3309 |  |
| **Circulatory disease** | **+0.6489** | 0.2641 | ±0.5282 | **+2.457** | **0.0140** | 1.9135 | * |
| **SD of daily means (mg/dL)** | **+0.0494** | 0.0121 | ±0.0242 | **+4.085** | **4.40e-05** | 1.0506 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0890**, LLR χ² = **50.90** (p = **4.32e-07**), AUC = **0.7047**, AIC = **545.0**, BIC = **596.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7275 | 0.9698 | ±1.9397 | +0.750 | 0.4532 | 2.0700 |  |
| Education: graduate level (vs college) | -0.4257 | 0.2786 | ±0.5572 | -1.528 | 0.1265 | 0.6533 |  |
| Education: high school or below (vs college) | +0.1069 | 0.2849 | ±0.5699 | +0.375 | 0.7076 | 1.1128 |  |
| Site: UCSD (vs UAB) | -0.0600 | 0.2804 | ±0.5608 | -0.214 | 0.8306 | 0.9418 |  |
| Site: UW (vs UAB) | -0.1277 | 0.2701 | ±0.5402 | -0.473 | 0.6363 | 0.8801 |  |
| **Age (years)** | **-0.0438** | 0.0117 | ±0.0234 | **-3.743** | **1.82e-04** | 0.9572 | *** |
| BMI (kg/m2) | +0.0216 | 0.0148 | ±0.0296 | +1.458 | 0.1448 | 1.0218 |  |
| Hypertension | +0.3006 | 0.2638 | ±0.5276 | +1.140 | 0.2545 | 1.3507 |  |
| High cholesterol | +0.2136 | 0.2441 | ±0.4881 | +0.875 | 0.3814 | 1.2381 |  |
| Kidney disease | +0.3371 | 0.2698 | ±0.5397 | +1.249 | 0.2116 | 1.4009 |  |
| **Circulatory disease** | **+0.7101** | 0.2584 | ±0.5169 | **+2.747** | **0.0060** | 2.0341 | ** |
| Time in range 70-180, pooled (%) | -0.0072 | 0.0041 | ±0.0081 | -1.771 | 0.0765 | 0.9928 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0883**, LLR χ² = **50.51** (p = **5.07e-07**), AUC = **0.7041**, AIC = **545.4**, BIC = **597.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7133 | 0.9713 | ±1.9426 | +0.734 | 0.4627 | 2.0406 |  |
| Education: graduate level (vs college) | -0.4296 | 0.2784 | ±0.5569 | -1.543 | 0.1228 | 0.6507 |  |
| Education: high school or below (vs college) | +0.1072 | 0.2850 | ±0.5699 | +0.376 | 0.7068 | 1.1132 |  |
| Site: UCSD (vs UAB) | -0.0612 | 0.2804 | ±0.5608 | -0.218 | 0.8273 | 0.9406 |  |
| Site: UW (vs UAB) | -0.1307 | 0.2700 | ±0.5400 | -0.484 | 0.6282 | 0.8775 |  |
| **Age (years)** | **-0.0440** | 0.0117 | ±0.0234 | **-3.762** | **1.69e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0216 | 0.0148 | ±0.0296 | +1.458 | 0.1447 | 1.0218 |  |
| Hypertension | +0.3018 | 0.2637 | ±0.5274 | +1.144 | 0.2525 | 1.3522 |  |
| High cholesterol | +0.2124 | 0.2439 | ±0.4878 | +0.871 | 0.3839 | 1.2367 |  |
| Kidney disease | +0.3352 | 0.2698 | ±0.5396 | +1.242 | 0.2141 | 1.3983 |  |
| **Circulatory disease** | **+0.7112** | 0.2583 | ±0.5167 | **+2.753** | **0.0059** | 2.0364 | ** |
| Avg. daily time in range 70-180 (%) | -0.0067 | 0.0041 | ±0.0081 | -1.657 | 0.0976 | 0.9933 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0918**, LLR χ² = **52.52** (p = **2.20e-07**), AUC = **0.7041**, AIC = **543.4**, BIC = **595.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0944 | 0.9520 | ±1.9040 | +0.099 | 0.9210 | 1.0990 |  |
| Education: graduate level (vs college) | -0.4734 | 0.2798 | ±0.5596 | -1.692 | 0.0906 | 0.6229 | . |
| Education: high school or below (vs college) | +0.1687 | 0.2832 | ±0.5663 | +0.596 | 0.5513 | 1.1838 |  |
| Site: UCSD (vs UAB) | -0.0765 | 0.2796 | ±0.5591 | -0.274 | 0.7844 | 0.9264 |  |
| Site: UW (vs UAB) | -0.1443 | 0.2696 | ±0.5391 | -0.535 | 0.5923 | 0.8656 |  |
| **Age (years)** | **-0.0437** | 0.0118 | ±0.0235 | **-3.720** | **1.99e-04** | 0.9572 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0295 | +1.632 | 0.1028 | 1.0244 |  |
| Hypertension | +0.2388 | 0.2651 | ±0.5302 | +0.901 | 0.3678 | 1.2697 |  |
| High cholesterol | +0.2482 | 0.2455 | ±0.4910 | +1.011 | 0.3120 | 1.2818 |  |
| Kidney disease | +0.3342 | 0.2709 | ±0.5418 | +1.234 | 0.2173 | 1.3969 |  |
| **Circulatory disease** | **+0.6934** | 0.2599 | ±0.5197 | **+2.668** | **0.0076** | 2.0005 | ** |
| **Any reading < 54 during wear (0/1)** | **+0.5481** | 0.2487 | ±0.4974 | **+2.204** | **0.0275** | 1.7299 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0861**, LLR χ² = **49.22** (p = **8.65e-07**), AUC = **0.6971**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2892 | 0.9436 | ±1.8873 | +0.306 | 0.7592 | 1.3354 |  |
| Education: graduate level (vs college) | -0.4472 | 0.2780 | ±0.5560 | -1.608 | 0.1077 | 0.6394 |  |
| Education: high school or below (vs college) | +0.1747 | 0.2826 | ±0.5651 | +0.618 | 0.5364 | 1.1909 |  |
| Site: UCSD (vs UAB) | -0.0893 | 0.2790 | ±0.5581 | -0.320 | 0.7490 | 0.9146 |  |
| Site: UW (vs UAB) | -0.1428 | 0.2697 | ±0.5395 | -0.529 | 0.5966 | 0.8670 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0234 | **-3.889** | **1.00e-04** | 0.9555 | *** |
| BMI (kg/m2) | +0.0238 | 0.0147 | ±0.0294 | +1.622 | 0.1049 | 1.0241 |  |
| Hypertension | +0.2616 | 0.2645 | ±0.5291 | +0.989 | 0.3226 | 1.2990 |  |
| High cholesterol | +0.2242 | 0.2443 | ±0.4886 | +0.918 | 0.3587 | 1.2514 |  |
| Kidney disease | +0.3459 | 0.2693 | ±0.5386 | +1.284 | 0.1990 | 1.4132 |  |
| **Circulatory disease** | **+0.7548** | 0.2590 | ±0.5179 | **+2.915** | **0.0036** | 2.1271 | ** |
| Time < 54 (%) | +0.4642 | 0.3895 | ±0.7789 | +1.192 | 0.2333 | 1.5908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0867**, LLR χ² = **49.56** (p = **7.52e-07**), AUC = **0.6973**, AIC = **546.4**, BIC = **598.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2988 | 0.9433 | ±1.8866 | +0.317 | 0.7515 | 1.3482 |  |
| Education: graduate level (vs college) | -0.4489 | 0.2778 | ±0.5556 | -1.616 | 0.1061 | 0.6383 |  |
| Education: high school or below (vs college) | +0.1744 | 0.2825 | ±0.5650 | +0.617 | 0.5369 | 1.1906 |  |
| Site: UCSD (vs UAB) | -0.0919 | 0.2787 | ±0.5574 | -0.330 | 0.7415 | 0.9122 |  |
| Site: UW (vs UAB) | -0.1465 | 0.2691 | ±0.5382 | -0.544 | 0.5862 | 0.8638 |  |
| **Age (years)** | **-0.0454** | 0.0117 | ±0.0234 | **-3.878** | **1.05e-04** | 0.9557 | *** |
| BMI (kg/m2) | +0.0236 | 0.0147 | ±0.0294 | +1.605 | 0.1085 | 1.0239 |  |
| Hypertension | +0.2695 | 0.2637 | ±0.5274 | +1.022 | 0.3068 | 1.3093 |  |
| High cholesterol | +0.2244 | 0.2444 | ±0.4887 | +0.918 | 0.3585 | 1.2516 |  |
| Kidney disease | +0.3396 | 0.2695 | ±0.5390 | +1.260 | 0.2077 | 1.4044 |  |
| **Circulatory disease** | **+0.7465** | 0.2583 | ±0.5165 | **+2.890** | **0.0038** | 2.1096 | ** |
| Avg. daily time < 54 (%) | +0.3815 | 0.3291 | ±0.6583 | +1.159 | 0.2464 | 1.4645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0883**, LLR χ² = **50.52** (p = **5.05e-07**), AUC = **0.7013**, AIC = **545.4**, BIC = **597.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2469 | 0.9455 | ±1.8910 | +0.261 | 0.7940 | 1.2800 |  |
| Education: graduate level (vs college) | -0.4542 | 0.2787 | ±0.5573 | -1.630 | 0.1031 | 0.6350 |  |
| Education: high school or below (vs college) | +0.1583 | 0.2829 | ±0.5658 | +0.560 | 0.5758 | 1.1715 |  |
| Site: UCSD (vs UAB) | -0.0781 | 0.2790 | ±0.5580 | -0.280 | 0.7796 | 0.9249 |  |
| Site: UW (vs UAB) | -0.1438 | 0.2697 | ±0.5394 | -0.533 | 0.5939 | 0.8661 |  |
| **Age (years)** | **-0.0459** | 0.0117 | ±0.0234 | **-3.919** | **8.88e-05** | 0.9551 | *** |
| BMI (kg/m2) | +0.0251 | 0.0147 | ±0.0294 | +1.706 | 0.0880 | 1.0254 | . |
| Hypertension | +0.2561 | 0.2640 | ±0.5280 | +0.970 | 0.3320 | 1.2919 |  |
| High cholesterol | +0.2303 | 0.2441 | ±0.4881 | +0.943 | 0.3455 | 1.2589 |  |
| Kidney disease | +0.3246 | 0.2706 | ±0.5412 | +1.200 | 0.2303 | 1.3835 |  |
| **Circulatory disease** | **+0.7582** | 0.2593 | ±0.5186 | **+2.924** | **0.0035** | 2.1343 | ** |
| Time 54-69, pooled (%) | +0.1833 | 0.1082 | ±0.2165 | +1.694 | 0.0903 | 1.2012 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0903**, LLR χ² = **51.67** (p = **3.13e-07**), AUC = **0.7010**, AIC = **544.2**, BIC = **596.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2560 | 0.9456 | ±1.8911 | +0.271 | 0.7866 | 1.2918 |  |
| Education: graduate level (vs college) | -0.4452 | 0.2786 | ±0.5572 | -1.598 | 0.1101 | 0.6407 |  |
| Education: high school or below (vs college) | +0.1648 | 0.2835 | ±0.5669 | +0.581 | 0.5610 | 1.1791 |  |
| Site: UCSD (vs UAB) | -0.0694 | 0.2794 | ±0.5588 | -0.248 | 0.8038 | 0.9329 |  |
| Site: UW (vs UAB) | -0.1274 | 0.2703 | ±0.5406 | -0.471 | 0.6375 | 0.8804 |  |
| **Age (years)** | **-0.0462** | 0.0117 | ±0.0234 | **-3.944** | **8.02e-05** | 0.9549 | *** |
| BMI (kg/m2) | +0.0247 | 0.0147 | ±0.0294 | +1.682 | 0.0926 | 1.0250 | . |
| Hypertension | +0.2474 | 0.2643 | ±0.5286 | +0.936 | 0.3493 | 1.2807 |  |
| High cholesterol | +0.2416 | 0.2448 | ±0.4897 | +0.987 | 0.3236 | 1.2733 |  |
| Kidney disease | +0.3240 | 0.2706 | ±0.5412 | +1.197 | 0.2312 | 1.3827 |  |
| **Circulatory disease** | **+0.7690** | 0.2595 | ±0.5190 | **+2.964** | **0.0030** | 2.1575 | ** |
| **Avg. daily time 54-69 (%)** | **+0.2070** | 0.1039 | ±0.2078 | **+1.992** | **0.0463** | 1.2300 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0885**, LLR χ² = **50.61** (p = **4.86e-07**), AUC = **0.7005**, AIC = **545.3**, BIC = **597.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2450 | 0.9457 | ±1.8914 | +0.259 | 0.7955 | 1.2777 |  |
| Education: graduate level (vs college) | -0.4515 | 0.2787 | ±0.5573 | -1.620 | 0.1052 | 0.6367 |  |
| Education: high school or below (vs college) | +0.1644 | 0.2829 | ±0.5658 | +0.581 | 0.5611 | 1.1787 |  |
| Site: UCSD (vs UAB) | -0.0751 | 0.2793 | ±0.5585 | -0.269 | 0.7880 | 0.9277 |  |
| Site: UW (vs UAB) | -0.1367 | 0.2700 | ±0.5400 | -0.506 | 0.6126 | 0.8722 |  |
| **Age (years)** | **-0.0459** | 0.0117 | ±0.0234 | **-3.917** | **8.97e-05** | 0.9552 | *** |
| BMI (kg/m2) | +0.0248 | 0.0147 | ±0.0294 | +1.691 | 0.0909 | 1.0252 | . |
| Hypertension | +0.2500 | 0.2644 | ±0.5288 | +0.945 | 0.3445 | 1.2840 |  |
| High cholesterol | +0.2340 | 0.2443 | ±0.4886 | +0.958 | 0.3382 | 1.2636 |  |
| Kidney disease | +0.3267 | 0.2704 | ±0.5409 | +1.208 | 0.2270 | 1.3864 |  |
| **Circulatory disease** | **+0.7629** | 0.2594 | ±0.5188 | **+2.941** | **0.0033** | 2.1444 | ** |
| Time < 70 (%) | +0.1572 | 0.0915 | ±0.1829 | +1.719 | 0.0857 | 1.1702 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0902**, LLR χ² = **51.57** (p = **3.26e-07**), AUC = **0.7007**, AIC = **544.3**, BIC = **596.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2600 | 0.9455 | ±1.8909 | +0.275 | 0.7833 | 1.2970 |  |
| Education: graduate level (vs college) | -0.4452 | 0.2785 | ±0.5569 | -1.599 | 0.1099 | 0.6407 |  |
| Education: high school or below (vs college) | +0.1696 | 0.2833 | ±0.5665 | +0.599 | 0.5495 | 1.1848 |  |
| Site: UCSD (vs UAB) | -0.0705 | 0.2794 | ±0.5588 | -0.252 | 0.8008 | 0.9319 |  |
| Site: UW (vs UAB) | -0.1252 | 0.2703 | ±0.5405 | -0.463 | 0.6433 | 0.8823 |  |
| **Age (years)** | **-0.0460** | 0.0117 | ±0.0234 | **-3.929** | **8.51e-05** | 0.9550 | *** |
| BMI (kg/m2) | +0.0244 | 0.0147 | ±0.0294 | +1.658 | 0.0973 | 1.0247 | . |
| Hypertension | +0.2466 | 0.2644 | ±0.5288 | +0.933 | 0.3509 | 1.2797 |  |
| High cholesterol | +0.2417 | 0.2449 | ±0.4897 | +0.987 | 0.3235 | 1.2735 |  |
| Kidney disease | +0.3236 | 0.2706 | ±0.5411 | +1.196 | 0.2316 | 1.3821 |  |
| **Circulatory disease** | **+0.7678** | 0.2593 | ±0.5186 | **+2.961** | **0.0031** | 2.1551 | ** |
| Avg. daily time < 70 (%) | +0.1649 | 0.0878 | ±0.1756 | +1.878 | 0.0604 | 1.1792 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0861**, LLR χ² = **49.23** (p = **8.61e-07**), AUC = **0.7000**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.8140 | 1.0241 | ±2.0482 | +0.795 | 0.4267 | 2.2570 |  |
| Education: graduate level (vs college) | -0.4281 | 0.2786 | ±0.5572 | -1.537 | 0.1244 | 0.6518 |  |
| Education: high school or below (vs college) | +0.1248 | 0.2844 | ±0.5688 | +0.439 | 0.6609 | 1.1329 |  |
| Site: UCSD (vs UAB) | -0.0835 | 0.2792 | ±0.5584 | -0.299 | 0.7648 | 0.9199 |  |
| Site: UW (vs UAB) | -0.1386 | 0.2701 | ±0.5402 | -0.513 | 0.6079 | 0.8706 |  |
| **Age (years)** | **-0.0438** | 0.0118 | ±0.0235 | **-3.729** | **1.92e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0232 | 0.0147 | ±0.0294 | +1.578 | 0.1146 | 1.0235 |  |
| Hypertension | +0.2809 | 0.2632 | ±0.5265 | +1.067 | 0.2859 | 1.3243 |  |
| High cholesterol | +0.2012 | 0.2432 | ±0.4864 | +0.827 | 0.4082 | 1.2228 |  |
| Kidney disease | +0.3421 | 0.2693 | ±0.5387 | +1.270 | 0.2041 | 1.4079 |  |
| **Circulatory disease** | **+0.7238** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0623 | ** |
| Time 54-250, pooled (%) | -0.0064 | 0.0053 | ±0.0106 | -1.210 | 0.2262 | 0.9936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0853**, LLR χ² = **48.76** (p = **1.05e-06**), AUC = **0.6985**, AIC = **547.2**, BIC = **598.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7442 | 1.0314 | ±2.0627 | +0.722 | 0.4706 | 2.1047 |  |
| Education: graduate level (vs college) | -0.4333 | 0.2785 | ±0.5570 | -1.556 | 0.1197 | 0.6483 |  |
| Education: high school or below (vs college) | +0.1303 | 0.2841 | ±0.5682 | +0.459 | 0.6466 | 1.1391 |  |
| Site: UCSD (vs UAB) | -0.0883 | 0.2791 | ±0.5582 | -0.316 | 0.7517 | 0.9155 |  |
| Site: UW (vs UAB) | -0.1465 | 0.2698 | ±0.5397 | -0.543 | 0.5872 | 0.8637 |  |
| **Age (years)** | **-0.0442** | 0.0117 | ±0.0235 | **-3.768** | **1.65e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0233 | 0.0147 | ±0.0294 | +1.586 | 0.1129 | 1.0236 |  |
| Hypertension | +0.2846 | 0.2631 | ±0.5261 | +1.082 | 0.2792 | 1.3293 |  |
| High cholesterol | +0.2011 | 0.2431 | ±0.4863 | +0.827 | 0.4083 | 1.2227 |  |
| Kidney disease | +0.3417 | 0.2693 | ±0.5386 | +1.269 | 0.2045 | 1.4073 |  |
| **Circulatory disease** | **+0.7239** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0625 | ** |
| Avg. daily time 54-250 (%) | -0.0053 | 0.0054 | ±0.0107 | -0.989 | 0.3225 | 0.9947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0872**, LLR χ² = **49.88** (p = **6.57e-07**), AUC = **0.7012**, AIC = **546.0**, BIC = **597.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1137 | 0.9533 | ±1.9065 | +0.119 | 0.9051 | 1.1204 |  |
| Education: graduate level (vs college) | -0.4567 | 0.2781 | ±0.5561 | -1.642 | 0.1005 | 0.6334 |  |
| Education: high school or below (vs college) | +0.1341 | 0.2829 | ±0.5658 | +0.474 | 0.6356 | 1.1435 |  |
| Site: UCSD (vs UAB) | -0.0839 | 0.2793 | ±0.5585 | -0.300 | 0.7638 | 0.9195 |  |
| Site: UW (vs UAB) | -0.1702 | 0.2684 | ±0.5367 | -0.634 | 0.5259 | 0.8435 |  |
| **Age (years)** | **-0.0456** | 0.0117 | ±0.0234 | **-3.903** | **9.50e-05** | 0.9554 | *** |
| BMI (kg/m2) | +0.0217 | 0.0148 | ±0.0297 | +1.458 | 0.1447 | 1.0219 |  |
| Hypertension | +0.3289 | 0.2650 | ±0.5301 | +1.241 | 0.2146 | 1.3895 |  |
| High cholesterol | +0.2173 | 0.2445 | ±0.4890 | +0.889 | 0.3741 | 1.2427 |  |
| Kidney disease | +0.3460 | 0.2696 | ±0.5392 | +1.283 | 0.1994 | 1.4134 |  |
| **Circulatory disease** | **+0.7070** | 0.2591 | ±0.5182 | **+2.728** | **0.0064** | 2.0279 | ** |
| Time 181-250, pooled (%) | +0.0108 | 0.0075 | ±0.0150 | +1.449 | 0.1473 | 1.0109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0876**, LLR χ² = **50.09** (p = **6.04e-07**), AUC = **0.7015**, AIC = **545.8**, BIC = **597.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1040 | 0.9534 | ±1.9068 | +0.109 | 0.9131 | 1.1096 |  |
| Education: graduate level (vs college) | -0.4595 | 0.2782 | ±0.5563 | -1.652 | 0.0986 | 0.6316 | . |
| Education: high school or below (vs college) | +0.1278 | 0.2832 | ±0.5664 | +0.451 | 0.6517 | 1.1364 |  |
| Site: UCSD (vs UAB) | -0.0796 | 0.2794 | ±0.5588 | -0.285 | 0.7756 | 0.9234 |  |
| Site: UW (vs UAB) | -0.1676 | 0.2685 | ±0.5370 | -0.624 | 0.5325 | 0.8457 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0234 | **-3.893** | **9.88e-05** | 0.9556 | *** |
| BMI (kg/m2) | +0.0214 | 0.0149 | ±0.0297 | +1.441 | 0.1497 | 1.0216 |  |
| Hypertension | +0.3302 | 0.2651 | ±0.5302 | +1.246 | 0.2129 | 1.3912 |  |
| High cholesterol | +0.2171 | 0.2445 | ±0.4889 | +0.888 | 0.3745 | 1.2425 |  |
| Kidney disease | +0.3449 | 0.2696 | ±0.5393 | +1.279 | 0.2008 | 1.4119 |  |
| **Circulatory disease** | **+0.7078** | 0.2591 | ±0.5181 | **+2.732** | **0.0063** | 2.0295 | ** |
| Avg. daily time 181-250 (%) | +0.0111 | 0.0073 | ±0.0147 | +1.519 | 0.1288 | 1.0112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0885**, LLR χ² = **50.61** (p = **4.86e-07**), AUC = **0.7038**, AIC = **545.3**, BIC = **597.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0272 | 0.9603 | ±1.9205 | +0.028 | 0.9774 | 1.0276 |  |
| Education: graduate level (vs college) | -0.4274 | 0.2785 | ±0.5570 | -1.535 | 0.1248 | 0.6522 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2848 | ±0.5696 | +0.384 | 0.7013 | 1.1154 |  |
| Site: UCSD (vs UAB) | -0.0642 | 0.2802 | ±0.5604 | -0.229 | 0.8187 | 0.9378 |  |
| Site: UW (vs UAB) | -0.1318 | 0.2699 | ±0.5398 | -0.489 | 0.6252 | 0.8765 |  |
| **Age (years)** | **-0.0438** | 0.0117 | ±0.0234 | **-3.749** | **1.78e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0217 | 0.0148 | ±0.0296 | +1.466 | 0.1427 | 1.0219 |  |
| Hypertension | +0.3020 | 0.2638 | ±0.5275 | +1.145 | 0.2522 | 1.3525 |  |
| High cholesterol | +0.2116 | 0.2440 | ±0.4879 | +0.867 | 0.3857 | 1.2357 |  |
| Kidney disease | +0.3388 | 0.2697 | ±0.5395 | +1.256 | 0.2092 | 1.4032 |  |
| **Circulatory disease** | **+0.7097** | 0.2584 | ±0.5168 | **+2.746** | **0.0060** | 2.0334 | ** |
| Time > 180 (%) | +0.0068 | 0.0040 | ±0.0081 | +1.688 | 0.0914 | 1.0068 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0877**, LLR χ² = **50.18** (p = **5.81e-07**), AUC = **0.7028**, AIC = **545.7**, BIC = **597.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0641 | 0.9584 | ±1.9168 | +0.067 | 0.9467 | 1.0662 |  |
| Education: graduate level (vs college) | -0.4318 | 0.2783 | ±0.5567 | -1.551 | 0.1208 | 0.6494 |  |
| Education: high school or below (vs college) | +0.1100 | 0.2848 | ±0.5697 | +0.386 | 0.6993 | 1.1163 |  |
| Site: UCSD (vs UAB) | -0.0661 | 0.2802 | ±0.5603 | -0.236 | 0.8134 | 0.9360 |  |
| Site: UW (vs UAB) | -0.1356 | 0.2698 | ±0.5395 | -0.503 | 0.6152 | 0.8732 |  |
| **Age (years)** | **-0.0441** | 0.0117 | ±0.0234 | **-3.768** | **1.65e-04** | 0.9569 | *** |
| BMI (kg/m2) | +0.0218 | 0.0148 | ±0.0296 | +1.470 | 0.1415 | 1.0220 |  |
| Hypertension | +0.3029 | 0.2636 | ±0.5272 | +1.149 | 0.2505 | 1.3538 |  |
| High cholesterol | +0.2100 | 0.2438 | ±0.4876 | +0.862 | 0.3889 | 1.2337 |  |
| Kidney disease | +0.3372 | 0.2697 | ±0.5394 | +1.250 | 0.2113 | 1.4010 |  |
| **Circulatory disease** | **+0.7110** | 0.2583 | ±0.5166 | **+2.753** | **0.0059** | 2.0361 | ** |
| Avg. daily time > 180 (%) | +0.0063 | 0.0040 | ±0.0081 | +1.553 | 0.1205 | 1.0063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0922**, LLR χ² = **52.74** (p = **2.00e-07**), AUC = **0.7084**, AIC = **543.2**, BIC = **594.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0152 | 0.9539 | ±1.9078 | +0.016 | 0.9873 | 1.0154 |  |
| Education: graduate level (vs college) | -0.4009 | 0.2796 | ±0.5592 | -1.434 | 0.1516 | 0.6697 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2849 | ±0.5699 | +0.392 | 0.6950 | 1.1182 |  |
| Site: UCSD (vs UAB) | -0.0369 | 0.2816 | ±0.5632 | -0.131 | 0.8957 | 0.9638 |  |
| Site: UW (vs UAB) | -0.1332 | 0.2699 | ±0.5399 | -0.494 | 0.6217 | 0.8753 |  |
| **Age (years)** | **-0.0430** | 0.0117 | ±0.0234 | **-3.676** | **2.37e-04** | 0.9579 | *** |
| BMI (kg/m2) | +0.0197 | 0.0149 | ±0.0298 | +1.325 | 0.1853 | 1.0199 |  |
| Hypertension | +0.3067 | 0.2646 | ±0.5293 | +1.159 | 0.2465 | 1.3590 |  |
| High cholesterol | +0.2291 | 0.2451 | ±0.4902 | +0.935 | 0.3499 | 1.2575 |  |
| Kidney disease | +0.3433 | 0.2702 | ±0.5405 | +1.270 | 0.2039 | 1.4096 |  |
| **Circulatory disease** | **+0.7034** | 0.2588 | ±0.5177 | **+2.717** | **0.0066** | 2.0206 | ** |
| **Nocturnal time > 180 (%)** | **+0.0079** | 0.0035 | ±0.0071 | **+2.242** | **0.0250** | 1.0080 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0860**, LLR χ² = **49.19** (p = **8.75e-07**), AUC = **0.6999**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1767 | 0.9523 | ±1.9047 | +0.186 | 0.8528 | 1.1933 |  |
| Education: graduate level (vs college) | -0.4286 | 0.2786 | ±0.5572 | -1.539 | 0.1239 | 0.6514 |  |
| Education: high school or below (vs college) | +0.1249 | 0.2844 | ±0.5688 | +0.439 | 0.6604 | 1.1331 |  |
| Site: UCSD (vs UAB) | -0.0842 | 0.2792 | ±0.5584 | -0.302 | 0.7628 | 0.9192 |  |
| Site: UW (vs UAB) | -0.1395 | 0.2700 | ±0.5401 | -0.517 | 0.6053 | 0.8698 |  |
| **Age (years)** | **-0.0438** | 0.0118 | ±0.0235 | **-3.731** | **1.91e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0232 | 0.0147 | ±0.0294 | +1.579 | 0.1143 | 1.0235 |  |
| Hypertension | +0.2815 | 0.2632 | ±0.5264 | +1.070 | 0.2848 | 1.3252 |  |
| High cholesterol | +0.2008 | 0.2432 | ±0.4864 | +0.826 | 0.4089 | 1.2224 |  |
| Kidney disease | +0.3422 | 0.2693 | ±0.5386 | +1.271 | 0.2038 | 1.4081 |  |
| **Circulatory disease** | **+0.7236** | 0.2576 | ±0.5153 | **+2.809** | **0.0050** | 2.0618 | ** |
| Time > 250 (%) | +0.0063 | 0.0053 | ±0.0106 | +1.193 | 0.2327 | 1.0063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0852**, LLR χ² = **48.70** (p = **1.07e-06**), AUC = **0.6984**, AIC = **547.2**, BIC = **598.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2163 | 0.9503 | ±1.9006 | +0.228 | 0.8200 | 1.2414 |  |
| Education: graduate level (vs college) | -0.4341 | 0.2785 | ±0.5569 | -1.559 | 0.1190 | 0.6479 |  |
| Education: high school or below (vs college) | +0.1307 | 0.2841 | ±0.5682 | +0.460 | 0.6455 | 1.1396 |  |
| Site: UCSD (vs UAB) | -0.0893 | 0.2791 | ±0.5581 | -0.320 | 0.7490 | 0.9146 |  |
| Site: UW (vs UAB) | -0.1477 | 0.2698 | ±0.5395 | -0.548 | 0.5840 | 0.8627 |  |
| **Age (years)** | **-0.0443** | 0.0117 | ±0.0235 | **-3.771** | **1.63e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0234 | 0.0147 | ±0.0294 | +1.587 | 0.1124 | 1.0236 |  |
| Hypertension | +0.2853 | 0.2630 | ±0.5261 | +1.085 | 0.2781 | 1.3301 |  |
| High cholesterol | +0.2007 | 0.2431 | ±0.4863 | +0.826 | 0.4091 | 1.2223 |  |
| Kidney disease | +0.3420 | 0.2693 | ±0.5386 | +1.270 | 0.2041 | 1.4078 |  |
| **Circulatory disease** | **+0.7239** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0624 | ** |
| Avg. daily time > 250 (%) | +0.0052 | 0.0054 | ±0.0108 | +0.962 | 0.3359 | 1.0052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 60 single-predictor tests; 15 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 60 tests (samples with n >= 500), of which **2** are significant at BH q < 0.05 in the all-tests family and 3 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 550): best single predictor out of sample is **SD of daily means** (CV R² 0.098 vs 0.080 for covariates alone, gain +0.017; +0.793 per SD, p = 3.3e-04, q = 0.044). FDR-robust associations (1): SD of daily means (higher outcome, +0.793 per SD, q = 0.044).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 550): best single predictor out of sample is **SD of daily means** (CV AUC 0.688 vs 0.650 for covariates alone, gain +0.038; OR 1.55 per SD, p = 4.4e-05, q = 0.012). FDR-robust associations (1): SD of daily means (higher outcome, OR 1.55 per SD, q = 0.012).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.038, via SD of daily means); CES-D-10 depressive symptoms (0-30) (+0.017, via SD of daily means). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (2 FDR-significant / 9 raw-significant of 16); Band 54-69 (0 FDR-significant / 2 raw-significant of 4); HbA1c (0 FDR-significant / 1 raw-significant of 2).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 2 FDR-significant (9 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (SD of daily means, ΔAIC -8.5); Clinically relevant depressive symptoms (SD of daily means, ΔAIC -11.6).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
