# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 393; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0615**, F-statistic = **3.57** (p = **1.53e-04**), Residual SE = **4.401** on **382** df, AIC = **2290.8**, BIC = **2334.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2725** | 1.7826 | ±3.5651 | **+4.641** | **3.47e-06** | *** |
| Education: graduate level (vs college) | -0.4633 | 0.4776 | ±0.9553 | -0.970 | 0.3321 |  |
| Education: high school or below (vs college) | +0.8485 | 0.9154 | ±1.8307 | +0.927 | 0.3539 |  |
| Site: UCSD (vs UAB) | -0.7089 | 0.5593 | ±1.1187 | -1.267 | 0.2050 |  |
| Site: UW (vs UAB) | -0.0976 | 0.6136 | ±1.2271 | -0.159 | 0.8736 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.824** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0351 | ±0.0703 | +1.881 | 0.0600 | . |
| Hypertension | +0.5328 | 0.5323 | ±1.0646 | +1.001 | 0.3169 |  |
| High cholesterol | +0.6718 | 0.4857 | ±0.9713 | +1.383 | 0.1665 |  |
| Kidney disease | +0.8591 | 0.8844 | ±1.7687 | +0.971 | 0.3313 |  |
| Circulatory disease | +1.3896 | 0.8270 | ±1.6540 | +1.680 | 0.0929 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.96e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4977** | 4.6602 | ±9.3203 | **+2.038** | **0.0415** | * |
| Education: graduate level (vs college) | -0.4647 | 0.4780 | ±0.9560 | -0.972 | 0.3309 |  |
| Education: high school or below (vs college) | +0.8548 | 0.9192 | ±1.8383 | +0.930 | 0.3524 |  |
| Site: UCSD (vs UAB) | -0.7148 | 0.5639 | ±1.1278 | -1.268 | 0.2050 |  |
| Site: UW (vs UAB) | -0.1077 | 0.6190 | ±1.2380 | -0.174 | 0.8618 |  |
| **Age (years)** | **-0.0806** | 0.0214 | ±0.0429 | **-3.762** | **1.69e-04** | *** |
| BMI (kg/m2) | +0.0670 | 0.0355 | ±0.0710 | +1.889 | 0.0589 | . |
| Hypertension | +0.5455 | 0.5291 | ±1.0583 | +1.031 | 0.3026 |  |
| High cholesterol | +0.6985 | 0.5065 | ±1.0131 | +1.379 | 0.1679 |  |
| Kidney disease | +0.8394 | 0.8917 | ±1.7833 | +0.941 | 0.3465 |  |
| Circulatory disease | +1.3813 | 0.8291 | ±1.6581 | +1.666 | 0.0957 | . |
| HbA1c (%) | -0.2348 | 0.8152 | ±1.6303 | -0.288 | 0.7733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2350** | 3.6545 | ±7.3090 | **+2.527** | **0.0115** | * |
| Education: graduate level (vs college) | -0.4605 | 0.4790 | ±0.9580 | -0.961 | 0.3364 |  |
| Education: high school or below (vs college) | +0.8438 | 0.9169 | ±1.8337 | +0.920 | 0.3574 |  |
| Site: UCSD (vs UAB) | -0.6997 | 0.5663 | ±1.1326 | -1.236 | 0.2166 |  |
| Site: UW (vs UAB) | -0.0870 | 0.6240 | ±1.2480 | -0.139 | 0.8891 |  |
| **Age (years)** | **-0.0815** | 0.0212 | ±0.0424 | **-3.844** | **1.21e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0351 | ±0.0702 | +1.902 | 0.0571 | . |
| Hypertension | +0.5421 | 0.5356 | ±1.0711 | +1.012 | 0.3114 |  |
| High cholesterol | +0.6648 | 0.4884 | ±0.9767 | +1.361 | 0.1734 |  |
| Kidney disease | +0.8691 | 0.8844 | ±1.7687 | +0.983 | 0.3258 |  |
| Circulatory disease | +1.3917 | 0.8285 | ±1.6569 | +1.680 | 0.0930 | . |
| Mean glucose (mg/dL) | -0.0086 | 0.0300 | ±0.0599 | -0.286 | 0.7750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.4199 | 7.5510 | ±15.1020 | +1.380 | 0.1676 |  |
| Education: graduate level (vs college) | -0.4605 | 0.4790 | ±0.9580 | -0.961 | 0.3364 |  |
| Education: high school or below (vs college) | +0.8438 | 0.9169 | ±1.8337 | +0.920 | 0.3574 |  |
| Site: UCSD (vs UAB) | -0.6997 | 0.5663 | ±1.1326 | -1.236 | 0.2166 |  |
| Site: UW (vs UAB) | -0.0870 | 0.6240 | ±1.2480 | -0.139 | 0.8891 |  |
| **Age (years)** | **-0.0815** | 0.0212 | ±0.0424 | **-3.844** | **1.21e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0351 | ±0.0702 | +1.902 | 0.0571 | . |
| Hypertension | +0.5421 | 0.5356 | ±1.0711 | +1.012 | 0.3114 |  |
| High cholesterol | +0.6648 | 0.4884 | ±0.9767 | +1.361 | 0.1734 |  |
| Kidney disease | +0.8691 | 0.8844 | ±1.7687 | +0.983 | 0.3258 |  |
| Circulatory disease | +1.3917 | 0.8285 | ±1.6569 | +1.680 | 0.0930 | . |
| GMI (%) | -0.3580 | 1.2526 | ±2.5052 | -0.286 | 0.7750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, R² = **0.0870**, Adj R² = **0.0606**, F-statistic = **3.30** (p = **2.42e-04**), Residual SE = **4.403** on **381** df, AIC = **2292.1**, BIC = **2339.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4350** | 3.0817 | ±6.1634 | **+3.386** | **7.09e-04** | *** |
| Education: graduate level (vs college) | -0.4765 | 0.4791 | ±0.9582 | -0.994 | 0.3200 |  |
| Education: high school or below (vs college) | +0.8219 | 0.9141 | ±1.8281 | +0.899 | 0.3685 |  |
| Site: UCSD (vs UAB) | -0.6631 | 0.5702 | ±1.1403 | -1.163 | 0.2448 |  |
| Site: UW (vs UAB) | -0.0577 | 0.6274 | ±1.2549 | -0.092 | 0.9267 |  |
| **Age (years)** | **-0.0836** | 0.0210 | ±0.0420 | **-3.985** | **6.75e-05** | *** |
| **BMI (kg/m2)** | **+0.0705** | 0.0356 | ±0.0711 | **+1.982** | **0.0474** | * |
| Hypertension | +0.5457 | 0.5329 | ±1.0658 | +1.024 | 0.3058 |  |
| High cholesterol | +0.6675 | 0.4866 | ±0.9732 | +1.372 | 0.1702 |  |
| Kidney disease | +0.8535 | 0.8838 | ±1.7676 | +0.966 | 0.3342 |  |
| Circulatory disease | +1.3880 | 0.8293 | ±1.6587 | +1.674 | 0.0942 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0189 | 0.0230 | ±0.0461 | -0.821 | 0.4119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0878**, Adj R² = **0.0614**, F-statistic = **3.33** (p = **2.12e-04**), Residual SE = **4.401** on **381** df, AIC = **2291.8**, BIC = **2339.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.6087** | 2.4517 | ±4.9034 | **+2.696** | **0.0070** | ** |
| Education: graduate level (vs college) | -0.4304 | 0.4829 | ±0.9657 | -0.891 | 0.3727 |  |
| Education: high school or below (vs college) | +0.8452 | 0.9186 | ±1.8371 | +0.920 | 0.3575 |  |
| Site: UCSD (vs UAB) | -0.6600 | 0.5599 | ±1.1197 | -1.179 | 0.2385 |  |
| Site: UW (vs UAB) | -0.0675 | 0.6130 | ±1.2260 | -0.110 | 0.9123 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0647 | 0.0351 | ±0.0702 | +1.842 | 0.0654 | . |
| Hypertension | +0.5254 | 0.5328 | ±1.0657 | +0.986 | 0.3241 |  |
| High cholesterol | +0.6973 | 0.4875 | ±0.9750 | +1.430 | 0.1526 |  |
| Kidney disease | +0.7977 | 0.8692 | ±1.7384 | +0.918 | 0.3588 |  |
| Circulatory disease | +1.3747 | 0.8275 | ±1.6549 | +1.661 | 0.0966 | . |
| Glucose SD, pooled (mg/dL) | +0.0992 | 0.1016 | ±0.2031 | +0.977 | 0.3288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0858**, Adj R² = **0.0594**, F-statistic = **3.25** (p = **2.91e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.6**, BIC = **2340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.6986** | 2.2995 | ±4.5990 | **+3.348** | **8.14e-04** | *** |
| Education: graduate level (vs college) | -0.4506 | 0.4814 | ±0.9628 | -0.936 | 0.3493 |  |
| Education: high school or below (vs college) | +0.8514 | 0.9178 | ±1.8355 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.6882 | 0.5573 | ±1.1146 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -0.0852 | 0.6127 | ±1.2255 | -0.139 | 0.8894 |  |
| **Age (years)** | **-0.0812** | 0.0213 | ±0.0426 | **-3.816** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0651 | 0.0353 | ±0.0705 | +1.845 | 0.0651 | . |
| Hypertension | +0.5343 | 0.5344 | ±1.0688 | +1.000 | 0.3174 |  |
| High cholesterol | +0.6798 | 0.4880 | ±0.9760 | +1.393 | 0.1637 |  |
| Kidney disease | +0.8360 | 0.8808 | ±1.7616 | +0.949 | 0.3426 |  |
| Circulatory disease | +1.3873 | 0.8274 | ±1.6549 | +1.677 | 0.0936 | . |
| Avg. daily SD (mg/dL) | +0.0379 | 0.1045 | ±0.2091 | +0.363 | 0.7168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, R² = **0.0883**, Adj R² = **0.0620**, F-statistic = **3.36** (p = **1.93e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.5**, BIC = **2339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4667** | 2.4484 | ±4.8967 | **+2.641** | **0.0083** | ** |
| Education: graduate level (vs college) | -0.4227 | 0.4828 | ±0.9657 | -0.875 | 0.3813 |  |
| Education: high school or below (vs college) | +0.8369 | 0.9171 | ±1.8343 | +0.913 | 0.3615 |  |
| Site: UCSD (vs UAB) | -0.6408 | 0.5650 | ±1.1299 | -1.134 | 0.2567 |  |
| Site: UW (vs UAB) | -0.0458 | 0.6182 | ±1.2365 | -0.074 | 0.9410 |  |
| **Age (years)** | **-0.0816** | 0.0213 | ±0.0426 | **-3.831** | **1.28e-04** | *** |
| BMI (kg/m2) | +0.0658 | 0.0350 | ±0.0700 | +1.879 | 0.0603 | . |
| Hypertension | +0.5411 | 0.5333 | ±1.0666 | +1.015 | 0.3103 |  |
| High cholesterol | +0.6888 | 0.4860 | ±0.9719 | +1.417 | 0.1563 |  |
| Kidney disease | +0.8133 | 0.8704 | ±1.7408 | +0.934 | 0.3501 |  |
| Circulatory disease | +1.3758 | 0.8293 | ±1.6586 | +1.659 | 0.0971 | . |
| CV (%) | +0.1205 | 0.1072 | ±0.2145 | +1.123 | 0.2613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, R² = **0.0887**, Adj R² = **0.0624**, F-statistic = **3.37** (p = **1.84e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.4**, BIC = **2339.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0284** | 2.2370 | ±4.4740 | **+4.483** | **7.36e-06** | *** |
| Education: graduate level (vs college) | -0.4154 | 0.4830 | ±0.9661 | -0.860 | 0.3898 |  |
| Education: high school or below (vs college) | +0.8367 | 0.9164 | ±1.8328 | +0.913 | 0.3613 |  |
| Site: UCSD (vs UAB) | -0.6533 | 0.5621 | ±1.1242 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -0.0583 | 0.6151 | ±1.2302 | -0.095 | 0.9245 |  |
| **Age (years)** | **-0.0814** | 0.0213 | ±0.0426 | **-3.822** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0659 | 0.0351 | ±0.0702 | +1.879 | 0.0603 | . |
| Hypertension | +0.5317 | 0.5323 | ±1.0647 | +0.999 | 0.3179 |  |
| High cholesterol | +0.6923 | 0.4859 | ±0.9719 | +1.425 | 0.1542 |  |
| Kidney disease | +0.8267 | 0.8690 | ±1.7380 | +0.951 | 0.3414 |  |
| Circulatory disease | +1.3767 | 0.8282 | ±1.6564 | +1.662 | 0.0965 | . |
| Mean / SD ratio | -0.2596 | 0.2077 | ±0.4154 | -1.250 | 0.2114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0858**, Adj R² = **0.0594**, F-statistic = **3.25** (p = **2.90e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.6**, BIC = **2340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.8214** | 2.3611 | ±4.7222 | **+3.736** | **1.87e-04** | *** |
| Education: graduate level (vs college) | -0.4473 | 0.4810 | ±0.9619 | -0.930 | 0.3523 |  |
| Education: high school or below (vs college) | +0.8484 | 0.9163 | ±1.8325 | +0.926 | 0.3545 |  |
| Site: UCSD (vs UAB) | -0.6877 | 0.5591 | ±1.1182 | -1.230 | 0.2187 |  |
| Site: UW (vs UAB) | -0.0851 | 0.6144 | ±1.2289 | -0.138 | 0.8899 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0653 | 0.0353 | ±0.0706 | +1.849 | 0.0645 | . |
| Hypertension | +0.5389 | 0.5350 | ±1.0700 | +1.007 | 0.3138 |  |
| High cholesterol | +0.6758 | 0.4873 | ±0.9745 | +1.387 | 0.1655 |  |
| Kidney disease | +0.8453 | 0.8826 | ±1.7651 | +0.958 | 0.3382 |  |
| Circulatory disease | +1.3882 | 0.8279 | ±1.6557 | +1.677 | 0.0936 | . |
| Avg. daily mean/SD | -0.0696 | 0.1831 | ±0.3662 | -0.380 | 0.7040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, R² = **0.1010**, Adj R² = **0.0750**, F-statistic = **3.89** (p = **2.38e-05**), Residual SE = **4.369** on **381** df, AIC = **2286.1**, BIC = **2333.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.2485 | 2.1681 | ±4.3362 | +1.960 | 0.0500 | . |
| Education: graduate level (vs college) | -0.4734 | 0.4775 | ±0.9550 | -0.991 | 0.3215 |  |
| Education: high school or below (vs college) | +0.6992 | 0.8907 | ±1.7815 | +0.785 | 0.4325 |  |
| Site: UCSD (vs UAB) | -0.6208 | 0.5459 | ±1.0917 | -1.137 | 0.2554 |  |
| Site: UW (vs UAB) | +0.0683 | 0.5962 | ±1.1925 | +0.115 | 0.9088 |  |
| **Age (years)** | **-0.0747** | 0.0213 | ±0.0425 | **-3.514** | **4.42e-04** | *** |
| **BMI (kg/m2)** | **+0.0720** | 0.0339 | ±0.0679 | **+2.122** | **0.0338** | * |
| Hypertension | +0.5919 | 0.5310 | ±1.0620 | +1.115 | 0.2650 |  |
| High cholesterol | +0.5914 | 0.4837 | ±0.9674 | +1.223 | 0.2214 |  |
| Kidney disease | +0.7399 | 0.8578 | ±1.7157 | +0.863 | 0.3884 |  |
| Circulatory disease | +1.3943 | 0.8189 | ±1.6377 | +1.703 | 0.0886 | . |
| **MAG (mg/dL/h)** | **+0.0996** | 0.0378 | ±0.0756 | **+2.636** | **0.0084** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, R² = **0.0875**, Adj R² = **0.0611**, F-statistic = **3.32** (p = **2.23e-04**), Residual SE = **4.402** on **381** df, AIC = **2291.9**, BIC = **2339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.6516** | 2.3592 | ±4.7184 | **+2.819** | **0.0048** | ** |
| Education: graduate level (vs college) | -0.4493 | 0.4788 | ±0.9575 | -0.938 | 0.3480 |  |
| Education: high school or below (vs college) | +0.8534 | 0.9111 | ±1.8222 | +0.937 | 0.3489 |  |
| Site: UCSD (vs UAB) | -0.6662 | 0.5550 | ±1.1100 | -1.200 | 0.2300 |  |
| Site: UW (vs UAB) | -0.0663 | 0.6100 | ±1.2200 | -0.109 | 0.9135 |  |
| **Age (years)** | **-0.0809** | 0.0213 | ±0.0425 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | +0.0684 | 0.0355 | ±0.0711 | +1.924 | 0.0544 | . |
| Hypertension | +0.5544 | 0.5340 | ±1.0680 | +1.038 | 0.2992 |  |
| High cholesterol | +0.6669 | 0.4866 | ±0.9732 | +1.370 | 0.1706 |  |
| Kidney disease | +0.8281 | 0.8655 | ±1.7311 | +0.957 | 0.3387 |  |
| Circulatory disease | +1.3779 | 0.8257 | ±1.6514 | +1.669 | 0.0952 | . |
| Avg. daily range (mg/dL) | +0.0188 | 0.0200 | ±0.0401 | +0.939 | 0.3476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, R² = **0.0913**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.20e-04**), Residual SE = **4.392** on **381** df, AIC = **2290.3**, BIC = **2338.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3475** | 1.9054 | ±3.8107 | **+3.856** | **1.15e-04** | *** |
| Education: graduate level (vs college) | -0.4880 | 0.4752 | ±0.9505 | -1.027 | 0.3045 |  |
| Education: high school or below (vs college) | +0.7754 | 0.9333 | ±1.8667 | +0.831 | 0.4061 |  |
| Site: UCSD (vs UAB) | -0.6897 | 0.5604 | ±1.1208 | -1.231 | 0.2184 |  |
| Site: UW (vs UAB) | -0.1352 | 0.6124 | ±1.2247 | -0.221 | 0.8252 |  |
| **Age (years)** | **-0.0818** | 0.0214 | ±0.0427 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0656 | 0.0349 | ±0.0699 | +1.877 | 0.0606 | . |
| Hypertension | +0.4842 | 0.5276 | ±1.0551 | +0.918 | 0.3587 |  |
| High cholesterol | +0.6512 | 0.4853 | ±0.9706 | +1.342 | 0.1796 |  |
| Kidney disease | +0.9175 | 0.8977 | ±1.7955 | +1.022 | 0.3068 |  |
| Circulatory disease | +1.3441 | 0.8321 | ±1.6642 | +1.615 | 0.1063 |  |
| SD of daily means (mg/dL) | +0.2011 | 0.1288 | ±0.2576 | +1.561 | 0.1185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, R² = **0.0861**, Adj R² = **0.0597**, F-statistic = **3.26** (p = **2.77e-04**), Residual SE = **4.405** on **381** df, AIC = **2292.5**, BIC = **2340.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +47.1756 | 67.2035 | ±134.4070 | +0.702 | 0.4827 |  |
| Education: graduate level (vs college) | -0.4575 | 0.4779 | ±0.9557 | -0.957 | 0.3384 |  |
| Education: high school or below (vs college) | +0.8518 | 0.9158 | ±1.8315 | +0.930 | 0.3523 |  |
| Site: UCSD (vs UAB) | -0.6916 | 0.5585 | ±1.1171 | -1.238 | 0.2156 |  |
| Site: UW (vs UAB) | -0.0823 | 0.6132 | ±1.2265 | -0.134 | 0.8933 |  |
| **Age (years)** | **-0.0808** | 0.0213 | ±0.0426 | **-3.796** | **1.47e-04** | *** |
| BMI (kg/m2) | +0.0672 | 0.0358 | ±0.0716 | +1.877 | 0.0605 | . |
| Hypertension | +0.5283 | 0.5325 | ±1.0649 | +0.992 | 0.3211 |  |
| High cholesterol | +0.6605 | 0.4875 | ±0.9750 | +1.355 | 0.1754 |  |
| Kidney disease | +0.8348 | 0.8709 | ±1.7417 | +0.959 | 0.3378 |  |
| Circulatory disease | +1.3848 | 0.8285 | ±1.6570 | +1.671 | 0.0946 | . |
| Time in range 70-180, pooled (%) | -0.3915 | 0.6751 | ±1.3502 | -0.580 | 0.5620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.93e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +33.4258 | 67.4653 | ±134.9306 | +0.495 | 0.6203 |  |
| Education: graduate level (vs college) | -0.4599 | 0.4775 | ±0.9550 | -0.963 | 0.3355 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9149 | ±1.8298 | +0.934 | 0.3505 |  |
| Site: UCSD (vs UAB) | -0.7024 | 0.5590 | ±1.1180 | -1.257 | 0.2089 |  |
| Site: UW (vs UAB) | -0.0966 | 0.6143 | ±1.2286 | -0.157 | 0.8751 |  |
| **Age (years)** | **-0.0807** | 0.0212 | ±0.0425 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | +0.0664 | 0.0352 | ±0.0705 | +1.883 | 0.0596 | . |
| Hypertension | +0.5380 | 0.5348 | ±1.0696 | +1.006 | 0.3144 |  |
| High cholesterol | +0.6617 | 0.4882 | ±0.9764 | +1.355 | 0.1753 |  |
| Kidney disease | +0.8566 | 0.8795 | ±1.7591 | +0.974 | 0.3301 |  |
| Circulatory disease | +1.3796 | 0.8266 | ±1.6532 | +1.669 | 0.0951 | . |
| Avg. daily time in range 70-180 (%) | -0.2529 | 0.6765 | ±1.3530 | -0.374 | 0.7085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0882**, Adj R² = **0.0618**, F-statistic = **3.35** (p = **1.99e-04**), Residual SE = **4.400** on **381** df, AIC = **2291.6**, BIC = **2339.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4222** | 1.7883 | ±3.5766 | **+4.710** | **2.48e-06** | *** |
| Education: graduate level (vs college) | -0.4768 | 0.4787 | ±0.9575 | -0.996 | 0.3192 |  |
| Education: high school or below (vs college) | +0.8212 | 0.9248 | ±1.8496 | +0.888 | 0.3746 |  |
| Site: UCSD (vs UAB) | -0.8157 | 0.5735 | ±1.1470 | -1.422 | 0.1549 |  |
| Site: UW (vs UAB) | -0.1674 | 0.6193 | ±1.2386 | -0.270 | 0.7869 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0425 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0352 | ±0.0705 | +1.879 | 0.0603 | . |
| Hypertension | +0.5736 | 0.5344 | ±1.0689 | +1.073 | 0.2831 |  |
| High cholesterol | +0.6742 | 0.4852 | ±0.9704 | +1.390 | 0.1647 |  |
| Kidney disease | +0.7900 | 0.8832 | ±1.7663 | +0.895 | 0.3710 |  |
| Circulatory disease | +1.4194 | 0.8291 | ±1.6582 | +1.712 | 0.0869 | . |
| Any reading < 54 during wear (0/1) | -0.6540 | 0.6311 | ±1.2622 | -1.036 | 0.3000 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0634**, F-statistic = **3.41** (p = **1.56e-04**), Residual SE = **4.396** on **381** df, AIC = **2291.0**, BIC = **2338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3862** | 1.8009 | ±3.6018 | **+4.657** | **3.21e-06** | *** |
| Education: graduate level (vs college) | -0.4753 | 0.4782 | ±0.9563 | -0.994 | 0.3202 |  |
| Education: high school or below (vs college) | +0.7829 | 0.9170 | ±1.8341 | +0.854 | 0.3933 |  |
| Site: UCSD (vs UAB) | -0.8081 | 0.5644 | ±1.1288 | -1.432 | 0.1522 |  |
| Site: UW (vs UAB) | -0.1510 | 0.6139 | ±1.2278 | -0.246 | 0.8057 |  |
| **Age (years)** | **-0.0823** | 0.0212 | ±0.0425 | **-3.871** | **1.08e-04** | *** |
| BMI (kg/m2) | +0.0692 | 0.0357 | ±0.0714 | +1.940 | 0.0524 | . |
| Hypertension | +0.5827 | 0.5328 | ±1.0655 | +1.094 | 0.2741 |  |
| High cholesterol | +0.6658 | 0.4842 | ±0.9684 | +1.375 | 0.1691 |  |
| Kidney disease | +0.7964 | 0.8827 | ±1.7654 | +0.902 | 0.3670 |  |
| Circulatory disease | +1.4625 | 0.8381 | ±1.6762 | +1.745 | 0.0810 | . |
| Time < 54 (%) | -5.9692 | 4.9258 | ±9.8516 | -1.212 | 0.2256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0634**, F-statistic = **3.41** (p = **1.56e-04**), Residual SE = **4.396** on **381** df, AIC = **2291.0**, BIC = **2338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3328** | 1.7921 | ±3.5842 | **+4.650** | **3.32e-06** | *** |
| Education: graduate level (vs college) | -0.4575 | 0.4765 | ±0.9530 | -0.960 | 0.3370 |  |
| Education: high school or below (vs college) | +0.8189 | 0.9146 | ±1.8291 | +0.895 | 0.3706 |  |
| Site: UCSD (vs UAB) | -0.7617 | 0.5576 | ±1.1152 | -1.366 | 0.1719 |  |
| Site: UW (vs UAB) | -0.1179 | 0.6142 | ±1.2284 | -0.192 | 0.8477 |  |
| **Age (years)** | **-0.0818** | 0.0212 | ±0.0424 | **-3.860** | **1.13e-04** | *** |
| BMI (kg/m2) | +0.0681 | 0.0354 | ±0.0709 | +1.922 | 0.0546 | . |
| Hypertension | +0.5581 | 0.5325 | ±1.0650 | +1.048 | 0.2946 |  |
| High cholesterol | +0.6647 | 0.4845 | ±0.9690 | +1.372 | 0.1701 |  |
| Kidney disease | +0.8195 | 0.8818 | ±1.7636 | +0.929 | 0.3527 |  |
| Circulatory disease | +1.4908 | 0.8449 | ±1.6899 | +1.764 | 0.0777 | . |
| Avg. daily time < 54 (%) | -7.0830 | 6.3729 | ±12.7458 | -1.111 | 0.2664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0884**, Adj R² = **0.0621**, F-statistic = **3.36** (p = **1.91e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.5**, BIC = **2339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0309** | 1.7877 | ±3.5754 | **+4.492** | **7.05e-06** | *** |
| Education: graduate level (vs college) | -0.4361 | 0.4762 | ±0.9523 | -0.916 | 0.3597 |  |
| Education: high school or below (vs college) | +0.8119 | 0.9203 | ±1.8407 | +0.882 | 0.3777 |  |
| Site: UCSD (vs UAB) | -0.6665 | 0.5607 | ±1.1213 | -1.189 | 0.2346 |  |
| Site: UW (vs UAB) | -0.0409 | 0.6179 | ±1.2357 | -0.066 | 0.9472 |  |
| **Age (years)** | **-0.0814** | 0.0213 | ±0.0425 | **-3.832** | **1.27e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0349 | ±0.0697 | +1.917 | 0.0552 | . |
| Hypertension | +0.5825 | 0.5331 | ±1.0663 | +1.093 | 0.2745 |  |
| High cholesterol | +0.6079 | 0.4883 | ±0.9765 | +1.245 | 0.2131 |  |
| Kidney disease | +0.9345 | 0.8858 | ±1.7716 | +1.055 | 0.2914 |  |
| Circulatory disease | +1.3956 | 0.8313 | ±1.6626 | +1.679 | 0.0932 | . |
| Time 54-69, pooled (%) | +1.4014 | 1.1837 | ±2.3674 | +1.184 | 0.2364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, R² = **0.0865**, Adj R² = **0.0601**, F-statistic = **3.28** (p = **2.60e-04**), Residual SE = **4.404** on **381** df, AIC = **2292.3**, BIC = **2340.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1532** | 1.7863 | ±3.5725 | **+4.564** | **5.01e-06** | *** |
| Education: graduate level (vs college) | -0.4412 | 0.4757 | ±0.9514 | -0.928 | 0.3537 |  |
| Education: high school or below (vs college) | +0.8259 | 0.9209 | ±1.8418 | +0.897 | 0.3698 |  |
| Site: UCSD (vs UAB) | -0.6977 | 0.5603 | ±1.1205 | -1.245 | 0.2130 |  |
| Site: UW (vs UAB) | -0.0836 | 0.6161 | ±1.2323 | -0.136 | 0.8920 |  |
| **Age (years)** | **-0.0815** | 0.0213 | ±0.0425 | **-3.832** | **1.27e-04** | *** |
| BMI (kg/m2) | +0.0664 | 0.0350 | ±0.0701 | +1.896 | 0.0580 | . |
| Hypertension | +0.5822 | 0.5390 | ±1.0781 | +1.080 | 0.2801 |  |
| High cholesterol | +0.6435 | 0.4890 | ±0.9781 | +1.316 | 0.1882 |  |
| Kidney disease | +0.9006 | 0.8848 | ±1.7695 | +1.018 | 0.3087 |  |
| Circulatory disease | +1.3798 | 0.8319 | ±1.6637 | +1.659 | 0.0972 | . |
| Avg. daily time 54-69 (%) | +0.8445 | 1.2348 | ±2.4696 | +0.684 | 0.4940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, R² = **0.0865**, Adj R² = **0.0601**, F-statistic = **3.28** (p = **2.60e-04**), Residual SE = **4.404** on **381** df, AIC = **2292.3**, BIC = **2340.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1303** | 1.7901 | ±3.5803 | **+4.542** | **5.58e-06** | *** |
| Education: graduate level (vs college) | -0.4474 | 0.4787 | ±0.9573 | -0.935 | 0.3500 |  |
| Education: high school or below (vs college) | +0.8373 | 0.9181 | ±1.8363 | +0.912 | 0.3618 |  |
| Site: UCSD (vs UAB) | -0.6741 | 0.5614 | ±1.1228 | -1.201 | 0.2298 |  |
| Site: UW (vs UAB) | -0.0609 | 0.6183 | ±1.2366 | -0.098 | 0.9215 |  |
| **Age (years)** | **-0.0812** | 0.0213 | ±0.0426 | **-3.813** | **1.37e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0350 | ±0.0700 | +1.888 | 0.0591 | . |
| Hypertension | +0.5529 | 0.5352 | ±1.0703 | +1.033 | 0.3015 |  |
| High cholesterol | +0.6387 | 0.4897 | ±0.9795 | +1.304 | 0.1922 |  |
| Kidney disease | +0.9069 | 0.8880 | ±1.7760 | +1.021 | 0.3071 |  |
| Circulatory disease | +1.3837 | 0.8310 | ±1.6620 | +1.665 | 0.0959 | . |
| Time < 70 (%) | +0.7427 | 1.1001 | ±2.2001 | +0.675 | 0.4996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.96e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2185** | 1.7885 | ±3.5770 | **+4.595** | **4.32e-06** | *** |
| Education: graduate level (vs college) | -0.4541 | 0.4781 | ±0.9562 | -0.950 | 0.3422 |  |
| Education: high school or below (vs college) | +0.8404 | 0.9202 | ±1.8404 | +0.913 | 0.3611 |  |
| Site: UCSD (vs UAB) | -0.7014 | 0.5599 | ±1.1198 | -1.253 | 0.2103 |  |
| Site: UW (vs UAB) | -0.0906 | 0.6166 | ±1.2333 | -0.147 | 0.8832 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.818** | **1.34e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0352 | ±0.0703 | +1.881 | 0.0600 | . |
| Hypertension | +0.5526 | 0.5398 | ±1.0796 | +1.024 | 0.3060 |  |
| High cholesterol | +0.6601 | 0.4900 | ±0.9800 | +1.347 | 0.1779 |  |
| Kidney disease | +0.8788 | 0.8872 | ±1.7744 | +0.991 | 0.3219 |  |
| Circulatory disease | +1.3803 | 0.8326 | ±1.6652 | +1.658 | 0.0974 | . |
| Avg. daily time < 70 (%) | +0.3605 | 1.1565 | ±2.3129 | +0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0635**, F-statistic = **3.41** (p = **1.54e-04**), Residual SE = **4.396** on **381** df, AIC = **2290.9**, BIC = **2338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -591.8577 | 487.5781 | ±975.1563 | -1.214 | 0.2248 |  |
| Education: graduate level (vs college) | -0.4799 | 0.4785 | ±0.9571 | -1.003 | 0.3159 |  |
| Education: high school or below (vs college) | +0.7787 | 0.9174 | ±1.8348 | +0.849 | 0.3960 |  |
| Site: UCSD (vs UAB) | -0.8090 | 0.5644 | ±1.1288 | -1.433 | 0.1517 |  |
| Site: UW (vs UAB) | -0.1478 | 0.6135 | ±1.2270 | -0.241 | 0.8097 |  |
| **Age (years)** | **-0.0824** | 0.0213 | ±0.0425 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | +0.0690 | 0.0356 | ±0.0712 | +1.938 | 0.0526 | . |
| Hypertension | +0.5812 | 0.5326 | ±1.0652 | +1.091 | 0.2751 |  |
| High cholesterol | +0.6712 | 0.4844 | ±0.9688 | +1.386 | 0.1659 |  |
| Kidney disease | +0.7949 | 0.8826 | ±1.7653 | +0.901 | 0.3678 |  |
| Circulatory disease | +1.4623 | 0.8379 | ±1.6759 | +1.745 | 0.0810 | . |
| Time 54-250, pooled (%) | +6.0026 | 4.8772 | ±9.7544 | +1.231 | 0.2184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0635**, F-statistic = **3.41** (p = **1.54e-04**), Residual SE = **4.396** on **381** df, AIC = **2290.9**, BIC = **2338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -700.9211 | 623.4404 | ±1246.8808 | -1.124 | 0.2609 |  |
| Education: graduate level (vs college) | -0.4635 | 0.4768 | ±0.9536 | -0.972 | 0.3310 |  |
| Education: high school or below (vs college) | +0.8138 | 0.9147 | ±1.8294 | +0.890 | 0.3736 |  |
| Site: UCSD (vs UAB) | -0.7623 | 0.5576 | ±1.1152 | -1.367 | 0.1716 |  |
| Site: UW (vs UAB) | -0.1134 | 0.6140 | ±1.2281 | -0.185 | 0.8535 |  |
| **Age (years)** | **-0.0821** | 0.0212 | ±0.0424 | **-3.869** | **1.09e-04** | *** |
| BMI (kg/m2) | +0.0678 | 0.0354 | ±0.0707 | +1.918 | 0.0551 | . |
| Hypertension | +0.5559 | 0.5323 | ±1.0646 | +1.044 | 0.2963 |  |
| High cholesterol | +0.6718 | 0.4850 | ±0.9701 | +1.385 | 0.1660 |  |
| Kidney disease | +0.8180 | 0.8817 | ±1.7634 | +0.928 | 0.3536 |  |
| Circulatory disease | +1.4900 | 0.8445 | ±1.6890 | +1.764 | 0.0777 | . |
| Avg. daily time 54-250 (%) | +7.0928 | 6.2359 | ±12.4718 | +1.137 | 0.2554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.06e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2429** | 1.8048 | ±3.6096 | **+4.567** | **4.94e-06** | *** |
| Education: graduate level (vs college) | -0.4638 | 0.4792 | ±0.9584 | -0.968 | 0.3331 |  |
| Education: high school or below (vs college) | +0.8501 | 0.9163 | ±1.8327 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.7091 | 0.5610 | ±1.1220 | -1.264 | 0.2062 |  |
| Site: UW (vs UAB) | -0.0983 | 0.6157 | ±1.2313 | -0.160 | 0.8732 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.820** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0663 | 0.0355 | ±0.0710 | +1.866 | 0.0620 | . |
| Hypertension | +0.5301 | 0.5325 | ±1.0650 | +0.996 | 0.3195 |  |
| High cholesterol | +0.6730 | 0.4870 | ±0.9740 | +1.382 | 0.1670 |  |
| Kidney disease | +0.8504 | 0.8814 | ±1.7628 | +0.965 | 0.3347 |  |
| Circulatory disease | +1.3893 | 0.8287 | ±1.6574 | +1.676 | 0.0936 | . |
| Time 181-250, pooled (%) | +0.0690 | 0.7615 | ±1.5231 | +0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.04e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2208** | 1.7874 | ±3.5748 | **+4.599** | **4.24e-06** | *** |
| Education: graduate level (vs college) | -0.4649 | 0.4799 | ±0.9597 | -0.969 | 0.3326 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9163 | ±1.8326 | +0.932 | 0.3512 |  |
| Site: UCSD (vs UAB) | -0.7083 | 0.5605 | ±1.1209 | -1.264 | 0.2063 |  |
| Site: UW (vs UAB) | -0.0995 | 0.6159 | ±1.2318 | -0.162 | 0.8717 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0423 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0353 | ±0.0706 | +1.877 | 0.0606 | . |
| Hypertension | +0.5284 | 0.5318 | ±1.0636 | +0.994 | 0.3205 |  |
| High cholesterol | +0.6710 | 0.4868 | ±0.9736 | +1.378 | 0.1681 |  |
| Kidney disease | +0.8508 | 0.8806 | ±1.7612 | +0.966 | 0.3340 |  |
| Circulatory disease | +1.3879 | 0.8278 | ±1.6555 | +1.677 | 0.0936 | . |
| Avg. daily time 181-250 (%) | +0.1280 | 0.7650 | ±1.5300 | +0.167 | 0.8671 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.06e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2439** | 1.8054 | ±3.6108 | **+4.566** | **4.97e-06** | *** |
| Education: graduate level (vs college) | -0.4637 | 0.4791 | ±0.9583 | -0.968 | 0.3332 |  |
| Education: high school or below (vs college) | +0.8501 | 0.9163 | ±1.8326 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.7091 | 0.5610 | ±1.1220 | -1.264 | 0.2062 |  |
| Site: UW (vs UAB) | -0.0983 | 0.6157 | ±1.2314 | -0.160 | 0.8732 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.820** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0663 | 0.0355 | ±0.0710 | +1.866 | 0.0620 | . |
| Hypertension | +0.5302 | 0.5325 | ±1.0650 | +0.996 | 0.3194 |  |
| High cholesterol | +0.6729 | 0.4870 | ±0.9740 | +1.382 | 0.1670 |  |
| Kidney disease | +0.8507 | 0.8815 | ±1.7630 | +0.965 | 0.3345 |  |
| Circulatory disease | +1.3893 | 0.8287 | ±1.6574 | +1.676 | 0.0936 | . |
| Time > 180 (%) | +0.0662 | 0.7604 | ±1.5208 | +0.087 | 0.9306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.04e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2217** | 1.7880 | ±3.5761 | **+4.598** | **4.26e-06** | *** |
| Education: graduate level (vs college) | -0.4648 | 0.4798 | ±0.9596 | -0.969 | 0.3327 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9163 | ±1.8326 | +0.932 | 0.3512 |  |
| Site: UCSD (vs UAB) | -0.7083 | 0.5604 | ±1.1209 | -1.264 | 0.2063 |  |
| Site: UW (vs UAB) | -0.0995 | 0.6160 | ±1.2319 | -0.162 | 0.8717 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0423 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0353 | ±0.0706 | +1.877 | 0.0606 | . |
| Hypertension | +0.5285 | 0.5318 | ±1.0636 | +0.994 | 0.3203 |  |
| High cholesterol | +0.6709 | 0.4868 | ±0.9736 | +1.378 | 0.1681 |  |
| Kidney disease | +0.8510 | 0.8807 | ±1.7613 | +0.966 | 0.3339 |  |
| Circulatory disease | +1.3879 | 0.8278 | ±1.6556 | +1.677 | 0.0936 | . |
| Avg. daily time > 180 (%) | +0.1249 | 0.7633 | ±1.5265 | +0.164 | 0.8701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0908**, Adj R² = **0.0646**, F-statistic = **3.46** (p = **1.30e-04**), Residual SE = **4.394** on **381** df, AIC = **2290.5**, BIC = **2338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9731** | 1.7794 | ±3.5588 | **+4.481** | **7.44e-06** | *** |
| Education: graduate level (vs college) | -0.4187 | 0.4783 | ±0.9566 | -0.875 | 0.3814 |  |
| Education: high school or below (vs college) | +0.8473 | 0.9228 | ±1.8457 | +0.918 | 0.3585 |  |
| Site: UCSD (vs UAB) | -0.6673 | 0.5628 | ±1.1256 | -1.186 | 0.2358 |  |
| Site: UW (vs UAB) | -0.1207 | 0.6139 | ±1.2278 | -0.197 | 0.8442 |  |
| **Age (years)** | **-0.0753** | 0.0210 | ±0.0419 | **-3.593** | **3.27e-04** | *** |
| BMI (kg/m2) | +0.0607 | 0.0354 | ±0.0708 | +1.714 | 0.0865 | . |
| Hypertension | +0.4902 | 0.5317 | ±1.0634 | +0.922 | 0.3566 |  |
| High cholesterol | +0.6276 | 0.4859 | ±0.9717 | +1.292 | 0.1964 |  |
| Kidney disease | +0.7936 | 0.8851 | ±1.7702 | +0.897 | 0.3699 |  |
| Circulatory disease | +1.4043 | 0.8202 | ±1.6404 | +1.712 | 0.0869 | . |
| Nocturnal time > 180 (%) | +1.0233 | 0.7515 | ±1.5030 | +1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 393; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.98** (p = **5.91e-04**), AUC = **0.6802**, AIC = **353.1**, BIC = **396.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2778 | 1.0135 | ±2.0271 | -0.274 | 0.7841 | 0.7575 |  |
| Education: graduate level (vs college) | -0.2457 | 0.2996 | ±0.5993 | -0.820 | 0.4122 | 0.7822 |  |
| Education: high school or below (vs college) | -0.0197 | 0.4906 | ±0.9812 | -0.040 | 0.9680 | 0.9805 |  |
| Site: UCSD (vs UAB) | -0.0916 | 0.3753 | ±0.7507 | -0.244 | 0.8072 | 0.9125 |  |
| Site: UW (vs UAB) | +0.2340 | 0.3547 | ±0.7095 | +0.660 | 0.5095 | 1.2636 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.642** | **2.70e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0422** | 0.0178 | ±0.0355 | **+2.377** | **0.0175** | 1.0431 | * |
| Hypertension | +0.2534 | 0.3183 | ±0.6366 | +0.796 | 0.4260 | 1.2884 |  |
| High cholesterol | +0.5777 | 0.2993 | ±0.5987 | +1.930 | 0.0536 | 1.7819 | . |
| Kidney disease | +0.3785 | 0.5798 | ±1.1595 | +0.653 | 0.5138 | 1.4602 |  |
| **Circulatory disease** | **+0.9049** | 0.4242 | ±0.8483 | **+2.133** | **0.0329** | 2.4718 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.99** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5336 | 2.6540 | ±5.3080 | -0.201 | 0.8407 | 0.5865 |  |
| Education: graduate level (vs college) | -0.2440 | 0.3001 | ±0.6001 | -0.813 | 0.4161 | 0.7835 |  |
| Education: high school or below (vs college) | -0.0206 | 0.4907 | ±0.9815 | -0.042 | 0.9664 | 0.9796 |  |
| Site: UCSD (vs UAB) | -0.0888 | 0.3763 | ±0.7526 | -0.236 | 0.8134 | 0.9150 |  |
| Site: UW (vs UAB) | +0.2364 | 0.3555 | ±0.7111 | +0.665 | 0.5061 | 1.2667 |  |
| **Age (years)** | **-0.0516** | 0.0142 | ±0.0284 | **-3.638** | **2.75e-04** | 0.9497 | *** |
| **BMI (kg/m2)** | **+0.0420** | 0.0179 | ±0.0358 | **+2.349** | **0.0188** | 1.0429 | * |
| Hypertension | +0.2506 | 0.3194 | ±0.6388 | +0.784 | 0.4328 | 1.2848 |  |
| High cholesterol | +0.5721 | 0.3041 | ±0.6082 | +1.881 | 0.0600 | 1.7719 | . |
| Kidney disease | +0.3814 | 0.5804 | ±1.1608 | +0.657 | 0.5111 | 1.4643 |  |
| **Circulatory disease** | **+0.9083** | 0.4253 | ±0.8507 | **+2.135** | **0.0327** | 2.4801 | * |
| HbA1c (%) | +0.0488 | 0.4673 | ±0.9345 | +0.104 | 0.9169 | 1.0500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0858**, LLR χ² = **31.06** (p = **0.0011**), AUC = **0.6795**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2858 | 2.3167 | ±4.6334 | +0.123 | 0.9018 | 1.3309 |  |
| Education: graduate level (vs college) | -0.2466 | 0.2997 | ±0.5995 | -0.823 | 0.4107 | 0.7815 |  |
| Education: high school or below (vs college) | -0.0249 | 0.4913 | ±0.9825 | -0.051 | 0.9595 | 0.9754 |  |
| Site: UCSD (vs UAB) | -0.0905 | 0.3754 | ±0.7508 | -0.241 | 0.8095 | 0.9135 |  |
| Site: UW (vs UAB) | +0.2384 | 0.3551 | ±0.7101 | +0.671 | 0.5020 | 1.2692 |  |
| **Age (years)** | **-0.0517** | 0.0142 | ±0.0283 | **-3.649** | **2.64e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0426** | 0.0178 | ±0.0357 | **+2.390** | **0.0168** | 1.0435 | * |
| Hypertension | +0.2565 | 0.3186 | ±0.6372 | +0.805 | 0.4207 | 1.2924 |  |
| High cholesterol | +0.5767 | 0.2993 | ±0.5985 | +1.927 | 0.0540 | 1.7801 | . |
| Kidney disease | +0.3888 | 0.5810 | ±1.1620 | +0.669 | 0.5033 | 1.4752 |  |
| **Circulatory disease** | **+0.9039** | 0.4246 | ±0.8492 | **+2.129** | **0.0333** | 2.4691 | * |
| Mean glucose (mg/dL) | -0.0049 | 0.0183 | ±0.0366 | -0.270 | 0.7869 | 0.9951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0858**, LLR χ² = **31.06** (p = **0.0011**), AUC = **0.6795**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9704 | 4.7250 | ±9.4499 | +0.205 | 0.8373 | 2.6389 |  |
| Education: graduate level (vs college) | -0.2466 | 0.2997 | ±0.5995 | -0.823 | 0.4107 | 0.7815 |  |
| Education: high school or below (vs college) | -0.0249 | 0.4913 | ±0.9825 | -0.051 | 0.9595 | 0.9754 |  |
| Site: UCSD (vs UAB) | -0.0905 | 0.3754 | ±0.7508 | -0.241 | 0.8095 | 0.9135 |  |
| Site: UW (vs UAB) | +0.2384 | 0.3551 | ±0.7101 | +0.671 | 0.5020 | 1.2692 |  |
| **Age (years)** | **-0.0517** | 0.0142 | ±0.0283 | **-3.649** | **2.64e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0426** | 0.0178 | ±0.0357 | **+2.390** | **0.0168** | 1.0435 | * |
| Hypertension | +0.2565 | 0.3186 | ±0.6372 | +0.805 | 0.4207 | 1.2924 |  |
| High cholesterol | +0.5767 | 0.2993 | ±0.5985 | +1.927 | 0.0540 | 1.7801 | . |
| Kidney disease | +0.3888 | 0.5810 | ±1.1620 | +0.669 | 0.5033 | 1.4752 |  |
| **Circulatory disease** | **+0.9039** | 0.4246 | ±0.8492 | **+2.129** | **0.0333** | 2.4691 | * |
| GMI (%) | -0.2068 | 0.7649 | ±1.5298 | -0.270 | 0.7869 | 0.8132 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0859**, LLR χ² = **31.11** (p = **0.0011**), AUC = **0.6791**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3447 | 2.0242 | ±4.0484 | +0.170 | 0.8648 | 1.4115 |  |
| Education: graduate level (vs college) | -0.2509 | 0.3002 | ±0.6003 | -0.836 | 0.4032 | 0.7781 |  |
| Education: high school or below (vs college) | -0.0268 | 0.4910 | ±0.9820 | -0.055 | 0.9564 | 0.9735 |  |
| Site: UCSD (vs UAB) | -0.0849 | 0.3758 | ±0.7516 | -0.226 | 0.8213 | 0.9186 |  |
| Site: UW (vs UAB) | +0.2424 | 0.3554 | ±0.7108 | +0.682 | 0.4953 | 1.2743 |  |
| **Age (years)** | **-0.0524** | 0.0144 | ±0.0287 | **-3.642** | **2.70e-04** | 0.9490 | *** |
| **BMI (kg/m2)** | **+0.0432** | 0.0180 | ±0.0359 | **+2.407** | **0.0161** | 1.0442 | * |
| Hypertension | +0.2565 | 0.3185 | ±0.6370 | +0.805 | 0.4206 | 1.2924 |  |
| High cholesterol | +0.5814 | 0.2994 | ±0.5989 | +1.942 | 0.0522 | 1.7886 | . |
| Kidney disease | +0.3801 | 0.5799 | ±1.1597 | +0.656 | 0.5121 | 1.4625 |  |
| **Circulatory disease** | **+0.9009** | 0.4249 | ±0.8498 | **+2.120** | **0.0340** | 2.4619 | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0053 | 0.0148 | ±0.0296 | -0.355 | 0.7229 | 0.9948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0883**, LLR χ² = **31.95** (p = **7.76e-04**), AUC = **0.6839**, AIC = **354.1**, BIC = **401.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3872 | 1.5171 | ±3.0342 | -0.914 | 0.3605 | 0.2498 |  |
| Education: graduate level (vs college) | -0.2230 | 0.3007 | ±0.6013 | -0.742 | 0.4583 | 0.8001 |  |
| Education: high school or below (vs college) | -0.0276 | 0.4927 | ±0.9854 | -0.056 | 0.9553 | 0.9727 |  |
| Site: UCSD (vs UAB) | -0.0404 | 0.3802 | ±0.7605 | -0.106 | 0.9154 | 0.9604 |  |
| Site: UW (vs UAB) | +0.2774 | 0.3589 | ±0.7179 | +0.773 | 0.4395 | 1.3198 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.643** | **2.70e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0416** | 0.0178 | ±0.0357 | **+2.335** | **0.0195** | 1.0425 | * |
| Hypertension | +0.2440 | 0.3195 | ±0.6389 | +0.764 | 0.4450 | 1.2763 |  |
| **High cholesterol** | **+0.5905** | 0.3003 | ±0.6005 | **+1.967** | **0.0492** | 1.8049 | * |
| Kidney disease | +0.3149 | 0.5880 | ±1.1761 | +0.535 | 0.5923 | 1.3701 |  |
| **Circulatory disease** | **+0.9182** | 0.4240 | ±0.8481 | **+2.165** | **0.0304** | 2.5048 | * |
| Glucose SD, pooled (mg/dL) | +0.0639 | 0.0650 | ±0.1301 | +0.982 | 0.3261 | 1.0659 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0873**, LLR χ² = **31.62** (p = **8.77e-04**), AUC = **0.6817**, AIC = **354.5**, BIC = **402.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0991 | 1.4450 | ±2.8899 | -0.761 | 0.4469 | 0.3332 |  |
| Education: graduate level (vs college) | -0.2265 | 0.3006 | ±0.6011 | -0.754 | 0.4511 | 0.7973 |  |
| Education: high school or below (vs college) | -0.0162 | 0.4919 | ±0.9838 | -0.033 | 0.9737 | 0.9839 |  |
| Site: UCSD (vs UAB) | -0.0489 | 0.3799 | ±0.7598 | -0.129 | 0.8976 | 0.9523 |  |
| Site: UW (vs UAB) | +0.2686 | 0.3585 | ±0.7170 | +0.749 | 0.4537 | 1.3082 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.638** | **2.74e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0411** | 0.0179 | ±0.0358 | **+2.300** | **0.0214** | 1.0420 | * |
| Hypertension | +0.2511 | 0.3191 | ±0.6381 | +0.787 | 0.4312 | 1.2855 |  |
| High cholesterol | +0.5872 | 0.3002 | ±0.6004 | +1.956 | 0.0505 | 1.7989 | . |
| Kidney disease | +0.3284 | 0.5866 | ±1.1731 | +0.560 | 0.5756 | 1.3887 |  |
| **Circulatory disease** | **+0.9177** | 0.4242 | ±0.8484 | **+2.163** | **0.0305** | 2.5035 | * |
| Avg. daily SD (mg/dL) | +0.0522 | 0.0655 | ±0.1310 | +0.797 | 0.4253 | 1.0536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0888**, LLR χ² = **32.17** (p = **7.17e-04**), AUC = **0.6842**, AIC = **353.9**, BIC = **401.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4410 | 1.4746 | ±2.9491 | -0.977 | 0.3284 | 0.2367 |  |
| Education: graduate level (vs college) | -0.2215 | 0.3008 | ±0.6016 | -0.736 | 0.4615 | 0.8013 |  |
| Education: high school or below (vs college) | -0.0370 | 0.4936 | ±0.9871 | -0.075 | 0.9403 | 0.9637 |  |
| Site: UCSD (vs UAB) | -0.0358 | 0.3803 | ±0.7605 | -0.094 | 0.9250 | 0.9649 |  |
| Site: UW (vs UAB) | +0.2885 | 0.3597 | ±0.7195 | +0.802 | 0.4226 | 1.3344 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0282 | **-3.662** | **2.50e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0423** | 0.0178 | ±0.0357 | **+2.371** | **0.0178** | 1.0432 | * |
| Hypertension | +0.2500 | 0.3196 | ±0.6392 | +0.782 | 0.4341 | 1.2840 |  |
| **High cholesterol** | **+0.5908** | 0.3002 | ±0.6003 | **+1.968** | **0.0490** | 1.8055 | * |
| Kidney disease | +0.3317 | 0.5866 | ±1.1733 | +0.565 | 0.5718 | 1.3933 |  |
| **Circulatory disease** | **+0.9153** | 0.4246 | ±0.8493 | **+2.156** | **0.0311** | 2.4975 | * |
| CV (%) | +0.0760 | 0.0699 | ±0.1397 | +1.087 | 0.2770 | 1.0789 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0886**, LLR χ² = **32.08** (p = **7.41e-04**), AUC = **0.6844**, AIC = **354.0**, BIC = **401.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7448 | 1.4147 | ±2.8294 | +0.527 | 0.5985 | 2.1061 |  |
| Education: graduate level (vs college) | -0.2224 | 0.3007 | ±0.6014 | -0.740 | 0.4596 | 0.8006 |  |
| Education: high school or below (vs college) | -0.0380 | 0.4936 | ±0.9872 | -0.077 | 0.9386 | 0.9627 |  |
| Site: UCSD (vs UAB) | -0.0513 | 0.3784 | ±0.7569 | -0.136 | 0.8922 | 0.9500 |  |
| Site: UW (vs UAB) | +0.2754 | 0.3581 | ±0.7162 | +0.769 | 0.4418 | 1.3171 |  |
| **Age (years)** | **-0.0516** | 0.0141 | ±0.0282 | **-3.653** | **2.59e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0356 | **+2.378** | **0.0174** | 1.0433 | * |
| Hypertension | +0.2453 | 0.3195 | ±0.6391 | +0.768 | 0.4426 | 1.2780 |  |
| **High cholesterol** | **+0.5908** | 0.3001 | ±0.6002 | **+1.969** | **0.0490** | 1.8054 | * |
| Kidney disease | +0.3476 | 0.5851 | ±1.1702 | +0.594 | 0.5524 | 1.4157 |  |
| **Circulatory disease** | **+0.9135** | 0.4246 | ±0.8492 | **+2.151** | **0.0314** | 2.4930 | * |
| Mean / SD ratio | -0.1541 | 0.1488 | ±0.2976 | -1.036 | 0.3004 | 0.8572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0870**, LLR χ² = **31.50** (p = **9.17e-04**), AUC = **0.6818**, AIC = **354.6**, BIC = **402.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3968 | 1.3882 | ±2.7765 | +0.286 | 0.7750 | 1.4871 |  |
| Education: graduate level (vs college) | -0.2285 | 0.3005 | ±0.6010 | -0.760 | 0.4470 | 0.7957 |  |
| Education: high school or below (vs college) | -0.0237 | 0.4921 | ±0.9841 | -0.048 | 0.9616 | 0.9766 |  |
| Site: UCSD (vs UAB) | -0.0620 | 0.3781 | ±0.7563 | -0.164 | 0.8697 | 0.9399 |  |
| Site: UW (vs UAB) | +0.2616 | 0.3574 | ±0.7149 | +0.732 | 0.4642 | 1.2990 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0282 | **-3.645** | **2.68e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0415** | 0.0178 | ±0.0357 | **+2.323** | **0.0202** | 1.0423 | * |
| Hypertension | +0.2556 | 0.3192 | ±0.6383 | +0.801 | 0.4232 | 1.2912 |  |
| High cholesterol | +0.5836 | 0.2999 | ±0.5997 | +1.946 | 0.0516 | 1.7925 | . |
| Kidney disease | +0.3548 | 0.5834 | ±1.1668 | +0.608 | 0.5431 | 1.4258 |  |
| **Circulatory disease** | **+0.9123** | 0.4244 | ±0.8487 | **+2.150** | **0.0316** | 2.4900 | * |
| Avg. daily mean/SD | -0.0876 | 0.1229 | ±0.2458 | -0.712 | 0.4762 | 0.9161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.1144**, LLR χ² = **41.44** (p = **2.03e-05**), AUC = **0.7176**, AIC = **344.6**, BIC = **392.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5985** | 1.4633 | ±2.9265 | **-2.459** | **0.0139** | 0.0274 | * |
| Education: graduate level (vs college) | -0.2440 | 0.3040 | ±0.6080 | -0.803 | 0.4222 | 0.7835 |  |
| Education: high school or below (vs college) | -0.1506 | 0.5045 | ±1.0089 | -0.298 | 0.7654 | 0.8602 |  |
| Site: UCSD (vs UAB) | -0.0039 | 0.3812 | ±0.7625 | -0.010 | 0.9918 | 0.9961 |  |
| Site: UW (vs UAB) | +0.3954 | 0.3643 | ±0.7287 | +1.085 | 0.2778 | 1.4850 |  |
| **Age (years)** | **-0.0470** | 0.0142 | ±0.0284 | **-3.309** | **9.36e-04** | 0.9541 | *** |
| **BMI (kg/m2)** | **+0.0489** | 0.0183 | ±0.0366 | **+2.671** | **0.0076** | 1.0501 | ** |
| Hypertension | +0.3275 | 0.3244 | ±0.6489 | +1.010 | 0.3127 | 1.3875 |  |
| High cholesterol | +0.5267 | 0.3049 | ±0.6098 | +1.728 | 0.0840 | 1.6934 | . |
| Kidney disease | +0.3132 | 0.5931 | ±1.1863 | +0.528 | 0.5974 | 1.3679 |  |
| **Circulatory disease** | **+0.9553** | 0.4328 | ±0.8656 | **+2.207** | **0.0273** | 2.5994 | * |
| **MAG (mg/dL/h)** | **+0.0793** | 0.0247 | ±0.0495 | **+3.206** | **0.0013** | 1.0826 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0897**, LLR χ² = **32.49** (p = **6.36e-04**), AUC = **0.6854**, AIC = **353.6**, BIC = **401.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6892 | 1.5349 | ±3.0698 | -1.101 | 0.2711 | 0.1847 |  |
| Education: graduate level (vs college) | -0.2380 | 0.3002 | ±0.6005 | -0.793 | 0.4278 | 0.7882 |  |
| Education: high school or below (vs college) | -0.0297 | 0.4941 | ±0.9882 | -0.060 | 0.9520 | 0.9707 |  |
| Site: UCSD (vs UAB) | -0.0402 | 0.3790 | ±0.7579 | -0.106 | 0.9155 | 0.9606 |  |
| Site: UW (vs UAB) | +0.2805 | 0.3582 | ±0.7165 | +0.783 | 0.4337 | 1.3237 |  |
| **Age (years)** | **-0.0518** | 0.0142 | ±0.0283 | **-3.653** | **2.59e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0440** | 0.0178 | ±0.0357 | **+2.470** | **0.0135** | 1.0450 | * |
| Hypertension | +0.2755 | 0.3205 | ±0.6410 | +0.860 | 0.3900 | 1.3172 |  |
| High cholesterol | +0.5744 | 0.3007 | ±0.6014 | +1.910 | 0.0561 | 1.7761 | . |
| Kidney disease | +0.3364 | 0.5859 | ±1.1719 | +0.574 | 0.5659 | 1.3999 |  |
| **Circulatory disease** | **+0.9125** | 0.4250 | ±0.8500 | **+2.147** | **0.0318** | 2.4905 | * |
| Avg. daily range (mg/dL) | +0.0166 | 0.0136 | ±0.0272 | +1.220 | 0.2225 | 1.0167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0909**, LLR χ² = **32.93** (p = **5.41e-04**), AUC = **0.6908**, AIC = **353.1**, BIC = **400.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8550 | 1.0958 | ±2.1915 | -0.780 | 0.4352 | 0.4253 |  |
| Education: graduate level (vs college) | -0.2428 | 0.3008 | ±0.6016 | -0.807 | 0.4196 | 0.7845 |  |
| Education: high school or below (vs college) | -0.0524 | 0.4914 | ±0.9828 | -0.107 | 0.9151 | 0.9490 |  |
| Site: UCSD (vs UAB) | -0.0734 | 0.3773 | ±0.7546 | -0.194 | 0.8458 | 0.9293 |  |
| Site: UW (vs UAB) | +0.2258 | 0.3568 | ±0.7136 | +0.633 | 0.5268 | 1.2533 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0281 | **-3.650** | **2.62e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0357 | **+2.400** | **0.0164** | 1.0437 | * |
| Hypertension | +0.2262 | 0.3203 | ±0.6406 | +0.706 | 0.4801 | 1.2538 |  |
| High cholesterol | +0.5583 | 0.3002 | ±0.6003 | +1.860 | 0.0629 | 1.7478 | . |
| Kidney disease | +0.4035 | 0.5807 | ±1.1614 | +0.695 | 0.4871 | 1.4971 |  |
| **Circulatory disease** | **+0.9207** | 0.4231 | ±0.8463 | **+2.176** | **0.0296** | 2.5110 | * |
| SD of daily means (mg/dL) | +0.1087 | 0.0774 | ±0.1547 | +1.405 | 0.1600 | 1.1148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0863**, LLR χ² = **31.25** (p = **0.0010**), AUC = **0.6817**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -24.9740 | 47.6036 | ±95.2072 | -0.525 | 0.5998 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2460 | 0.2998 | ±0.5995 | -0.821 | 0.4119 | 0.7819 |  |
| Education: high school or below (vs college) | -0.0220 | 0.4912 | ±0.9823 | -0.045 | 0.9642 | 0.9782 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3770 | ±0.7540 | -0.290 | 0.7718 | 0.8964 |  |
| Site: UW (vs UAB) | +0.2216 | 0.3559 | ±0.7117 | +0.623 | 0.5336 | 1.2480 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.647** | **2.65e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0418** | 0.0179 | ±0.0357 | **+2.341** | **0.0192** | 1.0427 | * |
| Hypertension | +0.2560 | 0.3184 | ±0.6368 | +0.804 | 0.4214 | 1.2918 |  |
| High cholesterol | +0.5822 | 0.2995 | ±0.5990 | +1.944 | 0.0519 | 1.7901 | . |
| Kidney disease | +0.4004 | 0.5805 | ±1.1609 | +0.690 | 0.4903 | 1.4925 |  |
| **Circulatory disease** | **+0.9018** | 0.4243 | ±0.8487 | **+2.125** | **0.0336** | 2.4640 | * |
| Time in range 70-180, pooled (%) | +0.2483 | 0.4785 | ±0.9571 | +0.519 | 0.6038 | 1.2819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.99** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -4.3819 | 45.7539 | ±91.5077 | -0.096 | 0.9237 | 0.0125 |  |
| Education: graduate level (vs college) | -0.2457 | 0.2997 | ±0.5993 | -0.820 | 0.4123 | 0.7822 |  |
| Education: high school or below (vs college) | -0.0204 | 0.4907 | ±0.9814 | -0.042 | 0.9668 | 0.9798 |  |
| Site: UCSD (vs UAB) | -0.0943 | 0.3766 | ±0.7531 | -0.250 | 0.8022 | 0.9100 |  |
| Site: UW (vs UAB) | +0.2328 | 0.3550 | ±0.7099 | +0.656 | 0.5119 | 1.2622 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.642** | **2.70e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0422** | 0.0178 | ±0.0356 | **+2.371** | **0.0177** | 1.0431 | * |
| Hypertension | +0.2522 | 0.3186 | ±0.6372 | +0.792 | 0.4286 | 1.2868 |  |
| High cholesterol | +0.5786 | 0.2995 | ±0.5990 | +1.932 | 0.0534 | 1.7835 | . |
| Kidney disease | +0.3800 | 0.5799 | ±1.1598 | +0.655 | 0.5123 | 1.4622 |  |
| **Circulatory disease** | **+0.9052** | 0.4242 | ±0.8484 | **+2.134** | **0.0329** | 2.4724 | * |
| Avg. daily time in range 70-180 (%) | +0.0413 | 0.4600 | ±0.9200 | +0.090 | 0.9285 | 1.0421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.33** (p = **9.76e-04**), AUC = **0.6825**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2347 | 1.0161 | ±2.0321 | -0.231 | 0.8173 | 0.7908 |  |
| Education: graduate level (vs college) | -0.2514 | 0.2999 | ±0.5998 | -0.838 | 0.4019 | 0.7777 |  |
| Education: high school or below (vs college) | -0.0354 | 0.4925 | ±0.9850 | -0.072 | 0.9427 | 0.9652 |  |
| Site: UCSD (vs UAB) | -0.1262 | 0.3799 | ±0.7597 | -0.332 | 0.7398 | 0.8815 |  |
| Site: UW (vs UAB) | +0.2124 | 0.3567 | ±0.7135 | +0.596 | 0.5515 | 1.2367 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.637** | **2.76e-04** | 0.9499 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0355 | **+2.388** | **0.0169** | 1.0433 | * |
| Hypertension | +0.2709 | 0.3196 | ±0.6392 | +0.848 | 0.3967 | 1.3111 |  |
| High cholesterol | +0.5771 | 0.2996 | ±0.5992 | +1.926 | 0.0541 | 1.7809 | . |
| Kidney disease | +0.3576 | 0.5812 | ±1.1624 | +0.615 | 0.5384 | 1.4298 |  |
| **Circulatory disease** | **+0.9157** | 0.4247 | ±0.8494 | **+2.156** | **0.0311** | 2.4985 | * |
| Any reading < 54 during wear (0/1) | -0.2324 | 0.3998 | ±0.7995 | -0.581 | 0.5610 | 0.7926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0874**, LLR χ² = **31.65** (p = **8.68e-04**), AUC = **0.6838**, AIC = **354.4**, BIC = **402.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2457 | 1.0131 | ±2.0261 | -0.242 | 0.8084 | 0.7822 |  |
| Education: graduate level (vs college) | -0.2499 | 0.3002 | ±0.6004 | -0.832 | 0.4053 | 0.7789 |  |
| Education: high school or below (vs college) | -0.0493 | 0.4931 | ±0.9863 | -0.100 | 0.9203 | 0.9519 |  |
| Site: UCSD (vs UAB) | -0.1280 | 0.3777 | ±0.7555 | -0.339 | 0.7346 | 0.8798 |  |
| Site: UW (vs UAB) | +0.2183 | 0.3556 | ±0.7112 | +0.614 | 0.5392 | 1.2440 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0283 | **-3.661** | **2.51e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0434** | 0.0178 | ±0.0356 | **+2.439** | **0.0147** | 1.0444 | * |
| Hypertension | +0.2739 | 0.3195 | ±0.6390 | +0.857 | 0.3913 | 1.3151 |  |
| High cholesterol | +0.5716 | 0.2996 | ±0.5993 | +1.908 | 0.0564 | 1.7712 | . |
| Kidney disease | +0.3590 | 0.5808 | ±1.1616 | +0.618 | 0.5365 | 1.4319 |  |
| **Circulatory disease** | **+0.9326** | 0.4252 | ±0.8505 | **+2.193** | **0.0283** | 2.5411 | * |
| Time < 54 (%) | -2.2464 | 2.9194 | ±5.8388 | -0.769 | 0.4416 | 0.1058 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0863**, LLR χ² = **31.26** (p = **0.0010**), AUC = **0.6820**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2699 | 1.0130 | ±2.0260 | -0.266 | 0.7899 | 0.7634 |  |
| Education: graduate level (vs college) | -0.2406 | 0.3000 | ±0.5999 | -0.802 | 0.4225 | 0.7862 |  |
| Education: high school or below (vs college) | -0.0294 | 0.4917 | ±0.9834 | -0.060 | 0.9523 | 0.9710 |  |
| Site: UCSD (vs UAB) | -0.1066 | 0.3763 | ±0.7526 | -0.283 | 0.7770 | 0.8989 |  |
| Site: UW (vs UAB) | +0.2291 | 0.3551 | ±0.7102 | +0.645 | 0.5189 | 1.2574 |  |
| **Age (years)** | **-0.0516** | 0.0141 | ±0.0283 | **-3.647** | **2.65e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0356 | **+2.407** | **0.0161** | 1.0438 | * |
| Hypertension | +0.2595 | 0.3189 | ±0.6378 | +0.814 | 0.4158 | 1.2963 |  |
| High cholesterol | +0.5708 | 0.2998 | ±0.5995 | +1.904 | 0.0569 | 1.7696 | . |
| Kidney disease | +0.3726 | 0.5802 | ±1.1604 | +0.642 | 0.5207 | 1.4516 |  |
| **Circulatory disease** | **+0.9311** | 0.4271 | ±0.8542 | **+2.180** | **0.0293** | 2.5373 | * |
| Avg. daily time < 54 (%) | -1.6735 | 3.3367 | ±6.6734 | -0.502 | 0.6160 | 0.1876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0906**, LLR χ² = **32.81** (p = **5.64e-04**), AUC = **0.6910**, AIC = **353.3**, BIC = **400.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4354 | 1.0220 | ±2.0439 | -0.426 | 0.6701 | 0.6470 |  |
| Education: graduate level (vs college) | -0.2377 | 0.3004 | ±0.6008 | -0.791 | 0.4287 | 0.7884 |  |
| Education: high school or below (vs college) | -0.0615 | 0.4950 | ±0.9901 | -0.124 | 0.9012 | 0.9404 |  |
| Site: UCSD (vs UAB) | -0.0641 | 0.3765 | ±0.7531 | -0.170 | 0.8648 | 0.9379 |  |
| Site: UW (vs UAB) | +0.2798 | 0.3575 | ±0.7149 | +0.783 | 0.4338 | 1.3228 |  |
| **Age (years)** | **-0.0523** | 0.0142 | ±0.0284 | **-3.683** | **2.31e-04** | 0.9490 | *** |
| **BMI (kg/m2)** | **+0.0433** | 0.0179 | ±0.0357 | **+2.422** | **0.0154** | 1.0442 | * |
| Hypertension | +0.2921 | 0.3218 | ±0.6436 | +0.908 | 0.3640 | 1.3392 |  |
| High cholesterol | +0.5340 | 0.3021 | ±0.6041 | +1.768 | 0.0771 | 1.7057 | . |
| Kidney disease | +0.4387 | 0.5864 | ±1.1728 | +0.748 | 0.4544 | 1.5506 |  |
| **Circulatory disease** | **+0.9143** | 0.4257 | ±0.8514 | **+2.148** | **0.0317** | 2.4952 | * |
| Time 54-69, pooled (%) | +1.0300 | 0.7455 | ±1.4909 | +1.382 | 0.1671 | 2.8011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0879**, LLR χ² = **31.82** (p = **8.14e-04**), AUC = **0.6845**, AIC = **354.3**, BIC = **401.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3662 | 1.0176 | ±2.0353 | -0.360 | 0.7189 | 0.6933 |  |
| Education: graduate level (vs college) | -0.2401 | 0.3000 | ±0.6001 | -0.800 | 0.4236 | 0.7866 |  |
| Education: high school or below (vs college) | -0.0540 | 0.4937 | ±0.9874 | -0.109 | 0.9129 | 0.9474 |  |
| Site: UCSD (vs UAB) | -0.0792 | 0.3759 | ±0.7518 | -0.211 | 0.8331 | 0.9239 |  |
| Site: UW (vs UAB) | +0.2525 | 0.3558 | ±0.7117 | +0.709 | 0.4780 | 1.2872 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.675** | **2.38e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0429** | 0.0178 | ±0.0356 | **+2.408** | **0.0160** | 1.0438 | * |
| Hypertension | +0.2973 | 0.3231 | ±0.6463 | +0.920 | 0.3575 | 1.3462 |  |
| High cholesterol | +0.5578 | 0.3006 | ±0.6012 | +1.856 | 0.0635 | 1.7469 | . |
| Kidney disease | +0.4176 | 0.5828 | ±1.1655 | +0.717 | 0.4737 | 1.5182 |  |
| **Circulatory disease** | **+0.8982** | 0.4247 | ±0.8494 | **+2.115** | **0.0345** | 2.4551 | * |
| Avg. daily time 54-69 (%) | +0.7110 | 0.7606 | ±1.5213 | +0.935 | 0.3499 | 2.0360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0882**, LLR χ² = **31.93** (p = **7.82e-04**), AUC = **0.6856**, AIC = **354.1**, BIC = **401.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3875 | 1.0215 | ±2.0430 | -0.379 | 0.7044 | 0.6787 |  |
| Education: graduate level (vs college) | -0.2402 | 0.3000 | ±0.6001 | -0.801 | 0.4234 | 0.7865 |  |
| Education: high school or below (vs college) | -0.0345 | 0.4921 | ±0.9843 | -0.070 | 0.9441 | 0.9661 |  |
| Site: UCSD (vs UAB) | -0.0611 | 0.3770 | ±0.7540 | -0.162 | 0.8712 | 0.9407 |  |
| Site: UW (vs UAB) | +0.2683 | 0.3572 | ±0.7144 | +0.751 | 0.4526 | 1.3078 |  |
| **Age (years)** | **-0.0519** | 0.0142 | ±0.0284 | **-3.658** | **2.54e-04** | 0.9494 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0357 | **+2.380** | **0.0173** | 1.0434 | * |
| Hypertension | +0.2689 | 0.3200 | ±0.6399 | +0.840 | 0.4008 | 1.3085 |  |
| High cholesterol | +0.5524 | 0.3010 | ±0.6020 | +1.835 | 0.0665 | 1.7375 | . |
| Kidney disease | +0.4215 | 0.5842 | ±1.1683 | +0.722 | 0.4706 | 1.5242 |  |
| **Circulatory disease** | **+0.9017** | 0.4252 | ±0.8504 | **+2.121** | **0.0340** | 2.4638 | * |
| Time < 70 (%) | +0.6563 | 0.6633 | ±1.3267 | +0.989 | 0.3225 | 1.9276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0869**, LLR χ² = **31.47** (p = **9.28e-04**), AUC = **0.6823**, AIC = **354.6**, BIC = **402.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3399 | 1.0174 | ±2.0348 | -0.334 | 0.7383 | 0.7118 |  |
| Education: graduate level (vs college) | -0.2440 | 0.2998 | ±0.5997 | -0.814 | 0.4158 | 0.7835 |  |
| Education: high school or below (vs college) | -0.0387 | 0.4920 | ±0.9839 | -0.079 | 0.9373 | 0.9620 |  |
| Site: UCSD (vs UAB) | -0.0779 | 0.3760 | ±0.7521 | -0.207 | 0.8359 | 0.9251 |  |
| Site: UW (vs UAB) | +0.2482 | 0.3557 | ±0.7114 | +0.698 | 0.4853 | 1.2817 |  |
| **Age (years)** | **-0.0519** | 0.0142 | ±0.0283 | **-3.661** | **2.51e-04** | 0.9495 | *** |
| **BMI (kg/m2)** | **+0.0425** | 0.0178 | ±0.0356 | **+2.387** | **0.0170** | 1.0434 | * |
| Hypertension | +0.2798 | 0.3212 | ±0.6425 | +0.871 | 0.3837 | 1.3229 |  |
| High cholesterol | +0.5664 | 0.3001 | ±0.6001 | +1.888 | 0.0591 | 1.7619 | . |
| Kidney disease | +0.4063 | 0.5819 | ±1.1639 | +0.698 | 0.4851 | 1.5013 |  |
| **Circulatory disease** | **+0.8918** | 0.4249 | ±0.8498 | **+2.099** | **0.0358** | 2.4396 | * |
| Avg. daily time < 70 (%) | +0.4826 | 0.6837 | ±1.3674 | +0.706 | 0.4803 | 1.6203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0878**, LLR χ² = **31.80** (p = **8.23e-04**), AUC = **0.6843**, AIC = **354.3**, BIC = **402.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -249.9017 | 295.6968 | ±591.3937 | -0.845 | 0.3980 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2536 | 0.3005 | ±0.6010 | -0.844 | 0.3988 | 0.7760 |  |
| Education: high school or below (vs college) | -0.0547 | 0.4935 | ±0.9870 | -0.111 | 0.9118 | 0.9468 |  |
| Site: UCSD (vs UAB) | -0.1315 | 0.3777 | ±0.7555 | -0.348 | 0.7278 | 0.8768 |  |
| Site: UW (vs UAB) | +0.2195 | 0.3556 | ±0.7112 | +0.617 | 0.5371 | 1.2454 |  |
| **Age (years)** | **-0.0519** | 0.0141 | ±0.0283 | **-3.668** | **2.44e-04** | 0.9494 | *** |
| **BMI (kg/m2)** | **+0.0434** | 0.0178 | ±0.0356 | **+2.440** | **0.0147** | 1.0444 | * |
| Hypertension | +0.2745 | 0.3195 | ±0.6389 | +0.859 | 0.3901 | 1.3159 |  |
| High cholesterol | +0.5748 | 0.2998 | ±0.5996 | +1.917 | 0.0552 | 1.7768 | . |
| Kidney disease | +0.3561 | 0.5810 | ±1.1620 | +0.613 | 0.5400 | 1.4277 |  |
| **Circulatory disease** | **+0.9349** | 0.4253 | ±0.8506 | **+2.198** | **0.0279** | 2.5470 | * |
| Time 54-250, pooled (%) | +2.4967 | 2.9574 | ±5.9148 | +0.844 | 0.3985 | 12.1422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0867**, LLR χ² = **31.39** (p = **9.56e-04**), AUC = **0.6819**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -203.8564 | 340.4895 | ±680.9789 | -0.599 | 0.5494 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2426 | 0.3000 | ±0.6000 | -0.809 | 0.4187 | 0.7846 |  |
| Education: high school or below (vs college) | -0.0334 | 0.4920 | ±0.9841 | -0.068 | 0.9458 | 0.9671 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3763 | ±0.7526 | -0.290 | 0.7715 | 0.8965 |  |
| Site: UW (vs UAB) | +0.2305 | 0.3552 | ±0.7103 | +0.649 | 0.5162 | 1.2593 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0283 | **-3.653** | **2.59e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0356 | **+2.408** | **0.0160** | 1.0438 | * |
| Hypertension | +0.2592 | 0.3190 | ±0.6380 | +0.813 | 0.4164 | 1.2959 |  |
| High cholesterol | +0.5726 | 0.2998 | ±0.5995 | +1.910 | 0.0561 | 1.7729 | . |
| Kidney disease | +0.3707 | 0.5804 | ±1.1607 | +0.639 | 0.5229 | 1.4488 |  |
| **Circulatory disease** | **+0.9358** | 0.4271 | ±0.8541 | **+2.191** | **0.0284** | 2.5491 | * |
| Avg. daily time 54-250 (%) | +2.0360 | 3.4051 | ±6.8102 | +0.598 | 0.5499 | 7.6596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0899**, LLR χ² = **32.56** (p = **6.19e-04**), AUC = **0.6880**, AIC = **353.5**, BIC = **401.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0326 | 1.0478 | ±2.0957 | -0.031 | 0.9752 | 0.9679 |  |
| Education: graduate level (vs college) | -0.2429 | 0.3003 | ±0.6006 | -0.809 | 0.4186 | 0.7844 |  |
| Education: high school or below (vs college) | -0.0362 | 0.4929 | ±0.9858 | -0.073 | 0.9414 | 0.9644 |  |
| Site: UCSD (vs UAB) | -0.1091 | 0.3763 | ±0.7526 | -0.290 | 0.7719 | 0.8967 |  |
| Site: UW (vs UAB) | +0.2325 | 0.3560 | ±0.7121 | +0.653 | 0.5137 | 1.2618 |  |
| **Age (years)** | **-0.0520** | 0.0142 | ±0.0284 | **-3.668** | **2.45e-04** | 0.9493 | *** |
| **BMI (kg/m2)** | **+0.0414** | 0.0181 | ±0.0362 | **+2.287** | **0.0222** | 1.0423 | * |
| Hypertension | +0.2735 | 0.3200 | ±0.6399 | +0.855 | 0.3927 | 1.3145 |  |
| High cholesterol | +0.5660 | 0.2998 | ±0.5997 | +1.888 | 0.0591 | 1.7611 | . |
| Kidney disease | +0.4707 | 0.5851 | ±1.1702 | +0.805 | 0.4211 | 1.6012 |  |
| **Circulatory disease** | **+0.8943** | 0.4256 | ±0.8511 | **+2.102** | **0.0356** | 2.4457 | * |
| Time 181-250, pooled (%) | -0.6456 | 0.5201 | ±1.0401 | -1.241 | 0.2145 | 0.5244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.31** (p = **9.83e-04**), AUC = **0.6824**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1562 | 1.0383 | ±2.0767 | -0.150 | 0.8804 | 0.8554 |  |
| Education: graduate level (vs college) | -0.2449 | 0.2999 | ±0.5998 | -0.817 | 0.4142 | 0.7828 |  |
| Education: high school or below (vs college) | -0.0340 | 0.4917 | ±0.9834 | -0.069 | 0.9448 | 0.9665 |  |
| Site: UCSD (vs UAB) | -0.1020 | 0.3760 | ±0.7519 | -0.271 | 0.7862 | 0.9030 |  |
| Site: UW (vs UAB) | +0.2339 | 0.3550 | ±0.7100 | +0.659 | 0.5100 | 1.2635 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.670** | **2.42e-04** | 0.9493 | *** |
| **BMI (kg/m2)** | **+0.0420** | 0.0178 | ±0.0356 | **+2.357** | **0.0184** | 1.0428 | * |
| Hypertension | +0.2603 | 0.3189 | ±0.6378 | +0.816 | 0.4145 | 1.2973 |  |
| High cholesterol | +0.5775 | 0.2994 | ±0.5987 | +1.929 | 0.0537 | 1.7816 | . |
| Kidney disease | +0.4030 | 0.5815 | ±1.1630 | +0.693 | 0.4882 | 1.4964 |  |
| **Circulatory disease** | **+0.8992** | 0.4247 | ±0.8493 | **+2.118** | **0.0342** | 2.4577 | * |
| Avg. daily time 181-250 (%) | -0.2874 | 0.5054 | ±1.0109 | -0.569 | 0.5697 | 0.7502 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0900**, LLR χ² = **32.60** (p = **6.10e-04**), AUC = **0.6882**, AIC = **353.5**, BIC = **401.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0274 | 1.0486 | ±2.0972 | -0.026 | 0.9792 | 0.9730 |  |
| Education: graduate level (vs college) | -0.2436 | 0.3003 | ±0.6006 | -0.811 | 0.4172 | 0.7838 |  |
| Education: high school or below (vs college) | -0.0370 | 0.4929 | ±0.9859 | -0.075 | 0.9401 | 0.9636 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3763 | ±0.7527 | -0.290 | 0.7715 | 0.8965 |  |
| Site: UW (vs UAB) | +0.2331 | 0.3561 | ±0.7121 | +0.655 | 0.5127 | 1.2625 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.669** | **2.43e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0414** | 0.0181 | ±0.0362 | **+2.284** | **0.0224** | 1.0422 | * |
| Hypertension | +0.2734 | 0.3200 | ±0.6400 | +0.854 | 0.3929 | 1.3144 |  |
| High cholesterol | +0.5668 | 0.2999 | ±0.5998 | +1.890 | 0.0587 | 1.7626 | . |
| Kidney disease | +0.4715 | 0.5851 | ±1.1702 | +0.806 | 0.4203 | 1.6024 |  |
| **Circulatory disease** | **+0.8941** | 0.4256 | ±0.8512 | **+2.101** | **0.0357** | 2.4450 | * |
| Time > 180 (%) | -0.6526 | 0.5196 | ±1.0391 | -1.256 | 0.2091 | 0.5207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.33** (p = **9.76e-04**), AUC = **0.6824**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1515 | 1.0389 | ±2.0777 | -0.146 | 0.8841 | 0.8595 |  |
| Education: graduate level (vs college) | -0.2453 | 0.2999 | ±0.5998 | -0.818 | 0.4134 | 0.7825 |  |
| Education: high school or below (vs college) | -0.0348 | 0.4918 | ±0.9835 | -0.071 | 0.9436 | 0.9658 |  |
| Site: UCSD (vs UAB) | -0.1023 | 0.3760 | ±0.7520 | -0.272 | 0.7856 | 0.9028 |  |
| Site: UW (vs UAB) | +0.2342 | 0.3550 | ±0.7100 | +0.660 | 0.5095 | 1.2639 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.672** | **2.41e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0419** | 0.0178 | ±0.0356 | **+2.356** | **0.0185** | 1.0428 | * |
| Hypertension | +0.2603 | 0.3189 | ±0.6378 | +0.816 | 0.4144 | 1.2973 |  |
| High cholesterol | +0.5780 | 0.2994 | ±0.5988 | +1.931 | 0.0535 | 1.7825 | . |
| Kidney disease | +0.4036 | 0.5815 | ±1.1630 | +0.694 | 0.4876 | 1.4972 |  |
| **Circulatory disease** | **+0.8990** | 0.4247 | ±0.8494 | **+2.117** | **0.0343** | 2.4571 | * |
| Avg. daily time > 180 (%) | -0.2957 | 0.5048 | ±1.0096 | -0.586 | 0.5581 | 0.7440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0857**, LLR χ² = **31.01** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3046 | 1.0250 | ±2.0500 | -0.297 | 0.7664 | 0.7374 |  |
| Education: graduate level (vs college) | -0.2434 | 0.3000 | ±0.6000 | -0.811 | 0.4172 | 0.7840 |  |
| Education: high school or below (vs college) | -0.0211 | 0.4909 | ±0.9817 | -0.043 | 0.9657 | 0.9791 |  |
| Site: UCSD (vs UAB) | -0.0875 | 0.3761 | ±0.7521 | -0.233 | 0.8160 | 0.9162 |  |
| Site: UW (vs UAB) | +0.2328 | 0.3549 | ±0.7098 | +0.656 | 0.5119 | 1.2621 |  |
| **Age (years)** | **-0.0509** | 0.0144 | ±0.0289 | **-3.530** | **4.16e-04** | 0.9503 | *** |
| **BMI (kg/m2)** | **+0.0419** | 0.0179 | ±0.0357 | **+2.345** | **0.0190** | 1.0428 | * |
| Hypertension | +0.2499 | 0.3189 | ±0.6378 | +0.784 | 0.4333 | 1.2839 |  |
| High cholesterol | +0.5735 | 0.3002 | ±0.6004 | +1.910 | 0.0561 | 1.7745 | . |
| Kidney disease | +0.3712 | 0.5816 | ±1.1633 | +0.638 | 0.5233 | 1.4495 |  |
| **Circulatory disease** | **+0.9063** | 0.4243 | ±0.8487 | **+2.136** | **0.0327** | 2.4751 | * |
| Nocturnal time > 180 (%) | +0.0630 | 0.3548 | ±0.7095 | +0.178 | 0.8590 | 1.0651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
