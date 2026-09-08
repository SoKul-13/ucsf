# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 204; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0889**, F-statistic = **2.98** (p = **0.0016**), Residual SE = **5.232** on **193** df, AIC = **1264.8**, BIC = **1301.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4499** | 3.3562 | ±6.7123 | **+3.412** | **6.46e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7884 | ±1.5769 | **-2.315** | **0.0206** | * |
| Education: high school or below (vs college) | +1.3506 | 1.3850 | ±2.7699 | +0.975 | 0.3295 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9806 | ±1.9611 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0358 | ±2.0715 | +1.133 | 0.2573 |  |
| **Age (years)** | **-0.1111** | 0.0396 | ±0.0791 | **-2.807** | **0.0050** | ** |
| BMI (kg/m2) | +0.0598 | 0.0565 | ±0.1130 | +1.059 | 0.2897 |  |
| Hypertension | -0.8462 | 0.9094 | ±1.8187 | -0.931 | 0.3521 |  |
| High cholesterol | +0.3900 | 0.7715 | ±1.5429 | +0.506 | 0.6132 |  |
| Kidney disease | +1.3666 | 1.2799 | ±2.5599 | +1.068 | 0.2856 |  |
| Circulatory disease | +0.6361 | 1.0940 | ±2.1880 | +0.581 | 0.5609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **204**, R² = **0.1456**, Adj R² = **0.0966**, F-statistic = **2.97** (p = **0.0011**), Residual SE = **5.210** on **192** df, AIC = **1264.0**, BIC = **1303.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.7504** | 5.0864 | ±10.1729 | **+3.490** | **4.83e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8840** | 0.7836 | ±1.5671 | **-2.404** | **0.0162** | * |
| Education: high school or below (vs college) | +1.4072 | 1.3883 | ±2.7767 | +1.014 | 0.3108 |  |
| Site: UCSD (vs UAB) | -0.0300 | 0.9806 | ±1.9612 | -0.031 | 0.9756 |  |
| Site: UW (vs UAB) | +1.1514 | 1.0412 | ±2.0824 | +1.106 | 0.2688 |  |
| **Age (years)** | **-0.1088** | 0.0396 | ±0.0792 | **-2.749** | **0.0060** | ** |
| BMI (kg/m2) | +0.0786 | 0.0566 | ±0.1132 | +1.388 | 0.1650 |  |
| Hypertension | -0.7592 | 0.9119 | ±1.8238 | -0.833 | 0.4051 |  |
| High cholesterol | +0.5196 | 0.7618 | ±1.5236 | +0.682 | 0.4952 |  |
| Kidney disease | +1.1943 | 1.2402 | ±2.4805 | +0.963 | 0.3355 |  |
| Circulatory disease | +0.8402 | 1.0908 | ±2.1815 | +0.770 | 0.4411 |  |
| HbA1c (%) | -1.1925 | 0.7234 | ±1.4467 | -1.648 | 0.0993 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **204**, R² = **0.1430**, Adj R² = **0.0939**, F-statistic = **2.91** (p = **0.0014**), Residual SE = **5.217** on **192** df, AIC = **1264.6**, BIC = **1304.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5058** | 4.3995 | ±8.7990 | **+3.752** | **1.76e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8500** | 0.7912 | ±1.5823 | **-2.338** | **0.0194** | * |
| Education: high school or below (vs college) | +1.2525 | 1.3661 | ±2.7321 | +0.917 | 0.3592 |  |
| Site: UCSD (vs UAB) | -0.0143 | 0.9797 | ±1.9593 | -0.015 | 0.9884 |  |
| Site: UW (vs UAB) | +1.1224 | 1.0275 | ±2.0551 | +1.092 | 0.2747 |  |
| **Age (years)** | **-0.1113** | 0.0394 | ±0.0788 | **-2.824** | **0.0047** | ** |
| BMI (kg/m2) | +0.0672 | 0.0564 | ±0.1129 | +1.190 | 0.2340 |  |
| Hypertension | -0.7903 | 0.9153 | ±1.8305 | -0.864 | 0.3878 |  |
| High cholesterol | +0.3544 | 0.7694 | ±1.5387 | +0.461 | 0.6450 |  |
| Kidney disease | +1.5169 | 1.2619 | ±2.5238 | +1.202 | 0.2293 |  |
| Circulatory disease | +0.6846 | 1.0928 | ±2.1856 | +0.626 | 0.5310 |  |
| Mean glucose (mg/dL) | -0.0415 | 0.0263 | ±0.0526 | -1.575 | 0.1152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **204**, R² = **0.1430**, Adj R² = **0.0939**, F-statistic = **2.91** (p = **0.0014**), Residual SE = **5.217** on **192** df, AIC = **1264.6**, BIC = **1304.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.2426** | 7.3136 | ±14.6272 | **+3.041** | **0.0024** | ** |
| **Education: graduate level (vs college)** | **-1.8500** | 0.7912 | ±1.5823 | **-2.338** | **0.0194** | * |
| Education: high school or below (vs college) | +1.2525 | 1.3661 | ±2.7321 | +0.917 | 0.3592 |  |
| Site: UCSD (vs UAB) | -0.0143 | 0.9797 | ±1.9593 | -0.015 | 0.9884 |  |
| Site: UW (vs UAB) | +1.1224 | 1.0275 | ±2.0551 | +1.092 | 0.2747 |  |
| **Age (years)** | **-0.1113** | 0.0394 | ±0.0788 | **-2.824** | **0.0047** | ** |
| BMI (kg/m2) | +0.0672 | 0.0564 | ±0.1129 | +1.190 | 0.2340 |  |
| Hypertension | -0.7903 | 0.9153 | ±1.8305 | -0.864 | 0.3878 |  |
| High cholesterol | +0.3544 | 0.7694 | ±1.5387 | +0.461 | 0.6450 |  |
| Kidney disease | +1.5169 | 1.2619 | ±2.5238 | +1.202 | 0.2293 |  |
| Circulatory disease | +0.6846 | 1.0928 | ±2.1856 | +0.626 | 0.5310 |  |
| GMI (%) | -1.7332 | 1.1003 | ±2.2007 | -1.575 | 0.1152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **204**, R² = **0.1344**, Adj R² = **0.0848**, F-statistic = **2.71** (p = **0.0029**), Residual SE = **5.244** on **192** df, AIC = **1266.6**, BIC = **1306.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.6297** | 4.4411 | ±8.8822 | **+2.844** | **0.0045** | ** |
| **Education: graduate level (vs college)** | **-1.8203** | 0.7935 | ±1.5871 | **-2.294** | **0.0218** | * |
| Education: high school or below (vs college) | +1.3329 | 1.3864 | ±2.7727 | +0.961 | 0.3363 |  |
| Site: UCSD (vs UAB) | +0.0089 | 0.9869 | ±1.9738 | +0.009 | 0.9928 |  |
| Site: UW (vs UAB) | +1.1698 | 1.0381 | ±2.0761 | +1.127 | 0.2598 |  |
| **Age (years)** | **-0.1122** | 0.0398 | ±0.0796 | **-2.821** | **0.0048** | ** |
| BMI (kg/m2) | +0.0622 | 0.0573 | ±0.1145 | +1.087 | 0.2772 |  |
| Hypertension | -0.8437 | 0.9150 | ±1.8299 | -0.922 | 0.3565 |  |
| High cholesterol | +0.3939 | 0.7730 | ±1.5460 | +0.510 | 0.6103 |  |
| Kidney disease | +1.3759 | 1.2835 | ±2.5669 | +1.072 | 0.2837 |  |
| Circulatory disease | +0.6620 | 1.1060 | ±2.2119 | +0.599 | 0.5494 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0094 | 0.0243 | ±0.0487 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1365**, Adj R² = **0.0870**, F-statistic = **2.76** (p = **0.0024**), Residual SE = **5.237** on **192** df, AIC = **1266.1**, BIC = **1305.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.7466** | 3.6623 | ±7.3245 | **+3.481** | **5.00e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7843** | 0.8000 | ±1.6000 | **-2.230** | **0.0257** | * |
| Education: high school or below (vs college) | +1.5029 | 1.4329 | ±2.8658 | +1.049 | 0.2942 |  |
| Site: UCSD (vs UAB) | -0.0475 | 0.9831 | ±1.9663 | -0.048 | 0.9615 |  |
| Site: UW (vs UAB) | +1.0606 | 1.0613 | ±2.1227 | +0.999 | 0.3176 |  |
| **Age (years)** | **-0.1089** | 0.0397 | ±0.0793 | **-2.745** | **0.0060** | ** |
| BMI (kg/m2) | +0.0591 | 0.0563 | ±0.1125 | +1.050 | 0.2938 |  |
| Hypertension | -0.7487 | 0.9343 | ±1.8687 | -0.801 | 0.4229 |  |
| High cholesterol | +0.3444 | 0.7832 | ±1.5664 | +0.440 | 0.6601 |  |
| Kidney disease | +1.5064 | 1.2869 | ±2.5738 | +1.171 | 0.2418 |  |
| Circulatory disease | +0.6994 | 1.1120 | ±2.2239 | +0.629 | 0.5294 |  |
| Glucose SD, pooled (mg/dL) | -0.0665 | 0.0809 | ±0.1617 | -0.823 | 0.4108 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1353**, Adj R² = **0.0858**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **5.241** on **192** df, AIC = **1266.4**, BIC = **1306.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.3322** | 3.6166 | ±7.2331 | **+3.410** | **6.50e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7987** | 0.7983 | ±1.5966 | **-2.253** | **0.0243** | * |
| Education: high school or below (vs college) | +1.4409 | 1.4228 | ±2.8456 | +1.013 | 0.3112 |  |
| Site: UCSD (vs UAB) | -0.0057 | 0.9850 | ±1.9700 | -0.006 | 0.9954 |  |
| Site: UW (vs UAB) | +1.1135 | 1.0537 | ±2.1074 | +1.057 | 0.2906 |  |
| **Age (years)** | **-0.1093** | 0.0396 | ±0.0793 | **-2.756** | **0.0058** | ** |
| BMI (kg/m2) | +0.0593 | 0.0564 | ±0.1127 | +1.052 | 0.2929 |  |
| Hypertension | -0.7540 | 0.9423 | ±1.8847 | -0.800 | 0.4236 |  |
| High cholesterol | +0.3530 | 0.7847 | ±1.5694 | +0.450 | 0.6529 |  |
| Kidney disease | +1.4388 | 1.2800 | ±2.5600 | +1.124 | 0.2610 |  |
| Circulatory disease | +0.6610 | 1.1075 | ±2.2150 | +0.597 | 0.5506 |  |
| Avg. daily SD (mg/dL) | -0.0507 | 0.0816 | ±0.1633 | -0.621 | 0.5343 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6899** | 3.8420 | ±7.6840 | **+3.043** | **0.0023** | ** |
| **Education: graduate level (vs college)** | **-1.8168** | 0.8008 | ±1.6016 | **-2.269** | **0.0233** | * |
| Education: high school or below (vs college) | +1.3836 | 1.4618 | ±2.9236 | +0.947 | 0.3439 |  |
| Site: UCSD (vs UAB) | -0.0030 | 0.9842 | ±1.9684 | -0.003 | 0.9975 |  |
| Site: UW (vs UAB) | +1.1553 | 1.0727 | ±2.1453 | +1.077 | 0.2814 |  |
| **Age (years)** | **-0.1107** | 0.0395 | ±0.0791 | **-2.799** | **0.0051** | ** |
| BMI (kg/m2) | +0.0593 | 0.0565 | ±0.1130 | +1.051 | 0.2935 |  |
| Hypertension | -0.8313 | 0.9252 | ±1.8504 | -0.899 | 0.3689 |  |
| High cholesterol | +0.3838 | 0.7793 | ±1.5586 | +0.492 | 0.6224 |  |
| Kidney disease | +1.3847 | 1.3000 | ±2.6000 | +1.065 | 0.2868 |  |
| Circulatory disease | +0.6441 | 1.1051 | ±2.2101 | +0.583 | 0.5600 |  |
| CV (%) | -0.0151 | 0.1144 | ±0.2289 | -0.132 | 0.8954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **204**, R² = **0.1339**, Adj R² = **0.0843**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8610** | 4.0417 | ±8.0833 | **+2.935** | **0.0033** | ** |
| **Education: graduate level (vs college)** | **-1.8355** | 0.7990 | ±1.5980 | **-2.297** | **0.0216** | * |
| Education: high school or below (vs college) | +1.3061 | 1.4459 | ±2.8918 | +0.903 | 0.3664 |  |
| Site: UCSD (vs UAB) | +0.0154 | 0.9831 | ±1.9662 | +0.016 | 0.9875 |  |
| Site: UW (vs UAB) | +1.1976 | 1.0694 | ±2.1387 | +1.120 | 0.2627 |  |
| **Age (years)** | **-0.1117** | 0.0397 | ±0.0794 | **-2.815** | **0.0049** | ** |
| BMI (kg/m2) | +0.0601 | 0.0568 | ±0.1135 | +1.059 | 0.2894 |  |
| Hypertension | -0.8702 | 0.9235 | ±1.8470 | -0.942 | 0.3461 |  |
| High cholesterol | +0.3964 | 0.7778 | ±1.5556 | +0.510 | 0.6103 |  |
| Kidney disease | +1.3399 | 1.3008 | ±2.6015 | +1.030 | 0.3029 |  |
| Circulatory disease | +0.6277 | 1.1010 | ±2.2019 | +0.570 | 0.5686 |  |
| Mean / SD ratio | -0.0604 | 0.3109 | ±0.6219 | -0.194 | 0.8459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1350**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **5.242** on **192** df, AIC = **1266.5**, BIC = **1306.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.5349** | 4.0024 | ±8.0049 | **+3.132** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.8434** | 0.7956 | ±1.5911 | **-2.317** | **0.0205** | * |
| Education: high school or below (vs college) | +1.2563 | 1.4186 | ±2.8373 | +0.886 | 0.3759 |  |
| Site: UCSD (vs UAB) | -0.0022 | 0.9789 | ±1.9578 | -0.002 | 0.9982 |  |
| Site: UW (vs UAB) | +1.2245 | 1.0601 | ±2.1202 | +1.155 | 0.2481 |  |
| **Age (years)** | **-0.1132** | 0.0398 | ±0.0795 | **-2.847** | **0.0044** | ** |
| BMI (kg/m2) | +0.0602 | 0.0571 | ±0.1142 | +1.055 | 0.2913 |  |
| Hypertension | -0.9357 | 0.9333 | ±1.8666 | -1.003 | 0.3160 |  |
| High cholesterol | +0.3998 | 0.7756 | ±1.5511 | +0.516 | 0.6062 |  |
| Kidney disease | +1.3161 | 1.2931 | ±2.5861 | +1.018 | 0.3088 |  |
| Circulatory disease | +0.6458 | 1.0961 | ±2.1923 | +0.589 | 0.5557 |  |
| Avg. daily mean/SD | -0.1327 | 0.2497 | ±0.4994 | -0.531 | 0.5952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **204**, R² = **0.1556**, Adj R² = **0.1072**, F-statistic = **3.22** (p = **4.84e-04**), Residual SE = **5.179** on **192** df, AIC = **1261.5**, BIC = **1301.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +6.9734 | 3.8959 | ±7.7918 | +1.790 | 0.0735 | . |
| **Education: graduate level (vs college)** | **-1.8693** | 0.7891 | ±1.5781 | **-2.369** | **0.0178** | * |
| Education: high school or below (vs college) | +1.1795 | 1.3409 | ±2.6818 | +0.880 | 0.3791 |  |
| Site: UCSD (vs UAB) | -0.0025 | 0.9548 | ±1.9097 | -0.003 | 0.9979 |  |
| Site: UW (vs UAB) | +1.2962 | 1.0140 | ±2.0280 | +1.278 | 0.2011 |  |
| **Age (years)** | **-0.1085** | 0.0392 | ±0.0785 | **-2.765** | **0.0057** | ** |
| BMI (kg/m2) | +0.0541 | 0.0573 | ±0.1146 | +0.944 | 0.3452 |  |
| Hypertension | -0.9214 | 0.9030 | ±1.8060 | -1.020 | 0.3076 |  |
| High cholesterol | +0.2862 | 0.7754 | ±1.5508 | +0.369 | 0.7121 |  |
| Kidney disease | +1.3889 | 1.2860 | ±2.5720 | +1.080 | 0.2801 |  |
| Circulatory disease | +0.7160 | 1.0894 | ±2.1787 | +0.657 | 0.5110 |  |
| **MAG (mg/dL/h)** | **+0.1266** | 0.0547 | ±0.1093 | **+2.315** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.3997** | 3.7671 | ±7.5341 | **+3.026** | **0.0025** | ** |
| **Education: graduate level (vs college)** | **-1.8256** | 0.7942 | ±1.5884 | **-2.299** | **0.0215** | * |
| Education: high school or below (vs college) | +1.3475 | 1.4150 | ±2.8300 | +0.952 | 0.3409 |  |
| Site: UCSD (vs UAB) | +0.0068 | 0.9809 | ±1.9618 | +0.007 | 0.9945 |  |
| Site: UW (vs UAB) | +1.1757 | 1.0506 | ±2.1012 | +1.119 | 0.2631 |  |
| **Age (years)** | **-0.1112** | 0.0398 | ±0.0795 | **-2.795** | **0.0052** | ** |
| BMI (kg/m2) | +0.0599 | 0.0568 | ±0.1135 | +1.056 | 0.2910 |  |
| Hypertension | -0.8491 | 0.9253 | ±1.8507 | -0.918 | 0.3588 |  |
| High cholesterol | +0.3908 | 0.7764 | ±1.5528 | +0.503 | 0.6147 |  |
| Kidney disease | +1.3647 | 1.2853 | ±2.5706 | +1.062 | 0.2883 |  |
| Circulatory disease | +0.6358 | 1.1019 | ±2.2037 | +0.577 | 0.5639 |  |
| Avg. daily range (mg/dL) | +0.0006 | 0.0201 | ±0.0402 | +0.027 | 0.9781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5562** | 3.4988 | ±6.9976 | **+3.303** | **9.57e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8219** | 0.7955 | ±1.5909 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3756 | 1.4511 | ±2.9021 | +0.948 | 0.3431 |  |
| Site: UCSD (vs UAB) | -0.0113 | 0.9856 | ±1.9713 | -0.011 | 0.9909 |  |
| Site: UW (vs UAB) | +1.1549 | 1.0647 | ±2.1294 | +1.085 | 0.2780 |  |
| **Age (years)** | **-0.1109** | 0.0398 | ±0.0796 | **-2.788** | **0.0053** | ** |
| BMI (kg/m2) | +0.0599 | 0.0568 | ±0.1136 | +1.053 | 0.2921 |  |
| Hypertension | -0.8541 | 0.9196 | ±1.8392 | -0.929 | 0.3530 |  |
| High cholesterol | +0.3935 | 0.7762 | ±1.5524 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3920 | 1.3289 | ±2.6577 | +1.048 | 0.2949 |  |
| Circulatory disease | +0.6587 | 1.0899 | ±2.1798 | +0.604 | 0.5456 |  |
| SD of daily means (mg/dL) | -0.0170 | 0.1613 | ±0.3225 | -0.105 | 0.9163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **204**, R² = **0.1503**, Adj R² = **0.1016**, F-statistic = **3.09** (p = **7.68e-04**), Residual SE = **5.195** on **192** df, AIC = **1262.8**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.9228 | 8.7946 | ±17.5891 | -0.446 | 0.6556 |  |
| **Education: graduate level (vs college)** | **-1.7540** | 0.7885 | ±1.5769 | **-2.225** | **0.0261** | * |
| Education: high school or below (vs college) | +1.5205 | 1.3862 | ±2.7723 | +1.097 | 0.2727 |  |
| Site: UCSD (vs UAB) | -0.1389 | 0.9724 | ±1.9448 | -0.143 | 0.8864 |  |
| Site: UW (vs UAB) | +1.0151 | 1.0229 | ±2.0458 | +0.992 | 0.3210 |  |
| **Age (years)** | **-0.1029** | 0.0402 | ±0.0805 | **-2.557** | **0.0105** | * |
| BMI (kg/m2) | +0.0640 | 0.0555 | ±0.1111 | +1.153 | 0.2489 |  |
| Hypertension | -0.7993 | 0.9164 | ±1.8329 | -0.872 | 0.3831 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5403 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6896 | 1.2364 | ±2.4727 | +1.367 | 0.1717 |  |
| Circulatory disease | +0.7515 | 1.0930 | ±2.1860 | +0.688 | 0.4917 |  |
| **Time in range 70-180, pooled (%)** | **+0.1538** | 0.0760 | ±0.1519 | **+2.024** | **0.0429** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **204**, R² = **0.1500**, Adj R² = **0.1014**, F-statistic = **3.08** (p = **7.82e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -4.1524 | 8.8587 | ±17.7175 | -0.469 | 0.6393 |  |
| **Education: graduate level (vs college)** | **-1.7656** | 0.7874 | ±1.5748 | **-2.242** | **0.0249** | * |
| Education: high school or below (vs college) | +1.4913 | 1.3836 | ±2.7671 | +1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -0.1338 | 0.9737 | ±1.9475 | -0.137 | 0.8907 |  |
| Site: UW (vs UAB) | +1.0431 | 1.0230 | ±2.0459 | +1.020 | 0.3079 |  |
| **Age (years)** | **-0.1027** | 0.0403 | ±0.0805 | **-2.549** | **0.0108** | * |
| BMI (kg/m2) | +0.0632 | 0.0554 | ±0.1108 | +1.140 | 0.2543 |  |
| Hypertension | -0.7836 | 0.9183 | ±1.8365 | -0.853 | 0.3935 |  |
| High cholesterol | +0.3194 | 0.7696 | ±1.5392 | +0.415 | 0.6781 |  |
| Kidney disease | +1.6942 | 1.2365 | ±2.4730 | +1.370 | 0.1707 |  |
| Circulatory disease | +0.7515 | 1.0929 | ±2.1858 | +0.688 | 0.4917 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.1559** | 0.0770 | ±0.1540 | **+2.024** | **0.0429** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4321** | 3.3765 | ±6.7531 | **+3.386** | **7.10e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8179** | 0.7962 | ±1.5925 | **-2.283** | **0.0224** | * |
| Education: high school or below (vs college) | +1.3646 | 1.3898 | ±2.7797 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | +0.0021 | 0.9817 | ±1.9634 | +0.002 | 0.9983 |  |
| Site: UW (vs UAB) | +1.1715 | 1.0400 | ±2.0800 | +1.126 | 0.2600 |  |
| **Age (years)** | **-0.1105** | 0.0401 | ±0.0803 | **-2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0596 | 0.0569 | ±0.1137 | +1.049 | 0.2942 |  |
| Hypertension | -0.8462 | 0.9113 | ±1.8226 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3965 | 0.7820 | ±1.5640 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3598 | 1.2822 | ±2.5645 | +1.060 | 0.2889 |  |
| Circulatory disease | +0.6427 | 1.1001 | ±2.2003 | +0.584 | 0.5591 |  |
| Time 54-69, pooled (%) | -0.1211 | 1.0901 | ±2.1801 | -0.111 | 0.9115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4501** | 3.3683 | ±6.7365 | **+3.399** | **6.75e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7970 | ±1.5941 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3505 | 1.3876 | ±2.7752 | +0.973 | 0.3304 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9825 | ±1.9650 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0385 | ±2.0771 | +1.130 | 0.2586 |  |
| **Age (years)** | **-0.1111** | 0.0401 | ±0.0801 | **-2.772** | **0.0056** | ** |
| BMI (kg/m2) | +0.0598 | 0.0569 | ±0.1137 | +1.052 | 0.2926 |  |
| Hypertension | -0.8462 | 0.9114 | ±1.8227 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3900 | 0.7808 | ±1.5616 | +0.499 | 0.6175 |  |
| Kidney disease | +1.3667 | 1.2833 | ±2.5666 | +1.065 | 0.2869 |  |
| Circulatory disease | +0.6361 | 1.0974 | ±2.1949 | +0.580 | 0.5622 |  |
| Avg. daily time 54-69 (%) | +0.0007 | 0.9072 | ±1.8144 | +0.001 | 0.9994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4321** | 3.3765 | ±6.7531 | **+3.386** | **7.10e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8179** | 0.7962 | ±1.5925 | **-2.283** | **0.0224** | * |
| Education: high school or below (vs college) | +1.3646 | 1.3898 | ±2.7797 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | +0.0021 | 0.9817 | ±1.9634 | +0.002 | 0.9983 |  |
| Site: UW (vs UAB) | +1.1715 | 1.0400 | ±2.0800 | +1.126 | 0.2600 |  |
| **Age (years)** | **-0.1105** | 0.0401 | ±0.0803 | **-2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0596 | 0.0569 | ±0.1137 | +1.049 | 0.2942 |  |
| Hypertension | -0.8462 | 0.9113 | ±1.8226 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3965 | 0.7820 | ±1.5640 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3598 | 1.2822 | ±2.5645 | +1.060 | 0.2889 |  |
| Circulatory disease | +0.6427 | 1.1001 | ±2.2003 | +0.584 | 0.5591 |  |
| Time < 70 (%) | -0.1211 | 1.0901 | ±2.1801 | -0.111 | 0.9115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4501** | 3.3683 | ±6.7365 | **+3.399** | **6.75e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7970 | ±1.5941 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3505 | 1.3876 | ±2.7752 | +0.973 | 0.3304 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9825 | ±1.9650 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0385 | ±2.0771 | +1.130 | 0.2586 |  |
| **Age (years)** | **-0.1111** | 0.0401 | ±0.0801 | **-2.772** | **0.0056** | ** |
| BMI (kg/m2) | +0.0598 | 0.0569 | ±0.1137 | +1.052 | 0.2926 |  |
| Hypertension | -0.8462 | 0.9114 | ±1.8227 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3900 | 0.7808 | ±1.5616 | +0.499 | 0.6175 |  |
| Kidney disease | +1.3667 | 1.2833 | ±2.5666 | +1.065 | 0.2869 |  |
| Circulatory disease | +0.6361 | 1.0974 | ±2.1949 | +0.580 | 0.5622 |  |
| Avg. daily time < 70 (%) | +0.0007 | 0.9072 | ±1.8144 | +0.001 | 0.9994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **204**, R² = **0.1499**, Adj R² = **0.1012**, F-statistic = **3.08** (p = **7.92e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4760** | 3.3610 | ±6.7220 | **+3.414** | **6.39e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7641** | 0.7881 | ±1.5762 | **-2.239** | **0.0252** | * |
| Education: high school or below (vs college) | +1.4998 | 1.3851 | ±2.7701 | +1.083 | 0.2789 |  |
| Site: UCSD (vs UAB) | -0.1317 | 0.9730 | ±1.9460 | -0.135 | 0.8923 |  |
| Site: UW (vs UAB) | +1.0202 | 1.0227 | ±2.0454 | +0.998 | 0.3185 |  |
| **Age (years)** | **-0.1037** | 0.0402 | ±0.0803 | **-2.583** | **0.0098** | ** |
| BMI (kg/m2) | +0.0642 | 0.0556 | ±0.1112 | +1.155 | 0.2480 |  |
| Hypertension | -0.8002 | 0.9165 | ±1.8330 | -0.873 | 0.3826 |  |
| High cholesterol | +0.3062 | 0.7708 | ±1.5416 | +0.397 | 0.6911 |  |
| Kidney disease | +1.6920 | 1.2389 | ±2.4778 | +1.366 | 0.1720 |  |
| Circulatory disease | +0.7412 | 1.0928 | ±2.1855 | +0.678 | 0.4976 |  |
| **Time 181-250, pooled (%)** | **-0.1508** | 0.0753 | ±0.1505 | **-2.004** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **204**, R² = **0.1497**, Adj R² = **0.1010**, F-statistic = **3.07** (p = **8.04e-04**), Residual SE = **5.197** on **192** df, AIC = **1263.0**, BIC = **1302.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4669** | 3.3619 | ±6.7239 | **+3.411** | **6.48e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7756** | 0.7870 | ±1.5741 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | +1.4722 | 1.3825 | ±2.7649 | +1.065 | 0.2869 |  |
| Site: UCSD (vs UAB) | -0.1305 | 0.9742 | ±1.9484 | -0.134 | 0.8934 |  |
| Site: UW (vs UAB) | +1.0451 | 1.0226 | ±2.0452 | +1.022 | 0.3068 |  |
| **Age (years)** | **-0.1036** | 0.0402 | ±0.0803 | **-2.578** | **0.0099** | ** |
| BMI (kg/m2) | +0.0634 | 0.0555 | ±0.1109 | +1.143 | 0.2532 |  |
| Hypertension | -0.7864 | 0.9180 | ±1.8360 | -0.857 | 0.3916 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5402 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6996 | 1.2394 | ±2.4789 | +1.371 | 0.1703 |  |
| Circulatory disease | +0.7432 | 1.0926 | ±2.1852 | +0.680 | 0.4964 |  |
| **Avg. daily time 181-250 (%)** | **-0.1528** | 0.0760 | ±0.1521 | **-2.010** | **0.0444** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **204**, R² = **0.1499**, Adj R² = **0.1012**, F-statistic = **3.08** (p = **7.92e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4760** | 3.3610 | ±6.7220 | **+3.414** | **6.39e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7641** | 0.7881 | ±1.5762 | **-2.239** | **0.0252** | * |
| Education: high school or below (vs college) | +1.4998 | 1.3851 | ±2.7701 | +1.083 | 0.2789 |  |
| Site: UCSD (vs UAB) | -0.1317 | 0.9730 | ±1.9460 | -0.135 | 0.8923 |  |
| Site: UW (vs UAB) | +1.0202 | 1.0227 | ±2.0454 | +0.998 | 0.3185 |  |
| **Age (years)** | **-0.1037** | 0.0402 | ±0.0803 | **-2.583** | **0.0098** | ** |
| BMI (kg/m2) | +0.0642 | 0.0556 | ±0.1112 | +1.155 | 0.2480 |  |
| Hypertension | -0.8002 | 0.9165 | ±1.8330 | -0.873 | 0.3826 |  |
| High cholesterol | +0.3062 | 0.7708 | ±1.5416 | +0.397 | 0.6911 |  |
| Kidney disease | +1.6920 | 1.2389 | ±2.4778 | +1.366 | 0.1720 |  |
| Circulatory disease | +0.7412 | 1.0928 | ±2.1855 | +0.678 | 0.4976 |  |
| **Time > 180 (%)** | **-0.1508** | 0.0753 | ±0.1505 | **-2.004** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **204**, R² = **0.1497**, Adj R² = **0.1010**, F-statistic = **3.07** (p = **8.04e-04**), Residual SE = **5.197** on **192** df, AIC = **1263.0**, BIC = **1302.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4669** | 3.3619 | ±6.7239 | **+3.411** | **6.48e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7756** | 0.7870 | ±1.5741 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | +1.4722 | 1.3825 | ±2.7649 | +1.065 | 0.2869 |  |
| Site: UCSD (vs UAB) | -0.1305 | 0.9742 | ±1.9484 | -0.134 | 0.8934 |  |
| Site: UW (vs UAB) | +1.0451 | 1.0226 | ±2.0452 | +1.022 | 0.3068 |  |
| **Age (years)** | **-0.1036** | 0.0402 | ±0.0803 | **-2.578** | **0.0099** | ** |
| BMI (kg/m2) | +0.0634 | 0.0555 | ±0.1109 | +1.143 | 0.2532 |  |
| Hypertension | -0.7864 | 0.9180 | ±1.8360 | -0.857 | 0.3916 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5402 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6996 | 1.2394 | ±2.4789 | +1.371 | 0.1703 |  |
| Circulatory disease | +0.7432 | 1.0926 | ±2.1852 | +0.680 | 0.4964 |  |
| **Avg. daily time > 180 (%)** | **-0.1528** | 0.0760 | ±0.1521 | **-2.010** | **0.0444** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **204**, R² = **0.1346**, Adj R² = **0.0850**, F-statistic = **2.71** (p = **0.0028**), Residual SE = **5.243** on **192** df, AIC = **1266.6**, BIC = **1306.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4475** | 3.3749 | ±6.7499 | **+3.392** | **6.94e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8224** | 0.7916 | ±1.5832 | **-2.302** | **0.0213** | * |
| Education: high school or below (vs college) | +1.4136 | 1.4136 | ±2.8271 | +1.000 | 0.3173 |  |
| Site: UCSD (vs UAB) | -0.0549 | 0.9795 | ±1.9590 | -0.056 | 0.9553 |  |
| Site: UW (vs UAB) | +1.1161 | 1.0250 | ±2.0501 | +1.089 | 0.2762 |  |
| **Age (years)** | **-0.1104** | 0.0397 | ±0.0793 | **-2.784** | **0.0054** | ** |
| BMI (kg/m2) | +0.0624 | 0.0576 | ±0.1152 | +1.084 | 0.2785 |  |
| Hypertension | -0.8869 | 0.9166 | ±1.8331 | -0.968 | 0.3332 |  |
| High cholesterol | +0.3971 | 0.7731 | ±1.5463 | +0.514 | 0.6076 |  |
| Kidney disease | +1.4450 | 1.3125 | ±2.6251 | +1.101 | 0.2709 |  |
| Circulatory disease | +0.6741 | 1.1205 | ±2.2411 | +0.602 | 0.5474 |  |
| Nocturnal time > 180 (%) | -0.0316 | 0.0892 | ±0.1785 | -0.354 | 0.7233 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 204; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3023**), AUC = **0.6397**, AIC = **237.5**, BIC = **274.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3393 | 1.5605 | ±3.1210 | +0.217 | 0.8279 | 1.4039 |  |
| Education: graduate level (vs college) | -0.2927 | 0.3823 | ±0.7646 | -0.766 | 0.4439 | 0.7463 |  |
| Education: high school or below (vs college) | +0.4893 | 0.4778 | ±0.9556 | +1.024 | 0.3059 | 1.6311 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6225 | 0.8032 |  |
| Site: UW (vs UAB) | +0.4211 | 0.4214 | ±0.8429 | +0.999 | 0.3177 | 1.5236 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0100 | 0.0247 | ±0.0495 | +0.406 | 0.6850 | 1.0101 |  |
| Hypertension | -0.4013 | 0.3896 | ±0.7793 | -1.030 | 0.3030 | 0.6694 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6027 | 0.5045 | ±1.0090 | +1.195 | 0.2322 | 1.8270 |  |
| Circulatory disease | +0.0583 | 0.4345 | ±0.8690 | +0.134 | 0.8932 | 1.0601 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0610**, LLR χ² = **13.86** (p = **0.2408**), AUC = **0.6649**, AIC = **237.3**, BIC = **277.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.0374 | 2.4750 | ±4.9500 | +1.227 | 0.2197 | 20.8516 |  |
| Education: graduate level (vs college) | -0.3050 | 0.3852 | ±0.7704 | -0.792 | 0.4285 | 0.7371 |  |
| Education: high school or below (vs college) | +0.5300 | 0.4808 | ±0.9615 | +1.102 | 0.2703 | 1.6989 |  |
| Site: UCSD (vs UAB) | -0.2176 | 0.4463 | ±0.8926 | -0.488 | 0.6259 | 0.8045 |  |
| Site: UW (vs UAB) | +0.4463 | 0.4215 | ±0.8431 | +1.059 | 0.2898 | 1.5625 |  |
| Age (years) | -0.0276 | 0.0190 | ±0.0381 | -1.448 | 0.1476 | 0.9728 |  |
| BMI (kg/m2) | +0.0176 | 0.0254 | ±0.0507 | +0.694 | 0.4879 | 1.0178 |  |
| Hypertension | -0.3607 | 0.3888 | ±0.7776 | -0.928 | 0.3536 | 0.6972 |  |
| High cholesterol | +0.1197 | 0.3695 | ±0.7391 | +0.324 | 0.7460 | 1.1272 |  |
| Kidney disease | +0.5171 | 0.5118 | ±1.0237 | +1.010 | 0.3124 | 1.6771 |  |
| Circulatory disease | +0.1574 | 0.4393 | ±0.8787 | +0.358 | 0.7201 | 1.1705 |  |
| HbA1c (%) | -0.5128 | 0.3656 | ±0.7312 | -1.403 | 0.1607 | 0.5988 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3829**), AUC = **0.6394**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3650 | 2.2429 | ±4.4859 | +0.163 | 0.8707 | 1.4406 |  |
| Education: graduate level (vs college) | -0.2929 | 0.3825 | ±0.7650 | -0.766 | 0.4439 | 0.7461 |  |
| Education: high school or below (vs college) | +0.4885 | 0.4799 | ±0.9599 | +1.018 | 0.3087 | 1.6300 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6224 | 0.8031 |  |
| Site: UW (vs UAB) | +0.4209 | 0.4216 | ±0.8432 | +0.998 | 0.3181 | 1.5233 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0101 | 0.0249 | ±0.0497 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4010 | 0.3901 | ±0.7802 | -1.028 | 0.3039 | 0.6696 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6031 | 0.5052 | ±1.0104 | +1.194 | 0.2326 | 1.8277 |  |
| Circulatory disease | +0.0586 | 0.4348 | ±0.8696 | +0.135 | 0.8928 | 1.0603 |  |
| Mean glucose (mg/dL) | -0.0002 | 0.0132 | ±0.0264 | -0.016 | 0.9872 | 0.9998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3829**), AUC = **0.6394**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3943 | 3.7757 | ±7.5514 | +0.104 | 0.9168 | 1.4833 |  |
| Education: graduate level (vs college) | -0.2929 | 0.3825 | ±0.7650 | -0.766 | 0.4439 | 0.7461 |  |
| Education: high school or below (vs college) | +0.4885 | 0.4799 | ±0.9599 | +1.018 | 0.3087 | 1.6300 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6224 | 0.8031 |  |
| Site: UW (vs UAB) | +0.4209 | 0.4216 | ±0.8432 | +0.998 | 0.3181 | 1.5233 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0101 | 0.0249 | ±0.0497 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4010 | 0.3901 | ±0.7802 | -1.028 | 0.3039 | 0.6696 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6031 | 0.5052 | ±1.0104 | +1.194 | 0.2326 | 1.8277 |  |
| Circulatory disease | +0.0586 | 0.4348 | ±0.8696 | +0.135 | 0.8928 | 1.0603 |  |
| GMI (%) | -0.0088 | 0.5520 | ±1.1039 | -0.016 | 0.9872 | 0.9912 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0546**, LLR χ² = **12.40** (p = **0.3343**), AUC = **0.6469**, AIC = **238.8**, BIC = **278.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8248 | 2.1256 | ±4.2512 | -0.388 | 0.6980 | 0.4383 |  |
| Education: graduate level (vs college) | -0.2940 | 0.3832 | ±0.7664 | -0.767 | 0.4429 | 0.7453 |  |
| Education: high school or below (vs college) | +0.5136 | 0.4787 | ±0.9574 | +1.073 | 0.2833 | 1.6713 |  |
| Site: UCSD (vs UAB) | -0.2164 | 0.4463 | ±0.8927 | -0.485 | 0.6279 | 0.8055 |  |
| Site: UW (vs UAB) | +0.4273 | 0.4216 | ±0.8432 | +1.014 | 0.3108 | 1.5331 |  |
| Age (years) | -0.0271 | 0.0188 | ±0.0377 | -1.438 | 0.1504 | 0.9733 |  |
| BMI (kg/m2) | +0.0074 | 0.0250 | ±0.0499 | +0.297 | 0.7664 | 1.0074 |  |
| Hypertension | -0.4020 | 0.3898 | ±0.7796 | -1.031 | 0.3023 | 0.6690 |  |
| High cholesterol | +0.0317 | 0.3629 | ±0.7258 | +0.087 | 0.9303 | 1.0322 |  |
| Kidney disease | +0.6048 | 0.5033 | ±1.0067 | +1.202 | 0.2295 | 1.8309 |  |
| Circulatory disease | +0.0328 | 0.4365 | ±0.8730 | +0.075 | 0.9401 | 1.0334 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0094 | 0.0116 | ±0.0232 | +0.807 | 0.4198 | 1.0094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0519**, LLR χ² = **11.80** (p = **0.3792**), AUC = **0.6388**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.5012 | 1.7272 | ±3.4543 | +0.290 | 0.7717 | 1.6507 |  |
| Education: graduate level (vs college) | -0.2891 | 0.3827 | ±0.7653 | -0.756 | 0.4499 | 0.7489 |  |
| Education: high school or below (vs college) | +0.5063 | 0.4846 | ±0.9693 | +1.045 | 0.2962 | 1.6591 |  |
| Site: UCSD (vs UAB) | -0.2264 | 0.4467 | ±0.8934 | -0.507 | 0.6124 | 0.7974 |  |
| Site: UW (vs UAB) | +0.4078 | 0.4259 | ±0.8518 | +0.957 | 0.3383 | 1.5035 |  |
| Age (years) | -0.0277 | 0.0189 | ±0.0377 | -1.471 | 0.1414 | 0.9726 |  |
| BMI (kg/m2) | +0.0101 | 0.0248 | ±0.0495 | +0.407 | 0.6840 | 1.0101 |  |
| Hypertension | -0.3907 | 0.3927 | ±0.7854 | -0.995 | 0.3197 | 0.6766 |  |
| High cholesterol | +0.0380 | 0.3626 | ±0.7253 | +0.105 | 0.9166 | 1.0387 |  |
| Kidney disease | +0.6179 | 0.5101 | ±1.0202 | +1.211 | 0.2258 | 1.8550 |  |
| Circulatory disease | +0.0653 | 0.4359 | ±0.8718 | +0.150 | 0.8808 | 1.0675 |  |
| Glucose SD, pooled (mg/dL) | -0.0085 | 0.0389 | ±0.0778 | -0.219 | 0.8268 | 0.9915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0518**, LLR χ² = **11.76** (p = **0.3818**), AUC = **0.6394**, AIC = **239.4**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4197 | 1.6966 | ±3.3932 | +0.247 | 0.8046 | 1.5214 |  |
| Education: graduate level (vs college) | -0.2910 | 0.3826 | ±0.7651 | -0.761 | 0.4468 | 0.7475 |  |
| Education: high school or below (vs college) | +0.4965 | 0.4818 | ±0.9636 | +1.031 | 0.3027 | 1.6430 |  |
| Site: UCSD (vs UAB) | -0.2203 | 0.4454 | ±0.8909 | -0.495 | 0.6209 | 0.8023 |  |
| Site: UW (vs UAB) | +0.4162 | 0.4234 | ±0.8469 | +0.983 | 0.3256 | 1.5162 |  |
| Age (years) | -0.0279 | 0.0189 | ±0.0377 | -1.477 | 0.1397 | 0.9725 |  |
| BMI (kg/m2) | +0.0101 | 0.0248 | ±0.0495 | +0.407 | 0.6838 | 1.0101 |  |
| Hypertension | -0.3936 | 0.3949 | ±0.7897 | -0.997 | 0.3188 | 0.6746 |  |
| High cholesterol | +0.0388 | 0.3626 | ±0.7253 | +0.107 | 0.9148 | 1.0395 |  |
| Kidney disease | +0.6082 | 0.5070 | ±1.0139 | +1.200 | 0.2303 | 1.8371 |  |
| Circulatory disease | +0.0598 | 0.4348 | ±0.8696 | +0.138 | 0.8905 | 1.0617 |  |
| Avg. daily SD (mg/dL) | -0.0048 | 0.0395 | ±0.0789 | -0.121 | 0.9039 | 0.9952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0519**, LLR χ² = **11.80** (p = **0.3786**), AUC = **0.6391**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.5541 | 1.8068 | ±3.6136 | +0.307 | 0.7591 | 1.7403 |  |
| Education: graduate level (vs college) | -0.2869 | 0.3831 | ±0.7663 | -0.749 | 0.4540 | 0.7506 |  |
| Education: high school or below (vs college) | +0.5179 | 0.4933 | ±0.9866 | +1.050 | 0.2938 | 1.6785 |  |
| Site: UCSD (vs UAB) | -0.2274 | 0.4470 | ±0.8939 | -0.509 | 0.6109 | 0.7966 |  |
| Site: UW (vs UAB) | +0.4057 | 0.4263 | ±0.8526 | +0.952 | 0.3412 | 1.5004 |  |
| Age (years) | -0.0276 | 0.0189 | ±0.0378 | -1.463 | 0.1434 | 0.9727 |  |
| BMI (kg/m2) | +0.0097 | 0.0248 | ±0.0496 | +0.392 | 0.6948 | 1.0098 |  |
| Hypertension | -0.3898 | 0.3927 | ±0.7854 | -0.993 | 0.3209 | 0.6772 |  |
| High cholesterol | +0.0375 | 0.3627 | ±0.7253 | +0.103 | 0.9176 | 1.0382 |  |
| Kidney disease | +0.6191 | 0.5098 | ±1.0196 | +1.214 | 0.2246 | 1.8572 |  |
| Circulatory disease | +0.0645 | 0.4356 | ±0.8713 | +0.148 | 0.8823 | 1.0666 |  |
| CV (%) | -0.0138 | 0.0583 | ±0.1167 | -0.236 | 0.8135 | 0.9863 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0520**, LLR χ² = **11.81** (p = **0.3781**), AUC = **0.6403**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6025 | 1.8816 | ±3.7632 | +0.320 | 0.7488 | 1.8267 |  |
| Education: graduate level (vs college) | -0.2984 | 0.3830 | ±0.7660 | -0.779 | 0.4359 | 0.7420 |  |
| Education: high school or below (vs college) | +0.4627 | 0.4892 | ±0.9785 | +0.946 | 0.3442 | 1.5884 |  |
| Site: UCSD (vs UAB) | -0.2130 | 0.4455 | ±0.8909 | -0.478 | 0.6325 | 0.8081 |  |
| Site: UW (vs UAB) | +0.4359 | 0.4257 | ±0.8513 | +1.024 | 0.3058 | 1.5464 |  |
| Age (years) | -0.0285 | 0.0189 | ±0.0378 | -1.507 | 0.1318 | 0.9719 |  |
| BMI (kg/m2) | +0.0101 | 0.0247 | ±0.0495 | +0.408 | 0.6830 | 1.0102 |  |
| Hypertension | -0.4140 | 0.3929 | ±0.7858 | -1.054 | 0.2920 | 0.6610 |  |
| High cholesterol | +0.0417 | 0.3622 | ±0.7244 | +0.115 | 0.9084 | 1.0426 |  |
| Kidney disease | +0.5866 | 0.5082 | ±1.0165 | +1.154 | 0.2484 | 1.7979 |  |
| Circulatory disease | +0.0538 | 0.4348 | ±0.8696 | +0.124 | 0.9014 | 1.0553 |  |
| Mean / SD ratio | -0.0379 | 0.1515 | ±0.3031 | -0.250 | 0.8027 | 0.9628 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0522**, LLR χ² = **11.86** (p = **0.3741**), AUC = **0.6391**, AIC = **239.3**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6606 | 1.8273 | ±3.6545 | +0.362 | 0.7177 | 1.9359 |  |
| Education: graduate level (vs college) | -0.2969 | 0.3825 | ±0.7650 | -0.776 | 0.4376 | 0.7431 |  |
| Education: high school or below (vs college) | +0.4635 | 0.4838 | ±0.9676 | +0.958 | 0.3380 | 1.5897 |  |
| Site: UCSD (vs UAB) | -0.2218 | 0.4448 | ±0.8896 | -0.499 | 0.6180 | 0.8011 |  |
| Site: UW (vs UAB) | +0.4346 | 0.4233 | ±0.8466 | +1.027 | 0.3045 | 1.5444 |  |
| Age (years) | -0.0286 | 0.0189 | ±0.0378 | -1.517 | 0.1293 | 0.9718 |  |
| BMI (kg/m2) | +0.0100 | 0.0247 | ±0.0495 | +0.403 | 0.6873 | 1.0100 |  |
| Hypertension | -0.4248 | 0.3957 | ±0.7913 | -1.074 | 0.2830 | 0.6539 |  |
| High cholesterol | +0.0400 | 0.3622 | ±0.7244 | +0.110 | 0.9120 | 1.0408 |  |
| Kidney disease | +0.5883 | 0.5060 | ±1.0120 | +1.163 | 0.2450 | 1.8010 |  |
| Circulatory disease | +0.0625 | 0.4346 | ±0.8692 | +0.144 | 0.8856 | 1.0645 |  |
| Avg. daily mean/SD | -0.0385 | 0.1148 | ±0.2295 | -0.336 | 0.7369 | 0.9622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0972**, LLR χ² = **22.09** (p = **0.0237**), AUC = **0.6977**, AIC = **229.1**, BIC = **268.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6974 | 1.9043 | ±3.8087 | -1.416 | 0.1566 | 0.0674 |  |
| Education: graduate level (vs college) | -0.3542 | 0.3961 | ±0.7921 | -0.894 | 0.3712 | 0.7018 |  |
| Education: high school or below (vs college) | +0.4185 | 0.4946 | ±0.9893 | +0.846 | 0.3975 | 1.5197 |  |
| Site: UCSD (vs UAB) | -0.1799 | 0.4567 | ±0.9134 | -0.394 | 0.6936 | 0.8353 |  |
| Site: UW (vs UAB) | +0.5325 | 0.4363 | ±0.8727 | +1.220 | 0.2223 | 1.7032 |  |
| Age (years) | -0.0277 | 0.0193 | ±0.0386 | -1.435 | 0.1513 | 0.9727 |  |
| BMI (kg/m2) | +0.0048 | 0.0259 | ±0.0518 | +0.185 | 0.8530 | 1.0048 |  |
| Hypertension | -0.4682 | 0.3985 | ±0.7971 | -1.175 | 0.2401 | 0.6261 |  |
| High cholesterol | -0.0273 | 0.3750 | ±0.7499 | -0.073 | 0.9419 | 0.9730 |  |
| Kidney disease | +0.6626 | 0.5155 | ±1.0310 | +1.285 | 0.1987 | 1.9397 |  |
| Circulatory disease | +0.0949 | 0.4493 | ±0.8987 | +0.211 | 0.8327 | 1.0995 |  |
| **MAG (mg/dL/h)** | **+0.0871** | 0.0283 | ±0.0566 | **+3.077** | **0.0021** | 1.0910 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0533**, LLR χ² = **12.10** (p = **0.3560**), AUC = **0.6436**, AIC = **239.1**, BIC = **278.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1898 | 1.7982 | ±3.5964 | -0.106 | 0.9160 | 0.8272 |  |
| Education: graduate level (vs college) | -0.2973 | 0.3827 | ±0.7654 | -0.777 | 0.4373 | 0.7429 |  |
| Education: high school or below (vs college) | +0.4622 | 0.4795 | ±0.9591 | +0.964 | 0.3351 | 1.5876 |  |
| Site: UCSD (vs UAB) | -0.2091 | 0.4453 | ±0.8907 | -0.469 | 0.6387 | 0.8113 |  |
| Site: UW (vs UAB) | +0.4437 | 0.4232 | ±0.8465 | +1.048 | 0.2945 | 1.5584 |  |
| Age (years) | -0.0288 | 0.0188 | ±0.0376 | -1.531 | 0.1258 | 0.9716 |  |
| BMI (kg/m2) | +0.0107 | 0.0247 | ±0.0494 | +0.433 | 0.6650 | 1.0108 |  |
| Hypertension | -0.4306 | 0.3931 | ±0.7862 | -1.095 | 0.2734 | 0.6501 |  |
| High cholesterol | +0.0427 | 0.3624 | ±0.7247 | +0.118 | 0.9061 | 1.0436 |  |
| Kidney disease | +0.5876 | 0.5040 | ±1.0081 | +1.166 | 0.2437 | 1.7997 |  |
| Circulatory disease | +0.0545 | 0.4349 | ±0.8698 | +0.125 | 0.9003 | 1.0560 |  |
| Avg. daily range (mg/dL) | +0.0059 | 0.0099 | ±0.0197 | +0.594 | 0.5525 | 1.0059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3828**), AUC = **0.6404**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3541 | 1.6295 | ±3.2590 | +0.217 | 0.8280 | 1.4249 |  |
| Education: graduate level (vs college) | -0.2925 | 0.3823 | ±0.7646 | -0.765 | 0.4442 | 0.7464 |  |
| Education: high school or below (vs college) | +0.4923 | 0.4873 | ±0.9747 | +1.010 | 0.3124 | 1.6361 |  |
| Site: UCSD (vs UAB) | -0.2215 | 0.4514 | ±0.9028 | -0.491 | 0.6236 | 0.8013 |  |
| Site: UW (vs UAB) | +0.4186 | 0.4285 | ±0.8570 | +0.977 | 0.3286 | 1.5199 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.488 | 0.1367 | 0.9724 |  |
| BMI (kg/m2) | +0.0100 | 0.0248 | ±0.0495 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4027 | 0.3919 | ±0.7837 | -1.028 | 0.3042 | 0.6685 |  |
| High cholesterol | +0.0409 | 0.3625 | ±0.7250 | +0.113 | 0.9102 | 1.0417 |  |
| Kidney disease | +0.6058 | 0.5141 | ±1.0281 | +1.178 | 0.2386 | 1.8327 |  |
| Circulatory disease | +0.0616 | 0.4469 | ±0.8938 | +0.138 | 0.8903 | 1.0636 |  |
| SD of daily means (mg/dL) | -0.0023 | 0.0711 | ±0.1422 | -0.032 | 0.9747 | 0.9978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0606**, LLR χ² = **13.76** (p = **0.2466**), AUC = **0.6501**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -5.3007 | 4.4830 | ±8.9659 | -1.182 | 0.2370 | 0.0050 |  |
| Education: graduate level (vs college) | -0.2835 | 0.3842 | ±0.7684 | -0.738 | 0.4605 | 0.7531 |  |
| Education: high school or below (vs college) | +0.5278 | 0.4855 | ±0.9709 | +1.087 | 0.2769 | 1.6953 |  |
| Site: UCSD (vs UAB) | -0.2809 | 0.4513 | ±0.9026 | -0.622 | 0.5337 | 0.7551 |  |
| Site: UW (vs UAB) | +0.3635 | 0.4284 | ±0.8568 | +0.849 | 0.3961 | 1.4384 |  |
| Age (years) | -0.0254 | 0.0190 | ±0.0381 | -1.332 | 0.1828 | 0.9749 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.476 | 0.6338 | 1.0120 |  |
| Hypertension | -0.3967 | 0.3935 | ±0.7870 | -1.008 | 0.3134 | 0.6725 |  |
| High cholesterol | +0.0368 | 0.3656 | ±0.7311 | +0.101 | 0.9198 | 1.0375 |  |
| Kidney disease | +0.6759 | 0.5165 | ±1.0331 | +1.308 | 0.1907 | 1.9657 |  |
| Circulatory disease | +0.0869 | 0.4384 | ±0.8768 | +0.198 | 0.8429 | 1.0908 |  |
| Time in range 70-180, pooled (%) | +0.0565 | 0.0424 | ±0.0847 | +1.335 | 0.1819 | 1.0582 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0614**, LLR χ² = **13.95** (p = **0.2359**), AUC = **0.6518**, AIC = **237.3**, BIC = **277.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -5.7016 | 4.5909 | ±9.1818 | -1.242 | 0.2143 | 0.0033 |  |
| Education: graduate level (vs college) | -0.2876 | 0.3845 | ±0.7690 | -0.748 | 0.4545 | 0.7501 |  |
| Education: high school or below (vs college) | +0.5224 | 0.4856 | ±0.9711 | +1.076 | 0.2820 | 1.6860 |  |
| Site: UCSD (vs UAB) | -0.2792 | 0.4512 | ±0.9025 | -0.619 | 0.5361 | 0.7564 |  |
| Site: UW (vs UAB) | +0.3711 | 0.4285 | ±0.8570 | +0.866 | 0.3865 | 1.4493 |  |
| Age (years) | -0.0251 | 0.0191 | ±0.0381 | -1.320 | 0.1869 | 0.9752 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.474 | 0.6357 | 1.0119 |  |
| Hypertension | -0.3909 | 0.3939 | ±0.7878 | -0.992 | 0.3210 | 0.6765 |  |
| High cholesterol | +0.0377 | 0.3658 | ±0.7316 | +0.103 | 0.9178 | 1.0385 |  |
| Kidney disease | +0.6812 | 0.5175 | ±1.0351 | +1.316 | 0.1881 | 1.9762 |  |
| Circulatory disease | +0.0904 | 0.4386 | ±0.8772 | +0.206 | 0.8368 | 1.0946 |  |
| Avg. daily time in range 70-180 (%) | +0.0604 | 0.0434 | ±0.0868 | +1.393 | 0.1637 | 1.0623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0567**, LLR χ² = **12.89** (p = **0.3004**), AUC = **0.6435**, AIC = **238.3**, BIC = **278.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3229 | 1.5738 | ±3.1476 | +0.205 | 0.8374 | 1.3811 |  |
| Education: graduate level (vs college) | -0.2748 | 0.3836 | ±0.7672 | -0.716 | 0.4737 | 0.7597 |  |
| Education: high school or below (vs college) | +0.5729 | 0.4856 | ±0.9712 | +1.180 | 0.2380 | 1.7735 |  |
| Site: UCSD (vs UAB) | -0.2533 | 0.4484 | ±0.8969 | -0.565 | 0.5721 | 0.7762 |  |
| Site: UW (vs UAB) | +0.3846 | 0.4243 | ±0.8487 | +0.906 | 0.3648 | 1.4690 |  |
| Age (years) | -0.0255 | 0.0191 | ±0.0381 | -1.340 | 0.1801 | 0.9748 |  |
| BMI (kg/m2) | +0.0084 | 0.0249 | ±0.0497 | +0.337 | 0.7361 | 1.0084 |  |
| Hypertension | -0.4180 | 0.3922 | ±0.7845 | -1.066 | 0.2865 | 0.6583 |  |
| High cholesterol | +0.0686 | 0.3630 | ±0.7260 | +0.189 | 0.8502 | 1.0710 |  |
| Kidney disease | +0.5876 | 0.5062 | ±1.0124 | +1.161 | 0.2458 | 1.7996 |  |
| Circulatory disease | +0.0934 | 0.4386 | ±0.8771 | +0.213 | 0.8313 | 1.0979 |  |
| Time 54-69, pooled (%) | -0.8187 | 0.8522 | ±1.7044 | -0.961 | 0.3367 | 0.4410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0577**, LLR χ² = **13.12** (p = **0.2859**), AUC = **0.6453**, AIC = **238.1**, BIC = **277.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3185 | 1.5771 | ±3.1541 | +0.202 | 0.8399 | 1.3751 |  |
| Education: graduate level (vs college) | -0.2791 | 0.3840 | ±0.7680 | -0.727 | 0.4674 | 0.7565 |  |
| Education: high school or below (vs college) | +0.5806 | 0.4857 | ±0.9714 | +1.195 | 0.2319 | 1.7872 |  |
| Site: UCSD (vs UAB) | -0.2326 | 0.4474 | ±0.8949 | -0.520 | 0.6032 | 0.7925 |  |
| Site: UW (vs UAB) | +0.3943 | 0.4237 | ±0.8474 | +0.931 | 0.3520 | 1.4833 |  |
| Age (years) | -0.0254 | 0.0191 | ±0.0381 | -1.334 | 0.1821 | 0.9749 |  |
| BMI (kg/m2) | +0.0081 | 0.0249 | ±0.0498 | +0.324 | 0.7457 | 1.0081 |  |
| Hypertension | -0.4128 | 0.3920 | ±0.7840 | -1.053 | 0.2924 | 0.6618 |  |
| High cholesterol | +0.0654 | 0.3628 | ±0.7255 | +0.180 | 0.8568 | 1.0676 |  |
| Kidney disease | +0.5751 | 0.5064 | ±1.0128 | +1.136 | 0.2561 | 1.7773 |  |
| Circulatory disease | +0.0825 | 0.4388 | ±0.8776 | +0.188 | 0.8509 | 1.0860 |  |
| Avg. daily time 54-69 (%) | -0.9362 | 0.9101 | ±1.8202 | -1.029 | 0.3036 | 0.3921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0567**, LLR χ² = **12.89** (p = **0.3004**), AUC = **0.6435**, AIC = **238.3**, BIC = **278.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3229 | 1.5738 | ±3.1476 | +0.205 | 0.8374 | 1.3811 |  |
| Education: graduate level (vs college) | -0.2748 | 0.3836 | ±0.7672 | -0.716 | 0.4737 | 0.7597 |  |
| Education: high school or below (vs college) | +0.5729 | 0.4856 | ±0.9712 | +1.180 | 0.2380 | 1.7735 |  |
| Site: UCSD (vs UAB) | -0.2533 | 0.4484 | ±0.8969 | -0.565 | 0.5721 | 0.7762 |  |
| Site: UW (vs UAB) | +0.3846 | 0.4243 | ±0.8487 | +0.906 | 0.3648 | 1.4690 |  |
| Age (years) | -0.0255 | 0.0191 | ±0.0381 | -1.340 | 0.1801 | 0.9748 |  |
| BMI (kg/m2) | +0.0084 | 0.0249 | ±0.0497 | +0.337 | 0.7361 | 1.0084 |  |
| Hypertension | -0.4180 | 0.3922 | ±0.7845 | -1.066 | 0.2865 | 0.6583 |  |
| High cholesterol | +0.0686 | 0.3630 | ±0.7260 | +0.189 | 0.8502 | 1.0710 |  |
| Kidney disease | +0.5876 | 0.5062 | ±1.0124 | +1.161 | 0.2458 | 1.7996 |  |
| Circulatory disease | +0.0934 | 0.4386 | ±0.8771 | +0.213 | 0.8313 | 1.0979 |  |
| Time < 70 (%) | -0.8187 | 0.8522 | ±1.7044 | -0.961 | 0.3367 | 0.4410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0577**, LLR χ² = **13.12** (p = **0.2859**), AUC = **0.6453**, AIC = **238.1**, BIC = **277.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3185 | 1.5771 | ±3.1541 | +0.202 | 0.8399 | 1.3751 |  |
| Education: graduate level (vs college) | -0.2791 | 0.3840 | ±0.7680 | -0.727 | 0.4674 | 0.7565 |  |
| Education: high school or below (vs college) | +0.5806 | 0.4857 | ±0.9714 | +1.195 | 0.2319 | 1.7872 |  |
| Site: UCSD (vs UAB) | -0.2326 | 0.4474 | ±0.8949 | -0.520 | 0.6032 | 0.7925 |  |
| Site: UW (vs UAB) | +0.3943 | 0.4237 | ±0.8474 | +0.931 | 0.3520 | 1.4833 |  |
| Age (years) | -0.0254 | 0.0191 | ±0.0381 | -1.334 | 0.1821 | 0.9749 |  |
| BMI (kg/m2) | +0.0081 | 0.0249 | ±0.0498 | +0.324 | 0.7457 | 1.0081 |  |
| Hypertension | -0.4128 | 0.3920 | ±0.7840 | -1.053 | 0.2924 | 0.6618 |  |
| High cholesterol | +0.0654 | 0.3628 | ±0.7255 | +0.180 | 0.8568 | 1.0676 |  |
| Kidney disease | +0.5751 | 0.5064 | ±1.0128 | +1.136 | 0.2561 | 1.7773 |  |
| Circulatory disease | +0.0825 | 0.4388 | ±0.8776 | +0.188 | 0.8509 | 1.0860 |  |
| Avg. daily time < 70 (%) | -0.9362 | 0.9101 | ±1.8202 | -1.029 | 0.3036 | 0.3921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0597**, LLR χ² = **13.56** (p = **0.2583**), AUC = **0.6500**, AIC = **237.6**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3557 | 1.5712 | ±3.1424 | +0.226 | 0.8209 | 1.4271 |  |
| Education: graduate level (vs college) | -0.2865 | 0.3840 | ±0.7679 | -0.746 | 0.4555 | 0.7509 |  |
| Education: high school or below (vs college) | +0.5192 | 0.4847 | ±0.9694 | +1.071 | 0.2840 | 1.6807 |  |
| Site: UCSD (vs UAB) | -0.2749 | 0.4507 | ±0.9014 | -0.610 | 0.5419 | 0.7597 |  |
| Site: UW (vs UAB) | +0.3690 | 0.4278 | ±0.8555 | +0.863 | 0.3883 | 1.4463 |  |
| Age (years) | -0.0257 | 0.0190 | ±0.0380 | -1.354 | 0.1757 | 0.9746 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.477 | 0.6331 | 1.0120 |  |
| Hypertension | -0.3966 | 0.3931 | ±0.7863 | -1.009 | 0.3131 | 0.6726 |  |
| High cholesterol | +0.0346 | 0.3653 | ±0.7307 | +0.095 | 0.9246 | 1.0352 |  |
| Kidney disease | +0.6739 | 0.5159 | ±1.0319 | +1.306 | 0.1915 | 1.9618 |  |
| Circulatory disease | +0.0820 | 0.4379 | ±0.8758 | +0.187 | 0.8515 | 1.0854 |  |
| Time 181-250, pooled (%) | -0.0529 | 0.0416 | ±0.0832 | -1.272 | 0.2033 | 0.9484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0604**, LLR χ² = **13.71** (p = **0.2493**), AUC = **0.6504**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3472 | 1.5696 | ±3.1392 | +0.221 | 0.8249 | 1.4151 |  |
| Education: graduate level (vs college) | -0.2903 | 0.3842 | ±0.7685 | -0.756 | 0.4499 | 0.7480 |  |
| Education: high school or below (vs college) | +0.5139 | 0.4848 | ±0.9695 | +1.060 | 0.2891 | 1.6717 |  |
| Site: UCSD (vs UAB) | -0.2745 | 0.4508 | ±0.9015 | -0.609 | 0.5425 | 0.7599 |  |
| Site: UW (vs UAB) | +0.3755 | 0.4279 | ±0.8557 | +0.878 | 0.3801 | 1.4558 |  |
| Age (years) | -0.0256 | 0.0190 | ±0.0380 | -1.346 | 0.1784 | 0.9747 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.475 | 0.6350 | 1.0119 |  |
| Hypertension | -0.3917 | 0.3934 | ±0.7869 | -0.996 | 0.3195 | 0.6759 |  |
| High cholesterol | +0.0355 | 0.3656 | ±0.7311 | +0.097 | 0.9226 | 1.0362 |  |
| Kidney disease | +0.6791 | 0.5169 | ±1.0337 | +1.314 | 0.1889 | 1.9721 |  |
| Circulatory disease | +0.0858 | 0.4380 | ±0.8760 | +0.196 | 0.8448 | 1.0895 |  |
| Avg. daily time 181-250 (%) | -0.0561 | 0.0425 | ±0.0849 | -1.322 | 0.1860 | 0.9454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0597**, LLR χ² = **13.56** (p = **0.2583**), AUC = **0.6500**, AIC = **237.6**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3557 | 1.5712 | ±3.1424 | +0.226 | 0.8209 | 1.4271 |  |
| Education: graduate level (vs college) | -0.2865 | 0.3840 | ±0.7679 | -0.746 | 0.4555 | 0.7509 |  |
| Education: high school or below (vs college) | +0.5192 | 0.4847 | ±0.9694 | +1.071 | 0.2840 | 1.6807 |  |
| Site: UCSD (vs UAB) | -0.2749 | 0.4507 | ±0.9014 | -0.610 | 0.5419 | 0.7597 |  |
| Site: UW (vs UAB) | +0.3690 | 0.4278 | ±0.8555 | +0.863 | 0.3883 | 1.4463 |  |
| Age (years) | -0.0257 | 0.0190 | ±0.0380 | -1.354 | 0.1757 | 0.9746 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.477 | 0.6331 | 1.0120 |  |
| Hypertension | -0.3966 | 0.3931 | ±0.7863 | -1.009 | 0.3131 | 0.6726 |  |
| High cholesterol | +0.0346 | 0.3653 | ±0.7307 | +0.095 | 0.9246 | 1.0352 |  |
| Kidney disease | +0.6739 | 0.5159 | ±1.0319 | +1.306 | 0.1915 | 1.9618 |  |
| Circulatory disease | +0.0820 | 0.4379 | ±0.8758 | +0.187 | 0.8515 | 1.0854 |  |
| Time > 180 (%) | -0.0529 | 0.0416 | ±0.0832 | -1.272 | 0.2033 | 0.9484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0604**, LLR χ² = **13.71** (p = **0.2493**), AUC = **0.6504**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3472 | 1.5696 | ±3.1392 | +0.221 | 0.8249 | 1.4151 |  |
| Education: graduate level (vs college) | -0.2903 | 0.3842 | ±0.7685 | -0.756 | 0.4499 | 0.7480 |  |
| Education: high school or below (vs college) | +0.5139 | 0.4848 | ±0.9695 | +1.060 | 0.2891 | 1.6717 |  |
| Site: UCSD (vs UAB) | -0.2745 | 0.4508 | ±0.9015 | -0.609 | 0.5425 | 0.7599 |  |
| Site: UW (vs UAB) | +0.3755 | 0.4279 | ±0.8557 | +0.878 | 0.3801 | 1.4558 |  |
| Age (years) | -0.0256 | 0.0190 | ±0.0380 | -1.346 | 0.1784 | 0.9747 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.475 | 0.6350 | 1.0119 |  |
| Hypertension | -0.3917 | 0.3934 | ±0.7869 | -0.996 | 0.3195 | 0.6759 |  |
| High cholesterol | +0.0355 | 0.3656 | ±0.7311 | +0.097 | 0.9226 | 1.0362 |  |
| Kidney disease | +0.6791 | 0.5169 | ±1.0337 | +1.314 | 0.1889 | 1.9721 |  |
| Circulatory disease | +0.0858 | 0.4380 | ±0.8760 | +0.196 | 0.8448 | 1.0895 |  |
| Avg. daily time > 180 (%) | -0.0561 | 0.0425 | ±0.0849 | -1.322 | 0.1860 | 0.9454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0521**, LLR χ² = **11.84** (p = **0.3754**), AUC = **0.6405**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3285 | 1.5615 | ±3.1231 | +0.210 | 0.8334 | 1.3889 |  |
| Education: graduate level (vs college) | -0.2938 | 0.3823 | ±0.7646 | -0.769 | 0.4421 | 0.7454 |  |
| Education: high school or below (vs college) | +0.5080 | 0.4824 | ±0.9648 | +1.053 | 0.2923 | 1.6620 |  |
| Site: UCSD (vs UAB) | -0.2433 | 0.4522 | ±0.9044 | -0.538 | 0.5906 | 0.7840 |  |
| Site: UW (vs UAB) | +0.4003 | 0.4268 | ±0.8536 | +0.938 | 0.3483 | 1.4922 |  |
| Age (years) | -0.0276 | 0.0189 | ±0.0377 | -1.466 | 0.1425 | 0.9727 |  |
| BMI (kg/m2) | +0.0110 | 0.0250 | ±0.0499 | +0.442 | 0.6585 | 1.0111 |  |
| Hypertension | -0.4186 | 0.3940 | ±0.7881 | -1.062 | 0.2880 | 0.6579 |  |
| High cholesterol | +0.0451 | 0.3627 | ±0.7253 | +0.124 | 0.9011 | 1.0461 |  |
| Kidney disease | +0.6227 | 0.5096 | ±1.0193 | +1.222 | 0.2218 | 1.8639 |  |
| Circulatory disease | +0.0681 | 0.4359 | ±0.8718 | +0.156 | 0.8758 | 1.0705 |  |
| Nocturnal time > 180 (%) | -0.0102 | 0.0331 | ±0.0661 | -0.308 | 0.7578 | 0.9899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 46 single-predictor tests; 8 with raw p < 0.05 (about 2 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 204): best single predictor out of sample is **MAG** (CV R² 0.034 vs 0.014 for covariates alone, gain +0.020; +0.819 per SD, p = 0.021). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.021), TIR 70-180 (pooled) (p = 0.043), TIR 70-180 (daily avg) (p = 0.043), %181-250 (daily avg) (p = 0.044), %>180 (daily avg) (p = 0.044).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 204): best single predictor out of sample is **MAG** (CV AUC 0.593 vs 0.506 for covariates alone, gain +0.087; OR 1.76 per SD, p = 0.002). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.002).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.087, via MAG); CES-D-10 depressive symptoms (0-30) (+0.020, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 2 raw-significant of 16); Range 70-180 (0 FDR-significant / 2 raw-significant of 4); Band 181-250 (0 FDR-significant / 2 raw-significant of 4).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (MAG, ΔAIC -2.4); Clinically relevant depressive symptoms (MAG, ΔAIC -8.2).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
