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

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time in range 70-180, pooled (%) | 2138 | 2135 | +0.356 [+0.208, +0.503] | 0.01767 | 4.73 | 2.3e-06*** | 2.3e-05 (FDR<0.05) | 9.3e-06 (FDR<0.05) | -26.4 | -1.7 | 0.1022 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time in range 70-180 (%) | 2138 | 2134 | +0.350 [+0.202, +0.498] | 0.0173 | 4.63 | 3.6e-06*** | 3.4e-05 (FDR<0.05) | 1.1e-05 (FDR<0.05) | -25.4 | -0.8 | 0.1018 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time in range 70-180, pooled (%) | 2138 | 2135 | OR 0.827 [0.753, 0.908] | -0.009435 | -4.00 | 6.4e-05*** | 4.2e-04 (FDR<0.05) | 3.3e-04 (FDR<0.05) | -14.2 | -0.6 | 0.6657 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time in range 70-180 (%) | 2138 | 2134 | OR 0.828 [0.754, 0.909] | -0.009318 | -3.96 | 7.4e-05*** | 4.7e-04 (FDR<0.05) | 3.3e-04 (FDR<0.05) | -14.0 | -0.3 | 0.6655 | 0.6603 |
| MoCA memory index score (0-15) | Time in range 70-180, pooled (%) | 2138 | 2135 | +0.167 [+0.053, +0.281] | 0.008283 | 2.87 | 0.004** | 0.017 (FDR<0.05) | 0.016 (FDR<0.05) | -6.0 | -0.6 | 0.0657 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time in range 70-180 (%) | 2138 | 2134 | +0.167 [+0.053, +0.281] | 0.008252 | 2.87 | 0.004** | 0.017 (FDR<0.05) | 0.016 (FDR<0.05) | -6.0 | -0.6 | 0.0656 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time in range 70-180, pooled (%) | 2135 | 2132 | -0.144 [-0.379, +0.091] | -0.007131 | -1.20 | 0.231 | 0.400 | 0.620 | +0.2 | +0.4 | 0.0917 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time in range 70-180 (%) | 2135 | 2131 | -0.139 [-0.374, +0.096] | -0.006853 | -1.16 | 0.248 | 0.415 | 0.620 | +0.3 | +0.5 | 0.0917 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time in range 70-180, pooled (%) | 2135 | 2132 | OR 0.895 [0.807, 0.994] | -0.00548 | -2.07 | 0.038* | 0.111 | 0.158 | -2.2 | +0.5 | 0.6693 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time in range 70-180 (%) | 2135 | 2131 | OR 0.899 [0.810, 0.998] | -0.005251 | -1.99 | 0.047* | 0.130 | 0.158 | -1.8 | +0.9 | 0.6693 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time in range 70-180, pooled (%) | 2100 | 2097 | -0.045 [-0.090, +0.001] | -0.002213 | -1.91 | 0.056 | 0.146 | 0.173 | -2.9 | +8.0 | 0.1394 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time in range 70-180 (%) | 2100 | 2096 | -0.045 [-0.090, +0.001] | -0.002196 | -1.91 | 0.057 | 0.147 | 0.173 | -2.9 | +8.0 | 0.1394 | 0.1387 |
| Indoor temperature, mean (deg C) | Time in range 70-180, pooled (%) | 2100 | 2097 | -0.026 [-0.122, +0.069] | -0.001304 | -0.54 | 0.588 | 0.740 | 0.982 | +1.7 | +0.1 | 0.2891 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time in range 70-180 (%) | 2100 | 2096 | -0.023 [-0.119, +0.072] | -0.001151 | -0.48 | 0.632 | 0.781 | 0.982 | +1.7 | +0.2 | 0.2890 | 0.2896 |
| Indoor relative humidity, mean (%) | Time in range 70-180, pooled (%) | 2100 | 2097 | +0.068 [-0.210, +0.347] | 0.003375 | 0.48 | 0.632 | 0.781 | 0.898 | +1.7 | -0.1 | 0.2301 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time in range 70-180 (%) | 2100 | 2096 | +0.063 [-0.216, +0.342] | 0.003113 | 0.44 | 0.657 | 0.799 | 0.898 | +1.8 | -0.1 | 0.2300 | 0.2307 |
| Indoor VOC index, mean | Time in range 70-180, pooled (%) | 2100 | 2097 | +0.175 [-0.704, +1.053] | 0.008643 | 0.39 | 0.697 | 0.817 | 0.868 | +1.8 | +1.7 | 0.0255 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time in range 70-180 (%) | 2100 | 2096 | +0.198 [-0.684, +1.080] | 0.009775 | 0.44 | 0.659 | 0.799 | 0.868 | +1.7 | +1.7 | 0.0255 | 0.0271 |
| Steps per wear-day | Time in range 70-180, pooled (%) | 1872 | 1869 | -125.480 [-382.665, +131.705] | -6.29 | -0.96 | 0.339 | 0.500 | 0.424 | +0.5 | +8.4 | 0.1216 | 0.1222 |
| Steps per wear-day | Avg. daily time in range 70-180 (%) | 1872 | 1869 | -124.676 [-381.867, +132.515] | -6.219 | -0.95 | 0.342 | 0.502 | 0.424 | +0.5 | +8.5 | 0.1216 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time in range 70-180, pooled (%) | 1872 | 1869 | -0.401 [-1.129, +0.326] | -0.02011 | -1.08 | 0.280 | 0.447 | 0.351 | +0.3 | +8.5 | 0.1444 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time in range 70-180 (%) | 1872 | 1869 | -0.399 [-1.128, +0.330] | -0.01992 | -1.07 | 0.283 | 0.450 | 0.351 | +0.3 | +8.5 | 0.1444 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time in range 70-180, pooled (%) | 1877 | 1874 | -1.679 [-2.105, -1.253] | -0.08406 | -7.73 | 1.1e-14*** | 6.3e-13 (FDR<0.05) | 5.2e-14 (FDR<0.05) | -73.5 | -2.3 | 0.1805 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time in range 70-180 (%) | 1877 | 1874 | -1.667 [-2.092, -1.241] | -0.08302 | -7.67 | 1.7e-14*** | 7.4e-13 (FDR<0.05) | 5.9e-14 (FDR<0.05) | -72.3 | -1.1 | 0.1800 | 0.1482 |
| Total sleep time per night (min) | Time in range 70-180, pooled (%) | 1893 | 1891 | +1.916 [-1.242, +5.074] | 0.09728 | 1.19 | 0.234 | 0.400 | 0.403 | +0.6 | +9.5 | 0.0202 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time in range 70-180 (%) | 1893 | 1891 | +1.872 [-1.297, +5.042] | 0.0946 | 1.16 | 0.247 | 0.415 | 0.403 | +0.6 | +9.5 | 0.0202 | 0.0209 |
| Garmin stress score, mean (0-100) | Time in range 70-180, pooled (%) | 1879 | 1876 | -2.996 [-3.872, -2.119] | -0.1501 | -6.70 | 2.1e-11*** | 4.6e-10 (FDR<0.05) | 9.0e-11 (FDR<0.05) | -50.4 | +10.0 | 0.1143 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time in range 70-180 (%) | 1879 | 1876 | -2.959 [-3.835, -2.083] | -0.1475 | -6.62 | 3.6e-11*** | 7.1e-10 (FDR<0.05) | 1.2e-10 (FDR<0.05) | -49.1 | +11.3 | 0.1137 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time in range 70-180, pooled (%) | 1271 | 1271 | +0.328 [+0.112, +0.543] | 0.03694 | 2.98 | 0.003** | 0.052 | 0.011 (FDR<0.05) | -16.2 | -2.5 | 0.0874 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time in range 70-180 (%) | 1271 | 1270 | +0.324 [+0.108, +0.540] | 0.03636 | 2.94 | 0.003** | 0.052 | 0.011 (FDR<0.05) | -15.8 | -2.1 | 0.0871 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time in range 70-180, pooled (%) | 1271 | 1271 | OR 0.920 [0.816, 1.038] | -0.009342 | -1.35 | 0.176 | 0.532 | 0.480 | +0.2 | -0.1 | 0.6448 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time in range 70-180 (%) | 1271 | 1270 | OR 0.922 [0.818, 1.039] | -0.009166 | -1.34 | 0.182 | 0.533 | 0.480 | +0.2 | -0.0 | 0.6445 | 0.6443 |
| MoCA memory index score (0-15) | Time in range 70-180, pooled (%) | 1271 | 1271 | +0.171 [+0.037, +0.304] | 0.01922 | 2.50 | 0.012* | 0.131 | 0.035 (FDR<0.05) | -3.6 | -3.0 | 0.0496 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time in range 70-180 (%) | 1271 | 1270 | +0.176 [+0.044, +0.309] | 0.01978 | 2.61 | 0.009** | 0.104 | 0.028 (FDR<0.05) | -4.0 | -3.3 | 0.0498 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time in range 70-180, pooled (%) | 1270 | 1270 | -0.076 [-0.434, +0.282] | -0.008615 | -0.41 | 0.678 | 0.932 | 0.953 | +1.7 | -0.3 | 0.0631 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time in range 70-180 (%) | 1270 | 1269 | -0.082 [-0.439, +0.276] | -0.009281 | -0.45 | 0.653 | 0.932 | 0.953 | +1.6 | -0.4 | 0.0632 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time in range 70-180, pooled (%) | 1270 | 1270 | OR 0.906 [0.798, 1.028] | -0.01123 | -1.53 | 0.125 | 0.472 | 0.565 | -0.2 | -1.4 | 0.6759 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time in range 70-180 (%) | 1270 | 1269 | OR 0.907 [0.800, 1.029] | -0.01104 | -1.52 | 0.130 | 0.481 | 0.565 | -0.2 | -1.3 | 0.6757 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time in range 70-180, pooled (%) | 1251 | 1251 | +0.034 [-0.005, +0.073] | 0.00382 | 1.73 | 0.083 | 0.404 | 0.265 | +0.0 | -2.0 | 0.1142 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time in range 70-180 (%) | 1251 | 1250 | +0.034 [-0.005, +0.072] | 0.00377 | 1.72 | 0.086 | 0.404 | 0.265 | +0.1 | -1.9 | 0.1142 | 0.1139 |
| Indoor temperature, mean (deg C) | Time in range 70-180, pooled (%) | 1251 | 1251 | -0.048 [-0.158, +0.063] | -0.005345 | -0.85 | 0.396 | 0.797 | 0.915 | +1.2 | -0.8 | 0.2889 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time in range 70-180 (%) | 1251 | 1250 | -0.048 [-0.158, +0.062] | -0.005342 | -0.86 | 0.392 | 0.794 | 0.915 | +1.2 | -0.8 | 0.2889 | 0.2892 |
| Indoor relative humidity, mean (%) | Time in range 70-180, pooled (%) | 1251 | 1251 | +0.031 [-0.296, +0.358] | 0.003467 | 0.19 | 0.853 | 0.948 | 0.905 | +2.0 | +2.5 | 0.2388 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time in range 70-180 (%) | 1251 | 1250 | +0.021 [-0.304, +0.346] | 0.002338 | 0.13 | 0.899 | 0.964 | 0.905 | +2.0 | +2.5 | 0.2389 | 0.2403 |
| Indoor VOC index, mean | Time in range 70-180, pooled (%) | 1251 | 1251 | +0.201 [-0.741, +1.144] | 0.02255 | 0.42 | 0.675 | 0.932 | 0.784 | +1.8 | +1.2 | 0.0003 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time in range 70-180 (%) | 1251 | 1250 | +0.184 [-0.761, +1.130] | 0.02054 | 0.38 | 0.703 | 0.932 | 0.784 | +1.8 | +1.2 | 0.0004 | 0.0025 |
| Steps per wear-day | Time in range 70-180, pooled (%) | 1125 | 1125 | +44.618 [-193.349, +282.584] | 5.207 | 0.37 | 0.713 | 0.932 | 0.958 | +1.8 | +5.1 | 0.1064 | 0.1080 |
| Steps per wear-day | Avg. daily time in range 70-180 (%) | 1125 | 1125 | +48.810 [-189.118, +286.738] | 5.676 | 0.40 | 0.688 | 0.932 | 0.958 | +1.8 | +5.1 | 0.1064 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time in range 70-180, pooled (%) | 1125 | 1125 | -0.199 [-0.958, +0.560] | -0.02319 | -0.51 | 0.608 | 0.932 | 0.931 | +1.7 | +5.1 | 0.1232 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time in range 70-180 (%) | 1125 | 1125 | -0.178 [-0.939, +0.583] | -0.02069 | -0.46 | 0.647 | 0.932 | 0.931 | +1.7 | +5.2 | 0.1231 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time in range 70-180, pooled (%) | 1128 | 1128 | -0.728 [-1.309, -0.146] | -0.08501 | -2.45 | 0.014* | 0.137 | 0.034 (FDR<0.05) | -8.8 | +2.4 | 0.1081 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time in range 70-180 (%) | 1128 | 1128 | -0.712 [-1.294, -0.130] | -0.08287 | -2.40 | 0.017* | 0.137 | 0.034 (FDR<0.05) | -8.4 | +2.9 | 0.1076 | 0.1044 |
| Total sleep time per night (min) | Time in range 70-180, pooled (%) | 1137 | 1137 | -1.155 [-5.159, +2.849] | -0.1438 | -0.57 | 0.572 | 0.932 | 0.936 | +1.7 | +3.7 | -0.0068 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time in range 70-180 (%) | 1137 | 1137 | -1.222 [-5.231, +2.787] | -0.1516 | -0.60 | 0.550 | 0.932 | 0.936 | +1.6 | +3.6 | -0.0068 | -0.0051 |
| Garmin stress score, mean (0-100) | Time in range 70-180, pooled (%) | 1130 | 1130 | -0.793 [-2.174, +0.588] | -0.09275 | -1.13 | 0.260 | 0.638 | 0.471 | -0.5 | +7.2 | 0.0489 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time in range 70-180 (%) | 1130 | 1130 | -0.734 [-2.110, +0.642] | -0.08554 | -1.05 | 0.296 | 0.681 | 0.483 | -0.2 | +7.6 | 0.0487 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time in range 70-180, pooled (%) | 867 | 864 | +0.253 [+0.024, +0.481] | 0.009848 | 2.17 | 0.030* | not applied (n < 1000) | not applied (n < 1000) | -3.0 | -1.5 | 0.0581 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time in range 70-180 (%) | 867 | 864 | +0.246 [+0.016, +0.475] | 0.009508 | 2.10 | 0.036* | not applied (n < 1000) | not applied (n < 1000) | -2.7 | -1.2 | 0.0578 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time in range 70-180, pooled (%) | 867 | 864 | OR 0.855 [0.741, 0.986] | -0.006108 | -2.16 | 0.031* | not applied (n < 1000) | not applied (n < 1000) | -2.7 | -1.0 | 0.6438 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time in range 70-180 (%) | 867 | 864 | OR 0.856 [0.742, 0.987] | -0.006034 | -2.14 | 0.032* | not applied (n < 1000) | not applied (n < 1000) | -2.6 | -0.9 | 0.6440 | 0.6425 |
| MoCA memory index score (0-15) | Time in range 70-180, pooled (%) | 867 | 864 | +0.173 [-0.003, +0.349] | 0.006725 | 1.92 | 0.055 | not applied (n < 1000) | not applied (n < 1000) | -1.4 | +0.4 | 0.0314 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time in range 70-180 (%) | 867 | 864 | +0.171 [-0.006, +0.348] | 0.006605 | 1.89 | 0.059 | not applied (n < 1000) | not applied (n < 1000) | -1.3 | +0.5 | 0.0313 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time in range 70-180, pooled (%) | 865 | 862 | -0.215 [-0.574, +0.144] | -0.008358 | -1.17 | 0.241 | not applied (n < 1000) | not applied (n < 1000) | +0.4 | +1.7 | 0.0781 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time in range 70-180 (%) | 865 | 862 | -0.203 [-0.564, +0.157] | -0.007867 | -1.11 | 0.269 | not applied (n < 1000) | not applied (n < 1000) | +0.6 | +1.8 | 0.0781 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time in range 70-180, pooled (%) | 865 | 862 | OR 0.868 [0.739, 1.018] | -0.005522 | -1.74 | 0.082 | not applied (n < 1000) | not applied (n < 1000) | -1.0 | +2.0 | 0.6358 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time in range 70-180 (%) | 865 | 862 | OR 0.874 [0.744, 1.026] | -0.005232 | -1.65 | 0.099 | not applied (n < 1000) | not applied (n < 1000) | -0.7 | +2.3 | 0.6359 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time in range 70-180, pooled (%) | 849 | 846 | -0.075 [-0.147, -0.002] | -0.00291 | -2.02 | 0.043* | not applied (n < 1000) | not applied (n < 1000) | -3.4 | +6.0 | 0.1329 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time in range 70-180 (%) | 849 | 846 | -0.075 [-0.147, -0.002] | -0.00289 | -2.02 | 0.043* | not applied (n < 1000) | not applied (n < 1000) | -3.4 | +6.0 | 0.1329 | 0.1310 |
| Indoor temperature, mean (deg C) | Time in range 70-180, pooled (%) | 849 | 846 | +0.059 [-0.098, +0.217] | 0.0023 | 0.74 | 0.461 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | -0.3 | 0.2229 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time in range 70-180 (%) | 849 | 846 | +0.064 [-0.094, +0.222] | 0.00247 | 0.79 | 0.428 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | -0.4 | 0.2230 | 0.2264 |
| Indoor relative humidity, mean (%) | Time in range 70-180, pooled (%) | 849 | 846 | +0.145 [-0.306, +0.596] | 0.005621 | 0.63 | 0.530 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.3 | 0.1843 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time in range 70-180 (%) | 849 | 846 | +0.140 [-0.312, +0.592] | 0.005407 | 0.61 | 0.544 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.3 | 0.1842 | 0.1857 |
| Indoor VOC index, mean | Time in range 70-180, pooled (%) | 849 | 846 | +0.451 [-0.867, +1.769] | 0.01753 | 0.67 | 0.502 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +1.8 | 0.0264 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time in range 70-180 (%) | 849 | 846 | +0.505 [-0.820, +1.831] | 0.01953 | 0.75 | 0.455 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | +1.6 | 0.0266 | 0.0276 |
| Steps per wear-day | Time in range 70-180, pooled (%) | 747 | 744 | -115.817 [-530.170, +298.536] | -4.511 | -0.55 | 0.584 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +1.7 | 0.1370 | 0.1390 |
| Steps per wear-day | Avg. daily time in range 70-180 (%) | 747 | 744 | -119.774 [-533.581, +294.032] | -4.636 | -0.57 | 0.571 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +1.7 | 0.1370 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time in range 70-180, pooled (%) | 747 | 744 | -0.153 [-1.307, +1.001] | -0.005967 | -0.26 | 0.795 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +2.0 | 0.1526 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time in range 70-180 (%) | 747 | 744 | -0.168 [-1.324, +0.988] | -0.006509 | -0.29 | 0.776 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +1.9 | 0.1525 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time in range 70-180, pooled (%) | 749 | 746 | -1.072 [-1.717, -0.427] | -0.04169 | -3.26 | 0.001** | not applied (n < 1000) | not applied (n < 1000) | -9.9 | -3.8 | 0.1365 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time in range 70-180 (%) | 749 | 746 | -1.063 [-1.707, -0.420] | -0.04111 | -3.24 | 0.001** | not applied (n < 1000) | not applied (n < 1000) | -9.7 | -3.6 | 0.1362 | 0.1253 |
| Total sleep time per night (min) | Time in range 70-180, pooled (%) | 756 | 754 | +2.583 [-2.433, +7.599] | 0.1016 | 1.01 | 0.313 | not applied (n < 1000) | not applied (n < 1000) | +1.0 | +3.9 | 0.0053 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time in range 70-180 (%) | 756 | 754 | +2.581 [-2.457, +7.620] | 0.1009 | 1.00 | 0.315 | not applied (n < 1000) | not applied (n < 1000) | +1.0 | +3.9 | 0.0051 | 0.0066 |
| Garmin stress score, mean (0-100) | Time in range 70-180, pooled (%) | 749 | 746 | -2.611 [-3.935, -1.287] | -0.1016 | -3.86 | 1.1e-04*** | not applied (n < 1000) | not applied (n < 1000) | -14.2 | -1.1 | 0.1120 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time in range 70-180 (%) | 749 | 746 | -2.588 [-3.912, -1.265] | -0.1001 | -3.83 | 1.3e-04*** | not applied (n < 1000) | not applied (n < 1000) | -13.9 | -0.8 | 0.1116 | 0.0947 |


---

