# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 61; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, R² = **0.2226**, Adj R² = **0.0671**, F-statistic = **1.43** (p = **0.1943**), Residual SE = **5.569** on **50** df, AIC = **392.5**, BIC = **415.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.1432 | 8.0957 | ±16.1913 | +0.635 | 0.5252 |  |
| Education: graduate level (vs college) | -2.1151 | 1.7368 | ±3.4737 | -1.218 | 0.2233 |  |
| Education: high school or below (vs college) | +6.8963 | 5.8881 | ±11.7761 | +1.171 | 0.2415 |  |
| Site: UCSD (vs UAB) | +1.2167 | 1.9737 | ±3.9474 | +0.616 | 0.5376 |  |
| Site: UW (vs UAB) | +2.0298 | 2.4459 | ±4.8919 | +0.830 | 0.4066 |  |
| Age (years) | -0.0036 | 0.0899 | ±0.1797 | -0.040 | 0.9683 |  |
| BMI (kg/m2) | +0.0326 | 0.1402 | ±0.2804 | +0.233 | 0.8161 |  |
| Hypertension | +0.1610 | 1.7511 | ±3.5022 | +0.092 | 0.9268 |  |
| High cholesterol | +0.2873 | 1.6909 | ±3.3819 | +0.170 | 0.8651 |  |
| Kidney disease | +2.2120 | 5.6878 | ±11.3757 | +0.389 | 0.6973 |  |
| Circulatory disease | -2.7416 | 3.6962 | ±7.3923 | -0.742 | 0.4582 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **61**, R² = **0.2318**, Adj R² = **0.0593**, F-statistic = **1.34** (p = **0.2299**), Residual SE = **5.592** on **49** df, AIC = **393.7**, BIC = **419.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +14.4105 | 13.4260 | ±26.8520 | +1.073 | 0.2831 |  |
| Education: graduate level (vs college) | -2.3341 | 1.7926 | ±3.5852 | -1.302 | 0.1929 |  |
| Education: high school or below (vs college) | +7.8253 | 5.6712 | ±11.3424 | +1.380 | 0.1676 |  |
| Site: UCSD (vs UAB) | +1.3356 | 1.9868 | ±3.9737 | +0.672 | 0.5014 |  |
| Site: UW (vs UAB) | +2.1961 | 2.4911 | ±4.9822 | +0.882 | 0.3780 |  |
| Age (years) | +0.0004 | 0.0904 | ±0.1808 | +0.005 | 0.9962 |  |
| BMI (kg/m2) | +0.0390 | 0.1394 | ±0.2787 | +0.280 | 0.7794 |  |
| Hypertension | +0.3312 | 1.7724 | ±3.5448 | +0.187 | 0.8518 |  |
| High cholesterol | +0.4016 | 1.7650 | ±3.5301 | +0.228 | 0.8200 |  |
| Kidney disease | +1.8133 | 5.8147 | ±11.6294 | +0.312 | 0.7552 |  |
| Circulatory disease | -2.6934 | 3.6893 | ±7.3786 | -0.730 | 0.4654 |  |
| HbA1c (%) | -1.7490 | 2.3371 | ±4.6743 | -0.748 | 0.4542 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **61**, R² = **0.2269**, Adj R² = **0.0533**, F-statistic = **1.31** (p = **0.2490**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0944 | 12.2910 | ±24.5820 | -0.089 | 0.9291 |  |
| Education: graduate level (vs college) | -2.0510 | 1.7027 | ±3.4054 | -1.205 | 0.2284 |  |
| Education: high school or below (vs college) | +7.0843 | 6.0435 | ±12.0870 | +1.172 | 0.2411 |  |
| Site: UCSD (vs UAB) | +1.2691 | 1.9837 | ±3.9673 | +0.640 | 0.5223 |  |
| Site: UW (vs UAB) | +2.0055 | 2.4664 | ±4.9328 | +0.813 | 0.4162 |  |
| Age (years) | -0.0066 | 0.0913 | ±0.1825 | -0.073 | 0.9420 |  |
| BMI (kg/m2) | +0.0383 | 0.1435 | ±0.2871 | +0.267 | 0.7894 |  |
| Hypertension | +0.1590 | 1.7772 | ±3.5543 | +0.089 | 0.9287 |  |
| High cholesterol | +0.3409 | 1.7185 | ±3.4370 | +0.198 | 0.8428 |  |
| Kidney disease | +2.1787 | 5.6579 | ±11.3158 | +0.385 | 0.7002 |  |
| Circulatory disease | -2.9643 | 3.7125 | ±7.4250 | -0.798 | 0.4246 |  |
| Mean glucose (mg/dL) | +0.0539 | 0.0853 | ±0.1705 | +0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **61**, R² = **0.2269**, Adj R² = **0.0533**, F-statistic = **1.31** (p = **0.2490**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -8.5546 | 22.4835 | ±44.9670 | -0.380 | 0.7036 |  |
| Education: graduate level (vs college) | -2.0510 | 1.7027 | ±3.4054 | -1.205 | 0.2284 |  |
| Education: high school or below (vs college) | +7.0843 | 6.0435 | ±12.0870 | +1.172 | 0.2411 |  |
| Site: UCSD (vs UAB) | +1.2691 | 1.9837 | ±3.9673 | +0.640 | 0.5223 |  |
| Site: UW (vs UAB) | +2.0055 | 2.4664 | ±4.9328 | +0.813 | 0.4162 |  |
| Age (years) | -0.0066 | 0.0913 | ±0.1825 | -0.073 | 0.9420 |  |
| BMI (kg/m2) | +0.0383 | 0.1435 | ±0.2871 | +0.267 | 0.7894 |  |
| Hypertension | +0.1590 | 1.7772 | ±3.5543 | +0.089 | 0.9287 |  |
| High cholesterol | +0.3409 | 1.7185 | ±3.4370 | +0.198 | 0.8428 |  |
| Kidney disease | +2.1787 | 5.6579 | ±11.3158 | +0.385 | 0.7002 |  |
| Circulatory disease | -2.9643 | 3.7125 | ±7.4250 | -0.798 | 0.4246 |  |
| GMI (%) | +2.2538 | 3.5645 | ±7.1290 | +0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **61**, R² = **0.2504**, Adj R² = **0.0821**, F-statistic = **1.49** (p = **0.1665**), Residual SE = **5.523** on **49** df, AIC = **392.2**, BIC = **417.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -6.0990 | 13.5294 | ±27.0588 | -0.451 | 0.6521 |  |
| Education: graduate level (vs college) | -2.1041 | 1.6937 | ±3.3873 | -1.242 | 0.2141 |  |
| Education: high school or below (vs college) | +6.7850 | 6.0828 | ±12.1655 | +1.115 | 0.2647 |  |
| Site: UCSD (vs UAB) | +1.1930 | 1.9282 | ±3.8564 | +0.619 | 0.5361 |  |
| Site: UW (vs UAB) | +1.8374 | 2.4542 | ±4.9084 | +0.749 | 0.4541 |  |
| Age (years) | +0.0019 | 0.0912 | ±0.1824 | +0.021 | 0.9831 |  |
| BMI (kg/m2) | +0.0302 | 0.1541 | ±0.3082 | +0.196 | 0.8446 |  |
| Hypertension | -0.2145 | 1.7382 | ±3.4763 | -0.123 | 0.9018 |  |
| High cholesterol | +0.4703 | 1.7393 | ±3.4787 | +0.270 | 0.7869 |  |
| Kidney disease | +2.7994 | 5.2967 | ±10.5935 | +0.529 | 0.5971 |  |
| Circulatory disease | -3.0422 | 3.6575 | ±7.3150 | -0.832 | 0.4055 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0963 | 0.0735 | ±0.1471 | +1.309 | 0.1904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2288**, Adj R² = **0.0557**, F-statistic = **1.32** (p = **0.2414**), Residual SE = **5.602** on **49** df, AIC = **394.0**, BIC = **419.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.1723 | 8.8385 | ±17.6770 | +0.359 | 0.7197 |  |
| Education: graduate level (vs college) | -2.1308 | 1.7758 | ±3.5515 | -1.200 | 0.2302 |  |
| Education: high school or below (vs college) | +6.7951 | 6.3358 | ±12.6716 | +1.072 | 0.2835 |  |
| Site: UCSD (vs UAB) | +1.0207 | 2.0180 | ±4.0361 | +0.506 | 0.6130 |  |
| Site: UW (vs UAB) | +2.1144 | 2.5703 | ±5.1405 | +0.823 | 0.4107 |  |
| Age (years) | -0.0118 | 0.0914 | ±0.1829 | -0.129 | 0.8970 |  |
| BMI (kg/m2) | +0.0288 | 0.1538 | ±0.3075 | +0.187 | 0.8516 |  |
| Hypertension | -0.1708 | 1.6563 | ±3.3126 | -0.103 | 0.9179 |  |
| High cholesterol | +0.3116 | 1.7162 | ±3.4325 | +0.182 | 0.8559 |  |
| Kidney disease | +1.6200 | 6.6895 | ±13.3791 | +0.242 | 0.8087 |  |
| Circulatory disease | -2.7382 | 3.8315 | ±7.6629 | -0.715 | 0.4748 |  |
| Glucose SD, pooled (mg/dL) | +0.1701 | 0.3477 | ±0.6953 | +0.489 | 0.6247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2456**, Adj R² = **0.0763**, F-statistic = **1.45** (p = **0.1813**), Residual SE = **5.541** on **49** df, AIC = **392.6**, BIC = **418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.5280 | 8.8897 | ±17.7794 | +0.284 | 0.7761 |  |
| Education: graduate level (vs college) | -2.1138 | 1.7129 | ±3.4257 | -1.234 | 0.2172 |  |
| Education: high school or below (vs college) | +6.7666 | 6.1906 | ±12.3811 | +1.093 | 0.2744 |  |
| Site: UCSD (vs UAB) | +0.6338 | 1.9324 | ±3.8649 | +0.328 | 0.7429 |  |
| Site: UW (vs UAB) | +2.0757 | 2.4584 | ±4.9168 | +0.844 | 0.3985 |  |
| Age (years) | -0.0307 | 0.0898 | ±0.1796 | -0.342 | 0.7324 |  |
| BMI (kg/m2) | +0.0215 | 0.1541 | ±0.3082 | +0.139 | 0.8892 |  |
| Hypertension | -0.5066 | 1.6819 | ±3.3638 | -0.301 | 0.7632 |  |
| High cholesterol | +0.3453 | 1.7050 | ±3.4100 | +0.203 | 0.8395 |  |
| Kidney disease | +1.0839 | 6.3480 | ±12.6960 | +0.171 | 0.8644 |  |
| Circulatory disease | -2.5928 | 3.7050 | ±7.4100 | -0.700 | 0.4840 |  |
| Avg. daily SD (mg/dL) | +0.3386 | 0.3316 | ±0.6632 | +1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **61**, R² = **0.2249**, Adj R² = **0.0508**, F-statistic = **1.29** (p = **0.2572**), Residual SE = **5.617** on **49** df, AIC = **394.3**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.9077 | 8.8169 | ±17.6338 | +0.443 | 0.6576 |  |
| Education: graduate level (vs college) | -2.1418 | 1.8219 | ±3.6438 | -1.176 | 0.2398 |  |
| Education: high school or below (vs college) | +6.7977 | 6.1496 | ±12.2991 | +1.105 | 0.2690 |  |
| Site: UCSD (vs UAB) | +1.0841 | 2.0156 | ±4.0313 | +0.538 | 0.5907 |  |
| Site: UW (vs UAB) | +2.0890 | 2.5868 | ±5.1737 | +0.808 | 0.4194 |  |
| Age (years) | -0.0076 | 0.0912 | ±0.1824 | -0.084 | 0.9334 |  |
| BMI (kg/m2) | +0.0292 | 0.1499 | ±0.2997 | +0.195 | 0.8457 |  |
| Hypertension | -0.0356 | 1.6626 | ±3.3252 | -0.021 | 0.9829 |  |
| High cholesterol | +0.2829 | 1.7367 | ±3.4734 | +0.163 | 0.8706 |  |
| Kidney disease | +1.8368 | 6.5896 | ±13.1791 | +0.279 | 0.7804 |  |
| Circulatory disease | -2.6819 | 3.9332 | ±7.8663 | -0.682 | 0.4953 |  |
| CV (%) | +0.1204 | 0.3886 | ±0.7772 | +0.310 | 0.7566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **61**, R² = **0.2257**, Adj R² = **0.0518**, F-statistic = **1.30** (p = **0.2539**), Residual SE = **5.614** on **49** df, AIC = **394.2**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.5644 | 10.9967 | ±21.9934 | +0.688 | 0.4915 |  |
| Education: graduate level (vs college) | -2.1283 | 1.7953 | ±3.5906 | -1.185 | 0.2358 |  |
| Education: high school or below (vs college) | +6.7418 | 6.1212 | ±12.2423 | +1.101 | 0.2707 |  |
| Site: UCSD (vs UAB) | +1.0874 | 2.0027 | ±4.0055 | +0.543 | 0.5871 |  |
| Site: UW (vs UAB) | +2.1188 | 2.5981 | ±5.1963 | +0.816 | 0.4148 |  |
| Age (years) | -0.0070 | 0.0907 | ±0.1813 | -0.077 | 0.9385 |  |
| BMI (kg/m2) | +0.0275 | 0.1507 | ±0.3014 | +0.182 | 0.8554 |  |
| Hypertension | -0.0341 | 1.6819 | ±3.3638 | -0.020 | 0.9838 |  |
| High cholesterol | +0.2798 | 1.7286 | ±3.4572 | +0.162 | 0.8714 |  |
| Kidney disease | +1.9088 | 6.2945 | ±12.5890 | +0.303 | 0.7617 |  |
| Circulatory disease | -2.6375 | 3.9453 | ±7.8907 | -0.668 | 0.5038 |  |
| Mean / SD ratio | -0.2682 | 0.6884 | ±1.3768 | -0.390 | 0.6969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2363**, Adj R² = **0.0648**, F-statistic = **1.38** (p = **0.2133**), Residual SE = **5.575** on **49** df, AIC = **393.4**, BIC = **418.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.2076 | 10.2178 | ±20.4357 | +0.999 | 0.3178 |  |
| Education: graduate level (vs college) | -2.1238 | 1.7835 | ±3.5671 | -1.191 | 0.2337 |  |
| Education: high school or below (vs college) | +6.5067 | 6.1275 | ±12.2549 | +1.062 | 0.2883 |  |
| Site: UCSD (vs UAB) | +0.8057 | 1.9996 | ±3.9992 | +0.403 | 0.6870 |  |
| Site: UW (vs UAB) | +2.1709 | 2.5426 | ±5.0853 | +0.854 | 0.3932 |  |
| Age (years) | -0.0197 | 0.0897 | ±0.1794 | -0.219 | 0.8266 |  |
| BMI (kg/m2) | +0.0230 | 0.1506 | ±0.3012 | +0.153 | 0.8784 |  |
| Hypertension | -0.3420 | 1.7363 | ±3.4727 | -0.197 | 0.8438 |  |
| High cholesterol | +0.2292 | 1.7325 | ±3.4649 | +0.132 | 0.8947 |  |
| Kidney disease | +1.7142 | 6.1443 | ±12.2886 | +0.279 | 0.7803 |  |
| Circulatory disease | -2.3308 | 3.9123 | ±7.8245 | -0.596 | 0.5513 |  |
| Avg. daily mean/SD | -0.4137 | 0.4856 | ±0.9712 | -0.852 | 0.3942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **61**, R² = **0.2340**, Adj R² = **0.0620**, F-statistic = **1.36** (p = **0.2217**), Residual SE = **5.584** on **49** df, AIC = **393.6**, BIC = **418.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3658 | 9.2429 | ±18.4857 | +0.364 | 0.7157 |  |
| Education: graduate level (vs college) | -2.1737 | 1.8083 | ±3.6166 | -1.202 | 0.2293 |  |
| Education: high school or below (vs college) | +6.4214 | 6.0126 | ±12.0251 | +1.068 | 0.2855 |  |
| Site: UCSD (vs UAB) | +0.9362 | 1.9400 | ±3.8800 | +0.483 | 0.6294 |  |
| Site: UW (vs UAB) | +1.9651 | 2.4357 | ±4.8714 | +0.807 | 0.4198 |  |
| Age (years) | -0.0203 | 0.0860 | ±0.1719 | -0.236 | 0.8137 |  |
| BMI (kg/m2) | +0.0086 | 0.1521 | ±0.3041 | +0.056 | 0.9550 |  |
| Hypertension | -0.0777 | 1.6848 | ±3.3697 | -0.046 | 0.9632 |  |
| High cholesterol | +0.3938 | 1.6654 | ±3.3309 | +0.236 | 0.8131 |  |
| Kidney disease | +2.4860 | 5.5327 | ±11.0654 | +0.449 | 0.6532 |  |
| Circulatory disease | -2.2519 | 4.1188 | ±8.2377 | -0.547 | 0.5846 |  |
| MAG (mg/dL/h) | +0.1110 | 0.1690 | ±0.3381 | +0.657 | 0.5114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **61**, R² = **0.2389**, Adj R² = **0.0681**, F-statistic = **1.40** (p = **0.2039**), Residual SE = **5.566** on **49** df, AIC = **393.2**, BIC = **418.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.0363 | 9.4933 | ±18.9866 | +0.214 | 0.8302 |  |
| Education: graduate level (vs college) | -2.0780 | 1.7079 | ±3.4159 | -1.217 | 0.2237 |  |
| Education: high school or below (vs college) | +6.5558 | 6.0433 | ±12.0867 | +1.085 | 0.2780 |  |
| Site: UCSD (vs UAB) | +0.8421 | 1.8981 | ±3.7962 | +0.444 | 0.6573 |  |
| Site: UW (vs UAB) | +2.0912 | 2.4900 | ±4.9800 | +0.840 | 0.4010 |  |
| Age (years) | -0.0293 | 0.0895 | ±0.1789 | -0.327 | 0.7434 |  |
| BMI (kg/m2) | +0.0284 | 0.1489 | ±0.2978 | +0.191 | 0.8486 |  |
| Hypertension | -0.1749 | 1.6731 | ±3.3461 | -0.105 | 0.9168 |  |
| High cholesterol | +0.2810 | 1.7370 | ±3.4740 | +0.162 | 0.8715 |  |
| Kidney disease | +1.7857 | 5.9169 | ±11.8338 | +0.302 | 0.7628 |  |
| Circulatory disease | -2.3918 | 3.8844 | ±7.7688 | -0.616 | 0.5381 |  |
| Avg. daily range (mg/dL) | +0.0652 | 0.0803 | ±0.1606 | +0.812 | 0.4167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **61**, R² = **0.2280**, Adj R² = **0.0547**, F-statistic = **1.32** (p = **0.2444**), Residual SE = **5.605** on **49** df, AIC = **394.0**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.0150 | 8.2722 | ±16.5445 | +0.848 | 0.3964 |  |
| Education: graduate level (vs college) | -2.1311 | 1.7918 | ±3.5836 | -1.189 | 0.2343 |  |
| Education: high school or below (vs college) | +6.9878 | 5.9745 | ±11.9489 | +1.170 | 0.2422 |  |
| Site: UCSD (vs UAB) | +1.1140 | 1.9389 | ±3.8779 | +0.575 | 0.5656 |  |
| Site: UW (vs UAB) | +1.9236 | 2.6392 | ±5.2784 | +0.729 | 0.4661 |  |
| Age (years) | -0.0142 | 0.0955 | ±0.1911 | -0.149 | 0.8817 |  |
| BMI (kg/m2) | +0.0240 | 0.1352 | ±0.2703 | +0.177 | 0.8591 |  |
| Hypertension | +0.2261 | 1.7338 | ±3.4677 | +0.130 | 0.8963 |  |
| High cholesterol | +0.3505 | 1.7748 | ±3.5496 | +0.197 | 0.8435 |  |
| Kidney disease | +2.7010 | 6.7968 | ±13.5936 | +0.397 | 0.6911 |  |
| Circulatory disease | -2.5382 | 3.6167 | ±7.2335 | -0.702 | 0.4828 |  |
| SD of daily means (mg/dL) | -0.1856 | 0.4424 | ±0.8848 | -0.420 | 0.6748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **61**, R² = **0.2242**, Adj R² = **0.0501**, F-statistic = **1.29** (p = **0.2597**), Residual SE = **5.619** on **49** df, AIC = **394.3**, BIC = **419.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -71.6746 | 280.3807 | ±560.7615 | -0.256 | 0.7982 |  |
| Education: graduate level (vs college) | -2.1525 | 1.7572 | ±3.5145 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +6.7895 | 5.9169 | ±11.8338 | +1.147 | 0.2512 |  |
| Site: UCSD (vs UAB) | +1.2274 | 1.9874 | ±3.9748 | +0.618 | 0.5369 |  |
| Site: UW (vs UAB) | +2.0423 | 2.5935 | ±5.1871 | +0.787 | 0.4310 |  |
| Age (years) | -0.0020 | 0.0909 | ±0.1818 | -0.022 | 0.9824 |  |
| BMI (kg/m2) | +0.0376 | 0.1391 | ±0.2781 | +0.270 | 0.7868 |  |
| Hypertension | +0.2005 | 1.7604 | ±3.5209 | +0.114 | 0.9093 |  |
| High cholesterol | +0.3043 | 1.7834 | ±3.5668 | +0.171 | 0.8645 |  |
| Kidney disease | +2.3932 | 6.0506 | ±12.1013 | +0.396 | 0.6925 |  |
| Circulatory disease | -2.8898 | 4.2038 | ±8.4075 | -0.687 | 0.4918 |  |
| Time in range 70-180, pooled (%) | +0.7689 | 2.8274 | ±5.6548 | +0.272 | 0.7857 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **61**, R² = **0.2229**, Adj R² = **0.0484**, F-statistic = **1.28** (p = **0.2653**), Residual SE = **5.624** on **49** df, AIC = **394.4**, BIC = **419.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +38.5458 | 332.0928 | ±664.1857 | +0.116 | 0.9076 |  |
| Education: graduate level (vs college) | -2.0913 | 1.7128 | ±3.4256 | -1.221 | 0.2221 |  |
| Education: high school or below (vs college) | +6.9241 | 5.8893 | ±11.7786 | +1.176 | 0.2397 |  |
| Site: UCSD (vs UAB) | +1.1923 | 1.9793 | ±3.9585 | +0.602 | 0.5469 |  |
| Site: UW (vs UAB) | +2.0251 | 2.5949 | ±5.1898 | +0.780 | 0.4351 |  |
| Age (years) | -0.0068 | 0.0862 | ±0.1724 | -0.079 | 0.9373 |  |
| BMI (kg/m2) | +0.0309 | 0.1407 | ±0.2814 | +0.219 | 0.8264 |  |
| Hypertension | +0.1541 | 1.7741 | ±3.5481 | +0.087 | 0.9308 |  |
| High cholesterol | +0.2775 | 1.8192 | ±3.6384 | +0.153 | 0.8788 |  |
| Kidney disease | +2.1281 | 6.1488 | ±12.2976 | +0.346 | 0.7293 |  |
| Circulatory disease | -2.6855 | 4.2412 | ±8.4824 | -0.633 | 0.5266 |  |
| Avg. daily time in range 70-180 (%) | -0.3328 | 3.3282 | ±6.6564 | -0.100 | 0.9204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **61**, R² = **0.2344**, Adj R² = **0.0626**, F-statistic = **1.36** (p = **0.2200**), Residual SE = **5.582** on **49** df, AIC = **393.5**, BIC = **418.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.4984 | 8.8852 | ±17.7705 | +0.619 | 0.5360 |  |
| Education: graduate level (vs college) | -2.0850 | 1.8592 | ±3.7183 | -1.121 | 0.2621 |  |
| Education: high school or below (vs college) | +7.4532 | 6.8938 | ±13.7876 | +1.081 | 0.2796 |  |
| Site: UCSD (vs UAB) | +1.3282 | 1.9662 | ±3.9325 | +0.676 | 0.4993 |  |
| Site: UW (vs UAB) | +2.0781 | 2.6964 | ±5.3927 | +0.771 | 0.4409 |  |
| Age (years) | -0.0091 | 0.0976 | ±0.1953 | -0.093 | 0.9256 |  |
| BMI (kg/m2) | +0.0426 | 0.1458 | ±0.2916 | +0.292 | 0.7702 |  |
| Hypertension | +0.2877 | 1.8053 | ±3.6107 | +0.159 | 0.8734 |  |
| High cholesterol | +0.3024 | 1.7803 | ±3.5606 | +0.170 | 0.8651 |  |
| Kidney disease | +1.9525 | 6.3106 | ±12.6211 | +0.309 | 0.7570 |  |
| Circulatory disease | -3.0620 | 4.3668 | ±8.7337 | -0.701 | 0.4832 |  |
| Time 54-69, pooled (%) | -3.2878 | 5.4290 | ±10.8580 | -0.606 | 0.5448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **61**, R² = **0.2251**, Adj R² = **0.0511**, F-statistic = **1.29** (p = **0.2562**), Residual SE = **5.616** on **49** df, AIC = **394.3**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9539 | 8.1940 | ±16.3880 | +0.605 | 0.5455 |  |
| Education: graduate level (vs college) | -2.1034 | 1.9154 | ±3.8308 | -1.098 | 0.2721 |  |
| Education: high school or below (vs college) | +7.1400 | 6.6033 | ±13.2066 | +1.081 | 0.2796 |  |
| Site: UCSD (vs UAB) | +1.2809 | 1.9855 | ±3.9709 | +0.645 | 0.5188 |  |
| Site: UW (vs UAB) | +2.0181 | 2.8151 | ±5.6303 | +0.717 | 0.4734 |  |
| Age (years) | -0.0010 | 0.0900 | ±0.1801 | -0.011 | 0.9914 |  |
| BMI (kg/m2) | +0.0381 | 0.1416 | ±0.2832 | +0.269 | 0.7877 |  |
| Hypertension | +0.1873 | 1.8008 | ±3.6015 | +0.104 | 0.9172 |  |
| High cholesterol | +0.3386 | 1.9221 | ±3.8441 | +0.176 | 0.8601 |  |
| Kidney disease | +2.1319 | 6.1254 | ±12.2508 | +0.348 | 0.7278 |  |
| Circulatory disease | -2.8772 | 4.4514 | ±8.9027 | -0.646 | 0.5180 |  |
| Avg. daily time 54-69 (%) | -1.6162 | 6.9138 | ±13.8276 | -0.234 | 0.8152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **61**, R² = **0.2414**, Adj R² = **0.0711**, F-statistic = **1.42** (p = **0.1954**), Residual SE = **5.557** on **49** df, AIC = **393.0**, BIC = **418.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +6.0318 | 9.1141 | ±18.2282 | +0.662 | 0.5081 |  |
| Education: graduate level (vs college) | -2.0785 | 1.8233 | ±3.6467 | -1.140 | 0.2543 |  |
| Education: high school or below (vs college) | +7.4087 | 6.7639 | ±13.5278 | +1.095 | 0.2734 |  |
| Site: UCSD (vs UAB) | +1.2518 | 1.9756 | ±3.9512 | +0.634 | 0.5263 |  |
| Site: UW (vs UAB) | +2.0622 | 2.6752 | ±5.3505 | +0.771 | 0.4408 |  |
| Age (years) | -0.0172 | 0.1001 | ±0.2001 | -0.172 | 0.8636 |  |
| BMI (kg/m2) | +0.0472 | 0.1470 | ±0.2941 | +0.321 | 0.7482 |  |
| Hypertension | +0.3418 | 1.8055 | ±3.6111 | +0.189 | 0.8499 |  |
| High cholesterol | +0.2437 | 1.7299 | ±3.4598 | +0.141 | 0.8880 |  |
| Kidney disease | +1.9062 | 6.2946 | ±12.5891 | +0.303 | 0.7620 |  |
| Circulatory disease | -3.1552 | 4.2640 | ±8.5281 | -0.740 | 0.4593 |  |
| Time < 70 (%) | -3.6592 | 4.1336 | ±8.2671 | -0.885 | 0.3760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **61**, R² = **0.2267**, Adj R² = **0.0531**, F-statistic = **1.31** (p = **0.2499**), Residual SE = **5.610** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9652 | 8.3116 | ±16.6231 | +0.597 | 0.5503 |  |
| Education: graduate level (vs college) | -2.1257 | 1.8708 | ±3.7416 | -1.136 | 0.2559 |  |
| Education: high school or below (vs college) | +7.1637 | 6.5401 | ±13.0802 | +1.095 | 0.2734 |  |
| Site: UCSD (vs UAB) | +1.3002 | 1.9879 | ±3.9758 | +0.654 | 0.5131 |  |
| Site: UW (vs UAB) | +2.0382 | 2.7547 | ±5.5094 | +0.740 | 0.4594 |  |
| Age (years) | -0.0012 | 0.0911 | ±0.1822 | -0.013 | 0.9898 |  |
| BMI (kg/m2) | +0.0392 | 0.1430 | ±0.2860 | +0.274 | 0.7840 |  |
| Hypertension | +0.1997 | 1.7996 | ±3.5991 | +0.111 | 0.9117 |  |
| High cholesterol | +0.3719 | 1.9498 | ±3.8996 | +0.191 | 0.8487 |  |
| Kidney disease | +2.1134 | 6.1466 | ±12.2931 | +0.344 | 0.7310 |  |
| Circulatory disease | -2.9205 | 4.4259 | ±8.8517 | -0.660 | 0.5093 |  |
| Avg. daily time < 70 (%) | -1.9684 | 6.3136 | ±12.6273 | -0.312 | 0.7552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2379**, Adj R² = **0.0668**, F-statistic = **1.39** (p = **0.2073**), Residual SE = **5.569** on **49** df, AIC = **393.3**, BIC = **418.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1059.2279 | 700.1632 | ±1400.3265 | -1.513 | 0.1303 |  |
| Education: graduate level (vs college) | -2.0345 | 1.7480 | ±3.4961 | -1.164 | 0.2445 |  |
| Education: high school or below (vs college) | +6.5835 | 5.9574 | ±11.9148 | +1.105 | 0.2691 |  |
| Site: UCSD (vs UAB) | +0.8474 | 2.0187 | ±4.0375 | +0.420 | 0.6746 |  |
| Site: UW (vs UAB) | +1.8023 | 2.4475 | ±4.8950 | +0.736 | 0.4615 |  |
| Age (years) | -0.0282 | 0.0926 | ±0.1852 | -0.304 | 0.7609 |  |
| BMI (kg/m2) | +0.0377 | 0.1436 | ±0.2872 | +0.262 | 0.7930 |  |
| Hypertension | +0.1839 | 1.7808 | ±3.5616 | +0.103 | 0.9178 |  |
| High cholesterol | +0.0244 | 1.7256 | ±3.4513 | +0.014 | 0.9887 |  |
| Kidney disease | +2.2684 | 5.6594 | ±11.3187 | +0.401 | 0.6886 |  |
| Circulatory disease | -2.9021 | 3.6965 | ±7.3929 | -0.785 | 0.4324 |  |
| Time 54-250, pooled (%) | +10.6633 | 7.0229 | ±14.0457 | +1.518 | 0.1289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2290**, Adj R² = **0.0559**, F-statistic = **1.32** (p = **0.2407**), Residual SE = **5.602** on **49** df, AIC = **394.0**, BIC = **419.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1543.3750 | 2520.4766 | ±5040.9532 | -0.612 | 0.5403 |  |
| Education: graduate level (vs college) | -2.1965 | 1.7822 | ±3.5643 | -1.232 | 0.2178 |  |
| Education: high school or below (vs college) | +6.6651 | 5.9260 | ±11.8521 | +1.125 | 0.2607 |  |
| Site: UCSD (vs UAB) | +1.0846 | 2.0255 | ±4.0510 | +0.535 | 0.5923 |  |
| Site: UW (vs UAB) | +1.9445 | 2.5392 | ±5.0783 | +0.766 | 0.4438 |  |
| Age (years) | -0.0142 | 0.0944 | ±0.1888 | -0.150 | 0.8806 |  |
| BMI (kg/m2) | +0.0235 | 0.1434 | ±0.2869 | +0.164 | 0.8699 |  |
| Hypertension | +0.0652 | 1.8077 | ±3.6155 | +0.036 | 0.9712 |  |
| High cholesterol | +0.3228 | 1.7568 | ±3.5136 | +0.184 | 0.8542 |  |
| Kidney disease | +2.3726 | 5.7305 | ±11.4610 | +0.414 | 0.6788 |  |
| Circulatory disease | -2.8403 | 3.7080 | ±7.4159 | -0.766 | 0.4437 |  |
| Avg. daily time 54-250 (%) | +15.4977 | 25.2216 | ±50.4433 | +0.614 | 0.5389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **61**, R² = **0.2271**, Adj R² = **0.0536**, F-statistic = **1.31** (p = **0.2481**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.4482 | 8.4729 | ±16.9458 | +0.643 | 0.5202 |  |
| Education: graduate level (vs college) | -2.0113 | 1.6639 | ±3.3277 | -1.209 | 0.2267 |  |
| Education: high school or below (vs college) | +7.3391 | 6.3383 | ±12.6766 | +1.158 | 0.2469 |  |
| Site: UCSD (vs UAB) | +1.1936 | 1.9889 | ±3.9778 | +0.600 | 0.5484 |  |
| Site: UW (vs UAB) | +1.9934 | 2.4593 | ±4.9186 | +0.811 | 0.4176 |  |
| Age (years) | -0.0131 | 0.0918 | ±0.1835 | -0.143 | 0.8862 |  |
| BMI (kg/m2) | +0.0279 | 0.1494 | ±0.2988 | +0.187 | 0.8520 |  |
| Hypertension | +0.1440 | 1.7927 | ±3.5854 | +0.080 | 0.9360 |  |
| High cholesterol | +0.2202 | 1.7750 | ±3.5499 | +0.124 | 0.9013 |  |
| Kidney disease | +1.7209 | 6.2856 | ±12.5712 | +0.274 | 0.7843 |  |
| Circulatory disease | -2.6140 | 3.8707 | ±7.7415 | -0.675 | 0.4995 |  |
| Time 181-250, pooled (%) | +1.5883 | 3.3756 | ±6.7512 | +0.471 | 0.6380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **61**, R² = **0.2273**, Adj R² = **0.0539**, F-statistic = **1.31** (p = **0.2471**), Residual SE = **5.608** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.6932 | 8.5842 | ±17.1685 | +0.663 | 0.5072 |  |
| Education: graduate level (vs college) | -1.9957 | 1.6239 | ±3.2478 | -1.229 | 0.2191 |  |
| Education: high school or below (vs college) | +7.2528 | 6.3172 | ±12.6344 | +1.148 | 0.2509 |  |
| Site: UCSD (vs UAB) | +1.1480 | 1.9837 | ±3.9674 | +0.579 | 0.5628 |  |
| Site: UW (vs UAB) | +1.9865 | 2.4623 | ±4.9246 | +0.807 | 0.4198 |  |
| Age (years) | -0.0178 | 0.0921 | ±0.1842 | -0.193 | 0.8472 |  |
| BMI (kg/m2) | +0.0287 | 0.1502 | ±0.3005 | +0.191 | 0.8487 |  |
| Hypertension | +0.1440 | 1.7896 | ±3.5792 | +0.080 | 0.9359 |  |
| High cholesterol | +0.2949 | 1.7282 | ±3.4564 | +0.171 | 0.8645 |  |
| Kidney disease | +1.7387 | 6.3148 | ±12.6297 | +0.275 | 0.7831 |  |
| Circulatory disease | -2.6144 | 3.9008 | ±7.8016 | -0.670 | 0.5027 |  |
| Avg. daily time 181-250 (%) | +1.6247 | 3.4632 | ±6.9263 | +0.469 | 0.6390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **61**, R² = **0.2272**, Adj R² = **0.0537**, F-statistic = **1.31** (p = **0.2476**), Residual SE = **5.608** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.3699 | 8.4333 | ±16.8665 | +0.637 | 0.5243 |  |
| Education: graduate level (vs college) | -2.0220 | 1.6702 | ±3.3404 | -1.211 | 0.2260 |  |
| Education: high school or below (vs college) | +7.3389 | 6.3146 | ±12.6292 | +1.162 | 0.2451 |  |
| Site: UCSD (vs UAB) | +1.2100 | 1.9904 | ±3.9807 | +0.608 | 0.5432 |  |
| Site: UW (vs UAB) | +2.0180 | 2.4692 | ±4.9384 | +0.817 | 0.4138 |  |
| Age (years) | -0.0127 | 0.0912 | ±0.1824 | -0.139 | 0.8893 |  |
| BMI (kg/m2) | +0.0286 | 0.1490 | ±0.2980 | +0.192 | 0.8476 |  |
| Hypertension | +0.1578 | 1.7934 | ±3.5868 | +0.088 | 0.9299 |  |
| High cholesterol | +0.2332 | 1.7626 | ±3.5252 | +0.132 | 0.8947 |  |
| Kidney disease | +1.7054 | 6.2875 | ±12.5749 | +0.271 | 0.7862 |  |
| Circulatory disease | -2.6150 | 3.8640 | ±7.7280 | -0.677 | 0.4986 |  |
| Time > 180 (%) | +1.5874 | 3.2718 | ±6.5436 | +0.485 | 0.6276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **61**, R² = **0.2275**, Adj R² = **0.0540**, F-statistic = **1.31** (p = **0.2466**), Residual SE = **5.607** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.6016 | 8.5255 | ±17.0510 | +0.657 | 0.5112 |  |
| Education: graduate level (vs college) | -2.0086 | 1.6352 | ±3.2704 | -1.228 | 0.2193 |  |
| Education: high school or below (vs college) | +7.2497 | 6.2911 | ±12.5822 | +1.152 | 0.2492 |  |
| Site: UCSD (vs UAB) | +1.1667 | 1.9818 | ±3.9635 | +0.589 | 0.5560 |  |
| Site: UW (vs UAB) | +2.0142 | 2.4765 | ±4.9530 | +0.813 | 0.4160 |  |
| Age (years) | -0.0171 | 0.0912 | ±0.1824 | -0.188 | 0.8509 |  |
| BMI (kg/m2) | +0.0295 | 0.1498 | ±0.2995 | +0.197 | 0.8437 |  |
| Hypertension | +0.1595 | 1.7936 | ±3.5872 | +0.089 | 0.9292 |  |
| High cholesterol | +0.3092 | 1.7199 | ±3.4397 | +0.180 | 0.8573 |  |
| Kidney disease | +1.7253 | 6.3126 | ±12.6251 | +0.273 | 0.7846 |  |
| Circulatory disease | -2.6165 | 3.8913 | ±7.7826 | -0.672 | 0.5013 |  |
| Avg. daily time > 180 (%) | +1.6105 | 3.3380 | ±6.6760 | +0.482 | 0.6295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 61; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, events = **14**, McFadden pseudo-R² = **0.2203**, LLR χ² = **14.48** (p = **0.1523**), AUC = **0.7918**, AIC = **73.2**, BIC = **96.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0737 | 3.4742 | ±6.9484 | -0.309 | 0.7573 | 0.3418 |  |
| Education: graduate level (vs college) | -1.4373 | 0.9328 | ±1.8656 | -1.541 | 0.1234 | 0.2376 |  |
| **Education: high school or below (vs college)** | **+3.1891** | 1.5120 | ±3.0240 | **+2.109** | **0.0349** | 24.2668 | * |
| Site: UCSD (vs UAB) | -0.0642 | 0.9548 | ±1.9095 | -0.067 | 0.9464 | 0.9378 |  |
| Site: UW (vs UAB) | +1.2479 | 1.0258 | ±2.0516 | +1.217 | 0.2238 | 3.4829 |  |
| Age (years) | +0.0151 | 0.0418 | ±0.0835 | +0.361 | 0.7184 | 1.0152 |  |
| BMI (kg/m2) | -0.0339 | 0.0601 | ±0.1203 | -0.563 | 0.5731 | 0.9667 |  |
| Hypertension | +0.7195 | 0.8346 | ±1.6692 | +0.862 | 0.3887 | 2.0533 |  |
| High cholesterol | -0.8834 | 0.7722 | ±1.5445 | -1.144 | 0.2527 | 0.4134 |  |
| Kidney disease | +1.1169 | 2.5161 | ±5.0321 | +0.444 | 0.6571 | 3.0554 |  |
| Circulatory disease | -1.5827 | 1.4856 | ±2.9712 | -1.065 | 0.2867 | 0.2054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
