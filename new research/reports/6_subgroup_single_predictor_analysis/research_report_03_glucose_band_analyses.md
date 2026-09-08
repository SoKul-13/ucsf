# Phase 6 - Glucose-band analyses (54-69, 54-250, > 180 and the other bands) vs the usual 70-180 range

Glucose categories: severe hypo < 54; moderate hypo 54-69; normal / TIR 70-180; moderate hyper 181-250; severe hyper > 250 (mg/dL). Each band metric is the percentage of CGM time in the band (pooled over all valid readings, and the mean of the daily percentages over valid days), entered alone with the Phase 5 covariates. For the sparse bands < 54 and > 250 a 0/1 indicator (any reading in the band during wear) is also tested.

## 1. Are there enough people outside 54-250?

A band is called *feasible* when at least 100 participants in the population have >= 1 % of their CGM time in it; *marginal* when >= 100 have any time but fewer than 100 have >= 1 %.

| Population | Band | n | Any time in band | % of participants | >= 1% time | >= 5% time | >= 10% time | Mean % time | Median % time | 90th pct % time | Max % time | Median % time among exposed | Feasible? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Total analysis base | <54 | 2138 | 638 | 29.84 | 56 | 3 | 1 | 0.13 | 0.00 | 0.32 | 13.99 | 0.19 | marginal (>= 100 with any time, < 100 with >= 1%) |
| Total analysis base | 54-69 | 2138 | 1251 | 58.51 | 326 | 42 | 9 | 0.56 | 0.07 | 1.43 | 18.64 | 0.35 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | <70 | 2138 | 1259 | 58.89 | 377 | 57 | 16 | 0.69 | 0.07 | 1.82 | 25.08 | 0.39 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | 70-180 | 2138 | 2135 | 99.86 | 2125 | 2110 | 2100 | 87.58 | 96.42 | 99.60 | 100.00 | 96.43 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | 181-250 | 2138 | 1927 | 90.13 | 1407 | 826 | 581 | 8.69 | 2.55 | 27.97 | 71.98 | 3.51 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | >180 | 2138 | 1927 | 90.13 | 1410 | 837 | 607 | 11.73 | 2.56 | 37.64 | 100.00 | 3.59 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | >250 | 2138 | 795 | 37.18 | 461 | 240 | 159 | 3.04 | 0.00 | 5.96 | 97.08 | 1.51 | yes (>= 100 participants with >= 1% time) |
| Total analysis base | 54-250 | 2138 | 2138 | 100.00 | 2138 | 2134 | 2130 | 96.83 | 99.89 | 100.00 | 100.00 | 99.89 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | <54 | 1271 | 408 | 32.10 | 35 | 2 | 1 | 0.14 | 0.00 | 0.36 | 13.99 | 0.21 | marginal (>= 100 with any time, < 100 with >= 1%) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | 54-69 | 1271 | 828 | 65.15 | 221 | 22 | 5 | 0.59 | 0.11 | 1.50 | 18.64 | 0.35 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | <70 | 1271 | 831 | 65.38 | 253 | 34 | 10 | 0.73 | 0.14 | 1.89 | 22.09 | 0.39 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | 70-180 | 1271 | 1271 | 100.00 | 1267 | 1267 | 1267 | 95.51 | 98.11 | 99.72 | 100.00 | 98.11 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | 181-250 | 1271 | 1094 | 86.07 | 641 | 234 | 105 | 3.25 | 1.02 | 8.12 | 68.42 | 1.37 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | >180 | 1271 | 1094 | 86.07 | 643 | 240 | 114 | 3.76 | 1.02 | 8.85 | 99.54 | 1.37 | yes (>= 100 participants with >= 1% time) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | >250 | 1271 | 244 | 19.20 | 69 | 18 | 11 | 0.51 | 0.00 | 0.37 | 92.16 | 0.42 | marginal (>= 100 with any time, < 100 with >= 1%) |
| Healthy group (no diabetes + pre-diabetes / lifestyle) | 54-250 | 1271 | 1271 | 100.00 | 1271 | 1271 | 1270 | 99.34 | 100.00 | 100.00 | 100.00 | 100.00 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | <54 | 867 | 230 | 26.53 | 21 | 1 | 0 | 0.11 | 0.00 | 0.28 | 8.42 | 0.18 | marginal (>= 100 with any time, < 100 with >= 1%) |
| Non-healthy group (T2D non-insulin + T2D insulin) | 54-69 | 867 | 423 | 48.79 | 105 | 20 | 4 | 0.51 | 0.00 | 1.31 | 16.66 | 0.35 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | <70 | 867 | 428 | 49.37 | 124 | 23 | 6 | 0.62 | 0.00 | 1.68 | 25.08 | 0.42 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | 70-180 | 867 | 864 | 99.65 | 858 | 843 | 833 | 75.97 | 86.09 | 98.54 | 100.00 | 86.19 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | 181-250 | 867 | 833 | 96.08 | 766 | 592 | 476 | 16.67 | 12.07 | 40.18 | 71.98 | 13.26 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | >180 | 867 | 833 | 96.08 | 767 | 597 | 493 | 23.41 | 13.34 | 62.14 | 100.00 | 14.55 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | >250 | 867 | 551 | 63.55 | 392 | 222 | 148 | 6.74 | 0.53 | 17.67 | 97.08 | 3.02 | yes (>= 100 participants with >= 1% time) |
| Non-healthy group (T2D non-insulin + T2D insulin) | 54-250 | 867 | 867 | 100.00 | 867 | 863 | 860 | 93.15 | 99.16 | 100.00 | 100.00 | 99.16 | yes (>= 100 participants with >= 1% time) |

Total CGM readings below 54 mg/dL across the base: 7,215; above 250: 165,251.


---

## Band 70-180

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | 2138 | 2135 | **+0.01767** | 0.003736 | [0.01034, 0.02499] | **4.73** | **2.3e-06***** | *** |
| MoCA total score ~ TIR 70-180 (daily avg) | 2138 | 2134 | **+0.0173** | 0.003733 | [0.009983, 0.02461] | **4.63** | **3.6e-06***** | *** |
| Cognitive impairment ~ TIR 70-180 (pooled) | 2138 | 2135 | **-0.009435** | 0.002361 | [-0.01406, -0.004808] | **-4.00** | **6.4e-05***** | *** |
| Cognitive impairment ~ TIR 70-180 (daily avg) | 2138 | 2134 | **-0.009318** | 0.00235 | [-0.01392, -0.004711] | **-3.96** | **7.4e-05***** | *** |
| MoCA memory index score ~ TIR 70-180 (pooled) | 2138 | 2135 | **+0.008283** | 0.002884 | [0.002631, 0.01393] | **2.87** | **0.004**** | ** |
| MoCA memory index score ~ TIR 70-180 (daily avg) | 2138 | 2134 | **+0.008252** | 0.002878 | [0.002611, 0.01389] | **2.87** | **0.004**** | ** |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | 2135 | 2132 | -0.007131 | 0.005948 | [-0.01879, 0.004526] | -1.20 | 0.231 |  |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | 2135 | 2131 | -0.006853 | 0.005928 | [-0.01847, 0.004765] | -1.16 | 0.248 |  |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | 2135 | 2132 | **-0.00548** | 0.002646 | [-0.01067, -0.0002939] | **-2.07** | **0.038*** | * |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | 2135 | 2131 | **-0.005251** | 0.00264 | [-0.01043, -7.569e-05] | **-1.99** | **0.047*** | * |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | 2100 | 2097 | -0.002213 | 0.001156 | [-0.004479, 5.276e-05] | -1.91 | 0.056 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | 2100 | 2096 | -0.002196 | 0.001152 | [-0.004453, 6.099e-05] | -1.91 | 0.057 |  |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | 2100 | 2097 | -0.001304 | 0.002407 | [-0.006021, 0.003414] | -0.54 | 0.588 |  |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | 2100 | 2096 | -0.001151 | 0.002401 | [-0.005857, 0.003556] | -0.48 | 0.632 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | 2100 | 2097 | +0.003375 | 0.007036 | [-0.01042, 0.01717] | 0.48 | 0.632 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | 2100 | 2096 | +0.003113 | 0.00702 | [-0.01065, 0.01687] | 0.44 | 0.657 |  |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | 2100 | 2097 | +0.008643 | 0.02218 | [-0.03483, 0.05212] | 0.39 | 0.697 |  |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | 2100 | 2096 | +0.009775 | 0.02217 | [-0.03368, 0.05323] | 0.44 | 0.659 |  |
| Steps per wear-day ~ TIR 70-180 (pooled) | 1872 | 1869 | -6.29 | 6.578 | [-19.18, 6.602] | -0.96 | 0.339 |  |
| Steps per wear-day ~ TIR 70-180 (daily avg) | 1872 | 1869 | -6.219 | 6.545 | [-19.05, 6.61] | -0.95 | 0.342 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | 1872 | 1869 | -0.02011 | 0.01861 | [-0.05658, 0.01636] | -1.08 | 0.280 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | 1872 | 1869 | -0.01992 | 0.01855 | [-0.05627, 0.01644] | -1.07 | 0.283 |  |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | 1877 | 1874 | **-0.08406** | 0.01088 | [-0.1054, -0.06273] | **-7.73** | **1.1e-14***** | *** |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | 1877 | 1874 | **-0.08302** | 0.01082 | [-0.1042, -0.06181] | **-7.67** | **1.7e-14***** | *** |
| Total sleep time per night ~ TIR 70-180 (pooled) | 1893 | 1891 | +0.09728 | 0.0818 | [-0.06305, 0.2576] | 1.19 | 0.234 |  |
| Total sleep time per night ~ TIR 70-180 (daily avg) | 1893 | 1891 | +0.0946 | 0.08171 | [-0.06555, 0.2548] | 1.16 | 0.247 |  |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | 1879 | 1876 | **-0.1501** | 0.0224 | [-0.194, -0.1061] | **-6.70** | **2.1e-11***** | *** |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | 1879 | 1876 | **-0.1475** | 0.02228 | [-0.1911, -0.1038] | **-6.62** | **3.6e-11***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | **+0.356 [+0.208, +0.503]** | **2.3e-05 (FDR<0.05)** | **9.3e-06 (FDR<0.05)** | 0.1117 | -26.4 | -1.7 | 0.1022 \| 0.0915 |
| MoCA total score ~ TIR 70-180 (daily avg) | **+0.350 [+0.202, +0.498]** | **3.4e-05 (FDR<0.05)** | **1.1e-05 (FDR<0.05)** | 0.1113 | -25.4 | -0.8 | 0.1018 \| 0.0915 |
| Cognitive impairment ~ TIR 70-180 (pooled) | **OR 0.827 [0.753, 0.908]** | **4.2e-04 (FDR<0.05)** | **3.3e-04 (FDR<0.05)** | 0.6738 | -14.2 | -0.6 | 0.6657 \| 0.6603 |
| Cognitive impairment ~ TIR 70-180 (daily avg) | **OR 0.828 [0.754, 0.909]** | **4.7e-04 (FDR<0.05)** | **3.3e-04 (FDR<0.05)** | 0.6737 | -14.0 | -0.3 | 0.6655 \| 0.6603 |
| MoCA memory index score ~ TIR 70-180 (pooled) | **+0.167 [+0.053, +0.281]** | **0.017 (FDR<0.05)** | **0.016 (FDR<0.05)** | 0.0749 | -6.0 | -0.6 | 0.0657 \| 0.0630 |
| MoCA memory index score ~ TIR 70-180 (daily avg) | **+0.167 [+0.053, +0.281]** | **0.017 (FDR<0.05)** | **0.016 (FDR<0.05)** | 0.0749 | -6.0 | -0.6 | 0.0656 \| 0.0630 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | -0.144 [-0.379, +0.091] | 0.400 | 0.620 | 0.1035 | +0.2 | +0.4 | 0.0917 \| 0.0916 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | -0.139 [-0.374, +0.096] | 0.415 | 0.620 | 0.1035 | +0.3 | +0.5 | 0.0917 \| 0.0916 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | OR 0.895 [0.807, 0.994] | 0.111 | 0.158 | 0.6827 | -2.2 | +0.5 | 0.6693 \| 0.6681 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | OR 0.899 [0.810, 0.998] | 0.130 | 0.158 | 0.6826 | -1.8 | +0.9 | 0.6693 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | -0.045 [-0.090, +0.001] | 0.146 | 0.173 | 0.1528 | -2.9 | +8.0 | 0.1394 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | -0.045 [-0.090, +0.001] | 0.147 | 0.173 | 0.1528 | -2.9 | +8.0 | 0.1394 \| 0.1387 |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | -0.026 [-0.122, +0.069] | 0.740 | 0.982 | 0.2980 | +1.7 | +0.1 | 0.2891 \| 0.2896 |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | -0.023 [-0.119, +0.072] | 0.781 | 0.982 | 0.2980 | +1.7 | +0.2 | 0.2890 \| 0.2896 |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | +0.068 [-0.210, +0.347] | 0.781 | 0.898 | 0.2411 | +1.7 | -0.1 | 0.2301 \| 0.2307 |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | +0.063 [-0.216, +0.342] | 0.799 | 0.898 | 0.2411 | +1.8 | -0.1 | 0.2300 \| 0.2307 |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | +0.175 [-0.704, +1.053] | 0.817 | 0.868 | 0.0427 | +1.8 | +1.7 | 0.0255 \| 0.0271 |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | +0.198 [-0.684, +1.080] | 0.799 | 0.868 | 0.0427 | +1.7 | +1.7 | 0.0255 \| 0.0271 |
| Steps per wear-day ~ TIR 70-180 (pooled) | -125.480 [-382.665, +131.705] | 0.500 | 0.424 | 0.1355 | +0.5 | +8.4 | 0.1216 \| 0.1222 |
| Steps per wear-day ~ TIR 70-180 (daily avg) | -124.676 [-381.867, +132.515] | 0.502 | 0.424 | 0.1355 | +0.5 | +8.5 | 0.1216 \| 0.1222 |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | -0.401 [-1.129, +0.326] | 0.447 | 0.351 | 0.1564 | +0.3 | +8.5 | 0.1444 \| 0.1447 |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | -0.399 [-1.128, +0.330] | 0.450 | 0.351 | 0.1564 | +0.3 | +8.5 | 0.1444 \| 0.1447 |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | **-1.679 [-2.105, -1.253]** | **6.3e-13 (FDR<0.05)** | **5.2e-14 (FDR<0.05)** | 0.1929 | -73.5 | -2.3 | 0.1805 \| 0.1482 |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | **-1.667 [-2.092, -1.241]** | **7.4e-13 (FDR<0.05)** | **5.9e-14 (FDR<0.05)** | 0.1923 | -72.3 | -1.1 | 0.1800 \| 0.1482 |
| Total sleep time per night ~ TIR 70-180 (pooled) | +1.916 [-1.242, +5.074] | 0.400 | 0.403 | 0.0340 | +0.6 | +9.5 | 0.0202 \| 0.0209 |
| Total sleep time per night ~ TIR 70-180 (daily avg) | +1.872 [-1.297, +5.042] | 0.415 | 0.403 | 0.0340 | +0.6 | +9.5 | 0.0202 \| 0.0209 |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | **-2.996 [-3.872, -2.119]** | **4.6e-10 (FDR<0.05)** | **9.0e-11 (FDR<0.05)** | 0.1297 | -50.4 | +10.0 | 0.1143 \| 0.0902 |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | **-2.959 [-3.835, -2.083]** | **7.1e-10 (FDR<0.05)** | **1.2e-10 (FDR<0.05)** | 0.1290 | -49.1 | +11.3 | 0.1137 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | 1271 | 1271 | **+0.03694** | 0.0124 | [0.01264, 0.06124] | **2.98** | **0.003**** | ** |
| MoCA total score ~ TIR 70-180 (daily avg) | 1271 | 1270 | **+0.03636** | 0.01235 | [0.01215, 0.06057] | **2.94** | **0.003**** | ** |
| Cognitive impairment ~ TIR 70-180 (pooled) | 1271 | 1271 | -0.009342 | 0.006898 | [-0.02286, 0.004178] | -1.35 | 0.176 |  |
| Cognitive impairment ~ TIR 70-180 (daily avg) | 1271 | 1270 | -0.009166 | 0.006863 | [-0.02262, 0.004286] | -1.34 | 0.182 |  |
| MoCA memory index score ~ TIR 70-180 (pooled) | 1271 | 1271 | **+0.01922** | 0.007682 | [0.004165, 0.03428] | **2.50** | **0.012*** | * |
| MoCA memory index score ~ TIR 70-180 (daily avg) | 1271 | 1270 | **+0.01978** | 0.007584 | [0.004917, 0.03465] | **2.61** | **0.009**** | ** |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | 1270 | 1270 | -0.008615 | 0.02078 | [-0.04934, 0.03211] | -0.41 | 0.678 |  |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | 1270 | 1269 | -0.009281 | 0.02065 | [-0.04976, 0.0312] | -0.45 | 0.653 |  |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | 1270 | 1270 | -0.01123 | 0.007324 | [-0.02559, 0.003122] | -1.53 | 0.125 |  |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | 1270 | 1269 | -0.01104 | 0.007288 | [-0.02533, 0.003242] | -1.52 | 0.130 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | 1251 | 1251 | +0.00382 | 0.002206 | [-0.0005044, 0.008144] | 1.73 | 0.083 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | 1251 | 1250 | +0.00377 | 0.002193 | [-0.0005283, 0.008068] | 1.72 | 0.086 |  |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | 1251 | 1251 | -0.005345 | 0.006299 | [-0.01769, 0.007] | -0.85 | 0.396 |  |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | 1251 | 1250 | -0.005342 | 0.006235 | [-0.01756, 0.006878] | -0.86 | 0.392 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | 1251 | 1251 | +0.003467 | 0.01866 | [-0.03311, 0.04004] | 0.19 | 0.853 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | 1251 | 1250 | +0.002338 | 0.01846 | [-0.03385, 0.03852] | 0.13 | 0.899 |  |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | 1251 | 1251 | +0.02255 | 0.05384 | [-0.08296, 0.1281] | 0.42 | 0.675 |  |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | 1251 | 1250 | +0.02054 | 0.05378 | [-0.08488, 0.1259] | 0.38 | 0.703 |  |
| Steps per wear-day ~ TIR 70-180 (pooled) | 1125 | 1125 | +5.207 | 14.17 | [-22.57, 32.98] | 0.37 | 0.713 |  |
| Steps per wear-day ~ TIR 70-180 (daily avg) | 1125 | 1125 | +5.676 | 14.12 | [-21.99, 33.34] | 0.40 | 0.688 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | 1125 | 1125 | -0.02319 | 0.0452 | [-0.1118, 0.0654] | -0.51 | 0.608 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | 1125 | 1125 | -0.02069 | 0.04515 | [-0.1092, 0.0678] | -0.46 | 0.647 |  |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | 1128 | 1128 | **-0.08501** | 0.03465 | [-0.1529, -0.01709] | **-2.45** | **0.014*** | * |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | 1128 | 1128 | **-0.08287** | 0.03457 | [-0.1506, -0.01511] | **-2.40** | **0.017*** | * |
| Total sleep time per night ~ TIR 70-180 (pooled) | 1137 | 1137 | -0.1438 | 0.2544 | [-0.6424, 0.3548] | -0.57 | 0.572 |  |
| Total sleep time per night ~ TIR 70-180 (daily avg) | 1137 | 1137 | -0.1516 | 0.2538 | [-0.649, 0.3457] | -0.60 | 0.550 |  |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | 1130 | 1130 | -0.09275 | 0.08238 | [-0.2542, 0.06871] | -1.13 | 0.260 |  |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | 1130 | 1130 | -0.08554 | 0.08182 | [-0.2459, 0.07482] | -1.05 | 0.296 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | +0.328 [+0.112, +0.543] | 0.052 | **0.011 (FDR<0.05)** | 0.1100 | -16.2 | -2.5 | 0.0874 \| 0.0789 |
| MoCA total score ~ TIR 70-180 (daily avg) | +0.324 [+0.108, +0.540] | 0.052 | **0.011 (FDR<0.05)** | 0.1098 | -15.8 | -2.1 | 0.0871 \| 0.0789 |
| Cognitive impairment ~ TIR 70-180 (pooled) | OR 0.920 [0.816, 1.038] | 0.532 | 0.480 | 0.6608 | +0.2 | -0.1 | 0.6448 \| 0.6443 |
| Cognitive impairment ~ TIR 70-180 (daily avg) | OR 0.922 [0.818, 1.039] | 0.533 | 0.480 | 0.6607 | +0.2 | -0.0 | 0.6445 \| 0.6443 |
| MoCA memory index score ~ TIR 70-180 (pooled) | +0.171 [+0.037, +0.304] | 0.131 | **0.035 (FDR<0.05)** | 0.0751 | -3.6 | -3.0 | 0.0496 \| 0.0477 |
| MoCA memory index score ~ TIR 70-180 (daily avg) | +0.176 [+0.044, +0.309] | 0.104 | **0.028 (FDR<0.05)** | 0.0754 | -4.0 | -3.3 | 0.0498 \| 0.0477 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | -0.076 [-0.434, +0.282] | 0.932 | 0.953 | 0.0910 | +1.7 | -0.3 | 0.0631 \| 0.0675 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | -0.082 [-0.439, +0.276] | 0.932 | 0.953 | 0.0910 | +1.6 | -0.4 | 0.0632 \| 0.0675 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | OR 0.906 [0.798, 1.028] | 0.472 | 0.565 | 0.6956 | -0.2 | -1.4 | 0.6759 \| 0.6758 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | OR 0.907 [0.800, 1.029] | 0.481 | 0.565 | 0.6955 | -0.2 | -1.3 | 0.6757 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | +0.034 [-0.005, +0.073] | 0.404 | 0.265 | 0.1375 | +0.0 | -2.0 | 0.1142 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | +0.034 [-0.005, +0.072] | 0.404 | 0.265 | 0.1374 | +0.1 | -1.9 | 0.1142 \| 0.1139 |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | -0.048 [-0.158, +0.063] | 0.797 | 0.915 | 0.3101 | +1.2 | -0.8 | 0.2889 \| 0.2892 |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | -0.048 [-0.158, +0.062] | 0.794 | 0.915 | 0.3101 | +1.2 | -0.8 | 0.2889 \| 0.2892 |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | +0.031 [-0.296, +0.358] | 0.948 | 0.905 | 0.2596 | +2.0 | +2.5 | 0.2388 \| 0.2403 |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | +0.021 [-0.304, +0.346] | 0.964 | 0.905 | 0.2596 | +2.0 | +2.5 | 0.2389 \| 0.2403 |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | +0.201 [-0.741, +1.144] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | 0.0003 \| 0.0025 |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | +0.184 [-0.761, +1.130] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | 0.0004 \| 0.0025 |
| Steps per wear-day ~ TIR 70-180 (pooled) | +44.618 [-193.349, +282.584] | 0.932 | 0.958 | 0.1246 | +1.8 | +5.1 | 0.1064 \| 0.1080 |
| Steps per wear-day ~ TIR 70-180 (daily avg) | +48.810 [-189.118, +286.738] | 0.932 | 0.958 | 0.1246 | +1.8 | +5.1 | 0.1064 \| 0.1080 |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | -0.199 [-0.958, +0.560] | 0.932 | 0.931 | 0.1389 | +1.7 | +5.1 | 0.1232 \| 0.1245 |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | -0.178 [-0.939, +0.583] | 0.932 | 0.931 | 0.1388 | +1.7 | +5.2 | 0.1231 \| 0.1245 |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | -0.728 [-1.309, -0.146] | 0.137 | **0.034 (FDR<0.05)** | 0.1378 | -8.8 | +2.4 | 0.1081 \| 0.1044 |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | -0.712 [-1.294, -0.130] | 0.137 | **0.034 (FDR<0.05)** | 0.1375 | -8.4 | +2.9 | 0.1076 \| 0.1044 |
| Total sleep time per night ~ TIR 70-180 (pooled) | -1.155 [-5.159, +2.849] | 0.932 | 0.936 | 0.0208 | +1.7 | +3.7 | -0.0068 \| -0.0051 |
| Total sleep time per night ~ TIR 70-180 (daily avg) | -1.222 [-5.231, +2.787] | 0.932 | 0.936 | 0.0209 | +1.6 | +3.6 | -0.0068 \| -0.0051 |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | -0.793 [-2.174, +0.588] | 0.638 | 0.471 | 0.0746 | -0.5 | +7.2 | 0.0489 \| 0.0510 |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | -0.734 [-2.110, +0.642] | 0.681 | 0.483 | 0.0743 | -0.2 | +7.6 | 0.0487 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | 867 | 864 | **+0.009848** | 0.004539 | [0.0009518, 0.01874] | **2.17** | **0.030*** | * |
| MoCA total score ~ TIR 70-180 (daily avg) | 867 | 864 | **+0.009508** | 0.004533 | [0.0006235, 0.01839] | **2.10** | **0.036*** | * |
| Cognitive impairment ~ TIR 70-180 (pooled) | 867 | 864 | **-0.006108** | 0.002832 | [-0.01166, -0.0005577] | **-2.16** | **0.031*** | * |
| Cognitive impairment ~ TIR 70-180 (daily avg) | 867 | 864 | **-0.006034** | 0.002818 | [-0.01156, -0.0005115] | **-2.14** | **0.032*** | * |
| MoCA memory index score ~ TIR 70-180 (pooled) | 867 | 864 | +0.006725 | 0.003499 | [-0.0001342, 0.01358] | 1.92 | 0.055 |  |
| MoCA memory index score ~ TIR 70-180 (daily avg) | 867 | 864 | +0.006605 | 0.003497 | [-0.0002502, 0.01346] | 1.89 | 0.059 |  |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | 865 | 862 | -0.008358 | 0.007131 | [-0.02233, 0.005617] | -1.17 | 0.241 |  |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | 865 | 862 | -0.007867 | 0.00711 | [-0.0218, 0.006068] | -1.11 | 0.269 |  |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | 865 | 862 | -0.005522 | 0.003178 | [-0.01175, 0.0007069] | -1.74 | 0.082 |  |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | 865 | 862 | -0.005232 | 0.003169 | [-0.01144, 0.0009778] | -1.65 | 0.099 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | 849 | 846 | **-0.00291** | 0.001438 | [-0.005729, -9.191e-05] | **-2.02** | **0.043*** | * |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | 849 | 846 | **-0.00289** | 0.001428 | [-0.00569, -9.049e-05] | **-2.02** | **0.043*** | * |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | 849 | 846 | +0.0023 | 0.00312 | [-0.003816, 0.008416] | 0.74 | 0.461 |  |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | 849 | 846 | +0.00247 | 0.003114 | [-0.003633, 0.008572] | 0.79 | 0.428 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | 849 | 846 | +0.005621 | 0.008945 | [-0.01191, 0.02315] | 0.63 | 0.530 |  |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | 849 | 846 | +0.005407 | 0.008917 | [-0.01207, 0.02288] | 0.61 | 0.544 |  |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | 849 | 846 | +0.01753 | 0.02614 | [-0.03371, 0.06877] | 0.67 | 0.502 |  |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | 849 | 846 | +0.01953 | 0.02612 | [-0.03167, 0.07072] | 0.75 | 0.455 |  |
| Steps per wear-day ~ TIR 70-180 (pooled) | 747 | 744 | -4.511 | 8.234 | [-20.65, 11.63] | -0.55 | 0.584 |  |
| Steps per wear-day ~ TIR 70-180 (daily avg) | 747 | 744 | -4.636 | 8.172 | [-20.65, 11.38] | -0.57 | 0.571 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | 747 | 744 | -0.005967 | 0.02293 | [-0.05092, 0.03898] | -0.26 | 0.795 |  |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | 747 | 744 | -0.006509 | 0.02283 | [-0.05125, 0.03823] | -0.29 | 0.776 |  |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | 749 | 746 | **-0.04169** | 0.0128 | [-0.06678, -0.0166] | **-3.26** | **0.001**** | ** |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | 749 | 746 | **-0.04111** | 0.01269 | [-0.06598, -0.01623] | **-3.24** | **0.001**** | ** |
| Total sleep time per night ~ TIR 70-180 (pooled) | 756 | 754 | +0.1016 | 0.1006 | [-0.09563, 0.2988] | 1.01 | 0.313 |  |
| Total sleep time per night ~ TIR 70-180 (daily avg) | 756 | 754 | +0.1009 | 0.1004 | [-0.09601, 0.2977] | 1.00 | 0.315 |  |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | 749 | 746 | **-0.1016** | 0.02628 | [-0.1531, -0.05006] | **-3.86** | **1.1e-04***** | *** |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | 749 | 746 | **-0.1001** | 0.02611 | [-0.1512, -0.0489] | **-3.83** | **1.3e-04***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ TIR 70-180 (pooled) | +0.253 [+0.024, +0.481] | 0.159 | 0.071 | 0.0861 | -3.0 | -1.5 | 0.0581 \| 0.0541 |
| MoCA total score ~ TIR 70-180 (daily avg) | +0.246 [+0.016, +0.475] | 0.168 | 0.074 | 0.0858 | -2.7 | -1.2 | 0.0578 \| 0.0541 |
| Cognitive impairment ~ TIR 70-180 (pooled) | OR 0.855 [0.741, 0.986] | 0.160 | 0.107 | 0.6640 | -2.7 | -1.0 | 0.6438 \| 0.6425 |
| Cognitive impairment ~ TIR 70-180 (daily avg) | OR 0.856 [0.742, 0.987] | 0.161 | 0.107 | 0.6639 | -2.6 | -0.9 | 0.6440 \| 0.6425 |
| MoCA memory index score ~ TIR 70-180 (pooled) | +0.173 [-0.003, +0.349] | 0.204 | 0.122 | 0.0633 | -1.4 | +0.4 | 0.0314 \| 0.0286 |
| MoCA memory index score ~ TIR 70-180 (daily avg) | +0.171 [-0.006, +0.348] | 0.212 | 0.122 | 0.0632 | -1.3 | +0.5 | 0.0313 \| 0.0286 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (pooled) | -0.215 [-0.574, +0.144] | 0.455 | 0.578 | 0.1127 | +0.4 | +1.7 | 0.0781 \| 0.0796 |
| CES-D-10 depressive symptoms ~ TIR 70-180 (daily avg) | -0.203 [-0.564, +0.157] | 0.484 | 0.578 | 0.1125 | +0.6 | +1.8 | 0.0781 \| 0.0796 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (pooled) | OR 0.868 [0.739, 1.018] | 0.243 | 0.215 | 0.6654 | -1.0 | +2.0 | 0.6358 \| 0.6337 |
| Clinically relevant depressive symptoms ~ TIR 70-180 (daily avg) | OR 0.874 [0.744, 1.026] | 0.264 | 0.215 | 0.6651 | -0.7 | +2.3 | 0.6359 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (pooled) | -0.075 [-0.147, -0.002] | 0.182 | 0.148 | 0.1593 | -3.4 | +6.0 | 0.1329 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ TIR 70-180 (daily avg) | -0.075 [-0.147, -0.002] | 0.182 | 0.148 | 0.1592 | -3.4 | +6.0 | 0.1329 \| 0.1310 |
| Indoor temperature, mean ~ TIR 70-180 (pooled) | +0.059 [-0.098, +0.217] | 0.656 | 0.794 | 0.2507 | +1.4 | -0.3 | 0.2229 \| 0.2264 |
| Indoor temperature, mean ~ TIR 70-180 (daily avg) | +0.064 [-0.094, +0.222] | 0.640 | 0.794 | 0.2508 | +1.3 | -0.4 | 0.2230 \| 0.2264 |
| Indoor relative humidity, mean ~ TIR 70-180 (pooled) | +0.145 [-0.306, +0.596] | 0.717 | 0.938 | 0.2133 | +1.6 | -0.3 | 0.1843 \| 0.1857 |
| Indoor relative humidity, mean ~ TIR 70-180 (daily avg) | +0.140 [-0.312, +0.592] | 0.727 | 0.938 | 0.2133 | +1.6 | -0.3 | 0.1842 \| 0.1857 |
| Indoor VOC index, mean ~ TIR 70-180 (pooled) | +0.451 [-0.867, +1.769] | 0.692 | 0.599 | 0.0562 | +1.4 | +1.8 | 0.0264 \| 0.0276 |
| Indoor VOC index, mean ~ TIR 70-180 (daily avg) | +0.505 [-0.820, +1.831] | 0.656 | 0.585 | 0.0564 | +1.3 | +1.6 | 0.0266 \| 0.0276 |
| Steps per wear-day ~ TIR 70-180 (pooled) | -115.817 [-530.170, +298.536] | 0.763 | 0.751 | 0.1575 | +1.6 | +1.7 | 0.1370 \| 0.1390 |
| Steps per wear-day ~ TIR 70-180 (daily avg) | -119.774 [-533.581, +294.032] | 0.750 | 0.751 | 0.1575 | +1.6 | +1.7 | 0.1370 \| 0.1390 |
| Brisk-cadence minutes per day ~ TIR 70-180 (pooled) | -0.153 [-1.307, +1.001] | 0.873 | 0.821 | 0.1790 | +1.9 | +2.0 | 0.1526 \| 0.1546 |
| Brisk-cadence minutes per day ~ TIR 70-180 (daily avg) | -0.168 [-1.324, +0.988] | 0.865 | 0.821 | 0.1790 | +1.9 | +1.9 | 0.1525 \| 0.1546 |
| Resting heart-rate proxy ~ TIR 70-180 (pooled) | **-1.072 [-1.717, -0.427]** | **0.024 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1656 | -9.9 | -3.8 | 0.1365 \| 0.1253 |
| Resting heart-rate proxy ~ TIR 70-180 (daily avg) | **-1.063 [-1.707, -0.420]** | **0.024 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1654 | -9.7 | -3.6 | 0.1362 \| 0.1253 |
| Total sleep time per night ~ TIR 70-180 (pooled) | +2.583 [-2.433, +7.599] | 0.534 | 0.444 | 0.0376 | +1.0 | +3.9 | 0.0053 \| 0.0066 |
| Total sleep time per night ~ TIR 70-180 (daily avg) | +2.581 [-2.457, +7.620] | 0.537 | 0.444 | 0.0376 | +1.0 | +3.9 | 0.0051 \| 0.0066 |
| Garmin stress score, mean ~ TIR 70-180 (pooled) | **-2.611 [-3.935, -1.287]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1406 | -14.2 | -1.1 | 0.1120 \| 0.0947 |
| Garmin stress score, mean ~ TIR 70-180 (daily avg) | **-2.588 [-3.912, -1.265]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1403 | -13.9 | -0.8 | 0.1116 \| 0.0947 |


---

## Band 54-69

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | 2138 | 1251 | +0.01489 | 0.04337 | [-0.07012, 0.0999] | 0.34 | 0.731 |  |
| MoCA total score ~ %54-69 (daily avg) | 2138 | 1051 | +0.009357 | 0.04413 | [-0.07714, 0.09585] | 0.21 | 0.832 |  |
| Cognitive impairment ~ %54-69 (pooled) | 2138 | 1251 | +0.03119 | 0.03218 | [-0.03187, 0.09425] | 0.97 | 0.332 |  |
| Cognitive impairment ~ %54-69 (daily avg) | 2138 | 1051 | +0.03756 | 0.03167 | [-0.02451, 0.09963] | 1.19 | 0.236 |  |
| MoCA memory index score ~ %54-69 (pooled) | 2138 | 1251 | +0.00479 | 0.03608 | [-0.06593, 0.07551] | 0.13 | 0.894 |  |
| MoCA memory index score ~ %54-69 (daily avg) | 2138 | 1051 | -0.01511 | 0.037 | [-0.08763, 0.05741] | -0.41 | 0.683 |  |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | 2135 | 1250 | +0.053 | 0.07166 | [-0.08745, 0.1934] | 0.74 | 0.460 |  |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | 2135 | 1050 | +0.06801 | 0.07089 | [-0.07093, 0.2069] | 0.96 | 0.337 |  |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | 2135 | 1250 | +0.02108 | 0.03772 | [-0.05285, 0.09501] | 0.56 | 0.576 |  |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | 2135 | 1050 | +0.02161 | 0.03717 | [-0.05124, 0.09445] | 0.58 | 0.561 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | 2100 | 1226 | +0.03483 | 0.01908 | [-0.002553, 0.07222] | 1.83 | 0.068 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | 2100 | 1027 | +0.03644 | 0.01947 | [-0.001731, 0.07461] | 1.87 | 0.061 |  |
| Indoor temperature, mean ~ %54-69 (pooled) | 2100 | 1226 | +0.03829 | 0.02769 | [-0.01599, 0.09256] | 1.38 | 0.167 |  |
| Indoor temperature, mean ~ %54-69 (daily avg) | 2100 | 1027 | +0.04724 | 0.02739 | [-0.006432, 0.1009] | 1.73 | 0.085 |  |
| Indoor relative humidity, mean ~ %54-69 (pooled) | 2100 | 1226 | -0.1018 | 0.09234 | [-0.2828, 0.07918] | -1.10 | 0.270 |  |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | 2100 | 1027 | -0.107 | 0.09079 | [-0.285, 0.07091] | -1.18 | 0.238 |  |
| Indoor VOC index, mean ~ %54-69 (pooled) | 2100 | 1226 | +0.09074 | 0.2487 | [-0.3967, 0.5782] | 0.36 | 0.715 |  |
| Indoor VOC index, mean ~ %54-69 (daily avg) | 2100 | 1027 | +0.0625 | 0.2448 | [-0.4173, 0.5423] | 0.26 | 0.798 |  |
| Steps per wear-day ~ %54-69 (pooled) | 1872 | 1116 | **-146.6** | 62.73 | [-269.5, -23.62] | **-2.34** | **0.019*** | * |
| Steps per wear-day ~ %54-69 (daily avg) | 1872 | 935 | **-146.6** | 61.85 | [-267.8, -25.39] | **-2.37** | **0.018*** | * |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | 1872 | 1116 | -0.2966 | 0.1833 | [-0.6558, 0.06259] | -1.62 | 0.106 |  |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | 1872 | 935 | -0.3147 | 0.1826 | [-0.6725, 0.04312] | -1.72 | 0.085 |  |
| Resting heart-rate proxy ~ %54-69 (pooled) | 1877 | 1121 | -0.1179 | 0.1164 | [-0.346, 0.1102] | -1.01 | 0.311 |  |
| Resting heart-rate proxy ~ %54-69 (daily avg) | 1877 | 939 | -0.1198 | 0.1178 | [-0.3507, 0.1111] | -1.02 | 0.309 |  |
| Total sleep time per night ~ %54-69 (pooled) | 1893 | 1140 | +0.9811 | 0.9567 | [-0.894, 2.856] | 1.03 | 0.305 |  |
| Total sleep time per night ~ %54-69 (daily avg) | 1893 | 958 | +0.8015 | 0.9291 | [-1.02, 2.622] | 0.86 | 0.388 |  |
| Garmin stress score, mean ~ %54-69 (pooled) | 1879 | 1122 | -0.3514 | 0.2818 | [-0.9036, 0.2009] | -1.25 | 0.212 |  |
| Garmin stress score, mean ~ %54-69 (daily avg) | 1879 | 940 | -0.3685 | 0.2883 | [-0.9337, 0.1966] | -1.28 | 0.201 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | +0.021 [-0.100, +0.143] | 0.840 | 0.782 | 0.0998 | +1.9 | +26.5 | 0.0905 \| 0.0915 |
| MoCA total score ~ %54-69 (daily avg) | +0.014 [-0.112, +0.139] | 0.892 | 0.832 | 0.0998 | +2.0 | +26.6 | 0.0904 \| 0.0915 |
| Cognitive impairment ~ %54-69 (pooled) | OR 1.046 [0.955, 1.144] | 0.500 | 0.368 | 0.6684 | +1.1 | +14.7 | 0.6602 \| 0.6603 |
| Cognitive impairment ~ %54-69 (daily avg) | OR 1.056 [0.965, 1.155] | 0.401 | 0.281 | 0.6686 | +0.6 | +14.2 | 0.6604 \| 0.6603 |
| MoCA memory index score ~ %54-69 (pooled) | +0.007 [-0.094, +0.108] | 0.939 | 0.924 | 0.0715 | +2.0 | +7.4 | 0.0619 \| 0.0630 |
| MoCA memory index score ~ %54-69 (daily avg) | -0.022 [-0.127, +0.083] | 0.805 | 0.756 | 0.0715 | +1.9 | +7.2 | 0.0619 \| 0.0630 |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | +0.076 [-0.125, +0.277] | 0.630 | 0.620 | 0.1030 | +1.5 | +1.7 | 0.0911 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | +0.098 [-0.103, +0.300] | 0.500 | 0.620 | 0.1031 | +1.1 | +1.3 | 0.0913 \| 0.0916 |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | OR 1.031 [0.927, 1.146] | 0.732 | 0.687 | 0.6802 | +1.7 | +4.4 | 0.6671 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | OR 1.032 [0.928, 1.147] | 0.718 | 0.687 | 0.6802 | +1.7 | +4.4 | 0.6673 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | +0.050 [-0.004, +0.104] | 0.171 | 0.173 | 0.1535 | -4.6 | +6.3 | 0.1402 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | +0.053 [-0.003, +0.109] | 0.158 | 0.173 | 0.1538 | -5.4 | +5.5 | 0.1404 \| 0.1387 |
| Indoor temperature, mean ~ %54-69 (pooled) | +0.055 [-0.023, +0.133] | 0.322 | 0.982 | 0.2984 | +0.4 | -1.1 | 0.2895 \| 0.2896 |
| Indoor temperature, mean ~ %54-69 (daily avg) | +0.069 [-0.009, +0.147] | 0.195 | 0.801 | 0.2987 | -0.5 | -2.0 | 0.2898 \| 0.2896 |
| Indoor relative humidity, mean ~ %54-69 (pooled) | -0.146 [-0.407, +0.114] | 0.440 | 0.898 | 0.2415 | +0.8 | -1.1 | 0.2302 \| 0.2307 |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | -0.156 [-0.415, +0.103] | 0.404 | 0.898 | 0.2415 | +0.6 | -1.3 | 0.2302 \| 0.2307 |
| Indoor VOC index, mean ~ %54-69 (pooled) | +0.130 [-0.570, +0.831] | 0.834 | 0.868 | 0.0426 | +1.9 | +1.8 | 0.0262 \| 0.0271 |
| Indoor VOC index, mean ~ %54-69 (daily avg) | +0.091 [-0.607, +0.789] | 0.873 | 0.884 | 0.0426 | +1.9 | +1.9 | 0.0263 \| 0.0271 |
| Steps per wear-day ~ %54-69 (pooled) | -217.612 [-400.159, -35.066] | 0.065 | 0.083 | 0.1371 | -2.9 | +5.1 | 0.1232 \| 0.1222 |
| Steps per wear-day ~ %54-69 (daily avg) | -221.219 [-404.121, -38.317] | 0.060 | 0.083 | 0.1372 | -3.1 | +4.9 | 0.1232 \| 0.1222 |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | -0.440 [-0.974, +0.093] | 0.220 | 0.205 | 0.1567 | -0.2 | +8.0 | 0.1443 \| 0.1447 |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | -0.475 [-1.015, +0.065] | 0.195 | 0.192 | 0.1568 | -0.6 | +7.6 | 0.1444 \| 0.1447 |
| Resting heart-rate proxy ~ %54-69 (pooled) | -0.175 [-0.513, +0.163] | 0.482 | 0.371 | 0.1601 | +1.1 | +72.4 | 0.1481 \| 0.1482 |
| Resting heart-rate proxy ~ %54-69 (daily avg) | -0.181 [-0.528, +0.167] | 0.482 | 0.371 | 0.1601 | +1.1 | +72.3 | 0.1481 \| 0.1482 |
| Total sleep time per night ~ %54-69 (pooled) | +1.447 [-1.318, +4.212] | 0.480 | 0.473 | 0.0337 | +1.1 | +10.0 | 0.0205 \| 0.0209 |
| Total sleep time per night ~ %54-69 (daily avg) | +1.202 [-1.529, +3.932] | 0.556 | 0.523 | 0.0336 | +1.4 | +10.3 | 0.0203 \| 0.0209 |
| Garmin stress score, mean ~ %54-69 (pooled) | -0.521 [-1.340, +0.298] | 0.378 | 0.253 | 0.1058 | +0.3 | +60.7 | 0.0899 \| 0.0902 |
| Garmin stress score, mean ~ %54-69 (daily avg) | -0.555 [-1.407, +0.296] | 0.365 | 0.249 | 0.1059 | +0.1 | +60.5 | 0.0897 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | 1271 | 828 | +0.01442 | 0.04351 | [-0.07085, 0.09969] | 0.33 | 0.740 |  |
| MoCA total score ~ %54-69 (daily avg) | 1271 | 695 | +0.01152 | 0.04352 | [-0.07377, 0.09681] | 0.26 | 0.791 |  |
| Cognitive impairment ~ %54-69 (pooled) | 1271 | 828 | +0.0532 | 0.0431 | [-0.03126, 0.1377] | 1.23 | 0.217 |  |
| Cognitive impairment ~ %54-69 (daily avg) | 1271 | 695 | +0.05731 | 0.04265 | [-0.02628, 0.1409] | 1.34 | 0.179 |  |
| MoCA memory index score ~ %54-69 (pooled) | 1271 | 828 | +0.07024 | 0.03871 | [-0.005643, 0.1461] | 1.81 | 0.070 |  |
| MoCA memory index score ~ %54-69 (daily avg) | 1271 | 695 | +0.05337 | 0.03822 | [-0.02153, 0.1283] | 1.40 | 0.163 |  |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | 1270 | 828 | +0.02354 | 0.09993 | [-0.1723, 0.2194] | 0.24 | 0.814 |  |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | 1270 | 695 | +0.04257 | 0.1003 | [-0.154, 0.2392] | 0.42 | 0.671 |  |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | 1270 | 828 | +0.02884 | 0.05108 | [-0.07127, 0.1289] | 0.56 | 0.572 |  |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | 1270 | 695 | +0.0236 | 0.0512 | [-0.07675, 0.1239] | 0.46 | 0.645 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | 1251 | 814 | -0.001978 | 0.01753 | [-0.03633, 0.03237] | -0.11 | 0.910 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | 1251 | 682 | -0.001056 | 0.01807 | [-0.03647, 0.03436] | -0.06 | 0.953 |  |
| Indoor temperature, mean ~ %54-69 (pooled) | 1251 | 814 | +0.04401 | 0.03051 | [-0.01579, 0.1038] | 1.44 | 0.149 |  |
| Indoor temperature, mean ~ %54-69 (daily avg) | 1251 | 682 | +0.05075 | 0.03164 | [-0.01126, 0.1128] | 1.60 | 0.109 |  |
| Indoor relative humidity, mean ~ %54-69 (pooled) | 1251 | 814 | -0.1463 | 0.1007 | [-0.3437, 0.05102] | -1.45 | 0.146 |  |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | 1251 | 682 | -0.1334 | 0.1015 | [-0.3323, 0.06546] | -1.31 | 0.189 |  |
| Indoor VOC index, mean ~ %54-69 (pooled) | 1251 | 814 | -0.1084 | 0.3288 | [-0.7528, 0.5361] | -0.33 | 0.742 |  |
| Indoor VOC index, mean ~ %54-69 (daily avg) | 1251 | 682 | -0.1343 | 0.341 | [-0.8027, 0.5341] | -0.39 | 0.694 |  |
| Steps per wear-day ~ %54-69 (pooled) | 1125 | 747 | -33.59 | 87.7 | [-205.5, 138.3] | -0.38 | 0.702 |  |
| Steps per wear-day ~ %54-69 (daily avg) | 1125 | 626 | -28.61 | 89.96 | [-204.9, 147.7] | -0.32 | 0.750 |  |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | 1125 | 747 | -0.07241 | 0.2708 | [-0.6031, 0.4583] | -0.27 | 0.789 |  |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | 1125 | 626 | -0.08369 | 0.2766 | [-0.6258, 0.4584] | -0.30 | 0.762 |  |
| Resting heart-rate proxy ~ %54-69 (pooled) | 1128 | 749 | +0.003607 | 0.1461 | [-0.2828, 0.29] | 0.02 | 0.980 |  |
| Resting heart-rate proxy ~ %54-69 (daily avg) | 1128 | 627 | +0.005403 | 0.1491 | [-0.2869, 0.2977] | 0.04 | 0.971 |  |
| Total sleep time per night ~ %54-69 (pooled) | 1137 | 761 | +0.5538 | 1.091 | [-1.584, 2.691] | 0.51 | 0.612 |  |
| Total sleep time per night ~ %54-69 (daily avg) | 1137 | 637 | +0.5286 | 1.089 | [-1.606, 2.663] | 0.49 | 0.627 |  |
| Garmin stress score, mean ~ %54-69 (pooled) | 1130 | 750 | -0.07759 | 0.3633 | [-0.7896, 0.6344] | -0.21 | 0.831 |  |
| Garmin stress score, mean ~ %54-69 (daily avg) | 1130 | 628 | -0.123 | 0.3839 | [-0.8754, 0.6293] | -0.32 | 0.749 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | +0.020 [-0.099, +0.139] | 0.932 | 0.820 | 0.0973 | +1.9 | +15.6 | 0.0781 \| 0.0789 |
| MoCA total score ~ %54-69 (daily avg) | +0.016 [-0.103, +0.135] | 0.936 | 0.841 | 0.0973 | +2.0 | +15.7 | 0.0782 \| 0.0789 |
| Cognitive impairment ~ %54-69 (pooled) | OR 1.077 [0.957, 1.212] | 0.594 | 0.480 | 0.6610 | +0.5 | +0.3 | 0.6443 \| 0.6443 |
| Cognitive impairment ~ %54-69 (daily avg) | OR 1.083 [0.964, 1.218] | 0.532 | 0.480 | 0.6610 | +0.3 | +0.0 | 0.6443 \| 0.6443 |
| MoCA memory index score ~ %54-69 (pooled) | +0.098 [-0.008, +0.204] | 0.356 | 0.127 | 0.0723 | +0.1 | +0.8 | 0.0476 \| 0.0477 |
| MoCA memory index score ~ %54-69 (daily avg) | +0.075 [-0.030, +0.179] | 0.532 | 0.229 | 0.0718 | +0.9 | +1.6 | 0.0472 \| 0.0477 |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | +0.033 [-0.241, +0.307] | 0.939 | 0.953 | 0.0908 | +1.9 | -0.1 | 0.0661 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | +0.060 [-0.215, +0.335] | 0.932 | 0.953 | 0.0909 | +1.8 | -0.2 | 0.0662 \| 0.0675 |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | OR 1.041 [0.905, 1.198] | 0.932 | 0.958 | 0.6937 | +1.7 | +0.6 | 0.6725 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | OR 1.034 [0.898, 1.189] | 0.932 | 0.958 | 0.6935 | +1.8 | +0.7 | 0.6722 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | -0.003 [-0.051, +0.045] | 0.968 | 0.987 | 0.1361 | +2.0 | -0.0 | 0.1125 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | -0.001 [-0.051, +0.048] | 0.983 | 0.987 | 0.1361 | +2.0 | -0.0 | 0.1123 \| 0.1139 |
| Indoor temperature, mean ~ %54-69 (pooled) | +0.062 [-0.022, +0.146] | 0.510 | 0.771 | 0.3104 | +0.7 | -1.3 | 0.2891 \| 0.2892 |
| Indoor temperature, mean ~ %54-69 (daily avg) | +0.071 [-0.016, +0.158] | 0.441 | 0.674 | 0.3107 | +0.3 | -1.7 | 0.2892 \| 0.2892 |
| Indoor relative humidity, mean ~ %54-69 (pooled) | -0.205 [-0.482, +0.072] | 0.503 | 0.585 | 0.2605 | +0.5 | +1.0 | 0.2399 \| 0.2403 |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | -0.187 [-0.465, +0.092] | 0.542 | 0.585 | 0.2603 | +0.7 | +1.2 | 0.2396 \| 0.2403 |
| Indoor VOC index, mean ~ %54-69 (pooled) | -0.152 [-1.056, +0.752] | 0.932 | 0.784 | 0.0238 | +1.9 | +1.3 | 0.0014 \| 0.0025 |
| Indoor VOC index, mean ~ %54-69 (daily avg) | -0.188 [-1.124, +0.748] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | 0.0015 \| 0.0025 |
| Steps per wear-day ~ %54-69 (pooled) | -49.093 [-300.312, +202.126] | 0.932 | 0.958 | 0.1246 | +1.8 | +5.1 | 0.1069 \| 0.1080 |
| Steps per wear-day ~ %54-69 (daily avg) | -41.751 [-299.032, +215.529] | 0.932 | 0.958 | 0.1246 | +1.9 | +5.2 | 0.1068 \| 0.1080 |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | -0.106 [-0.881, +0.670] | 0.936 | 0.931 | 0.1387 | +1.9 | +5.4 | 0.1234 \| 0.1245 |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | -0.122 [-0.913, +0.669] | 0.932 | 0.931 | 0.1387 | +1.9 | +5.3 | 0.1234 \| 0.1245 |
| Resting heart-rate proxy ~ %54-69 (pooled) | +0.005 [-0.413, +0.423] | 0.989 | 0.980 | 0.1295 | +2.0 | +13.2 | 0.1026 \| 0.1044 |
| Resting heart-rate proxy ~ %54-69 (daily avg) | +0.008 [-0.418, +0.434] | 0.986 | 0.980 | 0.1295 | +2.0 | +13.2 | 0.1024 \| 0.1044 |
| Total sleep time per night ~ %54-69 (pooled) | +0.803 [-2.296, +3.901] | 0.932 | 0.936 | 0.0207 | +1.8 | +3.8 | -0.0067 \| -0.0051 |
| Total sleep time per night ~ %54-69 (daily avg) | +0.766 [-2.326, +3.857] | 0.932 | 0.936 | 0.0206 | +1.8 | +3.9 | -0.0066 \| -0.0051 |
| Garmin stress score, mean ~ %54-69 (pooled) | -0.113 [-1.153, +0.926] | 0.945 | 0.920 | 0.0726 | +1.9 | +9.7 | 0.0493 \| 0.0510 |
| Garmin stress score, mean ~ %54-69 (daily avg) | -0.179 [-1.276, +0.917] | 0.932 | 0.895 | 0.0727 | +1.9 | +9.7 | 0.0492 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | 867 | 423 | -0.005446 | 0.0823 | [-0.1668, 0.1559] | -0.07 | 0.947 |  |
| MoCA total score ~ %54-69 (daily avg) | 867 | 356 | -0.006059 | 0.08282 | [-0.1684, 0.1563] | -0.07 | 0.942 |  |
| Cognitive impairment ~ %54-69 (pooled) | 867 | 423 | +0.02454 | 0.04834 | [-0.0702, 0.1193] | 0.51 | 0.612 |  |
| Cognitive impairment ~ %54-69 (daily avg) | 867 | 356 | +0.0297 | 0.04729 | [-0.06298, 0.1224] | 0.63 | 0.530 |  |
| MoCA memory index score ~ %54-69 (pooled) | 867 | 423 | -0.08886 | 0.06002 | [-0.2065, 0.02878] | -1.48 | 0.139 |  |
| MoCA memory index score ~ %54-69 (daily avg) | 867 | 356 | -0.1055 | 0.05878 | [-0.2207, 0.009731] | -1.79 | 0.073 |  |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | 865 | 422 | +0.09863 | 0.1103 | [-0.1175, 0.3147] | 0.89 | 0.371 |  |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | 865 | 355 | +0.1086 | 0.1067 | [-0.1005, 0.3176] | 1.02 | 0.309 |  |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | 865 | 422 | +0.01534 | 0.05543 | [-0.09329, 0.124] | 0.28 | 0.782 |  |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | 865 | 355 | +0.0223 | 0.05374 | [-0.08302, 0.1276] | 0.42 | 0.678 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | 849 | 412 | **+0.08979** | 0.03251 | [0.02607, 0.1535] | **2.76** | **0.006**** | ** |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | 849 | 345 | **+0.08842** | 0.03256 | [0.02459, 0.1522] | **2.72** | **0.007**** | ** |
| Indoor temperature, mean ~ %54-69 (pooled) | 849 | 412 | +0.04232 | 0.05123 | [-0.05807, 0.1427] | 0.83 | 0.409 |  |
| Indoor temperature, mean ~ %54-69 (daily avg) | 849 | 345 | +0.05241 | 0.04855 | [-0.04274, 0.1476] | 1.08 | 0.280 |  |
| Indoor relative humidity, mean ~ %54-69 (pooled) | 849 | 412 | -0.04255 | 0.1797 | [-0.3947, 0.3096] | -0.24 | 0.813 |  |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | 849 | 345 | -0.07306 | 0.1709 | [-0.408, 0.2619] | -0.43 | 0.669 |  |
| Indoor VOC index, mean ~ %54-69 (pooled) | 849 | 412 | +0.3679 | 0.3629 | [-0.3433, 1.079] | 1.01 | 0.311 |  |
| Indoor VOC index, mean ~ %54-69 (daily avg) | 849 | 345 | +0.3206 | 0.3446 | [-0.3549, 0.996] | 0.93 | 0.352 |  |
| Steps per wear-day ~ %54-69 (pooled) | 747 | 369 | **-252.3** | 92.6 | [-433.8, -70.83] | **-2.72** | **0.006**** | ** |
| Steps per wear-day ~ %54-69 (daily avg) | 747 | 309 | **-253.7** | 87 | [-424.2, -83.2] | **-2.92** | **0.004**** | ** |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | 747 | 369 | -0.4851 | 0.2593 | [-0.9932, 0.02311] | -1.87 | 0.061 |  |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | 747 | 309 | **-0.5097** | 0.2561 | [-1.012, -0.007801] | **-1.99** | **0.047*** | * |
| Resting heart-rate proxy ~ %54-69 (pooled) | 749 | 372 | -0.1276 | 0.1874 | [-0.4949, 0.2396] | -0.68 | 0.496 |  |
| Resting heart-rate proxy ~ %54-69 (daily avg) | 749 | 312 | -0.1802 | 0.1932 | [-0.5588, 0.1985] | -0.93 | 0.351 |  |
| Total sleep time per night ~ %54-69 (pooled) | 756 | 379 | +1.474 | 1.856 | [-2.164, 5.111] | 0.79 | 0.427 |  |
| Total sleep time per night ~ %54-69 (daily avg) | 756 | 321 | +1.093 | 1.713 | [-2.264, 4.45] | 0.64 | 0.523 |  |
| Garmin stress score, mean ~ %54-69 (pooled) | 749 | 372 | -0.4502 | 0.4675 | [-1.366, 0.466] | -0.96 | 0.335 |  |
| Garmin stress score, mean ~ %54-69 (daily avg) | 749 | 312 | -0.4898 | 0.4621 | [-1.395, 0.4158] | -1.06 | 0.289 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-69 (pooled) | -0.008 [-0.246, +0.230] | 0.966 | 0.997 | 0.0808 | +2.0 | +3.5 | 0.0519 \| 0.0541 |
| MoCA total score ~ %54-69 (daily avg) | -0.009 [-0.256, +0.237] | 0.964 | 0.997 | 0.0808 | +2.0 | +3.5 | 0.0519 \| 0.0541 |
| Cognitive impairment ~ %54-69 (pooled) | OR 1.037 [0.902, 1.192] | 0.783 | 0.677 | 0.6603 | +1.7 | +3.4 | 0.6399 \| 0.6425 |
| Cognitive impairment ~ %54-69 (daily avg) | OR 1.046 [0.909, 1.204] | 0.717 | 0.622 | 0.6605 | +1.6 | +3.3 | 0.6403 \| 0.6425 |
| MoCA memory index score ~ %54-69 (pooled) | -0.131 [-0.305, +0.042] | 0.319 | 0.181 | 0.0618 | -0.0 | +1.8 | 0.0298 \| 0.0286 |
| MoCA memory index score ~ %54-69 (daily avg) | -0.160 [-0.335, +0.015] | 0.232 | 0.122 | 0.0629 | -1.0 | +0.8 | 0.0308 \| 0.0286 |
| CES-D-10 depressive symptoms ~ %54-69 (pooled) | +0.146 [-0.173, +0.464] | 0.594 | 0.578 | 0.1118 | +1.2 | +2.5 | 0.0787 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %54-69 (daily avg) | +0.165 [-0.153, +0.482] | 0.533 | 0.578 | 0.1121 | +1.0 | +2.3 | 0.0789 \| 0.0796 |
| Clinically relevant depressive symptoms ~ %54-69 (pooled) | OR 1.023 [0.871, 1.201] | 0.868 | 0.871 | 0.6604 | +1.9 | +4.9 | 0.6309 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %54-69 (daily avg) | OR 1.034 [0.882, 1.214] | 0.815 | 0.840 | 0.6608 | +1.8 | +4.8 | 0.6316 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (pooled) | +0.134 [+0.039, +0.228] | 0.055 | **0.034 (FDR<0.05)** | 0.1716 | -15.9 | -6.5 | 0.1424 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-69 (daily avg) | +0.135 [+0.038, +0.233] | 0.061 | **0.034 (FDR<0.05)** | 0.1721 | -16.4 | -7.0 | 0.1428 \| 0.1310 |
| Indoor temperature, mean ~ %54-69 (pooled) | +0.063 [-0.086, +0.212] | 0.630 | 0.794 | 0.2508 | +1.2 | -0.4 | 0.2255 \| 0.2264 |
| Indoor temperature, mean ~ %54-69 (daily avg) | +0.080 [-0.065, +0.226] | 0.501 | 0.794 | 0.2512 | +0.8 | -0.9 | 0.2259 \| 0.2264 |
| Indoor relative humidity, mean ~ %54-69 (pooled) | -0.063 [-0.587, +0.461] | 0.884 | 0.938 | 0.2130 | +1.9 | +0.0 | 0.1837 \| 0.1857 |
| Indoor relative humidity, mean ~ %54-69 (daily avg) | -0.112 [-0.625, +0.401] | 0.813 | 0.938 | 0.2132 | +1.7 | -0.1 | 0.1842 \| 0.1857 |
| Indoor VOC index, mean ~ %54-69 (pooled) | +0.548 [-0.511, +1.606] | 0.533 | 0.585 | 0.0566 | +1.1 | +1.5 | 0.0271 \| 0.0276 |
| Indoor VOC index, mean ~ %54-69 (daily avg) | +0.491 [-0.544, +1.526] | 0.570 | 0.585 | 0.0564 | +1.3 | +1.7 | 0.0269 \| 0.0276 |
| Steps per wear-day ~ %54-69 (pooled) | -383.181 [-658.791, -107.570] | 0.061 | **0.040 (FDR<0.05)** | 0.1623 | -2.7 | -2.6 | 0.1425 \| 0.1390 |
| Steps per wear-day ~ %54-69 (daily avg) | **-401.236 [-670.891, -131.581]** | **0.043 (FDR<0.05)** | **0.039 (FDR<0.05)** | 0.1628 | -3.2 | -3.1 | 0.1432 \| 0.1390 |
| Brisk-cadence minutes per day ~ %54-69 (pooled) | -0.737 [-1.508, +0.035] | 0.217 | 0.380 | 0.1812 | -0.1 | -0.1 | 0.1552 \| 0.1546 |
| Brisk-cadence minutes per day ~ %54-69 (daily avg) | -0.806 [-1.600, -0.012] | 0.189 | 0.380 | 0.1816 | -0.5 | -0.5 | 0.1556 \| 0.1546 |
| Resting heart-rate proxy ~ %54-69 (pooled) | -0.194 [-0.751, +0.363] | 0.689 | 0.618 | 0.1527 | +1.6 | +7.7 | 0.1243 \| 0.1253 |
| Resting heart-rate proxy ~ %54-69 (daily avg) | -0.285 [-0.883, +0.313] | 0.570 | 0.495 | 0.1532 | +1.1 | +7.2 | 0.1249 \| 0.1253 |
| Total sleep time per night ~ %54-69 (pooled) | +2.227 [-3.270, +7.725] | 0.640 | 0.552 | 0.0373 | +1.2 | +4.1 | 0.0046 \| 0.0066 |
| Total sleep time per night ~ %54-69 (daily avg) | +1.720 [-3.563, +7.003] | 0.714 | 0.624 | 0.0369 | +1.5 | +4.4 | 0.0043 \| 0.0066 |
| Garmin stress score, mean ~ %54-69 (pooled) | -0.683 [-2.072, +0.707] | 0.566 | 0.443 | 0.1231 | +0.9 | +13.9 | 0.0926 \| 0.0947 |
| Garmin stress score, mean ~ %54-69 (daily avg) | -0.773 [-2.204, +0.657] | 0.512 | 0.407 | 0.1235 | +0.5 | +13.6 | 0.0932 \| 0.0947 |


---

## Band <70

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | 2138 | 1259 | +0.01604 | 0.03501 | [-0.05257, 0.08466] | 0.46 | 0.647 |  |
| MoCA total score ~ %<70 (daily avg) | 2138 | 1058 | +0.009752 | 0.03637 | [-0.06153, 0.08103] | 0.27 | 0.789 |  |
| Cognitive impairment ~ %<70 (pooled) | 2138 | 1259 | +0.02106 | 0.02602 | [-0.02993, 0.07206] | 0.81 | 0.418 |  |
| Cognitive impairment ~ %<70 (daily avg) | 2138 | 1058 | +0.02873 | 0.02632 | [-0.02285, 0.08032] | 1.09 | 0.275 |  |
| MoCA memory index score ~ %<70 (pooled) | 2138 | 1259 | +0.01226 | 0.02715 | [-0.04096, 0.06547] | 0.45 | 0.652 |  |
| MoCA memory index score ~ %<70 (daily avg) | 2138 | 1058 | -0.01043 | 0.02949 | [-0.06822, 0.04736] | -0.35 | 0.723 |  |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | 2135 | 1258 | +0.02593 | 0.05756 | [-0.08689, 0.1387] | 0.45 | 0.652 |  |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | 2135 | 1057 | +0.04571 | 0.05927 | [-0.07045, 0.1619] | 0.77 | 0.441 |  |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | 2135 | 1258 | +0.0108 | 0.03111 | [-0.05016, 0.07177] | 0.35 | 0.728 |  |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | 2135 | 1057 | +0.01347 | 0.03115 | [-0.04758, 0.07452] | 0.43 | 0.665 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | 2100 | 1234 | +0.02707 | 0.01522 | [-0.002758, 0.0569] | 1.78 | 0.075 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | 2100 | 1034 | +0.03101 | 0.01628 | [-0.0008939, 0.06291] | 1.91 | 0.057 |  |
| Indoor temperature, mean ~ %<70 (pooled) | 2100 | 1234 | +0.03806 | 0.02336 | [-0.007719, 0.08384] | 1.63 | 0.103 |  |
| Indoor temperature, mean ~ %<70 (daily avg) | 2100 | 1034 | +0.04263 | 0.02403 | [-0.00446, 0.08973] | 1.77 | 0.076 |  |
| Indoor relative humidity, mean ~ %<70 (pooled) | 2100 | 1234 | -0.1051 | 0.07458 | [-0.2513, 0.04107] | -1.41 | 0.159 |  |
| Indoor relative humidity, mean ~ %<70 (daily avg) | 2100 | 1034 | -0.1111 | 0.07552 | [-0.2591, 0.03694] | -1.47 | 0.141 |  |
| Indoor VOC index, mean ~ %<70 (pooled) | 2100 | 1234 | +0.06307 | 0.1945 | [-0.3181, 0.4442] | 0.32 | 0.746 |  |
| Indoor VOC index, mean ~ %<70 (daily avg) | 2100 | 1034 | +0.06469 | 0.1957 | [-0.3188, 0.4482] | 0.33 | 0.741 |  |
| Steps per wear-day ~ %<70 (pooled) | 1872 | 1124 | **-124.7** | 47.86 | [-218.5, -30.86] | **-2.60** | **0.009**** | ** |
| Steps per wear-day ~ %<70 (daily avg) | 1872 | 942 | **-126.2** | 48.97 | [-222.2, -30.24] | **-2.58** | **0.010**** | ** |
| Brisk-cadence minutes per day ~ %<70 (pooled) | 1872 | 1124 | -0.2532 | 0.1421 | [-0.5317, 0.02533] | -1.78 | 0.075 |  |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | 1872 | 942 | -0.2762 | 0.1481 | [-0.5665, 0.01414] | -1.86 | 0.062 |  |
| Resting heart-rate proxy ~ %<70 (pooled) | 1877 | 1129 | -0.063 | 0.09092 | [-0.2412, 0.1152] | -0.69 | 0.488 |  |
| Resting heart-rate proxy ~ %<70 (daily avg) | 1877 | 946 | -0.07921 | 0.09867 | [-0.2726, 0.1142] | -0.80 | 0.422 |  |
| Total sleep time per night ~ %<70 (pooled) | 1893 | 1147 | +0.6698 | 0.7371 | [-0.775, 2.115] | 0.91 | 0.364 |  |
| Total sleep time per night ~ %<70 (daily avg) | 1893 | 965 | +0.5559 | 0.7302 | [-0.8753, 1.987] | 0.76 | 0.446 |  |
| Garmin stress score, mean ~ %<70 (pooled) | 1879 | 1130 | -0.2253 | 0.2222 | [-0.6607, 0.2102] | -1.01 | 0.311 |  |
| Garmin stress score, mean ~ %<70 (daily avg) | 1879 | 947 | -0.2685 | 0.2412 | [-0.7413, 0.2043] | -1.11 | 0.266 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | +0.028 [-0.093, +0.150] | 0.795 | 0.743 | 0.0999 | +1.8 | +26.4 | 0.0905 \| 0.0915 |
| MoCA total score ~ %<70 (daily avg) | +0.017 [-0.107, +0.141] | 0.868 | 0.815 | 0.0998 | +1.9 | +26.6 | 0.0904 \| 0.0915 |
| Cognitive impairment ~ %<70 (pooled) | OR 1.038 [0.948, 1.136] | 0.591 | 0.447 | 0.6683 | +1.3 | +15.0 | 0.6598 \| 0.6603 |
| Cognitive impairment ~ %<70 (daily avg) | OR 1.051 [0.961, 1.150] | 0.444 | 0.316 | 0.6686 | +0.8 | +14.4 | 0.6600 \| 0.6603 |
| MoCA memory index score ~ %<70 (pooled) | +0.022 [-0.073, +0.116] | 0.795 | 0.748 | 0.0715 | +1.9 | +7.2 | 0.0621 \| 0.0630 |
| MoCA memory index score ~ %<70 (daily avg) | -0.018 [-0.119, +0.082] | 0.837 | 0.773 | 0.0715 | +1.9 | +7.3 | 0.0619 \| 0.0630 |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | +0.046 [-0.154, +0.246] | 0.795 | 0.722 | 0.1028 | +1.8 | +2.1 | 0.0907 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | +0.080 [-0.123, +0.282] | 0.611 | 0.620 | 0.1030 | +1.4 | +1.6 | 0.0909 \| 0.0916 |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | OR 1.019 [0.915, 1.136] | 0.838 | 0.779 | 0.6800 | +1.9 | +4.6 | 0.6670 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | OR 1.024 [0.920, 1.139] | 0.803 | 0.756 | 0.6801 | +1.8 | +4.5 | 0.6671 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | +0.048 [-0.005, +0.102] | 0.184 | 0.173 | 0.1533 | -4.1 | +6.8 | 0.1399 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | +0.054 [-0.002, +0.110] | 0.147 | 0.173 | 0.1539 | -5.8 | +5.1 | 0.1405 \| 0.1387 |
| Indoor temperature, mean ~ %<70 (pooled) | +0.068 [-0.014, +0.150] | 0.218 | 0.801 | 0.2987 | -0.4 | -1.9 | 0.2897 \| 0.2896 |
| Indoor temperature, mean ~ %<70 (daily avg) | +0.075 [-0.008, +0.157] | 0.184 | 0.801 | 0.2988 | -0.9 | -2.4 | 0.2900 \| 0.2896 |
| Indoor relative humidity, mean ~ %<70 (pooled) | -0.188 [-0.448, +0.073] | 0.312 | 0.898 | 0.2418 | -0.0 | -1.9 | 0.2304 \| 0.2307 |
| Indoor relative humidity, mean ~ %<70 (daily avg) | -0.194 [-0.454, +0.065] | 0.283 | 0.898 | 0.2418 | -0.2 | -2.1 | 0.2305 \| 0.2307 |
| Indoor VOC index, mean ~ %<70 (pooled) | +0.113 [-0.568, +0.793] | 0.844 | 0.868 | 0.0426 | +1.9 | +1.9 | 0.0262 \| 0.0271 |
| Indoor VOC index, mean ~ %<70 (daily avg) | +0.113 [-0.558, +0.785] | 0.844 | 0.868 | 0.0426 | +1.9 | +1.9 | 0.0263 \| 0.0271 |
| Steps per wear-day ~ %<70 (pooled) | **-230.881 [-404.614, -57.147]** | **0.033 (FDR<0.05)** | 0.077 | 0.1373 | -3.5 | +4.5 | 0.1236 \| 0.1222 |
| Steps per wear-day ~ %<70 (daily avg) | **-230.175 [-405.202, -55.148]** | **0.035 (FDR<0.05)** | 0.077 | 0.1373 | -3.5 | +4.5 | 0.1235 \| 0.1222 |
| Brisk-cadence minutes per day ~ %<70 (pooled) | -0.469 [-0.985, +0.047] | 0.184 | 0.192 | 0.1568 | -0.5 | +7.7 | 0.1445 \| 0.1447 |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | -0.504 [-1.033, +0.026] | 0.158 | 0.192 | 0.1570 | -0.9 | +7.3 | 0.1446 \| 0.1447 |
| Resting heart-rate proxy ~ %<70 (pooled) | -0.117 [-0.446, +0.213] | 0.656 | 0.541 | 0.1599 | +1.6 | +72.8 | 0.1479 \| 0.1482 |
| Resting heart-rate proxy ~ %<70 (daily avg) | -0.144 [-0.496, +0.208] | 0.595 | 0.485 | 0.1600 | +1.4 | +72.6 | 0.1480 \| 0.1482 |
| Total sleep time per night ~ %<70 (pooled) | +1.233 [-1.427, +3.893] | 0.528 | 0.512 | 0.0336 | +1.4 | +10.3 | 0.0205 \| 0.0209 |
| Total sleep time per night ~ %<70 (daily avg) | +1.008 [-1.587, +3.603] | 0.617 | 0.577 | 0.0335 | +1.6 | +10.5 | 0.0203 \| 0.0209 |
| Garmin stress score, mean ~ %<70 (pooled) | -0.417 [-1.222, +0.389] | 0.482 | 0.344 | 0.1055 | +0.9 | +61.3 | 0.0897 \| 0.0902 |
| Garmin stress score, mean ~ %<70 (daily avg) | -0.489 [-1.350, +0.372] | 0.439 | 0.305 | 0.1057 | +0.5 | +60.9 | 0.0895 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | 1271 | 831 | +0.01435 | 0.03628 | [-0.05676, 0.08545] | 0.40 | 0.692 |  |
| MoCA total score ~ %<70 (daily avg) | 1271 | 700 | +0.01265 | 0.03745 | [-0.06075, 0.08604] | 0.34 | 0.736 |  |
| Cognitive impairment ~ %<70 (pooled) | 1271 | 831 | +0.03715 | 0.0344 | [-0.03027, 0.1046] | 1.08 | 0.280 |  |
| Cognitive impairment ~ %<70 (daily avg) | 1271 | 700 | +0.04366 | 0.03574 | [-0.02638, 0.1137] | 1.22 | 0.222 |  |
| MoCA memory index score ~ %<70 (pooled) | 1271 | 831 | **+0.06387** | 0.02889 | [0.007243, 0.1205] | **2.21** | **0.027*** | * |
| MoCA memory index score ~ %<70 (daily avg) | 1271 | 700 | +0.04754 | 0.0299 | [-0.01107, 0.1062] | 1.59 | 0.112 |  |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | 1270 | 831 | +0.005361 | 0.07801 | [-0.1475, 0.1583] | 0.07 | 0.945 |  |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | 1270 | 700 | +0.02887 | 0.08122 | [-0.1303, 0.1881] | 0.36 | 0.722 |  |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | 1270 | 831 | +0.01836 | 0.04195 | [-0.06386, 0.1006] | 0.44 | 0.662 |  |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | 1270 | 700 | +0.01269 | 0.04429 | [-0.07411, 0.0995] | 0.29 | 0.774 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | 1251 | 817 | -0.003091 | 0.01293 | [-0.02844, 0.02226] | -0.24 | 0.811 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | 1251 | 687 | -0.002172 | 0.01435 | [-0.0303, 0.02595] | -0.15 | 0.880 |  |
| Indoor temperature, mean ~ %<70 (pooled) | 1251 | 817 | +0.04875 | 0.02831 | [-0.006743, 0.1042] | 1.72 | 0.085 |  |
| Indoor temperature, mean ~ %<70 (daily avg) | 1251 | 687 | +0.05117 | 0.03018 | [-0.00797, 0.1103] | 1.70 | 0.090 |  |
| Indoor relative humidity, mean ~ %<70 (pooled) | 1251 | 817 | -0.1448 | 0.0807 | [-0.303, 0.01335] | -1.79 | 0.073 |  |
| Indoor relative humidity, mean ~ %<70 (daily avg) | 1251 | 687 | -0.1423 | 0.08776 | [-0.3143, 0.02966] | -1.62 | 0.105 |  |
| Indoor VOC index, mean ~ %<70 (pooled) | 1251 | 817 | -0.09491 | 0.255 | [-0.5947, 0.4048] | -0.37 | 0.710 |  |
| Indoor VOC index, mean ~ %<70 (daily avg) | 1251 | 687 | -0.1155 | 0.2809 | [-0.6661, 0.435] | -0.41 | 0.681 |  |
| Steps per wear-day ~ %<70 (pooled) | 1125 | 750 | -31.84 | 65.37 | [-160, 96.29] | -0.49 | 0.626 |  |
| Steps per wear-day ~ %<70 (daily avg) | 1125 | 631 | -24.1 | 72.54 | [-166.3, 118.1] | -0.33 | 0.740 |  |
| Brisk-cadence minutes per day ~ %<70 (pooled) | 1125 | 750 | -0.05909 | 0.2055 | [-0.4618, 0.3436] | -0.29 | 0.774 |  |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | 1125 | 631 | -0.06902 | 0.2263 | [-0.5126, 0.3746] | -0.30 | 0.760 |  |
| Resting heart-rate proxy ~ %<70 (pooled) | 1128 | 752 | +0.03263 | 0.1075 | [-0.178, 0.2433] | 0.30 | 0.761 |  |
| Resting heart-rate proxy ~ %<70 (daily avg) | 1128 | 632 | +0.02186 | 0.1197 | [-0.2127, 0.2565] | 0.18 | 0.855 |  |
| Total sleep time per night ~ %<70 (pooled) | 1137 | 764 | +0.06796 | 0.8445 | [-1.587, 1.723] | 0.08 | 0.936 |  |
| Total sleep time per night ~ %<70 (daily avg) | 1137 | 642 | +0.1054 | 0.881 | [-1.621, 1.832] | 0.12 | 0.905 |  |
| Garmin stress score, mean ~ %<70 (pooled) | 1130 | 753 | -0.0423 | 0.2782 | [-0.5875, 0.5029] | -0.15 | 0.879 |  |
| Garmin stress score, mean ~ %<70 (daily avg) | 1130 | 633 | -0.1033 | 0.3251 | [-0.7405, 0.5338] | -0.32 | 0.751 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | +0.025 [-0.100, +0.151] | 0.932 | 0.820 | 0.0973 | +1.9 | +15.6 | 0.0780 \| 0.0789 |
| MoCA total score ~ %<70 (daily avg) | +0.021 [-0.102, +0.144] | 0.932 | 0.820 | 0.0973 | +1.9 | +15.6 | 0.0781 \| 0.0789 |
| Cognitive impairment ~ %<70 (pooled) | OR 1.068 [0.948, 1.203] | 0.654 | 0.482 | 0.6613 | +0.9 | +0.7 | 0.6444 \| 0.6443 |
| Cognitive impairment ~ %<70 (daily avg) | OR 1.076 [0.957, 1.210] | 0.594 | 0.480 | 0.6611 | +0.6 | +0.3 | 0.6438 \| 0.6443 |
| MoCA memory index score ~ %<70 (pooled) | +0.113 [+0.013, +0.213] | 0.186 | 0.060 | 0.0728 | -0.4 | +0.2 | 0.0481 \| 0.0477 |
| MoCA memory index score ~ %<70 (daily avg) | +0.080 [-0.019, +0.178] | 0.441 | 0.168 | 0.0719 | +0.8 | +1.5 | 0.0475 \| 0.0477 |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | +0.009 [-0.261, +0.280] | 0.981 | 0.953 | 0.0907 | +2.0 | +0.0 | 0.0658 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | +0.048 [-0.218, +0.315] | 0.932 | 0.953 | 0.0908 | +1.9 | -0.1 | 0.0660 \| 0.0675 |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | OR 1.033 [0.893, 1.194] | 0.932 | 0.958 | 0.6933 | +1.8 | +0.7 | 0.6723 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | OR 1.021 [0.883, 1.181] | 0.932 | 0.958 | 0.6934 | +1.9 | +0.8 | 0.6722 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | -0.005 [-0.050, +0.039] | 0.939 | 0.987 | 0.1362 | +2.0 | -0.0 | 0.1125 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | -0.004 [-0.051, +0.044] | 0.964 | 0.987 | 0.1361 | +2.0 | -0.0 | 0.1123 \| 0.1139 |
| Indoor temperature, mean ~ %<70 (pooled) | +0.086 [-0.012, +0.185] | 0.404 | 0.674 | 0.3111 | -0.6 | -2.5 | 0.2896 \| 0.2892 |
| Indoor temperature, mean ~ %<70 (daily avg) | +0.086 [-0.013, +0.185] | 0.406 | 0.674 | 0.3111 | -0.5 | -2.5 | 0.2894 \| 0.2892 |
| Indoor relative humidity, mean ~ %<70 (pooled) | -0.256 [-0.537, +0.024] | 0.367 | 0.564 | 0.2610 | -0.4 | +0.1 | 0.2403 \| 0.2403 |
| Indoor relative humidity, mean ~ %<70 (daily avg) | -0.239 [-0.527, +0.050] | 0.438 | 0.585 | 0.2608 | -0.1 | +0.4 | 0.2399 \| 0.2403 |
| Indoor VOC index, mean ~ %<70 (pooled) | -0.168 [-1.053, +0.717] | 0.932 | 0.784 | 0.0239 | +1.9 | +1.2 | 0.0016 \| 0.0025 |
| Indoor VOC index, mean ~ %<70 (daily avg) | -0.194 [-1.117, +0.729] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | 0.0017 \| 0.0025 |
| Steps per wear-day ~ %<70 (pooled) | -58.830 [-295.605, +177.945] | 0.932 | 0.958 | 0.1247 | +1.7 | +5.0 | 0.1071 \| 0.1080 |
| Steps per wear-day ~ %<70 (daily avg) | -42.218 [-291.270, +206.834] | 0.932 | 0.958 | 0.1246 | +1.9 | +5.2 | 0.1069 \| 0.1080 |
| Brisk-cadence minutes per day ~ %<70 (pooled) | -0.109 [-0.853, +0.635] | 0.932 | 0.931 | 0.1387 | +1.9 | +5.4 | 0.1235 \| 0.1245 |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | -0.121 [-0.898, +0.656] | 0.932 | 0.931 | 0.1387 | +1.9 | +5.3 | 0.1234 \| 0.1245 |
| Resting heart-rate proxy ~ %<70 (pooled) | +0.060 [-0.329, +0.449] | 0.932 | 0.843 | 0.1296 | +1.9 | +13.1 | 0.1029 \| 0.1044 |
| Resting heart-rate proxy ~ %<70 (daily avg) | +0.038 [-0.372, +0.449] | 0.948 | 0.914 | 0.1296 | +2.0 | +13.2 | 0.1024 \| 0.1044 |
| Total sleep time per night ~ %<70 (pooled) | +0.125 [-2.913, +3.163] | 0.981 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0066 \| -0.0051 |
| Total sleep time per night ~ %<70 (daily avg) | +0.183 [-2.821, +3.188] | 0.966 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0065 \| -0.0051 |
| Garmin stress score, mean ~ %<70 (pooled) | -0.078 [-1.084, +0.928] | 0.964 | 0.940 | 0.0726 | +2.0 | +9.8 | 0.0493 \| 0.0510 |
| Garmin stress score, mean ~ %<70 (daily avg) | -0.181 [-1.295, +0.934] | 0.932 | 0.895 | 0.0727 | +1.9 | +9.7 | 0.0490 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | 867 | 428 | -0.0007986 | 0.06799 | [-0.1341, 0.1325] | -0.01 | 0.991 |  |
| MoCA total score ~ %<70 (daily avg) | 867 | 358 | -0.004084 | 0.06631 | [-0.134, 0.1259] | -0.06 | 0.951 |  |
| Cognitive impairment ~ %<70 (pooled) | 867 | 428 | +0.01773 | 0.03985 | [-0.06038, 0.09584] | 0.44 | 0.656 |  |
| Cognitive impairment ~ %<70 (daily avg) | 867 | 358 | +0.0238 | 0.03898 | [-0.0526, 0.1002] | 0.61 | 0.542 |  |
| MoCA memory index score ~ %<70 (pooled) | 867 | 428 | -0.06861 | 0.04665 | [-0.16, 0.02283] | -1.47 | 0.141 |  |
| MoCA memory index score ~ %<70 (daily avg) | 867 | 358 | -0.08541 | 0.04652 | [-0.1766, 0.005762] | -1.84 | 0.066 |  |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | 865 | 427 | +0.06113 | 0.09914 | [-0.1332, 0.2554] | 0.62 | 0.538 |  |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | 865 | 357 | +0.07316 | 0.09783 | [-0.1186, 0.2649] | 0.75 | 0.455 |  |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | 865 | 427 | +0.005217 | 0.04608 | [-0.0851, 0.09553] | 0.11 | 0.910 |  |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | 865 | 357 | +0.01661 | 0.04381 | [-0.06927, 0.1025] | 0.38 | 0.705 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | 849 | 417 | **+0.07601** | 0.02553 | [0.02597, 0.126] | **2.98** | **0.003**** | ** |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | 849 | 347 | **+0.07572** | 0.02647 | [0.02384, 0.1276] | **2.86** | **0.004**** | ** |
| Indoor temperature, mean ~ %<70 (pooled) | 849 | 417 | +0.03131 | 0.04185 | [-0.0507, 0.1133] | 0.75 | 0.454 |  |
| Indoor temperature, mean ~ %<70 (daily avg) | 849 | 347 | +0.03916 | 0.04095 | [-0.04109, 0.1194] | 0.96 | 0.339 |  |
| Indoor relative humidity, mean ~ %<70 (pooled) | 849 | 417 | -0.04425 | 0.1477 | [-0.3337, 0.2452] | -0.30 | 0.764 |  |
| Indoor relative humidity, mean ~ %<70 (daily avg) | 849 | 347 | -0.07117 | 0.138 | [-0.3416, 0.1993] | -0.52 | 0.606 |  |
| Indoor VOC index, mean ~ %<70 (pooled) | 849 | 417 | +0.2955 | 0.2819 | [-0.2571, 0.8481] | 1.05 | 0.295 |  |
| Indoor VOC index, mean ~ %<70 (daily avg) | 849 | 347 | +0.2914 | 0.2624 | [-0.2229, 0.8058] | 1.11 | 0.267 |  |
| Steps per wear-day ~ %<70 (pooled) | 747 | 374 | **-221.8** | 78.56 | [-375.8, -67.85] | **-2.82** | **0.005**** | ** |
| Steps per wear-day ~ %<70 (daily avg) | 747 | 311 | **-219.9** | 67.95 | [-353, -86.7] | **-3.24** | **0.001**** | ** |
| Brisk-cadence minutes per day ~ %<70 (pooled) | 747 | 374 | -0.4415 | 0.2269 | [-0.8862, 0.003253] | -1.95 | 0.052 |  |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | 747 | 311 | **-0.4571** | 0.2149 | [-0.8782, -0.03593] | **-2.13** | **0.033*** | * |
| Resting heart-rate proxy ~ %<70 (pooled) | 749 | 377 | -0.0611 | 0.1621 | [-0.3788, 0.2566] | -0.38 | 0.706 |  |
| Resting heart-rate proxy ~ %<70 (daily avg) | 749 | 314 | -0.125 | 0.1745 | [-0.4671, 0.2171] | -0.72 | 0.474 |  |
| Total sleep time per night ~ %<70 (pooled) | 756 | 383 | +1.532 | 1.401 | [-1.213, 4.277] | 1.09 | 0.274 |  |
| Total sleep time per night ~ %<70 (daily avg) | 756 | 323 | +1.116 | 1.293 | [-1.419, 3.65] | 0.86 | 0.388 |  |
| Garmin stress score, mean ~ %<70 (pooled) | 749 | 377 | -0.2554 | 0.4 | [-1.039, 0.5285] | -0.64 | 0.523 |  |
| Garmin stress score, mean ~ %<70 (daily avg) | 749 | 314 | -0.3255 | 0.3947 | [-1.099, 0.4482] | -0.82 | 0.410 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %<70 (pooled) | -0.001 [-0.239, +0.237] | 0.993 | 0.997 | 0.0808 | +2.0 | +3.5 | 0.0517 \| 0.0541 |
| MoCA total score ~ %<70 (daily avg) | -0.008 [-0.246, +0.231] | 0.966 | 0.997 | 0.0808 | +2.0 | +3.5 | 0.0519 \| 0.0541 |
| Cognitive impairment ~ %<70 (pooled) | OR 1.032 [0.898, 1.187] | 0.812 | 0.702 | 0.6603 | +1.8 | +3.5 | 0.6396 \| 0.6425 |
| Cognitive impairment ~ %<70 (daily avg) | OR 1.045 [0.908, 1.202] | 0.725 | 0.622 | 0.6606 | +1.6 | +3.3 | 0.6406 \| 0.6425 |
| MoCA memory index score ~ %<70 (pooled) | -0.123 [-0.286, +0.041] | 0.321 | 0.181 | 0.0615 | +0.3 | +2.0 | 0.0297 \| 0.0286 |
| MoCA memory index score ~ %<70 (daily avg) | -0.157 [-0.324, +0.011] | 0.222 | 0.122 | 0.0628 | -0.9 | +0.9 | 0.0308 \| 0.0286 |
| CES-D-10 depressive symptoms ~ %<70 (pooled) | +0.109 [-0.238, +0.457] | 0.722 | 0.667 | 0.1115 | +1.6 | +2.9 | 0.0783 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %<70 (daily avg) | +0.134 [-0.218, +0.487] | 0.656 | 0.593 | 0.1117 | +1.3 | +2.6 | 0.0784 \| 0.0796 |
| Clinically relevant depressive symptoms ~ %<70 (pooled) | OR 1.009 [0.859, 1.186] | 0.943 | 0.910 | 0.6605 | +2.0 | +5.0 | 0.6313 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %<70 (daily avg) | OR 1.031 [0.880, 1.207] | 0.829 | 0.840 | 0.6606 | +1.9 | +4.9 | 0.6315 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (pooled) | **+0.137 [+0.047, +0.227]** | **0.040 (FDR<0.05)** | **0.034 (FDR<0.05)** | 0.1724 | -16.8 | -7.4 | 0.1435 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<70 (daily avg) | **+0.140 [+0.044, +0.237]** | **0.047 (FDR<0.05)** | **0.034 (FDR<0.05)** | 0.1734 | -17.8 | -8.4 | 0.1439 \| 0.1310 |
| Indoor temperature, mean ~ %<70 (pooled) | +0.056 [-0.091, +0.204] | 0.656 | 0.794 | 0.2507 | +1.4 | -0.3 | 0.2253 \| 0.2264 |
| Indoor temperature, mean ~ %<70 (daily avg) | +0.073 [-0.076, +0.221] | 0.566 | 0.794 | 0.2510 | +1.0 | -0.7 | 0.2254 \| 0.2264 |
| Indoor relative humidity, mean ~ %<70 (pooled) | -0.080 [-0.601, +0.442] | 0.860 | 0.938 | 0.2131 | +1.9 | -0.0 | 0.1839 \| 0.1857 |
| Indoor relative humidity, mean ~ %<70 (daily avg) | -0.132 [-0.634, +0.370] | 0.780 | 0.938 | 0.2133 | +1.6 | -0.3 | 0.1844 \| 0.1857 |
| Indoor VOC index, mean ~ %<70 (pooled) | +0.533 [-0.463, +1.529] | 0.515 | 0.585 | 0.0565 | +1.2 | +1.5 | 0.0273 \| 0.0276 |
| Indoor VOC index, mean ~ %<70 (daily avg) | +0.541 [-0.413, +1.494] | 0.483 | 0.585 | 0.0565 | +1.2 | +1.5 | 0.0274 \| 0.0276 |
| Steps per wear-day ~ %<70 (pooled) | -411.853 [-697.727, -125.980] | 0.050 | **0.039 (FDR<0.05)** | 0.1631 | -3.4 | -3.3 | 0.1428 \| 0.1390 |
| Steps per wear-day ~ %<70 (daily avg) | **-423.808 [-680.504, -167.112]** | **0.024 (FDR<0.05)** | **0.038 (FDR<0.05)** | 0.1635 | -3.7 | -3.6 | 0.1438 \| 0.1390 |
| Brisk-cadence minutes per day ~ %<70 (pooled) | -0.820 [-1.645, +0.006] | 0.198 | 0.380 | 0.1817 | -0.6 | -0.6 | 0.1552 \| 0.1546 |
| Brisk-cadence minutes per day ~ %<70 (daily avg) | -0.881 [-1.693, -0.069] | 0.165 | 0.380 | 0.1822 | -1.0 | -1.0 | 0.1559 \| 0.1546 |
| Resting heart-rate proxy ~ %<70 (pooled) | -0.113 [-0.702, +0.476] | 0.829 | 0.811 | 0.1524 | +1.9 | +7.9 | 0.1239 \| 0.1253 |
| Resting heart-rate proxy ~ %<70 (daily avg) | -0.241 [-0.899, +0.418] | 0.664 | 0.618 | 0.1530 | +1.4 | +7.5 | 0.1244 \| 0.1253 |
| Total sleep time per night ~ %<70 (pooled) | +2.832 [-2.243, +7.907] | 0.491 | 0.444 | 0.0380 | +0.7 | +3.6 | 0.0057 \| 0.0066 |
| Total sleep time per night ~ %<70 (daily avg) | +2.140 [-2.722, +7.002] | 0.611 | 0.523 | 0.0373 | +1.3 | +4.2 | 0.0050 \| 0.0066 |
| Garmin stress score, mean ~ %<70 (pooled) | -0.474 [-1.927, +0.980] | 0.714 | 0.612 | 0.1224 | +1.5 | +14.5 | 0.0919 \| 0.0947 |
| Garmin stress score, mean ~ %<70 (daily avg) | -0.626 [-2.116, +0.863] | 0.630 | 0.508 | 0.1229 | +1.0 | +14.1 | 0.0925 \| 0.0947 |


---

## Band 54-250

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | 2138 | 2138 | **+0.02436** | 0.007284 | [0.01008, 0.03864] | **3.34** | **8.2e-04***** | *** |
| MoCA total score ~ %54-250 (daily avg) | 2138 | 2138 | **+0.02431** | 0.0075 | [0.009609, 0.03901] | **3.24** | **0.001**** | ** |
| Cognitive impairment ~ %54-250 (pooled) | 2138 | 2138 | **-0.01276** | 0.004415 | [-0.02142, -0.004111] | **-2.89** | **0.004**** | ** |
| Cognitive impairment ~ %54-250 (daily avg) | 2138 | 2138 | **-0.01258** | 0.004469 | [-0.02134, -0.003818] | **-2.81** | **0.005**** | ** |
| MoCA memory index score ~ %54-250 (pooled) | 2138 | 2138 | **+0.01116** | 0.005085 | [0.001197, 0.02113] | **2.20** | **0.028*** | * |
| MoCA memory index score ~ %54-250 (daily avg) | 2138 | 2138 | **+0.01103** | 0.00513 | [0.000978, 0.02109] | **2.15** | **0.032*** | * |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | 2135 | 2135 | -0.01304 | 0.01203 | [-0.03661, 0.01053] | -1.08 | 0.278 |  |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | 2135 | 2135 | -0.01201 | 0.01226 | [-0.03603, 0.01202] | -0.98 | 0.327 |  |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | 2135 | 2135 | -0.006643 | 0.004439 | [-0.01534, 0.002057] | -1.50 | 0.135 |  |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | 2135 | 2135 | -0.005932 | 0.004527 | [-0.0148, 0.002941] | -1.31 | 0.190 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | 2100 | 2100 | -0.003863 | 0.002349 | [-0.008466, 0.0007397] | -1.64 | 0.100 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | 2100 | 2100 | -0.003941 | 0.002372 | [-0.00859, 0.0007091] | -1.66 | 0.097 |  |
| Indoor temperature, mean ~ %54-250 (pooled) | 2100 | 2100 | -0.00221 | 0.004525 | [-0.01108, 0.006659] | -0.49 | 0.625 |  |
| Indoor temperature, mean ~ %54-250 (daily avg) | 2100 | 2100 | -0.001916 | 0.004603 | [-0.01094, 0.007105] | -0.42 | 0.677 |  |
| Indoor relative humidity, mean ~ %54-250 (pooled) | 2100 | 2100 | +0.0003887 | 0.01256 | [-0.02423, 0.025] | 0.03 | 0.975 |  |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | 2100 | 2100 | +0.0001247 | 0.01291 | [-0.02518, 0.02543] | 0.01 | 0.992 |  |
| Indoor VOC index, mean ~ %54-250 (pooled) | 2100 | 2100 | +0.06296 | 0.03663 | [-0.008845, 0.1348] | 1.72 | 0.086 |  |
| Indoor VOC index, mean ~ %54-250 (daily avg) | 2100 | 2100 | +0.06658 | 0.03778 | [-0.007472, 0.1406] | 1.76 | 0.078 |  |
| Steps per wear-day ~ %54-250 (pooled) | 1872 | 1872 | -0.716 | 12.2 | [-24.62, 23.19] | -0.06 | 0.953 |  |
| Steps per wear-day ~ %54-250 (daily avg) | 1872 | 1872 | -1.07 | 12.04 | [-24.67, 22.53] | -0.09 | 0.929 |  |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | 1872 | 1872 | -0.007468 | 0.03432 | [-0.07473, 0.0598] | -0.22 | 0.828 |  |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | 1872 | 1872 | -0.008357 | 0.03388 | [-0.07476, 0.05804] | -0.25 | 0.805 |  |
| Resting heart-rate proxy ~ %54-250 (pooled) | 1877 | 1877 | **-0.09173** | 0.02075 | [-0.1324, -0.05107] | **-4.42** | **9.8e-06***** | *** |
| Resting heart-rate proxy ~ %54-250 (daily avg) | 1877 | 1877 | **-0.09281** | 0.02143 | [-0.1348, -0.05081] | **-4.33** | **1.5e-05***** | *** |
| Total sleep time per night ~ %54-250 (pooled) | 1893 | 1893 | +0.09849 | 0.1422 | [-0.1801, 0.3771] | 0.69 | 0.488 |  |
| Total sleep time per night ~ %54-250 (daily avg) | 1893 | 1893 | +0.09236 | 0.1456 | [-0.1929, 0.3777] | 0.63 | 0.526 |  |
| Garmin stress score, mean ~ %54-250 (pooled) | 1879 | 1879 | **-0.1761** | 0.04553 | [-0.2653, -0.08686] | **-3.87** | **1.1e-04***** | *** |
| Garmin stress score, mean ~ %54-250 (daily avg) | 1879 | 1879 | **-0.1782** | 0.04685 | [-0.2701, -0.08638] | **-3.80** | **1.4e-04***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | **+0.268 [+0.111, +0.426]** | **0.004 (FDR<0.05)** | **0.001 (FDR<0.05)** | 0.1068 | -14.6 | +10.0 | 0.0973 \| 0.0915 |
| MoCA total score ~ %54-250 (daily avg) | **+0.265 [+0.105, +0.425]** | **0.006 (FDR<0.05)** | **0.002 (FDR<0.05)** | 0.1066 | -14.2 | +10.5 | 0.0970 \| 0.0915 |
| Cognitive impairment ~ %54-250 (pooled) | **OR 0.869 [0.790, 0.956]** | **0.017 (FDR<0.05)** | **0.007 (FDR<0.05)** | 0.6705 | -6.9 | +6.7 | 0.6630 \| 0.6603 |
| Cognitive impairment ~ %54-250 (daily avg) | **OR 0.872 [0.793, 0.959]** | **0.020 (FDR<0.05)** | **0.008 (FDR<0.05)** | 0.6704 | -6.4 | +7.2 | 0.6628 \| 0.6603 |
| MoCA memory index score ~ %54-250 (pooled) | +0.123 [+0.013, +0.233] | 0.087 | 0.051 | 0.0734 | -2.5 | +2.9 | 0.0643 \| 0.0630 |
| MoCA memory index score ~ %54-250 (daily avg) | +0.120 [+0.011, +0.229] | 0.093 | 0.051 | 0.0733 | -2.3 | +3.1 | 0.0642 \| 0.0630 |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | -0.144 [-0.404, +0.116] | 0.445 | 0.620 | 0.1035 | +0.1 | +0.4 | 0.0915 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | -0.131 [-0.392, +0.131] | 0.495 | 0.620 | 0.1034 | +0.4 | +0.7 | 0.0914 \| 0.0916 |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | OR 0.929 [0.844, 1.023] | 0.272 | 0.245 | 0.6819 | -0.2 | +2.5 | 0.6692 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | OR 0.937 [0.851, 1.033] | 0.351 | 0.295 | 0.6817 | +0.3 | +3.0 | 0.6689 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | -0.043 [-0.094, +0.008] | 0.214 | 0.173 | 0.1527 | -2.6 | +8.3 | 0.1391 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | -0.043 [-0.094, +0.008] | 0.210 | 0.173 | 0.1527 | -2.7 | +8.2 | 0.1392 \| 0.1387 |
| Indoor temperature, mean ~ %54-250 (pooled) | -0.024 [-0.122, +0.074] | 0.778 | 0.982 | 0.2980 | +1.7 | +0.2 | 0.2890 \| 0.2896 |
| Indoor temperature, mean ~ %54-250 (daily avg) | -0.021 [-0.119, +0.078] | 0.805 | 0.982 | 0.2979 | +1.8 | +0.3 | 0.2890 \| 0.2896 |
| Indoor relative humidity, mean ~ %54-250 (pooled) | +0.004 [-0.268, +0.276] | 0.986 | 0.992 | 0.2410 | +2.0 | +0.1 | 0.2299 \| 0.2307 |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | +0.001 [-0.275, +0.278] | 0.995 | 0.992 | 0.2410 | +2.0 | +0.1 | 0.2298 \| 0.2307 |
| Indoor VOC index, mean ~ %54-250 (pooled) | +0.696 [-0.098, +1.490] | 0.195 | 0.665 | 0.0443 | -1.8 | -1.8 | 0.0271 \| 0.0271 |
| Indoor VOC index, mean ~ %54-250 (daily avg) | +0.727 [-0.082, +1.535] | 0.187 | 0.665 | 0.0445 | -2.1 | -2.1 | 0.0272 \| 0.0271 |
| Steps per wear-day ~ %54-250 (pooled) | -7.846 [-269.806, +254.114] | 0.973 | 0.953 | 0.1348 | +2.0 | +10.0 | 0.1205 \| 0.1222 |
| Steps per wear-day ~ %54-250 (daily avg) | -11.532 [-265.942, +242.879] | 0.958 | 0.953 | 0.1348 | +2.0 | +10.0 | 0.1205 \| 0.1222 |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | -0.082 [-0.819, +0.655] | 0.892 | 0.828 | 0.1557 | +1.9 | +10.1 | 0.1433 \| 0.1447 |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | -0.090 [-0.806, +0.626] | 0.876 | 0.828 | 0.1557 | +1.9 | +10.1 | 0.1433 \| 0.1447 |
| Resting heart-rate proxy ~ %54-250 (pooled) | **-1.006 [-1.452, -0.560]** | **8.0e-05 (FDR<0.05)** | **1.4e-05 (FDR<0.05)** | 0.1721 | -25.7 | +45.5 | 0.1596 \| 0.1482 |
| Resting heart-rate proxy ~ %54-250 (daily avg) | **-1.001 [-1.455, -0.548]** | **1.1e-04 (FDR<0.05)** | **1.9e-05 (FDR<0.05)** | 0.1719 | -25.5 | +45.7 | 0.1594 \| 0.1482 |
| Total sleep time per night ~ %54-250 (pooled) | +1.040 [-1.902, +3.981] | 0.656 | 0.582 | 0.0335 | +1.6 | +10.5 | 0.0205 \| 0.0209 |
| Total sleep time per night ~ %54-250 (daily avg) | +0.959 [-2.004, +3.922] | 0.693 | 0.582 | 0.0334 | +1.6 | +10.5 | 0.0204 \| 0.0209 |
| Garmin stress score, mean ~ %54-250 (pooled) | **-1.930 [-2.908, -0.952]** | **6.5e-04 (FDR<0.05)** | **1.6e-04 (FDR<0.05)** | 0.1156 | -20.4 | +40.0 | 0.0998 \| 0.0902 |
| Garmin stress score, mean ~ %54-250 (daily avg) | **-1.922 [-2.912, -0.932]** | **8.0e-04 (FDR<0.05)** | **1.9e-04 (FDR<0.05)** | 0.1155 | -20.2 | +40.2 | 0.0996 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | 1271 | 1271 | +0.05585 | 0.03235 | [-0.007559, 0.1193] | 1.73 | 0.084 |  |
| MoCA total score ~ %54-250 (daily avg) | 1271 | 1271 | +0.05714 | 0.03361 | [-0.008734, 0.123] | 1.70 | 0.089 |  |
| Cognitive impairment ~ %54-250 (pooled) | 1271 | 1271 | -0.00545 | 0.01245 | [-0.02984, 0.01894] | -0.44 | 0.661 |  |
| Cognitive impairment ~ %54-250 (daily avg) | 1271 | 1271 | -0.004834 | 0.01268 | [-0.02969, 0.02002] | -0.38 | 0.703 |  |
| MoCA memory index score ~ %54-250 (pooled) | 1271 | 1271 | **+0.03412** | 0.01271 | [0.009217, 0.05902] | **2.69** | **0.007**** | ** |
| MoCA memory index score ~ %54-250 (daily avg) | 1271 | 1271 | **+0.03621** | 0.01282 | [0.01109, 0.06134] | **2.82** | **0.005**** | ** |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | 1270 | 1270 | +0.02713 | 0.03045 | [-0.03256, 0.08682] | 0.89 | 0.373 |  |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | 1270 | 1270 | +0.02672 | 0.03189 | [-0.03579, 0.08923] | 0.84 | 0.402 |  |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | 1270 | 1270 | -0.003937 | 0.01333 | [-0.03005, 0.02218] | -0.30 | 0.768 |  |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | 1270 | 1270 | -0.004079 | 0.01352 | [-0.03059, 0.02243] | -0.30 | 0.763 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | 1251 | 1251 | +0.003746 | 0.001987 | [-0.0001485, 0.00764] | 1.89 | 0.059 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | 1251 | 1251 | +0.003707 | 0.00196 | [-0.0001342, 0.007549] | 1.89 | 0.059 |  |
| Indoor temperature, mean ~ %54-250 (pooled) | 1251 | 1251 | -0.007218 | 0.01454 | [-0.03572, 0.02129] | -0.50 | 0.620 |  |
| Indoor temperature, mean ~ %54-250 (daily avg) | 1251 | 1251 | -0.006304 | 0.01453 | [-0.03479, 0.02218] | -0.43 | 0.664 |  |
| Indoor relative humidity, mean ~ %54-250 (pooled) | 1251 | 1251 | -0.02794 | 0.0264 | [-0.07968, 0.02379] | -1.06 | 0.290 |  |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | 1251 | 1251 | -0.03054 | 0.02668 | [-0.08283, 0.02174] | -1.14 | 0.252 |  |
| Indoor VOC index, mean ~ %54-250 (pooled) | 1251 | 1251 | +0.114 | 0.06693 | [-0.01718, 0.2452] | 1.70 | 0.089 |  |
| Indoor VOC index, mean ~ %54-250 (daily avg) | 1251 | 1251 | +0.1156 | 0.07058 | [-0.02275, 0.2539] | 1.64 | 0.102 |  |
| Steps per wear-day ~ %54-250 (pooled) | 1125 | 1125 | -17.2 | 27.35 | [-70.8, 36.39] | -0.63 | 0.529 |  |
| Steps per wear-day ~ %54-250 (daily avg) | 1125 | 1125 | -18.92 | 27.3 | [-72.42, 34.58] | -0.69 | 0.488 |  |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | 1125 | 1125 | -0.08962 | 0.09423 | [-0.2743, 0.09507] | -0.95 | 0.342 |  |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | 1125 | 1125 | -0.09328 | 0.0972 | [-0.2838, 0.09724] | -0.96 | 0.337 |  |
| Resting heart-rate proxy ~ %54-250 (pooled) | 1128 | 1128 | -0.1133 | 0.07036 | [-0.2512, 0.0246] | -1.61 | 0.107 |  |
| Resting heart-rate proxy ~ %54-250 (daily avg) | 1128 | 1128 | -0.1156 | 0.07517 | [-0.2629, 0.03177] | -1.54 | 0.124 |  |
| Total sleep time per night ~ %54-250 (pooled) | 1137 | 1137 | +0.1174 | 0.4156 | [-0.6972, 0.932] | 0.28 | 0.778 |  |
| Total sleep time per night ~ %54-250 (daily avg) | 1137 | 1137 | +0.1146 | 0.4281 | [-0.7245, 0.9536] | 0.27 | 0.789 |  |
| Garmin stress score, mean ~ %54-250 (pooled) | 1130 | 1130 | -0.1336 | 0.2101 | [-0.5454, 0.2782] | -0.64 | 0.525 |  |
| Garmin stress score, mean ~ %54-250 (daily avg) | 1130 | 1130 | -0.1331 | 0.2214 | [-0.5671, 0.3009] | -0.60 | 0.548 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | +0.272 [-0.037, +0.582] | 0.404 | 0.138 | 0.1061 | -10.6 | +3.1 | 0.0799 \| 0.0789 |
| MoCA total score ~ %54-250 (daily avg) | +0.273 [-0.042, +0.588] | 0.406 | 0.138 | 0.1062 | -10.7 | +3.0 | 0.0798 \| 0.0789 |
| Cognitive impairment ~ %54-250 (pooled) | OR 0.974 [0.865, 1.097] | 0.932 | 0.834 | 0.6595 | +1.8 | +1.6 | 0.6434 \| 0.6443 |
| Cognitive impairment ~ %54-250 (daily avg) | OR 0.977 [0.868, 1.100] | 0.932 | 0.834 | 0.6595 | +1.9 | +1.6 | 0.6434 \| 0.6443 |
| MoCA memory index score ~ %54-250 (pooled) | +0.166 [+0.045, +0.288] | 0.090 | **0.025 (FDR<0.05)** | 0.0749 | -3.4 | -2.7 | 0.0504 \| 0.0477 |
| MoCA memory index score ~ %54-250 (daily avg) | +0.173 [+0.053, +0.293] | 0.068 | **0.020 (FDR<0.05)** | 0.0752 | -3.8 | -3.2 | 0.0506 \| 0.0477 |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | +0.132 [-0.159, +0.423] | 0.771 | 0.953 | 0.0915 | +1.0 | -1.0 | 0.0665 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | +0.127 [-0.171, +0.425] | 0.804 | 0.953 | 0.0914 | +1.0 | -1.0 | 0.0664 \| 0.0675 |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | OR 0.981 [0.864, 1.114] | 0.932 | 0.958 | 0.6934 | +1.9 | +0.8 | 0.6714 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | OR 0.981 [0.864, 1.113] | 0.932 | 0.958 | 0.6934 | +1.9 | +0.8 | 0.6711 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | +0.018 [-0.001, +0.038] | 0.339 | 0.265 | 0.1365 | +1.4 | -0.6 | 0.1140 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | +0.018 [-0.001, +0.036] | 0.339 | 0.265 | 0.1365 | +1.5 | -0.5 | 0.1140 \| 0.1139 |
| Indoor temperature, mean ~ %54-250 (pooled) | -0.035 [-0.176, +0.105] | 0.932 | 0.915 | 0.3100 | +1.6 | -0.4 | 0.2884 \| 0.2892 |
| Indoor temperature, mean ~ %54-250 (daily avg) | -0.030 [-0.167, +0.107] | 0.932 | 0.936 | 0.3099 | +1.7 | -0.3 | 0.2884 \| 0.2892 |
| Indoor relative humidity, mean ~ %54-250 (pooled) | -0.137 [-0.392, +0.117] | 0.672 | 0.597 | 0.2600 | +1.3 | +1.8 | 0.2400 \| 0.2403 |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | -0.147 [-0.399, +0.105] | 0.629 | 0.597 | 0.2600 | +1.2 | +1.7 | 0.2401 \| 0.2403 |
| Indoor VOC index, mean ~ %54-250 (pooled) | +0.560 [-0.084, +1.205] | 0.406 | 0.490 | 0.0251 | +0.3 | -0.3 | 0.0029 \| 0.0025 |
| Indoor VOC index, mean ~ %54-250 (daily avg) | +0.556 [-0.110, +1.222] | 0.432 | 0.490 | 0.0250 | +0.3 | -0.3 | 0.0028 \| 0.0025 |
| Steps per wear-day ~ %54-250 (pooled) | -77.498 [-318.954, +163.959] | 0.924 | 0.958 | 0.1249 | +1.5 | +4.8 | 0.1073 \| 0.1080 |
| Steps per wear-day ~ %54-250 (daily avg) | -82.116 [-314.334, +150.102] | 0.884 | 0.958 | 0.1249 | +1.5 | +4.8 | 0.1075 \| 0.1080 |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | -0.404 [-1.236, +0.428] | 0.734 | 0.882 | 0.1396 | +0.7 | +4.1 | 0.1246 \| 0.1245 |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | -0.405 [-1.232, +0.422] | 0.732 | 0.882 | 0.1397 | +0.7 | +4.1 | 0.1246 \| 0.1245 |
| Resting heart-rate proxy ~ %54-250 (pooled) | -0.510 [-1.130, +0.111] | 0.441 | 0.175 | 0.1337 | -3.4 | +7.9 | 0.1054 \| 0.1044 |
| Resting heart-rate proxy ~ %54-250 (daily avg) | -0.501 [-1.140, +0.138] | 0.472 | 0.186 | 0.1335 | -3.2 | +8.0 | 0.1050 \| 0.1044 |
| Total sleep time per night ~ %54-250 (pooled) | +0.466 [-2.768, +3.701] | 0.932 | 0.936 | 0.0206 | +1.9 | +3.9 | -0.0060 \| -0.0051 |
| Total sleep time per night ~ %54-250 (daily avg) | +0.436 [-2.757, +3.629] | 0.936 | 0.936 | 0.0206 | +1.9 | +4.0 | -0.0059 \| -0.0051 |
| Garmin stress score, mean ~ %54-250 (pooled) | -0.601 [-2.452, +1.250] | 0.924 | 0.708 | 0.0738 | +0.5 | +8.3 | 0.0469 \| 0.0510 |
| Garmin stress score, mean ~ %54-250 (daily avg) | -0.576 [-2.456, +1.303] | 0.932 | 0.708 | 0.0737 | +0.6 | +8.4 | 0.0466 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | 867 | 867 | +0.01351 | 0.007467 | [-0.001125, 0.02815] | 1.81 | 0.070 |  |
| MoCA total score ~ %54-250 (daily avg) | 867 | 867 | +0.0134 | 0.007628 | [-0.001548, 0.02835] | 1.76 | 0.079 |  |
| Cognitive impairment ~ %54-250 (pooled) | 867 | 867 | -0.009233 | 0.004805 | [-0.01865, 0.0001836] | -1.92 | 0.055 |  |
| Cognitive impairment ~ %54-250 (daily avg) | 867 | 867 | -0.009102 | 0.004856 | [-0.01862, 0.0004147] | -1.87 | 0.061 |  |
| MoCA memory index score ~ %54-250 (pooled) | 867 | 867 | +0.007967 | 0.005482 | [-0.002779, 0.01871] | 1.45 | 0.146 |  |
| MoCA memory index score ~ %54-250 (daily avg) | 867 | 867 | +0.007585 | 0.005497 | [-0.003189, 0.01836] | 1.38 | 0.168 |  |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | 865 | 865 | -0.01921 | 0.01343 | [-0.04553, 0.007111] | -1.43 | 0.153 |  |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | 865 | 865 | -0.01777 | 0.0137 | [-0.04463, 0.00909] | -1.30 | 0.195 |  |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | 865 | 865 | -0.007745 | 0.00486 | [-0.01727, 0.00178] | -1.59 | 0.111 |  |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | 865 | 865 | -0.006827 | 0.004944 | [-0.01652, 0.002864] | -1.38 | 0.167 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | 849 | 849 | -0.004355 | 0.002737 | [-0.009719, 0.001009] | -1.59 | 0.112 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | 849 | 849 | -0.004444 | 0.002753 | [-0.009839, 0.000952] | -1.61 | 0.106 |  |
| Indoor temperature, mean ~ %54-250 (pooled) | 849 | 849 | +0.001641 | 0.005238 | [-0.008625, 0.01191] | 0.31 | 0.754 |  |
| Indoor temperature, mean ~ %54-250 (daily avg) | 849 | 849 | +0.001787 | 0.00532 | [-0.008639, 0.01221] | 0.34 | 0.737 |  |
| Indoor relative humidity, mean ~ %54-250 (pooled) | 849 | 849 | +0.005567 | 0.01454 | [-0.02293, 0.03406] | 0.38 | 0.702 |  |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | 849 | 849 | +0.005617 | 0.01494 | [-0.02366, 0.03489] | 0.38 | 0.707 |  |
| Indoor VOC index, mean ~ %54-250 (pooled) | 849 | 849 | +0.07101 | 0.04286 | [-0.01299, 0.155] | 1.66 | 0.098 |  |
| Indoor VOC index, mean ~ %54-250 (daily avg) | 849 | 849 | +0.07517 | 0.04417 | [-0.0114, 0.1617] | 1.70 | 0.089 |  |
| Steps per wear-day ~ %54-250 (pooled) | 747 | 747 | +5.99 | 13.69 | [-20.83, 32.81] | 0.44 | 0.662 |  |
| Steps per wear-day ~ %54-250 (daily avg) | 747 | 747 | +5.368 | 13.36 | [-20.83, 31.56] | 0.40 | 0.688 |  |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | 747 | 747 | +0.01956 | 0.03759 | [-0.05412, 0.09323] | 0.52 | 0.603 |  |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | 747 | 747 | +0.01776 | 0.03671 | [-0.05419, 0.0897] | 0.48 | 0.629 |  |
| Resting heart-rate proxy ~ %54-250 (pooled) | 749 | 749 | **-0.04271** | 0.02146 | [-0.08477, -0.0006513] | **-1.99** | **0.047*** | * |
| Resting heart-rate proxy ~ %54-250 (daily avg) | 749 | 749 | **-0.04394** | 0.02181 | [-0.08669, -0.001191] | **-2.01** | **0.044*** | * |
| Total sleep time per night ~ %54-250 (pooled) | 756 | 756 | +0.03181 | 0.1598 | [-0.2814, 0.3451] | 0.20 | 0.842 |  |
| Total sleep time per night ~ %54-250 (daily avg) | 756 | 756 | +0.02802 | 0.1628 | [-0.2911, 0.3471] | 0.17 | 0.863 |  |
| Garmin stress score, mean ~ %54-250 (pooled) | 749 | 749 | **-0.1129** | 0.04833 | [-0.2076, -0.01813] | **-2.33** | **0.020*** | * |
| Garmin stress score, mean ~ %54-250 (daily avg) | 749 | 749 | **-0.1156** | 0.04935 | [-0.2124, -0.01892] | **-2.34** | **0.019*** | * |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %54-250 (pooled) | +0.210 [-0.018, +0.438] | 0.229 | 0.109 | 0.0845 | -1.5 | +0.1 | 0.0565 \| 0.0541 |
| MoCA total score ~ %54-250 (daily avg) | +0.206 [-0.024, +0.436] | 0.242 | 0.112 | 0.0844 | -1.3 | +0.2 | 0.0564 \| 0.0541 |
| Cognitive impairment ~ %54-250 (pooled) | OR 0.866 [0.748, 1.003] | 0.204 | 0.114 | 0.6640 | -1.8 | -0.2 | 0.6447 \| 0.6425 |
| Cognitive impairment ~ %54-250 (daily avg) | OR 0.869 [0.751, 1.006] | 0.216 | 0.114 | 0.6638 | -1.7 | +0.0 | 0.6448 \| 0.6425 |
| MoCA memory index score ~ %54-250 (pooled) | +0.124 [-0.043, +0.291] | 0.329 | 0.181 | 0.0615 | +0.3 | +2.0 | 0.0299 \| 0.0286 |
| MoCA memory index score ~ %54-250 (daily avg) | +0.117 [-0.049, +0.282] | 0.360 | 0.192 | 0.0613 | +0.5 | +2.2 | 0.0297 \| 0.0286 |
| CES-D-10 depressive symptoms ~ %54-250 (pooled) | -0.299 [-0.709, +0.111] | 0.334 | 0.578 | 0.1143 | -1.1 | +0.1 | 0.0788 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %54-250 (daily avg) | -0.274 [-0.687, +0.140] | 0.390 | 0.578 | 0.1138 | -0.6 | +0.7 | 0.0784 \| 0.0796 |
| Clinically relevant depressive symptoms ~ %54-250 (pooled) | OR 0.886 [0.764, 1.028] | 0.270 | 0.215 | 0.6656 | -0.5 | +2.5 | 0.6365 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %54-250 (daily avg) | OR 0.900 [0.775, 1.045] | 0.360 | 0.291 | 0.6650 | +0.2 | +3.2 | 0.6351 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (pooled) | -0.068 [-0.152, +0.016] | 0.270 | 0.173 | 0.1583 | -2.5 | +7.0 | 0.1314 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %54-250 (daily avg) | -0.069 [-0.152, +0.015] | 0.270 | 0.173 | 0.1584 | -2.5 | +6.9 | 0.1315 \| 0.1310 |
| Indoor temperature, mean ~ %54-250 (pooled) | +0.026 [-0.135, +0.186] | 0.852 | 0.907 | 0.2503 | +1.9 | +0.2 | 0.2227 \| 0.2264 |
| Indoor temperature, mean ~ %54-250 (daily avg) | +0.028 [-0.133, +0.189] | 0.842 | 0.907 | 0.2503 | +1.9 | +0.2 | 0.2227 \| 0.2264 |
| Indoor relative humidity, mean ~ %54-250 (pooled) | +0.087 [-0.358, +0.532] | 0.829 | 0.938 | 0.2131 | +1.8 | -0.0 | 0.1840 \| 0.1857 |
| Indoor relative humidity, mean ~ %54-250 (daily avg) | +0.087 [-0.365, +0.539] | 0.829 | 0.938 | 0.2131 | +1.8 | -0.0 | 0.1839 \| 0.1857 |
| Indoor VOC index, mean ~ %54-250 (pooled) | +1.109 [-0.203, +2.420] | 0.263 | 0.504 | 0.0594 | -1.4 | -1.1 | 0.0290 \| 0.0276 |
| Indoor VOC index, mean ~ %54-250 (daily avg) | +1.161 [-0.176, +2.497] | 0.247 | 0.504 | 0.0598 | -1.7 | -1.4 | 0.0293 \| 0.0276 |
| Steps per wear-day ~ %54-250 (pooled) | +94.194 [-327.618, +516.007] | 0.812 | 0.751 | 0.1573 | +1.7 | +1.8 | 0.1374 \| 0.1390 |
| Steps per wear-day ~ %54-250 (daily avg) | +83.275 [-323.087, +489.637] | 0.825 | 0.751 | 0.1573 | +1.8 | +1.9 | 0.1375 \| 0.1390 |
| Brisk-cadence minutes per day ~ %54-250 (pooled) | +0.308 [-0.851, +1.466] | 0.780 | 0.821 | 0.1793 | +1.6 | +1.7 | 0.1533 \| 0.1546 |
| Brisk-cadence minutes per day ~ %54-250 (daily avg) | +0.275 [-0.841, +1.392] | 0.795 | 0.821 | 0.1792 | +1.7 | +1.8 | 0.1533 \| 0.1546 |
| Resting heart-rate proxy ~ %54-250 (pooled) | -0.672 [-1.334, -0.010] | 0.189 | 0.087 | 0.1576 | -2.7 | +3.4 | 0.1282 \| 0.1253 |
| Resting heart-rate proxy ~ %54-250 (daily avg) | -0.682 [-1.346, -0.018] | 0.182 | 0.087 | 0.1577 | -2.8 | +3.2 | 0.1281 \| 0.1253 |
| Total sleep time per night ~ %54-250 (pooled) | +0.486 [-4.296, +5.268] | 0.896 | 0.863 | 0.0364 | +2.0 | +4.9 | 0.0044 \| 0.0066 |
| Total sleep time per night ~ %54-250 (daily avg) | +0.422 [-4.384, +5.228] | 0.912 | 0.863 | 0.0364 | +2.0 | +4.9 | 0.0043 \| 0.0066 |
| Garmin stress score, mean ~ %54-250 (pooled) | -1.776 [-3.266, -0.285] | 0.116 | **0.034 (FDR<0.05)** | 0.1306 | -5.5 | +7.6 | 0.1011 \| 0.0947 |
| Garmin stress score, mean ~ %54-250 (daily avg) | -1.795 [-3.297, -0.294] | 0.116 | **0.034 (FDR<0.05)** | 0.1308 | -5.7 | +7.4 | 0.1012 \| 0.0947 |


---

## Band >180

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | 2138 | 1927 | **-0.01748** | 0.003708 | [-0.02475, -0.01021] | **-4.71** | **2.4e-06***** | *** |
| MoCA total score ~ %>180 (daily avg) | 2138 | 1876 | **-0.01713** | 0.003713 | [-0.0244, -0.009849] | **-4.61** | **4.0e-06***** | *** |
| MoCA total score ~ %>180 nocturnal | 2138 | 1109 | **-0.01568** | 0.003777 | [-0.02308, -0.008274] | **-4.15** | **3.3e-05***** | *** |
| Cognitive impairment ~ %>180 (pooled) | 2138 | 1927 | **+0.009094** | 0.002337 | [0.004514, 0.01367] | **3.89** | **9.9e-05***** | *** |
| Cognitive impairment ~ %>180 (daily avg) | 2138 | 1876 | **+0.008958** | 0.002331 | [0.00439, 0.01353] | **3.84** | **1.2e-04***** | *** |
| Cognitive impairment ~ %>180 nocturnal | 2138 | 1109 | **+0.007721** | 0.002332 | [0.003151, 0.01229] | **3.31** | **9.3e-04***** | *** |
| MoCA memory index score ~ %>180 (pooled) | 2138 | 1927 | **-0.008234** | 0.002859 | [-0.01384, -0.002631] | **-2.88** | **0.004**** | ** |
| MoCA memory index score ~ %>180 (daily avg) | 2138 | 1876 | **-0.008052** | 0.002858 | [-0.01365, -0.002449] | **-2.82** | **0.005**** | ** |
| MoCA memory index score ~ %>180 nocturnal | 2138 | 1109 | **-0.007592** | 0.002857 | [-0.01319, -0.001992] | **-2.66** | **0.008**** | ** |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | 2135 | 1924 | +0.006793 | 0.005898 | [-0.004767, 0.01835] | 1.15 | 0.249 |  |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | 2135 | 1873 | +0.006398 | 0.005887 | [-0.00514, 0.01794] | 1.09 | 0.277 |  |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | 2135 | 1106 | +0.01097 | 0.006023 | [-0.0008351, 0.02277] | 1.82 | 0.069 |  |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | 2135 | 1924 | **+0.005303** | 0.002623 | [0.0001619, 0.01044] | **2.02** | **0.043*** | * |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | 2135 | 1873 | +0.005081 | 0.002623 | [-5.933e-05, 0.01022] | 1.94 | 0.053 |  |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | 2135 | 1106 | **+0.007555** | 0.002526 | [0.002605, 0.0125] | **2.99** | **0.003**** | ** |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | 2100 | 1896 | +0.001952 | 0.001151 | [-0.0003031, 0.004207] | 1.70 | 0.090 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | 2100 | 1846 | +0.001921 | 0.001148 | [-0.0003302, 0.004172] | 1.67 | 0.094 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | 2100 | 1095 | **+0.002313** | 0.001169 | [2.242e-05, 0.004603] | **1.98** | **0.048*** | * |
| Indoor temperature, mean ~ %>180 (pooled) | 2100 | 1896 | +0.0009689 | 0.002384 | [-0.003704, 0.005642] | 0.41 | 0.684 |  |
| Indoor temperature, mean ~ %>180 (daily avg) | 2100 | 1846 | +0.0007993 | 0.002382 | [-0.003869, 0.005468] | 0.34 | 0.737 |  |
| Indoor temperature, mean ~ %>180 nocturnal | 2100 | 1095 | +0.0006301 | 0.002428 | [-0.004128, 0.005388] | 0.26 | 0.795 |  |
| Indoor relative humidity, mean ~ %>180 (pooled) | 2100 | 1896 | -0.002454 | 0.006974 | [-0.01612, 0.01122] | -0.35 | 0.725 |  |
| Indoor relative humidity, mean ~ %>180 (daily avg) | 2100 | 1846 | -0.002195 | 0.006969 | [-0.01586, 0.01146] | -0.32 | 0.753 |  |
| Indoor relative humidity, mean ~ %>180 nocturnal | 2100 | 1095 | -0.004339 | 0.006914 | [-0.01789, 0.009213] | -0.63 | 0.530 |  |
| Indoor VOC index, mean ~ %>180 (pooled) | 2100 | 1896 | -0.009003 | 0.02204 | [-0.0522, 0.0342] | -0.41 | 0.683 |  |
| Indoor VOC index, mean ~ %>180 (daily avg) | 2100 | 1846 | -0.01014 | 0.02208 | [-0.05341, 0.03313] | -0.46 | 0.646 |  |
| Indoor VOC index, mean ~ %>180 nocturnal | 2100 | 1095 | -0.007573 | 0.02437 | [-0.05533, 0.04019] | -0.31 | 0.756 |  |
| Steps per wear-day ~ %>180 (pooled) | 1872 | 1677 | +7.299 | 6.523 | [-5.486, 20.08] | 1.12 | 0.263 |  |
| Steps per wear-day ~ %>180 (daily avg) | 1872 | 1628 | +7.23 | 6.505 | [-5.518, 19.98] | 1.11 | 0.266 |  |
| Steps per wear-day ~ %>180 nocturnal | 1872 | 959 | +7.406 | 6.741 | [-5.807, 20.62] | 1.10 | 0.272 |  |
| Brisk-cadence minutes per day ~ %>180 (pooled) | 1872 | 1677 | +0.02202 | 0.01844 | [-0.01413, 0.05817] | 1.19 | 0.232 |  |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | 1872 | 1628 | +0.02204 | 0.01842 | [-0.01407, 0.05815] | 1.20 | 0.232 |  |
| Brisk-cadence minutes per day ~ %>180 nocturnal | 1872 | 959 | +0.01997 | 0.01906 | [-0.01739, 0.05734] | 1.05 | 0.295 |  |
| Resting heart-rate proxy ~ %>180 (pooled) | 1877 | 1680 | **+0.08311** | 0.01077 | [0.06201, 0.1042] | **7.72** | **1.2e-14***** | *** |
| Resting heart-rate proxy ~ %>180 (daily avg) | 1877 | 1631 | **+0.08253** | 0.01072 | [0.06151, 0.1035] | **7.70** | **1.4e-14***** | *** |
| Resting heart-rate proxy ~ %>180 nocturnal | 1877 | 960 | **+0.06833** | 0.01087 | [0.04701, 0.08964] | **6.28** | **3.3e-10***** | *** |
| Total sleep time per night ~ %>180 (pooled) | 1893 | 1699 | -0.1017 | 0.08123 | [-0.2609, 0.05753] | -1.25 | 0.211 |  |
| Total sleep time per night ~ %>180 (daily avg) | 1893 | 1652 | -0.09821 | 0.08135 | [-0.2577, 0.06123] | -1.21 | 0.227 |  |
| Total sleep time per night ~ %>180 nocturnal | 1893 | 969 | -0.03407 | 0.08043 | [-0.1917, 0.1236] | -0.42 | 0.672 |  |
| Garmin stress score, mean ~ %>180 (pooled) | 1879 | 1681 | **+0.1494** | 0.02218 | [0.1059, 0.1929] | **6.73** | **1.7e-11***** | *** |
| Garmin stress score, mean ~ %>180 (daily avg) | 1879 | 1632 | **+0.1477** | 0.0221 | [0.1044, 0.191] | **6.68** | **2.3e-11***** | *** |
| Garmin stress score, mean ~ %>180 nocturnal | 1879 | 962 | **+0.1206** | 0.02216 | [0.07714, 0.164] | **5.44** | **5.3e-08***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | **-0.355 [-0.503, -0.207]** | **2.4e-05 (FDR<0.05)** | **9.3e-06 (FDR<0.05)** | 0.1116 | -26.3 | -1.6 | 0.1021 \| 0.0915 |
| MoCA total score ~ %>180 (daily avg) | **-0.349 [-0.497, -0.201]** | **3.7e-05 (FDR<0.05)** | **1.1e-05 (FDR<0.05)** | 0.1112 | -25.3 | -0.6 | 0.1017 \| 0.0915 |
| MoCA total score ~ %>180 nocturnal | **-0.317 [-0.467, -0.167]** | **2.3e-04 (FDR<0.05)** | **6.9e-05 (FDR<0.05)** | 0.1093 | -20.7 | +3.9 | 0.1001 \| 0.0915 |
| Cognitive impairment ~ %>180 (pooled) | **OR 1.203 [1.096, 1.320]** | **6.1e-04 (FDR<0.05)** | **3.4e-04 (FDR<0.05)** | 0.6732 | -13.4 | +0.2 | 0.6653 \| 0.6603 |
| Cognitive impairment ~ %>180 (daily avg) | **OR 1.200 [1.094, 1.317]** | **7.0e-04 (FDR<0.05)** | **3.4e-04 (FDR<0.05)** | 0.6731 | -13.0 | +0.6 | 0.6650 \| 0.6603 |
| Cognitive impairment ~ %>180 nocturnal | **OR 1.169 [1.066, 1.282]** | **0.005 (FDR<0.05)** | **0.002 (FDR<0.05)** | 0.6718 | -9.1 | +4.5 | 0.6634 \| 0.6603 |
| MoCA memory index score ~ %>180 (pooled) | **-0.167 [-0.281, -0.053]** | **0.017 (FDR<0.05)** | **0.016 (FDR<0.05)** | 0.0750 | -6.1 | -0.7 | 0.0657 \| 0.0630 |
| MoCA memory index score ~ %>180 (daily avg) | **-0.164 [-0.278, -0.050]** | **0.020 (FDR<0.05)** | **0.017 (FDR<0.05)** | 0.0748 | -5.7 | -0.4 | 0.0655 \| 0.0630 |
| MoCA memory index score ~ %>180 nocturnal | **-0.154 [-0.267, -0.040]** | **0.029 (FDR<0.05)** | **0.021 (FDR<0.05)** | 0.0744 | -4.8 | +0.5 | 0.0652 \| 0.0630 |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | +0.138 [-0.097, +0.373] | 0.416 | 0.620 | 0.1035 | +0.3 | +0.6 | 0.0917 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | +0.130 [-0.105, +0.365] | 0.445 | 0.620 | 0.1034 | +0.5 | +0.7 | 0.0916 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | +0.222 [-0.017, +0.461] | 0.172 | 0.620 | 0.1046 | -2.4 | -2.2 | 0.0930 \| 0.0916 |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | OR 1.114 [1.003, 1.236] | 0.124 | 0.158 | 0.6824 | -2.0 | +0.7 | 0.6692 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | OR 1.109 [0.999, 1.231] | 0.141 | 0.158 | 0.6824 | -1.6 | +1.1 | 0.6691 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | **OR 1.165 [1.054, 1.288]** | **0.012 (FDR<0.05)** | **0.043 (FDR<0.05)** | 0.6860 | -6.6 | -3.9 | 0.6737 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | +0.040 [-0.006, +0.086] | 0.202 | 0.173 | 0.1524 | -1.9 | +9.0 | 0.1391 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | +0.039 [-0.007, +0.085] | 0.208 | 0.173 | 0.1523 | -1.8 | +9.1 | 0.1391 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | +0.047 [+0.000, +0.093] | 0.132 | 0.173 | 0.1530 | -3.5 | +7.5 | 0.1394 \| 0.1387 |
| Indoor temperature, mean ~ %>180 (pooled) | +0.020 [-0.075, +0.115] | 0.805 | 0.982 | 0.2979 | +1.8 | +0.3 | 0.2890 \| 0.2896 |
| Indoor temperature, mean ~ %>180 (daily avg) | +0.016 [-0.079, +0.112] | 0.842 | 0.982 | 0.2979 | +1.9 | +0.4 | 0.2890 \| 0.2896 |
| Indoor temperature, mean ~ %>180 nocturnal | +0.013 [-0.084, +0.109] | 0.872 | 0.982 | 0.2979 | +1.9 | +0.4 | 0.2889 \| 0.2896 |
| Indoor relative humidity, mean ~ %>180 (pooled) | -0.050 [-0.328, +0.228] | 0.837 | 0.898 | 0.2411 | +1.9 | +0.0 | 0.2300 \| 0.2307 |
| Indoor relative humidity, mean ~ %>180 (daily avg) | -0.045 [-0.324, +0.234] | 0.844 | 0.898 | 0.2411 | +1.9 | +0.0 | 0.2300 \| 0.2307 |
| Indoor relative humidity, mean ~ %>180 nocturnal | -0.088 [-0.362, +0.187] | 0.693 | 0.898 | 0.2412 | +1.6 | -0.3 | 0.2300 \| 0.2307 |
| Indoor VOC index, mean ~ %>180 (pooled) | -0.183 [-1.063, +0.696] | 0.805 | 0.868 | 0.0427 | +1.7 | +1.7 | 0.0256 \| 0.0271 |
| Indoor VOC index, mean ~ %>180 (daily avg) | -0.207 [-1.091, +0.676] | 0.795 | 0.868 | 0.0427 | +1.7 | +1.7 | 0.0256 \| 0.0271 |
| Indoor VOC index, mean ~ %>180 nocturnal | -0.153 [-1.120, +0.814] | 0.846 | 0.868 | 0.0427 | +1.8 | +1.8 | 0.0251 \| 0.0271 |
| Steps per wear-day ~ %>180 (pooled) | +146.772 [-110.327, +403.871] | 0.438 | 0.383 | 0.1358 | -0.1 | +7.9 | 0.1219 \| 0.1222 |
| Steps per wear-day ~ %>180 (daily avg) | +145.835 [-111.304, +402.974] | 0.439 | 0.383 | 0.1358 | -0.1 | +7.9 | 0.1219 \| 0.1222 |
| Steps per wear-day ~ %>180 nocturnal | +148.405 [-116.365, +413.176] | 0.440 | 0.383 | 0.1358 | -0.1 | +7.8 | 0.1216 \| 0.1222 |
| Brisk-cadence minutes per day ~ %>180 (pooled) | +0.443 [-0.284, +1.170] | 0.400 | 0.313 | 0.1566 | -0.1 | +8.1 | 0.1446 \| 0.1447 |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | +0.445 [-0.284, +1.173] | 0.400 | 0.313 | 0.1566 | -0.1 | +8.1 | 0.1445 \| 0.1447 |
| Brisk-cadence minutes per day ~ %>180 nocturnal | +0.400 [-0.348, +1.149] | 0.467 | 0.351 | 0.1564 | +0.3 | +8.4 | 0.1443 \| 0.1447 |
| Resting heart-rate proxy ~ %>180 (pooled) | **+1.673 [+1.249, +2.098]** | **6.3e-13 (FDR<0.05)** | **5.2e-14 (FDR<0.05)** | 0.1927 | -73.2 | -1.9 | 0.1804 \| 0.1482 |
| Resting heart-rate proxy ~ %>180 (daily avg) | **+1.667 [+1.242, +2.091]** | **6.8e-13 (FDR<0.05)** | **5.4e-14 (FDR<0.05)** | 0.1924 | -72.5 | -1.3 | 0.1801 \| 0.1482 |
| Resting heart-rate proxy ~ %>180 nocturnal | **+1.369 [+0.942, +1.796]** | **5.5e-09 (FDR<0.05)** | **6.4e-10 (FDR<0.05)** | 0.1820 | -48.3 | +22.9 | 0.1697 \| 0.1482 |
| Total sleep time per night ~ %>180 (pooled) | -2.019 [-5.179, +1.142] | 0.376 | 0.403 | 0.0341 | +0.4 | +9.3 | 0.0204 \| 0.0209 |
| Total sleep time per night ~ %>180 (daily avg) | -1.956 [-5.130, +1.219] | 0.398 | 0.403 | 0.0340 | +0.5 | +9.4 | 0.0203 \| 0.0209 |
| Total sleep time per night ~ %>180 nocturnal | -0.672 [-3.781, +2.437] | 0.805 | 0.718 | 0.0333 | +1.8 | +10.7 | 0.0200 \| 0.0209 |
| Garmin stress score, mean ~ %>180 (pooled) | **+3.006 [+2.131, +3.881]** | **3.8e-10 (FDR<0.05)** | **8.5e-11 (FDR<0.05)** | 0.1299 | -50.9 | +9.5 | 0.1145 \| 0.0902 |
| Garmin stress score, mean ~ %>180 (daily avg) | **+2.982 [+2.108, +3.856]** | **4.8e-10 (FDR<0.05)** | **9.0e-11 (FDR<0.05)** | 0.1295 | -50.0 | +10.4 | 0.1141 \| 0.0902 |
| Garmin stress score, mean ~ %>180 nocturnal | **+2.415 [+1.545, +3.285]** | **6.4e-07 (FDR<0.05)** | **1.0e-07 (FDR<0.05)** | 0.1212 | -32.2 | +28.2 | 0.1058 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | 1271 | 1094 | **-0.03752** | 0.01256 | [-0.06213, -0.01291] | **-2.99** | **0.003**** | ** |
| MoCA total score ~ %>180 (daily avg) | 1271 | 1049 | **-0.0369** | 0.01251 | [-0.06141, -0.01239] | **-2.95** | **0.003**** | ** |
| MoCA total score ~ %>180 nocturnal | 1271 | 446 | **-0.03131** | 0.01365 | [-0.05807, -0.004546] | **-2.29** | **0.022*** | * |
| Cognitive impairment ~ %>180 (pooled) | 1271 | 1094 | +0.007921 | 0.006872 | [-0.005547, 0.02139] | 1.15 | 0.249 |  |
| Cognitive impairment ~ %>180 (daily avg) | 1271 | 1049 | +0.00766 | 0.006845 | [-0.005756, 0.02108] | 1.12 | 0.263 |  |
| Cognitive impairment ~ %>180 nocturnal | 1271 | 446 | +0.000215 | 0.007255 | [-0.014, 0.01443] | 0.03 | 0.976 |  |
| MoCA memory index score ~ %>180 (pooled) | 1271 | 1094 | **-0.02173** | 0.007755 | [-0.03693, -0.006533] | **-2.80** | **0.005**** | ** |
| MoCA memory index score ~ %>180 (daily avg) | 1271 | 1049 | **-0.0215** | 0.007673 | [-0.03654, -0.006463] | **-2.80** | **0.005**** | ** |
| MoCA memory index score ~ %>180 nocturnal | 1271 | 446 | **-0.01903** | 0.007758 | [-0.03424, -0.003829] | **-2.45** | **0.014*** | * |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | 1270 | 1093 | +0.008409 | 0.02102 | [-0.03278, 0.0496] | 0.40 | 0.689 |  |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | 1270 | 1048 | +0.008275 | 0.02087 | [-0.03263, 0.04918] | 0.40 | 0.692 |  |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | 1270 | 445 | +0.02219 | 0.02543 | [-0.02766, 0.07204] | 0.87 | 0.383 |  |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | 1270 | 1093 | +0.01064 | 0.007319 | [-0.003702, 0.02499] | 1.45 | 0.146 |  |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | 1270 | 1048 | +0.01069 | 0.007288 | [-0.003597, 0.02497] | 1.47 | 0.143 |  |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | 1270 | 445 | **+0.01809** | 0.007493 | [0.003402, 0.03277] | **2.41** | **0.016*** | * |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | 1251 | 1077 | -0.003704 | 0.002212 | [-0.00804, 0.0006309] | -1.67 | 0.094 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | 1251 | 1033 | -0.003707 | 0.002204 | [-0.008027, 0.0006131] | -1.68 | 0.093 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | 1251 | 441 | -0.002567 | 0.002194 | [-0.006868, 0.001733] | -1.17 | 0.242 |  |
| Indoor temperature, mean ~ %>180 (pooled) | 1251 | 1077 | +0.003456 | 0.006323 | [-0.008937, 0.01585] | 0.55 | 0.585 |  |
| Indoor temperature, mean ~ %>180 (daily avg) | 1251 | 1033 | +0.003583 | 0.006275 | [-0.008715, 0.01588] | 0.57 | 0.568 |  |
| Indoor temperature, mean ~ %>180 nocturnal | 1251 | 441 | +0.005378 | 0.007048 | [-0.008437, 0.01919] | 0.76 | 0.445 |  |
| Indoor relative humidity, mean ~ %>180 (pooled) | 1251 | 1077 | +0.00216 | 0.01819 | [-0.03349, 0.03781] | 0.12 | 0.905 |  |
| Indoor relative humidity, mean ~ %>180 (daily avg) | 1251 | 1033 | +0.002596 | 0.01807 | [-0.03282, 0.03801] | 0.14 | 0.886 |  |
| Indoor relative humidity, mean ~ %>180 nocturnal | 1251 | 441 | +0.01497 | 0.01623 | [-0.01684, 0.04679] | 0.92 | 0.356 |  |
| Indoor VOC index, mean ~ %>180 (pooled) | 1251 | 1077 | -0.01889 | 0.05417 | [-0.1251, 0.08729] | -0.35 | 0.727 |  |
| Indoor VOC index, mean ~ %>180 (daily avg) | 1251 | 1033 | -0.01659 | 0.05409 | [-0.1226, 0.08942] | -0.31 | 0.759 |  |
| Indoor VOC index, mean ~ %>180 nocturnal | 1251 | 441 | -0.02239 | 0.05861 | [-0.1373, 0.09247] | -0.38 | 0.702 |  |
| Steps per wear-day ~ %>180 (pooled) | 1125 | 963 | -3.766 | 14.07 | [-31.34, 23.8] | -0.27 | 0.789 |  |
| Steps per wear-day ~ %>180 (daily avg) | 1125 | 920 | -4.715 | 14.06 | [-32.26, 22.83] | -0.34 | 0.737 |  |
| Steps per wear-day ~ %>180 nocturnal | 1125 | 392 | -3.545 | 14.96 | [-32.86, 25.77] | -0.24 | 0.813 |  |
| Brisk-cadence minutes per day ~ %>180 (pooled) | 1125 | 963 | +0.02601 | 0.04501 | [-0.06221, 0.1142] | 0.58 | 0.563 |  |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | 1125 | 920 | +0.02366 | 0.04496 | [-0.06446, 0.1118] | 0.53 | 0.599 |  |
| Brisk-cadence minutes per day ~ %>180 nocturnal | 1125 | 392 | +0.002537 | 0.04882 | [-0.09315, 0.09822] | 0.05 | 0.959 |  |
| Resting heart-rate proxy ~ %>180 (pooled) | 1128 | 964 | **+0.08387** | 0.03507 | [0.01514, 0.1526] | **2.39** | **0.017*** | * |
| Resting heart-rate proxy ~ %>180 (daily avg) | 1128 | 921 | **+0.08245** | 0.03498 | [0.01389, 0.151] | **2.36** | **0.018*** | * |
| Resting heart-rate proxy ~ %>180 nocturnal | 1128 | 392 | +0.03983 | 0.03879 | [-0.0362, 0.1159] | 1.03 | 0.305 |  |
| Total sleep time per night ~ %>180 (pooled) | 1137 | 976 | +0.1413 | 0.2584 | [-0.3651, 0.6477] | 0.55 | 0.584 |  |
| Total sleep time per night ~ %>180 (daily avg) | 1137 | 935 | +0.148 | 0.2578 | [-0.3574, 0.6534] | 0.57 | 0.566 |  |
| Total sleep time per night ~ %>180 nocturnal | 1137 | 397 | +0.1896 | 0.2587 | [-0.3174, 0.6965] | 0.73 | 0.464 |  |
| Garmin stress score, mean ~ %>180 (pooled) | 1130 | 965 | +0.0951 | 0.08306 | [-0.0677, 0.2579] | 1.14 | 0.252 |  |
| Garmin stress score, mean ~ %>180 (daily avg) | 1130 | 922 | +0.0903 | 0.08244 | [-0.07127, 0.2519] | 1.10 | 0.273 |  |
| Garmin stress score, mean ~ %>180 nocturnal | 1130 | 394 | +0.004074 | 0.09314 | [-0.1785, 0.1866] | 0.04 | 0.965 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | -0.333 [-0.552, -0.115] | 0.052 | **0.011 (FDR<0.05)** | 0.1104 | -16.8 | -3.1 | 0.0877 \| 0.0789 |
| MoCA total score ~ %>180 (daily avg) | -0.329 [-0.547, -0.110] | 0.052 | **0.011 (FDR<0.05)** | 0.1101 | -16.3 | -2.6 | 0.0874 \| 0.0789 |
| MoCA total score ~ %>180 nocturnal | -0.264 [-0.490, -0.038] | 0.158 | 0.052 | 0.1056 | -9.8 | +3.9 | 0.0833 \| 0.0789 |
| Cognitive impairment ~ %>180 (pooled) | OR 1.073 [0.952, 1.209] | 0.628 | 0.480 | 0.6602 | +0.7 | +0.5 | 0.6438 \| 0.6443 |
| Cognitive impairment ~ %>180 (daily avg) | OR 1.071 [0.950, 1.207] | 0.641 | 0.480 | 0.6601 | +0.7 | +0.5 | 0.6435 \| 0.6443 |
| Cognitive impairment ~ %>180 nocturnal | OR 1.002 [0.888, 1.130] | 0.988 | 0.976 | 0.6598 | +2.0 | +1.8 | 0.6430 \| 0.6443 |
| MoCA memory index score ~ %>180 (pooled) | -0.193 [-0.328, -0.058] | 0.068 | **0.020 (FDR<0.05)** | 0.0762 | -5.2 | -4.5 | 0.0504 \| 0.0477 |
| MoCA memory index score ~ %>180 (daily avg) | -0.192 [-0.326, -0.058] | 0.068 | **0.020 (FDR<0.05)** | 0.0761 | -5.1 | -4.4 | 0.0504 \| 0.0477 |
| MoCA memory index score ~ %>180 nocturnal | -0.161 [-0.289, -0.032] | 0.137 | **0.037 (FDR<0.05)** | 0.0746 | -3.0 | -2.3 | 0.0497 \| 0.0477 |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | +0.074 [-0.289, +0.437] | 0.932 | 0.953 | 0.0909 | +1.7 | -0.3 | 0.0626 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | +0.073 [-0.288, +0.434] | 0.932 | 0.953 | 0.0909 | +1.7 | -0.3 | 0.0628 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | +0.187 [-0.234, +0.608] | 0.788 | 0.953 | 0.0922 | -0.1 | -2.1 | 0.0622 \| 0.0675 |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | OR 1.098 [0.968, 1.246] | 0.503 | 0.565 | 0.6954 | -0.0 | -1.1 | 0.6751 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | OR 1.099 [0.969, 1.247] | 0.503 | 0.565 | 0.6954 | -0.0 | -1.2 | 0.6750 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | OR 1.165 [1.029, 1.319] | 0.137 | 0.489 | 0.7006 | -3.8 | -4.9 | 0.6816 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | -0.033 [-0.072, +0.006] | 0.412 | 0.265 | 0.1374 | +0.2 | -1.8 | 0.1138 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | -0.033 [-0.072, +0.006] | 0.410 | 0.265 | 0.1374 | +0.2 | -1.8 | 0.1138 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | -0.022 [-0.058, +0.015] | 0.621 | 0.417 | 0.1367 | +1.2 | -0.8 | 0.1133 \| 0.1139 |
| Indoor temperature, mean ~ %>180 (pooled) | +0.031 [-0.080, +0.142] | 0.932 | 0.915 | 0.3099 | +1.7 | -0.3 | 0.2886 \| 0.2892 |
| Indoor temperature, mean ~ %>180 (daily avg) | +0.032 [-0.078, +0.143] | 0.932 | 0.915 | 0.3099 | +1.6 | -0.3 | 0.2886 \| 0.2892 |
| Indoor temperature, mean ~ %>180 nocturnal | +0.046 [-0.072, +0.163] | 0.852 | 0.915 | 0.3101 | +1.3 | -0.7 | 0.2886 \| 0.2892 |
| Indoor relative humidity, mean ~ %>180 (pooled) | +0.019 [-0.299, +0.338] | 0.966 | 0.905 | 0.2596 | +2.0 | +2.5 | 0.2389 \| 0.2403 |
| Indoor relative humidity, mean ~ %>180 (daily avg) | +0.023 [-0.295, +0.341] | 0.964 | 0.905 | 0.2596 | +2.0 | +2.5 | 0.2390 \| 0.2403 |
| Indoor relative humidity, mean ~ %>180 nocturnal | +0.127 [-0.143, +0.398] | 0.758 | 0.613 | 0.2599 | +1.4 | +1.9 | 0.2398 \| 0.2403 |
| Indoor VOC index, mean ~ %>180 (pooled) | -0.169 [-1.119, +0.781] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | 0.0002 \| 0.0025 |
| Indoor VOC index, mean ~ %>180 (daily avg) | -0.149 [-1.100, +0.802] | 0.932 | 0.784 | 0.0238 | +1.9 | +1.3 | 0.0002 \| 0.0025 |
| Indoor VOC index, mean ~ %>180 nocturnal | -0.191 [-1.168, +0.787] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | -0.0002 \| 0.0025 |
| Steps per wear-day ~ %>180 (pooled) | -32.279 [-268.579, +204.021] | 0.936 | 0.958 | 0.1245 | +1.9 | +5.2 | 0.1063 \| 0.1080 |
| Steps per wear-day ~ %>180 (daily avg) | -40.529 [-277.335, +196.276] | 0.932 | 0.958 | 0.1246 | +1.9 | +5.2 | 0.1064 \| 0.1080 |
| Steps per wear-day ~ %>180 nocturnal | -28.677 [-265.799, +208.446] | 0.939 | 0.958 | 0.1245 | +1.9 | +5.2 | 0.1065 \| 0.1080 |
| Brisk-cadence minutes per day ~ %>180 (pooled) | +0.223 [-0.533, +0.979] | 0.932 | 0.931 | 0.1389 | +1.6 | +5.1 | 0.1232 \| 0.1245 |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | +0.203 [-0.554, +0.961] | 0.932 | 0.931 | 0.1389 | +1.7 | +5.1 | 0.1232 \| 0.1245 |
| Brisk-cadence minutes per day ~ %>180 nocturnal | +0.021 [-0.753, +0.794] | 0.983 | 0.994 | 0.1386 | +2.0 | +5.5 | 0.1232 \| 0.1245 |
| Resting heart-rate proxy ~ %>180 (pooled) | +0.718 [+0.130, +1.306] | 0.137 | **0.034 (FDR<0.05)** | 0.1376 | -8.5 | +2.7 | 0.1079 \| 0.1044 |
| Resting heart-rate proxy ~ %>180 (daily avg) | +0.708 [+0.119, +1.296] | 0.145 | **0.034 (FDR<0.05)** | 0.1374 | -8.2 | +3.0 | 0.1077 \| 0.1044 |
| Resting heart-rate proxy ~ %>180 nocturnal | +0.322 [-0.292, +0.936] | 0.688 | 0.378 | 0.1312 | -0.1 | +11.1 | 0.1019 \| 0.1044 |
| Total sleep time per night ~ %>180 (pooled) | +1.134 [-2.929, +5.196] | 0.932 | 0.936 | 0.0208 | +1.7 | +3.7 | -0.0069 \| -0.0051 |
| Total sleep time per night ~ %>180 (daily avg) | +1.191 [-2.876, +5.258] | 0.932 | 0.936 | 0.0208 | +1.6 | +3.6 | -0.0069 \| -0.0051 |
| Total sleep time per night ~ %>180 nocturnal | +1.419 [-2.375, +5.213] | 0.871 | 0.936 | 0.0210 | +1.5 | +3.5 | -0.0059 \| -0.0051 |
| Garmin stress score, mean ~ %>180 (pooled) | +0.813 [-0.579, +2.206] | 0.629 | 0.471 | 0.0747 | -0.7 | +7.1 | 0.0491 \| 0.0510 |
| Garmin stress score, mean ~ %>180 (daily avg) | +0.775 [-0.611, +2.161] | 0.648 | 0.471 | 0.0745 | -0.4 | +7.4 | 0.0490 \| 0.0510 |
| Garmin stress score, mean ~ %>180 nocturnal | +0.033 [-1.442, +1.507] | 0.983 | 0.965 | 0.0726 | +2.0 | +9.8 | 0.0469 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | 867 | 833 | **-0.00962** | 0.004489 | [-0.01842, -0.0008222] | **-2.14** | **0.032*** | * |
| MoCA total score ~ %>180 (daily avg) | 867 | 827 | **-0.009297** | 0.00449 | [-0.0181, -0.0004971] | **-2.07** | **0.038*** | * |
| MoCA total score ~ %>180 nocturnal | 867 | 663 | **-0.009428** | 0.004361 | [-0.01798, -0.0008794] | **-2.16** | **0.031*** | * |
| Cognitive impairment ~ %>180 (pooled) | 867 | 833 | **+0.005881** | 0.002798 | [0.0003967, 0.01137] | **2.10** | **0.036*** | * |
| Cognitive impairment ~ %>180 (daily avg) | 867 | 827 | **+0.005789** | 0.002788 | [0.0003249, 0.01125] | **2.08** | **0.038*** | * |
| Cognitive impairment ~ %>180 nocturnal | 867 | 663 | **+0.005648** | 0.002681 | [0.0003926, 0.0109] | **2.11** | **0.035*** | * |
| MoCA memory index score ~ %>180 (pooled) | 867 | 833 | -0.006238 | 0.003458 | [-0.01301, 0.0005394] | -1.80 | 0.071 |  |
| MoCA memory index score ~ %>180 (daily avg) | 867 | 827 | -0.006034 | 0.003459 | [-0.01281, 0.0007458] | -1.74 | 0.081 |  |
| MoCA memory index score ~ %>180 nocturnal | 867 | 663 | -0.006191 | 0.003338 | [-0.01273, 0.0003509] | -1.85 | 0.064 |  |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | 865 | 831 | +0.007871 | 0.007025 | [-0.005898, 0.02164] | 1.12 | 0.263 |  |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | 865 | 825 | +0.007334 | 0.007011 | [-0.006408, 0.02108] | 1.05 | 0.296 |  |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | 865 | 661 | +0.01094 | 0.006681 | [-0.002157, 0.02403] | 1.64 | 0.102 |  |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | 865 | 831 | +0.005372 | 0.003143 | [-0.0007878, 0.01153] | 1.71 | 0.087 |  |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | 865 | 825 | +0.005047 | 0.003139 | [-0.001105, 0.0112] | 1.61 | 0.108 |  |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | 865 | 661 | **+0.007248** | 0.002943 | [0.00148, 0.01302] | **2.46** | **0.014*** | * |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | 849 | 819 | +0.002467 | 0.001437 | [-0.0003502, 0.005284] | 1.72 | 0.086 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | 849 | 813 | +0.002436 | 0.001431 | [-0.0003675, 0.00524] | 1.70 | 0.089 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | 849 | 654 | +0.002681 | 0.001374 | [-1.261e-05, 0.005374] | 1.95 | 0.051 |  |
| Indoor temperature, mean ~ %>180 (pooled) | 849 | 819 | -0.002403 | 0.003087 | [-0.008452, 0.003647] | -0.78 | 0.436 |  |
| Indoor temperature, mean ~ %>180 (daily avg) | 849 | 813 | -0.002624 | 0.00308 | [-0.008661, 0.003412] | -0.85 | 0.394 |  |
| Indoor temperature, mean ~ %>180 nocturnal | 849 | 654 | -0.002405 | 0.002979 | [-0.008243, 0.003434] | -0.81 | 0.420 |  |
| Indoor relative humidity, mean ~ %>180 (pooled) | 849 | 819 | -0.005273 | 0.008869 | [-0.02265, 0.01211] | -0.59 | 0.552 |  |
| Indoor relative humidity, mean ~ %>180 (daily avg) | 849 | 813 | -0.004926 | 0.008848 | [-0.02227, 0.01242] | -0.56 | 0.578 |  |
| Indoor relative humidity, mean ~ %>180 nocturnal | 849 | 654 | -0.009368 | 0.008357 | [-0.02575, 0.007012] | -1.12 | 0.262 |  |
| Indoor VOC index, mean ~ %>180 (pooled) | 849 | 819 | -0.0186 | 0.02584 | [-0.06925, 0.03205] | -0.72 | 0.472 |  |
| Indoor VOC index, mean ~ %>180 (daily avg) | 849 | 813 | -0.02065 | 0.02586 | [-0.07134, 0.03003] | -0.80 | 0.425 |  |
| Indoor VOC index, mean ~ %>180 nocturnal | 849 | 654 | -0.0138 | 0.02773 | [-0.06815, 0.04055] | -0.50 | 0.619 |  |
| Steps per wear-day ~ %>180 (pooled) | 747 | 714 | +5.571 | 8.122 | [-10.35, 21.49] | 0.69 | 0.493 |  |
| Steps per wear-day ~ %>180 (daily avg) | 747 | 708 | +5.781 | 8.075 | [-10.05, 21.61] | 0.72 | 0.474 |  |
| Steps per wear-day ~ %>180 nocturnal | 747 | 567 | +5.974 | 7.922 | [-9.553, 21.5] | 0.75 | 0.451 |  |
| Brisk-cadence minutes per day ~ %>180 (pooled) | 747 | 714 | +0.008149 | 0.02259 | [-0.03614, 0.05243] | 0.36 | 0.718 |  |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | 747 | 708 | +0.008953 | 0.02253 | [-0.03521, 0.05312] | 0.40 | 0.691 |  |
| Brisk-cadence minutes per day ~ %>180 nocturnal | 747 | 567 | +0.01079 | 0.02222 | [-0.03277, 0.05435] | 0.49 | 0.627 |  |
| Resting heart-rate proxy ~ %>180 (pooled) | 749 | 716 | **+0.04103** | 0.01258 | [0.01636, 0.06569] | **3.26** | **0.001**** | ** |
| Resting heart-rate proxy ~ %>180 (daily avg) | 749 | 710 | **+0.04096** | 0.01249 | [0.01649, 0.06543] | **3.28** | **0.001**** | ** |
| Resting heart-rate proxy ~ %>180 nocturnal | 749 | 568 | **+0.03475** | 0.01208 | [0.01107, 0.05843] | **2.88** | **0.004**** | ** |
| Total sleep time per night ~ %>180 (pooled) | 756 | 723 | -0.1073 | 0.09973 | [-0.3028, 0.08817] | -1.08 | 0.282 |  |
| Total sleep time per night ~ %>180 (daily avg) | 756 | 717 | -0.1051 | 0.09974 | [-0.3006, 0.09036] | -1.05 | 0.292 |  |
| Total sleep time per night ~ %>180 nocturnal | 756 | 572 | -0.01934 | 0.09315 | [-0.2019, 0.1632] | -0.21 | 0.835 |  |
| Garmin stress score, mean ~ %>180 (pooled) | 749 | 716 | **+0.1005** | 0.02589 | [0.04979, 0.1513] | **3.88** | **1.0e-04***** | *** |
| Garmin stress score, mean ~ %>180 (daily avg) | 749 | 710 | **+0.09984** | 0.02575 | [0.04936, 0.1503] | **3.88** | **1.1e-04***** | *** |
| Garmin stress score, mean ~ %>180 nocturnal | 749 | 568 | **+0.08245** | 0.02465 | [0.03413, 0.1308] | **3.34** | **8.2e-04***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %>180 (pooled) | -0.249 [-0.477, -0.021] | 0.161 | 0.071 | 0.0860 | -2.9 | -1.3 | 0.0580 \| 0.0541 |
| MoCA total score ~ %>180 (daily avg) | -0.242 [-0.471, -0.013] | 0.170 | 0.074 | 0.0857 | -2.6 | -1.1 | 0.0576 \| 0.0541 |
| MoCA total score ~ %>180 nocturnal | -0.257 [-0.490, -0.024] | 0.160 | 0.071 | 0.0862 | -3.1 | -1.6 | 0.0574 \| 0.0541 |
| Cognitive impairment ~ %>180 (pooled) | OR 1.165 [1.010, 1.343] | 0.168 | 0.107 | 0.6638 | -2.5 | -0.8 | 0.6437 \| 0.6425 |
| Cognitive impairment ~ %>180 (daily avg) | OR 1.163 [1.008, 1.341] | 0.169 | 0.107 | 0.6635 | -2.4 | -0.7 | 0.6437 \| 0.6425 |
| Cognitive impairment ~ %>180 nocturnal | OR 1.166 [1.011, 1.346] | 0.168 | 0.107 | 0.6642 | -2.5 | -0.8 | 0.6446 \| 0.6425 |
| MoCA memory index score ~ %>180 (pooled) | -0.162 [-0.337, +0.014] | 0.229 | 0.122 | 0.0629 | -1.0 | +0.8 | 0.0309 \| 0.0286 |
| MoCA memory index score ~ %>180 (daily avg) | -0.157 [-0.334, +0.019] | 0.243 | 0.126 | 0.0627 | -0.8 | +1.0 | 0.0308 \| 0.0286 |
| MoCA memory index score ~ %>180 nocturnal | -0.169 [-0.347, +0.010] | 0.221 | 0.122 | 0.0631 | -1.2 | +0.6 | 0.0307 \| 0.0286 |
| CES-D-10 depressive symptoms ~ %>180 (pooled) | +0.204 [-0.153, +0.561] | 0.481 | 0.578 | 0.1126 | +0.5 | +1.8 | 0.0780 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %>180 (daily avg) | +0.191 [-0.167, +0.549] | 0.515 | 0.578 | 0.1124 | +0.7 | +2.0 | 0.0780 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %>180 nocturnal | +0.298 [-0.059, +0.656] | 0.264 | 0.578 | 0.1142 | -1.1 | +0.2 | 0.0797 \| 0.0796 |
| Clinically relevant depressive symptoms ~ %>180 (pooled) | OR 1.150 [0.980, 1.349] | 0.247 | 0.215 | 0.6653 | -0.9 | +2.1 | 0.6360 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %>180 (daily avg) | OR 1.141 [0.972, 1.339] | 0.270 | 0.215 | 0.6649 | -0.5 | +2.5 | 0.6356 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %>180 nocturnal | OR 1.219 [1.041, 1.426] | 0.100 | 0.122 | 0.6701 | -3.9 | -0.9 | 0.6405 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (pooled) | +0.064 [-0.009, +0.137] | 0.247 | 0.172 | 0.1579 | -2.0 | +7.5 | 0.1314 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 (daily avg) | +0.064 [-0.010, +0.137] | 0.247 | 0.172 | 0.1578 | -1.9 | +7.5 | 0.1314 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>180 nocturnal | +0.073 [-0.000, +0.147] | 0.198 | 0.158 | 0.1590 | -3.1 | +6.3 | 0.1321 \| 0.1310 |
| Indoor temperature, mean ~ %>180 (pooled) | -0.062 [-0.220, +0.095] | 0.651 | 0.794 | 0.2508 | +1.3 | -0.4 | 0.2230 \| 0.2264 |
| Indoor temperature, mean ~ %>180 (daily avg) | -0.068 [-0.226, +0.089] | 0.613 | 0.794 | 0.2509 | +1.1 | -0.5 | 0.2231 \| 0.2264 |
| Indoor temperature, mean ~ %>180 nocturnal | -0.066 [-0.225, +0.094] | 0.634 | 0.794 | 0.2508 | +1.2 | -0.5 | 0.2235 \| 0.2264 |
| Indoor relative humidity, mean ~ %>180 (pooled) | -0.137 [-0.589, +0.315] | 0.734 | 0.938 | 0.2133 | +1.6 | -0.3 | 0.1843 \| 0.1857 |
| Indoor relative humidity, mean ~ %>180 (daily avg) | -0.129 [-0.581, +0.324] | 0.757 | 0.938 | 0.2133 | +1.6 | -0.2 | 0.1842 \| 0.1857 |
| Indoor relative humidity, mean ~ %>180 nocturnal | -0.256 [-0.702, +0.191] | 0.481 | 0.938 | 0.2142 | +0.6 | -1.3 | 0.1853 \| 0.1857 |
| Indoor VOC index, mean ~ %>180 (pooled) | -0.483 [-1.799, +0.833] | 0.664 | 0.585 | 0.0563 | +1.4 | +1.7 | 0.0265 \| 0.0276 |
| Indoor VOC index, mean ~ %>180 (daily avg) | -0.539 [-1.862, +0.784] | 0.640 | 0.585 | 0.0565 | +1.2 | +1.5 | 0.0268 \| 0.0276 |
| Indoor VOC index, mean ~ %>180 nocturnal | -0.376 [-1.859, +1.106] | 0.790 | 0.710 | 0.0560 | +1.6 | +2.0 | 0.0253 \| 0.0276 |
| Steps per wear-day ~ %>180 (pooled) | +144.486 [-268.337, +557.310] | 0.688 | 0.727 | 0.1577 | +1.4 | +1.5 | 0.1372 \| 0.1390 |
| Steps per wear-day ~ %>180 (daily avg) | +150.615 [-261.757, +562.987] | 0.664 | 0.727 | 0.1578 | +1.3 | +1.4 | 0.1373 \| 0.1390 |
| Steps per wear-day ~ %>180 nocturnal | +162.753 [-260.264, +585.771] | 0.656 | 0.727 | 0.1579 | +1.2 | +1.3 | 0.1372 \| 0.1390 |
| Brisk-cadence minutes per day ~ %>180 (pooled) | +0.211 [-0.937, +1.360] | 0.833 | 0.821 | 0.1791 | +1.8 | +1.9 | 0.1525 \| 0.1546 |
| Brisk-cadence minutes per day ~ %>180 (daily avg) | +0.233 [-0.917, +1.384] | 0.826 | 0.821 | 0.1791 | +1.8 | +1.8 | 0.1525 \| 0.1546 |
| Brisk-cadence minutes per day ~ %>180 nocturnal | +0.294 [-0.893, +1.481] | 0.795 | 0.821 | 0.1792 | +1.7 | +1.7 | 0.1525 \| 0.1546 |
| Resting heart-rate proxy ~ %>180 (pooled) | **+1.065 [+0.425, +1.706]** | **0.024 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1655 | -9.8 | -3.7 | 0.1365 \| 0.1253 |
| Resting heart-rate proxy ~ %>180 (daily avg) | **+1.069 [+0.430, +1.707]** | **0.024 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1656 | -9.9 | -3.8 | 0.1365 \| 0.1253 |
| Resting heart-rate proxy ~ %>180 nocturnal | **+0.947 [+0.302, +1.592]** | **0.046 (FDR<0.05)** | **0.011 (FDR<0.05)** | 0.1626 | -7.2 | -1.1 | 0.1333 \| 0.1253 |
| Total sleep time per night ~ %>180 (pooled) | -2.757 [-7.779, +2.265] | 0.502 | 0.444 | 0.0378 | +0.8 | +3.7 | 0.0055 \| 0.0066 |
| Total sleep time per night ~ %>180 (daily avg) | -2.714 [-7.760, +2.333] | 0.513 | 0.444 | 0.0378 | +0.9 | +3.8 | 0.0053 \| 0.0066 |
| Total sleep time per night ~ %>180 nocturnal | -0.522 [-5.444, +4.401] | 0.891 | 0.863 | 0.0364 | +2.0 | +4.9 | 0.0041 \| 0.0066 |
| Garmin stress score, mean ~ %>180 (pooled) | **+2.610 [+1.293, +3.927]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1407 | -14.3 | -1.2 | 0.1121 \| 0.0947 |
| Garmin stress score, mean ~ %>180 (daily avg) | **+2.604 [+1.288, +3.921]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1406 | -14.2 | -1.1 | 0.1120 \| 0.0947 |
| Garmin stress score, mean ~ %>180 nocturnal | **+2.246 [+0.930, +3.562]** | **0.022 (FDR<0.05)** | **0.002 (FDR<0.05)** | 0.1356 | -9.9 | +3.2 | 0.1066 \| 0.0947 |


---

## Band 181-250

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | 2138 | 1927 | **-0.02505** | 0.005756 | [-0.03633, -0.01376] | **-4.35** | **1.4e-05***** | *** |
| MoCA total score ~ %181-250 (daily avg) | 2138 | 1876 | **-0.0243** | 0.005691 | [-0.03546, -0.01315] | **-4.27** | **2.0e-05***** | *** |
| Cognitive impairment ~ %181-250 (pooled) | 2138 | 1927 | **+0.01326** | 0.003672 | [0.006059, 0.02045] | **3.61** | **3.1e-04***** | *** |
| Cognitive impairment ~ %181-250 (daily avg) | 2138 | 1876 | **+0.0131** | 0.003625 | [0.005992, 0.0202] | **3.61** | **3.0e-04***** | *** |
| MoCA memory index score ~ %181-250 (pooled) | 2138 | 1927 | **-0.01191** | 0.004576 | [-0.02088, -0.002941] | **-2.60** | **0.009**** | ** |
| MoCA memory index score ~ %181-250 (daily avg) | 2138 | 1876 | **-0.01174** | 0.004535 | [-0.02063, -0.002852] | **-2.59** | **0.010**** | ** |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | 2135 | 1924 | +0.006888 | 0.008824 | [-0.01041, 0.02418] | 0.78 | 0.435 |  |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | 2135 | 1873 | +0.00696 | 0.00871 | [-0.01011, 0.02403] | 0.80 | 0.424 |  |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | 2135 | 1924 | +0.008072 | 0.004329 | [-0.000412, 0.01656] | 1.86 | 0.062 |  |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | 2135 | 1873 | +0.008147 | 0.004265 | [-0.000212, 0.01651] | 1.91 | 0.056 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | 2100 | 1896 | +0.002026 | 0.00166 | [-0.001227, 0.005279] | 1.22 | 0.222 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | 2100 | 1846 | +0.001962 | 0.001635 | [-0.001243, 0.005166] | 1.20 | 0.230 |  |
| Indoor temperature, mean ~ %181-250 (pooled) | 2100 | 1896 | +0.001007 | 0.003581 | [-0.006012, 0.008027] | 0.28 | 0.779 |  |
| Indoor temperature, mean ~ %181-250 (daily avg) | 2100 | 1846 | +0.0007616 | 0.003545 | [-0.006187, 0.00771] | 0.21 | 0.830 |  |
| Indoor relative humidity, mean ~ %181-250 (pooled) | 2100 | 1896 | -0.006603 | 0.01084 | [-0.02784, 0.01464] | -0.61 | 0.542 |  |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | 2100 | 1846 | -0.005971 | 0.01067 | [-0.02689, 0.01495] | -0.56 | 0.576 |  |
| Indoor VOC index, mean ~ %181-250 (pooled) | 2100 | 1896 | +0.02527 | 0.03778 | [-0.04878, 0.09932] | 0.67 | 0.504 |  |
| Indoor VOC index, mean ~ %181-250 (daily avg) | 2100 | 1846 | +0.02353 | 0.03693 | [-0.04885, 0.09591] | 0.64 | 0.524 |  |
| Steps per wear-day ~ %181-250 (pooled) | 1872 | 1677 | +16.89 | 9.52 | [-1.77, 35.55] | 1.77 | 0.076 |  |
| Steps per wear-day ~ %181-250 (daily avg) | 1872 | 1628 | +16.22 | 9.429 | [-2.262, 34.7] | 1.72 | 0.085 |  |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | 1872 | 1677 | +0.04757 | 0.02741 | [-0.00616, 0.1013] | 1.74 | 0.083 |  |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | 1872 | 1628 | +0.04616 | 0.0272 | [-0.007138, 0.09947] | 1.70 | 0.090 |  |
| Resting heart-rate proxy ~ %181-250 (pooled) | 1877 | 1680 | **+0.1368** | 0.01659 | [0.1043, 0.1693] | **8.25** | **1.6e-16***** | *** |
| Resting heart-rate proxy ~ %181-250 (daily avg) | 1877 | 1631 | **+0.1338** | 0.01641 | [0.1017, 0.166] | **8.15** | **3.5e-16***** | *** |
| Total sleep time per night ~ %181-250 (pooled) | 1893 | 1699 | -0.1758 | 0.1328 | [-0.4362, 0.08457] | -1.32 | 0.186 |  |
| Total sleep time per night ~ %181-250 (daily avg) | 1893 | 1652 | -0.1711 | 0.1311 | [-0.4281, 0.08591] | -1.30 | 0.192 |  |
| Garmin stress score, mean ~ %181-250 (pooled) | 1879 | 1681 | **+0.2369** | 0.03395 | [0.1704, 0.3035] | **6.98** | **3.0e-12***** | *** |
| Garmin stress score, mean ~ %181-250 (daily avg) | 1879 | 1632 | **+0.2305** | 0.03351 | [0.1648, 0.2962] | **6.88** | **6.0e-12***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | **-0.321 [-0.466, -0.177]** | **1.1e-04 (FDR<0.05)** | **3.5e-05 (FDR<0.05)** | 0.1095 | -21.2 | +3.4 | 0.1000 \| 0.0915 |
| MoCA total score ~ %181-250 (daily avg) | **-0.316 [-0.461, -0.171]** | **1.4e-04 (FDR<0.05)** | **4.3e-05 (FDR<0.05)** | 0.1092 | -20.4 | +4.2 | 0.0997 \| 0.0915 |
| Cognitive impairment ~ %181-250 (pooled) | **OR 1.185 [1.081, 1.300]** | **0.002 (FDR<0.05)** | **7.3e-04 (FDR<0.05)** | 0.6739 | -11.1 | +2.5 | 0.6654 \| 0.6603 |
| Cognitive impairment ~ %181-250 (daily avg) | **OR 1.186 [1.081, 1.300]** | **0.002 (FDR<0.05)** | **7.3e-04 (FDR<0.05)** | 0.6739 | -11.1 | +2.5 | 0.6655 \| 0.6603 |
| MoCA memory index score ~ %181-250 (pooled) | **-0.153 [-0.268, -0.038]** | **0.033 (FDR<0.05)** | **0.021 (FDR<0.05)** | 0.0744 | -4.7 | +0.6 | 0.0651 \| 0.0630 |
| MoCA memory index score ~ %181-250 (daily avg) | **-0.153 [-0.268, -0.037]** | **0.035 (FDR<0.05)** | **0.021 (FDR<0.05)** | 0.0744 | -4.7 | +0.6 | 0.0650 \| 0.0630 |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | +0.088 [-0.133, +0.310] | 0.607 | 0.620 | 0.1030 | +1.3 | +1.6 | 0.0914 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | +0.090 [-0.131, +0.312] | 0.596 | 0.620 | 0.1030 | +1.3 | +1.5 | 0.0914 \| 0.0916 |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | OR 1.109 [0.995, 1.237] | 0.158 | 0.161 | 0.6816 | -1.4 | +1.3 | 0.6682 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | OR 1.112 [0.997, 1.239] | 0.147 | 0.158 | 0.6817 | -1.6 | +1.1 | 0.6684 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | +0.026 [-0.016, +0.068] | 0.393 | 0.274 | 0.1515 | +0.3 | +11.2 | 0.1384 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | +0.026 [-0.016, +0.067] | 0.400 | 0.274 | 0.1514 | +0.4 | +11.3 | 0.1383 \| 0.1387 |
| Indoor temperature, mean ~ %181-250 (pooled) | +0.013 [-0.077, +0.103] | 0.864 | 0.982 | 0.2979 | +1.9 | +0.4 | 0.2889 \| 0.2896 |
| Indoor temperature, mean ~ %181-250 (daily avg) | +0.010 [-0.081, +0.101] | 0.892 | 0.982 | 0.2979 | +2.0 | +0.4 | 0.2889 \| 0.2896 |
| Indoor relative humidity, mean ~ %181-250 (pooled) | -0.085 [-0.358, +0.188] | 0.701 | 0.898 | 0.2412 | +1.6 | -0.2 | 0.2303 \| 0.2307 |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | -0.078 [-0.351, +0.195] | 0.732 | 0.898 | 0.2411 | +1.7 | -0.2 | 0.2303 \| 0.2307 |
| Indoor VOC index, mean ~ %181-250 (pooled) | +0.325 [-0.628, +1.278] | 0.675 | 0.868 | 0.0430 | +1.2 | +1.2 | 0.0257 \| 0.0271 |
| Indoor VOC index, mean ~ %181-250 (daily avg) | +0.307 [-0.637, +1.250] | 0.693 | 0.868 | 0.0429 | +1.3 | +1.3 | 0.0258 \| 0.0271 |
| Steps per wear-day ~ %181-250 (pooled) | +215.490 [-22.588, +453.567] | 0.184 | 0.198 | 0.1369 | -2.5 | +5.5 | 0.1234 \| 0.1222 |
| Steps per wear-day ~ %181-250 (daily avg) | +209.917 [-29.277, +449.111] | 0.195 | 0.202 | 0.1368 | -2.3 | +5.7 | 0.1233 \| 0.1222 |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | +0.607 [-0.079, +1.292] | 0.193 | 0.192 | 0.1574 | -2.0 | +6.2 | 0.1457 \| 0.1447 |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | +0.597 [-0.092, +1.287] | 0.202 | 0.192 | 0.1574 | -1.8 | +6.3 | 0.1457 \| 0.1447 |
| Resting heart-rate proxy ~ %181-250 (pooled) | **+1.747 [+1.331, +2.162]** | **7.1e-14 (FDR<0.05)** | **5.1e-15 (FDR<0.05)** | 0.1957 | -80.2 | -9.0 | 0.1829 \| 0.1482 |
| Resting heart-rate proxy ~ %181-250 (daily avg) | **+1.733 [+1.316, +2.149]** | **7.6e-14 (FDR<0.05)** | **5.4e-15 (FDR<0.05)** | 0.1951 | -78.8 | -7.6 | 0.1824 \| 0.1482 |
| Total sleep time per night ~ %181-250 (pooled) | -2.241 [-5.559, +1.078] | 0.346 | 0.397 | 0.0343 | +0.0 | +8.9 | 0.0196 \| 0.0209 |
| Total sleep time per night ~ %181-250 (daily avg) | -2.210 [-5.530, +1.110] | 0.353 | 0.397 | 0.0342 | +0.1 | +9.0 | 0.0196 \| 0.0209 |
| Garmin stress score, mean ~ %181-250 (pooled) | **+3.023 [+2.174, +3.872]** | **8.6e-11 (FDR<0.05)** | **4.6e-11 (FDR<0.05)** | 0.1302 | -51.6 | +8.8 | 0.1150 \| 0.0902 |
| Garmin stress score, mean ~ %181-250 (daily avg) | **+2.982 [+2.133, +3.832]** | **1.6e-10 (FDR<0.05)** | **5.6e-11 (FDR<0.05)** | 0.1295 | -50.1 | +10.3 | 0.1142 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | 1271 | 1094 | **-0.0435** | 0.01422 | [-0.07138, -0.01563] | **-3.06** | **0.002**** | ** |
| MoCA total score ~ %181-250 (daily avg) | 1271 | 1049 | **-0.04242** | 0.01402 | [-0.0699, -0.01494] | **-3.03** | **0.002**** | ** |
| Cognitive impairment ~ %181-250 (pooled) | 1271 | 1094 | +0.01357 | 0.009908 | [-0.005848, 0.03299] | 1.37 | 0.171 |  |
| Cognitive impairment ~ %181-250 (daily avg) | 1271 | 1049 | +0.0133 | 0.009775 | [-0.005857, 0.03246] | 1.36 | 0.174 |  |
| MoCA memory index score ~ %181-250 (pooled) | 1271 | 1094 | -0.02266 | 0.01242 | [-0.047, 0.001685] | -1.82 | 0.068 |  |
| MoCA memory index score ~ %181-250 (daily avg) | 1271 | 1049 | -0.02239 | 0.01206 | [-0.04602, 0.001239] | -1.86 | 0.063 |  |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | 1270 | 1093 | +0.03522 | 0.03034 | [-0.02425, 0.09469] | 1.16 | 0.246 |  |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | 1270 | 1048 | +0.03394 | 0.03012 | [-0.0251, 0.09298] | 1.13 | 0.260 |  |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | 1270 | 1093 | **+0.02234** | 0.01138 | [2.846e-05, 0.04465] | **1.96** | **0.050*** | * |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | 1270 | 1048 | +0.02181 | 0.01122 | [-0.0001829, 0.04381] | 1.94 | 0.052 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | 1251 | 1077 | -0.005637 | 0.004181 | [-0.01383, 0.002558] | -1.35 | 0.178 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | 1251 | 1033 | -0.005634 | 0.004153 | [-0.01377, 0.002505] | -1.36 | 0.175 |  |
| Indoor temperature, mean ~ %181-250 (pooled) | 1251 | 1077 | +0.004431 | 0.008831 | [-0.01288, 0.02174] | 0.50 | 0.616 |  |
| Indoor temperature, mean ~ %181-250 (daily avg) | 1251 | 1033 | +0.004823 | 0.00876 | [-0.01235, 0.02199] | 0.55 | 0.582 |  |
| Indoor relative humidity, mean ~ %181-250 (pooled) | 1251 | 1077 | -0.01806 | 0.02782 | [-0.07259, 0.03647] | -0.65 | 0.516 |  |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | 1251 | 1033 | -0.01685 | 0.02737 | [-0.07049, 0.0368] | -0.62 | 0.538 |  |
| Indoor VOC index, mean ~ %181-250 (pooled) | 1251 | 1077 | +0.03195 | 0.09078 | [-0.146, 0.2099] | 0.35 | 0.725 |  |
| Indoor VOC index, mean ~ %181-250 (daily avg) | 1251 | 1033 | +0.03436 | 0.08928 | [-0.1406, 0.2094] | 0.38 | 0.700 |  |
| Steps per wear-day ~ %181-250 (pooled) | 1125 | 963 | -18.78 | 17.2 | [-52.48, 14.92] | -1.09 | 0.275 |  |
| Steps per wear-day ~ %181-250 (daily avg) | 1125 | 920 | -19.86 | 16.88 | [-52.94, 13.23] | -1.18 | 0.239 |  |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | 1125 | 963 | +0.000432 | 0.05763 | [-0.1125, 0.1134] | 0.01 | 0.994 |  |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | 1125 | 920 | -0.002001 | 0.05701 | [-0.1137, 0.1097] | -0.04 | 0.972 |  |
| Resting heart-rate proxy ~ %181-250 (pooled) | 1128 | 964 | **+0.1104** | 0.04493 | [0.02234, 0.1985] | **2.46** | **0.014*** | * |
| Resting heart-rate proxy ~ %181-250 (daily avg) | 1128 | 921 | **+0.1079** | 0.04488 | [0.01991, 0.1958] | **2.40** | **0.016*** | * |
| Total sleep time per night ~ %181-250 (pooled) | 1137 | 976 | +0.2915 | 0.373 | [-0.4396, 1.023] | 0.78 | 0.435 |  |
| Total sleep time per night ~ %181-250 (daily avg) | 1137 | 935 | +0.2971 | 0.3686 | [-0.4253, 1.02] | 0.81 | 0.420 |  |
| Garmin stress score, mean ~ %181-250 (pooled) | 1130 | 965 | +0.1195 | 0.09744 | [-0.07145, 0.3105] | 1.23 | 0.220 |  |
| Garmin stress score, mean ~ %181-250 (daily avg) | 1130 | 922 | +0.1116 | 0.09574 | [-0.07607, 0.2992] | 1.17 | 0.244 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | -0.265 [-0.435, -0.095] | 0.051 | **0.011 (FDR<0.05)** | 0.1055 | -9.8 | +3.9 | 0.0856 \| 0.0789 |
| MoCA total score ~ %181-250 (daily avg) | -0.262 [-0.431, -0.092] | 0.052 | **0.011 (FDR<0.05)** | 0.1053 | -9.4 | +4.3 | 0.0853 \| 0.0789 |
| Cognitive impairment ~ %181-250 (pooled) | OR 1.086 [0.965, 1.223] | 0.532 | 0.480 | 0.6611 | +0.2 | -0.1 | 0.6445 \| 0.6443 |
| Cognitive impairment ~ %181-250 (daily avg) | OR 1.086 [0.965, 1.222] | 0.532 | 0.480 | 0.6610 | +0.2 | -0.0 | 0.6443 \| 0.6443 |
| MoCA memory index score ~ %181-250 (pooled) | -0.138 [-0.287, +0.010] | 0.352 | 0.127 | 0.0736 | -1.6 | -1.0 | 0.0479 \| 0.0477 |
| MoCA memory index score ~ %181-250 (daily avg) | -0.138 [-0.284, +0.008] | 0.340 | 0.127 | 0.0736 | -1.6 | -1.0 | 0.0480 \| 0.0477 |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | +0.213 [-0.146, +0.571] | 0.624 | 0.953 | 0.0926 | -0.7 | -2.6 | 0.0650 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | +0.207 [-0.153, +0.568] | 0.638 | 0.953 | 0.0925 | -0.5 | -2.5 | 0.0649 \| 0.0675 |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | OR 1.144 [1.000, 1.309] | 0.296 | 0.537 | 0.6978 | -1.7 | -2.8 | 0.6769 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | OR 1.143 [0.999, 1.307] | 0.305 | 0.537 | 0.6976 | -1.6 | -2.8 | 0.6767 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | -0.035 [-0.085, +0.016] | 0.532 | 0.367 | 0.1375 | +0.0 | -2.0 | 0.1133 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | -0.035 [-0.086, +0.016] | 0.532 | 0.367 | 0.1375 | -0.0 | -2.0 | 0.1132 \| 0.1139 |
| Indoor temperature, mean ~ %181-250 (pooled) | +0.027 [-0.079, +0.133] | 0.932 | 0.915 | 0.3099 | +1.7 | -0.2 | 0.2882 \| 0.2892 |
| Indoor temperature, mean ~ %181-250 (daily avg) | +0.030 [-0.077, +0.137] | 0.932 | 0.915 | 0.3099 | +1.7 | -0.3 | 0.2883 \| 0.2892 |
| Indoor relative humidity, mean ~ %181-250 (pooled) | -0.111 [-0.445, +0.224] | 0.918 | 0.758 | 0.2598 | +1.6 | +2.1 | 0.2390 \| 0.2403 |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | -0.105 [-0.438, +0.229] | 0.931 | 0.758 | 0.2598 | +1.6 | +2.1 | 0.2391 \| 0.2403 |
| Indoor VOC index, mean ~ %181-250 (pooled) | +0.196 [-0.896, +1.288] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.2 | -0.0012 \| 0.0025 |
| Indoor VOC index, mean ~ %181-250 (daily avg) | +0.213 [-0.873, +1.300] | 0.932 | 0.784 | 0.0239 | +1.8 | +1.1 | -0.0009 \| 0.0025 |
| Steps per wear-day ~ %181-250 (pooled) | -112.794 [-315.192, +89.605] | 0.648 | 0.958 | 0.1253 | +1.0 | +4.3 | 0.1069 \| 0.1080 |
| Steps per wear-day ~ %181-250 (daily avg) | -120.736 [-321.893, +80.422] | 0.619 | 0.958 | 0.1254 | +0.9 | +4.2 | 0.1071 \| 0.1080 |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | +0.003 [-0.676, +0.681] | 0.994 | 0.994 | 0.1386 | +2.0 | +5.5 | 0.1224 \| 0.1245 |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | -0.012 [-0.692, +0.667] | 0.986 | 0.994 | 0.1386 | +2.0 | +5.5 | 0.1225 \| 0.1245 |
| Resting heart-rate proxy ~ %181-250 (pooled) | +0.662 [+0.134, +1.191] | 0.137 | **0.034 (FDR<0.05)** | 0.1363 | -6.8 | +4.4 | 0.1070 \| 0.1044 |
| Resting heart-rate proxy ~ %181-250 (daily avg) | +0.655 [+0.121, +1.189] | 0.137 | **0.034 (FDR<0.05)** | 0.1361 | -6.6 | +4.6 | 0.1067 \| 0.1044 |
| Total sleep time per night ~ %181-250 (pooled) | +1.721 [-2.595, +6.036] | 0.846 | 0.936 | 0.0212 | +1.2 | +3.2 | -0.0073 \| -0.0051 |
| Total sleep time per night ~ %181-250 (daily avg) | +1.775 [-2.541, +6.090] | 0.822 | 0.936 | 0.0212 | +1.2 | +3.2 | -0.0072 \| -0.0051 |
| Garmin stress score, mean ~ %181-250 (pooled) | +0.717 [-0.428, +1.861] | 0.594 | 0.471 | 0.0742 | -0.0 | +7.7 | 0.0502 \| 0.0510 |
| Garmin stress score, mean ~ %181-250 (daily avg) | +0.677 [-0.462, +1.816] | 0.623 | 0.471 | 0.0740 | +0.2 | +8.0 | 0.0501 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | 867 | 833 | -0.01302 | 0.007598 | [-0.02791, 0.001873] | -1.71 | 0.087 |  |
| MoCA total score ~ %181-250 (daily avg) | 867 | 827 | -0.01235 | 0.007488 | [-0.02702, 0.00233] | -1.65 | 0.099 |  |
| Cognitive impairment ~ %181-250 (pooled) | 867 | 833 | +0.007197 | 0.004624 | [-0.001865, 0.01626] | 1.56 | 0.120 |  |
| Cognitive impairment ~ %181-250 (daily avg) | 867 | 827 | +0.007182 | 0.004551 | [-0.001737, 0.0161] | 1.58 | 0.114 |  |
| MoCA memory index score ~ %181-250 (pooled) | 867 | 833 | -0.009359 | 0.005874 | [-0.02087, 0.002154] | -1.59 | 0.111 |  |
| MoCA memory index score ~ %181-250 (daily avg) | 867 | 827 | -0.009243 | 0.005823 | [-0.02066, 0.002169] | -1.59 | 0.112 |  |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | 865 | 831 | +0.002482 | 0.01083 | [-0.01874, 0.02371] | 0.23 | 0.819 |  |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | 865 | 825 | +0.002942 | 0.01063 | [-0.0179, 0.02378] | 0.28 | 0.782 |  |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | 865 | 831 | +0.006472 | 0.005443 | [-0.004196, 0.01714] | 1.19 | 0.234 |  |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | 865 | 825 | +0.00679 | 0.005346 | [-0.003689, 0.01727] | 1.27 | 0.204 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | 849 | 819 | +0.002653 | 0.002137 | [-0.001535, 0.006842] | 1.24 | 0.214 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | 849 | 813 | +0.002563 | 0.002093 | [-0.001539, 0.006665] | 1.22 | 0.221 |  |
| Indoor temperature, mean ~ %181-250 (pooled) | 849 | 819 | -0.00493 | 0.004835 | [-0.01441, 0.004547] | -1.02 | 0.308 |  |
| Indoor temperature, mean ~ %181-250 (daily avg) | 849 | 813 | -0.005294 | 0.004772 | [-0.01465, 0.004059] | -1.11 | 0.267 |  |
| Indoor relative humidity, mean ~ %181-250 (pooled) | 849 | 819 | -0.009155 | 0.01442 | [-0.03742, 0.01911] | -0.63 | 0.526 |  |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | 849 | 813 | -0.008203 | 0.01414 | [-0.03592, 0.01951] | -0.58 | 0.562 |  |
| Indoor VOC index, mean ~ %181-250 (pooled) | 849 | 819 | +0.01983 | 0.04665 | [-0.0716, 0.1113] | 0.43 | 0.671 |  |
| Indoor VOC index, mean ~ %181-250 (daily avg) | 849 | 813 | +0.01622 | 0.04521 | [-0.07238, 0.1048] | 0.36 | 0.720 |  |
| Steps per wear-day ~ %181-250 (pooled) | 747 | 714 | +20.49 | 12.19 | [-3.398, 44.38] | 1.68 | 0.093 |  |
| Steps per wear-day ~ %181-250 (daily avg) | 747 | 708 | +19.71 | 12.04 | [-3.882, 43.3] | 1.64 | 0.102 |  |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | 747 | 714 | +0.04027 | 0.03467 | [-0.02768, 0.1082] | 1.16 | 0.245 |  |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | 747 | 708 | +0.0389 | 0.03428 | [-0.02829, 0.1061] | 1.13 | 0.256 |  |
| Resting heart-rate proxy ~ %181-250 (pooled) | 749 | 716 | **+0.06953** | 0.02008 | [0.03018, 0.1089] | **3.46** | **5.3e-04***** | *** |
| Resting heart-rate proxy ~ %181-250 (daily avg) | 749 | 710 | **+0.06734** | 0.01964 | [0.02885, 0.1058] | **3.43** | **6.1e-04***** | *** |
| Total sleep time per night ~ %181-250 (pooled) | 756 | 723 | -0.2508 | 0.1724 | [-0.5887, 0.08713] | -1.45 | 0.146 |  |
| Total sleep time per night ~ %181-250 (daily avg) | 756 | 717 | -0.245 | 0.1694 | [-0.5771, 0.08711] | -1.45 | 0.148 |  |
| Garmin stress score, mean ~ %181-250 (pooled) | 749 | 716 | **+0.1619** | 0.04146 | [0.08066, 0.2432] | **3.91** | **9.4e-05***** | *** |
| Garmin stress score, mean ~ %181-250 (daily avg) | 749 | 710 | **+0.1562** | 0.04071 | [0.07645, 0.236] | **3.84** | **1.2e-04***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ %181-250 (pooled) | -0.203 [-0.436, +0.029] | 0.247 | 0.117 | 0.0843 | -1.2 | +0.3 | 0.0552 \| 0.0541 |
| MoCA total score ~ %181-250 (daily avg) | -0.196 [-0.429, +0.037] | 0.264 | 0.128 | 0.0840 | -1.0 | +0.5 | 0.0551 \| 0.0541 |
| Cognitive impairment ~ %181-250 (pooled) | OR 1.119 [0.971, 1.289] | 0.284 | 0.176 | 0.6622 | -0.4 | +1.3 | 0.6425 \| 0.6425 |
| Cognitive impairment ~ %181-250 (daily avg) | OR 1.121 [0.973, 1.291] | 0.275 | 0.176 | 0.6623 | -0.5 | +1.2 | 0.6422 \| 0.6425 |
| MoCA memory index score ~ %181-250 (pooled) | -0.146 [-0.326, +0.034] | 0.270 | 0.158 | 0.0623 | -0.4 | +1.3 | 0.0294 \| 0.0286 |
| MoCA memory index score ~ %181-250 (daily avg) | -0.147 [-0.328, +0.034] | 0.271 | 0.158 | 0.0623 | -0.4 | +1.3 | 0.0295 \| 0.0286 |
| CES-D-10 depressive symptoms ~ %181-250 (pooled) | +0.039 [-0.293, +0.371] | 0.886 | 0.875 | 0.1111 | +1.9 | +3.2 | 0.0774 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %181-250 (daily avg) | +0.047 [-0.284, +0.378] | 0.868 | 0.875 | 0.1111 | +1.9 | +3.2 | 0.0774 \| 0.0796 |
| Clinically relevant depressive symptoms ~ %181-250 (pooled) | OR 1.107 [0.936, 1.307] | 0.450 | 0.346 | 0.6631 | +0.6 | +3.6 | 0.6314 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %181-250 (daily avg) | OR 1.114 [0.943, 1.316] | 0.406 | 0.333 | 0.6634 | +0.4 | +3.4 | 0.6319 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (pooled) | +0.042 [-0.024, +0.107] | 0.421 | 0.236 | 0.1556 | +0.3 | +9.7 | 0.1296 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %181-250 (daily avg) | +0.041 [-0.025, +0.106] | 0.432 | 0.236 | 0.1555 | +0.4 | +9.8 | 0.1296 \| 0.1310 |
| Indoor temperature, mean ~ %181-250 (pooled) | -0.077 [-0.226, +0.071] | 0.533 | 0.794 | 0.2511 | +0.9 | -0.8 | 0.2241 \| 0.2264 |
| Indoor temperature, mean ~ %181-250 (daily avg) | -0.084 [-0.233, +0.065] | 0.483 | 0.794 | 0.2513 | +0.7 | -1.0 | 0.2243 \| 0.2264 |
| Indoor relative humidity, mean ~ %181-250 (pooled) | -0.144 [-0.587, +0.300] | 0.715 | 0.938 | 0.2133 | +1.6 | -0.3 | 0.1840 \| 0.1857 |
| Indoor relative humidity, mean ~ %181-250 (daily avg) | -0.131 [-0.572, +0.311] | 0.743 | 0.938 | 0.2133 | +1.6 | -0.2 | 0.1839 \| 0.1857 |
| Indoor VOC index, mean ~ %181-250 (pooled) | +0.311 [-1.122, +1.744] | 0.813 | 0.743 | 0.0559 | +1.7 | +2.1 | 0.0244 \| 0.0276 |
| Indoor VOC index, mean ~ %181-250 (daily avg) | +0.258 [-1.153, +1.670] | 0.833 | 0.769 | 0.0558 | +1.8 | +2.2 | 0.0246 \| 0.0276 |
| Steps per wear-day ~ %181-250 (pooled) | +321.951 [-53.387, +697.290] | 0.256 | 0.315 | 0.1606 | -1.2 | -1.1 | 0.1404 \| 0.1390 |
| Steps per wear-day ~ %181-250 (daily avg) | +315.059 [-62.054, +692.172] | 0.264 | 0.315 | 0.1605 | -1.1 | -1.0 | 0.1401 \| 0.1390 |
| Brisk-cadence minutes per day ~ %181-250 (pooled) | +0.633 [-0.435, +1.701] | 0.461 | 0.663 | 0.1805 | +0.5 | +0.5 | 0.1543 \| 0.1546 |
| Brisk-cadence minutes per day ~ %181-250 (daily avg) | +0.622 [-0.452, +1.696] | 0.480 | 0.663 | 0.1805 | +0.5 | +0.6 | 0.1541 \| 0.1546 |
| Resting heart-rate proxy ~ %181-250 (pooled) | **+1.093 [+0.475, +1.712]** | **0.019 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1662 | -10.4 | -4.4 | 0.1366 \| 0.1253 |
| Resting heart-rate proxy ~ %181-250 (daily avg) | **+1.077 [+0.461, +1.692]** | **0.020 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.1658 | -10.1 | -4.0 | 0.1362 \| 0.1253 |
| Total sleep time per night ~ %181-250 (pooled) | -3.935 [-9.237, +1.367] | 0.329 | 0.328 | 0.0394 | -0.4 | +2.5 | 0.0067 \| 0.0066 |
| Total sleep time per night ~ %181-250 (daily avg) | -3.908 [-9.205, +1.389] | 0.332 | 0.328 | 0.0393 | -0.4 | +2.5 | 0.0065 \| 0.0066 |
| Garmin stress score, mean ~ %181-250 (pooled) | **+2.545 [+1.268, +3.822]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1397 | -13.4 | -0.4 | 0.1103 \| 0.0947 |
| Garmin stress score, mean ~ %181-250 (daily avg) | **+2.497 [+1.222, +3.773]** | **0.007 (FDR<0.05)** | **5.6e-04 (FDR<0.05)** | 0.1391 | -12.9 | +0.2 | 0.1096 \| 0.0947 |


---

## Band >250

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | 2138 | 795 | **-0.6184** | 0.1433 | [-0.8993, -0.3375] | **-4.32** | **1.6e-05***** | *** |
| MoCA total score ~ %>250 (pooled) | 2138 | 795 | **-0.02449** | 0.007291 | [-0.03878, -0.0102] | **-3.36** | **7.8e-04***** | *** |
| MoCA total score ~ %>250 (daily avg) | 2138 | 735 | **-0.02439** | 0.00751 | [-0.03911, -0.009669] | **-3.25** | **0.001**** | ** |
| Cognitive impairment ~ Any >250 (0/1) | 2138 | 795 | **+0.2899** | 0.09696 | [0.09989, 0.4799] | **2.99** | **0.003**** | ** |
| Cognitive impairment ~ %>250 (pooled) | 2138 | 795 | **+0.01273** | 0.004411 | [0.004079, 0.02137] | **2.88** | **0.004**** | ** |
| Cognitive impairment ~ %>250 (daily avg) | 2138 | 735 | **+0.0125** | 0.004467 | [0.003741, 0.02125] | **2.80** | **0.005**** | ** |
| MoCA memory index score ~ Any >250 (0/1) | 2138 | 795 | **-0.2804** | 0.1247 | [-0.5249, -0.03588] | **-2.25** | **0.025*** | * |
| MoCA memory index score ~ %>250 (pooled) | 2138 | 795 | **-0.01139** | 0.005082 | [-0.02135, -0.001429] | **-2.24** | **0.025*** | * |
| MoCA memory index score ~ %>250 (daily avg) | 2138 | 735 | **-0.01103** | 0.005127 | [-0.02108, -0.0009824] | **-2.15** | **0.031*** | * |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | 2135 | 793 | +0.07286 | 0.2174 | [-0.3533, 0.499] | 0.34 | 0.738 |  |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | 2135 | 793 | +0.01325 | 0.01202 | [-0.01031, 0.03682] | 1.10 | 0.270 |  |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | 2135 | 733 | +0.01204 | 0.01226 | [-0.01199, 0.03607] | 0.98 | 0.326 |  |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | 2135 | 793 | +0.1474 | 0.1212 | [-0.09018, 0.3849] | 1.22 | 0.224 |  |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | 2135 | 793 | +0.006694 | 0.004432 | [-0.001993, 0.01538] | 1.51 | 0.131 |  |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | 2135 | 733 | +0.00596 | 0.004524 | [-0.002908, 0.01483] | 1.32 | 0.188 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | 2100 | 783 | +0.01343 | 0.04189 | [-0.06866, 0.09553] | 0.32 | 0.748 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | 2100 | 783 | +0.00374 | 0.00235 | [-0.0008649, 0.008345] | 1.59 | 0.111 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | 2100 | 724 | +0.003786 | 0.002375 | [-0.0008684, 0.00844] | 1.59 | 0.111 |  |
| Indoor temperature, mean ~ Any >250 (0/1) | 2100 | 783 | -0.06036 | 0.09235 | [-0.2414, 0.1206] | -0.65 | 0.513 |  |
| Indoor temperature, mean ~ %>250 (pooled) | 2100 | 783 | +0.001855 | 0.004518 | [-0.007001, 0.01071] | 0.41 | 0.681 |  |
| Indoor temperature, mean ~ %>250 (daily avg) | 2100 | 724 | +0.001652 | 0.0046 | [-0.007364, 0.01067] | 0.36 | 0.720 |  |
| Indoor relative humidity, mean ~ Any >250 (0/1) | 2100 | 783 | -0.4405 | 0.2793 | [-0.988, 0.107] | -1.58 | 0.115 |  |
| Indoor relative humidity, mean ~ %>250 (pooled) | 2100 | 783 | +0.0006516 | 0.01254 | [-0.02394, 0.02524] | 0.05 | 0.959 |  |
| Indoor relative humidity, mean ~ %>250 (daily avg) | 2100 | 724 | +0.0008592 | 0.0129 | [-0.02443, 0.02614] | 0.07 | 0.947 |  |
| Indoor VOC index, mean ~ Any >250 (0/1) | 2100 | 783 | +1.064 | 0.7661 | [-0.437, 2.566] | 1.39 | 0.165 |  |
| Indoor VOC index, mean ~ %>250 (pooled) | 2100 | 783 | -0.06296 | 0.03665 | [-0.1348, 0.008874] | -1.72 | 0.086 |  |
| Indoor VOC index, mean ~ %>250 (daily avg) | 2100 | 724 | -0.06713 | 0.03783 | [-0.1413, 0.007015] | -1.77 | 0.076 |  |
| Steps per wear-day ~ Any >250 (0/1) | 1872 | 690 | +424.7 | 221.3 | [-9.001, 858.3] | 1.92 | 0.055 |  |
| Steps per wear-day ~ %>250 (pooled) | 1872 | 690 | +1.594 | 12.22 | [-22.36, 25.55] | 0.13 | 0.896 |  |
| Steps per wear-day ~ %>250 (daily avg) | 1872 | 637 | +1.822 | 12.07 | [-21.84, 25.48] | 0.15 | 0.880 |  |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | 1872 | 690 | **+1.322** | 0.6608 | [0.0265, 2.617] | **2.00** | **0.045*** | * |
| Brisk-cadence minutes per day ~ %>250 (pooled) | 1872 | 690 | +0.009263 | 0.03436 | [-0.05808, 0.07661] | 0.27 | 0.787 |  |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | 1872 | 637 | +0.01013 | 0.03394 | [-0.05639, 0.07664] | 0.30 | 0.765 |  |
| Resting heart-rate proxy ~ Any >250 (0/1) | 1877 | 692 | **+2.658** | 0.4056 | [1.863, 3.453] | **6.55** | **5.6e-11***** | *** |
| Resting heart-rate proxy ~ %>250 (pooled) | 1877 | 692 | **+0.09123** | 0.02068 | [0.05069, 0.1318] | **4.41** | **1.0e-05***** | *** |
| Resting heart-rate proxy ~ %>250 (daily avg) | 1877 | 638 | **+0.09273** | 0.02141 | [0.05076, 0.1347] | **4.33** | **1.5e-05***** | *** |
| Total sleep time per night ~ Any >250 (0/1) | 1893 | 694 | **-7.063** | 3.289 | [-13.51, -0.6173] | **-2.15** | **0.032*** | * |
| Total sleep time per night ~ %>250 (pooled) | 1893 | 694 | -0.09953 | 0.1422 | [-0.3783, 0.1792] | -0.70 | 0.484 |  |
| Total sleep time per night ~ %>250 (daily avg) | 1893 | 641 | -0.09255 | 0.1458 | [-0.3782, 0.1931] | -0.63 | 0.525 |  |
| Garmin stress score, mean ~ Any >250 (0/1) | 1879 | 692 | **+4.706** | 0.8561 | [3.028, 6.384] | **5.50** | **3.9e-08***** | *** |
| Garmin stress score, mean ~ %>250 (pooled) | 1879 | 692 | **+0.1758** | 0.04546 | [0.08673, 0.2649] | **3.87** | **1.1e-04***** | *** |
| Garmin stress score, mean ~ %>250 (daily avg) | 1879 | 640 | **+0.1787** | 0.04687 | [0.0868, 0.2705] | **3.81** | **1.4e-04***** | *** |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | **-0.299 [-0.435, -0.163]** | **1.2e-04 (FDR<0.05)** | **3.8e-05 (FDR<0.05)** | 0.1084 | -18.5 | +6.2 | 0.0988 \| 0.0915 |
| MoCA total score ~ %>250 (pooled) | **-0.270 [-0.428, -0.112]** | **0.004 (FDR<0.05)** | **0.001 (FDR<0.05)** | 0.1069 | -14.8 | +9.8 | 0.0974 \| 0.0915 |
| MoCA total score ~ %>250 (daily avg) | **-0.265 [-0.426, -0.105]** | **0.005 (FDR<0.05)** | **0.002 (FDR<0.05)** | 0.1066 | -14.3 | +10.4 | 0.0971 \| 0.0915 |
| Cognitive impairment ~ Any >250 (0/1) | **OR 1.150 [1.049, 1.261]** | **0.012 (FDR<0.05)** | **0.005 (FDR<0.05)** | 0.6735 | -6.9 | +6.7 | 0.6654 \| 0.6603 |
| Cognitive impairment ~ %>250 (pooled) | **OR 1.151 [1.046, 1.266]** | **0.017 (FDR<0.05)** | **0.007 (FDR<0.05)** | 0.6706 | -6.9 | +6.8 | 0.6629 \| 0.6603 |
| Cognitive impairment ~ %>250 (daily avg) | **OR 1.146 [1.042, 1.260]** | **0.021 (FDR<0.05)** | **0.008 (FDR<0.05)** | 0.6703 | -6.3 | +7.3 | 0.6627 \| 0.6603 |
| MoCA memory index score ~ Any >250 (0/1) | -0.136 [-0.254, -0.017] | 0.080 | **0.048 (FDR<0.05)** | 0.0738 | -3.4 | +2.0 | 0.0641 \| 0.0630 |
| MoCA memory index score ~ %>250 (pooled) | -0.126 [-0.235, -0.016] | 0.080 | **0.048 (FDR<0.05)** | 0.0735 | -2.7 | +2.7 | 0.0644 \| 0.0630 |
| MoCA memory index score ~ %>250 (daily avg) | -0.120 [-0.229, -0.011] | 0.093 | 0.051 | 0.0733 | -2.3 | +3.1 | 0.0642 \| 0.0630 |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | +0.035 [-0.171, +0.241] | 0.842 | 0.788 | 0.1028 | +1.9 | +2.1 | 0.0908 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | +0.146 [-0.114, +0.406] | 0.440 | 0.620 | 0.1036 | +0.0 | +0.3 | 0.0916 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | +0.131 [-0.130, +0.393] | 0.495 | 0.620 | 0.1034 | +0.4 | +0.7 | 0.0914 \| 0.0916 |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | OR 1.074 [0.957, 1.204] | 0.394 | 0.331 | 0.6795 | +0.5 | +3.2 | 0.6665 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | OR 1.077 [0.978, 1.185] | 0.267 | 0.245 | 0.6820 | -0.2 | +2.5 | 0.6693 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | OR 1.067 [0.969, 1.175] | 0.348 | 0.295 | 0.6817 | +0.3 | +3.0 | 0.6689 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | +0.006 [-0.033, +0.046] | 0.844 | 0.748 | 0.1508 | +1.9 | +12.8 | 0.1377 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | +0.041 [-0.010, +0.092] | 0.230 | 0.173 | 0.1525 | -2.4 | +8.6 | 0.1390 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | +0.041 [-0.009, +0.092] | 0.230 | 0.173 | 0.1525 | -2.3 | +8.6 | 0.1391 \| 0.1387 |
| Indoor temperature, mean ~ Any >250 (0/1) | -0.029 [-0.117, +0.058] | 0.686 | 0.982 | 0.2980 | +1.6 | +0.1 | 0.2889 \| 0.2896 |
| Indoor temperature, mean ~ %>250 (pooled) | +0.021 [-0.077, +0.118] | 0.805 | 0.982 | 0.2979 | +1.8 | +0.3 | 0.2890 \| 0.2896 |
| Indoor temperature, mean ~ %>250 (daily avg) | +0.018 [-0.080, +0.116] | 0.837 | 0.982 | 0.2979 | +1.8 | +0.3 | 0.2890 \| 0.2896 |
| Indoor relative humidity, mean ~ Any >250 (0/1) | -0.213 [-0.478, +0.052] | 0.235 | 0.898 | 0.2419 | -0.5 | -2.4 | 0.2308 \| 0.2307 |
| Indoor relative humidity, mean ~ %>250 (pooled) | +0.007 [-0.265, +0.279] | 0.977 | 0.992 | 0.2410 | +2.0 | +0.1 | 0.2299 \| 0.2307 |
| Indoor relative humidity, mean ~ %>250 (daily avg) | +0.009 [-0.267, +0.285] | 0.969 | 0.992 | 0.2410 | +2.0 | +0.1 | 0.2298 \| 0.2307 |
| Indoor VOC index, mean ~ Any >250 (0/1) | +0.515 [-0.211, +1.241] | 0.319 | 0.868 | 0.0435 | -0.1 | -0.1 | 0.0269 \| 0.0271 |
| Indoor VOC index, mean ~ %>250 (pooled) | -0.696 [-1.491, +0.098] | 0.195 | 0.665 | 0.0443 | -1.8 | -1.8 | 0.0271 \| 0.0271 |
| Indoor VOC index, mean ~ %>250 (daily avg) | -0.733 [-1.542, +0.077] | 0.184 | 0.665 | 0.0445 | -2.2 | -2.2 | 0.0273 \| 0.0271 |
| Steps per wear-day ~ Any >250 (0/1) | +204.919 [-4.344, +414.181] | 0.145 | 0.170 | 0.1367 | -2.2 | +5.8 | 0.1233 \| 0.1222 |
| Steps per wear-day ~ %>250 (pooled) | +17.470 [-245.130, +280.071] | 0.939 | 0.953 | 0.1348 | +2.0 | +9.9 | 0.1205 \| 0.1222 |
| Steps per wear-day ~ %>250 (daily avg) | +19.630 [-235.302, +274.563] | 0.930 | 0.953 | 0.1348 | +2.0 | +9.9 | 0.1205 \| 0.1222 |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | +0.638 [+0.013, +1.263] | 0.128 | 0.192 | 0.1577 | -2.5 | +5.7 | 0.1460 \| 0.1447 |
| Brisk-cadence minutes per day ~ %>250 (pooled) | +0.102 [-0.637, +0.840] | 0.868 | 0.828 | 0.1557 | +1.9 | +10.1 | 0.1432 \| 0.1447 |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | +0.109 [-0.608, +0.826] | 0.852 | 0.828 | 0.1557 | +1.9 | +10.1 | 0.1433 \| 0.1447 |
| Resting heart-rate proxy ~ Any >250 (0/1) | **+1.283 [+0.899, +1.666]** | **1.0e-09 (FDR<0.05)** | **1.2e-10 (FDR<0.05)** | 0.1795 | -42.8 | +28.4 | 0.1667 \| 0.1482 |
| Resting heart-rate proxy ~ %>250 (pooled) | **+1.001 [+0.556, +1.445]** | **8.3e-05 (FDR<0.05)** | **1.5e-05 (FDR<0.05)** | 0.1719 | -25.5 | +45.8 | 0.1595 \| 0.1482 |
| Resting heart-rate proxy ~ %>250 (daily avg) | **+1.000 [+0.548, +1.453]** | **1.1e-04 (FDR<0.05)** | **1.9e-05 (FDR<0.05)** | 0.1719 | -25.4 | +45.8 | 0.1594 \| 0.1482 |
| Total sleep time per night ~ Any >250 (0/1) | -3.404 [-6.511, -0.298] | 0.093 | 0.123 | 0.0356 | -2.6 | +6.3 | 0.0214 \| 0.0209 |
| Total sleep time per night ~ %>250 (pooled) | -1.051 [-3.995, +1.893] | 0.654 | 0.582 | 0.0335 | +1.6 | +10.5 | 0.0205 \| 0.0209 |
| Total sleep time per night ~ %>250 (daily avg) | -0.961 [-3.926, +2.005] | 0.693 | 0.582 | 0.0334 | +1.6 | +10.5 | 0.0204 \| 0.0209 |
| Garmin stress score, mean ~ Any >250 (0/1) | **+2.270 [+1.461, +3.080]** | **5.1e-07 (FDR<0.05)** | **8.0e-08 (FDR<0.05)** | 0.1195 | -28.7 | +31.7 | 0.1039 \| 0.0902 |
| Garmin stress score, mean ~ %>250 (pooled) | **+1.927 [+0.951, +2.904]** | **6.5e-04 (FDR<0.05)** | **1.6e-04 (FDR<0.05)** | 0.1156 | -20.3 | +40.1 | 0.0997 \| 0.0902 |
| Garmin stress score, mean ~ %>250 (daily avg) | **+1.926 [+0.936, +2.917]** | **7.9e-04 (FDR<0.05)** | **1.9e-04 (FDR<0.05)** | 0.1156 | -20.3 | +40.1 | 0.0996 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | 1271 | 244 | **-0.4572** | 0.2262 | [-0.9005, -0.01383] | **-2.02** | **0.043*** | * |
| MoCA total score ~ %>250 (pooled) | 1271 | 244 | -0.05711 | 0.03288 | [-0.1216, 0.007323] | -1.74 | 0.082 |  |
| MoCA total score ~ %>250 (daily avg) | 1271 | 207 | -0.05806 | 0.0339 | [-0.1245, 0.008393] | -1.71 | 0.087 |  |
| Cognitive impairment ~ Any >250 (0/1) | 1271 | 244 | +0.1423 | 0.1549 | [-0.1613, 0.4459] | 0.92 | 0.358 |  |
| Cognitive impairment ~ %>250 (pooled) | 1271 | 244 | +0.00508 | 0.01248 | [-0.01939, 0.02955] | 0.41 | 0.684 |  |
| Cognitive impairment ~ %>250 (daily avg) | 1271 | 207 | +0.004448 | 0.01269 | [-0.02043, 0.02933] | 0.35 | 0.726 |  |
| MoCA memory index score ~ Any >250 (0/1) | 1271 | 244 | -0.04361 | 0.1947 | [-0.4251, 0.3379] | -0.22 | 0.823 |  |
| MoCA memory index score ~ %>250 (pooled) | 1271 | 244 | **-0.03702** | 0.0127 | [-0.06192, -0.01212] | **-2.91** | **0.004**** | ** |
| MoCA memory index score ~ %>250 (daily avg) | 1271 | 207 | **-0.03768** | 0.01287 | [-0.0629, -0.01246] | **-2.93** | **0.003**** | ** |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | 1270 | 243 | +0.1666 | 0.3351 | [-0.4902, 0.8234] | 0.50 | 0.619 |  |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | 1270 | 243 | -0.02618 | 0.03088 | [-0.08669, 0.03433] | -0.85 | 0.396 |  |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | 1270 | 206 | -0.02678 | 0.0322 | [-0.08988, 0.03633] | -0.83 | 0.406 |  |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | 1270 | 243 | +0.2607 | 0.1927 | [-0.117, 0.6383] | 1.35 | 0.176 |  |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | 1270 | 243 | +0.004029 | 0.01332 | [-0.02208, 0.03013] | 0.30 | 0.762 |  |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | 1270 | 206 | +0.0045 | 0.01345 | [-0.02185, 0.03085] | 0.33 | 0.738 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | 1251 | 241 | -0.05589 | 0.06058 | [-0.1746, 0.06284] | -0.92 | 0.356 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | 1251 | 241 | -0.003548 | 0.001915 | [-0.007302, 0.0002055] | -1.85 | 0.064 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | 1251 | 205 | -0.00356 | 0.001909 | [-0.007302, 0.0001827] | -1.86 | 0.062 |  |
| Indoor temperature, mean ~ Any >250 (0/1) | 1251 | 241 | -0.2604 | 0.1388 | [-0.5324, 0.01154] | -1.88 | 0.061 |  |
| Indoor temperature, mean ~ %>250 (pooled) | 1251 | 241 | +0.004588 | 0.01443 | [-0.0237, 0.03288] | 0.32 | 0.751 |  |
| Indoor temperature, mean ~ %>250 (daily avg) | 1251 | 205 | +0.004465 | 0.01441 | [-0.02378, 0.03271] | 0.31 | 0.757 |  |
| Indoor relative humidity, mean ~ Any >250 (0/1) | 1251 | 241 | -0.4415 | 0.4291 | [-1.282, 0.3995] | -1.03 | 0.304 |  |
| Indoor relative humidity, mean ~ %>250 (pooled) | 1251 | 241 | +0.03502 | 0.02566 | [-0.01526, 0.0853] | 1.37 | 0.172 |  |
| Indoor relative humidity, mean ~ %>250 (daily avg) | 1251 | 205 | +0.03663 | 0.02619 | [-0.0147, 0.08795] | 1.40 | 0.162 |  |
| Indoor VOC index, mean ~ Any >250 (0/1) | 1251 | 241 | +0.3625 | 1.081 | [-1.756, 2.481] | 0.34 | 0.737 |  |
| Indoor VOC index, mean ~ %>250 (pooled) | 1251 | 241 | -0.1118 | 0.06753 | [-0.2442, 0.02058] | -1.66 | 0.098 |  |
| Indoor VOC index, mean ~ %>250 (daily avg) | 1251 | 205 | -0.1138 | 0.07087 | [-0.2527, 0.02515] | -1.61 | 0.108 |  |
| Steps per wear-day ~ Any >250 (0/1) | 1125 | 218 | +146 | 285.8 | [-414.2, 706.2] | 0.51 | 0.609 |  |
| Steps per wear-day ~ %>250 (pooled) | 1125 | 218 | +19.24 | 26.79 | [-33.26, 71.73] | 0.72 | 0.473 |  |
| Steps per wear-day ~ %>250 (daily avg) | 1125 | 186 | +19.77 | 27.2 | [-33.54, 73.07] | 0.73 | 0.467 |  |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | 1125 | 218 | +1.139 | 0.9316 | [-0.6868, 2.965] | 1.22 | 0.221 |  |
| Brisk-cadence minutes per day ~ %>250 (pooled) | 1125 | 218 | +0.0932 | 0.09473 | [-0.09247, 0.2789] | 0.98 | 0.325 |  |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | 1125 | 186 | +0.09587 | 0.0975 | [-0.09522, 0.287] | 0.98 | 0.325 |  |
| Resting heart-rate proxy ~ Any >250 (0/1) | 1128 | 218 | +0.8428 | 0.5614 | [-0.2574, 1.943] | 1.50 | 0.133 |  |
| Resting heart-rate proxy ~ %>250 (pooled) | 1128 | 218 | +0.1099 | 0.07293 | [-0.03301, 0.2529] | 1.51 | 0.132 |  |
| Resting heart-rate proxy ~ %>250 (daily avg) | 1128 | 185 | +0.1137 | 0.07671 | [-0.0366, 0.2641] | 1.48 | 0.138 |  |
| Total sleep time per night ~ Any >250 (0/1) | 1137 | 215 | -0.47 | 5.007 | [-10.28, 9.344] | -0.09 | 0.925 |  |
| Total sleep time per night ~ %>250 (pooled) | 1137 | 215 | -0.06004 | 0.4703 | [-0.9819, 0.8618] | -0.13 | 0.898 |  |
| Total sleep time per night ~ %>250 (daily avg) | 1137 | 183 | -0.06139 | 0.4728 | [-0.9881, 0.8653] | -0.13 | 0.897 |  |
| Garmin stress score, mean ~ Any >250 (0/1) | 1130 | 218 | +1.544 | 1.273 | [-0.9502, 4.039] | 1.21 | 0.225 |  |
| Garmin stress score, mean ~ %>250 (pooled) | 1130 | 218 | +0.1345 | 0.2143 | [-0.2856, 0.5546] | 0.63 | 0.530 |  |
| Garmin stress score, mean ~ %>250 (daily avg) | 1130 | 186 | +0.1372 | 0.223 | [-0.2998, 0.5742] | 0.62 | 0.538 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | -0.180 [-0.355, -0.005] | 0.264 | 0.084 | 0.1011 | -3.5 | +10.2 | 0.0809 \| 0.0789 |
| MoCA total score ~ %>250 (pooled) | -0.277 [-0.590, +0.036] | 0.404 | 0.138 | 0.1064 | -11.0 | +2.6 | 0.0801 \| 0.0789 |
| MoCA total score ~ %>250 (daily avg) | -0.276 [-0.593, +0.040] | 0.405 | 0.138 | 0.1064 | -11.0 | +2.7 | 0.0800 \| 0.0789 |
| Cognitive impairment ~ Any >250 (0/1) | OR 1.058 [0.938, 1.192] | 0.759 | 0.585 | 0.6618 | +1.2 | +0.9 | 0.6436 \| 0.6443 |
| Cognitive impairment ~ %>250 (pooled) | OR 1.025 [0.910, 1.154] | 0.932 | 0.834 | 0.6595 | +1.8 | +1.6 | 0.6433 \| 0.6443 |
| Cognitive impairment ~ %>250 (daily avg) | OR 1.021 [0.907, 1.150] | 0.932 | 0.834 | 0.6595 | +1.9 | +1.7 | 0.6432 \| 0.6443 |
| MoCA memory index score ~ Any >250 (0/1) | -0.017 [-0.168, +0.133] | 0.940 | 0.823 | 0.0710 | +1.9 | +2.6 | 0.0455 \| 0.0477 |
| MoCA memory index score ~ %>250 (pooled) | -0.180 [-0.300, -0.059] | 0.053 | **0.020 (FDR<0.05)** | 0.0756 | -4.3 | -3.6 | 0.0510 \| 0.0477 |
| MoCA memory index score ~ %>250 (daily avg) | -0.179 [-0.300, -0.059] | 0.053 | **0.020 (FDR<0.05)** | 0.0755 | -4.3 | -3.6 | 0.0509 \| 0.0477 |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | +0.066 [-0.193, +0.324] | 0.932 | 0.953 | 0.0909 | +1.7 | -0.2 | 0.0656 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | -0.127 [-0.420, +0.166] | 0.797 | 0.953 | 0.0914 | +1.0 | -1.0 | 0.0662 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | -0.127 [-0.427, +0.173] | 0.808 | 0.953 | 0.0914 | +1.0 | -1.0 | 0.0662 \| 0.0675 |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | OR 1.108 [0.955, 1.286] | 0.532 | 0.607 | 0.6933 | +0.2 | -0.9 | 0.6738 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | OR 1.020 [0.899, 1.157] | 0.932 | 0.958 | 0.6933 | +1.9 | +0.8 | 0.6712 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | OR 1.022 [0.901, 1.158] | 0.932 | 0.958 | 0.6933 | +1.9 | +0.8 | 0.6712 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | -0.022 [-0.069, +0.025] | 0.758 | 0.552 | 0.1367 | +1.2 | -0.8 | 0.1130 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | -0.017 [-0.036, +0.001] | 0.340 | 0.265 | 0.1365 | +1.5 | -0.5 | 0.1139 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | -0.017 [-0.035, +0.001] | 0.340 | 0.265 | 0.1365 | +1.5 | -0.5 | 0.1139 \| 0.1139 |
| Indoor temperature, mean ~ Any >250 (0/1) | -0.103 [-0.210, +0.005] | 0.340 | 0.674 | 0.3117 | -1.7 | -3.6 | 0.2902 \| 0.2892 |
| Indoor temperature, mean ~ %>250 (pooled) | +0.022 [-0.116, +0.161] | 0.932 | 0.942 | 0.3098 | +1.8 | -0.1 | 0.2883 \| 0.2892 |
| Indoor temperature, mean ~ %>250 (daily avg) | +0.021 [-0.114, +0.157] | 0.932 | 0.942 | 0.3098 | +1.8 | -0.1 | 0.2883 \| 0.2892 |
| Indoor relative humidity, mean ~ Any >250 (0/1) | -0.174 [-0.506, +0.158] | 0.688 | 0.597 | 0.2602 | +0.9 | +1.4 | 0.2388 \| 0.2403 |
| Indoor relative humidity, mean ~ %>250 (pooled) | +0.171 [-0.075, +0.417] | 0.532 | 0.585 | 0.2602 | +0.9 | +1.4 | 0.2403 \| 0.2403 |
| Indoor relative humidity, mean ~ %>250 (daily avg) | +0.176 [-0.071, +0.422] | 0.532 | 0.585 | 0.2602 | +0.9 | +1.4 | 0.2403 \| 0.2403 |
| Indoor VOC index, mean ~ Any >250 (0/1) | +0.143 [-0.693, +0.979] | 0.932 | 0.784 | 0.0238 | +1.9 | +1.3 | 0.0009 \| 0.0025 |
| Indoor VOC index, mean ~ %>250 (pooled) | -0.547 [-1.194, +0.101] | 0.425 | 0.490 | 0.0250 | +0.4 | -0.2 | 0.0028 \| 0.0025 |
| Indoor VOC index, mean ~ %>250 (daily avg) | -0.546 [-1.213, +0.121] | 0.441 | 0.490 | 0.0250 | +0.4 | -0.2 | 0.0027 \| 0.0025 |
| Steps per wear-day ~ Any >250 (0/1) | +57.740 [-163.780, +279.259] | 0.932 | 0.958 | 0.1247 | +1.7 | +5.0 | 0.1061 \| 0.1080 |
| Steps per wear-day ~ %>250 (pooled) | +86.037 [-148.778, +320.853] | 0.872 | 0.958 | 0.1249 | +1.4 | +4.7 | 0.1075 \| 0.1080 |
| Steps per wear-day ~ %>250 (daily avg) | +85.411 [-144.929, +315.752] | 0.871 | 0.958 | 0.1249 | +1.4 | +4.7 | 0.1076 \| 0.1080 |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | +0.450 [-0.272, +1.172] | 0.594 | 0.882 | 0.1399 | +0.4 | +3.8 | 0.1234 \| 0.1245 |
| Brisk-cadence minutes per day ~ %>250 (pooled) | +0.417 [-0.414, +1.247] | 0.717 | 0.882 | 0.1397 | +0.6 | +4.1 | 0.1246 \| 0.1245 |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | +0.414 [-0.411, +1.240] | 0.717 | 0.882 | 0.1397 | +0.6 | +4.1 | 0.1246 \| 0.1245 |
| Resting heart-rate proxy ~ Any >250 (0/1) | +0.333 [-0.102, +0.768] | 0.486 | 0.186 | 0.1313 | -0.3 | +11.0 | 0.1046 \| 0.1044 |
| Resting heart-rate proxy ~ %>250 (pooled) | +0.491 [-0.147, +1.130] | 0.484 | 0.186 | 0.1334 | -3.0 | +8.2 | 0.1051 \| 0.1044 |
| Resting heart-rate proxy ~ %>250 (daily avg) | +0.491 [-0.158, +1.140] | 0.500 | 0.186 | 0.1334 | -3.0 | +8.2 | 0.1050 \| 0.1044 |
| Total sleep time per night ~ Any >250 (0/1) | -0.184 [-4.029, +3.660] | 0.977 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0067 \| -0.0051 |
| Total sleep time per night ~ %>250 (pooled) | -0.236 [-3.860, +3.388] | 0.964 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0061 \| -0.0051 |
| Total sleep time per night ~ %>250 (daily avg) | -0.232 [-3.737, +3.273] | 0.964 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0061 \| -0.0051 |
| Garmin stress score, mean ~ Any >250 (0/1) | +0.610 [-0.375, +1.594] | 0.599 | 0.471 | 0.0738 | +0.5 | +8.3 | 0.0508 \| 0.0510 |
| Garmin stress score, mean ~ %>250 (pooled) | +0.600 [-1.274, +2.475] | 0.924 | 0.708 | 0.0738 | +0.5 | +8.3 | 0.0469 \| 0.0510 |
| Garmin stress score, mean ~ %>250 (daily avg) | +0.591 [-1.293, +2.476] | 0.931 | 0.708 | 0.0737 | +0.6 | +8.4 | 0.0468 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | 867 | 551 | -0.4363 | 0.2307 | [-0.8885, 0.01577] | -1.89 | 0.059 |  |
| MoCA total score ~ %>250 (pooled) | 867 | 551 | -0.01351 | 0.007464 | [-0.02814, 0.001115] | -1.81 | 0.070 |  |
| MoCA total score ~ %>250 (daily avg) | 867 | 528 | -0.01339 | 0.007628 | [-0.02834, 0.001564] | -1.75 | 0.079 |  |
| Cognitive impairment ~ Any >250 (0/1) | 867 | 551 | +0.1706 | 0.1511 | [-0.1256, 0.4668] | 1.13 | 0.259 |  |
| Cognitive impairment ~ %>250 (pooled) | 867 | 551 | +0.009194 | 0.004797 | [-0.0002091, 0.0186] | 1.92 | 0.055 |  |
| Cognitive impairment ~ %>250 (daily avg) | 867 | 528 | +0.009035 | 0.004851 | [-0.0004728, 0.01854] | 1.86 | 0.063 |  |
| MoCA memory index score ~ Any >250 (0/1) | 867 | 551 | **-0.49** | 0.1945 | [-0.8712, -0.1088] | **-2.52** | **0.012*** | * |
| MoCA memory index score ~ %>250 (pooled) | 867 | 551 | -0.00784 | 0.005467 | [-0.01856, 0.002876] | -1.43 | 0.152 |  |
| MoCA memory index score ~ %>250 (daily avg) | 867 | 528 | -0.007382 | 0.005484 | [-0.01813, 0.003367] | -1.35 | 0.178 |  |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | 865 | 550 | -0.03675 | 0.3628 | [-0.7478, 0.6743] | -0.10 | 0.919 |  |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | 865 | 550 | +0.01924 | 0.0134 | [-0.007021, 0.04551] | 1.44 | 0.151 |  |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | 865 | 527 | +0.01776 | 0.01368 | [-0.009056, 0.04458] | 1.30 | 0.194 |  |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | 865 | 550 | +0.04924 | 0.1821 | [-0.3077, 0.4062] | 0.27 | 0.787 |  |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | 865 | 550 | +0.007781 | 0.004852 | [-0.001729, 0.01729] | 1.60 | 0.109 |  |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | 865 | 527 | +0.006796 | 0.004942 | [-0.002889, 0.01648] | 1.38 | 0.169 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | 849 | 542 | +0.02042 | 0.0694 | [-0.1156, 0.1564] | 0.29 | 0.769 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | 849 | 542 | +0.004143 | 0.002738 | [-0.001223, 0.009509] | 1.51 | 0.130 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | 849 | 519 | +0.004211 | 0.002757 | [-0.001192, 0.009614] | 1.53 | 0.127 |  |
| Indoor temperature, mean ~ Any >250 (0/1) | 849 | 542 | -0.06749 | 0.1616 | [-0.3843, 0.2493] | -0.42 | 0.676 |  |
| Indoor temperature, mean ~ %>250 (pooled) | 849 | 542 | -0.001669 | 0.005235 | [-0.01193, 0.008592] | -0.32 | 0.750 |  |
| Indoor temperature, mean ~ %>250 (daily avg) | 849 | 519 | -0.001834 | 0.005318 | [-0.01226, 0.008589] | -0.34 | 0.730 |  |
| Indoor relative humidity, mean ~ Any >250 (0/1) | 849 | 542 | -0.7738 | 0.4632 | [-1.682, 0.1341] | -1.67 | 0.095 |  |
| Indoor relative humidity, mean ~ %>250 (pooled) | 849 | 542 | -0.005343 | 0.01454 | [-0.03384, 0.02316] | -0.37 | 0.713 |  |
| Indoor relative humidity, mean ~ %>250 (daily avg) | 849 | 519 | -0.005294 | 0.01494 | [-0.03458, 0.02399] | -0.35 | 0.723 |  |
| Indoor VOC index, mean ~ Any >250 (0/1) | 849 | 542 | +1.782 | 1.21 | [-0.5897, 4.154] | 1.47 | 0.141 |  |
| Indoor VOC index, mean ~ %>250 (pooled) | 849 | 542 | -0.07141 | 0.04282 | [-0.1553, 0.01252] | -1.67 | 0.095 |  |
| Indoor VOC index, mean ~ %>250 (daily avg) | 849 | 519 | -0.07615 | 0.04418 | [-0.1627, 0.01045] | -1.72 | 0.085 |  |
| Steps per wear-day ~ Any >250 (0/1) | 747 | 472 | +519.9 | 392.8 | [-250, 1290] | 1.32 | 0.186 |  |
| Steps per wear-day ~ %>250 (pooled) | 747 | 472 | -5.229 | 13.69 | [-32.07, 21.61] | -0.38 | 0.703 |  |
| Steps per wear-day ~ %>250 (daily avg) | 747 | 451 | -4.592 | 13.38 | [-30.82, 21.64] | -0.34 | 0.732 |  |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | 747 | 472 | +0.8271 | 1.127 | [-1.382, 3.037] | 0.73 | 0.463 |  |
| Brisk-cadence minutes per day ~ %>250 (pooled) | 747 | 472 | -0.01786 | 0.03757 | [-0.0915, 0.05579] | -0.48 | 0.635 |  |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | 747 | 451 | -0.01595 | 0.03673 | [-0.08793, 0.05603] | -0.43 | 0.664 |  |
| Resting heart-rate proxy ~ Any >250 (0/1) | 749 | 474 | +1.288 | 0.6609 | [-0.007651, 2.583] | 1.95 | 0.051 |  |
| Resting heart-rate proxy ~ %>250 (pooled) | 749 | 474 | **+0.04225** | 0.02136 | [0.0003932, 0.08411] | **1.98** | **0.048*** | * |
| Resting heart-rate proxy ~ %>250 (daily avg) | 749 | 453 | **+0.04395** | 0.02176 | [0.001304, 0.08659] | **2.02** | **0.043*** | * |
| Total sleep time per night ~ Any >250 (0/1) | 756 | 479 | **-13.96** | 5.671 | [-25.07, -2.844] | **-2.46** | **0.014*** | * |
| Total sleep time per night ~ %>250 (pooled) | 756 | 479 | -0.03984 | 0.1601 | [-0.3537, 0.274] | -0.25 | 0.804 |  |
| Total sleep time per night ~ %>250 (daily avg) | 756 | 458 | -0.03427 | 0.1632 | [-0.3542, 0.2856] | -0.21 | 0.834 |  |
| Garmin stress score, mean ~ Any >250 (0/1) | 749 | 474 | **+3.273** | 1.383 | [0.5626, 5.983] | **2.37** | **0.018*** | * |
| Garmin stress score, mean ~ %>250 (pooled) | 749 | 474 | **+0.1119** | 0.04815 | [0.01753, 0.2063] | **2.32** | **0.020*** | * |
| Garmin stress score, mean ~ %>250 (daily avg) | 749 | 454 | **+0.1154** | 0.04926 | [0.01889, 0.212] | **2.34** | **0.019*** | * |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any >250 (0/1) | -0.210 [-0.428, +0.008] | 0.212 | 0.101 | 0.0844 | -1.4 | +0.1 | 0.0559 \| 0.0541 |
| MoCA total score ~ %>250 (pooled) | -0.210 [-0.438, +0.017] | 0.229 | 0.109 | 0.0845 | -1.5 | +0.1 | 0.0565 \| 0.0541 |
| MoCA total score ~ %>250 (daily avg) | -0.206 [-0.436, +0.024] | 0.242 | 0.112 | 0.0844 | -1.3 | +0.2 | 0.0564 \| 0.0541 |
| Cognitive impairment ~ Any >250 (0/1) | OR 1.086 [0.941, 1.252] | 0.480 | 0.335 | 0.6615 | +0.7 | +2.4 | 0.6414 \| 0.6425 |
| Cognitive impairment ~ %>250 (pooled) | OR 1.154 [0.997, 1.336] | 0.205 | 0.114 | 0.6640 | -1.8 | -0.1 | 0.6447 \| 0.6425 |
| Cognitive impairment ~ %>250 (daily avg) | OR 1.149 [0.993, 1.330] | 0.219 | 0.114 | 0.6636 | -1.6 | +0.1 | 0.6446 \| 0.6425 |
| MoCA memory index score ~ Any >250 (0/1) | -0.236 [-0.420, -0.052] | 0.091 | 0.052 | 0.0664 | -4.2 | -2.5 | 0.0335 \| 0.0286 |
| MoCA memory index score ~ %>250 (pooled) | -0.122 [-0.289, +0.045] | 0.334 | 0.181 | 0.0615 | +0.3 | +2.1 | 0.0298 \| 0.0286 |
| MoCA memory index score ~ %>250 (daily avg) | -0.114 [-0.279, +0.052] | 0.374 | 0.197 | 0.0612 | +0.5 | +2.3 | 0.0296 \| 0.0286 |
| CES-D-10 depressive symptoms ~ Any >250 (0/1) | -0.018 [-0.360, +0.325] | 0.948 | 0.950 | 0.1111 | +2.0 | +3.3 | 0.0769 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %>250 (pooled) | +0.300 [-0.109, +0.709] | 0.334 | 0.578 | 0.1143 | -1.2 | +0.1 | 0.0788 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %>250 (daily avg) | +0.274 [-0.139, +0.687] | 0.390 | 0.578 | 0.1138 | -0.6 | +0.6 | 0.0784 \| 0.0796 |
| Clinically relevant depressive symptoms ~ Any >250 (0/1) | OR 1.024 [0.862, 1.216] | 0.871 | 0.871 | 0.6604 | +1.9 | +4.9 | 0.6298 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %>250 (pooled) | OR 1.129 [0.973, 1.309] | 0.270 | 0.215 | 0.6655 | -0.5 | +2.5 | 0.6366 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %>250 (daily avg) | OR 1.110 [0.956, 1.289] | 0.360 | 0.291 | 0.6649 | +0.2 | +3.2 | 0.6350 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any >250 (0/1) | +0.010 [-0.056, +0.075] | 0.860 | 0.769 | 0.1540 | +1.9 | +11.3 | 0.1296 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (pooled) | +0.065 [-0.019, +0.149] | 0.304 | 0.183 | 0.1579 | -2.0 | +7.4 | 0.1309 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %>250 (daily avg) | +0.065 [-0.018, +0.148] | 0.297 | 0.183 | 0.1580 | -2.1 | +7.3 | 0.1310 \| 0.1310 |
| Indoor temperature, mean ~ Any >250 (0/1) | -0.032 [-0.185, +0.120] | 0.815 | 0.907 | 0.2503 | +1.8 | +0.1 | 0.2242 \| 0.2264 |
| Indoor temperature, mean ~ %>250 (pooled) | -0.026 [-0.186, +0.134] | 0.850 | 0.907 | 0.2503 | +1.9 | +0.2 | 0.2227 \| 0.2264 |
| Indoor temperature, mean ~ %>250 (daily avg) | -0.028 [-0.189, +0.133] | 0.838 | 0.907 | 0.2503 | +1.9 | +0.2 | 0.2227 \| 0.2264 |
| Indoor relative humidity, mean ~ Any >250 (0/1) | -0.372 [-0.808, +0.064] | 0.259 | 0.938 | 0.2157 | -0.9 | -2.8 | 0.1862 \| 0.1857 |
| Indoor relative humidity, mean ~ %>250 (pooled) | -0.083 [-0.529, +0.362] | 0.832 | 0.938 | 0.2131 | +1.9 | -0.0 | 0.1840 \| 0.1857 |
| Indoor relative humidity, mean ~ %>250 (daily avg) | -0.082 [-0.534, +0.370] | 0.835 | 0.938 | 0.2131 | +1.9 | -0.0 | 0.1839 \| 0.1857 |
| Indoor VOC index, mean ~ Any >250 (0/1) | +0.857 [-0.283, +1.997] | 0.321 | 0.585 | 0.0579 | -0.0 | +0.3 | 0.0281 \| 0.0276 |
| Indoor VOC index, mean ~ %>250 (pooled) | -1.116 [-2.427, +0.196] | 0.259 | 0.504 | 0.0595 | -1.5 | -1.1 | 0.0291 \| 0.0276 |
| Indoor VOC index, mean ~ %>250 (daily avg) | -1.176 [-2.513, +0.161] | 0.247 | 0.504 | 0.0599 | -1.8 | -1.5 | 0.0295 \| 0.0276 |
| Steps per wear-day ~ Any >250 (0/1) | +250.915 [-120.671, +622.500] | 0.382 | 0.480 | 0.1592 | +0.1 | +0.2 | 0.1385 \| 0.1390 |
| Steps per wear-day ~ %>250 (pooled) | -82.285 [-504.678, +340.108] | 0.829 | 0.751 | 0.1572 | +1.8 | +1.9 | 0.1373 \| 0.1390 |
| Steps per wear-day ~ %>250 (daily avg) | -71.239 [-478.205, +335.726] | 0.838 | 0.756 | 0.1572 | +1.8 | +2.0 | 0.1374 \| 0.1390 |
| Brisk-cadence minutes per day ~ Any >250 (0/1) | +0.399 [-0.667, +1.465] | 0.657 | 0.821 | 0.1795 | +1.4 | +1.5 | 0.1525 \| 0.1546 |
| Brisk-cadence minutes per day ~ %>250 (pooled) | -0.281 [-1.440, +0.878] | 0.798 | 0.821 | 0.1792 | +1.7 | +1.7 | 0.1532 \| 0.1546 |
| Brisk-cadence minutes per day ~ %>250 (daily avg) | -0.247 [-1.364, +0.869] | 0.812 | 0.821 | 0.1791 | +1.8 | +1.8 | 0.1532 \| 0.1546 |
| Resting heart-rate proxy ~ Any >250 (0/1) | +0.621 [-0.004, +1.246] | 0.198 | 0.088 | 0.1567 | -1.9 | +4.1 | 0.1264 \| 0.1253 |
| Resting heart-rate proxy ~ %>250 (pooled) | +0.665 [+0.006, +1.324] | 0.192 | 0.087 | 0.1575 | -2.6 | +3.5 | 0.1281 \| 0.1253 |
| Resting heart-rate proxy ~ %>250 (daily avg) | +0.682 [+0.020, +1.344] | 0.182 | 0.087 | 0.1577 | -2.8 | +3.2 | 0.1281 \| 0.1253 |
| Total sleep time per night ~ Any >250 (0/1) | -6.730 [-12.089, -1.371] | 0.100 | 0.143 | 0.0451 | -4.9 | -2.0 | 0.0121 \| 0.0066 |
| Total sleep time per night ~ %>250 (pooled) | -0.609 [-5.403, +4.186] | 0.878 | 0.863 | 0.0364 | +1.9 | +4.8 | 0.0044 \| 0.0066 |
| Total sleep time per night ~ %>250 (daily avg) | -0.516 [-5.334, +4.302] | 0.891 | 0.863 | 0.0364 | +2.0 | +4.9 | 0.0043 \| 0.0066 |
| Garmin stress score, mean ~ Any >250 (0/1) | +1.579 [+0.271, +2.886] | 0.116 | **0.034 (FDR<0.05)** | 0.1286 | -3.8 | +9.2 | 0.0990 \| 0.0947 |
| Garmin stress score, mean ~ %>250 (pooled) | +1.762 [+0.276, +3.248] | 0.116 | **0.034 (FDR<0.05)** | 0.1304 | -5.4 | +7.7 | 0.1010 \| 0.0947 |
| Garmin stress score, mean ~ %>250 (daily avg) | +1.792 [+0.293, +3.291] | 0.116 | **0.034 (FDR<0.05)** | 0.1307 | -5.7 | +7.4 | 0.1012 \| 0.0947 |


---

## Band <54

### Total analysis base

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | 2138 | 638 | **+0.2967** | 0.1422 | [0.01796, 0.5753] | **2.09** | **0.037*** | * |
| MoCA total score ~ %<54 (pooled) | 2138 | 638 | +0.07538 | 0.1199 | [-0.1596, 0.3103] | 0.63 | 0.530 |  |
| MoCA total score ~ %<54 (daily avg) | 2138 | 420 | +0.05418 | 0.1529 | [-0.2455, 0.3539] | 0.35 | 0.723 |  |
| Cognitive impairment ~ Any <54 (0/1) | 2138 | 638 | **-0.231** | 0.1035 | [-0.4338, -0.0281] | **-2.23** | **0.026*** | * |
| Cognitive impairment ~ %<54 (pooled) | 2138 | 638 | +0.008243 | 0.08935 | [-0.1669, 0.1834] | 0.09 | 0.926 |  |
| Cognitive impairment ~ %<54 (daily avg) | 2138 | 420 | +0.04552 | 0.1054 | [-0.1611, 0.2521] | 0.43 | 0.666 |  |
| MoCA memory index score ~ Any <54 (0/1) | 2138 | 638 | +0.2038 | 0.1226 | [-0.03654, 0.444] | 1.66 | 0.097 |  |
| MoCA memory index score ~ %<54 (pooled) | 2138 | 638 | +0.1089 | 0.09815 | [-0.0835, 0.3012] | 1.11 | 0.267 |  |
| MoCA memory index score ~ %<54 (daily avg) | 2138 | 420 | +0.0006372 | 0.1068 | [-0.2087, 0.21] | 0.01 | 0.995 |  |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | 2135 | 637 | +0.1443 | 0.2281 | [-0.3028, 0.5914] | 0.63 | 0.527 |  |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | 2135 | 637 | -0.1034 | 0.1729 | [-0.4423, 0.2356] | -0.60 | 0.550 |  |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | 2135 | 419 | -0.02344 | 0.239 | [-0.4919, 0.445] | -0.10 | 0.922 |  |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | 2135 | 637 | +0.128 | 0.1245 | [-0.116, 0.3721] | 1.03 | 0.304 |  |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | 2135 | 637 | -0.05471 | 0.1338 | [-0.317, 0.2076] | -0.41 | 0.683 |  |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | 2135 | 419 | -0.03125 | 0.1447 | [-0.3148, 0.2523] | -0.22 | 0.829 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | 2100 | 628 | +0.041 | 0.04559 | [-0.04835, 0.1304] | 0.90 | 0.368 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | 2100 | 628 | +0.05161 | 0.05378 | [-0.05381, 0.157] | 0.96 | 0.337 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | 2100 | 415 | +0.09535 | 0.07122 | [-0.04424, 0.2349] | 1.34 | 0.181 |  |
| Indoor temperature, mean ~ Any <54 (0/1) | 2100 | 628 | -0.05401 | 0.09723 | [-0.2446, 0.1366] | -0.56 | 0.579 |  |
| Indoor temperature, mean ~ %<54 (pooled) | 2100 | 628 | +0.1554 | 0.09539 | [-0.03156, 0.3423] | 1.63 | 0.103 |  |
| Indoor temperature, mean ~ %<54 (daily avg) | 2100 | 415 | +0.1638 | 0.1283 | [-0.08765, 0.4152] | 1.28 | 0.202 |  |
| Indoor relative humidity, mean ~ Any <54 (0/1) | 2100 | 628 | -0.2906 | 0.2931 | [-0.865, 0.2838] | -0.99 | 0.321 |  |
| Indoor relative humidity, mean ~ %<54 (pooled) | 2100 | 628 | **-0.4596** | 0.2117 | [-0.8745, -0.04474] | **-2.17** | **0.030*** | * |
| Indoor relative humidity, mean ~ %<54 (daily avg) | 2100 | 415 | **-0.6104** | 0.3041 | [-1.206, -0.01444] | **-2.01** | **0.045*** | * |
| Indoor VOC index, mean ~ Any <54 (0/1) | 2100 | 628 | -0.7848 | 0.7883 | [-2.33, 0.7602] | -1.00 | 0.319 |  |
| Indoor VOC index, mean ~ %<54 (pooled) | 2100 | 628 | +0.04589 | 0.6379 | [-1.204, 1.296] | 0.07 | 0.943 |  |
| Indoor VOC index, mean ~ %<54 (daily avg) | 2100 | 415 | +0.3536 | 0.7188 | [-1.055, 1.762] | 0.49 | 0.623 |  |
| Steps per wear-day ~ Any <54 (0/1) | 1872 | 575 | **-479** | 212.5 | [-895.5, -62.64] | **-2.25** | **0.024*** | * |
| Steps per wear-day ~ %<54 (pooled) | 1872 | 575 | **-348.6** | 152 | [-646.5, -50.72] | **-2.29** | **0.022*** | * |
| Steps per wear-day ~ %<54 (daily avg) | 1872 | 373 | **-410** | 153.2 | [-710.4, -109.7] | **-2.68** | **0.007**** | ** |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | 1872 | 575 | -0.8998 | 0.6428 | [-2.16, 0.36] | -1.40 | 0.162 |  |
| Brisk-cadence minutes per day ~ %<54 (pooled) | 1872 | 575 | -0.7158 | 0.3662 | [-1.434, 0.001971] | -1.95 | 0.051 |  |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | 1872 | 373 | -0.9642 | 0.4963 | [-1.937, 0.008477] | -1.94 | 0.052 |  |
| Resting heart-rate proxy ~ Any <54 (0/1) | 1877 | 576 | -0.1124 | 0.4106 | [-0.9172, 0.6923] | -0.27 | 0.784 |  |
| Resting heart-rate proxy ~ %<54 (pooled) | 1877 | 576 | +0.1529 | 0.2423 | [-0.322, 0.6279] | 0.63 | 0.528 |  |
| Resting heart-rate proxy ~ %<54 (daily avg) | 1877 | 374 | +0.04968 | 0.3941 | [-0.7227, 0.8221] | 0.13 | 0.900 |  |
| Total sleep time per night ~ Any <54 (0/1) | 1893 | 588 | +3.187 | 3.359 | [-3.396, 9.77] | 0.95 | 0.343 |  |
| Total sleep time per night ~ %<54 (pooled) | 1893 | 588 | +0.43 | 2.648 | [-4.76, 5.62] | 0.16 | 0.871 |  |
| Total sleep time per night ~ %<54 (daily avg) | 1893 | 388 | +0.09387 | 2.732 | [-5.26, 5.448] | 0.03 | 0.973 |  |
| Garmin stress score, mean ~ Any <54 (0/1) | 1879 | 577 | -0.5158 | 0.8771 | [-2.235, 1.203] | -0.59 | 0.556 |  |
| Garmin stress score, mean ~ %<54 (pooled) | 1879 | 577 | +0.02025 | 0.6936 | [-1.339, 1.38] | 0.03 | 0.977 |  |
| Garmin stress score, mean ~ %<54 (daily avg) | 1879 | 375 | -0.2446 | 0.92 | [-2.048, 1.559] | -0.27 | 0.790 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | +0.136 [+0.008, +0.263] | 0.108 | **0.046 (FDR<0.05)** | 0.1016 | -2.3 | +22.3 | 0.0925 \| 0.0915 |
| MoCA total score ~ %<54 (pooled) | +0.039 [-0.082, +0.160] | 0.693 | 0.631 | 0.0999 | +1.6 | +26.3 | 0.0907 \| 0.0915 |
| MoCA total score ~ %<54 (daily avg) | +0.023 [-0.105, +0.151] | 0.837 | 0.782 | 0.0998 | +1.9 | +26.5 | 0.0906 \| 0.0915 |
| Cognitive impairment ~ Any <54 (0/1) | OR 0.900 [0.820, 0.987] | 0.081 | **0.032 (FDR<0.05)** | 0.6704 | -3.0 | +10.6 | 0.6619 \| 0.6603 |
| Cognitive impairment ~ %<54 (pooled) | OR 1.004 [0.918, 1.099] | 0.957 | 0.926 | 0.6678 | +2.0 | +15.6 | 0.6593 \| 0.6603 |
| Cognitive impairment ~ %<54 (daily avg) | OR 1.020 [0.933, 1.114] | 0.803 | 0.688 | 0.6679 | +1.8 | +15.4 | 0.6593 \| 0.6603 |
| MoCA memory index score ~ Any <54 (0/1) | +0.093 [-0.017, +0.203] | 0.210 | 0.136 | 0.0726 | -0.6 | +4.7 | 0.0635 \| 0.0630 |
| MoCA memory index score ~ %<54 (pooled) | +0.056 [-0.043, +0.155] | 0.439 | 0.345 | 0.0719 | +1.0 | +6.4 | 0.0629 \| 0.0630 |
| MoCA memory index score ~ %<54 (daily avg) | +0.000 [-0.089, +0.090] | 0.995 | 0.995 | 0.0715 | +2.0 | +7.4 | 0.0623 \| 0.0630 |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | +0.066 [-0.139, +0.271] | 0.693 | 0.632 | 0.1029 | +1.6 | +1.8 | 0.0910 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | -0.053 [-0.228, +0.121] | 0.708 | 0.632 | 0.1029 | +1.7 | +2.0 | 0.0909 \| 0.0916 |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | -0.010 [-0.211, +0.191] | 0.957 | 0.922 | 0.1027 | +2.0 | +2.2 | 0.0903 \| 0.0916 |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | OR 1.060 [0.948, 1.186] | 0.480 | 0.427 | 0.6797 | +1.0 | +3.7 | 0.6673 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | OR 0.972 [0.849, 1.113] | 0.805 | 0.756 | 0.6800 | +1.8 | +4.5 | 0.6676 \| 0.6681 |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | OR 0.987 [0.874, 1.114] | 0.892 | 0.857 | 0.6800 | +2.0 | +4.7 | 0.6667 \| 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | +0.019 [-0.022, +0.060] | 0.533 | 0.381 | 0.1512 | +1.1 | +12.0 | 0.1381 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | +0.027 [-0.028, +0.081] | 0.500 | 0.361 | 0.1515 | +0.1 | +11.0 | 0.1374 \| 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | +0.041 [-0.019, +0.101] | 0.341 | 0.248 | 0.1526 | -2.4 | +8.5 | 0.1387 \| 0.1387 |
| Indoor temperature, mean ~ Any <54 (0/1) | -0.025 [-0.112, +0.063] | 0.732 | 0.982 | 0.2980 | +1.7 | +0.2 | 0.2888 \| 0.2896 |
| Indoor temperature, mean ~ %<54 (pooled) | +0.080 [-0.016, +0.177] | 0.218 | 0.801 | 0.2990 | -1.4 | -2.9 | 0.2897 \| 0.2896 |
| Indoor temperature, mean ~ %<54 (daily avg) | +0.071 [-0.038, +0.179] | 0.365 | 0.982 | 0.2987 | -0.6 | -2.1 | 0.2894 \| 0.2896 |
| Indoor relative humidity, mean ~ Any <54 (0/1) | -0.133 [-0.396, +0.130] | 0.491 | 0.898 | 0.2414 | +1.0 | -0.9 | 0.2301 \| 0.2307 |
| Indoor relative humidity, mean ~ %<54 (pooled) | -0.238 [-0.453, -0.023] | 0.091 | 0.693 | 0.2422 | -1.3 | -3.1 | 0.2312 \| 0.2307 |
| Indoor relative humidity, mean ~ %<54 (daily avg) | -0.263 [-0.520, -0.006] | 0.127 | 0.693 | 0.2425 | -2.0 | -3.9 | 0.2313 \| 0.2307 |
| Indoor VOC index, mean ~ Any <54 (0/1) | -0.359 [-1.067, +0.348] | 0.490 | 0.868 | 0.0431 | +1.0 | +0.9 | 0.0265 \| 0.0271 |
| Indoor VOC index, mean ~ %<54 (pooled) | +0.024 [-0.624, +0.671] | 0.967 | 0.943 | 0.0426 | +2.0 | +2.0 | 0.0262 \| 0.0271 |
| Indoor VOC index, mean ~ %<54 (daily avg) | +0.152 [-0.455, +0.759] | 0.778 | 0.868 | 0.0427 | +1.8 | +1.8 | 0.0264 \| 0.0271 |
| Steps per wear-day ~ Any <54 (0/1) | -221.052 [-413.199, -28.905] | 0.079 | 0.083 | 0.1371 | -3.0 | +5.0 | 0.1234 \| 0.1222 |
| Steps per wear-day ~ %<54 (pooled) | -189.439 [-351.316, -27.562] | 0.072 | 0.083 | 0.1365 | -1.7 | +6.3 | 0.1231 \| 0.1222 |
| Steps per wear-day ~ %<54 (daily avg) | **-186.542 [-323.191, -49.893]** | **0.028 (FDR<0.05)** | 0.077 | 0.1365 | -1.6 | +6.4 | 0.1234 \| 0.1222 |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | -0.415 [-0.997, +0.166] | 0.315 | 0.250 | 0.1565 | +0.1 | +8.2 | 0.1445 \| 0.1447 |
| Brisk-cadence minutes per day ~ %<54 (pooled) | -0.389 [-0.779, +0.001] | 0.138 | 0.192 | 0.1564 | +0.3 | +8.5 | 0.1448 \| 0.1447 |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | -0.439 [-0.881, +0.004] | 0.141 | 0.192 | 0.1567 | -0.2 | +8.0 | 0.1449 \| 0.1447 |
| Resting heart-rate proxy ~ Any <54 (0/1) | -0.052 [-0.423, +0.319] | 0.868 | 0.810 | 0.1598 | +1.9 | +73.1 | 0.1476 \| 0.1482 |
| Resting heart-rate proxy ~ %<54 (pooled) | +0.083 [-0.175, +0.341] | 0.693 | 0.564 | 0.1598 | +1.8 | +73.0 | 0.1481 \| 0.1482 |
| Resting heart-rate proxy ~ %<54 (daily avg) | +0.023 [-0.328, +0.374] | 0.939 | 0.900 | 0.1597 | +2.0 | +73.2 | 0.1478 \| 0.1482 |
| Total sleep time per night ~ Any <54 (0/1) | +1.475 [-1.572, +4.522] | 0.502 | 0.506 | 0.0337 | +1.1 | +10.0 | 0.0201 \| 0.0209 |
| Total sleep time per night ~ %<54 (pooled) | +0.233 [-2.577, +3.043] | 0.924 | 0.900 | 0.0333 | +2.0 | +10.9 | 0.0203 \| 0.0209 |
| Total sleep time per night ~ %<54 (daily avg) | +0.043 [-2.384, +2.469] | 0.986 | 0.973 | 0.0333 | +2.0 | +10.9 | 0.0204 \| 0.0209 |
| Garmin stress score, mean ~ Any <54 (0/1) | -0.238 [-1.031, +0.555] | 0.715 | 0.595 | 0.1052 | +1.7 | +62.0 | 0.0894 \| 0.0902 |
| Garmin stress score, mean ~ %<54 (pooled) | +0.011 [-0.726, +0.748] | 0.986 | 0.977 | 0.1050 | +2.0 | +62.4 | 0.0894 \| 0.0902 |
| Garmin stress score, mean ~ %<54 (daily avg) | -0.111 [-0.930, +0.708] | 0.868 | 0.817 | 0.1051 | +1.9 | +62.3 | 0.0892 \| 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | 1271 | 408 | **+0.3559** | 0.1636 | [0.03526, 0.6765] | **2.18** | **0.030*** | * |
| MoCA total score ~ %<54 (pooled) | 1271 | 408 | +0.05016 | 0.1398 | [-0.2238, 0.3241] | 0.36 | 0.720 |  |
| MoCA total score ~ %<54 (daily avg) | 1271 | 265 | +0.07201 | 0.1679 | [-0.2571, 0.4011] | 0.43 | 0.668 |  |
| Cognitive impairment ~ Any <54 (0/1) | 1271 | 408 | **-0.2719** | 0.1365 | [-0.5395, -0.004358] | **-1.99** | **0.046*** | * |
| Cognitive impairment ~ %<54 (pooled) | 1271 | 408 | +0.03169 | 0.1063 | [-0.1767, 0.2401] | 0.30 | 0.766 |  |
| Cognitive impairment ~ %<54 (daily avg) | 1271 | 265 | +0.05371 | 0.1424 | [-0.2254, 0.3328] | 0.38 | 0.706 |  |
| MoCA memory index score ~ Any <54 (0/1) | 1271 | 408 | **+0.3472** | 0.1511 | [0.05112, 0.6433] | **2.30** | **0.022*** | * |
| MoCA memory index score ~ %<54 (pooled) | 1271 | 408 | +0.1869 | 0.2093 | [-0.2233, 0.5972] | 0.89 | 0.372 |  |
| MoCA memory index score ~ %<54 (daily avg) | 1271 | 265 | +0.1601 | 0.1796 | [-0.192, 0.5121] | 0.89 | 0.373 |  |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | 1270 | 408 | +0.07489 | 0.2896 | [-0.4926, 0.6424] | 0.26 | 0.796 |  |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | 1270 | 408 | -0.0907 | 0.2173 | [-0.5166, 0.3352] | -0.42 | 0.676 |  |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | 1270 | 265 | -0.01455 | 0.2485 | [-0.5017, 0.4726] | -0.06 | 0.953 |  |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | 1270 | 408 | +0.1616 | 0.1655 | [-0.1628, 0.486] | 0.98 | 0.329 |  |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | 1270 | 408 | -0.01248 | 0.1663 | [-0.3383, 0.3134] | -0.08 | 0.940 |  |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | 1270 | 265 | -0.1284 | 0.2593 | [-0.6366, 0.3797] | -0.50 | 0.620 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | 1251 | 400 | -0.007845 | 0.05637 | [-0.1183, 0.1026] | -0.14 | 0.889 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | 1251 | 400 | -0.0175 | 0.03162 | [-0.07947, 0.04447] | -0.55 | 0.580 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | 1251 | 260 | -0.02234 | 0.04295 | [-0.1065, 0.06184] | -0.52 | 0.603 |  |
| Indoor temperature, mean ~ Any <54 (0/1) | 1251 | 400 | -0.02802 | 0.1197 | [-0.2626, 0.2066] | -0.23 | 0.815 |  |
| Indoor temperature, mean ~ %<54 (pooled) | 1251 | 400 | +0.1995 | 0.1129 | [-0.02173, 0.4207] | 1.77 | 0.077 |  |
| Indoor temperature, mean ~ %<54 (daily avg) | 1251 | 260 | +0.2442 | 0.1802 | [-0.1089, 0.5974] | 1.36 | 0.175 |  |
| Indoor relative humidity, mean ~ Any <54 (0/1) | 1251 | 400 | -0.3568 | 0.3644 | [-1.071, 0.3573] | -0.98 | 0.327 |  |
| Indoor relative humidity, mean ~ %<54 (pooled) | 1251 | 400 | **-0.4995** | 0.1696 | [-0.832, -0.167] | **-2.94** | **0.003**** | ** |
| Indoor relative humidity, mean ~ %<54 (daily avg) | 1251 | 260 | **-0.7639** | 0.2373 | [-1.229, -0.2987] | **-3.22** | **0.001**** | ** |
| Indoor VOC index, mean ~ Any <54 (0/1) | 1251 | 400 | -1.036 | 0.9449 | [-2.888, 0.8159] | -1.10 | 0.273 |  |
| Indoor VOC index, mean ~ %<54 (pooled) | 1251 | 400 | -0.2529 | 0.6931 | [-1.611, 1.106] | -0.36 | 0.715 |  |
| Indoor VOC index, mean ~ %<54 (daily avg) | 1251 | 260 | -0.3362 | 0.99 | [-2.277, 1.604] | -0.34 | 0.734 |  |
| Steps per wear-day ~ Any <54 (0/1) | 1125 | 374 | -31.6 | 242.4 | [-506.7, 443.5] | -0.13 | 0.896 |  |
| Steps per wear-day ~ %<54 (pooled) | 1125 | 374 | -101.5 | 142.4 | [-380.7, 177.6] | -0.71 | 0.476 |  |
| Steps per wear-day ~ %<54 (daily avg) | 1125 | 241 | -64.17 | 225.6 | [-506.3, 378] | -0.28 | 0.776 |  |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | 1125 | 374 | +0.1846 | 0.7708 | [-1.326, 1.695] | 0.24 | 0.811 |  |
| Brisk-cadence minutes per day ~ %<54 (pooled) | 1125 | 374 | -0.1286 | 0.6136 | [-1.331, 1.074] | -0.21 | 0.834 |  |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | 1125 | 241 | -0.165 | 0.8196 | [-1.771, 1.441] | -0.20 | 0.840 |  |
| Resting heart-rate proxy ~ Any <54 (0/1) | 1128 | 373 | +0.4364 | 0.4846 | [-0.5135, 1.386] | 0.90 | 0.368 |  |
| Resting heart-rate proxy ~ %<54 (pooled) | 1128 | 373 | +0.2878 | 0.2594 | [-0.2207, 0.7963] | 1.11 | 0.267 |  |
| Resting heart-rate proxy ~ %<54 (daily avg) | 1128 | 240 | +0.2783 | 0.3599 | [-0.4271, 0.9838] | 0.77 | 0.439 |  |
| Total sleep time per night ~ Any <54 (0/1) | 1137 | 383 | +0.8253 | 4.176 | [-7.36, 9.011] | 0.20 | 0.843 |  |
| Total sleep time per night ~ %<54 (pooled) | 1137 | 383 | -2.641 | 1.958 | [-6.478, 1.197] | -1.35 | 0.177 |  |
| Total sleep time per night ~ %<54 (daily avg) | 1137 | 250 | -4.011 | 2.518 | [-8.946, 0.9242] | -1.59 | 0.111 |  |
| Garmin stress score, mean ~ Any <54 (0/1) | 1130 | 374 | +0.7802 | 1.076 | [-1.329, 2.889] | 0.73 | 0.468 |  |
| Garmin stress score, mean ~ %<54 (pooled) | 1130 | 374 | +0.0618 | 0.8855 | [-1.674, 1.797] | 0.07 | 0.944 |  |
| Garmin stress score, mean ~ %<54 (daily avg) | 1130 | 241 | -0.271 | 1.18 | [-2.584, 2.042] | -0.23 | 0.818 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | +0.166 [+0.016, +0.316] | 0.201 | 0.066 | 0.1005 | -2.6 | +11.1 | 0.0811 \| 0.0789 |
| MoCA total score ~ %<54 (pooled) | +0.029 [-0.127, +0.185] | 0.932 | 0.820 | 0.0973 | +1.9 | +15.6 | 0.0771 \| 0.0789 |
| MoCA total score ~ %<54 (daily avg) | +0.030 [-0.108, +0.169] | 0.932 | 0.820 | 0.0973 | +1.8 | +15.5 | 0.0774 \| 0.0789 |
| Cognitive impairment ~ Any <54 (0/1) | OR 0.881 [0.777, 0.998] | 0.280 | 0.479 | 0.6622 | -2.0 | -2.2 | 0.6460 \| 0.6443 |
| Cognitive impairment ~ %<54 (pooled) | OR 1.018 [0.904, 1.146] | 0.932 | 0.848 | 0.6604 | +1.9 | +1.7 | 0.6430 \| 0.6443 |
| Cognitive impairment ~ %<54 (daily avg) | OR 1.023 [0.909, 1.151] | 0.932 | 0.834 | 0.6603 | +1.9 | +1.6 | 0.6432 \| 0.6443 |
| MoCA memory index score ~ Any <54 (0/1) | +0.162 [+0.024, +0.300] | 0.158 | 0.051 | 0.0746 | -3.0 | -2.3 | 0.0490 \| 0.0477 |
| MoCA memory index score ~ %<54 (pooled) | +0.106 [-0.127, +0.340] | 0.771 | 0.462 | 0.0726 | -0.2 | +0.5 | 0.0446 \| 0.0477 |
| MoCA memory index score ~ %<54 (daily avg) | +0.067 [-0.081, +0.216] | 0.771 | 0.462 | 0.0716 | +1.1 | +1.8 | 0.0466 \| 0.0477 |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | +0.035 [-0.230, +0.300] | 0.939 | 0.953 | 0.0908 | +1.9 | -0.1 | 0.0662 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | -0.052 [-0.294, +0.191] | 0.932 | 0.953 | 0.0908 | +1.8 | -0.1 | 0.0655 \| 0.0675 |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | -0.006 [-0.212, +0.199] | 0.983 | 0.953 | 0.0907 | +2.0 | +0.0 | 0.0658 \| 0.0675 |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | OR 1.078 [0.927, 1.255] | 0.717 | 0.863 | 0.6927 | +1.1 | -0.1 | 0.6726 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | OR 0.993 [0.825, 1.195] | 0.981 | 0.958 | 0.6936 | +2.0 | +0.9 | 0.6744 \| 0.6758 |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | OR 0.947 [0.764, 1.174] | 0.932 | 0.958 | 0.6944 | +1.7 | +0.6 | 0.6760 \| 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | -0.004 [-0.055, +0.048] | 0.964 | 0.987 | 0.1361 | +2.0 | -0.0 | 0.1117 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | -0.010 [-0.046, +0.025] | 0.932 | 0.850 | 0.1362 | +1.8 | -0.2 | 0.1126 \| 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | -0.009 [-0.045, +0.026] | 0.932 | 0.850 | 0.1362 | +1.9 | -0.1 | 0.1129 \| 0.1139 |
| Indoor temperature, mean ~ Any <54 (0/1) | -0.013 [-0.123, +0.096] | 0.939 | 0.942 | 0.3097 | +1.9 | -0.0 | 0.2881 \| 0.2892 |
| Indoor temperature, mean ~ %<54 (pooled) | +0.114 [-0.012, +0.241] | 0.385 | 0.674 | 0.3122 | -2.5 | -4.5 | 0.2903 \| 0.2892 |
| Indoor temperature, mean ~ %<54 (daily avg) | +0.103 [-0.046, +0.253] | 0.532 | 0.776 | 0.3117 | -1.7 | -3.7 | 0.2891 \| 0.2892 |
| Indoor relative humidity, mean ~ Any <54 (0/1) | -0.166 [-0.500, +0.167] | 0.717 | 0.597 | 0.2602 | +1.0 | +1.5 | 0.2391 \| 0.2403 |
| Indoor relative humidity, mean ~ %<54 (pooled) | -0.286 [-0.477, -0.096] | 0.052 | 0.050 | 0.2613 | -1.0 | -0.5 | 0.2415 \| 0.2403 |
| Indoor relative humidity, mean ~ %<54 (daily avg) | **-0.324 [-0.521, -0.127]** | **0.036 (FDR<0.05)** | **0.040 (FDR<0.05)** | 0.2618 | -1.8 | -1.3 | 0.2417 \| 0.2403 |
| Indoor VOC index, mean ~ Any <54 (0/1) | -0.483 [-1.347, +0.381] | 0.648 | 0.564 | 0.0247 | +0.8 | +0.1 | 0.0026 \| 0.0025 |
| Indoor VOC index, mean ~ %<54 (pooled) | -0.145 [-0.923, +0.633] | 0.932 | 0.784 | 0.0238 | +1.9 | +1.3 | 0.0019 \| 0.0025 |
| Indoor VOC index, mean ~ %<54 (daily avg) | -0.142 [-0.964, +0.679] | 0.932 | 0.784 | 0.0238 | +1.9 | +1.3 | 0.0018 \| 0.0025 |
| Steps per wear-day ~ Any <54 (0/1) | -14.893 [-238.820, +209.035] | 0.964 | 0.958 | 0.1245 | +2.0 | +5.3 | 0.1064 \| 0.1080 |
| Steps per wear-day ~ %<54 (pooled) | -60.764 [-227.826, +106.297] | 0.872 | 0.958 | 0.1247 | +1.7 | +5.0 | 0.1077 \| 0.1080 |
| Steps per wear-day ~ %<54 (daily avg) | -28.610 [-225.739, +168.519] | 0.932 | 0.958 | 0.1245 | +1.9 | +5.2 | 0.1073 \| 0.1080 |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | +0.087 [-0.625, +0.799] | 0.939 | 0.931 | 0.1387 | +1.9 | +5.4 | 0.1229 \| 0.1245 |
| Brisk-cadence minutes per day ~ %<54 (pooled) | -0.077 [-0.797, +0.643] | 0.945 | 0.931 | 0.1387 | +2.0 | +5.4 | 0.1237 \| 0.1245 |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | -0.074 [-0.790, +0.643] | 0.946 | 0.931 | 0.1387 | +2.0 | +5.4 | 0.1234 \| 0.1245 |
| Resting heart-rate proxy ~ Any <54 (0/1) | +0.205 [-0.242, +0.652] | 0.771 | 0.439 | 0.1302 | +1.2 | +12.4 | 0.1038 \| 0.1044 |
| Resting heart-rate proxy ~ %<54 (pooled) | +0.172 [-0.132, +0.476] | 0.645 | 0.345 | 0.1300 | +1.4 | +12.6 | 0.1044 \| 0.1044 |
| Resting heart-rate proxy ~ %<54 (daily avg) | +0.124 [-0.190, +0.438] | 0.851 | 0.504 | 0.1298 | +1.7 | +12.9 | 0.1035 \| 0.1044 |
| Total sleep time per night ~ Any <54 (0/1) | +0.390 [-3.480, +4.261] | 0.946 | 0.936 | 0.0205 | +2.0 | +4.0 | -0.0064 \| -0.0051 |
| Total sleep time per night ~ %<54 (pooled) | -1.573 [-3.859, +0.713] | 0.532 | 0.936 | 0.0211 | +1.4 | +3.4 | -0.0051 \| -0.0051 |
| Total sleep time per night ~ %<54 (daily avg) | -1.782 [-3.975, +0.411] | 0.441 | 0.936 | 0.0212 | +1.2 | +3.2 | -0.0048 \| -0.0051 |
| Garmin stress score, mean ~ Any <54 (0/1) | +0.367 [-0.625, +1.360] | 0.871 | 0.708 | 0.0730 | +1.5 | +9.2 | 0.0500 \| 0.0510 |
| Garmin stress score, mean ~ %<54 (pooled) | +0.037 [-0.999, +1.073] | 0.981 | 0.965 | 0.0726 | +2.0 | +9.8 | 0.0496 \| 0.0510 |
| Garmin stress score, mean ~ %<54 (daily avg) | -0.121 [-1.150, +0.909] | 0.939 | 0.920 | 0.0726 | +1.9 | +9.7 | 0.0494 \| 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**

| Predictor (alone) | N | N with time in band | Coef (β) | Std. Err. | 95% CI | t / z | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | 867 | 230 | +0.1107 | 0.2623 | [-0.4035, 0.6249] | 0.42 | 0.673 |  |
| MoCA total score ~ %<54 (pooled) | 867 | 230 | +0.05366 | 0.4076 | [-0.7452, 0.8525] | 0.13 | 0.895 |  |
| MoCA total score ~ %<54 (daily avg) | 867 | 155 | +0.001075 | 0.3139 | [-0.6141, 0.6162] | 0.00 | 0.997 |  |
| Cognitive impairment ~ Any <54 (0/1) | 867 | 230 | -0.1236 | 0.1634 | [-0.4439, 0.1967] | -0.76 | 0.450 |  |
| Cognitive impairment ~ %<54 (pooled) | 867 | 230 | +0.01863 | 0.1678 | [-0.3102, 0.3474] | 0.11 | 0.912 |  |
| Cognitive impairment ~ %<54 (daily avg) | 867 | 155 | +0.06254 | 0.1618 | [-0.2546, 0.3797] | 0.39 | 0.699 |  |
| MoCA memory index score ~ Any <54 (0/1) | 867 | 230 | -0.06479 | 0.2103 | [-0.4769, 0.3473] | -0.31 | 0.758 |  |
| MoCA memory index score ~ %<54 (pooled) | 867 | 230 | -0.1426 | 0.1558 | [-0.448, 0.1629] | -0.91 | 0.360 |  |
| MoCA memory index score ~ %<54 (daily avg) | 867 | 155 | -0.2345 | 0.1777 | [-0.5828, 0.1137] | -1.32 | 0.187 |  |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | 865 | 229 | +0.2767 | 0.3737 | [-0.4558, 1.009] | 0.74 | 0.459 |  |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | 865 | 229 | -0.1166 | 0.4534 | [-1.005, 0.7721] | -0.26 | 0.797 |  |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | 865 | 154 | -0.01904 | 0.5949 | [-1.185, 1.147] | -0.03 | 0.974 |  |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | 865 | 229 | +0.1029 | 0.1923 | [-0.2741, 0.4798] | 0.53 | 0.593 |  |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | 865 | 229 | -0.1044 | 0.2218 | [-0.539, 0.3303] | -0.47 | 0.638 |  |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | 865 | 154 | +0.02887 | 0.1779 | [-0.3198, 0.3776] | 0.16 | 0.871 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | 849 | 228 | +0.1365 | 0.07856 | [-0.0175, 0.2904] | 1.74 | 0.082 |  |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | 849 | 228 | **+0.2665** | 0.0959 | [0.07851, 0.4544] | **2.78** | **0.005**** | ** |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | 849 | 155 | +0.2695 | 0.1462 | [-0.01697, 0.556] | 1.84 | 0.065 |  |
| Indoor temperature, mean ~ Any <54 (0/1) | 849 | 228 | -0.08461 | 0.1658 | [-0.4096, 0.2404] | -0.51 | 0.610 |  |
| Indoor temperature, mean ~ %<54 (pooled) | 849 | 228 | +0.04314 | 0.1788 | [-0.3073, 0.3936] | 0.24 | 0.809 |  |
| Indoor temperature, mean ~ %<54 (daily avg) | 849 | 155 | +0.05869 | 0.1998 | [-0.3329, 0.4503] | 0.29 | 0.769 |  |
| Indoor relative humidity, mean ~ Any <54 (0/1) | 849 | 228 | -0.1076 | 0.5046 | [-1.097, 0.8815] | -0.21 | 0.831 |  |
| Indoor relative humidity, mean ~ %<54 (pooled) | 849 | 228 | -0.2766 | 0.7618 | [-1.77, 1.217] | -0.36 | 0.717 |  |
| Indoor relative humidity, mean ~ %<54 (daily avg) | 849 | 155 | -0.3747 | 0.6872 | [-1.722, 0.9721] | -0.55 | 0.586 |  |
| Indoor VOC index, mean ~ Any <54 (0/1) | 849 | 228 | -0.3089 | 1.44 | [-3.131, 2.513] | -0.21 | 0.830 |  |
| Indoor VOC index, mean ~ %<54 (pooled) | 849 | 228 | +0.8004 | 0.9856 | [-1.131, 2.732] | 0.81 | 0.417 |  |
| Indoor VOC index, mean ~ %<54 (daily avg) | 849 | 155 | +1.276 | 1.045 | [-0.773, 3.325] | 1.22 | 0.222 |  |
| Steps per wear-day ~ Any <54 (0/1) | 747 | 201 | **-1131** | 403.6 | [-1922, -340.2] | **-2.80** | **0.005**** | ** |
| Steps per wear-day ~ %<54 (pooled) | 747 | 201 | -909.1 | 530 | [-1948, 129.6] | -1.72 | 0.086 |  |
| Steps per wear-day ~ %<54 (daily avg) | 747 | 132 | **-825** | 327.4 | [-1467, -183.3] | **-2.52** | **0.012*** | * |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | 747 | 201 | **-2.4** | 1.155 | [-4.665, -0.1356] | **-2.08** | **0.038*** | * |
| Brisk-cadence minutes per day ~ %<54 (pooled) | 747 | 201 | -2.009 | 1.714 | [-5.367, 1.35] | -1.17 | 0.241 |  |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | 747 | 132 | -1.918 | 1.276 | [-4.419, 0.584] | -1.50 | 0.133 |  |
| Resting heart-rate proxy ~ Any <54 (0/1) | 749 | 203 | -0.127 | 0.6844 | [-1.468, 1.215] | -0.19 | 0.853 |  |
| Resting heart-rate proxy ~ %<54 (pooled) | 749 | 203 | +0.4269 | 0.631 | [-0.8097, 1.664] | 0.68 | 0.499 |  |
| Resting heart-rate proxy ~ %<54 (daily avg) | 749 | 134 | -0.05779 | 1.038 | [-2.091, 1.976] | -0.06 | 0.956 |  |
| Total sleep time per night ~ Any <54 (0/1) | 756 | 205 | +6.788 | 5.753 | [-4.487, 18.06] | 1.18 | 0.238 |  |
| Total sleep time per night ~ %<54 (pooled) | 756 | 205 | **+9.374** | 4.617 | [0.3248, 18.42] | **2.03** | **0.042*** | * |
| Total sleep time per night ~ %<54 (daily avg) | 756 | 138 | +6.407 | 3.821 | [-1.082, 13.9] | 1.68 | 0.094 |  |
| Garmin stress score, mean ~ Any <54 (0/1) | 749 | 203 | -1.39 | 1.466 | [-4.263, 1.483] | -0.95 | 0.343 |  |
| Garmin stress score, mean ~ %<54 (pooled) | 749 | 203 | +0.8143 | 1.373 | [-1.877, 3.505] | 0.59 | 0.553 |  |
| Garmin stress score, mean ~ %<54 (daily avg) | 749 | 134 | +0.08406 | 1.928 | [-3.695, 3.863] | 0.04 | 0.965 |  |

**(B) Standardised effect, multiplicity and fit**

| Predictor (alone) | β per 1 SD (95% CI) | q, all tests in population | q, this outcome | Adj R² / AUC | ΔAIC vs covs | ΔAIC vs HbA1c | CV R²/AUC (predictor vs covariates-only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score ~ Any <54 (0/1) | +0.049 [-0.178, +0.276] | 0.814 | 0.835 | 0.0810 | +1.8 | +3.3 | 0.0515 \| 0.0541 |
| MoCA total score ~ %<54 (pooled) | +0.023 [-0.313, +0.358] | 0.932 | 0.997 | 0.0809 | +2.0 | +3.5 | 0.0494 \| 0.0541 |
| MoCA total score ~ %<54 (daily avg) | +0.000 [-0.269, +0.269] | 0.997 | 0.997 | 0.0808 | +2.0 | +3.5 | 0.0502 \| 0.0541 |
| Cognitive impairment ~ Any <54 (0/1) | OR 0.947 [0.822, 1.091] | 0.656 | 0.557 | 0.6621 | +1.4 | +3.1 | 0.6412 \| 0.6425 |
| Cognitive impairment ~ %<54 (pooled) | OR 1.008 [0.878, 1.157] | 0.943 | 0.912 | 0.6601 | +2.0 | +3.7 | 0.6398 \| 0.6425 |
| Cognitive impairment ~ %<54 (daily avg) | OR 1.028 [0.895, 1.181] | 0.829 | 0.722 | 0.6607 | +1.8 | +3.5 | 0.6402 \| 0.6425 |
| MoCA memory index score ~ Any <54 (0/1) | -0.029 [-0.211, +0.153] | 0.854 | 0.758 | 0.0598 | +1.9 | +3.7 | 0.0271 \| 0.0286 |
| MoCA memory index score ~ %<54 (pooled) | -0.060 [-0.188, +0.068] | 0.579 | 0.372 | 0.0601 | +1.6 | +3.4 | 0.0281 \| 0.0286 |
| MoCA memory index score ~ %<54 (daily avg) | -0.103 [-0.255, +0.050] | 0.382 | 0.200 | 0.0610 | +0.8 | +2.5 | 0.0292 \| 0.0286 |
| CES-D-10 depressive symptoms ~ Any <54 (0/1) | +0.122 [-0.201, +0.446] | 0.656 | 0.593 | 0.1116 | +1.5 | +2.8 | 0.0779 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %<54 (pooled) | -0.049 [-0.423, +0.325] | 0.874 | 0.875 | 0.1111 | +1.9 | +3.2 | 0.0780 \| 0.0796 |
| CES-D-10 depressive symptoms ~ %<54 (daily avg) | -0.008 [-0.519, +0.502] | 0.979 | 0.974 | 0.1111 | +2.0 | +3.3 | 0.0755 \| 0.0796 |
| Clinically relevant depressive symptoms ~ Any <54 (0/1) | OR 1.046 [0.886, 1.236] | 0.770 | 0.799 | 0.6612 | +1.7 | +4.7 | 0.6306 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %<54 (pooled) | OR 0.957 [0.797, 1.149] | 0.800 | 0.824 | 0.6597 | +1.8 | +4.8 | 0.6294 \| 0.6337 |
| Clinically relevant depressive symptoms ~ %<54 (daily avg) | OR 1.013 [0.869, 1.180] | 0.916 | 0.901 | 0.6605 | +2.0 | +5.0 | 0.6290 \| 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ Any <54 (0/1) | +0.061 [-0.008, +0.129] | 0.243 | 0.172 | 0.1575 | -1.6 | +7.8 | 0.1324 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (pooled) | +0.113 [+0.033, +0.193] | 0.054 | **0.034 (FDR<0.05)** | 0.1664 | -10.6 | -1.2 | 0.1385 \| 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) ~ %<54 (daily avg) | +0.119 [-0.007, +0.246] | 0.222 | 0.158 | 0.1679 | -12.1 | -2.7 | 0.1309 \| 0.1310 |
| Indoor temperature, mean ~ Any <54 (0/1) | -0.038 [-0.182, +0.107] | 0.783 | 0.907 | 0.2504 | +1.7 | +0.1 | 0.2238 \| 0.2264 |
| Indoor temperature, mean ~ %<54 (pooled) | +0.018 [-0.130, +0.167] | 0.883 | 0.907 | 0.2502 | +1.9 | +0.2 | 0.2243 \| 0.2264 |
| Indoor temperature, mean ~ %<54 (daily avg) | +0.026 [-0.147, +0.199] | 0.860 | 0.907 | 0.2503 | +1.9 | +0.2 | 0.2230 \| 0.2264 |
| Indoor relative humidity, mean ~ Any <54 (0/1) | -0.048 [-0.486, +0.391] | 0.891 | 0.938 | 0.2130 | +2.0 | +0.1 | 0.1833 \| 0.1857 |
| Indoor relative humidity, mean ~ %<54 (pooled) | -0.117 [-0.751, +0.516] | 0.833 | 0.938 | 0.2132 | +1.7 | -0.2 | 0.1824 \| 0.1857 |
| Indoor relative humidity, mean ~ %<54 (daily avg) | -0.166 [-0.761, +0.429] | 0.763 | 0.938 | 0.2135 | +1.4 | -0.5 | 0.1805 \| 0.1857 |
| Indoor VOC index, mean ~ Any <54 (0/1) | -0.137 [-1.388, +1.114] | 0.891 | 0.858 | 0.0557 | +1.9 | +2.3 | 0.0255 \| 0.0276 |
| Indoor VOC index, mean ~ %<54 (pooled) | +0.339 [-0.480, +1.159] | 0.634 | 0.585 | 0.0560 | +1.7 | +2.0 | 0.0274 \| 0.0276 |
| Indoor VOC index, mean ~ %<54 (daily avg) | +0.564 [-0.341, +1.469] | 0.433 | 0.585 | 0.0566 | +1.1 | +1.4 | 0.0268 \| 0.0276 |
| Steps per wear-day ~ Any <54 (0/1) | -502.034 [-853.109, -150.960] | 0.052 | **0.039 (FDR<0.05)** | 0.1659 | -5.9 | -5.8 | 0.1442 \| 0.1390 |
| Steps per wear-day ~ %<54 (pooled) | -407.095 [-872.220, +58.030] | 0.247 | 0.315 | 0.1629 | -3.2 | -3.1 | 0.1400 \| 0.1390 |
| Steps per wear-day ~ %<54 (daily avg) | -386.633 [-687.348, -85.917] | 0.091 | 0.061 | 0.1624 | -2.8 | -2.7 | 0.1427 \| 0.1390 |
| Brisk-cadence minutes per day ~ Any <54 (0/1) | -1.065 [-2.070, -0.060] | 0.169 | 0.380 | 0.1836 | -2.3 | -2.3 | 0.1559 \| 0.1546 |
| Brisk-cadence minutes per day ~ %<54 (pooled) | -0.900 [-2.403, +0.604] | 0.455 | 0.663 | 0.1823 | -1.1 | -1.1 | 0.1530 \| 0.1546 |
| Brisk-cadence minutes per day ~ %<54 (daily avg) | -0.899 [-2.071, +0.274] | 0.307 | 0.589 | 0.1823 | -1.1 | -1.1 | 0.1554 \| 0.1546 |
| Resting heart-rate proxy ~ Any <54 (0/1) | -0.056 [-0.653, +0.540] | 0.903 | 0.881 | 0.1523 | +2.0 | +8.0 | 0.1220 \| 0.1253 |
| Resting heart-rate proxy ~ %<54 (pooled) | +0.191 [-0.362, +0.744] | 0.689 | 0.618 | 0.1527 | +1.6 | +7.7 | 0.1239 \| 0.1253 |
| Resting heart-rate proxy ~ %<54 (daily avg) | -0.027 [-0.979, +0.925] | 0.968 | 0.956 | 0.1523 | +2.0 | +8.1 | 0.1219 \| 0.1253 |
| Total sleep time per night ~ Any <54 (0/1) | +3.020 [-1.996, +8.036] | 0.453 | 0.444 | 0.0382 | +0.6 | +3.5 | 0.0046 \| 0.0066 |
| Total sleep time per night ~ %<54 (pooled) | +4.193 [+0.145, +8.240] | 0.182 | 0.219 | 0.0399 | -0.8 | +2.1 | 0.0094 \| 0.0066 |
| Total sleep time per night ~ %<54 (daily avg) | +2.990 [-0.505, +6.485] | 0.257 | 0.290 | 0.0381 | +0.6 | +3.5 | 0.0070 \| 0.0066 |
| Garmin stress score, mean ~ Any <54 (0/1) | -0.618 [-1.896, +0.660] | 0.566 | 0.443 | 0.1229 | +1.1 | +14.2 | 0.0931 \| 0.0947 |
| Garmin stress score, mean ~ %<54 (pooled) | +0.364 [-0.839, +1.568] | 0.734 | 0.612 | 0.1222 | +1.7 | +14.8 | 0.0936 \| 0.0947 |
| Garmin stress score, mean ~ %<54 (daily avg) | +0.039 [-1.729, +1.808] | 0.972 | 0.965 | 0.1218 | +2.0 | +15.1 | 0.0921 \| 0.0947 |


---

# Interpretation of the band analyses


## Interpretation - band 70-180 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 84 single-predictor tests; 28 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 84 tests (samples with n >= 500), of which **14** are significant at BH q < 0.05 in the all-tests family and 20 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.102 vs 0.092 for covariates alone, gain +0.011; +0.356 per SD, p = 2.3e-06, q = 2.3e-05). FDR-robust associations (2): TIR 70-180 (pooled) (higher outcome, +0.356 per SD, q = 2.3e-05); TIR 70-180 (daily avg) (higher outcome, +0.35 per SD, q = 3.4e-05).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **TIR 70-180 (pooled)** (CV AUC 0.666 vs 0.660 for covariates alone, gain +0.005; OR 0.83 per SD, p = 6.4e-05, q = 4.2e-04). FDR-robust associations (2): TIR 70-180 (pooled) (lower outcome, OR 0.83 per SD, q = 4.2e-04); TIR 70-180 (daily avg) (lower outcome, OR 0.83 per SD, q = 4.7e-04).
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.031 vs 0.029 for covariates alone, gain +0.003; +0.173 per SD, p = 0.055, q = 0.204). FDR-robust associations (2): TIR 70-180 (pooled) (higher outcome, +0.167 per SD, q = 0.017); TIR 70-180 (daily avg) (higher outcome, +0.167 per SD, q = 0.017).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.092 vs 0.092 for covariates alone, gain +0.000; -0.144 per SD, p = 0.231, q = 0.400). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **TIR 70-180 (daily avg)** (CV AUC 0.636 vs 0.634 for covariates alone, gain +0.002; OR 0.87 per SD, p = 0.099, q = 0.264). No association survives FDR; nominal only: TIR 70-180 (pooled) (p = 0.038), TIR 70-180 (daily avg) (p = 0.047).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.133 vs 0.131 for covariates alone, gain +0.002; -0.0749 per SD, p = 0.043, q = 0.182). No association survives FDR; nominal only: TIR 70-180 (pooled) (p = 0.043), TIR 70-180 (daily avg) (p = 0.043). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **TIR 70-180 (daily avg)** (CV R² 0.289 vs 0.289 for covariates alone, gain -0.000; -0.0479 per SD, p = 0.392, q = 0.794). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.230 vs 0.231 for covariates alone, gain -0.001; +0.0682 per SD, p = 0.632, q = 0.781). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **TIR 70-180 (daily avg)** (CV R² 0.027 vs 0.028 for covariates alone, gain -0.001; +0.505 per SD, p = 0.455, q = 0.656). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.122 vs 0.122 for covariates alone, gain -0.001; -125 per SD, p = 0.339, q = 0.500). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.144 vs 0.145 for covariates alone, gain -0.000; -0.401 per SD, p = 0.280, q = 0.447). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.181 vs 0.148 for covariates alone, gain +0.032; -1.68 per SD, p = 1.1e-14, q = 6.3e-13). FDR-robust associations (4): TIR 70-180 (pooled) (lower outcome, -1.68 per SD, q = 6.3e-13); TIR 70-180 (daily avg) (lower outcome, -1.67 per SD, q = 7.4e-13); TIR 70-180 (pooled) (lower outcome, -1.07 per SD, q = 0.024); TIR 70-180 (daily avg) (lower outcome, -1.06 per SD, q = 0.024).
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.020 vs 0.021 for covariates alone, gain -0.001; +1.92 per SD, p = 0.234, q = 0.400). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.114 vs 0.090 for covariates alone, gain +0.024; -3 per SD, p = 2.1e-11, q = 4.6e-10). FDR-robust associations (4): TIR 70-180 (pooled) (lower outcome, -3 per SD, q = 4.6e-10); TIR 70-180 (daily avg) (lower outcome, -2.96 per SD, q = 7.1e-10); TIR 70-180 (pooled) (lower outcome, -2.61 per SD, q = 0.007); TIR 70-180 (daily avg) (lower outcome, -2.59 per SD, q = 0.007).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Resting heart-rate proxy (daily 5th pct, bpm) (+0.032, via TIR 70-180 (pooled)); Garmin stress score, mean (0-100) (+0.024, via TIR 70-180 (pooled)); MoCA total score (0-30) (+0.011, via TIR 70-180 (pooled)); Cognitive impairment (MoCA < 26) (+0.005, via TIR 70-180 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Range 70-180 (14 FDR-significant / 28 raw-significant of 84).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band 54-69 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 84 single-predictor tests; 7 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 84 tests (samples with n >= 500), of which **1** are significant at BH q < 0.05 in the all-tests family and 4 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.078 vs 0.079 for covariates alone, gain -0.001; +0.0161 per SD, p = 0.791, q = 0.936). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **%54-69 (daily avg)** (CV AUC 0.660 vs 0.660 for covariates alone, gain +0.000; OR 1.06 per SD, p = 0.236, q = 0.401). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.031 vs 0.029 for covariates alone, gain +0.002; -0.16 per SD, p = 0.073, q = 0.232). No glycaemic measure is associated with this outcome (all p > 0.05).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.091 vs 0.092 for covariates alone, gain -0.000; +0.0985 per SD, p = 0.337, q = 0.500). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%54-69 (daily avg)** (CV AUC 0.667 vs 0.668 for covariates alone, gain -0.001; OR 1.03 per SD, p = 0.561, q = 0.718). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.143 vs 0.131 for covariates alone, gain +0.012; +0.135 per SD, p = 0.007, q = 0.061). No association survives FDR; nominal only: %54-69 (pooled) (p = 0.006), %54-69 (daily avg) (p = 0.007).
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.290 vs 0.290 for covariates alone, gain +0.000; +0.0687 per SD, p = 0.085, q = 0.195). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.230 vs 0.231 for covariates alone, gain -0.000; -0.156 per SD, p = 0.238, q = 0.404). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%54-69 (pooled)** (CV R² 0.027 vs 0.028 for covariates alone, gain -0.001; +0.548 per SD, p = 0.311, q = 0.533). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.143 vs 0.139 for covariates alone, gain +0.004; -401 per SD, p = 0.004, q = 0.043). FDR-robust associations (1): %54-69 (daily avg) (lower outcome, -401 per SD, q = 0.043).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.156 vs 0.155 for covariates alone, gain +0.001; -0.806 per SD, p = 0.047, q = 0.189). No association survives FDR; nominal only: %54-69 (daily avg) (p = 0.047). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.148 vs 0.148 for covariates alone, gain -0.000; -0.181 per SD, p = 0.309, q = 0.482). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%54-69 (pooled)** (CV R² 0.020 vs 0.021 for covariates alone, gain -0.000; +1.45 per SD, p = 0.305, q = 0.480). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%54-69 (pooled)** (CV R² 0.090 vs 0.090 for covariates alone, gain -0.000; -0.521 per SD, p = 0.212, q = 0.378). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.012, via %54-69 (daily avg)); Steps per wear-day (+0.004, via %54-69 (daily avg)); MoCA memory index score (0-15) (+0.002, via %54-69 (daily avg)); Brisk-cadence minutes per day (>= 100 steps/min) (+0.001, via %54-69 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 54-69 (1 FDR-significant / 7 raw-significant of 84).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band <70 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 84 single-predictor tests; 8 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 84 tests (samples with n >= 500), of which **5** are significant at BH q < 0.05 in the all-tests family and 4 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.078 vs 0.079 for covariates alone, gain -0.001; +0.0212 per SD, p = 0.736, q = 0.932). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **%<70 (pooled)** (CV AUC 0.644 vs 0.644 for covariates alone, gain +0.000; OR 1.07 per SD, p = 0.280, q = 0.654). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.031 vs 0.029 for covariates alone, gain +0.002; -0.157 per SD, p = 0.066, q = 0.222). No association survives FDR; nominal only: %<70 (pooled) (p = 0.027).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.091 vs 0.092 for covariates alone, gain -0.001; +0.0797 per SD, p = 0.441, q = 0.611). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%<70 (daily avg)** (CV AUC 0.667 vs 0.668 for covariates alone, gain -0.001; OR 1.02 per SD, p = 0.665, q = 0.803). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.144 vs 0.131 for covariates alone, gain +0.013; +0.14 per SD, p = 0.004, q = 0.047). FDR-robust associations (2): %<70 (pooled) (higher outcome, +0.137 per SD, q = 0.040); %<70 (daily avg) (higher outcome, +0.14 per SD, q = 0.047).
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.290 vs 0.289 for covariates alone, gain +0.000; +0.0863 per SD, p = 0.085, q = 0.404). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.240 vs 0.240 for covariates alone, gain -0.000; -0.256 per SD, p = 0.073, q = 0.367). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.027 vs 0.028 for covariates alone, gain -0.000; +0.541 per SD, p = 0.267, q = 0.483). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.144 vs 0.139 for covariates alone, gain +0.005; -424 per SD, p = 0.001, q = 0.024). FDR-robust associations (3): %<70 (daily avg) (lower outcome, -424 per SD, q = 0.024); %<70 (pooled) (lower outcome, -231 per SD, q = 0.033); %<70 (daily avg) (lower outcome, -230 per SD, q = 0.035).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.156 vs 0.155 for covariates alone, gain +0.001; -0.881 per SD, p = 0.033, q = 0.165). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.033). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.148 vs 0.148 for covariates alone, gain -0.000; -0.144 per SD, p = 0.422, q = 0.595). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.021 vs 0.021 for covariates alone, gain -0.000; +1.23 per SD, p = 0.364, q = 0.528). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.090 vs 0.090 for covariates alone, gain -0.000; -0.417 per SD, p = 0.311, q = 0.482). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.013, via %<70 (daily avg)); Steps per wear-day (+0.005, via %<70 (daily avg)); MoCA memory index score (0-15) (+0.002, via %<70 (daily avg)); Brisk-cadence minutes per day (>= 100 steps/min) (+0.001, via %<70 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band < 70 (5 FDR-significant / 8 raw-significant of 84).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band 54-250 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 84 single-predictor tests; 16 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 84 tests (samples with n >= 500), of which **8** are significant at BH q < 0.05 in the all-tests family and 12 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.097 vs 0.092 for covariates alone, gain +0.006; +0.268 per SD, p = 8.2e-04, q = 0.004). FDR-robust associations (2): %54-250 (pooled) (higher outcome, +0.268 per SD, q = 0.004); %54-250 (daily avg) (higher outcome, +0.265 per SD, q = 0.006).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **%54-250 (pooled)** (CV AUC 0.663 vs 0.660 for covariates alone, gain +0.003; OR 0.87 per SD, p = 0.004, q = 0.017). FDR-robust associations (2): %54-250 (pooled) (lower outcome, OR 0.87 per SD, q = 0.017); %54-250 (daily avg) (lower outcome, OR 0.87 per SD, q = 0.020).
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.051 vs 0.048 for covariates alone, gain +0.003; +0.173 per SD, p = 0.005, q = 0.068). No association survives FDR; nominal only: %54-250 (daily avg) (p = 0.005), %54-250 (pooled) (p = 0.007), %54-250 (pooled) (p = 0.028), %54-250 (daily avg) (p = 0.032).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.092 vs 0.092 for covariates alone, gain -0.000; -0.144 per SD, p = 0.278, q = 0.445). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%54-250 (pooled)** (CV AUC 0.637 vs 0.634 for covariates alone, gain +0.003; OR 0.89 per SD, p = 0.111, q = 0.270). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.139 vs 0.139 for covariates alone, gain +0.001; -0.043 per SD, p = 0.097, q = 0.210). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.289 vs 0.290 for covariates alone, gain -0.001; -0.0244 per SD, p = 0.625, q = 0.778). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.240 vs 0.240 for covariates alone, gain -0.000; -0.147 per SD, p = 0.252, q = 0.629). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.029 vs 0.028 for covariates alone, gain +0.002; +1.16 per SD, p = 0.089, q = 0.247). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.107 vs 0.108 for covariates alone, gain -0.001; -82.1 per SD, p = 0.488, q = 0.884). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.125 vs 0.124 for covariates alone, gain +0.000; -0.404 per SD, p = 0.342, q = 0.734). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.160 vs 0.148 for covariates alone, gain +0.011; -1.01 per SD, p = 9.8e-06, q = 8.0e-05). FDR-robust associations (2): %54-250 (pooled) (lower outcome, -1.01 per SD, q = 8.0e-05); %54-250 (daily avg) (lower outcome, -1 per SD, q = 1.1e-04).
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.021 vs 0.021 for covariates alone, gain -0.000; +1.04 per SD, p = 0.488, q = 0.656). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%54-250 (pooled)** (CV R² 0.100 vs 0.090 for covariates alone, gain +0.010; -1.93 per SD, p = 1.1e-04, q = 6.5e-04). FDR-robust associations (2): %54-250 (pooled) (lower outcome, -1.93 per SD, q = 6.5e-04); %54-250 (daily avg) (lower outcome, -1.92 per SD, q = 8.0e-04).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Resting heart-rate proxy (daily 5th pct, bpm) (+0.011, via %54-250 (pooled)); Garmin stress score, mean (0-100) (+0.010, via %54-250 (pooled)); MoCA total score (0-30) (+0.006, via %54-250 (pooled)); MoCA memory index score (0-15) (+0.003, via %54-250 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 54-250 (8 FDR-significant / 16 raw-significant of 84).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band >180 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 126 single-predictor tests; 40 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 126 tests (samples with n >= 500), of which **22** are significant at BH q < 0.05 in the all-tests family and 29 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.102 vs 0.092 for covariates alone, gain +0.011; -0.355 per SD, p = 2.4e-06, q = 2.4e-05). FDR-robust associations (3): %>180 (pooled) (lower outcome, -0.355 per SD, q = 2.4e-05); %>180 (daily avg) (lower outcome, -0.349 per SD, q = 3.7e-05); %>180 nocturnal (lower outcome, -0.317 per SD, q = 2.3e-04).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **%>180 (pooled)** (CV AUC 0.665 vs 0.660 for covariates alone, gain +0.005; OR 1.20 per SD, p = 9.9e-05, q = 6.1e-04). FDR-robust associations (3): %>180 (pooled) (higher outcome, OR 1.20 per SD, q = 6.1e-04); %>180 (daily avg) (higher outcome, OR 1.20 per SD, q = 7.0e-04); %>180 nocturnal (higher outcome, OR 1.17 per SD, q = 0.005).
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.050 vs 0.048 for covariates alone, gain +0.003; -0.193 per SD, p = 0.005, q = 0.068). FDR-robust associations (3): %>180 (pooled) (lower outcome, -0.167 per SD, q = 0.017); %>180 (daily avg) (lower outcome, -0.164 per SD, q = 0.020); %>180 nocturnal (lower outcome, -0.154 per SD, q = 0.029).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.093 vs 0.092 for covariates alone, gain +0.001; +0.222 per SD, p = 0.069, q = 0.172). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%>180 nocturnal** (CV AUC 0.641 vs 0.634 for covariates alone, gain +0.007; OR 1.22 per SD, p = 0.014, q = 0.100). FDR-robust associations (1): %>180 nocturnal (higher outcome, OR 1.17 per SD, q = 0.012).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.132 vs 0.131 for covariates alone, gain +0.001; +0.0731 per SD, p = 0.051, q = 0.198). No association survives FDR; nominal only: %>180 nocturnal (p = 0.048). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.289 vs 0.289 for covariates alone, gain -0.001; +0.0458 per SD, p = 0.445, q = 0.852). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.185 vs 0.186 for covariates alone, gain -0.000; -0.256 per SD, p = 0.262, q = 0.481). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%>180 (daily avg)** (CV R² 0.027 vs 0.028 for covariates alone, gain -0.001; -0.539 per SD, p = 0.425, q = 0.640). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.122 vs 0.122 for covariates alone, gain -0.000; +147 per SD, p = 0.263, q = 0.438). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.145 vs 0.145 for covariates alone, gain -0.000; +0.443 per SD, p = 0.232, q = 0.400). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.180 vs 0.148 for covariates alone, gain +0.032; +1.67 per SD, p = 1.2e-14, q = 6.3e-13). FDR-robust associations (6): %>180 (pooled) (higher outcome, +1.67 per SD, q = 6.3e-13); %>180 (daily avg) (higher outcome, +1.67 per SD, q = 6.8e-13); %>180 nocturnal (higher outcome, +1.37 per SD, q = 5.5e-09); %>180 (daily avg) (higher outcome, +1.07 per SD, q = 0.024); %>180 (pooled) (higher outcome, +1.07 per SD, q = 0.024); %>180 nocturnal (higher outcome, +0.947 per SD, q = 0.046).
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.020 vs 0.021 for covariates alone, gain -0.001; -2.02 per SD, p = 0.211, q = 0.376). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.114 vs 0.090 for covariates alone, gain +0.024; +3.01 per SD, p = 1.7e-11, q = 3.8e-10). FDR-robust associations (6): %>180 (pooled) (higher outcome, +3.01 per SD, q = 3.8e-10); %>180 (daily avg) (higher outcome, +2.98 per SD, q = 4.8e-10); %>180 nocturnal (higher outcome, +2.42 per SD, q = 6.4e-07); %>180 (pooled) (higher outcome, +2.61 per SD, q = 0.007); %>180 (daily avg) (higher outcome, +2.6 per SD, q = 0.007); %>180 nocturnal (higher outcome, +2.25 per SD, q = 0.022).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Resting heart-rate proxy (daily 5th pct, bpm) (+0.032, via %>180 (pooled)); Garmin stress score, mean (0-100) (+0.024, via %>180 (pooled)); MoCA total score (0-30) (+0.011, via %>180 (pooled)); Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.007, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 180 (22 FDR-significant / 40 raw-significant of 126).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band 181-250 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 84 single-predictor tests; 19 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 84 tests (samples with n >= 500), of which **14** are significant at BH q < 0.05 in the all-tests family and 18 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.100 vs 0.092 for covariates alone, gain +0.009; -0.321 per SD, p = 1.4e-05, q = 1.1e-04). FDR-robust associations (2): %181-250 (pooled) (lower outcome, -0.321 per SD, q = 1.1e-04); %181-250 (daily avg) (lower outcome, -0.316 per SD, q = 1.4e-04).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **%181-250 (daily avg)** (CV AUC 0.666 vs 0.660 for covariates alone, gain +0.005; OR 1.19 per SD, p = 3.0e-04, q = 0.002). FDR-robust associations (2): %181-250 (daily avg) (higher outcome, OR 1.19 per SD, q = 0.002); %181-250 (pooled) (higher outcome, OR 1.19 per SD, q = 0.002).
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.065 vs 0.063 for covariates alone, gain +0.002; -0.153 per SD, p = 0.009, q = 0.033). FDR-robust associations (2): %181-250 (pooled) (lower outcome, -0.153 per SD, q = 0.033); %181-250 (daily avg) (lower outcome, -0.153 per SD, q = 0.035).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%181-250 (daily avg)** (CV R² 0.091 vs 0.092 for covariates alone, gain -0.000; +0.0904 per SD, p = 0.424, q = 0.596). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%181-250 (pooled)** (CV AUC 0.677 vs 0.676 for covariates alone, gain +0.001; OR 1.14 per SD, p = 0.050, q = 0.296). No association survives FDR; nominal only: %181-250 (pooled) (p = 0.050). Not predictable from glycaemia in this sample.
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.138 vs 0.139 for covariates alone, gain -0.000; +0.0261 per SD, p = 0.222, q = 0.393). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%181-250 (daily avg)** (CV R² 0.289 vs 0.290 for covariates alone, gain -0.001; +0.00993 per SD, p = 0.830, q = 0.892). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.230 vs 0.231 for covariates alone, gain -0.000; -0.085 per SD, p = 0.542, q = 0.701). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%181-250 (daily avg)** (CV R² 0.026 vs 0.027 for covariates alone, gain -0.001; +0.307 per SD, p = 0.524, q = 0.693). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.140 vs 0.139 for covariates alone, gain +0.001; +322 per SD, p = 0.093, q = 0.256). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.146 vs 0.145 for covariates alone, gain +0.001; +0.607 per SD, p = 0.083, q = 0.193). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.183 vs 0.148 for covariates alone, gain +0.035; +1.75 per SD, p = 1.6e-16, q = 7.1e-14). FDR-robust associations (4): %181-250 (pooled) (higher outcome, +1.75 per SD, q = 7.1e-14); %181-250 (daily avg) (higher outcome, +1.73 per SD, q = 7.6e-14); %181-250 (pooled) (higher outcome, +1.09 per SD, q = 0.019); %181-250 (daily avg) (higher outcome, +1.08 per SD, q = 0.020).
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.007 vs 0.007 for covariates alone, gain +0.000; -3.93 per SD, p = 0.146, q = 0.329). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.115 vs 0.090 for covariates alone, gain +0.025; +3.02 per SD, p = 3.0e-12, q = 8.6e-11). FDR-robust associations (4): %181-250 (pooled) (higher outcome, +3.02 per SD, q = 8.6e-11); %181-250 (daily avg) (higher outcome, +2.98 per SD, q = 1.6e-10); %181-250 (pooled) (higher outcome, +2.55 per SD, q = 0.007); %181-250 (daily avg) (higher outcome, +2.5 per SD, q = 0.007).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Resting heart-rate proxy (daily 5th pct, bpm) (+0.035, via %181-250 (pooled)); Garmin stress score, mean (0-100) (+0.025, via %181-250 (pooled)); MoCA total score (0-30) (+0.009, via %181-250 (pooled)); Cognitive impairment (MoCA < 26) (+0.005, via %181-250 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 181-250 (14 FDR-significant / 19 raw-significant of 84).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band >250 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 126 single-predictor tests; 27 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 126 tests (samples with n >= 500), of which **12** are significant at BH q < 0.05 in the all-tests family and 19 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.099 vs 0.092 for covariates alone, gain +0.007; -0.299 per SD, p = 1.6e-05, q = 1.2e-04). FDR-robust associations (3): Any >250 (0/1) (lower outcome, -0.299 per SD, q = 1.2e-04); %>250 (pooled) (lower outcome, -0.27 per SD, q = 0.004); %>250 (daily avg) (lower outcome, -0.265 per SD, q = 0.005).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **Any >250 (0/1)** (CV AUC 0.665 vs 0.660 for covariates alone, gain +0.005; OR 1.15 per SD, p = 0.003, q = 0.012). FDR-robust associations (3): Any >250 (0/1) (higher outcome, OR 1.15 per SD, q = 0.012); %>250 (pooled) (higher outcome, OR 1.15 per SD, q = 0.017); %>250 (daily avg) (higher outcome, OR 1.15 per SD, q = 0.021).
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.033 vs 0.029 for covariates alone, gain +0.005; -0.236 per SD, p = 0.012, q = 0.091). No association survives FDR; nominal only: %>250 (daily avg) (p = 0.003), %>250 (pooled) (p = 0.004), Any >250 (0/1) (p = 0.012), Any >250 (0/1) (p = 0.025).
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **%>250 (pooled)** (CV R² 0.092 vs 0.092 for covariates alone, gain -0.000; +0.146 per SD, p = 0.270, q = 0.440). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%>250 (pooled)** (CV AUC 0.637 vs 0.634 for covariates alone, gain +0.003; OR 1.13 per SD, p = 0.109, q = 0.270). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%>250 (daily avg)** (CV R² 0.139 vs 0.139 for covariates alone, gain +0.000; +0.0413 per SD, p = 0.111, q = 0.230). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.290 vs 0.289 for covariates alone, gain +0.001; -0.103 per SD, p = 0.061, q = 0.340). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.186 vs 0.186 for covariates alone, gain +0.000; -0.372 per SD, p = 0.095, q = 0.259). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%>250 (daily avg)** (CV R² 0.029 vs 0.028 for covariates alone, gain +0.002; -1.18 per SD, p = 0.085, q = 0.247). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.123 vs 0.122 for covariates alone, gain +0.001; +205 per SD, p = 0.055, q = 0.145). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.146 vs 0.145 for covariates alone, gain +0.001; +0.638 per SD, p = 0.045, q = 0.128). No association survives FDR; nominal only: Any >250 (0/1) (p = 0.045). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.167 vs 0.148 for covariates alone, gain +0.019; +1.28 per SD, p = 5.6e-11, q = 1.0e-09). FDR-robust associations (3): Any >250 (0/1) (higher outcome, +1.28 per SD, q = 1.0e-09); %>250 (pooled) (higher outcome, +1 per SD, q = 8.3e-05); %>250 (daily avg) (higher outcome, +1 per SD, q = 1.1e-04).
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.012 vs 0.007 for covariates alone, gain +0.005; -6.73 per SD, p = 0.014, q = 0.100). No association survives FDR; nominal only: Any >250 (0/1) (p = 0.014), Any >250 (0/1) (p = 0.032).
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **Any >250 (0/1)** (CV R² 0.104 vs 0.090 for covariates alone, gain +0.014; +2.27 per SD, p = 3.9e-08, q = 5.1e-07). FDR-robust associations (3): Any >250 (0/1) (higher outcome, +2.27 per SD, q = 5.1e-07); %>250 (pooled) (higher outcome, +1.93 per SD, q = 6.5e-04); %>250 (daily avg) (higher outcome, +1.93 per SD, q = 7.9e-04).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Resting heart-rate proxy (daily 5th pct, bpm) (+0.019, via Any >250 (0/1)); Garmin stress score, mean (0-100) (+0.014, via Any >250 (0/1)); MoCA total score (0-30) (+0.007, via Any >250 (0/1)); Total sleep time per night (min) (+0.005, via Any >250 (0/1)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 250 (12 FDR-significant / 27 raw-significant of 126).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - band <54 (all populations pooled in the counts; see tables for population-specific rows)

**Scope.** 126 single-predictor tests; 17 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 126 tests (samples with n >= 500), of which **2** are significant at BH q < 0.05 in the all-tests family and 5 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.081 vs 0.079 for covariates alone, gain +0.002; +0.166 per SD, p = 0.030, q = 0.201). No association survives FDR; nominal only: Any <54 (0/1) (p = 0.030), Any <54 (0/1) (p = 0.037).
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **Any <54 (0/1)** (CV AUC 0.646 vs 0.644 for covariates alone, gain +0.002; OR 0.88 per SD, p = 0.046, q = 0.280). No association survives FDR; nominal only: Any <54 (0/1) (p = 0.026), Any <54 (0/1) (p = 0.046). Not predictable from glycaemia in this sample.
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.049 vs 0.048 for covariates alone, gain +0.001; +0.162 per SD, p = 0.022, q = 0.158). No association survives FDR; nominal only: Any <54 (0/1) (p = 0.022). Not predictable from glycaemia in this sample.
- **CES-D-10 depressive symptoms (0-30)** (n = 2,135): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.091 vs 0.092 for covariates alone, gain -0.001; +0.066 per SD, p = 0.527, q = 0.693). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 2,135): best single predictor out of sample is **%<54 (daily avg)** (CV AUC 0.676 vs 0.676 for covariates alone, gain +0.000; OR 0.95 per SD, p = 0.620, q = 0.932). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.138 vs 0.131 for covariates alone, gain +0.007; +0.113 per SD, p = 0.005, q = 0.054). No association survives FDR; nominal only: %<54 (pooled) (p = 0.005).
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.290 vs 0.289 for covariates alone, gain +0.001; +0.114 per SD, p = 0.077, q = 0.385). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.242 vs 0.240 for covariates alone, gain +0.001; -0.324 per SD, p = 0.001, q = 0.036). FDR-robust associations (1): %<54 (daily avg) (lower outcome, -0.324 per SD, q = 0.036).
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.003 vs 0.002 for covariates alone, gain +0.000; -0.483 per SD, p = 0.273, q = 0.648). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 1,872): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.144 vs 0.139 for covariates alone, gain +0.005; -502 per SD, p = 0.005, q = 0.052). FDR-robust associations (1): %<54 (daily avg) (lower outcome, -187 per SD, q = 0.028).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,872): best single predictor out of sample is **Any <54 (0/1)** (CV R² 0.156 vs 0.155 for covariates alone, gain +0.001; -1.07 per SD, p = 0.038, q = 0.169). No association survives FDR; nominal only: Any <54 (0/1) (p = 0.038). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,877): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.104 vs 0.104 for covariates alone, gain -0.000; +0.172 per SD, p = 0.267, q = 0.645). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Total sleep time per night (min)** (n = 1,893): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.009 vs 0.007 for covariates alone, gain +0.003; +4.19 per SD, p = 0.042, q = 0.182). No association survives FDR; nominal only: %<54 (pooled) (p = 0.042).
- **Garmin stress score, mean (0-100)** (n = 1,879): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.089 vs 0.090 for covariates alone, gain -0.001; +0.011 per SD, p = 0.977, q = 0.986). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.007, via %<54 (pooled)); Steps per wear-day (+0.005, via Any <54 (0/1)); Total sleep time per night (min) (+0.003, via %<54 (pooled)); MoCA total score (0-30) (+0.002, via Any <54 (0/1)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band < 54 (2 FDR-significant / 17 raw-significant of 126).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