## Band 54-69

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-69, pooled (%) | 2138 | 1251 | +0.021 [-0.100, +0.143] | 0.01489 | 0.34 | 0.731 | 0.840 | 0.782 | +1.9 | +26.5 | 0.0905 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time 54-69 (%) | 2138 | 1051 | +0.014 [-0.112, +0.139] | 0.009357 | 0.21 | 0.832 | 0.892 | 0.832 | +2.0 | +26.6 | 0.0904 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time 54-69, pooled (%) | 2138 | 1251 | OR 1.046 [0.955, 1.144] | 0.03119 | 0.97 | 0.332 | 0.500 | 0.368 | +1.1 | +14.7 | 0.6602 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-69 (%) | 2138 | 1051 | OR 1.056 [0.965, 1.155] | 0.03756 | 1.19 | 0.236 | 0.401 | 0.281 | +0.6 | +14.2 | 0.6604 | 0.6603 |
| MoCA memory index score (0-15) | Time 54-69, pooled (%) | 2138 | 1251 | +0.007 [-0.094, +0.108] | 0.00479 | 0.13 | 0.894 | 0.939 | 0.924 | +2.0 | +7.4 | 0.0619 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time 54-69 (%) | 2138 | 1051 | -0.022 [-0.127, +0.083] | -0.01511 | -0.41 | 0.683 | 0.805 | 0.756 | +1.9 | +7.2 | 0.0619 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time 54-69, pooled (%) | 2135 | 1250 | +0.076 [-0.125, +0.277] | 0.053 | 0.74 | 0.460 | 0.630 | 0.620 | +1.5 | +1.7 | 0.0911 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-69 (%) | 2135 | 1050 | +0.098 [-0.103, +0.300] | 0.06801 | 0.96 | 0.337 | 0.500 | 0.620 | +1.1 | +1.3 | 0.0913 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-69, pooled (%) | 2135 | 1250 | OR 1.031 [0.927, 1.146] | 0.02108 | 0.56 | 0.576 | 0.732 | 0.687 | +1.7 | +4.4 | 0.6671 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-69 (%) | 2135 | 1050 | OR 1.032 [0.928, 1.147] | 0.02161 | 0.58 | 0.561 | 0.718 | 0.687 | +1.7 | +4.4 | 0.6673 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-69, pooled (%) | 2100 | 1226 | +0.050 [-0.004, +0.104] | 0.03483 | 1.83 | 0.068 | 0.171 | 0.173 | -4.6 | +6.3 | 0.1402 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-69 (%) | 2100 | 1027 | +0.053 [-0.003, +0.109] | 0.03644 | 1.87 | 0.061 | 0.158 | 0.173 | -5.4 | +5.5 | 0.1404 | 0.1387 |
| Indoor temperature, mean (deg C) | Time 54-69, pooled (%) | 2100 | 1226 | +0.055 [-0.023, +0.133] | 0.03829 | 1.38 | 0.167 | 0.322 | 0.982 | +0.4 | -1.1 | 0.2895 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-69 (%) | 2100 | 1027 | +0.069 [-0.009, +0.147] | 0.04724 | 1.73 | 0.085 | 0.195 | 0.801 | -0.5 | -2.0 | 0.2898 | 0.2896 |
| Indoor relative humidity, mean (%) | Time 54-69, pooled (%) | 2100 | 1226 | -0.146 [-0.407, +0.114] | -0.1018 | -1.10 | 0.270 | 0.440 | 0.898 | +0.8 | -1.1 | 0.2302 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-69 (%) | 2100 | 1027 | -0.156 [-0.415, +0.103] | -0.107 | -1.18 | 0.238 | 0.404 | 0.898 | +0.6 | -1.3 | 0.2302 | 0.2307 |
| Indoor VOC index, mean | Time 54-69, pooled (%) | 2100 | 1226 | +0.130 [-0.570, +0.831] | 0.09074 | 0.36 | 0.715 | 0.834 | 0.868 | +1.9 | +1.8 | 0.0262 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time 54-69 (%) | 2100 | 1027 | +0.091 [-0.607, +0.789] | 0.0625 | 0.26 | 0.798 | 0.873 | 0.884 | +1.9 | +1.9 | 0.0263 | 0.0271 |
| Steps per wear-day | Time 54-69, pooled (%) | 1872 | 1116 | -217.612 [-400.159, -35.066] | -146.6 | -2.34 | 0.019* | 0.065 | 0.083 | -2.9 | +5.1 | 0.1232 | 0.1222 |
| Steps per wear-day | Avg. daily time 54-69 (%) | 1872 | 935 | -221.219 [-404.121, -38.317] | -146.6 | -2.37 | 0.018* | 0.060 | 0.083 | -3.1 | +4.9 | 0.1232 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-69, pooled (%) | 1872 | 1116 | -0.440 [-0.974, +0.093] | -0.2966 | -1.62 | 0.106 | 0.220 | 0.205 | -0.2 | +8.0 | 0.1443 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-69 (%) | 1872 | 935 | -0.475 [-1.015, +0.065] | -0.3147 | -1.72 | 0.085 | 0.195 | 0.192 | -0.6 | +7.6 | 0.1444 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-69, pooled (%) | 1877 | 1121 | -0.175 [-0.513, +0.163] | -0.1179 | -1.01 | 0.311 | 0.482 | 0.371 | +1.1 | +72.4 | 0.1481 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-69 (%) | 1877 | 939 | -0.181 [-0.528, +0.167] | -0.1198 | -1.02 | 0.309 | 0.482 | 0.371 | +1.1 | +72.3 | 0.1481 | 0.1482 |
| Total sleep time per night (min) | Time 54-69, pooled (%) | 1893 | 1140 | +1.447 [-1.318, +4.212] | 0.9811 | 1.03 | 0.305 | 0.480 | 0.473 | +1.1 | +10.0 | 0.0205 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time 54-69 (%) | 1893 | 958 | +1.202 [-1.529, +3.932] | 0.8015 | 0.86 | 0.388 | 0.556 | 0.523 | +1.4 | +10.3 | 0.0203 | 0.0209 |
| Garmin stress score, mean (0-100) | Time 54-69, pooled (%) | 1879 | 1122 | -0.521 [-1.340, +0.298] | -0.3514 | -1.25 | 0.212 | 0.378 | 0.253 | +0.3 | +60.7 | 0.0899 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-69 (%) | 1879 | 940 | -0.555 [-1.407, +0.296] | -0.3685 | -1.28 | 0.201 | 0.365 | 0.249 | +0.1 | +60.5 | 0.0897 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-69, pooled (%) | 1271 | 828 | +0.020 [-0.099, +0.139] | 0.01442 | 0.33 | 0.740 | 0.932 | 0.820 | +1.9 | +15.6 | 0.0781 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time 54-69 (%) | 1271 | 695 | +0.016 [-0.103, +0.135] | 0.01152 | 0.26 | 0.791 | 0.936 | 0.841 | +2.0 | +15.7 | 0.0782 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time 54-69, pooled (%) | 1271 | 828 | OR 1.077 [0.957, 1.212] | 0.0532 | 1.23 | 0.217 | 0.594 | 0.480 | +0.5 | +0.3 | 0.6443 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-69 (%) | 1271 | 695 | OR 1.083 [0.964, 1.218] | 0.05731 | 1.34 | 0.179 | 0.532 | 0.480 | +0.3 | +0.0 | 0.6443 | 0.6443 |
| MoCA memory index score (0-15) | Time 54-69, pooled (%) | 1271 | 828 | +0.098 [-0.008, +0.204] | 0.07024 | 1.81 | 0.070 | 0.356 | 0.127 | +0.1 | +0.8 | 0.0476 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time 54-69 (%) | 1271 | 695 | +0.075 [-0.030, +0.179] | 0.05337 | 1.40 | 0.163 | 0.532 | 0.229 | +0.9 | +1.6 | 0.0472 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time 54-69, pooled (%) | 1270 | 828 | +0.033 [-0.241, +0.307] | 0.02354 | 0.24 | 0.814 | 0.939 | 0.953 | +1.9 | -0.1 | 0.0661 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-69 (%) | 1270 | 695 | +0.060 [-0.215, +0.335] | 0.04257 | 0.42 | 0.671 | 0.932 | 0.953 | +1.8 | -0.2 | 0.0662 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-69, pooled (%) | 1270 | 828 | OR 1.041 [0.905, 1.198] | 0.02884 | 0.56 | 0.572 | 0.932 | 0.958 | +1.7 | +0.6 | 0.6725 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-69 (%) | 1270 | 695 | OR 1.034 [0.898, 1.189] | 0.0236 | 0.46 | 0.645 | 0.932 | 0.958 | +1.8 | +0.7 | 0.6722 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-69, pooled (%) | 1251 | 814 | -0.003 [-0.051, +0.045] | -0.001978 | -0.11 | 0.910 | 0.968 | 0.987 | +2.0 | -0.0 | 0.1125 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-69 (%) | 1251 | 682 | -0.001 [-0.051, +0.048] | -0.001056 | -0.06 | 0.953 | 0.983 | 0.987 | +2.0 | -0.0 | 0.1123 | 0.1139 |
| Indoor temperature, mean (deg C) | Time 54-69, pooled (%) | 1251 | 814 | +0.062 [-0.022, +0.146] | 0.04401 | 1.44 | 0.149 | 0.510 | 0.771 | +0.7 | -1.3 | 0.2891 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-69 (%) | 1251 | 682 | +0.071 [-0.016, +0.158] | 0.05075 | 1.60 | 0.109 | 0.441 | 0.674 | +0.3 | -1.7 | 0.2892 | 0.2892 |
| Indoor relative humidity, mean (%) | Time 54-69, pooled (%) | 1251 | 814 | -0.205 [-0.482, +0.072] | -0.1463 | -1.45 | 0.146 | 0.503 | 0.585 | +0.5 | +1.0 | 0.2399 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-69 (%) | 1251 | 682 | -0.187 [-0.465, +0.092] | -0.1334 | -1.31 | 0.189 | 0.542 | 0.585 | +0.7 | +1.2 | 0.2396 | 0.2403 |
| Indoor VOC index, mean | Time 54-69, pooled (%) | 1251 | 814 | -0.152 [-1.056, +0.752] | -0.1084 | -0.33 | 0.742 | 0.932 | 0.784 | +1.9 | +1.3 | 0.0014 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time 54-69 (%) | 1251 | 682 | -0.188 [-1.124, +0.748] | -0.1343 | -0.39 | 0.694 | 0.932 | 0.784 | +1.8 | +1.2 | 0.0015 | 0.0025 |
| Steps per wear-day | Time 54-69, pooled (%) | 1125 | 747 | -49.093 [-300.312, +202.126] | -33.59 | -0.38 | 0.702 | 0.932 | 0.958 | +1.8 | +5.1 | 0.1069 | 0.1080 |
| Steps per wear-day | Avg. daily time 54-69 (%) | 1125 | 626 | -41.751 [-299.032, +215.529] | -28.61 | -0.32 | 0.750 | 0.932 | 0.958 | +1.9 | +5.2 | 0.1068 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-69, pooled (%) | 1125 | 747 | -0.106 [-0.881, +0.670] | -0.07241 | -0.27 | 0.789 | 0.936 | 0.931 | +1.9 | +5.4 | 0.1234 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-69 (%) | 1125 | 626 | -0.122 [-0.913, +0.669] | -0.08369 | -0.30 | 0.762 | 0.932 | 0.931 | +1.9 | +5.3 | 0.1234 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-69, pooled (%) | 1128 | 749 | +0.005 [-0.413, +0.423] | 0.003607 | 0.02 | 0.980 | 0.989 | 0.980 | +2.0 | +13.2 | 0.1026 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-69 (%) | 1128 | 627 | +0.008 [-0.418, +0.434] | 0.005403 | 0.04 | 0.971 | 0.986 | 0.980 | +2.0 | +13.2 | 0.1024 | 0.1044 |
| Total sleep time per night (min) | Time 54-69, pooled (%) | 1137 | 761 | +0.803 [-2.296, +3.901] | 0.5538 | 0.51 | 0.612 | 0.932 | 0.936 | +1.8 | +3.8 | -0.0067 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time 54-69 (%) | 1137 | 637 | +0.766 [-2.326, +3.857] | 0.5286 | 0.49 | 0.627 | 0.932 | 0.936 | +1.8 | +3.9 | -0.0066 | -0.0051 |
| Garmin stress score, mean (0-100) | Time 54-69, pooled (%) | 1130 | 750 | -0.113 [-1.153, +0.926] | -0.07759 | -0.21 | 0.831 | 0.945 | 0.920 | +1.9 | +9.7 | 0.0493 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-69 (%) | 1130 | 628 | -0.179 [-1.276, +0.917] | -0.123 | -0.32 | 0.749 | 0.932 | 0.895 | +1.9 | +9.7 | 0.0492 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-69, pooled (%) | 867 | 423 | -0.008 [-0.246, +0.230] | -0.005446 | -0.07 | 0.947 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0519 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time 54-69 (%) | 867 | 356 | -0.009 [-0.256, +0.237] | -0.006059 | -0.07 | 0.942 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0519 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time 54-69, pooled (%) | 867 | 423 | OR 1.037 [0.902, 1.192] | 0.02454 | 0.51 | 0.612 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +3.4 | 0.6399 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-69 (%) | 867 | 356 | OR 1.046 [0.909, 1.204] | 0.0297 | 0.63 | 0.530 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +3.3 | 0.6403 | 0.6425 |
| MoCA memory index score (0-15) | Time 54-69, pooled (%) | 867 | 423 | -0.131 [-0.305, +0.042] | -0.08886 | -1.48 | 0.139 | not applied (n < 1000) | not applied (n < 1000) | -0.0 | +1.8 | 0.0298 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time 54-69 (%) | 867 | 356 | -0.160 [-0.335, +0.015] | -0.1055 | -1.79 | 0.073 | not applied (n < 1000) | not applied (n < 1000) | -1.0 | +0.8 | 0.0308 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time 54-69, pooled (%) | 865 | 422 | +0.146 [-0.173, +0.464] | 0.09863 | 0.89 | 0.371 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +2.5 | 0.0787 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-69 (%) | 865 | 355 | +0.165 [-0.153, +0.482] | 0.1086 | 1.02 | 0.309 | not applied (n < 1000) | not applied (n < 1000) | +1.0 | +2.3 | 0.0789 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-69, pooled (%) | 865 | 422 | OR 1.023 [0.871, 1.201] | 0.01534 | 0.28 | 0.782 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +4.9 | 0.6309 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-69 (%) | 865 | 355 | OR 1.034 [0.882, 1.214] | 0.0223 | 0.42 | 0.678 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +4.8 | 0.6316 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-69, pooled (%) | 849 | 412 | +0.134 [+0.039, +0.228] | 0.08979 | 2.76 | 0.006** | not applied (n < 1000) | not applied (n < 1000) | -15.9 | -6.5 | 0.1424 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-69 (%) | 849 | 345 | +0.135 [+0.038, +0.233] | 0.08842 | 2.72 | 0.007** | not applied (n < 1000) | not applied (n < 1000) | -16.4 | -7.0 | 0.1428 | 0.1310 |
| Indoor temperature, mean (deg C) | Time 54-69, pooled (%) | 849 | 412 | +0.063 [-0.086, +0.212] | 0.04232 | 0.83 | 0.409 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | -0.4 | 0.2255 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-69 (%) | 849 | 345 | +0.080 [-0.065, +0.226] | 0.05241 | 1.08 | 0.280 | not applied (n < 1000) | not applied (n < 1000) | +0.8 | -0.9 | 0.2259 | 0.2264 |
| Indoor relative humidity, mean (%) | Time 54-69, pooled (%) | 849 | 412 | -0.063 [-0.587, +0.461] | -0.04255 | -0.24 | 0.813 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.0 | 0.1837 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-69 (%) | 849 | 345 | -0.112 [-0.625, +0.401] | -0.07306 | -0.43 | 0.669 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | -0.1 | 0.1842 | 0.1857 |
| Indoor VOC index, mean | Time 54-69, pooled (%) | 849 | 412 | +0.548 [-0.511, +1.606] | 0.3679 | 1.01 | 0.311 | not applied (n < 1000) | not applied (n < 1000) | +1.1 | +1.5 | 0.0271 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time 54-69 (%) | 849 | 345 | +0.491 [-0.544, +1.526] | 0.3206 | 0.93 | 0.352 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | +1.7 | 0.0269 | 0.0276 |
| Steps per wear-day | Time 54-69, pooled (%) | 747 | 369 | -383.181 [-658.791, -107.570] | -252.3 | -2.72 | 0.006** | not applied (n < 1000) | not applied (n < 1000) | -2.7 | -2.6 | 0.1425 | 0.1390 |
| Steps per wear-day | Avg. daily time 54-69 (%) | 747 | 309 | -401.236 [-670.891, -131.581] | -253.7 | -2.92 | 0.004** | not applied (n < 1000) | not applied (n < 1000) | -3.2 | -3.1 | 0.1432 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-69, pooled (%) | 747 | 369 | -0.737 [-1.508, +0.035] | -0.4851 | -1.87 | 0.061 | not applied (n < 1000) | not applied (n < 1000) | -0.1 | -0.1 | 0.1552 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-69 (%) | 747 | 309 | -0.806 [-1.600, -0.012] | -0.5097 | -1.99 | 0.047* | not applied (n < 1000) | not applied (n < 1000) | -0.5 | -0.5 | 0.1556 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-69, pooled (%) | 749 | 372 | -0.194 [-0.751, +0.363] | -0.1276 | -0.68 | 0.496 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +7.7 | 0.1243 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-69 (%) | 749 | 312 | -0.285 [-0.883, +0.313] | -0.1802 | -0.93 | 0.351 | not applied (n < 1000) | not applied (n < 1000) | +1.1 | +7.2 | 0.1249 | 0.1253 |
| Total sleep time per night (min) | Time 54-69, pooled (%) | 756 | 379 | +2.227 [-3.270, +7.725] | 1.474 | 0.79 | 0.427 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +4.1 | 0.0046 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time 54-69 (%) | 756 | 321 | +1.720 [-3.563, +7.003] | 1.093 | 0.64 | 0.523 | not applied (n < 1000) | not applied (n < 1000) | +1.5 | +4.4 | 0.0043 | 0.0066 |
| Garmin stress score, mean (0-100) | Time 54-69, pooled (%) | 749 | 372 | -0.683 [-2.072, +0.707] | -0.4502 | -0.96 | 0.335 | not applied (n < 1000) | not applied (n < 1000) | +0.9 | +13.9 | 0.0926 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-69 (%) | 749 | 312 | -0.773 [-2.204, +0.657] | -0.4898 | -1.06 | 0.289 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +13.6 | 0.0932 | 0.0947 |


---

