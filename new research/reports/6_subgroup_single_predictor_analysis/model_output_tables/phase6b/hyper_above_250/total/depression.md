# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Total analysis base - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 793; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1360**, F-statistic = **13.47** (p = **5.13e-22**), Residual SE = **4.800** on **782** df, AIC = **4749.2**, BIC = **4800.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5398** | 1.4612 | ±2.9224 | **+7.213** | **5.47e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0567** | 0.3573 | ±0.7145 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4950** | 0.6077 | ±1.2153 | **+2.460** | **0.0139** | * |
| Site: UCSD (vs UAB) | -0.2142 | 0.4675 | ±0.9349 | -0.458 | 0.6468 |  |
| Site: UW (vs UAB) | -0.7134 | 0.4037 | ±0.8075 | -1.767 | 0.0772 | . |
| **Age (years)** | **-0.1135** | 0.0162 | ±0.0325 | **-6.990** | **2.74e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0274 | ±0.0548 | **+2.351** | **0.0187** | * |
| Hypertension | +0.3963 | 0.3727 | ±0.7454 | +1.063 | 0.2876 |  |
| High cholesterol | +0.4108 | 0.3621 | ±0.7242 | +1.135 | 0.2565 |  |
| Kidney disease | +0.9556 | 0.5192 | ±1.0384 | +1.841 | 0.0657 | . |
| **Circulatory disease** | **+1.6761** | 0.5081 | ±1.0163 | **+3.299** | **9.72e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **793**, R² = **0.1491**, Adj R² = **0.1371**, F-statistic = **12.44** (p = **7.71e-22**), Residual SE = **4.797** on **781** df, AIC = **4749.2**, BIC = **4805.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4280** | 1.7288 | ±3.4576 | **+5.453** | **4.94e-08** | *** |
| **Education: graduate level (vs college)** | **-1.0187** | 0.3576 | ±0.7151 | **-2.849** | **0.0044** | ** |
| **Education: high school or below (vs college)** | **+1.3926** | 0.6047 | ±1.2094 | **+2.303** | **0.0213** | * |
| Site: UCSD (vs UAB) | -0.1852 | 0.4681 | ±0.9361 | -0.396 | 0.6923 |  |
| Site: UW (vs UAB) | -0.6679 | 0.4083 | ±0.8167 | -1.636 | 0.1019 |  |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.954** | **3.56e-12** | *** |
| **BMI (kg/m2)** | **+0.0588** | 0.0279 | ±0.0558 | **+2.107** | **0.0351** | * |
| Hypertension | +0.3715 | 0.3749 | ±0.7498 | +0.991 | 0.3217 |  |
| High cholesterol | +0.3900 | 0.3605 | ±0.7210 | +1.082 | 0.2793 |  |
| Kidney disease | +0.9497 | 0.5208 | ±1.0416 | +1.823 | 0.0682 | . |
| **Circulatory disease** | **+1.6391** | 0.5088 | ±1.0177 | **+3.221** | **0.0013** | ** |
| HbA1c (%) | +0.1862 | 0.1536 | ±0.3071 | +1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.32** (p = **1.31e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.3**, BIC = **4806.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9602** | 1.6263 | ±3.2526 | **+6.124** | **9.10e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0436** | 0.3576 | ±0.7153 | **-2.918** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4335** | 0.6109 | ±1.2218 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | -0.1854 | 0.4697 | ±0.9393 | -0.395 | 0.6930 |  |
| Site: UW (vs UAB) | -0.6853 | 0.4090 | ±0.8181 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.948** | **3.70e-12** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0277 | ±0.0553 | **+2.215** | **0.0267** | * |
| Hypertension | +0.3852 | 0.3734 | ±0.7468 | +1.032 | 0.3022 |  |
| High cholesterol | +0.4035 | 0.3617 | ±0.7235 | +1.115 | 0.2646 |  |
| Kidney disease | +0.9322 | 0.5252 | ±1.0504 | +1.775 | 0.0759 | . |
| **Circulatory disease** | **+1.6471** | 0.5094 | ±1.0189 | **+3.233** | **0.0012** | ** |
| Mean glucose (mg/dL) | +0.0040 | 0.0049 | ±0.0099 | +0.819 | 0.4125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.32** (p = **1.31e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.3**, BIC = **4806.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4010** | 2.0180 | ±4.0360 | **+4.659** | **3.18e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0436** | 0.3576 | ±0.7153 | **-2.918** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4335** | 0.6109 | ±1.2218 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | -0.1854 | 0.4697 | ±0.9393 | -0.395 | 0.6930 |  |
| Site: UW (vs UAB) | -0.6853 | 0.4090 | ±0.8181 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.948** | **3.70e-12** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0277 | ±0.0553 | **+2.215** | **0.0267** | * |
| Hypertension | +0.3852 | 0.3734 | ±0.7468 | +1.032 | 0.3022 |  |
| High cholesterol | +0.4035 | 0.3617 | ±0.7235 | +1.115 | 0.2646 |  |
| Kidney disease | +0.9322 | 0.5252 | ±1.0504 | +1.775 | 0.0759 | . |
| **Circulatory disease** | **+1.6471** | 0.5094 | ±1.0189 | **+3.233** | **0.0012** | ** |
| GMI (%) | +0.1690 | 0.2062 | ±0.4124 | +0.819 | 0.4125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **793**, R² = **0.1488**, Adj R² = **0.1368**, F-statistic = **12.41** (p = **8.74e-22**), Residual SE = **4.798** on **781** df, AIC = **4749.4**, BIC = **4805.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7817** | 1.6025 | ±3.2051 | **+6.104** | **1.04e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0300** | 0.3581 | ±0.7162 | **-2.876** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+1.4172** | 0.6083 | ±1.2166 | **+2.330** | **0.0198** | * |
| Site: UCSD (vs UAB) | -0.1749 | 0.4684 | ±0.9368 | -0.373 | 0.7088 |  |
| Site: UW (vs UAB) | -0.6869 | 0.4069 | ±0.8138 | -1.688 | 0.0914 | . |
| **Age (years)** | **-0.1120** | 0.0163 | ±0.0326 | **-6.875** | **6.21e-12** | *** |
| **BMI (kg/m2)** | **+0.0587** | 0.0277 | ±0.0555 | **+2.118** | **0.0342** | * |
| Hypertension | +0.3853 | 0.3732 | ±0.7464 | +1.033 | 0.3018 |  |
| High cholesterol | +0.4031 | 0.3614 | ±0.7227 | +1.116 | 0.2646 |  |
| Kidney disease | +0.9432 | 0.5239 | ±1.0477 | +1.800 | 0.0718 | . |
| **Circulatory disease** | **+1.6385** | 0.5092 | ±1.0183 | **+3.218** | **0.0013** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0054 | 0.0046 | ±0.0092 | +1.180 | 0.2382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1494**, Adj R² = **0.1374**, F-statistic = **12.47** (p = **6.82e-22**), Residual SE = **4.796** on **781** df, AIC = **4748.9**, BIC = **4805.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.8444** | 1.5486 | ±3.0972 | **+6.357** | **2.06e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0215** | 0.3571 | ±0.7141 | **-2.861** | **0.0042** | ** |
| **Education: high school or below (vs college)** | **+1.4176** | 0.6092 | ±1.2185 | **+2.327** | **0.0200** | * |
| Site: UCSD (vs UAB) | -0.1702 | 0.4687 | ±0.9373 | -0.363 | 0.7164 |  |
| Site: UW (vs UAB) | -0.6353 | 0.4116 | ±0.8231 | -1.544 | 0.1227 |  |
| **Age (years)** | **-0.1137** | 0.0163 | ±0.0325 | **-6.988** | **2.78e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0556 | **+2.153** | **0.0313** | * |
| Hypertension | +0.3653 | 0.3750 | ±0.7499 | +0.974 | 0.3299 |  |
| High cholesterol | +0.4189 | 0.3610 | ±0.7219 | +1.161 | 0.2458 |  |
| Kidney disease | +0.8209 | 0.5353 | ±1.0707 | +1.533 | 0.1252 |  |
| **Circulatory disease** | **+1.6389** | 0.5098 | ±1.0196 | **+3.215** | **0.0013** | ** |
| Glucose SD, pooled (mg/dL) | +0.0222 | 0.0158 | ±0.0315 | +1.408 | 0.1592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1357**, F-statistic = **12.31** (p = **1.37e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.4**, BIC = **4806.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1214** | 1.5381 | ±3.0763 | **+6.580** | **4.70e-11** | *** |
| **Education: graduate level (vs college)** | **-1.0410** | 0.3569 | ±0.7137 | **-2.917** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4464** | 0.6123 | ±1.2246 | **+2.362** | **0.0182** | * |
| Site: UCSD (vs UAB) | -0.1885 | 0.4699 | ±0.9397 | -0.401 | 0.6882 |  |
| Site: UW (vs UAB) | -0.6719 | 0.4102 | ±0.8203 | -1.638 | 0.1014 |  |
| **Age (years)** | **-0.1138** | 0.0163 | ±0.0325 | **-6.993** | **2.69e-12** | *** |
| **BMI (kg/m2)** | **+0.0625** | 0.0277 | ±0.0553 | **+2.258** | **0.0239** | * |
| Hypertension | +0.3811 | 0.3754 | ±0.7507 | +1.015 | 0.3099 |  |
| High cholesterol | +0.4146 | 0.3620 | ±0.7241 | +1.145 | 0.2522 |  |
| Kidney disease | +0.8722 | 0.5364 | ±1.0728 | +1.626 | 0.1039 |  |
| **Circulatory disease** | **+1.6578** | 0.5097 | ±1.0194 | **+3.252** | **0.0011** | ** |
| Avg. daily SD (mg/dL) | +0.0146 | 0.0178 | ±0.0357 | +0.817 | 0.4137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.26** (p = **1.68e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4807.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1464** | 1.6337 | ±3.2673 | **+6.211** | **5.27e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0461** | 0.3568 | ±0.7136 | **-2.932** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4923** | 0.6085 | ±1.2171 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | -0.2048 | 0.4684 | ±0.9367 | -0.437 | 0.6620 |  |
| Site: UW (vs UAB) | -0.6892 | 0.4064 | ±0.8128 | -1.696 | 0.0899 | . |
| **Age (years)** | **-0.1139** | 0.0162 | ±0.0324 | **-7.022** | **2.19e-12** | *** |
| **BMI (kg/m2)** | **+0.0641** | 0.0275 | ±0.0551 | **+2.326** | **0.0200** | * |
| Hypertension | +0.3861 | 0.3748 | ±0.7495 | +1.030 | 0.3029 |  |
| High cholesterol | +0.4222 | 0.3637 | ±0.7274 | +1.161 | 0.2457 |  |
| Kidney disease | +0.9036 | 0.5252 | ±1.0505 | +1.720 | 0.0854 | . |
| **Circulatory disease** | **+1.6753** | 0.5092 | ±1.0184 | **+3.290** | **0.0010** | ** |
| CV (%) | +0.0179 | 0.0326 | ±0.0652 | +0.549 | 0.5831 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **793**, R² = **0.1476**, Adj R² = **0.1356**, F-statistic = **12.29** (p = **1.47e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1791** | 1.6856 | ±3.3713 | **+6.632** | **3.31e-11** | *** |
| **Education: graduate level (vs college)** | **-1.0442** | 0.3570 | ±0.7140 | **-2.925** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4927** | 0.6083 | ±1.2166 | **+2.454** | **0.0141** | * |
| Site: UCSD (vs UAB) | -0.2091 | 0.4678 | ±0.9355 | -0.447 | 0.6549 |  |
| Site: UW (vs UAB) | -0.6850 | 0.4052 | ±0.8105 | -1.690 | 0.0910 | . |
| **Age (years)** | **-0.1140** | 0.0162 | ±0.0324 | **-7.027** | **2.11e-12** | *** |
| **BMI (kg/m2)** | **+0.0643** | 0.0275 | ±0.0551 | **+2.334** | **0.0196** | * |
| Hypertension | +0.3828 | 0.3750 | ±0.7499 | +1.021 | 0.3073 |  |
| High cholesterol | +0.4187 | 0.3626 | ±0.7253 | +1.155 | 0.2482 |  |
| Kidney disease | +0.8944 | 0.5224 | ±1.0449 | +1.712 | 0.0869 | . |
| **Circulatory disease** | **+1.6691** | 0.5090 | ±1.0179 | **+3.280** | **0.0010** | ** |
| Mean / SD ratio | -0.1367 | 0.1799 | ±0.3597 | -0.760 | 0.4471 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1349**, F-statistic = **12.23** (p = **1.94e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.2**, BIC = **4807.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5731** | 1.6885 | ±3.3769 | **+6.262** | **3.80e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0561** | 0.3570 | ±0.7141 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4948** | 0.6086 | ±1.2172 | **+2.456** | **0.0140** | * |
| Site: UCSD (vs UAB) | -0.2140 | 0.4680 | ±0.9361 | -0.457 | 0.6475 |  |
| Site: UW (vs UAB) | -0.7120 | 0.4037 | ±0.8075 | -1.764 | 0.0778 | . |
| **Age (years)** | **-0.1135** | 0.0163 | ±0.0325 | **-6.977** | **3.01e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0274 | ±0.0549 | **+2.350** | **0.0188** | * |
| Hypertension | +0.3957 | 0.3751 | ±0.7501 | +1.055 | 0.2915 |  |
| High cholesterol | +0.4114 | 0.3633 | ±0.7265 | +1.133 | 0.2574 |  |
| Kidney disease | +0.9524 | 0.5218 | ±1.0436 | +1.825 | 0.0680 | . |
| **Circulatory disease** | **+1.6761** | 0.5088 | ±1.0176 | **+3.294** | **9.86e-04** | *** |
| Avg. daily mean/SD | -0.0061 | 0.1446 | ±0.2893 | -0.042 | 0.9663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **793**, R² = **0.1513**, Adj R² = **0.1394**, F-statistic = **12.66** (p = **2.91e-22**), Residual SE = **4.791** on **781** df, AIC = **4747.0**, BIC = **4803.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6502** | 1.7843 | ±3.5686 | **+4.848** | **1.25e-06** | *** |
| **Education: graduate level (vs college)** | **-0.9941** | 0.3573 | ±0.7146 | **-2.782** | **0.0054** | ** |
| **Education: high school or below (vs college)** | **+1.4580** | 0.6028 | ±1.2057 | **+2.418** | **0.0156** | * |
| Site: UCSD (vs UAB) | -0.1416 | 0.4681 | ±0.9361 | -0.302 | 0.7623 |  |
| Site: UW (vs UAB) | -0.5694 | 0.4140 | ±0.8279 | -1.376 | 0.1690 |  |
| **Age (years)** | **-0.1107** | 0.0162 | ±0.0324 | **-6.825** | **8.77e-12** | *** |
| **BMI (kg/m2)** | **+0.0619** | 0.0274 | ±0.0548 | **+2.260** | **0.0238** | * |
| Hypertension | +0.4172 | 0.3726 | ±0.7452 | +1.120 | 0.2629 |  |
| High cholesterol | +0.4651 | 0.3617 | ±0.7234 | +1.286 | 0.1985 |  |
| Kidney disease | +0.8785 | 0.5254 | ±1.0509 | +1.672 | 0.0945 | . |
| **Circulatory disease** | **+1.6558** | 0.5121 | ±1.0242 | **+3.233** | **0.0012** | ** |
| MAG (mg/dL/h) | +0.0369 | 0.0198 | ±0.0397 | +1.859 | 0.0631 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **793**, R² = **0.1474**, Adj R² = **0.1354**, F-statistic = **12.28** (p = **1.56e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.7**, BIC = **4806.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0293** | 1.6536 | ±3.3073 | **+6.065** | **1.32e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0442** | 0.3567 | ±0.7135 | **-2.927** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4574** | 0.6130 | ±1.2260 | **+2.378** | **0.0174** | * |
| Site: UCSD (vs UAB) | -0.1890 | 0.4709 | ±0.9418 | -0.401 | 0.6881 |  |
| Site: UW (vs UAB) | -0.6775 | 0.4107 | ±0.8214 | -1.650 | 0.0990 | . |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0325 | **-6.966** | **3.25e-12** | *** |
| **BMI (kg/m2)** | **+0.0634** | 0.0275 | ±0.0551 | **+2.302** | **0.0213** | * |
| Hypertension | +0.3925 | 0.3739 | ±0.7477 | +1.050 | 0.2938 |  |
| High cholesterol | +0.4163 | 0.3626 | ±0.7252 | +1.148 | 0.2509 |  |
| Kidney disease | +0.8905 | 0.5357 | ±1.0714 | +1.662 | 0.0964 | . |
| **Circulatory disease** | **+1.6601** | 0.5100 | ±1.0199 | **+3.255** | **0.0011** | ** |
| Avg. daily range (mg/dL) | +0.0034 | 0.0052 | ±0.0105 | +0.656 | 0.5120 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **793**, R² = **0.1572**, Adj R² = **0.1453**, F-statistic = **13.24** (p = **2.34e-23**), Residual SE = **4.774** on **781** df, AIC = **4741.6**, BIC = **4797.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.8582** | 1.4738 | ±2.9476 | **+6.689** | **2.25e-11** | *** |
| **Education: graduate level (vs college)** | **-0.9410** | 0.3577 | ±0.7154 | **-2.631** | **0.0085** | ** |
| **Education: high school or below (vs college)** | **+1.4228** | 0.6000 | ±1.2000 | **+2.371** | **0.0177** | * |
| Site: UCSD (vs UAB) | -0.1586 | 0.4645 | ±0.9290 | -0.342 | 0.7327 |  |
| Site: UW (vs UAB) | -0.5919 | 0.4059 | ±0.8118 | -1.458 | 0.1448 |  |
| **Age (years)** | **-0.1110** | 0.0164 | ±0.0328 | **-6.768** | **1.31e-11** | *** |
| BMI (kg/m2) | +0.0531 | 0.0277 | ±0.0555 | +1.915 | 0.0555 | . |
| Hypertension | +0.3172 | 0.3735 | ±0.7470 | +0.849 | 0.3957 |  |
| High cholesterol | +0.4164 | 0.3578 | ±0.7156 | +1.164 | 0.2445 |  |
| Kidney disease | +0.8397 | 0.5256 | ±1.0512 | +1.598 | 0.1102 |  |
| **Circulatory disease** | **+1.5678** | 0.5051 | ±1.0103 | **+3.104** | **0.0019** | ** |
| **SD of daily means (mg/dL)** | **+0.0664** | 0.0226 | ±0.0451 | **+2.943** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **793**, R² = **0.1483**, Adj R² = **0.1363**, F-statistic = **12.37** (p = **1.06e-21**), Residual SE = **4.799** on **781** df, AIC = **4749.9**, BIC = **4806.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2404** | 1.6145 | ±3.2291 | **+6.962** | **3.36e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0387** | 0.3575 | ±0.7150 | **-2.906** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.4219** | 0.6124 | ±1.2248 | **+2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | -0.1717 | 0.4707 | ±0.9413 | -0.365 | 0.7153 |  |
| Site: UW (vs UAB) | -0.6712 | 0.4108 | ±0.8215 | -1.634 | 0.1022 |  |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0326 | **-6.953** | **3.59e-12** | *** |
| **BMI (kg/m2)** | **+0.0597** | 0.0278 | ±0.0556 | **+2.148** | **0.0317** | * |
| Hypertension | +0.3874 | 0.3730 | ±0.7459 | +1.039 | 0.2990 |  |
| High cholesterol | +0.4108 | 0.3614 | ±0.7229 | +1.137 | 0.2557 |  |
| Kidney disease | +0.9109 | 0.5288 | ±1.0576 | +1.722 | 0.0850 | . |
| **Circulatory disease** | **+1.6460** | 0.5083 | ±1.0167 | **+3.238** | **0.0012** | ** |
| Time in range 70-180, pooled (%) | -0.0080 | 0.0078 | ±0.0156 | -1.025 | 0.3056 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **793**, R² = **0.1482**, Adj R² = **0.1362**, F-statistic = **12.35** (p = **1.15e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.0**, BIC = **4806.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1996** | 1.6208 | ±3.2416 | **+6.910** | **4.85e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0416** | 0.3575 | ±0.7149 | **-2.914** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4251** | 0.6130 | ±1.2259 | **+2.325** | **0.0201** | * |
| Site: UCSD (vs UAB) | -0.1722 | 0.4708 | ±0.9416 | -0.366 | 0.7146 |  |
| Site: UW (vs UAB) | -0.6733 | 0.4106 | ±0.8212 | -1.640 | 0.1010 |  |
| **Age (years)** | **-0.1134** | 0.0163 | ±0.0326 | **-6.957** | **3.47e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0557 | **+2.154** | **0.0313** | * |
| Hypertension | +0.3886 | 0.3730 | ±0.7459 | +1.042 | 0.2975 |  |
| High cholesterol | +0.4105 | 0.3615 | ±0.7231 | +1.135 | 0.2562 |  |
| Kidney disease | +0.9112 | 0.5289 | ±1.0577 | +1.723 | 0.0849 | . |
| **Circulatory disease** | **+1.6482** | 0.5086 | ±1.0172 | **+3.241** | **0.0012** | ** |
| Avg. daily time in range 70-180 (%) | -0.0075 | 0.0078 | ±0.0156 | -0.957 | 0.3388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **793**, R² = **0.1498**, Adj R² = **0.1378**, F-statistic = **12.51** (p = **5.65e-22**), Residual SE = **4.795** on **781** df, AIC = **4748.5**, BIC = **4804.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.2916** | 1.4637 | ±2.9274 | **+7.031** | **2.05e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0394** | 0.3569 | ±0.7138 | **-2.912** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.5321** | 0.6061 | ±1.2121 | **+2.528** | **0.0115** | * |
| Site: UCSD (vs UAB) | -0.1791 | 0.4657 | ±0.9315 | -0.385 | 0.7006 |  |
| Site: UW (vs UAB) | -0.6744 | 0.4028 | ±0.8055 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.1123** | 0.0163 | ±0.0327 | **-6.875** | **6.20e-12** | *** |
| **BMI (kg/m2)** | **+0.0640** | 0.0272 | ±0.0545 | **+2.350** | **0.0188** | * |
| Hypertension | +0.3602 | 0.3740 | ±0.7480 | +0.963 | 0.3355 |  |
| High cholesterol | +0.4604 | 0.3607 | ±0.7213 | +1.276 | 0.2018 |  |
| Kidney disease | +0.9446 | 0.5182 | ±1.0365 | +1.823 | 0.0684 | . |
| **Circulatory disease** | **+1.6441** | 0.5125 | ±1.0251 | **+3.208** | **0.0013** | ** |
| Any reading < 54 during wear (0/1) | +0.6632 | 0.4129 | ±0.8258 | +1.606 | 0.1082 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1349**, F-statistic = **12.23** (p = **1.94e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.2**, BIC = **4807.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5440** | 1.4660 | ±2.9320 | **+7.192** | **6.37e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0577** | 0.3576 | ±0.7152 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4937** | 0.6079 | ±1.2158 | **+2.457** | **0.0140** | * |
| Site: UCSD (vs UAB) | -0.2158 | 0.4685 | ±0.9369 | -0.461 | 0.6451 |  |
| Site: UW (vs UAB) | -0.7153 | 0.4056 | ±0.8113 | -1.764 | 0.0778 | . |
| **Age (years)** | **-0.1135** | 0.0162 | ±0.0325 | **-6.988** | **2.78e-12** | *** |
| **BMI (kg/m2)** | **+0.0644** | 0.0275 | ±0.0550 | **+2.342** | **0.0192** | * |
| Hypertension | +0.3964 | 0.3728 | ±0.7457 | +1.063 | 0.2877 |  |
| High cholesterol | +0.4094 | 0.3627 | ±0.7254 | +1.129 | 0.2590 |  |
| Kidney disease | +0.9554 | 0.5192 | ±1.0385 | +1.840 | 0.0658 | . |
| **Circulatory disease** | **+1.6754** | 0.5083 | ±1.0166 | **+3.296** | **9.81e-04** | *** |
| Time < 54 (%) | -0.0151 | 0.1685 | ±0.3371 | -0.090 | 0.9285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **793**, R² = **0.1470**, Adj R² = **0.1350**, F-statistic = **12.24** (p = **1.87e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.1**, BIC = **4807.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5198** | 1.4658 | ±2.9315 | **+7.177** | **7.13e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0514** | 0.3577 | ±0.7154 | **-2.940** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **+1.5027** | 0.6080 | ±1.2161 | **+2.471** | **0.0135** | * |
| Site: UCSD (vs UAB) | -0.2051 | 0.4686 | ±0.9372 | -0.438 | 0.6616 |  |
| Site: UW (vs UAB) | -0.7011 | 0.4062 | ±0.8123 | -1.726 | 0.0843 | . |
| **Age (years)** | **-0.1136** | 0.0163 | ±0.0325 | **-6.987** | **2.80e-12** | *** |
| **BMI (kg/m2)** | **+0.0646** | 0.0275 | ±0.0551 | **+2.349** | **0.0188** | * |
| Hypertension | +0.3956 | 0.3729 | ±0.7459 | +1.061 | 0.2888 |  |
| High cholesterol | +0.4203 | 0.3630 | ±0.7260 | +1.158 | 0.2470 |  |
| Kidney disease | +0.9549 | 0.5195 | ±1.0390 | +1.838 | 0.0661 | . |
| **Circulatory disease** | **+1.6801** | 0.5084 | ±1.0169 | **+3.304** | **9.52e-04** | *** |
| Avg. daily time < 54 (%) | +0.0988 | 0.3648 | ±0.7296 | +0.271 | 0.7866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.62e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4930** | 1.4621 | ±2.9243 | **+7.176** | **7.15e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0430** | 0.3574 | ±0.7147 | **-2.919** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.5085** | 0.6075 | ±1.2149 | **+2.483** | **0.0130** | * |
| Site: UCSD (vs UAB) | -0.1900 | 0.4675 | ±0.9350 | -0.406 | 0.6845 |  |
| Site: UW (vs UAB) | -0.6857 | 0.4047 | ±0.8094 | -1.694 | 0.0902 | . |
| **Age (years)** | **-0.1138** | 0.0162 | ±0.0325 | **-7.014** | **2.31e-12** | *** |
| **BMI (kg/m2)** | **+0.0644** | 0.0275 | ±0.0549 | **+2.345** | **0.0190** | * |
| Hypertension | +0.3883 | 0.3728 | ±0.7457 | +1.041 | 0.2977 |  |
| High cholesterol | +0.4368 | 0.3653 | ±0.7306 | +1.196 | 0.2318 |  |
| Kidney disease | +0.9459 | 0.5207 | ±1.0415 | +1.816 | 0.0693 | . |
| **Circulatory disease** | **+1.6904** | 0.5092 | ±1.0185 | **+3.320** | **9.02e-04** | *** |
| Time 54-69, pooled (%) | +0.1041 | 0.1688 | ±0.3377 | +0.616 | 0.5376 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.31** (p = **1.35e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.4**, BIC = **4806.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4876** | 1.4617 | ±2.9233 | **+7.175** | **7.23e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0353** | 0.3574 | ±0.7148 | **-2.897** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.5168** | 0.6077 | ±1.2154 | **+2.496** | **0.0126** | * |
| Site: UCSD (vs UAB) | -0.1794 | 0.4679 | ±0.9357 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -0.6695 | 0.4055 | ±0.8111 | -1.651 | 0.0987 | . |
| **Age (years)** | **-0.1141** | 0.0162 | ±0.0325 | **-7.025** | **2.14e-12** | *** |
| **BMI (kg/m2)** | **+0.0642** | 0.0275 | ±0.0550 | **+2.336** | **0.0195** | * |
| Hypertension | +0.3848 | 0.3728 | ±0.7456 | +1.032 | 0.3020 |  |
| High cholesterol | +0.4494 | 0.3648 | ±0.7296 | +1.232 | 0.2180 |  |
| Kidney disease | +0.9431 | 0.5202 | ±1.0404 | +1.813 | 0.0698 | . |
| **Circulatory disease** | **+1.6992** | 0.5096 | ±1.0193 | **+3.334** | **8.56e-04** | *** |
| Avg. daily time 54-69 (%) | +0.1411 | 0.1722 | ±0.3443 | +0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **793**, R² = **0.1471**, Adj R² = **0.1351**, F-statistic = **12.25** (p = **1.77e-21**), Residual SE = **4.802** on **781** df, AIC = **4751.0**, BIC = **4807.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4995** | 1.4646 | ±2.9293 | **+7.169** | **7.57e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0455** | 0.3574 | ±0.7148 | **-2.925** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.5069** | 0.6076 | ±1.2151 | **+2.480** | **0.0131** | * |
| Site: UCSD (vs UAB) | -0.1955 | 0.4680 | ±0.9360 | -0.418 | 0.6762 |  |
| Site: UW (vs UAB) | -0.6916 | 0.4053 | ±0.8107 | -1.706 | 0.0880 | . |
| **Age (years)** | **-0.1138** | 0.0162 | ±0.0325 | **-7.012** | **2.35e-12** | *** |
| **BMI (kg/m2)** | **+0.0646** | 0.0274 | ±0.0549 | **+2.355** | **0.0185** | * |
| Hypertension | +0.3920 | 0.3727 | ±0.7454 | +1.052 | 0.2929 |  |
| High cholesterol | +0.4300 | 0.3648 | ±0.7296 | +1.179 | 0.2385 |  |
| Kidney disease | +0.9512 | 0.5201 | ±1.0402 | +1.829 | 0.0674 | . |
| **Circulatory disease** | **+1.6865** | 0.5088 | ±1.0175 | **+3.315** | **9.17e-04** | *** |
| Time < 70 (%) | +0.0555 | 0.1075 | ±0.2149 | +0.516 | 0.6057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **793**, R² = **0.1476**, Adj R² = **0.1356**, F-statistic = **12.29** (p = **1.48e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4868** | 1.4636 | ±2.9272 | **+7.165** | **7.77e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0377** | 0.3575 | ±0.7150 | **-2.903** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.5165** | 0.6078 | ±1.2156 | **+2.495** | **0.0126** | * |
| Site: UCSD (vs UAB) | -0.1828 | 0.4683 | ±0.9365 | -0.390 | 0.6962 |  |
| Site: UW (vs UAB) | -0.6731 | 0.4060 | ±0.8121 | -1.658 | 0.0974 | . |
| **Age (years)** | **-0.1140** | 0.0162 | ±0.0325 | **-7.018** | **2.25e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0275 | ±0.0550 | **+2.346** | **0.0190** | * |
| Hypertension | +0.3880 | 0.3726 | ±0.7451 | +1.042 | 0.2976 |  |
| High cholesterol | +0.4450 | 0.3646 | ±0.7292 | +1.220 | 0.2223 |  |
| Kidney disease | +0.9467 | 0.5200 | ±1.0400 | +1.821 | 0.0687 | . |
| **Circulatory disease** | **+1.6950** | 0.5093 | ±1.0185 | **+3.328** | **8.74e-04** | *** |
| Avg. daily time < 70 (%) | +0.0926 | 0.1205 | ±0.2411 | +0.768 | 0.4422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **793**, R² = **0.1475**, Adj R² = **0.1355**, F-statistic = **12.29** (p = **1.50e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2393** | 1.8438 | ±3.6876 | **+6.096** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0369** | 0.3582 | ±0.7163 | **-2.895** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.4508** | 0.6096 | ±1.2191 | **+2.380** | **0.0173** | * |
| Site: UCSD (vs UAB) | -0.1895 | 0.4697 | ±0.9395 | -0.403 | 0.6866 |  |
| Site: UW (vs UAB) | -0.6815 | 0.4113 | ±0.8226 | -1.657 | 0.0975 | . |
| **Age (years)** | **-0.1125** | 0.0163 | ±0.0326 | **-6.901** | **5.16e-12** | *** |
| **BMI (kg/m2)** | **+0.0630** | 0.0276 | ±0.0552 | **+2.281** | **0.0225** | * |
| Hypertension | +0.3856 | 0.3731 | ±0.7462 | +1.034 | 0.3013 |  |
| High cholesterol | +0.4150 | 0.3623 | ±0.7246 | +1.146 | 0.2520 |  |
| Kidney disease | +0.9375 | 0.5232 | ±1.0464 | +1.792 | 0.0731 | . |
| **Circulatory disease** | **+1.6565** | 0.5107 | ±1.0214 | **+3.244** | **0.0012** | ** |
| Time 54-250, pooled (%) | -0.0079 | 0.0127 | ±0.0255 | -0.619 | 0.5358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.63e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1302** | 1.8717 | ±3.7433 | **+5.947** | **2.74e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0407** | 0.3580 | ±0.7160 | **-2.907** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.4587** | 0.6098 | ±1.2196 | **+2.392** | **0.0168** | * |
| Site: UCSD (vs UAB) | -0.1936 | 0.4700 | ±0.9400 | -0.412 | 0.6804 |  |
| Site: UW (vs UAB) | -0.6880 | 0.4108 | ±0.8215 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.1128** | 0.0163 | ±0.0326 | **-6.924** | **4.40e-12** | *** |
| **BMI (kg/m2)** | **+0.0632** | 0.0276 | ±0.0552 | **+2.288** | **0.0221** | * |
| Hypertension | +0.3881 | 0.3731 | ±0.7462 | +1.040 | 0.2982 |  |
| High cholesterol | +0.4143 | 0.3625 | ±0.7249 | +1.143 | 0.2530 |  |
| Kidney disease | +0.9391 | 0.5232 | ±1.0464 | +1.795 | 0.0727 | . |
| **Circulatory disease** | **+1.6590** | 0.5108 | ±1.0216 | **+3.248** | **0.0012** | ** |
| Avg. daily time 54-250 (%) | -0.0066 | 0.0130 | ±0.0259 | -0.507 | 0.6124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **793**, R² = **0.1481**, Adj R² = **0.1361**, F-statistic = **12.34** (p = **1.19e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5297** | 1.4658 | ±2.9315 | **+7.184** | **6.78e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0616** | 0.3578 | ±0.7156 | **-2.967** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+1.4504** | 0.6133 | ±1.2266 | **+2.365** | **0.0180** | * |
| Site: UCSD (vs UAB) | -0.1905 | 0.4697 | ±0.9395 | -0.405 | 0.6852 |  |
| Site: UW (vs UAB) | -0.7018 | 0.4054 | ±0.8109 | -1.731 | 0.0835 | . |
| **Age (years)** | **-0.1147** | 0.0163 | ±0.0327 | **-7.018** | **2.26e-12** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0278 | ±0.0556 | **+2.139** | **0.0324** | * |
| Hypertension | +0.4002 | 0.3729 | ±0.7458 | +1.073 | 0.2831 |  |
| High cholesterol | +0.4013 | 0.3620 | ±0.7239 | +1.109 | 0.2676 |  |
| Kidney disease | +0.9165 | 0.5286 | ±1.0572 | +1.734 | 0.0829 | . |
| **Circulatory disease** | **+1.6589** | 0.5065 | ±1.0131 | **+3.275** | **0.0011** | ** |
| Time 181-250, pooled (%) | +0.0122 | 0.0126 | ±0.0252 | +0.969 | 0.3327 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **793**, R² = **0.1481**, Adj R² = **0.1361**, F-statistic = **12.34** (p = **1.18e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5270** | 1.4664 | ±2.9328 | **+7.179** | **7.04e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0635** | 0.3579 | ±0.7159 | **-2.971** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+1.4467** | 0.6140 | ±1.2280 | **+2.356** | **0.0185** | * |
| Site: UCSD (vs UAB) | -0.1869 | 0.4698 | ±0.9395 | -0.398 | 0.6907 |  |
| Site: UW (vs UAB) | -0.6990 | 0.4057 | ±0.8114 | -1.723 | 0.0849 | . |
| **Age (years)** | **-0.1146** | 0.0163 | ±0.0327 | **-7.016** | **2.29e-12** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0278 | ±0.0557 | **+2.136** | **0.0327** | * |
| Hypertension | +0.3998 | 0.3728 | ±0.7455 | +1.073 | 0.2835 |  |
| High cholesterol | +0.4006 | 0.3620 | ±0.7239 | +1.107 | 0.2684 |  |
| Kidney disease | +0.9150 | 0.5287 | ±1.0574 | +1.731 | 0.0835 | . |
| **Circulatory disease** | **+1.6604** | 0.5069 | ±1.0137 | **+3.276** | **0.0011** | ** |
| Avg. daily time 181-250 (%) | +0.0121 | 0.0124 | ±0.0248 | +0.972 | 0.3309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **793**, R² = **0.1483**, Adj R² = **0.1363**, F-statistic = **12.36** (p = **1.10e-21**), Residual SE = **4.799** on **781** df, AIC = **4749.9**, BIC = **4806.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4483** | 1.4695 | ±2.9390 | **+7.110** | **1.16e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0409** | 0.3575 | ±0.7150 | **-2.912** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4230** | 0.6125 | ±1.2249 | **+2.323** | **0.0202** | * |
| Site: UCSD (vs UAB) | -0.1759 | 0.4704 | ±0.9408 | -0.374 | 0.7084 |  |
| Site: UW (vs UAB) | -0.6758 | 0.4100 | ±0.8201 | -1.648 | 0.0993 | . |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0326 | **-6.952** | **3.61e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0556 | **+2.155** | **0.0312** | * |
| Hypertension | +0.3883 | 0.3730 | ±0.7460 | +1.041 | 0.2978 |  |
| High cholesterol | +0.4082 | 0.3615 | ±0.7229 | +1.129 | 0.2588 |  |
| Kidney disease | +0.9132 | 0.5284 | ±1.0568 | +1.728 | 0.0840 | . |
| **Circulatory disease** | **+1.6457** | 0.5083 | ±1.0166 | **+3.238** | **0.0012** | ** |
| Time > 180 (%) | +0.0077 | 0.0077 | ±0.0155 | +0.997 | 0.3186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **793**, R² = **0.1480**, Adj R² = **0.1360**, F-statistic = **12.34** (p = **1.20e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4631** | 1.4690 | ±2.9379 | **+7.123** | **1.06e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0438** | 0.3575 | ±0.7150 | **-2.920** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4273** | 0.6130 | ±1.2261 | **+2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.1768 | 0.4705 | ±0.9411 | -0.376 | 0.7070 |  |
| Site: UW (vs UAB) | -0.6786 | 0.4099 | ±0.8197 | -1.656 | 0.0978 | . |
| **Age (years)** | **-0.1134** | 0.0163 | ±0.0326 | **-6.957** | **3.49e-12** | *** |
| **BMI (kg/m2)** | **+0.0602** | 0.0278 | ±0.0556 | **+2.164** | **0.0305** | * |
| Hypertension | +0.3896 | 0.3730 | ±0.7460 | +1.045 | 0.2962 |  |
| High cholesterol | +0.4079 | 0.3616 | ±0.7232 | +1.128 | 0.2592 |  |
| Kidney disease | +0.9143 | 0.5284 | ±1.0568 | +1.730 | 0.0836 | . |
| **Circulatory disease** | **+1.6483** | 0.5086 | ±1.0171 | **+3.241** | **0.0012** | ** |
| Avg. daily time > 180 (%) | +0.0070 | 0.0077 | ±0.0154 | +0.914 | 0.3609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **793**, R² = **0.1495**, Adj R² = **0.1376**, F-statistic = **12.48** (p = **6.36e-22**), Residual SE = **4.796** on **781** df, AIC = **4748.7**, BIC = **4804.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4629** | 1.4688 | ±2.9376 | **+7.123** | **1.05e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0152** | 0.3582 | ±0.7165 | **-2.834** | **0.0046** | ** |
| **Education: high school or below (vs college)** | **+1.4102** | 0.6094 | ±1.2187 | **+2.314** | **0.0207** | * |
| Site: UCSD (vs UAB) | -0.1560 | 0.4688 | ±0.9376 | -0.333 | 0.7393 |  |
| Site: UW (vs UAB) | -0.6754 | 0.4076 | ±0.8151 | -1.657 | 0.0975 | . |
| **Age (years)** | **-0.1123** | 0.0163 | ±0.0327 | **-6.867** | **6.55e-12** | *** |
| **BMI (kg/m2)** | **+0.0567** | 0.0280 | ±0.0560 | **+2.025** | **0.0429** | * |
| Hypertension | +0.3910 | 0.3726 | ±0.7451 | +1.049 | 0.2940 |  |
| High cholesterol | +0.4156 | 0.3611 | ±0.7222 | +1.151 | 0.2498 |  |
| Kidney disease | +0.9155 | 0.5274 | ±1.0547 | +1.736 | 0.0826 | . |
| **Circulatory disease** | **+1.6384** | 0.5086 | ±1.0172 | **+3.222** | **0.0013** | ** |
| Nocturnal time > 180 (%) | +0.0098 | 0.0070 | ±0.0140 | +1.400 | 0.1615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **793**, R² = **0.1475**, Adj R² = **0.1355**, F-statistic = **12.29** (p = **1.49e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4526** | 1.4734 | ±2.9468 | **+7.094** | **1.30e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0374** | 0.3581 | ±0.7162 | **-2.897** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.4501** | 0.6097 | ±1.2193 | **+2.379** | **0.0174** | * |
| Site: UCSD (vs UAB) | -0.1903 | 0.4696 | ±0.9391 | -0.405 | 0.6853 |  |
| Site: UW (vs UAB) | -0.6824 | 0.4109 | ±0.8218 | -1.661 | 0.0968 | . |
| **Age (years)** | **-0.1125** | 0.0163 | ±0.0326 | **-6.900** | **5.21e-12** | *** |
| **BMI (kg/m2)** | **+0.0630** | 0.0276 | ±0.0552 | **+2.280** | **0.0226** | * |
| Hypertension | +0.3856 | 0.3731 | ±0.7462 | +1.034 | 0.3013 |  |
| High cholesterol | +0.4143 | 0.3622 | ±0.7245 | +1.144 | 0.2528 |  |
| Kidney disease | +0.9374 | 0.5232 | ±1.0464 | +1.792 | 0.0732 | . |
| **Circulatory disease** | **+1.6560** | 0.5107 | ±1.0214 | **+3.243** | **0.0012** | ** |
| Time > 250 (%) | +0.0079 | 0.0127 | ±0.0255 | +0.621 | 0.5347 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.64e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4763** | 1.4714 | ±2.9429 | **+7.120** | **1.08e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0412** | 0.3580 | ±0.7160 | **-2.909** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4587** | 0.6099 | ±1.2198 | **+2.392** | **0.0168** | * |
| Site: UCSD (vs UAB) | -0.1945 | 0.4699 | ±0.9398 | -0.414 | 0.6790 |  |
| Site: UW (vs UAB) | -0.6891 | 0.4104 | ±0.8209 | -1.679 | 0.0931 | . |
| **Age (years)** | **-0.1128** | 0.0163 | ±0.0326 | **-6.923** | **4.41e-12** | *** |
| **BMI (kg/m2)** | **+0.0632** | 0.0276 | ±0.0553 | **+2.288** | **0.0221** | * |
| Hypertension | +0.3883 | 0.3731 | ±0.7462 | +1.041 | 0.2980 |  |
| High cholesterol | +0.4136 | 0.3624 | ±0.7249 | +1.141 | 0.2537 |  |
| Kidney disease | +0.9394 | 0.5231 | ±1.0463 | +1.796 | 0.0725 | . |
| **Circulatory disease** | **+1.6590** | 0.5108 | ±1.0217 | **+3.248** | **0.0012** | ** |
| Avg. daily time > 250 (%) | +0.0065 | 0.0129 | ±0.0259 | +0.500 | 0.6172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 793; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0914**, LLR χ² = **74.14** (p = **7.00e-12**), AUC = **0.7072**, AIC = **758.9**, BIC = **810.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1259 | 0.7675 | ±1.5350 | -0.164 | 0.8697 | 0.8817 |  |
| Education: graduate level (vs college) | -0.3009 | 0.2195 | ±0.4390 | -1.371 | 0.1705 | 0.7402 |  |
| Education: high school or below (vs college) | +0.1936 | 0.2529 | ±0.5057 | +0.766 | 0.4439 | 1.2136 |  |
| Site: UCSD (vs UAB) | -0.2245 | 0.2356 | ±0.4712 | -0.953 | 0.3407 | 0.7989 |  |
| Site: UW (vs UAB) | -0.3745 | 0.2252 | ±0.4503 | -1.663 | 0.0963 | 0.6876 | . |
| **Age (years)** | **-0.0424** | 0.0097 | ±0.0194 | **-4.380** | **1.18e-05** | 0.9585 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.842** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2749 | 0.2185 | ±0.4369 | +1.258 | 0.2083 | 1.3164 |  |
| High cholesterol | +0.2062 | 0.2029 | ±0.4058 | +1.016 | 0.3094 | 1.2290 |  |
| Kidney disease | +0.3617 | 0.2411 | ±0.4823 | +1.500 | 0.1336 | 1.4358 |  |
| **Circulatory disease** | **+0.7652** | 0.2246 | ±0.4492 | **+3.407** | **6.56e-04** | 2.1495 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0949**, LLR χ² = **76.97** (p = **5.67e-12**), AUC = **0.7110**, AIC = **758.1**, BIC = **814.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8192 | 0.8730 | ±1.7459 | -0.938 | 0.3481 | 0.4408 |  |
| Education: graduate level (vs college) | -0.2688 | 0.2205 | ±0.4410 | -1.219 | 0.2229 | 0.7643 |  |
| Education: high school or below (vs college) | +0.1328 | 0.2569 | ±0.5139 | +0.517 | 0.6054 | 1.1420 |  |
| Site: UCSD (vs UAB) | -0.2001 | 0.2367 | ±0.4734 | -0.845 | 0.3979 | 0.8186 |  |
| Site: UW (vs UAB) | -0.3367 | 0.2271 | ±0.4542 | -1.483 | 0.1381 | 0.7141 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.289** | **1.79e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0126 | ±0.0252 | **+2.575** | **0.0100** | 1.0330 | * |
| Hypertension | +0.2590 | 0.2192 | ±0.4383 | +1.182 | 0.2374 | 1.2956 |  |
| High cholesterol | +0.1915 | 0.2032 | ±0.4064 | +0.942 | 0.3461 | 1.2110 |  |
| Kidney disease | +0.3705 | 0.2414 | ±0.4829 | +1.535 | 0.1249 | 1.4485 |  |
| **Circulatory disease** | **+0.7477** | 0.2247 | ±0.4494 | **+3.327** | **8.77e-04** | 2.1120 | *** |
| HbA1c (%) | +0.1070 | 0.0628 | ±0.1255 | +1.705 | 0.0882 | 1.1130 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.54** (p = **1.07e-11**), AUC = **0.7101**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5363 | 0.8430 | ±1.6861 | -0.636 | 0.5247 | 0.5849 |  |
| Education: graduate level (vs college) | -0.2842 | 0.2201 | ±0.4402 | -1.291 | 0.1966 | 0.7526 |  |
| Education: high school or below (vs college) | +0.1569 | 0.2553 | ±0.5106 | +0.614 | 0.5390 | 1.1698 |  |
| Site: UCSD (vs UAB) | -0.2036 | 0.2365 | ±0.4731 | -0.861 | 0.3894 | 0.8158 |  |
| Site: UW (vs UAB) | -0.3501 | 0.2264 | ±0.4529 | -1.546 | 0.1221 | 0.7046 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.303** | **1.68e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0336** | 0.0125 | ±0.0251 | **+2.684** | **0.0073** | 1.0342 | ** |
| Hypertension | +0.2653 | 0.2187 | ±0.4374 | +1.213 | 0.2252 | 1.3038 |  |
| High cholesterol | +0.1992 | 0.2030 | ±0.4060 | +0.981 | 0.3264 | 1.2205 |  |
| Kidney disease | +0.3536 | 0.2414 | ±0.4827 | +1.465 | 0.1429 | 1.4242 |  |
| **Circulatory disease** | **+0.7490** | 0.2248 | ±0.4495 | **+3.332** | **8.61e-04** | 2.1148 | *** |
| Mean glucose (mg/dL) | +0.0026 | 0.0021 | ±0.0043 | +1.194 | 0.2324 | 1.0026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.54** (p = **1.07e-11**), AUC = **0.7101**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8902 | 1.0018 | ±2.0036 | -0.889 | 0.3742 | 0.4106 |  |
| Education: graduate level (vs college) | -0.2842 | 0.2201 | ±0.4402 | -1.291 | 0.1966 | 0.7526 |  |
| Education: high school or below (vs college) | +0.1569 | 0.2553 | ±0.5106 | +0.614 | 0.5390 | 1.1698 |  |
| Site: UCSD (vs UAB) | -0.2036 | 0.2365 | ±0.4731 | -0.861 | 0.3894 | 0.8158 |  |
| Site: UW (vs UAB) | -0.3501 | 0.2264 | ±0.4529 | -1.546 | 0.1221 | 0.7046 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.303** | **1.68e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0336** | 0.0125 | ±0.0251 | **+2.684** | **0.0073** | 1.0342 | ** |
| Hypertension | +0.2653 | 0.2187 | ±0.4374 | +1.213 | 0.2252 | 1.3038 |  |
| High cholesterol | +0.1992 | 0.2030 | ±0.4060 | +0.981 | 0.3264 | 1.2205 |  |
| Kidney disease | +0.3536 | 0.2414 | ±0.4827 | +1.465 | 0.1429 | 1.4242 |  |
| **Circulatory disease** | **+0.7490** | 0.2248 | ±0.4495 | **+3.332** | **8.61e-04** | 2.1148 | *** |
| GMI (%) | +0.1069 | 0.0895 | ±0.1791 | +1.194 | 0.2324 | 1.1129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0961**, LLR χ² = **77.93** (p = **3.71e-12**), AUC = **0.7141**, AIC = **757.1**, BIC = **813.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7359 | 0.8313 | ±1.6627 | -0.885 | 0.3761 | 0.4791 |  |
| Education: graduate level (vs college) | -0.2650 | 0.2207 | ±0.4413 | -1.201 | 0.2298 | 0.7672 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2557 | ±0.5114 | +0.552 | 0.5806 | 1.1517 |  |
| Site: UCSD (vs UAB) | -0.1912 | 0.2369 | ±0.4738 | -0.807 | 0.4195 | 0.8259 |  |
| Site: UW (vs UAB) | -0.3485 | 0.2264 | ±0.4527 | -1.539 | 0.1237 | 0.7058 |  |
| **Age (years)** | **-0.0410** | 0.0097 | ±0.0194 | **-4.220** | **2.44e-05** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0319** | 0.0126 | ±0.0252 | **+2.532** | **0.0113** | 1.0324 | * |
| Hypertension | +0.2649 | 0.2190 | ±0.4381 | +1.209 | 0.2266 | 1.3032 |  |
| High cholesterol | +0.1996 | 0.2034 | ±0.4068 | +0.981 | 0.3264 | 1.2209 |  |
| Kidney disease | +0.3657 | 0.2415 | ±0.4830 | +1.514 | 0.1299 | 1.4416 |  |
| **Circulatory disease** | **+0.7431** | 0.2248 | ±0.4495 | **+3.306** | **9.46e-04** | 2.1024 | *** |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0039** | 0.0020 | ±0.0040 | **+1.965** | **0.0494** | 1.0039 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0958**, LLR χ² = **77.71** (p = **4.09e-12**), AUC = **0.7131**, AIC = **757.4**, BIC = **813.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6183 | 0.8124 | ±1.6247 | -0.761 | 0.4466 | 0.5389 |  |
| Education: graduate level (vs college) | -0.2664 | 0.2208 | ±0.4416 | -1.206 | 0.2277 | 0.7662 |  |
| Education: high school or below (vs college) | +0.1458 | 0.2552 | ±0.5103 | +0.572 | 0.5676 | 1.1570 |  |
| Site: UCSD (vs UAB) | -0.2083 | 0.2365 | ±0.4730 | -0.881 | 0.3784 | 0.8119 |  |
| Site: UW (vs UAB) | -0.3214 | 0.2275 | ±0.4550 | -1.413 | 0.1577 | 0.7251 |  |
| **Age (years)** | **-0.0421** | 0.0097 | ±0.0193 | **-4.349** | **1.37e-05** | 0.9588 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0126 | ±0.0251 | **+2.593** | **0.0095** | 1.0331 | ** |
| Hypertension | +0.2568 | 0.2193 | ±0.4386 | +1.171 | 0.2415 | 1.2928 |  |
| High cholesterol | +0.2088 | 0.2032 | ±0.4063 | +1.028 | 0.3040 | 1.2322 |  |
| Kidney disease | +0.2731 | 0.2465 | ±0.4930 | +1.108 | 0.2678 | 1.3141 |  |
| **Circulatory disease** | **+0.7512** | 0.2250 | ±0.4501 | **+3.338** | **8.43e-04** | 2.1195 | *** |
| Glucose SD, pooled (mg/dL) | +0.0143 | 0.0075 | ±0.0150 | +1.898 | 0.0577 | 1.0144 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0930**, LLR χ² = **75.40** (p = **1.14e-11**), AUC = **0.7096**, AIC = **759.7**, BIC = **815.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4310 | 0.8153 | ±1.6306 | -0.529 | 0.5970 | 0.6498 |  |
| Education: graduate level (vs college) | -0.2836 | 0.2202 | ±0.4405 | -1.288 | 0.1978 | 0.7531 |  |
| Education: high school or below (vs college) | +0.1619 | 0.2548 | ±0.5096 | +0.635 | 0.5252 | 1.1757 |  |
| Site: UCSD (vs UAB) | -0.2143 | 0.2360 | ±0.4720 | -0.908 | 0.3639 | 0.8071 |  |
| Site: UW (vs UAB) | -0.3458 | 0.2268 | ±0.4536 | -1.525 | 0.1273 | 0.7076 |  |
| **Age (years)** | **-0.0423** | 0.0097 | ±0.0194 | **-4.373** | **1.23e-05** | 0.9586 | *** |
| **BMI (kg/m2)** | **+0.0341** | 0.0125 | ±0.0250 | **+2.731** | **0.0063** | 1.0347 | ** |
| Hypertension | +0.2672 | 0.2187 | ±0.4374 | +1.222 | 0.2219 | 1.3063 |  |
| High cholesterol | +0.2077 | 0.2029 | ±0.4058 | +1.024 | 0.3060 | 1.2308 |  |
| Kidney disease | +0.3044 | 0.2468 | ±0.4936 | +1.233 | 0.2175 | 1.3558 |  |
| **Circulatory disease** | **+0.7588** | 0.2247 | ±0.4493 | **+3.377** | **7.32e-04** | 2.1357 | *** |
| Avg. daily SD (mg/dL) | +0.0097 | 0.0086 | ±0.0172 | +1.128 | 0.2592 | 1.0098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0918**, LLR χ² = **74.48** (p = **1.70e-11**), AUC = **0.7080**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3433 | 0.8512 | ±1.7025 | -0.403 | 0.6867 | 0.7094 |  |
| Education: graduate level (vs college) | -0.2943 | 0.2199 | ±0.4398 | -1.338 | 0.1807 | 0.7450 |  |
| Education: high school or below (vs college) | +0.1914 | 0.2530 | ±0.5059 | +0.757 | 0.4492 | 1.2110 |  |
| Site: UCSD (vs UAB) | -0.2247 | 0.2357 | ±0.4713 | -0.954 | 0.3403 | 0.7987 |  |
| Site: UW (vs UAB) | -0.3632 | 0.2260 | ±0.4521 | -1.607 | 0.1081 | 0.6955 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.400** | **1.08e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0350** | 0.0124 | ±0.0249 | **+2.813** | **0.0049** | 1.0356 | ** |
| Hypertension | +0.2707 | 0.2187 | ±0.4374 | +1.238 | 0.2159 | 1.3108 |  |
| High cholesterol | +0.2127 | 0.2032 | ±0.4065 | +1.047 | 0.2952 | 1.2371 |  |
| Kidney disease | +0.3286 | 0.2479 | ±0.4957 | +1.326 | 0.1850 | 1.3890 |  |
| **Circulatory disease** | **+0.7671** | 0.2248 | ±0.4496 | **+3.412** | **6.44e-04** | 2.1536 | *** |
| CV (%) | +0.0101 | 0.0171 | ±0.0341 | +0.589 | 0.5557 | 1.0101 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.27** (p = **1.87e-11**), AUC = **0.7073**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0371 | 0.8878 | ±1.7755 | +0.042 | 0.9666 | 1.0378 |  |
| Education: graduate level (vs college) | -0.2970 | 0.2198 | ±0.4396 | -1.351 | 0.1767 | 0.7430 |  |
| Education: high school or below (vs college) | +0.1933 | 0.2529 | ±0.5058 | +0.764 | 0.4446 | 1.2132 |  |
| Site: UCSD (vs UAB) | -0.2260 | 0.2357 | ±0.4713 | -0.959 | 0.3377 | 0.7977 |  |
| Site: UW (vs UAB) | -0.3682 | 0.2259 | ±0.4517 | -1.630 | 0.1031 | 0.6920 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.389** | **1.14e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0249 | **+2.830** | **0.0047** | 1.0358 | ** |
| Hypertension | +0.2733 | 0.2186 | ±0.4371 | +1.251 | 0.2111 | 1.3144 |  |
| High cholesterol | +0.2076 | 0.2029 | ±0.4059 | +1.023 | 0.3063 | 1.2307 |  |
| Kidney disease | +0.3445 | 0.2457 | ±0.4915 | +1.402 | 0.1609 | 1.4113 |  |
| **Circulatory disease** | **+0.7641** | 0.2248 | ±0.4495 | **+3.400** | **6.74e-04** | 2.1471 | *** |
| Mean / SD ratio | -0.0346 | 0.0945 | ±0.1891 | -0.366 | 0.7147 | 0.9660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0918**, LLR χ² = **74.45** (p = **1.73e-11**), AUC = **0.7074**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3541 | 0.8683 | ±1.7367 | -0.408 | 0.6834 | 0.7018 |  |
| Education: graduate level (vs college) | -0.3056 | 0.2196 | ±0.4393 | -1.391 | 0.1641 | 0.7367 |  |
| Education: high school or below (vs college) | +0.1948 | 0.2530 | ±0.5060 | +0.770 | 0.4413 | 1.2151 |  |
| Site: UCSD (vs UAB) | -0.2212 | 0.2357 | ±0.4714 | -0.939 | 0.3479 | 0.8015 |  |
| Site: UW (vs UAB) | -0.3822 | 0.2256 | ±0.4513 | -1.694 | 0.0903 | 0.6824 | . |
| **Age (years)** | **-0.0422** | 0.0097 | ±0.0194 | **-4.355** | **1.33e-05** | 0.9587 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0249 | **+2.838** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2763 | 0.2186 | ±0.4371 | +1.264 | 0.2061 | 1.3183 |  |
| High cholesterol | +0.2030 | 0.2030 | ±0.4061 | +1.000 | 0.3175 | 1.2251 |  |
| Kidney disease | +0.3869 | 0.2453 | ±0.4906 | +1.577 | 0.1147 | 1.4724 |  |
| **Circulatory disease** | **+0.7649** | 0.2245 | ±0.4489 | **+3.408** | **6.54e-04** | 2.1489 | *** |
| Avg. daily mean/SD | +0.0417 | 0.0740 | ±0.1480 | +0.563 | 0.5734 | 1.0425 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0951**, LLR χ² = **77.14** (p = **5.25e-12**), AUC = **0.7093**, AIC = **757.9**, BIC = **814.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9733 | 0.9117 | ±1.8234 | -1.068 | 0.2857 | 0.3778 |  |
| Education: graduate level (vs college) | -0.2684 | 0.2208 | ±0.4415 | -1.216 | 0.2240 | 0.7646 |  |
| Education: high school or below (vs college) | +0.1657 | 0.2548 | ±0.5097 | +0.650 | 0.5155 | 1.1802 |  |
| Site: UCSD (vs UAB) | -0.1999 | 0.2365 | ±0.4730 | -0.846 | 0.3978 | 0.8188 |  |
| Site: UW (vs UAB) | -0.3058 | 0.2291 | ±0.4582 | -1.335 | 0.1820 | 0.7366 |  |
| **Age (years)** | **-0.0410** | 0.0097 | ±0.0195 | **-4.212** | **2.53e-05** | 0.9598 | *** |
| **BMI (kg/m2)** | **+0.0342** | 0.0125 | ±0.0250 | **+2.739** | **0.0062** | 1.0348 | ** |
| Hypertension | +0.2867 | 0.2194 | ±0.4389 | +1.307 | 0.1914 | 1.3320 |  |
| High cholesterol | +0.2280 | 0.2039 | ±0.4078 | +1.118 | 0.2635 | 1.2561 |  |
| Kidney disease | +0.3358 | 0.2422 | ±0.4845 | +1.386 | 0.1657 | 1.3990 |  |
| **Circulatory disease** | **+0.7585** | 0.2252 | ±0.4504 | **+3.368** | **7.57e-04** | 2.1351 | *** |
| MAG (mg/dL/h) | +0.0162 | 0.0093 | ±0.0185 | +1.742 | 0.0815 | 1.0163 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0927**, LLR χ² = **75.19** (p = **1.25e-11**), AUC = **0.7094**, AIC = **759.9**, BIC = **816.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5368 | 0.8667 | ±1.7334 | -0.619 | 0.5357 | 0.5846 |  |
| Education: graduate level (vs college) | -0.2843 | 0.2202 | ±0.4405 | -1.291 | 0.1968 | 0.7525 |  |
| Education: high school or below (vs college) | +0.1636 | 0.2549 | ±0.5098 | +0.642 | 0.5208 | 1.1778 |  |
| Site: UCSD (vs UAB) | -0.2110 | 0.2362 | ±0.4723 | -0.893 | 0.3716 | 0.8098 |  |
| Site: UW (vs UAB) | -0.3472 | 0.2269 | ±0.4538 | -1.530 | 0.1260 | 0.7067 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.338** | **1.44e-05** | 0.9588 | *** |
| **BMI (kg/m2)** | **+0.0345** | 0.0125 | ±0.0249 | **+2.768** | **0.0056** | 1.0351 | ** |
| Hypertension | +0.2758 | 0.2186 | ±0.4372 | +1.262 | 0.2070 | 1.3176 |  |
| High cholesterol | +0.2088 | 0.2030 | ±0.4059 | +1.029 | 0.3036 | 1.2322 |  |
| Kidney disease | +0.3092 | 0.2469 | ±0.4938 | +1.252 | 0.2104 | 1.3623 |  |
| **Circulatory disease** | **+0.7569** | 0.2249 | ±0.4497 | **+3.366** | **7.62e-04** | 2.1317 | *** |
| Avg. daily range (mg/dL) | +0.0026 | 0.0026 | ±0.0051 | +1.031 | 0.3028 | 1.0026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.1064**, LLR χ² = **86.32** (p = **8.74e-14**), AUC = **0.7259**, AIC = **748.7**, BIC = **804.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5956 | 0.7790 | ±1.5580 | -0.765 | 0.4445 | 0.5512 |  |
| Education: graduate level (vs college) | -0.2203 | 0.2226 | ±0.4453 | -0.990 | 0.3223 | 0.8022 |  |
| Education: high school or below (vs college) | +0.1616 | 0.2564 | ±0.5128 | +0.630 | 0.5286 | 1.1754 |  |
| Site: UCSD (vs UAB) | -0.2058 | 0.2386 | ±0.4771 | -0.863 | 0.3883 | 0.8140 |  |
| Site: UW (vs UAB) | -0.2921 | 0.2283 | ±0.4566 | -1.279 | 0.2008 | 0.7467 |  |
| **Age (years)** | **-0.0405** | 0.0097 | ±0.0193 | **-4.197** | **2.71e-05** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0301** | 0.0126 | ±0.0253 | **+2.381** | **0.0172** | 1.0306 | * |
| Hypertension | +0.2259 | 0.2214 | ±0.4429 | +1.020 | 0.3076 | 1.2535 |  |
| High cholesterol | +0.2066 | 0.2048 | ±0.4095 | +1.009 | 0.3130 | 1.2295 |  |
| Kidney disease | +0.3032 | 0.2447 | ±0.4893 | +1.239 | 0.2153 | 1.3542 |  |
| **Circulatory disease** | **+0.7178** | 0.2276 | ±0.4551 | **+3.154** | **0.0016** | 2.0499 | ** |
| **SD of daily means (mg/dL)** | **+0.0371** | 0.0106 | ±0.0212 | **+3.499** | **4.67e-04** | 1.0378 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0932**, LLR χ² = **75.60** (p = **1.04e-11**), AUC = **0.7096**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2048 | 0.8145 | ±1.6289 | +0.251 | 0.8015 | 1.2273 |  |
| Education: graduate level (vs college) | -0.2822 | 0.2202 | ±0.4405 | -1.281 | 0.2000 | 0.7541 |  |
| Education: high school or below (vs college) | +0.1592 | 0.2549 | ±0.5097 | +0.625 | 0.5321 | 1.1726 |  |
| Site: UCSD (vs UAB) | -0.1997 | 0.2368 | ±0.4735 | -0.843 | 0.3990 | 0.8190 |  |
| Site: UW (vs UAB) | -0.3458 | 0.2267 | ±0.4534 | -1.525 | 0.1272 | 0.7077 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.323** | **1.54e-05** | 0.9590 | *** |
| **BMI (kg/m2)** | **+0.0331** | 0.0126 | ±0.0252 | **+2.626** | **0.0086** | 1.0336 | ** |
| Hypertension | +0.2678 | 0.2187 | ±0.4375 | +1.224 | 0.2208 | 1.3071 |  |
| High cholesterol | +0.2027 | 0.2030 | ±0.4060 | +0.999 | 0.3179 | 1.2248 |  |
| Kidney disease | +0.3440 | 0.2417 | ±0.4835 | +1.423 | 0.1548 | 1.4105 |  |
| **Circulatory disease** | **+0.7506** | 0.2248 | ±0.4495 | **+3.340** | **8.39e-04** | 2.1183 | *** |
| Time in range 70-180, pooled (%) | -0.0043 | 0.0035 | ±0.0071 | -1.220 | 0.2226 | 0.9957 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0929**, LLR χ² = **75.39** (p = **1.14e-11**), AUC = **0.7093**, AIC = **759.7**, BIC = **815.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1842 | 0.8159 | ±1.6318 | +0.226 | 0.8214 | 1.2023 |  |
| Education: graduate level (vs college) | -0.2848 | 0.2201 | ±0.4402 | -1.294 | 0.1957 | 0.7522 |  |
| Education: high school or below (vs college) | +0.1608 | 0.2549 | ±0.5099 | +0.631 | 0.5283 | 1.1744 |  |
| Site: UCSD (vs UAB) | -0.2002 | 0.2368 | ±0.4736 | -0.846 | 0.3978 | 0.8185 |  |
| Site: UW (vs UAB) | -0.3476 | 0.2267 | ±0.4534 | -1.533 | 0.1253 | 0.7064 |  |
| **Age (years)** | **-0.0419** | 0.0097 | ±0.0194 | **-4.333** | **1.47e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0332** | 0.0126 | ±0.0252 | **+2.634** | **0.0084** | 1.0337 | ** |
| Hypertension | +0.2689 | 0.2187 | ±0.4374 | +1.230 | 0.2188 | 1.3085 |  |
| High cholesterol | +0.2029 | 0.2030 | ±0.4060 | +1.000 | 0.3174 | 1.2250 |  |
| Kidney disease | +0.3439 | 0.2418 | ±0.4836 | +1.422 | 0.1549 | 1.4105 |  |
| **Circulatory disease** | **+0.7519** | 0.2247 | ±0.4495 | **+3.346** | **8.20e-04** | 2.1211 | *** |
| Avg. daily time in range 70-180 (%) | -0.0040 | 0.0035 | ±0.0070 | -1.126 | 0.2601 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0993**, LLR χ² = **80.52** (p = **1.17e-12**), AUC = **0.7115**, AIC = **754.5**, BIC = **810.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3244 | 0.7729 | ±1.5457 | -0.420 | 0.6747 | 0.7230 |  |
| Education: graduate level (vs college) | -0.2965 | 0.2208 | ±0.4416 | -1.343 | 0.1794 | 0.7434 |  |
| Education: high school or below (vs college) | +0.2206 | 0.2543 | ±0.5085 | +0.868 | 0.3856 | 1.2468 |  |
| Site: UCSD (vs UAB) | -0.1985 | 0.2369 | ±0.4739 | -0.838 | 0.4021 | 0.8199 |  |
| Site: UW (vs UAB) | -0.3463 | 0.2266 | ±0.4532 | -1.528 | 0.1265 | 0.7073 |  |
| **Age (years)** | **-0.0416** | 0.0097 | ±0.0194 | **-4.287** | **1.81e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0351** | 0.0125 | ±0.0250 | **+2.812** | **0.0049** | 1.0357 | ** |
| Hypertension | +0.2391 | 0.2207 | ±0.4414 | +1.084 | 0.2786 | 1.2701 |  |
| High cholesterol | +0.2504 | 0.2049 | ±0.4098 | +1.222 | 0.2217 | 1.2846 |  |
| Kidney disease | +0.3462 | 0.2433 | ±0.4866 | +1.423 | 0.1547 | 1.4137 |  |
| **Circulatory disease** | **+0.7422** | 0.2263 | ±0.4525 | **+3.280** | **0.0010** | 2.1005 | ** |
| **Any reading < 54 during wear (0/1)** | **+0.5266** | 0.2056 | ±0.4112 | **+2.561** | **0.0104** | 1.6931 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0914**, LLR χ² = **74.17** (p = **1.96e-11**), AUC = **0.7070**, AIC = **760.9**, BIC = **817.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1313 | 0.7682 | ±1.5364 | -0.171 | 0.8642 | 0.8769 |  |
| Education: graduate level (vs college) | -0.2990 | 0.2198 | ±0.4396 | -1.360 | 0.1737 | 0.7416 |  |
| Education: high school or below (vs college) | +0.1961 | 0.2533 | ±0.5066 | +0.774 | 0.4388 | 1.2166 |  |
| Site: UCSD (vs UAB) | -0.2219 | 0.2361 | ±0.4721 | -0.940 | 0.3471 | 0.8010 |  |
| Site: UW (vs UAB) | -0.3713 | 0.2259 | ±0.4519 | -1.643 | 0.1003 | 0.6899 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.383** | **1.17e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0354** | 0.0124 | ±0.0249 | **+2.846** | **0.0044** | 1.0360 | ** |
| Hypertension | +0.2742 | 0.2185 | ±0.4370 | +1.255 | 0.2095 | 1.3155 |  |
| High cholesterol | +0.2093 | 0.2036 | ±0.4073 | +1.028 | 0.3041 | 1.2328 |  |
| Kidney disease | +0.3620 | 0.2412 | ±0.4824 | +1.501 | 0.1334 | 1.4361 |  |
| **Circulatory disease** | **+0.7672** | 0.2249 | ±0.4498 | **+3.412** | **6.46e-04** | 2.1538 | *** |
| Time < 54 (%) | +0.0345 | 0.1860 | ±0.3721 | +0.186 | 0.8527 | 1.0352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.28** (p = **1.87e-11**), AUC = **0.7066**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1355 | 0.7682 | ±1.5364 | -0.176 | 0.8600 | 0.8733 |  |
| Education: graduate level (vs college) | -0.2974 | 0.2198 | ±0.4395 | -1.353 | 0.1761 | 0.7428 |  |
| Education: high school or below (vs college) | +0.1992 | 0.2534 | ±0.5067 | +0.786 | 0.4316 | 1.2205 |  |
| Site: UCSD (vs UAB) | -0.2189 | 0.2361 | ±0.4723 | -0.927 | 0.3539 | 0.8034 |  |
| Site: UW (vs UAB) | -0.3670 | 0.2262 | ±0.4523 | -1.623 | 0.1047 | 0.6928 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.388** | **1.15e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.844** | **0.0045** | 1.0360 | ** |
| Hypertension | +0.2729 | 0.2186 | ±0.4372 | +1.249 | 0.2118 | 1.3138 |  |
| High cholesterol | +0.2135 | 0.2039 | ±0.4079 | +1.047 | 0.2952 | 1.2380 |  |
| Kidney disease | +0.3610 | 0.2412 | ±0.4824 | +1.497 | 0.1344 | 1.4348 |  |
| **Circulatory disease** | **+0.7688** | 0.2248 | ±0.4496 | **+3.419** | **6.28e-04** | 2.1571 | *** |
| Avg. daily time < 54 (%) | +0.0712 | 0.1834 | ±0.3667 | +0.388 | 0.6979 | 1.0738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.32** (p = **1.83e-11**), AUC = **0.7075**, AIC = **760.7**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1384 | 0.7683 | ±1.5366 | -0.180 | 0.8571 | 0.8708 |  |
| Education: graduate level (vs college) | -0.2967 | 0.2198 | ±0.4396 | -1.350 | 0.1771 | 0.7433 |  |
| Education: high school or below (vs college) | +0.1973 | 0.2531 | ±0.5062 | +0.779 | 0.4357 | 1.2181 |  |
| Site: UCSD (vs UAB) | -0.2174 | 0.2362 | ±0.4724 | -0.920 | 0.3574 | 0.8046 |  |
| Site: UW (vs UAB) | -0.3670 | 0.2260 | ±0.4520 | -1.624 | 0.1044 | 0.6928 |  |
| **Age (years)** | **-0.0426** | 0.0097 | ±0.0194 | **-4.392** | **1.12e-05** | 0.9583 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.839** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2715 | 0.2187 | ±0.4373 | +1.242 | 0.2143 | 1.3119 |  |
| High cholesterol | +0.2158 | 0.2042 | ±0.4084 | +1.057 | 0.2906 | 1.2409 |  |
| Kidney disease | +0.3572 | 0.2414 | ±0.4829 | +1.479 | 0.1390 | 1.4293 |  |
| **Circulatory disease** | **+0.7710** | 0.2250 | ±0.4501 | **+3.426** | **6.12e-04** | 2.1620 | *** |
| Time 54-69, pooled (%) | +0.0357 | 0.0824 | ±0.1648 | +0.434 | 0.6646 | 1.0364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0919**, LLR χ² = **74.54** (p = **1.66e-11**), AUC = **0.7080**, AIC = **760.5**, BIC = **816.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1406 | 0.7683 | ±1.5365 | -0.183 | 0.8548 | 0.8688 |  |
| Education: graduate level (vs college) | -0.2932 | 0.2200 | ±0.4400 | -1.333 | 0.1826 | 0.7459 |  |
| Education: high school or below (vs college) | +0.2007 | 0.2533 | ±0.5066 | +0.793 | 0.4281 | 1.2223 |  |
| Site: UCSD (vs UAB) | -0.2136 | 0.2363 | ±0.4726 | -0.904 | 0.3661 | 0.8077 |  |
| Site: UW (vs UAB) | -0.3610 | 0.2264 | ±0.4528 | -1.595 | 0.1108 | 0.6970 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.402** | **1.07e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0249 | **+2.831** | **0.0046** | 1.0358 | ** |
| Hypertension | +0.2697 | 0.2187 | ±0.4374 | +1.233 | 0.2175 | 1.3096 |  |
| High cholesterol | +0.2217 | 0.2045 | ±0.4090 | +1.084 | 0.2783 | 1.2482 |  |
| Kidney disease | +0.3558 | 0.2414 | ±0.4828 | +1.474 | 0.1406 | 1.4273 |  |
| **Circulatory disease** | **+0.7749** | 0.2251 | ±0.4503 | **+3.442** | **5.78e-04** | 2.1703 | *** |
| Avg. daily time 54-69 (%) | +0.0500 | 0.0766 | ±0.1531 | +0.653 | 0.5137 | 1.0513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.29** (p = **1.85e-11**), AUC = **0.7073**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1392 | 0.7685 | ±1.5369 | -0.181 | 0.8563 | 0.8701 |  |
| Education: graduate level (vs college) | -0.2964 | 0.2199 | ±0.4398 | -1.348 | 0.1777 | 0.7435 |  |
| Education: high school or below (vs college) | +0.1982 | 0.2532 | ±0.5065 | +0.783 | 0.4338 | 1.2192 |  |
| Site: UCSD (vs UAB) | -0.2174 | 0.2363 | ±0.4727 | -0.920 | 0.3577 | 0.8046 |  |
| Site: UW (vs UAB) | -0.3665 | 0.2262 | ±0.4524 | -1.620 | 0.1052 | 0.6932 |  |
| **Age (years)** | **-0.0426** | 0.0097 | ±0.0194 | **-4.392** | **1.12e-05** | 0.9583 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.844** | **0.0045** | 1.0360 | ** |
| Hypertension | +0.2719 | 0.2186 | ±0.4373 | +1.244 | 0.2136 | 1.3125 |  |
| High cholesterol | +0.2156 | 0.2044 | ±0.4087 | +1.055 | 0.2914 | 1.2406 |  |
| Kidney disease | +0.3586 | 0.2413 | ±0.4827 | +1.486 | 0.1373 | 1.4313 |  |
| **Circulatory disease** | **+0.7710** | 0.2251 | ±0.4502 | **+3.425** | **6.15e-04** | 2.1619 | *** |
| Time < 70 (%) | +0.0262 | 0.0649 | ±0.1297 | +0.404 | 0.6862 | 1.0266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0919**, LLR χ² = **74.51** (p = **1.69e-11**), AUC = **0.7074**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1416 | 0.7684 | ±1.5367 | -0.184 | 0.8538 | 0.8680 |  |
| Education: graduate level (vs college) | -0.2935 | 0.2200 | ±0.4400 | -1.334 | 0.1822 | 0.7457 |  |
| Education: high school or below (vs college) | +0.2018 | 0.2534 | ±0.5068 | +0.796 | 0.4259 | 1.2236 |  |
| Site: UCSD (vs UAB) | -0.2136 | 0.2364 | ±0.4728 | -0.904 | 0.3661 | 0.8077 |  |
| Site: UW (vs UAB) | -0.3607 | 0.2265 | ±0.4531 | -1.592 | 0.1113 | 0.6972 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.400** | **1.08e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0248 | **+2.835** | **0.0046** | 1.0358 | ** |
| Hypertension | +0.2700 | 0.2187 | ±0.4374 | +1.235 | 0.2169 | 1.3100 |  |
| High cholesterol | +0.2214 | 0.2046 | ±0.4092 | +1.082 | 0.2793 | 1.2478 |  |
| Kidney disease | +0.3570 | 0.2414 | ±0.4827 | +1.479 | 0.1391 | 1.4290 |  |
| **Circulatory disease** | **+0.7741** | 0.2251 | ±0.4502 | **+3.439** | **5.84e-04** | 2.1687 | *** |
| Avg. daily time < 70 (%) | +0.0368 | 0.0591 | ±0.1182 | +0.623 | 0.5332 | 1.0375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0920**, LLR χ² = **74.64** (p = **1.59e-11**), AUC = **0.7086**, AIC = **760.4**, BIC = **816.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1660 | 0.8700 | ±1.7400 | +0.191 | 0.8487 | 1.1806 |  |
| Education: graduate level (vs college) | -0.2883 | 0.2203 | ±0.4405 | -1.309 | 0.1906 | 0.7495 |  |
| Education: high school or below (vs college) | +0.1734 | 0.2548 | ±0.5097 | +0.680 | 0.4962 | 1.1894 |  |
| Site: UCSD (vs UAB) | -0.2109 | 0.2365 | ±0.4729 | -0.892 | 0.3725 | 0.8099 |  |
| Site: UW (vs UAB) | -0.3574 | 0.2266 | ±0.4533 | -1.577 | 0.1148 | 0.6995 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.302** | **1.70e-05** | 0.9591 | *** |
| **BMI (kg/m2)** | **+0.0347** | 0.0125 | ±0.0249 | **+2.788** | **0.0053** | 1.0354 | ** |
| Hypertension | +0.2676 | 0.2187 | ±0.4374 | +1.224 | 0.2210 | 1.3069 |  |
| High cholesterol | +0.2066 | 0.2028 | ±0.4057 | +1.019 | 0.3084 | 1.2295 |  |
| Kidney disease | +0.3568 | 0.2413 | ±0.4826 | +1.479 | 0.1392 | 1.4288 |  |
| **Circulatory disease** | **+0.7584** | 0.2245 | ±0.4491 | **+3.377** | **7.32e-04** | 2.1348 | *** |
| Time 54-250, pooled (%) | -0.0035 | 0.0049 | ±0.0098 | -0.712 | 0.4766 | 0.9965 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0917**, LLR χ² = **74.40** (p = **1.76e-11**), AUC = **0.7080**, AIC = **760.7**, BIC = **816.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0955 | 0.8779 | ±1.7559 | +0.109 | 0.9133 | 1.1002 |  |
| Education: graduate level (vs college) | -0.2919 | 0.2202 | ±0.4404 | -1.326 | 0.1850 | 0.7468 |  |
| Education: high school or below (vs college) | +0.1787 | 0.2548 | ±0.5095 | +0.701 | 0.4830 | 1.1957 |  |
| Site: UCSD (vs UAB) | -0.2143 | 0.2365 | ±0.4729 | -0.906 | 0.3648 | 0.8071 |  |
| Site: UW (vs UAB) | -0.3623 | 0.2265 | ±0.4530 | -1.600 | 0.1097 | 0.6961 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.326** | **1.52e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0349** | 0.0125 | ±0.0249 | **+2.799** | **0.0051** | 1.0355 | ** |
| Hypertension | +0.2700 | 0.2187 | ±0.4373 | +1.235 | 0.2169 | 1.3100 |  |
| High cholesterol | +0.2066 | 0.2028 | ±0.4057 | +1.018 | 0.3085 | 1.2295 |  |
| Kidney disease | +0.3574 | 0.2413 | ±0.4827 | +1.481 | 0.1386 | 1.4296 |  |
| **Circulatory disease** | **+0.7599** | 0.2246 | ±0.4492 | **+3.383** | **7.17e-04** | 2.1381 | *** |
| Avg. daily time 54-250 (%) | -0.0026 | 0.0050 | ±0.0100 | -0.519 | 0.6038 | 0.9974 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0932**, LLR χ² = **75.61** (p = **1.03e-11**), AUC = **0.7094**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1767 | 0.7685 | ±1.5370 | -0.230 | 0.8182 | 0.8381 |  |
| Education: graduate level (vs college) | -0.2963 | 0.2198 | ±0.4396 | -1.348 | 0.1776 | 0.7435 |  |
| Education: high school or below (vs college) | +0.1756 | 0.2532 | ±0.5065 | +0.693 | 0.4881 | 1.1919 |  |
| Site: UCSD (vs UAB) | -0.2113 | 0.2362 | ±0.4723 | -0.895 | 0.3709 | 0.8095 |  |
| Site: UW (vs UAB) | -0.3628 | 0.2256 | ±0.4511 | -1.609 | 0.1077 | 0.6957 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0193 | **-4.417** | **9.99e-06** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0127 | ±0.0253 | **+2.570** | **0.0102** | 1.0331 | * |
| Hypertension | +0.2793 | 0.2189 | ±0.4377 | +1.276 | 0.2019 | 1.3223 |  |
| High cholesterol | +0.1968 | 0.2033 | ±0.4066 | +0.968 | 0.3330 | 1.2175 |  |
| Kidney disease | +0.3418 | 0.2418 | ±0.4836 | +1.414 | 0.1575 | 1.4075 |  |
| **Circulatory disease** | **+0.7533** | 0.2251 | ±0.4502 | **+3.347** | **8.18e-04** | 2.1240 | *** |
| Time 181-250, pooled (%) | +0.0077 | 0.0063 | ±0.0126 | +1.222 | 0.2217 | 1.0077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0934**, LLR χ² = **75.75** (p = **9.74e-12**), AUC = **0.7097**, AIC = **759.3**, BIC = **815.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1798 | 0.7687 | ±1.5374 | -0.234 | 0.8150 | 0.8354 |  |
| Education: graduate level (vs college) | -0.2977 | 0.2198 | ±0.4396 | -1.354 | 0.1756 | 0.7425 |  |
| Education: high school or below (vs college) | +0.1723 | 0.2534 | ±0.5068 | +0.680 | 0.4965 | 1.1881 |  |
| Site: UCSD (vs UAB) | -0.2086 | 0.2363 | ±0.4725 | -0.883 | 0.3772 | 0.8117 |  |
| Site: UW (vs UAB) | -0.3605 | 0.2257 | ±0.4513 | -1.598 | 0.1101 | 0.6973 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0193 | **-4.413** | **1.02e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0127 | ±0.0253 | **+2.556** | **0.0106** | 1.0329 | * |
| Hypertension | +0.2792 | 0.2189 | ±0.4377 | +1.276 | 0.2020 | 1.3221 |  |
| High cholesterol | +0.1961 | 0.2033 | ±0.4067 | +0.964 | 0.3349 | 1.2166 |  |
| Kidney disease | +0.3404 | 0.2419 | ±0.4837 | +1.408 | 0.1592 | 1.4056 |  |
| **Circulatory disease** | **+0.7540** | 0.2250 | ±0.4501 | **+3.350** | **8.07e-04** | 2.1254 | *** |
| Avg. daily time 181-250 (%) | +0.0079 | 0.0062 | ±0.0123 | +1.278 | 0.2014 | 1.0079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.53** (p = **1.07e-11**), AUC = **0.7095**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2203 | 0.7724 | ±1.5447 | -0.285 | 0.7754 | 0.8023 |  |
| Education: graduate level (vs college) | -0.2835 | 0.2202 | ±0.4403 | -1.288 | 0.1979 | 0.7532 |  |
| Education: high school or below (vs college) | +0.1597 | 0.2549 | ±0.5097 | +0.627 | 0.5310 | 1.1731 |  |
| Site: UCSD (vs UAB) | -0.2015 | 0.2367 | ±0.4733 | -0.851 | 0.3945 | 0.8175 |  |
| Site: UW (vs UAB) | -0.3479 | 0.2266 | ±0.4532 | -1.535 | 0.1247 | 0.7062 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.322** | **1.54e-05** | 0.9590 | *** |
| **BMI (kg/m2)** | **+0.0331** | 0.0126 | ±0.0252 | **+2.632** | **0.0085** | 1.0337 | ** |
| Hypertension | +0.2685 | 0.2187 | ±0.4374 | +1.228 | 0.2195 | 1.3080 |  |
| High cholesterol | +0.2015 | 0.2030 | ±0.4060 | +0.992 | 0.3210 | 1.2232 |  |
| Kidney disease | +0.3450 | 0.2417 | ±0.4834 | +1.428 | 0.1534 | 1.4120 |  |
| **Circulatory disease** | **+0.7502** | 0.2248 | ±0.4496 | **+3.337** | **8.46e-04** | 2.1174 | *** |
| Time > 180 (%) | +0.0042 | 0.0035 | ±0.0070 | +1.189 | 0.2343 | 1.0042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0928**, LLR χ² = **75.30** (p = **1.19e-11**), AUC = **0.7091**, AIC = **759.8**, BIC = **815.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2063 | 0.7717 | ±1.5435 | -0.267 | 0.7892 | 0.8136 |  |
| Education: graduate level (vs college) | -0.2862 | 0.2201 | ±0.4401 | -1.301 | 0.1934 | 0.7511 |  |
| Education: high school or below (vs college) | +0.1615 | 0.2550 | ±0.5099 | +0.633 | 0.5265 | 1.1752 |  |
| Site: UCSD (vs UAB) | -0.2023 | 0.2367 | ±0.4734 | -0.855 | 0.3928 | 0.8168 |  |
| Site: UW (vs UAB) | -0.3500 | 0.2266 | ±0.4531 | -1.545 | 0.1224 | 0.7047 |  |
| **Age (years)** | **-0.0419** | 0.0097 | ±0.0194 | **-4.333** | **1.47e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0333** | 0.0126 | ±0.0252 | **+2.643** | **0.0082** | 1.0338 | ** |
| Hypertension | +0.2697 | 0.2187 | ±0.4373 | +1.233 | 0.2174 | 1.3096 |  |
| High cholesterol | +0.2017 | 0.2030 | ±0.4060 | +0.993 | 0.3205 | 1.2234 |  |
| Kidney disease | +0.3452 | 0.2417 | ±0.4835 | +1.428 | 0.1533 | 1.4123 |  |
| **Circulatory disease** | **+0.7516** | 0.2248 | ±0.4496 | **+3.344** | **8.26e-04** | 2.1205 | *** |
| Avg. daily time > 180 (%) | +0.0038 | 0.0035 | ±0.0070 | +1.084 | 0.2786 | 1.0038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0962**, LLR χ² = **78.00** (p = **3.59e-12**), AUC = **0.7141**, AIC = **757.1**, BIC = **813.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2333 | 0.7709 | ±1.5418 | -0.303 | 0.7621 | 0.7919 |  |
| Education: graduate level (vs college) | -0.2579 | 0.2211 | ±0.4422 | -1.166 | 0.2435 | 0.7727 |  |
| Education: high school or below (vs college) | +0.1502 | 0.2549 | ±0.5098 | +0.589 | 0.5557 | 1.1621 |  |
| Site: UCSD (vs UAB) | -0.1808 | 0.2374 | ±0.4748 | -0.762 | 0.4462 | 0.8346 |  |
| Site: UW (vs UAB) | -0.3417 | 0.2266 | ±0.4533 | -1.508 | 0.1316 | 0.7105 |  |
| **Age (years)** | **-0.0412** | 0.0097 | ±0.0194 | **-4.258** | **2.06e-05** | 0.9596 | *** |
| **BMI (kg/m2)** | **+0.0309** | 0.0127 | ±0.0254 | **+2.440** | **0.0147** | 1.0314 | * |
| Hypertension | +0.2690 | 0.2192 | ±0.4383 | +1.227 | 0.2197 | 1.3087 |  |
| High cholesterol | +0.2070 | 0.2034 | ±0.4069 | +1.017 | 0.3090 | 1.2300 |  |
| Kidney disease | +0.3496 | 0.2417 | ±0.4833 | +1.447 | 0.1480 | 1.4185 |  |
| **Circulatory disease** | **+0.7446** | 0.2249 | ±0.4499 | **+3.311** | **9.31e-04** | 2.1057 | *** |
| **Nocturnal time > 180 (%)** | **+0.0062** | 0.0031 | ±0.0062 | **+1.988** | **0.0468** | 1.0062 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0920**, LLR χ² = **74.63** (p = **1.60e-11**), AUC = **0.7087**, AIC = **760.4**, BIC = **816.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1808 | 0.7723 | ±1.5445 | -0.234 | 0.8149 | 0.8346 |  |
| Education: graduate level (vs college) | -0.2886 | 0.2202 | ±0.4405 | -1.310 | 0.1901 | 0.7493 |  |
| Education: high school or below (vs college) | +0.1733 | 0.2549 | ±0.5098 | +0.680 | 0.4965 | 1.1892 |  |
| Site: UCSD (vs UAB) | -0.2112 | 0.2364 | ±0.4728 | -0.893 | 0.3717 | 0.8096 |  |
| Site: UW (vs UAB) | -0.3579 | 0.2266 | ±0.4532 | -1.579 | 0.1143 | 0.6992 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.301** | **1.70e-05** | 0.9591 | *** |
| **BMI (kg/m2)** | **+0.0347** | 0.0125 | ±0.0249 | **+2.788** | **0.0053** | 1.0354 | ** |
| Hypertension | +0.2678 | 0.2187 | ±0.4374 | +1.224 | 0.2208 | 1.3070 |  |
| High cholesterol | +0.2063 | 0.2028 | ±0.4057 | +1.017 | 0.3090 | 1.2292 |  |
| Kidney disease | +0.3568 | 0.2413 | ±0.4826 | +1.479 | 0.1392 | 1.4288 |  |
| **Circulatory disease** | **+0.7582** | 0.2246 | ±0.4491 | **+3.376** | **7.34e-04** | 2.1345 | *** |
| Time > 250 (%) | +0.0035 | 0.0049 | ±0.0098 | +0.707 | 0.4795 | 1.0035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0917**, LLR χ² = **74.39** (p = **1.77e-11**), AUC = **0.7081**, AIC = **760.7**, BIC = **816.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1617 | 0.7712 | ±1.5425 | -0.210 | 0.8339 | 0.8507 |  |
| Education: graduate level (vs college) | -0.2922 | 0.2202 | ±0.4404 | -1.327 | 0.1845 | 0.7466 |  |
| Education: high school or below (vs college) | +0.1788 | 0.2548 | ±0.5096 | +0.702 | 0.4829 | 1.1958 |  |
| Site: UCSD (vs UAB) | -0.2147 | 0.2364 | ±0.4728 | -0.908 | 0.3639 | 0.8068 |  |
| Site: UW (vs UAB) | -0.3628 | 0.2265 | ±0.4529 | -1.602 | 0.1091 | 0.6957 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.327** | **1.51e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0349** | 0.0125 | ±0.0249 | **+2.800** | **0.0051** | 1.0355 | ** |
| Hypertension | +0.2702 | 0.2186 | ±0.4373 | +1.236 | 0.2166 | 1.3102 |  |
| High cholesterol | +0.2063 | 0.2028 | ±0.4057 | +1.017 | 0.3090 | 1.2292 |  |
| Kidney disease | +0.3575 | 0.2413 | ±0.4827 | +1.481 | 0.1385 | 1.4297 |  |
| **Circulatory disease** | **+0.7599** | 0.2246 | ±0.4493 | **+3.383** | **7.17e-04** | 2.1381 | *** |
| Avg. daily time > 250 (%) | +0.0025 | 0.0050 | ±0.0100 | +0.509 | 0.6106 | 1.0025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 60 single-predictor tests; 5 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 60 tests (samples with n >= 500), of which **2** are significant at BH q < 0.05 in the all-tests family and 1 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 793): best single predictor out of sample is **SD of daily means** (CV R² 0.115 vs 0.105 for covariates alone, gain +0.010; +0.552 per SD, p = 0.003, q = 0.034). FDR-robust associations (1): SD of daily means (higher outcome, +0.552 per SD, q = 0.034).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 793): best single predictor out of sample is **SD of daily means** (CV AUC 0.704 vs 0.685 for covariates alone, gain +0.019; OR 1.36 per SD, p = 4.7e-04, q = 0.007). FDR-robust associations (1): SD of daily means (higher outcome, OR 1.36 per SD, q = 0.007).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.019, via SD of daily means); CES-D-10 depressive symptoms (0-30) (+0.010, via SD of daily means). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (2 FDR-significant / 2 raw-significant of 16); CGM level (0 FDR-significant / 1 raw-significant of 6); Band < 54 (0 FDR-significant / 1 raw-significant of 6).
Level metrics: 0 FDR-significant (1 raw); variability metrics: 2 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (SD of daily means, ΔAIC -7.6); Clinically relevant depressive symptoms (SD of daily means, ΔAIC -9.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
