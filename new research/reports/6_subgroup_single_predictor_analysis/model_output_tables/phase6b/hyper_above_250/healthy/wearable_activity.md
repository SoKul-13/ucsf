# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 218; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **218**, R² = **0.1805**, Adj R² = **0.1410**, F-statistic = **4.56** (p = **7.51e-06**), Residual SE = **3791.965** on **207** df, AIC = **4222.3**, BIC = **4259.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17110.1703** | 2233.2517 | ±4466.5034 | **+7.662** | **1.84e-14** | *** |
| Education: graduate level (vs college) | -505.7855 | 503.0871 | ±1006.1741 | -1.005 | 0.3147 |  |
| Education: high school or below (vs college) | +3090.6699 | 1913.3797 | ±3826.7595 | +1.615 | 0.1062 |  |
| Site: UCSD (vs UAB) | +1482.8834 | 895.0404 | ±1790.0807 | +1.657 | 0.0976 | . |
| Site: UW (vs UAB) | +771.5487 | 584.9014 | ±1169.8028 | +1.319 | 0.1871 |  |
| **Age (years)** | **-108.0952** | 26.1377 | ±52.2755 | **-4.136** | **3.54e-05** | *** |
| BMI (kg/m2) | -40.6528 | 43.7436 | ±87.4872 | -0.929 | 0.3527 |  |
| Hypertension | -1060.7786 | 611.8647 | ±1223.7293 | -1.734 | 0.0830 | . |
| High cholesterol | +594.3359 | 587.9378 | ±1175.8757 | +1.011 | 0.3121 |  |
| Kidney disease | +397.4573 | 1426.7867 | ±2853.5734 | +0.279 | 0.7806 |  |
| Circulatory disease | -1203.2000 | 1088.6872 | ±2177.3745 | -1.105 | 0.2691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **218**, R² = **0.1835**, Adj R² = **0.1399**, F-statistic = **4.21** (p = **1.24e-05**), Residual SE = **3794.226** on **206** df, AIC = **4223.5**, BIC = **4264.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15727.7638** | 2502.3236 | ±5004.6472 | **+6.285** | **3.27e-10** | *** |
| Education: graduate level (vs college) | -501.9816 | 503.8621 | ±1007.7243 | -0.996 | 0.3191 |  |
| Education: high school or below (vs college) | +2988.7176 | 1958.5936 | ±3917.1873 | +1.526 | 0.1270 |  |
| Site: UCSD (vs UAB) | +1461.9548 | 903.1953 | ±1806.3906 | +1.619 | 0.1055 |  |
| Site: UW (vs UAB) | +750.8197 | 589.1331 | ±1178.2661 | +1.274 | 0.2025 |  |
| **Age (years)** | **-108.1140** | 26.1220 | ±52.2440 | **-4.139** | **3.49e-05** | *** |
| BMI (kg/m2) | -44.4551 | 44.8843 | ±89.7687 | -0.990 | 0.3220 |  |
| Hypertension | -1061.8065 | 612.6274 | ±1225.2548 | -1.733 | 0.0831 | . |
| High cholesterol | +542.0678 | 594.6251 | ±1189.2502 | +0.912 | 0.3620 |  |
| Kidney disease | +434.3540 | 1419.7703 | ±2839.5406 | +0.306 | 0.7597 |  |
| Circulatory disease | -1315.2644 | 1095.5579 | ±2191.1158 | -1.201 | 0.2299 |  |
| HbA1c (%) | +259.2581 | 274.8800 | ±549.7600 | +0.943 | 0.3456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **218**, R² = **0.1806**, Adj R² = **0.1368**, F-statistic = **4.13** (p = **1.68e-05**), Residual SE = **3801.085** on **206** df, AIC = **4224.3**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17208.7174** | 2479.5725 | ±4959.1450 | **+6.940** | **3.92e-12** | *** |
| Education: graduate level (vs college) | -501.9276 | 505.9030 | ±1011.8060 | -0.992 | 0.3211 |  |
| Education: high school or below (vs college) | +3099.9211 | 1969.6049 | ±3939.2099 | +1.574 | 0.1155 |  |
| Site: UCSD (vs UAB) | +1483.5603 | 902.1911 | ±1804.3823 | +1.644 | 0.1001 |  |
| Site: UW (vs UAB) | +774.2517 | 590.3767 | ±1180.7534 | +1.311 | 0.1897 |  |
| **Age (years)** | **-108.1589** | 26.2115 | ±52.4231 | **-4.126** | **3.69e-05** | *** |
| BMI (kg/m2) | -40.0620 | 45.4436 | ±90.8873 | -0.882 | 0.3780 |  |
| Hypertension | -1058.5449 | 617.1148 | ±1234.2297 | -1.715 | 0.0863 | . |
| High cholesterol | +597.9478 | 595.5037 | ±1191.0074 | +1.004 | 0.3153 |  |
| Kidney disease | +399.9384 | 1433.2498 | ±2866.4995 | +0.279 | 0.7802 |  |
| Circulatory disease | -1196.5239 | 1107.9228 | ±2215.8456 | -1.080 | 0.2802 |  |
| Mean glucose (mg/dL) | -0.8489 | 11.4763 | ±22.9526 | -0.074 | 0.9410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **218**, R² = **0.1806**, Adj R² = **0.1368**, F-statistic = **4.13** (p = **1.68e-05**), Residual SE = **3801.085** on **206** df, AIC = **4224.3**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17326.1795** | 3481.1390 | ±6962.2780 | **+4.977** | **6.45e-07** | *** |
| Education: graduate level (vs college) | -501.9276 | 505.9030 | ±1011.8060 | -0.992 | 0.3211 |  |
| Education: high school or below (vs college) | +3099.9211 | 1969.6049 | ±3939.2099 | +1.574 | 0.1155 |  |
| Site: UCSD (vs UAB) | +1483.5603 | 902.1911 | ±1804.3823 | +1.644 | 0.1001 |  |
| Site: UW (vs UAB) | +774.2517 | 590.3767 | ±1180.7534 | +1.311 | 0.1897 |  |
| **Age (years)** | **-108.1589** | 26.2115 | ±52.4231 | **-4.126** | **3.69e-05** | *** |
| BMI (kg/m2) | -40.0620 | 45.4436 | ±90.8873 | -0.882 | 0.3780 |  |
| Hypertension | -1058.5449 | 617.1148 | ±1234.2297 | -1.715 | 0.0863 | . |
| High cholesterol | +597.9478 | 595.5037 | ±1191.0074 | +1.004 | 0.3153 |  |
| Kidney disease | +399.9384 | 1433.2498 | ±2866.4995 | +0.279 | 0.7802 |  |
| Circulatory disease | -1196.5239 | 1107.9228 | ±2215.8456 | -1.080 | 0.2802 |  |
| GMI (%) | -35.4870 | 479.7780 | ±959.5561 | -0.074 | 0.9410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **218**, R² = **0.1808**, Adj R² = **0.1371**, F-statistic = **4.13** (p = **1.64e-05**), Residual SE = **3800.521** on **206** df, AIC = **4224.2**, BIC = **4264.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16861.2034** | 2321.0966 | ±4642.1932 | **+7.264** | **3.75e-13** | *** |
| Education: graduate level (vs college) | -511.5516 | 504.2465 | ±1008.4931 | -1.014 | 0.3104 |  |
| Education: high school or below (vs college) | +3069.7118 | 1952.1236 | ±3904.2471 | +1.572 | 0.1158 |  |
| Site: UCSD (vs UAB) | +1476.3786 | 904.1882 | ±1808.3763 | +1.633 | 0.1025 |  |
| Site: UW (vs UAB) | +766.7852 | 588.4338 | ±1176.8677 | +1.303 | 0.1925 |  |
| **Age (years)** | **-107.7297** | 26.1440 | ±52.2879 | **-4.121** | **3.78e-05** | *** |
| BMI (kg/m2) | -42.7966 | 45.6451 | ±91.2902 | -0.938 | 0.3485 |  |
| Hypertension | -1066.7558 | 615.5941 | ±1231.1882 | -1.733 | 0.0831 | . |
| High cholesterol | +583.6874 | 593.9636 | ±1187.9273 | +0.983 | 0.3258 |  |
| Kidney disease | +410.7695 | 1433.2734 | ±2866.5469 | +0.287 | 0.7744 |  |
| Circulatory disease | -1222.6128 | 1100.2974 | ±2200.5947 | -1.111 | 0.2665 |  |
| Nocturnal mean 00-06h (mg/dL) | +2.2550 | 9.0268 | ±18.0536 | +0.250 | 0.8027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1821**, Adj R² = **0.1384**, F-statistic = **4.17** (p = **1.45e-05**), Residual SE = **3797.631** on **206** df, AIC = **4223.9**, BIC = **4264.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17718.2352** | 2398.5675 | ±4797.1350 | **+7.387** | **1.50e-13** | *** |
| Education: graduate level (vs college) | -506.2824 | 504.7126 | ±1009.4252 | -1.003 | 0.3158 |  |
| Education: high school or below (vs college) | +3088.8214 | 1928.9644 | ±3857.9288 | +1.601 | 0.1093 |  |
| Site: UCSD (vs UAB) | +1455.5968 | 895.0864 | ±1790.1728 | +1.626 | 0.1039 |  |
| Site: UW (vs UAB) | +759.7304 | 585.2559 | ±1170.5118 | +1.298 | 0.1942 |  |
| **Age (years)** | **-107.7953** | 26.2410 | ±52.4819 | **-4.108** | **3.99e-05** | *** |
| BMI (kg/m2) | -38.1328 | 44.5251 | ±89.0502 | -0.856 | 0.3918 |  |
| Hypertension | -1044.9431 | 618.3333 | ±1236.6666 | -1.690 | 0.0910 | . |
| High cholesterol | +569.7868 | 594.9877 | ±1189.9755 | +0.958 | 0.3382 |  |
| Kidney disease | +510.9180 | 1487.5921 | ±2975.1841 | +0.343 | 0.7313 |  |
| Circulatory disease | -1164.4718 | 1091.1261 | ±2182.2521 | -1.067 | 0.2859 |  |
| Glucose SD, pooled (mg/dL) | -22.7042 | 41.9352 | ±83.8705 | -0.541 | 0.5882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1818**, Adj R² = **0.1381**, F-statistic = **4.16** (p = **1.49e-05**), Residual SE = **3798.329** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17588.5226** | 2336.3502 | ±4672.7003 | **+7.528** | **5.14e-14** | *** |
| Education: graduate level (vs college) | -500.1483 | 505.5486 | ±1011.0973 | -0.989 | 0.3225 |  |
| Education: high school or below (vs college) | +3084.8243 | 1925.1359 | ±3850.2717 | +1.602 | 0.1091 |  |
| Site: UCSD (vs UAB) | +1464.7980 | 895.8687 | ±1791.7375 | +1.635 | 0.1020 |  |
| Site: UW (vs UAB) | +764.7524 | 585.6773 | ±1171.3547 | +1.306 | 0.1916 |  |
| **Age (years)** | **-107.8419** | 26.2756 | ±52.5511 | **-4.104** | **4.06e-05** | *** |
| BMI (kg/m2) | -37.5587 | 44.9829 | ±89.9659 | -0.835 | 0.4037 |  |
| Hypertension | -1039.1713 | 618.2117 | ±1236.4235 | -1.681 | 0.0928 | . |
| High cholesterol | +569.2402 | 592.5782 | ±1185.1565 | +0.961 | 0.3367 |  |
| Kidney disease | +484.9997 | 1476.1589 | ±2952.3178 | +0.329 | 0.7425 |  |
| Circulatory disease | -1160.5719 | 1091.6047 | ±2183.2094 | -1.063 | 0.2877 |  |
| Avg. daily SD (mg/dL) | -21.0043 | 43.6581 | ±87.3162 | -0.481 | 0.6304 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **218**, R² = **0.1815**, Adj R² = **0.1378**, F-statistic = **4.15** (p = **1.53e-05**), Residual SE = **3798.856** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17764.1279** | 2621.5805 | ±5243.1611 | **+6.776** | **1.23e-11** | *** |
| Education: graduate level (vs college) | -531.3778 | 507.0034 | ±1014.0068 | -1.048 | 0.2946 |  |
| Education: high school or below (vs college) | +3045.1178 | 1934.9668 | ±3869.9337 | +1.574 | 0.1155 |  |
| Site: UCSD (vs UAB) | +1448.4569 | 903.2333 | ±1806.4665 | +1.604 | 0.1088 |  |
| Site: UW (vs UAB) | +738.4002 | 581.6592 | ±1163.3183 | +1.269 | 0.2043 |  |
| **Age (years)** | **-107.3750** | 26.2739 | ±52.5478 | **-4.087** | **4.37e-05** | *** |
| BMI (kg/m2) | -41.3303 | 44.0182 | ±88.0365 | -0.939 | 0.3478 |  |
| Hypertension | -1062.6873 | 615.2514 | ±1230.5028 | -1.727 | 0.0841 | . |
| High cholesterol | +546.3233 | 607.7837 | ±1215.5674 | +0.899 | 0.3687 |  |
| Kidney disease | +477.6579 | 1476.6020 | ±2953.2041 | +0.323 | 0.7463 |  |
| Circulatory disease | -1201.3008 | 1091.5470 | ±2183.0941 | -1.101 | 0.2711 |  |
| CV (%) | -28.2363 | 59.6200 | ±119.2400 | -0.474 | 0.6358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **218**, R² = **0.1808**, Adj R² = **0.1371**, F-statistic = **4.13** (p = **1.65e-05**), Residual SE = **3800.549** on **206** df, AIC = **4224.2**, BIC = **4264.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16775.1194** | 2656.6304 | ±5313.2607 | **+6.314** | **2.71e-10** | *** |
| Education: graduate level (vs college) | -512.3988 | 506.1844 | ±1012.3688 | -1.012 | 0.3114 |  |
| Education: high school or below (vs college) | +3075.7069 | 1930.6082 | ±3861.2164 | +1.593 | 0.1111 |  |
| Site: UCSD (vs UAB) | +1469.5337 | 899.7905 | ±1799.5810 | +1.633 | 0.1024 |  |
| Site: UW (vs UAB) | +756.8807 | 580.3309 | ±1160.6619 | +1.304 | 0.1922 |  |
| **Age (years)** | **-107.7942** | 26.2647 | ±52.5294 | **-4.104** | **4.06e-05** | *** |
| BMI (kg/m2) | -41.0689 | 43.9853 | ±87.9706 | -0.934 | 0.3505 |  |
| Hypertension | -1056.1868 | 616.7806 | ±1233.5613 | -1.712 | 0.0868 | . |
| High cholesterol | +574.2118 | 607.0407 | ±1214.0815 | +0.946 | 0.3442 |  |
| Kidney disease | +431.9588 | 1475.0254 | ±2950.0507 | +0.293 | 0.7696 |  |
| Circulatory disease | -1202.1297 | 1092.3592 | ±2184.7184 | -1.100 | 0.2711 |  |
| Mean / SD ratio | +73.4245 | 299.4080 | ±598.8161 | +0.245 | 0.8063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1806**, Adj R² = **0.1368**, F-statistic = **4.13** (p = **1.68e-05**), Residual SE = **3801.056** on **206** df, AIC = **4224.3**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17242.2745** | 2643.9550 | ±5287.9100 | **+6.521** | **6.97e-11** | *** |
| Education: graduate level (vs college) | -504.9853 | 506.4934 | ±1012.9867 | -0.997 | 0.3188 |  |
| Education: high school or below (vs college) | +3096.1688 | 1919.4524 | ±3838.9047 | +1.613 | 0.1067 |  |
| Site: UCSD (vs UAB) | +1486.3696 | 895.3520 | ±1790.7040 | +1.660 | 0.0969 | . |
| Site: UW (vs UAB) | +777.8252 | 579.3249 | ±1158.6498 | +1.343 | 0.1794 |  |
| **Age (years)** | **-108.2654** | 26.3276 | ±52.6552 | **-4.112** | **3.92e-05** | *** |
| BMI (kg/m2) | -40.6439 | 43.8573 | ±87.7147 | -0.927 | 0.3541 |  |
| Hypertension | -1063.9161 | 614.1307 | ±1228.2614 | -1.732 | 0.0832 | . |
| High cholesterol | +602.9884 | 601.4934 | ±1202.9868 | +1.002 | 0.3161 |  |
| Kidney disease | +384.2023 | 1464.2395 | ±2928.4791 | +0.262 | 0.7930 |  |
| Circulatory disease | -1203.9523 | 1092.1347 | ±2184.2694 | -1.102 | 0.2703 |  |
| Avg. daily mean/SD | -23.3457 | 227.7135 | ±455.4270 | -0.103 | 0.9183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **218**, R² = **0.1866**, Adj R² = **0.1431**, F-statistic = **4.29** (p = **9.10e-06**), Residual SE = **3787.184** on **206** df, AIC = **4222.7**, BIC = **4263.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15272.5501** | 2868.3075 | ±5736.6150 | **+5.325** | **1.01e-07** | *** |
| Education: graduate level (vs college) | -439.2449 | 511.6568 | ±1023.3136 | -0.858 | 0.3906 |  |
| Education: high school or below (vs college) | +3165.7382 | 1893.5160 | ±3787.0319 | +1.672 | 0.0945 | . |
| Site: UCSD (vs UAB) | +1566.7240 | 897.0208 | ±1794.0415 | +1.747 | 0.0807 | . |
| Site: UW (vs UAB) | +929.3434 | 594.6103 | ±1189.2206 | +1.563 | 0.1181 |  |
| **Age (years)** | **-106.7888** | 26.2235 | ±52.4470 | **-4.072** | **4.66e-05** | *** |
| BMI (kg/m2) | -47.4801 | 42.8693 | ±85.7386 | -1.108 | 0.2681 |  |
| Hypertension | -963.5764 | 615.9861 | ±1231.9722 | -1.564 | 0.1178 |  |
| High cholesterol | +712.9420 | 592.0604 | ±1184.1209 | +1.204 | 0.2285 |  |
| Kidney disease | +408.6609 | 1405.5583 | ±2811.1166 | +0.291 | 0.7712 |  |
| Circulatory disease | -1209.3703 | 1090.5254 | ±2181.0509 | -1.109 | 0.2674 |  |
| MAG (mg/dL/h) | +38.9300 | 30.6065 | ±61.2130 | +1.272 | 0.2034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **218**, R² = **0.1807**, Adj R² = **0.1370**, F-statistic = **4.13** (p = **1.66e-05**), Residual SE = **3800.691** on **206** df, AIC = **4224.2**, BIC = **4264.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17404.5337** | 2632.2553 | ±5264.5107 | **+6.612** | **3.79e-11** | *** |
| Education: graduate level (vs college) | -505.8285 | 506.0371 | ±1012.0741 | -1.000 | 0.3175 |  |
| Education: high school or below (vs college) | +3091.1797 | 1926.8264 | ±3853.6529 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +1469.4409 | 898.5703 | ±1797.1407 | +1.635 | 0.1020 |  |
| Site: UW (vs UAB) | +760.1852 | 585.3366 | ±1170.6732 | +1.299 | 0.1940 |  |
| **Age (years)** | **-108.1698** | 26.2774 | ±52.5549 | **-4.116** | **3.85e-05** | *** |
| BMI (kg/m2) | -39.8359 | 44.3794 | ±88.7587 | -0.898 | 0.3694 |  |
| Hypertension | -1058.9936 | 615.8909 | ±1231.7819 | -1.719 | 0.0855 | . |
| High cholesterol | +576.0539 | 593.8070 | ±1187.6140 | +0.970 | 0.3320 |  |
| Kidney disease | +417.9580 | 1446.1374 | ±2892.2747 | +0.289 | 0.7726 |  |
| Circulatory disease | -1190.1547 | 1096.2921 | ±2192.5842 | -1.086 | 0.2776 |  |
| Avg. daily range (mg/dL) | -2.2307 | 11.3173 | ±22.6345 | -0.197 | 0.8437 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **218**, R² = **0.1813**, Adj R² = **0.1376**, F-statistic = **4.15** (p = **1.56e-05**), Residual SE = **3799.367** on **206** df, AIC = **4224.1**, BIC = **4264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17303.5868** | 2225.7848 | ±4451.5696 | **+7.774** | **7.60e-15** | *** |
| Education: graduate level (vs college) | -519.4213 | 509.4573 | ±1018.9146 | -1.020 | 0.3079 |  |
| Education: high school or below (vs college) | +3096.3476 | 1919.5263 | ±3839.0526 | +1.613 | 0.1067 |  |
| Site: UCSD (vs UAB) | +1471.5758 | 891.5254 | ±1783.0508 | +1.651 | 0.0988 | . |
| Site: UW (vs UAB) | +773.7266 | 588.0201 | ±1176.0402 | +1.316 | 0.1882 |  |
| **Age (years)** | **-107.7267** | 26.2948 | ±52.5896 | **-4.097** | **4.19e-05** | *** |
| BMI (kg/m2) | -39.8306 | 44.0161 | ±88.0322 | -0.905 | 0.3655 |  |
| Hypertension | -1069.2851 | 614.4389 | ±1228.8779 | -1.740 | 0.0818 | . |
| High cholesterol | +603.1974 | 589.4661 | ±1178.9321 | +1.023 | 0.3062 |  |
| Kidney disease | +429.0190 | 1433.2928 | ±2866.5856 | +0.299 | 0.7647 |  |
| Circulatory disease | -1207.8306 | 1091.4909 | ±2182.9819 | -1.107 | 0.2685 |  |
| SD of daily means (mg/dL) | -27.2648 | 57.8475 | ±115.6950 | -0.471 | 0.6374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **218**, R² = **0.1819**, Adj R² = **0.1382**, F-statistic = **4.16** (p = **1.47e-05**), Residual SE = **3797.985** on **206** df, AIC = **4223.9**, BIC = **4264.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16121.9143** | 3282.5453 | ±6565.0906 | **+4.911** | **9.04e-07** | *** |
| Education: graduate level (vs college) | -495.1587 | 504.9295 | ±1009.8590 | -0.981 | 0.3268 |  |
| Education: high school or below (vs college) | +3125.2346 | 1946.0740 | ±3892.1480 | +1.606 | 0.1083 |  |
| Site: UCSD (vs UAB) | +1474.0419 | 899.7875 | ±1799.5750 | +1.638 | 0.1014 |  |
| Site: UW (vs UAB) | +770.3541 | 586.6176 | ±1173.2351 | +1.313 | 0.1891 |  |
| **Age (years)** | **-108.7459** | 26.1522 | ±52.3044 | **-4.158** | **3.21e-05** | *** |
| BMI (kg/m2) | -35.8351 | 46.4945 | ±92.9890 | -0.771 | 0.4409 |  |
| Hypertension | -1051.6904 | 618.9197 | ±1237.8393 | -1.699 | 0.0893 | . |
| High cholesterol | +611.5228 | 594.9629 | ±1189.9258 | +1.028 | 0.3040 |  |
| Kidney disease | +447.7313 | 1442.0154 | ±2884.0308 | +0.310 | 0.7562 |  |
| Circulatory disease | -1174.0312 | 1101.5324 | ±2203.0649 | -1.066 | 0.2865 |  |
| Time in range 70-180, pooled (%) | +10.0406 | 21.9515 | ±43.9030 | +0.457 | 0.6474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **218**, R² = **0.1822**, Adj R² = **0.1385**, F-statistic = **4.17** (p = **1.43e-05**), Residual SE = **3797.362** on **206** df, AIC = **4223.9**, BIC = **4264.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16028.8572** | 3294.1877 | ±6588.3754 | **+4.866** | **1.14e-06** | *** |
| Education: graduate level (vs college) | -492.3676 | 505.0034 | ±1010.0068 | -0.975 | 0.3296 |  |
| Education: high school or below (vs college) | +3124.4517 | 1944.2027 | ±3888.4055 | +1.607 | 0.1080 |  |
| Site: UCSD (vs UAB) | +1470.5865 | 899.4523 | ±1798.9046 | +1.635 | 0.1021 |  |
| Site: UW (vs UAB) | +768.8461 | 586.4497 | ±1172.8993 | +1.311 | 0.1899 |  |
| **Age (years)** | **-108.7367** | 26.1467 | ±52.2934 | **-4.159** | **3.20e-05** | *** |
| BMI (kg/m2) | -35.2834 | 46.6335 | ±93.2670 | -0.757 | 0.4493 |  |
| Hypertension | -1049.9624 | 619.0780 | ±1238.1560 | -1.696 | 0.0899 | . |
| High cholesterol | +613.6663 | 595.0725 | ±1190.1450 | +1.031 | 0.3024 |  |
| Kidney disease | +453.7205 | 1441.6574 | ±2883.3148 | +0.315 | 0.7530 |  |
| Circulatory disease | -1172.9042 | 1100.6808 | ±2201.3616 | -1.066 | 0.2866 |  |
| Avg. daily time in range 70-180 (%) | +10.8765 | 21.7520 | ±43.5040 | +0.500 | 0.6171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.1808**, Adj R² = **0.1370**, F-statistic = **4.13** (p = **1.65e-05**), Residual SE = **3800.656** on **206** df, AIC = **4224.2**, BIC = **4264.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17136.3424** | 2259.6860 | ±4519.3720 | **+7.584** | **3.36e-14** | *** |
| Education: graduate level (vs college) | -516.9433 | 506.7382 | ±1013.4764 | -1.020 | 0.3077 |  |
| Education: high school or below (vs college) | +3071.9031 | 1907.5221 | ±3815.0441 | +1.610 | 0.1073 |  |
| Site: UCSD (vs UAB) | +1474.1201 | 899.5039 | ±1799.0078 | +1.639 | 0.1013 |  |
| Site: UW (vs UAB) | +757.8885 | 588.6560 | ±1177.3120 | +1.287 | 0.1979 |  |
| **Age (years)** | **-107.9658** | 26.2274 | ±52.4548 | **-4.117** | **3.85e-05** | *** |
| BMI (kg/m2) | -39.7485 | 43.6537 | ±87.3073 | -0.911 | 0.3625 |  |
| Hypertension | -1063.2855 | 612.4536 | ±1224.9072 | -1.736 | 0.0825 | . |
| High cholesterol | +581.6833 | 585.8225 | ±1171.6451 | +0.993 | 0.3207 |  |
| Kidney disease | +398.8170 | 1430.2909 | ±2860.5819 | +0.279 | 0.7804 |  |
| Circulatory disease | -1191.8138 | 1093.7351 | ±2187.4701 | -1.090 | 0.2759 |  |
| Any reading < 54 during wear (0/1) | -137.3729 | 569.6795 | ±1139.3591 | -0.241 | 0.8094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.1811**, Adj R² = **0.1374**, F-statistic = **4.14** (p = **1.59e-05**), Residual SE = **3799.771** on **206** df, AIC = **4224.1**, BIC = **4264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17173.6157** | 2253.1906 | ±4506.3813 | **+7.622** | **2.50e-14** | *** |
| Education: graduate level (vs college) | -528.0691 | 509.6793 | ±1019.3585 | -1.036 | 0.3002 |  |
| Education: high school or below (vs college) | +3062.3839 | 1915.2653 | ±3830.5305 | +1.599 | 0.1098 |  |
| Site: UCSD (vs UAB) | +1456.9565 | 901.2056 | ±1802.4112 | +1.617 | 0.1059 |  |
| Site: UW (vs UAB) | +735.1454 | 592.0568 | ±1184.1136 | +1.242 | 0.2144 |  |
| **Age (years)** | **-107.3261** | 26.2174 | ±52.4348 | **-4.094** | **4.25e-05** | *** |
| BMI (kg/m2) | -42.0620 | 44.2899 | ±88.5799 | -0.950 | 0.3423 |  |
| Hypertension | -1072.9699 | 613.8666 | ±1227.7331 | -1.748 | 0.0805 | . |
| High cholesterol | +572.4025 | 592.0754 | ±1184.1507 | +0.967 | 0.3337 |  |
| Kidney disease | +392.0827 | 1425.4529 | ±2850.9058 | +0.275 | 0.7833 |  |
| Circulatory disease | -1207.4167 | 1087.7708 | ±2175.5415 | -1.110 | 0.2670 |  |
| Time < 54 (%) | -102.8508 | 209.3255 | ±418.6510 | -0.491 | 0.6232 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.1813**, Adj R² = **0.1375**, F-statistic = **4.15** (p = **1.57e-05**), Residual SE = **3799.489** on **206** df, AIC = **4224.1**, BIC = **4264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17171.5884** | 2250.5158 | ±4501.0316 | **+7.630** | **2.35e-14** | *** |
| Education: graduate level (vs college) | -528.7821 | 509.2478 | ±1018.4955 | -1.038 | 0.2991 |  |
| Education: high school or below (vs college) | +3058.4452 | 1916.3193 | ±3832.6386 | +1.596 | 0.1105 |  |
| Site: UCSD (vs UAB) | +1453.2094 | 902.9372 | ±1805.8745 | +1.609 | 0.1075 |  |
| Site: UW (vs UAB) | +725.6726 | 594.5940 | ±1189.1879 | +1.220 | 0.2223 |  |
| **Age (years)** | **-107.2428** | 26.2337 | ±52.4673 | **-4.088** | **4.35e-05** | *** |
| BMI (kg/m2) | -41.7642 | 44.0563 | ±88.1125 | -0.948 | 0.3431 |  |
| Hypertension | -1074.8461 | 613.7818 | ±1227.5637 | -1.751 | 0.0799 | . |
| High cholesterol | +564.4288 | 593.0681 | ±1186.1362 | +0.952 | 0.3412 |  |
| Kidney disease | +392.6024 | 1425.4050 | ±2850.8101 | +0.275 | 0.7830 |  |
| Circulatory disease | -1207.3737 | 1087.6359 | ±2175.2717 | -1.110 | 0.2670 |  |
| Avg. daily time < 54 (%) | -149.2827 | 199.6899 | ±399.3798 | -0.748 | 0.4547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.1817**, Adj R² = **0.1380**, F-statistic = **4.16** (p = **1.50e-05**), Residual SE = **3798.458** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17162.1973** | 2248.9353 | ±4497.8706 | **+7.631** | **2.32e-14** | *** |
| Education: graduate level (vs college) | -544.4394 | 511.3250 | ±1022.6500 | -1.065 | 0.2870 |  |
| Education: high school or below (vs college) | +3039.1195 | 1920.2498 | ±3840.4996 | +1.583 | 0.1135 |  |
| Site: UCSD (vs UAB) | +1452.2345 | 904.7361 | ±1809.4722 | +1.605 | 0.1085 |  |
| Site: UW (vs UAB) | +721.4924 | 592.1462 | ±1184.2923 | +1.218 | 0.2231 |  |
| **Age (years)** | **-107.6763** | 26.1731 | ±52.3463 | **-4.114** | **3.89e-05** | *** |
| BMI (kg/m2) | -38.8720 | 43.6438 | ±87.2875 | -0.891 | 0.3731 |  |
| Hypertension | -1076.8748 | 612.6273 | ±1225.2546 | -1.758 | 0.0788 | . |
| High cholesterol | +550.1133 | 594.7798 | ±1189.5596 | +0.925 | 0.3550 |  |
| Kidney disease | +398.1859 | 1420.7344 | ±2841.4689 | +0.280 | 0.7793 |  |
| Circulatory disease | -1204.9806 | 1086.3199 | ±2172.6399 | -1.109 | 0.2673 |  |
| Time 54-69, pooled (%) | -108.5740 | 141.2804 | ±282.5609 | -0.769 | 0.4422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **218**, R² = **0.1814**, Adj R² = **0.1377**, F-statistic = **4.15** (p = **1.54e-05**), Residual SE = **3799.091** on **206** df, AIC = **4224.1**, BIC = **4264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17154.2062** | 2246.1358 | ±4492.2716 | **+7.637** | **2.22e-14** | *** |
| Education: graduate level (vs college) | -540.3824 | 510.5630 | ±1021.1261 | -1.058 | 0.2899 |  |
| Education: high school or below (vs college) | +3041.8386 | 1923.8072 | ±3847.6145 | +1.581 | 0.1138 |  |
| Site: UCSD (vs UAB) | +1454.8749 | 904.8994 | ±1809.7989 | +1.608 | 0.1079 |  |
| Site: UW (vs UAB) | +723.3677 | 593.0517 | ±1186.1034 | +1.220 | 0.2226 |  |
| **Age (years)** | **-107.6044** | 26.1808 | ±52.3615 | **-4.110** | **3.96e-05** | *** |
| BMI (kg/m2) | -39.3465 | 43.7240 | ±87.4480 | -0.900 | 0.3682 |  |
| Hypertension | -1075.6632 | 612.6023 | ±1225.2046 | -1.756 | 0.0791 | . |
| High cholesterol | +553.2031 | 595.9173 | ±1191.8346 | +0.928 | 0.3532 |  |
| Kidney disease | +398.2673 | 1422.2277 | ±2844.4553 | +0.280 | 0.7795 |  |
| Circulatory disease | -1207.5639 | 1087.5442 | ±2175.0884 | -1.110 | 0.2668 |  |
| Avg. daily time 54-69 (%) | -90.4774 | 143.0926 | ±286.1853 | -0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **218**, R² = **0.1818**, Adj R² = **0.1381**, F-statistic = **4.16** (p = **1.49e-05**), Residual SE = **3798.285** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17192.2556** | 2257.2966 | ±4514.5932 | **+7.616** | **2.61e-14** | *** |
| Education: graduate level (vs college) | -548.6740 | 513.7982 | ±1027.5964 | -1.068 | 0.2856 |  |
| Education: high school or below (vs college) | +3034.5150 | 1919.3577 | ±3838.7154 | +1.581 | 0.1139 |  |
| Site: UCSD (vs UAB) | +1442.8637 | 906.6531 | ±1813.3063 | +1.591 | 0.1115 |  |
| Site: UW (vs UAB) | +710.5137 | 595.4365 | ±1190.8730 | +1.193 | 0.2328 |  |
| **Age (years)** | **-107.2462** | 26.1784 | ±52.3568 | **-4.097** | **4.19e-05** | *** |
| BMI (kg/m2) | -40.4505 | 43.7135 | ±87.4270 | -0.925 | 0.3548 |  |
| Hypertension | -1080.7585 | 613.5860 | ±1227.1720 | -1.761 | 0.0782 | . |
| High cholesterol | +547.8613 | 595.6763 | ±1191.3527 | +0.920 | 0.3577 |  |
| Kidney disease | +394.0463 | 1421.2511 | ±2842.5022 | +0.277 | 0.7816 |  |
| Circulatory disease | -1207.4986 | 1086.1258 | ±2172.2516 | -1.112 | 0.2662 |  |
| Time < 70 (%) | -74.8917 | 83.7119 | ±167.4238 | -0.895 | 0.3710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **218**, R² = **0.1816**, Adj R² = **0.1379**, F-statistic = **4.15** (p = **1.52e-05**), Residual SE = **3798.775** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17173.0717** | 2250.9164 | ±4501.8329 | **+7.629** | **2.36e-14** | *** |
| Education: graduate level (vs college) | -543.3549 | 512.1152 | ±1024.2304 | -1.061 | 0.2887 |  |
| Education: high school or below (vs college) | +3037.7527 | 1922.6455 | ±3845.2910 | +1.580 | 0.1141 |  |
| Site: UCSD (vs UAB) | +1447.2812 | 906.7092 | ±1813.4185 | +1.596 | 0.1104 |  |
| Site: UW (vs UAB) | +712.7302 | 596.1724 | ±1192.3447 | +1.196 | 0.2319 |  |
| **Age (years)** | **-107.3154** | 26.1980 | ±52.3961 | **-4.096** | **4.20e-05** | *** |
| BMI (kg/m2) | -40.1631 | 43.7188 | ±87.4376 | -0.919 | 0.3583 |  |
| Hypertension | -1078.9001 | 613.1968 | ±1226.3935 | -1.759 | 0.0785 | . |
| High cholesterol | +548.4651 | 596.4806 | ±1192.9611 | +0.920 | 0.3578 |  |
| Kidney disease | +395.8066 | 1422.3108 | ±2844.6216 | +0.278 | 0.7808 |  |
| Circulatory disease | -1208.5360 | 1087.1738 | ±2174.3476 | -1.112 | 0.2663 |  |
| Avg. daily time < 70 (%) | -70.0361 | 91.1922 | ±182.3843 | -0.768 | 0.4425 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.1816**, Adj R² = **0.1379**, F-statistic = **4.16** (p = **1.51e-05**), Residual SE = **3798.608** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18447.2496** | 3494.1840 | ±6988.3679 | **+5.279** | **1.30e-07** | *** |
| Education: graduate level (vs college) | -498.9208 | 505.3025 | ±1010.6051 | -0.987 | 0.3235 |  |
| Education: high school or below (vs college) | +3043.7724 | 1945.8910 | ±3891.7821 | +1.564 | 0.1178 |  |
| Site: UCSD (vs UAB) | +1487.9201 | 898.8531 | ±1797.7061 | +1.655 | 0.0979 | . |
| Site: UW (vs UAB) | +778.2194 | 588.8496 | ±1177.6993 | +1.322 | 0.1863 |  |
| **Age (years)** | **-107.4405** | 26.3077 | ±52.6155 | **-4.084** | **4.43e-05** | *** |
| BMI (kg/m2) | -41.9809 | 44.1414 | ±88.2829 | -0.951 | 0.3416 |  |
| Hypertension | -1043.3395 | 614.4123 | ±1228.8246 | -1.698 | 0.0895 | . |
| High cholesterol | +595.0861 | 590.4421 | ±1180.8842 | +1.008 | 0.3135 |  |
| Kidney disease | +396.6282 | 1431.0026 | ±2862.0052 | +0.277 | 0.7817 |  |
| Circulatory disease | -1246.7998 | 1114.2306 | ±2228.4611 | -1.119 | 0.2631 |  |
| Time 54-250, pooled (%) | -13.8238 | 27.2848 | ±54.5696 | -0.507 | 0.6124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.1817**, Adj R² = **0.1380**, F-statistic = **4.16** (p = **1.51e-05**), Residual SE = **3798.564** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18519.5379** | 3572.4049 | ±7144.8097 | **+5.184** | **2.17e-07** | *** |
| Education: graduate level (vs college) | -499.8469 | 505.1375 | ±1010.2749 | -0.990 | 0.3224 |  |
| Education: high school or below (vs college) | +3043.2289 | 1945.8359 | ±3891.6719 | +1.564 | 0.1178 |  |
| Site: UCSD (vs UAB) | +1487.1676 | 898.7243 | ±1797.4486 | +1.655 | 0.0980 | . |
| Site: UW (vs UAB) | +776.1145 | 588.4809 | ±1176.9617 | +1.319 | 0.1872 |  |
| **Age (years)** | **-107.4220** | 26.3018 | ±52.6036 | **-4.084** | **4.42e-05** | *** |
| BMI (kg/m2) | -42.2645 | 44.2056 | ±88.4112 | -0.956 | 0.3390 |  |
| Hypertension | -1043.0939 | 614.5540 | ±1229.1079 | -1.697 | 0.0896 | . |
| High cholesterol | +594.9098 | 590.4245 | ±1180.8490 | +1.008 | 0.3136 |  |
| Kidney disease | +397.0868 | 1430.6085 | ±2861.2170 | +0.278 | 0.7813 |  |
| Circulatory disease | -1247.5031 | 1113.9809 | ±2227.9619 | -1.120 | 0.2628 |  |
| Avg. daily time 54-250 (%) | -14.4557 | 27.9879 | ±55.9757 | -0.516 | 0.6055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.1890**, Adj R² = **0.1457**, F-statistic = **4.37** (p = **7.03e-06**), Residual SE = **3781.413** on **206** df, AIC = **4222.0**, BIC = **4262.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17019.7589** | 2238.3161 | ±4476.6322 | **+7.604** | **2.88e-14** | *** |
| Education: graduate level (vs college) | -426.6242 | 508.5439 | ±1017.0877 | -0.839 | 0.4015 |  |
| Education: high school or below (vs college) | +3112.4088 | 1901.2498 | ±3802.4995 | +1.637 | 0.1016 |  |
| Site: UCSD (vs UAB) | +1473.1927 | 892.9031 | ±1785.8062 | +1.650 | 0.0990 | . |
| Site: UW (vs UAB) | +805.7076 | 582.9073 | ±1165.8145 | +1.382 | 0.1669 |  |
| **Age (years)** | **-108.9779** | 25.9716 | ±51.9433 | **-4.196** | **2.72e-05** | *** |
| BMI (kg/m2) | -25.4355 | 47.3820 | ±94.7641 | -0.537 | 0.5914 |  |
| Hypertension | -964.8841 | 613.6169 | ±1227.2338 | -1.572 | 0.1158 |  |
| High cholesterol | +684.3644 | 592.7879 | ±1185.5758 | +1.154 | 0.2483 |  |
| Kidney disease | +602.1103 | 1460.2485 | ±2920.4970 | +0.412 | 0.6801 |  |
| Circulatory disease | -1212.8300 | 1088.4090 | ±2176.8179 | -1.114 | 0.2651 |  |
| Time 181-250, pooled (%) | -41.4243 | 29.6096 | ±59.2193 | -1.399 | 0.1618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **218**, R² = **0.1896**, Adj R² = **0.1464**, F-statistic = **4.38** (p = **6.60e-06**), Residual SE = **3780.022** on **206** df, AIC = **4221.9**, BIC = **4262.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17009.7117** | 2236.7097 | ±4473.4194 | **+7.605** | **2.85e-14** | *** |
| Education: graduate level (vs college) | -421.2498 | 508.9765 | ±1017.9531 | -0.828 | 0.4079 |  |
| Education: high school or below (vs college) | +3105.8450 | 1901.5739 | ±3803.1479 | +1.633 | 0.1024 |  |
| Site: UCSD (vs UAB) | +1461.0008 | 891.6875 | ±1783.3749 | +1.638 | 0.1013 |  |
| Site: UW (vs UAB) | +796.5688 | 582.5593 | ±1165.1186 | +1.367 | 0.1715 |  |
| **Age (years)** | **-108.8393** | 25.9687 | ±51.9375 | **-4.191** | **2.78e-05** | *** |
| BMI (kg/m2) | -25.3151 | 47.1772 | ±94.3545 | -0.537 | 0.5915 |  |
| Hypertension | -961.4164 | 614.1363 | ±1228.2727 | -1.565 | 0.1175 |  |
| High cholesterol | +689.0789 | 592.7668 | ±1185.5336 | +1.162 | 0.2450 |  |
| Kidney disease | +611.7660 | 1457.9987 | ±2915.9973 | +0.420 | 0.6748 |  |
| Circulatory disease | -1212.8377 | 1087.1566 | ±2174.3133 | -1.116 | 0.2646 |  |
| Avg. daily time 181-250 (%) | -41.7077 | 28.6070 | ±57.2141 | -1.458 | 0.1449 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **218**, R² = **0.1816**, Adj R² = **0.1379**, F-statistic = **4.16** (p = **1.52e-05**), Residual SE = **3798.736** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17114.3365** | 2235.1538 | ±4470.3077 | **+7.657** | **1.90e-14** | *** |
| Education: graduate level (vs college) | -491.5540 | 505.2826 | ±1010.5651 | -0.973 | 0.3306 |  |
| Education: high school or below (vs college) | +3127.2494 | 1949.5022 | ±3899.0044 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +1479.8626 | 900.2832 | ±1800.5663 | +1.644 | 0.1002 |  |
| Site: UW (vs UAB) | +777.6216 | 587.3672 | ±1174.7344 | +1.324 | 0.1855 |  |
| **Age (years)** | **-108.7596** | 26.1552 | ±52.3104 | **-4.158** | **3.21e-05** | *** |
| BMI (kg/m2) | -36.4897 | 46.5754 | ±93.1507 | -0.783 | 0.4334 |  |
| Hypertension | -1050.5530 | 618.6702 | ±1237.3403 | -1.698 | 0.0895 | . |
| High cholesterol | +614.6861 | 596.4244 | ±1192.8489 | +1.031 | 0.3027 |  |
| Kidney disease | +441.5433 | 1442.4705 | ±2884.9410 | +0.306 | 0.7595 |  |
| Circulatory disease | -1177.3512 | 1101.9266 | ±2203.8531 | -1.068 | 0.2853 |  |
| Time > 180 (%) | -8.7253 | 21.6717 | ±43.3434 | -0.403 | 0.6872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **218**, R² = **0.1819**, Adj R² = **0.1382**, F-statistic = **4.16** (p = **1.48e-05**), Residual SE = **3798.095** on **206** df, AIC = **4223.9**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17107.0981** | 2235.9547 | ±4471.9093 | **+7.651** | **2.00e-14** | *** |
| Education: graduate level (vs college) | -488.5718 | 505.4497 | ±1010.8993 | -0.967 | 0.3337 |  |
| Education: high school or below (vs college) | +3128.2225 | 1947.5764 | ±3895.1528 | +1.606 | 0.1082 |  |
| Site: UCSD (vs UAB) | +1476.8320 | 899.8303 | ±1799.6606 | +1.641 | 0.1007 |  |
| Site: UW (vs UAB) | +777.2995 | 587.1879 | ±1174.3758 | +1.324 | 0.1856 |  |
| **Age (years)** | **-108.7771** | 26.1454 | ±52.2908 | **-4.160** | **3.18e-05** | *** |
| BMI (kg/m2) | -35.9200 | 46.6439 | ±93.2879 | -0.770 | 0.4412 |  |
| Hypertension | -1048.5914 | 618.9430 | ±1237.8859 | -1.694 | 0.0902 | . |
| High cholesterol | +617.9888 | 596.7350 | ±1193.4699 | +1.036 | 0.3004 |  |
| Kidney disease | +447.9922 | 1442.1976 | ±2884.3952 | +0.311 | 0.7561 |  |
| Circulatory disease | -1175.3712 | 1101.0130 | ±2202.0259 | -1.068 | 0.2857 |  |
| Avg. daily time > 180 (%) | -9.7248 | 21.4991 | ±42.9983 | -0.452 | 0.6510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **218**, R² = **0.1806**, Adj R² = **0.1368**, F-statistic = **4.13** (p = **1.69e-05**), Residual SE = **3801.114** on **206** df, AIC = **4224.3**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17106.4621** | 2255.9605 | ±4511.9210 | **+7.583** | **3.38e-14** | *** |
| Education: graduate level (vs college) | -506.6520 | 505.8633 | ±1011.7267 | -1.002 | 0.3166 |  |
| Education: high school or below (vs college) | +3091.0139 | 1925.1152 | ±3850.2304 | +1.606 | 0.1084 |  |
| Site: UCSD (vs UAB) | +1482.8377 | 899.8956 | ±1799.7912 | +1.648 | 0.0994 | . |
| Site: UW (vs UAB) | +771.4279 | 587.3807 | ±1174.7615 | +1.313 | 0.1891 |  |
| **Age (years)** | **-108.2341** | 26.2268 | ±52.4537 | **-4.127** | **3.68e-05** | *** |
| BMI (kg/m2) | -39.9623 | 47.8573 | ±95.7146 | -0.835 | 0.4037 |  |
| Hypertension | -1060.8618 | 615.7573 | ±1231.5146 | -1.723 | 0.0849 | . |
| High cholesterol | +598.0145 | 594.3216 | ±1188.6432 | +1.006 | 0.3143 |  |
| Kidney disease | +395.7979 | 1432.3155 | ±2864.6309 | +0.276 | 0.7823 |  |
| Circulatory disease | -1200.0641 | 1095.1396 | ±2190.2792 | -1.096 | 0.2732 |  |
| Nocturnal time > 180 (%) | -1.1311 | 18.1507 | ±36.3014 | -0.062 | 0.9503 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.1818**, Adj R² = **0.1381**, F-statistic = **4.16** (p = **1.48e-05**), Residual SE = **3798.197** on **206** df, AIC = **4223.9**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17070.3869** | 2245.1309 | ±4490.2618 | **+7.603** | **2.89e-14** | *** |
| Education: graduate level (vs college) | -501.5990 | 504.5681 | ±1009.1361 | -0.994 | 0.3202 |  |
| Education: high school or below (vs college) | +3035.8187 | 1947.9587 | ±3895.9174 | +1.558 | 0.1191 |  |
| Site: UCSD (vs UAB) | +1484.5625 | 898.7189 | ±1797.4377 | +1.652 | 0.0986 | . |
| Site: UW (vs UAB) | +773.4722 | 587.9364 | ±1175.8729 | +1.316 | 0.1883 |  |
| **Age (years)** | **-107.2751** | 26.3241 | ±52.6482 | **-4.075** | **4.60e-05** | *** |
| BMI (kg/m2) | -42.2946 | 44.1945 | ±88.3890 | -0.957 | 0.3386 |  |
| Hypertension | -1043.6842 | 613.6922 | ±1227.3845 | -1.701 | 0.0890 | . |
| High cholesterol | +591.9581 | 590.2958 | ±1180.5916 | +1.003 | 0.3159 |  |
| Kidney disease | +395.7788 | 1430.8201 | ±2861.6403 | +0.277 | 0.7821 |  |
| Circulatory disease | -1250.9834 | 1114.7135 | ±2229.4270 | -1.122 | 0.2618 |  |
| Time > 250 (%) | +14.9559 | 26.9628 | ±53.9255 | +0.555 | 0.5791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 218)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **218**, R² = **0.1818**, Adj R² = **0.1381**, F-statistic = **4.16** (p = **1.48e-05**), Residual SE = **3798.217** on **206** df, AIC = **4224.0**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17077.8867** | 2244.6079 | ±4489.2159 | **+7.608** | **2.77e-14** | *** |
| Education: graduate level (vs college) | -501.8244 | 504.5623 | ±1009.1247 | -0.995 | 0.3199 |  |
| Education: high school or below (vs college) | +3036.7125 | 1947.5459 | ±3895.0918 | +1.559 | 0.1189 |  |
| Site: UCSD (vs UAB) | +1484.3889 | 898.6234 | ±1797.2468 | +1.652 | 0.0986 | . |
| Site: UW (vs UAB) | +771.6805 | 587.7573 | ±1175.5145 | +1.313 | 0.1892 |  |
| **Age (years)** | **-107.2887** | 26.3152 | ±52.6303 | **-4.077** | **4.56e-05** | *** |
| BMI (kg/m2) | -42.4876 | 44.2352 | ±88.4704 | -0.960 | 0.3368 |  |
| Hypertension | -1043.3598 | 613.9645 | ±1227.9290 | -1.699 | 0.0892 | . |
| High cholesterol | +591.8578 | 590.3601 | ±1180.7203 | +1.003 | 0.3161 |  |
| Kidney disease | +396.5602 | 1430.4326 | ±2860.8651 | +0.277 | 0.7816 |  |
| Circulatory disease | -1250.9100 | 1114.2875 | ±2228.5749 | -1.123 | 0.2616 |  |
| Avg. daily time > 250 (%) | +15.4266 | 27.6409 | ±55.2817 | +0.558 | 0.5768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 218; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **218**, R² = **0.2027**, Adj R² = **0.1642**, F-statistic = **5.26** (p = **6.80e-07**), Residual SE = **12.165** on **207** df, AIC = **1718.7**, BIC = **1756.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0842** | 7.3964 | ±14.7928 | **+5.690** | **1.27e-08** | *** |
| Education: graduate level (vs college) | -0.7168 | 1.7108 | ±3.4216 | -0.419 | 0.6752 |  |
| Education: high school or below (vs college) | +8.4977 | 5.0646 | ±10.1291 | +1.678 | 0.0934 | . |
| **Site: UCSD (vs UAB)** | **+7.6286** | 2.8098 | ±5.6196 | **+2.715** | **0.0066** | ** |
| **Site: UW (vs UAB)** | **+4.7975** | 1.8838 | ±3.7676 | **+2.547** | **0.0109** | * |
| **Age (years)** | **-0.3634** | 0.0822 | ±0.1643 | **-4.424** | **9.70e-06** | *** |
| BMI (kg/m2) | +0.0318 | 0.1365 | ±0.2730 | +0.233 | 0.8158 |  |
| Hypertension | -3.5624 | 1.9374 | ±3.8748 | -1.839 | 0.0660 | . |
| High cholesterol | +2.1351 | 1.8235 | ±3.6471 | +1.171 | 0.2417 |  |
| Kidney disease | +4.0439 | 4.6723 | ±9.3447 | +0.865 | 0.3868 |  |
| Circulatory disease | -4.8820 | 3.2042 | ±6.4083 | -1.524 | 0.1276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **218**, R² = **0.2067**, Adj R² = **0.1644**, F-statistic = **4.88** (p = **1.06e-06**), Residual SE = **12.164** on **206** df, AIC = **1719.6**, BIC = **1760.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+36.8771** | 8.7866 | ±17.5732 | **+4.197** | **2.71e-05** | *** |
| Education: graduate level (vs college) | -0.7025 | 1.7137 | ±3.4275 | -0.410 | 0.6819 |  |
| Education: high school or below (vs college) | +8.1137 | 5.1604 | ±10.3209 | +1.572 | 0.1159 |  |
| **Site: UCSD (vs UAB)** | **+7.5497** | 2.8284 | ±5.6567 | **+2.669** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **+4.7194** | 1.9013 | ±3.8027 | **+2.482** | **0.0131** | * |
| **Age (years)** | **-0.3635** | 0.0822 | ±0.1644 | **-4.423** | **9.72e-06** | *** |
| BMI (kg/m2) | +0.0175 | 0.1420 | ±0.2839 | +0.123 | 0.9020 |  |
| Hypertension | -3.5662 | 1.9406 | ±3.8811 | -1.838 | 0.0661 | . |
| High cholesterol | +1.9382 | 1.8356 | ±3.6712 | +1.056 | 0.2910 |  |
| Kidney disease | +4.1828 | 4.6453 | ±9.2906 | +0.900 | 0.3679 |  |
| Circulatory disease | -5.3042 | 3.2642 | ±6.5283 | -1.625 | 0.1042 |  |
| HbA1c (%) | +0.9766 | 1.0334 | ±2.0667 | +0.945 | 0.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **218**, R² = **0.2031**, Adj R² = **0.1605**, F-statistic = **4.77** (p = **1.57e-06**), Residual SE = **12.192** on **206** df, AIC = **1720.6**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9988** | 8.0812 | ±16.1623 | **+5.073** | **3.91e-07** | *** |
| Education: graduate level (vs college) | -0.7593 | 1.7200 | ±3.4401 | -0.441 | 0.6589 |  |
| Education: high school or below (vs college) | +8.3958 | 5.1903 | ±10.3807 | +1.618 | 0.1058 |  |
| **Site: UCSD (vs UAB)** | **+7.6211** | 2.8324 | ±5.6648 | **+2.691** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **+4.7678** | 1.9090 | ±3.8181 | **+2.497** | **0.0125** | * |
| **Age (years)** | **-0.3627** | 0.0826 | ±0.1652 | **-4.390** | **1.13e-05** | *** |
| BMI (kg/m2) | +0.0253 | 0.1452 | ±0.2903 | +0.174 | 0.8617 |  |
| Hypertension | -3.5870 | 1.9613 | ±3.9227 | -1.829 | 0.0674 | . |
| High cholesterol | +2.0953 | 1.8276 | ±3.6551 | +1.147 | 0.2516 |  |
| Kidney disease | +4.0165 | 4.6749 | ±9.3497 | +0.859 | 0.3902 |  |
| Circulatory disease | -4.9556 | 3.2641 | ±6.5283 | -1.518 | 0.1290 |  |
| Mean glucose (mg/dL) | +0.0093 | 0.0372 | ±0.0744 | +0.251 | 0.8016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **218**, R² = **0.2031**, Adj R² = **0.1605**, F-statistic = **4.77** (p = **1.57e-06**), Residual SE = **12.192** on **206** df, AIC = **1720.6**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.7050** | 11.2159 | ±22.4319 | **+3.540** | **4.00e-04** | *** |
| Education: graduate level (vs college) | -0.7593 | 1.7200 | ±3.4401 | -0.441 | 0.6589 |  |
| Education: high school or below (vs college) | +8.3958 | 5.1903 | ±10.3807 | +1.618 | 0.1058 |  |
| **Site: UCSD (vs UAB)** | **+7.6211** | 2.8324 | ±5.6648 | **+2.691** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **+4.7678** | 1.9090 | ±3.8181 | **+2.497** | **0.0125** | * |
| **Age (years)** | **-0.3627** | 0.0826 | ±0.1652 | **-4.390** | **1.13e-05** | *** |
| BMI (kg/m2) | +0.0253 | 0.1452 | ±0.2903 | +0.174 | 0.8617 |  |
| Hypertension | -3.5870 | 1.9613 | ±3.9227 | -1.829 | 0.0674 | . |
| High cholesterol | +2.0953 | 1.8276 | ±3.6551 | +1.147 | 0.2516 |  |
| Kidney disease | +4.0165 | 4.6749 | ±9.3497 | +0.859 | 0.3902 |  |
| Circulatory disease | -4.9556 | 3.2641 | ±6.5283 | -1.518 | 0.1290 |  |
| GMI (%) | +0.3909 | 1.5557 | ±3.1115 | +0.251 | 0.8016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **218**, R² = **0.2039**, Adj R² = **0.1614**, F-statistic = **4.80** (p = **1.45e-06**), Residual SE = **12.186** on **206** df, AIC = **1720.4**, BIC = **1761.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.4297** | 7.7923 | ±15.5845 | **+5.188** | **2.12e-07** | *** |
| Education: graduate level (vs college) | -0.7551 | 1.7141 | ±3.4281 | -0.441 | 0.6595 |  |
| Education: high school or below (vs college) | +8.3584 | 5.1389 | ±10.2777 | +1.627 | 0.1038 |  |
| **Site: UCSD (vs UAB)** | **+7.5853** | 2.8346 | ±5.6692 | **+2.676** | **0.0075** | ** |
| **Site: UW (vs UAB)** | **+4.7659** | 1.8983 | ±3.7966 | **+2.511** | **0.0121** | * |
| **Age (years)** | **-0.3610** | 0.0826 | ±0.1651 | **-4.372** | **1.23e-05** | *** |
| BMI (kg/m2) | +0.0176 | 0.1461 | ±0.2921 | +0.120 | 0.9043 |  |
| Hypertension | -3.6021 | 1.9600 | ±3.9201 | -1.838 | 0.0661 | . |
| High cholesterol | +2.0644 | 1.8245 | ±3.6490 | +1.131 | 0.2579 |  |
| Kidney disease | +4.1323 | 4.6866 | ±9.3732 | +0.882 | 0.3779 |  |
| Circulatory disease | -5.0111 | 3.2463 | ±6.4926 | -1.544 | 0.1227 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0150 | 0.0306 | ±0.0612 | +0.490 | 0.6241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **218**, R² = **0.2033**, Adj R² = **0.1607**, F-statistic = **4.78** (p = **1.55e-06**), Residual SE = **12.190** on **206** df, AIC = **1720.6**, BIC = **1761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.2495** | 7.8612 | ±15.7224 | **+5.502** | **3.76e-08** | *** |
| Education: graduate level (vs college) | -0.7178 | 1.7184 | ±3.4367 | -0.418 | 0.6762 |  |
| Education: high school or below (vs college) | +8.4942 | 5.1146 | ±10.2292 | +1.661 | 0.0968 | . |
| **Site: UCSD (vs UAB)** | **+7.5763** | 2.8187 | ±5.6375 | **+2.688** | **0.0072** | ** |
| **Site: UW (vs UAB)** | **+4.7749** | 1.8861 | ±3.7723 | **+2.532** | **0.0114** | * |
| **Age (years)** | **-0.3628** | 0.0825 | ±0.1651 | **-4.396** | **1.10e-05** | *** |
| BMI (kg/m2) | +0.0366 | 0.1392 | ±0.2785 | +0.263 | 0.7925 |  |
| Hypertension | -3.5320 | 1.9605 | ±3.9210 | -1.802 | 0.0716 | . |
| High cholesterol | +2.0881 | 1.8490 | ±3.6980 | +1.129 | 0.2588 |  |
| Kidney disease | +4.2613 | 4.8645 | ±9.7290 | +0.876 | 0.3810 |  |
| Circulatory disease | -4.8078 | 3.2161 | ±6.4322 | -1.495 | 0.1349 |  |
| Glucose SD, pooled (mg/dL) | -0.0435 | 0.1342 | ±0.2683 | -0.324 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **218**, R² = **0.2032**, Adj R² = **0.1606**, F-statistic = **4.78** (p = **1.56e-06**), Residual SE = **12.191** on **206** df, AIC = **1720.6**, BIC = **1761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0368** | 7.6989 | ±15.3979 | **+5.590** | **2.27e-08** | *** |
| Education: graduate level (vs college) | -0.7056 | 1.7225 | ±3.4451 | -0.410 | 0.6821 |  |
| Education: high school or below (vs college) | +8.4861 | 5.1064 | ±10.2128 | +1.662 | 0.0965 | . |
| **Site: UCSD (vs UAB)** | **+7.5925** | 2.8243 | ±5.6485 | **+2.688** | **0.0072** | ** |
| **Site: UW (vs UAB)** | **+4.7840** | 1.8864 | ±3.7727 | **+2.536** | **0.0112** | * |
| **Age (years)** | **-0.3629** | 0.0826 | ±0.1652 | **-4.393** | **1.12e-05** | *** |
| BMI (kg/m2) | +0.0380 | 0.1412 | ±0.2823 | +0.269 | 0.7880 |  |
| Hypertension | -3.5193 | 1.9675 | ±3.9349 | -1.789 | 0.0737 | . |
| High cholesterol | +2.0852 | 1.8460 | ±3.6921 | +1.130 | 0.2587 |  |
| Kidney disease | +4.2182 | 4.8209 | ±9.6419 | +0.875 | 0.3816 |  |
| Circulatory disease | -4.7972 | 3.2209 | ±6.4418 | -1.489 | 0.1364 |  |
| Avg. daily SD (mg/dL) | -0.0418 | 0.1387 | ±0.2775 | -0.301 | 0.7631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **218**, R² = **0.2041**, Adj R² = **0.1616**, F-statistic = **4.80** (p = **1.41e-06**), Residual SE = **12.184** on **206** df, AIC = **1720.4**, BIC = **1761.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.6099** | 8.7272 | ±17.4543 | **+5.112** | **3.19e-07** | *** |
| Education: graduate level (vs college) | -0.8156 | 1.7168 | ±3.4336 | -0.475 | 0.6347 |  |
| Education: high school or below (vs college) | +8.3218 | 5.1158 | ±10.2315 | +1.627 | 0.1038 |  |
| **Site: UCSD (vs UAB)** | **+7.4956** | 2.8411 | ±5.6821 | **+2.638** | **0.0083** | ** |
| **Site: UW (vs UAB)** | **+4.6695** | 1.8841 | ±3.7681 | **+2.478** | **0.0132** | * |
| **Age (years)** | **-0.3606** | 0.0824 | ±0.1648 | **-4.376** | **1.21e-05** | *** |
| BMI (kg/m2) | +0.0292 | 0.1369 | ±0.2738 | +0.213 | 0.8312 |  |
| Hypertension | -3.5697 | 1.9474 | ±3.8948 | -1.833 | 0.0668 | . |
| High cholesterol | +1.9497 | 1.8550 | ±3.7100 | +1.051 | 0.2932 |  |
| Kidney disease | +4.3536 | 4.8388 | ±9.6776 | +0.900 | 0.3683 |  |
| Circulatory disease | -4.8747 | 3.2107 | ±6.4213 | -1.518 | 0.1289 |  |
| CV (%) | -0.1091 | 0.1929 | ±0.3858 | -0.565 | 0.5719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **218**, R² = **0.2030**, Adj R² = **0.1605**, F-statistic = **4.77** (p = **1.59e-06**), Residual SE = **12.192** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9253** | 8.7555 | ±17.5110 | **+4.674** | **2.95e-06** | *** |
| Education: graduate level (vs college) | -0.7397 | 1.7186 | ±3.4371 | -0.430 | 0.6669 |  |
| Education: high school or below (vs college) | +8.4459 | 5.1024 | ±10.2048 | +1.655 | 0.0979 | . |
| **Site: UCSD (vs UAB)** | **+7.5824** | 2.8307 | ±5.6614 | **+2.679** | **0.0074** | ** |
| **Site: UW (vs UAB)** | **+4.7468** | 1.8805 | ±3.7611 | **+2.524** | **0.0116** | * |
| **Age (years)** | **-0.3624** | 0.0825 | ±0.1650 | **-4.391** | **1.13e-05** | *** |
| BMI (kg/m2) | +0.0304 | 0.1372 | ±0.2744 | +0.221 | 0.8248 |  |
| Hypertension | -3.5465 | 1.9521 | ±3.9042 | -1.817 | 0.0693 | . |
| High cholesterol | +2.0655 | 1.8573 | ±3.7146 | +1.112 | 0.2661 |  |
| Kidney disease | +4.1632 | 4.8265 | ±9.6530 | +0.863 | 0.3884 |  |
| Circulatory disease | -4.8783 | 3.2155 | ±6.4310 | -1.517 | 0.1292 |  |
| Mean / SD ratio | +0.2540 | 1.0073 | ±2.0147 | +0.252 | 0.8009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **218**, R² = **0.2027**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.64e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1768** | 8.6352 | ±17.2703 | **+4.884** | **1.04e-06** | *** |
| Education: graduate level (vs college) | -0.7162 | 1.7203 | ±3.4407 | -0.416 | 0.6772 |  |
| Education: high school or below (vs college) | +8.5015 | 5.0804 | ±10.1608 | +1.673 | 0.0942 | . |
| **Site: UCSD (vs UAB)** | **+7.6310** | 2.8231 | ±5.6462 | **+2.703** | **0.0069** | ** |
| **Site: UW (vs UAB)** | **+4.8019** | 1.8779 | ±3.7558 | **+2.557** | **0.0106** | * |
| **Age (years)** | **-0.3635** | 0.0825 | ±0.1650 | **-4.406** | **1.05e-05** | *** |
| BMI (kg/m2) | +0.0318 | 0.1370 | ±0.2740 | +0.232 | 0.8164 |  |
| Hypertension | -3.5646 | 1.9503 | ±3.9006 | -1.828 | 0.0676 | . |
| High cholesterol | +2.1412 | 1.8576 | ±3.7152 | +1.153 | 0.2490 |  |
| Kidney disease | +4.0346 | 4.7835 | ±9.5671 | +0.843 | 0.3990 |  |
| Circulatory disease | -4.8826 | 3.2154 | ±6.4309 | -1.518 | 0.1289 |  |
| Avg. daily mean/SD | -0.0164 | 0.7590 | ±1.5180 | -0.022 | 0.9828 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **218**, R² = **0.2064**, Adj R² = **0.1640**, F-statistic = **4.87** (p = **1.10e-06**), Residual SE = **12.166** on **206** df, AIC = **1719.7**, BIC = **1760.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.4295** | 9.6399 | ±19.2798 | **+3.883** | **1.03e-04** | *** |
| Education: graduate level (vs college) | -0.5483 | 1.7368 | ±3.4737 | -0.316 | 0.7523 |  |
| Education: high school or below (vs college) | +8.6878 | 5.0221 | ±10.0442 | +1.730 | 0.0836 | . |
| **Site: UCSD (vs UAB)** | **+7.8409** | 2.8307 | ±5.6614 | **+2.770** | **0.0056** | ** |
| **Site: UW (vs UAB)** | **+5.1972** | 1.8986 | ±3.7972 | **+2.737** | **0.0062** | ** |
| **Age (years)** | **-0.3601** | 0.0830 | ±0.1659 | **-4.340** | **1.42e-05** | *** |
| BMI (kg/m2) | +0.0145 | 0.1353 | ±0.2705 | +0.107 | 0.9146 |  |
| Hypertension | -3.3161 | 1.9284 | ±3.8569 | -1.720 | 0.0855 | . |
| High cholesterol | +2.4356 | 1.8586 | ±3.7172 | +1.310 | 0.1900 |  |
| Kidney disease | +4.0722 | 4.6196 | ±9.2392 | +0.882 | 0.3780 |  |
| Circulatory disease | -4.8977 | 3.2112 | ±6.4224 | -1.525 | 0.1272 |  |
| MAG (mg/dL/h) | +0.0986 | 0.1015 | ±0.2031 | +0.971 | 0.3314 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **218**, R² = **0.2028**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.62e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.6736** | 8.7437 | ±17.4874 | **+4.880** | **1.06e-06** | *** |
| Education: graduate level (vs college) | -0.7169 | 1.7207 | ±3.4415 | -0.417 | 0.6770 |  |
| Education: high school or below (vs college) | +8.4987 | 5.1093 | ±10.2186 | +1.663 | 0.0962 | . |
| **Site: UCSD (vs UAB)** | **+7.6016** | 2.8323 | ±5.6645 | **+2.684** | **0.0073** | ** |
| **Site: UW (vs UAB)** | **+4.7748** | 1.8760 | ±3.7521 | **+2.545** | **0.0109** | * |
| **Age (years)** | **-0.3636** | 0.0827 | ±0.1654 | **-4.397** | **1.10e-05** | *** |
| BMI (kg/m2) | +0.0334 | 0.1389 | ±0.2777 | +0.241 | 0.8097 |  |
| Hypertension | -3.5588 | 1.9526 | ±3.9053 | -1.823 | 0.0684 | . |
| High cholesterol | +2.0985 | 1.8567 | ±3.7134 | +1.130 | 0.2584 |  |
| Kidney disease | +4.0849 | 4.7374 | ±9.4748 | +0.862 | 0.3885 |  |
| Circulatory disease | -4.8559 | 3.2251 | ±6.4502 | -1.506 | 0.1322 |  |
| Avg. daily range (mg/dL) | -0.0045 | 0.0362 | ±0.0725 | -0.123 | 0.9019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **218**, R² = **0.2028**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.63e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2333** | 7.4147 | ±14.8294 | **+5.696** | **1.23e-08** | *** |
| Education: graduate level (vs college) | -0.7273 | 1.7379 | ±3.4758 | -0.419 | 0.6756 |  |
| Education: high school or below (vs college) | +8.5021 | 5.0878 | ±10.1756 | +1.671 | 0.0947 | . |
| **Site: UCSD (vs UAB)** | **+7.6198** | 2.8024 | ±5.6048 | **+2.719** | **0.0065** | ** |
| **Site: UW (vs UAB)** | **+4.7992** | 1.8929 | ±3.7857 | **+2.535** | **0.0112** | * |
| **Age (years)** | **-0.3631** | 0.0826 | ±0.1651 | **-4.399** | **1.09e-05** | *** |
| BMI (kg/m2) | +0.0324 | 0.1380 | ±0.2761 | +0.235 | 0.8142 |  |
| Hypertension | -3.5689 | 1.9440 | ±3.8879 | -1.836 | 0.0664 | . |
| High cholesterol | +2.1420 | 1.8252 | ±3.6503 | +1.174 | 0.2406 |  |
| Kidney disease | +4.0682 | 4.7038 | ±9.4077 | +0.865 | 0.3871 |  |
| Circulatory disease | -4.8856 | 3.2119 | ±6.4239 | -1.521 | 0.1282 |  |
| SD of daily means (mg/dL) | -0.0210 | 0.1967 | ±0.3934 | -0.107 | 0.9149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **218**, R² = **0.2028**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.63e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.3854** | 10.9289 | ±21.8578 | **+3.787** | **1.53e-04** | *** |
| Education: graduate level (vs college) | -0.7093 | 1.7165 | ±3.4330 | -0.413 | 0.6794 |  |
| Education: high school or below (vs college) | +8.5221 | 5.1632 | ±10.3265 | +1.651 | 0.0988 | . |
| **Site: UCSD (vs UAB)** | **+7.6223** | 2.8281 | ±5.6562 | **+2.695** | **0.0070** | ** |
| **Site: UW (vs UAB)** | **+4.7967** | 1.8960 | ±3.7920 | **+2.530** | **0.0114** | * |
| **Age (years)** | **-0.3639** | 0.0825 | ±0.1650 | **-4.411** | **1.03e-05** | *** |
| BMI (kg/m2) | +0.0352 | 0.1487 | ±0.2974 | +0.237 | 0.8128 |  |
| Hypertension | -3.5559 | 1.9597 | ±3.9194 | -1.815 | 0.0696 | . |
| High cholesterol | +2.1473 | 1.8376 | ±3.6753 | +1.169 | 0.2426 |  |
| Kidney disease | +4.0794 | 4.7155 | ±9.4311 | +0.865 | 0.3870 |  |
| Circulatory disease | -4.8614 | 3.2421 | ±6.4841 | -1.499 | 0.1337 |  |
| Time in range 70-180, pooled (%) | +0.0071 | 0.0703 | ±0.1407 | +0.101 | 0.9196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **218**, R² = **0.2029**, Adj R² = **0.1603**, F-statistic = **4.77** (p = **1.61e-06**), Residual SE = **12.193** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.0684** | 10.9640 | ±21.9279 | **+3.746** | **1.80e-04** | *** |
| Education: graduate level (vs college) | -0.7042 | 1.7167 | ±3.4334 | -0.410 | 0.6817 |  |
| Education: high school or below (vs college) | +8.5294 | 5.1612 | ±10.3223 | +1.653 | 0.0984 | . |
| **Site: UCSD (vs UAB)** | **+7.6170** | 2.8277 | ±5.6554 | **+2.694** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **+4.7950** | 1.8951 | ±3.7902 | **+2.530** | **0.0114** | * |
| **Age (years)** | **-0.3640** | 0.0825 | ±0.1650 | **-4.413** | **1.02e-05** | *** |
| BMI (kg/m2) | +0.0368 | 0.1492 | ±0.2983 | +0.247 | 0.8049 |  |
| Hypertension | -3.5522 | 1.9615 | ±3.9230 | -1.811 | 0.0701 | . |
| High cholesterol | +2.1533 | 1.8380 | ±3.6760 | +1.172 | 0.2414 |  |
| Kidney disease | +4.0967 | 4.7156 | ±9.4311 | +0.869 | 0.3850 |  |
| Circulatory disease | -4.8536 | 3.2392 | ±6.4784 | -1.498 | 0.1340 |  |
| Avg. daily time in range 70-180 (%) | +0.0102 | 0.0699 | ±0.1397 | +0.146 | 0.8837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.2032**, Adj R² = **0.1607**, F-statistic = **4.78** (p = **1.55e-06**), Residual SE = **12.190** on **206** df, AIC = **1720.6**, BIC = **1761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2140** | 7.5108 | ±15.0215 | **+5.620** | **1.90e-08** | *** |
| Education: graduate level (vs college) | -0.7721 | 1.7141 | ±3.4281 | -0.450 | 0.6524 |  |
| Education: high school or below (vs college) | +8.4046 | 5.0527 | ±10.1053 | +1.663 | 0.0962 | . |
| **Site: UCSD (vs UAB)** | **+7.5851** | 2.8374 | ±5.6749 | **+2.673** | **0.0075** | ** |
| **Site: UW (vs UAB)** | **+4.7298** | 1.8983 | ±3.7965 | **+2.492** | **0.0127** | * |
| **Age (years)** | **-0.3628** | 0.0824 | ±0.1647 | **-4.405** | **1.06e-05** | *** |
| BMI (kg/m2) | +0.0363 | 0.1363 | ±0.2727 | +0.266 | 0.7901 |  |
| Hypertension | -3.5748 | 1.9365 | ±3.8730 | -1.846 | 0.0649 | . |
| High cholesterol | +2.0724 | 1.8176 | ±3.6352 | +1.140 | 0.2542 |  |
| Kidney disease | +4.0506 | 4.6726 | ±9.3451 | +0.867 | 0.3860 |  |
| Circulatory disease | -4.8256 | 3.2193 | ±6.4387 | -1.499 | 0.1339 |  |
| Any reading < 54 during wear (0/1) | -0.6813 | 1.8901 | ±3.7801 | -0.360 | 0.7185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.2030**, Adj R² = **0.1604**, F-statistic = **4.77** (p = **1.59e-06**), Residual SE = **12.192** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2173** | 7.4732 | ±14.9464 | **+5.649** | **1.61e-08** | *** |
| Education: graduate level (vs college) | -0.7635 | 1.7324 | ±3.4648 | -0.441 | 0.6594 |  |
| Education: high school or below (vs college) | +8.4384 | 5.0802 | ±10.1603 | +1.661 | 0.0967 | . |
| **Site: UCSD (vs UAB)** | **+7.5742** | 2.8360 | ±5.6720 | **+2.671** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **+4.7212** | 1.9079 | ±3.8158 | **+2.475** | **0.0133** | * |
| **Age (years)** | **-0.3618** | 0.0822 | ±0.1643 | **-4.403** | **1.07e-05** | *** |
| BMI (kg/m2) | +0.0288 | 0.1384 | ±0.2768 | +0.208 | 0.8349 |  |
| Hypertension | -3.5879 | 1.9409 | ±3.8818 | -1.849 | 0.0645 | . |
| High cholesterol | +2.0891 | 1.8383 | ±3.6766 | +1.136 | 0.2558 |  |
| Kidney disease | +4.0326 | 4.6707 | ±9.3415 | +0.863 | 0.3879 |  |
| Circulatory disease | -4.8909 | 3.2008 | ±6.4016 | -1.528 | 0.1265 |  |
| Time < 54 (%) | -0.2156 | 1.2234 | ±2.4467 | -0.176 | 0.8601 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.2031**, Adj R² = **0.1606**, F-statistic = **4.77** (p = **1.57e-06**), Residual SE = **12.191** on **206** df, AIC = **1720.6**, BIC = **1761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2355** | 7.4680 | ±14.9359 | **+5.656** | **1.55e-08** | *** |
| Education: graduate level (vs college) | -0.7735 | 1.7347 | ±3.4694 | -0.446 | 0.6557 |  |
| Education: high school or below (vs college) | +8.4183 | 5.0802 | ±10.1604 | +1.657 | 0.0975 | . |
| **Site: UCSD (vs UAB)** | **+7.5554** | 2.8437 | ±5.6873 | **+2.657** | **0.0079** | ** |
| **Site: UW (vs UAB)** | **+4.6845** | 1.9144 | ±3.8288 | **+2.447** | **0.0144** | * |
| **Age (years)** | **-0.3613** | 0.0822 | ±0.1644 | **-4.396** | **1.10e-05** | *** |
| BMI (kg/m2) | +0.0291 | 0.1376 | ±0.2751 | +0.211 | 0.8327 |  |
| Hypertension | -3.5970 | 1.9404 | ±3.8807 | -1.854 | 0.0638 | . |
| High cholesterol | +2.0614 | 1.8387 | ±3.6775 | +1.121 | 0.2622 |  |
| Kidney disease | +4.0319 | 4.6706 | ±9.3413 | +0.863 | 0.3880 |  |
| Circulatory disease | -4.8923 | 3.2001 | ±6.4002 | -1.529 | 0.1263 |  |
| Avg. daily time < 54 (%) | -0.3678 | 0.8505 | ±1.7010 | -0.432 | 0.6654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.2041**, Adj R² = **0.1616**, F-statistic = **4.80** (p = **1.40e-06**), Residual SE = **12.183** on **206** df, AIC = **1720.3**, BIC = **1761.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2708** | 7.4583 | ±14.9166 | **+5.668** | **1.45e-08** | *** |
| Education: graduate level (vs college) | -0.8554 | 1.7389 | ±3.4778 | -0.492 | 0.6228 |  |
| Education: high school or below (vs college) | +8.3128 | 5.0870 | ±10.1740 | +1.634 | 0.1022 |  |
| **Site: UCSD (vs UAB)** | **+7.5186** | 2.8408 | ±5.6815 | **+2.647** | **0.0081** | ** |
| **Site: UW (vs UAB)** | **+4.6180** | 1.9006 | ±3.8012 | **+2.430** | **0.0151** | * |
| **Age (years)** | **-0.3619** | 0.0822 | ±0.1644 | **-4.404** | **1.06e-05** | *** |
| BMI (kg/m2) | +0.0382 | 0.1361 | ±0.2722 | +0.281 | 0.7790 |  |
| Hypertension | -3.6201 | 1.9370 | ±3.8741 | -1.869 | 0.0616 | . |
| High cholesterol | +1.9765 | 1.8370 | ±3.6740 | +1.076 | 0.2820 |  |
| Kidney disease | +4.0465 | 4.6504 | ±9.3007 | +0.870 | 0.3842 |  |
| Circulatory disease | -4.8884 | 3.1950 | ±6.3900 | -1.530 | 0.1260 |  |
| Time 54-69, pooled (%) | -0.3894 | 0.4785 | ±0.9570 | -0.814 | 0.4157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **218**, R² = **0.2042**, Adj R² = **0.1617**, F-statistic = **4.81** (p = **1.39e-06**), Residual SE = **12.183** on **206** df, AIC = **1720.3**, BIC = **1760.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2704** | 7.4517 | ±14.9034 | **+5.673** | **1.41e-08** | *** |
| Education: graduate level (vs college) | -0.8631 | 1.7399 | ±3.4798 | -0.496 | 0.6199 |  |
| Education: high school or below (vs college) | +8.2912 | 5.0966 | ±10.1932 | +1.627 | 0.1038 |  |
| **Site: UCSD (vs UAB)** | **+7.5101** | 2.8436 | ±5.6873 | **+2.641** | **0.0083** | ** |
| **Site: UW (vs UAB)** | **+4.5938** | 1.9033 | ±3.8066 | **+2.414** | **0.0158** | * |
| **Age (years)** | **-0.3613** | 0.0822 | ±0.1643 | **-4.398** | **1.09e-05** | *** |
| BMI (kg/m2) | +0.0373 | 0.1364 | ±0.2727 | +0.274 | 0.7843 |  |
| Hypertension | -3.6253 | 1.9362 | ±3.8724 | -1.872 | 0.0612 | . |
| High cholesterol | +1.9612 | 1.8401 | ±3.6802 | +1.066 | 0.2865 |  |
| Kidney disease | +4.0473 | 4.6522 | ±9.3045 | +0.870 | 0.3843 |  |
| Circulatory disease | -4.9005 | 3.1975 | ±6.3950 | -1.533 | 0.1254 |  |
| Avg. daily time 54-69 (%) | -0.3825 | 0.4414 | ±0.8828 | -0.867 | 0.3862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **218**, R² = **0.2038**, Adj R² = **0.1613**, F-statistic = **4.79** (p = **1.45e-06**), Residual SE = **12.186** on **206** df, AIC = **1720.4**, BIC = **1761.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.3356** | 7.4896 | ±14.9792 | **+5.653** | **1.58e-08** | *** |
| Education: graduate level (vs college) | -0.8482 | 1.7467 | ±3.4933 | -0.486 | 0.6273 |  |
| Education: high school or below (vs college) | +8.3257 | 5.0890 | ±10.1781 | +1.636 | 0.1018 |  |
| **Site: UCSD (vs UAB)** | **+7.5060** | 2.8503 | ±5.7005 | **+2.633** | **0.0085** | ** |
| **Site: UW (vs UAB)** | **+4.6106** | 1.9134 | ±3.8269 | **+2.410** | **0.0160** | * |
| **Age (years)** | **-0.3608** | 0.0821 | ±0.1641 | **-4.396** | **1.10e-05** | *** |
| BMI (kg/m2) | +0.0324 | 0.1365 | ±0.2729 | +0.238 | 0.8122 |  |
| Hypertension | -3.6235 | 1.9389 | ±3.8779 | -1.869 | 0.0616 | . |
| High cholesterol | +1.9928 | 1.8428 | ±3.6855 | +1.081 | 0.2795 |  |
| Kidney disease | +4.0334 | 4.6563 | ±9.3127 | +0.866 | 0.3864 |  |
| Circulatory disease | -4.8952 | 3.1947 | ±6.3894 | -1.532 | 0.1254 |  |
| Time < 70 (%) | -0.2294 | 0.3009 | ±0.6018 | -0.762 | 0.4458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **218**, R² = **0.2040**, Adj R² = **0.1615**, F-statistic = **4.80** (p = **1.42e-06**), Residual SE = **12.184** on **206** df, AIC = **1720.4**, BIC = **1761.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.3137** | 7.4724 | ±14.9447 | **+5.663** | **1.49e-08** | *** |
| Education: graduate level (vs college) | -0.8539 | 1.7466 | ±3.4932 | -0.489 | 0.6249 |  |
| Education: high school or below (vs college) | +8.3046 | 5.0962 | ±10.1924 | +1.630 | 0.1032 |  |
| **Site: UCSD (vs UAB)** | **+7.4987** | 2.8531 | ±5.7062 | **+2.628** | **0.0086** | ** |
| **Site: UW (vs UAB)** | **+4.5829** | 1.9156 | ±3.8311 | **+2.392** | **0.0167** | * |
| **Age (years)** | **-0.3606** | 0.0821 | ±0.1643 | **-4.390** | **1.13e-05** | *** |
| BMI (kg/m2) | +0.0336 | 0.1364 | ±0.2728 | +0.246 | 0.8055 |  |
| Hypertension | -3.6285 | 1.9376 | ±3.8752 | -1.873 | 0.0611 | . |
| High cholesterol | +1.9678 | 1.8442 | ±3.6885 | +1.067 | 0.2860 |  |
| Kidney disease | +4.0378 | 4.6567 | ±9.3134 | +0.867 | 0.3859 |  |
| Circulatory disease | -4.9015 | 3.1964 | ±6.3927 | -1.533 | 0.1252 |  |
| Avg. daily time < 70 (%) | -0.2555 | 0.3299 | ±0.6598 | -0.774 | 0.4387 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.2054**, Adj R² = **0.1629**, F-statistic = **4.84** (p = **1.23e-06**), Residual SE = **12.174** on **206** df, AIC = **1720.0**, BIC = **1760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8318** | 12.1241 | ±24.2481 | **+4.028** | **5.63e-05** | *** |
| Education: graduate level (vs college) | -0.6822 | 1.7181 | ±3.4362 | -0.397 | 0.6913 |  |
| Education: high school or below (vs college) | +8.2610 | 5.1326 | ±10.2652 | +1.610 | 0.1075 |  |
| **Site: UCSD (vs UAB)** | **+7.6540** | 2.8182 | ±5.6363 | **+2.716** | **0.0066** | ** |
| **Site: UW (vs UAB)** | **+4.8312** | 1.8966 | ±3.7932 | **+2.547** | **0.0109** | * |
| **Age (years)** | **-0.3601** | 0.0830 | ±0.1661 | **-4.337** | **1.44e-05** | *** |
| BMI (kg/m2) | +0.0251 | 0.1389 | ±0.2778 | +0.181 | 0.8566 |  |
| Hypertension | -3.4743 | 1.9359 | ±3.8718 | -1.795 | 0.0727 | . |
| High cholesterol | +2.1389 | 1.8315 | ±3.6630 | +1.168 | 0.2429 |  |
| Kidney disease | +4.0397 | 4.6850 | ±9.3699 | +0.862 | 0.3885 |  |
| Circulatory disease | -5.1021 | 3.2949 | ±6.5897 | -1.548 | 0.1215 |  |
| Time 54-250, pooled (%) | -0.0698 | 0.0971 | ±0.1941 | -0.719 | 0.4723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.2054**, Adj R² = **0.1629**, F-statistic = **4.84** (p = **1.23e-06**), Residual SE = **12.174** on **206** df, AIC = **1720.0**, BIC = **1760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1172** | 12.4236 | ±24.8473 | **+3.954** | **7.70e-05** | *** |
| Education: graduate level (vs college) | -0.6872 | 1.7178 | ±3.4355 | -0.400 | 0.6891 |  |
| Education: high school or below (vs college) | +8.2610 | 5.1330 | ±10.2660 | +1.609 | 0.1075 |  |
| **Site: UCSD (vs UAB)** | **+7.6499** | 2.8178 | ±5.6356 | **+2.715** | **0.0066** | ** |
| **Site: UW (vs UAB)** | **+4.8203** | 1.8961 | ±3.7922 | **+2.542** | **0.0110** | * |
| **Age (years)** | **-0.3601** | 0.0830 | ±0.1660 | **-4.337** | **1.44e-05** | *** |
| BMI (kg/m2) | +0.0238 | 0.1393 | ±0.2786 | +0.171 | 0.8645 |  |
| Hypertension | -3.4741 | 1.9361 | ±3.8722 | -1.794 | 0.0728 | . |
| High cholesterol | +2.1380 | 1.8315 | ±3.6631 | +1.167 | 0.2431 |  |
| Kidney disease | +4.0420 | 4.6831 | ±9.3661 | +0.863 | 0.3881 |  |
| Circulatory disease | -5.1031 | 3.2930 | ±6.5861 | -1.550 | 0.1212 |  |
| Avg. daily time 54-250 (%) | -0.0721 | 0.0999 | ±0.1997 | -0.722 | 0.4701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.2068**, Adj R² = **0.1644**, F-statistic = **4.88** (p = **1.06e-06**), Residual SE = **12.163** on **206** df, AIC = **1719.6**, BIC = **1760.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.8817** | 7.4729 | ±14.9458 | **+5.604** | **2.09e-08** | *** |
| Education: graduate level (vs college) | -0.5395 | 1.7371 | ±3.4742 | -0.311 | 0.7561 |  |
| Education: high school or below (vs college) | +8.5464 | 5.0439 | ±10.0879 | +1.694 | 0.0902 | . |
| **Site: UCSD (vs UAB)** | **+7.6069** | 2.8168 | ±5.6335 | **+2.701** | **0.0069** | ** |
| **Site: UW (vs UAB)** | **+4.8740** | 1.8913 | ±3.7825 | **+2.577** | **0.0100** | ** |
| **Age (years)** | **-0.3654** | 0.0821 | ±0.1642 | **-4.449** | **8.61e-06** | *** |
| BMI (kg/m2) | +0.0659 | 0.1514 | ±0.3028 | +0.435 | 0.6635 |  |
| Hypertension | -3.3476 | 1.9463 | ±3.8927 | -1.720 | 0.0854 | . |
| High cholesterol | +2.3368 | 1.8284 | ±3.6567 | +1.278 | 0.2012 |  |
| Kidney disease | +4.5022 | 4.7920 | ±9.5839 | +0.940 | 0.3475 |  |
| Circulatory disease | -4.9036 | 3.2204 | ±6.4408 | -1.523 | 0.1278 |  |
| Time 181-250, pooled (%) | -0.0928 | 0.0976 | ±0.1953 | -0.950 | 0.3420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **218**, R² = **0.2070**, Adj R² = **0.1647**, F-statistic = **4.89** (p = **1.03e-06**), Residual SE = **12.162** on **206** df, AIC = **1719.6**, BIC = **1760.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.8603** | 7.4726 | ±14.9453 | **+5.602** | **2.12e-08** | *** |
| Education: graduate level (vs college) | -0.5284 | 1.7383 | ±3.4765 | -0.304 | 0.7611 |  |
| Education: high school or below (vs college) | +8.5315 | 5.0470 | ±10.0941 | +1.690 | 0.0910 | . |
| **Site: UCSD (vs UAB)** | **+7.5798** | 2.8146 | ±5.6292 | **+2.693** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **+4.8533** | 1.8904 | ±3.7807 | **+2.567** | **0.0102** | * |
| **Age (years)** | **-0.3651** | 0.0822 | ±0.1643 | **-4.444** | **8.84e-06** | *** |
| BMI (kg/m2) | +0.0660 | 0.1509 | ±0.3018 | +0.437 | 0.6619 |  |
| Hypertension | -3.3409 | 1.9514 | ±3.9028 | -1.712 | 0.0869 | . |
| High cholesterol | +2.3463 | 1.8280 | ±3.6561 | +1.284 | 0.1993 |  |
| Kidney disease | +4.5215 | 4.7850 | ±9.5701 | +0.945 | 0.3447 |  |
| Circulatory disease | -4.9035 | 3.2172 | ±6.4344 | -1.524 | 0.1275 |  |
| Avg. daily time 181-250 (%) | -0.0930 | 0.0945 | ±0.1890 | -0.983 | 0.3254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **218**, R² = **0.2027**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.63e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0858** | 7.4339 | ±14.8678 | **+5.661** | **1.50e-08** | *** |
| Education: graduate level (vs college) | -0.7114 | 1.7175 | ±3.4350 | -0.414 | 0.6787 |  |
| Education: high school or below (vs college) | +8.5117 | 5.1699 | ±10.3398 | +1.646 | 0.0997 | . |
| **Site: UCSD (vs UAB)** | **+7.6274** | 2.8295 | ±5.6591 | **+2.696** | **0.0070** | ** |
| **Site: UW (vs UAB)** | **+4.7998** | 1.8999 | ±3.7999 | **+2.526** | **0.0115** | * |
| **Age (years)** | **-0.3637** | 0.0825 | ±0.1650 | **-4.409** | **1.04e-05** | *** |
| BMI (kg/m2) | +0.0334 | 0.1490 | ±0.2980 | +0.224 | 0.8227 |  |
| Hypertension | -3.5584 | 1.9594 | ±3.9188 | -1.816 | 0.0694 | . |
| High cholesterol | +2.1429 | 1.8380 | ±3.6760 | +1.166 | 0.2437 |  |
| Kidney disease | +4.0607 | 4.7140 | ±9.4281 | +0.861 | 0.3890 |  |
| Circulatory disease | -4.8722 | 3.2419 | ±6.4838 | -1.503 | 0.1329 |  |
| Time > 180 (%) | -0.0033 | 0.0695 | ±0.1390 | -0.048 | 0.9618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **218**, R² = **0.2028**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.63e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0822** | 7.4399 | ±14.8798 | **+5.656** | **1.55e-08** | *** |
| Education: graduate level (vs college) | -0.7057 | 1.7180 | ±3.4359 | -0.411 | 0.6812 |  |
| Education: high school or below (vs college) | +8.5220 | 5.1674 | ±10.3348 | +1.649 | 0.0991 | . |
| **Site: UCSD (vs UAB)** | **+7.6246** | 2.8286 | ±5.6573 | **+2.696** | **0.0070** | ** |
| **Site: UW (vs UAB)** | **+4.8012** | 1.8995 | ±3.7990 | **+2.528** | **0.0115** | * |
| **Age (years)** | **-0.3639** | 0.0825 | ±0.1650 | **-4.412** | **1.03e-05** | *** |
| BMI (kg/m2) | +0.0349 | 0.1492 | ±0.2985 | +0.234 | 0.8153 |  |
| Hypertension | -3.5545 | 1.9613 | ±3.9227 | -1.812 | 0.0699 | . |
| High cholesterol | +2.1504 | 1.8387 | ±3.6773 | +1.170 | 0.2422 |  |
| Kidney disease | +4.0765 | 4.7142 | ±9.4283 | +0.865 | 0.3872 |  |
| Circulatory disease | -4.8640 | 3.2394 | ±6.4788 | -1.502 | 0.1332 |  |
| Avg. daily time > 180 (%) | -0.0063 | 0.0690 | ±0.1380 | -0.091 | 0.9274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **218**, R² = **0.2028**, Adj R² = **0.1602**, F-statistic = **4.76** (p = **1.63e-06**), Residual SE = **12.194** on **206** df, AIC = **1720.7**, BIC = **1761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0988** | 7.4752 | ±14.9504 | **+5.632** | **1.78e-08** | *** |
| Education: graduate level (vs college) | -0.7134 | 1.7207 | ±3.4413 | -0.415 | 0.6784 |  |
| Education: high school or below (vs college) | +8.4963 | 5.1176 | ±10.2352 | +1.660 | 0.0969 | . |
| **Site: UCSD (vs UAB)** | **+7.6287** | 2.8278 | ±5.6556 | **+2.698** | **0.0070** | ** |
| **Site: UW (vs UAB)** | **+4.7980** | 1.8934 | ±3.7868 | **+2.534** | **0.0113** | * |
| **Age (years)** | **-0.3629** | 0.0826 | ±0.1652 | **-4.394** | **1.11e-05** | *** |
| BMI (kg/m2) | +0.0291 | 0.1518 | ±0.3036 | +0.192 | 0.8481 |  |
| Hypertension | -3.5620 | 1.9524 | ±3.9048 | -1.824 | 0.0681 | . |
| High cholesterol | +2.1206 | 1.8327 | ±3.6654 | +1.157 | 0.2472 |  |
| Kidney disease | +4.0504 | 4.6929 | ±9.3858 | +0.863 | 0.3881 |  |
| Circulatory disease | -4.8944 | 3.2253 | ±6.4506 | -1.517 | 0.1291 |  |
| Nocturnal time > 180 (%) | +0.0045 | 0.0616 | ±0.1233 | +0.072 | 0.9424 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.2056**, Adj R² = **0.1631**, F-statistic = **4.85** (p = **1.20e-06**), Residual SE = **12.173** on **206** df, AIC = **1720.0**, BIC = **1760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.8915** | 7.4491 | ±14.8983 | **+5.624** | **1.87e-08** | *** |
| Education: graduate level (vs college) | -0.6965 | 1.7160 | ±3.4320 | -0.406 | 0.6848 |  |
| Education: high school or below (vs college) | +8.2319 | 5.1379 | ±10.2757 | +1.602 | 0.1091 |  |
| **Site: UCSD (vs UAB)** | **+7.6367** | 2.8184 | ±5.6368 | **+2.710** | **0.0067** | ** |
| **Site: UW (vs UAB)** | **+4.8068** | 1.8948 | ±3.7895 | **+2.537** | **0.0112** | * |
| **Age (years)** | **-0.3594** | 0.0831 | ±0.1662 | **-4.325** | **1.52e-05** | *** |
| BMI (kg/m2) | +0.0238 | 0.1392 | ±0.2783 | +0.171 | 0.8639 |  |
| Hypertension | -3.4795 | 1.9346 | ±3.8691 | -1.799 | 0.0721 | . |
| High cholesterol | +2.1236 | 1.8296 | ±3.6592 | +1.161 | 0.2458 |  |
| Kidney disease | +4.0357 | 4.6842 | ±9.3684 | +0.862 | 0.3889 |  |
| Circulatory disease | -5.1136 | 3.2952 | ±6.5904 | -1.552 | 0.1207 |  |
| Time > 250 (%) | +0.0725 | 0.0970 | ±0.1941 | +0.747 | 0.4552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 218)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **218**, R² = **0.2055**, Adj R² = **0.1631**, F-statistic = **4.85** (p = **1.21e-06**), Residual SE = **12.173** on **206** df, AIC = **1720.0**, BIC = **1760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9279** | 7.4490 | ±14.8979 | **+5.629** | **1.82e-08** | *** |
| Education: graduate level (vs college) | -0.6976 | 1.7161 | ±3.4322 | -0.407 | 0.6844 |  |
| Education: high school or below (vs college) | +8.2364 | 5.1369 | ±10.2737 | +1.603 | 0.1088 |  |
| **Site: UCSD (vs UAB)** | **+7.6358** | 2.8179 | ±5.6358 | **+2.710** | **0.0067** | ** |
| **Site: UW (vs UAB)** | **+4.7982** | 1.8948 | ±3.7897 | **+2.532** | **0.0113** | * |
| **Age (years)** | **-0.3595** | 0.0831 | ±0.1662 | **-4.328** | **1.51e-05** | *** |
| BMI (kg/m2) | +0.0229 | 0.1394 | ±0.2789 | +0.164 | 0.8694 |  |
| Hypertension | -3.4780 | 1.9349 | ±3.8698 | -1.797 | 0.0723 | . |
| High cholesterol | +2.1231 | 1.8298 | ±3.6597 | +1.160 | 0.2459 |  |
| Kidney disease | +4.0395 | 4.6825 | ±9.3650 | +0.863 | 0.3883 |  |
| Circulatory disease | -5.1130 | 3.2931 | ±6.5863 | -1.553 | 0.1205 |  |
| Avg. daily time > 250 (%) | +0.0747 | 0.0994 | ±0.1988 | +0.751 | 0.4525 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 218; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **218**, R² = **0.1149**, Adj R² = **0.0721**, F-statistic = **2.69** (p = **0.0041**), Residual SE = **7.192** on **207** df, AIC = **1489.6**, BIC = **1526.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9989** | 4.5896 | ±9.1792 | **+13.726** | **7.06e-43** | *** |
| Education: graduate level (vs college) | +0.5415 | 1.0477 | ±2.0953 | +0.517 | 0.6053 |  |
| Education: high school or below (vs college) | +3.3085 | 2.8876 | ±5.7752 | +1.146 | 0.2519 |  |
| Site: UCSD (vs UAB) | -1.1076 | 1.6674 | ±3.3348 | -0.664 | 0.5065 |  |
| Site: UW (vs UAB) | -1.8258 | 1.2755 | ±2.5510 | -1.431 | 0.1523 |  |
| **Age (years)** | **-0.1209** | 0.0522 | ±0.1043 | **-2.318** | **0.0204** | * |
| BMI (kg/m2) | +0.1663 | 0.0853 | ±0.1707 | +1.949 | 0.0513 | . |
| Hypertension | -0.7291 | 1.0957 | ±2.1913 | -0.665 | 0.5058 |  |
| High cholesterol | +1.5352 | 1.0641 | ±2.1282 | +1.443 | 0.1491 |  |
| Kidney disease | +0.9842 | 3.1112 | ±6.2223 | +0.316 | 0.7517 |  |
| Circulatory disease | +3.3001 | 2.0019 | ±4.0039 | +1.648 | 0.0993 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **218**, R² = **0.1370**, Adj R² = **0.0909**, F-statistic = **2.97** (p = **0.0011**), Residual SE = **7.119** on **206** df, AIC = **1486.1**, BIC = **1526.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.1103** | 5.4481 | ±10.8961 | **+10.299** | **7.11e-25** | *** |
| Education: graduate level (vs college) | +0.5598 | 1.0393 | ±2.0786 | +0.539 | 0.5901 |  |
| Education: high school or below (vs college) | +2.7290 | 2.8971 | ±5.7942 | +0.942 | 0.3462 |  |
| Site: UCSD (vs UAB) | -1.2335 | 1.6862 | ±3.3723 | -0.732 | 0.4645 |  |
| Site: UW (vs UAB) | -1.9368 | 1.2533 | ±2.5067 | -1.545 | 0.1223 |  |
| **Age (years)** | **-0.1213** | 0.0520 | ±0.1039 | **-2.334** | **0.0196** | * |
| BMI (kg/m2) | +0.1484 | 0.0868 | ±0.1735 | +1.710 | 0.0873 | . |
| Hypertension | -0.7393 | 1.0720 | ±2.1440 | -0.690 | 0.4904 |  |
| High cholesterol | +1.2927 | 1.0673 | ±2.1345 | +1.211 | 0.2258 |  |
| Kidney disease | +1.1081 | 3.0985 | ±6.1970 | +0.358 | 0.7206 |  |
| Circulatory disease | +2.7212 | 1.8350 | ±3.6700 | +1.483 | 0.1381 |  |
| **HbA1c (%)** | **+1.2917** | 0.6116 | ±1.2233 | **+2.112** | **0.0347** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **218**, R² = **0.1402**, Adj R² = **0.0943**, F-statistic = **3.05** (p = **8.25e-04**), Residual SE = **7.106** on **206** df, AIC = **1485.3**, BIC = **1525.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.8863** | 5.1683 | ±10.3367 | **+11.200** | **4.07e-29** | *** |
| Education: graduate level (vs college) | +0.3486 | 1.0417 | ±2.0835 | +0.335 | 0.7379 |  |
| Education: high school or below (vs college) | +2.7506 | 2.8928 | ±5.7856 | +0.951 | 0.3417 |  |
| Site: UCSD (vs UAB) | -1.1477 | 1.6789 | ±3.3577 | -0.684 | 0.4942 |  |
| Site: UW (vs UAB) | -1.9774 | 1.2525 | ±2.5049 | -1.579 | 0.1144 |  |
| **Age (years)** | **-0.1178** | 0.0519 | ±0.1037 | **-2.271** | **0.0231** | * |
| BMI (kg/m2) | +0.1366 | 0.0885 | ±0.1770 | +1.544 | 0.1226 |  |
| Hypertension | -0.8568 | 1.0712 | ±2.1424 | -0.800 | 0.4238 |  |
| High cholesterol | +1.3598 | 1.0526 | ±2.1051 | +1.292 | 0.1964 |  |
| Kidney disease | +0.7861 | 3.0393 | ±6.0786 | +0.259 | 0.7959 |  |
| Circulatory disease | +2.9276 | 1.8678 | ±3.7356 | +1.567 | 0.1170 |  |
| Mean glucose (mg/dL) | +0.0440 | 0.0228 | ±0.0457 | +1.928 | 0.0538 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **218**, R² = **0.1402**, Adj R² = **0.0943**, F-statistic = **3.05** (p = **8.25e-04**), Residual SE = **7.106** on **206** df, AIC = **1485.3**, BIC = **1525.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7937** | 7.1949 | ±14.3898 | **+7.199** | **6.08e-13** | *** |
| Education: graduate level (vs college) | +0.3486 | 1.0417 | ±2.0835 | +0.335 | 0.7379 |  |
| Education: high school or below (vs college) | +2.7506 | 2.8928 | ±5.7856 | +0.951 | 0.3417 |  |
| Site: UCSD (vs UAB) | -1.1477 | 1.6789 | ±3.3577 | -0.684 | 0.4942 |  |
| Site: UW (vs UAB) | -1.9774 | 1.2525 | ±2.5049 | -1.579 | 0.1144 |  |
| **Age (years)** | **-0.1178** | 0.0519 | ±0.1037 | **-2.271** | **0.0231** | * |
| BMI (kg/m2) | +0.1366 | 0.0885 | ±0.1770 | +1.544 | 0.1226 |  |
| Hypertension | -0.8568 | 1.0712 | ±2.1424 | -0.800 | 0.4238 |  |
| High cholesterol | +1.3598 | 1.0526 | ±2.1051 | +1.292 | 0.1964 |  |
| Kidney disease | +0.7861 | 3.0393 | ±6.0786 | +0.259 | 0.7959 |  |
| Circulatory disease | +2.9276 | 1.8678 | ±3.7356 | +1.567 | 0.1170 |  |
| GMI (%) | +1.8407 | 0.9545 | ±1.9091 | +1.928 | 0.0538 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **218**, R² = **0.1311**, Adj R² = **0.0847**, F-statistic = **2.82** (p = **0.0019**), Residual SE = **7.144** on **206** df, AIC = **1487.6**, BIC = **1528.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.5090** | 4.9429 | ±9.8857 | **+12.039** | **2.21e-33** | *** |
| Education: graduate level (vs college) | +0.4640 | 1.0467 | ±2.0934 | +0.443 | 0.6576 |  |
| Education: high school or below (vs college) | +2.9774 | 2.8777 | ±5.7554 | +1.035 | 0.3008 |  |
| Site: UCSD (vs UAB) | -1.2014 | 1.6751 | ±3.3503 | -0.717 | 0.4732 |  |
| Site: UW (vs UAB) | -1.8980 | 1.2642 | ±2.5284 | -1.501 | 0.1333 |  |
| **Age (years)** | **-0.1159** | 0.0520 | ±0.1041 | **-2.227** | **0.0259** | * |
| BMI (kg/m2) | +0.1368 | 0.0905 | ±0.1810 | +1.511 | 0.1308 |  |
| Hypertension | -0.8184 | 1.0870 | ±2.1739 | -0.753 | 0.4515 |  |
| High cholesterol | +1.3918 | 1.0585 | ±2.1170 | +1.315 | 0.1886 |  |
| Kidney disease | +1.1376 | 3.0536 | ±6.1071 | +0.373 | 0.7095 |  |
| Circulatory disease | +3.0155 | 1.8951 | ±3.7902 | +1.591 | 0.1116 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0316 | 0.0204 | ±0.0408 | +1.550 | 0.1211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1410**, Adj R² = **0.0951**, F-statistic = **3.07** (p = **7.69e-04**), Residual SE = **7.103** on **206** df, AIC = **1485.1**, BIC = **1525.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3556** | 4.9926 | ±9.9851 | **+11.688** | **1.46e-31** | *** |
| Education: graduate level (vs college) | +0.5546 | 1.0347 | ±2.0694 | +0.536 | 0.5920 |  |
| Education: high school or below (vs college) | +3.1660 | 2.8142 | ±5.6283 | +1.125 | 0.2606 |  |
| Site: UCSD (vs UAB) | -0.9215 | 1.6794 | ±3.3588 | -0.549 | 0.5832 |  |
| Site: UW (vs UAB) | -1.7565 | 1.2439 | ±2.4878 | -1.412 | 0.1579 |  |
| **Age (years)** | **-0.1236** | 0.0515 | ±0.1030 | **-2.401** | **0.0163** | * |
| BMI (kg/m2) | +0.1491 | 0.0884 | ±0.1768 | +1.686 | 0.0918 | . |
| Hypertension | -0.8696 | 1.0738 | ±2.1477 | -0.810 | 0.4180 |  |
| High cholesterol | +1.7516 | 1.0814 | ±2.1628 | +1.620 | 0.1053 |  |
| Kidney disease | -0.0185 | 3.1549 | ±6.3099 | -0.006 | 0.9953 |  |
| Circulatory disease | +2.9543 | 1.8958 | ±3.7917 | +1.558 | 0.1192 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1733** | 0.0880 | ±0.1759 | **+1.970** | **0.0488** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1349**, Adj R² = **0.0887**, F-statistic = **2.92** (p = **0.0013**), Residual SE = **7.128** on **206** df, AIC = **1486.6**, BIC = **1527.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4386** | 4.7638 | ±9.5276 | **+12.477** | **9.96e-36** | *** |
| Education: graduate level (vs college) | +0.5090 | 1.0402 | ±2.0803 | +0.489 | 0.6246 |  |
| Education: high school or below (vs college) | +3.2243 | 2.8322 | ±5.6645 | +1.138 | 0.2549 |  |
| Site: UCSD (vs UAB) | -0.9867 | 1.6728 | ±3.3455 | -0.590 | 0.5553 |  |
| Site: UW (vs UAB) | -1.7930 | 1.2521 | ±2.5042 | -1.432 | 0.1521 |  |
| **Age (years)** | **-0.1231** | 0.0515 | ±0.1030 | **-2.391** | **0.0168** | * |
| BMI (kg/m2) | +0.1449 | 0.0892 | ±0.1784 | +1.625 | 0.1043 |  |
| Hypertension | -0.9074 | 1.0885 | ±2.1770 | -0.834 | 0.4045 |  |
| High cholesterol | +1.7437 | 1.0795 | ±2.1591 | +1.615 | 0.1063 |  |
| Kidney disease | +0.2205 | 3.1140 | ±6.2281 | +0.071 | 0.9435 |  |
| Circulatory disease | +2.9411 | 1.9039 | ±3.8078 | +1.545 | 0.1224 |  |
| Avg. daily SD (mg/dL) | +0.1563 | 0.0870 | ±0.1740 | +1.796 | 0.0725 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **218**, R² = **0.1188**, Adj R² = **0.0717**, F-statistic = **2.52** (p = **0.0053**), Residual SE = **7.194** on **206** df, AIC = **1490.6**, BIC = **1531.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.6248** | 5.2198 | ±10.4395 | **+11.615** | **3.48e-31** | *** |
| Education: graduate level (vs college) | +0.6361 | 1.0522 | ±2.1044 | +0.605 | 0.5455 |  |
| Education: high school or below (vs college) | +3.4315 | 2.8855 | ±5.7710 | +1.189 | 0.2343 |  |
| Site: UCSD (vs UAB) | -0.9905 | 1.6747 | ±3.3495 | -0.591 | 0.5542 |  |
| Site: UW (vs UAB) | -1.7109 | 1.2872 | ±2.5743 | -1.329 | 0.1838 |  |
| **Age (years)** | **-0.1237** | 0.0523 | ±0.1046 | **-2.365** | **0.0180** | * |
| **BMI (kg/m2)** | **+0.1693** | 0.0857 | ±0.1714 | **+1.976** | **0.0482** | * |
| Hypertension | -0.7268 | 1.0980 | ±2.1960 | -0.662 | 0.5080 |  |
| High cholesterol | +1.7180 | 1.0788 | ±2.1576 | +1.593 | 0.1113 |  |
| Kidney disease | +0.6566 | 3.1953 | ±6.3907 | +0.206 | 0.8372 |  |
| Circulatory disease | +3.2800 | 2.0222 | ±4.0444 | +1.622 | 0.1048 |  |
| CV (%) | +0.1025 | 0.1095 | ±0.2191 | +0.936 | 0.3495 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **218**, R² = **0.1202**, Adj R² = **0.0732**, F-statistic = **2.56** (p = **0.0047**), Residual SE = **7.188** on **206** df, AIC = **1490.3**, BIC = **1530.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.7646** | 5.3144 | ±10.6288 | **+12.375** | **3.58e-35** | *** |
| Education: graduate level (vs college) | +0.5975 | 1.0502 | ±2.1003 | +0.569 | 0.5694 |  |
| Education: high school or below (vs college) | +3.3810 | 2.8828 | ±5.7656 | +1.173 | 0.2409 |  |
| Site: UCSD (vs UAB) | -1.0084 | 1.6653 | ±3.3307 | -0.606 | 0.5448 |  |
| Site: UW (vs UAB) | -1.7109 | 1.2810 | ±2.5621 | -1.336 | 0.1817 |  |
| **Age (years)** | **-0.1236** | 0.0521 | ±0.1042 | **-2.372** | **0.0177** | * |
| **BMI (kg/m2)** | **+0.1704** | 0.0858 | ±0.1716 | **+1.987** | **0.0469** | * |
| Hypertension | -0.7721 | 1.0944 | ±2.1889 | -0.705 | 0.4805 |  |
| High cholesterol | +1.7124 | 1.0704 | ±2.1408 | +1.600 | 0.1096 |  |
| Kidney disease | +0.6556 | 3.1887 | ±6.3775 | +0.206 | 0.8371 |  |
| Circulatory disease | +3.2757 | 2.0224 | ±4.0448 | +1.620 | 0.1053 |  |
| Mean / SD ratio | -0.6063 | 0.5683 | ±1.1366 | -1.067 | 0.2861 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **218**, R² = **0.1183**, Adj R² = **0.0712**, F-statistic = **2.51** (p = **0.0055**), Residual SE = **7.196** on **206** df, AIC = **1490.8**, BIC = **1531.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.1224** | 5.3587 | ±10.7174 | **+12.153** | **5.56e-34** | *** |
| Education: graduate level (vs college) | +0.5565 | 1.0481 | ±2.0963 | +0.531 | 0.5955 |  |
| Education: high school or below (vs college) | +3.3589 | 2.8853 | ±5.7707 | +1.164 | 0.2444 |  |
| Site: UCSD (vs UAB) | -1.0572 | 1.6638 | ±3.3276 | -0.635 | 0.5252 |  |
| Site: UW (vs UAB) | -1.7299 | 1.2789 | ±2.5578 | -1.353 | 0.1762 |  |
| **Age (years)** | **-0.1238** | 0.0524 | ±0.1049 | **-2.361** | **0.0182** | * |
| BMI (kg/m2) | +0.1670 | 0.0858 | ±0.1715 | +1.947 | 0.0516 | . |
| Hypertension | -0.7842 | 1.0974 | ±2.1948 | -0.715 | 0.4748 |  |
| High cholesterol | +1.6815 | 1.0739 | ±2.1478 | +1.566 | 0.1174 |  |
| Kidney disease | +0.7380 | 3.1430 | ±6.2859 | +0.235 | 0.8144 |  |
| Circulatory disease | +3.2759 | 2.0196 | ±4.0391 | +1.622 | 0.1048 |  |
| Avg. daily mean/SD | -0.3754 | 0.4261 | ±0.8523 | -0.881 | 0.3784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **218**, R² = **0.1182**, Adj R² = **0.0711**, F-statistic = **2.51** (p = **0.0055**), Residual SE = **7.196** on **206** df, AIC = **1490.8**, BIC = **1531.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5124** | 5.2733 | ±10.5466 | **+11.475** | **1.76e-30** | *** |
| Education: graduate level (vs college) | +0.6366 | 1.0404 | ±2.0808 | +0.612 | 0.5406 |  |
| Education: high school or below (vs college) | +3.3836 | 2.8710 | ±5.7421 | +1.179 | 0.2386 |  |
| Site: UCSD (vs UAB) | -0.9896 | 1.6913 | ±3.3825 | -0.585 | 0.5585 |  |
| Site: UW (vs UAB) | -1.6172 | 1.3304 | ±2.6609 | -1.216 | 0.2241 |  |
| **Age (years)** | **-0.1192** | 0.0522 | ±0.1044 | **-2.282** | **0.0225** | * |
| BMI (kg/m2) | +0.1574 | 0.0853 | ±0.1706 | +1.845 | 0.0651 | . |
| Hypertension | -0.6037 | 1.0939 | ±2.1878 | -0.552 | 0.5810 |  |
| High cholesterol | +1.6972 | 1.1157 | ±2.2313 | +1.521 | 0.1282 |  |
| Kidney disease | +0.9745 | 3.0741 | ±6.1481 | +0.317 | 0.7512 |  |
| Circulatory disease | +3.2816 | 1.9996 | ±3.9991 | +1.641 | 0.1008 |  |
| MAG (mg/dL/h) | +0.0527 | 0.0608 | ±0.1216 | +0.866 | 0.3863 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **218**, R² = **0.1271**, Adj R² = **0.0805**, F-statistic = **2.73** (p = **0.0026**), Residual SE = **7.160** on **206** df, AIC = **1488.6**, BIC = **1529.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8012** | 5.0668 | ±10.1335 | **+11.605** | **3.87e-31** | *** |
| Education: graduate level (vs college) | +0.5505 | 1.0440 | ±2.0881 | +0.527 | 0.5980 |  |
| Education: high school or below (vs college) | +3.2173 | 2.8377 | ±5.6754 | +1.134 | 0.2569 |  |
| Site: UCSD (vs UAB) | -0.9197 | 1.6768 | ±3.3535 | -0.549 | 0.5833 |  |
| Site: UW (vs UAB) | -1.6763 | 1.2685 | ±2.5370 | -1.321 | 0.1863 |  |
| **Age (years)** | **-0.1200** | 0.0518 | ±0.1037 | **-2.315** | **0.0206** | * |
| BMI (kg/m2) | +0.1557 | 0.0866 | ±0.1732 | +1.798 | 0.0721 | . |
| Hypertension | -0.7678 | 1.0881 | ±2.1763 | -0.706 | 0.4804 |  |
| High cholesterol | +1.8081 | 1.0922 | ±2.1844 | +1.655 | 0.0978 | . |
| Kidney disease | +0.6169 | 3.1068 | ±6.2135 | +0.199 | 0.8426 |  |
| Circulatory disease | +3.0856 | 1.9577 | ±3.9155 | +1.576 | 0.1150 |  |
| Avg. daily range (mg/dL) | +0.0318 | 0.0206 | ±0.0412 | +1.545 | 0.1224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **218**, R² = **0.1486**, Adj R² = **0.1032**, F-statistic = **3.27** (p = **3.81e-04**), Residual SE = **7.071** on **206** df, AIC = **1483.1**, BIC = **1523.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.6646** | 4.7794 | ±9.5588 | **+12.693** | **6.47e-37** | *** |
| Education: graduate level (vs college) | +0.7069 | 1.0378 | ±2.0756 | +0.681 | 0.4958 |  |
| Education: high school or below (vs college) | +3.2322 | 2.8152 | ±5.6303 | +1.148 | 0.2509 |  |
| Site: UCSD (vs UAB) | -0.9714 | 1.6646 | ±3.3292 | -0.584 | 0.5595 |  |
| Site: UW (vs UAB) | -1.8533 | 1.2372 | ±2.4745 | -1.498 | 0.1342 |  |
| **Age (years)** | **-0.1254** | 0.0527 | ±0.1054 | **-2.379** | **0.0173** | * |
| BMI (kg/m2) | +0.1565 | 0.0876 | ±0.1752 | +1.787 | 0.0740 | . |
| Hypertension | -0.6277 | 1.0675 | ±2.1349 | -0.588 | 0.5565 |  |
| High cholesterol | +1.4294 | 1.0655 | ±2.1311 | +1.341 | 0.1798 |  |
| Kidney disease | +0.5964 | 3.1331 | ±6.2661 | +0.190 | 0.8490 |  |
| Circulatory disease | +3.3533 | 1.9167 | ±3.8334 | +1.750 | 0.0802 | . |
| **SD of daily means (mg/dL)** | **+0.3290** | 0.1295 | ±0.2590 | **+2.541** | **0.0111** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **218**, R² = **0.1368**, Adj R² = **0.0907**, F-statistic = **2.97** (p = **0.0011**), Residual SE = **7.120** on **206** df, AIC = **1486.1**, BIC = **1526.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.2373** | 7.0373 | ±14.0746 | **+9.981** | **1.85e-23** | *** |
| Education: graduate level (vs college) | +0.4691 | 1.0404 | ±2.0809 | +0.451 | 0.6521 |  |
| Education: high school or below (vs college) | +2.9684 | 2.8779 | ±5.7557 | +1.031 | 0.3023 |  |
| Site: UCSD (vs UAB) | -1.0543 | 1.6839 | ±3.3677 | -0.626 | 0.5312 |  |
| Site: UW (vs UAB) | -1.8288 | 1.2547 | ±2.5094 | -1.458 | 0.1450 |  |
| **Age (years)** | **-0.1164** | 0.0519 | ±0.1038 | **-2.243** | **0.0249** | * |
| BMI (kg/m2) | +0.1321 | 0.0927 | ±0.1854 | +1.425 | 0.1541 |  |
| Hypertension | -0.8068 | 1.0755 | ±2.1510 | -0.750 | 0.4531 |  |
| High cholesterol | +1.4251 | 1.0661 | ±2.1322 | +1.337 | 0.1813 |  |
| Kidney disease | +0.5399 | 3.1071 | ±6.2142 | +0.174 | 0.8621 |  |
| Circulatory disease | +3.0584 | 1.8945 | ±3.7890 | +1.614 | 0.1064 |  |
| Time in range 70-180, pooled (%) | -0.0736 | 0.0475 | ±0.0950 | -1.549 | 0.1215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **218**, R² = **0.1354**, Adj R² = **0.0892**, F-statistic = **2.93** (p = **0.0013**), Residual SE = **7.126** on **206** df, AIC = **1486.5**, BIC = **1527.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.9995** | 7.0669 | ±14.1338 | **+9.905** | **3.95e-23** | *** |
| Education: graduate level (vs college) | +0.4598 | 1.0428 | ±2.0857 | +0.441 | 0.6592 |  |
| Education: high school or below (vs college) | +3.0105 | 2.8739 | ±5.7478 | +1.048 | 0.2949 |  |
| Site: UCSD (vs UAB) | -1.0379 | 1.6843 | ±3.3686 | -0.616 | 0.5378 |  |
| Site: UW (vs UAB) | -1.8191 | 1.2562 | ±2.5124 | -1.448 | 0.1476 |  |
| **Age (years)** | **-0.1170** | 0.0520 | ±0.1041 | **-2.248** | **0.0246** | * |
| BMI (kg/m2) | +0.1326 | 0.0929 | ±0.1858 | +1.427 | 0.1535 |  |
| Hypertension | -0.8095 | 1.0773 | ±2.1547 | -0.751 | 0.4524 |  |
| High cholesterol | +1.4242 | 1.0669 | ±2.1338 | +1.335 | 0.1819 |  |
| Kidney disease | +0.5504 | 3.1090 | ±6.2179 | +0.177 | 0.8595 |  |
| Circulatory disease | +3.0783 | 1.8997 | ±3.7994 | +1.620 | 0.1051 |  |
| Avg. daily time in range 70-180 (%) | -0.0704 | 0.0472 | ±0.0943 | -1.494 | 0.1353 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.1150**, Adj R² = **0.0678**, F-statistic = **2.43** (p = **0.0072**), Residual SE = **7.209** on **206** df, AIC = **1491.6**, BIC = **1532.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0392** | 4.6012 | ±9.2025 | **+13.701** | **1.01e-42** | *** |
| Education: graduate level (vs college) | +0.5239 | 1.0633 | ±2.1265 | +0.493 | 0.6222 |  |
| Education: high school or below (vs college) | +3.2836 | 2.9582 | ±5.9165 | +1.110 | 0.2670 |  |
| Site: UCSD (vs UAB) | -1.1211 | 1.6820 | ±3.3639 | -0.667 | 0.5051 |  |
| Site: UW (vs UAB) | -1.8462 | 1.2891 | ±2.5782 | -1.432 | 0.1521 |  |
| **Age (years)** | **-0.1207** | 0.0528 | ±0.1057 | **-2.285** | **0.0223** | * |
| BMI (kg/m2) | +0.1677 | 0.0864 | ±0.1729 | +1.940 | 0.0524 | . |
| Hypertension | -0.7323 | 1.1027 | ±2.2053 | -0.664 | 0.5066 |  |
| High cholesterol | +1.5152 | 1.0879 | ±2.1758 | +1.393 | 0.1637 |  |
| Kidney disease | +0.9899 | 3.1183 | ±6.2366 | +0.317 | 0.7509 |  |
| Circulatory disease | +3.3190 | 2.0234 | ±4.0468 | +1.640 | 0.1009 |  |
| Any reading < 54 during wear (0/1) | -0.2112 | 1.2974 | ±2.5949 | -0.163 | 0.8707 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.1183**, Adj R² = **0.0712**, F-statistic = **2.51** (p = **0.0055**), Residual SE = **7.196** on **206** df, AIC = **1490.8**, BIC = **1531.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7225** | 4.6145 | ±9.2290 | **+13.592** | **4.44e-42** | *** |
| Education: graduate level (vs college) | +0.6395 | 1.0524 | ±2.1047 | +0.608 | 0.5434 |  |
| Education: high school or below (vs college) | +3.4301 | 2.9112 | ±5.8223 | +1.178 | 0.2387 |  |
| Site: UCSD (vs UAB) | -0.9930 | 1.6845 | ±3.3691 | -0.590 | 0.5555 |  |
| Site: UW (vs UAB) | -1.6677 | 1.3047 | ±2.6094 | -1.278 | 0.2012 |  |
| **Age (years)** | **-0.1243** | 0.0526 | ±0.1052 | **-2.364** | **0.0181** | * |
| **BMI (kg/m2)** | **+0.1725** | 0.0872 | ±0.1743 | **+1.979** | **0.0478** | * |
| Hypertension | -0.6768 | 1.1005 | ±2.2010 | -0.615 | 0.5386 |  |
| High cholesterol | +1.6304 | 1.0880 | ±2.1759 | +1.499 | 0.1340 |  |
| Kidney disease | +1.0058 | 3.1143 | ±6.2286 | +0.323 | 0.7467 |  |
| Circulatory disease | +3.3175 | 2.0090 | ±4.0180 | +1.651 | 0.0987 | . |
| Time < 54 (%) | +0.4482 | 1.9574 | ±3.9148 | +0.229 | 0.8189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.1179**, Adj R² = **0.0708**, F-statistic = **2.50** (p = **0.0057**), Residual SE = **7.197** on **206** df, AIC = **1490.9**, BIC = **1531.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7694** | 4.6114 | ±9.2227 | **+13.612** | **3.40e-42** | *** |
| Education: graduate level (vs college) | +0.6283 | 1.0500 | ±2.0999 | +0.598 | 0.5495 |  |
| Education: high school or below (vs college) | +3.4271 | 2.9020 | ±5.8040 | +1.181 | 0.2376 |  |
| Site: UCSD (vs UAB) | -0.9951 | 1.6848 | ±3.3695 | -0.591 | 0.5548 |  |
| Site: UW (vs UAB) | -1.6549 | 1.3105 | ±2.6210 | -1.263 | 0.2067 |  |
| **Age (years)** | **-0.1241** | 0.0526 | ±0.1053 | **-2.358** | **0.0184** | * |
| **BMI (kg/m2)** | **+0.1705** | 0.0862 | ±0.1723 | **+1.979** | **0.0478** | * |
| Hypertension | -0.6774 | 1.0999 | ±2.1999 | -0.616 | 0.5380 |  |
| High cholesterol | +1.6466 | 1.0898 | ±2.1796 | +1.511 | 0.1308 |  |
| Kidney disease | +1.0004 | 3.1124 | ±6.2247 | +0.321 | 0.7479 |  |
| Circulatory disease | +3.3147 | 2.0100 | ±4.0200 | +1.649 | 0.0991 | . |
| Avg. daily time < 54 (%) | +0.5580 | 1.0366 | ±2.0733 | +0.538 | 0.5904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.1210**, Adj R² = **0.0741**, F-statistic = **2.58** (p = **0.0044**), Residual SE = **7.185** on **206** df, AIC = **1490.1**, BIC = **1530.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7812** | 4.5868 | ±9.1736 | **+13.687** | **1.21e-42** | *** |
| Education: graduate level (vs college) | +0.7042 | 1.0483 | ±2.0967 | +0.672 | 0.5018 |  |
| Education: high school or below (vs college) | +3.5181 | 2.8936 | ±5.7872 | +1.216 | 0.2241 |  |
| Site: UCSD (vs UAB) | -0.9788 | 1.6718 | ±3.3435 | -0.586 | 0.5582 |  |
| Site: UW (vs UAB) | -1.6175 | 1.3094 | ±2.6187 | -1.235 | 0.2167 |  |
| **Age (years)** | **-0.1227** | 0.0524 | ±0.1047 | **-2.343** | **0.0191** | * |
| BMI (kg/m2) | +0.1590 | 0.0848 | ±0.1696 | +1.874 | 0.0609 | . |
| Hypertension | -0.6630 | 1.1038 | ±2.2076 | -0.601 | 0.5481 |  |
| High cholesterol | +1.7208 | 1.0869 | ±2.1739 | +1.583 | 0.1134 |  |
| Kidney disease | +0.9756 | 3.1517 | ±6.3034 | +0.310 | 0.7569 |  |
| Circulatory disease | +3.3053 | 2.0241 | ±4.0482 | +1.633 | 0.1025 |  |
| Time 54-69, pooled (%) | +0.4543 | 0.3853 | ±0.7705 | +1.179 | 0.2384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **218**, R² = **0.1211**, Adj R² = **0.0742**, F-statistic = **2.58** (p = **0.0043**), Residual SE = **7.184** on **206** df, AIC = **1490.1**, BIC = **1530.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7856** | 4.5857 | ±9.1714 | **+13.692** | **1.14e-42** | *** |
| Education: graduate level (vs college) | +0.7098 | 1.0483 | ±2.0966 | +0.677 | 0.4983 |  |
| Education: high school or below (vs college) | +3.5413 | 2.8932 | ±5.7863 | +1.224 | 0.2209 |  |
| Site: UCSD (vs UAB) | -0.9711 | 1.6733 | ±3.3467 | -0.580 | 0.5617 |  |
| Site: UW (vs UAB) | -1.5932 | 1.3111 | ±2.6221 | -1.215 | 0.2243 |  |
| **Age (years)** | **-0.1233** | 0.0525 | ±0.1051 | **-2.348** | **0.0189** | * |
| BMI (kg/m2) | +0.1601 | 0.0847 | ±0.1694 | +1.890 | 0.0587 | . |
| Hypertension | -0.6580 | 1.1033 | ±2.2067 | -0.596 | 0.5510 |  |
| High cholesterol | +1.7345 | 1.0914 | ±2.1828 | +1.589 | 0.1120 |  |
| Kidney disease | +0.9767 | 3.1407 | ±6.2814 | +0.311 | 0.7558 |  |
| Circulatory disease | +3.3197 | 2.0184 | ±4.0368 | +1.645 | 0.1000 |  |
| Avg. daily time 54-69 (%) | +0.4382 | 0.3516 | ±0.7031 | +1.246 | 0.2126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **218**, R² = **0.1216**, Adj R² = **0.0747**, F-statistic = **2.59** (p = **0.0042**), Residual SE = **7.182** on **206** df, AIC = **1489.9**, BIC = **1530.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6505** | 4.5953 | ±9.1906 | **+13.634** | **2.53e-42** | *** |
| Education: graduate level (vs college) | +0.7248 | 1.0502 | ±2.1004 | +0.690 | 0.4901 |  |
| Education: high school or below (vs college) | +3.5414 | 2.9020 | ±5.8040 | +1.220 | 0.2223 |  |
| Site: UCSD (vs UAB) | -0.9362 | 1.6803 | ±3.3607 | -0.557 | 0.5774 |  |
| Site: UW (vs UAB) | -1.5679 | 1.3184 | ±2.6369 | -1.189 | 0.2344 |  |
| **Age (years)** | **-0.1245** | 0.0525 | ±0.1051 | **-2.371** | **0.0177** | * |
| BMI (kg/m2) | +0.1655 | 0.0850 | ±0.1700 | +1.948 | 0.0514 | . |
| Hypertension | -0.6458 | 1.1042 | ±2.2084 | -0.585 | 0.5587 |  |
| High cholesterol | +1.7326 | 1.0906 | ±2.1813 | +1.589 | 0.1122 |  |
| Kidney disease | +0.9934 | 3.1403 | ±6.2806 | +0.316 | 0.7517 |  |
| Circulatory disease | +3.3161 | 2.0218 | ±4.0435 | +1.640 | 0.1010 |  |
| Time < 70 (%) | +0.3179 | 0.2135 | ±0.4269 | +1.489 | 0.1364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **218**, R² = **0.1211**, Adj R² = **0.0741**, F-statistic = **2.58** (p = **0.0044**), Residual SE = **7.185** on **206** df, AIC = **1490.1**, BIC = **1530.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7171** | 4.5932 | ±9.1864 | **+13.654** | **1.90e-42** | *** |
| Education: graduate level (vs college) | +0.7109 | 1.0493 | ±2.0986 | +0.677 | 0.4981 |  |
| Education: high school or below (vs college) | +3.5418 | 2.8987 | ±5.7973 | +1.222 | 0.2218 |  |
| Site: UCSD (vs UAB) | -0.9466 | 1.6802 | ±3.3603 | -0.563 | 0.5732 |  |
| Site: UW (vs UAB) | -1.5632 | 1.3197 | ±2.6395 | -1.184 | 0.2362 |  |
| **Age (years)** | **-0.1244** | 0.0527 | ±0.1054 | **-2.362** | **0.0182** | * |
| BMI (kg/m2) | +0.1642 | 0.0847 | ±0.1695 | +1.938 | 0.0527 | . |
| Hypertension | -0.6491 | 1.1038 | ±2.2075 | -0.588 | 0.5565 |  |
| High cholesterol | +1.7405 | 1.0959 | ±2.1918 | +1.588 | 0.1122 |  |
| Kidney disease | +0.9879 | 3.1321 | ±6.2642 | +0.315 | 0.7524 |  |
| Circulatory disease | +3.3224 | 2.0179 | ±4.0358 | +1.646 | 0.0997 | . |
| Avg. daily time < 70 (%) | +0.3137 | 0.2194 | ±0.4387 | +1.430 | 0.1527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.1293**, Adj R² = **0.0828**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **7.151** on **206** df, AIC = **1488.0**, BIC = **1528.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.8508** | 8.3128 | ±16.6257 | **+8.643** | **5.46e-18** | *** |
| Education: graduate level (vs college) | +0.5888 | 1.0489 | ±2.0978 | +0.561 | 0.5746 |  |
| Education: high school or below (vs college) | +2.9552 | 2.8879 | ±5.7758 | +1.023 | 0.3062 |  |
| Site: UCSD (vs UAB) | -1.0819 | 1.6832 | ±3.3664 | -0.643 | 0.5204 |  |
| Site: UW (vs UAB) | -1.7871 | 1.2731 | ±2.5462 | -1.404 | 0.1604 |  |
| **Age (years)** | **-0.1167** | 0.0524 | ±0.1049 | **-2.226** | **0.0260** | * |
| BMI (kg/m2) | +0.1581 | 0.0862 | ±0.1725 | +1.833 | 0.0668 | . |
| Hypertension | -0.6185 | 1.0926 | ±2.1853 | -0.566 | 0.5714 |  |
| High cholesterol | +1.5487 | 1.0696 | ±2.1391 | +1.448 | 0.1476 |  |
| Kidney disease | +0.9417 | 3.1267 | ±6.2535 | +0.301 | 0.7633 |  |
| Circulatory disease | +2.9980 | 1.9039 | ±3.8079 | +1.575 | 0.1153 |  |
| Time 54-250, pooled (%) | -0.0915 | 0.0701 | ±0.1402 | -1.305 | 0.1918 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.1292**, Adj R² = **0.0827**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **7.151** on **206** df, AIC = **1488.0**, BIC = **1528.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.2268** | 8.6987 | ±17.3974 | **+8.303** | **1.01e-16** | *** |
| Education: graduate level (vs college) | +0.5823 | 1.0499 | ±2.0997 | +0.555 | 0.5791 |  |
| Education: high school or below (vs college) | +2.9568 | 2.8878 | ±5.7756 | +1.024 | 0.3059 |  |
| Site: UCSD (vs UAB) | -1.0865 | 1.6831 | ±3.3662 | -0.646 | 0.5186 |  |
| Site: UW (vs UAB) | -1.8012 | 1.2724 | ±2.5448 | -1.416 | 0.1569 |  |
| **Age (years)** | **-0.1167** | 0.0525 | ±0.1050 | **-2.223** | **0.0262** | * |
| BMI (kg/m2) | +0.1563 | 0.0864 | ±0.1728 | +1.809 | 0.0704 | . |
| Hypertension | -0.6181 | 1.0935 | ±2.1870 | -0.565 | 0.5719 |  |
| High cholesterol | +1.5470 | 1.0704 | ±2.1408 | +1.445 | 0.1484 |  |
| Kidney disease | +0.9462 | 3.1267 | ±6.2534 | +0.303 | 0.7622 |  |
| Circulatory disease | +2.9971 | 1.9031 | ±3.8061 | +1.575 | 0.1153 |  |
| Avg. daily time 54-250 (%) | -0.0947 | 0.0742 | ±0.1483 | -1.276 | 0.2019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.1257**, Adj R² = **0.0790**, F-statistic = **2.69** (p = **0.0029**), Residual SE = **7.166** on **206** df, AIC = **1488.9**, BIC = **1529.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1850** | 4.6395 | ±9.2790 | **+13.619** | **3.09e-42** | *** |
| Education: graduate level (vs college) | +0.3823 | 1.0505 | ±2.1009 | +0.364 | 0.7159 |  |
| Education: high school or below (vs college) | +3.2036 | 2.9158 | ±5.8316 | +1.099 | 0.2719 |  |
| Site: UCSD (vs UAB) | -1.0939 | 1.6793 | ±3.3587 | -0.651 | 0.5148 |  |
| Site: UW (vs UAB) | -1.9048 | 1.2636 | ±2.5273 | -1.507 | 0.1317 |  |
| **Age (years)** | **-0.1193** | 0.0519 | ±0.1038 | **-2.299** | **0.0215** | * |
| BMI (kg/m2) | +0.1356 | 0.0968 | ±0.1936 | +1.401 | 0.1613 |  |
| Hypertension | -0.9356 | 1.0963 | ±2.1925 | -0.853 | 0.3934 |  |
| High cholesterol | +1.3593 | 1.0529 | ±2.1059 | +1.291 | 0.1967 |  |
| Kidney disease | +0.5082 | 3.0980 | ±6.1959 | +0.164 | 0.8697 |  |
| Circulatory disease | +3.3003 | 1.9790 | ±3.9580 | +1.668 | 0.0954 | . |
| Time 181-250, pooled (%) | +0.0857 | 0.0745 | ±0.1490 | +1.150 | 0.2502 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **218**, R² = **0.1248**, Adj R² = **0.0781**, F-statistic = **2.67** (p = **0.0032**), Residual SE = **7.169** on **206** df, AIC = **1489.1**, BIC = **1529.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1907** | 4.6475 | ±9.2950 | **+13.597** | **4.19e-42** | *** |
| Education: graduate level (vs college) | +0.3837 | 1.0533 | ±2.1067 | +0.364 | 0.7157 |  |
| Education: high school or below (vs college) | +3.2248 | 2.9091 | ±5.8182 | +1.109 | 0.2676 |  |
| Site: UCSD (vs UAB) | -1.0712 | 1.6820 | ±3.3640 | -0.637 | 0.5242 |  |
| Site: UW (vs UAB) | -1.8814 | 1.2637 | ±2.5274 | -1.489 | 0.1365 |  |
| **Age (years)** | **-0.1196** | 0.0520 | ±0.1040 | **-2.300** | **0.0215** | * |
| BMI (kg/m2) | +0.1376 | 0.0965 | ±0.1930 | +1.426 | 0.1538 |  |
| Hypertension | -0.9271 | 1.0991 | ±2.1981 | -0.844 | 0.3989 |  |
| High cholesterol | +1.3629 | 1.0531 | ±2.1062 | +1.294 | 0.1956 |  |
| Kidney disease | +0.5254 | 3.1023 | ±6.2046 | +0.169 | 0.8655 |  |
| Circulatory disease | +3.3006 | 1.9797 | ±3.9595 | +1.667 | 0.0955 | . |
| Avg. daily time 181-250 (%) | +0.0799 | 0.0727 | ±0.1455 | +1.099 | 0.2719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **218**, R² = **0.1336**, Adj R² = **0.0873**, F-statistic = **2.89** (p = **0.0015**), Residual SE = **7.133** on **206** df, AIC = **1487.0**, BIC = **1527.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9655** | 4.6343 | ±9.2686 | **+13.587** | **4.80e-42** | *** |
| Education: graduate level (vs college) | +0.4360 | 1.0454 | ±2.0908 | +0.417 | 0.6766 |  |
| Education: high school or below (vs college) | +2.9464 | 2.8904 | ±5.7808 | +1.019 | 0.3080 |  |
| Site: UCSD (vs UAB) | -1.0951 | 1.6821 | ±3.3642 | -0.651 | 0.5150 |  |
| Site: UW (vs UAB) | -1.8834 | 1.2573 | ±2.5146 | -1.498 | 0.1341 |  |
| **Age (years)** | **-0.1160** | 0.0519 | ±0.1039 | **-2.233** | **0.0255** | * |
| BMI (kg/m2) | +0.1351 | 0.0928 | ±0.1855 | +1.456 | 0.1454 |  |
| Hypertension | -0.8183 | 1.0801 | ±2.1603 | -0.758 | 0.4487 |  |
| High cholesterol | +1.3920 | 1.0657 | ±2.1314 | +1.306 | 0.1915 |  |
| Kidney disease | +0.5740 | 3.1045 | ±6.2090 | +0.185 | 0.8533 |  |
| Circulatory disease | +3.0746 | 1.8994 | ±3.7988 | +1.619 | 0.1055 |  |
| Time > 180 (%) | +0.0676 | 0.0473 | ±0.0945 | +1.430 | 0.1527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **218**, R² = **0.1325**, Adj R² = **0.0862**, F-statistic = **2.86** (p = **0.0016**), Residual SE = **7.138** on **206** df, AIC = **1487.2**, BIC = **1527.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0184** | 4.6421 | ±9.2843 | **+13.575** | **5.61e-42** | *** |
| Education: graduate level (vs college) | +0.4310 | 1.0474 | ±2.0948 | +0.411 | 0.6807 |  |
| Education: high school or below (vs college) | +2.9849 | 2.8874 | ±5.7749 | +1.034 | 0.3012 |  |
| Site: UCSD (vs UAB) | -1.0766 | 1.6829 | ±3.3658 | -0.640 | 0.5223 |  |
| Site: UW (vs UAB) | -1.8741 | 1.2586 | ±2.5172 | -1.489 | 0.1365 |  |
| **Age (years)** | **-0.1166** | 0.0520 | ±0.1041 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | +0.1356 | 0.0929 | ±0.1857 | +1.460 | 0.1443 |  |
| Hypertension | -0.8199 | 1.0820 | ±2.1640 | -0.758 | 0.4486 |  |
| High cholesterol | +1.3901 | 1.0663 | ±2.1325 | +1.304 | 0.1923 |  |
| Kidney disease | +0.5829 | 3.1075 | ±6.2150 | +0.188 | 0.8512 |  |
| Circulatory disease | +3.0906 | 1.9048 | ±3.8097 | +1.623 | 0.1047 |  |
| Avg. daily time > 180 (%) | +0.0650 | 0.0469 | ±0.0938 | +1.386 | 0.1656 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **218**, R² = **0.1163**, Adj R² = **0.0691**, F-statistic = **2.46** (p = **0.0065**), Residual SE = **7.204** on **206** df, AIC = **1491.3**, BIC = **1531.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0573** | 4.6738 | ±9.3477 | **+13.492** | **1.75e-41** | *** |
| Education: graduate level (vs college) | +0.5556 | 1.0532 | ±2.1064 | +0.528 | 0.5978 |  |
| Education: high school or below (vs college) | +3.2982 | 2.9040 | ±5.8080 | +1.136 | 0.2561 |  |
| Site: UCSD (vs UAB) | -1.1071 | 1.6807 | ±3.3614 | -0.659 | 0.5101 |  |
| Site: UW (vs UAB) | -1.8247 | 1.2817 | ±2.5633 | -1.424 | 0.1545 |  |
| **Age (years)** | **-0.1188** | 0.0522 | ±0.1045 | **-2.273** | **0.0230** | * |
| BMI (kg/m2) | +0.1555 | 0.0957 | ±0.1914 | +1.625 | 0.1041 |  |
| Hypertension | -0.7286 | 1.1033 | ±2.2067 | -0.660 | 0.5090 |  |
| High cholesterol | +1.4779 | 1.0767 | ±2.1534 | +1.373 | 0.1699 |  |
| Kidney disease | +1.0060 | 3.1309 | ±6.2617 | +0.321 | 0.7480 |  |
| Circulatory disease | +3.2490 | 1.9999 | ±3.9998 | +1.625 | 0.1042 |  |
| Nocturnal time > 180 (%) | +0.0178 | 0.0471 | ±0.0943 | +0.378 | 0.7052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.1280**, Adj R² = **0.0815**, F-statistic = **2.75** (p = **0.0024**), Residual SE = **7.156** on **206** df, AIC = **1488.3**, BIC = **1529.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7647** | 4.6464 | ±9.2929 | **+13.508** | **1.40e-41** | *** |
| Education: graduate level (vs college) | +0.5677 | 1.0501 | ±2.1003 | +0.541 | 0.5888 |  |
| Education: high school or below (vs college) | +2.9457 | 2.8988 | ±5.7975 | +1.016 | 0.3095 |  |
| Site: UCSD (vs UAB) | -1.1054 | 1.6819 | ±3.3638 | -0.657 | 0.5110 |  |
| Site: UW (vs UAB) | -1.8197 | 1.2720 | ±2.5440 | -1.431 | 0.1526 |  |
| **Age (years)** | **-0.1162** | 0.0525 | ±0.1050 | **-2.215** | **0.0268** | * |
| BMI (kg/m2) | +0.1572 | 0.0864 | ±0.1727 | +1.820 | 0.0687 | . |
| Hypertension | -0.6332 | 1.0916 | ±2.1832 | -0.580 | 0.5619 |  |
| High cholesterol | +1.5296 | 1.0709 | ±2.1419 | +1.428 | 0.1532 |  |
| Kidney disease | +0.9392 | 3.1268 | ±6.2536 | +0.300 | 0.7639 |  |
| Circulatory disease | +3.0068 | 1.9069 | ±3.8137 | +1.577 | 0.1148 |  |
| Time > 250 (%) | +0.0878 | 0.0722 | ±0.1443 | +1.217 | 0.2235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 218)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **218**, R² = **0.1283**, Adj R² = **0.0817**, F-statistic = **2.76** (p = **0.0024**), Residual SE = **7.155** on **206** df, AIC = **1488.3**, BIC = **1528.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8064** | 4.6492 | ±9.2985 | **+13.509** | **1.39e-41** | *** |
| Education: graduate level (vs college) | +0.5668 | 1.0507 | ±2.1014 | +0.539 | 0.5896 |  |
| Education: high school or below (vs college) | +2.9483 | 2.8968 | ±5.7935 | +1.018 | 0.3088 |  |
| Site: UCSD (vs UAB) | -1.1056 | 1.6822 | ±3.3645 | -0.657 | 0.5110 |  |
| Site: UW (vs UAB) | -1.8301 | 1.2717 | ±2.5433 | -1.439 | 0.1501 |  |
| **Age (years)** | **-0.1163** | 0.0525 | ±0.1050 | **-2.215** | **0.0268** | * |
| BMI (kg/m2) | +0.1559 | 0.0865 | ±0.1730 | +1.803 | 0.0714 | . |
| Hypertension | -0.6300 | 1.0927 | ±2.1855 | -0.577 | 0.5642 |  |
| High cholesterol | +1.5284 | 1.0717 | ±2.1433 | +1.426 | 0.1538 |  |
| Kidney disease | +0.9447 | 3.1270 | ±6.2540 | +0.302 | 0.7626 |  |
| Circulatory disease | +3.0041 | 1.9052 | ±3.8105 | +1.577 | 0.1148 |  |
| Avg. daily time > 250 (%) | +0.0917 | 0.0756 | ±0.1513 | +1.212 | 0.2254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 215; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **215**, R² = **0.0664**, Adj R² = **0.0207**, F-statistic = **1.45** (p = **0.1600**), Residual SE = **64.511** on **204** df, AIC = **2412.6**, BIC = **2449.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.4821** | 45.4871 | ±90.9742 | **+9.332** | **1.04e-20** | *** |
| Education: graduate level (vs college) | -3.5144 | 9.4815 | ±18.9630 | -0.371 | 0.7109 |  |
| Education: high school or below (vs college) | -9.6845 | 22.7661 | ±45.5323 | -0.425 | 0.6706 |  |
| **Site: UCSD (vs UAB)** | **-27.1882** | 13.2873 | ±26.5746 | **-2.046** | **0.0407** | * |
| Site: UW (vs UAB) | -13.7767 | 12.4035 | ±24.8069 | -1.111 | 0.2667 |  |
| Age (years) | -0.6207 | 0.5123 | ±1.0247 | -1.212 | 0.2257 |  |
| BMI (kg/m2) | -0.2173 | 0.7564 | ±1.5128 | -0.287 | 0.7739 |  |
| Hypertension | +4.8078 | 9.6437 | ±19.2874 | +0.499 | 0.6181 |  |
| High cholesterol | -3.7261 | 9.0763 | ±18.1526 | -0.411 | 0.6814 |  |
| Kidney disease | -38.7157 | 27.5954 | ±55.1908 | -1.403 | 0.1606 |  |
| **Circulatory disease** | **+40.5777** | 19.5979 | ±39.1958 | **+2.071** | **0.0384** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **215**, R² = **0.0761**, Adj R² = **0.0261**, F-statistic = **1.52** (p = **0.1260**), Residual SE = **64.332** on **203** df, AIC = **2412.3**, BIC = **2452.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+466.1038** | 51.5998 | ±103.1996 | **+9.033** | **1.67e-19** | *** |
| Education: graduate level (vs college) | -3.9164 | 9.4685 | ±18.9371 | -0.414 | 0.6791 |  |
| Education: high school or below (vs college) | -5.6509 | 23.1343 | ±46.2686 | -0.244 | 0.8070 |  |
| **Site: UCSD (vs UAB)** | **-27.0957** | 13.2425 | ±26.4850 | **-2.046** | **0.0407** | * |
| Site: UW (vs UAB) | -13.1489 | 12.3589 | ±24.7178 | -1.064 | 0.2874 |  |
| Age (years) | -0.6060 | 0.5114 | ±1.0229 | -1.185 | 0.2360 |  |
| BMI (kg/m2) | -0.1408 | 0.7577 | ±1.5155 | -0.186 | 0.8526 |  |
| Hypertension | +4.3005 | 9.6083 | ±19.2167 | +0.448 | 0.6545 |  |
| High cholesterol | -1.8815 | 9.1096 | ±18.2192 | -0.207 | 0.8364 |  |
| Kidney disease | -38.9493 | 27.6175 | ±55.2350 | -1.410 | 0.1584 |  |
| **Circulatory disease** | **+44.1196** | 20.2419 | ±40.4837 | **+2.180** | **0.0293** | * |
| HbA1c (%) | -7.7523 | 4.3045 | ±8.6090 | -1.801 | 0.0717 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **215**, R² = **0.0679**, Adj R² = **0.0174**, F-statistic = **1.34** (p = **0.2024**), Residual SE = **64.619** on **203** df, AIC = **2414.3**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+436.1572** | 49.9086 | ±99.8172 | **+8.739** | **2.35e-18** | *** |
| Education: graduate level (vs college) | -3.1836 | 9.5223 | ±19.0446 | -0.334 | 0.7381 |  |
| Education: high school or below (vs college) | -8.1689 | 23.3361 | ±46.6722 | -0.350 | 0.7263 |  |
| **Site: UCSD (vs UAB)** | **-27.4089** | 13.3683 | ±26.7366 | **-2.050** | **0.0403** | * |
| Site: UW (vs UAB) | -13.5274 | 12.4483 | ±24.8966 | -1.087 | 0.2772 |  |
| Age (years) | -0.6226 | 0.5170 | ±1.0340 | -1.204 | 0.2285 |  |
| BMI (kg/m2) | -0.1672 | 0.7834 | ±1.5668 | -0.213 | 0.8309 |  |
| Hypertension | +4.8119 | 9.6751 | ±19.3501 | +0.497 | 0.6189 |  |
| High cholesterol | -3.1406 | 9.0300 | ±18.0600 | -0.348 | 0.7280 |  |
| Kidney disease | -38.0855 | 27.7796 | ±55.5592 | -1.371 | 0.1704 |  |
| **Circulatory disease** | **+41.5440** | 19.9834 | ±39.9667 | **+2.079** | **0.0376** | * |
| Mean glucose (mg/dL) | -0.0985 | 0.1846 | ±0.3692 | -0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **215**, R² = **0.0679**, Adj R² = **0.0174**, F-statistic = **1.34** (p = **0.2024**), Residual SE = **64.619** on **203** df, AIC = **2414.3**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+449.7927** | 64.6211 | ±129.2423 | **+6.960** | **3.39e-12** | *** |
| Education: graduate level (vs college) | -3.1836 | 9.5223 | ±19.0446 | -0.334 | 0.7381 |  |
| Education: high school or below (vs college) | -8.1689 | 23.3361 | ±46.6722 | -0.350 | 0.7263 |  |
| **Site: UCSD (vs UAB)** | **-27.4089** | 13.3683 | ±26.7366 | **-2.050** | **0.0403** | * |
| Site: UW (vs UAB) | -13.5274 | 12.4483 | ±24.8966 | -1.087 | 0.2772 |  |
| Age (years) | -0.6226 | 0.5170 | ±1.0340 | -1.204 | 0.2285 |  |
| BMI (kg/m2) | -0.1672 | 0.7834 | ±1.5668 | -0.213 | 0.8309 |  |
| Hypertension | +4.8119 | 9.6751 | ±19.3501 | +0.497 | 0.6189 |  |
| High cholesterol | -3.1406 | 9.0300 | ±18.0600 | -0.348 | 0.7280 |  |
| Kidney disease | -38.0855 | 27.7796 | ±55.5592 | -1.371 | 0.1704 |  |
| **Circulatory disease** | **+41.5440** | 19.9834 | ±39.9667 | **+2.079** | **0.0376** | * |
| GMI (%) | -4.1195 | 7.7169 | ±15.4339 | -0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **215**, R² = **0.0675**, Adj R² = **0.0169**, F-statistic = **1.33** (p = **0.2071**), Residual SE = **64.634** on **203** df, AIC = **2414.4**, BIC = **2454.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+432.9701** | 48.8726 | ±97.7452 | **+8.859** | **8.06e-19** | *** |
| Education: graduate level (vs college) | -3.3964 | 9.4950 | ±18.9899 | -0.358 | 0.7206 |  |
| Education: high school or below (vs college) | -8.6623 | 23.2347 | ±46.4693 | -0.373 | 0.7093 |  |
| **Site: UCSD (vs UAB)** | **-27.2828** | 13.3162 | ±26.6324 | **-2.049** | **0.0405** | * |
| Site: UW (vs UAB) | -13.6907 | 12.4457 | ±24.8914 | -1.100 | 0.2713 |  |
| Age (years) | -0.6293 | 0.5172 | ±1.0345 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | -0.1612 | 0.7891 | ±1.5782 | -0.204 | 0.8381 |  |
| Hypertension | +4.7896 | 9.6705 | ±19.3411 | +0.495 | 0.6204 |  |
| High cholesterol | -3.2005 | 9.0521 | ±18.1042 | -0.354 | 0.7237 |  |
| Kidney disease | -38.9091 | 27.6508 | ±55.3016 | -1.407 | 0.1594 |  |
| **Circulatory disease** | **+41.3818** | 19.9808 | ±39.9617 | **+2.071** | **0.0384** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0748 | 0.1590 | ±0.3180 | -0.470 | 0.6382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **215**, R² = **0.0734**, Adj R² = **0.0232**, F-statistic = **1.46** (p = **0.1484**), Residual SE = **64.428** on **203** df, AIC = **2413.0**, BIC = **2453.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+445.4687** | 47.7665 | ±95.5330 | **+9.326** | **1.10e-20** | *** |
| Education: graduate level (vs college) | -3.6744 | 9.4874 | ±18.9748 | -0.387 | 0.6985 |  |
| Education: high school or below (vs college) | -8.7868 | 22.6613 | ±45.3226 | -0.388 | 0.6982 |  |
| **Site: UCSD (vs UAB)** | **-28.3292** | 13.5321 | ±27.0641 | **-2.093** | **0.0363** | * |
| Site: UW (vs UAB) | -14.1288 | 12.3425 | ±24.6849 | -1.145 | 0.2523 |  |
| Age (years) | -0.5990 | 0.5163 | ±1.0325 | -1.160 | 0.2459 |  |
| BMI (kg/m2) | -0.1538 | 0.7669 | ±1.5338 | -0.201 | 0.8411 |  |
| Hypertension | +5.1866 | 9.5827 | ±19.1654 | +0.541 | 0.5883 |  |
| High cholesterol | -4.5895 | 9.3478 | ±18.6956 | -0.491 | 0.6234 |  |
| Kidney disease | -34.0265 | 28.3456 | ±56.6912 | -1.200 | 0.2300 |  |
| **Circulatory disease** | **+42.2987** | 19.7169 | ±39.4338 | **+2.145** | **0.0319** | * |
| Glucose SD, pooled (mg/dL) | -0.7848 | 0.7310 | ±1.4620 | -1.074 | 0.2830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **215**, R² = **0.0798**, Adj R² = **0.0299**, F-statistic = **1.60** (p = **0.1006**), Residual SE = **64.204** on **203** df, AIC = **2411.5**, BIC = **2451.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+450.2550** | 46.0451 | ±92.0903 | **+9.779** | **1.39e-22** | *** |
| Education: graduate level (vs college) | -3.4017 | 9.4693 | ±18.9386 | -0.359 | 0.7194 |  |
| Education: high school or below (vs college) | -8.5420 | 22.5374 | ±45.0748 | -0.379 | 0.7047 |  |
| **Site: UCSD (vs UAB)** | **-28.5528** | 13.4886 | ±26.9773 | **-2.117** | **0.0343** | * |
| Site: UW (vs UAB) | -14.0611 | 12.3097 | ±24.6194 | -1.142 | 0.2533 |  |
| Age (years) | -0.5917 | 0.5178 | ±1.0355 | -1.143 | 0.2531 |  |
| BMI (kg/m2) | -0.0856 | 0.7745 | ±1.5491 | -0.110 | 0.9120 |  |
| Hypertension | +5.6427 | 9.5438 | ±19.0875 | +0.591 | 0.5544 |  |
| High cholesterol | -5.0306 | 9.3676 | ±18.7351 | -0.537 | 0.5912 |  |
| Kidney disease | -32.8601 | 28.6759 | ±57.3518 | -1.146 | 0.2518 |  |
| **Circulatory disease** | **+43.2714** | 19.6752 | ±39.3503 | **+2.199** | **0.0279** | * |
| Avg. daily SD (mg/dL) | -1.1299 | 0.7852 | ±1.5704 | -1.439 | 0.1501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **215**, R² = **0.0700**, Adj R² = **0.0196**, F-statistic = **1.39** (p = **0.1801**), Residual SE = **64.546** on **203** df, AIC = **2413.8**, BIC = **2454.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+444.0035** | 50.1355 | ±100.2711 | **+8.856** | **8.29e-19** | *** |
| Education: graduate level (vs college) | -4.2890 | 9.4825 | ±18.9650 | -0.452 | 0.6510 |  |
| Education: high school or below (vs college) | -10.8159 | 22.8950 | ±45.7899 | -0.472 | 0.6366 |  |
| **Site: UCSD (vs UAB)** | **-28.0656** | 13.5470 | ±27.0940 | **-2.072** | **0.0383** | * |
| Site: UW (vs UAB) | -14.6516 | 12.4392 | ±24.8785 | -1.178 | 0.2389 |  |
| Age (years) | -0.5950 | 0.5128 | ±1.0256 | -1.160 | 0.2459 |  |
| BMI (kg/m2) | -0.2367 | 0.7487 | ±1.4974 | -0.316 | 0.7518 |  |
| Hypertension | +4.8885 | 9.6158 | ±19.2317 | +0.508 | 0.6112 |  |
| High cholesterol | -5.3648 | 9.3370 | ±18.6741 | -0.575 | 0.5656 |  |
| Kidney disease | -36.0416 | 27.9587 | ±55.9173 | -1.289 | 0.1974 |  |
| **Circulatory disease** | **+40.7012** | 19.8303 | ±39.6606 | **+2.052** | **0.0401** | * |
| CV (%) | -0.8570 | 1.0138 | ±2.0276 | -0.845 | 0.3979 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **215**, R² = **0.0723**, Adj R² = **0.0220**, F-statistic = **1.44** (p = **0.1578**), Residual SE = **64.465** on **203** df, AIC = **2413.2**, BIC = **2453.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.4541** | 52.2552 | ±104.5103 | **+7.625** | **2.44e-14** | *** |
| Education: graduate level (vs college) | -3.9931 | 9.4808 | ±18.9615 | -0.421 | 0.6736 |  |
| Education: high school or below (vs college) | -10.5194 | 22.9226 | ±45.8453 | -0.459 | 0.6463 |  |
| **Site: UCSD (vs UAB)** | **-27.9060** | 13.4148 | ±26.8296 | **-2.080** | **0.0375** | * |
| Site: UW (vs UAB) | -14.6803 | 12.3720 | ±24.7441 | -1.187 | 0.2354 |  |
| Age (years) | -0.5929 | 0.5139 | ±1.0278 | -1.154 | 0.2486 |  |
| BMI (kg/m2) | -0.2457 | 0.7467 | ±1.4933 | -0.329 | 0.7421 |  |
| Hypertension | +5.4065 | 9.5923 | ±19.1846 | +0.564 | 0.5730 |  |
| High cholesterol | -5.5194 | 9.2927 | ±18.5854 | -0.594 | 0.5525 |  |
| Kidney disease | -35.7840 | 27.9250 | ±55.8501 | -1.281 | 0.2000 |  |
| **Circulatory disease** | **+40.6906** | 19.8219 | ±39.6437 | **+2.053** | **0.0401** | * |
| Mean / SD ratio | +5.5899 | 4.8598 | ±9.7195 | +1.150 | 0.2500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **215**, R² = **0.0985**, Adj R² = **0.0496**, F-statistic = **2.02** (p = **0.0285**), Residual SE = **63.550** on **203** df, AIC = **2407.1**, BIC = **2447.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+366.2937** | 51.4431 | ±102.8863 | **+7.120** | **1.08e-12** | *** |
| Education: graduate level (vs college) | -3.7648 | 9.3861 | ±18.7721 | -0.401 | 0.6883 |  |
| Education: high school or below (vs college) | -10.7822 | 22.6034 | ±45.2067 | -0.477 | 0.6334 |  |
| **Site: UCSD (vs UAB)** | **-28.3168** | 13.3669 | ±26.7338 | **-2.118** | **0.0341** | * |
| Site: UW (vs UAB) | -16.0382 | 12.1848 | ±24.3697 | -1.316 | 0.1881 |  |
| Age (years) | -0.5336 | 0.5083 | ±1.0166 | -1.050 | 0.2939 |  |
| BMI (kg/m2) | -0.2230 | 0.7230 | ±1.4460 | -0.309 | 0.7577 |  |
| Hypertension | +6.4730 | 9.4370 | ±18.8740 | +0.686 | 0.4928 |  |
| High cholesterol | -7.8701 | 9.2709 | ±18.5418 | -0.849 | 0.3959 |  |
| Kidney disease | -32.0033 | 28.1286 | ±56.2573 | -1.138 | 0.2552 |  |
| **Circulatory disease** | **+40.7620** | 19.7978 | ±39.5955 | **+2.059** | **0.0395** | * |
| **Avg. daily mean/SD** | **+10.0905** | 3.9652 | ±7.9304 | **+2.545** | **0.0109** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **215**, R² = **0.1139**, Adj R² = **0.0659**, F-statistic = **2.37** (p = **0.0088**), Residual SE = **63.002** on **203** df, AIC = **2403.4**, BIC = **2443.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+505.5945** | 49.5925 | ±99.1850 | **+10.195** | **2.09e-24** | *** |
| Education: graduate level (vs college) | -6.5113 | 9.3082 | ±18.6165 | -0.700 | 0.4842 |  |
| Education: high school or below (vs college) | -11.5151 | 21.9544 | ±43.9088 | -0.524 | 0.5999 |  |
| **Site: UCSD (vs UAB)** | **-30.7591** | 13.1277 | ±26.2555 | **-2.343** | **0.0191** | * |
| Site: UW (vs UAB) | -20.7623 | 12.3380 | ±24.6760 | -1.683 | 0.0924 | . |
| Age (years) | -0.6563 | 0.4930 | ±0.9860 | -1.331 | 0.1831 |  |
| BMI (kg/m2) | +0.0567 | 0.7396 | ±1.4792 | +0.077 | 0.9389 |  |
| Hypertension | +0.5212 | 9.5641 | ±19.1282 | +0.054 | 0.9565 |  |
| High cholesterol | -9.0400 | 9.0452 | ±18.0904 | -0.999 | 0.3176 |  |
| Kidney disease | -38.3504 | 26.9473 | ±53.8947 | -1.423 | 0.1547 |  |
| **Circulatory disease** | **+41.1216** | 19.6078 | ±39.2157 | **+2.097** | **0.0360** | * |
| **MAG (mg/dL/h)** | **-1.7349** | 0.5076 | ±1.0153 | **-3.418** | **6.32e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **215**, R² = **0.0872**, Adj R² = **0.0378**, F-statistic = **1.76** (p = **0.0622**), Residual SE = **63.944** on **203** df, AIC = **2409.7**, BIC = **2450.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+472.3981** | 49.6636 | ±99.3272 | **+9.512** | **1.87e-21** | *** |
| Education: graduate level (vs college) | -3.6358 | 9.4395 | ±18.8789 | -0.385 | 0.7001 |  |
| Education: high school or below (vs college) | -8.1142 | 22.3113 | ±44.6227 | -0.364 | 0.7161 |  |
| **Site: UCSD (vs UAB)** | **-29.6489** | 13.6228 | ±27.2457 | **-2.176** | **0.0295** | * |
| Site: UW (vs UAB) | -15.5582 | 12.2604 | ±24.5208 | -1.269 | 0.2044 |  |
| Age (years) | -0.6200 | 0.5125 | ±1.0250 | -1.210 | 0.2263 |  |
| BMI (kg/m2) | -0.1124 | 0.7473 | ±1.4946 | -0.150 | 0.8804 |  |
| Hypertension | +4.8741 | 9.5268 | ±19.0537 | +0.512 | 0.6089 |  |
| High cholesterol | -6.7646 | 9.4069 | ±18.8137 | -0.719 | 0.4721 |  |
| Kidney disease | -34.2899 | 28.4634 | ±56.9268 | -1.205 | 0.2283 |  |
| **Circulatory disease** | **+43.0620** | 19.6192 | ±39.2385 | **+2.195** | **0.0282** | * |
| Avg. daily range (mg/dL) | -0.3631 | 0.2030 | ±0.4060 | -1.789 | 0.0737 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **215**, R² = **0.0673**, Adj R² = **0.0168**, F-statistic = **1.33** (p = **0.2085**), Residual SE = **64.638** on **203** df, AIC = **2414.4**, BIC = **2454.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+427.7541** | 46.2390 | ±92.4780 | **+9.251** | **2.23e-20** | *** |
| Education: graduate level (vs college) | -3.7416 | 9.5062 | ±19.0124 | -0.394 | 0.6939 |  |
| Education: high school or below (vs college) | -9.5052 | 22.7249 | ±45.4497 | -0.418 | 0.6757 |  |
| **Site: UCSD (vs UAB)** | **-27.3565** | 13.2660 | ±26.5319 | **-2.062** | **0.0392** | * |
| Site: UW (vs UAB) | -13.7625 | 12.4081 | ±24.8163 | -1.109 | 0.2674 |  |
| Age (years) | -0.6130 | 0.5139 | ±1.0279 | -1.193 | 0.2330 |  |
| BMI (kg/m2) | -0.2048 | 0.7595 | ±1.5191 | -0.270 | 0.7874 |  |
| Hypertension | +4.6515 | 9.6423 | ±19.2846 | +0.482 | 0.6295 |  |
| High cholesterol | -3.5381 | 9.0559 | ±18.1118 | -0.391 | 0.6960 |  |
| Kidney disease | -38.1955 | 27.8838 | ±55.7676 | -1.370 | 0.1707 |  |
| **Circulatory disease** | **+40.5837** | 19.6330 | ±39.2660 | **+2.067** | **0.0387** | * |
| SD of daily means (mg/dL) | -0.4698 | 0.9519 | ±1.9037 | -0.494 | 0.6216 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **215**, R² = **0.0664**, Adj R² = **0.0158**, F-statistic = **1.31** (p = **0.2189**), Residual SE = **64.669** on **203** df, AIC = **2414.6**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+422.8971** | 61.7687 | ±123.5374 | **+6.846** | **7.57e-12** | *** |
| Education: graduate level (vs college) | -3.5123 | 9.5271 | ±19.0541 | -0.369 | 0.7124 |  |
| Education: high school or below (vs college) | -9.5923 | 23.2681 | ±46.5362 | -0.412 | 0.6802 |  |
| **Site: UCSD (vs UAB)** | **-27.2274** | 13.5054 | ±27.0109 | **-2.016** | **0.0438** | * |
| Site: UW (vs UAB) | -13.7814 | 12.4727 | ±24.9453 | -1.105 | 0.2692 |  |
| Age (years) | -0.6212 | 0.5154 | ±1.0308 | -1.205 | 0.2281 |  |
| BMI (kg/m2) | -0.2113 | 0.8112 | ±1.6223 | -0.260 | 0.7945 |  |
| Hypertension | +4.7993 | 9.7058 | ±19.4115 | +0.494 | 0.6210 |  |
| High cholesterol | -3.6849 | 9.0522 | ±18.1045 | -0.407 | 0.6840 |  |
| Kidney disease | -38.5992 | 27.8157 | ±55.6313 | -1.388 | 0.1652 |  |
| **Circulatory disease** | **+40.6415** | 20.0162 | ±40.0324 | **+2.030** | **0.0423** | * |
| Time in range 70-180, pooled (%) | +0.0163 | 0.3753 | ±0.7506 | +0.043 | 0.9653 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **215**, R² = **0.0664**, Adj R² = **0.0158**, F-statistic = **1.31** (p = **0.2190**), Residual SE = **64.669** on **203** df, AIC = **2414.6**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.1553** | 62.1180 | ±124.2360 | **+6.828** | **8.60e-12** | *** |
| Education: graduate level (vs college) | -3.5134 | 9.5317 | ±19.0634 | -0.369 | 0.7124 |  |
| Education: high school or below (vs college) | -9.6670 | 23.2406 | ±46.4812 | -0.416 | 0.6774 |  |
| **Site: UCSD (vs UAB)** | **-27.1971** | 13.5146 | ±27.0292 | **-2.012** | **0.0442** | * |
| Site: UW (vs UAB) | -13.7782 | 12.4745 | ±24.9490 | -1.105 | 0.2694 |  |
| Age (years) | -0.6208 | 0.5153 | ±1.0305 | -1.205 | 0.2283 |  |
| BMI (kg/m2) | -0.2160 | 0.8140 | ±1.6280 | -0.265 | 0.7907 |  |
| Hypertension | +4.8063 | 9.7066 | ±19.4132 | +0.495 | 0.6205 |  |
| High cholesterol | -3.7174 | 9.0459 | ±18.0917 | -0.411 | 0.6811 |  |
| Kidney disease | -38.6915 | 27.8499 | ±55.6998 | -1.389 | 0.1647 |  |
| **Circulatory disease** | **+40.5903** | 19.9959 | ±39.9919 | **+2.030** | **0.0424** | * |
| Avg. daily time in range 70-180 (%) | +0.0033 | 0.3734 | ±0.7467 | +0.009 | 0.9929 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **215**, R² = **0.0828**, Adj R² = **0.0331**, F-statistic = **1.67** (p = **0.0834**), Residual SE = **64.101** on **203** df, AIC = **2410.8**, BIC = **2451.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+421.2787** | 46.0916 | ±92.1832 | **+9.140** | **6.24e-20** | *** |
| Education: graduate level (vs college) | -1.5485 | 9.4631 | ±18.9263 | -0.164 | 0.8700 |  |
| Education: high school or below (vs college) | -7.2092 | 23.5135 | ±47.0269 | -0.307 | 0.7592 |  |
| **Site: UCSD (vs UAB)** | **-27.2248** | 13.3094 | ±26.6188 | **-2.046** | **0.0408** | * |
| Site: UW (vs UAB) | -12.2183 | 12.4694 | ±24.9387 | -0.980 | 0.3272 |  |
| Age (years) | -0.6519 | 0.5170 | ±1.0340 | -1.261 | 0.2073 |  |
| BMI (kg/m2) | -0.3278 | 0.7497 | ±1.4995 | -0.437 | 0.6619 |  |
| Hypertension | +4.9413 | 9.4937 | ±18.9873 | +0.520 | 0.6027 |  |
| High cholesterol | -1.6794 | 8.9949 | ±17.9898 | -0.187 | 0.8519 |  |
| Kidney disease | -38.8687 | 26.5367 | ±53.0734 | -1.465 | 0.1430 |  |
| **Circulatory disease** | **+39.1621** | 18.7906 | ±37.5812 | **+2.084** | **0.0371** | * |
| Any reading < 54 during wear (0/1) | +18.7949 | 10.5156 | ±21.0312 | +1.787 | 0.0739 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **215**, R² = **0.0669**, Adj R² = **0.0163**, F-statistic = **1.32** (p = **0.2139**), Residual SE = **64.654** on **203** df, AIC = **2414.5**, BIC = **2454.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.4187** | 45.7690 | ±91.5379 | **+9.295** | **1.47e-20** | *** |
| Education: graduate level (vs college) | -3.8464 | 9.5768 | ±19.1536 | -0.402 | 0.6880 |  |
| Education: high school or below (vs college) | -10.0746 | 22.8642 | ±45.7284 | -0.441 | 0.6595 |  |
| **Site: UCSD (vs UAB)** | **-27.5420** | 13.4448 | ±26.8896 | **-2.049** | **0.0405** | * |
| Site: UW (vs UAB) | -14.2872 | 12.7412 | ±25.4824 | -1.121 | 0.2621 |  |
| Age (years) | -0.6104 | 0.5141 | ±1.0283 | -1.187 | 0.2352 |  |
| BMI (kg/m2) | -0.2374 | 0.7649 | ±1.5298 | -0.310 | 0.7563 |  |
| Hypertension | +4.6146 | 9.6936 | ±19.3872 | +0.476 | 0.6340 |  |
| High cholesterol | -4.0287 | 9.1889 | ±18.3777 | -0.438 | 0.6611 |  |
| Kidney disease | -38.8108 | 27.6522 | ±55.3043 | -1.404 | 0.1605 |  |
| **Circulatory disease** | **+40.5774** | 19.6463 | ±39.2927 | **+2.065** | **0.0389** | * |
| Time < 54 (%) | -1.4026 | 4.4749 | ±8.9498 | -0.313 | 0.7539 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **215**, R² = **0.0671**, Adj R² = **0.0166**, F-statistic = **1.33** (p = **0.2109**), Residual SE = **64.645** on **203** df, AIC = **2414.4**, BIC = **2454.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.5804** | 45.7213 | ±91.4427 | **+9.308** | **1.30e-20** | *** |
| Education: graduate level (vs college) | -3.9211 | 9.5882 | ±19.1765 | -0.409 | 0.6826 |  |
| Education: high school or below (vs college) | -10.2202 | 22.8567 | ±45.7135 | -0.447 | 0.6548 |  |
| **Site: UCSD (vs UAB)** | **-27.6455** | 13.4496 | ±26.8992 | **-2.055** | **0.0398** | * |
| Site: UW (vs UAB) | -14.5218 | 12.8056 | ±25.6112 | -1.134 | 0.2568 |  |
| Age (years) | -0.6080 | 0.5134 | ±1.0269 | -1.184 | 0.2364 |  |
| BMI (kg/m2) | -0.2362 | 0.7605 | ±1.5210 | -0.311 | 0.7561 |  |
| Hypertension | +4.5539 | 9.7013 | ±19.4027 | +0.469 | 0.6388 |  |
| High cholesterol | -4.1970 | 9.2293 | ±18.4586 | -0.455 | 0.6493 |  |
| Kidney disease | -38.8492 | 27.6603 | ±55.3206 | -1.405 | 0.1602 |  |
| **Circulatory disease** | **+40.6354** | 19.6609 | ±39.3218 | **+2.067** | **0.0388** | * |
| Avg. daily time < 54 (%) | -2.3329 | 2.7337 | ±5.4675 | -0.853 | 0.3935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **215**, R² = **0.0679**, Adj R² = **0.0174**, F-statistic = **1.34** (p = **0.2025**), Residual SE = **64.619** on **203** df, AIC = **2414.3**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.6136** | 45.6095 | ±91.2191 | **+9.288** | **1.57e-20** | *** |
| Education: graduate level (vs college) | -2.7949 | 9.5016 | ±19.0033 | -0.294 | 0.7686 |  |
| Education: high school or below (vs college) | -8.7496 | 22.9584 | ±45.9168 | -0.381 | 0.7031 |  |
| **Site: UCSD (vs UAB)** | **-26.7376** | 13.3769 | ±26.7537 | **-1.999** | **0.0456** | * |
| Site: UW (vs UAB) | -12.9204 | 12.7412 | ±25.4825 | -1.014 | 0.3106 |  |
| Age (years) | -0.6291 | 0.5144 | ±1.0288 | -1.223 | 0.2213 |  |
| BMI (kg/m2) | -0.2494 | 0.7555 | ±1.5109 | -0.330 | 0.7413 |  |
| Hypertension | +5.0825 | 9.7129 | ±19.4258 | +0.523 | 0.6008 |  |
| High cholesterol | -2.9010 | 9.1100 | ±18.2199 | -0.318 | 0.7501 |  |
| Kidney disease | -38.7235 | 27.4773 | ±54.9546 | -1.409 | 0.1587 |  |
| **Circulatory disease** | **+40.6285** | 19.5221 | ±39.0441 | **+2.081** | **0.0374** | * |
| Time 54-69, pooled (%) | +1.9209 | 3.5591 | ±7.1182 | +0.540 | 0.5894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **215**, R² = **0.0667**, Adj R² = **0.0161**, F-statistic = **1.32** (p = **0.2161**), Residual SE = **64.661** on **203** df, AIC = **2414.5**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.1235** | 45.5450 | ±91.0901 | **+9.312** | **1.25e-20** | *** |
| Education: graduate level (vs college) | -3.2129 | 9.4935 | ±18.9869 | -0.338 | 0.7350 |  |
| Education: high school or below (vs college) | -9.2629 | 22.9270 | ±45.8540 | -0.404 | 0.6862 |  |
| **Site: UCSD (vs UAB)** | **-26.9848** | 13.4081 | ±26.8163 | **-2.013** | **0.0442** | * |
| Site: UW (vs UAB) | -13.3844 | 12.7856 | ±25.5712 | -1.047 | 0.2952 |  |
| Age (years) | -0.6250 | 0.5145 | ±1.0290 | -1.215 | 0.2245 |  |
| BMI (kg/m2) | -0.2285 | 0.7582 | ±1.5163 | -0.301 | 0.7631 |  |
| Hypertension | +4.9316 | 9.7179 | ±19.4359 | +0.507 | 0.6118 |  |
| High cholesterol | -3.3700 | 9.1096 | ±18.2192 | -0.370 | 0.7114 |  |
| Kidney disease | -38.7185 | 27.5996 | ±55.1993 | -1.403 | 0.1607 |  |
| **Circulatory disease** | **+40.6198** | 19.5847 | ±39.1694 | **+2.074** | **0.0381** | * |
| Avg. daily time 54-69 (%) | +0.7555 | 2.0276 | ±4.0551 | +0.373 | 0.7095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **215**, R² = **0.0666**, Adj R² = **0.0161**, F-statistic = **1.32** (p = **0.2165**), Residual SE = **64.662** on **203** df, AIC = **2414.5**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.9232** | 45.7350 | ±91.4700 | **+9.269** | **1.88e-20** | *** |
| Education: graduate level (vs college) | -3.2093 | 9.5568 | ±19.1135 | -0.336 | 0.7370 |  |
| Education: high school or below (vs college) | -9.3028 | 22.9643 | ±45.9285 | -0.405 | 0.6854 |  |
| **Site: UCSD (vs UAB)** | **-26.9453** | 13.4492 | ±26.8985 | **-2.003** | **0.0451** | * |
| Site: UW (vs UAB) | -13.3726 | 12.8703 | ±25.7407 | -1.039 | 0.2988 |  |
| Age (years) | -0.6266 | 0.5150 | ±1.0301 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | -0.2185 | 0.7595 | ±1.5189 | -0.288 | 0.7736 |  |
| Hypertension | +4.9479 | 9.7251 | ±19.4503 | +0.509 | 0.6109 |  |
| High cholesterol | -3.4041 | 9.1709 | ±18.3417 | -0.371 | 0.7105 |  |
| Kidney disease | -38.6839 | 27.6150 | ±55.2299 | -1.401 | 0.1613 |  |
| **Circulatory disease** | **+40.5910** | 19.5825 | ±39.1651 | **+2.073** | **0.0382** | * |
| Time < 70 (%) | +0.4991 | 1.6357 | ±3.2714 | +0.305 | 0.7603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **215**, R² = **0.0664**, Adj R² = **0.0158**, F-statistic = **1.31** (p = **0.2190**), Residual SE = **64.669** on **203** df, AIC = **2414.6**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.4523** | 45.6115 | ±91.2229 | **+9.306** | **1.33e-20** | *** |
| Education: graduate level (vs college) | -3.4963 | 9.5450 | ±19.0900 | -0.366 | 0.7141 |  |
| Education: high school or below (vs college) | -9.6596 | 22.9234 | ±45.8469 | -0.421 | 0.6735 |  |
| **Site: UCSD (vs UAB)** | **-27.1735** | 13.4559 | ±26.9117 | **-2.019** | **0.0434** | * |
| Site: UW (vs UAB) | -13.7503 | 12.8836 | ±25.7672 | -1.067 | 0.2858 |  |
| Age (years) | -0.6211 | 0.5147 | ±1.0294 | -1.207 | 0.2276 |  |
| BMI (kg/m2) | -0.2175 | 0.7575 | ±1.5150 | -0.287 | 0.7740 |  |
| Hypertension | +4.8164 | 9.7288 | ±19.4577 | +0.495 | 0.6206 |  |
| High cholesterol | -3.7049 | 9.1793 | ±18.3586 | -0.404 | 0.6865 |  |
| Kidney disease | -38.7140 | 27.6657 | ±55.3313 | -1.399 | 0.1617 |  |
| **Circulatory disease** | **+40.5787** | 19.6161 | ±39.2323 | **+2.069** | **0.0386** | * |
| Avg. daily time < 70 (%) | +0.0315 | 1.3355 | ±2.6711 | +0.024 | 0.9812 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **215**, R² = **0.0679**, Adj R² = **0.0174**, F-statistic = **1.34** (p = **0.2020**), Residual SE = **64.618** on **203** df, AIC = **2414.2**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.4591** | 61.5396 | ±123.0792 | **+6.442** | **1.18e-10** | *** |
| Education: graduate level (vs college) | -3.9179 | 9.5152 | ±19.0304 | -0.412 | 0.6805 |  |
| Education: high school or below (vs college) | -8.3689 | 23.2675 | ±46.5349 | -0.360 | 0.7191 |  |
| **Site: UCSD (vs UAB)** | **-27.6808** | 13.4520 | ±26.9041 | **-2.058** | **0.0396** | * |
| Site: UW (vs UAB) | -13.9501 | 12.4553 | ±24.9107 | -1.120 | 0.2627 |  |
| Age (years) | -0.6260 | 0.5143 | ±1.0286 | -1.217 | 0.2235 |  |
| BMI (kg/m2) | -0.2138 | 0.7575 | ±1.5151 | -0.282 | 0.7778 |  |
| Hypertension | +4.0725 | 9.7182 | ±19.4364 | +0.419 | 0.6752 |  |
| High cholesterol | -3.5397 | 9.0752 | ±18.1505 | -0.390 | 0.6965 |  |
| Kidney disease | -38.3100 | 27.6393 | ±55.2786 | -1.386 | 0.1657 |  |
| **Circulatory disease** | **+41.6808** | 20.0528 | ±40.1057 | **+2.079** | **0.0377** | * |
| Time 54-250, pooled (%) | +0.2930 | 0.4171 | ±0.8342 | +0.703 | 0.4823 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **215**, R² = **0.0680**, Adj R² = **0.0175**, F-statistic = **1.35** (p = **0.2015**), Residual SE = **64.616** on **203** df, AIC = **2414.2**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+394.5760** | 62.8454 | ±125.6908 | **+6.279** | **3.42e-10** | *** |
| Education: graduate level (vs college) | -3.9089 | 9.5116 | ±19.0232 | -0.411 | 0.6811 |  |
| Education: high school or below (vs college) | -8.3397 | 23.2608 | ±46.5216 | -0.359 | 0.7199 |  |
| **Site: UCSD (vs UAB)** | **-27.6784** | 13.4399 | ±26.8798 | **-2.059** | **0.0395** | * |
| Site: UW (vs UAB) | -13.9081 | 12.4432 | ±24.8863 | -1.118 | 0.2637 |  |
| Age (years) | -0.6263 | 0.5143 | ±1.0286 | -1.218 | 0.2233 |  |
| BMI (kg/m2) | -0.2083 | 0.7586 | ±1.5172 | -0.275 | 0.7837 |  |
| Hypertension | +4.0500 | 9.7229 | ±19.4458 | +0.417 | 0.6770 |  |
| High cholesterol | -3.5253 | 9.0714 | ±18.1428 | -0.389 | 0.6976 |  |
| Kidney disease | -38.3126 | 27.6722 | ±55.3444 | -1.385 | 0.1662 |  |
| **Circulatory disease** | **+41.7112** | 20.0465 | ±40.0931 | **+2.081** | **0.0375** | * |
| Avg. daily time 54-250 (%) | +0.3101 | 0.4273 | ±0.8546 | +0.726 | 0.4679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **215**, R² = **0.0671**, Adj R² = **0.0165**, F-statistic = **1.33** (p = **0.2112**), Residual SE = **64.646** on **203** df, AIC = **2414.4**, BIC = **2454.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.8573** | 46.0920 | ±92.1840 | **+9.218** | **3.04e-20** | *** |
| Education: graduate level (vs college) | -3.8657 | 9.6799 | ±19.3599 | -0.399 | 0.6896 |  |
| Education: high school or below (vs college) | -9.9930 | 23.0940 | ±46.1880 | -0.433 | 0.6652 |  |
| **Site: UCSD (vs UAB)** | **-27.0974** | 13.3999 | ±26.7998 | **-2.022** | **0.0432** | * |
| Site: UW (vs UAB) | -13.9173 | 12.5097 | ±25.0193 | -1.113 | 0.2659 |  |
| Age (years) | -0.6182 | 0.5137 | ±1.0274 | -1.203 | 0.2288 |  |
| BMI (kg/m2) | -0.2807 | 0.8492 | ±1.6983 | -0.331 | 0.7410 |  |
| Hypertension | +4.4094 | 9.7434 | ±19.4867 | +0.453 | 0.6509 |  |
| High cholesterol | -4.1598 | 9.0358 | ±18.0716 | -0.460 | 0.6453 |  |
| Kidney disease | -39.7906 | 28.1940 | ±56.3880 | -1.411 | 0.1582 |  |
| **Circulatory disease** | **+40.5455** | 19.8069 | ±39.6139 | **+2.047** | **0.0407** | * |
| Time 181-250, pooled (%) | +0.1867 | 0.6183 | ±1.2366 | +0.302 | 0.7626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **215**, R² = **0.0674**, Adj R² = **0.0169**, F-statistic = **1.33** (p = **0.2076**), Residual SE = **64.635** on **203** df, AIC = **2414.4**, BIC = **2454.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.9581** | 46.0994 | ±92.1989 | **+9.218** | **3.02e-20** | *** |
| Education: graduate level (vs college) | -3.9520 | 9.6828 | ±19.3656 | -0.408 | 0.6832 |  |
| Education: high school or below (vs college) | -10.0110 | 23.0835 | ±46.1671 | -0.434 | 0.6645 |  |
| **Site: UCSD (vs UAB)** | **-27.0061** | 13.4206 | ±26.8412 | **-2.012** | **0.0442** | * |
| Site: UW (vs UAB) | -13.8902 | 12.4972 | ±24.9943 | -1.111 | 0.2664 |  |
| Age (years) | -0.6184 | 0.5132 | ±1.0264 | -1.205 | 0.2282 |  |
| BMI (kg/m2) | -0.2921 | 0.8451 | ±1.6902 | -0.346 | 0.7296 |  |
| Hypertension | +4.3303 | 9.7385 | ±19.4769 | +0.445 | 0.6566 |  |
| High cholesterol | -4.2652 | 9.0227 | ±18.0454 | -0.473 | 0.6364 |  |
| Kidney disease | -40.0331 | 28.1612 | ±56.3224 | -1.422 | 0.1552 |  |
| **Circulatory disease** | **+40.5389** | 19.8073 | ±39.6146 | **+2.047** | **0.0407** | * |
| Avg. daily time 181-250 (%) | +0.2209 | 0.5962 | ±1.1923 | +0.371 | 0.7109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **215**, R² = **0.0665**, Adj R² = **0.0159**, F-statistic = **1.31** (p = **0.2187**), Residual SE = **64.668** on **203** df, AIC = **2414.6**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.5255** | 45.6823 | ±91.3646 | **+9.293** | **1.50e-20** | *** |
| Education: graduate level (vs college) | -3.4954 | 9.5391 | ±19.0781 | -0.366 | 0.7140 |  |
| Education: high school or below (vs college) | -9.5201 | 23.3270 | ±46.6540 | -0.408 | 0.6832 |  |
| **Site: UCSD (vs UAB)** | **-27.2373** | 13.4589 | ±26.9179 | **-2.024** | **0.0430** | * |
| Site: UW (vs UAB) | -13.7633 | 12.4660 | ±24.9320 | -1.104 | 0.2696 |  |
| Age (years) | -0.6217 | 0.5156 | ±1.0313 | -1.206 | 0.2279 |  |
| BMI (kg/m2) | -0.2079 | 0.8114 | ±1.6229 | -0.256 | 0.7978 |  |
| Hypertension | +4.8017 | 9.7004 | ±19.4007 | +0.495 | 0.6206 |  |
| High cholesterol | -3.6448 | 9.0484 | ±18.0969 | -0.403 | 0.6871 |  |
| Kidney disease | -38.5311 | 27.8764 | ±55.7528 | -1.382 | 0.1669 |  |
| **Circulatory disease** | **+40.6785** | 20.0112 | ±40.0224 | **+2.033** | **0.0421** | * |
| Time > 180 (%) | -0.0256 | 0.3754 | ±0.7509 | -0.068 | 0.9456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **215**, R² = **0.0664**, Adj R² = **0.0158**, F-statistic = **1.31** (p = **0.2190**), Residual SE = **64.669** on **203** df, AIC = **2414.6**, BIC = **2455.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.4858** | 45.7166 | ±91.4333 | **+9.285** | **1.61e-20** | *** |
| Education: graduate level (vs college) | -3.5110 | 9.5451 | ±19.0903 | -0.368 | 0.7130 |  |
| Education: high school or below (vs college) | -9.6612 | 23.2915 | ±46.5829 | -0.415 | 0.6783 |  |
| **Site: UCSD (vs UAB)** | **-27.1967** | 13.4683 | ±26.9365 | **-2.019** | **0.0435** | * |
| Site: UW (vs UAB) | -13.7752 | 12.4689 | ±24.9378 | -1.105 | 0.2693 |  |
| Age (years) | -0.6209 | 0.5153 | ±1.0306 | -1.205 | 0.2283 |  |
| BMI (kg/m2) | -0.2158 | 0.8129 | ±1.6257 | -0.266 | 0.7906 |  |
| Hypertension | +4.8071 | 9.7034 | ±19.4068 | +0.495 | 0.6203 |  |
| High cholesterol | -3.7134 | 9.0402 | ±18.0805 | -0.411 | 0.6812 |  |
| Kidney disease | -38.6875 | 27.9016 | ±55.8031 | -1.387 | 0.1656 |  |
| **Circulatory disease** | **+40.5924** | 19.9935 | ±39.9870 | **+2.030** | **0.0423** | * |
| Avg. daily time > 180 (%) | -0.0039 | 0.3726 | ±0.7453 | -0.010 | 0.9917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **215**, R² = **0.0669**, Adj R² = **0.0163**, F-statistic = **1.32** (p = **0.2134**), Residual SE = **64.653** on **203** df, AIC = **2414.5**, BIC = **2454.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+424.6472** | 45.8028 | ±91.6056 | **+9.271** | **1.84e-20** | *** |
| Education: graduate level (vs college) | -3.3571 | 9.5149 | ±19.0297 | -0.353 | 0.7242 |  |
| Education: high school or below (vs college) | -9.8174 | 23.2848 | ±46.5696 | -0.422 | 0.6733 |  |
| **Site: UCSD (vs UAB)** | **-26.9802** | 13.4239 | ±26.8477 | **-2.010** | **0.0444** | * |
| Site: UW (vs UAB) | -13.7331 | 12.4574 | ±24.9148 | -1.102 | 0.2703 |  |
| Age (years) | -0.6113 | 0.5143 | ±1.0286 | -1.189 | 0.2346 |  |
| BMI (kg/m2) | -0.2676 | 0.8249 | ±1.6498 | -0.324 | 0.7456 |  |
| Hypertension | +4.9592 | 9.6755 | ±19.3510 | +0.513 | 0.6083 |  |
| High cholesterol | -4.1519 | 9.0616 | ±18.1232 | -0.458 | 0.6468 |  |
| Kidney disease | -38.7149 | 27.7033 | ±55.4066 | -1.397 | 0.1623 |  |
| **Circulatory disease** | **+40.2302** | 20.0510 | ±40.1019 | **+2.006** | **0.0448** | * |
| Nocturnal time > 180 (%) | +0.0985 | 0.3438 | ±0.6877 | +0.286 | 0.7745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **215**, R² = **0.0678**, Adj R² = **0.0172**, F-statistic = **1.34** (p = **0.2039**), Residual SE = **64.623** on **203** df, AIC = **2414.3**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.5087** | 45.5915 | ±91.1829 | **+9.333** | **1.03e-20** | *** |
| Education: graduate level (vs college) | -3.8306 | 9.5047 | ±19.0094 | -0.403 | 0.6869 |  |
| Education: high school or below (vs college) | -8.3622 | 23.3309 | ±46.6618 | -0.358 | 0.7200 |  |
| **Site: UCSD (vs UAB)** | **-27.5844** | 13.4217 | ±26.8433 | **-2.055** | **0.0399** | * |
| Site: UW (vs UAB) | -13.8399 | 12.4364 | ±24.8729 | -1.113 | 0.2658 |  |
| Age (years) | -0.6278 | 0.5144 | ±1.0289 | -1.220 | 0.2223 |  |
| BMI (kg/m2) | -0.2100 | 0.7595 | ±1.5189 | -0.277 | 0.7821 |  |
| Hypertension | +4.1501 | 9.7041 | ±19.4081 | +0.428 | 0.6689 |  |
| High cholesterol | -3.4898 | 9.0725 | ±18.1450 | -0.385 | 0.7005 |  |
| Kidney disease | -38.3130 | 27.6316 | ±55.2632 | -1.387 | 0.1656 |  |
| **Circulatory disease** | **+41.6217** | 20.0584 | ±40.1167 | **+2.075** | **0.0380** | * |
| Time > 250 (%) | -0.2773 | 0.4359 | ±0.8718 | -0.636 | 0.5246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 215)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **215**, R² = **0.0678**, Adj R² = **0.0173**, F-statistic = **1.34** (p = **0.2034**), Residual SE = **64.622** on **203** df, AIC = **2414.3**, BIC = **2454.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.3911** | 45.5798 | ±91.1596 | **+9.333** | **1.03e-20** | *** |
| Education: graduate level (vs college) | -3.8358 | 9.5030 | ±19.0060 | -0.404 | 0.6865 |  |
| Education: high school or below (vs college) | -8.3476 | 23.3131 | ±46.6262 | -0.358 | 0.7203 |  |
| **Site: UCSD (vs UAB)** | **-27.5936** | 13.4163 | ±26.8325 | **-2.057** | **0.0397** | * |
| Site: UW (vs UAB) | -13.8072 | 12.4298 | ±24.8595 | -1.111 | 0.2666 |  |
| Age (years) | -0.6276 | 0.5144 | ±1.0288 | -1.220 | 0.2224 |  |
| BMI (kg/m2) | -0.2064 | 0.7601 | ±1.5202 | -0.272 | 0.7860 |  |
| Hypertension | +4.1243 | 9.7100 | ±19.4199 | +0.425 | 0.6710 |  |
| High cholesterol | -3.4774 | 9.0685 | ±18.1370 | -0.383 | 0.7014 |  |
| Kidney disease | -38.3184 | 27.6651 | ±55.3301 | -1.385 | 0.1660 |  |
| **Circulatory disease** | **+41.6406** | 20.0467 | ±40.0933 | **+2.077** | **0.0378** | * |
| Avg. daily time > 250 (%) | -0.2928 | 0.4432 | ±0.8864 | -0.661 | 0.5088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 218; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **218**, R² = **0.0493**, Adj R² = **0.0034**, F-statistic = **1.07** (p = **0.3839**), Residual SE = **16.396** on **207** df, AIC = **1848.9**, BIC = **1886.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2514** | 10.6263 | ±21.2525 | **+5.388** | **7.14e-08** | *** |
| Education: graduate level (vs college) | -0.9018 | 2.4054 | ±4.8108 | -0.375 | 0.7077 |  |
| Education: high school or below (vs college) | +2.1600 | 5.5470 | ±11.0941 | +0.389 | 0.6970 |  |
| Site: UCSD (vs UAB) | +2.7470 | 3.4687 | ±6.9374 | +0.792 | 0.4284 |  |
| Site: UW (vs UAB) | +0.2211 | 2.8981 | ±5.7962 | +0.076 | 0.9392 |  |
| **Age (years)** | **-0.2187** | 0.1113 | ±0.2226 | **-1.965** | **0.0494** | * |
| BMI (kg/m2) | +0.1503 | 0.2092 | ±0.4184 | +0.719 | 0.4723 |  |
| Hypertension | -3.9887 | 2.4855 | ±4.9709 | -1.605 | 0.1085 |  |
| High cholesterol | +3.6305 | 2.4018 | ±4.8037 | +1.512 | 0.1307 |  |
| Kidney disease | +3.1733 | 5.7596 | ±11.5193 | +0.551 | 0.5817 |  |
| Circulatory disease | +0.0126 | 4.7441 | ±9.4883 | +0.003 | 0.9979 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **218**, R² = **0.0734**, Adj R² = **0.0239**, F-statistic = **1.48** (p = **0.1398**), Residual SE = **16.226** on **206** df, AIC = **1845.3**, BIC = **1885.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.5062** | 13.1692 | ±26.3383 | **+3.152** | **0.0016** | ** |
| Education: graduate level (vs college) | -0.8563 | 2.4030 | ±4.8061 | -0.356 | 0.7216 |  |
| Education: high school or below (vs college) | +0.8860 | 5.2794 | ±10.5588 | +0.168 | 0.8667 |  |
| Site: UCSD (vs UAB) | +2.4614 | 3.4699 | ±6.9398 | +0.709 | 0.4781 |  |
| Site: UW (vs UAB) | -0.0202 | 2.8324 | ±5.6649 | -0.007 | 0.9943 |  |
| **Age (years)** | **-0.2200** | 0.1109 | ±0.2218 | **-1.984** | **0.0472** | * |
| BMI (kg/m2) | +0.1087 | 0.2081 | ±0.4162 | +0.523 | 0.6013 |  |
| Hypertension | -3.9667 | 2.4530 | ±4.9061 | -1.617 | 0.1059 |  |
| High cholesterol | +3.0148 | 2.3956 | ±4.7912 | +1.258 | 0.2082 |  |
| Kidney disease | +3.5854 | 5.7540 | ±11.5081 | +0.623 | 0.5332 |  |
| Circulatory disease | -1.2375 | 4.5125 | ±9.0249 | -0.274 | 0.7839 |  |
| **HbA1c (%)** | **+2.9567** | 1.2952 | ±2.5904 | **+2.283** | **0.0224** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **218**, R² = **0.0556**, Adj R² = **0.0052**, F-statistic = **1.10** (p = **0.3602**), Residual SE = **16.381** on **206** df, AIC = **1849.4**, BIC = **1890.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6537** | 13.1717 | ±26.3433 | **+3.922** | **8.80e-05** | *** |
| Education: graduate level (vs college) | -1.1107 | 2.4315 | ±4.8629 | -0.457 | 0.6478 |  |
| Education: high school or below (vs college) | +1.5578 | 5.4690 | ±10.9381 | +0.285 | 0.7758 |  |
| Site: UCSD (vs UAB) | +2.6990 | 3.5070 | ±7.0139 | +0.770 | 0.4415 |  |
| Site: UW (vs UAB) | +0.0601 | 2.8880 | ±5.7760 | +0.021 | 0.9834 |  |
| Age (years) | -0.2157 | 0.1120 | ±0.2240 | -1.926 | 0.0541 | . |
| BMI (kg/m2) | +0.1178 | 0.2128 | ±0.4257 | +0.553 | 0.5800 |  |
| Hypertension | -4.1013 | 2.5177 | ±5.0353 | -1.629 | 0.1033 |  |
| High cholesterol | +3.4032 | 2.4101 | ±4.8202 | +1.412 | 0.1579 |  |
| Kidney disease | +3.0199 | 5.7705 | ±11.5411 | +0.523 | 0.6007 |  |
| Circulatory disease | -0.3542 | 4.7194 | ±9.4388 | -0.075 | 0.9402 |  |
| Mean glucose (mg/dL) | +0.0483 | 0.0613 | ±0.1226 | +0.789 | 0.4303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **218**, R² = **0.0556**, Adj R² = **0.0052**, F-statistic = **1.10** (p = **0.3602**), Residual SE = **16.381** on **206** df, AIC = **1849.4**, BIC = **1890.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.9653** | 19.4155 | ±38.8309 | **+2.316** | **0.0206** | * |
| Education: graduate level (vs college) | -1.1107 | 2.4315 | ±4.8629 | -0.457 | 0.6478 |  |
| Education: high school or below (vs college) | +1.5578 | 5.4690 | ±10.9381 | +0.285 | 0.7758 |  |
| Site: UCSD (vs UAB) | +2.6990 | 3.5070 | ±7.0139 | +0.770 | 0.4415 |  |
| Site: UW (vs UAB) | +0.0601 | 2.8880 | ±5.7760 | +0.021 | 0.9834 |  |
| Age (years) | -0.2157 | 0.1120 | ±0.2240 | -1.926 | 0.0541 | . |
| BMI (kg/m2) | +0.1178 | 0.2128 | ±0.4257 | +0.553 | 0.5800 |  |
| Hypertension | -4.1013 | 2.5177 | ±5.0353 | -1.629 | 0.1033 |  |
| High cholesterol | +3.4032 | 2.4101 | ±4.8202 | +1.412 | 0.1579 |  |
| Kidney disease | +3.0199 | 5.7705 | ±11.5411 | +0.523 | 0.6007 |  |
| Circulatory disease | -0.3542 | 4.7194 | ±9.4388 | -0.075 | 0.9402 |  |
| GMI (%) | +2.0207 | 2.5621 | ±5.1243 | +0.789 | 0.4303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **218**, R² = **0.0508**, Adj R² = **0.0001**, F-statistic = **1.00** (p = **0.4461**), Residual SE = **16.423** on **206** df, AIC = **1850.5**, BIC = **1891.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9518** | 12.5425 | ±25.0850 | **+4.381** | **1.18e-05** | *** |
| Education: graduate level (vs college) | -0.9513 | 2.4317 | ±4.8633 | -0.391 | 0.6956 |  |
| Education: high school or below (vs college) | +1.9304 | 5.5971 | ±11.1943 | +0.345 | 0.7302 |  |
| Site: UCSD (vs UAB) | +2.6795 | 3.4966 | ±6.9931 | +0.766 | 0.4435 |  |
| Site: UW (vs UAB) | +0.1741 | 2.9175 | ±5.8349 | +0.060 | 0.9524 |  |
| Age (years) | -0.2156 | 0.1126 | ±0.2252 | -1.915 | 0.0555 | . |
| BMI (kg/m2) | +0.1310 | 0.2183 | ±0.4367 | +0.600 | 0.5485 |  |
| Hypertension | -4.0362 | 2.5463 | ±5.0926 | -1.585 | 0.1129 |  |
| High cholesterol | +3.5227 | 2.4157 | ±4.8314 | +1.458 | 0.1448 |  |
| Kidney disease | +3.2917 | 5.8111 | ±11.6222 | +0.566 | 0.5711 |  |
| Circulatory disease | -0.1602 | 4.7819 | ±9.5637 | -0.034 | 0.9733 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0209 | 0.0581 | ±0.1162 | +0.360 | 0.7191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **218**, R² = **0.0579**, Adj R² = **0.0076**, F-statistic = **1.15** (p = **0.3236**), Residual SE = **16.361** on **206** df, AIC = **1848.9**, BIC = **1889.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4613** | 12.4184 | ±24.8367 | **+4.144** | **3.41e-05** | *** |
| Education: graduate level (vs college) | -0.8873 | 2.4124 | ±4.8249 | -0.368 | 0.7130 |  |
| Education: high school or below (vs college) | +2.1393 | 5.4032 | ±10.8065 | +0.396 | 0.6922 |  |
| Site: UCSD (vs UAB) | +3.0126 | 3.5427 | ±7.0854 | +0.850 | 0.3951 |  |
| Site: UW (vs UAB) | +0.3284 | 2.9050 | ±5.8100 | +0.113 | 0.9100 |  |
| **Age (years)** | **-0.2218** | 0.1108 | ±0.2216 | **-2.001** | **0.0454** | * |
| BMI (kg/m2) | +0.1268 | 0.2144 | ±0.4289 | +0.591 | 0.5543 |  |
| Hypertension | -4.1361 | 2.5118 | ±5.0237 | -1.647 | 0.0996 | . |
| High cholesterol | +3.8498 | 2.4535 | ±4.9070 | +1.569 | 0.1166 |  |
| Kidney disease | +2.0826 | 5.8513 | ±11.7025 | +0.356 | 0.7219 |  |
| Circulatory disease | -0.3524 | 4.6923 | ±9.3847 | -0.075 | 0.9401 |  |
| Glucose SD, pooled (mg/dL) | +0.2165 | 0.2024 | ±0.4049 | +1.069 | 0.2850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **218**, R² = **0.0580**, Adj R² = **0.0077**, F-statistic = **1.15** (p = **0.3225**), Residual SE = **16.361** on **206** df, AIC = **1848.9**, BIC = **1889.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.1520** | 11.9242 | ±23.8483 | **+4.374** | **1.22e-05** | *** |
| Education: graduate level (vs college) | -0.9486 | 2.4064 | ±4.8128 | -0.394 | 0.6934 |  |
| Education: high school or below (vs college) | +2.1618 | 5.4245 | ±10.8489 | +0.399 | 0.6902 |  |
| Site: UCSD (vs UAB) | +2.9440 | 3.5238 | ±7.0476 | +0.835 | 0.4035 |  |
| Site: UW (vs UAB) | +0.2861 | 2.9032 | ±5.8063 | +0.099 | 0.9215 |  |
| **Age (years)** | **-0.2218** | 0.1107 | ±0.2214 | **-2.004** | **0.0451** | * |
| BMI (kg/m2) | +0.1181 | 0.2145 | ±0.4290 | +0.551 | 0.5819 |  |
| Hypertension | -4.2120 | 2.5208 | ±5.0416 | -1.671 | 0.0947 | . |
| High cholesterol | +3.8770 | 2.4517 | ±4.9034 | +1.581 | 0.1138 |  |
| Kidney disease | +2.2251 | 5.8046 | ±11.6092 | +0.383 | 0.7015 |  |
| Circulatory disease | -0.4349 | 4.7062 | ±9.4123 | -0.092 | 0.9264 |  |
| Avg. daily SD (mg/dL) | +0.2244 | 0.2011 | ±0.4021 | +1.116 | 0.2644 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **218**, R² = **0.0527**, Adj R² = **0.0021**, F-statistic = **1.04** (p = **0.4114**), Residual SE = **16.407** on **206** df, AIC = **1850.1**, BIC = **1890.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4215** | 12.4116 | ±24.8232 | **+4.224** | **2.40e-05** | *** |
| Education: graduate level (vs college) | -0.7125 | 2.4247 | ±4.8494 | -0.294 | 0.7689 |  |
| Education: high school or below (vs college) | +2.5146 | 5.5538 | ±11.1076 | +0.453 | 0.6507 |  |
| Site: UCSD (vs UAB) | +3.0109 | 3.4717 | ±6.9433 | +0.867 | 0.3858 |  |
| Site: UW (vs UAB) | +0.4662 | 2.9047 | ±5.8095 | +0.160 | 0.8725 |  |
| **Age (years)** | **-0.2238** | 0.1114 | ±0.2228 | **-2.010** | **0.0445** | * |
| BMI (kg/m2) | +0.1550 | 0.2127 | ±0.4253 | +0.729 | 0.4660 |  |
| Hypertension | -3.9809 | 2.5062 | ±5.0124 | -1.588 | 0.1122 |  |
| High cholesterol | +3.9874 | 2.4201 | ±4.8401 | +1.648 | 0.0994 | . |
| Kidney disease | +2.5822 | 5.9053 | ±11.8107 | +0.437 | 0.6619 |  |
| Circulatory disease | -0.0066 | 4.7637 | ±9.5273 | -0.001 | 0.9989 |  |
| CV (%) | +0.2084 | 0.2734 | ±0.5468 | +0.762 | 0.4459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **218**, R² = **0.0554**, Adj R² = **0.0050**, F-statistic = **1.10** (p = **0.3640**), Residual SE = **16.383** on **206** df, AIC = **1849.5**, BIC = **1890.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7233** | 12.0878 | ±24.1756 | **+5.272** | **1.35e-07** | *** |
| Education: graduate level (vs college) | -0.7754 | 2.4129 | ±4.8258 | -0.321 | 0.7480 |  |
| Education: high school or below (vs college) | +2.4824 | 5.5599 | ±11.1199 | +0.446 | 0.6552 |  |
| Site: UCSD (vs UAB) | +3.0173 | 3.4702 | ±6.9404 | +0.869 | 0.3846 |  |
| Site: UW (vs UAB) | +0.5064 | 2.9156 | ±5.8313 | +0.174 | 0.8621 |  |
| **Age (years)** | **-0.2242** | 0.1110 | ±0.2219 | **-2.021** | **0.0433** | * |
| BMI (kg/m2) | +0.1579 | 0.2132 | ±0.4264 | +0.741 | 0.4590 |  |
| Hypertension | -4.0869 | 2.5059 | ±5.0118 | -1.631 | 0.1029 |  |
| High cholesterol | +4.0261 | 2.4141 | ±4.8282 | +1.668 | 0.0954 | . |
| Kidney disease | +2.5093 | 5.9016 | ±11.8031 | +0.425 | 0.6707 |  |
| Circulatory disease | -0.0160 | 4.7579 | ±9.5158 | -0.003 | 0.9973 |  |
| Mean / SD ratio | -1.4196 | 1.3331 | ±2.6661 | -1.065 | 0.2869 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **218**, R² = **0.0580**, Adj R² = **0.0077**, F-statistic = **1.15** (p = **0.3217**), Residual SE = **16.360** on **206** df, AIC = **1848.9**, BIC = **1889.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.7171** | 11.9193 | ±23.8386 | **+5.430** | **5.65e-08** | *** |
| Education: graduate level (vs college) | -0.8508 | 2.3947 | ±4.7895 | -0.355 | 0.7224 |  |
| Education: high school or below (vs college) | +2.4526 | 5.5518 | ±11.1036 | +0.442 | 0.6587 |  |
| Site: UCSD (vs UAB) | +2.9494 | 3.4580 | ±6.9161 | +0.853 | 0.3937 |  |
| Site: UW (vs UAB) | +0.5726 | 2.9084 | ±5.8167 | +0.197 | 0.8439 |  |
| **Age (years)** | **-0.2284** | 0.1110 | ±0.2221 | **-2.057** | **0.0397** | * |
| BMI (kg/m2) | +0.1511 | 0.2132 | ±0.4264 | +0.709 | 0.4786 |  |
| Hypertension | -4.1653 | 2.5042 | ±5.0084 | -1.663 | 0.0962 | . |
| High cholesterol | +4.1112 | 2.4209 | ±4.8418 | +1.698 | 0.0895 | . |
| Kidney disease | +2.4195 | 5.8233 | ±11.6466 | +0.415 | 0.6778 |  |
| Circulatory disease | -0.0286 | 4.7682 | ±9.5364 | -0.006 | 0.9952 |  |
| Avg. daily mean/SD | -1.3188 | 1.0012 | ±2.0024 | -1.317 | 0.1878 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **218**, R² = **0.0497**, Adj R² = **-0.0010**, F-statistic = **0.98** (p = **0.4655**), Residual SE = **16.432** on **206** df, AIC = **1850.8**, BIC = **1891.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2983** | 12.0887 | ±24.1775 | **+4.574** | **4.78e-06** | *** |
| Education: graduate level (vs college) | -0.8267 | 2.3972 | ±4.7944 | -0.345 | 0.7302 |  |
| Education: high school or below (vs college) | +2.2280 | 5.5722 | ±11.1444 | +0.400 | 0.6893 |  |
| Site: UCSD (vs UAB) | +2.8409 | 3.4903 | ±6.9806 | +0.814 | 0.4157 |  |
| Site: UW (vs UAB) | +0.3868 | 2.9266 | ±5.8531 | +0.132 | 0.8948 |  |
| Age (years) | -0.2174 | 0.1112 | ±0.2225 | -1.954 | 0.0507 | . |
| BMI (kg/m2) | +0.1432 | 0.2111 | ±0.4223 | +0.678 | 0.4976 |  |
| Hypertension | -3.8853 | 2.5002 | ±5.0004 | -1.554 | 0.1202 |  |
| High cholesterol | +3.7510 | 2.4963 | ±4.9927 | +1.503 | 0.1329 |  |
| Kidney disease | +3.1816 | 5.7430 | ±11.4861 | +0.554 | 0.5796 |  |
| Circulatory disease | +0.0066 | 4.7588 | ±9.5176 | +0.001 | 0.9989 |  |
| MAG (mg/dL/h) | +0.0414 | 0.1400 | ±0.2800 | +0.296 | 0.7673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **218**, R² = **0.0565**, Adj R² = **0.0062**, F-statistic = **1.12** (p = **0.3454**), Residual SE = **16.373** on **206** df, AIC = **1849.2**, BIC = **1889.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2020** | 12.5604 | ±25.1207 | **+3.997** | **6.42e-05** | *** |
| Education: graduate level (vs college) | -0.8865 | 2.4051 | ±4.8102 | -0.369 | 0.7124 |  |
| Education: high school or below (vs college) | +2.0970 | 5.4457 | ±10.8914 | +0.385 | 0.7002 |  |
| Site: UCSD (vs UAB) | +3.0797 | 3.5129 | ±7.0258 | +0.877 | 0.3807 |  |
| Site: UW (vs UAB) | +0.4860 | 2.9061 | ±5.8121 | +0.167 | 0.8672 |  |
| Age (years) | -0.2172 | 0.1112 | ±0.2224 | -1.953 | 0.0508 | . |
| BMI (kg/m2) | +0.1314 | 0.2122 | ±0.4245 | +0.619 | 0.5359 |  |
| Hypertension | -4.0279 | 2.4980 | ±4.9961 | -1.612 | 0.1069 |  |
| High cholesterol | +4.0482 | 2.4792 | ±4.9584 | +1.633 | 0.1025 |  |
| Kidney disease | +2.6689 | 5.7661 | ±11.5322 | +0.463 | 0.6435 |  |
| Circulatory disease | -0.2954 | 4.7456 | ±9.4911 | -0.062 | 0.9504 |  |
| Avg. daily range (mg/dL) | +0.0535 | 0.0471 | ±0.0941 | +1.137 | 0.2556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **218**, R² = **0.0535**, Adj R² = **0.0029**, F-statistic = **1.06** (p = **0.3975**), Residual SE = **16.400** on **206** df, AIC = **1849.9**, BIC = **1890.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.4594** | 11.2083 | ±22.4166 | **+4.948** | **7.50e-07** | *** |
| Education: graduate level (vs college) | -0.7719 | 2.4282 | ±4.8564 | -0.318 | 0.7506 |  |
| Education: high school or below (vs college) | +2.0666 | 5.4563 | ±10.9126 | +0.379 | 0.7049 |  |
| Site: UCSD (vs UAB) | +2.8405 | 3.4859 | ±6.9718 | +0.815 | 0.4151 |  |
| Site: UW (vs UAB) | +0.1981 | 2.9021 | ±5.8042 | +0.068 | 0.9456 |  |
| **Age (years)** | **-0.2225** | 0.1112 | ±0.2224 | **-2.001** | **0.0454** | * |
| BMI (kg/m2) | +0.1433 | 0.2129 | ±0.4258 | +0.673 | 0.5008 |  |
| Hypertension | -3.8993 | 2.4812 | ±4.9625 | -1.572 | 0.1161 |  |
| High cholesterol | +3.5389 | 2.4165 | ±4.8331 | +1.464 | 0.1431 |  |
| Kidney disease | +2.8750 | 5.7985 | ±11.5969 | +0.496 | 0.6200 |  |
| Circulatory disease | +0.0645 | 4.7217 | ±9.4434 | +0.014 | 0.9891 |  |
| SD of daily means (mg/dL) | +0.2537 | 0.3123 | ±0.6247 | +0.812 | 0.4167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **218**, R² = **0.0567**, Adj R² = **0.0063**, F-statistic = **1.13** (p = **0.3428**), Residual SE = **16.372** on **206** df, AIC = **1849.2**, BIC = **1889.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4732** | 14.9329 | ±29.8658 | **+4.451** | **8.53e-06** | *** |
| Education: graduate level (vs college) | -0.9936 | 2.4228 | ±4.8456 | -0.410 | 0.6817 |  |
| Education: high school or below (vs college) | +1.7947 | 5.4314 | ±10.8628 | +0.330 | 0.7411 |  |
| Site: UCSD (vs UAB) | +2.8268 | 3.5351 | ±7.0702 | +0.800 | 0.4239 |  |
| Site: UW (vs UAB) | +0.2277 | 2.8904 | ±5.7809 | +0.079 | 0.9372 |  |
| Age (years) | -0.2130 | 0.1120 | ±0.2240 | -1.902 | 0.0572 | . |
| BMI (kg/m2) | +0.1060 | 0.2145 | ±0.4291 | +0.494 | 0.6211 |  |
| Hypertension | -4.0661 | 2.5136 | ±5.0273 | -1.618 | 0.1057 |  |
| High cholesterol | +3.4569 | 2.4311 | ±4.8622 | +1.422 | 0.1550 |  |
| Kidney disease | +2.6969 | 5.8338 | ±11.6676 | +0.462 | 0.6439 |  |
| Circulatory disease | -0.2524 | 4.6958 | ±9.3917 | -0.054 | 0.9571 |  |
| Time in range 70-180, pooled (%) | -0.0936 | 0.1117 | ±0.2233 | -0.838 | 0.4018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **218**, R² = **0.0560**, Adj R² = **0.0055**, F-statistic = **1.11** (p = **0.3548**), Residual SE = **16.378** on **206** df, AIC = **1849.3**, BIC = **1890.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0055** | 14.9216 | ±29.8431 | **+4.423** | **9.71e-06** | *** |
| Education: graduate level (vs college) | -1.0034 | 2.4244 | ±4.8488 | -0.414 | 0.6790 |  |
| Education: high school or below (vs college) | +1.8469 | 5.4423 | ±10.8846 | +0.339 | 0.7343 |  |
| Site: UCSD (vs UAB) | +2.8444 | 3.5363 | ±7.0726 | +0.804 | 0.4212 |  |
| Site: UW (vs UAB) | +0.2387 | 2.8922 | ±5.7845 | +0.083 | 0.9342 |  |
| Age (years) | -0.2138 | 0.1121 | ±0.2242 | -1.907 | 0.0565 | . |
| BMI (kg/m2) | +0.1075 | 0.2145 | ±0.4291 | +0.501 | 0.6164 |  |
| Hypertension | -4.0696 | 2.5147 | ±5.0294 | -1.618 | 0.1056 |  |
| High cholesterol | +3.4616 | 2.4310 | ±4.8619 | +1.424 | 0.1545 |  |
| Kidney disease | +2.7109 | 5.8362 | ±11.6723 | +0.465 | 0.6423 |  |
| Circulatory disease | -0.2261 | 4.7037 | ±9.4073 | -0.048 | 0.9617 |  |
| Avg. daily time in range 70-180 (%) | -0.0880 | 0.1100 | ±0.2200 | -0.800 | 0.4238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.0494**, Adj R² = **-0.0013**, F-statistic = **0.97** (p = **0.4718**), Residual SE = **16.435** on **206** df, AIC = **1850.9**, BIC = **1891.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.1816** | 10.6244 | ±21.2488 | **+5.382** | **7.36e-08** | *** |
| Education: graduate level (vs college) | -0.8711 | 2.4293 | ±4.8586 | -0.359 | 0.7199 |  |
| Education: high school or below (vs college) | +2.2082 | 5.6851 | ±11.3702 | +0.388 | 0.6977 |  |
| Site: UCSD (vs UAB) | +2.7714 | 3.4579 | ±6.9158 | +0.801 | 0.4229 |  |
| Site: UW (vs UAB) | +0.2573 | 2.8876 | ±5.7752 | +0.089 | 0.9290 |  |
| Age (years) | -0.2191 | 0.1121 | ±0.2242 | -1.954 | 0.0507 | . |
| BMI (kg/m2) | +0.1479 | 0.2119 | ±0.4238 | +0.698 | 0.4850 |  |
| Hypertension | -3.9820 | 2.5040 | ±5.0080 | -1.590 | 0.1118 |  |
| High cholesterol | +3.6634 | 2.4263 | ±4.8526 | +1.510 | 0.1311 |  |
| Kidney disease | +3.1689 | 5.8022 | ±11.6045 | +0.546 | 0.5850 |  |
| Circulatory disease | -0.0179 | 4.7859 | ±9.5718 | -0.004 | 0.9970 |  |
| Any reading < 54 during wear (0/1) | +0.3686 | 2.7229 | ±5.4458 | +0.135 | 0.8923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.0493**, Adj R² = **-0.0015**, F-statistic = **0.97** (p = **0.4736**), Residual SE = **16.436** on **206** df, AIC = **1850.9**, BIC = **1891.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2590** | 10.7225 | ±21.4449 | **+5.340** | **9.29e-08** | *** |
| Education: graduate level (vs college) | -0.9045 | 2.4222 | ±4.8445 | -0.373 | 0.7088 |  |
| Education: high school or below (vs college) | +2.1567 | 5.5981 | ±11.1963 | +0.385 | 0.7000 |  |
| Site: UCSD (vs UAB) | +2.7439 | 3.4820 | ±6.9641 | +0.788 | 0.4307 |  |
| Site: UW (vs UAB) | +0.2167 | 2.9299 | ±5.8598 | +0.074 | 0.9410 |  |
| Age (years) | -0.2186 | 0.1122 | ±0.2243 | -1.949 | 0.0513 | . |
| BMI (kg/m2) | +0.1502 | 0.2162 | ±0.4325 | +0.694 | 0.4874 |  |
| Hypertension | -3.9902 | 2.4984 | ±4.9968 | -1.597 | 0.1102 |  |
| High cholesterol | +3.6279 | 2.4487 | ±4.8975 | +1.482 | 0.1385 |  |
| Kidney disease | +3.1726 | 5.7624 | ±11.5248 | +0.551 | 0.5819 |  |
| Circulatory disease | +0.0120 | 4.7451 | ±9.4903 | +0.003 | 0.9980 |  |
| Time < 54 (%) | -0.0123 | 5.9323 | ±11.8646 | -0.002 | 0.9984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **218**, R² = **0.0493**, Adj R² = **-0.0014**, F-statistic = **0.97** (p = **0.4735**), Residual SE = **16.436** on **206** df, AIC = **1850.9**, BIC = **1891.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2279** | 10.7188 | ±21.4375 | **+5.339** | **9.34e-08** | *** |
| Education: graduate level (vs college) | -0.8929 | 2.4120 | ±4.8240 | -0.370 | 0.7113 |  |
| Education: high school or below (vs college) | +2.1720 | 5.5654 | ±11.1308 | +0.390 | 0.6963 |  |
| Site: UCSD (vs UAB) | +2.7585 | 3.4784 | ±6.9567 | +0.793 | 0.4277 |  |
| Site: UW (vs UAB) | +0.2387 | 2.9307 | ±5.8614 | +0.081 | 0.9351 |  |
| **Age (years)** | **-0.2190** | 0.1118 | ±0.2235 | **-1.960** | **0.0500** | * |
| BMI (kg/m2) | +0.1508 | 0.2151 | ±0.4301 | +0.701 | 0.4833 |  |
| Hypertension | -3.9833 | 2.4988 | ±4.9976 | -1.594 | 0.1109 |  |
| High cholesterol | +3.6418 | 2.4381 | ±4.8763 | +1.494 | 0.1353 |  |
| Kidney disease | +3.1750 | 5.7620 | ±11.5241 | +0.551 | 0.5816 |  |
| Circulatory disease | +0.0142 | 4.7460 | ±9.4920 | +0.003 | 0.9976 |  |
| Avg. daily time < 54 (%) | +0.0574 | 4.1563 | ±8.3127 | +0.014 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **218**, R² = **0.0560**, Adj R² = **0.0056**, F-statistic = **1.11** (p = **0.3537**), Residual SE = **16.378** on **206** df, AIC = **1849.3**, BIC = **1889.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7488** | 10.6265 | ±21.2530 | **+5.340** | **9.28e-08** | *** |
| Education: graduate level (vs college) | -0.5279 | 2.4019 | ±4.8038 | -0.220 | 0.8261 |  |
| Education: high school or below (vs college) | +2.6635 | 5.5535 | ±11.1069 | +0.480 | 0.6315 |  |
| Site: UCSD (vs UAB) | +3.0490 | 3.4363 | ±6.8726 | +0.887 | 0.3749 |  |
| Site: UW (vs UAB) | +0.7031 | 2.8935 | ±5.7871 | +0.243 | 0.8080 |  |
| **Age (years)** | **-0.2227** | 0.1116 | ±0.2232 | **-1.995** | **0.0460** | * |
| BMI (kg/m2) | +0.1331 | 0.2081 | ±0.4163 | +0.639 | 0.5226 |  |
| Hypertension | -3.8370 | 2.5316 | ±5.0632 | -1.516 | 0.1296 |  |
| High cholesterol | +4.0565 | 2.4389 | ±4.8779 | +1.663 | 0.0963 | . |
| Kidney disease | +3.1657 | 5.8573 | ±11.7146 | +0.540 | 0.5889 |  |
| Circulatory disease | +0.0271 | 4.7745 | ±9.5490 | +0.006 | 0.9955 |  |
| Time 54-69, pooled (%) | +1.0463 | 2.0575 | ±4.1150 | +0.509 | 0.6111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **218**, R² = **0.0561**, Adj R² = **0.0057**, F-statistic = **1.11** (p = **0.3525**), Residual SE = **16.377** on **206** df, AIC = **1849.3**, BIC = **1889.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7619** | 10.6253 | ±21.2506 | **+5.342** | **9.19e-08** | *** |
| Education: graduate level (vs college) | -0.5176 | 2.4057 | ±4.8114 | -0.215 | 0.8297 |  |
| Education: high school or below (vs college) | +2.7107 | 5.5410 | ±11.0820 | +0.489 | 0.6247 |  |
| Site: UCSD (vs UAB) | +3.0643 | 3.4390 | ±6.8779 | +0.891 | 0.3729 |  |
| Site: UW (vs UAB) | +0.7547 | 2.8972 | ±5.7943 | +0.260 | 0.7945 |  |
| **Age (years)** | **-0.2240** | 0.1120 | ±0.2240 | **-2.000** | **0.0455** | * |
| BMI (kg/m2) | +0.1357 | 0.2083 | ±0.4165 | +0.652 | 0.5146 |  |
| Hypertension | -3.8279 | 2.5340 | ±5.0680 | -1.511 | 0.1309 |  |
| High cholesterol | +4.0867 | 2.4511 | ±4.9022 | +1.667 | 0.0955 | . |
| Kidney disease | +3.1642 | 5.8369 | ±11.6738 | +0.542 | 0.5877 |  |
| Circulatory disease | +0.0577 | 4.7604 | ±9.5209 | +0.012 | 0.9903 |  |
| Avg. daily time 54-69 (%) | +1.0021 | 1.9858 | ±3.9715 | +0.505 | 0.6138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **218**, R² = **0.0523**, Adj R² = **0.0017**, F-statistic = **1.03** (p = **0.4185**), Residual SE = **16.410** on **206** df, AIC = **1850.2**, BIC = **1890.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7425** | 10.6825 | ±21.3650 | **+5.312** | **1.09e-07** | *** |
| Education: graduate level (vs college) | -0.6338 | 2.4027 | ±4.8053 | -0.264 | 0.7919 |  |
| Education: high school or below (vs college) | +2.5059 | 5.5591 | ±11.1182 | +0.451 | 0.6521 |  |
| Site: UCSD (vs UAB) | +2.9986 | 3.4482 | ±6.8965 | +0.870 | 0.3845 |  |
| Site: UW (vs UAB) | +0.5990 | 2.9010 | ±5.8020 | +0.206 | 0.8364 |  |
| **Age (years)** | **-0.2240** | 0.1120 | ±0.2241 | **-1.999** | **0.0456** | * |
| BMI (kg/m2) | +0.1491 | 0.2134 | ±0.4269 | +0.699 | 0.4848 |  |
| Hypertension | -3.8655 | 2.5171 | ±5.0342 | -1.536 | 0.1246 |  |
| High cholesterol | +3.9168 | 2.4237 | ±4.8474 | +1.616 | 0.1061 |  |
| Kidney disease | +3.1930 | 5.8093 | ±11.6186 | +0.550 | 0.5826 |  |
| Circulatory disease | +0.0388 | 4.7641 | ±9.5282 | +0.008 | 0.9935 |  |
| Time < 70 (%) | +0.4647 | 1.1258 | ±2.2515 | +0.413 | 0.6797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **218**, R² = **0.0530**, Adj R² = **0.0024**, F-statistic = **1.05** (p = **0.4062**), Residual SE = **16.404** on **206** df, AIC = **1850.0**, BIC = **1890.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7754** | 10.6723 | ±21.3446 | **+5.320** | **1.04e-07** | *** |
| Education: graduate level (vs college) | -0.6162 | 2.4033 | ±4.8066 | -0.256 | 0.7976 |  |
| Education: high school or below (vs college) | +2.5624 | 5.5469 | ±11.0938 | +0.462 | 0.6441 |  |
| Site: UCSD (vs UAB) | +3.0210 | 3.4497 | ±6.8995 | +0.876 | 0.3812 |  |
| Site: UW (vs UAB) | +0.6653 | 2.9075 | ±5.8150 | +0.229 | 0.8190 |  |
| **Age (years)** | **-0.2246** | 0.1123 | ±0.2246 | **-1.999** | **0.0456** | * |
| BMI (kg/m2) | +0.1466 | 0.2118 | ±0.4237 | +0.692 | 0.4889 |  |
| Hypertension | -3.8538 | 2.5245 | ±5.0490 | -1.527 | 0.1269 |  |
| High cholesterol | +3.9763 | 2.4380 | ±4.8761 | +1.631 | 0.1029 |  |
| Kidney disease | +3.1848 | 5.8045 | ±11.6090 | +0.549 | 0.5832 |  |
| Circulatory disease | +0.0514 | 4.7593 | ±9.5187 | +0.011 | 0.9914 |  |
| Avg. daily time < 70 (%) | +0.5296 | 1.2203 | ±2.4405 | +0.434 | 0.6643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.0549**, Adj R² = **0.0044**, F-statistic = **1.09** (p = **0.3733**), Residual SE = **16.388** on **206** df, AIC = **1849.6**, BIC = **1890.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3111** | 23.0670 | ±46.1340 | **+3.005** | **0.0027** | ** |
| Education: graduate level (vs college) | -0.8366 | 2.4403 | ±4.8806 | -0.343 | 0.7317 |  |
| Education: high school or below (vs college) | +1.7044 | 5.5574 | ±11.1149 | +0.307 | 0.7591 |  |
| Site: UCSD (vs UAB) | +2.7851 | 3.5445 | ±7.0891 | +0.786 | 0.4320 |  |
| Site: UW (vs UAB) | +0.2787 | 2.9132 | ±5.8265 | +0.096 | 0.9238 |  |
| Age (years) | -0.2131 | 0.1126 | ±0.2251 | -1.893 | 0.0583 | . |
| BMI (kg/m2) | +0.1389 | 0.2126 | ±0.4252 | +0.653 | 0.5136 |  |
| Hypertension | -3.8239 | 2.5497 | ±5.0993 | -1.500 | 0.1337 |  |
| High cholesterol | +3.6290 | 2.4417 | ±4.8833 | +1.486 | 0.1372 |  |
| Kidney disease | +3.1614 | 5.8266 | ±11.6532 | +0.543 | 0.5874 |  |
| Circulatory disease | -0.3738 | 4.7426 | ±9.4852 | -0.079 | 0.9372 |  |
| Time 54-250, pooled (%) | -0.1246 | 0.2118 | ±0.4237 | -0.588 | 0.5564 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **218**, R² = **0.0549**, Adj R² = **0.0044**, F-statistic = **1.09** (p = **0.3733**), Residual SE = **16.388** on **206** df, AIC = **1849.6**, BIC = **1890.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.8528** | 23.9682 | ±47.9364 | **+2.914** | **0.0036** | ** |
| Education: graduate level (vs college) | -0.8451 | 2.4413 | ±4.8826 | -0.346 | 0.7292 |  |
| Education: high school or below (vs college) | +1.7020 | 5.5564 | ±11.1128 | +0.306 | 0.7594 |  |
| Site: UCSD (vs UAB) | +2.7780 | 3.5436 | ±7.0872 | +0.784 | 0.4331 |  |
| Site: UW (vs UAB) | +0.2592 | 2.9120 | ±5.8239 | +0.089 | 0.9291 |  |
| Age (years) | -0.2130 | 0.1126 | ±0.2251 | -1.892 | 0.0585 | . |
| BMI (kg/m2) | +0.1364 | 0.2127 | ±0.4254 | +0.642 | 0.5212 |  |
| Hypertension | -3.8230 | 2.5535 | ±5.1071 | -1.497 | 0.1344 |  |
| High cholesterol | +3.6270 | 2.4429 | ±4.8857 | +1.485 | 0.1376 |  |
| Kidney disease | +3.1653 | 5.8267 | ±11.6533 | +0.543 | 0.5870 |  |
| Circulatory disease | -0.3766 | 4.7432 | ±9.4863 | -0.079 | 0.9367 |  |
| Avg. daily time 54-250 (%) | -0.1292 | 0.2209 | ±0.4418 | -0.585 | 0.5587 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.0519**, Adj R² = **0.0012**, F-statistic = **1.02** (p = **0.4262**), Residual SE = **16.414** on **206** df, AIC = **1850.3**, BIC = **1890.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.4532** | 10.6633 | ±21.3266 | **+5.388** | **7.13e-08** | *** |
| Education: graduate level (vs college) | -1.0710 | 2.4154 | ±4.8307 | -0.443 | 0.6575 |  |
| Education: high school or below (vs college) | +2.0938 | 5.5428 | ±11.0856 | +0.378 | 0.7056 |  |
| Site: UCSD (vs UAB) | +2.7705 | 3.5029 | ±7.0057 | +0.791 | 0.4290 |  |
| Site: UW (vs UAB) | +0.1436 | 2.8876 | ±5.7753 | +0.050 | 0.9603 |  |
| Age (years) | -0.2169 | 0.1117 | ±0.2235 | -1.941 | 0.0522 | . |
| BMI (kg/m2) | +0.1172 | 0.2154 | ±0.4308 | +0.544 | 0.5864 |  |
| Hypertension | -4.1972 | 2.5411 | ±5.0823 | -1.652 | 0.0986 | . |
| High cholesterol | +3.4260 | 2.4005 | ±4.8009 | +1.427 | 0.1535 |  |
| Kidney disease | +2.7200 | 5.7787 | ±11.5574 | +0.471 | 0.6379 |  |
| Circulatory disease | +0.0359 | 4.7475 | ±9.4950 | +0.008 | 0.9940 |  |
| Time 181-250, pooled (%) | +0.0909 | 0.1532 | ±0.3064 | +0.593 | 0.5530 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **218**, R² = **0.0514**, Adj R² = **0.0007**, F-statistic = **1.01** (p = **0.4349**), Residual SE = **16.418** on **206** df, AIC = **1850.4**, BIC = **1891.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.4463** | 10.6630 | ±21.3260 | **+5.387** | **7.15e-08** | *** |
| Education: graduate level (vs college) | -1.0594 | 2.4176 | ±4.8353 | -0.438 | 0.6612 |  |
| Education: high school or below (vs college) | +2.1151 | 5.5398 | ±11.0795 | +0.382 | 0.7026 |  |
| Site: UCSD (vs UAB) | +2.7909 | 3.5111 | ±7.0221 | +0.795 | 0.4267 |  |
| Site: UW (vs UAB) | +0.1711 | 2.8929 | ±5.7858 | +0.059 | 0.9528 |  |
| Age (years) | -0.2174 | 0.1119 | ±0.2237 | -1.943 | 0.0520 | . |
| BMI (kg/m2) | +0.1212 | 0.2154 | ±0.4307 | +0.563 | 0.5734 |  |
| Hypertension | -4.1770 | 2.5413 | ±5.0826 | -1.644 | 0.1002 |  |
| High cholesterol | +3.4434 | 2.3977 | ±4.7955 | +1.436 | 0.1510 |  |
| Kidney disease | +2.7601 | 5.7790 | ±11.5580 | +0.478 | 0.6329 |  |
| Circulatory disease | +0.0328 | 4.7503 | ±9.5007 | +0.007 | 0.9945 |  |
| Avg. daily time 181-250 (%) | +0.0797 | 0.1474 | ±0.2949 | +0.541 | 0.5888 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **218**, R² = **0.0555**, Adj R² = **0.0050**, F-statistic = **1.10** (p = **0.3627**), Residual SE = **16.382** on **206** df, AIC = **1849.5**, BIC = **1890.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2178** | 10.7110 | ±21.4220 | **+5.342** | **9.19e-08** | *** |
| Education: graduate level (vs college) | -1.0343 | 2.4245 | ±4.8489 | -0.427 | 0.6697 |  |
| Education: high school or below (vs college) | +1.7645 | 5.4499 | ±10.8997 | +0.324 | 0.7461 |  |
| Site: UCSD (vs UAB) | +2.7735 | 3.5233 | ±7.0466 | +0.787 | 0.4312 |  |
| Site: UW (vs UAB) | +0.1579 | 2.8882 | ±5.7763 | +0.055 | 0.9564 |  |
| Age (years) | -0.2125 | 0.1121 | ±0.2242 | -1.896 | 0.0580 | . |
| BMI (kg/m2) | +0.1103 | 0.2152 | ±0.4305 | +0.512 | 0.6084 |  |
| Hypertension | -4.0816 | 2.5181 | ±5.0362 | -1.621 | 0.1050 |  |
| High cholesterol | +3.4202 | 2.4282 | ±4.8563 | +1.409 | 0.1590 |  |
| Kidney disease | +2.7365 | 5.8245 | ±11.6490 | +0.470 | 0.6385 |  |
| Circulatory disease | -0.2332 | 4.7039 | ±9.4078 | -0.050 | 0.9605 |  |
| Time > 180 (%) | +0.0851 | 0.1116 | ±0.2232 | +0.763 | 0.4457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **218**, R² = **0.0547**, Adj R² = **0.0043**, F-statistic = **1.08** (p = **0.3750**), Residual SE = **16.389** on **206** df, AIC = **1849.6**, BIC = **1890.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2831** | 10.7057 | ±21.4115 | **+5.351** | **8.76e-08** | *** |
| Education: graduate level (vs college) | -1.0360 | 2.4261 | ±4.8522 | -0.427 | 0.6694 |  |
| Education: high school or below (vs college) | +1.8178 | 5.4619 | ±10.9239 | +0.333 | 0.7393 |  |
| Site: UCSD (vs UAB) | +2.7937 | 3.5260 | ±7.0520 | +0.792 | 0.4282 |  |
| Site: UW (vs UAB) | +0.1705 | 2.8912 | ±5.7825 | +0.059 | 0.9530 |  |
| Age (years) | -0.2134 | 0.1122 | ±0.2244 | -1.902 | 0.0572 | . |
| BMI (kg/m2) | +0.1123 | 0.2153 | ±0.4306 | +0.522 | 0.6019 |  |
| Hypertension | -4.0817 | 2.5195 | ±5.0391 | -1.620 | 0.1052 |  |
| High cholesterol | +3.4267 | 2.4274 | ±4.8548 | +1.412 | 0.1581 |  |
| Kidney disease | +2.7552 | 5.8274 | ±11.6549 | +0.473 | 0.6364 |  |
| Circulatory disease | -0.2082 | 4.7132 | ±9.4264 | -0.044 | 0.9648 |  |
| Avg. daily time > 180 (%) | +0.0792 | 0.1100 | ±0.2200 | +0.720 | 0.4713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **218**, R² = **0.0498**, Adj R² = **-0.0009**, F-statistic = **0.98** (p = **0.4637**), Residual SE = **16.431** on **206** df, AIC = **1850.8**, BIC = **1891.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.1728** | 10.6796 | ±21.3593 | **+5.353** | **8.63e-08** | *** |
| Education: graduate level (vs college) | -0.9208 | 2.4183 | ±4.8365 | -0.381 | 0.7034 |  |
| Education: high school or below (vs college) | +2.1708 | 5.7927 | ±11.5854 | +0.375 | 0.7079 |  |
| Site: UCSD (vs UAB) | +2.7459 | 3.4965 | ±6.9930 | +0.785 | 0.4323 |  |
| Site: UW (vs UAB) | +0.2190 | 2.9274 | ±5.8548 | +0.075 | 0.9404 |  |
| Age (years) | -0.2216 | 0.1131 | ±0.2262 | -1.960 | 0.0500 | . |
| BMI (kg/m2) | +0.1648 | 0.2243 | ±0.4487 | +0.735 | 0.4625 |  |
| Hypertension | -3.9909 | 2.5313 | ±5.0625 | -1.577 | 0.1149 |  |
| High cholesterol | +3.7091 | 2.4237 | ±4.8473 | +1.530 | 0.1259 |  |
| Kidney disease | +3.1391 | 5.8238 | ±11.6476 | +0.539 | 0.5899 |  |
| Circulatory disease | +0.0780 | 4.8757 | ±9.7515 | +0.016 | 0.9872 |  |
| Nocturnal time > 180 (%) | -0.0238 | 0.1182 | ±0.2363 | -0.201 | 0.8404 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **218**, R² = **0.0549**, Adj R² = **0.0044**, F-statistic = **1.09** (p = **0.3723**), Residual SE = **16.387** on **206** df, AIC = **1849.6**, BIC = **1890.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9227** | 10.7373 | ±21.4747 | **+5.301** | **1.15e-07** | *** |
| Education: graduate level (vs college) | -0.8636 | 2.4378 | ±4.8756 | -0.354 | 0.7232 |  |
| Education: high school or below (vs college) | +1.6671 | 5.5625 | ±11.1250 | +0.300 | 0.7644 |  |
| Site: UCSD (vs UAB) | +2.7536 | 3.5384 | ±7.0768 | +0.778 | 0.4364 |  |
| Site: UW (vs UAB) | +0.2349 | 2.9099 | ±5.8198 | +0.081 | 0.9357 |  |
| Age (years) | -0.2121 | 0.1126 | ±0.2253 | -1.883 | 0.0597 | . |
| BMI (kg/m2) | +0.1370 | 0.2126 | ±0.4252 | +0.645 | 0.5192 |  |
| Hypertension | -3.8375 | 2.5481 | ±5.0962 | -1.506 | 0.1321 |  |
| High cholesterol | +3.6027 | 2.4427 | ±4.8855 | +1.475 | 0.1402 |  |
| Kidney disease | +3.1551 | 5.8261 | ±11.6521 | +0.542 | 0.5881 |  |
| Circulatory disease | -0.3827 | 4.7416 | ±9.4832 | -0.081 | 0.9357 |  |
| Time > 250 (%) | +0.1258 | 0.2141 | ±0.4281 | +0.587 | 0.5569 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 218)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **218**, R² = **0.0548**, Adj R² = **0.0044**, F-statistic = **1.09** (p = **0.3734**), Residual SE = **16.388** on **206** df, AIC = **1849.6**, BIC = **1890.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9866** | 10.7373 | ±21.4747 | **+5.307** | **1.11e-07** | *** |
| Education: graduate level (vs college) | -0.8652 | 2.4394 | ±4.8788 | -0.355 | 0.7228 |  |
| Education: high school or below (vs college) | +1.6739 | 5.5617 | ±11.1235 | +0.301 | 0.7634 |  |
| Site: UCSD (vs UAB) | +2.7521 | 3.5385 | ±7.0770 | +0.778 | 0.4367 |  |
| Site: UW (vs UAB) | +0.2196 | 2.9101 | ±5.8201 | +0.075 | 0.9398 |  |
| Age (years) | -0.2122 | 0.1126 | ±0.2252 | -1.884 | 0.0595 | . |
| BMI (kg/m2) | +0.1354 | 0.2128 | ±0.4255 | +0.637 | 0.5244 |  |
| Hypertension | -3.8349 | 2.5520 | ±5.1040 | -1.503 | 0.1329 |  |
| High cholesterol | +3.6014 | 2.4441 | ±4.8882 | +1.473 | 0.1406 |  |
| Kidney disease | +3.1613 | 5.8264 | ±11.6528 | +0.543 | 0.5874 |  |
| Circulatory disease | -0.3810 | 4.7422 | ±9.4844 | -0.080 | 0.9360 |  |
| Avg. daily time > 250 (%) | +0.1294 | 0.2225 | ±0.4451 | +0.582 | 0.5608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 6 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 218): best single predictor out of sample is **%<70 (pooled)** (CV R² -0.019 vs -0.017 for covariates alone, gain -0.002; -150 per SD, p = 0.371). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 218): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.024 vs 0.028 for covariates alone, gain -0.004; -0.46 per SD, p = 0.446). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 218): best single predictor out of sample is **SD of daily means** (CV R² -0.058 vs -0.079 for covariates alone, gain +0.021; +1.38 per SD, p = 0.011). Raw p < 0.05 (FDR not applicable here): SD of daily means (p = 0.011), HbA1c (p = 0.035), SD (pooled) (p = 0.049).
- **Total sleep time per night (min)** (n = 215): best single predictor out of sample is **MAG** (CV R² -0.068 vs -0.109 for covariates alone, gain +0.041; -15.1 per SD, p = 6.3e-04). Raw p < 0.05 (FDR not applicable here): MAG (p = 6.3e-04), Mean/SD (daily avg) (p = 0.011).
- **Garmin stress score, mean (0-100)** (n = 218): best single predictor out of sample is **HbA1c** (CV R² -0.093 vs -0.108 for covariates alone, gain +0.015; +2.65 per SD, p = 0.022). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 0.022).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.041, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.021, via SD of daily means); Garmin stress score, mean (0-100) (+0.015, via HbA1c); Steps per wear-day (-0.002, via %<70 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 4 raw-significant of 40); HbA1c (0 FDR-significant / 2 raw-significant of 5); CGM level (0 FDR-significant / 0 raw-significant of 15).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (4 raw); HbA1c alone: 0 FDR-significant (2 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Resting heart-rate proxy (SD of daily means, ΔAIC -3.0); Total sleep time per night (MAG, ΔAIC -9.0).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