## Band <70

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time < 70, pooled (%) | 2138 | 1259 | +0.028 [-0.093, +0.150] | 0.01604 | 0.46 | 0.647 | 0.795 | 0.743 | +1.8 | +26.4 | 0.0905 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time < 70 (%) | 2138 | 1058 | +0.017 [-0.107, +0.141] | 0.009752 | 0.27 | 0.789 | 0.868 | 0.815 | +1.9 | +26.6 | 0.0904 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time < 70, pooled (%) | 2138 | 1259 | OR 1.038 [0.948, 1.136] | 0.02106 | 0.81 | 0.418 | 0.591 | 0.447 | +1.3 | +15.0 | 0.6598 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 70 (%) | 2138 | 1058 | OR 1.051 [0.961, 1.150] | 0.02873 | 1.09 | 0.275 | 0.444 | 0.316 | +0.8 | +14.4 | 0.6600 | 0.6603 |
| MoCA memory index score (0-15) | Time < 70, pooled (%) | 2138 | 1259 | +0.022 [-0.073, +0.116] | 0.01226 | 0.45 | 0.652 | 0.795 | 0.748 | +1.9 | +7.2 | 0.0621 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time < 70 (%) | 2138 | 1058 | -0.018 [-0.119, +0.082] | -0.01043 | -0.35 | 0.723 | 0.837 | 0.773 | +1.9 | +7.3 | 0.0619 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time < 70, pooled (%) | 2135 | 1258 | +0.046 [-0.154, +0.246] | 0.02593 | 0.45 | 0.652 | 0.795 | 0.722 | +1.8 | +2.1 | 0.0907 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 70 (%) | 2135 | 1057 | +0.080 [-0.123, +0.282] | 0.04571 | 0.77 | 0.441 | 0.611 | 0.620 | +1.4 | +1.6 | 0.0909 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 70, pooled (%) | 2135 | 1258 | OR 1.019 [0.915, 1.136] | 0.0108 | 0.35 | 0.728 | 0.838 | 0.779 | +1.9 | +4.6 | 0.6670 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 70 (%) | 2135 | 1057 | OR 1.024 [0.920, 1.139] | 0.01347 | 0.43 | 0.665 | 0.803 | 0.756 | +1.8 | +4.5 | 0.6671 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 70, pooled (%) | 2100 | 1234 | +0.048 [-0.005, +0.102] | 0.02707 | 1.78 | 0.075 | 0.184 | 0.173 | -4.1 | +6.8 | 0.1399 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 70 (%) | 2100 | 1034 | +0.054 [-0.002, +0.110] | 0.03101 | 1.91 | 0.057 | 0.147 | 0.173 | -5.8 | +5.1 | 0.1405 | 0.1387 |
| Indoor temperature, mean (deg C) | Time < 70, pooled (%) | 2100 | 1234 | +0.068 [-0.014, +0.150] | 0.03806 | 1.63 | 0.103 | 0.218 | 0.801 | -0.4 | -1.9 | 0.2897 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time < 70 (%) | 2100 | 1034 | +0.075 [-0.008, +0.157] | 0.04263 | 1.77 | 0.076 | 0.184 | 0.801 | -0.9 | -2.4 | 0.2900 | 0.2896 |
| Indoor relative humidity, mean (%) | Time < 70, pooled (%) | 2100 | 1234 | -0.188 [-0.448, +0.073] | -0.1051 | -1.41 | 0.159 | 0.312 | 0.898 | -0.0 | -1.9 | 0.2304 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time < 70 (%) | 2100 | 1034 | -0.194 [-0.454, +0.065] | -0.1111 | -1.47 | 0.141 | 0.283 | 0.898 | -0.2 | -2.1 | 0.2305 | 0.2307 |
| Indoor VOC index, mean | Time < 70, pooled (%) | 2100 | 1234 | +0.113 [-0.568, +0.793] | 0.06307 | 0.32 | 0.746 | 0.844 | 0.868 | +1.9 | +1.9 | 0.0262 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time < 70 (%) | 2100 | 1034 | +0.113 [-0.558, +0.785] | 0.06469 | 0.33 | 0.741 | 0.844 | 0.868 | +1.9 | +1.9 | 0.0263 | 0.0271 |
| Steps per wear-day | Time < 70, pooled (%) | 1872 | 1124 | -230.881 [-404.614, -57.147] | -124.7 | -2.60 | 0.009** | 0.033 (FDR<0.05) | 0.077 | -3.5 | +4.5 | 0.1236 | 0.1222 |
| Steps per wear-day | Avg. daily time < 70 (%) | 1872 | 942 | -230.175 [-405.202, -55.148] | -126.2 | -2.58 | 0.010** | 0.035 (FDR<0.05) | 0.077 | -3.5 | +4.5 | 0.1235 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 70, pooled (%) | 1872 | 1124 | -0.469 [-0.985, +0.047] | -0.2532 | -1.78 | 0.075 | 0.184 | 0.192 | -0.5 | +7.7 | 0.1445 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 70 (%) | 1872 | 942 | -0.504 [-1.033, +0.026] | -0.2762 | -1.86 | 0.062 | 0.158 | 0.192 | -0.9 | +7.3 | 0.1446 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 70, pooled (%) | 1877 | 1129 | -0.117 [-0.446, +0.213] | -0.063 | -0.69 | 0.488 | 0.656 | 0.541 | +1.6 | +72.8 | 0.1479 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 70 (%) | 1877 | 946 | -0.144 [-0.496, +0.208] | -0.07921 | -0.80 | 0.422 | 0.595 | 0.485 | +1.4 | +72.6 | 0.1480 | 0.1482 |
| Total sleep time per night (min) | Time < 70, pooled (%) | 1893 | 1147 | +1.233 [-1.427, +3.893] | 0.6698 | 0.91 | 0.364 | 0.528 | 0.512 | +1.4 | +10.3 | 0.0205 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time < 70 (%) | 1893 | 965 | +1.008 [-1.587, +3.603] | 0.5559 | 0.76 | 0.446 | 0.617 | 0.577 | +1.6 | +10.5 | 0.0203 | 0.0209 |
| Garmin stress score, mean (0-100) | Time < 70, pooled (%) | 1879 | 1130 | -0.417 [-1.222, +0.389] | -0.2253 | -1.01 | 0.311 | 0.482 | 0.344 | +0.9 | +61.3 | 0.0897 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time < 70 (%) | 1879 | 947 | -0.489 [-1.350, +0.372] | -0.2685 | -1.11 | 0.266 | 0.439 | 0.305 | +0.5 | +60.9 | 0.0895 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time < 70, pooled (%) | 1271 | 831 | +0.025 [-0.100, +0.151] | 0.01435 | 0.40 | 0.692 | 0.932 | 0.820 | +1.9 | +15.6 | 0.0780 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time < 70 (%) | 1271 | 700 | +0.021 [-0.102, +0.144] | 0.01265 | 0.34 | 0.736 | 0.932 | 0.820 | +1.9 | +15.6 | 0.0781 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time < 70, pooled (%) | 1271 | 831 | OR 1.068 [0.948, 1.203] | 0.03715 | 1.08 | 0.280 | 0.654 | 0.482 | +0.9 | +0.7 | 0.6444 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 70 (%) | 1271 | 700 | OR 1.076 [0.957, 1.210] | 0.04366 | 1.22 | 0.222 | 0.594 | 0.480 | +0.6 | +0.3 | 0.6438 | 0.6443 |
| MoCA memory index score (0-15) | Time < 70, pooled (%) | 1271 | 831 | +0.113 [+0.013, +0.213] | 0.06387 | 2.21 | 0.027* | 0.186 | 0.060 | -0.4 | +0.2 | 0.0481 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time < 70 (%) | 1271 | 700 | +0.080 [-0.019, +0.178] | 0.04754 | 1.59 | 0.112 | 0.441 | 0.168 | +0.8 | +1.5 | 0.0475 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time < 70, pooled (%) | 1270 | 831 | +0.009 [-0.261, +0.280] | 0.005361 | 0.07 | 0.945 | 0.981 | 0.953 | +2.0 | +0.0 | 0.0658 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 70 (%) | 1270 | 700 | +0.048 [-0.218, +0.315] | 0.02887 | 0.36 | 0.722 | 0.932 | 0.953 | +1.9 | -0.1 | 0.0660 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 70, pooled (%) | 1270 | 831 | OR 1.033 [0.893, 1.194] | 0.01836 | 0.44 | 0.662 | 0.932 | 0.958 | +1.8 | +0.7 | 0.6723 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 70 (%) | 1270 | 700 | OR 1.021 [0.883, 1.181] | 0.01269 | 0.29 | 0.774 | 0.932 | 0.958 | +1.9 | +0.8 | 0.6722 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 70, pooled (%) | 1251 | 817 | -0.005 [-0.050, +0.039] | -0.003091 | -0.24 | 0.811 | 0.939 | 0.987 | +2.0 | -0.0 | 0.1125 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 70 (%) | 1251 | 687 | -0.004 [-0.051, +0.044] | -0.002172 | -0.15 | 0.880 | 0.964 | 0.987 | +2.0 | -0.0 | 0.1123 | 0.1139 |
| Indoor temperature, mean (deg C) | Time < 70, pooled (%) | 1251 | 817 | +0.086 [-0.012, +0.185] | 0.04875 | 1.72 | 0.085 | 0.404 | 0.674 | -0.6 | -2.5 | 0.2896 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time < 70 (%) | 1251 | 687 | +0.086 [-0.013, +0.185] | 0.05117 | 1.70 | 0.090 | 0.406 | 0.674 | -0.5 | -2.5 | 0.2894 | 0.2892 |
| Indoor relative humidity, mean (%) | Time < 70, pooled (%) | 1251 | 817 | -0.256 [-0.537, +0.024] | -0.1448 | -1.79 | 0.073 | 0.367 | 0.564 | -0.4 | +0.1 | 0.2403 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time < 70 (%) | 1251 | 687 | -0.239 [-0.527, +0.050] | -0.1423 | -1.62 | 0.105 | 0.438 | 0.585 | -0.1 | +0.4 | 0.2399 | 0.2403 |
| Indoor VOC index, mean | Time < 70, pooled (%) | 1251 | 817 | -0.168 [-1.053, +0.717] | -0.09491 | -0.37 | 0.710 | 0.932 | 0.784 | +1.9 | +1.2 | 0.0016 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time < 70 (%) | 1251 | 687 | -0.194 [-1.117, +0.729] | -0.1155 | -0.41 | 0.681 | 0.932 | 0.784 | +1.8 | +1.2 | 0.0017 | 0.0025 |
| Steps per wear-day | Time < 70, pooled (%) | 1125 | 750 | -58.830 [-295.605, +177.945] | -31.84 | -0.49 | 0.626 | 0.932 | 0.958 | +1.7 | +5.0 | 0.1071 | 0.1080 |
| Steps per wear-day | Avg. daily time < 70 (%) | 1125 | 631 | -42.218 [-291.270, +206.834] | -24.1 | -0.33 | 0.740 | 0.932 | 0.958 | +1.9 | +5.2 | 0.1069 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 70, pooled (%) | 1125 | 750 | -0.109 [-0.853, +0.635] | -0.05909 | -0.29 | 0.774 | 0.932 | 0.931 | +1.9 | +5.4 | 0.1235 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 70 (%) | 1125 | 631 | -0.121 [-0.898, +0.656] | -0.06902 | -0.30 | 0.760 | 0.932 | 0.931 | +1.9 | +5.3 | 0.1234 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 70, pooled (%) | 1128 | 752 | +0.060 [-0.329, +0.449] | 0.03263 | 0.30 | 0.761 | 0.932 | 0.843 | +1.9 | +13.1 | 0.1029 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 70 (%) | 1128 | 632 | +0.038 [-0.372, +0.449] | 0.02186 | 0.18 | 0.855 | 0.948 | 0.914 | +2.0 | +13.2 | 0.1024 | 0.1044 |
| Total sleep time per night (min) | Time < 70, pooled (%) | 1137 | 764 | +0.125 [-2.913, +3.163] | 0.06796 | 0.08 | 0.936 | 0.981 | 0.936 | +2.0 | +4.0 | -0.0066 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time < 70 (%) | 1137 | 642 | +0.183 [-2.821, +3.188] | 0.1054 | 0.12 | 0.905 | 0.966 | 0.936 | +2.0 | +4.0 | -0.0065 | -0.0051 |
| Garmin stress score, mean (0-100) | Time < 70, pooled (%) | 1130 | 753 | -0.078 [-1.084, +0.928] | -0.0423 | -0.15 | 0.879 | 0.964 | 0.940 | +2.0 | +9.8 | 0.0493 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time < 70 (%) | 1130 | 633 | -0.181 [-1.295, +0.934] | -0.1033 | -0.32 | 0.751 | 0.932 | 0.895 | +1.9 | +9.7 | 0.0490 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time < 70, pooled (%) | 867 | 428 | -0.001 [-0.239, +0.237] | -0.0007986 | -0.01 | 0.991 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0517 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time < 70 (%) | 867 | 358 | -0.008 [-0.246, +0.231] | -0.004084 | -0.06 | 0.951 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0519 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time < 70, pooled (%) | 867 | 428 | OR 1.032 [0.898, 1.187] | 0.01773 | 0.44 | 0.656 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +3.5 | 0.6396 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 70 (%) | 867 | 358 | OR 1.045 [0.908, 1.202] | 0.0238 | 0.61 | 0.542 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +3.3 | 0.6406 | 0.6425 |
| MoCA memory index score (0-15) | Time < 70, pooled (%) | 867 | 428 | -0.123 [-0.286, +0.041] | -0.06861 | -1.47 | 0.141 | not applied (n < 1000) | not applied (n < 1000) | +0.3 | +2.0 | 0.0297 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time < 70 (%) | 867 | 358 | -0.157 [-0.324, +0.011] | -0.08541 | -1.84 | 0.066 | not applied (n < 1000) | not applied (n < 1000) | -0.9 | +0.9 | 0.0308 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time < 70, pooled (%) | 865 | 427 | +0.109 [-0.238, +0.457] | 0.06113 | 0.62 | 0.538 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +2.9 | 0.0783 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 70 (%) | 865 | 357 | +0.134 [-0.218, +0.487] | 0.07316 | 0.75 | 0.455 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | +2.6 | 0.0784 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 70, pooled (%) | 865 | 427 | OR 1.009 [0.859, 1.186] | 0.005217 | 0.11 | 0.910 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +5.0 | 0.6313 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 70 (%) | 865 | 357 | OR 1.031 [0.880, 1.207] | 0.01661 | 0.38 | 0.705 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +4.9 | 0.6315 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 70, pooled (%) | 849 | 417 | +0.137 [+0.047, +0.227] | 0.07601 | 2.98 | 0.003** | not applied (n < 1000) | not applied (n < 1000) | -16.8 | -7.4 | 0.1435 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 70 (%) | 849 | 347 | +0.140 [+0.044, +0.237] | 0.07572 | 2.86 | 0.004** | not applied (n < 1000) | not applied (n < 1000) | -17.8 | -8.4 | 0.1439 | 0.1310 |
| Indoor temperature, mean (deg C) | Time < 70, pooled (%) | 849 | 417 | +0.056 [-0.091, +0.204] | 0.03131 | 0.75 | 0.454 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | -0.3 | 0.2253 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time < 70 (%) | 849 | 347 | +0.073 [-0.076, +0.221] | 0.03916 | 0.96 | 0.339 | not applied (n < 1000) | not applied (n < 1000) | +1.0 | -0.7 | 0.2254 | 0.2264 |
| Indoor relative humidity, mean (%) | Time < 70, pooled (%) | 849 | 417 | -0.080 [-0.601, +0.442] | -0.04425 | -0.30 | 0.764 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | -0.0 | 0.1839 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time < 70 (%) | 849 | 347 | -0.132 [-0.634, +0.370] | -0.07117 | -0.52 | 0.606 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.3 | 0.1844 | 0.1857 |
| Indoor VOC index, mean | Time < 70, pooled (%) | 849 | 417 | +0.533 [-0.463, +1.529] | 0.2955 | 1.05 | 0.295 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +1.5 | 0.0273 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time < 70 (%) | 849 | 347 | +0.541 [-0.413, +1.494] | 0.2914 | 1.11 | 0.267 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +1.5 | 0.0274 | 0.0276 |
| Steps per wear-day | Time < 70, pooled (%) | 747 | 374 | -411.853 [-697.727, -125.980] | -221.8 | -2.82 | 0.005** | not applied (n < 1000) | not applied (n < 1000) | -3.4 | -3.3 | 0.1428 | 0.1390 |
| Steps per wear-day | Avg. daily time < 70 (%) | 747 | 311 | -423.808 [-680.504, -167.112] | -219.9 | -3.24 | 0.001** | not applied (n < 1000) | not applied (n < 1000) | -3.7 | -3.6 | 0.1438 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 70, pooled (%) | 747 | 374 | -0.820 [-1.645, +0.006] | -0.4415 | -1.95 | 0.052 | not applied (n < 1000) | not applied (n < 1000) | -0.6 | -0.6 | 0.1552 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 70 (%) | 747 | 311 | -0.881 [-1.693, -0.069] | -0.4571 | -2.13 | 0.033* | not applied (n < 1000) | not applied (n < 1000) | -1.0 | -1.0 | 0.1559 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 70, pooled (%) | 749 | 377 | -0.113 [-0.702, +0.476] | -0.0611 | -0.38 | 0.706 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +7.9 | 0.1239 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 70 (%) | 749 | 314 | -0.241 [-0.899, +0.418] | -0.125 | -0.72 | 0.474 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +7.5 | 0.1244 | 0.1253 |
| Total sleep time per night (min) | Time < 70, pooled (%) | 756 | 383 | +2.832 [-2.243, +7.907] | 1.532 | 1.09 | 0.274 | not applied (n < 1000) | not applied (n < 1000) | +0.7 | +3.6 | 0.0057 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time < 70 (%) | 756 | 323 | +2.140 [-2.722, +7.002] | 1.116 | 0.86 | 0.388 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | +4.2 | 0.0050 | 0.0066 |
| Garmin stress score, mean (0-100) | Time < 70, pooled (%) | 749 | 377 | -0.474 [-1.927, +0.980] | -0.2554 | -0.64 | 0.523 | not applied (n < 1000) | not applied (n < 1000) | +1.5 | +14.5 | 0.0919 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time < 70 (%) | 749 | 314 | -0.626 [-2.116, +0.863] | -0.3255 | -0.82 | 0.410 | not applied (n < 1000) | not applied (n < 1000) | +1.0 | +14.1 | 0.0925 | 0.0947 |


---

## Band 54-250

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-250, pooled (%) | 2138 | 2138 | +0.268 [+0.111, +0.426] | 0.02436 | 3.34 | 8.2e-04*** | 0.004 (FDR<0.05) | 0.001 (FDR<0.05) | -14.6 | +10.0 | 0.0973 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time 54-250 (%) | 2138 | 2138 | +0.265 [+0.105, +0.425] | 0.02431 | 3.24 | 0.001** | 0.006 (FDR<0.05) | 0.002 (FDR<0.05) | -14.2 | +10.5 | 0.0970 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time 54-250, pooled (%) | 2138 | 2138 | OR 0.869 [0.790, 0.956] | -0.01276 | -2.89 | 0.004** | 0.017 (FDR<0.05) | 0.007 (FDR<0.05) | -6.9 | +6.7 | 0.6630 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-250 (%) | 2138 | 2138 | OR 0.872 [0.793, 0.959] | -0.01258 | -2.81 | 0.005** | 0.020 (FDR<0.05) | 0.008 (FDR<0.05) | -6.4 | +7.2 | 0.6628 | 0.6603 |
| MoCA memory index score (0-15) | Time 54-250, pooled (%) | 2138 | 2138 | +0.123 [+0.013, +0.233] | 0.01116 | 2.20 | 0.028* | 0.087 | 0.051 | -2.5 | +2.9 | 0.0643 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time 54-250 (%) | 2138 | 2138 | +0.120 [+0.011, +0.229] | 0.01103 | 2.15 | 0.032* | 0.093 | 0.051 | -2.3 | +3.1 | 0.0642 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time 54-250, pooled (%) | 2135 | 2135 | -0.144 [-0.404, +0.116] | -0.01304 | -1.08 | 0.278 | 0.445 | 0.620 | +0.1 | +0.4 | 0.0915 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-250 (%) | 2135 | 2135 | -0.131 [-0.392, +0.131] | -0.01201 | -0.98 | 0.327 | 0.495 | 0.620 | +0.4 | +0.7 | 0.0914 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-250, pooled (%) | 2135 | 2135 | OR 0.929 [0.844, 1.023] | -0.006643 | -1.50 | 0.135 | 0.272 | 0.245 | -0.2 | +2.5 | 0.6692 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-250 (%) | 2135 | 2135 | OR 0.937 [0.851, 1.033] | -0.005932 | -1.31 | 0.190 | 0.351 | 0.295 | +0.3 | +3.0 | 0.6689 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-250, pooled (%) | 2100 | 2100 | -0.043 [-0.094, +0.008] | -0.003863 | -1.64 | 0.100 | 0.214 | 0.173 | -2.6 | +8.3 | 0.1391 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-250 (%) | 2100 | 2100 | -0.043 [-0.094, +0.008] | -0.003941 | -1.66 | 0.097 | 0.210 | 0.173 | -2.7 | +8.2 | 0.1392 | 0.1387 |
| Indoor temperature, mean (deg C) | Time 54-250, pooled (%) | 2100 | 2100 | -0.024 [-0.122, +0.074] | -0.00221 | -0.49 | 0.625 | 0.778 | 0.982 | +1.7 | +0.2 | 0.2890 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-250 (%) | 2100 | 2100 | -0.021 [-0.119, +0.078] | -0.001916 | -0.42 | 0.677 | 0.805 | 0.982 | +1.8 | +0.3 | 0.2890 | 0.2896 |
| Indoor relative humidity, mean (%) | Time 54-250, pooled (%) | 2100 | 2100 | +0.004 [-0.268, +0.276] | 0.0003887 | 0.03 | 0.975 | 0.986 | 0.992 | +2.0 | +0.1 | 0.2299 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-250 (%) | 2100 | 2100 | +0.001 [-0.275, +0.278] | 0.0001247 | 0.01 | 0.992 | 0.995 | 0.992 | +2.0 | +0.1 | 0.2298 | 0.2307 |
| Indoor VOC index, mean | Time 54-250, pooled (%) | 2100 | 2100 | +0.696 [-0.098, +1.490] | 0.06296 | 1.72 | 0.086 | 0.195 | 0.665 | -1.8 | -1.8 | 0.0271 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time 54-250 (%) | 2100 | 2100 | +0.727 [-0.082, +1.535] | 0.06658 | 1.76 | 0.078 | 0.187 | 0.665 | -2.1 | -2.1 | 0.0272 | 0.0271 |
| Steps per wear-day | Time 54-250, pooled (%) | 1872 | 1872 | -7.846 [-269.806, +254.114] | -0.716 | -0.06 | 0.953 | 0.973 | 0.953 | +2.0 | +10.0 | 0.1205 | 0.1222 |
| Steps per wear-day | Avg. daily time 54-250 (%) | 1872 | 1872 | -11.532 [-265.942, +242.879] | -1.07 | -0.09 | 0.929 | 0.958 | 0.953 | +2.0 | +10.0 | 0.1205 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-250, pooled (%) | 1872 | 1872 | -0.082 [-0.819, +0.655] | -0.007468 | -0.22 | 0.828 | 0.892 | 0.828 | +1.9 | +10.1 | 0.1433 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-250 (%) | 1872 | 1872 | -0.090 [-0.806, +0.626] | -0.008357 | -0.25 | 0.805 | 0.876 | 0.828 | +1.9 | +10.1 | 0.1433 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-250, pooled (%) | 1877 | 1877 | -1.006 [-1.452, -0.560] | -0.09173 | -4.42 | 9.8e-06*** | 8.0e-05 (FDR<0.05) | 1.4e-05 (FDR<0.05) | -25.7 | +45.5 | 0.1596 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-250 (%) | 1877 | 1877 | -1.001 [-1.455, -0.548] | -0.09281 | -4.33 | 1.5e-05*** | 1.1e-04 (FDR<0.05) | 1.9e-05 (FDR<0.05) | -25.5 | +45.7 | 0.1594 | 0.1482 |
| Total sleep time per night (min) | Time 54-250, pooled (%) | 1893 | 1893 | +1.040 [-1.902, +3.981] | 0.09849 | 0.69 | 0.488 | 0.656 | 0.582 | +1.6 | +10.5 | 0.0205 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time 54-250 (%) | 1893 | 1893 | +0.959 [-2.004, +3.922] | 0.09236 | 0.63 | 0.526 | 0.693 | 0.582 | +1.6 | +10.5 | 0.0204 | 0.0209 |
| Garmin stress score, mean (0-100) | Time 54-250, pooled (%) | 1879 | 1879 | -1.930 [-2.908, -0.952] | -0.1761 | -3.87 | 1.1e-04*** | 6.5e-04 (FDR<0.05) | 1.6e-04 (FDR<0.05) | -20.4 | +40.0 | 0.0998 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-250 (%) | 1879 | 1879 | -1.922 [-2.912, -0.932] | -0.1782 | -3.80 | 1.4e-04*** | 8.0e-04 (FDR<0.05) | 1.9e-04 (FDR<0.05) | -20.2 | +40.2 | 0.0996 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-250, pooled (%) | 1271 | 1271 | +0.272 [-0.037, +0.582] | 0.05585 | 1.73 | 0.084 | 0.404 | 0.138 | -10.6 | +3.1 | 0.0799 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time 54-250 (%) | 1271 | 1271 | +0.273 [-0.042, +0.588] | 0.05714 | 1.70 | 0.089 | 0.406 | 0.138 | -10.7 | +3.0 | 0.0798 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time 54-250, pooled (%) | 1271 | 1271 | OR 0.974 [0.865, 1.097] | -0.00545 | -0.44 | 0.661 | 0.932 | 0.834 | +1.8 | +1.6 | 0.6434 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-250 (%) | 1271 | 1271 | OR 0.977 [0.868, 1.100] | -0.004834 | -0.38 | 0.703 | 0.932 | 0.834 | +1.9 | +1.6 | 0.6434 | 0.6443 |
| MoCA memory index score (0-15) | Time 54-250, pooled (%) | 1271 | 1271 | +0.166 [+0.045, +0.288] | 0.03412 | 2.69 | 0.007** | 0.090 | 0.025 (FDR<0.05) | -3.4 | -2.7 | 0.0504 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time 54-250 (%) | 1271 | 1271 | +0.173 [+0.053, +0.293] | 0.03621 | 2.82 | 0.005** | 0.068 | 0.020 (FDR<0.05) | -3.8 | -3.2 | 0.0506 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time 54-250, pooled (%) | 1270 | 1270 | +0.132 [-0.159, +0.423] | 0.02713 | 0.89 | 0.373 | 0.771 | 0.953 | +1.0 | -1.0 | 0.0665 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-250 (%) | 1270 | 1270 | +0.127 [-0.171, +0.425] | 0.02672 | 0.84 | 0.402 | 0.804 | 0.953 | +1.0 | -1.0 | 0.0664 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-250, pooled (%) | 1270 | 1270 | OR 0.981 [0.864, 1.114] | -0.003937 | -0.30 | 0.768 | 0.932 | 0.958 | +1.9 | +0.8 | 0.6714 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-250 (%) | 1270 | 1270 | OR 0.981 [0.864, 1.113] | -0.004079 | -0.30 | 0.763 | 0.932 | 0.958 | +1.9 | +0.8 | 0.6711 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-250, pooled (%) | 1251 | 1251 | +0.018 [-0.001, +0.038] | 0.003746 | 1.89 | 0.059 | 0.339 | 0.265 | +1.4 | -0.6 | 0.1140 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-250 (%) | 1251 | 1251 | +0.018 [-0.001, +0.036] | 0.003707 | 1.89 | 0.059 | 0.339 | 0.265 | +1.5 | -0.5 | 0.1140 | 0.1139 |
| Indoor temperature, mean (deg C) | Time 54-250, pooled (%) | 1251 | 1251 | -0.035 [-0.176, +0.105] | -0.007218 | -0.50 | 0.620 | 0.932 | 0.915 | +1.6 | -0.4 | 0.2884 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-250 (%) | 1251 | 1251 | -0.030 [-0.167, +0.107] | -0.006304 | -0.43 | 0.664 | 0.932 | 0.936 | +1.7 | -0.3 | 0.2884 | 0.2892 |
| Indoor relative humidity, mean (%) | Time 54-250, pooled (%) | 1251 | 1251 | -0.137 [-0.392, +0.117] | -0.02794 | -1.06 | 0.290 | 0.672 | 0.597 | +1.3 | +1.8 | 0.2400 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-250 (%) | 1251 | 1251 | -0.147 [-0.399, +0.105] | -0.03054 | -1.14 | 0.252 | 0.629 | 0.597 | +1.2 | +1.7 | 0.2401 | 0.2403 |
| Indoor VOC index, mean | Time 54-250, pooled (%) | 1251 | 1251 | +0.560 [-0.084, +1.205] | 0.114 | 1.70 | 0.089 | 0.406 | 0.490 | +0.3 | -0.3 | 0.0029 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time 54-250 (%) | 1251 | 1251 | +0.556 [-0.110, +1.222] | 0.1156 | 1.64 | 0.102 | 0.432 | 0.490 | +0.3 | -0.3 | 0.0028 | 0.0025 |
| Steps per wear-day | Time 54-250, pooled (%) | 1125 | 1125 | -77.498 [-318.954, +163.959] | -17.2 | -0.63 | 0.529 | 0.924 | 0.958 | +1.5 | +4.8 | 0.1073 | 0.1080 |
| Steps per wear-day | Avg. daily time 54-250 (%) | 1125 | 1125 | -82.116 [-314.334, +150.102] | -18.92 | -0.69 | 0.488 | 0.884 | 0.958 | +1.5 | +4.8 | 0.1075 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-250, pooled (%) | 1125 | 1125 | -0.404 [-1.236, +0.428] | -0.08962 | -0.95 | 0.342 | 0.734 | 0.882 | +0.7 | +4.1 | 0.1246 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-250 (%) | 1125 | 1125 | -0.405 [-1.232, +0.422] | -0.09328 | -0.96 | 0.337 | 0.732 | 0.882 | +0.7 | +4.1 | 0.1246 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-250, pooled (%) | 1128 | 1128 | -0.510 [-1.130, +0.111] | -0.1133 | -1.61 | 0.107 | 0.441 | 0.175 | -3.4 | +7.9 | 0.1054 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-250 (%) | 1128 | 1128 | -0.501 [-1.140, +0.138] | -0.1156 | -1.54 | 0.124 | 0.472 | 0.186 | -3.2 | +8.0 | 0.1050 | 0.1044 |
| Total sleep time per night (min) | Time 54-250, pooled (%) | 1137 | 1137 | +0.466 [-2.768, +3.701] | 0.1174 | 0.28 | 0.778 | 0.932 | 0.936 | +1.9 | +3.9 | -0.0060 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time 54-250 (%) | 1137 | 1137 | +0.436 [-2.757, +3.629] | 0.1146 | 0.27 | 0.789 | 0.936 | 0.936 | +1.9 | +4.0 | -0.0059 | -0.0051 |
| Garmin stress score, mean (0-100) | Time 54-250, pooled (%) | 1130 | 1130 | -0.601 [-2.452, +1.250] | -0.1336 | -0.64 | 0.525 | 0.924 | 0.708 | +0.5 | +8.3 | 0.0469 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-250 (%) | 1130 | 1130 | -0.576 [-2.456, +1.303] | -0.1331 | -0.60 | 0.548 | 0.932 | 0.708 | +0.6 | +8.4 | 0.0466 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 54-250, pooled (%) | 867 | 867 | +0.210 [-0.018, +0.438] | 0.01351 | 1.81 | 0.070 | not applied (n < 1000) | not applied (n < 1000) | -1.5 | +0.1 | 0.0565 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time 54-250 (%) | 867 | 867 | +0.206 [-0.024, +0.436] | 0.0134 | 1.76 | 0.079 | not applied (n < 1000) | not applied (n < 1000) | -1.3 | +0.2 | 0.0564 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time 54-250, pooled (%) | 867 | 867 | OR 0.866 [0.748, 1.003] | -0.009233 | -1.92 | 0.055 | not applied (n < 1000) | not applied (n < 1000) | -1.8 | -0.2 | 0.6447 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 54-250 (%) | 867 | 867 | OR 0.869 [0.751, 1.006] | -0.009102 | -1.87 | 0.061 | not applied (n < 1000) | not applied (n < 1000) | -1.7 | +0.0 | 0.6448 | 0.6425 |
| MoCA memory index score (0-15) | Time 54-250, pooled (%) | 867 | 867 | +0.124 [-0.043, +0.291] | 0.007967 | 1.45 | 0.146 | not applied (n < 1000) | not applied (n < 1000) | +0.3 | +2.0 | 0.0299 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time 54-250 (%) | 867 | 867 | +0.117 [-0.049, +0.282] | 0.007585 | 1.38 | 0.168 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +2.2 | 0.0297 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time 54-250, pooled (%) | 865 | 865 | -0.299 [-0.709, +0.111] | -0.01921 | -1.43 | 0.153 | not applied (n < 1000) | not applied (n < 1000) | -1.1 | +0.1 | 0.0788 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 54-250 (%) | 865 | 865 | -0.274 [-0.687, +0.140] | -0.01777 | -1.30 | 0.195 | not applied (n < 1000) | not applied (n < 1000) | -0.6 | +0.7 | 0.0784 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 54-250, pooled (%) | 865 | 865 | OR 0.886 [0.764, 1.028] | -0.007745 | -1.59 | 0.111 | not applied (n < 1000) | not applied (n < 1000) | -0.5 | +2.5 | 0.6365 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 54-250 (%) | 865 | 865 | OR 0.900 [0.775, 1.045] | -0.006827 | -1.38 | 0.167 | not applied (n < 1000) | not applied (n < 1000) | +0.2 | +3.2 | 0.6351 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 54-250, pooled (%) | 849 | 849 | -0.068 [-0.152, +0.016] | -0.004355 | -1.59 | 0.112 | not applied (n < 1000) | not applied (n < 1000) | -2.5 | +7.0 | 0.1314 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 54-250 (%) | 849 | 849 | -0.069 [-0.152, +0.015] | -0.004444 | -1.61 | 0.106 | not applied (n < 1000) | not applied (n < 1000) | -2.5 | +6.9 | 0.1315 | 0.1310 |
| Indoor temperature, mean (deg C) | Time 54-250, pooled (%) | 849 | 849 | +0.026 [-0.135, +0.186] | 0.001641 | 0.31 | 0.754 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2227 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time 54-250 (%) | 849 | 849 | +0.028 [-0.133, +0.189] | 0.001787 | 0.34 | 0.737 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2227 | 0.2264 |
| Indoor relative humidity, mean (%) | Time 54-250, pooled (%) | 849 | 849 | +0.087 [-0.358, +0.532] | 0.005567 | 0.38 | 0.702 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | -0.0 | 0.1840 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time 54-250 (%) | 849 | 849 | +0.087 [-0.365, +0.539] | 0.005617 | 0.38 | 0.707 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | -0.0 | 0.1839 | 0.1857 |
| Indoor VOC index, mean | Time 54-250, pooled (%) | 849 | 849 | +1.109 [-0.203, +2.420] | 0.07101 | 1.66 | 0.098 | not applied (n < 1000) | not applied (n < 1000) | -1.4 | -1.1 | 0.0290 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time 54-250 (%) | 849 | 849 | +1.161 [-0.176, +2.497] | 0.07517 | 1.70 | 0.089 | not applied (n < 1000) | not applied (n < 1000) | -1.7 | -1.4 | 0.0293 | 0.0276 |
| Steps per wear-day | Time 54-250, pooled (%) | 747 | 747 | +94.194 [-327.618, +516.007] | 5.99 | 0.44 | 0.662 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +1.8 | 0.1374 | 0.1390 |
| Steps per wear-day | Avg. daily time 54-250 (%) | 747 | 747 | +83.275 [-323.087, +489.637] | 5.368 | 0.40 | 0.688 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +1.9 | 0.1375 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 54-250, pooled (%) | 747 | 747 | +0.308 [-0.851, +1.466] | 0.01956 | 0.52 | 0.603 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +1.7 | 0.1533 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 54-250 (%) | 747 | 747 | +0.275 [-0.841, +1.392] | 0.01776 | 0.48 | 0.629 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +1.8 | 0.1533 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 54-250, pooled (%) | 749 | 749 | -0.672 [-1.334, -0.010] | -0.04271 | -1.99 | 0.047* | not applied (n < 1000) | not applied (n < 1000) | -2.7 | +3.4 | 0.1282 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 54-250 (%) | 749 | 749 | -0.682 [-1.346, -0.018] | -0.04394 | -2.01 | 0.044* | not applied (n < 1000) | not applied (n < 1000) | -2.8 | +3.2 | 0.1281 | 0.1253 |
| Total sleep time per night (min) | Time 54-250, pooled (%) | 756 | 756 | +0.486 [-4.296, +5.268] | 0.03181 | 0.20 | 0.842 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +4.9 | 0.0044 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time 54-250 (%) | 756 | 756 | +0.422 [-4.384, +5.228] | 0.02802 | 0.17 | 0.863 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +4.9 | 0.0043 | 0.0066 |
| Garmin stress score, mean (0-100) | Time 54-250, pooled (%) | 749 | 749 | -1.776 [-3.266, -0.285] | -0.1129 | -2.33 | 0.020* | not applied (n < 1000) | not applied (n < 1000) | -5.5 | +7.6 | 0.1011 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time 54-250 (%) | 749 | 749 | -1.795 [-3.297, -0.294] | -0.1156 | -2.34 | 0.019* | not applied (n < 1000) | not applied (n < 1000) | -5.7 | +7.4 | 0.1012 | 0.0947 |


