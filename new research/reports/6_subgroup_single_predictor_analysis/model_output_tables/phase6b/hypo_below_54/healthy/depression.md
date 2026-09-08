# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 408; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **408**, R² = **0.1331**, Adj R² = **0.1113**, F-statistic = **6.10** (p = **1.18e-08**), Residual SE = **4.896** on **397** df, AIC = **2464.8**, BIC = **2509.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4608** | 2.0242 | ±4.0484 | **+3.192** | **0.0014** | ** |
| **Education: graduate level (vs college)** | **-1.0510** | 0.5249 | ±1.0498 | **-2.002** | **0.0453** | * |
| Education: high school or below (vs college) | +1.8383 | 1.2721 | ±2.5442 | +1.445 | 0.1484 |  |
| Site: UCSD (vs UAB) | +0.5668 | 0.6765 | ±1.3531 | +0.838 | 0.4022 |  |
| Site: UW (vs UAB) | +0.9264 | 0.5938 | ±1.1875 | +1.560 | 0.1187 |  |
| **Age (years)** | **-0.0939** | 0.0231 | ±0.0462 | **-4.060** | **4.91e-05** | *** |
| **BMI (kg/m2)** | **+0.1429** | 0.0464 | ±0.0928 | **+3.079** | **0.0021** | ** |
| Hypertension | -0.0422 | 0.5931 | ±1.1863 | -0.071 | 0.9433 |  |
| High cholesterol | +0.5101 | 0.5254 | ±1.0508 | +0.971 | 0.3316 |  |
| Kidney disease | +0.2630 | 1.0876 | ±2.1752 | +0.242 | 0.8089 |  |
| Circulatory disease | +0.9974 | 0.8060 | ±1.6120 | +1.238 | 0.2159 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **408**, R² = **0.1336**, Adj R² = **0.1095**, F-statistic = **5.55** (p = **2.79e-08**), Residual SE = **4.901** on **396** df, AIC = **2466.6**, BIC = **2514.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.1041 | 4.2023 | ±8.4046 | +1.215 | 0.2245 |  |
| **Education: graduate level (vs college)** | **-1.0392** | 0.5225 | ±1.0450 | **-1.989** | **0.0467** | * |
| Education: high school or below (vs college) | +1.8089 | 1.2806 | ±2.5613 | +1.412 | 0.1578 |  |
| Site: UCSD (vs UAB) | +0.5252 | 0.6779 | ±1.3559 | +0.775 | 0.4385 |  |
| Site: UW (vs UAB) | +0.9164 | 0.5963 | ±1.1926 | +1.537 | 0.1243 |  |
| **Age (years)** | **-0.0957** | 0.0239 | ±0.0477 | **-4.009** | **6.09e-05** | *** |
| **BMI (kg/m2)** | **+0.1405** | 0.0460 | ±0.0920 | **+3.054** | **0.0023** | ** |
| Hypertension | -0.0371 | 0.5975 | ±1.1951 | -0.062 | 0.9504 |  |
| High cholesterol | +0.4729 | 0.5449 | ±1.0897 | +0.868 | 0.3855 |  |
| Kidney disease | +0.2498 | 1.0955 | ±2.1909 | +0.228 | 0.8196 |  |
| Circulatory disease | +1.0143 | 0.8118 | ±1.6236 | +1.249 | 0.2115 |  |
| HbA1c (%) | +0.2767 | 0.7299 | ±1.4599 | +0.379 | 0.7047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **408**, R² = **0.1334**, Adj R² = **0.1093**, F-statistic = **5.54** (p = **2.90e-08**), Residual SE = **4.901** on **396** df, AIC = **2466.7**, BIC = **2514.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.8315 | 3.0485 | ±6.0970 | +1.913 | 0.0558 | . |
| **Education: graduate level (vs college)** | **-1.0611** | 0.5304 | ±1.0607 | **-2.001** | **0.0454** | * |
| Education: high school or below (vs college) | +1.8128 | 1.2860 | ±2.5719 | +1.410 | 0.1586 |  |
| Site: UCSD (vs UAB) | +0.5605 | 0.6789 | ±1.3577 | +0.826 | 0.4090 |  |
| Site: UW (vs UAB) | +0.9049 | 0.6005 | ±1.2011 | +1.507 | 0.1318 |  |
| **Age (years)** | **-0.0944** | 0.0232 | ±0.0465 | **-4.063** | **4.84e-05** | *** |
| **BMI (kg/m2)** | **+0.1423** | 0.0465 | ±0.0929 | **+3.062** | **0.0022** | ** |
| Hypertension | -0.0589 | 0.5995 | ±1.1990 | -0.098 | 0.9217 |  |
| High cholesterol | +0.4919 | 0.5295 | ±1.0591 | +0.929 | 0.3529 |  |
| Kidney disease | +0.2250 | 1.1019 | ±2.2037 | +0.204 | 0.8382 |  |
| Circulatory disease | +1.0020 | 0.8092 | ±1.6183 | +1.238 | 0.2156 |  |
| Mean glucose (mg/dL) | +0.0062 | 0.0222 | ±0.0443 | +0.281 | 0.7791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **408**, R² = **0.1334**, Adj R² = **0.1093**, F-statistic = **5.54** (p = **2.90e-08**), Residual SE = **4.901** on **396** df, AIC = **2466.7**, BIC = **2514.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9706 | 5.7167 | ±11.4333 | +0.869 | 0.3846 |  |
| **Education: graduate level (vs college)** | **-1.0611** | 0.5304 | ±1.0607 | **-2.001** | **0.0454** | * |
| Education: high school or below (vs college) | +1.8128 | 1.2860 | ±2.5719 | +1.410 | 0.1586 |  |
| Site: UCSD (vs UAB) | +0.5605 | 0.6789 | ±1.3577 | +0.826 | 0.4090 |  |
| Site: UW (vs UAB) | +0.9049 | 0.6005 | ±1.2011 | +1.507 | 0.1318 |  |
| **Age (years)** | **-0.0944** | 0.0232 | ±0.0465 | **-4.063** | **4.84e-05** | *** |
| **BMI (kg/m2)** | **+0.1423** | 0.0465 | ±0.0929 | **+3.062** | **0.0022** | ** |
| Hypertension | -0.0589 | 0.5995 | ±1.1990 | -0.098 | 0.9217 |  |
| High cholesterol | +0.4919 | 0.5295 | ±1.0591 | +0.929 | 0.3529 |  |
| Kidney disease | +0.2250 | 1.1019 | ±2.2037 | +0.204 | 0.8382 |  |
| Circulatory disease | +1.0020 | 0.8092 | ±1.6183 | +1.238 | 0.2156 |  |
| GMI (%) | +0.2601 | 0.9270 | ±1.8540 | +0.281 | 0.7791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **408**, R² = **0.1331**, Adj R² = **0.1091**, F-statistic = **5.53** (p = **3.04e-08**), Residual SE = **4.902** on **396** df, AIC = **2466.8**, BIC = **2515.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.2801** | 2.8235 | ±5.6470 | **+2.224** | **0.0261** | * |
| **Education: graduate level (vs college)** | **-1.0529** | 0.5289 | ±1.0577 | **-1.991** | **0.0465** | * |
| Education: high school or below (vs college) | +1.8286 | 1.2881 | ±2.5761 | +1.420 | 0.1557 |  |
| Site: UCSD (vs UAB) | +0.5635 | 0.6788 | ±1.3575 | +0.830 | 0.4064 |  |
| Site: UW (vs UAB) | +0.9213 | 0.5962 | ±1.1923 | +1.545 | 0.1223 |  |
| **Age (years)** | **-0.0938** | 0.0232 | ±0.0463 | **-4.050** | **5.13e-05** | *** |
| **BMI (kg/m2)** | **+0.1423** | 0.0471 | ±0.0941 | **+3.025** | **0.0025** | ** |
| Hypertension | -0.0470 | 0.5952 | ±1.1905 | -0.079 | 0.9371 |  |
| High cholesterol | +0.5031 | 0.5293 | ±1.0586 | +0.951 | 0.3418 |  |
| Kidney disease | +0.2603 | 1.0968 | ±2.1937 | +0.237 | 0.8124 |  |
| Circulatory disease | +1.0010 | 0.8092 | ±1.6184 | +1.237 | 0.2160 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0018 | 0.0201 | ±0.0402 | +0.089 | 0.9287 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1369**, Adj R² = **0.1129**, F-statistic = **5.71** (p = **1.46e-08**), Residual SE = **4.891** on **396** df, AIC = **2465.1**, BIC = **2513.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.6993** | 2.1122 | ±4.2243 | **+2.698** | **0.0070** | ** |
| **Education: graduate level (vs college)** | **-1.0777** | 0.5241 | ±1.0483 | **-2.056** | **0.0398** | * |
| Education: high school or below (vs college) | +1.8297 | 1.2669 | ±2.5337 | +1.444 | 0.1487 |  |
| Site: UCSD (vs UAB) | +0.5162 | 0.6812 | ±1.3625 | +0.758 | 0.4486 |  |
| Site: UW (vs UAB) | +0.9008 | 0.5968 | ±1.1936 | +1.509 | 0.1312 |  |
| **Age (years)** | **-0.0984** | 0.0233 | ±0.0466 | **-4.224** | **2.40e-05** | *** |
| **BMI (kg/m2)** | **+0.1415** | 0.0462 | ±0.0923 | **+3.064** | **0.0022** | ** |
| Hypertension | -0.0840 | 0.5964 | ±1.1928 | -0.141 | 0.8880 |  |
| High cholesterol | +0.5361 | 0.5265 | ±1.0531 | +1.018 | 0.3086 |  |
| Kidney disease | +0.0544 | 1.0904 | ±2.1809 | +0.050 | 0.9602 |  |
| Circulatory disease | +1.0106 | 0.8095 | ±1.6191 | +1.248 | 0.2119 |  |
| Glucose SD, pooled (mg/dL) | +0.0511 | 0.0399 | ±0.0797 | +1.281 | 0.2001 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1372**, Adj R² = **0.1133**, F-statistic = **5.73** (p = **1.36e-08**), Residual SE = **4.890** on **396** df, AIC = **2464.9**, BIC = **2513.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.7433** | 2.1110 | ±4.2220 | **+2.721** | **0.0065** | ** |
| **Education: graduate level (vs college)** | **-1.0694** | 0.5241 | ±1.0482 | **-2.041** | **0.0413** | * |
| Education: high school or below (vs college) | +1.8086 | 1.2614 | ±2.5227 | +1.434 | 0.1516 |  |
| Site: UCSD (vs UAB) | +0.5021 | 0.6842 | ±1.3685 | +0.734 | 0.4630 |  |
| Site: UW (vs UAB) | +0.8899 | 0.5984 | ±1.1968 | +1.487 | 0.1370 |  |
| **Age (years)** | **-0.0992** | 0.0233 | ±0.0467 | **-4.252** | **2.12e-05** | *** |
| **BMI (kg/m2)** | **+0.1410** | 0.0461 | ±0.0922 | **+3.060** | **0.0022** | ** |
| Hypertension | -0.0801 | 0.5972 | ±1.1943 | -0.134 | 0.8933 |  |
| High cholesterol | +0.5274 | 0.5260 | ±1.0520 | +1.003 | 0.3160 |  |
| Kidney disease | +0.0294 | 1.0897 | ±2.1794 | +0.027 | 0.9785 |  |
| Circulatory disease | +1.0170 | 0.8085 | ±1.6170 | +1.258 | 0.2084 |  |
| Avg. daily SD (mg/dL) | +0.0584 | 0.0463 | ±0.0926 | +1.261 | 0.2073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **408**, R² = **0.1362**, Adj R² = **0.1122**, F-statistic = **5.68** (p = **1.67e-08**), Residual SE = **4.893** on **396** df, AIC = **2465.4**, BIC = **2513.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.4743** | 2.1800 | ±4.3599 | **+2.511** | **0.0120** | * |
| **Education: graduate level (vs college)** | **-1.0614** | 0.5237 | ±1.0473 | **-2.027** | **0.0427** | * |
| Education: high school or below (vs college) | +1.8712 | 1.2685 | ±2.5371 | +1.475 | 0.1402 |  |
| Site: UCSD (vs UAB) | +0.5265 | 0.6813 | ±1.3625 | +0.773 | 0.4396 |  |
| Site: UW (vs UAB) | +0.9414 | 0.5922 | ±1.1844 | +1.590 | 0.1119 |  |
| **Age (years)** | **-0.0978** | 0.0233 | ±0.0466 | **-4.201** | **2.66e-05** | *** |
| **BMI (kg/m2)** | **+0.1425** | 0.0463 | ±0.0926 | **+3.078** | **0.0021** | ** |
| Hypertension | -0.0566 | 0.5945 | ±1.1889 | -0.095 | 0.9242 |  |
| High cholesterol | +0.5696 | 0.5280 | ±1.0559 | +1.079 | 0.2807 |  |
| Kidney disease | +0.1138 | 1.0854 | ±2.1708 | +0.105 | 0.9165 |  |
| Circulatory disease | +1.0048 | 0.8077 | ±1.6154 | +1.244 | 0.2135 |  |
| CV (%) | +0.0642 | 0.0502 | ±0.1004 | +1.278 | 0.2012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **408**, R² = **0.1390**, Adj R² = **0.1151**, F-statistic = **5.81** (p = **9.48e-09**), Residual SE = **4.885** on **396** df, AIC = **2464.0**, BIC = **2512.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.8903** | 2.3974 | ±4.7948 | **+3.708** | **2.09e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0986** | 0.5217 | ±1.0434 | **-2.106** | **0.0352** | * |
| Education: high school or below (vs college) | +1.8460 | 1.2591 | ±2.5181 | +1.466 | 0.1426 |  |
| Site: UCSD (vs UAB) | +0.5036 | 0.6831 | ±1.3662 | +0.737 | 0.4610 |  |
| Site: UW (vs UAB) | +0.9126 | 0.5945 | ±1.1891 | +1.535 | 0.1248 |  |
| **Age (years)** | **-0.0997** | 0.0232 | ±0.0465 | **-4.291** | **1.78e-05** | *** |
| **BMI (kg/m2)** | **+0.1414** | 0.0460 | ±0.0920 | **+3.072** | **0.0021** | ** |
| Hypertension | -0.0616 | 0.5949 | ±1.1898 | -0.104 | 0.9175 |  |
| High cholesterol | +0.5648 | 0.5264 | ±1.0528 | +1.073 | 0.2833 |  |
| Kidney disease | +0.0809 | 1.0822 | ±2.1645 | +0.075 | 0.9404 |  |
| Circulatory disease | +0.9954 | 0.8063 | ±1.6125 | +1.235 | 0.2170 |  |
| Mean / SD ratio | -0.3659 | 0.2162 | ±0.4324 | -1.692 | 0.0906 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1370**, Adj R² = **0.1130**, F-statistic = **5.71** (p = **1.43e-08**), Residual SE = **4.891** on **396** df, AIC = **2465.0**, BIC = **2513.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4011** | 2.4168 | ±4.8337 | **+3.476** | **5.09e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0890** | 0.5236 | ±1.0472 | **-2.080** | **0.0375** | * |
| Education: high school or below (vs college) | +1.7980 | 1.2565 | ±2.5131 | +1.431 | 0.1525 |  |
| Site: UCSD (vs UAB) | +0.4921 | 0.6899 | ±1.3799 | +0.713 | 0.4757 |  |
| Site: UW (vs UAB) | +0.9060 | 0.5962 | ±1.1924 | +1.520 | 0.1286 |  |
| **Age (years)** | **-0.0991** | 0.0233 | ±0.0465 | **-4.262** | **2.02e-05** | *** |
| **BMI (kg/m2)** | **+0.1405** | 0.0459 | ±0.0918 | **+3.060** | **0.0022** | ** |
| Hypertension | -0.0453 | 0.5959 | ±1.1917 | -0.076 | 0.9394 |  |
| High cholesterol | +0.5389 | 0.5263 | ±1.0525 | +1.024 | 0.3058 |  |
| Kidney disease | +0.0848 | 1.0816 | ±2.1633 | +0.078 | 0.9375 |  |
| Circulatory disease | +1.0059 | 0.8039 | ±1.6079 | +1.251 | 0.2109 |  |
| Avg. daily mean/SD | -0.2369 | 0.1787 | ±0.3573 | -1.326 | 0.1849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **408**, R² = **0.1331**, Adj R² = **0.1090**, F-statistic = **5.53** (p = **3.05e-08**), Residual SE = **4.902** on **396** df, AIC = **2466.8**, BIC = **2515.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5178** | 2.3080 | ±4.6160 | **+2.824** | **0.0047** | ** |
| **Education: graduate level (vs college)** | **-1.0509** | 0.5264 | ±1.0529 | **-1.996** | **0.0459** | * |
| Education: high school or below (vs college) | +1.8374 | 1.2760 | ±2.5520 | +1.440 | 0.1499 |  |
| Site: UCSD (vs UAB) | +0.5679 | 0.6816 | ±1.3631 | +0.833 | 0.4047 |  |
| Site: UW (vs UAB) | +0.9237 | 0.5984 | ±1.1969 | +1.544 | 0.1227 |  |
| **Age (years)** | **-0.0939** | 0.0231 | ±0.0463 | **-4.056** | **4.99e-05** | *** |
| **BMI (kg/m2)** | **+0.1429** | 0.0466 | ±0.0933 | **+3.065** | **0.0022** | ** |
| Hypertension | -0.0412 | 0.5944 | ±1.1888 | -0.069 | 0.9447 |  |
| High cholesterol | +0.5076 | 0.5371 | ±1.0741 | +0.945 | 0.3446 |  |
| Kidney disease | +0.2636 | 1.0892 | ±2.1785 | +0.242 | 0.8088 |  |
| Circulatory disease | +0.9972 | 0.8080 | ±1.6160 | +1.234 | 0.2171 |  |
| MAG (mg/dL/h) | -0.0014 | 0.0327 | ±0.0654 | -0.042 | 0.9668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **408**, R² = **0.1351**, Adj R² = **0.1111**, F-statistic = **5.62** (p = **2.07e-08**), Residual SE = **4.896** on **396** df, AIC = **2465.9**, BIC = **2514.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.7279** | 2.1939 | ±4.3878 | **+2.611** | **0.0090** | ** |
| **Education: graduate level (vs college)** | **-1.0545** | 0.5246 | ±1.0493 | **-2.010** | **0.0444** | * |
| Education: high school or below (vs college) | +1.8232 | 1.2676 | ±2.5352 | +1.438 | 0.1503 |  |
| Site: UCSD (vs UAB) | +0.5284 | 0.6829 | ±1.3657 | +0.774 | 0.4390 |  |
| Site: UW (vs UAB) | +0.9170 | 0.5960 | ±1.1920 | +1.539 | 0.1239 |  |
| **Age (years)** | **-0.0970** | 0.0233 | ±0.0466 | **-4.166** | **3.10e-05** | *** |
| **BMI (kg/m2)** | **+0.1443** | 0.0464 | ±0.0929 | **+3.107** | **0.0019** | ** |
| Hypertension | -0.0603 | 0.5963 | ±1.1926 | -0.101 | 0.9195 |  |
| High cholesterol | +0.5374 | 0.5274 | ±1.0548 | +1.019 | 0.3082 |  |
| Kidney disease | +0.1401 | 1.0913 | ±2.1826 | +0.128 | 0.8978 |  |
| Circulatory disease | +1.0065 | 0.8083 | ±1.6165 | +1.245 | 0.2130 |  |
| Avg. daily range (mg/dL) | +0.0089 | 0.0098 | ±0.0197 | +0.906 | 0.3652 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **408**, R² = **0.1350**, Adj R² = **0.1109**, F-statistic = **5.62** (p = **2.13e-08**), Residual SE = **4.897** on **396** df, AIC = **2466.0**, BIC = **2514.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.1568** | 2.0199 | ±4.0399 | **+3.048** | **0.0023** | ** |
| **Education: graduate level (vs college)** | **-1.0844** | 0.5254 | ±1.0509 | **-2.064** | **0.0390** | * |
| Education: high school or below (vs college) | +1.8851 | 1.2739 | ±2.5478 | +1.480 | 0.1389 |  |
| Site: UCSD (vs UAB) | +0.5759 | 0.6759 | ±1.3517 | +0.852 | 0.3941 |  |
| Site: UW (vs UAB) | +0.9233 | 0.5937 | ±1.1873 | +1.555 | 0.1199 |  |
| **Age (years)** | **-0.0945** | 0.0232 | ±0.0464 | **-4.076** | **4.59e-05** | *** |
| **BMI (kg/m2)** | **+0.1403** | 0.0466 | ±0.0931 | **+3.013** | **0.0026** | ** |
| Hypertension | -0.0454 | 0.5933 | ±1.1866 | -0.076 | 0.9390 |  |
| High cholesterol | +0.5083 | 0.5254 | ±1.0507 | +0.967 | 0.3333 |  |
| Kidney disease | +0.2235 | 1.1054 | ±2.2109 | +0.202 | 0.8398 |  |
| Circulatory disease | +0.9903 | 0.8071 | ±1.6142 | +1.227 | 0.2199 |  |
| SD of daily means (mg/dL) | +0.0593 | 0.0541 | ±0.1083 | +1.095 | 0.2737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **408**, R² = **0.1440**, Adj R² = **0.1202**, F-statistic = **6.06** (p = **3.50e-09**), Residual SE = **4.871** on **396** df, AIC = **2461.7**, BIC = **2509.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9940** | 5.9338 | ±11.8677 | **+2.864** | **0.0042** | ** |
| **Education: graduate level (vs college)** | **-1.0503** | 0.5203 | ±1.0407 | **-2.019** | **0.0435** | * |
| Education: high school or below (vs college) | +1.8581 | 1.2780 | ±2.5560 | +1.454 | 0.1460 |  |
| Site: UCSD (vs UAB) | +0.6273 | 0.6775 | ±1.3550 | +0.926 | 0.3545 |  |
| Site: UW (vs UAB) | +0.9846 | 0.5875 | ±1.1751 | +1.676 | 0.0938 | . |
| **Age (years)** | **-0.0979** | 0.0230 | ±0.0461 | **-4.247** | **2.16e-05** | *** |
| **BMI (kg/m2)** | **+0.1416** | 0.0463 | ±0.0927 | **+3.055** | **0.0022** | ** |
| Hypertension | -0.0654 | 0.5938 | ±1.1875 | -0.110 | 0.9123 |  |
| High cholesterol | +0.5475 | 0.5251 | ±1.0501 | +1.043 | 0.2971 |  |
| Kidney disease | -0.0876 | 1.1077 | ±2.2154 | -0.079 | 0.9370 |  |
| Circulatory disease | +1.0909 | 0.8064 | ±1.6128 | +1.353 | 0.1761 |  |
| Time in range 70-180, pooled (%) | -0.1075 | 0.0577 | ±0.1154 | -1.863 | 0.0624 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **408**, R² = **0.1464**, Adj R² = **0.1227**, F-statistic = **6.17** (p = **2.18e-09**), Residual SE = **4.864** on **396** df, AIC = **2460.5**, BIC = **2508.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.8065** | 6.0308 | ±12.0617 | **+2.953** | **0.0032** | ** |
| **Education: graduate level (vs college)** | **-1.0441** | 0.5202 | ±1.0405 | **-2.007** | **0.0448** | * |
| Education: high school or below (vs college) | +1.8785 | 1.2738 | ±2.5476 | +1.475 | 0.1403 |  |
| Site: UCSD (vs UAB) | +0.6159 | 0.6762 | ±1.3525 | +0.911 | 0.3624 |  |
| Site: UW (vs UAB) | +0.9885 | 0.5866 | ±1.1731 | +1.685 | 0.0920 | . |
| **Age (years)** | **-0.0989** | 0.0230 | ±0.0460 | **-4.297** | **1.73e-05** | *** |
| **BMI (kg/m2)** | **+0.1403** | 0.0462 | ±0.0924 | **+3.037** | **0.0024** | ** |
| Hypertension | -0.0659 | 0.5934 | ±1.1868 | -0.111 | 0.9116 |  |
| High cholesterol | +0.5351 | 0.5243 | ±1.0487 | +1.020 | 0.3075 |  |
| Kidney disease | -0.1184 | 1.1143 | ±2.2287 | -0.106 | 0.9154 |  |
| Circulatory disease | +1.0955 | 0.8066 | ±1.6133 | +1.358 | 0.1744 |  |
| Avg. daily time in range 70-180 (%) | -0.1145 | 0.0584 | ±0.1168 | -1.960 | 0.0500 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.1334**, Adj R² = **0.1093**, F-statistic = **5.54** (p = **2.90e-08**), Residual SE = **4.901** on **396** df, AIC = **2466.7**, BIC = **2514.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5410** | 2.0503 | ±4.1006 | **+3.190** | **0.0014** | ** |
| **Education: graduate level (vs college)** | **-1.0540** | 0.5259 | ±1.0519 | **-2.004** | **0.0451** | * |
| Education: high school or below (vs college) | +1.8249 | 1.2799 | ±2.5598 | +1.426 | 0.1539 |  |
| Site: UCSD (vs UAB) | +0.5343 | 0.6840 | ±1.3681 | +0.781 | 0.4347 |  |
| Site: UW (vs UAB) | +0.9006 | 0.5994 | ±1.1987 | +1.503 | 0.1329 |  |
| **Age (years)** | **-0.0938** | 0.0232 | ±0.0463 | **-4.046** | **5.20e-05** | *** |
| **BMI (kg/m2)** | **+0.1424** | 0.0467 | ±0.0934 | **+3.050** | **0.0023** | ** |
| Hypertension | -0.0527 | 0.5948 | ±1.1896 | -0.089 | 0.9294 |  |
| High cholesterol | +0.4923 | 0.5306 | ±1.0612 | +0.928 | 0.3535 |  |
| Kidney disease | +0.2706 | 1.0884 | ±2.1767 | +0.249 | 0.8036 |  |
| Circulatory disease | +0.9897 | 0.8047 | ±1.6094 | +1.230 | 0.2188 |  |
| Time < 54 (%) | -0.0909 | 0.2627 | ±0.5254 | -0.346 | 0.7294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **408**, R² = **0.1331**, Adj R² = **0.1090**, F-statistic = **5.53** (p = **3.05e-08**), Residual SE = **4.902** on **396** df, AIC = **2466.8**, BIC = **2515.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4555** | 2.0378 | ±4.0756 | **+3.168** | **0.0015** | ** |
| **Education: graduate level (vs college)** | **-1.0503** | 0.5264 | ±1.0529 | **-1.995** | **0.0460** | * |
| Education: high school or below (vs college) | +1.8399 | 1.2837 | ±2.5673 | +1.433 | 0.1518 |  |
| Site: UCSD (vs UAB) | +0.5696 | 0.6799 | ±1.3599 | +0.838 | 0.4022 |  |
| Site: UW (vs UAB) | +0.9296 | 0.5975 | ±1.1951 | +1.556 | 0.1198 |  |
| **Age (years)** | **-0.0939** | 0.0232 | ±0.0465 | **-4.042** | **5.29e-05** | *** |
| **BMI (kg/m2)** | **+0.1429** | 0.0466 | ±0.0932 | **+3.067** | **0.0022** | ** |
| Hypertension | -0.0406 | 0.5972 | ±1.1944 | -0.068 | 0.9458 |  |
| High cholesterol | +0.5118 | 0.5284 | ±1.0568 | +0.969 | 0.3327 |  |
| Kidney disease | +0.2621 | 1.0898 | ±2.1796 | +0.241 | 0.8099 |  |
| Circulatory disease | +0.9983 | 0.8043 | ±1.6086 | +1.241 | 0.2145 |  |
| Avg. daily time < 54 (%) | +0.0120 | 0.2685 | ±0.5371 | +0.045 | 0.9643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.1333**, Adj R² = **0.1092**, F-statistic = **5.54** (p = **2.94e-08**), Residual SE = **4.902** on **396** df, AIC = **2466.7**, BIC = **2514.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.3931** | 2.0342 | ±4.0683 | **+3.143** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.0467** | 0.5255 | ±1.0510 | **-1.992** | **0.0464** | * |
| Education: high school or below (vs college) | +1.8560 | 1.2786 | ±2.5572 | +1.452 | 0.1466 |  |
| Site: UCSD (vs UAB) | +0.5813 | 0.6742 | ±1.3484 | +0.862 | 0.3885 |  |
| Site: UW (vs UAB) | +0.9467 | 0.5903 | ±1.1806 | +1.604 | 0.1088 |  |
| **Age (years)** | **-0.0938** | 0.0232 | ±0.0464 | **-4.047** | **5.19e-05** | *** |
| **BMI (kg/m2)** | **+0.1426** | 0.0466 | ±0.0933 | **+3.057** | **0.0022** | ** |
| Hypertension | -0.0296 | 0.5961 | ±1.1922 | -0.050 | 0.9604 |  |
| High cholesterol | +0.5218 | 0.5293 | ±1.0587 | +0.986 | 0.3243 |  |
| Kidney disease | +0.2642 | 1.0913 | ±2.1826 | +0.242 | 0.8087 |  |
| Circulatory disease | +1.0035 | 0.8058 | ±1.6115 | +1.245 | 0.2130 |  |
| Time 54-69, pooled (%) | +0.0340 | 0.1221 | ±0.2442 | +0.278 | 0.7807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **408**, R² = **0.1337**, Adj R² = **0.1097**, F-statistic = **5.56** (p = **2.70e-08**), Residual SE = **4.900** on **396** df, AIC = **2466.5**, BIC = **2514.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.3654** | 2.0287 | ±4.0573 | **+3.138** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.0403** | 0.5256 | ±1.0511 | **-1.979** | **0.0478** | * |
| Education: high school or below (vs college) | +1.8776 | 1.2797 | ±2.5594 | +1.467 | 0.1423 |  |
| Site: UCSD (vs UAB) | +0.5874 | 0.6739 | ±1.3478 | +0.872 | 0.3834 |  |
| Site: UW (vs UAB) | +0.9652 | 0.5896 | ±1.1792 | +1.637 | 0.1016 |  |
| **Age (years)** | **-0.0940** | 0.0232 | ±0.0464 | **-4.053** | **5.05e-05** | *** |
| **BMI (kg/m2)** | **+0.1422** | 0.0466 | ±0.0933 | **+3.049** | **0.0023** | ** |
| Hypertension | -0.0177 | 0.5966 | ±1.1931 | -0.030 | 0.9763 |  |
| High cholesterol | +0.5302 | 0.5282 | ±1.0563 | +1.004 | 0.3154 |  |
| Kidney disease | +0.2670 | 1.0895 | ±2.1791 | +0.245 | 0.8064 |  |
| Circulatory disease | +1.0054 | 0.8051 | ±1.6102 | +1.249 | 0.2117 |  |
| Avg. daily time 54-69 (%) | +0.0604 | 0.1218 | ±0.2437 | +0.496 | 0.6201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **408**, R² = **0.1331**, Adj R² = **0.1091**, F-statistic = **5.53** (p = **3.04e-08**), Residual SE = **4.902** on **396** df, AIC = **2466.8**, BIC = **2515.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4309** | 2.0437 | ±4.0874 | **+3.147** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.0493** | 0.5258 | ±1.0516 | **-1.996** | **0.0460** | * |
| Education: high school or below (vs college) | +1.8453 | 1.2817 | ±2.5634 | +1.440 | 0.1499 |  |
| Site: UCSD (vs UAB) | +0.5749 | 0.6763 | ±1.3526 | +0.850 | 0.3953 |  |
| Site: UW (vs UAB) | +0.9356 | 0.5932 | ±1.1864 | +1.577 | 0.1148 |  |
| **Age (years)** | **-0.0939** | 0.0232 | ±0.0463 | **-4.053** | **5.05e-05** | *** |
| **BMI (kg/m2)** | **+0.1429** | 0.0466 | ±0.0931 | **+3.069** | **0.0021** | ** |
| Hypertension | -0.0371 | 0.5966 | ±1.1932 | -0.062 | 0.9504 |  |
| High cholesterol | +0.5157 | 0.5311 | ±1.0622 | +0.971 | 0.3316 |  |
| Kidney disease | +0.2625 | 1.0926 | ±2.1852 | +0.240 | 0.8102 |  |
| Circulatory disease | +1.0002 | 0.8055 | ±1.6110 | +1.242 | 0.2143 |  |
| Time < 70 (%) | +0.0104 | 0.0935 | ±0.1869 | +0.111 | 0.9114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **408**, R² = **0.1336**, Adj R² = **0.1095**, F-statistic = **5.55** (p = **2.80e-08**), Residual SE = **4.901** on **396** df, AIC = **2466.6**, BIC = **2514.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.3752** | 2.0323 | ±4.0646 | **+3.137** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.0410** | 0.5260 | ±1.0520 | **-1.979** | **0.0478** | * |
| Education: high school or below (vs college) | +1.8715 | 1.2828 | ±2.5657 | +1.459 | 0.1446 |  |
| Site: UCSD (vs UAB) | +0.5912 | 0.6744 | ±1.3487 | +0.877 | 0.3807 |  |
| Site: UW (vs UAB) | +0.9651 | 0.5911 | ±1.1822 | +1.633 | 0.1025 |  |
| **Age (years)** | **-0.0941** | 0.0232 | ±0.0464 | **-4.059** | **4.93e-05** | *** |
| **BMI (kg/m2)** | **+0.1426** | 0.0466 | ±0.0932 | **+3.060** | **0.0022** | ** |
| Hypertension | -0.0195 | 0.5975 | ±1.1950 | -0.033 | 0.9740 |  |
| High cholesterol | +0.5302 | 0.5288 | ±1.0576 | +1.003 | 0.3161 |  |
| Kidney disease | +0.2627 | 1.0908 | ±2.1815 | +0.241 | 0.8097 |  |
| Circulatory disease | +1.0061 | 0.8048 | ±1.6096 | +1.250 | 0.2113 |  |
| Avg. daily time < 70 (%) | +0.0425 | 0.0966 | ±0.1933 | +0.440 | 0.6602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.1343**, Adj R² = **0.1103**, F-statistic = **5.59** (p = **2.42e-08**), Residual SE = **4.899** on **396** df, AIC = **2466.3**, BIC = **2514.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +21.6482 | 18.4208 | ±36.8415 | +1.175 | 0.2399 |  |
| **Education: graduate level (vs college)** | **-1.0450** | 0.5254 | ±1.0507 | **-1.989** | **0.0467** | * |
| Education: high school or below (vs college) | +1.8629 | 1.2740 | ±2.5479 | +1.462 | 0.1437 |  |
| Site: UCSD (vs UAB) | +0.6213 | 0.6814 | ±1.3628 | +0.912 | 0.3619 |  |
| Site: UW (vs UAB) | +0.9766 | 0.6010 | ±1.2019 | +1.625 | 0.1041 |  |
| **Age (years)** | **-0.0948** | 0.0232 | ±0.0464 | **-4.088** | **4.35e-05** | *** |
| **BMI (kg/m2)** | **+0.1438** | 0.0465 | ±0.0931 | **+3.088** | **0.0020** | ** |
| Hypertension | -0.0310 | 0.5951 | ±1.1902 | -0.052 | 0.9584 |  |
| High cholesterol | +0.5508 | 0.5303 | ±1.0606 | +1.039 | 0.2990 |  |
| Kidney disease | +0.1641 | 1.1159 | ±2.2318 | +0.147 | 0.8831 |  |
| Circulatory disease | +1.0255 | 0.8057 | ±1.6114 | +1.273 | 0.2031 |  |
| Time 54-250, pooled (%) | -0.1530 | 0.1841 | ±0.3682 | -0.831 | 0.4059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.1368**, Adj R² = **0.1129**, F-statistic = **5.71** (p = **1.47e-08**), Residual SE = **4.892** on **396** df, AIC = **2465.1**, BIC = **2513.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +36.9760 | 22.7376 | ±45.4752 | +1.626 | 0.1039 |  |
| Education: graduate level (vs college) | -1.0292 | 0.5255 | ±1.0509 | -1.959 | 0.0502 | . |
| Education: high school or below (vs college) | +1.8860 | 1.2691 | ±2.5383 | +1.486 | 0.1373 |  |
| Site: UCSD (vs UAB) | +0.6444 | 0.6771 | ±1.3542 | +0.952 | 0.3412 |  |
| Site: UW (vs UAB) | +1.0189 | 0.5976 | ±1.1951 | +1.705 | 0.0882 | . |
| **Age (years)** | **-0.0967** | 0.0232 | ±0.0465 | **-4.161** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.1434** | 0.0465 | ±0.0929 | **+3.086** | **0.0020** | ** |
| Hypertension | -0.0129 | 0.5961 | ±1.1922 | -0.022 | 0.9827 |  |
| High cholesterol | +0.5673 | 0.5287 | ±1.0575 | +1.073 | 0.2833 |  |
| Kidney disease | +0.0574 | 1.1287 | ±2.2573 | +0.051 | 0.9594 |  |
| Circulatory disease | +1.0523 | 0.8055 | ±1.6110 | +1.306 | 0.1914 |  |
| Avg. daily time 54-250 (%) | -0.3059 | 0.2265 | ±0.4529 | -1.351 | 0.1768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.1458**, Adj R² = **0.1221**, F-statistic = **6.14** (p = **2.45e-09**), Residual SE = **4.866** on **396** df, AIC = **2460.8**, BIC = **2509.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5668** | 1.9934 | ±3.9867 | **+3.294** | **9.86e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0738** | 0.5201 | ±1.0402 | **-2.064** | **0.0390** | * |
| Education: high school or below (vs college) | +1.7668 | 1.2886 | ±2.5771 | +1.371 | 0.1703 |  |
| Site: UCSD (vs UAB) | +0.5349 | 0.6815 | ±1.3630 | +0.785 | 0.4325 |  |
| Site: UW (vs UAB) | +0.8714 | 0.5950 | ±1.1900 | +1.465 | 0.1430 |  |
| **Age (years)** | **-0.0986** | 0.0230 | ±0.0460 | **-4.289** | **1.79e-05** | *** |
| **BMI (kg/m2)** | **+0.1417** | 0.0461 | ±0.0923 | **+3.071** | **0.0021** | ** |
| Hypertension | -0.1370 | 0.5937 | ±1.1874 | -0.231 | 0.8176 |  |
| High cholesterol | +0.4725 | 0.5238 | ±1.0476 | +0.902 | 0.3671 |  |
| Kidney disease | -0.1183 | 1.0950 | ±2.1900 | -0.108 | 0.9139 |  |
| Circulatory disease | +1.0705 | 0.8120 | ±1.6240 | +1.318 | 0.1874 |  |
| Time 181-250, pooled (%) | +0.1439 | 0.0771 | ±0.1541 | +1.868 | 0.0618 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **408**, R² = **0.1462**, Adj R² = **0.1225**, F-statistic = **6.16** (p = **2.26e-09**), Residual SE = **4.865** on **396** df, AIC = **2460.6**, BIC = **2508.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5922** | 1.9924 | ±3.9847 | **+3.309** | **9.37e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0772** | 0.5204 | ±1.0409 | **-2.070** | **0.0385** | * |
| Education: high school or below (vs college) | +1.7745 | 1.2844 | ±2.5687 | +1.382 | 0.1671 |  |
| Site: UCSD (vs UAB) | +0.5435 | 0.6811 | ±1.3623 | +0.798 | 0.4249 |  |
| Site: UW (vs UAB) | +0.8699 | 0.5956 | ±1.1912 | +1.460 | 0.1442 |  |
| **Age (years)** | **-0.0984** | 0.0229 | ±0.0459 | **-4.290** | **1.79e-05** | *** |
| **BMI (kg/m2)** | **+0.1411** | 0.0461 | ±0.0922 | **+3.061** | **0.0022** | ** |
| Hypertension | -0.1414 | 0.5936 | ±1.1873 | -0.238 | 0.8118 |  |
| High cholesterol | +0.4678 | 0.5236 | ±1.0472 | +0.893 | 0.3716 |  |
| Kidney disease | -0.1193 | 1.1052 | ±2.2103 | -0.108 | 0.9141 |  |
| Circulatory disease | +1.0738 | 0.8122 | ±1.6245 | +1.322 | 0.1861 |  |
| Avg. daily time 181-250 (%) | +0.1402 | 0.0760 | ±0.1521 | +1.844 | 0.0652 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **408**, R² = **0.1456**, Adj R² = **0.1219**, F-statistic = **6.13** (p = **2.55e-09**), Residual SE = **4.867** on **396** df, AIC = **2460.9**, BIC = **2509.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5710** | 1.9945 | ±3.9889 | **+3.295** | **9.86e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0703** | 0.5208 | ±1.0415 | **-2.055** | **0.0399** | * |
| Education: high school or below (vs college) | +1.7772 | 1.2857 | ±2.5715 | +1.382 | 0.1669 |  |
| Site: UCSD (vs UAB) | +0.5388 | 0.6815 | ±1.3629 | +0.791 | 0.4292 |  |
| Site: UW (vs UAB) | +0.8838 | 0.5946 | ±1.1891 | +1.486 | 0.1372 |  |
| **Age (years)** | **-0.0986** | 0.0230 | ±0.0459 | **-4.296** | **1.74e-05** | *** |
| **BMI (kg/m2)** | **+0.1418** | 0.0462 | ±0.0923 | **+3.073** | **0.0021** | ** |
| Hypertension | -0.1308 | 0.5933 | ±1.1866 | -0.220 | 0.8256 |  |
| High cholesterol | +0.4860 | 0.5242 | ±1.0483 | +0.927 | 0.3539 |  |
| Kidney disease | -0.1424 | 1.1042 | ±2.2084 | -0.129 | 0.8974 |  |
| Circulatory disease | +1.0739 | 0.8119 | ±1.6237 | +1.323 | 0.1859 |  |
| Time > 180 (%) | +0.1262 | 0.0694 | ±0.1389 | +1.818 | 0.0690 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **408**, R² = **0.1461**, Adj R² = **0.1223**, F-statistic = **6.16** (p = **2.32e-09**), Residual SE = **4.865** on **396** df, AIC = **2460.7**, BIC = **2508.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.6012** | 1.9939 | ±3.9878 | **+3.311** | **9.30e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0723** | 0.5213 | ±1.0426 | **-2.057** | **0.0397** | * |
| Education: high school or below (vs college) | +1.7855 | 1.2808 | ±2.5615 | +1.394 | 0.1633 |  |
| Site: UCSD (vs UAB) | +0.5488 | 0.6809 | ±1.3618 | +0.806 | 0.4203 |  |
| Site: UW (vs UAB) | +0.8811 | 0.5958 | ±1.1916 | +1.479 | 0.1392 |  |
| **Age (years)** | **-0.0986** | 0.0229 | ±0.0458 | **-4.300** | **1.71e-05** | *** |
| **BMI (kg/m2)** | **+0.1411** | 0.0461 | ±0.0922 | **+3.061** | **0.0022** | ** |
| Hypertension | -0.1333 | 0.5932 | ±1.1865 | -0.225 | 0.8223 |  |
| High cholesterol | +0.4789 | 0.5238 | ±1.0477 | +0.914 | 0.3606 |  |
| Kidney disease | -0.1458 | 1.1145 | ±2.2290 | -0.131 | 0.8959 |  |
| Circulatory disease | +1.0778 | 0.8119 | ±1.6238 | +1.328 | 0.1843 |  |
| Avg. daily time > 180 (%) | +0.1229 | 0.0703 | ±0.1406 | +1.748 | 0.0804 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **408**, R² = **0.1569**, Adj R² = **0.1335**, F-statistic = **6.70** (p = **2.50e-10**), Residual SE = **4.834** on **396** df, AIC = **2455.5**, BIC = **2503.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7200** | 1.9785 | ±3.9569 | **+3.397** | **6.82e-04** | *** |
| Education: graduate level (vs college) | -0.9769 | 0.5171 | ±1.0341 | -1.889 | 0.0588 | . |
| Education: high school or below (vs college) | +1.7278 | 1.2907 | ±2.5814 | +1.339 | 0.1807 |  |
| Site: UCSD (vs UAB) | +0.5856 | 0.6837 | ±1.3675 | +0.857 | 0.3917 |  |
| Site: UW (vs UAB) | +0.9089 | 0.5847 | ±1.1694 | +1.554 | 0.1201 |  |
| **Age (years)** | **-0.0976** | 0.0228 | ±0.0456 | **-4.281** | **1.86e-05** | *** |
| **BMI (kg/m2)** | **+0.1342** | 0.0463 | ±0.0927 | **+2.897** | **0.0038** | ** |
| Hypertension | -0.1738 | 0.5881 | ±1.1761 | -0.296 | 0.7676 |  |
| High cholesterol | +0.5229 | 0.5215 | ±1.0430 | +1.003 | 0.3161 |  |
| Kidney disease | +0.2395 | 1.1166 | ±2.2333 | +0.214 | 0.8302 |  |
| Circulatory disease | +1.1995 | 0.8080 | ±1.6159 | +1.485 | 0.1376 |  |
| **Nocturnal time > 180 (%)** | **+0.1784** | 0.0549 | ±0.1098 | **+3.250** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.1346**, Adj R² = **0.1106**, F-statistic = **5.60** (p = **2.28e-08**), Residual SE = **4.898** on **396** df, AIC = **2466.1**, BIC = **2514.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4307** | 2.0185 | ±4.0371 | **+3.186** | **0.0014** | ** |
| **Education: graduate level (vs college)** | **-1.0340** | 0.5238 | ±1.0476 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | +1.8446 | 1.2767 | ±2.5534 | +1.445 | 0.1485 |  |
| Site: UCSD (vs UAB) | +0.5326 | 0.6836 | ±1.3671 | +0.779 | 0.4359 |  |
| Site: UW (vs UAB) | +0.9292 | 0.5939 | ±1.1878 | +1.565 | 0.1177 |  |
| **Age (years)** | **-0.0953** | 0.0230 | ±0.0460 | **-4.145** | **3.40e-05** | *** |
| **BMI (kg/m2)** | **+0.1441** | 0.0465 | ±0.0930 | **+3.100** | **0.0019** | ** |
| Hypertension | -0.0661 | 0.5965 | ±1.1929 | -0.111 | 0.9117 |  |
| High cholesterol | +0.5164 | 0.5269 | ±1.0539 | +0.980 | 0.3271 |  |
| Kidney disease | +0.2026 | 1.0671 | ±2.1342 | +0.190 | 0.8494 |  |
| Circulatory disease | +1.0194 | 0.8074 | ±1.6148 | +1.263 | 0.2068 |  |
| Any reading > 250 during wear (0/1) | +0.5488 | 0.6865 | ±1.3729 | +0.799 | 0.4240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.1396**, Adj R² = **0.1157**, F-statistic = **5.84** (p = **8.41e-09**), Residual SE = **4.884** on **396** df, AIC = **2463.7**, BIC = **2511.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5443** | 2.0181 | ±4.0362 | **+3.243** | **0.0012** | ** |
| **Education: graduate level (vs college)** | **-1.0476** | 0.5277 | ±1.0553 | **-1.985** | **0.0471** | * |
| Education: high school or below (vs college) | +1.8462 | 1.2708 | ±2.5416 | +1.453 | 0.1463 |  |
| Site: UCSD (vs UAB) | +0.5664 | 0.6807 | ±1.3614 | +0.832 | 0.4054 |  |
| Site: UW (vs UAB) | +0.9535 | 0.5937 | ±1.1874 | +1.606 | 0.1083 |  |
| **Age (years)** | **-0.0970** | 0.0231 | ±0.0461 | **-4.207** | **2.59e-05** | *** |
| **BMI (kg/m2)** | **+0.1429** | 0.0464 | ±0.0929 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.0687 | 0.5929 | ±1.1857 | -0.116 | 0.9078 |  |
| High cholesterol | +0.5531 | 0.5325 | ±1.0650 | +1.039 | 0.2989 |  |
| Kidney disease | -0.0817 | 1.1417 | ±2.2834 | -0.072 | 0.9429 |  |
| Circulatory disease | +1.0573 | 0.8116 | ±1.6232 | +1.303 | 0.1927 |  |
| Time > 250 (%) | +0.6131 | 0.5458 | ±1.0916 | +1.123 | 0.2613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.1402**, Adj R² = **0.1163**, F-statistic = **5.87** (p = **7.51e-09**), Residual SE = **4.882** on **396** df, AIC = **2463.5**, BIC = **2511.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.5827** | 2.0217 | ±4.0435 | **+3.256** | **0.0011** | ** |
| **Education: graduate level (vs college)** | **-1.0430** | 0.5320 | ±1.0641 | **-1.960** | **0.0500** | * |
| Education: high school or below (vs college) | +1.8532 | 1.2663 | ±2.5326 | +1.463 | 0.1433 |  |
| Site: UCSD (vs UAB) | +0.5784 | 0.6796 | ±1.3591 | +0.851 | 0.3947 |  |
| Site: UW (vs UAB) | +0.9472 | 0.5954 | ±1.1907 | +1.591 | 0.1116 |  |
| **Age (years)** | **-0.0972** | 0.0230 | ±0.0461 | **-4.218** | **2.46e-05** | *** |
| **BMI (kg/m2)** | **+0.1421** | 0.0464 | ±0.0929 | **+3.061** | **0.0022** | ** |
| Hypertension | -0.0620 | 0.5927 | ±1.1854 | -0.105 | 0.9167 |  |
| High cholesterol | +0.5386 | 0.5332 | ±1.0663 | +1.010 | 0.3124 |  |
| Kidney disease | -0.0927 | 1.1482 | ±2.2964 | -0.081 | 0.9356 |  |
| Circulatory disease | +1.0620 | 0.8101 | ±1.6203 | +1.311 | 0.1899 |  |
| Avg. daily time > 250 (%) | +0.5937 | 0.6412 | ±1.2824 | +0.926 | 0.3545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 408; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0742**, LLR χ² = **30.18** (p = **7.99e-04**), AUC = **0.6900**, AIC = **398.5**, BIC = **442.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5949 | 1.0156 | ±2.0312 | -1.570 | 0.1163 | 0.2029 |  |
| Education: graduate level (vs college) | -0.2997 | 0.2917 | ±0.5833 | -1.028 | 0.3041 | 0.7410 |  |
| Education: high school or below (vs college) | +0.1362 | 0.4786 | ±0.9573 | +0.284 | 0.7761 | 1.1459 |  |
| Site: UCSD (vs UAB) | -0.1269 | 0.3853 | ±0.7705 | -0.329 | 0.7420 | 0.8809 |  |
| Site: UW (vs UAB) | +0.2123 | 0.2965 | ±0.5930 | +0.716 | 0.4739 | 1.2366 |  |
| **Age (years)** | **-0.0299** | 0.0133 | ±0.0266 | **-2.254** | **0.0242** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0593** | 0.0173 | ±0.0347 | **+3.424** | **6.16e-04** | 1.0611 | *** |
| Hypertension | +0.0129 | 0.2905 | ±0.5809 | +0.044 | 0.9646 | 1.0130 |  |
| High cholesterol | +0.1373 | 0.2813 | ±0.5625 | +0.488 | 0.6254 | 1.1472 |  |
| Kidney disease | +0.1010 | 0.5070 | ±1.0141 | +0.199 | 0.8421 | 1.1063 |  |
| Circulatory disease | +0.5063 | 0.3592 | ±0.7185 | +1.409 | 0.1587 | 1.6591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0824**, LLR χ² = **33.49** (p = **4.38e-04**), AUC = **0.7075**, AIC = **397.2**, BIC = **445.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.2127** | 1.7949 | ±3.5897 | **-2.347** | **0.0189** | 0.0148 | * |
| Education: graduate level (vs college) | -0.2770 | 0.2929 | ±0.5858 | -0.946 | 0.3442 | 0.7580 |  |
| Education: high school or below (vs college) | +0.0985 | 0.4779 | ±0.9558 | +0.206 | 0.8367 | 1.1035 |  |
| Site: UCSD (vs UAB) | -0.2011 | 0.3909 | ±0.7818 | -0.515 | 0.6069 | 0.8178 |  |
| Site: UW (vs UAB) | +0.2040 | 0.2987 | ±0.5975 | +0.683 | 0.4947 | 1.2263 |  |
| **Age (years)** | **-0.0338** | 0.0136 | ±0.0272 | **-2.491** | **0.0127** | 0.9667 | * |
| **BMI (kg/m2)** | **+0.0552** | 0.0175 | ±0.0351 | **+3.145** | **0.0017** | 1.0567 | ** |
| Hypertension | +0.0046 | 0.2938 | ±0.5876 | +0.016 | 0.9874 | 1.0046 |  |
| High cholesterol | +0.0658 | 0.2857 | ±0.5715 | +0.230 | 0.8180 | 1.0680 |  |
| Kidney disease | +0.0806 | 0.5085 | ±1.0170 | +0.159 | 0.8741 | 1.0839 |  |
| Circulatory disease | +0.5513 | 0.3616 | ±0.7232 | +1.525 | 0.1273 | 1.7356 |  |
| HbA1c (%) | +0.5325 | 0.2982 | ±0.5965 | +1.785 | 0.0742 | 1.7031 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0788**, LLR χ² = **32.03** (p = **7.53e-04**), AUC = **0.6980**, AIC = **398.6**, BIC = **446.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8638** | 1.3766 | ±2.7532 | **-2.080** | **0.0375** | 0.0571 | * |
| Education: graduate level (vs college) | -0.3280 | 0.2926 | ±0.5852 | -1.121 | 0.2624 | 0.7204 |  |
| Education: high school or below (vs college) | +0.1024 | 0.4778 | ±0.9557 | +0.214 | 0.8303 | 1.1078 |  |
| Site: UCSD (vs UAB) | -0.1391 | 0.3862 | ±0.7724 | -0.360 | 0.7187 | 0.8701 |  |
| Site: UW (vs UAB) | +0.1762 | 0.2982 | ±0.5964 | +0.591 | 0.5546 | 1.1927 |  |
| **Age (years)** | **-0.0311** | 0.0133 | ±0.0266 | **-2.336** | **0.0195** | 0.9694 | * |
| **BMI (kg/m2)** | **+0.0584** | 0.0174 | ±0.0348 | **+3.357** | **7.88e-04** | 1.0601 | *** |
| Hypertension | -0.0249 | 0.2943 | ±0.5886 | -0.085 | 0.9325 | 0.9754 |  |
| High cholesterol | +0.0891 | 0.2841 | ±0.5682 | +0.314 | 0.7539 | 1.0932 |  |
| Kidney disease | +0.0344 | 0.5098 | ±1.0197 | +0.068 | 0.9462 | 1.0350 |  |
| Circulatory disease | +0.5165 | 0.3597 | ±0.7194 | +1.436 | 0.1510 | 1.6762 |  |
| Mean glucose (mg/dL) | +0.0124 | 0.0090 | ±0.0181 | +1.376 | 0.1689 | 1.0125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0788**, LLR χ² = **32.03** (p = **7.53e-04**), AUC = **0.6980**, AIC = **398.6**, BIC = **446.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -4.5864 | 2.4059 | ±4.8118 | -1.906 | 0.0566 | 0.0102 | . |
| Education: graduate level (vs college) | -0.3280 | 0.2926 | ±0.5852 | -1.121 | 0.2624 | 0.7204 |  |
| Education: high school or below (vs college) | +0.1024 | 0.4778 | ±0.9557 | +0.214 | 0.8303 | 1.1078 |  |
| Site: UCSD (vs UAB) | -0.1391 | 0.3862 | ±0.7724 | -0.360 | 0.7187 | 0.8701 |  |
| Site: UW (vs UAB) | +0.1762 | 0.2982 | ±0.5964 | +0.591 | 0.5546 | 1.1927 |  |
| **Age (years)** | **-0.0311** | 0.0133 | ±0.0266 | **-2.336** | **0.0195** | 0.9694 | * |
| **BMI (kg/m2)** | **+0.0584** | 0.0174 | ±0.0348 | **+3.357** | **7.88e-04** | 1.0601 | *** |
| Hypertension | -0.0249 | 0.2943 | ±0.5886 | -0.085 | 0.9325 | 0.9754 |  |
| High cholesterol | +0.0891 | 0.2841 | ±0.5682 | +0.314 | 0.7539 | 1.0932 |  |
| Kidney disease | +0.0344 | 0.5098 | ±1.0197 | +0.068 | 0.9462 | 1.0350 |  |
| Circulatory disease | +0.5165 | 0.3597 | ±0.7194 | +1.436 | 0.1510 | 1.6762 |  |
| GMI (%) | +0.5204 | 0.3783 | ±0.7566 | +1.376 | 0.1689 | 1.6827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0792**, LLR χ² = **32.21** (p = **7.06e-04**), AUC = **0.6991**, AIC = **398.5**, BIC = **446.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7817** | 1.3117 | ±2.6234 | **-2.121** | **0.0339** | 0.0619 | * |
| Education: graduate level (vs college) | -0.3166 | 0.2922 | ±0.5844 | -1.084 | 0.2786 | 0.7286 |  |
| Education: high school or below (vs college) | +0.0937 | 0.4771 | ±0.9542 | +0.196 | 0.8444 | 1.0982 |  |
| Site: UCSD (vs UAB) | -0.1547 | 0.3864 | ±0.7728 | -0.400 | 0.6889 | 0.8567 |  |
| Site: UW (vs UAB) | +0.1749 | 0.2979 | ±0.5958 | +0.587 | 0.5571 | 1.1911 |  |
| **Age (years)** | **-0.0300** | 0.0133 | ±0.0266 | **-2.253** | **0.0243** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0559** | 0.0175 | ±0.0350 | **+3.200** | **0.0014** | 1.0575 | ** |
| Hypertension | -0.0223 | 0.2939 | ±0.5877 | -0.076 | 0.9396 | 0.9780 |  |
| High cholesterol | +0.0818 | 0.2845 | ±0.5690 | +0.287 | 0.7739 | 1.0852 |  |
| Kidney disease | +0.0975 | 0.5062 | ±1.0123 | +0.193 | 0.8473 | 1.1024 |  |
| Circulatory disease | +0.5337 | 0.3601 | ±0.7201 | +1.482 | 0.1383 | 1.7052 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0118 | 0.0082 | ±0.0164 | +1.438 | 0.1506 | 1.0119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0838**, LLR χ² = **34.09** (p = **3.50e-04**), AUC = **0.7015**, AIC = **396.6**, BIC = **444.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1564** | 1.0609 | ±2.1219 | **-2.033** | **0.0421** | 0.1157 | * |
| Education: graduate level (vs college) | -0.3320 | 0.2937 | ±0.5875 | -1.130 | 0.2584 | 0.7175 |  |
| Education: high school or below (vs college) | +0.1280 | 0.4806 | ±0.9613 | +0.266 | 0.7901 | 1.1365 |  |
| Site: UCSD (vs UAB) | -0.1717 | 0.3900 | ±0.7800 | -0.440 | 0.6597 | 0.8422 |  |
| Site: UW (vs UAB) | +0.2083 | 0.2980 | ±0.5959 | +0.699 | 0.4845 | 1.2316 |  |
| **Age (years)** | **-0.0346** | 0.0136 | ±0.0273 | **-2.536** | **0.0112** | 0.9660 | * |
| **BMI (kg/m2)** | **+0.0587** | 0.0174 | ±0.0347 | **+3.384** | **7.14e-04** | 1.0605 | *** |
| Hypertension | -0.0317 | 0.2955 | ±0.5911 | -0.107 | 0.9146 | 0.9688 |  |
| High cholesterol | +0.1532 | 0.2834 | ±0.5667 | +0.540 | 0.5889 | 1.1655 |  |
| Kidney disease | -0.0556 | 0.5180 | ±1.0360 | -0.107 | 0.9145 | 0.9459 |  |
| Circulatory disease | +0.5392 | 0.3607 | ±0.7214 | +1.495 | 0.1350 | 1.7146 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0395** | 0.0197 | ±0.0394 | **+2.008** | **0.0446** | 1.0403 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0839**, LLR χ² = **34.13** (p = **3.44e-04**), AUC = **0.7020**, AIC = **396.5**, BIC = **444.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1230** | 1.0562 | ±2.1125 | **-2.010** | **0.0444** | 0.1197 | * |
| Education: graduate level (vs college) | -0.3214 | 0.2936 | ±0.5872 | -1.095 | 0.2736 | 0.7251 |  |
| Education: high school or below (vs college) | +0.1137 | 0.4815 | ±0.9630 | +0.236 | 0.8133 | 1.1204 |  |
| Site: UCSD (vs UAB) | -0.1741 | 0.3895 | ±0.7789 | -0.447 | 0.6549 | 0.8403 |  |
| Site: UW (vs UAB) | +0.2043 | 0.2984 | ±0.5968 | +0.685 | 0.4936 | 1.2267 |  |
| **Age (years)** | **-0.0350** | 0.0137 | ±0.0273 | **-2.560** | **0.0105** | 0.9656 | * |
| **BMI (kg/m2)** | **+0.0589** | 0.0174 | ±0.0348 | **+3.387** | **7.08e-04** | 1.0607 | *** |
| Hypertension | -0.0277 | 0.2956 | ±0.5913 | -0.094 | 0.9252 | 0.9726 |  |
| High cholesterol | +0.1477 | 0.2832 | ±0.5663 | +0.522 | 0.6020 | 1.1591 |  |
| Kidney disease | -0.0702 | 0.5192 | ±1.0383 | -0.135 | 0.8925 | 0.9322 |  |
| Circulatory disease | +0.5402 | 0.3608 | ±0.7216 | +1.497 | 0.1343 | 1.7163 |  |
| **Avg. daily SD (mg/dL)** | **+0.0435** | 0.0215 | ±0.0430 | **+2.021** | **0.0433** | 1.0444 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0782**, LLR χ² = **31.80** (p = **8.22e-04**), AUC = **0.6948**, AIC = **398.9**, BIC = **447.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.1199 | 1.0999 | ±2.1997 | -1.927 | 0.0539 | 0.1200 | . |
| Education: graduate level (vs college) | -0.3104 | 0.2928 | ±0.5856 | -1.060 | 0.2890 | 0.7331 |  |
| Education: high school or below (vs college) | +0.1448 | 0.4812 | ±0.9625 | +0.301 | 0.7635 | 1.1558 |  |
| Site: UCSD (vs UAB) | -0.1499 | 0.3875 | ±0.7751 | -0.387 | 0.6990 | 0.8608 |  |
| Site: UW (vs UAB) | +0.2299 | 0.2977 | ±0.5954 | +0.772 | 0.4401 | 1.2584 |  |
| **Age (years)** | **-0.0328** | 0.0136 | ±0.0272 | **-2.419** | **0.0156** | 0.9677 | * |
| **BMI (kg/m2)** | **+0.0592** | 0.0173 | ±0.0346 | **+3.419** | **6.28e-04** | 1.0610 | *** |
| Hypertension | -0.0012 | 0.2924 | ±0.5849 | -0.004 | 0.9966 | 0.9988 |  |
| High cholesterol | +0.1706 | 0.2837 | ±0.5674 | +0.601 | 0.5477 | 1.1860 |  |
| Kidney disease | +0.0218 | 0.5127 | ±1.0253 | +0.043 | 0.9660 | 1.0221 |  |
| Circulatory disease | +0.5274 | 0.3600 | ±0.7199 | +1.465 | 0.1429 | 1.6945 |  |
| CV (%) | +0.0358 | 0.0277 | ±0.0555 | +1.291 | 0.1967 | 1.0365 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0802**, LLR χ² = **32.62** (p = **6.05e-04**), AUC = **0.6975**, AIC = **398.0**, BIC = **446.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3353 | 1.2931 | ±2.5862 | -0.259 | 0.7954 | 0.7151 |  |
| Education: graduate level (vs college) | -0.3316 | 0.2937 | ±0.5875 | -1.129 | 0.2589 | 0.7178 |  |
| Education: high school or below (vs college) | +0.1285 | 0.4822 | ±0.9644 | +0.266 | 0.7899 | 1.1371 |  |
| Site: UCSD (vs UAB) | -0.1529 | 0.3879 | ±0.7759 | -0.394 | 0.6935 | 0.8582 |  |
| Site: UW (vs UAB) | +0.2189 | 0.2978 | ±0.5956 | +0.735 | 0.4623 | 1.2447 |  |
| **Age (years)** | **-0.0336** | 0.0136 | ±0.0272 | **-2.471** | **0.0135** | 0.9669 | * |
| **BMI (kg/m2)** | **+0.0589** | 0.0173 | ±0.0347 | **+3.398** | **6.79e-04** | 1.0607 | *** |
| Hypertension | -0.0029 | 0.2929 | ±0.5859 | -0.010 | 0.9920 | 0.9971 |  |
| High cholesterol | +0.1567 | 0.2831 | ±0.5663 | +0.553 | 0.5801 | 1.1696 |  |
| Kidney disease | +0.0155 | 0.5117 | ±1.0233 | +0.030 | 0.9759 | 1.0156 |  |
| Circulatory disease | +0.5291 | 0.3598 | ±0.7195 | +1.471 | 0.1414 | 1.6974 |  |
| Mean / SD ratio | -0.1876 | 0.1206 | ±0.2412 | -1.556 | 0.1198 | 0.8289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0787**, LLR χ² = **32.01** (p = **7.60e-04**), AUC = **0.6946**, AIC = **398.7**, BIC = **446.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5238 | 1.2880 | ±2.5761 | -0.407 | 0.6843 | 0.5923 |  |
| Education: graduate level (vs college) | -0.3221 | 0.2933 | ±0.5865 | -1.098 | 0.2721 | 0.7246 |  |
| Education: high school or below (vs college) | +0.1105 | 0.4818 | ±0.9635 | +0.229 | 0.8186 | 1.1168 |  |
| Site: UCSD (vs UAB) | -0.1607 | 0.3876 | ±0.7751 | -0.415 | 0.6784 | 0.8516 |  |
| Site: UW (vs UAB) | +0.2155 | 0.2977 | ±0.5953 | +0.724 | 0.4691 | 1.2405 |  |
| **Age (years)** | **-0.0334** | 0.0136 | ±0.0273 | **-2.449** | **0.0143** | 0.9672 | * |
| **BMI (kg/m2)** | **+0.0586** | 0.0174 | ±0.0347 | **+3.376** | **7.35e-04** | 1.0603 | *** |
| Hypertension | +0.0067 | 0.2927 | ±0.5853 | +0.023 | 0.9817 | 1.0067 |  |
| High cholesterol | +0.1460 | 0.2825 | ±0.5650 | +0.517 | 0.6053 | 1.1572 |  |
| Kidney disease | +0.0083 | 0.5127 | ±1.0253 | +0.016 | 0.9871 | 1.0084 |  |
| Circulatory disease | +0.5251 | 0.3597 | ±0.7194 | +1.460 | 0.1443 | 1.6906 |  |
| Avg. daily mean/SD | -0.1311 | 0.0977 | ±0.1954 | -1.342 | 0.1796 | 0.8771 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0745**, LLR χ² = **30.28** (p = **0.0014**), AUC = **0.6896**, AIC = **400.4**, BIC = **448.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3831 | 1.2222 | ±2.4444 | -1.132 | 0.2578 | 0.2508 |  |
| Education: graduate level (vs college) | -0.2971 | 0.2918 | ±0.5836 | -1.018 | 0.3086 | 0.7430 |  |
| Education: high school or below (vs college) | +0.1334 | 0.4787 | ±0.9574 | +0.279 | 0.7805 | 1.1427 |  |
| Site: UCSD (vs UAB) | -0.1253 | 0.3855 | ±0.7709 | -0.325 | 0.7451 | 0.8822 |  |
| Site: UW (vs UAB) | +0.2006 | 0.2988 | ±0.5976 | +0.671 | 0.5019 | 1.2222 |  |
| **Age (years)** | **-0.0300** | 0.0133 | ±0.0266 | **-2.256** | **0.0240** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0593** | 0.0173 | ±0.0347 | **+3.424** | **6.17e-04** | 1.0611 | *** |
| Hypertension | +0.0186 | 0.2908 | ±0.5816 | +0.064 | 0.9489 | 1.0188 |  |
| High cholesterol | +0.1266 | 0.2832 | ±0.5664 | +0.447 | 0.6549 | 1.1349 |  |
| Kidney disease | +0.0994 | 0.5076 | ±1.0151 | +0.196 | 0.8448 | 1.1045 |  |
| Circulatory disease | +0.5051 | 0.3596 | ±0.7192 | +1.405 | 0.1601 | 1.6571 |  |
| MAG (mg/dL/h) | -0.0052 | 0.0166 | ±0.0331 | -0.311 | 0.7557 | 0.9949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0780**, LLR χ² = **31.72** (p = **8.47e-04**), AUC = **0.6958**, AIC = **398.9**, BIC = **447.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0788 | 1.0914 | ±2.1827 | -1.905 | 0.0568 | 0.1251 | . |
| Education: graduate level (vs college) | -0.3074 | 0.2926 | ±0.5852 | -1.051 | 0.2934 | 0.7353 |  |
| Education: high school or below (vs college) | +0.1221 | 0.4802 | ±0.9604 | +0.254 | 0.7993 | 1.1298 |  |
| Site: UCSD (vs UAB) | -0.1501 | 0.3871 | ±0.7743 | -0.388 | 0.6983 | 0.8606 |  |
| Site: UW (vs UAB) | +0.2165 | 0.2974 | ±0.5949 | +0.728 | 0.4666 | 1.2418 |  |
| **Age (years)** | **-0.0327** | 0.0136 | ±0.0271 | **-2.414** | **0.0158** | 0.9678 | * |
| **BMI (kg/m2)** | **+0.0607** | 0.0174 | ±0.0348 | **+3.487** | **4.88e-04** | 1.0625 | *** |
| Hypertension | -0.0072 | 0.2933 | ±0.5866 | -0.025 | 0.9804 | 0.9928 |  |
| High cholesterol | +0.1541 | 0.2825 | ±0.5649 | +0.546 | 0.5854 | 1.1666 |  |
| Kidney disease | +0.0254 | 0.5113 | ±1.0227 | +0.050 | 0.9604 | 1.0257 |  |
| Circulatory disease | +0.5227 | 0.3597 | ±0.7194 | +1.453 | 0.1462 | 1.6866 |  |
| Avg. daily range (mg/dL) | +0.0061 | 0.0048 | ±0.0097 | +1.256 | 0.2092 | 1.0061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0767**, LLR χ² = **31.18** (p = **0.0010**), AUC = **0.6891**, AIC = **399.5**, BIC = **447.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.7271 | 1.0235 | ±2.0470 | -1.687 | 0.0915 | 0.1778 | . |
| Education: graduate level (vs college) | -0.3271 | 0.2932 | ±0.5863 | -1.116 | 0.2646 | 0.7210 |  |
| Education: high school or below (vs college) | +0.1624 | 0.4785 | ±0.9570 | +0.339 | 0.7343 | 1.1763 |  |
| Site: UCSD (vs UAB) | -0.1304 | 0.3866 | ±0.7733 | -0.337 | 0.7359 | 0.8777 |  |
| Site: UW (vs UAB) | +0.2083 | 0.2964 | ±0.5927 | +0.703 | 0.4820 | 1.2316 |  |
| **Age (years)** | **-0.0308** | 0.0134 | ±0.0267 | **-2.304** | **0.0212** | 0.9697 | * |
| **BMI (kg/m2)** | **+0.0575** | 0.0174 | ±0.0347 | **+3.313** | **9.22e-04** | 1.0592 | *** |
| Hypertension | +0.0071 | 0.2917 | ±0.5834 | +0.024 | 0.9806 | 1.0071 |  |
| High cholesterol | +0.1360 | 0.2824 | ±0.5648 | +0.482 | 0.6302 | 1.1457 |  |
| Kidney disease | +0.0891 | 0.5069 | ±1.0138 | +0.176 | 0.8605 | 1.0932 |  |
| Circulatory disease | +0.5163 | 0.3589 | ±0.7178 | +1.438 | 0.1503 | 1.6757 |  |
| SD of daily means (mg/dL) | +0.0331 | 0.0326 | ±0.0652 | +1.015 | 0.3102 | 1.0337 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0938**, LLR χ² = **38.15** (p = **7.38e-05**), AUC = **0.7112**, AIC = **392.5**, BIC = **440.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7020 | 2.4646 | ±4.9292 | +1.908 | 0.0564 | 110.1721 | . |
| Education: graduate level (vs college) | -0.3195 | 0.2960 | ±0.5920 | -1.079 | 0.2804 | 0.7265 |  |
| Education: high school or below (vs college) | +0.1427 | 0.4803 | ±0.9607 | +0.297 | 0.7664 | 1.1534 |  |
| Site: UCSD (vs UAB) | -0.0661 | 0.3909 | ±0.7819 | -0.169 | 0.8657 | 0.9360 |  |
| Site: UW (vs UAB) | +0.2804 | 0.3024 | ±0.6049 | +0.927 | 0.3538 | 1.3237 |  |
| **Age (years)** | **-0.0343** | 0.0136 | ±0.0272 | **-2.526** | **0.0116** | 0.9663 | * |
| **BMI (kg/m2)** | **+0.0595** | 0.0174 | ±0.0348 | **+3.422** | **6.22e-04** | 1.0613 | *** |
| Hypertension | +0.0018 | 0.2960 | ±0.5921 | +0.006 | 0.9951 | 1.0018 |  |
| High cholesterol | +0.1539 | 0.2856 | ±0.5711 | +0.539 | 0.5898 | 1.1664 |  |
| Kidney disease | -0.1414 | 0.5300 | ±1.0599 | -0.267 | 0.7897 | 0.8682 |  |
| Circulatory disease | +0.6049 | 0.3634 | ±0.7267 | +1.665 | 0.0960 | 1.8310 | . |
| **Time in range 70-180, pooled (%)** | **-0.0638** | 0.0228 | ±0.0456 | **-2.802** | **0.0051** | 0.9381 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0933**, LLR χ² = **37.93** (p = **8.03e-05**), AUC = **0.7116**, AIC = **392.7**, BIC = **440.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.4155 | 2.4099 | ±4.8198 | +1.832 | 0.0669 | 82.7245 | . |
| Education: graduate level (vs college) | -0.3131 | 0.2957 | ±0.5914 | -1.059 | 0.2897 | 0.7312 |  |
| Education: high school or below (vs college) | +0.1540 | 0.4798 | ±0.9596 | +0.321 | 0.7482 | 1.1665 |  |
| Site: UCSD (vs UAB) | -0.0757 | 0.3905 | ±0.7810 | -0.194 | 0.8463 | 0.9271 |  |
| Site: UW (vs UAB) | +0.2770 | 0.3021 | ±0.6043 | +0.917 | 0.3593 | 1.3191 |  |
| **Age (years)** | **-0.0345** | 0.0136 | ±0.0272 | **-2.538** | **0.0112** | 0.9661 | * |
| **BMI (kg/m2)** | **+0.0589** | 0.0174 | ±0.0348 | **+3.388** | **7.05e-04** | 1.0606 | *** |
| Hypertension | -0.0002 | 0.2963 | ±0.5926 | -0.001 | 0.9995 | 0.9998 |  |
| High cholesterol | +0.1457 | 0.2855 | ±0.5710 | +0.510 | 0.6100 | 1.1568 |  |
| Kidney disease | -0.1306 | 0.5302 | ±1.0603 | -0.246 | 0.8054 | 0.8776 |  |
| Circulatory disease | +0.6013 | 0.3628 | ±0.7255 | +1.658 | 0.0974 | 1.8245 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.0603** | 0.0220 | ±0.0439 | **-2.744** | **0.0061** | 0.9415 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0753**, LLR χ² = **30.60** (p = **0.0013**), AUC = **0.6932**, AIC = **400.1**, BIC = **448.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5204 | 1.0225 | ±2.0451 | -1.487 | 0.1371 | 0.2186 |  |
| Education: graduate level (vs college) | -0.2930 | 0.2920 | ±0.5839 | -1.003 | 0.3156 | 0.7460 |  |
| Education: high school or below (vs college) | +0.1283 | 0.4778 | ±0.9557 | +0.268 | 0.7884 | 1.1369 |  |
| Site: UCSD (vs UAB) | -0.1639 | 0.3890 | ±0.7780 | -0.421 | 0.6735 | 0.8488 |  |
| Site: UW (vs UAB) | +0.1870 | 0.2987 | ±0.5974 | +0.626 | 0.5314 | 1.2056 |  |
| **Age (years)** | **-0.0299** | 0.0133 | ±0.0266 | **-2.252** | **0.0243** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0595** | 0.0174 | ±0.0348 | **+3.423** | **6.19e-04** | 1.0613 | *** |
| Hypertension | +0.0017 | 0.2914 | ±0.5828 | +0.006 | 0.9953 | 1.0017 |  |
| High cholesterol | +0.1163 | 0.2831 | ±0.5662 | +0.411 | 0.6814 | 1.1233 |  |
| Kidney disease | +0.1069 | 0.5082 | ±1.0164 | +0.210 | 0.8334 | 1.1128 |  |
| Circulatory disease | +0.4967 | 0.3593 | ±0.7187 | +1.382 | 0.1669 | 1.6433 |  |
| Time < 54 (%) | -0.1292 | 0.2137 | ±0.4275 | -0.604 | 0.5456 | 0.8788 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0770**, LLR χ² = **31.29** (p = **9.89e-04**), AUC = **0.6983**, AIC = **399.4**, BIC = **447.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5548 | 1.0171 | ±2.0341 | -1.529 | 0.1263 | 0.2112 |  |
| Education: graduate level (vs college) | -0.2962 | 0.2920 | ±0.5839 | -1.015 | 0.3103 | 0.7436 |  |
| Education: high school or below (vs college) | +0.1191 | 0.4780 | ±0.9561 | +0.249 | 0.8032 | 1.1265 |  |
| Site: UCSD (vs UAB) | -0.1803 | 0.3880 | ±0.7760 | -0.465 | 0.6422 | 0.8351 |  |
| Site: UW (vs UAB) | +0.1570 | 0.3004 | ±0.6008 | +0.523 | 0.6012 | 1.1700 |  |
| **Age (years)** | **-0.0291** | 0.0133 | ±0.0266 | **-2.190** | **0.0285** | 0.9713 | * |
| **BMI (kg/m2)** | **+0.0605** | 0.0175 | ±0.0350 | **+3.454** | **5.51e-04** | 1.0623 | *** |
| Hypertension | -0.0168 | 0.2923 | ±0.5846 | -0.058 | 0.9541 | 0.9833 |  |
| High cholesterol | +0.1105 | 0.2825 | ±0.5649 | +0.391 | 0.6955 | 1.1169 |  |
| Kidney disease | +0.1161 | 0.5086 | ±1.0171 | +0.228 | 0.8194 | 1.1231 |  |
| Circulatory disease | +0.4832 | 0.3602 | ±0.7203 | +1.342 | 0.1797 | 1.6213 |  |
| Avg. daily time < 54 (%) | -0.2934 | 0.3103 | ±0.6205 | -0.946 | 0.3442 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0742**, LLR χ² = **30.18** (p = **0.0015**), AUC = **0.6902**, AIC = **400.5**, BIC = **448.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5966 | 1.0203 | ±2.0406 | -1.565 | 0.1176 | 0.2026 |  |
| Education: graduate level (vs college) | -0.2996 | 0.2918 | ±0.5836 | -1.027 | 0.3045 | 0.7411 |  |
| Education: high school or below (vs college) | +0.1365 | 0.4791 | ±0.9582 | +0.285 | 0.7757 | 1.1463 |  |
| Site: UCSD (vs UAB) | -0.1262 | 0.3867 | ±0.7734 | -0.326 | 0.7441 | 0.8814 |  |
| Site: UW (vs UAB) | +0.2130 | 0.2990 | ±0.5980 | +0.713 | 0.4761 | 1.2374 |  |
| **Age (years)** | **-0.0300** | 0.0133 | ±0.0266 | **-2.253** | **0.0243** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0593** | 0.0173 | ±0.0347 | **+3.422** | **6.23e-04** | 1.0611 | *** |
| Hypertension | +0.0134 | 0.2921 | ±0.5842 | +0.046 | 0.9633 | 1.0135 |  |
| High cholesterol | +0.1378 | 0.2825 | ±0.5649 | +0.488 | 0.6257 | 1.1477 |  |
| Kidney disease | +0.1010 | 0.5071 | ±1.0141 | +0.199 | 0.8422 | 1.1062 |  |
| Circulatory disease | +0.5067 | 0.3600 | ±0.7200 | +1.408 | 0.1593 | 1.6598 |  |
| Time 54-69, pooled (%) | +0.0011 | 0.0596 | ±0.1192 | +0.018 | 0.9855 | 1.0011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0742**, LLR χ² = **30.19** (p = **0.0015**), AUC = **0.6902**, AIC = **400.5**, BIC = **448.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5908 | 1.0182 | ±2.0364 | -1.562 | 0.1182 | 0.2038 |  |
| Education: graduate level (vs college) | -0.3003 | 0.2918 | ±0.5837 | -1.029 | 0.3034 | 0.7406 |  |
| Education: high school or below (vs college) | +0.1346 | 0.4794 | ±0.9588 | +0.281 | 0.7790 | 1.1440 |  |
| Site: UCSD (vs UAB) | -0.1284 | 0.3862 | ±0.7723 | -0.332 | 0.7396 | 0.8795 |  |
| Site: UW (vs UAB) | +0.2101 | 0.2991 | ±0.5981 | +0.703 | 0.4823 | 1.2338 |  |
| **Age (years)** | **-0.0299** | 0.0133 | ±0.0266 | **-2.250** | **0.0245** | 0.9705 | * |
| **BMI (kg/m2)** | **+0.0594** | 0.0173 | ±0.0347 | **+3.423** | **6.20e-04** | 1.0612 | *** |
| Hypertension | +0.0112 | 0.2921 | ±0.5842 | +0.038 | 0.9695 | 1.0112 |  |
| High cholesterol | +0.1359 | 0.2824 | ±0.5647 | +0.481 | 0.6302 | 1.1456 |  |
| Kidney disease | +0.1009 | 0.5070 | ±1.0140 | +0.199 | 0.8423 | 1.1061 |  |
| Circulatory disease | +0.5051 | 0.3598 | ±0.7197 | +1.404 | 0.1604 | 1.6572 |  |
| Avg. daily time 54-69 (%) | -0.0033 | 0.0583 | ±0.1165 | -0.056 | 0.9550 | 0.9967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0743**, LLR χ² = **30.21** (p = **0.0015**), AUC = **0.6906**, AIC = **400.5**, BIC = **448.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5774 | 1.0215 | ±2.0430 | -1.544 | 0.1226 | 0.2065 |  |
| Education: graduate level (vs college) | -0.3004 | 0.2916 | ±0.5832 | -1.030 | 0.3030 | 0.7406 |  |
| Education: high school or below (vs college) | +0.1330 | 0.4788 | ±0.9576 | +0.278 | 0.7811 | 1.1423 |  |
| Site: UCSD (vs UAB) | -0.1337 | 0.3876 | ±0.7752 | -0.345 | 0.7301 | 0.8748 |  |
| Site: UW (vs UAB) | +0.2056 | 0.2995 | ±0.5990 | +0.686 | 0.4925 | 1.2282 |  |
| **Age (years)** | **-0.0299** | 0.0133 | ±0.0266 | **-2.248** | **0.0245** | 0.9706 | * |
| **BMI (kg/m2)** | **+0.0594** | 0.0173 | ±0.0347 | **+3.425** | **6.14e-04** | 1.0612 | *** |
| Hypertension | +0.0081 | 0.2921 | ±0.5843 | +0.028 | 0.9780 | 1.0081 |  |
| High cholesterol | +0.1325 | 0.2829 | ±0.5658 | +0.468 | 0.6395 | 1.1417 |  |
| Kidney disease | +0.1018 | 0.5071 | ±1.0141 | +0.201 | 0.8409 | 1.1072 |  |
| Circulatory disease | +0.5025 | 0.3600 | ±0.7200 | +1.396 | 0.1627 | 1.6529 |  |
| Time < 70 (%) | -0.0078 | 0.0499 | ±0.0997 | -0.157 | 0.8750 | 0.9922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0744**, LLR χ² = **30.25** (p = **0.0014**), AUC = **0.6908**, AIC = **400.4**, BIC = **448.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5760 | 1.0182 | ±2.0364 | -1.548 | 0.1217 | 0.2068 |  |
| Education: graduate level (vs college) | -0.3021 | 0.2917 | ±0.5834 | -1.036 | 0.3003 | 0.7392 |  |
| Education: high school or below (vs college) | +0.1290 | 0.4791 | ±0.9582 | +0.269 | 0.7877 | 1.1377 |  |
| Site: UCSD (vs UAB) | -0.1357 | 0.3866 | ±0.7732 | -0.351 | 0.7257 | 0.8731 |  |
| Site: UW (vs UAB) | +0.2007 | 0.2998 | ±0.5996 | +0.669 | 0.5033 | 1.2222 |  |
| **Age (years)** | **-0.0298** | 0.0133 | ±0.0266 | **-2.239** | **0.0251** | 0.9707 | * |
| **BMI (kg/m2)** | **+0.0595** | 0.0174 | ±0.0347 | **+3.428** | **6.07e-04** | 1.0613 | *** |
| Hypertension | +0.0046 | 0.2923 | ±0.5846 | +0.016 | 0.9873 | 1.0046 |  |
| High cholesterol | +0.1304 | 0.2825 | ±0.5651 | +0.461 | 0.6445 | 1.1392 |  |
| Kidney disease | +0.1015 | 0.5070 | ±1.0140 | +0.200 | 0.8414 | 1.1068 |  |
| Circulatory disease | +0.5005 | 0.3600 | ±0.7200 | +1.390 | 0.1644 | 1.6496 |  |
| Avg. daily time < 70 (%) | -0.0130 | 0.0507 | ±0.1014 | -0.257 | 0.7973 | 0.9871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0787**, LLR χ² = **32.00** (p = **7.64e-04**), AUC = **0.6947**, AIC = **398.7**, BIC = **446.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +12.2325 | 9.5522 | ±19.1045 | +1.281 | 0.2003 | 205362.9565 |  |
| Education: graduate level (vs college) | -0.3041 | 0.2922 | ±0.5843 | -1.041 | 0.2979 | 0.7378 |  |
| Education: high school or below (vs college) | +0.1495 | 0.4808 | ±0.9615 | +0.311 | 0.7558 | 1.1613 |  |
| Site: UCSD (vs UAB) | -0.0740 | 0.3892 | ±0.7783 | -0.190 | 0.8492 | 0.9287 |  |
| Site: UW (vs UAB) | +0.2648 | 0.3006 | ±0.6013 | +0.881 | 0.3784 | 1.3032 |  |
| **Age (years)** | **-0.0315** | 0.0134 | ±0.0269 | **-2.348** | **0.0189** | 0.9689 | * |
| **BMI (kg/m2)** | **+0.0602** | 0.0173 | ±0.0346 | **+3.478** | **5.04e-04** | 1.0621 | *** |
| Hypertension | +0.0219 | 0.2919 | ±0.5838 | +0.075 | 0.9403 | 1.0221 |  |
| High cholesterol | +0.1800 | 0.2843 | ±0.5686 | +0.633 | 0.5267 | 1.1972 |  |
| Kidney disease | +0.0106 | 0.5134 | ±1.0268 | +0.021 | 0.9835 | 1.0107 |  |
| Circulatory disease | +0.5434 | 0.3617 | ±0.7234 | +1.502 | 0.1330 | 1.7218 |  |
| Time 54-250, pooled (%) | -0.1390 | 0.0956 | ±0.1912 | -1.454 | 0.1459 | 0.8702 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0797**, LLR χ² = **32.41** (p = **6.55e-04**), AUC = **0.6949**, AIC = **398.2**, BIC = **446.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +15.3498 | 10.7040 | ±21.4081 | +1.434 | 0.1516 | 4638039.3872 |  |
| Education: graduate level (vs college) | -0.2979 | 0.2923 | ±0.5847 | -1.019 | 0.3082 | 0.7424 |  |
| Education: high school or below (vs college) | +0.1547 | 0.4806 | ±0.9612 | +0.322 | 0.7476 | 1.1673 |  |
| Site: UCSD (vs UAB) | -0.0776 | 0.3890 | ±0.7779 | -0.200 | 0.8418 | 0.9253 |  |
| Site: UW (vs UAB) | +0.2744 | 0.3012 | ±0.6024 | +0.911 | 0.3623 | 1.3157 |  |
| **Age (years)** | **-0.0323** | 0.0135 | ±0.0270 | **-2.395** | **0.0166** | 0.9682 | * |
| **BMI (kg/m2)** | **+0.0597** | 0.0173 | ±0.0346 | **+3.453** | **5.54e-04** | 1.0615 | *** |
| Hypertension | +0.0248 | 0.2927 | ±0.5855 | +0.085 | 0.9324 | 1.0251 |  |
| High cholesterol | +0.1727 | 0.2837 | ±0.5674 | +0.609 | 0.5428 | 1.1885 |  |
| Kidney disease | -0.0160 | 0.5174 | ±1.0348 | -0.031 | 0.9754 | 0.9842 |  |
| Circulatory disease | +0.5533 | 0.3619 | ±0.7239 | +1.529 | 0.1264 | 1.7389 |  |
| Avg. daily time 54-250 (%) | -0.1695 | 0.1067 | ±0.2134 | -1.589 | 0.1121 | 0.8441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0975**, LLR χ² = **39.65** (p = **4.11e-05**), AUC = **0.7078**, AIC = **391.0**, BIC = **439.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5085 | 1.0263 | ±2.0526 | -1.470 | 0.1416 | 0.2213 |  |
| Education: graduate level (vs college) | -0.3377 | 0.2966 | ±0.5933 | -1.138 | 0.2550 | 0.7134 |  |
| Education: high school or below (vs college) | +0.0999 | 0.4793 | ±0.9587 | +0.208 | 0.8349 | 1.1051 |  |
| Site: UCSD (vs UAB) | -0.1332 | 0.3915 | ±0.7830 | -0.340 | 0.7337 | 0.8753 |  |
| Site: UW (vs UAB) | +0.2144 | 0.3018 | ±0.6036 | +0.710 | 0.4775 | 1.2391 |  |
| **Age (years)** | **-0.0343** | 0.0136 | ±0.0271 | **-2.534** | **0.0113** | 0.9662 | * |
| **BMI (kg/m2)** | **+0.0599** | 0.0175 | ±0.0350 | **+3.425** | **6.15e-04** | 1.0617 | *** |
| Hypertension | -0.0569 | 0.2991 | ±0.5982 | -0.190 | 0.8492 | 0.9447 |  |
| High cholesterol | +0.0943 | 0.2869 | ±0.5738 | +0.329 | 0.7424 | 1.0989 |  |
| Kidney disease | -0.1603 | 0.5344 | ±1.0688 | -0.300 | 0.7643 | 0.8519 |  |
| Circulatory disease | +0.5818 | 0.3630 | ±0.7261 | +1.603 | 0.1090 | 1.7892 |  |
| **Time 181-250, pooled (%)** | **+0.0854** | 0.0288 | ±0.0576 | **+2.962** | **0.0031** | 1.0891 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0975**, LLR χ² = **39.65** (p = **4.11e-05**), AUC = **0.7090**, AIC = **391.0**, BIC = **439.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4893 | 1.0260 | ±2.0519 | -1.452 | 0.1466 | 0.2255 |  |
| Education: graduate level (vs college) | -0.3390 | 0.2967 | ±0.5934 | -1.143 | 0.2532 | 0.7125 |  |
| Education: high school or below (vs college) | +0.1030 | 0.4793 | ±0.9586 | +0.215 | 0.8298 | 1.1085 |  |
| Site: UCSD (vs UAB) | -0.1279 | 0.3914 | ±0.7828 | -0.327 | 0.7438 | 0.8799 |  |
| Site: UW (vs UAB) | +0.2116 | 0.3018 | ±0.6036 | +0.701 | 0.4832 | 1.2356 |  |
| **Age (years)** | **-0.0344** | 0.0136 | ±0.0271 | **-2.533** | **0.0113** | 0.9662 | * |
| **BMI (kg/m2)** | **+0.0596** | 0.0175 | ±0.0350 | **+3.408** | **6.55e-04** | 1.0614 | *** |
| Hypertension | -0.0585 | 0.2991 | ±0.5982 | -0.196 | 0.8448 | 0.9431 |  |
| High cholesterol | +0.0937 | 0.2870 | ±0.5740 | +0.327 | 0.7440 | 1.0982 |  |
| Kidney disease | -0.1597 | 0.5352 | ±1.0705 | -0.298 | 0.7655 | 0.8524 |  |
| Circulatory disease | +0.5839 | 0.3631 | ±0.7261 | +1.608 | 0.1078 | 1.7929 |  |
| **Avg. daily time 181-250 (%)** | **+0.0819** | 0.0279 | ±0.0558 | **+2.935** | **0.0033** | 1.0854 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0979**, LLR χ² = **39.80** (p = **3.88e-05**), AUC = **0.7097**, AIC = **390.9**, BIC = **439.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4994 | 1.0273 | ±2.0545 | -1.460 | 0.1444 | 0.2233 |  |
| Education: graduate level (vs college) | -0.3351 | 0.2969 | ±0.5939 | -1.128 | 0.2592 | 0.7153 |  |
| Education: high school or below (vs college) | +0.1042 | 0.4792 | ±0.9584 | +0.218 | 0.8278 | 1.1099 |  |
| Site: UCSD (vs UAB) | -0.1355 | 0.3918 | ±0.7836 | -0.346 | 0.7295 | 0.8733 |  |
| Site: UW (vs UAB) | +0.2203 | 0.3018 | ±0.6037 | +0.730 | 0.4654 | 1.2465 |  |
| **Age (years)** | **-0.0345** | 0.0136 | ±0.0271 | **-2.541** | **0.0111** | 0.9661 | * |
| **BMI (kg/m2)** | **+0.0599** | 0.0175 | ±0.0350 | **+3.425** | **6.15e-04** | 1.0617 | *** |
| Hypertension | -0.0552 | 0.2990 | ±0.5981 | -0.185 | 0.8535 | 0.9463 |  |
| High cholesterol | +0.1045 | 0.2867 | ±0.5735 | +0.364 | 0.7155 | 1.1102 |  |
| Kidney disease | -0.1821 | 0.5384 | ±1.0768 | -0.338 | 0.7352 | 0.8335 |  |
| Circulatory disease | +0.5849 | 0.3632 | ±0.7264 | +1.610 | 0.1073 | 1.7948 |  |
| **Time > 180 (%)** | **+0.0763** | 0.0260 | ±0.0520 | **+2.933** | **0.0034** | 1.0792 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0978**, LLR χ² = **39.76** (p = **3.94e-05**), AUC = **0.7116**, AIC = **390.9**, BIC = **439.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4770 | 1.0269 | ±2.0539 | -1.438 | 0.1504 | 0.2283 |  |
| Education: graduate level (vs college) | -0.3352 | 0.2969 | ±0.5938 | -1.129 | 0.2589 | 0.7152 |  |
| Education: high school or below (vs college) | +0.1084 | 0.4791 | ±0.9582 | +0.226 | 0.8210 | 1.1145 |  |
| Site: UCSD (vs UAB) | -0.1286 | 0.3916 | ±0.7832 | -0.328 | 0.7427 | 0.8793 |  |
| Site: UW (vs UAB) | +0.2164 | 0.3018 | ±0.6037 | +0.717 | 0.4735 | 1.2416 |  |
| **Age (years)** | **-0.0345** | 0.0136 | ±0.0272 | **-2.542** | **0.0110** | 0.9661 | * |
| **BMI (kg/m2)** | **+0.0596** | 0.0175 | ±0.0350 | **+3.405** | **6.61e-04** | 1.0614 | *** |
| Hypertension | -0.0554 | 0.2989 | ±0.5979 | -0.185 | 0.8529 | 0.9461 |  |
| High cholesterol | +0.1025 | 0.2868 | ±0.5737 | +0.357 | 0.7207 | 1.1080 |  |
| Kidney disease | -0.1796 | 0.5392 | ±1.0784 | -0.333 | 0.7391 | 0.8356 |  |
| Circulatory disease | +0.5866 | 0.3631 | ±0.7263 | +1.615 | 0.1063 | 1.7978 |  |
| **Avg. daily time > 180 (%)** | **+0.0730** | 0.0254 | ±0.0508 | **+2.876** | **0.0040** | 1.0758 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.1080**, LLR χ² = **43.92** (p = **7.52e-06**), AUC = **0.7172**, AIC = **386.7**, BIC = **434.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3714 | 1.0315 | ±2.0629 | -1.330 | 0.1837 | 0.2537 |  |
| Education: graduate level (vs college) | -0.2673 | 0.2972 | ±0.5944 | -0.899 | 0.3685 | 0.7655 |  |
| Education: high school or below (vs college) | +0.0813 | 0.4805 | ±0.9609 | +0.169 | 0.8656 | 1.0847 |  |
| Site: UCSD (vs UAB) | -0.1329 | 0.3932 | ±0.7864 | -0.338 | 0.7354 | 0.8756 |  |
| Site: UW (vs UAB) | +0.2022 | 0.3031 | ±0.6062 | +0.667 | 0.5047 | 1.2241 |  |
| **Age (years)** | **-0.0344** | 0.0136 | ±0.0273 | **-2.523** | **0.0116** | 0.9662 | * |
| **BMI (kg/m2)** | **+0.0556** | 0.0175 | ±0.0350 | **+3.176** | **0.0015** | 1.0572 | ** |
| Hypertension | -0.0934 | 0.3020 | ±0.6040 | -0.309 | 0.7572 | 0.9109 |  |
| High cholesterol | +0.1490 | 0.2883 | ±0.5766 | +0.517 | 0.6052 | 1.1607 |  |
| Kidney disease | +0.1108 | 0.5132 | ±1.0263 | +0.216 | 0.8291 | 1.1172 |  |
| Circulatory disease | +0.6667 | 0.3655 | ±0.7309 | +1.824 | 0.0681 | 1.9478 | . |
| **Nocturnal time > 180 (%)** | **+0.0986** | 0.0306 | ±0.0612 | **+3.222** | **0.0013** | 1.1036 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0825**, LLR χ² = **33.54** (p = **4.30e-04**), AUC = **0.6961**, AIC = **397.1**, BIC = **445.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6136 | 1.0198 | ±2.0396 | -1.582 | 0.1136 | 0.1992 |  |
| Education: graduate level (vs college) | -0.2824 | 0.2934 | ±0.5868 | -0.963 | 0.3358 | 0.7540 |  |
| Education: high school or below (vs college) | +0.1431 | 0.4792 | ±0.9584 | +0.299 | 0.7652 | 1.1539 |  |
| Site: UCSD (vs UAB) | -0.1682 | 0.3881 | ±0.7762 | -0.433 | 0.6648 | 0.8452 |  |
| Site: UW (vs UAB) | +0.2231 | 0.2983 | ±0.5965 | +0.748 | 0.4545 | 1.2499 |  |
| **Age (years)** | **-0.0325** | 0.0134 | ±0.0269 | **-2.419** | **0.0156** | 0.9680 | * |
| **BMI (kg/m2)** | **+0.0613** | 0.0174 | ±0.0349 | **+3.518** | **4.36e-04** | 1.0632 | *** |
| Hypertension | -0.0213 | 0.2948 | ±0.5897 | -0.072 | 0.9425 | 0.9790 |  |
| High cholesterol | +0.1387 | 0.2835 | ±0.5670 | +0.489 | 0.6247 | 1.1488 |  |
| Kidney disease | +0.0181 | 0.5159 | ±1.0319 | +0.035 | 0.9720 | 1.0183 |  |
| Circulatory disease | +0.5403 | 0.3612 | ±0.7223 | +1.496 | 0.1346 | 1.7166 |  |
| Any reading > 250 during wear (0/1) | +0.6272 | 0.3341 | ±0.6681 | +1.877 | 0.0605 | 1.8723 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0904**, LLR χ² = **36.77** (p = **1.26e-04**), AUC = **0.7091**, AIC = **393.9**, BIC = **442.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4947 | 1.0272 | ±2.0544 | -1.455 | 0.1456 | 0.2243 |  |
| Education: graduate level (vs college) | -0.3072 | 0.2959 | ±0.5918 | -1.038 | 0.2993 | 0.7355 |  |
| Education: high school or below (vs college) | +0.1380 | 0.4796 | ±0.9591 | +0.288 | 0.7736 | 1.1479 |  |
| Site: UCSD (vs UAB) | -0.1452 | 0.3927 | ±0.7854 | -0.370 | 0.7116 | 0.8649 |  |
| Site: UW (vs UAB) | +0.2411 | 0.2997 | ±0.5993 | +0.805 | 0.4210 | 1.2727 |  |
| **Age (years)** | **-0.0333** | 0.0135 | ±0.0271 | **-2.465** | **0.0137** | 0.9672 | * |
| **BMI (kg/m2)** | **+0.0599** | 0.0175 | ±0.0350 | **+3.424** | **6.16e-04** | 1.0617 | *** |
| Hypertension | -0.0202 | 0.2957 | ±0.5914 | -0.068 | 0.9456 | 0.9800 |  |
| High cholesterol | +0.1701 | 0.2855 | ±0.5709 | +0.596 | 0.5514 | 1.1854 |  |
| Kidney disease | -0.1717 | 0.5431 | ±1.0861 | -0.316 | 0.7519 | 0.8422 |  |
| Circulatory disease | +0.5686 | 0.3630 | ±0.7261 | +1.566 | 0.1173 | 1.7659 |  |
| **Time > 250 (%)** | **+0.4209** | 0.1809 | ±0.3617 | **+2.327** | **0.0199** | 1.5234 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 408)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **408**, events = **81**, McFadden pseudo-R² = **0.0897**, LLR χ² = **36.49** (p = **1.40e-04**), AUC = **0.7099**, AIC = **394.2**, BIC = **442.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4654 | 1.0274 | ±2.0547 | -1.426 | 0.1538 | 0.2310 |  |
| Education: graduate level (vs college) | -0.3054 | 0.2958 | ±0.5916 | -1.033 | 0.3018 | 0.7368 |  |
| Education: high school or below (vs college) | +0.1412 | 0.4799 | ±0.9598 | +0.294 | 0.7685 | 1.1517 |  |
| Site: UCSD (vs UAB) | -0.1317 | 0.3920 | ±0.7840 | -0.336 | 0.7369 | 0.8766 |  |
| Site: UW (vs UAB) | +0.2342 | 0.2997 | ±0.5994 | +0.782 | 0.4345 | 1.2639 |  |
| **Age (years)** | **-0.0334** | 0.0135 | ±0.0271 | **-2.467** | **0.0136** | 0.9671 | * |
| **BMI (kg/m2)** | **+0.0593** | 0.0175 | ±0.0349 | **+3.397** | **6.81e-04** | 1.0611 | *** |
| Hypertension | -0.0139 | 0.2953 | ±0.5906 | -0.047 | 0.9626 | 0.9862 |  |
| High cholesterol | +0.1593 | 0.2852 | ±0.5704 | +0.558 | 0.5766 | 1.1727 |  |
| Kidney disease | -0.1550 | 0.5405 | ±1.0810 | -0.287 | 0.7743 | 0.8564 |  |
| Circulatory disease | +0.5697 | 0.3627 | ±0.7254 | +1.571 | 0.1163 | 1.7677 |  |
| **Avg. daily time > 250 (%)** | **+0.3868** | 0.1769 | ±0.3538 | **+2.186** | **0.0288** | 1.4722 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 60 single-predictor tests; 12 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 408): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.078 vs 0.055 for covariates alone, gain +0.023; +0.813 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): %>180 nocturnal (p = 0.001).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 408): best single predictor out of sample is **%>180 nocturnal** (CV AUC 0.634 vs 0.609 for covariates alone, gain +0.025; OR 1.57 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): %>180 nocturnal (p = 0.001), %181-250 (pooled) (p = 0.003), %181-250 (daily avg) (p = 0.003), %>180 (pooled) (p = 0.003), %>180 (daily avg) (p = 0.004).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.025, via %>180 nocturnal); CES-D-10 depressive symptoms (0-30) (+0.023, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 180 (0 FDR-significant / 4 raw-significant of 6); CGM variability (0 FDR-significant / 2 raw-significant of 16); Range 70-180 (0 FDR-significant / 2 raw-significant of 4).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%>180 nocturnal, ΔAIC -11.2); Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -10.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
