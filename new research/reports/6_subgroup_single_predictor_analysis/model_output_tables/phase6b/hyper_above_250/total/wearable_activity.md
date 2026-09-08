# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Total analysis base - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 690; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1535**, F-statistic = **13.49** (p = **8.56e-22**), Residual SE = **4604.077** on **679** df, AIC = **13608.9**, BIC = **13658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21543.0182** | 1500.7933 | ±3001.5866 | **+14.354** | **1.00e-46** | *** |
| Education: graduate level (vs college) | -47.3197 | 379.6187 | ±759.2373 | -0.125 | 0.9008 |  |
| Education: high school or below (vs college) | +1058.8636 | 632.8681 | ±1265.7361 | +1.673 | 0.0943 | . |
| Site: UCSD (vs UAB) | +664.8012 | 487.0980 | ±974.1960 | +1.365 | 0.1723 |  |
| Site: UW (vs UAB) | +15.2514 | 425.2723 | ±850.5446 | +0.036 | 0.9714 |  |
| **Age (years)** | **-160.2026** | 16.4631 | ±32.9261 | **-9.731** | **2.22e-22** | *** |
| BMI (kg/m2) | -48.4338 | 29.0686 | ±58.1372 | -1.666 | 0.0957 | . |
| Hypertension | -269.6488 | 389.9338 | ±779.8676 | -0.692 | 0.4892 |  |
| High cholesterol | +299.9184 | 379.0434 | ±758.0868 | +0.791 | 0.4288 |  |
| **Kidney disease** | **-1290.2472** | 467.0888 | ±934.1775 | **-2.762** | **0.0057** | ** |
| **Circulatory disease** | **-1425.6425** | 440.6012 | ±881.2023 | **-3.236** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **690**, R² = **0.1707**, Adj R² = **0.1573**, F-statistic = **12.69** (p = **4.98e-22**), Residual SE = **4593.856** on **678** df, AIC = **13606.8**, BIC = **13661.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20000.5328** | 1672.3985 | ±3344.7970 | **+11.959** | **5.81e-33** | *** |
| Education: graduate level (vs college) | +17.1653 | 384.1704 | ±768.3408 | +0.045 | 0.9644 |  |
| Education: high school or below (vs college) | +933.9534 | 631.2671 | ±1262.5342 | +1.479 | 0.1390 |  |
| Site: UCSD (vs UAB) | +694.0932 | 486.6987 | ±973.3975 | +1.426 | 0.1538 |  |
| Site: UW (vs UAB) | +83.8873 | 422.6922 | ±845.3843 | +0.198 | 0.8427 |  |
| **Age (years)** | **-159.9177** | 16.3840 | ±32.7680 | **-9.761** | **1.66e-22** | *** |
| **BMI (kg/m2)** | **-58.5668** | 29.6548 | ±59.3096 | **-1.975** | **0.0483** | * |
| Hypertension | -313.4526 | 391.6305 | ±783.2609 | -0.800 | 0.4235 |  |
| High cholesterol | +283.7085 | 379.0696 | ±758.1393 | +0.748 | 0.4542 |  |
| **Kidney disease** | **-1275.4091** | 466.6248 | ±933.2496 | **-2.733** | **0.0063** | ** |
| **Circulatory disease** | **-1457.7345** | 442.0612 | ±884.1224 | **-3.298** | **9.75e-04** | *** |
| HbA1c (%) | +270.4922 | 154.9667 | ±309.9334 | +1.745 | 0.0809 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.29e-21**), Residual SE = **4604.936** on **678** df, AIC = **13610.2**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21006.2131** | 1588.2194 | ±3176.4389 | **+13.226** | **6.19e-40** | *** |
| Education: graduate level (vs college) | -31.6708 | 383.0422 | ±766.0844 | -0.083 | 0.9341 |  |
| Education: high school or below (vs college) | +1007.9318 | 628.3307 | ±1256.6614 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +685.1824 | 485.4473 | ±970.8946 | +1.411 | 0.1581 |  |
| Site: UW (vs UAB) | +41.6325 | 423.5810 | ±847.1620 | +0.098 | 0.9217 |  |
| **Age (years)** | **-159.8568** | 16.4221 | ±32.8442 | **-9.734** | **2.15e-22** | *** |
| BMI (kg/m2) | -52.3256 | 29.4520 | ±58.9040 | -1.777 | 0.0756 | . |
| Hypertension | -282.3796 | 391.4612 | ±782.9224 | -0.721 | 0.4707 |  |
| High cholesterol | +301.8208 | 379.8386 | ±759.6771 | +0.795 | 0.4268 |  |
| **Kidney disease** | **-1309.3741** | 470.8464 | ±941.6928 | **-2.781** | **0.0054** | ** |
| **Circulatory disease** | **-1456.2670** | 443.8650 | ±887.7300 | **-3.281** | **0.0010** | ** |
| Mean glucose (mg/dL) | +3.9347 | 5.2623 | ±10.5246 | +0.748 | 0.4546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.29e-21**), Residual SE = **4604.936** on **678** df, AIC = **13610.2**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20461.7339** | 1960.4944 | ±3920.9888 | **+10.437** | **1.68e-25** | *** |
| Education: graduate level (vs college) | -31.6708 | 383.0422 | ±766.0844 | -0.083 | 0.9341 |  |
| Education: high school or below (vs college) | +1007.9318 | 628.3307 | ±1256.6614 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +685.1824 | 485.4473 | ±970.8946 | +1.411 | 0.1581 |  |
| Site: UW (vs UAB) | +41.6325 | 423.5810 | ±847.1620 | +0.098 | 0.9217 |  |
| **Age (years)** | **-159.8568** | 16.4221 | ±32.8442 | **-9.734** | **2.15e-22** | *** |
| BMI (kg/m2) | -52.3256 | 29.4520 | ±58.9040 | -1.777 | 0.0756 | . |
| Hypertension | -282.3796 | 391.4612 | ±782.9224 | -0.721 | 0.4707 |  |
| High cholesterol | +301.8208 | 379.8386 | ±759.6771 | +0.795 | 0.4268 |  |
| **Kidney disease** | **-1309.3741** | 470.8464 | ±941.6928 | **-2.781** | **0.0054** | ** |
| **Circulatory disease** | **-1456.2670** | 443.8650 | ±887.7300 | **-3.281** | **0.0010** | ** |
| GMI (%) | +164.4952 | 219.9950 | ±439.9900 | +0.748 | 0.4546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **690**, R² = **0.1684**, Adj R² = **0.1549**, F-statistic = **12.48** (p = **1.21e-21**), Residual SE = **4600.289** on **678** df, AIC = **13608.8**, BIC = **13663.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20721.6256** | 1582.4176 | ±3164.8353 | **+13.095** | **3.52e-39** | *** |
| Education: graduate level (vs college) | -13.7794 | 384.1674 | ±768.3347 | -0.036 | 0.9714 |  |
| Education: high school or below (vs college) | +978.9994 | 626.6794 | ±1253.3588 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +695.4477 | 484.7585 | ±969.5169 | +1.435 | 0.1514 |  |
| Site: UW (vs UAB) | +45.1378 | 423.1643 | ±846.3287 | +0.107 | 0.9151 |  |
| **Age (years)** | **-158.7886** | 16.3715 | ±32.7431 | **-9.699** | **3.04e-22** | *** |
| BMI (kg/m2) | -56.4472 | 29.5854 | ±59.1708 | -1.908 | 0.0564 | . |
| Hypertension | -287.1270 | 391.4074 | ±782.8148 | -0.734 | 0.4632 |  |
| High cholesterol | +309.3549 | 379.7470 | ±759.4940 | +0.815 | 0.4153 |  |
| **Kidney disease** | **-1293.0693** | 469.3785 | ±938.7569 | **-2.755** | **0.0059** | ** |
| **Circulatory disease** | **-1475.4615** | 443.6421 | ±887.2843 | **-3.326** | **8.82e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +6.2791 | 5.1316 | ±10.2632 | +1.224 | 0.2211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1659**, Adj R² = **0.1524**, F-statistic = **12.26** (p = **3.10e-21**), Residual SE = **4607.124** on **678** df, AIC = **13610.8**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21394.7271** | 1522.1778 | ±3044.3555 | **+14.055** | **7.14e-45** | *** |
| Education: graduate level (vs college) | -38.8706 | 385.5182 | ±771.0364 | -0.101 | 0.9197 |  |
| Education: high school or below (vs college) | +1042.2130 | 630.1985 | ±1260.3970 | +1.654 | 0.0982 | . |
| Site: UCSD (vs UAB) | +676.3856 | 482.6809 | ±965.3618 | +1.401 | 0.1611 |  |
| Site: UW (vs UAB) | +34.7989 | 421.7594 | ±843.5188 | +0.083 | 0.9342 |  |
| **Age (years)** | **-160.3468** | 16.5758 | ±33.1517 | **-9.674** | **3.91e-22** | *** |
| BMI (kg/m2) | -49.4899 | 29.4272 | ±58.8544 | -1.682 | 0.0926 | . |
| Hypertension | -277.3797 | 392.4702 | ±784.9405 | -0.707 | 0.4797 |  |
| High cholesterol | +304.2682 | 379.9137 | ±759.8274 | +0.801 | 0.4232 |  |
| **Kidney disease** | **-1318.6626** | 484.3868 | ±968.7736 | **-2.722** | **0.0065** | ** |
| **Circulatory disease** | **-1433.5466** | 443.5360 | ±887.0721 | **-3.232** | **0.0012** | ** |
| Glucose SD, pooled (mg/dL) | +4.9212 | 17.3196 | ±34.6393 | +0.284 | 0.7763 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.469** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21529.7268** | 1528.6432 | ±3057.2864 | **+14.084** | **4.75e-45** | *** |
| Education: graduate level (vs college) | -46.7309 | 383.2719 | ±766.5439 | -0.122 | 0.9030 |  |
| Education: high school or below (vs college) | +1057.2653 | 633.5457 | ±1267.0914 | +1.669 | 0.0952 | . |
| Site: UCSD (vs UAB) | +665.8026 | 482.1618 | ±964.3236 | +1.381 | 0.1673 |  |
| Site: UW (vs UAB) | +16.8037 | 421.6039 | ±843.2078 | +0.040 | 0.9682 |  |
| **Age (years)** | **-160.2211** | 16.5924 | ±33.1848 | **-9.656** | **4.62e-22** | *** |
| BMI (kg/m2) | -48.4991 | 29.2378 | ±58.4755 | -1.659 | 0.0972 | . |
| Hypertension | -270.2653 | 392.4272 | ±784.8545 | -0.689 | 0.4910 |  |
| High cholesterol | +300.2521 | 379.5500 | ±759.1001 | +0.791 | 0.4289 |  |
| **Kidney disease** | **-1292.8768** | 484.0962 | ±968.1924 | **-2.671** | **0.0076** | ** |
| **Circulatory disease** | **-1426.2473** | 442.5686 | ±885.1372 | **-3.223** | **0.0013** | ** |
| Avg. daily SD (mg/dL) | +0.4803 | 18.5898 | ±37.1796 | +0.026 | 0.9794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **690**, R² = **0.1666**, Adj R² = **0.1530**, F-statistic = **12.32** (p = **2.43e-21**), Residual SE = **4605.356** on **678** df, AIC = **13610.3**, BIC = **13664.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22128.8116** | 1624.3208 | ±3248.6416 | **+13.623** | **2.91e-42** | *** |
| Education: graduate level (vs college) | -63.2611 | 381.5556 | ±763.1111 | -0.166 | 0.8683 |  |
| Education: high school or below (vs college) | +1069.1705 | 632.7412 | ±1265.4824 | +1.690 | 0.0911 | . |
| Site: UCSD (vs UAB) | +639.7637 | 485.4058 | ±970.8117 | +1.318 | 0.1875 |  |
| Site: UW (vs UAB) | -27.0008 | 425.5256 | ±851.0513 | -0.063 | 0.9494 |  |
| **Age (years)** | **-159.3871** | 16.5263 | ±33.0525 | **-9.644** | **5.19e-22** | *** |
| BMI (kg/m2) | -48.5075 | 28.9821 | ±57.9642 | -1.674 | 0.0942 | . |
| Hypertension | -254.5364 | 391.1636 | ±782.3271 | -0.651 | 0.5152 |  |
| High cholesterol | +284.2147 | 379.3046 | ±758.6091 | +0.749 | 0.4537 |  |
| **Kidney disease** | **-1216.3418** | 477.0439 | ±954.0877 | **-2.550** | **0.0108** | * |
| **Circulatory disease** | **-1429.5475** | 440.6297 | ±881.2593 | **-3.244** | **0.0012** | ** |
| CV (%) | -26.2244 | 30.8152 | ±61.6304 | -0.851 | 0.3948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.21e-21**), Residual SE = **4607.367** on **678** df, AIC = **13610.9**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21689.4298** | 1739.6366 | ±3479.2733 | **+12.468** | **1.12e-35** | *** |
| Education: graduate level (vs college) | -44.4389 | 380.9653 | ±761.9306 | -0.117 | 0.9071 |  |
| Education: high school or below (vs college) | +1056.9223 | 633.6817 | ±1267.3634 | +1.668 | 0.0953 | . |
| Site: UCSD (vs UAB) | +668.2296 | 485.7892 | ±971.5784 | +1.376 | 0.1690 |  |
| Site: UW (vs UAB) | +23.1571 | 423.8337 | ±847.6673 | +0.055 | 0.9564 |  |
| **Age (years)** | **-160.3455** | 16.5028 | ±33.0056 | **-9.716** | **2.57e-22** | *** |
| BMI (kg/m2) | -48.3512 | 29.1146 | ±58.2293 | -1.661 | 0.0968 | . |
| Hypertension | -273.0011 | 391.3782 | ±782.7564 | -0.698 | 0.4855 |  |
| High cholesterol | +301.4258 | 379.0118 | ±758.0236 | +0.795 | 0.4264 |  |
| **Kidney disease** | **-1304.5452** | 476.4126 | ±952.8252 | **-2.738** | **0.0062** | ** |
| **Circulatory disease** | **-1426.2471** | 441.1101 | ±882.2203 | **-3.233** | **0.0012** | ** |
| Mean / SD ratio | -31.6650 | 164.3227 | ±328.6455 | -0.193 | 0.8472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1660**, Adj R² = **0.1525**, F-statistic = **12.27** (p = **2.99e-21**), Residual SE = **4606.865** on **678** df, AIC = **13610.7**, BIC = **13665.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21872.4623** | 1695.4211 | ±3390.8422 | **+12.901** | **4.45e-38** | *** |
| Education: graduate level (vs college) | -42.2616 | 379.6514 | ±759.3028 | -0.111 | 0.9114 |  |
| Education: high school or below (vs college) | +1053.1010 | 635.2944 | ±1270.5888 | +1.658 | 0.0974 | . |
| Site: UCSD (vs UAB) | +671.1360 | 486.4048 | ±972.8096 | +1.380 | 0.1677 |  |
| Site: UW (vs UAB) | +32.1965 | 423.6089 | ±847.2178 | +0.076 | 0.9394 |  |
| **Age (years)** | **-160.6887** | 16.4909 | ±32.9818 | **-9.744** | **1.96e-22** | *** |
| BMI (kg/m2) | -47.8419 | 29.1118 | ±58.2236 | -1.643 | 0.1003 |  |
| Hypertension | -277.8491 | 390.8171 | ±781.6341 | -0.711 | 0.4771 |  |
| High cholesterol | +304.9979 | 378.9854 | ±757.9708 | +0.805 | 0.4209 |  |
| **Kidney disease** | **-1322.3025** | 473.1716 | ±946.3431 | **-2.795** | **0.0052** | ** |
| **Circulatory disease** | **-1423.9662** | 440.7785 | ±881.5570 | **-3.231** | **0.0012** | ** |
| Avg. daily mean/SD | -61.3099 | 129.6089 | ±259.2179 | -0.473 | 0.6362 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **690**, R² = **0.1703**, Adj R² = **0.1568**, F-statistic = **12.65** (p = **5.91e-22**), Residual SE = **4595.101** on **678** df, AIC = **13607.2**, BIC = **13661.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19696.3304** | 1799.5226 | ±3599.0452 | **+10.945** | **7.00e-28** | *** |
| Education: graduate level (vs college) | +7.1941 | 381.5395 | ±763.0790 | +0.019 | 0.9850 |  |
| Education: high school or below (vs college) | +1021.4258 | 629.1415 | ±1258.2830 | +1.624 | 0.1045 |  |
| Site: UCSD (vs UAB) | +751.5406 | 489.4807 | ±978.9613 | +1.535 | 0.1247 |  |
| Site: UW (vs UAB) | +153.2053 | 425.0915 | ±850.1829 | +0.360 | 0.7185 |  |
| **Age (years)** | **-157.7646** | 16.3034 | ±32.6067 | **-9.677** | **3.78e-22** | *** |
| BMI (kg/m2) | -49.7299 | 29.0299 | ±58.0598 | -1.713 | 0.0867 | . |
| Hypertension | -248.6170 | 390.1754 | ±780.3507 | -0.637 | 0.5240 |  |
| High cholesterol | +346.9125 | 382.5457 | ±765.0915 | +0.907 | 0.3645 |  |
| **Kidney disease** | **-1365.8487** | 468.7044 | ±937.4087 | **-2.914** | **0.0036** | ** |
| **Circulatory disease** | **-1434.7615** | 440.2083 | ±880.4165 | **-3.259** | **0.0011** | ** |
| MAG (mg/dL/h) | +35.8123 | 21.1825 | ±42.3649 | +1.691 | 0.0909 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.19e-21**), Residual SE = **4607.332** on **678** df, AIC = **13610.9**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21390.3432** | 1638.2427 | ±3276.4854 | **+13.057** | **5.81e-39** | *** |
| Education: graduate level (vs college) | -43.3228 | 382.2617 | ±764.5235 | -0.113 | 0.9098 |  |
| Education: high school or below (vs college) | +1046.8805 | 633.9924 | ±1267.9848 | +1.651 | 0.0987 | . |
| Site: UCSD (vs UAB) | +673.7281 | 482.7165 | ±965.4330 | +1.396 | 0.1628 |  |
| Site: UW (vs UAB) | +27.3518 | 422.6918 | ±845.3836 | +0.065 | 0.9484 |  |
| **Age (years)** | **-160.2019** | 16.4929 | ±32.9858 | **-9.713** | **2.64e-22** | *** |
| BMI (kg/m2) | -48.7248 | 29.1512 | ±58.3024 | -1.671 | 0.0946 | . |
| Hypertension | -271.3801 | 391.5158 | ±783.0317 | -0.693 | 0.4882 |  |
| High cholesterol | +302.8575 | 379.5215 | ±759.0431 | +0.798 | 0.4249 |  |
| **Kidney disease** | **-1309.3552** | 480.0665 | ±960.1329 | **-2.727** | **0.0064** | ** |
| **Circulatory disease** | **-1429.6168** | 442.3751 | ±884.7503 | **-3.232** | **0.0012** | ** |
| Avg. daily range (mg/dL) | +1.0464 | 5.4457 | ±10.8914 | +0.192 | 0.8476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **690**, R² = **0.1686**, Adj R² = **0.1552**, F-statistic = **12.50** (p = **1.10e-21**), Residual SE = **4599.598** on **678** df, AIC = **13608.6**, BIC = **13663.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21216.5687** | 1494.5111 | ±2989.0223 | **+14.196** | **9.65e-46** | *** |
| Education: graduate level (vs college) | +8.3989 | 391.8855 | ±783.7711 | +0.021 | 0.9829 |  |
| Education: high school or below (vs college) | +1029.2665 | 628.5590 | ±1257.1179 | +1.638 | 0.1015 |  |
| Site: UCSD (vs UAB) | +694.0621 | 486.4465 | ±972.8931 | +1.427 | 0.1536 |  |
| Site: UW (vs UAB) | +83.4958 | 423.7099 | ±847.4198 | +0.197 | 0.8438 |  |
| **Age (years)** | **-159.1699** | 16.3509 | ±32.7018 | **-9.735** | **2.15e-22** | *** |
| BMI (kg/m2) | -54.7497 | 29.4681 | ±58.9363 | -1.858 | 0.0632 | . |
| Hypertension | -312.9617 | 391.1188 | ±782.2377 | -0.800 | 0.4236 |  |
| High cholesterol | +316.1738 | 378.8160 | ±757.6319 | +0.835 | 0.4039 |  |
| **Kidney disease** | **-1330.5716** | 471.6328 | ±943.2656 | **-2.821** | **0.0048** | ** |
| **Circulatory disease** | **-1481.2720** | 445.7988 | ±891.5976 | **-3.323** | **8.91e-04** | *** |
| SD of daily means (mg/dL) | +34.2837 | 26.7847 | ±53.5695 | +1.280 | 0.2006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **690**, R² = **0.1668**, Adj R² = **0.1533**, F-statistic = **12.34** (p = **2.20e-21**), Residual SE = **4604.641** on **678** df, AIC = **13610.1**, BIC = **13664.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22158.5494** | 1751.6401 | ±3503.2802 | **+12.650** | **1.12e-36** | *** |
| Education: graduate level (vs college) | -28.8198 | 383.9622 | ±767.9244 | -0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +1005.6737 | 627.4300 | ±1254.8599 | +1.603 | 0.1090 |  |
| Site: UCSD (vs UAB) | +695.5087 | 484.6706 | ±969.3412 | +1.435 | 0.1513 |  |
| Site: UW (vs UAB) | +50.9305 | 424.5983 | ±849.1966 | +0.120 | 0.9045 |  |
| **Age (years)** | **-160.2004** | 16.4914 | ±32.9828 | **-9.714** | **2.62e-22** | *** |
| BMI (kg/m2) | -53.1762 | 29.4112 | ±58.8225 | -1.808 | 0.0706 | . |
| Hypertension | -280.4042 | 391.3927 | ±782.7854 | -0.716 | 0.4737 |  |
| High cholesterol | +309.8068 | 379.7726 | ±759.5451 | +0.816 | 0.4146 |  |
| **Kidney disease** | **-1320.1825** | 474.0132 | ±948.0265 | **-2.785** | **0.0054** | ** |
| **Circulatory disease** | **-1456.1877** | 441.8429 | ±883.6857 | **-3.296** | **9.82e-04** | *** |
| Time in range 70-180, pooled (%) | -6.7079 | 8.5178 | ±17.0356 | -0.788 | 0.4310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.27e-21**), Residual SE = **4604.843** on **678** df, AIC = **13610.1**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22140.4149** | 1754.5811 | ±3509.1621 | **+12.619** | **1.67e-36** | *** |
| Education: graduate level (vs college) | -31.2357 | 383.5740 | ±767.1481 | -0.081 | 0.9351 |  |
| Education: high school or below (vs college) | +1006.1430 | 627.1516 | ±1254.3033 | +1.604 | 0.1086 |  |
| Site: UCSD (vs UAB) | +696.6150 | 484.3411 | ±968.6823 | +1.438 | 0.1504 |  |
| Site: UW (vs UAB) | +50.0463 | 424.4287 | ±848.8574 | +0.118 | 0.9061 |  |
| **Age (years)** | **-160.2748** | 16.5027 | ±33.0053 | **-9.712** | **2.68e-22** | *** |
| BMI (kg/m2) | -53.0542 | 29.4467 | ±58.8933 | -1.802 | 0.0716 | . |
| Hypertension | -279.1870 | 391.3239 | ±782.6477 | -0.713 | 0.4756 |  |
| High cholesterol | +308.9738 | 379.8143 | ±759.6285 | +0.813 | 0.4159 |  |
| **Kidney disease** | **-1321.5841** | 474.4073 | ±948.8145 | **-2.786** | **0.0053** | ** |
| **Circulatory disease** | **-1454.4007** | 442.0209 | ±884.0417 | **-3.290** | **0.0010** | ** |
| Avg. daily time in range 70-180 (%) | -6.4165 | 8.4344 | ±16.8689 | -0.761 | 0.4468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1693**, Adj R² = **0.1558**, F-statistic = **12.56** (p = **8.59e-22**), Residual SE = **4597.811** on **678** df, AIC = **13608.0**, BIC = **13662.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21795.2489** | 1522.8846 | ±3045.7693 | **+14.312** | **1.85e-46** | *** |
| Education: graduate level (vs college) | -64.6144 | 380.0925 | ±760.1850 | -0.170 | 0.8650 |  |
| Education: high school or below (vs college) | +1015.6631 | 629.0069 | ±1258.0137 | +1.615 | 0.1064 |  |
| Site: UCSD (vs UAB) | +616.7296 | 490.0523 | ±980.1046 | +1.258 | 0.2082 |  |
| Site: UW (vs UAB) | -22.1632 | 428.1568 | ±856.3135 | -0.052 | 0.9587 |  |
| **Age (years)** | **-161.0584** | 16.5693 | ±33.1385 | **-9.720** | **2.47e-22** | *** |
| BMI (kg/m2) | -48.3383 | 29.2520 | ±58.5039 | -1.652 | 0.0984 | . |
| Hypertension | -242.7734 | 391.7915 | ±783.5829 | -0.620 | 0.5355 |  |
| High cholesterol | +264.0081 | 378.2895 | ±756.5790 | +0.698 | 0.4852 |  |
| **Kidney disease** | **-1293.1809** | 467.9560 | ±935.9121 | **-2.763** | **0.0057** | ** |
| **Circulatory disease** | **-1383.9087** | 441.8017 | ±883.6034 | **-3.132** | **0.0017** | ** |
| Any reading < 54 during wear (0/1) | -699.6394 | 413.0243 | ±826.0485 | -1.694 | 0.0903 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1677**, Adj R² = **0.1542**, F-statistic = **12.42** (p = **1.59e-21**), Residual SE = **4602.286** on **678** df, AIC = **13609.4**, BIC = **13663.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21651.9359** | 1506.2815 | ±3012.5629 | **+14.374** | **7.49e-47** | *** |
| Education: graduate level (vs college) | -75.5819 | 380.3965 | ±760.7929 | -0.199 | 0.8425 |  |
| Education: high school or below (vs college) | +1023.3439 | 633.6138 | ±1267.2275 | +1.615 | 0.1063 |  |
| Site: UCSD (vs UAB) | +625.0745 | 489.6438 | ±979.2876 | +1.277 | 0.2017 |  |
| Site: UW (vs UAB) | -34.5419 | 429.2829 | ±858.5658 | -0.080 | 0.9359 |  |
| **Age (years)** | **-159.3834** | 16.4631 | ±32.9262 | **-9.681** | **3.62e-22** | *** |
| BMI (kg/m2) | -50.1786 | 29.1368 | ±58.2737 | -1.722 | 0.0850 | . |
| Hypertension | -269.3140 | 390.3696 | ±780.7393 | -0.690 | 0.4903 |  |
| High cholesterol | +261.7239 | 380.2306 | ±760.4611 | +0.688 | 0.4912 |  |
| **Kidney disease** | **-1298.9427** | 466.4627 | ±932.9253 | **-2.785** | **0.0054** | ** |
| **Circulatory disease** | **-1445.9815** | 441.5811 | ±883.1622 | **-3.275** | **0.0011** | ** |
| Time < 54 (%) | -361.9507 | 619.8516 | ±1239.7032 | -0.584 | 0.5593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1687**, Adj R² = **0.1552**, F-statistic = **12.51** (p = **1.07e-21**), Residual SE = **4599.429** on **678** df, AIC = **13608.5**, BIC = **13663.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21651.9986** | 1504.5964 | ±3009.1928 | **+14.391** | **5.93e-47** | *** |
| Education: graduate level (vs college) | -77.6545 | 380.5882 | ±761.1764 | -0.204 | 0.8383 |  |
| Education: high school or below (vs college) | +1011.7310 | 633.3336 | ±1266.6671 | +1.597 | 0.1102 |  |
| Site: UCSD (vs UAB) | +613.5422 | 490.2941 | ±980.5882 | +1.251 | 0.2108 |  |
| Site: UW (vs UAB) | -55.0660 | 429.1751 | ±858.3502 | -0.128 | 0.8979 |  |
| **Age (years)** | **-159.3222** | 16.4646 | ±32.9292 | **-9.677** | **3.79e-22** | *** |
| BMI (kg/m2) | -49.5683 | 29.0549 | ±58.1098 | -1.706 | 0.0880 | . |
| Hypertension | -263.8081 | 389.4574 | ±778.9149 | -0.677 | 0.4982 |  |
| High cholesterol | +243.7600 | 379.7831 | ±759.5663 | +0.642 | 0.5210 |  |
| **Kidney disease** | **-1289.9052** | 466.2614 | ±932.5229 | **-2.766** | **0.0057** | ** |
| **Circulatory disease** | **-1451.5282** | 440.9031 | ±881.8061 | **-3.292** | **9.94e-04** | *** |
| Avg. daily time < 54 (%) | -519.2349 | 334.9115 | ±669.8230 | -1.550 | 0.1211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1701**, Adj R² = **0.1566**, F-statistic = **12.63** (p = **6.41e-22**), Residual SE = **4595.691** on **678** df, AIC = **13607.4**, BIC = **13661.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21700.2196** | 1498.3257 | ±2996.6514 | **+14.483** | **1.55e-47** | *** |
| Education: graduate level (vs college) | -101.6528 | 378.6451 | ±757.2902 | -0.268 | 0.7883 |  |
| Education: high school or below (vs college) | +1015.0026 | 632.1327 | ±1264.2654 | +1.606 | 0.1083 |  |
| Site: UCSD (vs UAB) | +585.3926 | 488.2029 | ±976.4058 | +1.199 | 0.2305 |  |
| Site: UW (vs UAB) | -79.1892 | 426.8884 | ±853.7767 | -0.186 | 0.8528 |  |
| **Age (years)** | **-158.7509** | 16.4387 | ±32.8775 | **-9.657** | **4.59e-22** | *** |
| BMI (kg/m2) | -48.8513 | 29.0341 | ±58.0682 | -1.683 | 0.0925 | . |
| Hypertension | -246.7868 | 388.4215 | ±776.8430 | -0.635 | 0.5252 |  |
| High cholesterol | +218.7556 | 377.3164 | ±754.6329 | +0.580 | 0.5621 |  |
| **Kidney disease** | **-1281.8352** | 465.8631 | ±931.7263 | **-2.752** | **0.0059** | ** |
| **Circulatory disease** | **-1483.1063** | 439.6566 | ±879.3131 | **-3.373** | **7.43e-04** | *** |
| **Time 54-69, pooled (%)** | **-318.0817** | 154.8236 | ±309.6471 | **-2.054** | **0.0399** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **690**, R² = **0.1705**, Adj R² = **0.1571**, F-statistic = **12.67** (p = **5.34e-22**), Residual SE = **4594.368** on **678** df, AIC = **13607.0**, BIC = **13661.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21670.7522** | 1498.5110 | ±2997.0220 | **+14.462** | **2.12e-47** | *** |
| Education: graduate level (vs college) | -103.3671 | 378.7894 | ±757.5787 | -0.273 | 0.7849 |  |
| Education: high school or below (vs college) | +1007.9186 | 631.0353 | ±1262.0706 | +1.597 | 0.1102 |  |
| Site: UCSD (vs UAB) | +580.2411 | 488.9846 | ±977.9692 | +1.187 | 0.2354 |  |
| Site: UW (vs UAB) | -90.9237 | 427.9157 | ±855.8313 | -0.212 | 0.8317 |  |
| **Age (years)** | **-158.4847** | 16.4279 | ±32.8557 | **-9.647** | **5.05e-22** | *** |
| BMI (kg/m2) | -48.4853 | 29.0455 | ±58.0910 | -1.669 | 0.0951 | . |
| Hypertension | -244.1403 | 388.4408 | ±776.8815 | -0.629 | 0.5297 |  |
| High cholesterol | +213.3498 | 376.3968 | ±752.7936 | +0.567 | 0.5708 |  |
| **Kidney disease** | **-1277.4327** | 465.8878 | ±931.7757 | **-2.742** | **0.0061** | ** |
| **Circulatory disease** | **-1484.8886** | 440.2841 | ±880.5682 | **-3.373** | **7.45e-04** | *** |
| **Avg. daily time 54-69 (%)** | **-312.0102** | 140.3172 | ±280.6343 | **-2.224** | **0.0262** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **690**, R² = **0.1702**, Adj R² = **0.1567**, F-statistic = **12.64** (p = **6.08e-22**), Residual SE = **4595.300** on **678** df, AIC = **13607.3**, BIC = **13661.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21731.3956** | 1501.4356 | ±3002.8711 | **+14.474** | **1.78e-47** | *** |
| Education: graduate level (vs college) | -106.2867 | 379.4261 | ±758.8522 | -0.280 | 0.7794 |  |
| Education: high school or below (vs college) | +1002.9461 | 632.2693 | ±1264.5387 | +1.586 | 0.1127 |  |
| Site: UCSD (vs UAB) | +579.6536 | 489.7163 | ±979.4326 | +1.184 | 0.2366 |  |
| Site: UW (vs UAB) | -87.6813 | 428.4359 | ±856.8718 | -0.205 | 0.8378 |  |
| **Age (years)** | **-158.5852** | 16.4402 | ±32.8805 | **-9.646** | **5.10e-22** | *** |
| BMI (kg/m2) | -49.8868 | 28.9789 | ±57.9577 | -1.721 | 0.0852 | . |
| Hypertension | -252.4016 | 388.6366 | ±777.2731 | -0.649 | 0.5160 |  |
| High cholesterol | +214.4672 | 377.9082 | ±755.8164 | +0.568 | 0.5704 |  |
| **Kidney disease** | **-1289.6734** | 465.6222 | ±931.2445 | **-2.770** | **0.0056** | ** |
| **Circulatory disease** | **-1481.7552** | 440.0057 | ±880.0115 | **-3.368** | **7.58e-04** | *** |
| **Time < 70 (%)** | **-236.9123** | 96.4272 | ±192.8545 | **-2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **690**, R² = **0.1708**, Adj R² = **0.1573**, F-statistic = **12.70** (p = **4.83e-22**), Residual SE = **4593.646** on **678** df, AIC = **13606.8**, BIC = **13661.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21691.9253** | 1500.2090 | ±3000.4179 | **+14.459** | **2.19e-47** | *** |
| Education: graduate level (vs college) | -104.5608 | 379.5770 | ±759.1540 | -0.275 | 0.7830 |  |
| Education: high school or below (vs college) | +997.7757 | 631.5354 | ±1263.0708 | +1.580 | 0.1141 |  |
| Site: UCSD (vs UAB) | +575.8967 | 490.2317 | ±980.4634 | +1.175 | 0.2401 |  |
| Site: UW (vs UAB) | -99.1367 | 429.0556 | ±858.1113 | -0.231 | 0.8173 |  |
| **Age (years)** | **-158.4710** | 16.4307 | ±32.8614 | **-9.645** | **5.17e-22** | *** |
| BMI (kg/m2) | -48.9988 | 28.9899 | ±57.9798 | -1.690 | 0.0910 | . |
| Hypertension | -247.2857 | 388.5594 | ±777.1188 | -0.636 | 0.5245 |  |
| High cholesterol | +207.1972 | 377.3641 | ±754.7283 | +0.549 | 0.5830 |  |
| **Kidney disease** | **-1280.2132** | 465.6437 | ±931.2874 | **-2.749** | **0.0060** | ** |
| **Circulatory disease** | **-1483.2884** | 440.4434 | ±880.8868 | **-3.368** | **7.58e-04** | *** |
| **Avg. daily time < 70 (%)** | **-240.4531** | 87.9352 | ±175.8705 | **-2.734** | **0.0062** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.471** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21554.8551** | 2007.2692 | ±4014.5385 | **+10.738** | **6.72e-27** | *** |
| Education: graduate level (vs college) | -46.9220 | 386.7841 | ±773.5682 | -0.121 | 0.9034 |  |
| Education: high school or below (vs college) | +1058.2743 | 625.1065 | ±1250.2131 | +1.693 | 0.0905 | . |
| Site: UCSD (vs UAB) | +665.0799 | 484.9763 | ±969.9526 | +1.371 | 0.1703 |  |
| Site: UW (vs UAB) | +15.7628 | 423.7599 | ±847.5197 | +0.037 | 0.9703 |  |
| **Age (years)** | **-160.1870** | 16.3254 | ±32.6508 | **-9.812** | **9.98e-23** | *** |
| BMI (kg/m2) | -48.4680 | 29.3401 | ±58.6802 | -1.652 | 0.0985 | . |
| Hypertension | -269.8022 | 390.6640 | ±781.3281 | -0.691 | 0.4898 |  |
| High cholesterol | +300.0535 | 381.0181 | ±762.0361 | +0.788 | 0.4310 |  |
| **Kidney disease** | **-1290.5128** | 470.4119 | ±940.8239 | **-2.743** | **0.0061** | ** |
| **Circulatory disease** | **-1425.9513** | 443.4871 | ±886.9742 | **-3.215** | **0.0013** | ** |
| Time 54-250, pooled (%) | -0.1303 | 12.8068 | ±25.6135 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.461** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21600.6451** | 1995.5832 | ±3991.1663 | **+10.824** | **2.64e-27** | *** |
| Education: graduate level (vs college) | -45.4858 | 386.7495 | ±773.4991 | -0.118 | 0.9064 |  |
| Education: high school or below (vs college) | +1056.1037 | 625.8216 | ±1251.6431 | +1.688 | 0.0915 | . |
| Site: UCSD (vs UAB) | +666.1525 | 484.9823 | ±969.9646 | +1.374 | 0.1696 |  |
| Site: UW (vs UAB) | +17.5868 | 423.7547 | ±847.5095 | +0.042 | 0.9669 |  |
| **Age (years)** | **-160.1382** | 16.3489 | ±32.6978 | **-9.795** | **1.18e-22** | *** |
| BMI (kg/m2) | -48.6006 | 29.3090 | ±58.6180 | -1.658 | 0.0973 | . |
| Hypertension | -270.3052 | 390.6822 | ±781.3644 | -0.692 | 0.4890 |  |
| High cholesterol | +300.5631 | 380.9142 | ±761.8285 | +0.789 | 0.4301 |  |
| **Kidney disease** | **-1291.6843** | 470.8081 | ±941.6161 | **-2.744** | **0.0061** | ** |
| **Circulatory disease** | **-1427.1833** | 443.4588 | ±886.9176 | **-3.218** | **0.0013** | ** |
| Avg. daily time 54-250 (%) | -0.6242 | 12.5594 | ±25.1187 | -0.050 | 0.9604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1691**, Adj R² = **0.1557**, F-statistic = **12.55** (p = **9.06e-22**), Residual SE = **4598.193** on **678** df, AIC = **13608.1**, BIC = **13662.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21571.5303** | 1502.5028 | ±3005.0055 | **+14.357** | **9.62e-47** | *** |
| Education: graduate level (vs college) | -56.8069 | 377.9325 | ±755.8650 | -0.150 | 0.8805 |  |
| Education: high school or below (vs college) | +986.6784 | 635.4438 | ±1270.8877 | +1.553 | 0.1205 |  |
| Site: UCSD (vs UAB) | +709.3825 | 486.4106 | ±972.8213 | +1.458 | 0.1447 |  |
| Site: UW (vs UAB) | +37.5975 | 425.6476 | ±851.2951 | +0.088 | 0.9296 |  |
| **Age (years)** | **-162.5340** | 16.6141 | ±33.2281 | **-9.783** | **1.33e-22** | *** |
| **BMI (kg/m2)** | **-57.5085** | 29.0374 | ±58.0748 | **-1.980** | **0.0476** | * |
| Hypertension | -276.8727 | 390.9561 | ±781.9123 | -0.708 | 0.4788 |  |
| High cholesterol | +303.6202 | 378.8492 | ±757.6984 | +0.801 | 0.4229 |  |
| **Kidney disease** | **-1339.0777** | 472.1696 | ±944.3392 | **-2.836** | **0.0046** | ** |
| **Circulatory disease** | **-1473.8015** | 439.8135 | ±879.6270 | **-3.351** | **8.05e-04** | *** |
| Time 181-250, pooled (%) | +20.3659 | 13.1264 | ±26.2527 | +1.552 | 0.1208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **690**, R² = **0.1687**, Adj R² = **0.1552**, F-statistic = **12.51** (p = **1.07e-21**), Residual SE = **4599.366** on **678** df, AIC = **13608.5**, BIC = **13662.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21565.2621** | 1503.3746 | ±3006.7493 | **+14.345** | **1.15e-46** | *** |
| Education: graduate level (vs college) | -58.7188 | 378.0489 | ±756.0977 | -0.155 | 0.8766 |  |
| Education: high school or below (vs college) | +985.0105 | 633.5293 | ±1267.0585 | +1.555 | 0.1200 |  |
| Site: UCSD (vs UAB) | +711.8623 | 486.1087 | ±972.2174 | +1.464 | 0.1431 |  |
| Site: UW (vs UAB) | +40.2716 | 425.4875 | ±850.9750 | +0.095 | 0.9246 |  |
| **Age (years)** | **-162.2351** | 16.6278 | ±33.2557 | **-9.757** | **1.72e-22** | *** |
| BMI (kg/m2) | -56.8849 | 29.1712 | ±58.3424 | -1.950 | 0.0512 | . |
| Hypertension | -276.2384 | 391.1025 | ±782.2051 | -0.706 | 0.4800 |  |
| High cholesterol | +301.8022 | 379.1991 | ±758.3981 | +0.796 | 0.4261 |  |
| **Kidney disease** | **-1337.6450** | 472.4344 | ±944.8688 | **-2.831** | **0.0046** | ** |
| **Circulatory disease** | **-1466.7544** | 440.5612 | ±881.1224 | **-3.329** | **8.71e-04** | *** |
| Avg. daily time 181-250 (%) | +18.6582 | 12.8673 | ±25.7345 | +1.450 | 0.1470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **690**, R² = **0.1671**, Adj R² = **0.1535**, F-statistic = **12.36** (p = **2.01e-21**), Residual SE = **4603.968** on **678** df, AIC = **13609.9**, BIC = **13664.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21487.9319** | 1499.3420 | ±2998.6840 | **+14.332** | **1.39e-46** | *** |
| Education: graduate level (vs college) | -28.7478 | 383.3638 | ±766.7276 | -0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +998.4226 | 627.3725 | ±1254.7451 | +1.591 | 0.1115 |  |
| Site: UCSD (vs UAB) | +696.0260 | 484.8899 | ±969.7797 | +1.435 | 0.1512 |  |
| Site: UW (vs UAB) | +51.4065 | 424.4319 | ±848.8638 | +0.121 | 0.9036 |  |
| **Age (years)** | **-160.1496** | 16.4827 | ±32.9654 | **-9.716** | **2.57e-22** | *** |
| BMI (kg/m2) | -53.7123 | 29.3942 | ±58.7885 | -1.827 | 0.0677 | . |
| Hypertension | -280.9783 | 391.3809 | ±782.7618 | -0.718 | 0.4728 |  |
| High cholesterol | +308.1603 | 379.6943 | ±759.3885 | +0.812 | 0.4170 |  |
| **Kidney disease** | **-1323.2623** | 473.9549 | ±947.9099 | **-2.792** | **0.0052** | ** |
| **Circulatory disease** | **-1461.1017** | 441.8986 | ±883.7972 | **-3.306** | **9.45e-04** | *** |
| Time > 180 (%) | +7.4020 | 8.4338 | ±16.8676 | +0.878 | 0.3801 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1670**, Adj R² = **0.1535**, F-statistic = **12.36** (p = **2.05e-21**), Residual SE = **4604.101** on **678** df, AIC = **13609.9**, BIC = **13664.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21497.7209** | 1499.9994 | ±2999.9987 | **+14.332** | **1.38e-46** | *** |
| Education: graduate level (vs college) | -30.9515 | 383.0216 | ±766.0432 | -0.081 | 0.9356 |  |
| Education: high school or below (vs college) | +997.7483 | 627.0307 | ±1254.0614 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +697.9068 | 484.5518 | ±969.1037 | +1.440 | 0.1498 |  |
| Site: UW (vs UAB) | +50.9445 | 424.2729 | ±848.5458 | +0.120 | 0.9044 |  |
| **Age (years)** | **-160.2319** | 16.4930 | ±32.9860 | **-9.715** | **2.60e-22** | *** |
| BMI (kg/m2) | -53.6462 | 29.4291 | ±58.8581 | -1.823 | 0.0683 | . |
| Hypertension | -279.7031 | 391.2938 | ±782.5875 | -0.715 | 0.4747 |  |
| High cholesterol | +307.3186 | 379.7251 | ±759.4501 | +0.809 | 0.4183 |  |
| **Kidney disease** | **-1325.1833** | 474.3249 | ±948.6498 | **-2.794** | **0.0052** | ** |
| **Circulatory disease** | **-1459.7097** | 442.1163 | ±884.2326 | **-3.302** | **9.61e-04** | *** |
| Avg. daily time > 180 (%) | +7.2152 | 8.3701 | ±16.7402 | +0.862 | 0.3887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1679**, Adj R² = **0.1544**, F-statistic = **12.44** (p = **1.47e-21**), Residual SE = **4601.708** on **678** df, AIC = **13609.2**, BIC = **13663.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21516.0211** | 1503.8717 | ±3007.7433 | **+14.307** | **1.98e-46** | *** |
| Education: graduate level (vs college) | -8.2813 | 387.2526 | ±774.5052 | -0.021 | 0.9829 |  |
| Education: high school or below (vs college) | +994.9263 | 625.0727 | ±1250.1455 | +1.592 | 0.1115 |  |
| Site: UCSD (vs UAB) | +706.8489 | 483.6921 | ±967.3841 | +1.461 | 0.1439 |  |
| Site: UW (vs UAB) | +51.5872 | 423.8732 | ±847.7464 | +0.122 | 0.9031 |  |
| **Age (years)** | **-159.2472** | 16.4409 | ±32.8817 | **-9.686** | **3.46e-22** | *** |
| BMI (kg/m2) | -56.4983 | 29.4478 | ±58.8956 | -1.919 | 0.0550 | . |
| Hypertension | -280.9422 | 391.1611 | ±782.3222 | -0.718 | 0.4726 |  |
| High cholesterol | +320.5406 | 379.7265 | ±759.4529 | +0.844 | 0.3986 |  |
| **Kidney disease** | **-1311.6845** | 472.6284 | ±945.2568 | **-2.775** | **0.0055** | ** |
| **Circulatory disease** | **-1468.6883** | 441.2877 | ±882.5754 | **-3.328** | **8.74e-04** | *** |
| Nocturnal time > 180 (%) | +8.6654 | 7.7923 | ±15.5847 | +1.112 | 0.2661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.460** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21537.4682** | 1495.3632 | ±2990.7264 | **+14.403** | **4.97e-47** | *** |
| Education: graduate level (vs college) | -45.4524 | 386.5076 | ±773.0152 | -0.118 | 0.9064 |  |
| Education: high school or below (vs college) | +1055.9630 | 624.9556 | ±1249.9113 | +1.690 | 0.0911 | . |
| Site: UCSD (vs UAB) | +666.0750 | 485.0727 | ±970.1453 | +1.373 | 0.1697 |  |
| Site: UW (vs UAB) | +17.6286 | 423.6545 | ±847.3091 | +0.042 | 0.9668 |  |
| **Age (years)** | **-160.1262** | 16.3228 | ±32.6457 | **-9.810** | **1.02e-22** | *** |
| BMI (kg/m2) | -48.6017 | 29.3516 | ±58.7032 | -1.656 | 0.0978 | . |
| Hypertension | -270.3869 | 390.6737 | ±781.3473 | -0.692 | 0.4889 |  |
| High cholesterol | +300.5032 | 380.8671 | ±761.7343 | +0.789 | 0.4301 |  |
| **Kidney disease** | **-1291.5418** | 470.5087 | ±941.0173 | **-2.745** | **0.0061** | ** |
| **Circulatory disease** | **-1427.1652** | 443.5493 | ±887.0987 | **-3.218** | **0.0013** | ** |
| Time > 250 (%) | +0.6277 | 12.8157 | ±25.6314 | +0.049 | 0.9609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.23e-21**), Residual SE = **4607.433** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21534.2204** | 1496.9509 | ±2993.9018 | **+14.385** | **6.39e-47** | *** |
| Education: graduate level (vs college) | -43.9284 | 386.5231 | ±773.0462 | -0.114 | 0.9095 |  |
| Education: high school or below (vs college) | +1053.5495 | 625.7043 | ±1251.4087 | +1.684 | 0.0922 | . |
| Site: UCSD (vs UAB) | +667.2344 | 485.0640 | ±970.1279 | +1.376 | 0.1690 |  |
| Site: UW (vs UAB) | +19.4982 | 423.6839 | ±847.3678 | +0.046 | 0.9633 |  |
| **Age (years)** | **-160.0791** | 16.3469 | ±32.6937 | **-9.793** | **1.21e-22** | *** |
| BMI (kg/m2) | -48.7512 | 29.3145 | ±58.6290 | -1.663 | 0.0963 | . |
| Hypertension | -270.8740 | 390.6768 | ±781.3536 | -0.693 | 0.4881 |  |
| High cholesterol | +301.0074 | 380.7639 | ±761.5278 | +0.791 | 0.4292 |  |
| **Kidney disease** | **-1292.9579** | 470.8643 | ±941.7286 | **-2.746** | **0.0060** | ** |
| **Circulatory disease** | **-1428.6083** | 443.5101 | ±887.0202 | **-3.221** | **0.0013** | ** |
| Avg. daily time > 250 (%) | +1.1777 | 12.5722 | ±25.1445 | +0.094 | 0.9254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 690; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **690**, R² = **0.1849**, Adj R² = **0.1729**, F-statistic = **15.40** (p = **5.12e-25**), Residual SE = **13.513** on **679** df, AIC = **5562.1**, BIC = **5612.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3722** | 4.3530 | ±8.7061 | **+13.410** | **5.32e-41** | *** |
| Education: graduate level (vs college) | -0.3768 | 1.1370 | ±2.2739 | -0.331 | 0.7403 |  |
| Education: high school or below (vs college) | +3.1159 | 1.7654 | ±3.5307 | +1.765 | 0.0776 | . |
| **Site: UCSD (vs UAB)** | **+2.9142** | 1.4586 | ±2.9172 | **+1.998** | **0.0457** | * |
| Site: UW (vs UAB) | +1.1397 | 1.2145 | ±2.4291 | +0.938 | 0.3480 |  |
| **Age (years)** | **-0.5229** | 0.0489 | ±0.0978 | **-10.699** | **1.03e-26** | *** |
| BMI (kg/m2) | -0.0486 | 0.0814 | ±0.1627 | -0.597 | 0.5505 |  |
| Hypertension | -1.0976 | 1.1607 | ±2.3213 | -0.946 | 0.3443 |  |
| High cholesterol | +0.9646 | 1.0857 | ±2.1713 | +0.889 | 0.3743 |  |
| Kidney disease | -2.3816 | 1.4240 | ±2.8480 | -1.672 | 0.0944 | . |
| **Circulatory disease** | **-3.7550** | 1.2733 | ±2.5465 | **-2.949** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **690**, R² = **0.1900**, Adj R² = **0.1769**, F-statistic = **14.46** (p = **2.71e-25**), Residual SE = **13.480** on **678** df, AIC = **5559.7**, BIC = **5614.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.6792** | 4.7444 | ±9.4888 | **+11.314** | **1.12e-29** | *** |
| Education: graduate level (vs college) | -0.1806 | 1.1447 | ±2.2894 | -0.158 | 0.8746 |  |
| Education: high school or below (vs college) | +2.7359 | 1.7610 | ±3.5220 | +1.554 | 0.1203 |  |
| **Site: UCSD (vs UAB)** | **+3.0034** | 1.4551 | ±2.9101 | **+2.064** | **0.0390** | * |
| Site: UW (vs UAB) | +1.3485 | 1.2050 | ±2.4100 | +1.119 | 0.2631 |  |
| **Age (years)** | **-0.5221** | 0.0487 | ±0.0974 | **-10.722** | **8.06e-27** | *** |
| BMI (kg/m2) | -0.0794 | 0.0838 | ±0.1677 | -0.947 | 0.3435 |  |
| Hypertension | -1.2309 | 1.1676 | ±2.3352 | -1.054 | 0.2918 |  |
| High cholesterol | +0.9153 | 1.0843 | ±2.1685 | +0.844 | 0.3986 |  |
| Kidney disease | -2.3364 | 1.4165 | ±2.8330 | -1.649 | 0.0991 | . |
| **Circulatory disease** | **-3.8526** | 1.2740 | ±2.5481 | **-3.024** | **0.0025** | ** |
| HbA1c (%) | +0.8230 | 0.4304 | ±0.8607 | +1.912 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6485** | 4.4876 | ±8.9753 | **+12.623** | **1.57e-36** | *** |
| Education: graduate level (vs college) | -0.3266 | 1.1468 | ±2.2936 | -0.285 | 0.7758 |  |
| Education: high school or below (vs college) | +2.9524 | 1.7505 | ±3.5010 | +1.687 | 0.0917 | . |
| **Site: UCSD (vs UAB)** | **+2.9797** | 1.4486 | ±2.8973 | **+2.057** | **0.0397** | * |
| Site: UW (vs UAB) | +1.2244 | 1.2020 | ±2.4040 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.5218** | 0.0487 | ±0.0975 | **-10.705** | **9.63e-27** | *** |
| BMI (kg/m2) | -0.0611 | 0.0831 | ±0.1662 | -0.735 | 0.4624 |  |
| Hypertension | -1.1385 | 1.1676 | ±2.3352 | -0.975 | 0.3295 |  |
| High cholesterol | +0.9707 | 1.0884 | ±2.1768 | +0.892 | 0.3724 |  |
| Kidney disease | -2.4430 | 1.4309 | ±2.8619 | -1.707 | 0.0878 | . |
| **Circulatory disease** | **-3.8533** | 1.2793 | ±2.5586 | **-3.012** | **0.0026** | ** |
| Mean glucose (mg/dL) | +0.0126 | 0.0149 | ±0.0298 | +0.848 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9002** | 5.4508 | ±10.9016 | **+10.072** | **7.35e-24** | *** |
| Education: graduate level (vs college) | -0.3266 | 1.1468 | ±2.2936 | -0.285 | 0.7758 |  |
| Education: high school or below (vs college) | +2.9524 | 1.7505 | ±3.5010 | +1.687 | 0.0917 | . |
| **Site: UCSD (vs UAB)** | **+2.9797** | 1.4486 | ±2.8973 | **+2.057** | **0.0397** | * |
| Site: UW (vs UAB) | +1.2244 | 1.2020 | ±2.4040 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.5218** | 0.0487 | ±0.0975 | **-10.705** | **9.63e-27** | *** |
| BMI (kg/m2) | -0.0611 | 0.0831 | ±0.1662 | -0.735 | 0.4624 |  |
| Hypertension | -1.1385 | 1.1676 | ±2.3352 | -0.975 | 0.3295 |  |
| High cholesterol | +0.9707 | 1.0884 | ±2.1768 | +0.892 | 0.3724 |  |
| Kidney disease | -2.4430 | 1.4309 | ±2.8619 | -1.707 | 0.0878 | . |
| **Circulatory disease** | **-3.8533** | 1.2793 | ±2.5586 | **-3.012** | **0.0026** | ** |
| GMI (%) | +0.5282 | 0.6226 | ±1.2452 | +0.848 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **690**, R² = **0.1874**, Adj R² = **0.1742**, F-statistic = **14.21** (p = **7.68e-25**), Residual SE = **13.502** on **678** df, AIC = **5561.9**, BIC = **5616.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.9652** | 4.4923 | ±8.9846 | **+12.458** | **1.27e-35** | *** |
| Education: graduate level (vs college) | -0.2785 | 1.1502 | ±2.3004 | -0.242 | 0.8087 |  |
| Education: high school or below (vs college) | +2.8819 | 1.7494 | ±3.4988 | +1.647 | 0.0995 | . |
| **Site: UCSD (vs UAB)** | **+3.0040** | 1.4475 | ±2.8950 | **+2.075** | **0.0380** | * |
| Site: UW (vs UAB) | +1.2273 | 1.2035 | ±2.4070 | +1.020 | 0.3078 |  |
| **Age (years)** | **-0.5188** | 0.0485 | ±0.0971 | **-10.687** | **1.17e-26** | *** |
| BMI (kg/m2) | -0.0721 | 0.0835 | ±0.1670 | -0.863 | 0.3882 |  |
| Hypertension | -1.1488 | 1.1671 | ±2.3343 | -0.984 | 0.3250 |  |
| High cholesterol | +0.9923 | 1.0891 | ±2.1781 | +0.911 | 0.3622 |  |
| Kidney disease | -2.3898 | 1.4259 | ±2.8518 | -1.676 | 0.0937 | . |
| **Circulatory disease** | **-3.9010** | 1.2800 | ±2.5600 | **-3.048** | **0.0023** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0184 | 0.0147 | ±0.0294 | +1.253 | 0.2102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1857**, Adj R² = **0.1725**, F-statistic = **14.05** (p = **1.51e-24**), Residual SE = **13.516** on **678** df, AIC = **5563.4**, BIC = **5617.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2518** | 4.3852 | ±8.7704 | **+13.056** | **5.89e-39** | *** |
| Education: graduate level (vs college) | -0.3130 | 1.1531 | ±2.3061 | -0.271 | 0.7860 |  |
| Education: high school or below (vs college) | +2.9901 | 1.7530 | ±3.5060 | +1.706 | 0.0881 | . |
| **Site: UCSD (vs UAB)** | **+3.0018** | 1.4418 | ±2.8836 | **+2.082** | **0.0373** | * |
| Site: UW (vs UAB) | +1.2874 | 1.1934 | ±2.3868 | +1.079 | 0.2807 |  |
| **Age (years)** | **-0.5240** | 0.0492 | ±0.0984 | **-10.654** | **1.66e-26** | *** |
| BMI (kg/m2) | -0.0566 | 0.0825 | ±0.1649 | -0.686 | 0.4927 |  |
| Hypertension | -1.1560 | 1.1727 | ±2.3454 | -0.986 | 0.3243 |  |
| High cholesterol | +0.9975 | 1.0878 | ±2.1755 | +0.917 | 0.3591 |  |
| Kidney disease | -2.5962 | 1.4786 | ±2.9572 | -1.756 | 0.0791 | . |
| **Circulatory disease** | **-3.8147** | 1.2746 | ±2.5492 | **-2.993** | **0.0028** | ** |
| Glucose SD, pooled (mg/dL) | +0.0372 | 0.0500 | ±0.1000 | +0.744 | 0.4571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1851**, Adj R² = **0.1719**, F-statistic = **14.00** (p = **1.88e-24**), Residual SE = **13.521** on **678** df, AIC = **5563.9**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7287** | 4.4053 | ±8.8106 | **+13.104** | **3.11e-39** | *** |
| Education: graduate level (vs college) | -0.3483 | 1.1476 | ±2.2952 | -0.304 | 0.7615 |  |
| Education: high school or below (vs college) | +3.0385 | 1.7631 | ±3.5263 | +1.723 | 0.0848 | . |
| **Site: UCSD (vs UAB)** | **+2.9627** | 1.4427 | ±2.8855 | **+2.054** | **0.0400** | * |
| Site: UW (vs UAB) | +1.2149 | 1.1943 | ±2.3886 | +1.017 | 0.3090 |  |
| **Age (years)** | **-0.5238** | 0.0493 | ±0.0985 | **-10.633** | **2.10e-26** | *** |
| BMI (kg/m2) | -0.0517 | 0.0819 | ±0.1638 | -0.632 | 0.5274 |  |
| Hypertension | -1.1274 | 1.1727 | ±2.3454 | -0.961 | 0.3363 |  |
| High cholesterol | +0.9808 | 1.0877 | ±2.1754 | +0.902 | 0.3672 |  |
| Kidney disease | -2.5089 | 1.4764 | ±2.9529 | -1.699 | 0.0893 | . |
| **Circulatory disease** | **-3.7843** | 1.2745 | ±2.5490 | **-2.969** | **0.0030** | ** |
| Avg. daily SD (mg/dL) | +0.0233 | 0.0539 | ±0.1079 | +0.431 | 0.6664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1718**, F-statistic = **13.99** (p = **1.94e-24**), Residual SE = **13.522** on **678** df, AIC = **5563.9**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.2104** | 4.7785 | ±9.5570 | **+12.391** | **2.92e-35** | *** |
| Education: graduate level (vs college) | -0.3996 | 1.1414 | ±2.2828 | -0.350 | 0.7262 |  |
| Education: high school or below (vs college) | +3.1307 | 1.7669 | ±3.5339 | +1.772 | 0.0764 | . |
| **Site: UCSD (vs UAB)** | **+2.8784** | 1.4550 | ±2.9099 | **+1.978** | **0.0479** | * |
| Site: UW (vs UAB) | +1.0792 | 1.2171 | ±2.4342 | +0.887 | 0.3752 |  |
| **Age (years)** | **-0.5218** | 0.0490 | ±0.0980 | **-10.651** | **1.73e-26** | *** |
| BMI (kg/m2) | -0.0487 | 0.0813 | ±0.1627 | -0.599 | 0.5494 |  |
| Hypertension | -1.0760 | 1.1660 | ±2.3320 | -0.923 | 0.3561 |  |
| High cholesterol | +0.9421 | 1.0836 | ±2.1672 | +0.869 | 0.3846 |  |
| Kidney disease | -2.2758 | 1.4647 | ±2.9295 | -1.554 | 0.1202 |  |
| **Circulatory disease** | **-3.7606** | 1.2753 | ±2.5506 | **-2.949** | **0.0032** | ** |
| CV (%) | -0.0375 | 0.0906 | ±0.1812 | -0.414 | 0.6787 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **690**, R² = **0.1853**, Adj R² = **0.1721**, F-statistic = **14.02** (p = **1.73e-24**), Residual SE = **13.519** on **678** df, AIC = **5563.7**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.9058** | 5.0036 | ±10.0071 | **+11.973** | **4.94e-33** | *** |
| Education: graduate level (vs college) | -0.3467 | 1.1408 | ±2.2816 | -0.304 | 0.7612 |  |
| Education: high school or below (vs college) | +3.0956 | 1.7667 | ±3.5333 | +1.752 | 0.0797 | . |
| **Site: UCSD (vs UAB)** | **+2.9501** | 1.4558 | ±2.9116 | **+2.026** | **0.0427** | * |
| Site: UW (vs UAB) | +1.2225 | 1.2102 | ±2.4205 | +1.010 | 0.3124 |  |
| **Age (years)** | **-0.5244** | 0.0490 | ±0.0980 | **-10.707** | **9.42e-27** | *** |
| BMI (kg/m2) | -0.0477 | 0.0817 | ±0.1634 | -0.584 | 0.5592 |  |
| Hypertension | -1.1327 | 1.1659 | ±2.3318 | -0.972 | 0.3313 |  |
| High cholesterol | +0.9804 | 1.0844 | ±2.1689 | +0.904 | 0.3660 |  |
| Kidney disease | -2.5313 | 1.4637 | ±2.9273 | -1.729 | 0.0837 | . |
| **Circulatory disease** | **-3.7613** | 1.2729 | ±2.5457 | **-2.955** | **0.0031** | ** |
| Mean / SD ratio | -0.3317 | 0.4784 | ±0.9568 | -0.693 | 0.4881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1855**, Adj R² = **0.1723**, F-statistic = **14.04** (p = **1.61e-24**), Residual SE = **13.518** on **678** df, AIC = **5563.5**, BIC = **5618.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.0587** | 4.8820 | ±9.7640 | **+12.302** | **8.82e-35** | *** |
| Education: graduate level (vs college) | -0.3509 | 1.1373 | ±2.2747 | -0.309 | 0.7577 |  |
| Education: high school or below (vs college) | +3.0864 | 1.7709 | ±3.5418 | +1.743 | 0.0814 | . |
| **Site: UCSD (vs UAB)** | **+2.9467** | 1.4580 | ±2.9160 | **+2.021** | **0.0433** | * |
| Site: UW (vs UAB) | +1.2264 | 1.2115 | ±2.4230 | +1.012 | 0.3114 |  |
| **Age (years)** | **-0.5254** | 0.0489 | ±0.0979 | **-10.735** | **6.97e-27** | *** |
| BMI (kg/m2) | -0.0456 | 0.0817 | ±0.1634 | -0.557 | 0.5772 |  |
| Hypertension | -1.1396 | 1.1646 | ±2.3293 | -0.978 | 0.3278 |  |
| High cholesterol | +0.9906 | 1.0849 | ±2.1698 | +0.913 | 0.3612 |  |
| Kidney disease | -2.5457 | 1.4471 | ±2.8941 | -1.759 | 0.0785 | . |
| **Circulatory disease** | **-3.7464** | 1.2726 | ±2.5453 | **-2.944** | **0.0032** | ** |
| Avg. daily mean/SD | -0.3139 | 0.3775 | ±0.7549 | -0.831 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **690**, R² = **0.1903**, Adj R² = **0.1771**, F-statistic = **14.48** (p = **2.48e-25**), Residual SE = **13.478** on **678** df, AIC = **5559.5**, BIC = **5613.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3472** | 5.2448 | ±10.4897 | **+9.981** | **1.85e-23** | *** |
| Education: graduate level (vs college) | -0.1990 | 1.1418 | ±2.2836 | -0.174 | 0.8617 |  |
| Education: high school or below (vs college) | +2.9938 | 1.7503 | ±3.5007 | +1.710 | 0.0872 | . |
| **Site: UCSD (vs UAB)** | **+3.1972** | 1.4646 | ±2.9292 | **+2.183** | **0.0290** | * |
| Site: UW (vs UAB) | +1.5898 | 1.2073 | ±2.4146 | +1.317 | 0.1879 |  |
| **Age (years)** | **-0.5150** | 0.0485 | ±0.0970 | **-10.618** | **2.46e-26** | *** |
| BMI (kg/m2) | -0.0528 | 0.0815 | ±0.1629 | -0.648 | 0.5168 |  |
| Hypertension | -1.0290 | 1.1610 | ±2.3221 | -0.886 | 0.3755 |  |
| High cholesterol | +1.1179 | 1.0971 | ±2.1942 | +1.019 | 0.3082 |  |
| Kidney disease | -2.6282 | 1.4249 | ±2.8497 | -1.845 | 0.0651 | . |
| **Circulatory disease** | **-3.7848** | 1.2688 | ±2.5377 | **-2.983** | **0.0029** | ** |
| MAG (mg/dL/h) | +0.1168 | 0.0611 | ±0.1223 | +1.911 | 0.0560 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **690**, R² = **0.1854**, Adj R² = **0.1722**, F-statistic = **14.03** (p = **1.70e-24**), Residual SE = **13.519** on **678** df, AIC = **5563.7**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9321** | 4.7304 | ±9.4608 | **+12.035** | **2.32e-33** | *** |
| Education: graduate level (vs college) | -0.3391 | 1.1448 | ±2.2896 | -0.296 | 0.7671 |  |
| Education: high school or below (vs college) | +3.0029 | 1.7646 | ±3.5291 | +1.702 | 0.0888 | . |
| **Site: UCSD (vs UAB)** | **+2.9984** | 1.4446 | ±2.8893 | **+2.076** | **0.0379** | * |
| Site: UW (vs UAB) | +1.2538 | 1.1977 | ±2.3954 | +1.047 | 0.2952 |  |
| **Age (years)** | **-0.5229** | 0.0489 | ±0.0979 | **-10.683** | **1.22e-26** | *** |
| BMI (kg/m2) | -0.0513 | 0.0816 | ±0.1632 | -0.629 | 0.5294 |  |
| Hypertension | -1.1139 | 1.1670 | ±2.3340 | -0.955 | 0.3398 |  |
| High cholesterol | +0.9923 | 1.0880 | ±2.1759 | +0.912 | 0.3617 |  |
| Kidney disease | -2.5618 | 1.4682 | ±2.9364 | -1.745 | 0.0810 | . |
| **Circulatory disease** | **-3.7925** | 1.2742 | ±2.5484 | **-2.976** | **0.0029** | ** |
| Avg. daily range (mg/dL) | +0.0099 | 0.0159 | ±0.0319 | +0.619 | 0.5360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **690**, R² = **0.1884**, Adj R² = **0.1752**, F-statistic = **14.30** (p = **5.25e-25**), Residual SE = **13.494** on **678** df, AIC = **5561.1**, BIC = **5615.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2982** | 4.3285 | ±8.6571 | **+13.237** | **5.34e-40** | *** |
| Education: graduate level (vs college) | -0.1935 | 1.1669 | ±2.3339 | -0.166 | 0.8683 |  |
| Education: high school or below (vs college) | +3.0185 | 1.7500 | ±3.5001 | +1.725 | 0.0846 | . |
| **Site: UCSD (vs UAB)** | **+3.0105** | 1.4518 | ±2.9036 | **+2.074** | **0.0381** | * |
| Site: UW (vs UAB) | +1.3642 | 1.2037 | ±2.4075 | +1.133 | 0.2571 |  |
| **Age (years)** | **-0.5195** | 0.0486 | ±0.0971 | **-10.698** | **1.04e-26** | *** |
| BMI (kg/m2) | -0.0694 | 0.0825 | ±0.1650 | -0.841 | 0.4006 |  |
| Hypertension | -1.2401 | 1.1695 | ±2.3390 | -1.060 | 0.2890 |  |
| High cholesterol | +1.0181 | 1.0839 | ±2.1677 | +0.939 | 0.3476 |  |
| Kidney disease | -2.5142 | 1.4350 | ±2.8699 | -1.752 | 0.0798 | . |
| **Circulatory disease** | **-3.9380** | 1.2740 | ±2.5479 | **-3.091** | **0.0020** | ** |
| SD of daily means (mg/dL) | +0.1128 | 0.0741 | ±0.1481 | +1.523 | 0.1277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2483** | 5.1961 | ±10.3921 | **+11.595** | **4.37e-31** | *** |
| Education: graduate level (vs college) | -0.3204 | 1.1497 | ±2.2994 | -0.279 | 0.7805 |  |
| Education: high school or below (vs college) | +2.9538 | 1.7534 | ±3.5068 | +1.685 | 0.0921 | . |
| **Site: UCSD (vs UAB)** | **+3.0078** | 1.4432 | ±2.8864 | **+2.084** | **0.0371** | * |
| Site: UW (vs UAB) | +1.2484 | 1.1982 | ±2.3964 | +1.042 | 0.2974 |  |
| **Age (years)** | **-0.5229** | 0.0490 | ±0.0979 | **-10.678** | **1.28e-26** | *** |
| BMI (kg/m2) | -0.0630 | 0.0832 | ±0.1664 | -0.758 | 0.4487 |  |
| Hypertension | -1.1304 | 1.1677 | ±2.3354 | -0.968 | 0.3330 |  |
| High cholesterol | +0.9948 | 1.0896 | ±2.1792 | +0.913 | 0.3613 |  |
| Kidney disease | -2.4728 | 1.4389 | ±2.8777 | -1.719 | 0.0857 | . |
| **Circulatory disease** | **-3.8481** | 1.2756 | ±2.5512 | **-3.017** | **0.0026** | ** |
| Time in range 70-180, pooled (%) | -0.0204 | 0.0240 | ±0.0480 | -0.853 | 0.3939 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.07** (p = **1.38e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2222** | 5.2062 | ±10.4124 | **+11.567** | **6.03e-31** | *** |
| Education: graduate level (vs college) | -0.3270 | 1.1486 | ±2.2973 | -0.285 | 0.7759 |  |
| Education: high school or below (vs college) | +2.9527 | 1.7526 | ±3.5052 | +1.685 | 0.0920 | . |
| **Site: UCSD (vs UAB)** | **+3.0128** | 1.4418 | ±2.8837 | **+2.090** | **0.0367** | * |
| Site: UW (vs UAB) | +1.2474 | 1.1976 | ±2.3952 | +1.042 | 0.2976 |  |
| **Age (years)** | **-0.5232** | 0.0490 | ±0.0980 | **-10.674** | **1.35e-26** | *** |
| BMI (kg/m2) | -0.0629 | 0.0833 | ±0.1666 | -0.755 | 0.4504 |  |
| Hypertension | -1.1271 | 1.1674 | ±2.3347 | -0.966 | 0.3343 |  |
| High cholesterol | +0.9927 | 1.0896 | ±2.1791 | +0.911 | 0.3623 |  |
| Kidney disease | -2.4786 | 1.4399 | ±2.8797 | -1.721 | 0.0852 | . |
| **Circulatory disease** | **-3.8441** | 1.2761 | ±2.5521 | **-3.012** | **0.0026** | ** |
| Avg. daily time in range 70-180 (%) | -0.0199 | 0.0238 | ±0.0476 | -0.835 | 0.4038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1866**, Adj R² = **0.1734**, F-statistic = **14.14** (p = **1.06e-24**), Residual SE = **13.509** on **678** df, AIC = **5562.6**, BIC = **5617.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8970** | 4.4412 | ±8.8825 | **+13.261** | **3.88e-40** | *** |
| Education: graduate level (vs college) | -0.4128 | 1.1374 | ±2.2748 | -0.363 | 0.7166 |  |
| Education: high school or below (vs college) | +3.0260 | 1.7614 | ±3.5228 | +1.718 | 0.0858 | . |
| Site: UCSD (vs UAB) | +2.8142 | 1.4707 | ±2.9414 | +1.914 | 0.0557 | . |
| Site: UW (vs UAB) | +1.0618 | 1.2238 | ±2.4476 | +0.868 | 0.3856 |  |
| **Age (years)** | **-0.5247** | 0.0493 | ±0.0985 | **-10.653** | **1.68e-26** | *** |
| BMI (kg/m2) | -0.0484 | 0.0818 | ±0.1636 | -0.591 | 0.5543 |  |
| Hypertension | -1.0417 | 1.1668 | ±2.3337 | -0.893 | 0.3720 |  |
| High cholesterol | +0.8899 | 1.0816 | ±2.1631 | +0.823 | 0.4106 |  |
| Kidney disease | -2.3877 | 1.4250 | ±2.8499 | -1.676 | 0.0938 | . |
| **Circulatory disease** | **-3.6682** | 1.2787 | ±2.5573 | **-2.869** | **0.0041** | ** |
| Any reading < 54 during wear (0/1) | -1.4558 | 1.2208 | ±2.4416 | -1.192 | 0.2331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1864**, Adj R² = **0.1732**, F-statistic = **14.12** (p = **1.13e-24**), Residual SE = **13.510** on **678** df, AIC = **5562.8**, BIC = **5617.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6657** | 4.3744 | ±8.7489 | **+13.411** | **5.21e-41** | *** |
| Education: graduate level (vs college) | -0.4530 | 1.1395 | ±2.2790 | -0.398 | 0.6910 |  |
| Education: high school or below (vs college) | +3.0202 | 1.7671 | ±3.5341 | +1.709 | 0.0874 | . |
| Site: UCSD (vs UAB) | +2.8072 | 1.4669 | ±2.9338 | +1.914 | 0.0557 | . |
| Site: UW (vs UAB) | +1.0055 | 1.2228 | ±2.4456 | +0.822 | 0.4109 |  |
| **Age (years)** | **-0.5207** | 0.0488 | ±0.0977 | **-10.663** | **1.51e-26** | *** |
| BMI (kg/m2) | -0.0533 | 0.0815 | ±0.1630 | -0.654 | 0.5133 |  |
| Hypertension | -1.0967 | 1.1604 | ±2.3207 | -0.945 | 0.3446 |  |
| High cholesterol | +0.8617 | 1.0864 | ±2.1727 | +0.793 | 0.4277 |  |
| Kidney disease | -2.4050 | 1.4221 | ±2.8443 | -1.691 | 0.0908 | . |
| **Circulatory disease** | **-3.8098** | 1.2737 | ±2.5474 | **-2.991** | **0.0028** | ** |
| Time < 54 (%) | -0.9754 | 1.1328 | ±2.2657 | -0.861 | 0.3892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1875**, Adj R² = **0.1743**, F-statistic = **14.23** (p = **7.31e-25**), Residual SE = **13.501** on **678** df, AIC = **5561.8**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6815** | 4.3692 | ±8.7384 | **+13.431** | **3.99e-41** | *** |
| Education: graduate level (vs college) | -0.4629 | 1.1402 | ±2.2804 | -0.406 | 0.6848 |  |
| Education: high school or below (vs college) | +2.9822 | 1.7667 | ±3.5334 | +1.688 | 0.0914 | . |
| Site: UCSD (vs UAB) | +2.7688 | 1.4695 | ±2.9390 | +1.884 | 0.0595 | . |
| Site: UW (vs UAB) | +0.9402 | 1.2245 | ±2.4490 | +0.768 | 0.4426 |  |
| **Age (years)** | **-0.5204** | 0.0489 | ±0.0977 | **-10.651** | **1.73e-26** | *** |
| BMI (kg/m2) | -0.0518 | 0.0813 | ±0.1626 | -0.637 | 0.5240 |  |
| Hypertension | -1.0810 | 1.1592 | ±2.3183 | -0.933 | 0.3510 |  |
| High cholesterol | +0.8053 | 1.0862 | ±2.1724 | +0.741 | 0.4585 |  |
| Kidney disease | -2.3806 | 1.4212 | ±2.8423 | -1.675 | 0.0939 | . |
| **Circulatory disease** | **-3.8285** | 1.2730 | ±2.5461 | **-3.007** | **0.0026** | ** |
| Avg. daily time < 54 (%) | -1.4735 | 0.8642 | ±1.7283 | -1.705 | 0.0882 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1879**, Adj R² = **0.1748**, F-statistic = **14.26** (p = **6.19e-25**), Residual SE = **13.497** on **678** df, AIC = **5561.5**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7691** | 4.3579 | ±8.7158 | **+13.486** | **1.90e-41** | *** |
| Education: graduate level (vs college) | -0.5140 | 1.1344 | ±2.2688 | -0.453 | 0.6505 |  |
| Education: high school or below (vs college) | +3.0052 | 1.7674 | ±3.5347 | +1.700 | 0.0891 | . |
| Site: UCSD (vs UAB) | +2.7137 | 1.4659 | ±2.9318 | +1.851 | 0.0641 | . |
| Site: UW (vs UAB) | +0.9012 | 1.2218 | ±2.4436 | +0.738 | 0.4607 |  |
| **Age (years)** | **-0.5193** | 0.0488 | ±0.0975 | **-10.647** | **1.80e-26** | *** |
| BMI (kg/m2) | -0.0496 | 0.0813 | ±0.1626 | -0.610 | 0.5416 |  |
| Hypertension | -1.0399 | 1.1570 | ±2.3139 | -0.899 | 0.3688 |  |
| High cholesterol | +0.7597 | 1.0801 | ±2.1602 | +0.703 | 0.4818 |  |
| Kidney disease | -2.3603 | 1.4196 | ±2.8391 | -1.663 | 0.0964 | . |
| **Circulatory disease** | **-3.9001** | 1.2707 | ±2.5414 | **-3.069** | **0.0021** | ** |
| Time 54-69, pooled (%) | -0.8032 | 0.4391 | ±0.8783 | -1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **690**, R² = **0.1887**, Adj R² = **0.1755**, F-statistic = **14.33** (p = **4.61e-25**), Residual SE = **13.491** on **678** df, AIC = **5560.8**, BIC = **5615.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7132** | 4.3546 | ±8.7092 | **+13.483** | **1.97e-41** | *** |
| Education: graduate level (vs college) | -0.5264 | 1.1345 | ±2.2689 | -0.464 | 0.6426 |  |
| Education: high school or below (vs college) | +2.9799 | 1.7630 | ±3.5261 | +1.690 | 0.0910 | . |
| Site: UCSD (vs UAB) | +2.6885 | 1.4680 | ±2.9360 | +1.831 | 0.0670 | . |
| Site: UW (vs UAB) | +0.8563 | 1.2247 | ±2.4494 | +0.699 | 0.4844 |  |
| **Age (years)** | **-0.5183** | 0.0487 | ±0.0975 | **-10.634** | **2.08e-26** | *** |
| BMI (kg/m2) | -0.0487 | 0.0813 | ±0.1627 | -0.599 | 0.5492 |  |
| Hypertension | -1.0295 | 1.1568 | ±2.3136 | -0.890 | 0.3735 |  |
| High cholesterol | +0.7335 | 1.0775 | ±2.1550 | +0.681 | 0.4960 |  |
| Kidney disease | -2.3473 | 1.4194 | ±2.8389 | -1.654 | 0.0982 | . |
| **Circulatory disease** | **-3.9132** | 1.2723 | ±2.5446 | **-3.076** | **0.0021** | ** |
| **Avg. daily time 54-69 (%)** | **-0.8328** | 0.4057 | ±0.8113 | **-2.053** | **0.0401** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **690**, R² = **0.1882**, Adj R² = **0.1750**, F-statistic = **14.29** (p = **5.67e-25**), Residual SE = **13.496** on **678** df, AIC = **5561.3**, BIC = **5615.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8568** | 4.3683 | ±8.7365 | **+13.474** | **2.23e-41** | *** |
| Education: graduate level (vs college) | -0.5285 | 1.1370 | ±2.2740 | -0.465 | 0.6420 |  |
| Education: high school or below (vs college) | +2.9721 | 1.7676 | ±3.5351 | +1.681 | 0.0927 | . |
| Site: UCSD (vs UAB) | +2.6952 | 1.4702 | ±2.9404 | +1.833 | 0.0668 | . |
| Site: UW (vs UAB) | +0.8749 | 1.2252 | ±2.4504 | +0.714 | 0.4752 |  |
| **Age (years)** | **-0.5188** | 0.0488 | ±0.0975 | **-10.639** | **1.95e-26** | *** |
| BMI (kg/m2) | -0.0523 | 0.0812 | ±0.1623 | -0.645 | 0.5192 |  |
| Hypertension | -1.0532 | 1.1576 | ±2.3153 | -0.910 | 0.3629 |  |
| High cholesterol | +0.7448 | 1.0816 | ±2.1632 | +0.689 | 0.4911 |  |
| Kidney disease | -2.3801 | 1.4189 | ±2.8379 | -1.677 | 0.0935 | . |
| **Circulatory disease** | **-3.8994** | 1.2711 | ±2.5422 | **-3.068** | **0.0022** | ** |
| **Time < 70 (%)** | **-0.6094** | 0.2834 | ±0.5668 | **-2.151** | **0.0315** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **690**, R² = **0.1890**, Adj R² = **0.1759**, F-statistic = **14.37** (p = **4.01e-25**), Residual SE = **13.488** on **678** df, AIC = **5560.5**, BIC = **5615.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7764** | 4.3604 | ±8.7207 | **+13.480** | **2.06e-41** | *** |
| Education: graduate level (vs college) | -0.5322 | 1.1371 | ±2.2742 | -0.468 | 0.6397 |  |
| Education: high school or below (vs college) | +2.9501 | 1.7640 | ±3.5280 | +1.672 | 0.0945 | . |
| Site: UCSD (vs UAB) | +2.6729 | 1.4717 | ±2.9434 | +1.816 | 0.0693 | . |
| Site: UW (vs UAB) | +0.8292 | 1.2274 | ±2.4548 | +0.676 | 0.4993 |  |
| **Age (years)** | **-0.5182** | 0.0488 | ±0.0975 | **-10.630** | **2.16e-26** | *** |
| BMI (kg/m2) | -0.0501 | 0.0812 | ±0.1624 | -0.617 | 0.5370 |  |
| Hypertension | -1.0369 | 1.1573 | ±2.3146 | -0.896 | 0.3703 |  |
| High cholesterol | +0.7129 | 1.0799 | ±2.1598 | +0.660 | 0.5091 |  |
| Kidney disease | -2.3543 | 1.4188 | ±2.8376 | -1.659 | 0.0970 | . |
| **Circulatory disease** | **-3.9115** | 1.2724 | ±2.5448 | **-3.074** | **0.0021** | ** |
| **Avg. daily time < 70 (%)** | **-0.6528** | 0.2729 | ±0.5459 | **-2.392** | **0.0168** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1849**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **2.01e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.1027** | 5.8368 | ±11.6735 | **+10.126** | **4.24e-24** | *** |
| Education: graduate level (vs college) | -0.3523 | 1.1598 | ±2.3197 | -0.304 | 0.7613 |  |
| Education: high school or below (vs college) | +3.0795 | 1.7455 | ±3.4909 | +1.764 | 0.0777 | . |
| **Site: UCSD (vs UAB)** | **+2.9314** | 1.4482 | ±2.8964 | **+2.024** | **0.0429** | * |
| Site: UW (vs UAB) | +1.1713 | 1.1988 | ±2.3977 | +0.977 | 0.3286 |  |
| **Age (years)** | **-0.5220** | 0.0485 | ±0.0969 | **-10.769** | **4.80e-27** | *** |
| BMI (kg/m2) | -0.0507 | 0.0824 | ±0.1648 | -0.615 | 0.5384 |  |
| Hypertension | -1.1070 | 1.1649 | ±2.3298 | -0.950 | 0.3419 |  |
| High cholesterol | +0.9730 | 1.0918 | ±2.1837 | +0.891 | 0.3729 |  |
| Kidney disease | -2.3979 | 1.4340 | ±2.8679 | -1.672 | 0.0945 | . |
| **Circulatory disease** | **-3.7741** | 1.2800 | ±2.5601 | **-2.948** | **0.0032** | ** |
| Time 54-250, pooled (%) | -0.0080 | 0.0361 | ±0.0722 | -0.223 | 0.8239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **1.99e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.2591** | 5.8030 | ±11.6060 | **+10.212** | **1.76e-24** | *** |
| Education: graduate level (vs college) | -0.3486 | 1.1597 | ±2.3194 | -0.301 | 0.7637 |  |
| Education: high school or below (vs college) | +3.0734 | 1.7470 | ±3.4941 | +1.759 | 0.0785 | . |
| **Site: UCSD (vs UAB)** | **+2.9350** | 1.4480 | ±2.8961 | **+2.027** | **0.0427** | * |
| Site: UW (vs UAB) | +1.1756 | 1.1995 | ±2.3990 | +0.980 | 0.3270 |  |
| **Age (years)** | **-0.5219** | 0.0485 | ±0.0971 | **-10.753** | **5.72e-27** | *** |
| BMI (kg/m2) | -0.0512 | 0.0823 | ±0.1646 | -0.622 | 0.5342 |  |
| Hypertension | -1.1077 | 1.1648 | ±2.3295 | -0.951 | 0.3416 |  |
| High cholesterol | +0.9745 | 1.0914 | ±2.1829 | +0.893 | 0.3719 |  |
| Kidney disease | -2.4037 | 1.4351 | ±2.8702 | -1.675 | 0.0939 | . |
| **Circulatory disease** | **-3.7787** | 1.2795 | ±2.5590 | **-2.953** | **0.0031** | ** |
| Avg. daily time 54-250 (%) | -0.0096 | 0.0354 | ±0.0709 | -0.271 | 0.7864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1873**, Adj R² = **0.1741**, F-statistic = **14.20** (p = **8.02e-25**), Residual SE = **13.503** on **678** df, AIC = **5562.0**, BIC = **5616.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4441** | 4.3687 | ±8.7374 | **+13.378** | **8.15e-41** | *** |
| Education: graduate level (vs college) | -0.4008 | 1.1338 | ±2.2677 | -0.353 | 0.7237 |  |
| Education: high school or below (vs college) | +2.9338 | 1.7741 | ±3.5482 | +1.654 | 0.0982 | . |
| **Site: UCSD (vs UAB)** | **+3.0267** | 1.4518 | ±2.9035 | **+2.085** | **0.0371** | * |
| Site: UW (vs UAB) | +1.1961 | 1.2118 | ±2.4237 | +0.987 | 0.3236 |  |
| **Age (years)** | **-0.5288** | 0.0497 | ±0.0993 | **-10.650** | **1.75e-26** | *** |
| BMI (kg/m2) | -0.0715 | 0.0824 | ±0.1648 | -0.867 | 0.3858 |  |
| Hypertension | -1.1158 | 1.1648 | ±2.3297 | -0.958 | 0.3381 |  |
| High cholesterol | +0.9740 | 1.0869 | ±2.1738 | +0.896 | 0.3702 |  |
| Kidney disease | -2.5047 | 1.4312 | ±2.8623 | -1.750 | 0.0801 | . |
| **Circulatory disease** | **-3.8765** | 1.2709 | ±2.5418 | **-3.050** | **0.0023** | ** |
| Time 181-250, pooled (%) | +0.0514 | 0.0378 | ±0.0756 | +1.358 | 0.1745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **690**, R² = **0.1870**, Adj R² = **0.1739**, F-statistic = **14.18** (p = **8.81e-25**), Residual SE = **13.505** on **678** df, AIC = **5562.2**, BIC = **5616.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4292** | 4.3696 | ±8.7392 | **+13.372** | **8.84e-41** | *** |
| Education: graduate level (vs college) | -0.4060 | 1.1340 | ±2.2680 | -0.358 | 0.7203 |  |
| Education: high school or below (vs college) | +2.9268 | 1.7695 | ±3.5390 | +1.654 | 0.0981 | . |
| **Site: UCSD (vs UAB)** | **+3.0348** | 1.4501 | ±2.9003 | **+2.093** | **0.0364** | * |
| Site: UW (vs UAB) | +1.2038 | 1.2103 | ±2.4207 | +0.995 | 0.3199 |  |
| **Age (years)** | **-0.5281** | 0.0497 | ±0.0993 | **-10.636** | **2.02e-26** | *** |
| BMI (kg/m2) | -0.0702 | 0.0828 | ±0.1656 | -0.848 | 0.3964 |  |
| Hypertension | -1.1145 | 1.1651 | ±2.3302 | -0.957 | 0.3388 |  |
| High cholesterol | +0.9694 | 1.0875 | ±2.1751 | +0.891 | 0.3727 |  |
| Kidney disease | -2.5029 | 1.4318 | ±2.8636 | -1.748 | 0.0804 | . |
| **Circulatory disease** | **-3.8603** | 1.2731 | ±2.5463 | **-3.032** | **0.0024** | ** |
| Avg. daily time 181-250 (%) | +0.0478 | 0.0371 | ±0.0742 | +1.287 | 0.1980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **690**, R² = **0.1862**, Adj R² = **0.1729**, F-statistic = **14.10** (p = **1.25e-24**), Residual SE = **13.512** on **678** df, AIC = **5563.0**, BIC = **5617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2071** | 4.3380 | ±8.6759 | **+13.418** | **4.74e-41** | *** |
| Education: graduate level (vs college) | -0.3212 | 1.1480 | ±2.2961 | -0.280 | 0.7797 |  |
| Education: high school or below (vs college) | +2.9348 | 1.7534 | ±3.5069 | +1.674 | 0.0942 | . |
| **Site: UCSD (vs UAB)** | **+3.0078** | 1.4443 | ±2.8887 | **+2.082** | **0.0373** | * |
| Site: UW (vs UAB) | +1.2480 | 1.1993 | ±2.3985 | +1.041 | 0.2980 |  |
| **Age (years)** | **-0.5228** | 0.0489 | ±0.0979 | **-10.682** | **1.24e-26** | *** |
| BMI (kg/m2) | -0.0644 | 0.0832 | ±0.1664 | -0.774 | 0.4388 |  |
| Hypertension | -1.1315 | 1.1674 | ±2.3349 | -0.969 | 0.3324 |  |
| High cholesterol | +0.9893 | 1.0891 | ±2.1782 | +0.908 | 0.3637 |  |
| Kidney disease | -2.4805 | 1.4383 | ±2.8766 | -1.725 | 0.0846 | . |
| **Circulatory disease** | **-3.8613** | 1.2756 | ±2.5512 | **-3.027** | **0.0025** | ** |
| Time > 180 (%) | +0.0222 | 0.0238 | ±0.0475 | +0.933 | 0.3507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1861**, Adj R² = **0.1729**, F-statistic = **14.10** (p = **1.25e-24**), Residual SE = **13.512** on **678** df, AIC = **5563.0**, BIC = **5617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2340** | 4.3423 | ±8.6846 | **+13.411** | **5.23e-41** | *** |
| Education: graduate level (vs college) | -0.3269 | 1.1471 | ±2.2942 | -0.285 | 0.7756 |  |
| Education: high school or below (vs college) | +2.9295 | 1.7523 | ±3.5047 | +1.672 | 0.0946 | . |
| **Site: UCSD (vs UAB)** | **+3.0152** | 1.4429 | ±2.8858 | **+2.090** | **0.0366** | * |
| Site: UW (vs UAB) | +1.2486 | 1.1987 | ±2.3975 | +1.042 | 0.2976 |  |
| **Age (years)** | **-0.5230** | 0.0490 | ±0.0980 | **-10.677** | **1.30e-26** | *** |
| BMI (kg/m2) | -0.0645 | 0.0833 | ±0.1666 | -0.774 | 0.4388 |  |
| Hypertension | -1.1282 | 1.1670 | ±2.3341 | -0.967 | 0.3337 |  |
| High cholesterol | +0.9872 | 1.0890 | ±2.1780 | +0.906 | 0.3647 |  |
| Kidney disease | -2.4881 | 1.4392 | ±2.8784 | -1.729 | 0.0838 | . |
| **Circulatory disease** | **-3.8589** | 1.2762 | ±2.5523 | **-3.024** | **0.0025** | ** |
| Avg. daily time > 180 (%) | +0.0220 | 0.0236 | ±0.0473 | +0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1866**, Adj R² = **0.1734**, F-statistic = **14.14** (p = **1.04e-24**), Residual SE = **13.508** on **678** df, AIC = **5562.6**, BIC = **5617.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2983** | 4.3610 | ±8.7219 | **+13.368** | **9.28e-41** | *** |
| Education: graduate level (vs college) | -0.2700 | 1.1594 | ±2.3187 | -0.233 | 0.8159 |  |
| Education: high school or below (vs college) | +2.9409 | 1.7508 | ±3.5016 | +1.680 | 0.0930 | . |
| **Site: UCSD (vs UAB)** | **+3.0293** | 1.4418 | ±2.8836 | **+2.101** | **0.0356** | * |
| Site: UW (vs UAB) | +1.2391 | 1.2007 | ±2.4013 | +1.032 | 0.3020 |  |
| **Age (years)** | **-0.5203** | 0.0487 | ±0.0974 | **-10.684** | **1.21e-26** | *** |
| BMI (kg/m2) | -0.0707 | 0.0832 | ±0.1663 | -0.850 | 0.3956 |  |
| Hypertension | -1.1285 | 1.1664 | ±2.3328 | -0.968 | 0.3333 |  |
| High cholesterol | +1.0211 | 1.0908 | ±2.1815 | +0.936 | 0.3492 |  |
| Kidney disease | -2.4402 | 1.4356 | ±2.8712 | -1.700 | 0.0892 | . |
| **Circulatory disease** | **-3.8728** | 1.2745 | ±2.5489 | **-3.039** | **0.0024** | ** |
| Nocturnal time > 180 (%) | +0.0237 | 0.0221 | ±0.0441 | +1.075 | 0.2822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **1.99e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2893** | 4.3268 | ±8.6536 | **+13.472** | **2.29e-41** | *** |
| Education: graduate level (vs college) | -0.3489 | 1.1590 | ±2.3180 | -0.301 | 0.7634 |  |
| Education: high school or below (vs college) | +3.0726 | 1.7451 | ±3.4902 | +1.761 | 0.0783 | . |
| **Site: UCSD (vs UAB)** | **+2.9333** | 1.4486 | ±2.8973 | **+2.025** | **0.0429** | * |
| Site: UW (vs UAB) | +1.1752 | 1.1991 | ±2.3981 | +0.980 | 0.3270 |  |
| **Age (years)** | **-0.5218** | 0.0485 | ±0.0969 | **-10.768** | **4.86e-27** | *** |
| BMI (kg/m2) | -0.0511 | 0.0824 | ±0.1649 | -0.620 | 0.5354 |  |
| Hypertension | -1.1086 | 1.1649 | ±2.3298 | -0.952 | 0.3413 |  |
| High cholesterol | +0.9734 | 1.0914 | ±2.1828 | +0.892 | 0.3725 |  |
| Kidney disease | -2.4009 | 1.4341 | ±2.8682 | -1.674 | 0.0941 | . |
| **Circulatory disease** | **-3.7778** | 1.2801 | ±2.5602 | **-2.951** | **0.0032** | ** |
| Time > 250 (%) | +0.0094 | 0.0361 | ±0.0723 | +0.259 | 0.7953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1718**, F-statistic = **13.99** (p = **1.96e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2887** | 4.3338 | ±8.6676 | **+13.450** | **3.09e-41** | *** |
| Education: graduate level (vs college) | -0.3446 | 1.1590 | ±2.3180 | -0.297 | 0.7662 |  |
| Education: high school or below (vs college) | +3.0655 | 1.7467 | ±3.4935 | +1.755 | 0.0793 | . |
| **Site: UCSD (vs UAB)** | **+2.9373** | 1.4484 | ±2.8968 | **+2.028** | **0.0426** | * |
| Site: UW (vs UAB) | +1.1800 | 1.1998 | ±2.3995 | +0.984 | 0.3253 |  |
| **Age (years)** | **-0.5218** | 0.0485 | ±0.0971 | **-10.752** | **5.83e-27** | *** |
| BMI (kg/m2) | -0.0516 | 0.0823 | ±0.1646 | -0.627 | 0.5307 |  |
| Hypertension | -1.1092 | 1.1647 | ±2.3294 | -0.952 | 0.3409 |  |
| High cholesterol | +0.9750 | 1.0910 | ±2.1820 | +0.894 | 0.3715 |  |
| Kidney disease | -2.4073 | 1.4351 | ±2.8702 | -1.677 | 0.0935 | . |
| **Circulatory disease** | **-3.7832** | 1.2796 | ±2.5591 | **-2.957** | **0.0031** | ** |
| Avg. daily time > 250 (%) | +0.0112 | 0.0355 | ±0.0710 | +0.315 | 0.7528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 692; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **692**, R² = **0.1495**, Adj R² = **0.1371**, F-statistic = **11.97** (p = **3.43e-19**), Residual SE = **8.427** on **681** df, AIC = **4924.7**, BIC = **4974.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.6611** | 2.7711 | ±5.5422 | **+25.499** | **2.00e-143** | *** |
| Education: graduate level (vs college) | -0.8187 | 0.7236 | ±1.4472 | -1.131 | 0.2579 |  |
| **Education: high school or below (vs college)** | **+2.4427** | 0.9751 | ±1.9501 | **+2.505** | **0.0122** | * |
| Site: UCSD (vs UAB) | -1.1672 | 0.8975 | ±1.7951 | -1.300 | 0.1935 |  |
| Site: UW (vs UAB) | -0.9820 | 0.7917 | ±1.5835 | -1.240 | 0.2148 |  |
| **Age (years)** | **-0.2068** | 0.0317 | ±0.0634 | **-6.518** | **7.14e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0497 | ±0.0994 | **+4.337** | **1.45e-05** | *** |
| Hypertension | +0.5415 | 0.7341 | ±1.4682 | +0.738 | 0.4608 |  |
| High cholesterol | +0.6128 | 0.7107 | ±1.4214 | +0.862 | 0.3886 |  |
| Kidney disease | +0.1586 | 0.9577 | ±1.9154 | +0.166 | 0.8685 |  |
| Circulatory disease | -0.3380 | 0.8512 | ±1.7024 | -0.397 | 0.6913 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **692**, R² = **0.1814**, Adj R² = **0.1682**, F-statistic = **13.70** (p = **6.61e-24**), Residual SE = **8.274** on **680** df, AIC = **4900.2**, BIC = **4954.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5088** | 3.1417 | ±6.2833 | **+20.215** | **7.22e-91** | *** |
| Education: graduate level (vs college) | -0.5201 | 0.7191 | ±1.4383 | -0.723 | 0.4695 |  |
| Education: high school or below (vs college) | +1.8275 | 0.9573 | ±1.9146 | +1.909 | 0.0563 | . |
| Site: UCSD (vs UAB) | -1.0529 | 0.8920 | ±1.7840 | -1.180 | 0.2379 |  |
| Site: UW (vs UAB) | -0.6675 | 0.7844 | ±1.5689 | -0.851 | 0.3948 |  |
| **Age (years)** | **-0.2051** | 0.0311 | ±0.0622 | **-6.593** | **4.31e-11** | *** |
| **BMI (kg/m2)** | **+0.1692** | 0.0510 | ±0.1019 | **+3.320** | **9.00e-04** | *** |
| Hypertension | +0.3259 | 0.7226 | ±1.4453 | +0.451 | 0.6520 |  |
| High cholesterol | +0.5543 | 0.7037 | ±1.4075 | +0.788 | 0.4309 |  |
| Kidney disease | +0.2162 | 0.9544 | ±1.9087 | +0.227 | 0.8208 |  |
| Circulatory disease | -0.4929 | 0.8418 | ±1.6836 | -0.586 | 0.5582 |  |
| **HbA1c (%)** | **+1.2497** | 0.2375 | ±0.4750 | **+5.262** | **1.43e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **692**, R² = **0.1856**, Adj R² = **0.1724**, F-statistic = **14.09** (p = **1.29e-24**), Residual SE = **8.253** on **680** df, AIC = **4896.7**, BIC = **4951.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.5039** | 3.0427 | ±6.0855 | **+21.199** | **9.71e-100** | *** |
| Education: graduate level (vs college) | -0.6400 | 0.7124 | ±1.4248 | -0.898 | 0.3690 |  |
| Education: high school or below (vs college) | +1.8142 | 0.9526 | ±1.9051 | +1.905 | 0.0568 | . |
| Site: UCSD (vs UAB) | -0.9541 | 0.8901 | ±1.7801 | -1.072 | 0.2837 |  |
| Site: UW (vs UAB) | -0.6778 | 0.7800 | ±1.5599 | -0.869 | 0.3848 |  |
| **Age (years)** | **-0.2024** | 0.0308 | ±0.0615 | **-6.580** | **4.72e-11** | *** |
| **BMI (kg/m2)** | **+0.1725** | 0.0506 | ±0.1011 | **+3.412** | **6.44e-04** | *** |
| Hypertension | +0.3775 | 0.7220 | ±1.4439 | +0.523 | 0.6011 |  |
| High cholesterol | +0.6541 | 0.7005 | ±1.4009 | +0.934 | 0.3504 |  |
| Kidney disease | -0.0628 | 0.9491 | ±1.8981 | -0.066 | 0.9472 |  |
| Circulatory disease | -0.6870 | 0.8398 | ±1.6796 | -0.818 | 0.4133 |  |
| **Mean glucose (mg/dL)** | **+0.0447** | 0.0087 | ±0.0174 | **+5.137** | **2.79e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **692**, R² = **0.1856**, Adj R² = **0.1724**, F-statistic = **14.09** (p = **1.29e-24**), Residual SE = **8.253** on **680** df, AIC = **4896.7**, BIC = **4951.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3157** | 3.7405 | ±7.4809 | **+15.590** | **8.45e-55** | *** |
| Education: graduate level (vs college) | -0.6400 | 0.7124 | ±1.4248 | -0.898 | 0.3690 |  |
| Education: high school or below (vs college) | +1.8142 | 0.9526 | ±1.9051 | +1.905 | 0.0568 | . |
| Site: UCSD (vs UAB) | -0.9541 | 0.8901 | ±1.7801 | -1.072 | 0.2837 |  |
| Site: UW (vs UAB) | -0.6778 | 0.7800 | ±1.5599 | -0.869 | 0.3848 |  |
| **Age (years)** | **-0.2024** | 0.0308 | ±0.0615 | **-6.580** | **4.72e-11** | *** |
| **BMI (kg/m2)** | **+0.1725** | 0.0506 | ±0.1011 | **+3.412** | **6.44e-04** | *** |
| Hypertension | +0.3775 | 0.7220 | ±1.4439 | +0.523 | 0.6011 |  |
| High cholesterol | +0.6541 | 0.7005 | ±1.4009 | +0.934 | 0.3504 |  |
| Kidney disease | -0.0628 | 0.9491 | ±1.8981 | -0.066 | 0.9472 |  |
| Circulatory disease | -0.6870 | 0.8398 | ±1.6796 | -0.818 | 0.4133 |  |
| **GMI (%)** | **+1.8695** | 0.3639 | ±0.7279 | **+5.137** | **2.79e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **692**, R² = **0.1803**, Adj R² = **0.1671**, F-statistic = **13.60** (p = **1.00e-23**), Residual SE = **8.279** on **680** df, AIC = **4901.1**, BIC = **4955.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.4858** | 3.0047 | ±6.0094 | **+21.795** | **2.61e-105** | *** |
| Education: graduate level (vs college) | -0.6094 | 0.7195 | ±1.4390 | -0.847 | 0.3970 |  |
| **Education: high school or below (vs college)** | **+1.9125** | 0.9441 | ±1.8882 | **+2.026** | **0.0428** | * |
| Site: UCSD (vs UAB) | -0.9858 | 0.8936 | ±1.7871 | -1.103 | 0.2699 |  |
| Site: UW (vs UAB) | -0.7904 | 0.7798 | ±1.5595 | -1.014 | 0.3107 |  |
| **Age (years)** | **-0.1976** | 0.0311 | ±0.0623 | **-6.346** | **2.21e-10** | *** |
| **BMI (kg/m2)** | **+0.1664** | 0.0509 | ±0.1017 | **+3.272** | **0.0011** | ** |
| Hypertension | +0.4208 | 0.7243 | ±1.4485 | +0.581 | 0.5613 |  |
| High cholesterol | +0.6844 | 0.7051 | ±1.4101 | +0.971 | 0.3317 |  |
| Kidney disease | +0.1381 | 0.9477 | ±1.8953 | +0.146 | 0.8841 |  |
| Circulatory disease | -0.6507 | 0.8405 | ±1.6810 | -0.774 | 0.4389 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0392** | 0.0082 | ±0.0164 | **+4.785** | **1.71e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1682**, Adj R² = **0.1548**, F-statistic = **12.50** (p = **1.09e-21**), Residual SE = **8.340** on **680** df, AIC = **4911.3**, BIC = **4965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3490** | 2.8961 | ±5.7922 | **+23.255** | **1.26e-119** | *** |
| Education: graduate level (vs college) | -0.6301 | 0.7197 | ±1.4393 | -0.876 | 0.3812 |  |
| **Education: high school or below (vs college)** | **+2.0102** | 0.9766 | ±1.9533 | **+2.058** | **0.0396** | * |
| Site: UCSD (vs UAB) | -0.9465 | 0.8982 | ±1.7965 | -1.054 | 0.2920 |  |
| Site: UW (vs UAB) | -0.5554 | 0.7958 | ±1.5916 | -0.698 | 0.4853 |  |
| **Age (years)** | **-0.2094** | 0.0310 | ±0.0619 | **-6.761** | **1.37e-11** | *** |
| **BMI (kg/m2)** | **+0.1930** | 0.0507 | ±0.1014 | **+3.809** | **1.40e-04** | *** |
| Hypertension | +0.3464 | 0.7353 | ±1.4706 | +0.471 | 0.6376 |  |
| High cholesterol | +0.7355 | 0.7086 | ±1.4172 | +1.038 | 0.2993 |  |
| Kidney disease | -0.4803 | 0.9678 | ±1.9356 | -0.496 | 0.6197 |  |
| Circulatory disease | -0.5179 | 0.8485 | ±1.6970 | -0.610 | 0.5416 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1085** | 0.0308 | ±0.0616 | **+3.523** | **4.26e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1649**, Adj R² = **0.1514**, F-statistic = **12.20** (p = **3.92e-21**), Residual SE = **8.357** on **680** df, AIC = **4914.1**, BIC = **4968.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5402** | 2.9020 | ±5.8039 | **+23.274** | **8.14e-120** | *** |
| Education: graduate level (vs college) | -0.6781 | 0.7180 | ±1.4360 | -0.944 | 0.3449 |  |
| **Education: high school or below (vs college)** | **+2.0139** | 0.9839 | ±1.9678 | **+2.047** | **0.0407** | * |
| Site: UCSD (vs UAB) | -0.9644 | 0.8990 | ±1.7981 | -1.073 | 0.2834 |  |
| Site: UW (vs UAB) | -0.6273 | 0.7966 | ±1.5931 | -0.788 | 0.4310 |  |
| **Age (years)** | **-0.2106** | 0.0311 | ±0.0622 | **-6.773** | **1.26e-11** | *** |
| **BMI (kg/m2)** | **+0.2009** | 0.0503 | ±0.1007 | **+3.990** | **6.60e-05** | *** |
| Hypertension | +0.3761 | 0.7356 | ±1.4712 | +0.511 | 0.6092 |  |
| High cholesterol | +0.7132 | 0.7083 | ±1.4165 | +1.007 | 0.3139 |  |
| Kidney disease | -0.4679 | 0.9783 | ±1.9567 | -0.478 | 0.6325 |  |
| Circulatory disease | -0.4868 | 0.8465 | ±1.6930 | -0.575 | 0.5653 |  |
| **Avg. daily SD (mg/dL)** | **+0.1117** | 0.0346 | ±0.0693 | **+3.224** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.6**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8456** | 3.0576 | ±6.1152 | **+23.170** | **9.09e-119** | *** |
| Education: graduate level (vs college) | -0.8238 | 0.7245 | ±1.4490 | -1.137 | 0.2555 |  |
| **Education: high school or below (vs college)** | **+2.4475** | 0.9789 | ±1.9578 | **+2.500** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1741 | 0.9025 | ±1.8050 | -1.301 | 0.1933 |  |
| Site: UW (vs UAB) | -0.9950 | 0.8039 | ±1.6079 | -1.238 | 0.2158 |  |
| **Age (years)** | **-0.2065** | 0.0319 | ±0.0638 | **-6.475** | **9.45e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0498 | ±0.0995 | **+4.329** | **1.49e-05** | *** |
| Hypertension | +0.5467 | 0.7399 | ±1.4799 | +0.739 | 0.4600 |  |
| High cholesterol | +0.6072 | 0.7159 | ±1.4317 | +0.848 | 0.3963 |  |
| Kidney disease | +0.1825 | 0.9871 | ±1.9742 | +0.185 | 0.8534 |  |
| Circulatory disease | -0.3388 | 0.8519 | ±1.7037 | -0.398 | 0.6909 |  |
| CV (%) | -0.0082 | 0.0607 | ±0.1214 | -0.136 | 0.8921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.7**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8317** | 3.2219 | ±6.4439 | **+21.984** | **4.09e-107** | *** |
| Education: graduate level (vs college) | -0.8153 | 0.7239 | ±1.4478 | -1.126 | 0.2601 |  |
| **Education: high school or below (vs college)** | **+2.4393** | 0.9798 | ±1.9596 | **+2.490** | **0.0128** | * |
| Site: UCSD (vs UAB) | -1.1639 | 0.8998 | ±1.7995 | -1.294 | 0.1958 |  |
| Site: UW (vs UAB) | -0.9731 | 0.8017 | ±1.6034 | -1.214 | 0.2248 |  |
| **Age (years)** | **-0.2069** | 0.0318 | ±0.0636 | **-6.505** | **7.78e-11** | *** |
| **BMI (kg/m2)** | **+0.2156** | 0.0498 | ±0.0996 | **+4.331** | **1.48e-05** | *** |
| Hypertension | +0.5371 | 0.7395 | ±1.4789 | +0.726 | 0.4676 |  |
| High cholesterol | +0.6150 | 0.7126 | ±1.4252 | +0.863 | 0.3881 |  |
| Kidney disease | +0.1413 | 0.9747 | ±1.9493 | +0.145 | 0.8847 |  |
| Circulatory disease | -0.3391 | 0.8525 | ±1.7049 | -0.398 | 0.6908 |  |
| Mean / SD ratio | -0.0369 | 0.3363 | ±0.6725 | -0.110 | 0.9125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.6**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.4394** | 3.1779 | ±6.3559 | **+22.165** | **7.45e-109** | *** |
| Education: graduate level (vs college) | -0.8223 | 0.7234 | ±1.4467 | -1.137 | 0.2556 |  |
| **Education: high school or below (vs college)** | **+2.4479** | 0.9793 | ±1.9586 | **+2.500** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1706 | 0.8999 | ±1.7997 | -1.301 | 0.1933 |  |
| Site: UW (vs UAB) | -0.9930 | 0.7994 | ±1.5989 | -1.242 | 0.2142 |  |
| **Age (years)** | **-0.2064** | 0.0319 | ±0.0638 | **-6.473** | **9.62e-11** | *** |
| **BMI (kg/m2)** | **+0.2151** | 0.0497 | ±0.0994 | **+4.327** | **1.51e-05** | *** |
| Hypertension | +0.5475 | 0.7392 | ±1.4784 | +0.741 | 0.4589 |  |
| High cholesterol | +0.6089 | 0.7128 | ±1.4257 | +0.854 | 0.3930 |  |
| Kidney disease | +0.1811 | 0.9767 | ±1.9534 | +0.185 | 0.8529 |  |
| Circulatory disease | -0.3384 | 0.8519 | ±1.7037 | -0.397 | 0.6912 |  |
| Avg. daily mean/SD | +0.0412 | 0.2632 | ±0.5264 | +0.157 | 0.8755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **692**, R² = **0.1566**, Adj R² = **0.1429**, F-statistic = **11.47** (p = **9.02e-20**), Residual SE = **8.399** on **680** df, AIC = **4920.9**, BIC = **4975.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4568** | 3.4299 | ±6.8599 | **+19.375** | **1.24e-83** | *** |
| Education: graduate level (vs college) | -0.6935 | 0.7236 | ±1.4472 | -0.958 | 0.3379 |  |
| **Education: high school or below (vs college)** | **+2.3273** | 0.9693 | ±1.9386 | **+2.401** | **0.0164** | * |
| Site: UCSD (vs UAB) | -0.9844 | 0.9057 | ±1.8113 | -1.087 | 0.2771 |  |
| Site: UW (vs UAB) | -0.6703 | 0.8143 | ±1.6286 | -0.823 | 0.4104 |  |
| **Age (years)** | **-0.2010** | 0.0316 | ±0.0632 | **-6.363** | **1.98e-10** | *** |
| **BMI (kg/m2)** | **+0.2130** | 0.0500 | ±0.1000 | **+4.258** | **2.06e-05** | *** |
| Hypertension | +0.5763 | 0.7337 | ±1.4673 | +0.786 | 0.4321 |  |
| High cholesterol | +0.7308 | 0.7145 | ±1.4289 | +1.023 | 0.3064 |  |
| Kidney disease | -0.0151 | 0.9710 | ±1.9421 | -0.016 | 0.9876 |  |
| Circulatory disease | -0.3585 | 0.8477 | ±1.6953 | -0.423 | 0.6724 |  |
| **MAG (mg/dL/h)** | **+0.0811** | 0.0364 | ±0.0728 | **+2.228** | **0.0259** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **692**, R² = **0.1604**, Adj R² = **0.1468**, F-statistic = **11.81** (p = **2.14e-20**), Residual SE = **8.380** on **680** df, AIC = **4917.8**, BIC = **4972.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.5804** | 3.1023 | ±6.2045 | **+21.462** | **3.54e-102** | *** |
| Education: graduate level (vs college) | -0.7091 | 0.7204 | ±1.4408 | -0.984 | 0.3250 |  |
| **Education: high school or below (vs college)** | **+2.0805** | 0.9818 | ±1.9635 | **+2.119** | **0.0341** | * |
| Site: UCSD (vs UAB) | -0.9517 | 0.9003 | ±1.8007 | -1.057 | 0.2905 |  |
| Site: UW (vs UAB) | -0.6652 | 0.8015 | ±1.6030 | -0.830 | 0.4066 |  |
| **Age (years)** | **-0.2064** | 0.0313 | ±0.0626 | **-6.593** | **4.32e-11** | *** |
| **BMI (kg/m2)** | **+0.2083** | 0.0501 | ±0.1002 | **+4.157** | **3.23e-05** | *** |
| Hypertension | +0.4782 | 0.7331 | ±1.4663 | +0.652 | 0.5142 |  |
| High cholesterol | +0.7080 | 0.7106 | ±1.4212 | +0.996 | 0.3191 |  |
| Kidney disease | -0.3614 | 0.9826 | ±1.9652 | -0.368 | 0.7131 |  |
| Circulatory disease | -0.4505 | 0.8470 | ±1.6940 | -0.532 | 0.5948 |  |
| **Avg. daily range (mg/dL)** | **+0.0278** | 0.0098 | ±0.0195 | **+2.845** | **0.0044** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **692**, R² = **0.1767**, Adj R² = **0.1634**, F-statistic = **13.27** (p = **4.19e-23**), Residual SE = **8.298** on **680** df, AIC = **4904.2**, BIC = **4958.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.7937** | 2.7763 | ±5.5526 | **+24.779** | **1.51e-135** | *** |
| Education: graduate level (vs college) | -0.5093 | 0.7246 | ±1.4493 | -0.703 | 0.4822 |  |
| **Education: high school or below (vs college)** | **+2.2176** | 0.9520 | ±1.9041 | **+2.329** | **0.0198** | * |
| Site: UCSD (vs UAB) | -1.0390 | 0.8945 | ±1.7891 | -1.162 | 0.2454 |  |
| Site: UW (vs UAB) | -0.6018 | 0.7856 | ±1.5713 | -0.766 | 0.4437 |  |
| **Age (years)** | **-0.2004** | 0.0311 | ±0.0622 | **-6.446** | **1.15e-10** | *** |
| **BMI (kg/m2)** | **+0.1810** | 0.0500 | ±0.1000 | **+3.619** | **2.96e-04** | *** |
| Hypertension | +0.2772 | 0.7316 | ±1.4632 | +0.379 | 0.7047 |  |
| High cholesterol | +0.7285 | 0.7101 | ±1.4203 | +1.026 | 0.3049 |  |
| Kidney disease | -0.0624 | 0.9411 | ±1.8823 | -0.066 | 0.9471 |  |
| Circulatory disease | -0.6397 | 0.8496 | ±1.6992 | -0.753 | 0.4515 |  |
| **SD of daily means (mg/dL)** | **+0.1910** | 0.0439 | ±0.0878 | **+4.347** | **1.38e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **692**, R² = **0.1883**, Adj R² = **0.1751**, F-statistic = **14.34** (p = **4.49e-25**), Residual SE = **8.239** on **680** df, AIC = **4894.4**, BIC = **4948.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.4612** | 2.9896 | ±5.9792 | **+25.910** | **5.09e-148** | *** |
| Education: graduate level (vs college) | -0.6123 | 0.7131 | ±1.4262 | -0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.7914 | 0.9515 | ±1.9030 | +1.883 | 0.0597 | . |
| Site: UCSD (vs UAB) | -0.8487 | 0.8912 | ±1.7825 | -0.952 | 0.3409 |  |
| Site: UW (vs UAB) | -0.5797 | 0.7806 | ±1.5613 | -0.743 | 0.4577 |  |
| **Age (years)** | **-0.2062** | 0.0308 | ±0.0616 | **-6.696** | **2.14e-11** | *** |
| **BMI (kg/m2)** | **+0.1640** | 0.0508 | ±0.1016 | **+3.230** | **0.0012** | ** |
| Hypertension | +0.3999 | 0.7245 | ±1.4489 | +0.552 | 0.5809 |  |
| High cholesterol | +0.7469 | 0.7027 | ±1.4054 | +1.063 | 0.2878 |  |
| Kidney disease | -0.1814 | 0.9478 | ±1.8955 | -0.191 | 0.8482 |  |
| Circulatory disease | -0.6809 | 0.8354 | ±1.6709 | -0.815 | 0.4150 |  |
| **Time in range 70-180, pooled (%)** | **-0.0748** | 0.0141 | ±0.0283 | **-5.287** | **1.24e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **692**, R² = **0.1871**, Adj R² = **0.1740**, F-statistic = **14.23** (p = **7.07e-25**), Residual SE = **8.245** on **680** df, AIC = **4895.4**, BIC = **4949.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.4083** | 2.9979 | ±5.9959 | **+25.820** | **5.22e-147** | *** |
| Education: graduate level (vs college) | -0.6352 | 0.7137 | ±1.4275 | -0.890 | 0.3735 |  |
| Education: high school or below (vs college) | +1.7846 | 0.9515 | ±1.9030 | +1.876 | 0.0607 | . |
| Site: UCSD (vs UAB) | -0.8284 | 0.8919 | ±1.7838 | -0.929 | 0.3530 |  |
| Site: UW (vs UAB) | -0.5813 | 0.7813 | ±1.5627 | -0.744 | 0.4569 |  |
| **Age (years)** | **-0.2071** | 0.0309 | ±0.0617 | **-6.710** | **1.94e-11** | *** |
| **BMI (kg/m2)** | **+0.1642** | 0.0510 | ±0.1019 | **+3.222** | **0.0013** | ** |
| Hypertension | +0.4114 | 0.7247 | ±1.4495 | +0.568 | 0.5702 |  |
| High cholesterol | +0.7394 | 0.7033 | ±1.4066 | +1.051 | 0.2931 |  |
| Kidney disease | -0.2046 | 0.9498 | ±1.8995 | -0.215 | 0.8294 |  |
| Circulatory disease | -0.6679 | 0.8367 | ±1.6734 | -0.798 | 0.4247 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0731** | 0.0140 | ±0.0281 | **-5.208** | **1.91e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1504**, Adj R² = **0.1367**, F-statistic = **10.95** (p = **8.87e-19**), Residual SE = **8.429** on **680** df, AIC = **4926.0**, BIC = **4980.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8958** | 2.7963 | ±5.5926 | **+25.353** | **8.25e-142** | *** |
| Education: graduate level (vs college) | -0.8345 | 0.7251 | ±1.4501 | -1.151 | 0.2498 |  |
| **Education: high school or below (vs college)** | **+2.4106** | 0.9775 | ±1.9551 | **+2.466** | **0.0137** | * |
| Site: UCSD (vs UAB) | -1.2071 | 0.9026 | ±1.8052 | -1.337 | 0.1811 |  |
| Site: UW (vs UAB) | -1.0160 | 0.7963 | ±1.5926 | -1.276 | 0.2020 |  |
| **Age (years)** | **-0.2076** | 0.0318 | ±0.0636 | **-6.524** | **6.83e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0500 | ±0.1000 | **+4.312** | **1.62e-05** | *** |
| Hypertension | +0.5687 | 0.7360 | ±1.4720 | +0.773 | 0.4397 |  |
| High cholesterol | +0.5774 | 0.7171 | ±1.4343 | +0.805 | 0.4207 |  |
| Kidney disease | +0.1554 | 0.9600 | ±1.9200 | +0.162 | 0.8714 |  |
| Circulatory disease | -0.3011 | 0.8527 | ±1.7053 | -0.353 | 0.7240 |  |
| Any reading < 54 during wear (0/1) | -0.6350 | 0.7622 | ±1.5244 | -0.833 | 0.4048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1495**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.23e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.7**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.6545** | 2.7792 | ±5.5585 | **+25.422** | **1.43e-142** | *** |
| Education: graduate level (vs college) | -0.8170 | 0.7250 | ±1.4500 | -1.127 | 0.2598 |  |
| **Education: high school or below (vs college)** | **+2.4449** | 0.9774 | ±1.9548 | **+2.501** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1647 | 0.9021 | ±1.8043 | -1.291 | 0.1967 |  |
| Site: UW (vs UAB) | -0.9790 | 0.7979 | ±1.5959 | -1.227 | 0.2198 |  |
| **Age (years)** | **-0.2068** | 0.0318 | ±0.0636 | **-6.505** | **7.76e-11** | *** |
| **BMI (kg/m2)** | **+0.2156** | 0.0499 | ±0.0998 | **+4.320** | **1.56e-05** | *** |
| Hypertension | +0.5414 | 0.7344 | ±1.4687 | +0.737 | 0.4610 |  |
| High cholesterol | +0.6151 | 0.7143 | ±1.4286 | +0.861 | 0.3891 |  |
| Kidney disease | +0.1591 | 0.9577 | ±1.9154 | +0.166 | 0.8680 |  |
| Circulatory disease | -0.3367 | 0.8523 | ±1.7045 | -0.395 | 0.6928 |  |
| Time < 54 (%) | +0.0221 | 0.2663 | ±0.5326 | +0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1499**, Adj R² = **0.1361**, F-statistic = **10.90** (p = **1.09e-18**), Residual SE = **8.432** on **680** df, AIC = **4926.4**, BIC = **4980.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7279** | 2.7799 | ±5.5599 | **+25.442** | **8.62e-143** | *** |
| Education: graduate level (vs college) | -0.8376 | 0.7246 | ±1.4491 | -1.156 | 0.2477 |  |
| **Education: high school or below (vs college)** | **+2.4137** | 0.9771 | ±1.9542 | **+2.470** | **0.0135** | * |
| Site: UCSD (vs UAB) | -1.1989 | 0.9029 | ±1.8057 | -1.328 | 0.1842 |  |
| Site: UW (vs UAB) | -1.0253 | 0.7997 | ±1.5995 | -1.282 | 0.1998 |  |
| **Age (years)** | **-0.2062** | 0.0318 | ±0.0636 | **-6.482** | **9.07e-11** | *** |
| **BMI (kg/m2)** | **+0.2148** | 0.0500 | ±0.0999 | **+4.299** | **1.72e-05** | *** |
| Hypertension | +0.5451 | 0.7343 | ±1.4686 | +0.742 | 0.4578 |  |
| High cholesterol | +0.5782 | 0.7150 | ±1.4300 | +0.809 | 0.4187 |  |
| Kidney disease | +0.1591 | 0.9582 | ±1.9164 | +0.166 | 0.8681 |  |
| Circulatory disease | -0.3537 | 0.8522 | ±1.7045 | -0.415 | 0.6781 |  |
| Avg. daily time < 54 (%) | -0.3203 | 0.6032 | ±1.2063 | -0.531 | 0.5954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1505**, Adj R² = **0.1367**, F-statistic = **10.95** (p = **8.77e-19**), Residual SE = **8.429** on **680** df, AIC = **4925.9**, BIC = **4980.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7902** | 2.7798 | ±5.5597 | **+25.465** | **4.76e-143** | *** |
| Education: graduate level (vs college) | -0.8648 | 0.7259 | ±1.4519 | -1.191 | 0.2336 |  |
| **Education: high school or below (vs college)** | **+2.4057** | 0.9756 | ±1.9512 | **+2.466** | **0.0137** | * |
| Site: UCSD (vs UAB) | -1.2338 | 0.9034 | ±1.8069 | -1.366 | 0.1720 |  |
| Site: UW (vs UAB) | -1.0604 | 0.8038 | ±1.6076 | -1.319 | 0.1871 |  |
| **Age (years)** | **-0.2055** | 0.0318 | ±0.0637 | **-6.454** | **1.09e-10** | *** |
| **BMI (kg/m2)** | **+0.2152** | 0.0499 | ±0.0998 | **+4.312** | **1.62e-05** | *** |
| Hypertension | +0.5605 | 0.7358 | ±1.4717 | +0.762 | 0.4462 |  |
| High cholesterol | +0.5448 | 0.7178 | ±1.4355 | +0.759 | 0.4478 |  |
| Kidney disease | +0.1676 | 0.9587 | ±1.9174 | +0.175 | 0.8613 |  |
| Circulatory disease | -0.3846 | 0.8531 | ±1.7061 | -0.451 | 0.6521 |  |
| Time 54-69, pooled (%) | -0.2670 | 0.3651 | ±0.7302 | -0.731 | 0.4647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **692**, R² = **0.1510**, Adj R² = **0.1373**, F-statistic = **11.00** (p = **7.07e-19**), Residual SE = **8.426** on **680** df, AIC = **4925.5**, BIC = **4979.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7873** | 2.7771 | ±5.5542 | **+25.489** | **2.58e-143** | *** |
| Education: graduate level (vs college) | -0.8763 | 0.7255 | ±1.4510 | -1.208 | 0.2271 |  |
| **Education: high school or below (vs college)** | **+2.3905** | 0.9749 | ±1.9497 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | -1.2531 | 0.9039 | ±1.8077 | -1.386 | 0.1656 |  |
| Site: UW (vs UAB) | -1.0889 | 0.8043 | ±1.6087 | -1.354 | 0.1758 |  |
| **Age (years)** | **-0.2050** | 0.0319 | ±0.0637 | **-6.432** | **1.26e-10** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0499 | ±0.0999 | **+4.316** | **1.59e-05** | *** |
| Hypertension | +0.5673 | 0.7360 | ±1.4720 | +0.771 | 0.4409 |  |
| High cholesterol | +0.5249 | 0.7169 | ±1.4339 | +0.732 | 0.4641 |  |
| Kidney disease | +0.1740 | 0.9591 | ±1.9181 | +0.181 | 0.8560 |  |
| Circulatory disease | -0.3963 | 0.8539 | ±1.7078 | -0.464 | 0.6426 |  |
| Avg. daily time 54-69 (%) | -0.3176 | 0.3583 | ±0.7166 | -0.887 | 0.3753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **692**, R² = **0.1500**, Adj R² = **0.1363**, F-statistic = **10.91** (p = **1.04e-18**), Residual SE = **8.431** on **680** df, AIC = **4926.3**, BIC = **4980.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7701** | 2.7833 | ±5.5666 | **+25.427** | **1.28e-142** | *** |
| Education: graduate level (vs college) | -0.8537 | 0.7265 | ±1.4530 | -1.175 | 0.2399 |  |
| **Education: high school or below (vs college)** | **+2.4097** | 0.9769 | ±1.9539 | **+2.467** | **0.0136** | * |
| Site: UCSD (vs UAB) | -1.2173 | 0.9050 | ±1.8099 | -1.345 | 0.1786 |  |
| Site: UW (vs UAB) | -1.0420 | 0.8049 | ±1.6098 | -1.295 | 0.1955 |  |
| **Age (years)** | **-0.2058** | 0.0319 | ±0.0637 | **-6.460** | **1.05e-10** | *** |
| **BMI (kg/m2)** | **+0.2147** | 0.0500 | ±0.0999 | **+4.298** | **1.73e-05** | *** |
| Hypertension | +0.5516 | 0.7344 | ±1.4687 | +0.751 | 0.4526 |  |
| High cholesterol | +0.5627 | 0.7181 | ±1.4362 | +0.784 | 0.4333 |  |
| Kidney disease | +0.1601 | 0.9584 | ±1.9168 | +0.167 | 0.8673 |  |
| Circulatory disease | -0.3700 | 0.8529 | ±1.7058 | -0.434 | 0.6644 |  |
| Time < 70 (%) | -0.1393 | 0.2063 | ±0.4126 | -0.675 | 0.4994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **692**, R² = **0.1508**, Adj R² = **0.1371**, F-statistic = **10.98** (p = **7.71e-19**), Residual SE = **8.427** on **680** df, AIC = **4925.6**, BIC = **4980.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7937** | 2.7801 | ±5.5601 | **+25.465** | **4.83e-143** | *** |
| Education: graduate level (vs college) | -0.8713 | 0.7256 | ±1.4511 | -1.201 | 0.2298 |  |
| **Education: high school or below (vs college)** | **+2.3869** | 0.9758 | ±1.9516 | **+2.446** | **0.0144** | * |
| Site: UCSD (vs UAB) | -1.2480 | 0.9050 | ±1.8100 | -1.379 | 0.1679 |  |
| Site: UW (vs UAB) | -1.0851 | 0.8051 | ±1.6102 | -1.348 | 0.1777 |  |
| **Age (years)** | **-0.2052** | 0.0319 | ±0.0637 | **-6.439** | **1.21e-10** | *** |
| **BMI (kg/m2)** | **+0.2150** | 0.0500 | ±0.0999 | **+4.303** | **1.69e-05** | *** |
| Hypertension | +0.5618 | 0.7347 | ±1.4694 | +0.765 | 0.4445 |  |
| High cholesterol | +0.5286 | 0.7174 | ±1.4348 | +0.737 | 0.4612 |  |
| Kidney disease | +0.1696 | 0.9588 | ±1.9176 | +0.177 | 0.8596 |  |
| Circulatory disease | -0.3889 | 0.8534 | ±1.7069 | -0.456 | 0.6486 |  |
| Avg. daily time < 70 (%) | -0.2188 | 0.2304 | ±0.4608 | -0.950 | 0.3423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1634**, Adj R² = **0.1499**, F-statistic = **12.08** (p = **6.76e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.3**, BIC = **4969.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.6501** | 3.2199 | ±6.4398 | **+23.805** | **2.96e-125** | *** |
| Education: graduate level (vs college) | -0.6176 | 0.7253 | ±1.4506 | -0.851 | 0.3945 |  |
| **Education: high school or below (vs college)** | **+2.1193** | 0.9577 | ±1.9155 | **+2.213** | **0.0269** | * |
| Site: UCSD (vs UAB) | -1.0369 | 0.8948 | ±1.7895 | -1.159 | 0.2465 |  |
| Site: UW (vs UAB) | -0.7196 | 0.7949 | ±1.5898 | -0.905 | 0.3653 |  |
| **Age (years)** | **-0.1986** | 0.0314 | ±0.0629 | **-6.319** | **2.63e-10** | *** |
| **BMI (kg/m2)** | **+0.1987** | 0.0504 | ±0.1009 | **+3.939** | **8.18e-05** | *** |
| Hypertension | +0.4552 | 0.7319 | ±1.4639 | +0.622 | 0.5340 |  |
| High cholesterol | +0.6918 | 0.7081 | ±1.4162 | +0.977 | 0.3285 |  |
| Kidney disease | +0.0229 | 0.9594 | ±1.9187 | +0.024 | 0.9810 |  |
| Circulatory disease | -0.4942 | 0.8416 | ±1.6832 | -0.587 | 0.5570 |  |
| **Time 54-250, pooled (%)** | **-0.0662** | 0.0210 | ±0.0420 | **-3.153** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1636**, Adj R² = **0.1500**, F-statistic = **12.09** (p = **6.43e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.2**, BIC = **4969.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.8630** | 3.2618 | ±6.5235 | **+23.565** | **8.82e-123** | *** |
| Education: graduate level (vs college) | -0.6215 | 0.7249 | ±1.4497 | -0.857 | 0.3912 |  |
| **Education: high school or below (vs college)** | **+2.1186** | 0.9584 | ±1.9167 | **+2.211** | **0.0271** | * |
| Site: UCSD (vs UAB) | -1.0336 | 0.8947 | ±1.7894 | -1.155 | 0.2480 |  |
| Site: UW (vs UAB) | -0.7271 | 0.7947 | ±1.5893 | -0.915 | 0.3602 |  |
| **Age (years)** | **-0.1995** | 0.0314 | ±0.0629 | **-6.349** | **2.17e-10** | *** |
| **BMI (kg/m2)** | **+0.1980** | 0.0506 | ±0.1011 | **+3.916** | **8.99e-05** | *** |
| Hypertension | +0.4614 | 0.7315 | ±1.4629 | +0.631 | 0.5282 |  |
| High cholesterol | +0.6936 | 0.7081 | ±1.4161 | +0.980 | 0.3273 |  |
| Kidney disease | +0.0029 | 0.9602 | ±1.9204 | +0.003 | 0.9976 |  |
| Circulatory disease | -0.5034 | 0.8423 | ±1.6847 | -0.598 | 0.5501 |  |
| **Avg. daily time 54-250 (%)** | **-0.0675** | 0.0216 | ±0.0432 | **-3.125** | **0.0018** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1890**, Adj R² = **0.1759**, F-statistic = **14.41** (p = **3.35e-25**), Residual SE = **8.235** on **680** df, AIC = **4893.8**, BIC = **4948.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7822** | 2.7138 | ±5.4275 | **+26.083** | **5.71e-150** | *** |
| Education: graduate level (vs college) | -0.8757 | 0.7067 | ±1.4134 | -1.239 | 0.2153 |  |
| **Education: high school or below (vs college)** | **+1.9407** | 0.9763 | ±1.9525 | **+1.988** | **0.0468** | * |
| Site: UCSD (vs UAB) | -0.9087 | 0.8892 | ±1.7785 | -1.022 | 0.3068 |  |
| Site: UW (vs UAB) | -0.8398 | 0.7719 | ±1.5439 | -1.088 | 0.2767 |  |
| **Age (years)** | **-0.2208** | 0.0313 | ±0.0625 | **-7.065** | **1.61e-12** | *** |
| **BMI (kg/m2)** | **+0.1604** | 0.0502 | ±0.1004 | **+3.195** | **0.0014** | ** |
| Hypertension | +0.4758 | 0.7224 | ±1.4449 | +0.659 | 0.5101 |  |
| High cholesterol | +0.6565 | 0.7015 | ±1.4030 | +0.936 | 0.3494 |  |
| Kidney disease | -0.1535 | 0.9369 | ±1.8738 | -0.164 | 0.8699 |  |
| Circulatory disease | -0.6420 | 0.8432 | ±1.6863 | -0.761 | 0.4464 |  |
| **Time 181-250, pooled (%)** | **+0.1267** | 0.0231 | ±0.0462 | **+5.484** | **4.17e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **692**, R² = **0.1873**, Adj R² = **0.1741**, F-statistic = **14.25** (p = **6.56e-25**), Residual SE = **8.244** on **680** df, AIC = **4895.2**, BIC = **4949.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7535** | 2.7164 | ±5.4328 | **+26.047** | **1.45e-149** | *** |
| Education: graduate level (vs college) | -0.8909 | 0.7086 | ±1.4172 | -1.257 | 0.2087 |  |
| **Education: high school or below (vs college)** | **+1.9129** | 0.9722 | ±1.9445 | **+1.967** | **0.0491** | * |
| Site: UCSD (vs UAB) | -0.8776 | 0.8904 | ±1.7808 | -0.986 | 0.3243 |  |
| Site: UW (vs UAB) | -0.8160 | 0.7735 | ±1.5470 | -1.055 | 0.2914 |  |
| **Age (years)** | **-0.2196** | 0.0313 | ±0.0625 | **-7.022** | **2.18e-12** | *** |
| **BMI (kg/m2)** | **+0.1617** | 0.0504 | ±0.1007 | **+3.211** | **0.0013** | ** |
| Hypertension | +0.4794 | 0.7235 | ±1.4471 | +0.663 | 0.5076 |  |
| High cholesterol | +0.6441 | 0.7025 | ±1.4050 | +0.917 | 0.3592 |  |
| Kidney disease | -0.1585 | 0.9395 | ±1.8790 | -0.169 | 0.8660 |  |
| Circulatory disease | -0.6106 | 0.8452 | ±1.6904 | -0.722 | 0.4700 |  |
| **Avg. daily time 181-250 (%)** | **+0.1215** | 0.0226 | ±0.0452 | **+5.372** | **7.81e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **692**, R² = **0.1881**, Adj R² = **0.1750**, F-statistic = **14.32** (p = **4.74e-25**), Residual SE = **8.240** on **680** df, AIC = **4894.5**, BIC = **4949.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.0454** | 2.7276 | ±5.4552 | **+25.680** | **1.94e-145** | *** |
| Education: graduate level (vs college) | -0.6329 | 0.7126 | ±1.4252 | -0.888 | 0.3744 |  |
| Education: high school or below (vs college) | +1.7804 | 0.9518 | ±1.9036 | +1.871 | 0.0614 | . |
| Site: UCSD (vs UAB) | -0.8786 | 0.8908 | ±1.7816 | -0.986 | 0.3240 |  |
| Site: UW (vs UAB) | -0.6156 | 0.7792 | ±1.5585 | -0.790 | 0.4295 |  |
| **Age (years)** | **-0.2057** | 0.0308 | ±0.0616 | **-6.677** | **2.43e-11** | *** |
| **BMI (kg/m2)** | **+0.1641** | 0.0509 | ±0.1017 | **+3.226** | **0.0013** | ** |
| Hypertension | +0.4067 | 0.7241 | ±1.4482 | +0.562 | 0.5743 |  |
| High cholesterol | +0.7189 | 0.7020 | ±1.4040 | +1.024 | 0.3058 |  |
| Kidney disease | -0.1772 | 0.9477 | ±1.8954 | -0.187 | 0.8516 |  |
| Circulatory disease | -0.6945 | 0.8354 | ±1.6709 | -0.831 | 0.4058 |  |
| **Time > 180 (%)** | **+0.0741** | 0.0140 | ±0.0280 | **+5.298** | **1.17e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1874**, Adj R² = **0.1743**, F-statistic = **14.26** (p = **6.26e-25**), Residual SE = **8.243** on **680** df, AIC = **4895.1**, BIC = **4949.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.1400** | 2.7324 | ±5.4648 | **+25.670** | **2.56e-145** | *** |
| Education: graduate level (vs college) | -0.6532 | 0.7132 | ±1.4264 | -0.916 | 0.3597 |  |
| Education: high school or below (vs college) | +1.7679 | 0.9515 | ±1.9030 | +1.858 | 0.0632 | . |
| Site: UCSD (vs UAB) | -0.8563 | 0.8914 | ±1.7828 | -0.961 | 0.3367 |  |
| Site: UW (vs UAB) | -0.6168 | 0.7797 | ±1.5595 | -0.791 | 0.4289 |  |
| **Age (years)** | **-0.2065** | 0.0309 | ±0.0617 | **-6.693** | **2.19e-11** | *** |
| **BMI (kg/m2)** | **+0.1642** | 0.0510 | ±0.1021 | **+3.217** | **0.0013** | ** |
| Hypertension | +0.4186 | 0.7242 | ±1.4484 | +0.578 | 0.5633 |  |
| High cholesterol | +0.7110 | 0.7023 | ±1.4046 | +1.012 | 0.3114 |  |
| Kidney disease | -0.1999 | 0.9495 | ±1.8990 | -0.211 | 0.8333 |  |
| Circulatory disease | -0.6839 | 0.8369 | ±1.6737 | -0.817 | 0.4138 |  |
| **Avg. daily time > 180 (%)** | **+0.0729** | 0.0139 | ±0.0278 | **+5.250** | **1.52e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1744**, Adj R² = **0.1611**, F-statistic = **13.06** (p = **1.00e-22**), Residual SE = **8.309** on **680** df, AIC = **4906.1**, BIC = **4960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.4498** | 2.7561 | ±5.5121 | **+25.562** | **4.06e-144** | *** |
| Education: graduate level (vs college) | -0.5751 | 0.7258 | ±1.4516 | -0.792 | 0.4281 |  |
| **Education: high school or below (vs college)** | **+2.0122** | 0.9440 | ±1.8879 | **+2.132** | **0.0330** | * |
| Site: UCSD (vs UAB) | -0.9144 | 0.8965 | ±1.7931 | -1.020 | 0.3078 |  |
| Site: UW (vs UAB) | -0.7491 | 0.7829 | ±1.5658 | -0.957 | 0.3387 |  |
| **Age (years)** | **-0.2005** | 0.0314 | ±0.0628 | **-6.383** | **1.74e-10** | *** |
| **BMI (kg/m2)** | **+0.1659** | 0.0513 | ±0.1025 | **+3.236** | **0.0012** | ** |
| Hypertension | +0.4602 | 0.7306 | ±1.4613 | +0.630 | 0.5288 |  |
| High cholesterol | +0.7547 | 0.7091 | ±1.4181 | +1.064 | 0.2872 |  |
| Kidney disease | +0.0226 | 0.9484 | ±1.8968 | +0.024 | 0.9810 |  |
| Circulatory disease | -0.6082 | 0.8373 | ±1.6746 | -0.726 | 0.4676 |  |
| **Nocturnal time > 180 (%)** | **+0.0543** | 0.0127 | ±0.0254 | **+4.274** | **1.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1634**, Adj R² = **0.1499**, F-statistic = **12.07** (p = **6.80e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.3**, BIC = **4969.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.0477** | 2.7894 | ±5.5788 | **+25.112** | **3.69e-139** | *** |
| Education: graduate level (vs college) | -0.6230 | 0.7251 | ±1.4501 | -0.859 | 0.3903 |  |
| **Education: high school or below (vs college)** | **+2.1131** | 0.9580 | ±1.9160 | **+2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | -1.0442 | 0.8946 | ±1.7893 | -1.167 | 0.2431 |  |
| Site: UW (vs UAB) | -0.7289 | 0.7943 | ±1.5885 | -0.918 | 0.3588 |  |
| **Age (years)** | **-0.1985** | 0.0314 | ±0.0629 | **-6.312** | **2.76e-10** | *** |
| **BMI (kg/m2)** | **+0.1984** | 0.0505 | ±0.1009 | **+3.931** | **8.47e-05** | *** |
| Hypertension | +0.4553 | 0.7319 | ±1.4638 | +0.622 | 0.5339 |  |
| High cholesterol | +0.6848 | 0.7080 | ±1.4159 | +0.967 | 0.3334 |  |
| Kidney disease | +0.0215 | 0.9594 | ±1.9188 | +0.022 | 0.9821 |  |
| Circulatory disease | -0.4978 | 0.8416 | ±1.6833 | -0.591 | 0.5542 |  |
| **Time > 250 (%)** | **+0.0662** | 0.0210 | ±0.0419 | **+3.157** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **692**, R² = **0.1637**, Adj R² = **0.1502**, F-statistic = **12.10** (p = **6.10e-21**), Residual SE = **8.363** on **680** df, AIC = **4915.1**, BIC = **4969.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.1249** | 2.7925 | ±5.5850 | **+25.112** | **3.70e-139** | *** |
| Education: graduate level (vs college) | -0.6245 | 0.7247 | ±1.4494 | -0.862 | 0.3888 |  |
| **Education: high school or below (vs college)** | **+2.1109** | 0.9585 | ±1.9170 | **+2.202** | **0.0276** | * |
| Site: UCSD (vs UAB) | -1.0397 | 0.8946 | ±1.7891 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -0.7350 | 0.7940 | ±1.5881 | -0.926 | 0.3546 |  |
| **Age (years)** | **-0.1994** | 0.0314 | ±0.0629 | **-6.343** | **2.26e-10** | *** |
| **BMI (kg/m2)** | **+0.1978** | 0.0506 | ±0.1012 | **+3.909** | **9.27e-05** | *** |
| Hypertension | +0.4618 | 0.7314 | ±1.4627 | +0.631 | 0.5278 |  |
| High cholesterol | +0.6867 | 0.7078 | ±1.4157 | +0.970 | 0.3320 |  |
| Kidney disease | +0.0022 | 0.9602 | ±1.9204 | +0.002 | 0.9982 |  |
| Circulatory disease | -0.5075 | 0.8424 | ±1.6848 | -0.602 | 0.5469 |  |
| **Avg. daily time > 250 (%)** | **+0.0678** | 0.0216 | ±0.0432 | **+3.142** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 694; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **694**, R² = **0.0405**, Adj R² = **0.0264**, F-statistic = **2.88** (p = **0.0016**), Residual SE = **66.292** on **683** df, AIC = **7801.8**, BIC = **7851.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.3068** | 22.0318 | ±44.0636 | **+17.353** | **1.89e-67** | *** |
| Education: graduate level (vs college) | -1.5602 | 5.6599 | ±11.3197 | -0.276 | 0.7828 |  |
| Education: high school or below (vs college) | -11.0140 | 7.7007 | ±15.4015 | -1.430 | 0.1526 |  |
| **Site: UCSD (vs UAB)** | **-19.1719** | 6.2197 | ±12.4394 | **-3.082** | **0.0021** | ** |
| Site: UW (vs UAB) | +0.3116 | 6.5446 | ±13.0892 | +0.048 | 0.9620 |  |
| Age (years) | +0.1968 | 0.2616 | ±0.5233 | +0.752 | 0.4520 |  |
| **BMI (kg/m2)** | **-0.9525** | 0.3584 | ±0.7168 | **-2.658** | **0.0079** | ** |
| Hypertension | -9.4587 | 5.4709 | ±10.9418 | -1.729 | 0.0838 | . |
| High cholesterol | +0.6950 | 5.1964 | ±10.3928 | +0.134 | 0.8936 |  |
| Kidney disease | -0.7362 | 7.8512 | ±15.7024 | -0.094 | 0.9253 |  |
| **Circulatory disease** | **+16.1730** | 7.5709 | ±15.1417 | **+2.136** | **0.0327** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **694**, R² = **0.0478**, Adj R² = **0.0325**, F-statistic = **3.11** (p = **4.15e-04**), Residual SE = **66.087** on **682** df, AIC = **7798.4**, BIC = **7853.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+408.2180** | 23.9973 | ±47.9946 | **+17.011** | **6.81e-65** | *** |
| Education: graduate level (vs college) | -2.6886 | 5.6984 | ±11.3968 | -0.472 | 0.6371 |  |
| Education: high school or below (vs college) | -8.8992 | 7.6512 | ±15.3023 | -1.163 | 0.2448 |  |
| **Site: UCSD (vs UAB)** | **-19.6161** | 6.2029 | ±12.4058 | **-3.162** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.7953 | 6.5490 | ±13.0981 | -0.121 | 0.9033 |  |
| Age (years) | +0.1920 | 0.2601 | ±0.5202 | +0.738 | 0.4604 |  |
| **BMI (kg/m2)** | **-0.7920** | 0.3720 | ±0.7441 | **-2.129** | **0.0333** | * |
| Hypertension | -8.8530 | 5.4512 | ±10.9024 | -1.624 | 0.1044 |  |
| High cholesterol | +0.9483 | 5.1714 | ±10.3428 | +0.183 | 0.8545 |  |
| Kidney disease | -0.8813 | 7.8517 | ±15.7033 | -0.112 | 0.9106 |  |
| **Circulatory disease** | **+16.7905** | 7.5219 | ±15.0438 | **+2.232** | **0.0256** | * |
| **HbA1c (%)** | **-4.4957** | 1.7375 | ±3.4750 | **-2.587** | **0.0097** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **694**, R² = **0.0410**, Adj R² = **0.0255**, F-statistic = **2.65** (p = **0.0025**), Residual SE = **66.324** on **682** df, AIC = **7803.4**, BIC = **7857.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.6803** | 23.6082 | ±47.2164 | **+16.421** | **1.34e-60** | *** |
| Education: graduate level (vs college) | -1.7571 | 5.6849 | ±11.3697 | -0.309 | 0.7573 |  |
| Education: high school or below (vs college) | -10.5355 | 7.7340 | ±15.4680 | -1.362 | 0.1731 |  |
| **Site: UCSD (vs UAB)** | **-19.3769** | 6.2317 | ±12.4634 | **-3.109** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0549 | 6.5570 | ±13.1141 | +0.008 | 0.9933 |  |
| Age (years) | +0.1943 | 0.2620 | ±0.5240 | +0.742 | 0.4583 |  |
| **BMI (kg/m2)** | **-0.9167** | 0.3691 | ±0.7381 | **-2.484** | **0.0130** | * |
| Hypertension | -9.3648 | 5.4708 | ±10.9416 | -1.712 | 0.0869 | . |
| High cholesterol | +0.6898 | 5.2044 | ±10.4088 | +0.133 | 0.8946 |  |
| Kidney disease | -0.5065 | 7.9097 | ±15.8194 | -0.064 | 0.9489 |  |
| **Circulatory disease** | **+16.4977** | 7.6235 | ±15.2470 | **+2.164** | **0.0305** | * |
| Mean glucose (mg/dL) | -0.0391 | 0.0671 | ±0.1342 | -0.583 | 0.5598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **694**, R² = **0.0410**, Adj R² = **0.0255**, F-statistic = **2.65** (p = **0.0025**), Residual SE = **66.324** on **682** df, AIC = **7803.4**, BIC = **7857.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.0956** | 28.2877 | ±56.5753 | **+13.896** | **6.66e-44** | *** |
| Education: graduate level (vs college) | -1.7571 | 5.6849 | ±11.3697 | -0.309 | 0.7573 |  |
| Education: high school or below (vs college) | -10.5355 | 7.7340 | ±15.4680 | -1.362 | 0.1731 |  |
| **Site: UCSD (vs UAB)** | **-19.3769** | 6.2317 | ±12.4634 | **-3.109** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0549 | 6.5570 | ±13.1141 | +0.008 | 0.9933 |  |
| Age (years) | +0.1943 | 0.2620 | ±0.5240 | +0.742 | 0.4583 |  |
| **BMI (kg/m2)** | **-0.9167** | 0.3691 | ±0.7381 | **-2.484** | **0.0130** | * |
| Hypertension | -9.3648 | 5.4708 | ±10.9416 | -1.712 | 0.0869 | . |
| High cholesterol | +0.6898 | 5.2044 | ±10.4088 | +0.133 | 0.8946 |  |
| Kidney disease | -0.5065 | 7.9097 | ±15.8194 | -0.064 | 0.9489 |  |
| **Circulatory disease** | **+16.4977** | 7.6235 | ±15.2470 | **+2.164** | **0.0305** | * |
| GMI (%) | -1.6360 | 2.8058 | ±5.6117 | -0.583 | 0.5598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **694**, R² = **0.0405**, Adj R² = **0.0250**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.340** on **682** df, AIC = **7803.7**, BIC = **7858.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+383.4633** | 23.3668 | ±46.7336 | **+16.411** | **1.61e-60** | *** |
| Education: graduate level (vs college) | -1.6150 | 5.6923 | ±11.3846 | -0.284 | 0.7766 |  |
| Education: high school or below (vs college) | -10.9105 | 7.7388 | ±15.4776 | -1.410 | 0.1586 |  |
| **Site: UCSD (vs UAB)** | **-19.2221** | 6.2378 | ±12.4757 | **-3.082** | **0.0021** | ** |
| Site: UW (vs UAB) | +0.2702 | 6.5574 | ±13.1149 | +0.041 | 0.9671 |  |
| Age (years) | +0.1950 | 0.2625 | ±0.5249 | +0.743 | 0.4574 |  |
| **BMI (kg/m2)** | **-0.9422** | 0.3722 | ±0.7443 | **-2.532** | **0.0114** | * |
| Hypertension | -9.4456 | 5.4781 | ±10.9562 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6884 | 5.2041 | ±10.4081 | +0.132 | 0.8948 |  |
| Kidney disease | -0.7175 | 7.8737 | ±15.7474 | -0.091 | 0.9274 |  |
| **Circulatory disease** | **+16.2487** | 7.6363 | ±15.2726 | **+2.128** | **0.0334** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0088 | 0.0638 | ±0.1276 | -0.137 | 0.8909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0461**, Adj R² = **0.0307**, F-statistic = **2.99** (p = **6.62e-04**), Residual SE = **66.147** on **682** df, AIC = **7799.7**, BIC = **7854.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.4000** | 22.8519 | ±45.7037 | **+17.303** | **4.48e-67** | *** |
| Education: graduate level (vs college) | -2.4186 | 5.6886 | ±11.3772 | -0.425 | 0.6707 |  |
| Education: high school or below (vs college) | -9.3165 | 7.6881 | ±15.3763 | -1.212 | 0.2256 |  |
| **Site: UCSD (vs UAB)** | **-20.0176** | 6.2240 | ±12.4480 | **-3.216** | **0.0013** | ** |
| Site: UW (vs UAB) | -1.3950 | 6.5931 | ±13.1862 | -0.212 | 0.8324 |  |
| Age (years) | +0.2113 | 0.2597 | ±0.5194 | +0.813 | 0.4160 |  |
| **BMI (kg/m2)** | **-0.8538** | 0.3685 | ±0.7370 | **-2.317** | **0.0205** | * |
| Hypertension | -8.7931 | 5.4646 | ±10.9292 | -1.609 | 0.1076 |  |
| High cholesterol | +0.2293 | 5.1819 | ±10.3639 | +0.044 | 0.9647 |  |
| Kidney disease | +1.8501 | 8.1919 | ±16.3838 | +0.226 | 0.8213 |  |
| **Circulatory disease** | **+16.8977** | 7.5068 | ±15.0136 | **+2.251** | **0.0244** | * |
| **Glucose SD, pooled (mg/dL)** | **-0.4407** | 0.2173 | ±0.4347 | **-2.028** | **0.0426** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0454**, Adj R² = **0.0300**, F-statistic = **2.95** (p = **7.91e-04**), Residual SE = **66.170** on **682** df, AIC = **7800.2**, BIC = **7854.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.1003** | 22.8697 | ±45.7394 | **+17.276** | **7.11e-67** | *** |
| Education: graduate level (vs college) | -2.2449 | 5.6688 | ±11.3376 | -0.396 | 0.6921 |  |
| Education: high school or below (vs college) | -9.2510 | 7.7220 | ±15.4440 | -1.198 | 0.2309 |  |
| **Site: UCSD (vs UAB)** | **-19.9623** | 6.2385 | ±12.4769 | **-3.200** | **0.0014** | ** |
| Site: UW (vs UAB) | -1.1487 | 6.5904 | ±13.1807 | -0.174 | 0.8616 |  |
| Age (years) | +0.2169 | 0.2598 | ±0.5196 | +0.835 | 0.4039 |  |
| **BMI (kg/m2)** | **-0.8840** | 0.3653 | ±0.7306 | **-2.420** | **0.0155** | * |
| Hypertension | -8.8898 | 5.4581 | ±10.9162 | -1.629 | 0.1034 |  |
| High cholesterol | +0.3144 | 5.1850 | ±10.3701 | +0.061 | 0.9516 |  |
| Kidney disease | +1.9042 | 8.2037 | ±16.4075 | +0.232 | 0.8165 |  |
| **Circulatory disease** | **+16.7879** | 7.5187 | ±15.0374 | **+2.233** | **0.0256** | * |
| Avg. daily SD (mg/dL) | -0.4709 | 0.2458 | ±0.4916 | -1.916 | 0.0554 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **694**, R² = **0.0442**, Adj R² = **0.0288**, F-statistic = **2.87** (p = **0.0011**), Residual SE = **66.211** on **682** df, AIC = **7801.1**, BIC = **7855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.4438** | 24.1383 | ±48.2767 | **+16.548** | **1.65e-61** | *** |
| Education: graduate level (vs college) | -2.0574 | 5.6651 | ±11.3301 | -0.363 | 0.7165 |  |
| Education: high school or below (vs college) | -10.4820 | 7.6968 | ±15.3935 | -1.362 | 0.1732 |  |
| **Site: UCSD (vs UAB)** | **-19.7305** | 6.2368 | ±12.4736 | **-3.164** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.8977 | 6.5837 | ±13.1673 | -0.136 | 0.8915 |  |
| Age (years) | +0.2205 | 0.2604 | ±0.5208 | +0.847 | 0.3971 |  |
| **BMI (kg/m2)** | **-0.9445** | 0.3599 | ±0.7198 | **-2.625** | **0.0087** | ** |
| Hypertension | -8.9812 | 5.4680 | ±10.9360 | -1.643 | 0.1005 |  |
| High cholesterol | +0.1198 | 5.1907 | ±10.3815 | +0.023 | 0.9816 |  |
| Kidney disease | +1.4109 | 8.1344 | ±16.2688 | +0.173 | 0.8623 |  |
| **Circulatory disease** | **+16.0629** | 7.5374 | ±15.0749 | **+2.131** | **0.0331** | * |
| CV (%) | -0.7781 | 0.4633 | ±0.9266 | -1.680 | 0.0931 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **694**, R² = **0.0466**, Adj R² = **0.0312**, F-statistic = **3.03** (p = **5.72e-04**), Residual SE = **66.128** on **682** df, AIC = **7799.3**, BIC = **7853.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.3916** | 25.1630 | ±50.3260 | **+14.163** | **1.55e-45** | *** |
| Education: graduate level (vs college) | -2.0962 | 5.6529 | ±11.3059 | -0.371 | 0.7108 |  |
| Education: high school or below (vs college) | -10.3305 | 7.6849 | ±15.3697 | -1.344 | 0.1789 |  |
| **Site: UCSD (vs UAB)** | **-19.5454** | 6.2109 | ±12.4218 | **-3.147** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.9989 | 6.5704 | ±13.1409 | -0.152 | 0.8792 |  |
| Age (years) | +0.2232 | 0.2603 | ±0.5207 | +0.857 | 0.3913 |  |
| **BMI (kg/m2)** | **-0.9530** | 0.3599 | ±0.7198 | **-2.648** | **0.0081** | ** |
| Hypertension | -8.8384 | 5.4688 | ±10.9375 | -1.616 | 0.1061 |  |
| High cholesterol | +0.3284 | 5.1847 | ±10.3694 | +0.063 | 0.9495 |  |
| Kidney disease | +1.6716 | 8.0660 | ±16.1320 | +0.207 | 0.8358 |  |
| **Circulatory disease** | **+16.2729** | 7.5148 | ±15.0295 | **+2.165** | **0.0304** | * |
| **Mean / SD ratio** | **+5.5004** | 2.4726 | ±4.9452 | **+2.225** | **0.0261** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0491**, Adj R² = **0.0338**, F-statistic = **3.20** (p = **2.91e-04**), Residual SE = **66.041** on **682** df, AIC = **7797.5**, BIC = **7852.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+353.6626** | 24.6718 | ±49.3436 | **+14.335** | **1.33e-46** | *** |
| Education: graduate level (vs college) | -2.0518 | 5.6311 | ±11.2621 | -0.364 | 0.7156 |  |
| Education: high school or below (vs college) | -10.1453 | 7.6989 | ±15.3977 | -1.318 | 0.1876 |  |
| **Site: UCSD (vs UAB)** | **-19.4520** | 6.2148 | ±12.4295 | **-3.130** | **0.0017** | ** |
| Site: UW (vs UAB) | -1.0232 | 6.5582 | ±13.1164 | -0.156 | 0.8760 |  |
| Age (years) | +0.2407 | 0.2598 | ±0.5195 | +0.927 | 0.3541 |  |
| **BMI (kg/m2)** | **-0.9868** | 0.3583 | ±0.7165 | **-2.754** | **0.0059** | ** |
| Hypertension | -8.7570 | 5.4537 | ±10.9074 | -1.606 | 0.1083 |  |
| High cholesterol | +0.1984 | 5.1769 | ±10.3537 | +0.038 | 0.9694 |  |
| Kidney disease | +1.9466 | 8.0081 | ±16.0161 | +0.243 | 0.8079 |  |
| **Circulatory disease** | **+16.0113** | 7.5407 | ±15.0814 | **+2.123** | **0.0337** | * |
| **Avg. daily mean/SD** | **+5.2112** | 2.0181 | ±4.0362 | **+2.582** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **694**, R² = **0.0612**, Adj R² = **0.0460**, F-statistic = **4.04** (p = **9.52e-06**), Residual SE = **65.622** on **682** df, AIC = **7788.6**, BIC = **7843.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+435.0134** | 26.3327 | ±52.6655 | **+16.520** | **2.64e-61** | *** |
| Education: graduate level (vs college) | -3.2794 | 5.6426 | ±11.2853 | -0.581 | 0.5611 |  |
| Education: high school or below (vs college) | -9.5318 | 7.5646 | ±15.1293 | -1.260 | 0.2077 |  |
| **Site: UCSD (vs UAB)** | **-21.1549** | 6.1940 | ±12.3880 | **-3.415** | **6.37e-04** | *** |
| Site: UW (vs UAB) | -3.5503 | 6.5182 | ±13.0364 | -0.545 | 0.5860 |  |
| Age (years) | +0.1341 | 0.2600 | ±0.5200 | +0.516 | 0.6059 |  |
| **BMI (kg/m2)** | **-0.9158** | 0.3559 | ±0.7119 | **-2.573** | **0.0101** | * |
| Hypertension | -9.9424 | 5.4124 | ±10.8248 | -1.837 | 0.0662 | . |
| High cholesterol | -0.5826 | 5.1843 | ±10.3686 | -0.112 | 0.9105 |  |
| Kidney disease | +1.3947 | 7.9108 | ±15.8215 | +0.176 | 0.8601 |  |
| **Circulatory disease** | **+16.2829** | 7.4446 | ±14.8893 | **+2.187** | **0.0287** | * |
| **MAG (mg/dL/h)** | **-1.0357** | 0.2615 | ±0.5231 | **-3.960** | **7.50e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **694**, R² = **0.0460**, Adj R² = **0.0306**, F-statistic = **2.99** (p = **6.77e-04**), Residual SE = **66.150** on **682** df, AIC = **7799.8**, BIC = **7854.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.5657** | 24.4072 | ±48.8144 | **+16.535** | **2.06e-61** | *** |
| Education: graduate level (vs college) | -2.1925 | 5.6649 | ±11.3297 | -0.387 | 0.6987 |  |
| Education: high school or below (vs college) | -9.0941 | 7.7140 | ±15.4281 | -1.179 | 0.2384 |  |
| **Site: UCSD (vs UAB)** | **-20.1928** | 6.2474 | ±12.4948 | **-3.232** | **0.0012** | ** |
| Site: UW (vs UAB) | -1.3405 | 6.5909 | ±13.1818 | -0.203 | 0.8388 |  |
| Age (years) | +0.1989 | 0.2599 | ±0.5198 | +0.765 | 0.4441 |  |
| **BMI (kg/m2)** | **-0.9082** | 0.3618 | ±0.7235 | **-2.510** | **0.0121** | * |
| Hypertension | -9.2227 | 5.4541 | ±10.9082 | -1.691 | 0.0908 | . |
| High cholesterol | +0.2398 | 5.1890 | ±10.3780 | +0.046 | 0.9631 |  |
| Kidney disease | +1.9830 | 8.1611 | ±16.3222 | +0.243 | 0.8080 |  |
| **Circulatory disease** | **+16.7407** | 7.5074 | ±15.0148 | **+2.230** | **0.0258** | * |
| **Avg. daily range (mg/dL)** | **-0.1475** | 0.0724 | ±0.1449 | **-2.036** | **0.0418** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **694**, R² = **0.0459**, Adj R² = **0.0305**, F-statistic = **2.98** (p = **6.94e-04**), Residual SE = **66.153** on **682** df, AIC = **7799.8**, BIC = **7854.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.2703** | 22.3463 | ±44.6925 | **+17.375** | **1.27e-67** | *** |
| Education: graduate level (vs college) | -2.6093 | 5.7294 | ±11.4588 | -0.455 | 0.6488 |  |
| Education: high school or below (vs college) | -10.3166 | 7.6138 | ±15.2277 | -1.355 | 0.1754 |  |
| **Site: UCSD (vs UAB)** | **-19.6171** | 6.1787 | ±12.3575 | **-3.175** | **0.0015** | ** |
| Site: UW (vs UAB) | -0.9667 | 6.5845 | ±13.1690 | -0.147 | 0.8833 |  |
| Age (years) | +0.1777 | 0.2616 | ±0.5232 | +0.679 | 0.4969 |  |
| **BMI (kg/m2)** | **-0.8334** | 0.3644 | ±0.7288 | **-2.287** | **0.0222** | * |
| Hypertension | -8.6565 | 5.4936 | ±10.9871 | -1.576 | 0.1151 |  |
| High cholesterol | +0.3402 | 5.1830 | ±10.3661 | +0.066 | 0.9477 |  |
| Kidney disease | +0.0543 | 7.9736 | ±15.9471 | +0.007 | 0.9946 |  |
| **Circulatory disease** | **+17.1760** | 7.5122 | ±15.0244 | **+2.286** | **0.0222** | * |
| SD of daily means (mg/dL) | -0.6333 | 0.3282 | ±0.6565 | -1.930 | 0.0537 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.329** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.6139** | 24.6781 | ±49.3561 | **+15.302** | **7.46e-53** | *** |
| Education: graduate level (vs college) | -1.7415 | 5.6829 | ±11.3657 | -0.306 | 0.7593 |  |
| Education: high school or below (vs college) | -10.6159 | 7.7576 | ±15.5152 | -1.368 | 0.1712 |  |
| **Site: UCSD (vs UAB)** | **-19.4017** | 6.2526 | ±12.5052 | **-3.103** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0422 | 6.5849 | ±13.1698 | +0.006 | 0.9949 |  |
| Age (years) | +0.1976 | 0.2620 | ±0.5239 | +0.754 | 0.4507 |  |
| **BMI (kg/m2)** | **-0.9180** | 0.3726 | ±0.7451 | **-2.464** | **0.0137** | * |
| Hypertension | -9.4049 | 5.4713 | ±10.9426 | -1.719 | 0.0856 | . |
| High cholesterol | +0.6246 | 5.2038 | ±10.4076 | +0.120 | 0.9045 |  |
| Kidney disease | -0.4760 | 7.9373 | ±15.8747 | -0.060 | 0.9522 |  |
| **Circulatory disease** | **+16.4132** | 7.5953 | ±15.1906 | **+2.161** | **0.0307** | * |
| Time in range 70-180, pooled (%) | +0.0513 | 0.1089 | ±0.2179 | +0.471 | 0.6374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **694**, R² = **0.0407**, Adj R² = **0.0252**, F-statistic = **2.63** (p = **0.0027**), Residual SE = **66.332** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+378.2660** | 24.7673 | ±49.5347 | **+15.273** | **1.16e-52** | *** |
| Education: graduate level (vs college) | -1.7035 | 5.6804 | ±11.3609 | -0.300 | 0.7643 |  |
| Education: high school or below (vs college) | -10.6614 | 7.7642 | ±15.5284 | -1.373 | 0.1697 |  |
| **Site: UCSD (vs UAB)** | **-19.3847** | 6.2613 | ±12.5225 | **-3.096** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.0777 | 6.5865 | ±13.1730 | +0.012 | 0.9906 |  |
| Age (years) | +0.1979 | 0.2621 | ±0.5241 | +0.755 | 0.4500 |  |
| **BMI (kg/m2)** | **-0.9227** | 0.3728 | ±0.7456 | **-2.475** | **0.0133** | * |
| Hypertension | -9.4179 | 5.4724 | ±10.9448 | -1.721 | 0.0853 | . |
| High cholesterol | +0.6378 | 5.2039 | ±10.4078 | +0.123 | 0.9025 |  |
| Kidney disease | -0.4966 | 7.9478 | ±15.8956 | -0.062 | 0.9502 |  |
| **Circulatory disease** | **+16.3743** | 7.5955 | ±15.1909 | **+2.156** | **0.0311** | * |
| Avg. daily time in range 70-180 (%) | +0.0436 | 0.1085 | ±0.2170 | +0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **694**, R² = **0.0412**, Adj R² = **0.0258**, F-statistic = **2.67** (p = **0.0023**), Residual SE = **66.314** on **682** df, AIC = **7803.2**, BIC = **7857.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.6705** | 22.3192 | ±44.6384 | **+17.056** | **3.17e-65** | *** |
| Education: graduate level (vs college) | -1.4057 | 5.6800 | ±11.3599 | -0.247 | 0.8045 |  |
| Education: high school or below (vs college) | -10.8334 | 7.7437 | ±15.4875 | -1.399 | 0.1618 |  |
| **Site: UCSD (vs UAB)** | **-18.9644** | 6.2361 | ±12.4722 | **-3.041** | **0.0024** | ** |
| Site: UW (vs UAB) | +0.5344 | 6.5460 | ±13.0920 | +0.082 | 0.9349 |  |
| Age (years) | +0.2025 | 0.2623 | ±0.5246 | +0.772 | 0.4401 |  |
| **BMI (kg/m2)** | **-0.9522** | 0.3601 | ±0.7202 | **-2.644** | **0.0082** | ** |
| Hypertension | -9.6538 | 5.4895 | ±10.9790 | -1.759 | 0.0786 | . |
| High cholesterol | +0.9586 | 5.2255 | ±10.4510 | +0.183 | 0.8545 |  |
| Kidney disease | -0.6799 | 7.8527 | ±15.7054 | -0.087 | 0.9310 |  |
| **Circulatory disease** | **+15.9608** | 7.5628 | ±15.1255 | **+2.110** | **0.0348** | * |
| Any reading < 54 during wear (0/1) | +4.3380 | 5.9799 | ±11.9597 | +0.725 | 0.4682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.331** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.9117** | 22.0768 | ±44.1535 | **+17.345** | **2.17e-67** | *** |
| Education: graduate level (vs college) | -1.7186 | 5.6745 | ±11.3490 | -0.303 | 0.7620 |  |
| Education: high school or below (vs college) | -11.1924 | 7.7199 | ±15.4399 | -1.450 | 0.1471 |  |
| **Site: UCSD (vs UAB)** | **-19.3752** | 6.2502 | ±12.5005 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0462 | 6.5908 | ±13.1816 | +0.007 | 0.9944 |  |
| Age (years) | +0.2009 | 0.2619 | ±0.5239 | +0.767 | 0.4432 |  |
| **BMI (kg/m2)** | **-0.9618** | 0.3590 | ±0.7179 | **-2.679** | **0.0074** | ** |
| Hypertension | -9.4667 | 5.4717 | ±10.9434 | -1.730 | 0.0836 | . |
| High cholesterol | +0.4907 | 5.2316 | ±10.4632 | +0.094 | 0.9253 |  |
| Kidney disease | -0.7888 | 7.8530 | ±15.7061 | -0.100 | 0.9200 |  |
| **Circulatory disease** | **+16.0752** | 7.5803 | ±15.1607 | **+2.121** | **0.0340** | * |
| Time < 54 (%) | -1.9106 | 1.6284 | ±3.2567 | -1.173 | 0.2407 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.5973** | 22.0708 | ±44.1416 | **+17.335** | **2.56e-67** | *** |
| Education: graduate level (vs college) | -1.6403 | 5.6726 | ±11.3451 | -0.289 | 0.7725 |  |
| Education: high school or below (vs college) | -11.1252 | 7.7232 | ±15.4464 | -1.440 | 0.1497 |  |
| **Site: UCSD (vs UAB)** | **-19.2904** | 6.2568 | ±12.5136 | **-3.083** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1381 | 6.6062 | ±13.2124 | +0.021 | 0.9833 |  |
| Age (years) | +0.1987 | 0.2618 | ±0.5235 | +0.759 | 0.4478 |  |
| **BMI (kg/m2)** | **-0.9554** | 0.3584 | ±0.7167 | **-2.666** | **0.0077** | ** |
| Hypertension | -9.4506 | 5.4717 | ±10.9435 | -1.727 | 0.0841 | . |
| High cholesterol | +0.5568 | 5.2437 | ±10.4875 | +0.106 | 0.9154 |  |
| Kidney disease | -0.7416 | 7.8524 | ±15.7048 | -0.094 | 0.9248 |  |
| **Circulatory disease** | **+16.1193** | 7.5812 | ±15.1624 | **+2.126** | **0.0335** | * |
| Avg. daily time < 54 (%) | -1.2663 | 2.4806 | ±4.9611 | -0.511 | 0.6097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **694**, R² = **0.0436**, Adj R² = **0.0282**, F-statistic = **2.82** (p = **0.0013**), Residual SE = **66.233** on **682** df, AIC = **7801.5**, BIC = **7856.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.5215** | 22.0616 | ±44.1232 | **+17.248** | **1.16e-66** | *** |
| Education: graduate level (vs college) | -0.9173 | 5.6629 | ±11.3258 | -0.162 | 0.8713 |  |
| Education: high school or below (vs college) | -10.5854 | 7.7035 | ±15.4070 | -1.374 | 0.1694 |  |
| **Site: UCSD (vs UAB)** | **-18.3371** | 6.2458 | ±12.4916 | **-2.936** | **0.0033** | ** |
| Site: UW (vs UAB) | +1.3776 | 6.5972 | ±13.1944 | +0.209 | 0.8346 |  |
| Age (years) | +0.1811 | 0.2624 | ±0.5249 | +0.690 | 0.4902 |  |
| **BMI (kg/m2)** | **-0.9513** | 0.3587 | ±0.7174 | **-2.652** | **0.0080** | ** |
| Hypertension | -9.7013 | 5.4891 | ±10.9783 | -1.767 | 0.0772 | . |
| High cholesterol | +1.6594 | 5.2607 | ±10.5214 | +0.315 | 0.7524 |  |
| Kidney disease | -0.8173 | 7.8342 | ±15.6685 | -0.104 | 0.9169 |  |
| **Circulatory disease** | **+16.8632** | 7.5911 | ±15.1822 | **+2.221** | **0.0263** | * |
| Time 54-69, pooled (%) | +3.6440 | 2.5760 | ±5.1520 | +1.415 | 0.1572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **694**, R² = **0.0427**, Adj R² = **0.0273**, F-statistic = **2.77** (p = **0.0016**), Residual SE = **66.262** on **682** df, AIC = **7802.1**, BIC = **7856.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.1431** | 22.0382 | ±44.0765 | **+17.295** | **5.16e-67** | *** |
| Education: graduate level (vs college) | -1.0239 | 5.6624 | ±11.3247 | -0.181 | 0.8565 |  |
| Education: high school or below (vs college) | -10.5916 | 7.7076 | ±15.4152 | -1.374 | 0.1694 |  |
| **Site: UCSD (vs UAB)** | **-18.4518** | 6.2545 | ±12.5090 | **-2.950** | **0.0032** | ** |
| Site: UW (vs UAB) | +1.2811 | 6.6053 | ±13.2106 | +0.194 | 0.8462 |  |
| Age (years) | +0.1817 | 0.2626 | ±0.5252 | +0.692 | 0.4889 |  |
| **BMI (kg/m2)** | **-0.9555** | 0.3591 | ±0.7182 | **-2.661** | **0.0078** | ** |
| Hypertension | -9.6769 | 5.4841 | ±10.9682 | -1.765 | 0.0776 | . |
| High cholesterol | +1.5214 | 5.2664 | ±10.5328 | +0.289 | 0.7727 |  |
| Kidney disease | -0.8439 | 7.8400 | ±15.6801 | -0.108 | 0.9143 |  |
| **Circulatory disease** | **+16.7467** | 7.5869 | ±15.1737 | **+2.207** | **0.0273** | * |
| Avg. daily time 54-69 (%) | +2.8936 | 2.2010 | ±4.4020 | +1.315 | 0.1886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **694**, R² = **0.0416**, Adj R² = **0.0261**, F-statistic = **2.69** (p = **0.0021**), Residual SE = **66.302** on **682** df, AIC = **7803.0**, BIC = **7857.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.0092** | 22.0853 | ±44.1707 | **+17.252** | **1.09e-66** | *** |
| Education: graduate level (vs college) | -1.1430 | 5.6705 | ±11.3409 | -0.202 | 0.8403 |  |
| Education: high school or below (vs college) | -10.6746 | 7.7239 | ±15.4478 | -1.382 | 0.1670 |  |
| **Site: UCSD (vs UAB)** | **-18.6321** | 6.2578 | ±12.5155 | **-2.977** | **0.0029** | ** |
| Site: UW (vs UAB) | +1.0057 | 6.6124 | ±13.2247 | +0.152 | 0.8791 |  |
| Age (years) | +0.1864 | 0.2623 | ±0.5246 | +0.711 | 0.4773 |  |
| **BMI (kg/m2)** | **-0.9442** | 0.3591 | ±0.7181 | **-2.629** | **0.0086** | ** |
| Hypertension | -9.5592 | 5.4787 | ±10.9573 | -1.745 | 0.0810 | . |
| High cholesterol | +1.2928 | 5.2700 | ±10.5401 | +0.245 | 0.8062 |  |
| Kidney disease | -0.7278 | 7.8446 | ±15.6892 | -0.093 | 0.9261 |  |
| **Circulatory disease** | **+16.5600** | 7.5911 | ±15.1821 | **+2.182** | **0.0291** | * |
| Time < 70 (%) | +1.6087 | 1.7147 | ±3.4294 | +0.938 | 0.3481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **694**, R² = **0.0415**, Adj R² = **0.0261**, F-statistic = **2.69** (p = **0.0022**), Residual SE = **66.305** on **682** df, AIC = **7803.0**, BIC = **7857.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.3783** | 22.0589 | ±44.1179 | **+17.289** | **5.69e-67** | *** |
| Education: graduate level (vs college) | -1.1947 | 5.6674 | ±11.3348 | -0.211 | 0.8330 |  |
| Education: high school or below (vs college) | -10.6703 | 7.7193 | ±15.4386 | -1.382 | 0.1669 |  |
| **Site: UCSD (vs UAB)** | **-18.6685** | 6.2632 | ±12.5264 | **-2.981** | **0.0029** | ** |
| Site: UW (vs UAB) | +1.0055 | 6.6161 | ±13.2322 | +0.152 | 0.8792 |  |
| Age (years) | +0.1869 | 0.2623 | ±0.5247 | +0.712 | 0.4762 |  |
| **BMI (kg/m2)** | **-0.9507** | 0.3591 | ±0.7182 | **-2.647** | **0.0081** | ** |
| Hypertension | -9.5790 | 5.4764 | ±10.9529 | -1.749 | 0.0803 | . |
| High cholesterol | +1.2752 | 5.2716 | ±10.5432 | +0.242 | 0.8089 |  |
| Kidney disease | -0.7847 | 7.8467 | ±15.6933 | -0.100 | 0.9203 |  |
| **Circulatory disease** | **+16.5268** | 7.5849 | ±15.1698 | **+2.179** | **0.0293** | * |
| Avg. daily time < 70 (%) | +1.4700 | 1.4209 | ±2.8418 | +1.035 | 0.3009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.63** (p = **0.0027**), Residual SE = **66.336** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.6241** | 26.8053 | ±53.6106 | **+14.088** | **4.52e-45** | *** |
| Education: graduate level (vs college) | -1.7368 | 5.7360 | ±11.4719 | -0.303 | 0.7621 |  |
| Education: high school or below (vs college) | -10.8164 | 7.6893 | ±15.3786 | -1.407 | 0.1595 |  |
| **Site: UCSD (vs UAB)** | **-19.2909** | 6.2337 | ±12.4673 | **-3.095** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1165 | 6.5376 | ±13.0753 | +0.018 | 0.9858 |  |
| Age (years) | +0.1911 | 0.2620 | ±0.5241 | +0.729 | 0.4657 |  |
| **BMI (kg/m2)** | **-0.9404** | 0.3640 | ±0.7279 | **-2.584** | **0.0098** | ** |
| Hypertension | -9.4183 | 5.4725 | ±10.9451 | -1.721 | 0.0852 | . |
| High cholesterol | +0.6437 | 5.2039 | ±10.4077 | +0.124 | 0.9016 |  |
| Kidney disease | -0.6158 | 7.8947 | ±15.7895 | -0.078 | 0.9378 |  |
| **Circulatory disease** | **+16.3115** | 7.6181 | ±15.2362 | **+2.141** | **0.0323** | * |
| Time 54-250, pooled (%) | +0.0518 | 0.1553 | ±0.3106 | +0.333 | 0.7389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+378.2323** | 27.1214 | ±54.2429 | **+13.946** | **3.33e-44** | *** |
| Education: graduate level (vs college) | -1.7060 | 5.7344 | ±11.4687 | -0.298 | 0.7661 |  |
| Education: high school or below (vs college) | -10.8474 | 7.6896 | ±15.3793 | -1.411 | 0.1583 |  |
| **Site: UCSD (vs UAB)** | **-19.2743** | 6.2356 | ±12.4711 | **-3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1525 | 6.5347 | ±13.0695 | +0.023 | 0.9814 |  |
| Age (years) | +0.1926 | 0.2619 | ±0.5239 | +0.735 | 0.4621 |  |
| **BMI (kg/m2)** | **-0.9420** | 0.3641 | ±0.7281 | **-2.587** | **0.0097** | ** |
| Hypertension | -9.4293 | 5.4729 | ±10.9458 | -1.723 | 0.0849 | . |
| High cholesterol | +0.6508 | 5.2039 | ±10.4077 | +0.125 | 0.9005 |  |
| Kidney disease | -0.6211 | 7.9054 | ±15.8107 | -0.079 | 0.9374 |  |
| **Circulatory disease** | **+16.2957** | 7.6222 | ±15.2444 | **+2.138** | **0.0325** | * |
| Avg. daily time 54-250 (%) | +0.0443 | 0.1585 | ±0.3170 | +0.280 | 0.7797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **694**, R² = **0.0409**, Adj R² = **0.0254**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.326** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.1694** | 22.0505 | ±44.1009 | **+17.332** | **2.72e-67** | *** |
| Education: graduate level (vs college) | -1.5546 | 5.6789 | ±11.3578 | -0.274 | 0.7843 |  |
| Education: high school or below (vs college) | -10.6172 | 7.8113 | ±15.6226 | -1.359 | 0.1741 |  |
| **Site: UCSD (vs UAB)** | **-19.3626** | 6.2465 | ±12.4931 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.1957 | 6.5820 | ±13.1639 | +0.030 | 0.9763 |  |
| Age (years) | +0.2086 | 0.2630 | ±0.5260 | +0.793 | 0.4277 |  |
| **BMI (kg/m2)** | **-0.9095** | 0.3724 | ±0.7448 | **-2.442** | **0.0146** | * |
| Hypertension | -9.4391 | 5.4757 | ±10.9515 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6837 | 5.2066 | ±10.4132 | +0.131 | 0.8955 |  |
| Kidney disease | -0.4699 | 7.9289 | ±15.8578 | -0.059 | 0.9527 |  |
| **Circulatory disease** | **+16.3877** | 7.5665 | ±15.1330 | **+2.166** | **0.0303** | * |
| Time 181-250, pooled (%) | -0.0979 | 0.1915 | ±0.3830 | -0.512 | 0.6090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.329** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.2108** | 22.0545 | ±44.1090 | **+17.330** | **2.78e-67** | *** |
| Education: graduate level (vs college) | -1.5444 | 5.6807 | ±11.3615 | -0.272 | 0.7857 |  |
| Education: high school or below (vs college) | -10.6380 | 7.8241 | ±15.6482 | -1.360 | 0.1739 |  |
| **Site: UCSD (vs UAB)** | **-19.3671** | 6.2561 | ±12.5123 | **-3.096** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1906 | 6.5877 | ±13.1754 | +0.029 | 0.9769 |  |
| Age (years) | +0.2064 | 0.2631 | ±0.5261 | +0.785 | 0.4326 |  |
| **BMI (kg/m2)** | **-0.9151** | 0.3724 | ±0.7449 | **-2.457** | **0.0140** | * |
| Hypertension | -9.4422 | 5.4767 | ±10.9533 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6925 | 5.2074 | ±10.4147 | +0.133 | 0.8942 |  |
| Kidney disease | -0.4957 | 7.9306 | ±15.8612 | -0.063 | 0.9502 |  |
| **Circulatory disease** | **+16.3452** | 7.5684 | ±15.1367 | **+2.160** | **0.0308** | * |
| Avg. daily time 181-250 (%) | -0.0841 | 0.1874 | ±0.3747 | -0.449 | 0.6535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **694**, R² = **0.0409**, Adj R² = **0.0254**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.327** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.7440** | 22.0340 | ±44.0680 | **+17.371** | **1.38e-67** | *** |
| Education: graduate level (vs college) | -1.7437 | 5.6816 | ±11.3631 | -0.307 | 0.7589 |  |
| Education: high school or below (vs college) | -10.5673 | 7.7603 | ±15.5206 | -1.362 | 0.1733 |  |
| **Site: UCSD (vs UAB)** | **-19.4042** | 6.2474 | ±12.4948 | **-3.106** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0416 | 6.5789 | ±13.1577 | +0.006 | 0.9950 |  |
| Age (years) | +0.1973 | 0.2619 | ±0.5239 | +0.753 | 0.4513 |  |
| **BMI (kg/m2)** | **-0.9145** | 0.3725 | ±0.7449 | **-2.455** | **0.0141** | * |
| Hypertension | -9.4034 | 5.4714 | ±10.9429 | -1.719 | 0.0857 | . |
| High cholesterol | +0.6389 | 5.2033 | ±10.4066 | +0.123 | 0.9023 |  |
| Kidney disease | -0.4517 | 7.9370 | ±15.8740 | -0.057 | 0.9546 |  |
| **Circulatory disease** | **+16.4489** | 7.5971 | ±15.1942 | **+2.165** | **0.0304** | * |
| Time > 180 (%) | -0.0561 | 0.1082 | ±0.2164 | -0.518 | 0.6042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.330** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.6334** | 22.0355 | ±44.0709 | **+17.364** | **1.53e-67** | *** |
| Education: graduate level (vs college) | -1.7077 | 5.6795 | ±11.3589 | -0.301 | 0.7637 |  |
| Education: high school or below (vs college) | -10.6100 | 7.7665 | ±15.5330 | -1.366 | 0.1719 |  |
| **Site: UCSD (vs UAB)** | **-19.3923** | 6.2548 | ±12.5096 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0741 | 6.5798 | ±13.1595 | +0.011 | 0.9910 |  |
| Age (years) | +0.1977 | 0.2620 | ±0.5240 | +0.755 | 0.4504 |  |
| **BMI (kg/m2)** | **-0.9192** | 0.3725 | ±0.7449 | **-2.468** | **0.0136** | * |
| Hypertension | -9.4173 | 5.4725 | ±10.9450 | -1.721 | 0.0853 | . |
| High cholesterol | +0.6505 | 5.2036 | ±10.4072 | +0.125 | 0.9005 |  |
| Kidney disease | -0.4710 | 7.9469 | ±15.8937 | -0.059 | 0.9527 |  |
| **Circulatory disease** | **+16.4089** | 7.5970 | ±15.1939 | **+2.160** | **0.0308** | * |
| Avg. daily time > 180 (%) | -0.0486 | 0.1078 | ±0.2156 | -0.451 | 0.6523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.338** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.2283** | 22.0445 | ±44.0891 | **+17.339** | **2.39e-67** | *** |
| Education: graduate level (vs college) | -1.4492 | 5.6973 | ±11.3946 | -0.254 | 0.7992 |  |
| Education: high school or below (vs college) | -11.1664 | 7.7598 | ±15.5195 | -1.439 | 0.1501 |  |
| **Site: UCSD (vs UAB)** | **-19.0541** | 6.2712 | ±12.5424 | **-3.038** | **0.0024** | ** |
| Site: UW (vs UAB) | +0.4043 | 6.5759 | ±13.1518 | +0.061 | 0.9510 |  |
| Age (years) | +0.1988 | 0.2620 | ±0.5239 | +0.759 | 0.4478 |  |
| **BMI (kg/m2)** | **-0.9721** | 0.3758 | ±0.7517 | **-2.586** | **0.0097** | ** |
| Hypertension | -9.4704 | 5.4802 | ±10.9605 | -1.728 | 0.0840 | . |
| High cholesterol | +0.7419 | 5.2089 | ±10.4177 | +0.142 | 0.8867 |  |
| Kidney disease | -0.8103 | 7.8961 | ±15.7923 | -0.103 | 0.9183 |  |
| **Circulatory disease** | **+16.0586** | 7.6053 | ±15.2107 | **+2.111** | **0.0347** | * |
| Nocturnal time > 180 (%) | +0.0221 | 0.0978 | ±0.1956 | +0.226 | 0.8215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.336** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.7568** | 22.0414 | ±44.0827 | **+17.365** | **1.51e-67** | *** |
| Education: graduate level (vs college) | -1.7231 | 5.7330 | ±11.4660 | -0.301 | 0.7638 |  |
| Education: high school or below (vs college) | -10.8226 | 7.6906 | ±15.3812 | -1.407 | 0.1594 |  |
| **Site: UCSD (vs UAB)** | **-19.2792** | 6.2323 | ±12.4646 | **-3.093** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1339 | 6.5358 | ±13.0717 | +0.020 | 0.9837 |  |
| Age (years) | +0.1913 | 0.2621 | ±0.5241 | +0.730 | 0.4653 |  |
| **BMI (kg/m2)** | **-0.9408** | 0.3641 | ±0.7283 | **-2.584** | **0.0098** | ** |
| Hypertension | -9.4203 | 5.4729 | ±10.9458 | -1.721 | 0.0852 | . |
| High cholesterol | +0.6517 | 5.2034 | ±10.4068 | +0.125 | 0.9003 |  |
| Kidney disease | -0.6210 | 7.8951 | ±15.7903 | -0.079 | 0.9373 |  |
| **Circulatory disease** | **+16.3064** | 7.6201 | ±15.2402 | **+2.140** | **0.0324** | * |
| Time > 250 (%) | -0.0489 | 0.1553 | ±0.3106 | -0.315 | 0.7527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.6440** | 22.0386 | ±44.0771 | **+17.362** | **1.59e-67** | *** |
| Education: graduate level (vs college) | -1.6985 | 5.7320 | ±11.4640 | -0.296 | 0.7670 |  |
| Education: high school or below (vs college) | -10.8491 | 7.6907 | ±15.3814 | -1.411 | 0.1583 |  |
| **Site: UCSD (vs UAB)** | **-19.2669** | 6.2340 | ±12.4680 | **-3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1636 | 6.5329 | ±13.0659 | +0.025 | 0.9800 |  |
| Age (years) | +0.1927 | 0.2620 | ±0.5239 | +0.736 | 0.4619 |  |
| **BMI (kg/m2)** | **-0.9422** | 0.3641 | ±0.7282 | **-2.588** | **0.0097** | ** |
| Hypertension | -9.4306 | 5.4731 | ±10.9461 | -1.723 | 0.0849 | . |
| High cholesterol | +0.6569 | 5.2034 | ±10.4068 | +0.126 | 0.8995 |  |
| Kidney disease | -0.6247 | 7.9054 | ±15.8107 | -0.079 | 0.9370 |  |
| **Circulatory disease** | **+16.2934** | 7.6239 | ±15.2478 | **+2.137** | **0.0326** | * |
| Avg. daily time > 250 (%) | -0.0429 | 0.1585 | ±0.3170 | -0.271 | 0.7868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 692; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0987**, F-statistic = **8.57** (p = **2.95e-13**), Residual SE = **17.463** on **681** df, AIC = **5933.1**, BIC = **5983.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3603** | 5.7369 | ±11.4738 | **+11.393** | **4.53e-30** | *** |
| Education: graduate level (vs college) | -2.2336 | 1.5020 | ±3.0041 | -1.487 | 0.1370 |  |
| Education: high school or below (vs college) | +2.8033 | 1.9940 | ±3.9880 | +1.406 | 0.1598 |  |
| Site: UCSD (vs UAB) | +3.5406 | 1.8239 | ±3.6478 | +1.941 | 0.0522 | . |
| Site: UW (vs UAB) | +1.0064 | 1.6008 | ±3.2016 | +0.629 | 0.5295 |  |
| **Age (years)** | **-0.3799** | 0.0661 | ±0.1321 | **-5.751** | **8.86e-09** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0987 | ±0.1973 | **+4.160** | **3.19e-05** | *** |
| Hypertension | -0.3276 | 1.5404 | ±3.0808 | -0.213 | 0.8316 |  |
| High cholesterol | +1.2435 | 1.4558 | ±2.9116 | +0.854 | 0.3930 |  |
| Kidney disease | -1.1705 | 1.9537 | ±3.9074 | -0.599 | 0.5491 |  |
| Circulatory disease | -2.4329 | 1.8320 | ±3.6641 | -1.328 | 0.1842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **692**, R² = **0.1530**, Adj R² = **0.1393**, F-statistic = **11.16** (p = **3.44e-19**), Residual SE = **17.065** on **680** df, AIC = **5902.2**, BIC = **5956.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9034** | 6.3705 | ±12.7411 | **+7.676** | **1.64e-14** | *** |
| Education: graduate level (vs college) | -1.5421 | 1.4881 | ±2.9762 | -1.036 | 0.3001 |  |
| Education: high school or below (vs college) | +1.3988 | 1.9350 | ±3.8699 | +0.723 | 0.4697 |  |
| **Site: UCSD (vs UAB)** | **+3.8141** | 1.7956 | ±3.5912 | **+2.124** | **0.0337** | * |
| Site: UW (vs UAB) | +1.7337 | 1.5839 | ±3.1679 | +1.095 | 0.2737 |  |
| **Age (years)** | **-0.3770** | 0.0642 | ±0.1284 | **-5.872** | **4.31e-09** | *** |
| **BMI (kg/m2)** | **+0.3046** | 0.0990 | ±0.1980 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.8258 | 1.5082 | ±3.0165 | -0.547 | 0.5840 |  |
| High cholesterol | +1.0824 | 1.4302 | ±2.8603 | +0.757 | 0.4491 |  |
| Kidney disease | -0.9954 | 1.9051 | ±3.8102 | -0.523 | 0.6013 |  |
| Circulatory disease | -2.7526 | 1.7957 | ±3.5914 | -1.533 | 0.1253 |  |
| **HbA1c (%)** | **+2.8794** | 0.4818 | ±0.9635 | **+5.977** | **2.27e-09** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **692**, R² = **0.1462**, Adj R² = **0.1324**, F-statistic = **10.59** (p = **4.20e-18**), Residual SE = **17.133** on **680** df, AIC = **5907.7**, BIC = **5962.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.1816** | 6.3266 | ±12.6531 | **+8.406** | **4.24e-17** | *** |
| Education: graduate level (vs college) | -1.8713 | 1.4902 | ±2.9804 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.5696 | 1.9182 | ±3.8364 | +0.818 | 0.4132 |  |
| **Site: UCSD (vs UAB)** | **+3.9645** | 1.8113 | ±3.6226 | **+2.189** | **0.0286** | * |
| Site: UW (vs UAB) | +1.6115 | 1.5895 | ±3.1791 | +1.014 | 0.3107 |  |
| **Age (years)** | **-0.3721** | 0.0642 | ±0.1283 | **-5.799** | **6.68e-09** | *** |
| **BMI (kg/m2)** | **+0.3260** | 0.0989 | ±0.1979 | **+3.295** | **9.84e-04** | *** |
| Hypertension | -0.6532 | 1.5234 | ±3.0467 | -0.429 | 0.6681 |  |
| High cholesterol | +1.2992 | 1.4408 | ±2.8815 | +0.902 | 0.3672 |  |
| Kidney disease | -1.5618 | 1.9210 | ±3.8419 | -0.813 | 0.4162 |  |
| Circulatory disease | -3.0821 | 1.8051 | ±3.6102 | -1.707 | 0.0877 | . |
| **Mean glucose (mg/dL)** | **+0.0886** | 0.0191 | ±0.0382 | **+4.639** | **3.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **692**, R² = **0.1462**, Adj R² = **0.1324**, F-statistic = **10.59** (p = **4.20e-18**), Residual SE = **17.133** on **680** df, AIC = **5907.7**, BIC = **5962.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9148** | 7.9039 | ±15.8077 | **+5.177** | **2.26e-07** | *** |
| Education: graduate level (vs college) | -1.8713 | 1.4902 | ±2.9804 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.5696 | 1.9182 | ±3.8364 | +0.818 | 0.4132 |  |
| **Site: UCSD (vs UAB)** | **+3.9645** | 1.8113 | ±3.6226 | **+2.189** | **0.0286** | * |
| Site: UW (vs UAB) | +1.6115 | 1.5895 | ±3.1791 | +1.014 | 0.3107 |  |
| **Age (years)** | **-0.3721** | 0.0642 | ±0.1283 | **-5.799** | **6.68e-09** | *** |
| **BMI (kg/m2)** | **+0.3260** | 0.0989 | ±0.1979 | **+3.295** | **9.84e-04** | *** |
| Hypertension | -0.6532 | 1.5234 | ±3.0467 | -0.429 | 0.6681 |  |
| High cholesterol | +1.2992 | 1.4408 | ±2.8815 | +0.902 | 0.3672 |  |
| Kidney disease | -1.5618 | 1.9210 | ±3.8419 | -0.813 | 0.4162 |  |
| Circulatory disease | -3.0821 | 1.8051 | ±3.6102 | -1.707 | 0.0877 | . |
| **GMI (%)** | **+3.7060** | 0.7989 | ±1.5977 | **+4.639** | **3.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **692**, R² = **0.1381**, Adj R² = **0.1241**, F-statistic = **9.90** (p = **8.26e-17**), Residual SE = **17.215** on **680** df, AIC = **5914.3**, BIC = **5968.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.6797** | 6.2708 | ±12.5416 | **+8.879** | **6.73e-19** | *** |
| Education: graduate level (vs college) | -1.8378 | 1.5034 | ±3.0069 | -1.222 | 0.2216 |  |
| Education: high school or below (vs college) | +1.8135 | 1.9186 | ±3.8372 | +0.945 | 0.3445 |  |
| **Site: UCSD (vs UAB)** | **+3.8850** | 1.8204 | ±3.6408 | **+2.134** | **0.0328** | * |
| Site: UW (vs UAB) | +1.3668 | 1.5895 | ±3.1790 | +0.860 | 0.3898 |  |
| **Age (years)** | **-0.3636** | 0.0650 | ±0.1299 | **-5.597** | **2.18e-08** | *** |
| **BMI (kg/m2)** | **+0.3196** | 0.0998 | ±0.1996 | **+3.203** | **0.0014** | ** |
| Hypertension | -0.5615 | 1.5282 | ±3.0564 | -0.367 | 0.7133 |  |
| High cholesterol | +1.3592 | 1.4504 | ±2.9007 | +0.937 | 0.3487 |  |
| Kidney disease | -1.1757 | 1.9288 | ±3.8576 | -0.610 | 0.5422 |  |
| Circulatory disease | -2.9891 | 1.8114 | ±3.6229 | -1.650 | 0.0989 | . |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0735** | 0.0183 | ±0.0366 | **+4.012** | **6.03e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1307**, Adj R² = **0.1166**, F-statistic = **9.29** (p = **1.19e-15**), Residual SE = **17.289** on **680** df, AIC = **5920.2**, BIC = **5974.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6598** | 6.0344 | ±12.0689 | **+9.721** | **2.46e-22** | *** |
| Education: graduate level (vs college) | -1.8400 | 1.5021 | ±3.0042 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +1.9583 | 1.9786 | ±3.9573 | +0.990 | 0.3223 |  |
| **Site: UCSD (vs UAB)** | **+3.9935** | 1.8249 | ±3.6499 | **+2.188** | **0.0286** | * |
| Site: UW (vs UAB) | +1.8782 | 1.6280 | ±3.2560 | +1.154 | 0.2486 |  |
| **Age (years)** | **-0.3860** | 0.0645 | ±0.1290 | **-5.985** | **2.16e-09** | *** |
| **BMI (kg/m2)** | **+0.3642** | 0.0998 | ±0.1995 | **+3.650** | **2.62e-04** | *** |
| Hypertension | -0.7123 | 1.5469 | ±3.0938 | -0.460 | 0.6452 |  |
| High cholesterol | +1.4649 | 1.4575 | ±2.9150 | +1.005 | 0.3149 |  |
| Kidney disease | -2.4178 | 1.9612 | ±3.9225 | -1.233 | 0.2177 |  |
| Circulatory disease | -2.7522 | 1.8178 | ±3.6356 | -1.514 | 0.1300 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.2208** | 0.0631 | ±0.1262 | **+3.500** | **4.65e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1296**, Adj R² = **0.1155**, F-statistic = **9.21** (p = **1.72e-15**), Residual SE = **17.299** on **680** df, AIC = **5921.0**, BIC = **5975.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5798** | 6.0789 | ±12.1579 | **+9.637** | **5.61e-22** | *** |
| Education: graduate level (vs college) | -1.9114 | 1.4967 | ±2.9934 | -1.277 | 0.2016 |  |
| Education: high school or below (vs college) | +1.8953 | 1.9939 | ±3.9878 | +0.951 | 0.3418 |  |
| **Site: UCSD (vs UAB)** | **+3.9760** | 1.8235 | ±3.6469 | **+2.180** | **0.0292** | * |
| Site: UW (vs UAB) | +1.7846 | 1.6294 | ±3.2588 | +1.095 | 0.2734 |  |
| **Age (years)** | **-0.3892** | 0.0646 | ±0.1292 | **-6.023** | **1.71e-09** | *** |
| **BMI (kg/m2)** | **+0.3779** | 0.0994 | ±0.1987 | **+3.803** | **1.43e-04** | *** |
| Hypertension | -0.6693 | 1.5489 | ±3.0978 | -0.432 | 0.6657 |  |
| High cholesterol | +1.4337 | 1.4569 | ±2.9138 | +0.984 | 0.3251 |  |
| Kidney disease | -2.4856 | 1.9772 | ±3.9544 | -1.257 | 0.2087 |  |
| Circulatory disease | -2.7083 | 1.8168 | ±3.6336 | -1.491 | 0.1360 |  |
| **Avg. daily SD (mg/dL)** | **+0.2443** | 0.0739 | ±0.1477 | **+3.308** | **9.40e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0974**, F-statistic = **7.78** (p = **8.90e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.7653** | 6.4391 | ±12.8782 | **+10.213** | **1.73e-24** | *** |
| Education: graduate level (vs college) | -2.2452 | 1.5065 | ±3.0130 | -1.490 | 0.1361 |  |
| Education: high school or below (vs college) | +2.8121 | 1.9984 | ±3.9967 | +1.407 | 0.1594 |  |
| Site: UCSD (vs UAB) | +3.5252 | 1.8298 | ±3.6597 | +1.927 | 0.0540 | . |
| Site: UW (vs UAB) | +0.9777 | 1.6206 | ±3.2413 | +0.603 | 0.5463 |  |
| **Age (years)** | **-0.3793** | 0.0663 | ±0.1326 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0988 | ±0.1977 | **+4.152** | **3.29e-05** | *** |
| Hypertension | -0.3168 | 1.5452 | ±3.0904 | -0.205 | 0.8376 |  |
| High cholesterol | +1.2320 | 1.4589 | ±2.9179 | +0.844 | 0.3984 |  |
| Kidney disease | -1.1195 | 1.9920 | ±3.9840 | -0.562 | 0.5741 |  |
| Circulatory disease | -2.4360 | 1.8345 | ±3.6690 | -1.328 | 0.1842 |  |
| CV (%) | -0.0182 | 0.1284 | ±0.2569 | -0.141 | 0.8876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0975**, F-statistic = **7.78** (p = **8.77e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0931** | 6.5416 | ±13.0832 | **+10.104** | **5.33e-24** | *** |
| Education: graduate level (vs college) | -2.2184 | 1.5049 | ±3.0097 | -1.474 | 0.1404 |  |
| Education: high school or below (vs college) | +2.7916 | 2.0024 | ±4.0049 | +1.394 | 0.1633 |  |
| Site: UCSD (vs UAB) | +3.5550 | 1.8281 | ±3.6562 | +1.945 | 0.0518 | . |
| Site: UW (vs UAB) | +1.0450 | 1.6207 | ±3.2413 | +0.645 | 0.5190 |  |
| **Age (years)** | **-0.3806** | 0.0661 | ±0.1322 | **-5.758** | **8.52e-09** | *** |
| **BMI (kg/m2)** | **+0.4107** | 0.0989 | ±0.1978 | **+4.153** | **3.29e-05** | *** |
| Hypertension | -0.3446 | 1.5457 | ±3.0914 | -0.223 | 0.8236 |  |
| High cholesterol | +1.2518 | 1.4584 | ±2.9167 | +0.858 | 0.3907 |  |
| Kidney disease | -1.2420 | 1.9810 | ±3.9620 | -0.627 | 0.5307 |  |
| Circulatory disease | -2.4355 | 1.8358 | ±3.6716 | -1.327 | 0.1846 |  |
| Mean / SD ratio | -0.1581 | 0.7058 | ±1.4117 | -0.224 | 0.8227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1119**, Adj R² = **0.0975**, F-statistic = **7.79** (p = **8.70e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1543** | 6.4244 | ±12.8489 | **+10.297** | **7.25e-25** | *** |
| Education: graduate level (vs college) | -2.2198 | 1.5031 | ±3.0063 | -1.477 | 0.1397 |  |
| Education: high school or below (vs college) | +2.7868 | 2.0037 | ±4.0073 | +1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | +3.5520 | 1.8280 | ±3.6560 | +1.943 | 0.0520 | . |
| Site: UW (vs UAB) | +1.0456 | 1.6172 | ±3.2344 | +0.647 | 0.5179 |  |
| **Age (years)** | **-0.3811** | 0.0662 | ±0.1324 | **-5.758** | **8.51e-09** | *** |
| **BMI (kg/m2)** | **+0.4117** | 0.0991 | ±0.1983 | **+4.152** | **3.29e-05** | *** |
| Hypertension | -0.3467 | 1.5461 | ±3.0921 | -0.224 | 0.8226 |  |
| High cholesterol | +1.2559 | 1.4591 | ±2.9182 | +0.861 | 0.3894 |  |
| Kidney disease | -1.2479 | 1.9870 | ±3.9739 | -0.628 | 0.5300 |  |
| Circulatory disease | -2.4286 | 1.8362 | ±3.6724 | -1.323 | 0.1860 |  |
| Avg. daily mean/SD | -0.1470 | 0.5600 | ±1.1200 | -0.263 | 0.7929 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **692**, R² = **0.1163**, Adj R² = **0.1020**, F-statistic = **8.13** (p = **1.90e-13**), Residual SE = **17.431** on **680** df, AIC = **5931.6**, BIC = **5986.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5723** | 6.9375 | ±13.8750 | **+8.443** | **3.10e-17** | *** |
| Education: graduate level (vs college) | -2.0193 | 1.5017 | ±3.0035 | -1.345 | 0.1787 |  |
| Education: high school or below (vs college) | +2.6325 | 1.9882 | ±3.9763 | +1.324 | 0.1855 |  |
| **Site: UCSD (vs UAB)** | **+3.8207** | 1.8386 | ±3.6773 | **+2.078** | **0.0377** | * |
| Site: UW (vs UAB) | +1.5113 | 1.6426 | ±3.2852 | +0.920 | 0.3575 |  |
| **Age (years)** | **-0.3708** | 0.0656 | ±0.1313 | **-5.648** | **1.62e-08** | *** |
| **BMI (kg/m2)** | **+0.4055** | 0.0993 | ±0.1987 | **+4.082** | **4.47e-05** | *** |
| Hypertension | -0.2571 | 1.5427 | ±3.0855 | -0.167 | 0.8676 |  |
| High cholesterol | +1.4286 | 1.4698 | ±2.9396 | +0.972 | 0.3311 |  |
| Kidney disease | -1.4311 | 1.9710 | ±3.9421 | -0.726 | 0.4678 |  |
| Circulatory disease | -2.4466 | 1.8267 | ±3.6534 | -1.339 | 0.1805 |  |
| MAG (mg/dL/h) | +0.1313 | 0.0731 | ±0.1462 | +1.796 | 0.0725 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **692**, R² = **0.1232**, Adj R² = **0.1091**, F-statistic = **8.69** (p = **1.66e-14**), Residual SE = **17.362** on **680** df, AIC = **5926.1**, BIC = **5980.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.8926** | 6.5268 | ±13.0536 | **+8.717** | **2.86e-18** | *** |
| Education: graduate level (vs college) | -1.9878 | 1.5014 | ±3.0027 | -1.324 | 0.1855 |  |
| Education: high school or below (vs college) | +2.0766 | 1.9964 | ±3.9927 | +1.040 | 0.2983 |  |
| **Site: UCSD (vs UAB)** | **+3.9718** | 1.8296 | ±3.6593 | **+2.171** | **0.0299** | * |
| Site: UW (vs UAB) | +1.6680 | 1.6375 | ±3.2750 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.3798** | 0.0651 | ±0.1302 | **-5.832** | **5.48e-09** | *** |
| **BMI (kg/m2)** | **+0.3944** | 0.0991 | ±0.1981 | **+3.981** | **6.86e-05** | *** |
| Hypertension | -0.4405 | 1.5470 | ±3.0939 | -0.285 | 0.7758 |  |
| High cholesterol | +1.4240 | 1.4620 | ±2.9240 | +0.974 | 0.3301 |  |
| Kidney disease | -2.2098 | 1.9838 | ±3.9677 | -1.114 | 0.2653 |  |
| Circulatory disease | -2.6264 | 1.8236 | ±3.6472 | -1.440 | 0.1498 |  |
| **Avg. daily range (mg/dL)** | **+0.0580** | 0.0212 | ±0.0423 | **+2.740** | **0.0061** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **692**, R² = **0.1271**, Adj R² = **0.1130**, F-statistic = **9.00** (p = **4.17e-15**), Residual SE = **17.324** on **680** df, AIC = **5923.0**, BIC = **5977.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5211** | 5.7876 | ±11.5753 | **+10.803** | **3.35e-27** | *** |
| Education: graduate level (vs college) | -1.7622 | 1.5193 | ±3.0386 | -1.160 | 0.2461 |  |
| Education: high school or below (vs college) | +2.4680 | 1.9422 | ±3.8845 | +1.271 | 0.2038 |  |
| **Site: UCSD (vs UAB)** | **+3.7463** | 1.8235 | ±3.6470 | **+2.054** | **0.0399** | * |
| Site: UW (vs UAB) | +1.5880 | 1.6074 | ±3.2149 | +0.988 | 0.3232 |  |
| **Age (years)** | **-0.3705** | 0.0652 | ±0.1304 | **-5.684** | **1.32e-08** | *** |
| **BMI (kg/m2)** | **+0.3583** | 0.0987 | ±0.1975 | **+3.628** | **2.85e-04** | *** |
| Hypertension | -0.7368 | 1.5444 | ±3.0888 | -0.477 | 0.6333 |  |
| High cholesterol | +1.4080 | 1.4605 | ±2.9210 | +0.964 | 0.3350 |  |
| Kidney disease | -1.4871 | 1.9410 | ±3.8820 | -0.766 | 0.4436 |  |
| Circulatory disease | -2.8757 | 1.8289 | ±3.6578 | -1.572 | 0.1159 |  |
| **SD of daily means (mg/dL)** | **+0.2912** | 0.0837 | ±0.1673 | **+3.481** | **5.00e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **692**, R² = **0.1498**, Adj R² = **0.1360**, F-statistic = **10.89** (p = **1.12e-18**), Residual SE = **17.097** on **680** df, AIC = **5904.8**, BIC = **5959.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0467** | 6.1317 | ±12.2634 | **+12.891** | **5.03e-38** | *** |
| Education: graduate level (vs college) | -1.8141 | 1.4893 | ±2.9787 | -1.218 | 0.2232 |  |
| Education: high school or below (vs college) | +1.5223 | 1.9194 | ±3.8387 | +0.793 | 0.4277 |  |
| **Site: UCSD (vs UAB)** | **+4.1926** | 1.8185 | ±3.6371 | **+2.305** | **0.0211** | * |
| Site: UW (vs UAB) | +1.8177 | 1.5903 | ±3.1806 | +1.143 | 0.2530 |  |
| **Age (years)** | **-0.3797** | 0.0642 | ±0.1285 | **-5.910** | **3.42e-09** | *** |
| **BMI (kg/m2)** | **+0.3074** | 0.0997 | ±0.1993 | **+3.085** | **0.0020** | ** |
| Hypertension | -0.6078 | 1.5275 | ±3.0550 | -0.398 | 0.6907 |  |
| High cholesterol | +1.4808 | 1.4454 | ±2.8908 | +1.024 | 0.3056 |  |
| Kidney disease | -1.7998 | 1.9195 | ±3.8390 | -0.938 | 0.3484 |  |
| Circulatory disease | -3.0750 | 1.7980 | ±3.5960 | -1.710 | 0.0872 | . |
| **Time in range 70-180, pooled (%)** | **-0.1502** | 0.0295 | ±0.0590 | **-5.087** | **3.65e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **692**, R² = **0.1485**, Adj R² = **0.1347**, F-statistic = **10.78** (p = **1.80e-18**), Residual SE = **17.110** on **680** df, AIC = **5905.8**, BIC = **5960.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.9119** | 6.1523 | ±12.3046 | **+12.826** | **1.17e-37** | *** |
| Education: graduate level (vs college) | -1.8604 | 1.4905 | ±2.9811 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.5099 | 1.9203 | ±3.8405 | +0.786 | 0.4317 |  |
| **Site: UCSD (vs UAB)** | **+4.2303** | 1.8210 | ±3.6419 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | +1.8127 | 1.5914 | ±3.1828 | +1.139 | 0.2547 |  |
| **Age (years)** | **-0.3814** | 0.0644 | ±0.1288 | **-5.923** | **3.15e-09** | *** |
| **BMI (kg/m2)** | **+0.3079** | 0.1000 | ±0.2000 | **+3.079** | **0.0021** | ** |
| Hypertension | -0.5834 | 1.5281 | ±3.0561 | -0.382 | 0.7026 |  |
| High cholesterol | +1.4661 | 1.4459 | ±2.8919 | +1.014 | 0.3106 |  |
| Kidney disease | -1.8462 | 1.9224 | ±3.8447 | -0.960 | 0.3369 |  |
| Circulatory disease | -3.0485 | 1.8003 | ±3.6007 | -1.693 | 0.0904 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.1465** | 0.0293 | ±0.0586 | **-5.002** | **5.67e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1128**, Adj R² = **0.0984**, F-statistic = **7.86** (p = **6.34e-13**), Residual SE = **17.466** on **680** df, AIC = **5934.3**, BIC = **5988.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.8652** | 5.8029 | ±11.6058 | **+11.350** | **7.38e-30** | *** |
| Education: graduate level (vs college) | -2.2682 | 1.5064 | ±3.0128 | -1.506 | 0.1321 |  |
| Education: high school or below (vs college) | +2.7308 | 1.9989 | ±3.9978 | +1.366 | 0.1719 |  |
| Site: UCSD (vs UAB) | +3.4535 | 1.8292 | ±3.6584 | +1.888 | 0.0590 | . |
| Site: UW (vs UAB) | +0.9320 | 1.6086 | ±3.2171 | +0.579 | 0.5623 |  |
| **Age (years)** | **-0.3818** | 0.0663 | ±0.1326 | **-5.758** | **8.49e-09** | *** |
| **BMI (kg/m2)** | **+0.4108** | 0.0991 | ±0.1982 | **+4.146** | **3.39e-05** | *** |
| Hypertension | -0.2784 | 1.5416 | ±3.0832 | -0.181 | 0.8567 |  |
| High cholesterol | +1.1715 | 1.4603 | ±2.9207 | +0.802 | 0.4224 |  |
| Kidney disease | -1.1793 | 1.9571 | ±3.9142 | -0.603 | 0.5468 |  |
| Circulatory disease | -2.3546 | 1.8302 | ±3.6604 | -1.286 | 0.1983 |  |
| Any reading < 54 during wear (0/1) | -1.3828 | 1.5834 | ±3.1668 | -0.873 | 0.3825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1120**, Adj R² = **0.0977**, F-statistic = **7.80** (p = **8.17e-13**), Residual SE = **17.473** on **680** df, AIC = **5934.9**, BIC = **5989.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5129** | 5.7571 | ±11.5143 | **+11.379** | **5.30e-30** | *** |
| Education: graduate level (vs college) | -2.2740 | 1.5046 | ±3.0092 | -1.511 | 0.1307 |  |
| Education: high school or below (vs college) | +2.7532 | 1.9977 | ±3.9954 | +1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +3.4846 | 1.8286 | ±3.6573 | +1.906 | 0.0567 | . |
| Site: UW (vs UAB) | +0.9365 | 1.6102 | ±3.2204 | +0.582 | 0.5608 |  |
| **Age (years)** | **-0.3787** | 0.0662 | ±0.1323 | **-5.723** | **1.04e-08** | *** |
| **BMI (kg/m2)** | **+0.4079** | 0.0993 | ±0.1985 | **+4.109** | **3.97e-05** | *** |
| Hypertension | -0.3271 | 1.5413 | ±3.0827 | -0.212 | 0.8320 |  |
| High cholesterol | +1.1898 | 1.4601 | ±2.9202 | +0.815 | 0.4151 |  |
| Kidney disease | -1.1825 | 1.9542 | ±3.9085 | -0.605 | 0.5451 |  |
| Circulatory disease | -2.4614 | 1.8335 | ±3.6671 | -1.342 | 0.1795 |  |
| Time < 54 (%) | -0.5112 | 1.3113 | ±2.6227 | -0.390 | 0.6967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1126**, Adj R² = **0.0982**, F-statistic = **7.84** (p = **6.83e-13**), Residual SE = **17.468** on **680** df, AIC = **5934.4**, BIC = **5988.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5688** | 5.7546 | ±11.5092 | **+11.394** | **4.47e-30** | *** |
| Education: graduate level (vs college) | -2.2923 | 1.5033 | ±3.0066 | -1.525 | 0.1273 |  |
| Education: high school or below (vs college) | +2.7124 | 1.9955 | ±3.9910 | +1.359 | 0.1741 |  |
| Site: UCSD (vs UAB) | +3.4410 | 1.8298 | ±3.6596 | +1.881 | 0.0600 | . |
| Site: UW (vs UAB) | +0.8715 | 1.6111 | ±3.2223 | +0.541 | 0.5886 |  |
| **Age (years)** | **-0.3782** | 0.0662 | ±0.1323 | **-5.717** | **1.09e-08** | *** |
| **BMI (kg/m2)** | **+0.4082** | 0.0991 | ±0.1983 | **+4.117** | **3.83e-05** | *** |
| Hypertension | -0.3159 | 1.5401 | ±3.0801 | -0.205 | 0.8375 |  |
| High cholesterol | +1.1358 | 1.4588 | ±2.9175 | +0.779 | 0.4362 |  |
| Kidney disease | -1.1693 | 1.9541 | ±3.9082 | -0.598 | 0.5496 |  |
| Circulatory disease | -2.4822 | 1.8323 | ±3.6645 | -1.355 | 0.1755 |  |
| Avg. daily time < 54 (%) | -0.9999 | 1.0347 | ±2.0694 | -0.966 | 0.3338 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1123**, Adj R² = **0.0979**, F-statistic = **7.82** (p = **7.56e-13**), Residual SE = **17.471** on **680** df, AIC = **5934.7**, BIC = **5989.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5536** | 5.7651 | ±11.5301 | **+11.371** | **5.84e-30** | *** |
| Education: graduate level (vs college) | -2.3025 | 1.5069 | ±3.0138 | -1.528 | 0.1265 |  |
| Education: high school or below (vs college) | +2.7474 | 1.9931 | ±3.9862 | +1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +3.4392 | 1.8261 | ±3.6521 | +1.883 | 0.0596 | . |
| Site: UW (vs UAB) | +0.8885 | 1.6175 | ±3.2350 | +0.549 | 0.5828 |  |
| **Age (years)** | **-0.3780** | 0.0663 | ±0.1326 | **-5.703** | **1.18e-08** | *** |
| **BMI (kg/m2)** | **+0.4100** | 0.0991 | ±0.1982 | **+4.136** | **3.53e-05** | *** |
| Hypertension | -0.3006 | 1.5513 | ±3.1025 | -0.194 | 0.8464 |  |
| High cholesterol | +1.1430 | 1.4577 | ±2.9154 | +0.784 | 0.4330 |  |
| Kidney disease | -1.1577 | 1.9541 | ±3.9083 | -0.592 | 0.5536 |  |
| Circulatory disease | -2.5036 | 1.8399 | ±3.6798 | -1.361 | 0.1736 |  |
| Time 54-69, pooled (%) | -0.4015 | 1.1048 | ±2.2096 | -0.363 | 0.7163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **692**, R² = **0.1124**, Adj R² = **0.0981**, F-statistic = **7.83** (p = **7.17e-13**), Residual SE = **17.469** on **680** df, AIC = **5934.6**, BIC = **5989.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5291** | 5.7526 | ±11.5052 | **+11.391** | **4.63e-30** | *** |
| Education: graduate level (vs college) | -2.3103 | 1.5056 | ±3.0111 | -1.535 | 0.1249 |  |
| Education: high school or below (vs college) | +2.7329 | 1.9914 | ±3.9828 | +1.372 | 0.1699 |  |
| Site: UCSD (vs UAB) | +3.4233 | 1.8280 | ±3.6560 | +1.873 | 0.0611 | . |
| Site: UW (vs UAB) | +0.8626 | 1.6199 | ±3.2398 | +0.533 | 0.5944 |  |
| **Age (years)** | **-0.3775** | 0.0663 | ±0.1327 | **-5.691** | **1.27e-08** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0990 | ±0.1980 | **+4.146** | **3.38e-05** | *** |
| Hypertension | -0.2946 | 1.5512 | ±3.1024 | -0.190 | 0.8494 |  |
| High cholesterol | +1.1272 | 1.4562 | ±2.9124 | +0.774 | 0.4389 |  |
| Kidney disease | -1.1502 | 1.9548 | ±3.9096 | -0.588 | 0.5563 |  |
| Circulatory disease | -2.5116 | 1.8393 | ±3.6787 | -1.366 | 0.1721 |  |
| Avg. daily time 54-69 (%) | -0.4269 | 1.0180 | ±2.0360 | -0.419 | 0.6749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **692**, R² = **0.1123**, Adj R² = **0.0979**, F-statistic = **7.82** (p = **7.43e-13**), Residual SE = **17.470** on **680** df, AIC = **5934.6**, BIC = **5989.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6012** | 5.7715 | ±11.5431 | **+11.366** | **6.15e-30** | *** |
| Education: graduate level (vs college) | -2.3110 | 1.5074 | ±3.0148 | -1.533 | 0.1253 |  |
| Education: high school or below (vs college) | +2.7300 | 1.9948 | ±3.9897 | +1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | +3.4287 | 1.8284 | ±3.6569 | +1.875 | 0.0608 | . |
| Site: UW (vs UAB) | +0.8734 | 1.6189 | ±3.2377 | +0.540 | 0.5895 |  |
| **Age (years)** | **-0.3778** | 0.0663 | ±0.1326 | **-5.698** | **1.21e-08** | *** |
| **BMI (kg/m2)** | **+0.4086** | 0.0994 | ±0.1988 | **+4.111** | **3.95e-05** | *** |
| Hypertension | -0.3065 | 1.5456 | ±3.0913 | -0.198 | 0.8428 |  |
| High cholesterol | +1.1337 | 1.4588 | ±2.9175 | +0.777 | 0.4371 |  |
| Kidney disease | -1.1679 | 1.9533 | ±3.9067 | -0.598 | 0.5499 |  |
| Circulatory disease | -2.5045 | 1.8373 | ±3.6747 | -1.363 | 0.1728 |  |
| Time < 70 (%) | -0.3089 | 0.6625 | ±1.3250 | -0.466 | 0.6410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **692**, R² = **0.1126**, Adj R² = **0.0983**, F-statistic = **7.84** (p = **6.70e-13**), Residual SE = **17.467** on **680** df, AIC = **5934.4**, BIC = **5988.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5808** | 5.7570 | ±11.5139 | **+11.392** | **4.61e-30** | *** |
| Education: graduate level (vs college) | -2.3206 | 1.5050 | ±3.0101 | -1.542 | 0.1231 |  |
| Education: high school or below (vs college) | +2.7099 | 1.9924 | ±3.9847 | +1.360 | 0.1738 |  |
| Site: UCSD (vs UAB) | +3.4039 | 1.8298 | ±3.6596 | +1.860 | 0.0628 | . |
| Site: UW (vs UAB) | +0.8342 | 1.6205 | ±3.2411 | +0.515 | 0.6067 |  |
| **Age (years)** | **-0.3772** | 0.0663 | ±0.1326 | **-5.690** | **1.27e-08** | *** |
| **BMI (kg/m2)** | **+0.4096** | 0.0991 | ±0.1983 | **+4.132** | **3.59e-05** | *** |
| Hypertension | -0.2951 | 1.5470 | ±3.0939 | -0.191 | 0.8487 |  |
| High cholesterol | +1.1046 | 1.4576 | ±2.9152 | +0.758 | 0.4485 |  |
| Kidney disease | -1.1527 | 1.9539 | ±3.9078 | -0.590 | 0.5552 |  |
| Circulatory disease | -2.5182 | 1.8370 | ±3.6740 | -1.371 | 0.1704 |  |
| Avg. daily time < 70 (%) | -0.3651 | 0.6659 | ±1.3319 | -0.548 | 0.5835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1281**, Adj R² = **0.1140**, F-statistic = **9.08** (p = **3.00e-15**), Residual SE = **17.315** on **680** df, AIC = **5922.3**, BIC = **5976.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.5253** | 7.0705 | ±14.1409 | **+11.106** | **1.17e-28** | *** |
| Education: graduate level (vs college) | -1.7916 | 1.5115 | ±3.0230 | -1.185 | 0.2359 |  |
| Education: high school or below (vs college) | +2.1065 | 1.9461 | ±3.8922 | +1.082 | 0.2791 |  |
| **Site: UCSD (vs UAB)** | **+3.8356** | 1.8224 | ±3.6448 | **+2.105** | **0.0353** | * |
| Site: UW (vs UAB) | +1.5844 | 1.6119 | ±3.2239 | +0.983 | 0.3257 |  |
| **Age (years)** | **-0.3623** | 0.0649 | ±0.1299 | **-5.579** | **2.41e-08** | *** |
| **BMI (kg/m2)** | **+0.3735** | 0.0989 | ±0.1979 | **+3.775** | **1.60e-04** | *** |
| Hypertension | -0.5163 | 1.5338 | ±3.0676 | -0.337 | 0.7364 |  |
| High cholesterol | +1.4046 | 1.4557 | ±2.9113 | +0.965 | 0.3346 |  |
| Kidney disease | -1.4483 | 1.9425 | ±3.8850 | -0.746 | 0.4559 |  |
| Circulatory disease | -2.7589 | 1.8091 | ±3.6183 | -1.525 | 0.1273 |  |
| **Time 54-250, pooled (%)** | **-0.1454** | 0.0487 | ±0.0974 | **-2.988** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1282**, Adj R² = **0.1141**, F-statistic = **9.09** (p = **2.82e-15**), Residual SE = **17.313** on **680** df, AIC = **5922.1**, BIC = **5976.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0038** | 7.1838 | ±14.3675 | **+10.998** | **3.93e-28** | *** |
| Education: graduate level (vs college) | -1.7997 | 1.5107 | ±3.0214 | -1.191 | 0.2335 |  |
| Education: high school or below (vs college) | +2.1041 | 1.9457 | ±3.8913 | +1.081 | 0.2795 |  |
| **Site: UCSD (vs UAB)** | **+3.8428** | 1.8221 | ±3.6443 | **+2.109** | **0.0349** | * |
| Site: UW (vs UAB) | +1.5684 | 1.6107 | ±3.2213 | +0.974 | 0.3302 |  |
| **Age (years)** | **-0.3643** | 0.0649 | ±0.1299 | **-5.610** | **2.03e-08** | *** |
| **BMI (kg/m2)** | **+0.3721** | 0.0992 | ±0.1984 | **+3.750** | **1.77e-04** | *** |
| Hypertension | -0.5023 | 1.5329 | ±3.0659 | -0.328 | 0.7432 |  |
| High cholesterol | +1.4083 | 1.4554 | ±2.9109 | +0.968 | 0.3333 |  |
| Kidney disease | -1.4923 | 1.9430 | ±3.8859 | -0.768 | 0.4424 |  |
| Circulatory disease | -2.7791 | 1.8099 | ±3.6198 | -1.535 | 0.1247 |  |
| **Avg. daily time 54-250 (%)** | **-0.1483** | 0.0499 | ±0.0998 | **-2.971** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1457**, Adj R² = **0.1319**, F-statistic = **10.54** (p = **5.12e-18**), Residual SE = **17.139** on **680** df, AIC = **5908.1**, BIC = **5962.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6206** | 5.6793 | ±11.3587 | **+11.554** | **7.02e-31** | *** |
| Education: graduate level (vs college) | -2.3331 | 1.4807 | ±2.9614 | -1.576 | 0.1151 |  |
| Education: high school or below (vs college) | +1.8801 | 1.9665 | ±3.9330 | +0.956 | 0.3390 |  |
| **Site: UCSD (vs UAB)** | **+4.0311** | 1.8146 | ±3.6293 | **+2.221** | **0.0263** | * |
| Site: UW (vs UAB) | +1.2765 | 1.5749 | ±3.1497 | +0.811 | 0.4176 |  |
| **Age (years)** | **-0.4072** | 0.0650 | ±0.1301 | **-6.262** | **3.80e-10** | *** |
| **BMI (kg/m2)** | **+0.3073** | 0.1007 | ±0.2013 | **+3.052** | **0.0023** | ** |
| Hypertension | -0.4468 | 1.5323 | ±3.0646 | -0.292 | 0.7706 |  |
| High cholesterol | +1.2963 | 1.4426 | ±2.8852 | +0.899 | 0.3689 |  |
| Kidney disease | -1.7059 | 1.9146 | ±3.8292 | -0.891 | 0.3729 |  |
| Circulatory disease | -2.9590 | 1.8204 | ±3.6408 | -1.625 | 0.1041 |  |
| **Time 181-250, pooled (%)** | **+0.2381** | 0.0478 | ±0.0955 | **+4.985** | **6.21e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **692**, R² = **0.1438**, Adj R² = **0.1300**, F-statistic = **10.38** (p = **1.02e-17**), Residual SE = **17.158** on **680** df, AIC = **5909.6**, BIC = **5964.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5646** | 5.6845 | ±11.3689 | **+11.534** | **8.89e-31** | *** |
| Education: graduate level (vs college) | -2.3602 | 1.4845 | ±2.9690 | -1.590 | 0.1119 |  |
| Education: high school or below (vs college) | +1.8328 | 1.9617 | ±3.9233 | +0.934 | 0.3501 |  |
| **Site: UCSD (vs UAB)** | **+4.0840** | 1.8182 | ±3.6364 | **+2.246** | **0.0247** | * |
| Site: UW (vs UAB) | +1.3189 | 1.5782 | ±3.1564 | +0.836 | 0.4033 |  |
| **Age (years)** | **-0.4047** | 0.0651 | ±0.1302 | **-6.217** | **5.06e-10** | *** |
| **BMI (kg/m2)** | **+0.3104** | 0.1009 | ±0.2018 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.4390 | 1.5335 | ±3.0671 | -0.286 | 0.7747 |  |
| High cholesterol | +1.2744 | 1.4439 | ±2.8878 | +0.883 | 0.3775 |  |
| Kidney disease | -1.7137 | 1.9191 | ±3.8382 | -0.893 | 0.3719 |  |
| Circulatory disease | -2.8984 | 1.8248 | ±3.6496 | -1.588 | 0.1122 |  |
| **Avg. daily time 181-250 (%)** | **+0.2269** | 0.0468 | ±0.0936 | **+4.850** | **1.23e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **692**, R² = **0.1497**, Adj R² = **0.1360**, F-statistic = **10.88** (p = **1.15e-18**), Residual SE = **17.098** on **680** df, AIC = **5904.8**, BIC = **5959.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.1577** | 5.6461 | ±11.2922 | **+11.363** | **6.38e-30** | *** |
| Education: graduate level (vs college) | -1.8553 | 1.4885 | ±2.9771 | -1.246 | 0.2126 |  |
| Education: high school or below (vs college) | +1.4989 | 1.9187 | ±3.8374 | +0.781 | 0.4347 |  |
| **Site: UCSD (vs UAB)** | **+4.1327** | 1.8171 | ±3.6342 | **+2.274** | **0.0229** | * |
| Site: UW (vs UAB) | +1.7461 | 1.5875 | ±3.1751 | +1.100 | 0.2714 |  |
| **Age (years)** | **-0.3786** | 0.0643 | ±0.1285 | **-5.892** | **3.81e-09** | *** |
| **BMI (kg/m2)** | **+0.3075** | 0.0998 | ±0.1996 | **+3.080** | **0.0021** | ** |
| Hypertension | -0.5950 | 1.5269 | ±3.0538 | -0.390 | 0.6968 |  |
| High cholesterol | +1.4257 | 1.4434 | ±2.8868 | +0.988 | 0.3233 |  |
| Kidney disease | -1.7927 | 1.9186 | ±3.8373 | -0.934 | 0.3501 |  |
| Circulatory disease | -3.1035 | 1.7987 | ±3.5975 | -1.725 | 0.0845 | . |
| **Time > 180 (%)** | **+0.1488** | 0.0293 | ±0.0586 | **+5.075** | **3.87e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1487**, Adj R² = **0.1349**, F-statistic = **10.80** (p = **1.70e-18**), Residual SE = **17.109** on **680** df, AIC = **5905.7**, BIC = **5960.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.3522** | 5.6558 | ±11.3117 | **+11.378** | **5.38e-30** | *** |
| Education: graduate level (vs college) | -1.8969 | 1.4898 | ±2.9796 | -1.273 | 0.2029 |  |
| Education: high school or below (vs college) | +1.4787 | 1.9190 | ±3.8381 | +0.771 | 0.4410 |  |
| **Site: UCSD (vs UAB)** | **+4.1725** | 1.8194 | ±3.6389 | **+2.293** | **0.0218** | * |
| Site: UW (vs UAB) | +1.7401 | 1.5885 | ±3.1769 | +1.095 | 0.2733 |  |
| **Age (years)** | **-0.3803** | 0.0644 | ±0.1288 | **-5.906** | **3.50e-09** | *** |
| **BMI (kg/m2)** | **+0.3081** | 0.1002 | ±0.2003 | **+3.076** | **0.0021** | ** |
| Hypertension | -0.5692 | 1.5272 | ±3.0543 | -0.373 | 0.7094 |  |
| High cholesterol | +1.4096 | 1.4434 | ±2.8868 | +0.977 | 0.3288 |  |
| Kidney disease | -1.8359 | 1.9212 | ±3.8423 | -0.956 | 0.3393 |  |
| Circulatory disease | -3.0797 | 1.8012 | ±3.6025 | -1.710 | 0.0873 | . |
| **Avg. daily time > 180 (%)** | **+0.1458** | 0.0291 | ±0.0583 | **+5.007** | **5.53e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1342**, Adj R² = **0.1202**, F-statistic = **9.58** (p = **3.30e-16**), Residual SE = **17.253** on **680** df, AIC = **5917.3**, BIC = **5971.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.9687** | 5.7250 | ±11.4500 | **+11.348** | **7.57e-30** | *** |
| Education: graduate level (vs college) | -1.7654 | 1.5106 | ±3.0211 | -1.169 | 0.2425 |  |
| Education: high school or below (vs college) | +1.9905 | 1.9230 | ±3.8460 | +1.035 | 0.3006 |  |
| **Site: UCSD (vs UAB)** | **+4.0421** | 1.8295 | ±3.6590 | **+2.209** | **0.0271** | * |
| Site: UW (vs UAB) | +1.4573 | 1.5940 | ±3.1880 | +0.914 | 0.3606 |  |
| **Age (years)** | **-0.3683** | 0.0655 | ±0.1310 | **-5.624** | **1.87e-08** | *** |
| **BMI (kg/m2)** | **+0.3153** | 0.1013 | ±0.2025 | **+3.114** | **0.0018** | ** |
| Hypertension | -0.4885 | 1.5363 | ±3.0727 | -0.318 | 0.7505 |  |
| High cholesterol | +1.5001 | 1.4557 | ±2.9113 | +1.031 | 0.3028 |  |
| Kidney disease | -1.4048 | 1.9355 | ±3.8710 | -0.726 | 0.4680 |  |
| Circulatory disease | -2.9301 | 1.8066 | ±3.6132 | -1.622 | 0.1048 |  |
| **Nocturnal time > 180 (%)** | **+0.1046** | 0.0266 | ±0.0532 | **+3.935** | **8.33e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1282**, Adj R² = **0.1141**, F-statistic = **9.09** (p = **2.85e-15**), Residual SE = **17.313** on **680** df, AIC = **5922.1**, BIC = **5976.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0199** | 5.7147 | ±11.4293 | **+11.203** | **3.95e-29** | *** |
| Education: graduate level (vs college) | -1.8011 | 1.5109 | ±3.0217 | -1.192 | 0.2332 |  |
| Education: high school or below (vs college) | +2.0891 | 1.9460 | ±3.8920 | +1.074 | 0.2830 |  |
| **Site: UCSD (vs UAB)** | **+3.8209** | 1.8216 | ±3.6433 | **+2.098** | **0.0359** | * |
| Site: UW (vs UAB) | +1.5669 | 1.6104 | ±3.2208 | +0.973 | 0.3305 |  |
| **Age (years)** | **-0.3619** | 0.0649 | ±0.1299 | **-5.572** | **2.51e-08** | *** |
| **BMI (kg/m2)** | **+0.3726** | 0.0990 | ±0.1979 | **+3.765** | **1.66e-04** | *** |
| Hypertension | -0.5170 | 1.5336 | ±3.0672 | -0.337 | 0.7360 |  |
| High cholesterol | +1.3900 | 1.4550 | ±2.9099 | +0.955 | 0.3394 |  |
| Kidney disease | -1.4529 | 1.9425 | ±3.8851 | -0.748 | 0.4545 |  |
| Circulatory disease | -2.7685 | 1.8093 | ±3.6186 | -1.530 | 0.1260 |  |
| **Time > 250 (%)** | **+0.1461** | 0.0487 | ±0.0973 | **+3.002** | **0.0027** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **692**, R² = **0.1285**, Adj R² = **0.1144**, F-statistic = **9.11** (p = **2.59e-15**), Residual SE = **17.311** on **680** df, AIC = **5921.9**, BIC = **5976.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.1935** | 5.7204 | ±11.4409 | **+11.222** | **3.19e-29** | *** |
| Education: graduate level (vs college) | -1.8055 | 1.5102 | ±3.0205 | -1.195 | 0.2319 |  |
| Education: high school or below (vs college) | +2.0856 | 1.9453 | ±3.8906 | +1.072 | 0.2837 |  |
| **Site: UCSD (vs UAB)** | **+3.8300** | 1.8214 | ±3.6429 | **+2.103** | **0.0355** | * |
| Site: UW (vs UAB) | +1.5521 | 1.6092 | ±3.2184 | +0.965 | 0.3348 |  |
| **Age (years)** | **-0.3640** | 0.0649 | ±0.1299 | **-5.604** | **2.09e-08** | *** |
| **BMI (kg/m2)** | **+0.3715** | 0.0993 | ±0.1985 | **+3.743** | **1.82e-04** | *** |
| Hypertension | -0.5017 | 1.5326 | ±3.0651 | -0.327 | 0.7434 |  |
| High cholesterol | +1.3933 | 1.4545 | ±2.9090 | +0.958 | 0.3381 |  |
| Kidney disease | -1.4944 | 1.9429 | ±3.8858 | -0.769 | 0.4418 |  |
| Circulatory disease | -2.7889 | 1.8100 | ±3.6201 | -1.541 | 0.1234 |  |
| **Avg. daily time > 250 (%)** | **+0.1494** | 0.0500 | ±0.0999 | **+2.990** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 52 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 150 tests (samples with n >= 500), of which **38** are significant at BH q < 0.05 in the all-tests family and 40 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 690): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.131 vs 0.128 for covariates alone, gain +0.003; -362 per SD, p = 0.006, q = 0.050). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.006), %<70 (pooled) (p = 0.014), %54-69 (daily avg) (p = 0.026), %54-69 (pooled) (p = 0.040).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 690): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.150 vs 0.148 for covariates alone, gain +0.003; -0.983 per SD, p = 0.017, q = 0.087). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.017), %<70 (pooled) (p = 0.032), %54-69 (daily avg) (p = 0.040).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 692): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.150 vs 0.111 for covariates alone, gain +0.039; +1.88 per SD, p = 4.2e-08, q = 8.8e-06). FDR-robust associations (19): %181-250 (pooled) (higher outcome, +1.88 per SD, q = 8.8e-06); %181-250 (daily avg) (higher outcome, +1.84 per SD, q = 9.1e-06); %>180 (pooled) (higher outcome, +1.89 per SD, q = 9.1e-06); TIR 70-180 (pooled) (lower outcome, -1.9 per SD, q = 9.1e-06); HbA1c (higher outcome, +1.73 per SD, q = 9.1e-06); %>180 (daily avg) (higher outcome, +1.88 per SD, q = 9.1e-06); ....
- **Total sleep time per night (min)** (n = 694): best single predictor out of sample is **MAG** (CV R² 0.014 vs -0.005 for covariates alone, gain +0.019; -10 per SD, p = 7.5e-05, q = 0.001). FDR-robust associations (1): MAG (lower outcome, -10 per SD, q = 0.001).
- **Garmin stress score, mean (0-100)** (n = 692): best single predictor out of sample is **HbA1c** (CV R² 0.111 vs 0.069 for covariates alone, gain +0.042; +3.98 per SD, p = 2.3e-09, q = 9.5e-07). FDR-robust associations (18): HbA1c (higher outcome, +3.98 per SD, q = 9.5e-07); TIR 70-180 (pooled) (lower outcome, -3.81 per SD, q = 1.4e-05); %>180 (pooled) (higher outcome, +3.8 per SD, q = 1.4e-05); %>180 (daily avg) (higher outcome, +3.75 per SD, q = 1.7e-05); TIR 70-180 (daily avg) (lower outcome, -3.75 per SD, q = 1.7e-05); %181-250 (pooled) (higher outcome, +3.54 per SD, q = 1.7e-05); ....

**Most predictable outcomes (largest out-of-sample gain over covariates):** Garmin stress score, mean (0-100) (+0.042, via HbA1c); Resting heart-rate proxy (daily 5th pct, bpm) (+0.039, via %181-250 (pooled)); Total sleep time per night (min) (+0.019, via MAG); Steps per wear-day (+0.003, via %<70 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (8 FDR-significant / 14 raw-significant of 40); CGM level (6 FDR-significant / 6 raw-significant of 15); Band > 180 (6 FDR-significant / 6 raw-significant of 15).
Level metrics: 6 FDR-significant (6 raw); variability metrics: 8 FDR-significant (14 raw); HbA1c alone: 2 FDR-significant (3 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Resting heart-rate proxy (%181-250 (pooled), ΔAIC -6.4); Total sleep time per night (MAG, ΔAIC -9.8).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