---

## Band >180

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time > 180, pooled (%) | 2138 | 1927 | -0.355 [-0.503, -0.207] | -0.01748 | -4.71 | 2.4e-06*** | 2.4e-05 (FDR<0.05) | 9.3e-06 (FDR<0.05) | -26.3 | -1.6 | 0.1021 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time > 180 (%) | 2138 | 1876 | -0.349 [-0.497, -0.201] | -0.01713 | -4.61 | 4.0e-06*** | 3.7e-05 (FDR<0.05) | 1.1e-05 (FDR<0.05) | -25.3 | -0.6 | 0.1017 | 0.0915 |
| MoCA total score (0-30) | Nocturnal time > 180 (%) | 2138 | 1109 | -0.317 [-0.467, -0.167] | -0.01568 | -4.15 | 3.3e-05*** | 2.3e-04 (FDR<0.05) | 6.9e-05 (FDR<0.05) | -20.7 | +3.9 | 0.1001 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time > 180, pooled (%) | 2138 | 1927 | OR 1.203 [1.096, 1.320] | 0.009094 | 3.89 | 9.9e-05*** | 6.1e-04 (FDR<0.05) | 3.4e-04 (FDR<0.05) | -13.4 | +0.2 | 0.6653 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 180 (%) | 2138 | 1876 | OR 1.200 [1.094, 1.317] | 0.008958 | 3.84 | 1.2e-04*** | 7.0e-04 (FDR<0.05) | 3.4e-04 (FDR<0.05) | -13.0 | +0.6 | 0.6650 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Nocturnal time > 180 (%) | 2138 | 1109 | OR 1.169 [1.066, 1.282] | 0.007721 | 3.31 | 9.3e-04*** | 0.005 (FDR<0.05) | 0.002 (FDR<0.05) | -9.1 | +4.5 | 0.6634 | 0.6603 |
| MoCA memory index score (0-15) | Time > 180, pooled (%) | 2138 | 1927 | -0.167 [-0.281, -0.053] | -0.008234 | -2.88 | 0.004** | 0.017 (FDR<0.05) | 0.016 (FDR<0.05) | -6.1 | -0.7 | 0.0657 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time > 180 (%) | 2138 | 1876 | -0.164 [-0.278, -0.050] | -0.008052 | -2.82 | 0.005** | 0.020 (FDR<0.05) | 0.017 (FDR<0.05) | -5.7 | -0.4 | 0.0655 | 0.0630 |
| MoCA memory index score (0-15) | Nocturnal time > 180 (%) | 2138 | 1109 | -0.154 [-0.267, -0.040] | -0.007592 | -2.66 | 0.008** | 0.029 (FDR<0.05) | 0.021 (FDR<0.05) | -4.8 | +0.5 | 0.0652 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time > 180, pooled (%) | 2135 | 1924 | +0.138 [-0.097, +0.373] | 0.006793 | 1.15 | 0.249 | 0.416 | 0.620 | +0.3 | +0.6 | 0.0917 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 180 (%) | 2135 | 1873 | +0.130 [-0.105, +0.365] | 0.006398 | 1.09 | 0.277 | 0.445 | 0.620 | +0.5 | +0.7 | 0.0916 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Nocturnal time > 180 (%) | 2135 | 1106 | +0.222 [-0.017, +0.461] | 0.01097 | 1.82 | 0.069 | 0.172 | 0.620 | -2.4 | -2.2 | 0.0930 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 180, pooled (%) | 2135 | 1924 | OR 1.114 [1.003, 1.236] | 0.005303 | 2.02 | 0.043* | 0.124 | 0.158 | -2.0 | +0.7 | 0.6692 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 180 (%) | 2135 | 1873 | OR 1.109 [0.999, 1.231] | 0.005081 | 1.94 | 0.053 | 0.141 | 0.158 | -1.6 | +1.1 | 0.6691 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Nocturnal time > 180 (%) | 2135 | 1106 | OR 1.165 [1.054, 1.288] | 0.007555 | 2.99 | 0.003** | 0.012 (FDR<0.05) | 0.043 (FDR<0.05) | -6.6 | -3.9 | 0.6737 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 180, pooled (%) | 2100 | 1896 | +0.040 [-0.006, +0.086] | 0.001952 | 1.70 | 0.090 | 0.202 | 0.173 | -1.9 | +9.0 | 0.1391 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 180 (%) | 2100 | 1846 | +0.039 [-0.007, +0.085] | 0.001921 | 1.67 | 0.094 | 0.208 | 0.173 | -1.8 | +9.1 | 0.1391 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Nocturnal time > 180 (%) | 2100 | 1095 | +0.047 [+0.000, +0.093] | 0.002313 | 1.98 | 0.048* | 0.132 | 0.173 | -3.5 | +7.5 | 0.1394 | 0.1387 |
| Indoor temperature, mean (deg C) | Time > 180, pooled (%) | 2100 | 1896 | +0.020 [-0.075, +0.115] | 0.0009689 | 0.41 | 0.684 | 0.805 | 0.982 | +1.8 | +0.3 | 0.2890 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time > 180 (%) | 2100 | 1846 | +0.016 [-0.079, +0.112] | 0.0007993 | 0.34 | 0.737 | 0.842 | 0.982 | +1.9 | +0.4 | 0.2890 | 0.2896 |
| Indoor temperature, mean (deg C) | Nocturnal time > 180 (%) | 2100 | 1095 | +0.013 [-0.084, +0.109] | 0.0006301 | 0.26 | 0.795 | 0.872 | 0.982 | +1.9 | +0.4 | 0.2889 | 0.2896 |
| Indoor relative humidity, mean (%) | Time > 180, pooled (%) | 2100 | 1896 | -0.050 [-0.328, +0.228] | -0.002454 | -0.35 | 0.725 | 0.837 | 0.898 | +1.9 | +0.0 | 0.2300 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time > 180 (%) | 2100 | 1846 | -0.045 [-0.324, +0.234] | -0.002195 | -0.32 | 0.753 | 0.844 | 0.898 | +1.9 | +0.0 | 0.2300 | 0.2307 |
| Indoor relative humidity, mean (%) | Nocturnal time > 180 (%) | 2100 | 1095 | -0.088 [-0.362, +0.187] | -0.004339 | -0.63 | 0.530 | 0.693 | 0.898 | +1.6 | -0.3 | 0.2300 | 0.2307 |
| Indoor VOC index, mean | Time > 180, pooled (%) | 2100 | 1896 | -0.183 [-1.063, +0.696] | -0.009003 | -0.41 | 0.683 | 0.805 | 0.868 | +1.7 | +1.7 | 0.0256 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time > 180 (%) | 2100 | 1846 | -0.207 [-1.091, +0.676] | -0.01014 | -0.46 | 0.646 | 0.795 | 0.868 | +1.7 | +1.7 | 0.0256 | 0.0271 |
| Indoor VOC index, mean | Nocturnal time > 180 (%) | 2100 | 1095 | -0.153 [-1.120, +0.814] | -0.007573 | -0.31 | 0.756 | 0.846 | 0.868 | +1.8 | +1.8 | 0.0251 | 0.0271 |
| Steps per wear-day | Time > 180, pooled (%) | 1872 | 1677 | +146.772 [-110.327, +403.871] | 7.299 | 1.12 | 0.263 | 0.438 | 0.383 | -0.1 | +7.9 | 0.1219 | 0.1222 |
| Steps per wear-day | Avg. daily time > 180 (%) | 1872 | 1628 | +145.835 [-111.304, +402.974] | 7.23 | 1.11 | 0.266 | 0.439 | 0.383 | -0.1 | +7.9 | 0.1219 | 0.1222 |
| Steps per wear-day | Nocturnal time > 180 (%) | 1872 | 959 | +148.405 [-116.365, +413.176] | 7.406 | 1.10 | 0.272 | 0.440 | 0.383 | -0.1 | +7.8 | 0.1216 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 180, pooled (%) | 1872 | 1677 | +0.443 [-0.284, +1.170] | 0.02202 | 1.19 | 0.232 | 0.400 | 0.313 | -0.1 | +8.1 | 0.1446 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 180 (%) | 1872 | 1628 | +0.445 [-0.284, +1.173] | 0.02204 | 1.20 | 0.232 | 0.400 | 0.313 | -0.1 | +8.1 | 0.1445 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Nocturnal time > 180 (%) | 1872 | 959 | +0.400 [-0.348, +1.149] | 0.01997 | 1.05 | 0.295 | 0.467 | 0.351 | +0.3 | +8.4 | 0.1443 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 180, pooled (%) | 1877 | 1680 | +1.673 [+1.249, +2.098] | 0.08311 | 7.72 | 1.2e-14*** | 6.3e-13 (FDR<0.05) | 5.2e-14 (FDR<0.05) | -73.2 | -1.9 | 0.1804 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 180 (%) | 1877 | 1631 | +1.667 [+1.242, +2.091] | 0.08253 | 7.70 | 1.4e-14*** | 6.8e-13 (FDR<0.05) | 5.4e-14 (FDR<0.05) | -72.5 | -1.3 | 0.1801 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Nocturnal time > 180 (%) | 1877 | 960 | +1.369 [+0.942, +1.796] | 0.06833 | 6.28 | 3.3e-10*** | 5.5e-09 (FDR<0.05) | 6.4e-10 (FDR<0.05) | -48.3 | +22.9 | 0.1697 | 0.1482 |
| Total sleep time per night (min) | Time > 180, pooled (%) | 1893 | 1699 | -2.019 [-5.179, +1.142] | -0.1017 | -1.25 | 0.211 | 0.376 | 0.403 | +0.4 | +9.3 | 0.0204 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time > 180 (%) | 1893 | 1652 | -1.956 [-5.130, +1.219] | -0.09821 | -1.21 | 0.227 | 0.398 | 0.403 | +0.5 | +9.4 | 0.0203 | 0.0209 |
| Total sleep time per night (min) | Nocturnal time > 180 (%) | 1893 | 969 | -0.672 [-3.781, +2.437] | -0.03407 | -0.42 | 0.672 | 0.805 | 0.718 | +1.8 | +10.7 | 0.0200 | 0.0209 |
| Garmin stress score, mean (0-100) | Time > 180, pooled (%) | 1879 | 1681 | +3.006 [+2.131, +3.881] | 0.1494 | 6.73 | 1.7e-11*** | 3.8e-10 (FDR<0.05) | 8.5e-11 (FDR<0.05) | -50.9 | +9.5 | 0.1145 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time > 180 (%) | 1879 | 1632 | +2.982 [+2.108, +3.856] | 0.1477 | 6.68 | 2.3e-11*** | 4.8e-10 (FDR<0.05) | 9.0e-11 (FDR<0.05) | -50.0 | +10.4 | 0.1141 | 0.0902 |
| Garmin stress score, mean (0-100) | Nocturnal time > 180 (%) | 1879 | 962 | +2.415 [+1.545, +3.285] | 0.1206 | 5.44 | 5.3e-08*** | 6.4e-07 (FDR<0.05) | 1.0e-07 (FDR<0.05) | -32.2 | +28.2 | 0.1058 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time > 180, pooled (%) | 1271 | 1094 | -0.333 [-0.552, -0.115] | -0.03752 | -2.99 | 0.003** | 0.052 | 0.011 (FDR<0.05) | -16.8 | -3.1 | 0.0877 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time > 180 (%) | 1271 | 1049 | -0.329 [-0.547, -0.110] | -0.0369 | -2.95 | 0.003** | 0.052 | 0.011 (FDR<0.05) | -16.3 | -2.6 | 0.0874 | 0.0789 |
| MoCA total score (0-30) | Nocturnal time > 180 (%) | 1271 | 446 | -0.264 [-0.490, -0.038] | -0.03131 | -2.29 | 0.022* | 0.158 | 0.052 | -9.8 | +3.9 | 0.0833 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time > 180, pooled (%) | 1271 | 1094 | OR 1.073 [0.952, 1.209] | 0.007921 | 1.15 | 0.249 | 0.628 | 0.480 | +0.7 | +0.5 | 0.6438 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 180 (%) | 1271 | 1049 | OR 1.071 [0.950, 1.207] | 0.00766 | 1.12 | 0.263 | 0.641 | 0.480 | +0.7 | +0.5 | 0.6435 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Nocturnal time > 180 (%) | 1271 | 446 | OR 1.002 [0.888, 1.130] | 0.000215 | 0.03 | 0.976 | 0.988 | 0.976 | +2.0 | +1.8 | 0.6430 | 0.6443 |
| MoCA memory index score (0-15) | Time > 180, pooled (%) | 1271 | 1094 | -0.193 [-0.328, -0.058] | -0.02173 | -2.80 | 0.005** | 0.068 | 0.020 (FDR<0.05) | -5.2 | -4.5 | 0.0504 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time > 180 (%) | 1271 | 1049 | -0.192 [-0.326, -0.058] | -0.0215 | -2.80 | 0.005** | 0.068 | 0.020 (FDR<0.05) | -5.1 | -4.4 | 0.0504 | 0.0477 |
| MoCA memory index score (0-15) | Nocturnal time > 180 (%) | 1271 | 446 | -0.161 [-0.289, -0.032] | -0.01903 | -2.45 | 0.014* | 0.137 | 0.037 (FDR<0.05) | -3.0 | -2.3 | 0.0497 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time > 180, pooled (%) | 1270 | 1093 | +0.074 [-0.289, +0.437] | 0.008409 | 0.40 | 0.689 | 0.932 | 0.953 | +1.7 | -0.3 | 0.0626 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 180 (%) | 1270 | 1048 | +0.073 [-0.288, +0.434] | 0.008275 | 0.40 | 0.692 | 0.932 | 0.953 | +1.7 | -0.3 | 0.0628 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Nocturnal time > 180 (%) | 1270 | 445 | +0.187 [-0.234, +0.608] | 0.02219 | 0.87 | 0.383 | 0.788 | 0.953 | -0.1 | -2.1 | 0.0622 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 180, pooled (%) | 1270 | 1093 | OR 1.098 [0.968, 1.246] | 0.01064 | 1.45 | 0.146 | 0.503 | 0.565 | -0.0 | -1.1 | 0.6751 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 180 (%) | 1270 | 1048 | OR 1.099 [0.969, 1.247] | 0.01069 | 1.47 | 0.143 | 0.503 | 0.565 | -0.0 | -1.2 | 0.6750 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Nocturnal time > 180 (%) | 1270 | 445 | OR 1.165 [1.029, 1.319] | 0.01809 | 2.41 | 0.016* | 0.137 | 0.489 | -3.8 | -4.9 | 0.6816 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 180, pooled (%) | 1251 | 1077 | -0.033 [-0.072, +0.006] | -0.003704 | -1.67 | 0.094 | 0.412 | 0.265 | +0.2 | -1.8 | 0.1138 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 180 (%) | 1251 | 1033 | -0.033 [-0.072, +0.006] | -0.003707 | -1.68 | 0.093 | 0.410 | 0.265 | +0.2 | -1.8 | 0.1138 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Nocturnal time > 180 (%) | 1251 | 441 | -0.022 [-0.058, +0.015] | -0.002567 | -1.17 | 0.242 | 0.621 | 0.417 | +1.2 | -0.8 | 0.1133 | 0.1139 |
| Indoor temperature, mean (deg C) | Time > 180, pooled (%) | 1251 | 1077 | +0.031 [-0.080, +0.142] | 0.003456 | 0.55 | 0.585 | 0.932 | 0.915 | +1.7 | -0.3 | 0.2886 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time > 180 (%) | 1251 | 1033 | +0.032 [-0.078, +0.143] | 0.003583 | 0.57 | 0.568 | 0.932 | 0.915 | +1.6 | -0.3 | 0.2886 | 0.2892 |
| Indoor temperature, mean (deg C) | Nocturnal time > 180 (%) | 1251 | 441 | +0.046 [-0.072, +0.163] | 0.005378 | 0.76 | 0.445 | 0.852 | 0.915 | +1.3 | -0.7 | 0.2886 | 0.2892 |
| Indoor relative humidity, mean (%) | Time > 180, pooled (%) | 1251 | 1077 | +0.019 [-0.299, +0.338] | 0.00216 | 0.12 | 0.905 | 0.966 | 0.905 | +2.0 | +2.5 | 0.2389 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time > 180 (%) | 1251 | 1033 | +0.023 [-0.295, +0.341] | 0.002596 | 0.14 | 0.886 | 0.964 | 0.905 | +2.0 | +2.5 | 0.2390 | 0.2403 |
| Indoor relative humidity, mean (%) | Nocturnal time > 180 (%) | 1251 | 441 | +0.127 [-0.143, +0.398] | 0.01497 | 0.92 | 0.356 | 0.758 | 0.613 | +1.4 | +1.9 | 0.2398 | 0.2403 |
| Indoor VOC index, mean | Time > 180, pooled (%) | 1251 | 1077 | -0.169 [-1.119, +0.781] | -0.01889 | -0.35 | 0.727 | 0.932 | 0.784 | +1.8 | +1.2 | 0.0002 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time > 180 (%) | 1251 | 1033 | -0.149 [-1.100, +0.802] | -0.01659 | -0.31 | 0.759 | 0.932 | 0.784 | +1.9 | +1.3 | 0.0002 | 0.0025 |
| Indoor VOC index, mean | Nocturnal time > 180 (%) | 1251 | 441 | -0.191 [-1.168, +0.787] | -0.02239 | -0.38 | 0.702 | 0.932 | 0.784 | +1.8 | +1.2 | -0.0002 | 0.0025 |
| Steps per wear-day | Time > 180, pooled (%) | 1125 | 963 | -32.279 [-268.579, +204.021] | -3.766 | -0.27 | 0.789 | 0.936 | 0.958 | +1.9 | +5.2 | 0.1063 | 0.1080 |
| Steps per wear-day | Avg. daily time > 180 (%) | 1125 | 920 | -40.529 [-277.335, +196.276] | -4.715 | -0.34 | 0.737 | 0.932 | 0.958 | +1.9 | +5.2 | 0.1064 | 0.1080 |
| Steps per wear-day | Nocturnal time > 180 (%) | 1125 | 392 | -28.677 [-265.799, +208.446] | -3.545 | -0.24 | 0.813 | 0.939 | 0.958 | +1.9 | +5.2 | 0.1065 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 180, pooled (%) | 1125 | 963 | +0.223 [-0.533, +0.979] | 0.02601 | 0.58 | 0.563 | 0.932 | 0.931 | +1.6 | +5.1 | 0.1232 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 180 (%) | 1125 | 920 | +0.203 [-0.554, +0.961] | 0.02366 | 0.53 | 0.599 | 0.932 | 0.931 | +1.7 | +5.1 | 0.1232 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Nocturnal time > 180 (%) | 1125 | 392 | +0.021 [-0.753, +0.794] | 0.002537 | 0.05 | 0.959 | 0.983 | 0.994 | +2.0 | +5.5 | 0.1232 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 180, pooled (%) | 1128 | 964 | +0.718 [+0.130, +1.306] | 0.08387 | 2.39 | 0.017* | 0.137 | 0.034 (FDR<0.05) | -8.5 | +2.7 | 0.1079 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 180 (%) | 1128 | 921 | +0.708 [+0.119, +1.296] | 0.08245 | 2.36 | 0.018* | 0.145 | 0.034 (FDR<0.05) | -8.2 | +3.0 | 0.1077 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Nocturnal time > 180 (%) | 1128 | 392 | +0.322 [-0.292, +0.936] | 0.03983 | 1.03 | 0.305 | 0.688 | 0.378 | -0.1 | +11.1 | 0.1019 | 0.1044 |
| Total sleep time per night (min) | Time > 180, pooled (%) | 1137 | 976 | +1.134 [-2.929, +5.196] | 0.1413 | 0.55 | 0.584 | 0.932 | 0.936 | +1.7 | +3.7 | -0.0069 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time > 180 (%) | 1137 | 935 | +1.191 [-2.876, +5.258] | 0.148 | 0.57 | 0.566 | 0.932 | 0.936 | +1.6 | +3.6 | -0.0069 | -0.0051 |
| Total sleep time per night (min) | Nocturnal time > 180 (%) | 1137 | 397 | +1.419 [-2.375, +5.213] | 0.1896 | 0.73 | 0.464 | 0.871 | 0.936 | +1.5 | +3.5 | -0.0059 | -0.0051 |
| Garmin stress score, mean (0-100) | Time > 180, pooled (%) | 1130 | 965 | +0.813 [-0.579, +2.206] | 0.0951 | 1.14 | 0.252 | 0.629 | 0.471 | -0.7 | +7.1 | 0.0491 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time > 180 (%) | 1130 | 922 | +0.775 [-0.611, +2.161] | 0.0903 | 1.10 | 0.273 | 0.648 | 0.471 | -0.4 | +7.4 | 0.0490 | 0.0510 |
| Garmin stress score, mean (0-100) | Nocturnal time > 180 (%) | 1130 | 394 | +0.033 [-1.442, +1.507] | 0.004074 | 0.04 | 0.965 | 0.983 | 0.965 | +2.0 | +9.8 | 0.0469 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time > 180, pooled (%) | 867 | 833 | -0.249 [-0.477, -0.021] | -0.00962 | -2.14 | 0.032* | not applied (n < 1000) | not applied (n < 1000) | -2.9 | -1.3 | 0.0580 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time > 180 (%) | 867 | 827 | -0.242 [-0.471, -0.013] | -0.009297 | -2.07 | 0.038* | not applied (n < 1000) | not applied (n < 1000) | -2.6 | -1.1 | 0.0576 | 0.0541 |
| MoCA total score (0-30) | Nocturnal time > 180 (%) | 867 | 663 | -0.257 [-0.490, -0.024] | -0.009428 | -2.16 | 0.031* | not applied (n < 1000) | not applied (n < 1000) | -3.1 | -1.6 | 0.0574 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time > 180, pooled (%) | 867 | 833 | OR 1.165 [1.010, 1.343] | 0.005881 | 2.10 | 0.036* | not applied (n < 1000) | not applied (n < 1000) | -2.5 | -0.8 | 0.6437 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 180 (%) | 867 | 827 | OR 1.163 [1.008, 1.341] | 0.005789 | 2.08 | 0.038* | not applied (n < 1000) | not applied (n < 1000) | -2.4 | -0.7 | 0.6437 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Nocturnal time > 180 (%) | 867 | 663 | OR 1.166 [1.011, 1.346] | 0.005648 | 2.11 | 0.035* | not applied (n < 1000) | not applied (n < 1000) | -2.5 | -0.8 | 0.6446 | 0.6425 |
| MoCA memory index score (0-15) | Time > 180, pooled (%) | 867 | 833 | -0.162 [-0.337, +0.014] | -0.006238 | -1.80 | 0.071 | not applied (n < 1000) | not applied (n < 1000) | -1.0 | +0.8 | 0.0309 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time > 180 (%) | 867 | 827 | -0.157 [-0.334, +0.019] | -0.006034 | -1.74 | 0.081 | not applied (n < 1000) | not applied (n < 1000) | -0.8 | +1.0 | 0.0308 | 0.0286 |
| MoCA memory index score (0-15) | Nocturnal time > 180 (%) | 867 | 663 | -0.169 [-0.347, +0.010] | -0.006191 | -1.85 | 0.064 | not applied (n < 1000) | not applied (n < 1000) | -1.2 | +0.6 | 0.0307 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time > 180, pooled (%) | 865 | 831 | +0.204 [-0.153, +0.561] | 0.007871 | 1.12 | 0.263 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +1.8 | 0.0780 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 180 (%) | 865 | 825 | +0.191 [-0.167, +0.549] | 0.007334 | 1.05 | 0.296 | not applied (n < 1000) | not applied (n < 1000) | +0.7 | +2.0 | 0.0780 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Nocturnal time > 180 (%) | 865 | 661 | +0.298 [-0.059, +0.656] | 0.01094 | 1.64 | 0.102 | not applied (n < 1000) | not applied (n < 1000) | -1.1 | +0.2 | 0.0797 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 180, pooled (%) | 865 | 831 | OR 1.150 [0.980, 1.349] | 0.005372 | 1.71 | 0.087 | not applied (n < 1000) | not applied (n < 1000) | -0.9 | +2.1 | 0.6360 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 180 (%) | 865 | 825 | OR 1.141 [0.972, 1.339] | 0.005047 | 1.61 | 0.108 | not applied (n < 1000) | not applied (n < 1000) | -0.5 | +2.5 | 0.6356 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Nocturnal time > 180 (%) | 865 | 661 | OR 1.219 [1.041, 1.426] | 0.007248 | 2.46 | 0.014* | not applied (n < 1000) | not applied (n < 1000) | -3.9 | -0.9 | 0.6405 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 180, pooled (%) | 849 | 819 | +0.064 [-0.009, +0.137] | 0.002467 | 1.72 | 0.086 | not applied (n < 1000) | not applied (n < 1000) | -2.0 | +7.5 | 0.1314 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 180 (%) | 849 | 813 | +0.064 [-0.010, +0.137] | 0.002436 | 1.70 | 0.089 | not applied (n < 1000) | not applied (n < 1000) | -1.9 | +7.5 | 0.1314 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Nocturnal time > 180 (%) | 849 | 654 | +0.073 [-0.000, +0.147] | 0.002681 | 1.95 | 0.051 | not applied (n < 1000) | not applied (n < 1000) | -3.1 | +6.3 | 0.1321 | 0.1310 |
| Indoor temperature, mean (deg C) | Time > 180, pooled (%) | 849 | 819 | -0.062 [-0.220, +0.095] | -0.002403 | -0.78 | 0.436 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | -0.4 | 0.2230 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time > 180 (%) | 849 | 813 | -0.068 [-0.226, +0.089] | -0.002624 | -0.85 | 0.394 | not applied (n < 1000) | not applied (n < 1000) | +1.1 | -0.5 | 0.2231 | 0.2264 |
| Indoor temperature, mean (deg C) | Nocturnal time > 180 (%) | 849 | 654 | -0.066 [-0.225, +0.094] | -0.002405 | -0.81 | 0.420 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | -0.5 | 0.2235 | 0.2264 |
| Indoor relative humidity, mean (%) | Time > 180, pooled (%) | 849 | 819 | -0.137 [-0.589, +0.315] | -0.005273 | -0.59 | 0.552 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.3 | 0.1843 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time > 180 (%) | 849 | 813 | -0.129 [-0.581, +0.324] | -0.004926 | -0.56 | 0.578 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.2 | 0.1842 | 0.1857 |
| Indoor relative humidity, mean (%) | Nocturnal time > 180 (%) | 849 | 654 | -0.256 [-0.702, +0.191] | -0.009368 | -1.12 | 0.262 | not applied (n < 1000) | not applied (n < 1000) | +0.6 | -1.3 | 0.1853 | 0.1857 |
| Indoor VOC index, mean | Time > 180, pooled (%) | 849 | 819 | -0.483 [-1.799, +0.833] | -0.0186 | -0.72 | 0.472 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +1.7 | 0.0265 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time > 180 (%) | 849 | 813 | -0.539 [-1.862, +0.784] | -0.02065 | -0.80 | 0.425 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +1.5 | 0.0268 | 0.0276 |
| Indoor VOC index, mean | Nocturnal time > 180 (%) | 849 | 654 | -0.376 [-1.859, +1.106] | -0.0138 | -0.50 | 0.619 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +2.0 | 0.0253 | 0.0276 |
| Steps per wear-day | Time > 180, pooled (%) | 747 | 714 | +144.486 [-268.337, +557.310] | 5.571 | 0.69 | 0.493 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +1.5 | 0.1372 | 0.1390 |
| Steps per wear-day | Avg. daily time > 180 (%) | 747 | 708 | +150.615 [-261.757, +562.987] | 5.781 | 0.72 | 0.474 | not applied (n < 1000) | not applied (n < 1000) | +1.3 | +1.4 | 0.1373 | 0.1390 |
| Steps per wear-day | Nocturnal time > 180 (%) | 747 | 567 | +162.753 [-260.264, +585.771] | 5.974 | 0.75 | 0.451 | not applied (n < 1000) | not applied (n < 1000) | +1.2 | +1.3 | 0.1372 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 180, pooled (%) | 747 | 714 | +0.211 [-0.937, +1.360] | 0.008149 | 0.36 | 0.718 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +1.9 | 0.1525 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 180 (%) | 747 | 708 | +0.233 [-0.917, +1.384] | 0.008953 | 0.40 | 0.691 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +1.8 | 0.1525 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Nocturnal time > 180 (%) | 747 | 567 | +0.294 [-0.893, +1.481] | 0.01079 | 0.49 | 0.627 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +1.7 | 0.1525 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 180, pooled (%) | 749 | 716 | +1.065 [+0.425, +1.706] | 0.04103 | 3.26 | 0.001** | not applied (n < 1000) | not applied (n < 1000) | -9.8 | -3.7 | 0.1365 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 180 (%) | 749 | 710 | +1.069 [+0.430, +1.707] | 0.04096 | 3.28 | 0.001** | not applied (n < 1000) | not applied (n < 1000) | -9.9 | -3.8 | 0.1365 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Nocturnal time > 180 (%) | 749 | 568 | +0.947 [+0.302, +1.592] | 0.03475 | 2.88 | 0.004** | not applied (n < 1000) | not applied (n < 1000) | -7.2 | -1.1 | 0.1333 | 0.1253 |
| Total sleep time per night (min) | Time > 180, pooled (%) | 756 | 723 | -2.757 [-7.779, +2.265] | -0.1073 | -1.08 | 0.282 | not applied (n < 1000) | not applied (n < 1000) | +0.8 | +3.7 | 0.0055 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time > 180 (%) | 756 | 717 | -2.714 [-7.760, +2.333] | -0.1051 | -1.05 | 0.292 | not applied (n < 1000) | not applied (n < 1000) | +0.9 | +3.8 | 0.0053 | 0.0066 |
| Total sleep time per night (min) | Nocturnal time > 180 (%) | 756 | 572 | -0.522 [-5.444, +4.401] | -0.01934 | -0.21 | 0.835 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +4.9 | 0.0041 | 0.0066 |
| Garmin stress score, mean (0-100) | Time > 180, pooled (%) | 749 | 716 | +2.610 [+1.293, +3.927] | 0.1005 | 3.88 | 1.0e-04*** | not applied (n < 1000) | not applied (n < 1000) | -14.3 | -1.2 | 0.1121 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time > 180 (%) | 749 | 710 | +2.604 [+1.288, +3.921] | 0.09984 | 3.88 | 1.1e-04*** | not applied (n < 1000) | not applied (n < 1000) | -14.2 | -1.1 | 0.1120 | 0.0947 |
| Garmin stress score, mean (0-100) | Nocturnal time > 180 (%) | 749 | 568 | +2.246 [+0.930, +3.562] | 0.08245 | 3.34 | 8.2e-04*** | not applied (n < 1000) | not applied (n < 1000) | -9.9 | +3.2 | 0.1066 | 0.0947 |


---

## Band 181-250

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 181-250, pooled (%) | 2138 | 1927 | -0.321 [-0.466, -0.177] | -0.02505 | -4.35 | 1.4e-05*** | 1.1e-04 (FDR<0.05) | 3.5e-05 (FDR<0.05) | -21.2 | +3.4 | 0.1000 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time 181-250 (%) | 2138 | 1876 | -0.316 [-0.461, -0.171] | -0.0243 | -4.27 | 2.0e-05*** | 1.4e-04 (FDR<0.05) | 4.3e-05 (FDR<0.05) | -20.4 | +4.2 | 0.0997 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Time 181-250, pooled (%) | 2138 | 1927 | OR 1.185 [1.081, 1.300] | 0.01326 | 3.61 | 3.1e-04*** | 0.002 (FDR<0.05) | 7.3e-04 (FDR<0.05) | -11.1 | +2.5 | 0.6654 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 181-250 (%) | 2138 | 1876 | OR 1.186 [1.081, 1.300] | 0.0131 | 3.61 | 3.0e-04*** | 0.002 (FDR<0.05) | 7.3e-04 (FDR<0.05) | -11.1 | +2.5 | 0.6655 | 0.6603 |
| MoCA memory index score (0-15) | Time 181-250, pooled (%) | 2138 | 1927 | -0.153 [-0.268, -0.038] | -0.01191 | -2.60 | 0.009** | 0.033 (FDR<0.05) | 0.021 (FDR<0.05) | -4.7 | +0.6 | 0.0651 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time 181-250 (%) | 2138 | 1876 | -0.153 [-0.268, -0.037] | -0.01174 | -2.59 | 0.010** | 0.035 (FDR<0.05) | 0.021 (FDR<0.05) | -4.7 | +0.6 | 0.0650 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Time 181-250, pooled (%) | 2135 | 1924 | +0.088 [-0.133, +0.310] | 0.006888 | 0.78 | 0.435 | 0.607 | 0.620 | +1.3 | +1.6 | 0.0914 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 181-250 (%) | 2135 | 1873 | +0.090 [-0.131, +0.312] | 0.00696 | 0.80 | 0.424 | 0.596 | 0.620 | +1.3 | +1.5 | 0.0914 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 181-250, pooled (%) | 2135 | 1924 | OR 1.109 [0.995, 1.237] | 0.008072 | 1.86 | 0.062 | 0.158 | 0.161 | -1.4 | +1.3 | 0.6682 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 181-250 (%) | 2135 | 1873 | OR 1.112 [0.997, 1.239] | 0.008147 | 1.91 | 0.056 | 0.147 | 0.158 | -1.6 | +1.1 | 0.6684 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 181-250, pooled (%) | 2100 | 1896 | +0.026 [-0.016, +0.068] | 0.002026 | 1.22 | 0.222 | 0.393 | 0.274 | +0.3 | +11.2 | 0.1384 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 181-250 (%) | 2100 | 1846 | +0.026 [-0.016, +0.067] | 0.001962 | 1.20 | 0.230 | 0.400 | 0.274 | +0.4 | +11.3 | 0.1383 | 0.1387 |
| Indoor temperature, mean (deg C) | Time 181-250, pooled (%) | 2100 | 1896 | +0.013 [-0.077, +0.103] | 0.001007 | 0.28 | 0.779 | 0.864 | 0.982 | +1.9 | +0.4 | 0.2889 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time 181-250 (%) | 2100 | 1846 | +0.010 [-0.081, +0.101] | 0.0007616 | 0.21 | 0.830 | 0.892 | 0.982 | +2.0 | +0.4 | 0.2889 | 0.2896 |
| Indoor relative humidity, mean (%) | Time 181-250, pooled (%) | 2100 | 1896 | -0.085 [-0.358, +0.188] | -0.006603 | -0.61 | 0.542 | 0.701 | 0.898 | +1.6 | -0.2 | 0.2303 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time 181-250 (%) | 2100 | 1846 | -0.078 [-0.351, +0.195] | -0.005971 | -0.56 | 0.576 | 0.732 | 0.898 | +1.7 | -0.2 | 0.2303 | 0.2307 |
| Indoor VOC index, mean | Time 181-250, pooled (%) | 2100 | 1896 | +0.325 [-0.628, +1.278] | 0.02527 | 0.67 | 0.504 | 0.675 | 0.868 | +1.2 | +1.2 | 0.0257 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time 181-250 (%) | 2100 | 1846 | +0.307 [-0.637, +1.250] | 0.02353 | 0.64 | 0.524 | 0.693 | 0.868 | +1.3 | +1.3 | 0.0258 | 0.0271 |
| Steps per wear-day | Time 181-250, pooled (%) | 1872 | 1677 | +215.490 [-22.588, +453.567] | 16.89 | 1.77 | 0.076 | 0.184 | 0.198 | -2.5 | +5.5 | 0.1234 | 0.1222 |
| Steps per wear-day | Avg. daily time 181-250 (%) | 1872 | 1628 | +209.917 [-29.277, +449.111] | 16.22 | 1.72 | 0.085 | 0.195 | 0.202 | -2.3 | +5.7 | 0.1233 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 181-250, pooled (%) | 1872 | 1677 | +0.607 [-0.079, +1.292] | 0.04757 | 1.74 | 0.083 | 0.193 | 0.192 | -2.0 | +6.2 | 0.1457 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 181-250 (%) | 1872 | 1628 | +0.597 [-0.092, +1.287] | 0.04616 | 1.70 | 0.090 | 0.202 | 0.192 | -1.8 | +6.3 | 0.1457 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 181-250, pooled (%) | 1877 | 1680 | +1.747 [+1.331, +2.162] | 0.1368 | 8.25 | 1.6e-16*** | 7.1e-14 (FDR<0.05) | 5.1e-15 (FDR<0.05) | -80.2 | -9.0 | 0.1829 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 181-250 (%) | 1877 | 1631 | +1.733 [+1.316, +2.149] | 0.1338 | 8.15 | 3.5e-16*** | 7.6e-14 (FDR<0.05) | 5.4e-15 (FDR<0.05) | -78.8 | -7.6 | 0.1824 | 0.1482 |
| Total sleep time per night (min) | Time 181-250, pooled (%) | 1893 | 1699 | -2.241 [-5.559, +1.078] | -0.1758 | -1.32 | 0.186 | 0.346 | 0.397 | +0.0 | +8.9 | 0.0196 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time 181-250 (%) | 1893 | 1652 | -2.210 [-5.530, +1.110] | -0.1711 | -1.30 | 0.192 | 0.353 | 0.397 | +0.1 | +9.0 | 0.0196 | 0.0209 |
| Garmin stress score, mean (0-100) | Time 181-250, pooled (%) | 1879 | 1681 | +3.023 [+2.174, +3.872] | 0.2369 | 6.98 | 3.0e-12*** | 8.6e-11 (FDR<0.05) | 4.6e-11 (FDR<0.05) | -51.6 | +8.8 | 0.1150 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time 181-250 (%) | 1879 | 1632 | +2.982 [+2.133, +3.832] | 0.2305 | 6.88 | 6.0e-12*** | 1.6e-10 (FDR<0.05) | 5.6e-11 (FDR<0.05) | -50.1 | +10.3 | 0.1142 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 181-250, pooled (%) | 1271 | 1094 | -0.265 [-0.435, -0.095] | -0.0435 | -3.06 | 0.002** | 0.051 | 0.011 (FDR<0.05) | -9.8 | +3.9 | 0.0856 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time 181-250 (%) | 1271 | 1049 | -0.262 [-0.431, -0.092] | -0.04242 | -3.03 | 0.002** | 0.052 | 0.011 (FDR<0.05) | -9.4 | +4.3 | 0.0853 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Time 181-250, pooled (%) | 1271 | 1094 | OR 1.086 [0.965, 1.223] | 0.01357 | 1.37 | 0.171 | 0.532 | 0.480 | +0.2 | -0.1 | 0.6445 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 181-250 (%) | 1271 | 1049 | OR 1.086 [0.965, 1.222] | 0.0133 | 1.36 | 0.174 | 0.532 | 0.480 | +0.2 | -0.0 | 0.6443 | 0.6443 |
| MoCA memory index score (0-15) | Time 181-250, pooled (%) | 1271 | 1094 | -0.138 [-0.287, +0.010] | -0.02266 | -1.82 | 0.068 | 0.352 | 0.127 | -1.6 | -1.0 | 0.0479 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time 181-250 (%) | 1271 | 1049 | -0.138 [-0.284, +0.008] | -0.02239 | -1.86 | 0.063 | 0.340 | 0.127 | -1.6 | -1.0 | 0.0480 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Time 181-250, pooled (%) | 1270 | 1093 | +0.213 [-0.146, +0.571] | 0.03522 | 1.16 | 0.246 | 0.624 | 0.953 | -0.7 | -2.6 | 0.0650 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 181-250 (%) | 1270 | 1048 | +0.207 [-0.153, +0.568] | 0.03394 | 1.13 | 0.260 | 0.638 | 0.953 | -0.5 | -2.5 | 0.0649 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 181-250, pooled (%) | 1270 | 1093 | OR 1.144 [1.000, 1.309] | 0.02234 | 1.96 | 0.050* | 0.296 | 0.537 | -1.7 | -2.8 | 0.6769 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 181-250 (%) | 1270 | 1048 | OR 1.143 [0.999, 1.307] | 0.02181 | 1.94 | 0.052 | 0.305 | 0.537 | -1.6 | -2.8 | 0.6767 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 181-250, pooled (%) | 1251 | 1077 | -0.035 [-0.085, +0.016] | -0.005637 | -1.35 | 0.178 | 0.532 | 0.367 | +0.0 | -2.0 | 0.1133 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 181-250 (%) | 1251 | 1033 | -0.035 [-0.086, +0.016] | -0.005634 | -1.36 | 0.175 | 0.532 | 0.367 | -0.0 | -2.0 | 0.1132 | 0.1139 |
| Indoor temperature, mean (deg C) | Time 181-250, pooled (%) | 1251 | 1077 | +0.027 [-0.079, +0.133] | 0.004431 | 0.50 | 0.616 | 0.932 | 0.915 | +1.7 | -0.2 | 0.2882 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time 181-250 (%) | 1251 | 1033 | +0.030 [-0.077, +0.137] | 0.004823 | 0.55 | 0.582 | 0.932 | 0.915 | +1.7 | -0.3 | 0.2883 | 0.2892 |
| Indoor relative humidity, mean (%) | Time 181-250, pooled (%) | 1251 | 1077 | -0.111 [-0.445, +0.224] | -0.01806 | -0.65 | 0.516 | 0.918 | 0.758 | +1.6 | +2.1 | 0.2390 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time 181-250 (%) | 1251 | 1033 | -0.105 [-0.438, +0.229] | -0.01685 | -0.62 | 0.538 | 0.931 | 0.758 | +1.6 | +2.1 | 0.2391 | 0.2403 |
| Indoor VOC index, mean | Time 181-250, pooled (%) | 1251 | 1077 | +0.196 [-0.896, +1.288] | 0.03195 | 0.35 | 0.725 | 0.932 | 0.784 | +1.8 | +1.2 | -0.0012 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time 181-250 (%) | 1251 | 1033 | +0.213 [-0.873, +1.300] | 0.03436 | 0.38 | 0.700 | 0.932 | 0.784 | +1.8 | +1.1 | -0.0009 | 0.0025 |
| Steps per wear-day | Time 181-250, pooled (%) | 1125 | 963 | -112.794 [-315.192, +89.605] | -18.78 | -1.09 | 0.275 | 0.648 | 0.958 | +1.0 | +4.3 | 0.1069 | 0.1080 |
| Steps per wear-day | Avg. daily time 181-250 (%) | 1125 | 920 | -120.736 [-321.893, +80.422] | -19.86 | -1.18 | 0.239 | 0.619 | 0.958 | +0.9 | +4.2 | 0.1071 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 181-250, pooled (%) | 1125 | 963 | +0.003 [-0.676, +0.681] | 0.000432 | 0.01 | 0.994 | 0.994 | 0.994 | +2.0 | +5.5 | 0.1224 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 181-250 (%) | 1125 | 920 | -0.012 [-0.692, +0.667] | -0.002001 | -0.04 | 0.972 | 0.986 | 0.994 | +2.0 | +5.5 | 0.1225 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 181-250, pooled (%) | 1128 | 964 | +0.662 [+0.134, +1.191] | 0.1104 | 2.46 | 0.014* | 0.137 | 0.034 (FDR<0.05) | -6.8 | +4.4 | 0.1070 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 181-250 (%) | 1128 | 921 | +0.655 [+0.121, +1.189] | 0.1079 | 2.40 | 0.016* | 0.137 | 0.034 (FDR<0.05) | -6.6 | +4.6 | 0.1067 | 0.1044 |
| Total sleep time per night (min) | Time 181-250, pooled (%) | 1137 | 976 | +1.721 [-2.595, +6.036] | 0.2915 | 0.78 | 0.435 | 0.846 | 0.936 | +1.2 | +3.2 | -0.0073 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time 181-250 (%) | 1137 | 935 | +1.775 [-2.541, +6.090] | 0.2971 | 0.81 | 0.420 | 0.822 | 0.936 | +1.2 | +3.2 | -0.0072 | -0.0051 |
| Garmin stress score, mean (0-100) | Time 181-250, pooled (%) | 1130 | 965 | +0.717 [-0.428, +1.861] | 0.1195 | 1.23 | 0.220 | 0.594 | 0.471 | -0.0 | +7.7 | 0.0502 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time 181-250 (%) | 1130 | 922 | +0.677 [-0.462, +1.816] | 0.1116 | 1.17 | 0.244 | 0.623 | 0.471 | +0.2 | +8.0 | 0.0501 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Time 181-250, pooled (%) | 867 | 833 | -0.203 [-0.436, +0.029] | -0.01302 | -1.71 | 0.087 | not applied (n < 1000) | not applied (n < 1000) | -1.2 | +0.3 | 0.0552 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time 181-250 (%) | 867 | 827 | -0.196 [-0.429, +0.037] | -0.01235 | -1.65 | 0.099 | not applied (n < 1000) | not applied (n < 1000) | -1.0 | +0.5 | 0.0551 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Time 181-250, pooled (%) | 867 | 833 | OR 1.119 [0.971, 1.289] | 0.007197 | 1.56 | 0.120 | not applied (n < 1000) | not applied (n < 1000) | -0.4 | +1.3 | 0.6425 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time 181-250 (%) | 867 | 827 | OR 1.121 [0.973, 1.291] | 0.007182 | 1.58 | 0.114 | not applied (n < 1000) | not applied (n < 1000) | -0.5 | +1.2 | 0.6422 | 0.6425 |
| MoCA memory index score (0-15) | Time 181-250, pooled (%) | 867 | 833 | -0.146 [-0.326, +0.034] | -0.009359 | -1.59 | 0.111 | not applied (n < 1000) | not applied (n < 1000) | -0.4 | +1.3 | 0.0294 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time 181-250 (%) | 867 | 827 | -0.147 [-0.328, +0.034] | -0.009243 | -1.59 | 0.112 | not applied (n < 1000) | not applied (n < 1000) | -0.4 | +1.3 | 0.0295 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Time 181-250, pooled (%) | 865 | 831 | +0.039 [-0.293, +0.371] | 0.002482 | 0.23 | 0.819 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +3.2 | 0.0774 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time 181-250 (%) | 865 | 825 | +0.047 [-0.284, +0.378] | 0.002942 | 0.28 | 0.782 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +3.2 | 0.0774 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time 181-250, pooled (%) | 865 | 831 | OR 1.107 [0.936, 1.307] | 0.006472 | 1.19 | 0.234 | not applied (n < 1000) | not applied (n < 1000) | +0.6 | +3.6 | 0.6314 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time 181-250 (%) | 865 | 825 | OR 1.114 [0.943, 1.316] | 0.00679 | 1.27 | 0.204 | not applied (n < 1000) | not applied (n < 1000) | +0.4 | +3.4 | 0.6319 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time 181-250, pooled (%) | 849 | 819 | +0.042 [-0.024, +0.107] | 0.002653 | 1.24 | 0.214 | not applied (n < 1000) | not applied (n < 1000) | +0.3 | +9.7 | 0.1296 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time 181-250 (%) | 849 | 813 | +0.041 [-0.025, +0.106] | 0.002563 | 1.22 | 0.221 | not applied (n < 1000) | not applied (n < 1000) | +0.4 | +9.8 | 0.1296 | 0.1310 |
| Indoor temperature, mean (deg C) | Time 181-250, pooled (%) | 849 | 819 | -0.077 [-0.226, +0.071] | -0.00493 | -1.02 | 0.308 | not applied (n < 1000) | not applied (n < 1000) | +0.9 | -0.8 | 0.2241 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time 181-250 (%) | 849 | 813 | -0.084 [-0.233, +0.065] | -0.005294 | -1.11 | 0.267 | not applied (n < 1000) | not applied (n < 1000) | +0.7 | -1.0 | 0.2243 | 0.2264 |
| Indoor relative humidity, mean (%) | Time 181-250, pooled (%) | 849 | 819 | -0.144 [-0.587, +0.300] | -0.009155 | -0.63 | 0.526 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.3 | 0.1840 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time 181-250 (%) | 849 | 813 | -0.131 [-0.572, +0.311] | -0.008203 | -0.58 | 0.562 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | -0.2 | 0.1839 | 0.1857 |
| Indoor VOC index, mean | Time 181-250, pooled (%) | 849 | 819 | +0.311 [-1.122, +1.744] | 0.01983 | 0.43 | 0.671 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +2.1 | 0.0244 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time 181-250 (%) | 849 | 813 | +0.258 [-1.153, +1.670] | 0.01622 | 0.36 | 0.720 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +2.2 | 0.0246 | 0.0276 |
| Steps per wear-day | Time 181-250, pooled (%) | 747 | 714 | +321.951 [-53.387, +697.290] | 20.49 | 1.68 | 0.093 | not applied (n < 1000) | not applied (n < 1000) | -1.2 | -1.1 | 0.1404 | 0.1390 |
| Steps per wear-day | Avg. daily time 181-250 (%) | 747 | 708 | +315.059 [-62.054, +692.172] | 19.71 | 1.64 | 0.102 | not applied (n < 1000) | not applied (n < 1000) | -1.1 | -1.0 | 0.1401 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time 181-250, pooled (%) | 747 | 714 | +0.633 [-0.435, +1.701] | 0.04027 | 1.16 | 0.245 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +0.5 | 0.1543 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time 181-250 (%) | 747 | 708 | +0.622 [-0.452, +1.696] | 0.0389 | 1.13 | 0.256 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +0.6 | 0.1541 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time 181-250, pooled (%) | 749 | 716 | +1.093 [+0.475, +1.712] | 0.06953 | 3.46 | 5.3e-04*** | not applied (n < 1000) | not applied (n < 1000) | -10.4 | -4.4 | 0.1366 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time 181-250 (%) | 749 | 710 | +1.077 [+0.461, +1.692] | 0.06734 | 3.43 | 6.1e-04*** | not applied (n < 1000) | not applied (n < 1000) | -10.1 | -4.0 | 0.1362 | 0.1253 |
| Total sleep time per night (min) | Time 181-250, pooled (%) | 756 | 723 | -3.935 [-9.237, +1.367] | -0.2508 | -1.45 | 0.146 | not applied (n < 1000) | not applied (n < 1000) | -0.4 | +2.5 | 0.0067 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time 181-250 (%) | 756 | 717 | -3.908 [-9.205, +1.389] | -0.245 | -1.45 | 0.148 | not applied (n < 1000) | not applied (n < 1000) | -0.4 | +2.5 | 0.0065 | 0.0066 |
| Garmin stress score, mean (0-100) | Time 181-250, pooled (%) | 749 | 716 | +2.545 [+1.268, +3.822] | 0.1619 | 3.91 | 9.4e-05*** | not applied (n < 1000) | not applied (n < 1000) | -13.4 | -0.4 | 0.1103 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time 181-250 (%) | 749 | 710 | +2.497 [+1.222, +3.773] | 0.1562 | 3.84 | 1.2e-04*** | not applied (n < 1000) | not applied (n < 1000) | -12.9 | +0.2 | 0.1096 | 0.0947 |


---

## Band >250

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading > 250 during wear (0/1) | 2138 | 795 | -0.299 [-0.435, -0.163] | -0.6184 | -4.32 | 1.6e-05*** | 1.2e-04 (FDR<0.05) | 3.8e-05 (FDR<0.05) | -18.5 | +6.2 | 0.0988 | 0.0915 |
| MoCA total score (0-30) | Time > 250, pooled (%) | 2138 | 795 | -0.270 [-0.428, -0.112] | -0.02449 | -3.36 | 7.8e-04*** | 0.004 (FDR<0.05) | 0.001 (FDR<0.05) | -14.8 | +9.8 | 0.0974 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time > 250 (%) | 2138 | 735 | -0.265 [-0.426, -0.105] | -0.02439 | -3.25 | 0.001** | 0.005 (FDR<0.05) | 0.002 (FDR<0.05) | -14.3 | +10.4 | 0.0971 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Any reading > 250 during wear (0/1) | 2138 | 795 | OR 1.150 [1.049, 1.261] | 0.2899 | 2.99 | 0.003** | 0.012 (FDR<0.05) | 0.005 (FDR<0.05) | -6.9 | +6.7 | 0.6654 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Time > 250, pooled (%) | 2138 | 795 | OR 1.151 [1.046, 1.266] | 0.01273 | 2.88 | 0.004** | 0.017 (FDR<0.05) | 0.007 (FDR<0.05) | -6.9 | +6.8 | 0.6629 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 250 (%) | 2138 | 735 | OR 1.146 [1.042, 1.260] | 0.0125 | 2.80 | 0.005** | 0.021 (FDR<0.05) | 0.008 (FDR<0.05) | -6.3 | +7.3 | 0.6627 | 0.6603 |
| MoCA memory index score (0-15) | Any reading > 250 during wear (0/1) | 2138 | 795 | -0.136 [-0.254, -0.017] | -0.2804 | -2.25 | 0.025* | 0.080 | 0.048 (FDR<0.05) | -3.4 | +2.0 | 0.0641 | 0.0630 |
| MoCA memory index score (0-15) | Time > 250, pooled (%) | 2138 | 795 | -0.126 [-0.235, -0.016] | -0.01139 | -2.24 | 0.025* | 0.080 | 0.048 (FDR<0.05) | -2.7 | +2.7 | 0.0644 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time > 250 (%) | 2138 | 735 | -0.120 [-0.229, -0.011] | -0.01103 | -2.15 | 0.031* | 0.093 | 0.051 | -2.3 | +3.1 | 0.0642 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Any reading > 250 during wear (0/1) | 2135 | 793 | +0.035 [-0.171, +0.241] | 0.07286 | 0.34 | 0.738 | 0.842 | 0.788 | +1.9 | +2.1 | 0.0908 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Time > 250, pooled (%) | 2135 | 793 | +0.146 [-0.114, +0.406] | 0.01325 | 1.10 | 0.270 | 0.440 | 0.620 | +0.0 | +0.3 | 0.0916 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 250 (%) | 2135 | 733 | +0.131 [-0.130, +0.393] | 0.01204 | 0.98 | 0.326 | 0.495 | 0.620 | +0.4 | +0.7 | 0.0914 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading > 250 during wear (0/1) | 2135 | 793 | OR 1.074 [0.957, 1.204] | 0.1474 | 1.22 | 0.224 | 0.394 | 0.331 | +0.5 | +3.2 | 0.6665 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 250, pooled (%) | 2135 | 793 | OR 1.077 [0.978, 1.185] | 0.006694 | 1.51 | 0.131 | 0.267 | 0.245 | -0.2 | +2.5 | 0.6693 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 250 (%) | 2135 | 733 | OR 1.067 [0.969, 1.175] | 0.00596 | 1.32 | 0.188 | 0.348 | 0.295 | +0.3 | +3.0 | 0.6689 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading > 250 during wear (0/1) | 2100 | 783 | +0.006 [-0.033, +0.046] | 0.01343 | 0.32 | 0.748 | 0.844 | 0.748 | +1.9 | +12.8 | 0.1377 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 250, pooled (%) | 2100 | 783 | +0.041 [-0.010, +0.092] | 0.00374 | 1.59 | 0.111 | 0.230 | 0.173 | -2.4 | +8.6 | 0.1390 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 250 (%) | 2100 | 724 | +0.041 [-0.009, +0.092] | 0.003786 | 1.59 | 0.111 | 0.230 | 0.173 | -2.3 | +8.6 | 0.1391 | 0.1387 |
| Indoor temperature, mean (deg C) | Any reading > 250 during wear (0/1) | 2100 | 783 | -0.029 [-0.117, +0.058] | -0.06036 | -0.65 | 0.513 | 0.686 | 0.982 | +1.6 | +0.1 | 0.2889 | 0.2896 |
| Indoor temperature, mean (deg C) | Time > 250, pooled (%) | 2100 | 783 | +0.021 [-0.077, +0.118] | 0.001855 | 0.41 | 0.681 | 0.805 | 0.982 | +1.8 | +0.3 | 0.2890 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time > 250 (%) | 2100 | 724 | +0.018 [-0.080, +0.116] | 0.001652 | 0.36 | 0.720 | 0.837 | 0.982 | +1.8 | +0.3 | 0.2890 | 0.2896 |
| Indoor relative humidity, mean (%) | Any reading > 250 during wear (0/1) | 2100 | 783 | -0.213 [-0.478, +0.052] | -0.4405 | -1.58 | 0.115 | 0.235 | 0.898 | -0.5 | -2.4 | 0.2308 | 0.2307 |
| Indoor relative humidity, mean (%) | Time > 250, pooled (%) | 2100 | 783 | +0.007 [-0.265, +0.279] | 0.0006516 | 0.05 | 0.959 | 0.977 | 0.992 | +2.0 | +0.1 | 0.2299 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time > 250 (%) | 2100 | 724 | +0.009 [-0.267, +0.285] | 0.0008592 | 0.07 | 0.947 | 0.969 | 0.992 | +2.0 | +0.1 | 0.2298 | 0.2307 |
| Indoor VOC index, mean | Any reading > 250 during wear (0/1) | 2100 | 783 | +0.515 [-0.211, +1.241] | 1.064 | 1.39 | 0.165 | 0.319 | 0.868 | -0.1 | -0.1 | 0.0269 | 0.0271 |
| Indoor VOC index, mean | Time > 250, pooled (%) | 2100 | 783 | -0.696 [-1.491, +0.098] | -0.06296 | -1.72 | 0.086 | 0.195 | 0.665 | -1.8 | -1.8 | 0.0271 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time > 250 (%) | 2100 | 724 | -0.733 [-1.542, +0.077] | -0.06713 | -1.77 | 0.076 | 0.184 | 0.665 | -2.2 | -2.2 | 0.0273 | 0.0271 |
| Steps per wear-day | Any reading > 250 during wear (0/1) | 1872 | 690 | +204.919 [-4.344, +414.181] | 424.7 | 1.92 | 0.055 | 0.145 | 0.170 | -2.2 | +5.8 | 0.1233 | 0.1222 |
| Steps per wear-day | Time > 250, pooled (%) | 1872 | 690 | +17.470 [-245.130, +280.071] | 1.594 | 0.13 | 0.896 | 0.939 | 0.953 | +2.0 | +9.9 | 0.1205 | 0.1222 |
| Steps per wear-day | Avg. daily time > 250 (%) | 1872 | 637 | +19.630 [-235.302, +274.563] | 1.822 | 0.15 | 0.880 | 0.930 | 0.953 | +2.0 | +9.9 | 0.1205 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading > 250 during wear (0/1) | 1872 | 690 | +0.638 [+0.013, +1.263] | 1.322 | 2.00 | 0.045* | 0.128 | 0.192 | -2.5 | +5.7 | 0.1460 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 250, pooled (%) | 1872 | 690 | +0.102 [-0.637, +0.840] | 0.009263 | 0.27 | 0.787 | 0.868 | 0.828 | +1.9 | +10.1 | 0.1432 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 250 (%) | 1872 | 637 | +0.109 [-0.608, +0.826] | 0.01013 | 0.30 | 0.765 | 0.852 | 0.828 | +1.9 | +10.1 | 0.1433 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading > 250 during wear (0/1) | 1877 | 692 | +1.283 [+0.899, +1.666] | 2.658 | 6.55 | 5.6e-11*** | 1.0e-09 (FDR<0.05) | 1.2e-10 (FDR<0.05) | -42.8 | +28.4 | 0.1667 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 250, pooled (%) | 1877 | 692 | +1.001 [+0.556, +1.445] | 0.09123 | 4.41 | 1.0e-05*** | 8.3e-05 (FDR<0.05) | 1.5e-05 (FDR<0.05) | -25.5 | +45.8 | 0.1595 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 250 (%) | 1877 | 638 | +1.000 [+0.548, +1.453] | 0.09273 | 4.33 | 1.5e-05*** | 1.1e-04 (FDR<0.05) | 1.9e-05 (FDR<0.05) | -25.4 | +45.8 | 0.1594 | 0.1482 |
| Total sleep time per night (min) | Any reading > 250 during wear (0/1) | 1893 | 694 | -3.404 [-6.511, -0.298] | -7.063 | -2.15 | 0.032* | 0.093 | 0.123 | -2.6 | +6.3 | 0.0214 | 0.0209 |
| Total sleep time per night (min) | Time > 250, pooled (%) | 1893 | 694 | -1.051 [-3.995, +1.893] | -0.09953 | -0.70 | 0.484 | 0.654 | 0.582 | +1.6 | +10.5 | 0.0205 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time > 250 (%) | 1893 | 641 | -0.961 [-3.926, +2.005] | -0.09255 | -0.63 | 0.525 | 0.693 | 0.582 | +1.6 | +10.5 | 0.0204 | 0.0209 |
| Garmin stress score, mean (0-100) | Any reading > 250 during wear (0/1) | 1879 | 692 | +2.270 [+1.461, +3.080] | 4.706 | 5.50 | 3.9e-08*** | 5.1e-07 (FDR<0.05) | 8.0e-08 (FDR<0.05) | -28.7 | +31.7 | 0.1039 | 0.0902 |
| Garmin stress score, mean (0-100) | Time > 250, pooled (%) | 1879 | 692 | +1.927 [+0.951, +2.904] | 0.1758 | 3.87 | 1.1e-04*** | 6.5e-04 (FDR<0.05) | 1.6e-04 (FDR<0.05) | -20.3 | +40.1 | 0.0997 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time > 250 (%) | 1879 | 640 | +1.926 [+0.936, +2.917] | 0.1787 | 3.81 | 1.4e-04*** | 7.9e-04 (FDR<0.05) | 1.9e-04 (FDR<0.05) | -20.3 | +40.1 | 0.0996 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading > 250 during wear (0/1) | 1271 | 244 | -0.180 [-0.355, -0.005] | -0.4572 | -2.02 | 0.043* | 0.264 | 0.084 | -3.5 | +10.2 | 0.0809 | 0.0789 |
| MoCA total score (0-30) | Time > 250, pooled (%) | 1271 | 244 | -0.277 [-0.590, +0.036] | -0.05711 | -1.74 | 0.082 | 0.404 | 0.138 | -11.0 | +2.6 | 0.0801 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time > 250 (%) | 1271 | 207 | -0.276 [-0.593, +0.040] | -0.05806 | -1.71 | 0.087 | 0.405 | 0.138 | -11.0 | +2.7 | 0.0800 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Any reading > 250 during wear (0/1) | 1271 | 244 | OR 1.058 [0.938, 1.192] | 0.1423 | 0.92 | 0.358 | 0.759 | 0.585 | +1.2 | +0.9 | 0.6436 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Time > 250, pooled (%) | 1271 | 244 | OR 1.025 [0.910, 1.154] | 0.00508 | 0.41 | 0.684 | 0.932 | 0.834 | +1.8 | +1.6 | 0.6433 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 250 (%) | 1271 | 207 | OR 1.021 [0.907, 1.150] | 0.004448 | 0.35 | 0.726 | 0.932 | 0.834 | +1.9 | +1.7 | 0.6432 | 0.6443 |
| MoCA memory index score (0-15) | Any reading > 250 during wear (0/1) | 1271 | 244 | -0.017 [-0.168, +0.133] | -0.04361 | -0.22 | 0.823 | 0.940 | 0.823 | +1.9 | +2.6 | 0.0455 | 0.0477 |
| MoCA memory index score (0-15) | Time > 250, pooled (%) | 1271 | 244 | -0.180 [-0.300, -0.059] | -0.03702 | -2.91 | 0.004** | 0.053 | 0.020 (FDR<0.05) | -4.3 | -3.6 | 0.0510 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time > 250 (%) | 1271 | 207 | -0.179 [-0.300, -0.059] | -0.03768 | -2.93 | 0.003** | 0.053 | 0.020 (FDR<0.05) | -4.3 | -3.6 | 0.0509 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Any reading > 250 during wear (0/1) | 1270 | 243 | +0.066 [-0.193, +0.324] | 0.1666 | 0.50 | 0.619 | 0.932 | 0.953 | +1.7 | -0.2 | 0.0656 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Time > 250, pooled (%) | 1270 | 243 | -0.127 [-0.420, +0.166] | -0.02618 | -0.85 | 0.396 | 0.797 | 0.953 | +1.0 | -1.0 | 0.0662 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 250 (%) | 1270 | 206 | -0.127 [-0.427, +0.173] | -0.02678 | -0.83 | 0.406 | 0.808 | 0.953 | +1.0 | -1.0 | 0.0662 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading > 250 during wear (0/1) | 1270 | 243 | OR 1.108 [0.955, 1.286] | 0.2607 | 1.35 | 0.176 | 0.532 | 0.607 | +0.2 | -0.9 | 0.6738 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 250, pooled (%) | 1270 | 243 | OR 1.020 [0.899, 1.157] | 0.004029 | 0.30 | 0.762 | 0.932 | 0.958 | +1.9 | +0.8 | 0.6712 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 250 (%) | 1270 | 206 | OR 1.022 [0.901, 1.158] | 0.0045 | 0.33 | 0.738 | 0.932 | 0.958 | +1.9 | +0.8 | 0.6712 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading > 250 during wear (0/1) | 1251 | 241 | -0.022 [-0.069, +0.025] | -0.05589 | -0.92 | 0.356 | 0.758 | 0.552 | +1.2 | -0.8 | 0.1130 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 250, pooled (%) | 1251 | 241 | -0.017 [-0.036, +0.001] | -0.003548 | -1.85 | 0.064 | 0.340 | 0.265 | +1.5 | -0.5 | 0.1139 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 250 (%) | 1251 | 205 | -0.017 [-0.035, +0.001] | -0.00356 | -1.86 | 0.062 | 0.340 | 0.265 | +1.5 | -0.5 | 0.1139 | 0.1139 |
| Indoor temperature, mean (deg C) | Any reading > 250 during wear (0/1) | 1251 | 241 | -0.103 [-0.210, +0.005] | -0.2604 | -1.88 | 0.061 | 0.340 | 0.674 | -1.7 | -3.6 | 0.2902 | 0.2892 |
| Indoor temperature, mean (deg C) | Time > 250, pooled (%) | 1251 | 241 | +0.022 [-0.116, +0.161] | 0.004588 | 0.32 | 0.751 | 0.932 | 0.942 | +1.8 | -0.1 | 0.2883 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time > 250 (%) | 1251 | 205 | +0.021 [-0.114, +0.157] | 0.004465 | 0.31 | 0.757 | 0.932 | 0.942 | +1.8 | -0.1 | 0.2883 | 0.2892 |
| Indoor relative humidity, mean (%) | Any reading > 250 during wear (0/1) | 1251 | 241 | -0.174 [-0.506, +0.158] | -0.4415 | -1.03 | 0.304 | 0.688 | 0.597 | +0.9 | +1.4 | 0.2388 | 0.2403 |
| Indoor relative humidity, mean (%) | Time > 250, pooled (%) | 1251 | 241 | +0.171 [-0.075, +0.417] | 0.03502 | 1.37 | 0.172 | 0.532 | 0.585 | +0.9 | +1.4 | 0.2403 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time > 250 (%) | 1251 | 205 | +0.176 [-0.071, +0.422] | 0.03663 | 1.40 | 0.162 | 0.532 | 0.585 | +0.9 | +1.4 | 0.2403 | 0.2403 |
| Indoor VOC index, mean | Any reading > 250 during wear (0/1) | 1251 | 241 | +0.143 [-0.693, +0.979] | 0.3625 | 0.34 | 0.737 | 0.932 | 0.784 | +1.9 | +1.3 | 0.0009 | 0.0025 |
| Indoor VOC index, mean | Time > 250, pooled (%) | 1251 | 241 | -0.547 [-1.194, +0.101] | -0.1118 | -1.66 | 0.098 | 0.425 | 0.490 | +0.4 | -0.2 | 0.0028 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time > 250 (%) | 1251 | 205 | -0.546 [-1.213, +0.121] | -0.1138 | -1.61 | 0.108 | 0.441 | 0.490 | +0.4 | -0.2 | 0.0027 | 0.0025 |
| Steps per wear-day | Any reading > 250 during wear (0/1) | 1125 | 218 | +57.740 [-163.780, +279.259] | 146 | 0.51 | 0.609 | 0.932 | 0.958 | +1.7 | +5.0 | 0.1061 | 0.1080 |
| Steps per wear-day | Time > 250, pooled (%) | 1125 | 218 | +86.037 [-148.778, +320.853] | 19.24 | 0.72 | 0.473 | 0.872 | 0.958 | +1.4 | +4.7 | 0.1075 | 0.1080 |
| Steps per wear-day | Avg. daily time > 250 (%) | 1125 | 186 | +85.411 [-144.929, +315.752] | 19.77 | 0.73 | 0.467 | 0.871 | 0.958 | +1.4 | +4.7 | 0.1076 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading > 250 during wear (0/1) | 1125 | 218 | +0.450 [-0.272, +1.172] | 1.139 | 1.22 | 0.221 | 0.594 | 0.882 | +0.4 | +3.8 | 0.1234 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 250, pooled (%) | 1125 | 218 | +0.417 [-0.414, +1.247] | 0.0932 | 0.98 | 0.325 | 0.717 | 0.882 | +0.6 | +4.1 | 0.1246 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 250 (%) | 1125 | 186 | +0.414 [-0.411, +1.240] | 0.09587 | 0.98 | 0.325 | 0.717 | 0.882 | +0.6 | +4.1 | 0.1246 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading > 250 during wear (0/1) | 1128 | 218 | +0.333 [-0.102, +0.768] | 0.8428 | 1.50 | 0.133 | 0.486 | 0.186 | -0.3 | +11.0 | 0.1046 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 250, pooled (%) | 1128 | 218 | +0.491 [-0.147, +1.130] | 0.1099 | 1.51 | 0.132 | 0.484 | 0.186 | -3.0 | +8.2 | 0.1051 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 250 (%) | 1128 | 185 | +0.491 [-0.158, +1.140] | 0.1137 | 1.48 | 0.138 | 0.500 | 0.186 | -3.0 | +8.2 | 0.1050 | 0.1044 |
| Total sleep time per night (min) | Any reading > 250 during wear (0/1) | 1137 | 215 | -0.184 [-4.029, +3.660] | -0.47 | -0.09 | 0.925 | 0.977 | 0.936 | +2.0 | +4.0 | -0.0067 | -0.0051 |
| Total sleep time per night (min) | Time > 250, pooled (%) | 1137 | 215 | -0.236 [-3.860, +3.388] | -0.06004 | -0.13 | 0.898 | 0.964 | 0.936 | +2.0 | +4.0 | -0.0061 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time > 250 (%) | 1137 | 183 | -0.232 [-3.737, +3.273] | -0.06139 | -0.13 | 0.897 | 0.964 | 0.936 | +2.0 | +4.0 | -0.0061 | -0.0051 |
| Garmin stress score, mean (0-100) | Any reading > 250 during wear (0/1) | 1130 | 218 | +0.610 [-0.375, +1.594] | 1.544 | 1.21 | 0.225 | 0.599 | 0.471 | +0.5 | +8.3 | 0.0508 | 0.0510 |
| Garmin stress score, mean (0-100) | Time > 250, pooled (%) | 1130 | 218 | +0.600 [-1.274, +2.475] | 0.1345 | 0.63 | 0.530 | 0.924 | 0.708 | +0.5 | +8.3 | 0.0469 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time > 250 (%) | 1130 | 186 | +0.591 [-1.293, +2.476] | 0.1372 | 0.62 | 0.538 | 0.931 | 0.708 | +0.6 | +8.4 | 0.0468 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading > 250 during wear (0/1) | 867 | 551 | -0.210 [-0.428, +0.008] | -0.4363 | -1.89 | 0.059 | not applied (n < 1000) | not applied (n < 1000) | -1.4 | +0.1 | 0.0559 | 0.0541 |
| MoCA total score (0-30) | Time > 250, pooled (%) | 867 | 551 | -0.210 [-0.438, +0.017] | -0.01351 | -1.81 | 0.070 | not applied (n < 1000) | not applied (n < 1000) | -1.5 | +0.1 | 0.0565 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time > 250 (%) | 867 | 528 | -0.206 [-0.436, +0.024] | -0.01339 | -1.75 | 0.079 | not applied (n < 1000) | not applied (n < 1000) | -1.3 | +0.2 | 0.0564 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Any reading > 250 during wear (0/1) | 867 | 551 | OR 1.086 [0.941, 1.252] | 0.1706 | 1.13 | 0.259 | not applied (n < 1000) | not applied (n < 1000) | +0.7 | +2.4 | 0.6414 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Time > 250, pooled (%) | 867 | 551 | OR 1.154 [0.997, 1.336] | 0.009194 | 1.92 | 0.055 | not applied (n < 1000) | not applied (n < 1000) | -1.8 | -0.1 | 0.6447 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time > 250 (%) | 867 | 528 | OR 1.149 [0.993, 1.330] | 0.009035 | 1.86 | 0.063 | not applied (n < 1000) | not applied (n < 1000) | -1.6 | +0.1 | 0.6446 | 0.6425 |
| MoCA memory index score (0-15) | Any reading > 250 during wear (0/1) | 867 | 551 | -0.236 [-0.420, -0.052] | -0.49 | -2.52 | 0.012* | not applied (n < 1000) | not applied (n < 1000) | -4.2 | -2.5 | 0.0335 | 0.0286 |
| MoCA memory index score (0-15) | Time > 250, pooled (%) | 867 | 551 | -0.122 [-0.289, +0.045] | -0.00784 | -1.43 | 0.152 | not applied (n < 1000) | not applied (n < 1000) | +0.3 | +2.1 | 0.0298 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time > 250 (%) | 867 | 528 | -0.114 [-0.279, +0.052] | -0.007382 | -1.35 | 0.178 | not applied (n < 1000) | not applied (n < 1000) | +0.5 | +2.3 | 0.0296 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Any reading > 250 during wear (0/1) | 865 | 550 | -0.018 [-0.360, +0.325] | -0.03675 | -0.10 | 0.919 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.3 | 0.0769 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Time > 250, pooled (%) | 865 | 550 | +0.300 [-0.109, +0.709] | 0.01924 | 1.44 | 0.151 | not applied (n < 1000) | not applied (n < 1000) | -1.2 | +0.1 | 0.0788 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time > 250 (%) | 865 | 527 | +0.274 [-0.139, +0.687] | 0.01776 | 1.30 | 0.194 | not applied (n < 1000) | not applied (n < 1000) | -0.6 | +0.6 | 0.0784 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading > 250 during wear (0/1) | 865 | 550 | OR 1.024 [0.862, 1.216] | 0.04924 | 0.27 | 0.787 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +4.9 | 0.6298 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time > 250, pooled (%) | 865 | 550 | OR 1.129 [0.973, 1.309] | 0.007781 | 1.60 | 0.109 | not applied (n < 1000) | not applied (n < 1000) | -0.5 | +2.5 | 0.6366 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time > 250 (%) | 865 | 527 | OR 1.110 [0.956, 1.289] | 0.006796 | 1.38 | 0.169 | not applied (n < 1000) | not applied (n < 1000) | +0.2 | +3.2 | 0.6350 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading > 250 during wear (0/1) | 849 | 542 | +0.010 [-0.056, +0.075] | 0.02042 | 0.29 | 0.769 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +11.3 | 0.1296 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time > 250, pooled (%) | 849 | 542 | +0.065 [-0.019, +0.149] | 0.004143 | 1.51 | 0.130 | not applied (n < 1000) | not applied (n < 1000) | -2.0 | +7.4 | 0.1309 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time > 250 (%) | 849 | 519 | +0.065 [-0.018, +0.148] | 0.004211 | 1.53 | 0.127 | not applied (n < 1000) | not applied (n < 1000) | -2.1 | +7.3 | 0.1310 | 0.1310 |
| Indoor temperature, mean (deg C) | Any reading > 250 during wear (0/1) | 849 | 542 | -0.032 [-0.185, +0.120] | -0.06749 | -0.42 | 0.676 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +0.1 | 0.2242 | 0.2264 |
| Indoor temperature, mean (deg C) | Time > 250, pooled (%) | 849 | 542 | -0.026 [-0.186, +0.134] | -0.001669 | -0.32 | 0.750 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2227 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time > 250 (%) | 849 | 519 | -0.028 [-0.189, +0.133] | -0.001834 | -0.34 | 0.730 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2227 | 0.2264 |
| Indoor relative humidity, mean (%) | Any reading > 250 during wear (0/1) | 849 | 542 | -0.372 [-0.808, +0.064] | -0.7738 | -1.67 | 0.095 | not applied (n < 1000) | not applied (n < 1000) | -0.9 | -2.8 | 0.1862 | 0.1857 |
| Indoor relative humidity, mean (%) | Time > 250, pooled (%) | 849 | 542 | -0.083 [-0.529, +0.362] | -0.005343 | -0.37 | 0.713 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | -0.0 | 0.1840 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time > 250 (%) | 849 | 519 | -0.082 [-0.534, +0.370] | -0.005294 | -0.35 | 0.723 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | -0.0 | 0.1839 | 0.1857 |
| Indoor VOC index, mean | Any reading > 250 during wear (0/1) | 849 | 542 | +0.857 [-0.283, +1.997] | 1.782 | 1.47 | 0.141 | not applied (n < 1000) | not applied (n < 1000) | -0.0 | +0.3 | 0.0281 | 0.0276 |
| Indoor VOC index, mean | Time > 250, pooled (%) | 849 | 542 | -1.116 [-2.427, +0.196] | -0.07141 | -1.67 | 0.095 | not applied (n < 1000) | not applied (n < 1000) | -1.5 | -1.1 | 0.0291 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time > 250 (%) | 849 | 519 | -1.176 [-2.513, +0.161] | -0.07615 | -1.72 | 0.085 | not applied (n < 1000) | not applied (n < 1000) | -1.8 | -1.5 | 0.0295 | 0.0276 |
| Steps per wear-day | Any reading > 250 during wear (0/1) | 747 | 472 | +250.915 [-120.671, +622.500] | 519.9 | 1.32 | 0.186 | not applied (n < 1000) | not applied (n < 1000) | +0.1 | +0.2 | 0.1385 | 0.1390 |
| Steps per wear-day | Time > 250, pooled (%) | 747 | 472 | -82.285 [-504.678, +340.108] | -5.229 | -0.38 | 0.703 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +1.9 | 0.1373 | 0.1390 |
| Steps per wear-day | Avg. daily time > 250 (%) | 747 | 451 | -71.239 [-478.205, +335.726] | -4.592 | -0.34 | 0.732 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +2.0 | 0.1374 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading > 250 during wear (0/1) | 747 | 472 | +0.399 [-0.667, +1.465] | 0.8271 | 0.73 | 0.463 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +1.5 | 0.1525 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time > 250, pooled (%) | 747 | 472 | -0.281 [-1.440, +0.878] | -0.01786 | -0.48 | 0.635 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +1.7 | 0.1532 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time > 250 (%) | 747 | 451 | -0.247 [-1.364, +0.869] | -0.01595 | -0.43 | 0.664 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +1.8 | 0.1532 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading > 250 during wear (0/1) | 749 | 474 | +0.621 [-0.004, +1.246] | 1.288 | 1.95 | 0.051 | not applied (n < 1000) | not applied (n < 1000) | -1.9 | +4.1 | 0.1264 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time > 250, pooled (%) | 749 | 474 | +0.665 [+0.006, +1.324] | 0.04225 | 1.98 | 0.048* | not applied (n < 1000) | not applied (n < 1000) | -2.6 | +3.5 | 0.1281 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time > 250 (%) | 749 | 453 | +0.682 [+0.020, +1.344] | 0.04395 | 2.02 | 0.043* | not applied (n < 1000) | not applied (n < 1000) | -2.8 | +3.2 | 0.1281 | 0.1253 |
| Total sleep time per night (min) | Any reading > 250 during wear (0/1) | 756 | 479 | -6.730 [-12.089, -1.371] | -13.96 | -2.46 | 0.014* | not applied (n < 1000) | not applied (n < 1000) | -4.9 | -2.0 | 0.0121 | 0.0066 |
| Total sleep time per night (min) | Time > 250, pooled (%) | 756 | 479 | -0.609 [-5.403, +4.186] | -0.03984 | -0.25 | 0.804 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +4.8 | 0.0044 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time > 250 (%) | 756 | 458 | -0.516 [-5.334, +4.302] | -0.03427 | -0.21 | 0.834 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +4.9 | 0.0043 | 0.0066 |
| Garmin stress score, mean (0-100) | Any reading > 250 during wear (0/1) | 749 | 474 | +1.579 [+0.271, +2.886] | 3.273 | 2.37 | 0.018* | not applied (n < 1000) | not applied (n < 1000) | -3.8 | +9.2 | 0.0990 | 0.0947 |
| Garmin stress score, mean (0-100) | Time > 250, pooled (%) | 749 | 474 | +1.762 [+0.276, +3.248] | 0.1119 | 2.32 | 0.020* | not applied (n < 1000) | not applied (n < 1000) | -5.4 | +7.7 | 0.1010 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time > 250 (%) | 749 | 454 | +1.792 [+0.293, +3.291] | 0.1154 | 2.34 | 0.019* | not applied (n < 1000) | not applied (n < 1000) | -5.7 | +7.4 | 0.1012 | 0.0947 |


---

## Band <54

### Total analysis base

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading < 54 during wear (0/1) | 2138 | 638 | +0.136 [+0.008, +0.263] | 0.2967 | 2.09 | 0.037* | 0.108 | 0.046 (FDR<0.05) | -2.3 | +22.3 | 0.0925 | 0.0915 |
| MoCA total score (0-30) | Time < 54, pooled (%) | 2138 | 638 | +0.039 [-0.082, +0.160] | 0.07538 | 0.63 | 0.530 | 0.693 | 0.631 | +1.6 | +26.3 | 0.0907 | 0.0915 |
| MoCA total score (0-30) | Avg. daily time < 54 (%) | 2138 | 420 | +0.023 [-0.105, +0.151] | 0.05418 | 0.35 | 0.723 | 0.837 | 0.782 | +1.9 | +26.5 | 0.0906 | 0.0915 |
| Cognitive impairment (MoCA < 26) | Any reading < 54 during wear (0/1) | 2138 | 638 | OR 0.900 [0.820, 0.987] | -0.231 | -2.23 | 0.026* | 0.081 | 0.032 (FDR<0.05) | -3.0 | +10.6 | 0.6619 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Time < 54, pooled (%) | 2138 | 638 | OR 1.004 [0.918, 1.099] | 0.008243 | 0.09 | 0.926 | 0.957 | 0.926 | +2.0 | +15.6 | 0.6593 | 0.6603 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 54 (%) | 2138 | 420 | OR 1.020 [0.933, 1.114] | 0.04552 | 0.43 | 0.666 | 0.803 | 0.688 | +1.8 | +15.4 | 0.6593 | 0.6603 |
| MoCA memory index score (0-15) | Any reading < 54 during wear (0/1) | 2138 | 638 | +0.093 [-0.017, +0.203] | 0.2038 | 1.66 | 0.097 | 0.210 | 0.136 | -0.6 | +4.7 | 0.0635 | 0.0630 |
| MoCA memory index score (0-15) | Time < 54, pooled (%) | 2138 | 638 | +0.056 [-0.043, +0.155] | 0.1089 | 1.11 | 0.267 | 0.439 | 0.345 | +1.0 | +6.4 | 0.0629 | 0.0630 |
| MoCA memory index score (0-15) | Avg. daily time < 54 (%) | 2138 | 420 | +0.000 [-0.089, +0.090] | 0.0006372 | 0.01 | 0.995 | 0.995 | 0.995 | +2.0 | +7.4 | 0.0623 | 0.0630 |
| CES-D-10 depressive symptoms (0-30) | Any reading < 54 during wear (0/1) | 2135 | 637 | +0.066 [-0.139, +0.271] | 0.1443 | 0.63 | 0.527 | 0.693 | 0.632 | +1.6 | +1.8 | 0.0910 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Time < 54, pooled (%) | 2135 | 637 | -0.053 [-0.228, +0.121] | -0.1034 | -0.60 | 0.550 | 0.708 | 0.632 | +1.7 | +2.0 | 0.0909 | 0.0916 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 54 (%) | 2135 | 419 | -0.010 [-0.211, +0.191] | -0.02344 | -0.10 | 0.922 | 0.957 | 0.922 | +2.0 | +2.2 | 0.0903 | 0.0916 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading < 54 during wear (0/1) | 2135 | 637 | OR 1.060 [0.948, 1.186] | 0.128 | 1.03 | 0.304 | 0.480 | 0.427 | +1.0 | +3.7 | 0.6673 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 54, pooled (%) | 2135 | 637 | OR 0.972 [0.849, 1.113] | -0.05471 | -0.41 | 0.683 | 0.805 | 0.756 | +1.8 | +4.5 | 0.6676 | 0.6681 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 54 (%) | 2135 | 419 | OR 0.987 [0.874, 1.114] | -0.03125 | -0.22 | 0.829 | 0.892 | 0.857 | +2.0 | +4.7 | 0.6667 | 0.6681 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading < 54 during wear (0/1) | 2100 | 628 | +0.019 [-0.022, +0.060] | 0.041 | 0.90 | 0.368 | 0.533 | 0.381 | +1.1 | +12.0 | 0.1381 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 54, pooled (%) | 2100 | 628 | +0.027 [-0.028, +0.081] | 0.05161 | 0.96 | 0.337 | 0.500 | 0.361 | +0.1 | +11.0 | 0.1374 | 0.1387 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 54 (%) | 2100 | 415 | +0.041 [-0.019, +0.101] | 0.09535 | 1.34 | 0.181 | 0.341 | 0.248 | -2.4 | +8.5 | 0.1387 | 0.1387 |
| Indoor temperature, mean (deg C) | Any reading < 54 during wear (0/1) | 2100 | 628 | -0.025 [-0.112, +0.063] | -0.05401 | -0.56 | 0.579 | 0.732 | 0.982 | +1.7 | +0.2 | 0.2888 | 0.2896 |
| Indoor temperature, mean (deg C) | Time < 54, pooled (%) | 2100 | 628 | +0.080 [-0.016, +0.177] | 0.1554 | 1.63 | 0.103 | 0.218 | 0.801 | -1.4 | -2.9 | 0.2897 | 0.2896 |
| Indoor temperature, mean (deg C) | Avg. daily time < 54 (%) | 2100 | 415 | +0.071 [-0.038, +0.179] | 0.1638 | 1.28 | 0.202 | 0.365 | 0.982 | -0.6 | -2.1 | 0.2894 | 0.2896 |
| Indoor relative humidity, mean (%) | Any reading < 54 during wear (0/1) | 2100 | 628 | -0.133 [-0.396, +0.130] | -0.2906 | -0.99 | 0.321 | 0.491 | 0.898 | +1.0 | -0.9 | 0.2301 | 0.2307 |
| Indoor relative humidity, mean (%) | Time < 54, pooled (%) | 2100 | 628 | -0.238 [-0.453, -0.023] | -0.4596 | -2.17 | 0.030* | 0.091 | 0.693 | -1.3 | -3.1 | 0.2312 | 0.2307 |
| Indoor relative humidity, mean (%) | Avg. daily time < 54 (%) | 2100 | 415 | -0.263 [-0.520, -0.006] | -0.6104 | -2.01 | 0.045* | 0.127 | 0.693 | -2.0 | -3.9 | 0.2313 | 0.2307 |
| Indoor VOC index, mean | Any reading < 54 during wear (0/1) | 2100 | 628 | -0.359 [-1.067, +0.348] | -0.7848 | -1.00 | 0.319 | 0.490 | 0.868 | +1.0 | +0.9 | 0.0265 | 0.0271 |
| Indoor VOC index, mean | Time < 54, pooled (%) | 2100 | 628 | +0.024 [-0.624, +0.671] | 0.04589 | 0.07 | 0.943 | 0.967 | 0.943 | +2.0 | +2.0 | 0.0262 | 0.0271 |
| Indoor VOC index, mean | Avg. daily time < 54 (%) | 2100 | 415 | +0.152 [-0.455, +0.759] | 0.3536 | 0.49 | 0.623 | 0.778 | 0.868 | +1.8 | +1.8 | 0.0264 | 0.0271 |
| Steps per wear-day | Any reading < 54 during wear (0/1) | 1872 | 575 | -221.052 [-413.199, -28.905] | -479 | -2.25 | 0.024* | 0.079 | 0.083 | -3.0 | +5.0 | 0.1234 | 0.1222 |
| Steps per wear-day | Time < 54, pooled (%) | 1872 | 575 | -189.439 [-351.316, -27.562] | -348.6 | -2.29 | 0.022* | 0.072 | 0.083 | -1.7 | +6.3 | 0.1231 | 0.1222 |
| Steps per wear-day | Avg. daily time < 54 (%) | 1872 | 373 | -186.542 [-323.191, -49.893] | -410 | -2.68 | 0.007** | 0.028 (FDR<0.05) | 0.077 | -1.6 | +6.4 | 0.1234 | 0.1222 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading < 54 during wear (0/1) | 1872 | 575 | -0.415 [-0.997, +0.166] | -0.8998 | -1.40 | 0.162 | 0.315 | 0.250 | +0.1 | +8.2 | 0.1445 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 54, pooled (%) | 1872 | 575 | -0.389 [-0.779, +0.001] | -0.7158 | -1.95 | 0.051 | 0.138 | 0.192 | +0.3 | +8.5 | 0.1448 | 0.1447 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 54 (%) | 1872 | 373 | -0.439 [-0.881, +0.004] | -0.9642 | -1.94 | 0.052 | 0.141 | 0.192 | -0.2 | +8.0 | 0.1449 | 0.1447 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading < 54 during wear (0/1) | 1877 | 576 | -0.052 [-0.423, +0.319] | -0.1124 | -0.27 | 0.784 | 0.868 | 0.810 | +1.9 | +73.1 | 0.1476 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 54, pooled (%) | 1877 | 576 | +0.083 [-0.175, +0.341] | 0.1529 | 0.63 | 0.528 | 0.693 | 0.564 | +1.8 | +73.0 | 0.1481 | 0.1482 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 54 (%) | 1877 | 374 | +0.023 [-0.328, +0.374] | 0.04968 | 0.13 | 0.900 | 0.939 | 0.900 | +2.0 | +73.2 | 0.1478 | 0.1482 |
| Total sleep time per night (min) | Any reading < 54 during wear (0/1) | 1893 | 588 | +1.475 [-1.572, +4.522] | 3.187 | 0.95 | 0.343 | 0.502 | 0.506 | +1.1 | +10.0 | 0.0201 | 0.0209 |
| Total sleep time per night (min) | Time < 54, pooled (%) | 1893 | 588 | +0.233 [-2.577, +3.043] | 0.43 | 0.16 | 0.871 | 0.924 | 0.900 | +2.0 | +10.9 | 0.0203 | 0.0209 |
| Total sleep time per night (min) | Avg. daily time < 54 (%) | 1893 | 388 | +0.043 [-2.384, +2.469] | 0.09387 | 0.03 | 0.973 | 0.986 | 0.973 | +2.0 | +10.9 | 0.0204 | 0.0209 |
| Garmin stress score, mean (0-100) | Any reading < 54 during wear (0/1) | 1879 | 577 | -0.238 [-1.031, +0.555] | -0.5158 | -0.59 | 0.556 | 0.715 | 0.595 | +1.7 | +62.0 | 0.0894 | 0.0902 |
| Garmin stress score, mean (0-100) | Time < 54, pooled (%) | 1879 | 577 | +0.011 [-0.726, +0.748] | 0.02025 | 0.03 | 0.977 | 0.986 | 0.977 | +2.0 | +62.4 | 0.0894 | 0.0902 |
| Garmin stress score, mean (0-100) | Avg. daily time < 54 (%) | 1879 | 375 | -0.111 [-0.930, +0.708] | -0.2446 | -0.27 | 0.790 | 0.868 | 0.817 | +1.9 | +62.3 | 0.0892 | 0.0902 |

### Healthy group (no diabetes + pre-diabetes / lifestyle)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading < 54 during wear (0/1) | 1271 | 408 | +0.166 [+0.016, +0.316] | 0.3559 | 2.18 | 0.030* | 0.201 | 0.066 | -2.6 | +11.1 | 0.0811 | 0.0789 |
| MoCA total score (0-30) | Time < 54, pooled (%) | 1271 | 408 | +0.029 [-0.127, +0.185] | 0.05016 | 0.36 | 0.720 | 0.932 | 0.820 | +1.9 | +15.6 | 0.0771 | 0.0789 |
| MoCA total score (0-30) | Avg. daily time < 54 (%) | 1271 | 265 | +0.030 [-0.108, +0.169] | 0.07201 | 0.43 | 0.668 | 0.932 | 0.820 | +1.8 | +15.5 | 0.0774 | 0.0789 |
| Cognitive impairment (MoCA < 26) | Any reading < 54 during wear (0/1) | 1271 | 408 | OR 0.881 [0.777, 0.998] | -0.2719 | -1.99 | 0.046* | 0.280 | 0.479 | -2.0 | -2.2 | 0.6460 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Time < 54, pooled (%) | 1271 | 408 | OR 1.018 [0.904, 1.146] | 0.03169 | 0.30 | 0.766 | 0.932 | 0.848 | +1.9 | +1.7 | 0.6430 | 0.6443 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 54 (%) | 1271 | 265 | OR 1.023 [0.909, 1.151] | 0.05371 | 0.38 | 0.706 | 0.932 | 0.834 | +1.9 | +1.6 | 0.6432 | 0.6443 |
| MoCA memory index score (0-15) | Any reading < 54 during wear (0/1) | 1271 | 408 | +0.162 [+0.024, +0.300] | 0.3472 | 2.30 | 0.022* | 0.158 | 0.051 | -3.0 | -2.3 | 0.0490 | 0.0477 |
| MoCA memory index score (0-15) | Time < 54, pooled (%) | 1271 | 408 | +0.106 [-0.127, +0.340] | 0.1869 | 0.89 | 0.372 | 0.771 | 0.462 | -0.2 | +0.5 | 0.0446 | 0.0477 |
| MoCA memory index score (0-15) | Avg. daily time < 54 (%) | 1271 | 265 | +0.067 [-0.081, +0.216] | 0.1601 | 0.89 | 0.373 | 0.771 | 0.462 | +1.1 | +1.8 | 0.0466 | 0.0477 |
| CES-D-10 depressive symptoms (0-30) | Any reading < 54 during wear (0/1) | 1270 | 408 | +0.035 [-0.230, +0.300] | 0.07489 | 0.26 | 0.796 | 0.939 | 0.953 | +1.9 | -0.1 | 0.0662 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Time < 54, pooled (%) | 1270 | 408 | -0.052 [-0.294, +0.191] | -0.0907 | -0.42 | 0.676 | 0.932 | 0.953 | +1.8 | -0.1 | 0.0655 | 0.0675 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 54 (%) | 1270 | 265 | -0.006 [-0.212, +0.199] | -0.01455 | -0.06 | 0.953 | 0.983 | 0.953 | +2.0 | +0.0 | 0.0658 | 0.0675 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading < 54 during wear (0/1) | 1270 | 408 | OR 1.078 [0.927, 1.255] | 0.1616 | 0.98 | 0.329 | 0.717 | 0.863 | +1.1 | -0.1 | 0.6726 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 54, pooled (%) | 1270 | 408 | OR 0.993 [0.825, 1.195] | -0.01248 | -0.08 | 0.940 | 0.981 | 0.958 | +2.0 | +0.9 | 0.6744 | 0.6758 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 54 (%) | 1270 | 265 | OR 0.947 [0.764, 1.174] | -0.1284 | -0.50 | 0.620 | 0.932 | 0.958 | +1.7 | +0.6 | 0.6760 | 0.6758 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading < 54 during wear (0/1) | 1251 | 400 | -0.004 [-0.055, +0.048] | -0.007845 | -0.14 | 0.889 | 0.964 | 0.987 | +2.0 | -0.0 | 0.1117 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 54, pooled (%) | 1251 | 400 | -0.010 [-0.046, +0.025] | -0.0175 | -0.55 | 0.580 | 0.932 | 0.850 | +1.8 | -0.2 | 0.1126 | 0.1139 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 54 (%) | 1251 | 260 | -0.009 [-0.045, +0.026] | -0.02234 | -0.52 | 0.603 | 0.932 | 0.850 | +1.9 | -0.1 | 0.1129 | 0.1139 |
| Indoor temperature, mean (deg C) | Any reading < 54 during wear (0/1) | 1251 | 400 | -0.013 [-0.123, +0.096] | -0.02802 | -0.23 | 0.815 | 0.939 | 0.942 | +1.9 | -0.0 | 0.2881 | 0.2892 |
| Indoor temperature, mean (deg C) | Time < 54, pooled (%) | 1251 | 400 | +0.114 [-0.012, +0.241] | 0.1995 | 1.77 | 0.077 | 0.385 | 0.674 | -2.5 | -4.5 | 0.2903 | 0.2892 |
| Indoor temperature, mean (deg C) | Avg. daily time < 54 (%) | 1251 | 260 | +0.103 [-0.046, +0.253] | 0.2442 | 1.36 | 0.175 | 0.532 | 0.776 | -1.7 | -3.7 | 0.2891 | 0.2892 |
| Indoor relative humidity, mean (%) | Any reading < 54 during wear (0/1) | 1251 | 400 | -0.166 [-0.500, +0.167] | -0.3568 | -0.98 | 0.327 | 0.717 | 0.597 | +1.0 | +1.5 | 0.2391 | 0.2403 |
| Indoor relative humidity, mean (%) | Time < 54, pooled (%) | 1251 | 400 | -0.286 [-0.477, -0.096] | -0.4995 | -2.94 | 0.003** | 0.052 | 0.050 | -1.0 | -0.5 | 0.2415 | 0.2403 |
| Indoor relative humidity, mean (%) | Avg. daily time < 54 (%) | 1251 | 260 | -0.324 [-0.521, -0.127] | -0.7639 | -3.22 | 0.001** | 0.036 (FDR<0.05) | 0.040 (FDR<0.05) | -1.8 | -1.3 | 0.2417 | 0.2403 |
| Indoor VOC index, mean | Any reading < 54 during wear (0/1) | 1251 | 400 | -0.483 [-1.347, +0.381] | -1.036 | -1.10 | 0.273 | 0.648 | 0.564 | +0.8 | +0.1 | 0.0026 | 0.0025 |
| Indoor VOC index, mean | Time < 54, pooled (%) | 1251 | 400 | -0.145 [-0.923, +0.633] | -0.2529 | -0.36 | 0.715 | 0.932 | 0.784 | +1.9 | +1.3 | 0.0019 | 0.0025 |
| Indoor VOC index, mean | Avg. daily time < 54 (%) | 1251 | 260 | -0.142 [-0.964, +0.679] | -0.3362 | -0.34 | 0.734 | 0.932 | 0.784 | +1.9 | +1.3 | 0.0018 | 0.0025 |
| Steps per wear-day | Any reading < 54 during wear (0/1) | 1125 | 374 | -14.893 [-238.820, +209.035] | -31.6 | -0.13 | 0.896 | 0.964 | 0.958 | +2.0 | +5.3 | 0.1064 | 0.1080 |
| Steps per wear-day | Time < 54, pooled (%) | 1125 | 374 | -60.764 [-227.826, +106.297] | -101.5 | -0.71 | 0.476 | 0.872 | 0.958 | +1.7 | +5.0 | 0.1077 | 0.1080 |
| Steps per wear-day | Avg. daily time < 54 (%) | 1125 | 241 | -28.610 [-225.739, +168.519] | -64.17 | -0.28 | 0.776 | 0.932 | 0.958 | +1.9 | +5.2 | 0.1073 | 0.1080 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading < 54 during wear (0/1) | 1125 | 374 | +0.087 [-0.625, +0.799] | 0.1846 | 0.24 | 0.811 | 0.939 | 0.931 | +1.9 | +5.4 | 0.1229 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 54, pooled (%) | 1125 | 374 | -0.077 [-0.797, +0.643] | -0.1286 | -0.21 | 0.834 | 0.945 | 0.931 | +2.0 | +5.4 | 0.1237 | 0.1245 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 54 (%) | 1125 | 241 | -0.074 [-0.790, +0.643] | -0.165 | -0.20 | 0.840 | 0.946 | 0.931 | +2.0 | +5.4 | 0.1234 | 0.1245 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading < 54 during wear (0/1) | 1128 | 373 | +0.205 [-0.242, +0.652] | 0.4364 | 0.90 | 0.368 | 0.771 | 0.439 | +1.2 | +12.4 | 0.1038 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 54, pooled (%) | 1128 | 373 | +0.172 [-0.132, +0.476] | 0.2878 | 1.11 | 0.267 | 0.645 | 0.345 | +1.4 | +12.6 | 0.1044 | 0.1044 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 54 (%) | 1128 | 240 | +0.124 [-0.190, +0.438] | 0.2783 | 0.77 | 0.439 | 0.851 | 0.504 | +1.7 | +12.9 | 0.1035 | 0.1044 |
| Total sleep time per night (min) | Any reading < 54 during wear (0/1) | 1137 | 383 | +0.390 [-3.480, +4.261] | 0.8253 | 0.20 | 0.843 | 0.946 | 0.936 | +2.0 | +4.0 | -0.0064 | -0.0051 |
| Total sleep time per night (min) | Time < 54, pooled (%) | 1137 | 383 | -1.573 [-3.859, +0.713] | -2.641 | -1.35 | 0.177 | 0.532 | 0.936 | +1.4 | +3.4 | -0.0051 | -0.0051 |
| Total sleep time per night (min) | Avg. daily time < 54 (%) | 1137 | 250 | -1.782 [-3.975, +0.411] | -4.011 | -1.59 | 0.111 | 0.441 | 0.936 | +1.2 | +3.2 | -0.0048 | -0.0051 |
| Garmin stress score, mean (0-100) | Any reading < 54 during wear (0/1) | 1130 | 374 | +0.367 [-0.625, +1.360] | 0.7802 | 0.73 | 0.468 | 0.871 | 0.708 | +1.5 | +9.2 | 0.0500 | 0.0510 |
| Garmin stress score, mean (0-100) | Time < 54, pooled (%) | 1130 | 374 | +0.037 [-0.999, +1.073] | 0.0618 | 0.07 | 0.944 | 0.981 | 0.965 | +2.0 | +9.8 | 0.0496 | 0.0510 |
| Garmin stress score, mean (0-100) | Avg. daily time < 54 (%) | 1130 | 241 | -0.121 [-1.150, +0.909] | -0.271 | -0.23 | 0.818 | 0.939 | 0.920 | +1.9 | +9.7 | 0.0494 | 0.0510 |

### Non-healthy group (T2D non-insulin + T2D insulin)

| Outcome | Predictor (entered alone) | n | n with any time in band | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, family = all tests in population) | q (BH, family = this outcome) | dAIC vs covariates-only | dAIC vs HbA1c-only | CV R2 / AUC (predictor | covariates only) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA total score (0-30) | Any reading < 54 during wear (0/1) | 867 | 230 | +0.049 [-0.178, +0.276] | 0.1107 | 0.42 | 0.673 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +3.3 | 0.0515 | 0.0541 |
| MoCA total score (0-30) | Time < 54, pooled (%) | 867 | 230 | +0.023 [-0.313, +0.358] | 0.05366 | 0.13 | 0.895 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0494 | 0.0541 |
| MoCA total score (0-30) | Avg. daily time < 54 (%) | 867 | 155 | +0.000 [-0.269, +0.269] | 0.001075 | 0.00 | 0.997 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.5 | 0.0502 | 0.0541 |
| Cognitive impairment (MoCA < 26) | Any reading < 54 during wear (0/1) | 867 | 230 | OR 0.947 [0.822, 1.091] | -0.1236 | -0.76 | 0.450 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | +3.1 | 0.6412 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Time < 54, pooled (%) | 867 | 230 | OR 1.008 [0.878, 1.157] | 0.01863 | 0.11 | 0.912 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.7 | 0.6398 | 0.6425 |
| Cognitive impairment (MoCA < 26) | Avg. daily time < 54 (%) | 867 | 155 | OR 1.028 [0.895, 1.181] | 0.06254 | 0.39 | 0.699 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +3.5 | 0.6402 | 0.6425 |
| MoCA memory index score (0-15) | Any reading < 54 during wear (0/1) | 867 | 230 | -0.029 [-0.211, +0.153] | -0.06479 | -0.31 | 0.758 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +3.7 | 0.0271 | 0.0286 |
| MoCA memory index score (0-15) | Time < 54, pooled (%) | 867 | 230 | -0.060 [-0.188, +0.068] | -0.1426 | -0.91 | 0.360 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +3.4 | 0.0281 | 0.0286 |
| MoCA memory index score (0-15) | Avg. daily time < 54 (%) | 867 | 155 | -0.103 [-0.255, +0.050] | -0.2345 | -1.32 | 0.187 | not applied (n < 1000) | not applied (n < 1000) | +0.8 | +2.5 | 0.0292 | 0.0286 |
| CES-D-10 depressive symptoms (0-30) | Any reading < 54 during wear (0/1) | 865 | 229 | +0.122 [-0.201, +0.446] | 0.2767 | 0.74 | 0.459 | not applied (n < 1000) | not applied (n < 1000) | +1.5 | +2.8 | 0.0779 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Time < 54, pooled (%) | 865 | 229 | -0.049 [-0.423, +0.325] | -0.1166 | -0.26 | 0.797 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +3.2 | 0.0780 | 0.0796 |
| CES-D-10 depressive symptoms (0-30) | Avg. daily time < 54 (%) | 865 | 154 | -0.008 [-0.519, +0.502] | -0.01904 | -0.03 | 0.974 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +3.3 | 0.0755 | 0.0796 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Any reading < 54 during wear (0/1) | 865 | 229 | OR 1.046 [0.886, 1.236] | 0.1029 | 0.53 | 0.593 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +4.7 | 0.6306 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Time < 54, pooled (%) | 865 | 229 | OR 0.957 [0.797, 1.149] | -0.1044 | -0.47 | 0.638 | not applied (n < 1000) | not applied (n < 1000) | +1.8 | +4.8 | 0.6294 | 0.6337 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | Avg. daily time < 54 (%) | 865 | 154 | OR 1.013 [0.869, 1.180] | 0.02887 | 0.16 | 0.871 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +5.0 | 0.6290 | 0.6337 |
| Indoor PM2.5, log(1 + mean ug/m3) | Any reading < 54 during wear (0/1) | 849 | 228 | +0.061 [-0.008, +0.129] | 0.1365 | 1.74 | 0.082 | not applied (n < 1000) | not applied (n < 1000) | -1.6 | +7.8 | 0.1324 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Time < 54, pooled (%) | 849 | 228 | +0.113 [+0.033, +0.193] | 0.2665 | 2.78 | 0.005** | not applied (n < 1000) | not applied (n < 1000) | -10.6 | -1.2 | 0.1385 | 0.1310 |
| Indoor PM2.5, log(1 + mean ug/m3) | Avg. daily time < 54 (%) | 849 | 155 | +0.119 [-0.007, +0.246] | 0.2695 | 1.84 | 0.065 | not applied (n < 1000) | not applied (n < 1000) | -12.1 | -2.7 | 0.1309 | 0.1310 |
| Indoor temperature, mean (deg C) | Any reading < 54 during wear (0/1) | 849 | 228 | -0.038 [-0.182, +0.107] | -0.08461 | -0.51 | 0.610 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +0.1 | 0.2238 | 0.2264 |
| Indoor temperature, mean (deg C) | Time < 54, pooled (%) | 849 | 228 | +0.018 [-0.130, +0.167] | 0.04314 | 0.24 | 0.809 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2243 | 0.2264 |
| Indoor temperature, mean (deg C) | Avg. daily time < 54 (%) | 849 | 155 | +0.026 [-0.147, +0.199] | 0.05869 | 0.29 | 0.769 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +0.2 | 0.2230 | 0.2264 |
| Indoor relative humidity, mean (%) | Any reading < 54 during wear (0/1) | 849 | 228 | -0.048 [-0.486, +0.391] | -0.1076 | -0.21 | 0.831 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +0.1 | 0.1833 | 0.1857 |
| Indoor relative humidity, mean (%) | Time < 54, pooled (%) | 849 | 228 | -0.117 [-0.751, +0.516] | -0.2766 | -0.36 | 0.717 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | -0.2 | 0.1824 | 0.1857 |
| Indoor relative humidity, mean (%) | Avg. daily time < 54 (%) | 849 | 155 | -0.166 [-0.761, +0.429] | -0.3747 | -0.55 | 0.586 | not applied (n < 1000) | not applied (n < 1000) | +1.4 | -0.5 | 0.1805 | 0.1857 |
| Indoor VOC index, mean | Any reading < 54 during wear (0/1) | 849 | 228 | -0.137 [-1.388, +1.114] | -0.3089 | -0.21 | 0.830 | not applied (n < 1000) | not applied (n < 1000) | +1.9 | +2.3 | 0.0255 | 0.0276 |
| Indoor VOC index, mean | Time < 54, pooled (%) | 849 | 228 | +0.339 [-0.480, +1.159] | 0.8004 | 0.81 | 0.417 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +2.0 | 0.0274 | 0.0276 |
| Indoor VOC index, mean | Avg. daily time < 54 (%) | 849 | 155 | +0.564 [-0.341, +1.469] | 1.276 | 1.22 | 0.222 | not applied (n < 1000) | not applied (n < 1000) | +1.1 | +1.4 | 0.0268 | 0.0276 |
| Steps per wear-day | Any reading < 54 during wear (0/1) | 747 | 201 | -502.034 [-853.109, -150.960] | -1131 | -2.80 | 0.005** | not applied (n < 1000) | not applied (n < 1000) | -5.9 | -5.8 | 0.1442 | 0.1390 |
| Steps per wear-day | Time < 54, pooled (%) | 747 | 201 | -407.095 [-872.220, +58.030] | -909.1 | -1.72 | 0.086 | not applied (n < 1000) | not applied (n < 1000) | -3.2 | -3.1 | 0.1400 | 0.1390 |
| Steps per wear-day | Avg. daily time < 54 (%) | 747 | 132 | -386.633 [-687.348, -85.917] | -825 | -2.52 | 0.012* | not applied (n < 1000) | not applied (n < 1000) | -2.8 | -2.7 | 0.1427 | 0.1390 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Any reading < 54 during wear (0/1) | 747 | 201 | -1.065 [-2.070, -0.060] | -2.4 | -2.08 | 0.038* | not applied (n < 1000) | not applied (n < 1000) | -2.3 | -2.3 | 0.1559 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Time < 54, pooled (%) | 747 | 201 | -0.900 [-2.403, +0.604] | -2.009 | -1.17 | 0.241 | not applied (n < 1000) | not applied (n < 1000) | -1.1 | -1.1 | 0.1530 | 0.1546 |
| Brisk-cadence minutes per day (>= 100 steps/min) | Avg. daily time < 54 (%) | 747 | 132 | -0.899 [-2.071, +0.274] | -1.918 | -1.50 | 0.133 | not applied (n < 1000) | not applied (n < 1000) | -1.1 | -1.1 | 0.1554 | 0.1546 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Any reading < 54 during wear (0/1) | 749 | 203 | -0.056 [-0.653, +0.540] | -0.127 | -0.19 | 0.853 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +8.0 | 0.1220 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Time < 54, pooled (%) | 749 | 203 | +0.191 [-0.362, +0.744] | 0.4269 | 0.68 | 0.499 | not applied (n < 1000) | not applied (n < 1000) | +1.6 | +7.7 | 0.1239 | 0.1253 |
| Resting heart-rate proxy (daily 5th pct, bpm) | Avg. daily time < 54 (%) | 749 | 134 | -0.027 [-0.979, +0.925] | -0.05779 | -0.06 | 0.956 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +8.1 | 0.1219 | 0.1253 |
| Total sleep time per night (min) | Any reading < 54 during wear (0/1) | 756 | 205 | +3.020 [-1.996, +8.036] | 6.788 | 1.18 | 0.238 | not applied (n < 1000) | not applied (n < 1000) | +0.6 | +3.5 | 0.0046 | 0.0066 |
| Total sleep time per night (min) | Time < 54, pooled (%) | 756 | 205 | +4.193 [+0.145, +8.240] | 9.374 | 2.03 | 0.042* | not applied (n < 1000) | not applied (n < 1000) | -0.8 | +2.1 | 0.0094 | 0.0066 |
| Total sleep time per night (min) | Avg. daily time < 54 (%) | 756 | 138 | +2.990 [-0.505, +6.485] | 6.407 | 1.68 | 0.094 | not applied (n < 1000) | not applied (n < 1000) | +0.6 | +3.5 | 0.0070 | 0.0066 |
| Garmin stress score, mean (0-100) | Any reading < 54 during wear (0/1) | 749 | 203 | -0.618 [-1.896, +0.660] | -1.39 | -0.95 | 0.343 | not applied (n < 1000) | not applied (n < 1000) | +1.1 | +14.2 | 0.0931 | 0.0947 |
| Garmin stress score, mean (0-100) | Time < 54, pooled (%) | 749 | 203 | +0.364 [-0.839, +1.568] | 0.8143 | 0.59 | 0.553 | not applied (n < 1000) | not applied (n < 1000) | +1.7 | +14.8 | 0.0936 | 0.0947 |
| Garmin stress score, mean (0-100) | Avg. daily time < 54 (%) | 749 | 134 | +0.039 [-1.729, +1.808] | 0.08406 | 0.04 | 0.965 | not applied (n < 1000) | not applied (n < 1000) | +2.0 | +15.1 | 0.0921 | 0.0947 |
