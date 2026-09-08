# Phase 6b - Single-predictor tables inside the actual-value glucose cohorts

Cohorts are defined by each participant's own CGM readings over the wear period; inside every cohort the full Phase 6 predictor set (HbA1c, CGM level and variability, time in range 70-180, and the glucose bands) is entered one measure at a time with the Phase 5 covariates, in the total, healthy (no diabetes + pre-diabetes) and non-healthy (T2D oral + insulin) populations.

## Cohort sizes and feasibility

| Cohort | Definition | N | Healthy | Non-healthy | MoCA | MoCA<26 events | CES-D>=10 events | Environment | Steps | Resting HR | Sleep | Feasible? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| normal_70_180 | Normal range only: every reading within 70-180 | 39 | 30 | 9 | 39 | 10 | 6 | 37 | 35 | 36 | 34 | no - fewer than 100 participants |
| near_normal_99 | Near-normal substitute: >= 99% of readings within 70-180 | 454 | 393 | 61 | 454 | 148 | 82 | 443 | 401 | 403 | 409 | yes |
| within_54_250 | Within 54-250: no reading < 54 and none > 250 | 890 | 685 | 205 | 890 | 336 | 155 | 872 | 771 | 774 | 779 | yes |
| hypo_below_54 | Hypoglycaemia exposure: at least one reading < 54 | 638 | 408 | 230 | 638 | 228 | 137 | 628 | 575 | 576 | 588 | yes |
| hyper_above_250 | Hyperglycaemia exposure: at least one reading > 250 | 795 | 244 | 551 | 795 | 371 | 165 | 783 | 690 | 692 | 694 | yes |

Overlap of the exposure cohorts (total): hypoglycaemia only 453, hyperglycaemia only 610, both 185, neither (within 54-250) 890.

**FDR.** The Phase 6 rule (BH only when n >= 1000) is not met by any cohort, so the rule column reads 'not applied'. An informational BH q over all tests in the population is shown alongside and must be read as such.

## Significance counts

| Cohort | Population | Tests | n min | n max | Raw p < 0.05 | Informational q < 0.05 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Hyperglycaemia exposure: at least one reading > 250 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 420 | 215 | 244 | 49 | 10 |
| Hyperglycaemia exposure: at least one reading > 250 | Non-healthy group (T2D non-insulin + T2D insulin) | 420 | 472 | 551 | 70 | 4 |
| Hyperglycaemia exposure: at least one reading > 250 | Total analysis base | 420 | 690 | 795 | 117 | 50 |
| Hypoglycaemia exposure: at least one reading < 54 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 420 | 373 | 408 | 31 | 0 |
| Hypoglycaemia exposure: at least one reading < 54 | Non-healthy group (T2D non-insulin + T2D insulin) | 420 | 201 | 230 | 81 | 10 |
| Hypoglycaemia exposure: at least one reading < 54 | Total analysis base | 420 | 575 | 638 | 144 | 66 |
| Near-normal substitute: >= 99% of readings within 70-180 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 392 | 344 | 393 | 26 | 0 |
| Near-normal substitute: >= 99% of readings within 70-180 | Non-healthy group (T2D non-insulin + T2D insulin) | 96 | 60 | 61 | 0 | 0 |
| Near-normal substitute: >= 99% of readings within 70-180 | Total analysis base | 392 | 401 | 454 | 26 | 0 |
| Within 54-250: no reading < 54 and none > 250 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 322 | 593 | 685 | 38 | 10 |
| Within 54-250: no reading < 54 and none > 250 | Non-healthy group (T2D non-insulin + T2D insulin) | 322 | 177 | 205 | 30 | 0 |
| Within 54-250: no reading < 54 and none > 250 | Total analysis base | 322 | 771 | 890 | 73 | 22 |

---

## Cohort: Normal range only: every reading within 70-180

_Not analysed: only 39 participants (fewer than 100). See the near-normal substitute cohort._

---

## Cohort: Near-normal substitute: >= 99% of readings within 70-180

### Population: Total analysis base

#### MoCA total score (0-30)
*n = 454; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 454 | -0.125 [-0.391, +0.141] | -0.3988 | -0.92 | 0.356 | not applied (n < 1000) | 0.843 | +1.0 | +0.0 | 0.0592 | 0.0631 |
| Mean glucose (mg/dL) | 454 | -0.222 [-0.475, +0.032] | -0.02957 | -1.72 | 0.086 | not applied (n < 1000) | 0.704 | -1.3 | -2.3 | 0.0696 | 0.0631 |
| GMI (%) | 454 | -0.222 [-0.475, +0.032] | -1.236 | -1.72 | 0.086 | not applied (n < 1000) | 0.704 | -1.3 | -2.3 | 0.0696 | 0.0631 |
| Nocturnal mean 00-06h (mg/dL) | 454 | -0.120 [-0.382, +0.142] | -0.01235 | -0.90 | 0.369 | not applied (n < 1000) | 0.843 | +1.1 | +0.0 | 0.0613 | 0.0631 |
| Glucose SD, pooled (mg/dL) | 454 | -0.005 [-0.276, +0.266] | -0.001989 | -0.03 | 0.973 | not applied (n < 1000) | 0.986 | +2.0 | +0.9 | 0.0556 | 0.0631 |
| Avg. daily SD (mg/dL) | 454 | +0.111 [-0.151, +0.373] | 0.04635 | 0.83 | 0.406 | not applied (n < 1000) | 0.844 | +1.2 | +0.2 | 0.0552 | 0.0631 |
| CV (%) | 454 | +0.090 [-0.166, +0.346] | 0.04181 | 0.69 | 0.492 | not applied (n < 1000) | 0.853 | +1.5 | +0.4 | 0.0605 | 0.0631 |
| Mean / SD ratio | 454 | -0.109 [-0.362, +0.143] | -0.1033 | -0.85 | 0.397 | not applied (n < 1000) | 0.843 | +1.2 | +0.2 | 0.0616 | 0.0631 |
| Avg. daily mean / SD | 454 | -0.168 [-0.426, +0.091] | -0.1229 | -1.27 | 0.204 | not applied (n < 1000) | 0.727 | +0.2 | -0.9 | 0.0611 | 0.0631 |
| MAG (mg/dL/h) | 454 | -0.057 [-0.295, +0.182] | -0.00966 | -0.46 | 0.642 | not applied (n < 1000) | 0.939 | +1.8 | +0.7 | 0.0554 | 0.0631 |
| Avg. daily range (mg/dL) | 454 | +0.108 [-0.146, +0.361] | 0.009613 | 0.83 | 0.405 | not applied (n < 1000) | 0.844 | +1.2 | +0.2 | 0.0540 | 0.0631 |
| SD of daily means (mg/dL) | 454 | -0.296 [-0.593, +0.002] | -0.1585 | -1.95 | 0.052 | not applied (n < 1000) | 0.692 | -3.7 | -4.8 | 0.0655 | 0.0631 |
| Time in range 70-180, pooled (%) | 454 | +0.047 [-0.199, +0.292] | 0.1564 | 0.37 | 0.708 | not applied (n < 1000) | 0.950 | +1.9 | +0.8 | 0.0592 | 0.0631 |
| Avg. daily time in range 70-180 (%) | 454 | -0.071 [-0.332, +0.191] | -0.2288 | -0.53 | 0.596 | not applied (n < 1000) | 0.920 | +1.7 | +0.6 | 0.0594 | 0.0631 |
| Any reading < 54 during wear (0/1) | 454 | +0.166 [-0.072, +0.404] | 0.4445 | 1.37 | 0.172 | not applied (n < 1000) | 0.727 | +0.2 | -0.8 | 0.0654 | 0.0631 |
| Time < 54, pooled (%) | 454 | +0.079 [-0.185, +0.343] | 1.472 | 0.59 | 0.558 | not applied (n < 1000) | 0.897 | +1.6 | +0.6 | 0.0603 | 0.0631 |
| Avg. daily time < 54 (%) | 454 | +0.112 [-0.138, +0.363] | 2.797 | 0.88 | 0.379 | not applied (n < 1000) | 0.843 | +1.2 | +0.1 | 0.0623 | 0.0631 |
| Time 54-69, pooled (%) | 454 | +0.142 [-0.099, +0.384] | 0.7826 | 1.16 | 0.247 | not applied (n < 1000) | 0.727 | +0.7 | -0.4 | 0.0643 | 0.0631 |
| Avg. daily time 54-69 (%) | 454 | +0.190 [-0.041, +0.421] | 1.064 | 1.62 | 0.106 | not applied (n < 1000) | 0.717 | -0.4 | -1.4 | 0.0670 | 0.0631 |
| Time < 70, pooled (%) | 454 | +0.146 [-0.095, +0.388] | 0.7164 | 1.19 | 0.234 | not applied (n < 1000) | 0.727 | +0.6 | -0.5 | 0.0639 | 0.0631 |
| Avg. daily time < 70 (%) | 454 | +0.196 [-0.033, +0.425] | 1.002 | 1.68 | 0.094 | not applied (n < 1000) | 0.704 | -0.5 | -1.6 | 0.0673 | 0.0631 |
| Time 54-250, pooled (%) | 454 | -0.065 [-0.332, +0.202] | -1.187 | -0.48 | 0.633 | not applied (n < 1000) | 0.939 | +1.7 | +0.7 | 0.0594 | 0.0631 |
| Avg. daily time 54-250 (%) | 454 | -0.094 [-0.334, +0.147] | -2.278 | -0.76 | 0.446 | not applied (n < 1000) | 0.845 | +1.4 | +0.4 | 0.0599 | 0.0631 |
| Time 181-250, pooled (%) | 454 | -0.155 [-0.407, +0.097] | -0.555 | -1.21 | 0.227 | not applied (n < 1000) | 0.727 | +0.4 | -0.6 | 0.0621 | 0.0631 |
| Avg. daily time 181-250 (%) | 454 | -0.054 [-0.318, +0.209] | -0.1943 | -0.40 | 0.686 | not applied (n < 1000) | 0.949 | +1.8 | +0.8 | 0.0583 | 0.0631 |
| Time > 180, pooled (%) | 454 | -0.157 [-0.408, +0.094] | -0.5611 | -1.22 | 0.221 | not applied (n < 1000) | 0.727 | +0.4 | -0.7 | 0.0622 | 0.0631 |
| Avg. daily time > 180 (%) | 454 | -0.057 [-0.320, +0.207] | -0.202 | -0.42 | 0.673 | not applied (n < 1000) | 0.949 | +1.8 | +0.7 | 0.0584 | 0.0631 |
| Nocturnal time > 180 (%) | 454 | -0.145 [-0.480, +0.191] | -0.4047 | -0.85 | 0.398 | not applied (n < 1000) | 0.843 | +0.7 | -0.4 | 0.0525 | 0.0631 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Cognitive impairment (MoCA < 26)
*n = 454; events = 148; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 454 | OR 1.017 [0.819, 1.263] | 0.05276 | 0.15 | 0.881 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.6340 | 0.6382 |
| Mean glucose (mg/dL) | 454 | OR 1.180 [0.958, 1.454] | 0.02207 | 1.55 | 0.120 | not applied (n < 1000) | 0.727 | -0.4 | -2.4 | 0.6402 | 0.6382 |
| GMI (%) | 454 | OR 1.180 [0.958, 1.454] | 0.9227 | 1.55 | 0.120 | not applied (n < 1000) | 0.727 | -0.4 | -2.4 | 0.6402 | 0.6382 |
| Nocturnal mean 00-06h (mg/dL) | 454 | OR 1.104 [0.890, 1.370] | 0.01019 | 0.90 | 0.366 | not applied (n < 1000) | 0.843 | +1.2 | -0.8 | 0.6391 | 0.6382 |
| Glucose SD, pooled (mg/dL) | 454 | OR 1.005 [0.815, 1.240] | 0.002202 | 0.05 | 0.961 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.6305 | 0.6382 |
| Avg. daily SD (mg/dL) | 454 | OR 0.965 [0.783, 1.190] | -0.01476 | -0.33 | 0.740 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.6321 | 0.6382 |
| CV (%) | 454 | OR 0.938 [0.761, 1.158] | -0.02957 | -0.59 | 0.553 | not applied (n < 1000) | 0.891 | +1.6 | -0.3 | 0.6357 | 0.6382 |
| Mean / SD ratio | 454 | OR 1.087 [0.882, 1.339] | 0.0786 | 0.78 | 0.435 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.6356 | 0.6382 |
| Avg. daily mean / SD | 454 | OR 1.094 [0.889, 1.346] | 0.06568 | 0.85 | 0.397 | not applied (n < 1000) | 0.843 | +1.3 | -0.7 | 0.6354 | 0.6382 |
| MAG (mg/dL/h) | 454 | OR 1.151 [0.933, 1.420] | 0.02403 | 1.31 | 0.189 | not applied (n < 1000) | 0.727 | +0.3 | -1.7 | 0.6404 | 0.6382 |
| Avg. daily range (mg/dL) | 454 | OR 1.021 [0.830, 1.257] | 0.001872 | 0.20 | 0.843 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.6318 | 0.6382 |
| SD of daily means (mg/dL) | 454 | OR 1.133 [0.920, 1.394] | 0.06679 | 1.18 | 0.239 | not applied (n < 1000) | 0.727 | +0.6 | -1.4 | 0.6391 | 0.6382 |
| Time in range 70-180, pooled (%) | 454 | OR 0.958 [0.778, 1.179] | -0.1442 | -0.41 | 0.683 | not applied (n < 1000) | 0.949 | +1.8 | -0.1 | 0.6290 | 0.6382 |
| Avg. daily time in range 70-180 (%) | 454 | OR 1.035 [0.841, 1.273] | 0.1098 | 0.32 | 0.748 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.6334 | 0.6382 |
| Any reading < 54 during wear (0/1) | 454 | OR 0.943 [0.762, 1.168] | -0.1563 | -0.54 | 0.592 | not applied (n < 1000) | 0.920 | +1.7 | -0.3 | 0.6376 | 0.6382 |
| Time < 54, pooled (%) | 454 | OR 0.968 [0.780, 1.202] | -0.6017 | -0.29 | 0.771 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.6359 | 0.6382 |
| Avg. daily time < 54 (%) | 454 | OR 0.906 [0.713, 1.152] | -2.446 | -0.80 | 0.422 | not applied (n < 1000) | 0.845 | +1.3 | -0.7 | 0.6369 | 0.6382 |
| Time 54-69, pooled (%) | 454 | OR 0.869 [0.699, 1.081] | -0.7721 | -1.26 | 0.206 | not applied (n < 1000) | 0.727 | +0.4 | -1.6 | 0.6420 | 0.6382 |
| Avg. daily time 54-69 (%) | 454 | OR 0.821 [0.656, 1.027] | -1.101 | -1.72 | 0.085 | not applied (n < 1000) | 0.704 | -1.1 | -3.1 | 0.6430 | 0.6382 |
| Time < 70, pooled (%) | 454 | OR 0.876 [0.706, 1.088] | -0.6457 | -1.20 | 0.232 | not applied (n < 1000) | 0.727 | +0.5 | -1.4 | 0.6421 | 0.6382 |
| Avg. daily time < 70 (%) | 454 | OR 0.821 [0.656, 1.026] | -1.008 | -1.73 | 0.083 | not applied (n < 1000) | 0.704 | -1.2 | -3.1 | 0.6428 | 0.6382 |
| Time 54-250, pooled (%) | 454 | OR 1.009 [0.814, 1.251] | 0.1651 | 0.08 | 0.934 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.6353 | 0.6382 |
| Avg. daily time 54-250 (%) | 454 | OR 1.060 [0.845, 1.330] | 1.415 | 0.50 | 0.616 | not applied (n < 1000) | 0.929 | +1.7 | -0.2 | 0.6355 | 0.6382 |
| Time 181-250, pooled (%) | 454 | OR 1.148 [0.931, 1.415] | 0.4937 | 1.29 | 0.197 | not applied (n < 1000) | 0.727 | +0.3 | -1.6 | 0.6339 | 0.6382 |
| Avg. daily time 181-250 (%) | 454 | OR 1.091 [0.887, 1.342] | 0.3105 | 0.82 | 0.411 | not applied (n < 1000) | 0.844 | +1.3 | -0.7 | 0.6290 | 0.6382 |
| Time > 180, pooled (%) | 454 | OR 1.153 [0.935, 1.422] | 0.5079 | 1.33 | 0.184 | not applied (n < 1000) | 0.727 | +0.2 | -1.7 | 0.6342 | 0.6382 |
| Avg. daily time > 180 (%) | 454 | OR 1.096 [0.890, 1.349] | 0.3257 | 0.86 | 0.388 | not applied (n < 1000) | 0.843 | +1.3 | -0.7 | 0.6286 | 0.6382 |
| Nocturnal time > 180 (%) | 454 | OR 1.135 [0.929, 1.386] | 0.354 | 1.24 | 0.215 | not applied (n < 1000) | 0.727 | +0.5 | -1.5 | 0.6372 | 0.6382 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### MoCA memory index score (0-15)
*n = 454; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 454 | +0.012 [-0.267, +0.291] | 0.03865 | 0.09 | 0.932 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0223 | 0.0287 |
| Mean glucose (mg/dL) | 454 | -0.108 [-0.357, +0.141] | -0.01437 | -0.85 | 0.396 | not applied (n < 1000) | 0.843 | +1.2 | -0.8 | 0.0273 | 0.0287 |
| GMI (%) | 454 | -0.108 [-0.357, +0.141] | -0.6009 | -0.85 | 0.396 | not applied (n < 1000) | 0.843 | +1.2 | -0.8 | 0.0273 | 0.0287 |
| Nocturnal mean 00-06h (mg/dL) | 454 | -0.105 [-0.356, +0.145] | -0.01082 | -0.82 | 0.410 | not applied (n < 1000) | 0.844 | +1.3 | -0.7 | 0.0272 | 0.0287 |
| Glucose SD, pooled (mg/dL) | 454 | +0.005 [-0.217, +0.227] | 0.002016 | 0.04 | 0.966 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0240 | 0.0287 |
| Avg. daily SD (mg/dL) | 454 | +0.094 [-0.128, +0.315] | 0.03905 | 0.83 | 0.408 | not applied (n < 1000) | 0.844 | +1.4 | -0.6 | 0.0239 | 0.0287 |
| CV (%) | 454 | +0.043 [-0.189, +0.274] | 0.01989 | 0.36 | 0.717 | not applied (n < 1000) | 0.950 | +1.9 | -0.1 | 0.0259 | 0.0287 |
| Mean / SD ratio | 454 | -0.039 [-0.267, +0.189] | -0.0367 | -0.33 | 0.739 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.0260 | 0.0287 |
| Avg. daily mean / SD | 454 | -0.088 [-0.319, +0.142] | -0.06461 | -0.75 | 0.454 | not applied (n < 1000) | 0.845 | +1.5 | -0.5 | 0.0268 | 0.0287 |
| MAG (mg/dL/h) | 454 | -0.068 [-0.319, +0.183] | -0.01167 | -0.53 | 0.594 | not applied (n < 1000) | 0.920 | +1.7 | -0.3 | 0.0239 | 0.0287 |
| Avg. daily range (mg/dL) | 454 | +0.046 [-0.179, +0.271] | 0.004094 | 0.40 | 0.690 | not applied (n < 1000) | 0.949 | +1.9 | -0.1 | 0.0235 | 0.0287 |
| SD of daily means (mg/dL) | 454 | -0.337 [-0.584, -0.090] | -0.1806 | -2.67 | 0.007** | not applied (n < 1000) | 0.294 | -5.8 | -7.8 | 0.0367 | 0.0287 |
| Time in range 70-180, pooled (%) | 454 | -0.030 [-0.267, +0.208] | -0.0985 | -0.24 | 0.807 | not applied (n < 1000) | 0.971 | +1.9 | -0.1 | 0.0206 | 0.0287 |
| Avg. daily time in range 70-180 (%) | 454 | -0.098 [-0.324, +0.128] | -0.316 | -0.85 | 0.397 | not applied (n < 1000) | 0.843 | +1.3 | -0.7 | 0.0226 | 0.0287 |
| Any reading < 54 during wear (0/1) | 454 | +0.012 [-0.264, +0.288] | 0.03296 | 0.09 | 0.930 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.0255 | 0.0287 |
| Time < 54, pooled (%) | 454 | +0.016 [-0.215, +0.248] | 0.3076 | 0.14 | 0.889 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.0255 | 0.0287 |
| Avg. daily time < 54 (%) | 454 | +0.093 [-0.139, +0.324] | 2.303 | 0.78 | 0.433 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.0245 | 0.0287 |
| Time 54-69, pooled (%) | 454 | -0.069 [-0.335, +0.196] | -0.3818 | -0.51 | 0.609 | not applied (n < 1000) | 0.925 | +1.7 | -0.3 | 0.0262 | 0.0287 |
| Avg. daily time 54-69 (%) | 454 | +0.027 [-0.218, +0.272] | 0.1514 | 0.22 | 0.828 | not applied (n < 1000) | 0.981 | +2.0 | -0.0 | 0.0234 | 0.0287 |
| Time < 70, pooled (%) | 454 | -0.058 [-0.319, +0.204] | -0.2815 | -0.43 | 0.667 | not applied (n < 1000) | 0.949 | +1.8 | -0.2 | 0.0264 | 0.0287 |
| Avg. daily time < 70 (%) | 454 | +0.044 [-0.203, +0.291] | 0.2234 | 0.35 | 0.729 | not applied (n < 1000) | 0.952 | +1.9 | -0.1 | 0.0237 | 0.0287 |
| Time 54-250, pooled (%) | 454 | +0.043 [-0.262, +0.349] | 0.7933 | 0.28 | 0.780 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.0234 | 0.0287 |
| Avg. daily time 54-250 (%) | 454 | -0.007 [-0.267, +0.253] | -0.1717 | -0.05 | 0.958 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0194 | 0.0287 |
| Time 181-250, pooled (%) | 454 | +0.085 [-0.146, +0.316] | 0.3045 | 0.72 | 0.470 | not applied (n < 1000) | 0.845 | +1.5 | -0.5 | 0.0210 | 0.0287 |
| Avg. daily time 181-250 (%) | 454 | +0.090 [-0.142, +0.323] | 0.3221 | 0.76 | 0.447 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.0196 | 0.0287 |
| Time > 180, pooled (%) | 454 | +0.074 [-0.160, +0.308] | 0.2634 | 0.62 | 0.537 | not applied (n < 1000) | 0.888 | +1.6 | -0.4 | 0.0205 | 0.0287 |
| Avg. daily time > 180 (%) | 454 | +0.078 [-0.160, +0.315] | 0.2773 | 0.64 | 0.521 | not applied (n < 1000) | 0.885 | +1.6 | -0.4 | 0.0190 | 0.0287 |
| Nocturnal time > 180 (%) | 454 | +0.037 [-0.184, +0.257] | 0.1021 | 0.32 | 0.746 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.0221 | 0.0287 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### CES-D-10 depressive symptoms (0-30)
*n = 454; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 454 | -0.004 [-0.472, +0.465] | -0.01204 | -0.02 | 0.987 | not applied (n < 1000) | 0.990 | +2.0 | +0.0 | -0.0039 | -0.0008 |
| Mean glucose (mg/dL) | 454 | -0.031 [-0.448, +0.386] | -0.004143 | -0.15 | 0.884 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | -0.0059 | -0.0008 |
| GMI (%) | 454 | -0.031 [-0.448, +0.386] | -0.1732 | -0.15 | 0.884 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | -0.0059 | -0.0008 |
| Nocturnal mean 00-06h (mg/dL) | 454 | -0.038 [-0.467, +0.392] | -0.003862 | -0.17 | 0.864 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | -0.0066 | -0.0008 |
| Glucose SD, pooled (mg/dL) | 454 | +0.287 [-0.163, +0.737] | 0.1205 | 1.25 | 0.212 | not applied (n < 1000) | 0.727 | +0.3 | -1.7 | -0.0021 | -0.0008 |
| Avg. daily SD (mg/dL) | 454 | +0.255 [-0.210, +0.719] | 0.1063 | 1.07 | 0.282 | not applied (n < 1000) | 0.772 | +0.6 | -1.4 | -0.0033 | -0.0008 |
| CV (%) | 454 | +0.286 [-0.144, +0.716] | 0.1331 | 1.30 | 0.192 | not applied (n < 1000) | 0.727 | +0.2 | -1.8 | -0.0055 | -0.0008 |
| Mean / SD ratio | 454 | -0.301 [-0.713, +0.111] | -0.2848 | -1.43 | 0.152 | not applied (n < 1000) | 0.727 | +0.0 | -2.0 | -0.0053 | -0.0008 |
| Avg. daily mean / SD | 454 | -0.247 [-0.691, +0.198] | -0.1807 | -1.09 | 0.278 | not applied (n < 1000) | 0.772 | +0.7 | -1.3 | -0.0083 | -0.0008 |
| MAG (mg/dL/h) | 454 | +0.622 [+0.184, +1.061] | 0.1064 | 2.78 | 0.005** | not applied (n < 1000) | 0.294 | -6.4 | -8.4 | 0.0145 | -0.0008 |
| Avg. daily range (mg/dL) | 454 | +0.344 [-0.088, +0.775] | 0.03067 | 1.56 | 0.119 | not applied (n < 1000) | 0.727 | -0.6 | -2.6 | -0.0026 | -0.0008 |
| SD of daily means (mg/dL) | 454 | +0.215 [-0.255, +0.685] | 0.1153 | 0.90 | 0.369 | not applied (n < 1000) | 0.843 | +1.0 | -1.0 | -0.0036 | -0.0008 |
| Time in range 70-180, pooled (%) | 454 | -0.089 [-0.475, +0.297] | -0.2972 | -0.45 | 0.651 | not applied (n < 1000) | 0.949 | +1.8 | -0.2 | -0.0086 | -0.0008 |
| Avg. daily time in range 70-180 (%) | 454 | -0.146 [-0.554, +0.263] | -0.471 | -0.70 | 0.485 | not applied (n < 1000) | 0.845 | +1.5 | -0.5 | -0.0078 | -0.0008 |
| Any reading < 54 during wear (0/1) | 454 | -0.356 [-0.768, +0.057] | -0.9512 | -1.69 | 0.091 | not applied (n < 1000) | 0.704 | -0.7 | -2.7 | 0.0006 | -0.0008 |
| Time < 54, pooled (%) | 454 | -0.405 [-0.774, -0.037] | -7.573 | -2.15 | 0.031* | not applied (n < 1000) | 0.612 | -1.4 | -3.4 | 0.0023 | -0.0008 |
| Avg. daily time < 54 (%) | 454 | -0.285 [-0.724, +0.154] | -7.103 | -1.27 | 0.203 | not applied (n < 1000) | 0.727 | +0.2 | -1.8 | -0.0052 | -0.0008 |
| Time 54-69, pooled (%) | 454 | +0.169 [-0.261, +0.598] | 0.926 | 0.77 | 0.442 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | -0.0024 | -0.0008 |
| Avg. daily time 54-69 (%) | 454 | +0.139 [-0.302, +0.581] | 0.7791 | 0.62 | 0.536 | not applied (n < 1000) | 0.888 | +1.6 | -0.4 | -0.0049 | -0.0008 |
| Time < 70, pooled (%) | 454 | +0.047 [-0.376, +0.470] | 0.2302 | 0.22 | 0.827 | not applied (n < 1000) | 0.981 | +2.0 | -0.0 | -0.0034 | -0.0008 |
| Avg. daily time < 70 (%) | 454 | +0.068 [-0.371, +0.506] | 0.3454 | 0.30 | 0.762 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | -0.0059 | -0.0008 |
| Time 54-250, pooled (%) | 454 | +0.402 [+0.038, +0.766] | 7.338 | 2.17 | 0.030* | not applied (n < 1000) | 0.612 | -1.4 | -3.4 | 0.0024 | -0.0008 |
| Avg. daily time 54-250 (%) | 454 | +0.288 [-0.139, +0.716] | 7.023 | 1.32 | 0.186 | not applied (n < 1000) | 0.727 | +0.2 | -1.8 | -0.0043 | -0.0008 |
| Time 181-250, pooled (%) | 454 | +0.063 [-0.339, +0.466] | 0.2273 | 0.31 | 0.757 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | -0.0068 | -0.0008 |
| Avg. daily time 181-250 (%) | 454 | +0.116 [-0.296, +0.528] | 0.4139 | 0.55 | 0.582 | not applied (n < 1000) | 0.919 | +1.7 | -0.3 | -0.0060 | -0.0008 |
| Time > 180, pooled (%) | 454 | +0.062 [-0.340, +0.464] | 0.2223 | 0.30 | 0.762 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | -0.0068 | -0.0008 |
| Avg. daily time > 180 (%) | 454 | +0.114 [-0.297, +0.526] | 0.4073 | 0.54 | 0.586 | not applied (n < 1000) | 0.920 | +1.7 | -0.3 | -0.0059 | -0.0008 |
| Nocturnal time > 180 (%) | 454 | +0.661 [+0.107, +1.215] | 1.849 | 2.34 | 0.019* | not applied (n < 1000) | 0.479 | -7.2 | -9.2 | 0.0169 | -0.0008 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 454; events = 82; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 454 | OR 1.046 [0.814, 1.345] | 0.1437 | 0.35 | 0.725 | not applied (n < 1000) | 0.950 | +1.9 | +0.0 | 0.5983 | 0.6071 |
| Mean glucose (mg/dL) | 454 | OR 1.031 [0.806, 1.319] | 0.004088 | 0.24 | 0.807 | not applied (n < 1000) | 0.971 | +1.9 | +0.1 | 0.6025 | 0.6071 |
| GMI (%) | 454 | OR 1.031 [0.806, 1.319] | 0.1709 | 0.24 | 0.807 | not applied (n < 1000) | 0.971 | +1.9 | +0.1 | 0.6025 | 0.6071 |
| Nocturnal mean 00-06h (mg/dL) | 454 | OR 1.055 [0.821, 1.356] | 0.005528 | 0.42 | 0.674 | not applied (n < 1000) | 0.949 | +1.8 | -0.1 | 0.6079 | 0.6071 |
| Glucose SD, pooled (mg/dL) | 454 | OR 1.212 [0.937, 1.568] | 0.08082 | 1.46 | 0.144 | not applied (n < 1000) | 0.727 | -0.2 | -2.0 | 0.6077 | 0.6071 |
| Avg. daily SD (mg/dL) | 454 | OR 1.227 [0.947, 1.591] | 0.08549 | 1.55 | 0.122 | not applied (n < 1000) | 0.727 | -0.4 | -2.3 | 0.6093 | 0.6071 |
| CV (%) | 454 | OR 1.189 [0.922, 1.534] | 0.08062 | 1.34 | 0.182 | not applied (n < 1000) | 0.727 | +0.2 | -1.7 | 0.6040 | 0.6071 |
| Mean / SD ratio | 454 | OR 0.844 [0.648, 1.101] | -0.1601 | -1.25 | 0.211 | not applied (n < 1000) | 0.727 | +0.4 | -1.5 | 0.6044 | 0.6071 |
| Avg. daily mean / SD | 454 | OR 0.845 [0.645, 1.107] | -0.1235 | -1.22 | 0.222 | not applied (n < 1000) | 0.727 | +0.4 | -1.4 | 0.6087 | 0.6071 |
| MAG (mg/dL/h) | 454 | OR 1.531 [1.187, 1.974] | 0.07283 | 3.28 | 0.001** | not applied (n < 1000) | 0.240 | -9.0 | -10.9 | 0.6436 | 0.6071 |
| Avg. daily range (mg/dL) | 454 | OR 1.289 [0.992, 1.675] | 0.02266 | 1.90 | 0.057 | not applied (n < 1000) | 0.692 | -1.7 | -3.6 | 0.6153 | 0.6071 |
| SD of daily means (mg/dL) | 454 | OR 1.132 [0.889, 1.443] | 0.06661 | 1.01 | 0.315 | not applied (n < 1000) | 0.806 | +1.0 | -0.9 | 0.6100 | 0.6071 |
| Time in range 70-180, pooled (%) | 454 | OR 1.048 [0.815, 1.348] | 0.1568 | 0.37 | 0.714 | not applied (n < 1000) | 0.950 | +1.9 | -0.0 | 0.5989 | 0.6071 |
| Avg. daily time in range 70-180 (%) | 454 | OR 0.942 [0.736, 1.206] | -0.1916 | -0.47 | 0.638 | not applied (n < 1000) | 0.939 | +1.8 | -0.1 | 0.6046 | 0.6071 |
| Any reading < 54 during wear (0/1) | 454 | OR 0.862 [0.657, 1.131] | -0.3968 | -1.07 | 0.283 | not applied (n < 1000) | 0.772 | +0.8 | -1.1 | 0.6129 | 0.6071 |
| Time < 54, pooled (%) | 454 | OR 0.822 [0.609, 1.108] | -3.672 | -1.29 | 0.197 | not applied (n < 1000) | 0.727 | -0.0 | -1.9 | 0.6133 | 0.6071 |
| Avg. daily time < 54 (%) | 454 | OR 0.936 [0.720, 1.217] | -1.643 | -0.49 | 0.622 | not applied (n < 1000) | 0.935 | +1.7 | -0.1 | 0.6056 | 0.6071 |
| Time 54-69, pooled (%) | 454 | OR 1.162 [0.917, 1.473] | 0.8272 | 1.25 | 0.213 | not applied (n < 1000) | 0.727 | +0.5 | -1.4 | 0.6101 | 0.6071 |
| Avg. daily time 54-69 (%) | 454 | OR 1.142 [0.900, 1.449] | 0.7435 | 1.10 | 0.273 | not applied (n < 1000) | 0.766 | +0.8 | -1.0 | 0.6072 | 0.6071 |
| Time < 70, pooled (%) | 454 | OR 1.091 [0.861, 1.383] | 0.426 | 0.72 | 0.472 | not applied (n < 1000) | 0.845 | +1.5 | -0.4 | 0.6040 | 0.6071 |
| Avg. daily time < 70 (%) | 454 | OR 1.112 [0.877, 1.410] | 0.5432 | 0.88 | 0.380 | not applied (n < 1000) | 0.843 | +1.3 | -0.6 | 0.6064 | 0.6071 |
| Time 54-250, pooled (%) | 454 | OR 1.239 [0.912, 1.685] | 3.915 | 1.37 | 0.171 | not applied (n < 1000) | 0.727 | -0.3 | -2.2 | 0.6152 | 0.6071 |
| Avg. daily time 54-250 (%) | 454 | OR 1.094 [0.830, 1.440] | 2.181 | 0.64 | 0.524 | not applied (n < 1000) | 0.885 | +1.5 | -0.3 | 0.6055 | 0.6071 |
| Time 181-250, pooled (%) | 454 | OR 0.887 [0.686, 1.148] | -0.4291 | -0.91 | 0.362 | not applied (n < 1000) | 0.843 | +1.2 | -0.7 | 0.6056 | 0.6071 |
| Avg. daily time 181-250 (%) | 454 | OR 0.991 [0.772, 1.273] | -0.03062 | -0.07 | 0.946 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.6008 | 0.6071 |
| Time > 180, pooled (%) | 454 | OR 0.885 [0.684, 1.144] | -0.4384 | -0.93 | 0.351 | not applied (n < 1000) | 0.843 | +1.1 | -0.8 | 0.6060 | 0.6071 |
| Avg. daily time > 180 (%) | 454 | OR 0.988 [0.770, 1.269] | -0.04185 | -0.09 | 0.927 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.6008 | 0.6071 |
| Nocturnal time > 180 (%) | 454 | OR 1.190 [0.966, 1.465] | 0.4865 | 1.64 | 0.101 | not applied (n < 1000) | 0.709 | -0.6 | -2.5 | 0.6095 | 0.6071 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 443; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 443 | +0.045 [-0.056, +0.145] | 0.1418 | 0.87 | 0.386 | not applied (n < 1000) | 0.843 | +0.9 | +0.0 | 0.0722 | 0.0753 |
| Mean glucose (mg/dL) | 443 | -0.058 [-0.136, +0.021] | -0.00775 | -1.45 | 0.148 | not applied (n < 1000) | 0.727 | -0.1 | -1.0 | 0.0745 | 0.0753 |
| GMI (%) | 443 | -0.058 [-0.136, +0.021] | -0.324 | -1.45 | 0.148 | not applied (n < 1000) | 0.727 | -0.1 | -1.0 | 0.0745 | 0.0753 |
| Nocturnal mean 00-06h (mg/dL) | 443 | -0.037 [-0.117, +0.042] | -0.003855 | -0.92 | 0.357 | not applied (n < 1000) | 0.843 | +1.2 | +0.2 | 0.0729 | 0.0753 |
| Glucose SD, pooled (mg/dL) | 443 | -0.012 [-0.092, +0.067] | -0.005264 | -0.31 | 0.759 | not applied (n < 1000) | 0.958 | +1.9 | +1.0 | 0.0692 | 0.0753 |
| Avg. daily SD (mg/dL) | 443 | -0.008 [-0.086, +0.070] | -0.003406 | -0.21 | 0.837 | not applied (n < 1000) | 0.986 | +2.0 | +1.0 | 0.0693 | 0.0753 |
| CV (%) | 443 | +0.015 [-0.066, +0.095] | 0.006779 | 0.36 | 0.722 | not applied (n < 1000) | 0.950 | +1.9 | +0.9 | 0.0705 | 0.0753 |
| Mean / SD ratio | 443 | -0.007 [-0.085, +0.071] | -0.006585 | -0.17 | 0.862 | not applied (n < 1000) | 0.986 | +2.0 | +1.0 | 0.0706 | 0.0753 |
| Avg. daily mean / SD | 443 | -0.021 [-0.099, +0.057] | -0.01545 | -0.53 | 0.596 | not applied (n < 1000) | 0.920 | +1.7 | +0.8 | 0.0712 | 0.0753 |
| MAG (mg/dL/h) | 443 | +0.051 [-0.026, +0.127] | 0.008655 | 1.30 | 0.193 | not applied (n < 1000) | 0.727 | +0.4 | -0.5 | 0.0718 | 0.0753 |
| Avg. daily range (mg/dL) | 443 | -0.016 [-0.095, +0.063] | -0.001398 | -0.39 | 0.698 | not applied (n < 1000) | 0.949 | +1.8 | +0.9 | 0.0676 | 0.0753 |
| SD of daily means (mg/dL) | 443 | +0.029 [-0.052, +0.109] | 0.01542 | 0.70 | 0.483 | not applied (n < 1000) | 0.845 | +1.5 | +0.6 | 0.0706 | 0.0753 |
| Time in range 70-180, pooled (%) | 443 | -0.003 [-0.088, +0.081] | -0.01103 | -0.08 | 0.939 | not applied (n < 1000) | 0.986 | +2.0 | +1.1 | 0.0701 | 0.0753 |
| Avg. daily time in range 70-180 (%) | 443 | -0.003 [-0.088, +0.082] | -0.008896 | -0.06 | 0.949 | not applied (n < 1000) | 0.986 | +2.0 | +1.1 | 0.0659 | 0.0753 |
| Any reading < 54 during wear (0/1) | 443 | +0.039 [-0.057, +0.135] | 0.1051 | 0.80 | 0.423 | not applied (n < 1000) | 0.845 | +1.1 | +0.2 | 0.0689 | 0.0753 |
| Time < 54, pooled (%) | 443 | +0.072 [-0.024, +0.168] | 1.344 | 1.48 | 0.140 | not applied (n < 1000) | 0.727 | -1.1 | -2.0 | 0.0781 | 0.0753 |
| Avg. daily time < 54 (%) | 443 | +0.091 [-0.016, +0.198] | 2.304 | 1.67 | 0.094 | not applied (n < 1000) | 0.704 | -3.2 | -4.1 | 0.0724 | 0.0753 |
| Time 54-69, pooled (%) | 443 | +0.075 [-0.012, +0.163] | 0.4151 | 1.68 | 0.092 | not applied (n < 1000) | 0.704 | -1.5 | -2.4 | 0.0740 | 0.0753 |
| Avg. daily time 54-69 (%) | 443 | +0.072 [-0.018, +0.162] | 0.401 | 1.57 | 0.117 | not applied (n < 1000) | 0.727 | -1.1 | -2.1 | 0.0738 | 0.0753 |
| Time < 70, pooled (%) | 443 | +0.085 [-0.006, +0.176] | 0.4188 | 1.84 | 0.066 | not applied (n < 1000) | 0.692 | -2.5 | -3.4 | 0.0771 | 0.0753 |
| Avg. daily time < 70 (%) | 443 | +0.084 [-0.010, +0.178] | 0.4306 | 1.76 | 0.079 | not applied (n < 1000) | 0.704 | -2.3 | -3.3 | 0.0756 | 0.0753 |
| Time 54-250, pooled (%) | 443 | -0.064 [-0.161, +0.032] | -1.168 | -1.30 | 0.192 | not applied (n < 1000) | 0.727 | -0.4 | -1.4 | 0.0768 | 0.0753 |
| Avg. daily time 54-250 (%) | 443 | -0.081 [-0.183, +0.022] | -1.986 | -1.54 | 0.123 | not applied (n < 1000) | 0.727 | -2.0 | -2.9 | 0.0720 | 0.0753 |
| Time 181-250, pooled (%) | 443 | -0.057 [-0.137, +0.023] | -0.2043 | -1.39 | 0.165 | not applied (n < 1000) | 0.727 | -0.0 | -0.9 | 0.0729 | 0.0753 |
| Avg. daily time 181-250 (%) | 443 | -0.053 [-0.132, +0.025] | -0.1892 | -1.33 | 0.185 | not applied (n < 1000) | 0.727 | +0.2 | -0.7 | 0.0695 | 0.0753 |
| Time > 180, pooled (%) | 443 | -0.058 [-0.138, +0.022] | -0.2078 | -1.42 | 0.157 | not applied (n < 1000) | 0.727 | -0.1 | -1.0 | 0.0730 | 0.0753 |
| Avg. daily time > 180 (%) | 443 | -0.054 [-0.133, +0.024] | -0.1928 | -1.36 | 0.175 | not applied (n < 1000) | 0.727 | +0.2 | -0.8 | 0.0697 | 0.0753 |
| Nocturnal time > 180 (%) | 443 | -0.081 [-0.171, +0.008] | -0.2262 | -1.78 | 0.076 | not applied (n < 1000) | 0.704 | -1.9 | -2.8 | 0.0793 | 0.0753 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor temperature, mean (deg C)
*n = 443; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 443 | -0.070 [-0.281, +0.142] | -0.2211 | -0.64 | 0.520 | not applied (n < 1000) | 0.885 | +1.5 | +0.0 | 0.2879 | 0.2919 |
| Mean glucose (mg/dL) | 443 | -0.002 [-0.186, +0.181] | -0.0002999 | -0.02 | 0.981 | not applied (n < 1000) | 0.986 | +2.0 | +0.5 | 0.2869 | 0.2919 |
| GMI (%) | 443 | -0.002 [-0.186, +0.181] | -0.01254 | -0.02 | 0.981 | not applied (n < 1000) | 0.986 | +2.0 | +0.5 | 0.2869 | 0.2919 |
| Nocturnal mean 00-06h (mg/dL) | 443 | -0.098 [-0.284, +0.088] | -0.01015 | -1.03 | 0.301 | not applied (n < 1000) | 0.787 | +0.9 | -0.6 | 0.2884 | 0.2919 |
| Glucose SD, pooled (mg/dL) | 443 | -0.148 [-0.337, +0.042] | -0.06233 | -1.53 | 0.126 | not applied (n < 1000) | 0.727 | -0.7 | -2.2 | 0.2914 | 0.2919 |
| Avg. daily SD (mg/dL) | 443 | -0.185 [-0.382, +0.013] | -0.07702 | -1.83 | 0.067 | not applied (n < 1000) | 0.692 | -2.2 | -3.7 | 0.2912 | 0.2919 |
| CV (%) | 443 | -0.149 [-0.339, +0.040] | -0.06935 | -1.55 | 0.122 | not applied (n < 1000) | 0.727 | -0.8 | -2.2 | 0.2918 | 0.2919 |
| Mean / SD ratio | 443 | +0.134 [-0.061, +0.328] | 0.1265 | 1.35 | 0.178 | not applied (n < 1000) | 0.727 | -0.2 | -1.7 | 0.2910 | 0.2919 |
| Avg. daily mean / SD | 443 | +0.163 [-0.050, +0.376] | 0.1191 | 1.50 | 0.134 | not applied (n < 1000) | 0.727 | -1.3 | -2.8 | 0.2905 | 0.2919 |
| MAG (mg/dL/h) | 443 | -0.095 [-0.282, +0.093] | -0.0162 | -0.99 | 0.322 | not applied (n < 1000) | 0.810 | +0.9 | -0.6 | 0.2914 | 0.2919 |
| Avg. daily range (mg/dL) | 443 | -0.239 [-0.425, -0.052] | -0.02127 | -2.50 | 0.012* | not applied (n < 1000) | 0.400 | -5.2 | -6.7 | 0.2995 | 0.2919 |
| SD of daily means (mg/dL) | 443 | +0.098 [-0.070, +0.267] | 0.05255 | 1.14 | 0.253 | not applied (n < 1000) | 0.727 | +0.8 | -0.7 | 0.2916 | 0.2919 |
| Time in range 70-180, pooled (%) | 443 | +0.123 [-0.054, +0.301] | 0.4131 | 1.36 | 0.173 | not applied (n < 1000) | 0.727 | +0.1 | -1.4 | 0.2950 | 0.2919 |
| Avg. daily time in range 70-180 (%) | 443 | +0.097 [-0.084, +0.279] | 0.3145 | 1.05 | 0.294 | not applied (n < 1000) | 0.786 | +0.8 | -0.7 | 0.2909 | 0.2919 |
| Any reading < 54 during wear (0/1) | 443 | -0.043 [-0.236, +0.151] | -0.1142 | -0.43 | 0.666 | not applied (n < 1000) | 0.949 | +1.8 | +0.3 | 0.2892 | 0.2919 |
| Time < 54, pooled (%) | 443 | -0.027 [-0.292, +0.238] | -0.5017 | -0.20 | 0.842 | not applied (n < 1000) | 0.986 | +1.9 | +0.4 | 0.2846 | 0.2919 |
| Avg. daily time < 54 (%) | 443 | -0.008 [-0.226, +0.211] | -0.1901 | -0.07 | 0.946 | not applied (n < 1000) | 0.986 | +2.0 | +0.5 | 0.2890 | 0.2919 |
| Time 54-69, pooled (%) | 443 | -0.157 [-0.333, +0.019] | -0.8674 | -1.75 | 0.080 | not applied (n < 1000) | 0.704 | -1.1 | -2.6 | 0.2936 | 0.2919 |
| Avg. daily time 54-69 (%) | 443 | -0.114 [-0.282, +0.054] | -0.6371 | -1.33 | 0.184 | not applied (n < 1000) | 0.727 | +0.4 | -1.1 | 0.2901 | 0.2919 |
| Time < 70, pooled (%) | 443 | -0.147 [-0.332, +0.038] | -0.7209 | -1.56 | 0.120 | not applied (n < 1000) | 0.727 | -0.7 | -2.2 | 0.2932 | 0.2919 |
| Avg. daily time < 70 (%) | 443 | -0.106 [-0.274, +0.063] | -0.5401 | -1.23 | 0.218 | not applied (n < 1000) | 0.727 | +0.6 | -0.9 | 0.2899 | 0.2919 |
| Time 54-250, pooled (%) | 443 | +0.033 [-0.225, +0.291] | 0.5977 | 0.25 | 0.803 | not applied (n < 1000) | 0.971 | +1.9 | +0.4 | 0.2851 | 0.2919 |
| Avg. daily time 54-250 (%) | 443 | +0.017 [-0.201, +0.235] | 0.4127 | 0.15 | 0.880 | not applied (n < 1000) | 0.986 | +2.0 | +0.5 | 0.2891 | 0.2919 |
| Time 181-250, pooled (%) | 443 | -0.025 [-0.205, +0.154] | -0.0906 | -0.28 | 0.782 | not applied (n < 1000) | 0.958 | +1.9 | +0.4 | 0.2903 | 0.2919 |
| Avg. daily time 181-250 (%) | 443 | -0.034 [-0.214, +0.146] | -0.1193 | -0.37 | 0.715 | not applied (n < 1000) | 0.950 | +1.9 | +0.4 | 0.2893 | 0.2919 |
| Time > 180, pooled (%) | 443 | -0.026 [-0.205, +0.153] | -0.0947 | -0.29 | 0.772 | not applied (n < 1000) | 0.958 | +1.9 | +0.4 | 0.2904 | 0.2919 |
| Avg. daily time > 180 (%) | 443 | -0.035 [-0.214, +0.145] | -0.1234 | -0.38 | 0.704 | not applied (n < 1000) | 0.950 | +1.8 | +0.4 | 0.2893 | 0.2919 |
| Nocturnal time > 180 (%) | 443 | +0.060 [-0.089, +0.209] | 0.1683 | 0.79 | 0.428 | not applied (n < 1000) | 0.845 | +1.6 | +0.1 | 0.2908 | 0.2919 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor relative humidity, mean (%)
*n = 443; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 443 | +0.340 [-0.247, +0.928] | 1.083 | 1.14 | 0.256 | not applied (n < 1000) | 0.727 | +0.6 | +0.0 | 0.2185 | 0.2200 |
| Mean glucose (mg/dL) | 443 | +0.172 [-0.367, +0.711] | 0.02302 | 0.63 | 0.531 | not applied (n < 1000) | 0.886 | +1.6 | +1.0 | 0.2170 | 0.2200 |
| GMI (%) | 443 | +0.172 [-0.367, +0.711] | 0.9623 | 0.63 | 0.531 | not applied (n < 1000) | 0.886 | +1.6 | +1.0 | 0.2170 | 0.2200 |
| Nocturnal mean 00-06h (mg/dL) | 443 | +0.404 [-0.134, +0.942] | 0.04179 | 1.47 | 0.141 | not applied (n < 1000) | 0.727 | -0.1 | -0.7 | 0.2175 | 0.2200 |
| Glucose SD, pooled (mg/dL) | 443 | -0.194 [-0.765, +0.376] | -0.08193 | -0.67 | 0.505 | not applied (n < 1000) | 0.871 | +1.5 | +0.9 | 0.2186 | 0.2200 |
| Avg. daily SD (mg/dL) | 443 | -0.067 [-0.650, +0.515] | -0.02807 | -0.23 | 0.821 | not applied (n < 1000) | 0.981 | +1.9 | +1.3 | 0.2166 | 0.2200 |
| CV (%) | 443 | -0.238 [-0.818, +0.343] | -0.1104 | -0.80 | 0.422 | not applied (n < 1000) | 0.845 | +1.3 | +0.6 | 0.2194 | 0.2200 |
| Mean / SD ratio | 443 | +0.266 [-0.304, +0.836] | 0.2518 | 0.91 | 0.360 | not applied (n < 1000) | 0.843 | +1.1 | +0.4 | 0.2197 | 0.2200 |
| Avg. daily mean / SD | 443 | +0.044 [-0.545, +0.633] | 0.03223 | 0.15 | 0.883 | not applied (n < 1000) | 0.986 | +2.0 | +1.3 | 0.2153 | 0.2200 |
| MAG (mg/dL/h) | 443 | +0.109 [-0.452, +0.671] | 0.0187 | 0.38 | 0.703 | not applied (n < 1000) | 0.950 | +1.8 | +1.2 | 0.2176 | 0.2200 |
| Avg. daily range (mg/dL) | 443 | -0.008 [-0.600, +0.584] | -0.0007054 | -0.03 | 0.979 | not applied (n < 1000) | 0.986 | +2.0 | +1.3 | 0.2171 | 0.2200 |
| SD of daily means (mg/dL) | 443 | -0.057 [-0.644, +0.531] | -0.03034 | -0.19 | 0.850 | not applied (n < 1000) | 0.986 | +2.0 | +1.3 | 0.2182 | 0.2200 |
| Time in range 70-180, pooled (%) | 443 | -0.278 [-0.835, +0.279] | -0.9297 | -0.98 | 0.329 | not applied (n < 1000) | 0.815 | +1.0 | +0.3 | 0.2195 | 0.2200 |
| Avg. daily time in range 70-180 (%) | 443 | -0.208 [-0.776, +0.359] | -0.6745 | -0.72 | 0.472 | not applied (n < 1000) | 0.845 | +1.4 | +0.8 | 0.2154 | 0.2200 |
| Any reading < 54 during wear (0/1) | 443 | +0.164 [-0.430, +0.757] | 0.4382 | 0.54 | 0.589 | not applied (n < 1000) | 0.920 | +1.7 | +1.0 | 0.2186 | 0.2200 |
| Time < 54, pooled (%) | 443 | +0.398 [-0.404, +1.200] | 7.419 | 0.97 | 0.331 | not applied (n < 1000) | 0.816 | -0.0 | -0.7 | 0.2207 | 0.2200 |
| Avg. daily time < 54 (%) | 443 | +0.095 [-0.558, +0.749] | 2.4 | 0.29 | 0.775 | not applied (n < 1000) | 0.958 | +1.9 | +1.2 | 0.2171 | 0.2200 |
| Time 54-69, pooled (%) | 443 | +0.225 [-0.357, +0.808] | 1.243 | 0.76 | 0.448 | not applied (n < 1000) | 0.845 | +1.3 | +0.7 | 0.2150 | 0.2200 |
| Avg. daily time 54-69 (%) | 443 | +0.048 [-0.538, +0.634] | 0.2665 | 0.16 | 0.873 | not applied (n < 1000) | 0.986 | +2.0 | +1.3 | 0.2137 | 0.2200 |
| Time < 70, pooled (%) | 443 | +0.302 [-0.313, +0.916] | 1.481 | 0.96 | 0.336 | not applied (n < 1000) | 0.824 | +0.8 | +0.1 | 0.2168 | 0.2200 |
| Avg. daily time < 70 (%) | 443 | +0.063 [-0.523, +0.649] | 0.3222 | 0.21 | 0.833 | not applied (n < 1000) | 0.984 | +1.9 | +1.3 | 0.2138 | 0.2200 |
| Time 54-250, pooled (%) | 443 | -0.429 [-1.209, +0.352] | -7.807 | -1.08 | 0.281 | not applied (n < 1000) | 0.772 | -0.4 | -1.0 | 0.2218 | 0.2200 |
| Avg. daily time 54-250 (%) | 443 | -0.151 [-0.818, +0.516] | -3.721 | -0.44 | 0.657 | not applied (n < 1000) | 0.949 | +1.7 | +1.0 | 0.2171 | 0.2200 |
| Time 181-250, pooled (%) | 443 | +0.073 [-0.487, +0.633] | 0.2617 | 0.26 | 0.798 | not applied (n < 1000) | 0.971 | +1.9 | +1.3 | 0.2172 | 0.2200 |
| Avg. daily time 181-250 (%) | 443 | +0.178 [-0.401, +0.758] | 0.6336 | 0.60 | 0.547 | not applied (n < 1000) | 0.891 | +1.6 | +0.9 | 0.2177 | 0.2200 |
| Time > 180, pooled (%) | 443 | +0.080 [-0.479, +0.640] | 0.288 | 0.28 | 0.778 | not applied (n < 1000) | 0.958 | +1.9 | +1.3 | 0.2173 | 0.2200 |
| Avg. daily time > 180 (%) | 443 | +0.186 [-0.393, +0.765] | 0.6597 | 0.63 | 0.529 | not applied (n < 1000) | 0.886 | +1.5 | +0.9 | 0.2178 | 0.2200 |
| Nocturnal time > 180 (%) | 443 | -0.390 [-0.980, +0.199] | -1.089 | -1.30 | 0.194 | not applied (n < 1000) | 0.727 | +0.0 | -0.6 | 0.2227 | 0.2200 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor VOC index, mean
*n = 443; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 443 | -0.778 [-2.327, +0.771] | -2.476 | -0.98 | 0.325 | not applied (n < 1000) | 0.811 | +0.8 | +0.0 | -0.0374 | -0.0368 |
| Mean glucose (mg/dL) | 443 | -1.280 [-2.652, +0.092] | -0.1711 | -1.83 | 0.067 | not applied (n < 1000) | 0.692 | -1.7 | -2.5 | -0.0336 | -0.0368 |
| GMI (%) | 443 | -1.280 [-2.652, +0.092] | -7.151 | -1.83 | 0.067 | not applied (n < 1000) | 0.692 | -1.7 | -2.5 | -0.0336 | -0.0368 |
| Nocturnal mean 00-06h (mg/dL) | 443 | -0.946 [-2.286, +0.394] | -0.0978 | -1.38 | 0.167 | not applied (n < 1000) | 0.727 | +0.1 | -0.7 | -0.0332 | -0.0368 |
| Glucose SD, pooled (mg/dL) | 443 | -0.019 [-1.489, +1.450] | -0.00804 | -0.03 | 0.980 | not applied (n < 1000) | 0.986 | +2.0 | +1.2 | -0.0442 | -0.0368 |
| Avg. daily SD (mg/dL) | 443 | -0.144 [-1.642, +1.353] | -0.0603 | -0.19 | 0.850 | not applied (n < 1000) | 0.986 | +2.0 | +1.1 | -0.0470 | -0.0368 |
| CV (%) | 443 | +0.544 [-0.963, +2.052] | 0.2528 | 0.71 | 0.479 | not applied (n < 1000) | 0.845 | +1.4 | +0.5 | -0.0461 | -0.0368 |
| Mean / SD ratio | 443 | -0.536 [-2.038, +0.965] | -0.5079 | -0.70 | 0.484 | not applied (n < 1000) | 0.845 | +1.4 | +0.5 | -0.0475 | -0.0368 |
| Avg. daily mean / SD | 443 | -0.542 [-2.048, +0.964] | -0.3962 | -0.71 | 0.481 | not applied (n < 1000) | 0.845 | +1.4 | +0.5 | -0.0514 | -0.0368 |
| MAG (mg/dL/h) | 443 | +1.511 [+0.049, +2.974] | 0.2585 | 2.03 | 0.043* | not applied (n < 1000) | 0.645 | -3.0 | -3.9 | -0.0289 | -0.0368 |
| Avg. daily range (mg/dL) | 443 | +0.412 [-1.162, +1.986] | 0.03671 | 0.51 | 0.608 | not applied (n < 1000) | 0.925 | +1.6 | +0.8 | -0.0473 | -0.0368 |
| SD of daily means (mg/dL) | 443 | +0.051 [-1.236, +1.338] | 0.02712 | 0.08 | 0.938 | not applied (n < 1000) | 0.986 | +2.0 | +1.2 | -0.0418 | -0.0368 |
| Time in range 70-180, pooled (%) | 443 | -0.431 [-1.846, +0.985] | -1.441 | -0.60 | 0.551 | not applied (n < 1000) | 0.891 | +1.6 | +0.8 | -0.0423 | -0.0368 |
| Avg. daily time in range 70-180 (%) | 443 | -0.323 [-1.793, +1.146] | -1.046 | -0.43 | 0.666 | not applied (n < 1000) | 0.949 | +1.8 | +0.9 | -0.0470 | -0.0368 |
| Any reading < 54 during wear (0/1) | 443 | -0.018 [-1.394, +1.358] | -0.04791 | -0.03 | 0.980 | not applied (n < 1000) | 0.986 | +2.0 | +1.2 | -0.0418 | -0.0368 |
| Time < 54, pooled (%) | 443 | +0.438 [-0.910, +1.787] | 8.173 | 0.64 | 0.524 | not applied (n < 1000) | 0.885 | +1.6 | +0.8 | -0.0380 | -0.0368 |
| Avg. daily time < 54 (%) | 443 | +1.117 [-0.053, +2.287] | 28.17 | 1.87 | 0.061 | not applied (n < 1000) | 0.692 | -0.8 | -1.6 | -0.0276 | -0.0368 |
| Time 54-69, pooled (%) | 443 | +0.805 [-0.543, +2.153] | 4.437 | 1.17 | 0.242 | not applied (n < 1000) | 0.727 | +0.6 | -0.3 | -0.0402 | -0.0368 |
| Avg. daily time 54-69 (%) | 443 | +0.817 [-0.503, +2.138] | 4.562 | 1.21 | 0.225 | not applied (n < 1000) | 0.727 | +0.5 | -0.3 | -0.0391 | -0.0368 |
| Time < 70, pooled (%) | 443 | +0.828 [-0.509, +2.165] | 4.063 | 1.21 | 0.225 | not applied (n < 1000) | 0.727 | +0.5 | -0.3 | -0.0382 | -0.0368 |
| Avg. daily time < 70 (%) | 443 | +0.974 [-0.347, +2.294] | 4.98 | 1.45 | 0.148 | not applied (n < 1000) | 0.727 | -0.1 | -0.9 | -0.0367 | -0.0368 |
| Time 54-250, pooled (%) | 443 | -0.237 [-1.663, +1.189] | -4.308 | -0.33 | 0.745 | not applied (n < 1000) | 0.958 | +1.9 | +1.0 | -0.0396 | -0.0368 |
| Avg. daily time 54-250 (%) | 443 | -0.820 [-2.217, +0.577] | -20.23 | -1.15 | 0.250 | not applied (n < 1000) | 0.727 | +0.5 | -0.3 | -0.0321 | -0.0368 |
| Time 181-250, pooled (%) | 443 | -0.100 [-1.511, +1.312] | -0.3571 | -0.14 | 0.890 | not applied (n < 1000) | 0.986 | +2.0 | +1.1 | -0.0415 | -0.0368 |
| Avg. daily time 181-250 (%) | 443 | -0.270 [-1.748, +1.208] | -0.9606 | -0.36 | 0.720 | not applied (n < 1000) | 0.950 | +1.8 | +1.0 | -0.0455 | -0.0368 |
| Time > 180, pooled (%) | 443 | -0.135 [-1.548, +1.277] | -0.4844 | -0.19 | 0.851 | not applied (n < 1000) | 0.986 | +2.0 | +1.1 | -0.0413 | -0.0368 |
| Avg. daily time > 180 (%) | 443 | -0.308 [-1.787, +1.170] | -1.094 | -0.41 | 0.683 | not applied (n < 1000) | 0.949 | +1.8 | +1.0 | -0.0452 | -0.0368 |
| Nocturnal time > 180 (%) | 443 | +0.502 [-0.786, +1.791] | 1.401 | 0.76 | 0.445 | not applied (n < 1000) | 0.845 | +1.5 | +0.6 | -0.0404 | -0.0368 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Steps per wear-day
*n = 401; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 401 | +223.381 [-142.588, +589.351] | 718.1 | 1.20 | 0.232 | not applied (n < 1000) | 0.727 | +0.6 | +0.0 | 0.0738 | 0.0795 |
| Mean glucose (mg/dL) | 401 | +76.604 [-305.816, +459.023] | 10.25 | 0.39 | 0.695 | not applied (n < 1000) | 0.949 | +1.8 | +1.2 | 0.0729 | 0.0795 |
| GMI (%) | 401 | +76.604 [-305.816, +459.023] | 428.5 | 0.39 | 0.695 | not applied (n < 1000) | 0.949 | +1.8 | +1.2 | 0.0729 | 0.0795 |
| Nocturnal mean 00-06h (mg/dL) | 401 | +289.294 [-87.344, +665.931] | 29.72 | 1.51 | 0.132 | not applied (n < 1000) | 0.727 | -0.4 | -1.1 | 0.0743 | 0.0795 |
| Glucose SD, pooled (mg/dL) | 401 | -106.092 [-516.660, +304.475] | -43.95 | -0.51 | 0.613 | not applied (n < 1000) | 0.927 | +1.7 | +1.0 | 0.0749 | 0.0795 |
| Avg. daily SD (mg/dL) | 401 | -124.202 [-532.562, +284.158] | -51.32 | -0.60 | 0.551 | not applied (n < 1000) | 0.891 | +1.5 | +0.9 | 0.0750 | 0.0795 |
| CV (%) | 401 | -154.160 [-531.069, +222.750] | -70.83 | -0.80 | 0.423 | not applied (n < 1000) | 0.845 | +1.3 | +0.7 | 0.0777 | 0.0795 |
| Mean / SD ratio | 401 | +161.447 [-204.104, +526.998] | 151.5 | 0.87 | 0.387 | not applied (n < 1000) | 0.843 | +1.2 | +0.6 | 0.0780 | 0.0795 |
| Avg. daily mean / SD | 401 | +156.665 [-200.909, +514.239] | 114.5 | 0.86 | 0.390 | not applied (n < 1000) | 0.843 | +1.2 | +0.6 | 0.0780 | 0.0795 |
| MAG (mg/dL/h) | 401 | +254.252 [-169.919, +678.424] | 43 | 1.17 | 0.240 | not applied (n < 1000) | 0.727 | +0.0 | -0.6 | 0.0734 | 0.0795 |
| Avg. daily range (mg/dL) | 401 | -37.457 [-452.500, +377.587] | -3.299 | -0.18 | 0.860 | not applied (n < 1000) | 0.986 | +2.0 | +1.3 | 0.0683 | 0.0795 |
| SD of daily means (mg/dL) | 401 | +0.270 [-399.143, +399.683] | 0.1419 | 0.00 | 0.999 | not applied (n < 1000) | 0.999 | +2.0 | +1.4 | 0.0777 | 0.0795 |
| Time in range 70-180, pooled (%) | 401 | -343.974 [-694.409, +6.462] | -1152 | -1.92 | 0.054 | not applied (n < 1000) | 0.692 | -1.7 | -2.3 | 0.0717 | 0.0795 |
| Avg. daily time in range 70-180 (%) | 401 | -319.850 [-686.951, +47.250] | -1032 | -1.71 | 0.088 | not applied (n < 1000) | 0.704 | -1.2 | -1.8 | 0.0662 | 0.0795 |
| Any reading < 54 during wear (0/1) | 401 | +29.849 [-301.843, +361.541] | 77.67 | 0.18 | 0.860 | not applied (n < 1000) | 0.986 | +2.0 | +1.4 | 0.0689 | 0.0795 |
| Time < 54, pooled (%) | 401 | +283.407 [-193.204, +760.018] | 5028 | 1.17 | 0.244 | not applied (n < 1000) | 0.727 | -0.4 | -1.0 | 0.0680 | 0.0795 |
| Avg. daily time < 54 (%) | 401 | +272.455 [-237.187, +782.097] | 6477 | 1.05 | 0.295 | not applied (n < 1000) | 0.786 | -0.3 | -0.9 | 0.0722 | 0.0795 |
| Time 54-69, pooled (%) | 401 | +13.606 [-329.310, +356.522] | 74.15 | 0.08 | 0.938 | not applied (n < 1000) | 0.986 | +2.0 | +1.4 | 0.0713 | 0.0795 |
| Avg. daily time 54-69 (%) | 401 | -49.239 [-394.137, +295.659] | -274.8 | -0.28 | 0.780 | not applied (n < 1000) | 0.958 | +1.9 | +1.3 | 0.0740 | 0.0795 |
| Time < 70, pooled (%) | 401 | +86.116 [-292.884, +465.115] | 415.3 | 0.45 | 0.656 | not applied (n < 1000) | 0.949 | +1.8 | +1.2 | 0.0674 | 0.0795 |
| Avg. daily time < 70 (%) | 401 | +14.231 [-357.608, +386.071] | 72.18 | 0.08 | 0.940 | not applied (n < 1000) | 0.986 | +2.0 | +1.4 | 0.0703 | 0.0795 |
| Time 54-250, pooled (%) | 401 | -271.308 [-741.338, +198.723] | -4702 | -1.13 | 0.258 | not applied (n < 1000) | 0.727 | -0.2 | -0.8 | 0.0678 | 0.0795 |
| Avg. daily time 54-250 (%) | 401 | -259.071 [-766.135, +247.993] | -6026 | -1.00 | 0.317 | not applied (n < 1000) | 0.806 | -0.1 | -0.7 | 0.0716 | 0.0795 |
| Time 181-250, pooled (%) | 401 | +308.638 [-55.654, +672.931] | 1111 | 1.66 | 0.097 | not applied (n < 1000) | 0.704 | -1.0 | -1.6 | 0.0787 | 0.0795 |
| Avg. daily time 181-250 (%) | 401 | +342.287 [-25.269, +709.843] | 1211 | 1.83 | 0.068 | not applied (n < 1000) | 0.692 | -1.7 | -2.3 | 0.0764 | 0.0795 |
| Time > 180, pooled (%) | 401 | +306.957 [-56.704, +670.618] | 1102 | 1.65 | 0.098 | not applied (n < 1000) | 0.704 | -0.9 | -1.6 | 0.0787 | 0.0795 |
| Avg. daily time > 180 (%) | 401 | +340.247 [-26.476, +706.970] | 1200 | 1.82 | 0.069 | not applied (n < 1000) | 0.692 | -1.6 | -2.2 | 0.0763 | 0.0795 |
| Nocturnal time > 180 (%) | 401 | +491.267 [-189.456, +1171.989] | 1305 | 1.41 | 0.157 | not applied (n < 1000) | 0.727 | -5.2 | -5.8 | 0.0604 | 0.0795 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 401; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 401 | +0.463 [-0.781, +1.707] | 1.489 | 0.73 | 0.466 | not applied (n < 1000) | 0.845 | +1.4 | +0.0 | 0.0932 | 0.0997 |
| Mean glucose (mg/dL) | 401 | +0.045 [-1.221, +1.310] | 0.005989 | 0.07 | 0.945 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0948 | 0.0997 |
| GMI (%) | 401 | +0.045 [-1.221, +1.310] | 0.2504 | 0.07 | 0.945 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0948 | 0.0997 |
| Nocturnal mean 00-06h (mg/dL) | 401 | +0.535 [-0.686, +1.755] | 0.05496 | 0.86 | 0.390 | not applied (n < 1000) | 0.843 | +1.2 | -0.2 | 0.0942 | 0.0997 |
| Glucose SD, pooled (mg/dL) | 401 | -0.136 [-1.365, +1.092] | -0.05645 | -0.22 | 0.828 | not applied (n < 1000) | 0.981 | +1.9 | +0.5 | 0.0965 | 0.0997 |
| Avg. daily SD (mg/dL) | 401 | -0.347 [-1.524, +0.831] | -0.1432 | -0.58 | 0.564 | not applied (n < 1000) | 0.897 | +1.6 | +0.2 | 0.0976 | 0.0997 |
| CV (%) | 401 | -0.228 [-1.340, +0.884] | -0.1046 | -0.40 | 0.688 | not applied (n < 1000) | 0.949 | +1.8 | +0.4 | 0.0976 | 0.0997 |
| Mean / SD ratio | 401 | +0.222 [-0.889, +1.332] | 0.2079 | 0.39 | 0.696 | not applied (n < 1000) | 0.949 | +1.9 | +0.4 | 0.0975 | 0.0997 |
| Avg. daily mean / SD | 401 | +0.411 [-0.635, +1.456] | 0.3002 | 0.77 | 0.441 | not applied (n < 1000) | 0.845 | +1.5 | +0.1 | 0.0989 | 0.0997 |
| MAG (mg/dL/h) | 401 | +1.128 [-0.095, +2.350] | 0.1907 | 1.81 | 0.071 | not applied (n < 1000) | 0.692 | -1.8 | -3.2 | 0.1004 | 0.0997 |
| Avg. daily range (mg/dL) | 401 | +0.020 [-1.234, +1.274] | 0.00174 | 0.03 | 0.975 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0906 | 0.0997 |
| SD of daily means (mg/dL) | 401 | +0.487 [-0.844, +1.819] | 0.2559 | 0.72 | 0.473 | not applied (n < 1000) | 0.845 | +1.3 | -0.1 | 0.0982 | 0.0997 |
| Time in range 70-180, pooled (%) | 401 | -1.630 [-2.728, -0.531] | -5.456 | -2.91 | 0.004** | not applied (n < 1000) | 0.294 | -6.1 | -7.5 | 0.1087 | 0.0997 |
| Avg. daily time in range 70-180 (%) | 401 | -1.536 [-2.642, -0.430] | -4.956 | -2.72 | 0.006** | not applied (n < 1000) | 0.294 | -5.2 | -6.6 | 0.1009 | 0.0997 |
| Any reading < 54 during wear (0/1) | 401 | +0.244 [-0.876, +1.363] | 0.634 | 0.43 | 0.670 | not applied (n < 1000) | 0.949 | +1.8 | +0.4 | 0.0871 | 0.0997 |
| Time < 54, pooled (%) | 401 | +1.083 [-0.452, +2.617] | 19.21 | 1.38 | 0.167 | not applied (n < 1000) | 0.727 | -1.4 | -2.8 | 0.0921 | 0.0997 |
| Avg. daily time < 54 (%) | 401 | +1.037 [-0.731, +2.806] | 24.66 | 1.15 | 0.250 | not applied (n < 1000) | 0.727 | -1.2 | -2.7 | 0.0920 | 0.0997 |
| Time 54-69, pooled (%) | 401 | +0.531 [-0.593, +1.655] | 2.894 | 0.93 | 0.355 | not applied (n < 1000) | 0.843 | +1.2 | -0.3 | 0.0937 | 0.0997 |
| Avg. daily time 54-69 (%) | 401 | +0.301 [-0.830, +1.432] | 1.68 | 0.52 | 0.602 | not applied (n < 1000) | 0.925 | +1.7 | +0.3 | 0.0922 | 0.0997 |
| Time < 70, pooled (%) | 401 | +0.751 [-0.473, +1.974] | 3.621 | 1.20 | 0.229 | not applied (n < 1000) | 0.727 | +0.3 | -1.1 | 0.0922 | 0.0997 |
| Avg. daily time < 70 (%) | 401 | +0.495 [-0.728, +1.718] | 2.511 | 0.79 | 0.428 | not applied (n < 1000) | 0.845 | +1.3 | -0.2 | 0.0894 | 0.0997 |
| Time 54-250, pooled (%) | 401 | -1.100 [-2.590, +0.391] | -19.06 | -1.45 | 0.148 | not applied (n < 1000) | 0.727 | -1.5 | -2.9 | 0.0931 | 0.0997 |
| Avg. daily time 54-250 (%) | 401 | -1.076 [-2.760, +0.608] | -25.03 | -1.25 | 0.210 | not applied (n < 1000) | 0.727 | -1.5 | -2.9 | 0.0938 | 0.0997 |
| Time 181-250, pooled (%) | 401 | +1.194 [+0.043, +2.345] | 4.296 | 2.03 | 0.042* | not applied (n < 1000) | 0.645 | -2.3 | -3.7 | 0.1046 | 0.0997 |
| Avg. daily time 181-250 (%) | 401 | +1.336 [+0.193, +2.479] | 4.724 | 2.29 | 0.022* | not applied (n < 1000) | 0.479 | -3.4 | -4.8 | 0.1036 | 0.0997 |
| Time > 180, pooled (%) | 401 | +1.200 [+0.051, +2.349] | 4.31 | 2.05 | 0.041* | not applied (n < 1000) | 0.645 | -2.4 | -3.8 | 0.1046 | 0.0997 |
| Avg. daily time > 180 (%) | 401 | +1.341 [+0.201, +2.481] | 4.731 | 2.31 | 0.021* | not applied (n < 1000) | 0.479 | -3.5 | -4.9 | 0.1037 | 0.0997 |
| Nocturnal time > 180 (%) | 401 | +1.241 [-0.251, +2.734] | 3.297 | 1.63 | 0.103 | not applied (n < 1000) | 0.709 | -2.4 | -3.9 | 0.0906 | 0.0997 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 403; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 403 | +0.021 [-0.748, +0.789] | 0.06653 | 0.05 | 0.958 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.1260 | 0.1326 |
| Mean glucose (mg/dL) | 403 | +0.130 [-0.591, +0.850] | 0.01737 | 0.35 | 0.725 | not applied (n < 1000) | 0.950 | +1.9 | -0.1 | 0.1308 | 0.1326 |
| GMI (%) | 403 | +0.130 [-0.591, +0.850] | 0.7261 | 0.35 | 0.725 | not applied (n < 1000) | 0.950 | +1.9 | -0.1 | 0.1308 | 0.1326 |
| Nocturnal mean 00-06h (mg/dL) | 403 | +0.387 [-0.327, +1.100] | 0.03981 | 1.06 | 0.288 | not applied (n < 1000) | 0.779 | +0.8 | -1.2 | 0.1336 | 0.1326 |
| Glucose SD, pooled (mg/dL) | 403 | -0.009 [-0.733, +0.714] | -0.003891 | -0.03 | 0.980 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.1298 | 0.1326 |
| Avg. daily SD (mg/dL) | 403 | -0.019 [-0.735, +0.698] | -0.00769 | -0.05 | 0.959 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.1296 | 0.1326 |
| CV (%) | 403 | -0.093 [-0.745, +0.559] | -0.04252 | -0.28 | 0.780 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.1304 | 0.1326 |
| Mean / SD ratio | 403 | +0.128 [-0.507, +0.763] | 0.1182 | 0.39 | 0.694 | not applied (n < 1000) | 0.949 | +1.9 | -0.1 | 0.1301 | 0.1326 |
| Avg. daily mean / SD | 403 | +0.099 [-0.522, +0.721] | 0.07132 | 0.31 | 0.754 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.1289 | 0.1326 |
| MAG (mg/dL/h) | 403 | +0.690 [-0.020, +1.400] | 0.117 | 1.90 | 0.057 | not applied (n < 1000) | 0.692 | -2.0 | -4.0 | 0.1378 | 0.1326 |
| Avg. daily range (mg/dL) | 403 | +0.029 [-0.684, +0.742] | 0.002539 | 0.08 | 0.936 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.1274 | 0.1326 |
| SD of daily means (mg/dL) | 403 | +0.538 [-0.183, +1.260] | 0.2828 | 1.46 | 0.144 | not applied (n < 1000) | 0.727 | -0.4 | -2.4 | 0.1373 | 0.1326 |
| Time in range 70-180, pooled (%) | 403 | -0.167 [-0.872, +0.538] | -0.559 | -0.47 | 0.642 | not applied (n < 1000) | 0.939 | +1.8 | -0.2 | 0.1284 | 0.1326 |
| Avg. daily time in range 70-180 (%) | 403 | -0.193 [-0.849, +0.462] | -0.6233 | -0.58 | 0.563 | not applied (n < 1000) | 0.897 | +1.7 | -0.3 | 0.1302 | 0.1326 |
| Any reading < 54 during wear (0/1) | 403 | +0.290 [-0.376, +0.957] | 0.7574 | 0.85 | 0.393 | not applied (n < 1000) | 0.843 | +1.3 | -0.7 | 0.1276 | 0.1326 |
| Time < 54, pooled (%) | 403 | +0.717 [+0.167, +1.267] | 12.75 | 2.56 | 0.011* | not applied (n < 1000) | 0.378 | -2.2 | -4.2 | 0.1382 | 0.1326 |
| Avg. daily time < 54 (%) | 403 | +0.205 [-0.456, +0.866] | 4.892 | 0.61 | 0.543 | not applied (n < 1000) | 0.891 | +1.6 | -0.4 | 0.1293 | 0.1326 |
| Time 54-69, pooled (%) | 403 | +0.014 [-0.635, +0.663] | 0.07635 | 0.04 | 0.966 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.1309 | 0.1326 |
| Avg. daily time 54-69 (%) | 403 | -0.136 [-0.749, +0.478] | -0.7573 | -0.43 | 0.665 | not applied (n < 1000) | 0.949 | +1.8 | -0.1 | 0.1310 | 0.1326 |
| Time < 70, pooled (%) | 403 | +0.200 [-0.446, +0.845] | 0.9646 | 0.61 | 0.544 | not applied (n < 1000) | 0.891 | +1.7 | -0.3 | 0.1314 | 0.1326 |
| Avg. daily time < 70 (%) | 403 | -0.078 [-0.685, +0.529] | -0.3972 | -0.25 | 0.801 | not applied (n < 1000) | 0.971 | +1.9 | -0.0 | 0.1301 | 0.1326 |
| Time 54-250, pooled (%) | 403 | -0.675 [-1.226, -0.124] | -11.72 | -2.40 | 0.016* | not applied (n < 1000) | 0.479 | -1.7 | -3.7 | 0.1366 | 0.1326 |
| Avg. daily time 54-250 (%) | 403 | -0.165 [-0.857, +0.528] | -3.843 | -0.47 | 0.641 | not applied (n < 1000) | 0.939 | +1.8 | -0.2 | 0.1296 | 0.1326 |
| Time 181-250, pooled (%) | 403 | +0.038 [-0.706, +0.781] | 0.1355 | 0.10 | 0.921 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.1270 | 0.1326 |
| Avg. daily time 181-250 (%) | 403 | +0.272 [-0.437, +0.981] | 0.9622 | 0.75 | 0.452 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.1315 | 0.1326 |
| Time > 180, pooled (%) | 403 | +0.033 [-0.712, +0.777] | 0.1172 | 0.09 | 0.932 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.1270 | 0.1326 |
| Avg. daily time > 180 (%) | 403 | +0.266 [-0.445, +0.976] | 0.9379 | 0.73 | 0.463 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.1314 | 0.1326 |
| Nocturnal time > 180 (%) | 403 | +0.669 [-0.125, +1.462] | 1.78 | 1.65 | 0.099 | not applied (n < 1000) | 0.704 | -1.6 | -3.6 | 0.1367 | 0.1326 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Total sleep time per night (min)
*n = 409; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 409 | -10.472 [-16.821, -4.123] | -33.44 | -3.23 | 0.001** | not applied (n < 1000) | 0.240 | -7.7 | +0.0 | 0.0282 | 0.0016 |
| Mean glucose (mg/dL) | 409 | -6.649 [-12.862, -0.437] | -0.8919 | -2.10 | 0.036* | not applied (n < 1000) | 0.640 | -2.3 | +5.4 | 0.0028 | 0.0016 |
| GMI (%) | 409 | -6.649 [-12.862, -0.437] | -37.29 | -2.10 | 0.036* | not applied (n < 1000) | 0.640 | -2.3 | +5.4 | 0.0028 | 0.0016 |
| Nocturnal mean 00-06h (mg/dL) | 409 | -7.835 [-14.451, -1.219] | -0.8042 | -2.32 | 0.020* | not applied (n < 1000) | 0.479 | -3.7 | +4.1 | 0.0048 | 0.0016 |
| Glucose SD, pooled (mg/dL) | 409 | -0.443 [-7.375, +6.489] | -0.1834 | -0.13 | 0.900 | not applied (n < 1000) | 0.986 | +2.0 | +9.7 | -0.0019 | 0.0016 |
| Avg. daily SD (mg/dL) | 409 | -0.461 [-7.307, +6.385] | -0.1891 | -0.13 | 0.895 | not applied (n < 1000) | 0.986 | +2.0 | +9.7 | -0.0015 | 0.0016 |
| CV (%) | 409 | +2.426 [-4.230, +9.082] | 1.112 | 0.71 | 0.475 | not applied (n < 1000) | 0.845 | +1.4 | +9.2 | -0.0004 | 0.0016 |
| Mean / SD ratio | 409 | -2.465 [-9.116, +4.185] | -2.316 | -0.73 | 0.467 | not applied (n < 1000) | 0.845 | +1.4 | +9.1 | -0.0001 | 0.0016 |
| Avg. daily mean / SD | 409 | -1.106 [-7.626, +5.414] | -0.8044 | -0.33 | 0.740 | not applied (n < 1000) | 0.958 | +1.9 | +9.6 | -0.0008 | 0.0016 |
| MAG (mg/dL/h) | 409 | -7.684 [-14.193, -1.175] | -1.294 | -2.31 | 0.021* | not applied (n < 1000) | 0.479 | -3.7 | +4.0 | 0.0130 | 0.0016 |
| Avg. daily range (mg/dL) | 409 | +0.549 [-6.700, +7.799] | 0.04831 | 0.15 | 0.882 | not applied (n < 1000) | 0.986 | +2.0 | +9.7 | -0.0028 | 0.0016 |
| SD of daily means (mg/dL) | 409 | +0.133 [-5.889, +6.156] | 0.07044 | 0.04 | 0.965 | not applied (n < 1000) | 0.986 | +2.0 | +9.7 | -0.0010 | 0.0016 |
| Time in range 70-180, pooled (%) | 409 | -1.987 [-8.761, +4.788] | -6.649 | -0.57 | 0.565 | not applied (n < 1000) | 0.897 | +1.6 | +9.3 | -0.0002 | 0.0016 |
| Avg. daily time in range 70-180 (%) | 409 | -2.412 [-9.038, +4.214] | -7.792 | -0.71 | 0.476 | not applied (n < 1000) | 0.845 | +1.4 | +9.1 | 0.0006 | 0.0016 |
| Any reading < 54 during wear (0/1) | 409 | +1.336 [-4.284, +6.956] | 3.467 | 0.47 | 0.641 | not applied (n < 1000) | 0.939 | +1.8 | +9.5 | -0.0031 | 0.0016 |
| Time < 54, pooled (%) | 409 | +0.712 [-5.097, +6.520] | 12.73 | 0.24 | 0.810 | not applied (n < 1000) | 0.971 | +2.0 | +9.7 | -0.0100 | 0.0016 |
| Avg. daily time < 54 (%) | 409 | +2.715 [-2.411, +7.842] | 64.92 | 1.04 | 0.299 | not applied (n < 1000) | 0.787 | +1.3 | +9.0 | -0.0033 | 0.0016 |
| Time 54-69, pooled (%) | 409 | +9.186 [+2.993, +15.380] | 50.08 | 2.91 | 0.004** | not applied (n < 1000) | 0.294 | -6.3 | +1.5 | 0.0101 | 0.0016 |
| Avg. daily time 54-69 (%) | 409 | +8.801 [+2.415, +15.187] | 48.45 | 2.70 | 0.007** | not applied (n < 1000) | 0.294 | -5.5 | +2.2 | 0.0113 | 0.0016 |
| Time < 70, pooled (%) | 409 | +8.271 [+2.266, +14.276] | 39.99 | 2.70 | 0.007** | not applied (n < 1000) | 0.294 | -4.7 | +3.0 | 0.0081 | 0.0016 |
| Avg. daily time < 70 (%) | 409 | +8.543 [+2.356, +14.730] | 42.9 | 2.71 | 0.007** | not applied (n < 1000) | 0.294 | -5.1 | +2.6 | 0.0123 | 0.0016 |
| Time 54-250, pooled (%) | 409 | -0.202 [-5.974, +5.569] | -3.532 | -0.07 | 0.945 | not applied (n < 1000) | 0.986 | +2.0 | +9.7 | -0.0102 | 0.0016 |
| Avg. daily time 54-250 (%) | 409 | -1.960 [-7.456, +3.536] | -45.86 | -0.70 | 0.485 | not applied (n < 1000) | 0.845 | +1.6 | +9.3 | -0.0064 | 0.0016 |
| Time 181-250, pooled (%) | 409 | -3.847 [-10.476, +2.782] | -13.77 | -1.14 | 0.255 | not applied (n < 1000) | 0.727 | +0.5 | +8.3 | -0.0032 | 0.0016 |
| Avg. daily time 181-250 (%) | 409 | -3.177 [-9.420, +3.066] | -11.27 | -1.00 | 0.319 | not applied (n < 1000) | 0.806 | +1.0 | +8.7 | -0.0004 | 0.0016 |
| Time > 180, pooled (%) | 409 | -3.936 [-10.558, +2.686] | -14.06 | -1.17 | 0.244 | not applied (n < 1000) | 0.727 | +0.5 | +8.2 | -0.0031 | 0.0016 |
| Avg. daily time > 180 (%) | 409 | -3.274 [-9.507, +2.959] | -11.59 | -1.03 | 0.303 | not applied (n < 1000) | 0.787 | +0.9 | +8.7 | -0.0003 | 0.0016 |
| Nocturnal time > 180 (%) | 409 | -5.125 [-12.372, +2.123] | -13.73 | -1.39 | 0.166 | not applied (n < 1000) | 0.727 | -0.5 | +7.3 | 0.0037 | 0.0016 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Garmin stress score, mean (0-100)
*n = 403; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 403 | +0.128 [-1.671, +1.926] | 0.411 | 0.14 | 0.889 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0479 | 0.0562 |
| Mean glucose (mg/dL) | 403 | +0.979 [-0.681, +2.640] | 0.1313 | 1.16 | 0.248 | not applied (n < 1000) | 0.727 | +0.6 | -1.4 | 0.0561 | 0.0562 |
| GMI (%) | 403 | +0.979 [-0.681, +2.640] | 5.49 | 1.16 | 0.248 | not applied (n < 1000) | 0.727 | +0.6 | -1.4 | 0.0561 | 0.0562 |
| Nocturnal mean 00-06h (mg/dL) | 403 | +1.160 [-0.545, +2.865] | 0.1194 | 1.33 | 0.182 | not applied (n < 1000) | 0.727 | +0.1 | -1.9 | 0.0583 | 0.0562 |
| Glucose SD, pooled (mg/dL) | 403 | +0.885 [-0.848, +2.617] | 0.3637 | 1.00 | 0.317 | not applied (n < 1000) | 0.806 | +0.8 | -1.1 | 0.0553 | 0.0562 |
| Avg. daily SD (mg/dL) | 403 | +0.923 [-0.812, +2.658] | 0.3782 | 1.04 | 0.297 | not applied (n < 1000) | 0.786 | +0.7 | -1.2 | 0.0559 | 0.0562 |
| CV (%) | 403 | +0.431 [-1.202, +2.063] | 0.1967 | 0.52 | 0.605 | not applied (n < 1000) | 0.925 | +1.7 | -0.3 | 0.0521 | 0.0562 |
| Mean / SD ratio | 403 | -0.385 [-1.995, +1.226] | -0.3561 | -0.47 | 0.640 | not applied (n < 1000) | 0.939 | +1.8 | -0.2 | 0.0518 | 0.0562 |
| Avg. daily mean / SD | 403 | -0.524 [-2.115, +1.068] | -0.3762 | -0.64 | 0.519 | not applied (n < 1000) | 0.885 | +1.6 | -0.4 | 0.0520 | 0.0562 |
| MAG (mg/dL/h) | 403 | +0.672 [-0.975, +2.319] | 0.1139 | 0.80 | 0.424 | not applied (n < 1000) | 0.845 | +1.3 | -0.7 | 0.0548 | 0.0562 |
| Avg. daily range (mg/dL) | 403 | +0.794 [-0.896, +2.483] | 0.06942 | 0.92 | 0.357 | not applied (n < 1000) | 0.843 | +1.0 | -0.9 | 0.0564 | 0.0562 |
| SD of daily means (mg/dL) | 403 | +1.104 [-0.487, +2.695] | 0.5802 | 1.36 | 0.174 | not applied (n < 1000) | 0.727 | +0.2 | -1.8 | 0.0569 | 0.0562 |
| Time in range 70-180, pooled (%) | 403 | -1.090 [-2.713, +0.532] | -3.643 | -1.32 | 0.188 | not applied (n < 1000) | 0.727 | +0.2 | -1.8 | 0.0575 | 0.0562 |
| Avg. daily time in range 70-180 (%) | 403 | -1.155 [-2.747, +0.437] | -3.721 | -1.42 | 0.155 | not applied (n < 1000) | 0.727 | -0.0 | -2.0 | 0.0574 | 0.0562 |
| Any reading < 54 during wear (0/1) | 403 | +0.232 [-1.301, +1.765] | 0.6049 | 0.30 | 0.767 | not applied (n < 1000) | 0.958 | +1.9 | -0.1 | 0.0513 | 0.0562 |
| Time < 54, pooled (%) | 403 | +0.574 [-0.779, +1.927] | 10.21 | 0.83 | 0.406 | not applied (n < 1000) | 0.844 | +1.5 | -0.5 | 0.0528 | 0.0562 |
| Avg. daily time < 54 (%) | 403 | +0.035 [-1.555, +1.625] | 0.8371 | 0.04 | 0.965 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0475 | 0.0562 |
| Time 54-69, pooled (%) | 403 | -0.085 [-1.691, +1.520] | -0.4664 | -0.10 | 0.917 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0483 | 0.0562 |
| Avg. daily time 54-69 (%) | 403 | -0.628 [-2.209, +0.952] | -3.511 | -0.78 | 0.436 | not applied (n < 1000) | 0.845 | +1.4 | -0.6 | 0.0523 | 0.0562 |
| Time < 70, pooled (%) | 403 | +0.075 [-1.495, +1.645] | 0.361 | 0.09 | 0.926 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0473 | 0.0562 |
| Avg. daily time < 70 (%) | 403 | -0.560 [-2.120, +1.001] | -2.842 | -0.70 | 0.482 | not applied (n < 1000) | 0.845 | +1.5 | -0.4 | 0.0515 | 0.0562 |
| Time 54-250, pooled (%) | 403 | -0.623 [-1.963, +0.717] | -10.83 | -0.91 | 0.362 | not applied (n < 1000) | 0.843 | +1.4 | -0.5 | 0.0532 | 0.0562 |
| Avg. daily time 54-250 (%) | 403 | -0.123 [-1.648, +1.402] | -2.866 | -0.16 | 0.874 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.0499 | 0.0562 |
| Time 181-250, pooled (%) | 403 | +1.112 [-0.591, +2.815] | 4.001 | 1.28 | 0.201 | not applied (n < 1000) | 0.727 | +0.1 | -1.9 | 0.0565 | 0.0562 |
| Avg. daily time 181-250 (%) | 403 | +1.642 [-0.012, +3.295] | 5.808 | 1.95 | 0.052 | not applied (n < 1000) | 0.692 | -2.1 | -4.1 | 0.0629 | 0.0562 |
| Time > 180, pooled (%) | 403 | +1.122 [-0.580, +2.825] | 4.03 | 1.29 | 0.196 | not applied (n < 1000) | 0.727 | +0.1 | -1.9 | 0.0566 | 0.0562 |
| Avg. daily time > 180 (%) | 403 | +1.651 [-0.001, +3.302] | 5.824 | 1.96 | 0.050 | not applied (n < 1000) | 0.692 | -2.2 | -4.1 | 0.0630 | 0.0562 |
| Nocturnal time > 180 (%) | 403 | +1.928 [+0.096, +3.759] | 5.132 | 2.06 | 0.039* | not applied (n < 1000) | 0.645 | -3.4 | -5.4 | 0.0679 | 0.0562 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

### Population: Healthy group (no diabetes + pre-diabetes / lifestyle)

#### MoCA total score (0-30)
*n = 393; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 393 | -0.192 [-0.482, +0.099] | -0.6375 | -1.29 | 0.196 | not applied (n < 1000) | 0.714 | +0.0 | +0.0 | 0.0233 | 0.0208 |
| Mean glucose (mg/dL) | 393 | -0.199 [-0.476, +0.078] | -0.02632 | -1.41 | 0.160 | not applied (n < 1000) | 0.690 | -0.3 | -0.3 | 0.0211 | 0.0208 |
| GMI (%) | 393 | -0.199 [-0.476, +0.078] | -1.1 | -1.41 | 0.160 | not applied (n < 1000) | 0.690 | -0.3 | -0.3 | 0.0211 | 0.0208 |
| Nocturnal mean 00-06h (mg/dL) | 393 | -0.037 [-0.324, +0.249] | -0.003886 | -0.26 | 0.798 | not applied (n < 1000) | 0.933 | +1.9 | +1.9 | 0.0158 | 0.0208 |
| Glucose SD, pooled (mg/dL) | 393 | +0.073 [-0.219, +0.364] | 0.03248 | 0.49 | 0.626 | not applied (n < 1000) | 0.886 | +1.7 | +1.7 | 0.0118 | 0.0208 |
| Avg. daily SD (mg/dL) | 393 | +0.148 [-0.119, +0.415] | 0.06578 | 1.09 | 0.277 | not applied (n < 1000) | 0.737 | +0.7 | +0.7 | 0.0137 | 0.0208 |
| CV (%) | 393 | +0.162 [-0.106, +0.430] | 0.07912 | 1.19 | 0.235 | not applied (n < 1000) | 0.724 | +0.5 | +0.5 | 0.0170 | 0.0208 |
| Mean / SD ratio | 393 | -0.180 [-0.441, +0.082] | -0.1794 | -1.35 | 0.178 | not applied (n < 1000) | 0.690 | +0.1 | +0.1 | 0.0181 | 0.0208 |
| Avg. daily mean / SD | 393 | -0.209 [-0.467, +0.048] | -0.1679 | -1.60 | 0.110 | not applied (n < 1000) | 0.690 | -0.5 | -0.5 | 0.0200 | 0.0208 |
| MAG (mg/dL/h) | 393 | -0.043 [-0.296, +0.210] | -0.007359 | -0.33 | 0.741 | not applied (n < 1000) | 0.910 | +1.9 | +1.9 | 0.0194 | 0.0208 |
| Avg. daily range (mg/dL) | 393 | +0.105 [-0.156, +0.367] | 0.009668 | 0.79 | 0.429 | not applied (n < 1000) | 0.827 | +1.4 | +1.3 | 0.0144 | 0.0208 |
| SD of daily means (mg/dL) | 393 | -0.264 [-0.606, +0.077] | -0.1519 | -1.52 | 0.129 | not applied (n < 1000) | 0.690 | -2.1 | -2.1 | 0.0295 | 0.0208 |
| Time in range 70-180, pooled (%) | 393 | +0.022 [-0.241, +0.285] | 0.07489 | 0.17 | 0.868 | not applied (n < 1000) | 0.961 | +2.0 | +2.0 | 0.0134 | 0.0208 |
| Avg. daily time in range 70-180 (%) | 393 | -0.019 [-0.301, +0.264] | -0.06094 | -0.13 | 0.898 | not applied (n < 1000) | 0.969 | +2.0 | +2.0 | 0.0120 | 0.0208 |
| Any reading < 54 during wear (0/1) | 393 | +0.229 [-0.015, +0.473] | 0.6198 | 1.84 | 0.065 | not applied (n < 1000) | 0.690 | -1.0 | -1.0 | 0.0224 | 0.0208 |
| Time < 54, pooled (%) | 393 | +0.148 [-0.092, +0.388] | 2.922 | 1.21 | 0.228 | not applied (n < 1000) | 0.715 | +0.8 | +0.8 | 0.0205 | 0.0208 |
| Avg. daily time < 54 (%) | 393 | +0.090 [-0.175, +0.355] | 2.148 | 0.67 | 0.504 | not applied (n < 1000) | 0.838 | +1.5 | +1.5 | 0.0159 | 0.0208 |
| Time 54-69, pooled (%) | 393 | +0.145 [-0.116, +0.405] | 0.8063 | 1.09 | 0.277 | not applied (n < 1000) | 0.737 | +0.8 | +0.8 | 0.0179 | 0.0208 |
| Avg. daily time 54-69 (%) | 393 | +0.180 [-0.076, +0.437] | 1.014 | 1.38 | 0.168 | not applied (n < 1000) | 0.690 | +0.1 | +0.1 | 0.0186 | 0.0208 |
| Time < 70, pooled (%) | 393 | +0.165 [-0.089, +0.419] | 0.8242 | 1.28 | 0.202 | not applied (n < 1000) | 0.714 | +0.4 | +0.4 | 0.0183 | 0.0208 |
| Avg. daily time < 70 (%) | 393 | +0.182 [-0.072, +0.435] | 0.9256 | 1.40 | 0.160 | not applied (n < 1000) | 0.690 | +0.1 | +0.1 | 0.0181 | 0.0208 |
| Time 54-250, pooled (%) | 393 | -0.157 [-0.400, +0.086] | -3.099 | -1.27 | 0.205 | not applied (n < 1000) | 0.714 | +0.6 | +0.6 | 0.0208 | 0.0208 |
| Avg. daily time 54-250 (%) | 393 | -0.103 [-0.373, +0.167] | -2.423 | -0.75 | 0.456 | not applied (n < 1000) | 0.833 | +1.4 | +1.4 | 0.0161 | 0.0208 |
| Time 181-250, pooled (%) | 393 | -0.142 [-0.408, +0.125] | -0.5045 | -1.04 | 0.297 | not applied (n < 1000) | 0.750 | +0.8 | +0.8 | 0.0171 | 0.0208 |
| Avg. daily time 181-250 (%) | 393 | -0.107 [-0.392, +0.179] | -0.379 | -0.73 | 0.465 | not applied (n < 1000) | 0.833 | +1.3 | +1.3 | 0.0154 | 0.0208 |
| Time > 180, pooled (%) | 393 | -0.140 [-0.406, +0.126] | -0.4973 | -1.03 | 0.303 | not applied (n < 1000) | 0.752 | +0.9 | +0.9 | 0.0170 | 0.0208 |
| Avg. daily time > 180 (%) | 393 | -0.104 [-0.390, +0.181] | -0.3711 | -0.72 | 0.473 | not applied (n < 1000) | 0.833 | +1.4 | +1.4 | 0.0154 | 0.0208 |
| Nocturnal time > 180 (%) | 393 | -0.072 [-0.442, +0.298] | -0.212 | -0.38 | 0.704 | not applied (n < 1000) | 0.906 | +1.7 | +1.7 | 0.0122 | 0.0208 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Cognitive impairment (MoCA < 26)
*n = 393; events = 127; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 393 | OR 1.101 [0.871, 1.392] | 0.3198 | 0.80 | 0.422 | not applied (n < 1000) | 0.827 | +1.4 | +0.0 | 0.6318 | 0.6299 |
| Mean glucose (mg/dL) | 393 | OR 1.201 [0.957, 1.509] | 0.02431 | 1.58 | 0.114 | not applied (n < 1000) | 0.690 | -0.5 | -1.9 | 0.6249 | 0.6299 |
| GMI (%) | 393 | OR 1.201 [0.957, 1.509] | 1.016 | 1.58 | 0.114 | not applied (n < 1000) | 0.690 | -0.5 | -1.9 | 0.6249 | 0.6299 |
| Nocturnal mean 00-06h (mg/dL) | 393 | OR 1.080 [0.854, 1.367] | 0.008 | 0.64 | 0.521 | not applied (n < 1000) | 0.843 | +1.6 | +0.2 | 0.6214 | 0.6299 |
| Glucose SD, pooled (mg/dL) | 393 | OR 1.009 [0.802, 1.268] | 0.003878 | 0.07 | 0.941 | not applied (n < 1000) | 0.978 | +2.0 | +0.6 | 0.6253 | 0.6299 |
| Avg. daily SD (mg/dL) | 393 | OR 0.981 [0.781, 1.232] | -0.008572 | -0.17 | 0.868 | not applied (n < 1000) | 0.961 | +2.0 | +0.6 | 0.6251 | 0.6299 |
| CV (%) | 393 | OR 0.928 [0.738, 1.167] | -0.03634 | -0.64 | 0.523 | not applied (n < 1000) | 0.843 | +1.6 | +0.2 | 0.6192 | 0.6299 |
| Mean / SD ratio | 393 | OR 1.109 [0.884, 1.391] | 0.1033 | 0.89 | 0.371 | not applied (n < 1000) | 0.799 | +1.2 | -0.2 | 0.6209 | 0.6299 |
| Avg. daily mean / SD | 393 | OR 1.112 [0.888, 1.393] | 0.08523 | 0.93 | 0.354 | not applied (n < 1000) | 0.787 | +1.1 | -0.2 | 0.6214 | 0.6299 |
| MAG (mg/dL/h) | 393 | OR 1.183 [0.942, 1.486] | 0.02902 | 1.45 | 0.147 | not applied (n < 1000) | 0.690 | -0.1 | -1.5 | 0.6340 | 0.6299 |
| Avg. daily range (mg/dL) | 393 | OR 1.057 [0.843, 1.327] | 0.005117 | 0.48 | 0.630 | not applied (n < 1000) | 0.888 | +1.8 | +0.4 | 0.6279 | 0.6299 |
| SD of daily means (mg/dL) | 393 | OR 1.163 [0.930, 1.454] | 0.08677 | 1.33 | 0.185 | not applied (n < 1000) | 0.712 | +0.3 | -1.1 | 0.6277 | 0.6299 |
| Time in range 70-180, pooled (%) | 393 | OR 0.955 [0.761, 1.197] | -0.1565 | -0.40 | 0.687 | not applied (n < 1000) | 0.906 | +1.8 | +0.5 | 0.6259 | 0.6299 |
| Avg. daily time in range 70-180 (%) | 393 | OR 0.964 [0.769, 1.208] | -0.1204 | -0.32 | 0.750 | not applied (n < 1000) | 0.916 | +1.9 | +0.5 | 0.6260 | 0.6299 |
| Any reading < 54 during wear (0/1) | 393 | OR 0.906 [0.718, 1.144] | -0.2663 | -0.83 | 0.408 | not applied (n < 1000) | 0.822 | +1.3 | -0.1 | 0.6279 | 0.6299 |
| Time < 54, pooled (%) | 393 | OR 0.906 [0.704, 1.164] | -1.964 | -0.77 | 0.439 | not applied (n < 1000) | 0.828 | +1.4 | +0.0 | 0.6286 | 0.6299 |
| Avg. daily time < 54 (%) | 393 | OR 0.918 [0.710, 1.187] | -2.034 | -0.65 | 0.515 | not applied (n < 1000) | 0.838 | +1.5 | +0.2 | 0.6284 | 0.6299 |
| Time 54-69, pooled (%) | 393 | OR 0.845 [0.665, 1.073] | -0.939 | -1.38 | 0.168 | not applied (n < 1000) | 0.690 | +0.0 | -1.3 | 0.6301 | 0.6299 |
| Avg. daily time 54-69 (%) | 393 | OR 0.827 [0.648, 1.056] | -1.067 | -1.52 | 0.127 | not applied (n < 1000) | 0.690 | -0.4 | -1.8 | 0.6283 | 0.6299 |
| Time < 70, pooled (%) | 393 | OR 0.841 [0.663, 1.068] | -0.8622 | -1.42 | 0.155 | not applied (n < 1000) | 0.690 | -0.1 | -1.5 | 0.6296 | 0.6299 |
| Avg. daily time < 70 (%) | 393 | OR 0.829 [0.651, 1.057] | -0.9545 | -1.51 | 0.131 | not applied (n < 1000) | 0.690 | -0.4 | -1.8 | 0.6277 | 0.6299 |
| Time 54-250, pooled (%) | 393 | OR 1.112 [0.864, 1.432] | 2.096 | 0.82 | 0.410 | not applied (n < 1000) | 0.822 | +1.3 | -0.1 | 0.6288 | 0.6299 |
| Avg. daily time 54-250 (%) | 393 | OR 1.100 [0.848, 1.427] | 2.245 | 0.72 | 0.473 | not applied (n < 1000) | 0.833 | +1.4 | +0.1 | 0.6291 | 0.6299 |
| Time 181-250, pooled (%) | 393 | OR 1.187 [0.945, 1.492] | 0.611 | 1.47 | 0.141 | not applied (n < 1000) | 0.690 | -0.2 | -1.5 | 0.6327 | 0.6299 |
| Avg. daily time 181-250 (%) | 393 | OR 1.179 [0.940, 1.478] | 0.5847 | 1.42 | 0.154 | not applied (n < 1000) | 0.690 | -0.0 | -1.4 | 0.6337 | 0.6299 |
| Time > 180, pooled (%) | 393 | OR 1.186 [0.943, 1.491] | 0.6062 | 1.46 | 0.144 | not applied (n < 1000) | 0.690 | -0.1 | -1.5 | 0.6328 | 0.6299 |
| Avg. daily time > 180 (%) | 393 | OR 1.177 [0.939, 1.476] | 0.5792 | 1.41 | 0.158 | not applied (n < 1000) | 0.690 | +0.0 | -1.3 | 0.6339 | 0.6299 |
| Nocturnal time > 180 (%) | 393 | OR 1.129 [0.905, 1.408] | 0.3577 | 1.07 | 0.284 | not applied (n < 1000) | 0.737 | +0.9 | -0.5 | 0.6326 | 0.6299 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### MoCA memory index score (0-15)
*n = 393; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 393 | +0.023 [-0.290, +0.336] | 0.07763 | 0.15 | 0.884 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | -0.0534 | -0.0472 |
| Mean glucose (mg/dL) | 393 | -0.098 [-0.365, +0.168] | -0.01304 | -0.72 | 0.470 | not applied (n < 1000) | 0.833 | +1.4 | -0.5 | -0.0527 | -0.0472 |
| GMI (%) | 393 | -0.098 [-0.365, +0.168] | -0.545 | -0.72 | 0.470 | not applied (n < 1000) | 0.833 | +1.4 | -0.5 | -0.0527 | -0.0472 |
| Nocturnal mean 00-06h (mg/dL) | 393 | -0.073 [-0.348, +0.202] | -0.007535 | -0.52 | 0.605 | not applied (n < 1000) | 0.878 | +1.7 | -0.3 | -0.0528 | -0.0472 |
| Glucose SD, pooled (mg/dL) | 393 | +0.025 [-0.219, +0.270] | 0.0113 | 0.20 | 0.840 | not applied (n < 1000) | 0.961 | +2.0 | -0.0 | -0.0554 | -0.0472 |
| Avg. daily SD (mg/dL) | 393 | +0.074 [-0.166, +0.315] | 0.03294 | 0.61 | 0.545 | not applied (n < 1000) | 0.864 | +1.7 | -0.3 | -0.0528 | -0.0472 |
| CV (%) | 393 | +0.057 [-0.199, +0.313] | 0.02773 | 0.44 | 0.663 | not applied (n < 1000) | 0.906 | +1.8 | -0.2 | -0.0594 | -0.0472 |
| Mean / SD ratio | 393 | -0.076 [-0.327, +0.176] | -0.07551 | -0.59 | 0.555 | not applied (n < 1000) | 0.864 | +1.7 | -0.3 | -0.0584 | -0.0472 |
| Avg. daily mean / SD | 393 | -0.090 [-0.334, +0.154] | -0.07236 | -0.73 | 0.468 | not applied (n < 1000) | 0.833 | +1.5 | -0.5 | -0.0576 | -0.0472 |
| MAG (mg/dL/h) | 393 | -0.142 [-0.422, +0.139] | -0.02441 | -0.99 | 0.322 | not applied (n < 1000) | 0.770 | +0.8 | -1.1 | -0.0516 | -0.0472 |
| Avg. daily range (mg/dL) | 393 | +0.016 [-0.233, +0.264] | 0.00143 | 0.12 | 0.902 | not applied (n < 1000) | 0.970 | +2.0 | +0.0 | -0.0503 | -0.0472 |
| SD of daily means (mg/dL) | 393 | -0.285 [-0.552, -0.019] | -0.1639 | -2.10 | 0.036* | not applied (n < 1000) | 0.673 | -2.9 | -4.9 | -0.0390 | -0.0472 |
| Time in range 70-180, pooled (%) | 393 | -0.051 [-0.307, +0.205] | -0.1707 | -0.39 | 0.698 | not applied (n < 1000) | 0.906 | +1.8 | -0.1 | -0.0547 | -0.0472 |
| Avg. daily time in range 70-180 (%) | 393 | -0.064 [-0.311, +0.183] | -0.2098 | -0.51 | 0.612 | not applied (n < 1000) | 0.882 | +1.8 | -0.2 | -0.0550 | -0.0472 |
| Any reading < 54 during wear (0/1) | 393 | +0.022 [-0.266, +0.310] | 0.06018 | 0.15 | 0.880 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | -0.0559 | -0.0472 |
| Time < 54, pooled (%) | 393 | +0.060 [-0.157, +0.277] | 1.184 | 0.54 | 0.588 | not applied (n < 1000) | 0.874 | +1.8 | -0.2 | -0.0531 | -0.0472 |
| Avg. daily time < 54 (%) | 393 | +0.047 [-0.190, +0.285] | 1.127 | 0.39 | 0.696 | not applied (n < 1000) | 0.906 | +1.9 | -0.1 | -0.0602 | -0.0472 |
| Time 54-69, pooled (%) | 393 | -0.114 [-0.410, +0.181] | -0.6381 | -0.76 | 0.448 | not applied (n < 1000) | 0.833 | +1.2 | -0.7 | -0.0526 | -0.0472 |
| Avg. daily time 54-69 (%) | 393 | -0.035 [-0.312, +0.243] | -0.1953 | -0.25 | 0.806 | not applied (n < 1000) | 0.935 | +1.9 | -0.0 | -0.0579 | -0.0472 |
| Time < 70, pooled (%) | 393 | -0.087 [-0.378, +0.204] | -0.4339 | -0.59 | 0.557 | not applied (n < 1000) | 0.864 | +1.6 | -0.4 | -0.0545 | -0.0472 |
| Avg. daily time < 70 (%) | 393 | -0.021 [-0.300, +0.258] | -0.107 | -0.15 | 0.883 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | -0.0601 | -0.0472 |
| Time 54-250, pooled (%) | 393 | -0.060 [-0.276, +0.156] | -1.187 | -0.55 | 0.585 | not applied (n < 1000) | 0.874 | +1.8 | -0.2 | -0.0529 | -0.0472 |
| Avg. daily time 54-250 (%) | 393 | -0.048 [-0.283, +0.188] | -1.127 | -0.40 | 0.691 | not applied (n < 1000) | 0.906 | +1.9 | -0.1 | -0.0594 | -0.0472 |
| Time 181-250, pooled (%) | 393 | +0.115 [-0.132, +0.362] | 0.4091 | 0.91 | 0.362 | not applied (n < 1000) | 0.788 | +1.2 | -0.8 | -0.0475 | -0.0472 |
| Avg. daily time 181-250 (%) | 393 | +0.084 [-0.169, +0.336] | 0.298 | 0.65 | 0.515 | not applied (n < 1000) | 0.838 | +1.6 | -0.4 | -0.0513 | -0.0472 |
| Time > 180, pooled (%) | 393 | +0.115 [-0.132, +0.362] | 0.4089 | 0.91 | 0.361 | not applied (n < 1000) | 0.788 | +1.2 | -0.8 | -0.0475 | -0.0472 |
| Avg. daily time > 180 (%) | 393 | +0.084 [-0.168, +0.336] | 0.2978 | 0.65 | 0.515 | not applied (n < 1000) | 0.838 | +1.6 | -0.4 | -0.0513 | -0.0472 |
| Nocturnal time > 180 (%) | 393 | +0.038 [-0.216, +0.292] | 0.1122 | 0.29 | 0.770 | not applied (n < 1000) | 0.926 | +1.9 | -0.1 | -0.0496 | -0.0472 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### CES-D-10 depressive symptoms (0-30)
*n = 393; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 393 | -0.071 [-0.551, +0.410] | -0.2348 | -0.29 | 0.773 | not applied (n < 1000) | 0.926 | +1.9 | +0.0 | 0.0022 | 0.0106 |
| Mean glucose (mg/dL) | 393 | -0.065 [-0.508, +0.379] | -0.008563 | -0.29 | 0.775 | not applied (n < 1000) | 0.926 | +1.9 | +0.0 | 0.0059 | 0.0106 |
| GMI (%) | 393 | -0.065 [-0.508, +0.379] | -0.358 | -0.29 | 0.775 | not applied (n < 1000) | 0.926 | +1.9 | +0.0 | 0.0059 | 0.0106 |
| Nocturnal mean 00-06h (mg/dL) | 393 | -0.182 [-0.617, +0.253] | -0.01891 | -0.82 | 0.412 | not applied (n < 1000) | 0.822 | +1.4 | -0.5 | 0.0068 | 0.0106 |
| Glucose SD, pooled (mg/dL) | 393 | +0.222 [-0.223, +0.666] | 0.09919 | 0.98 | 0.329 | not applied (n < 1000) | 0.772 | +1.0 | -0.9 | 0.0106 | 0.0106 |
| Avg. daily SD (mg/dL) | 393 | +0.085 [-0.376, +0.547] | 0.03793 | 0.36 | 0.717 | not applied (n < 1000) | 0.908 | +1.9 | -0.1 | 0.0055 | 0.0106 |
| CV (%) | 393 | +0.247 [-0.184, +0.679] | 0.1205 | 1.12 | 0.261 | not applied (n < 1000) | 0.737 | +0.8 | -1.1 | 0.0102 | 0.0106 |
| Mean / SD ratio | 393 | -0.260 [-0.667, +0.148] | -0.2596 | -1.25 | 0.211 | not applied (n < 1000) | 0.714 | +0.6 | -1.3 | 0.0104 | 0.0106 |
| Avg. daily mean / SD | 393 | -0.087 [-0.535, +0.361] | -0.06958 | -0.38 | 0.704 | not applied (n < 1000) | 0.906 | +1.8 | -0.1 | 0.0021 | 0.0106 |
| MAG (mg/dL/h) | 393 | +0.578 [+0.148, +1.008] | 0.09963 | 2.64 | 0.008** | not applied (n < 1000) | 0.350 | -4.7 | -6.6 | 0.0237 | 0.0106 |
| Avg. daily range (mg/dL) | 393 | +0.205 [-0.223, +0.633] | 0.01881 | 0.94 | 0.348 | not applied (n < 1000) | 0.787 | +1.1 | -0.8 | 0.0059 | 0.0106 |
| SD of daily means (mg/dL) | 393 | +0.350 [-0.090, +0.790] | 0.2011 | 1.56 | 0.119 | not applied (n < 1000) | 0.690 | -0.5 | -2.4 | 0.0083 | 0.0106 |
| Time in range 70-180, pooled (%) | 393 | -0.116 [-0.509, +0.277] | -0.3915 | -0.58 | 0.562 | not applied (n < 1000) | 0.864 | +1.7 | -0.2 | 0.0076 | 0.0106 |
| Avg. daily time in range 70-180 (%) | 393 | -0.077 [-0.481, +0.327] | -0.2529 | -0.37 | 0.708 | not applied (n < 1000) | 0.906 | +1.9 | -0.0 | 0.0055 | 0.0106 |
| Any reading < 54 during wear (0/1) | 393 | -0.242 [-0.699, +0.215] | -0.654 | -1.04 | 0.300 | not applied (n < 1000) | 0.750 | +0.8 | -1.1 | 0.0029 | 0.0106 |
| Time < 54, pooled (%) | 393 | -0.302 [-0.789, +0.186] | -5.969 | -1.21 | 0.226 | not applied (n < 1000) | 0.714 | +0.2 | -1.7 | 0.0067 | 0.0106 |
| Avg. daily time < 54 (%) | 393 | -0.298 [-0.823, +0.227] | -7.083 | -1.11 | 0.266 | not applied (n < 1000) | 0.737 | +0.2 | -1.7 | 0.0004 | 0.0106 |
| Time 54-69, pooled (%) | 393 | +0.251 [-0.165, +0.667] | 1.401 | 1.18 | 0.236 | not applied (n < 1000) | 0.724 | +0.7 | -1.2 | 0.0121 | 0.0106 |
| Avg. daily time 54-69 (%) | 393 | +0.150 [-0.280, +0.580] | 0.8445 | 0.68 | 0.494 | not applied (n < 1000) | 0.838 | +1.5 | -0.4 | 0.0094 | 0.0106 |
| Time < 70, pooled (%) | 393 | +0.149 [-0.283, +0.581] | 0.7427 | 0.68 | 0.500 | not applied (n < 1000) | 0.838 | +1.6 | -0.4 | 0.0096 | 0.0106 |
| Avg. daily time < 70 (%) | 393 | +0.071 [-0.374, +0.515] | 0.3605 | 0.31 | 0.755 | not applied (n < 1000) | 0.918 | +1.9 | -0.0 | 0.0069 | 0.0106 |
| Time 54-250, pooled (%) | 393 | +0.304 [-0.180, +0.789] | 6.003 | 1.23 | 0.218 | not applied (n < 1000) | 0.714 | +0.2 | -1.7 | 0.0070 | 0.0106 |
| Avg. daily time 54-250 (%) | 393 | +0.301 [-0.217, +0.819] | 7.093 | 1.14 | 0.255 | not applied (n < 1000) | 0.737 | +0.2 | -1.7 | 0.0009 | 0.0106 |
| Time 181-250, pooled (%) | 393 | +0.019 [-0.400, +0.439] | 0.06898 | 0.09 | 0.928 | not applied (n < 1000) | 0.975 | +2.0 | +0.1 | 0.0062 | 0.0106 |
| Avg. daily time 181-250 (%) | 393 | +0.036 [-0.386, +0.458] | 0.128 | 0.17 | 0.867 | not applied (n < 1000) | 0.961 | +2.0 | +0.1 | 0.0057 | 0.0106 |
| Time > 180, pooled (%) | 393 | +0.019 [-0.400, +0.438] | 0.06623 | 0.09 | 0.931 | not applied (n < 1000) | 0.975 | +2.0 | +0.1 | 0.0062 | 0.0106 |
| Avg. daily time > 180 (%) | 393 | +0.035 [-0.386, +0.456] | 0.1249 | 0.16 | 0.870 | not applied (n < 1000) | 0.961 | +2.0 | +0.1 | 0.0057 | 0.0106 |
| Nocturnal time > 180 (%) | 393 | +0.346 [-0.152, +0.844] | 1.023 | 1.36 | 0.173 | not applied (n < 1000) | 0.690 | -0.3 | -2.2 | 0.0143 | 0.0106 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 393; events = 68; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 393 | OR 1.015 [0.771, 1.336] | 0.04875 | 0.10 | 0.917 | not applied (n < 1000) | 0.975 | +2.0 | +0.0 | 0.6132 | 0.6172 |
| Mean glucose (mg/dL) | 393 | OR 0.963 [0.735, 1.263] | -0.004947 | -0.27 | 0.787 | not applied (n < 1000) | 0.929 | +1.9 | -0.1 | 0.6087 | 0.6172 |
| GMI (%) | 393 | OR 0.963 [0.735, 1.263] | -0.2068 | -0.27 | 0.787 | not applied (n < 1000) | 0.929 | +1.9 | -0.1 | 0.6087 | 0.6172 |
| Nocturnal mean 00-06h (mg/dL) | 393 | OR 0.951 [0.719, 1.257] | -0.005254 | -0.35 | 0.723 | not applied (n < 1000) | 0.910 | +1.9 | -0.1 | 0.6125 | 0.6172 |
| Glucose SD, pooled (mg/dL) | 393 | OR 1.153 [0.868, 1.533] | 0.06386 | 0.98 | 0.326 | not applied (n < 1000) | 0.770 | +1.0 | -1.0 | 0.6172 | 0.6172 |
| Avg. daily SD (mg/dL) | 393 | OR 1.125 [0.842, 1.502] | 0.0522 | 0.80 | 0.425 | not applied (n < 1000) | 0.827 | +1.4 | -0.6 | 0.6137 | 0.6172 |
| CV (%) | 393 | OR 1.169 [0.882, 1.548] | 0.07595 | 1.09 | 0.277 | not applied (n < 1000) | 0.737 | +0.8 | -1.2 | 0.6214 | 0.6172 |
| Mean / SD ratio | 393 | OR 0.857 [0.640, 1.148] | -0.1541 | -1.04 | 0.300 | not applied (n < 1000) | 0.750 | +0.9 | -1.1 | 0.6209 | 0.6172 |
| Avg. daily mean / SD | 393 | OR 0.896 [0.664, 1.211] | -0.08758 | -0.71 | 0.476 | not applied (n < 1000) | 0.833 | +1.5 | -0.5 | 0.6170 | 0.6172 |
| MAG (mg/dL/h) | 393 | OR 1.585 [1.196, 2.100] | 0.07933 | 3.21 | 0.001** | not applied (n < 1000) | 0.264 | -8.5 | -10.4 | 0.6624 | 0.6172 |
| Avg. daily range (mg/dL) | 393 | OR 1.198 [0.896, 1.603] | 0.01661 | 1.22 | 0.223 | not applied (n < 1000) | 0.714 | +0.5 | -1.5 | 0.6178 | 0.6172 |
| SD of daily means (mg/dL) | 393 | OR 1.208 [0.928, 1.574] | 0.1087 | 1.41 | 0.160 | not applied (n < 1000) | 0.690 | +0.1 | -1.9 | 0.6273 | 0.6172 |
| Time in range 70-180, pooled (%) | 393 | OR 1.077 [0.815, 1.422] | 0.2483 | 0.52 | 0.604 | not applied (n < 1000) | 0.878 | +1.7 | -0.3 | 0.6007 | 0.6172 |
| Avg. daily time in range 70-180 (%) | 393 | OR 1.013 [0.769, 1.333] | 0.04127 | 0.09 | 0.929 | not applied (n < 1000) | 0.975 | +2.0 | +0.0 | 0.6008 | 0.6172 |
| Any reading < 54 during wear (0/1) | 393 | OR 0.918 [0.687, 1.226] | -0.2324 | -0.58 | 0.561 | not applied (n < 1000) | 0.864 | +1.7 | -0.3 | 0.6022 | 0.6172 |
| Time < 54, pooled (%) | 393 | OR 0.893 [0.669, 1.192] | -2.246 | -0.77 | 0.442 | not applied (n < 1000) | 0.828 | +1.3 | -0.7 | 0.6089 | 0.6172 |
| Avg. daily time < 54 (%) | 393 | OR 0.932 [0.708, 1.227] | -1.673 | -0.50 | 0.616 | not applied (n < 1000) | 0.885 | +1.7 | -0.3 | 0.6071 | 0.6172 |
| Time 54-69, pooled (%) | 393 | OR 1.203 [0.926, 1.563] | 1.03 | 1.38 | 0.167 | not applied (n < 1000) | 0.690 | +0.2 | -1.8 | 0.6224 | 0.6172 |
| Avg. daily time 54-69 (%) | 393 | OR 1.135 [0.871, 1.479] | 0.711 | 0.93 | 0.350 | not applied (n < 1000) | 0.787 | +1.2 | -0.8 | 0.6158 | 0.6172 |
| Time < 70, pooled (%) | 393 | OR 1.141 [0.879, 1.481] | 0.6563 | 0.99 | 0.322 | not applied (n < 1000) | 0.770 | +1.1 | -0.9 | 0.6170 | 0.6172 |
| Avg. daily time < 70 (%) | 393 | OR 1.099 [0.845, 1.430] | 0.4826 | 0.71 | 0.480 | not applied (n < 1000) | 0.833 | +1.5 | -0.5 | 0.6132 | 0.6172 |
| Time 54-250, pooled (%) | 393 | OR 1.135 [0.846, 1.523] | 2.497 | 0.84 | 0.399 | not applied (n < 1000) | 0.819 | +1.2 | -0.8 | 0.6072 | 0.6172 |
| Avg. daily time 54-250 (%) | 393 | OR 1.090 [0.821, 1.447] | 2.036 | 0.60 | 0.550 | not applied (n < 1000) | 0.864 | +1.6 | -0.4 | 0.6062 | 0.6172 |
| Time 181-250, pooled (%) | 393 | OR 0.834 [0.626, 1.111] | -0.6456 | -1.24 | 0.214 | not applied (n < 1000) | 0.714 | +0.4 | -1.6 | 0.6152 | 0.6172 |
| Avg. daily time 181-250 (%) | 393 | OR 0.922 [0.698, 1.219] | -0.2874 | -0.57 | 0.570 | not applied (n < 1000) | 0.866 | +1.7 | -0.3 | 0.6126 | 0.6172 |
| Time > 180, pooled (%) | 393 | OR 0.832 [0.625, 1.108] | -0.6526 | -1.26 | 0.209 | not applied (n < 1000) | 0.714 | +0.4 | -1.6 | 0.6156 | 0.6172 |
| Avg. daily time > 180 (%) | 393 | OR 0.920 [0.696, 1.216] | -0.2957 | -0.59 | 0.558 | not applied (n < 1000) | 0.864 | +1.7 | -0.3 | 0.6118 | 0.6172 |
| Nocturnal time > 180 (%) | 393 | OR 1.022 [0.807, 1.292] | 0.06304 | 0.18 | 0.859 | not applied (n < 1000) | 0.961 | +2.0 | -0.0 | 0.6151 | 0.6172 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 384; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 384 | +0.043 [-0.068, +0.153] | 0.1416 | 0.76 | 0.449 | not applied (n < 1000) | 0.833 | +1.2 | +0.0 | 0.0390 | 0.0469 |
| Mean glucose (mg/dL) | 384 | -0.072 [-0.160, +0.016] | -0.009558 | -1.60 | 0.111 | not applied (n < 1000) | 0.690 | -0.7 | -1.8 | 0.0434 | 0.0469 |
| GMI (%) | 384 | -0.072 [-0.160, +0.016] | -0.3996 | -1.60 | 0.111 | not applied (n < 1000) | 0.690 | -0.7 | -1.8 | 0.0434 | 0.0469 |
| Nocturnal mean 00-06h (mg/dL) | 384 | -0.037 [-0.124, +0.049] | -0.003903 | -0.84 | 0.399 | not applied (n < 1000) | 0.819 | +1.3 | +0.1 | 0.0420 | 0.0469 |
| Glucose SD, pooled (mg/dL) | 384 | -0.027 [-0.113, +0.059] | -0.01207 | -0.61 | 0.542 | not applied (n < 1000) | 0.864 | +1.6 | +0.4 | 0.0455 | 0.0469 |
| Avg. daily SD (mg/dL) | 384 | -0.025 [-0.108, +0.058] | -0.01103 | -0.58 | 0.559 | not applied (n < 1000) | 0.864 | +1.7 | +0.5 | 0.0454 | 0.0469 |
| CV (%) | 384 | +0.007 [-0.080, +0.094] | 0.003562 | 0.16 | 0.869 | not applied (n < 1000) | 0.961 | +2.0 | +0.8 | 0.0437 | 0.0469 |
| Mean / SD ratio | 384 | +0.000 [-0.085, +0.085] | 0.0001459 | 0.00 | 0.997 | not applied (n < 1000) | 1.000 | +2.0 | +0.8 | 0.0438 | 0.0469 |
| Avg. daily mean / SD | 384 | -0.010 [-0.093, +0.074] | -0.007703 | -0.22 | 0.822 | not applied (n < 1000) | 0.951 | +2.0 | +0.8 | 0.0432 | 0.0469 |
| MAG (mg/dL/h) | 384 | +0.040 [-0.045, +0.125] | 0.006923 | 0.92 | 0.355 | not applied (n < 1000) | 0.787 | +1.2 | +0.0 | 0.0473 | 0.0469 |
| Avg. daily range (mg/dL) | 384 | -0.034 [-0.121, +0.053] | -0.003126 | -0.77 | 0.441 | not applied (n < 1000) | 0.828 | +1.4 | +0.2 | 0.0456 | 0.0469 |
| SD of daily means (mg/dL) | 384 | +0.046 [-0.048, +0.140] | 0.02622 | 0.96 | 0.339 | not applied (n < 1000) | 0.786 | +0.9 | -0.3 | 0.0412 | 0.0469 |
| Time in range 70-180, pooled (%) | 384 | +0.007 [-0.085, +0.099] | 0.02307 | 0.15 | 0.885 | not applied (n < 1000) | 0.961 | +2.0 | +0.8 | 0.0417 | 0.0469 |
| Avg. daily time in range 70-180 (%) | 384 | +0.002 [-0.091, +0.095] | 0.006857 | 0.04 | 0.965 | not applied (n < 1000) | 0.988 | +2.0 | +0.8 | 0.0420 | 0.0469 |
| Any reading < 54 during wear (0/1) | 384 | +0.052 [-0.056, +0.160] | 0.142 | 0.95 | 0.343 | not applied (n < 1000) | 0.786 | +0.6 | -0.5 | 0.0422 | 0.0469 |
| Time < 54, pooled (%) | 384 | +0.090 [-0.020, +0.200] | 1.779 | 1.60 | 0.110 | not applied (n < 1000) | 0.690 | -2.1 | -3.3 | 0.0477 | 0.0469 |
| Avg. daily time < 54 (%) | 384 | +0.095 [-0.031, +0.220] | 2.287 | 1.48 | 0.139 | not applied (n < 1000) | 0.690 | -2.6 | -3.8 | 0.0493 | 0.0469 |
| Time 54-69, pooled (%) | 384 | +0.082 [-0.018, +0.182] | 0.4595 | 1.61 | 0.107 | not applied (n < 1000) | 0.690 | -1.4 | -2.6 | 0.0457 | 0.0469 |
| Avg. daily time 54-69 (%) | 384 | +0.077 [-0.026, +0.181] | 0.4359 | 1.47 | 0.142 | not applied (n < 1000) | 0.690 | -1.0 | -2.2 | 0.0429 | 0.0469 |
| Time < 70, pooled (%) | 384 | +0.095 [-0.007, +0.198] | 0.4779 | 1.82 | 0.068 | not applied (n < 1000) | 0.690 | -2.6 | -3.8 | 0.0475 | 0.0469 |
| Avg. daily time < 70 (%) | 384 | +0.090 [-0.017, +0.197] | 0.4613 | 1.65 | 0.099 | not applied (n < 1000) | 0.690 | -2.1 | -3.3 | 0.0453 | 0.0469 |
| Time 54-250, pooled (%) | 384 | -0.086 [-0.195, +0.023] | -1.702 | -1.55 | 0.122 | not applied (n < 1000) | 0.690 | -1.8 | -2.9 | 0.0471 | 0.0469 |
| Avg. daily time 54-250 (%) | 384 | -0.090 [-0.211, +0.032] | -2.148 | -1.45 | 0.148 | not applied (n < 1000) | 0.690 | -2.2 | -3.3 | 0.0482 | 0.0469 |
| Time 181-250, pooled (%) | 384 | -0.073 [-0.163, +0.016] | -0.2616 | -1.62 | 0.106 | not applied (n < 1000) | 0.690 | -0.8 | -2.0 | 0.0446 | 0.0469 |
| Avg. daily time 181-250 (%) | 384 | -0.063 [-0.150, +0.024] | -0.223 | -1.41 | 0.157 | not applied (n < 1000) | 0.690 | -0.1 | -1.2 | 0.0452 | 0.0469 |
| Time > 180, pooled (%) | 384 | -0.074 [-0.163, +0.015] | -0.2631 | -1.63 | 0.104 | not applied (n < 1000) | 0.690 | -0.8 | -2.0 | 0.0447 | 0.0469 |
| Avg. daily time > 180 (%) | 384 | -0.064 [-0.151, +0.024] | -0.2246 | -1.43 | 0.154 | not applied (n < 1000) | 0.690 | -0.1 | -1.3 | 0.0453 | 0.0469 |
| Nocturnal time > 180 (%) | 384 | -0.092 [-0.193, +0.009] | -0.2724 | -1.79 | 0.074 | not applied (n < 1000) | 0.690 | -2.1 | -3.3 | 0.0423 | 0.0469 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor temperature, mean (deg C)
*n = 384; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 384 | +0.049 [-0.173, +0.272] | 0.1643 | 0.44 | 0.664 | not applied (n < 1000) | 0.906 | +1.8 | +0.0 | 0.2784 | 0.2836 |
| Mean glucose (mg/dL) | 384 | +0.014 [-0.165, +0.193] | 0.001822 | 0.15 | 0.881 | not applied (n < 1000) | 0.961 | +2.0 | +0.2 | 0.2786 | 0.2836 |
| GMI (%) | 384 | +0.014 [-0.165, +0.193] | 0.07617 | 0.15 | 0.881 | not applied (n < 1000) | 0.961 | +2.0 | +0.2 | 0.2786 | 0.2836 |
| Nocturnal mean 00-06h (mg/dL) | 384 | -0.074 [-0.257, +0.109] | -0.007774 | -0.80 | 0.426 | not applied (n < 1000) | 0.827 | +1.4 | -0.3 | 0.2819 | 0.2836 |
| Glucose SD, pooled (mg/dL) | 384 | -0.209 [-0.395, -0.022] | -0.09404 | -2.19 | 0.029* | not applied (n < 1000) | 0.629 | -2.9 | -4.6 | 0.2894 | 0.2836 |
| Avg. daily SD (mg/dL) | 384 | -0.253 [-0.445, -0.061] | -0.1127 | -2.58 | 0.010** | not applied (n < 1000) | 0.350 | -5.2 | -6.9 | 0.2933 | 0.2836 |
| CV (%) | 384 | -0.208 [-0.392, -0.024] | -0.1015 | -2.21 | 0.027* | not applied (n < 1000) | 0.629 | -2.8 | -4.6 | 0.2873 | 0.2836 |
| Mean / SD ratio | 384 | +0.191 [+0.011, +0.371] | 0.1913 | 2.07 | 0.038* | not applied (n < 1000) | 0.677 | -2.1 | -3.8 | 0.2874 | 0.2836 |
| Avg. daily mean / SD | 384 | +0.232 [+0.050, +0.414] | 0.1861 | 2.49 | 0.013* | not applied (n < 1000) | 0.415 | -4.0 | -5.8 | 0.2903 | 0.2836 |
| MAG (mg/dL/h) | 384 | -0.137 [-0.330, +0.056] | -0.0237 | -1.39 | 0.163 | not applied (n < 1000) | 0.690 | -0.1 | -1.8 | 0.2842 | 0.2836 |
| Avg. daily range (mg/dL) | 384 | -0.270 [-0.458, -0.081] | -0.02477 | -2.80 | 0.005** | not applied (n < 1000) | 0.350 | -6.2 | -8.0 | 0.2979 | 0.2836 |
| SD of daily means (mg/dL) | 384 | +0.149 [-0.028, +0.326] | 0.08508 | 1.65 | 0.099 | not applied (n < 1000) | 0.690 | -0.5 | -2.2 | 0.2844 | 0.2836 |
| Time in range 70-180, pooled (%) | 384 | +0.121 [-0.071, +0.312] | 0.4074 | 1.23 | 0.218 | not applied (n < 1000) | 0.714 | +0.4 | -1.4 | 0.2873 | 0.2836 |
| Avg. daily time in range 70-180 (%) | 384 | +0.082 [-0.113, +0.277] | 0.2693 | 0.82 | 0.410 | not applied (n < 1000) | 0.822 | +1.2 | -0.5 | 0.2842 | 0.2836 |
| Any reading < 54 during wear (0/1) | 384 | -0.041 [-0.246, +0.164] | -0.1117 | -0.39 | 0.694 | not applied (n < 1000) | 0.906 | +1.8 | +0.1 | 0.2816 | 0.2836 |
| Time < 54, pooled (%) | 384 | +0.012 [-0.198, +0.222] | 0.2422 | 0.11 | 0.909 | not applied (n < 1000) | 0.972 | +2.0 | +0.2 | 0.2783 | 0.2836 |
| Avg. daily time < 54 (%) | 384 | +0.015 [-0.208, +0.238] | 0.3578 | 0.13 | 0.896 | not applied (n < 1000) | 0.969 | +2.0 | +0.2 | 0.2758 | 0.2836 |
| Time 54-69, pooled (%) | 384 | -0.147 [-0.342, +0.049] | -0.8235 | -1.47 | 0.141 | not applied (n < 1000) | 0.690 | -0.4 | -2.1 | 0.2838 | 0.2836 |
| Avg. daily time 54-69 (%) | 384 | -0.115 [-0.304, +0.074] | -0.6462 | -1.19 | 0.234 | not applied (n < 1000) | 0.724 | +0.5 | -1.2 | 0.2840 | 0.2836 |
| Time < 70, pooled (%) | 384 | -0.128 [-0.323, +0.068] | -0.6397 | -1.28 | 0.202 | not applied (n < 1000) | 0.714 | +0.2 | -1.6 | 0.2826 | 0.2836 |
| Avg. daily time < 70 (%) | 384 | -0.100 [-0.287, +0.086] | -0.5138 | -1.05 | 0.292 | not applied (n < 1000) | 0.749 | +0.9 | -0.9 | 0.2831 | 0.2836 |
| Time 54-250, pooled (%) | 384 | -0.009 [-0.219, +0.201] | -0.18 | -0.08 | 0.932 | not applied (n < 1000) | 0.975 | +2.0 | +0.2 | 0.2783 | 0.2836 |
| Avg. daily time 54-250 (%) | 384 | -0.011 [-0.235, +0.213] | -0.2556 | -0.09 | 0.926 | not applied (n < 1000) | 0.975 | +2.0 | +0.2 | 0.2759 | 0.2836 |
| Time 181-250, pooled (%) | 384 | -0.038 [-0.231, +0.156] | -0.1339 | -0.38 | 0.703 | not applied (n < 1000) | 0.906 | +1.8 | +0.1 | 0.2809 | 0.2836 |
| Avg. daily time 181-250 (%) | 384 | -0.020 [-0.214, +0.174] | -0.07001 | -0.20 | 0.842 | not applied (n < 1000) | 0.961 | +2.0 | +0.2 | 0.2790 | 0.2836 |
| Time > 180, pooled (%) | 384 | -0.038 [-0.231, +0.155] | -0.1356 | -0.39 | 0.699 | not applied (n < 1000) | 0.906 | +1.8 | +0.1 | 0.2809 | 0.2836 |
| Avg. daily time > 180 (%) | 384 | -0.020 [-0.214, +0.173] | -0.07193 | -0.21 | 0.837 | not applied (n < 1000) | 0.961 | +2.0 | +0.2 | 0.2790 | 0.2836 |
| Nocturnal time > 180 (%) | 384 | +0.098 [-0.074, +0.270] | 0.2889 | 1.11 | 0.266 | not applied (n < 1000) | 0.737 | +1.0 | -0.8 | 0.2828 | 0.2836 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor relative humidity, mean (%)
*n = 384; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 384 | +0.326 [-0.270, +0.922] | 1.084 | 1.07 | 0.284 | not applied (n < 1000) | 0.737 | +0.9 | +0.0 | 0.2439 | 0.2498 |
| Mean glucose (mg/dL) | 384 | +0.230 [-0.344, +0.803] | 0.03061 | 0.79 | 0.432 | not applied (n < 1000) | 0.827 | +1.4 | +0.5 | 0.2403 | 0.2498 |
| GMI (%) | 384 | +0.230 [-0.344, +0.803] | 1.28 | 0.79 | 0.432 | not applied (n < 1000) | 0.827 | +1.4 | +0.5 | 0.2403 | 0.2498 |
| Nocturnal mean 00-06h (mg/dL) | 384 | +0.409 [-0.181, +0.999] | 0.04281 | 1.36 | 0.174 | not applied (n < 1000) | 0.690 | +0.1 | -0.8 | 0.2453 | 0.2498 |
| Glucose SD, pooled (mg/dL) | 384 | -0.020 [-0.632, +0.592] | -0.009056 | -0.06 | 0.949 | not applied (n < 1000) | 0.979 | +2.0 | +1.1 | 0.2460 | 0.2498 |
| Avg. daily SD (mg/dL) | 384 | +0.159 [-0.475, +0.794] | 0.07101 | 0.49 | 0.622 | not applied (n < 1000) | 0.886 | +1.7 | +0.8 | 0.2459 | 0.2498 |
| CV (%) | 384 | -0.111 [-0.742, +0.520] | -0.05416 | -0.34 | 0.730 | not applied (n < 1000) | 0.910 | +1.9 | +1.0 | 0.2447 | 0.2498 |
| Mean / SD ratio | 384 | +0.138 [-0.489, +0.765] | 0.1385 | 0.43 | 0.666 | not applied (n < 1000) | 0.906 | +1.8 | +0.9 | 0.2452 | 0.2498 |
| Avg. daily mean / SD | 384 | -0.152 [-0.813, +0.509] | -0.1217 | -0.45 | 0.653 | not applied (n < 1000) | 0.906 | +1.7 | +0.8 | 0.2464 | 0.2498 |
| MAG (mg/dL/h) | 384 | +0.169 [-0.440, +0.778] | 0.02919 | 0.54 | 0.587 | not applied (n < 1000) | 0.874 | +1.7 | +0.8 | 0.2441 | 0.2498 |
| Avg. daily range (mg/dL) | 384 | +0.116 [-0.546, +0.779] | 0.01068 | 0.34 | 0.731 | not applied (n < 1000) | 0.910 | +1.8 | +1.0 | 0.2422 | 0.2498 |
| SD of daily means (mg/dL) | 384 | +0.018 [-0.576, +0.613] | 0.01054 | 0.06 | 0.951 | not applied (n < 1000) | 0.979 | +2.0 | +1.1 | 0.2463 | 0.2498 |
| Time in range 70-180, pooled (%) | 384 | -0.299 [-0.871, +0.274] | -1.008 | -1.02 | 0.307 | not applied (n < 1000) | 0.755 | +0.9 | +0.0 | 0.2481 | 0.2498 |
| Avg. daily time in range 70-180 (%) | 384 | -0.345 [-0.944, +0.254] | -1.132 | -1.13 | 0.259 | not applied (n < 1000) | 0.737 | +0.6 | -0.3 | 0.2491 | 0.2498 |
| Any reading < 54 during wear (0/1) | 384 | +0.180 [-0.437, +0.796] | 0.488 | 0.57 | 0.568 | not applied (n < 1000) | 0.866 | +1.6 | +0.7 | 0.2456 | 0.2498 |
| Time < 54, pooled (%) | 384 | +0.191 [-0.432, +0.814] | 3.79 | 0.60 | 0.548 | not applied (n < 1000) | 0.864 | +1.6 | +0.7 | 0.2448 | 0.2498 |
| Avg. daily time < 54 (%) | 384 | +0.133 [-0.564, +0.831] | 3.219 | 0.37 | 0.708 | not applied (n < 1000) | 0.906 | +1.8 | +0.9 | 0.2435 | 0.2498 |
| Time 54-69, pooled (%) | 384 | +0.115 [-0.509, +0.739] | 0.6452 | 0.36 | 0.718 | not applied (n < 1000) | 0.908 | +1.8 | +1.0 | 0.2416 | 0.2498 |
| Avg. daily time 54-69 (%) | 384 | +0.012 [-0.619, +0.643] | 0.06582 | 0.04 | 0.971 | not applied (n < 1000) | 0.990 | +2.0 | +1.1 | 0.2432 | 0.2498 |
| Time < 70, pooled (%) | 384 | +0.150 [-0.472, +0.773] | 0.7526 | 0.47 | 0.636 | not applied (n < 1000) | 0.894 | +1.7 | +0.9 | 0.2412 | 0.2498 |
| Avg. daily time < 70 (%) | 384 | +0.039 [-0.592, +0.670] | 0.2 | 0.12 | 0.903 | not applied (n < 1000) | 0.970 | +2.0 | +1.1 | 0.2429 | 0.2498 |
| Time 54-250, pooled (%) | 384 | -0.213 [-0.842, +0.416] | -4.197 | -0.66 | 0.508 | not applied (n < 1000) | 0.838 | +1.5 | +0.6 | 0.2455 | 0.2498 |
| Avg. daily time 54-250 (%) | 384 | -0.161 [-0.871, +0.549] | -3.863 | -0.45 | 0.656 | not applied (n < 1000) | 0.906 | +1.7 | +0.8 | 0.2441 | 0.2498 |
| Time 181-250, pooled (%) | 384 | +0.207 [-0.365, +0.778] | 0.7356 | 0.71 | 0.479 | not applied (n < 1000) | 0.833 | +1.5 | +0.6 | 0.2450 | 0.2498 |
| Avg. daily time 181-250 (%) | 384 | +0.342 [-0.263, +0.947] | 1.211 | 1.11 | 0.268 | not applied (n < 1000) | 0.737 | +0.6 | -0.3 | 0.2452 | 0.2498 |
| Time > 180, pooled (%) | 384 | +0.210 [-0.362, +0.782] | 0.7483 | 0.72 | 0.471 | not applied (n < 1000) | 0.833 | +1.5 | +0.6 | 0.2451 | 0.2498 |
| Avg. daily time > 180 (%) | 384 | +0.346 [-0.259, +0.951] | 1.223 | 1.12 | 0.263 | not applied (n < 1000) | 0.737 | +0.5 | -0.3 | 0.2452 | 0.2498 |
| Nocturnal time > 180 (%) | 384 | -0.266 [-0.843, +0.310] | -0.7879 | -0.91 | 0.365 | not applied (n < 1000) | 0.790 | +1.2 | +0.3 | 0.2458 | 0.2498 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Indoor VOC index, mean
*n = 384; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 384 | -1.482 [-3.177, +0.213] | -4.925 | -1.71 | 0.087 | not applied (n < 1000) | 0.690 | -1.7 | +0.0 | -0.0693 | -0.0705 |
| Mean glucose (mg/dL) | 384 | -1.532 [-3.029, -0.035] | -0.2041 | -2.01 | 0.045* | not applied (n < 1000) | 0.690 | -2.5 | -0.8 | -0.0672 | -0.0705 |
| GMI (%) | 384 | -1.532 [-3.029, -0.035] | -8.531 | -2.01 | 0.045* | not applied (n < 1000) | 0.690 | -2.5 | -0.8 | -0.0672 | -0.0705 |
| Nocturnal mean 00-06h (mg/dL) | 384 | -0.953 [-2.397, +0.491] | -0.09969 | -1.29 | 0.196 | not applied (n < 1000) | 0.714 | +0.3 | +2.0 | -0.0768 | -0.0705 |
| Glucose SD, pooled (mg/dL) | 384 | -1.015 [-2.533, +0.503] | -0.4576 | -1.31 | 0.190 | not applied (n < 1000) | 0.714 | +0.0 | +1.7 | -0.0723 | -0.0705 |
| Avg. daily SD (mg/dL) | 384 | -1.116 [-2.678, +0.446] | -0.4975 | -1.40 | 0.161 | not applied (n < 1000) | 0.690 | -0.4 | +1.3 | -0.0695 | -0.0705 |
| CV (%) | 384 | -0.265 [-1.825, +1.296] | -0.129 | -0.33 | 0.740 | not applied (n < 1000) | 0.910 | +1.9 | +3.6 | -0.0792 | -0.0705 |
| Mean / SD ratio | 384 | +0.353 [-1.217, +1.924] | 0.3543 | 0.44 | 0.659 | not applied (n < 1000) | 0.906 | +1.8 | +3.5 | -0.0776 | -0.0705 |
| Avg. daily mean / SD | 384 | +0.434 [-1.199, +2.067] | 0.3482 | 0.52 | 0.602 | not applied (n < 1000) | 0.878 | +1.6 | +3.3 | -0.0758 | -0.0705 |
| MAG (mg/dL/h) | 384 | +0.935 [-0.701, +2.570] | 0.1615 | 1.12 | 0.263 | not applied (n < 1000) | 0.737 | +0.4 | +2.1 | -0.0801 | -0.0705 |
| Avg. daily range (mg/dL) | 384 | -0.335 [-2.016, +1.347] | -0.03077 | -0.39 | 0.696 | not applied (n < 1000) | 0.906 | +1.8 | +3.5 | -0.0747 | -0.0705 |
| SD of daily means (mg/dL) | 384 | -0.456 [-1.810, +0.897] | -0.2606 | -0.66 | 0.509 | not applied (n < 1000) | 0.838 | +1.6 | +3.3 | -0.0797 | -0.0705 |
| Time in range 70-180, pooled (%) | 384 | +0.198 [-1.350, +1.747] | 0.6695 | 0.25 | 0.802 | not applied (n < 1000) | 0.933 | +1.9 | +3.6 | -0.0811 | -0.0705 |
| Avg. daily time in range 70-180 (%) | 384 | +0.270 [-1.321, +1.861] | 0.8857 | 0.33 | 0.739 | not applied (n < 1000) | 0.910 | +1.9 | +3.6 | -0.0804 | -0.0705 |
| Any reading < 54 during wear (0/1) | 384 | -0.050 [-1.502, +1.402] | -0.1361 | -0.07 | 0.946 | not applied (n < 1000) | 0.979 | +2.0 | +3.7 | -0.0769 | -0.0705 |
| Time < 54, pooled (%) | 384 | +0.674 [-0.747, +2.094] | 13.35 | 0.93 | 0.353 | not applied (n < 1000) | 0.787 | +1.1 | +2.8 | -0.0719 | -0.0705 |
| Avg. daily time < 54 (%) | 384 | +1.054 [-0.261, +2.369] | 25.45 | 1.57 | 0.116 | not applied (n < 1000) | 0.690 | -0.1 | +1.6 | -0.0661 | -0.0705 |
| Time 54-69, pooled (%) | 384 | +0.563 [-0.943, +2.069] | 3.158 | 0.73 | 0.464 | not applied (n < 1000) | 0.833 | +1.4 | +3.1 | -0.0724 | -0.0705 |
| Avg. daily time 54-69 (%) | 384 | +0.595 [-0.835, +2.025] | 3.349 | 0.82 | 0.415 | not applied (n < 1000) | 0.822 | +1.3 | +3.0 | -0.0726 | -0.0705 |
| Time < 70, pooled (%) | 384 | +0.669 [-0.824, +2.163] | 3.356 | 0.88 | 0.380 | not applied (n < 1000) | 0.805 | +1.1 | +2.8 | -0.0704 | -0.0705 |
| Avg. daily time < 70 (%) | 384 | +0.762 [-0.665, +2.190] | 3.902 | 1.05 | 0.295 | not applied (n < 1000) | 0.750 | +0.9 | +2.6 | -0.0698 | -0.0705 |
| Time 54-250, pooled (%) | 384 | -0.566 [-2.040, +0.907] | -11.18 | -0.75 | 0.451 | not applied (n < 1000) | 0.833 | +1.4 | +3.1 | -0.0715 | -0.0705 |
| Avg. daily time 54-250 (%) | 384 | -0.908 [-2.341, +0.526] | -21.73 | -1.24 | 0.214 | not applied (n < 1000) | 0.714 | +0.4 | +2.1 | -0.0666 | -0.0705 |
| Time 181-250, pooled (%) | 384 | -0.660 [-2.204, +0.884] | -2.351 | -0.84 | 0.402 | not applied (n < 1000) | 0.821 | +1.2 | +2.9 | -0.0779 | -0.0705 |
| Avg. daily time 181-250 (%) | 384 | -0.790 [-2.405, +0.825] | -2.798 | -0.96 | 0.338 | not applied (n < 1000) | 0.786 | +0.8 | +2.5 | -0.0769 | -0.0705 |
| Time > 180, pooled (%) | 384 | -0.678 [-2.223, +0.867] | -2.413 | -0.86 | 0.390 | not applied (n < 1000) | 0.818 | +1.1 | +2.8 | -0.0780 | -0.0705 |
| Avg. daily time > 180 (%) | 384 | -0.809 [-2.425, +0.807] | -2.863 | -0.98 | 0.326 | not applied (n < 1000) | 0.770 | +0.7 | +2.4 | -0.0770 | -0.0705 |
| Nocturnal time > 180 (%) | 384 | +0.444 [-0.965, +1.852] | 1.312 | 0.62 | 0.537 | not applied (n < 1000) | 0.863 | +1.6 | +3.3 | -0.0738 | -0.0705 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Steps per wear-day
*n = 344; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 344 | +239.888 [-148.331, +628.106] | 788.7 | 1.21 | 0.226 | not applied (n < 1000) | 0.714 | +0.4 | +0.0 | 0.0777 | 0.0842 |
| Mean glucose (mg/dL) | 344 | -55.982 [-467.079, +355.115] | -7.475 | -0.27 | 0.790 | not applied (n < 1000) | 0.929 | +1.9 | +1.5 | 0.0792 | 0.0842 |
| GMI (%) | 344 | -55.982 [-467.079, +355.115] | -312.5 | -0.27 | 0.790 | not applied (n < 1000) | 0.929 | +1.9 | +1.5 | 0.0792 | 0.0842 |
| Nocturnal mean 00-06h (mg/dL) | 344 | +37.304 [-346.092, +420.701] | 3.886 | 0.19 | 0.849 | not applied (n < 1000) | 0.961 | +2.0 | +1.6 | 0.0785 | 0.0842 |
| Glucose SD, pooled (mg/dL) | 344 | -274.780 [-674.179, +124.620] | -121.6 | -1.35 | 0.178 | not applied (n < 1000) | 0.690 | -0.3 | -0.7 | 0.0862 | 0.0842 |
| Avg. daily SD (mg/dL) | 344 | -318.921 [-703.185, +65.344] | -140.8 | -1.63 | 0.104 | not applied (n < 1000) | 0.690 | -1.1 | -1.5 | 0.0860 | 0.0842 |
| CV (%) | 344 | -254.642 [-616.943, +107.658] | -123.3 | -1.38 | 0.168 | not applied (n < 1000) | 0.690 | +0.0 | -0.4 | 0.0846 | 0.0842 |
| Mean / SD ratio | 344 | +260.635 [-110.127, +631.396] | 260.6 | 1.38 | 0.168 | not applied (n < 1000) | 0.690 | -0.1 | -0.5 | 0.0834 | 0.0842 |
| Avg. daily mean / SD | 344 | +300.903 [-64.524, +666.331] | 244.7 | 1.61 | 0.107 | not applied (n < 1000) | 0.690 | -0.8 | -1.2 | 0.0833 | 0.0842 |
| MAG (mg/dL/h) | 344 | +77.099 [-328.715, +482.913] | 13.15 | 0.37 | 0.710 | not applied (n < 1000) | 0.906 | +1.8 | +1.4 | 0.0725 | 0.0842 |
| Avg. daily range (mg/dL) | 344 | -181.392 [-598.886, +236.102] | -16.54 | -0.85 | 0.394 | not applied (n < 1000) | 0.818 | +1.0 | +0.6 | 0.0769 | 0.0842 |
| SD of daily means (mg/dL) | 344 | +20.875 [-420.886, +462.636] | 11.76 | 0.09 | 0.926 | not applied (n < 1000) | 0.975 | +2.0 | +1.6 | 0.0817 | 0.0842 |
| Time in range 70-180, pooled (%) | 344 | -288.853 [-637.260, +59.555] | -978.3 | -1.62 | 0.104 | not applied (n < 1000) | 0.690 | -0.6 | -1.0 | 0.0792 | 0.0842 |
| Avg. daily time in range 70-180 (%) | 344 | -311.984 [-664.426, +40.457] | -1021 | -1.73 | 0.083 | not applied (n < 1000) | 0.690 | -1.0 | -1.4 | 0.0823 | 0.0842 |
| Any reading < 54 during wear (0/1) | 344 | +54.277 [-288.416, +396.971] | 142.8 | 0.31 | 0.756 | not applied (n < 1000) | 0.918 | +1.9 | +1.5 | 0.0761 | 0.0842 |
| Time < 54, pooled (%) | 344 | +247.835 [-299.506, +795.176] | 4646 | 0.89 | 0.375 | not applied (n < 1000) | 0.799 | +0.2 | -0.2 | 0.0711 | 0.0842 |
| Avg. daily time < 54 (%) | 344 | +360.524 [-188.426, +909.474] | 8156 | 1.29 | 0.198 | not applied (n < 1000) | 0.714 | -2.0 | -2.4 | 0.0853 | 0.0842 |
| Time 54-69, pooled (%) | 344 | +54.553 [-295.092, +404.198] | 300.3 | 0.31 | 0.760 | not applied (n < 1000) | 0.919 | +1.9 | +1.5 | 0.0798 | 0.0842 |
| Avg. daily time 54-69 (%) | 344 | +28.798 [-323.771, +381.366] | 160.6 | 0.16 | 0.873 | not applied (n < 1000) | 0.961 | +2.0 | +1.6 | 0.0795 | 0.0842 |
| Time < 70, pooled (%) | 344 | +111.862 [-277.729, +501.453] | 547.8 | 0.56 | 0.574 | not applied (n < 1000) | 0.868 | +1.6 | +1.2 | 0.0782 | 0.0842 |
| Avg. daily time < 70 (%) | 344 | +106.519 [-289.771, +502.809] | 535.7 | 0.53 | 0.598 | not applied (n < 1000) | 0.878 | +1.7 | +1.3 | 0.0792 | 0.0842 |
| Time 54-250, pooled (%) | 344 | -240.204 [-790.066, +309.658] | -4486 | -0.86 | 0.392 | not applied (n < 1000) | 0.818 | +0.3 | -0.1 | 0.0708 | 0.0842 |
| Avg. daily time 54-250 (%) | 344 | -348.669 [-904.043, +206.705] | -7823 | -1.23 | 0.219 | not applied (n < 1000) | 0.714 | -1.7 | -2.1 | 0.0843 | 0.0842 |
| Time 181-250, pooled (%) | 344 | +227.342 [-138.175, +592.860] | 816.3 | 1.22 | 0.223 | not applied (n < 1000) | 0.714 | +0.4 | +0.0 | 0.0765 | 0.0842 |
| Avg. daily time 181-250 (%) | 344 | +263.797 [-99.830, +627.424] | 931.7 | 1.42 | 0.155 | not applied (n < 1000) | 0.690 | -0.2 | -0.5 | 0.0780 | 0.0842 |
| Time > 180, pooled (%) | 344 | +225.925 [-139.189, +591.038] | 810.5 | 1.21 | 0.225 | not applied (n < 1000) | 0.714 | +0.4 | +0.0 | 0.0765 | 0.0842 |
| Avg. daily time > 180 (%) | 344 | +262.194 [-101.022, +625.410] | 924.8 | 1.41 | 0.157 | not applied (n < 1000) | 0.690 | -0.1 | -0.5 | 0.0780 | 0.0842 |
| Nocturnal time > 180 (%) | 344 | +138.442 [-311.482, +588.367] | 387.6 | 0.60 | 0.546 | not applied (n < 1000) | 0.864 | +1.5 | +1.1 | 0.0827 | 0.0842 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 344; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 344 | +0.531 [-0.811, +1.873] | 1.747 | 0.78 | 0.438 | not applied (n < 1000) | 0.828 | +1.3 | +0.0 | 0.0828 | 0.0916 |
| Mean glucose (mg/dL) | 344 | -0.300 [-1.685, +1.085] | -0.04006 | -0.42 | 0.671 | not applied (n < 1000) | 0.906 | +1.8 | +0.4 | 0.0880 | 0.0916 |
| GMI (%) | 344 | -0.300 [-1.685, +1.085] | -1.675 | -0.42 | 0.671 | not applied (n < 1000) | 0.906 | +1.8 | +0.4 | 0.0880 | 0.0916 |
| Nocturnal mean 00-06h (mg/dL) | 344 | +0.011 [-1.342, +1.364] | 0.001176 | 0.02 | 0.987 | not applied (n < 1000) | 1.000 | +2.0 | +0.7 | 0.0864 | 0.0916 |
| Glucose SD, pooled (mg/dL) | 344 | -0.303 [-1.652, +1.047] | -0.134 | -0.44 | 0.660 | not applied (n < 1000) | 0.906 | +1.8 | +0.4 | 0.0861 | 0.0916 |
| Avg. daily SD (mg/dL) | 344 | -0.594 [-1.860, +0.673] | -0.2621 | -0.92 | 0.358 | not applied (n < 1000) | 0.788 | +1.1 | -0.2 | 0.0857 | 0.0916 |
| CV (%) | 344 | -0.231 [-1.443, +0.981] | -0.1118 | -0.37 | 0.709 | not applied (n < 1000) | 0.906 | +1.9 | +0.5 | 0.0885 | 0.0916 |
| Mean / SD ratio | 344 | +0.263 [-0.986, +1.512] | 0.2633 | 0.41 | 0.679 | not applied (n < 1000) | 0.906 | +1.8 | +0.5 | 0.0870 | 0.0916 |
| Avg. daily mean / SD | 344 | +0.579 [-0.614, +1.771] | 0.4705 | 0.95 | 0.342 | not applied (n < 1000) | 0.786 | +1.1 | -0.2 | 0.0861 | 0.0916 |
| MAG (mg/dL/h) | 344 | +1.055 [-0.305, +2.415] | 0.18 | 1.52 | 0.128 | not applied (n < 1000) | 0.690 | -0.9 | -2.2 | 0.0835 | 0.0916 |
| Avg. daily range (mg/dL) | 344 | -0.118 [-1.483, +1.248] | -0.01074 | -0.17 | 0.866 | not applied (n < 1000) | 0.961 | +2.0 | +0.6 | 0.0810 | 0.0916 |
| SD of daily means (mg/dL) | 344 | +0.653 [-0.844, +2.149] | 0.3679 | 0.85 | 0.393 | not applied (n < 1000) | 0.818 | +0.9 | -0.5 | 0.0926 | 0.0916 |
| Time in range 70-180, pooled (%) | 344 | -1.783 [-2.957, -0.609] | -6.039 | -2.98 | 0.003** | not applied (n < 1000) | 0.286 | -6.7 | -8.0 | 0.1047 | 0.0916 |
| Avg. daily time in range 70-180 (%) | 344 | -1.812 [-2.990, -0.635] | -5.931 | -3.02 | 0.003** | not applied (n < 1000) | 0.286 | -6.9 | -8.2 | 0.1075 | 0.0916 |
| Any reading < 54 during wear (0/1) | 344 | +0.313 [-0.882, +1.509] | 0.8244 | 0.51 | 0.608 | not applied (n < 1000) | 0.879 | +1.7 | +0.4 | 0.0834 | 0.0916 |
| Time < 54, pooled (%) | 344 | +1.021 [-0.832, +2.874] | 19.13 | 1.08 | 0.280 | not applied (n < 1000) | 0.737 | -0.7 | -2.0 | 0.0864 | 0.0916 |
| Avg. daily time < 54 (%) | 344 | +1.336 [-0.549, +3.221] | 30.23 | 1.39 | 0.165 | not applied (n < 1000) | 0.690 | -2.8 | -4.1 | 0.0979 | 0.0916 |
| Time 54-69, pooled (%) | 344 | +0.850 [-0.373, +2.073] | 4.678 | 1.36 | 0.173 | not applied (n < 1000) | 0.690 | +0.1 | -1.2 | 0.0938 | 0.0916 |
| Avg. daily time 54-69 (%) | 344 | +0.667 [-0.574, +1.908] | 3.721 | 1.05 | 0.292 | not applied (n < 1000) | 0.749 | +0.8 | -0.5 | 0.0910 | 0.0916 |
| Time < 70, pooled (%) | 344 | +1.013 [-0.313, +2.339] | 4.96 | 1.50 | 0.134 | not applied (n < 1000) | 0.690 | -0.7 | -2.0 | 0.0953 | 0.0916 |
| Avg. daily time < 70 (%) | 344 | +0.896 [-0.458, +2.250] | 4.505 | 1.30 | 0.195 | not applied (n < 1000) | 0.714 | -0.1 | -1.4 | 0.0934 | 0.0916 |
| Time 54-250, pooled (%) | 344 | -1.024 [-2.868, +0.821] | -19.11 | -1.09 | 0.277 | not applied (n < 1000) | 0.737 | -0.7 | -2.1 | 0.0864 | 0.0916 |
| Avg. daily time 54-250 (%) | 344 | -1.333 [-3.203, +0.537] | -29.92 | -1.40 | 0.162 | not applied (n < 1000) | 0.690 | -2.8 | -4.1 | 0.0977 | 0.0916 |
| Time 181-250, pooled (%) | 344 | +1.162 [-0.054, +2.378] | 4.171 | 1.87 | 0.061 | not applied (n < 1000) | 0.690 | -1.7 | -3.0 | 0.0921 | 0.0916 |
| Avg. daily time 181-250 (%) | 344 | +1.332 [+0.125, +2.539] | 4.704 | 2.16 | 0.031* | not applied (n < 1000) | 0.629 | -2.8 | -4.1 | 0.0964 | 0.0916 |
| Time > 180, pooled (%) | 344 | +1.162 [-0.052, +2.376] | 4.168 | 1.88 | 0.061 | not applied (n < 1000) | 0.690 | -1.7 | -3.0 | 0.0921 | 0.0916 |
| Avg. daily time > 180 (%) | 344 | +1.332 [+0.127, +2.537] | 4.698 | 2.17 | 0.030* | not applied (n < 1000) | 0.629 | -2.8 | -4.1 | 0.0964 | 0.0916 |
| Nocturnal time > 180 (%) | 344 | +0.767 [-0.753, +2.287] | 2.147 | 0.99 | 0.323 | not applied (n < 1000) | 0.770 | +0.5 | -0.8 | 0.0916 | 0.0916 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 346; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 346 | +0.104 [-0.703, +0.911] | 0.3423 | 0.25 | 0.800 | not applied (n < 1000) | 0.933 | +1.9 | +0.0 | 0.0630 | 0.0735 |
| Mean glucose (mg/dL) | 346 | -0.004 [-0.767, +0.759] | -0.0005292 | -0.01 | 0.992 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.0650 | 0.0735 |
| GMI (%) | 346 | -0.004 [-0.767, +0.759] | -0.02213 | -0.01 | 0.992 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.0650 | 0.0735 |
| Nocturnal mean 00-06h (mg/dL) | 346 | +0.269 [-0.501, +1.038] | 0.02806 | 0.68 | 0.494 | not applied (n < 1000) | 0.838 | +1.5 | -0.4 | 0.0670 | 0.0735 |
| Glucose SD, pooled (mg/dL) | 346 | +0.063 [-0.732, +0.858] | 0.02744 | 0.15 | 0.877 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | 0.0681 | 0.0735 |
| Avg. daily SD (mg/dL) | 346 | +0.068 [-0.705, +0.840] | 0.02946 | 0.17 | 0.864 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | 0.0698 | 0.0735 |
| CV (%) | 346 | +0.034 [-0.664, +0.733] | 0.01638 | 0.10 | 0.924 | not applied (n < 1000) | 0.975 | +2.0 | +0.1 | 0.0673 | 0.0735 |
| Mean / SD ratio | 346 | +0.006 [-0.679, +0.690] | 0.005541 | 0.02 | 0.987 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.0681 | 0.0735 |
| Avg. daily mean / SD | 346 | -0.023 [-0.692, +0.646] | -0.0181 | -0.07 | 0.947 | not applied (n < 1000) | 0.979 | +2.0 | +0.1 | 0.0704 | 0.0735 |
| MAG (mg/dL/h) | 346 | +0.621 [-0.172, +1.414] | 0.1061 | 1.53 | 0.125 | not applied (n < 1000) | 0.690 | -0.9 | -2.9 | 0.0733 | 0.0735 |
| Avg. daily range (mg/dL) | 346 | -0.045 [-0.824, +0.734] | -0.004067 | -0.11 | 0.910 | not applied (n < 1000) | 0.972 | +2.0 | +0.1 | 0.0670 | 0.0735 |
| SD of daily means (mg/dL) | 346 | +0.715 [-0.051, +1.482] | 0.4033 | 1.83 | 0.067 | not applied (n < 1000) | 0.690 | -2.1 | -4.0 | 0.0687 | 0.0735 |
| Time in range 70-180, pooled (%) | 346 | -0.222 [-0.975, +0.532] | -0.7486 | -0.58 | 0.565 | not applied (n < 1000) | 0.865 | +1.6 | -0.3 | 0.0731 | 0.0735 |
| Avg. daily time in range 70-180 (%) | 346 | -0.393 [-1.095, +0.308] | -1.285 | -1.10 | 0.272 | not applied (n < 1000) | 0.737 | +0.8 | -1.1 | 0.0752 | 0.0735 |
| Any reading < 54 during wear (0/1) | 346 | +0.119 [-0.545, +0.783] | 0.3138 | 0.35 | 0.725 | not applied (n < 1000) | 0.910 | +1.9 | -0.0 | 0.0675 | 0.0735 |
| Time < 54, pooled (%) | 346 | +0.618 [+0.014, +1.223] | 11.62 | 2.00 | 0.045* | not applied (n < 1000) | 0.690 | -0.9 | -2.9 | 0.0730 | 0.0735 |
| Avg. daily time < 54 (%) | 346 | +0.309 [-0.434, +1.052] | 7.005 | 0.81 | 0.415 | not applied (n < 1000) | 0.822 | +1.3 | -0.7 | 0.0734 | 0.0735 |
| Time 54-69, pooled (%) | 346 | -0.019 [-0.683, +0.644] | -0.1069 | -0.06 | 0.954 | not applied (n < 1000) | 0.979 | +2.0 | +0.1 | 0.0691 | 0.0735 |
| Avg. daily time 54-69 (%) | 346 | -0.064 [-0.741, +0.613] | -0.3576 | -0.19 | 0.853 | not applied (n < 1000) | 0.961 | +2.0 | +0.0 | 0.0687 | 0.0735 |
| Time < 70, pooled (%) | 346 | +0.141 [-0.520, +0.803] | 0.6938 | 0.42 | 0.675 | not applied (n < 1000) | 0.906 | +1.8 | -0.1 | 0.0681 | 0.0735 |
| Avg. daily time < 70 (%) | 346 | +0.012 [-0.660, +0.683] | 0.05947 | 0.03 | 0.973 | not applied (n < 1000) | 0.990 | +2.0 | +0.1 | 0.0687 | 0.0735 |
| Time 54-250, pooled (%) | 346 | -0.544 [-1.180, +0.092] | -10.19 | -1.68 | 0.093 | not applied (n < 1000) | 0.690 | -0.3 | -2.2 | 0.0723 | 0.0735 |
| Avg. daily time 54-250 (%) | 346 | -0.213 [-1.055, +0.628] | -4.796 | -0.50 | 0.620 | not applied (n < 1000) | 0.886 | +1.6 | -0.3 | 0.0722 | 0.0735 |
| Time 181-250, pooled (%) | 346 | +0.147 [-0.642, +0.937] | 0.5283 | 0.37 | 0.715 | not applied (n < 1000) | 0.908 | +1.8 | -0.1 | 0.0707 | 0.0735 |
| Avg. daily time 181-250 (%) | 346 | +0.431 [-0.318, +1.181] | 1.524 | 1.13 | 0.259 | not applied (n < 1000) | 0.737 | +0.5 | -1.4 | 0.0756 | 0.0735 |
| Time > 180, pooled (%) | 346 | +0.134 [-0.657, +0.925] | 0.4799 | 0.33 | 0.740 | not applied (n < 1000) | 0.910 | +1.9 | -0.1 | 0.0705 | 0.0735 |
| Avg. daily time > 180 (%) | 346 | +0.416 [-0.335, +1.168] | 1.469 | 1.09 | 0.278 | not applied (n < 1000) | 0.737 | +0.6 | -1.3 | 0.0750 | 0.0735 |
| Nocturnal time > 180 (%) | 346 | +0.702 [-0.113, +1.517] | 1.97 | 1.69 | 0.092 | not applied (n < 1000) | 0.690 | -1.6 | -3.5 | 0.0760 | 0.0735 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Total sleep time per night (min)
*n = 349; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 349 | -11.426 [-18.212, -4.641] | -37.71 | -3.30 | 9.7e-04*** | not applied (n < 1000) | 0.264 | -9.3 | +0.0 | 0.0050 | -0.0232 |
| Mean glucose (mg/dL) | 349 | -4.678 [-10.732, +1.376] | -0.6242 | -1.51 | 0.130 | not applied (n < 1000) | 0.690 | -0.0 | +9.3 | -0.0245 | -0.0232 |
| GMI (%) | 349 | -4.678 [-10.732, +1.376] | -26.09 | -1.51 | 0.130 | not applied (n < 1000) | 0.690 | -0.0 | +9.3 | -0.0245 | -0.0232 |
| Nocturnal mean 00-06h (mg/dL) | 349 | -5.904 [-12.437, +0.630] | -0.6121 | -1.77 | 0.077 | not applied (n < 1000) | 0.690 | -1.0 | +8.3 | -0.0158 | -0.0232 |
| Glucose SD, pooled (mg/dL) | 349 | +2.371 [-4.291, +9.034] | 1.047 | 0.70 | 0.485 | not applied (n < 1000) | 0.838 | +1.5 | +10.8 | -0.0329 | -0.0232 |
| Avg. daily SD (mg/dL) | 349 | +2.370 [-4.502, +9.243] | 1.037 | 0.68 | 0.499 | not applied (n < 1000) | 0.838 | +1.5 | +10.8 | -0.0304 | -0.0232 |
| CV (%) | 349 | +4.308 [-2.305, +10.921] | 2.076 | 1.28 | 0.202 | not applied (n < 1000) | 0.714 | +0.3 | +9.6 | -0.0298 | -0.0232 |
| Mean / SD ratio | 349 | -4.181 [-10.718, +2.356] | -4.174 | -1.25 | 0.210 | not applied (n < 1000) | 0.714 | +0.4 | +9.7 | -0.0302 | -0.0232 |
| Avg. daily mean / SD | 349 | -3.170 [-9.866, +3.527] | -2.55 | -0.93 | 0.354 | not applied (n < 1000) | 0.787 | +1.1 | +10.4 | -0.0300 | -0.0232 |
| MAG (mg/dL/h) | 349 | -4.958 [-11.754, +1.837] | -0.841 | -1.43 | 0.153 | not applied (n < 1000) | 0.690 | -0.2 | +9.1 | -0.0200 | -0.0232 |
| Avg. daily range (mg/dL) | 349 | +4.113 [-3.234, +11.460] | 0.3728 | 1.10 | 0.273 | not applied (n < 1000) | 0.737 | +0.4 | +9.7 | -0.0265 | -0.0232 |
| SD of daily means (mg/dL) | 349 | +0.687 [-5.630, +7.005] | 0.3901 | 0.21 | 0.831 | not applied (n < 1000) | 0.958 | +2.0 | +11.3 | -0.0338 | -0.0232 |
| Time in range 70-180, pooled (%) | 349 | -3.111 [-9.980, +3.759] | -10.53 | -0.89 | 0.375 | not applied (n < 1000) | 0.799 | +1.1 | +10.4 | -0.0248 | -0.0232 |
| Avg. daily time in range 70-180 (%) | 349 | -3.811 [-10.705, +3.082] | -12.5 | -1.08 | 0.279 | not applied (n < 1000) | 0.737 | +0.6 | +9.9 | -0.0221 | -0.0232 |
| Any reading < 54 during wear (0/1) | 349 | +2.020 [-3.929, +7.970] | 5.278 | 0.67 | 0.506 | not applied (n < 1000) | 0.838 | +1.6 | +10.9 | -0.0274 | -0.0232 |
| Time < 54, pooled (%) | 349 | +1.604 [-4.266, +7.475] | 30.23 | 0.54 | 0.592 | not applied (n < 1000) | 0.876 | +1.8 | +11.1 | -0.0273 | -0.0232 |
| Avg. daily time < 54 (%) | 349 | +3.620 [-1.645, +8.885] | 82.14 | 1.35 | 0.178 | not applied (n < 1000) | 0.690 | +0.8 | +10.1 | -0.0258 | -0.0232 |
| Time 54-69, pooled (%) | 349 | +8.540 [+2.317, +14.763] | 47.27 | 2.69 | 0.007** | not applied (n < 1000) | 0.350 | -4.8 | +4.5 | -0.0089 | -0.0232 |
| Avg. daily time 54-69 (%) | 349 | +8.684 [+2.185, +15.183] | 48.07 | 2.62 | 0.009** | not applied (n < 1000) | 0.350 | -5.0 | +4.4 | -0.0087 | -0.0232 |
| Time < 70, pooled (%) | 349 | +7.940 [+1.913, +13.968] | 39.1 | 2.58 | 0.010** | not applied (n < 1000) | 0.350 | -3.9 | +5.4 | -0.0130 | -0.0232 |
| Avg. daily time < 70 (%) | 349 | +8.574 [+2.204, +14.944] | 42.89 | 2.64 | 0.008** | not applied (n < 1000) | 0.350 | -4.8 | +4.5 | -0.0094 | -0.0232 |
| Time 54-250, pooled (%) | 349 | -1.212 [-7.176, +4.752] | -22.75 | -0.40 | 0.690 | not applied (n < 1000) | 0.906 | +1.9 | +11.2 | -0.0274 | -0.0232 |
| Avg. daily time 54-250 (%) | 349 | -3.086 [-8.500, +2.327] | -69.46 | -1.12 | 0.264 | not applied (n < 1000) | 0.737 | +1.1 | +10.4 | -0.0282 | -0.0232 |
| Time 181-250, pooled (%) | 349 | -2.282 [-9.128, +4.564] | -8.115 | -0.65 | 0.514 | not applied (n < 1000) | 0.838 | +1.5 | +10.8 | -0.0305 | -0.0232 |
| Avg. daily time 181-250 (%) | 349 | -1.767 [-8.313, +4.779] | -6.24 | -0.53 | 0.597 | not applied (n < 1000) | 0.878 | +1.7 | +11.0 | -0.0279 | -0.0232 |
| Time > 180, pooled (%) | 349 | -2.351 [-9.198, +4.497] | -8.35 | -0.67 | 0.501 | not applied (n < 1000) | 0.838 | +1.5 | +10.8 | -0.0306 | -0.0232 |
| Avg. daily time > 180 (%) | 349 | -1.843 [-8.391, +4.705] | -6.499 | -0.55 | 0.581 | not applied (n < 1000) | 0.873 | +1.7 | +11.0 | -0.0280 | -0.0232 |
| Nocturnal time > 180 (%) | 349 | -6.084 [-13.665, +1.497] | -17.14 | -1.57 | 0.116 | not applied (n < 1000) | 0.690 | -1.2 | +8.1 | -0.0255 | -0.0232 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Garmin stress score, mean (0-100)
*n = 346; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 346 | +0.480 [-1.453, +2.414] | 1.578 | 0.49 | 0.626 | not applied (n < 1000) | 0.886 | +1.7 | +0.0 | 0.0188 | 0.0341 |
| Mean glucose (mg/dL) | 346 | +0.916 [-0.853, +2.684] | 0.1225 | 1.01 | 0.310 | not applied (n < 1000) | 0.755 | +0.9 | -0.8 | 0.0342 | 0.0341 |
| GMI (%) | 346 | +0.916 [-0.853, +2.684] | 5.123 | 1.01 | 0.310 | not applied (n < 1000) | 0.755 | +0.9 | -0.8 | 0.0342 | 0.0341 |
| Nocturnal mean 00-06h (mg/dL) | 346 | +1.274 [-0.527, +3.074] | 0.1331 | 1.39 | 0.166 | not applied (n < 1000) | 0.690 | -0.1 | -1.8 | 0.0359 | 0.0341 |
| Glucose SD, pooled (mg/dL) | 346 | +1.142 [-0.759, +3.043] | 0.5004 | 1.18 | 0.239 | not applied (n < 1000) | 0.726 | +0.3 | -1.5 | 0.0335 | 0.0341 |
| Avg. daily SD (mg/dL) | 346 | +1.081 [-0.800, +2.961] | 0.4712 | 1.13 | 0.260 | not applied (n < 1000) | 0.737 | +0.4 | -1.3 | 0.0369 | 0.0341 |
| CV (%) | 346 | +0.679 [-1.117, +2.475] | 0.3262 | 0.74 | 0.459 | not applied (n < 1000) | 0.833 | +1.4 | -0.3 | 0.0297 | 0.0341 |
| Mean / SD ratio | 346 | -0.656 [-2.454, +1.142] | -0.644 | -0.72 | 0.475 | not applied (n < 1000) | 0.833 | +1.4 | -0.3 | 0.0307 | 0.0341 |
| Avg. daily mean / SD | 346 | -0.750 [-2.565, +1.064] | -0.5947 | -0.81 | 0.418 | not applied (n < 1000) | 0.823 | +1.2 | -0.5 | 0.0346 | 0.0341 |
| MAG (mg/dL/h) | 346 | +0.528 [-1.328, +2.385] | 0.09035 | 0.56 | 0.577 | not applied (n < 1000) | 0.870 | +1.6 | -0.1 | 0.0296 | 0.0341 |
| Avg. daily range (mg/dL) | 346 | +0.643 [-1.221, +2.508] | 0.05813 | 0.68 | 0.499 | not applied (n < 1000) | 0.838 | +1.4 | -0.3 | 0.0312 | 0.0341 |
| SD of daily means (mg/dL) | 346 | +1.731 [+0.013, +3.448] | 0.9758 | 1.98 | 0.048* | not applied (n < 1000) | 0.690 | -2.1 | -3.8 | 0.0353 | 0.0341 |
| Time in range 70-180, pooled (%) | 346 | -1.523 [-3.292, +0.247] | -5.145 | -1.69 | 0.092 | not applied (n < 1000) | 0.690 | -1.2 | -2.9 | 0.0401 | 0.0341 |
| Avg. daily time in range 70-180 (%) | 346 | -1.887 [-3.616, -0.159] | -6.164 | -2.14 | 0.032* | not applied (n < 1000) | 0.634 | -2.9 | -4.6 | 0.0486 | 0.0341 |
| Any reading < 54 during wear (0/1) | 346 | +0.000 [-1.601, +1.602] | 0.0009634 | 0.00 | 1.000 | not applied (n < 1000) | 1.000 | +2.0 | +0.3 | 0.0295 | 0.0341 |
| Time < 54, pooled (%) | 346 | +0.329 [-1.158, +1.816] | 6.182 | 0.43 | 0.664 | not applied (n < 1000) | 0.906 | +1.9 | +0.1 | 0.0314 | 0.0341 |
| Avg. daily time < 54 (%) | 346 | +0.271 [-1.347, +1.889] | 6.149 | 0.33 | 0.743 | not applied (n < 1000) | 0.910 | +1.9 | +0.2 | 0.0312 | 0.0341 |
| Time 54-69, pooled (%) | 346 | +0.228 [-1.498, +1.955] | 1.259 | 0.26 | 0.795 | not applied (n < 1000) | 0.933 | +1.9 | +0.2 | 0.0307 | 0.0341 |
| Avg. daily time 54-69 (%) | 346 | -0.071 [-1.816, +1.675] | -0.3944 | -0.08 | 0.937 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | 0.0317 | 0.0341 |
| Time < 70, pooled (%) | 346 | +0.286 [-1.387, +1.959] | 1.404 | 0.34 | 0.737 | not applied (n < 1000) | 0.910 | +1.9 | +0.2 | 0.0305 | 0.0341 |
| Avg. daily time < 70 (%) | 346 | -0.003 [-1.699, +1.694] | -0.01274 | -0.00 | 0.998 | not applied (n < 1000) | 1.000 | +2.0 | +0.3 | 0.0314 | 0.0341 |
| Time 54-250, pooled (%) | 346 | -0.297 [-1.786, +1.192] | -5.561 | -0.39 | 0.696 | not applied (n < 1000) | 0.906 | +1.9 | +0.2 | 0.0316 | 0.0341 |
| Avg. daily time 54-250 (%) | 346 | -0.229 [-1.853, +1.395] | -5.148 | -0.28 | 0.782 | not applied (n < 1000) | 0.929 | +1.9 | +0.2 | 0.0315 | 0.0341 |
| Time 181-250, pooled (%) | 346 | +1.422 [-0.394, +3.237] | 5.102 | 1.53 | 0.125 | not applied (n < 1000) | 0.690 | -0.8 | -2.5 | 0.0375 | 0.0341 |
| Avg. daily time 181-250 (%) | 346 | +2.048 [+0.301, +3.794] | 7.235 | 2.30 | 0.022* | not applied (n < 1000) | 0.575 | -3.7 | -5.5 | 0.0493 | 0.0341 |
| Time > 180, pooled (%) | 346 | +1.415 [-0.400, +3.229] | 5.072 | 1.53 | 0.127 | not applied (n < 1000) | 0.690 | -0.7 | -2.5 | 0.0373 | 0.0341 |
| Avg. daily time > 180 (%) | 346 | +2.039 [+0.294, +3.784] | 7.195 | 2.29 | 0.022* | not applied (n < 1000) | 0.575 | -3.7 | -5.4 | 0.0490 | 0.0341 |
| Nocturnal time > 180 (%) | 346 | +2.030 [+0.312, +3.748] | 5.697 | 2.32 | 0.021* | not applied (n < 1000) | 0.575 | -3.3 | -5.0 | 0.0393 | 0.0341 |

Skipped: Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

### Population: Non-healthy group (T2D non-insulin + T2D insulin)

#### MoCA total score (0-30)
*n = 61; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 61 | +0.428 [-0.398, +1.255] | 1.187 | 1.02 | 0.310 | not applied (n < 1000) | 0.915 | +0.8 | +0.0 | -0.5248 | -0.5888 |
| Mean glucose (mg/dL) | 61 | -0.515 [-1.279, +0.249] | -0.07101 | -1.32 | 0.187 | not applied (n < 1000) | 0.915 | -0.2 | -1.0 | -0.6505 | -0.5888 |
| GMI (%) | 61 | -0.515 [-1.279, +0.249] | -2.968 | -1.32 | 0.187 | not applied (n < 1000) | 0.915 | -0.2 | -1.0 | -0.6505 | -0.5888 |
| Nocturnal mean 00-06h (mg/dL) | 61 | -0.605 [-1.478, +0.268] | -0.05842 | -1.36 | 0.175 | not applied (n < 1000) | 0.915 | -1.0 | -1.8 | -0.6898 | -0.5888 |
| Glucose SD, pooled (mg/dL) | 61 | -0.273 [-1.329, +0.784] | -0.08574 | -0.51 | 0.613 | not applied (n < 1000) | 0.915 | +1.5 | +0.8 | -0.6622 | -0.5888 |
| Avg. daily SD (mg/dL) | 61 | +0.102 [-1.064, +1.269] | 0.03205 | 0.17 | 0.864 | not applied (n < 1000) | 0.976 | +1.9 | +1.2 | -0.7082 | -0.5888 |
| CV (%) | 61 | -0.097 [-1.204, +1.011] | -0.03548 | -0.17 | 0.864 | not applied (n < 1000) | 0.976 | +1.9 | +1.2 | -0.6955 | -0.5888 |
| Mean / SD ratio | 61 | +0.053 [-1.013, +1.118] | 0.03843 | 0.10 | 0.923 | not applied (n < 1000) | 0.980 | +2.0 | +1.2 | -0.6855 | -0.5888 |
| Avg. daily mean / SD | 61 | -0.241 [-1.361, +0.880] | -0.1236 | -0.42 | 0.673 | not applied (n < 1000) | 0.915 | +1.6 | +0.9 | -0.7046 | -0.5888 |
| MAG (mg/dL/h) | 61 | -0.137 [-1.092, +0.819] | -0.02235 | -0.28 | 0.779 | not applied (n < 1000) | 0.943 | +1.9 | +1.1 | -0.6788 | -0.5888 |
| Avg. daily range (mg/dL) | 61 | +0.296 [-0.775, +1.367] | 0.0228 | 0.54 | 0.588 | not applied (n < 1000) | 0.915 | +1.4 | +0.7 | -0.6809 | -0.5888 |
| SD of daily means (mg/dL) | 61 | -0.348 [-1.287, +0.592] | -0.1394 | -0.73 | 0.468 | not applied (n < 1000) | 0.915 | +1.1 | +0.3 | -0.7067 | -0.5888 |
| Time in range 70-180, pooled (%) | 61 | +0.194 [-0.617, +1.004] | 0.602 | 0.47 | 0.640 | not applied (n < 1000) | 0.915 | +1.7 | +0.9 | -0.6450 | -0.5888 |
| Avg. daily time in range 70-180 (%) | 61 | -0.465 [-1.327, +0.397] | -1.375 | -1.06 | 0.291 | not applied (n < 1000) | 0.915 | +0.4 | -0.4 | -0.5889 | -0.5888 |
| Time 54-69, pooled (%) | 61 | +0.294 [-0.555, +1.142] | 1.472 | 0.68 | 0.498 | not applied (n < 1000) | 0.915 | +1.3 | +0.5 | -0.6144 | -0.5888 |
| Avg. daily time 54-69 (%) | 61 | +0.434 [-0.279, +1.146] | 2.31 | 1.19 | 0.233 | not applied (n < 1000) | 0.915 | +0.5 | -0.3 | -0.5821 | -0.5888 |
| Time < 70, pooled (%) | 61 | +0.179 [-0.663, +1.022] | 0.7862 | 0.42 | 0.677 | not applied (n < 1000) | 0.915 | +1.8 | +1.0 | -0.6202 | -0.5888 |
| Avg. daily time < 70 (%) | 61 | +0.454 [-0.312, +1.219] | 2.324 | 1.16 | 0.245 | not applied (n < 1000) | 0.915 | +0.3 | -0.4 | -0.5891 | -0.5888 |
| Time 54-250, pooled (%) | 61 | +0.426 [-1.166, +2.018] | 5.626 | 0.52 | 0.600 | not applied (n < 1000) | 0.915 | +0.8 | -0.0 | -0.7816 | -0.5888 |
| Avg. daily time 54-250 (%) | 61 | +0.068 [-1.274, +1.411] | 2.188 | 0.10 | 0.921 | not applied (n < 1000) | 0.980 | +2.0 | +1.2 | -0.6424 | -0.5888 |
| Time 181-250, pooled (%) | 61 | -0.383 [-1.368, +0.603] | -1.435 | -0.76 | 0.447 | not applied (n < 1000) | 0.915 | +0.9 | +0.2 | -0.6478 | -0.5888 |
| Avg. daily time 181-250 (%) | 61 | +0.269 [-0.603, +1.141] | 0.9835 | 0.60 | 0.546 | not applied (n < 1000) | 0.915 | +1.5 | +0.7 | -0.6412 | -0.5888 |
| Time > 180, pooled (%) | 61 | -0.410 [-1.385, +0.565] | -1.524 | -0.82 | 0.410 | not applied (n < 1000) | 0.915 | +0.8 | -0.0 | -0.6440 | -0.5888 |
| Avg. daily time > 180 (%) | 61 | +0.221 [-0.678, +1.120] | 0.7997 | 0.48 | 0.630 | not applied (n < 1000) | 0.915 | +1.7 | +0.9 | -0.6493 | -0.5888 |

Skipped: Any reading < 54 during wear (0/1) (fewer than 30 participants with any time in band); Time < 54, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time < 54 (%) (fewer than 30 participants with any time in band); Nocturnal time > 180 (%) (fewer than 30 participants with any time in band); Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Cognitive impairment (MoCA < 26)
_no models_ (reference model failed in this cohort: LinAlgError)

#### MoCA memory index score (0-15)
*n = 61; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 61 | +0.118 [-0.718, +0.954] | 0.3268 | 0.28 | 0.782 | not applied (n < 1000) | 0.943 | +1.9 | +0.0 | -0.6845 | -0.6112 |
| Mean glucose (mg/dL) | 61 | -0.232 [-1.038, +0.573] | -0.03205 | -0.57 | 0.572 | not applied (n < 1000) | 0.915 | +1.5 | -0.4 | -0.6439 | -0.6112 |
| GMI (%) | 61 | -0.232 [-1.038, +0.573] | -1.34 | -0.57 | 0.572 | not applied (n < 1000) | 0.915 | +1.5 | -0.4 | -0.6439 | -0.6112 |
| Nocturnal mean 00-06h (mg/dL) | 61 | -0.241 [-1.004, +0.522] | -0.02332 | -0.62 | 0.535 | not applied (n < 1000) | 0.915 | +1.4 | -0.4 | -0.6249 | -0.6112 |
| Glucose SD, pooled (mg/dL) | 61 | -0.243 [-1.131, +0.644] | -0.0766 | -0.54 | 0.591 | not applied (n < 1000) | 0.915 | +1.6 | -0.3 | -0.6134 | -0.6112 |
| Avg. daily SD (mg/dL) | 61 | +0.035 [-0.871, +0.941] | 0.01106 | 0.08 | 0.939 | not applied (n < 1000) | 0.980 | +2.0 | +0.1 | -0.6958 | -0.6112 |
| CV (%) | 61 | -0.142 [-1.053, +0.768] | -0.05237 | -0.31 | 0.759 | not applied (n < 1000) | 0.943 | +1.9 | -0.0 | -0.6410 | -0.6112 |
| Mean / SD ratio | 61 | +0.211 [-0.694, +1.117] | 0.1543 | 0.46 | 0.647 | not applied (n < 1000) | 0.915 | +1.7 | -0.2 | -0.6498 | -0.6112 |
| Avg. daily mean / SD | 61 | -0.042 [-0.971, +0.888] | -0.02149 | -0.09 | 0.930 | not applied (n < 1000) | 0.980 | +2.0 | +0.1 | -0.7143 | -0.6112 |
| MAG (mg/dL/h) | 61 | +0.224 [-0.351, +0.799] | 0.03665 | 0.76 | 0.444 | not applied (n < 1000) | 0.915 | +1.6 | -0.3 | -0.7027 | -0.6112 |
| Avg. daily range (mg/dL) | 61 | +0.105 [-0.749, +0.959] | 0.008122 | 0.24 | 0.809 | not applied (n < 1000) | 0.943 | +1.9 | +0.0 | -0.6888 | -0.6112 |
| SD of daily means (mg/dL) | 61 | -0.507 [-1.292, +0.278] | -0.2033 | -1.27 | 0.205 | not applied (n < 1000) | 0.915 | -0.3 | -2.2 | -0.5894 | -0.6112 |
| Time in range 70-180, pooled (%) | 61 | +0.258 [-0.639, +1.155] | 0.8032 | 0.56 | 0.573 | not applied (n < 1000) | 0.915 | +1.4 | -0.5 | -0.6855 | -0.6112 |
| Avg. daily time in range 70-180 (%) | 61 | -0.118 [-1.095, +0.858] | -0.3501 | -0.24 | 0.812 | not applied (n < 1000) | 0.943 | +1.9 | -0.0 | -0.6783 | -0.6112 |
| Time 54-69, pooled (%) | 61 | +0.276 [-0.428, +0.981] | 1.385 | 0.77 | 0.442 | not applied (n < 1000) | 0.915 | +1.3 | -0.6 | -0.6703 | -0.6112 |
| Avg. daily time 54-69 (%) | 61 | +0.463 [-0.120, +1.046] | 2.466 | 1.56 | 0.120 | not applied (n < 1000) | 0.915 | -0.0 | -1.9 | -0.6093 | -0.6112 |
| Time < 70, pooled (%) | 61 | +0.207 [-0.498, +0.912] | 0.9069 | 0.57 | 0.565 | not applied (n < 1000) | 0.915 | +1.6 | -0.3 | -0.6673 | -0.6112 |
| Avg. daily time < 70 (%) | 61 | +0.517 [-0.078, +1.112] | 2.648 | 1.70 | 0.089 | not applied (n < 1000) | 0.915 | -0.6 | -2.5 | -0.5992 | -0.6112 |
| Time 54-250, pooled (%) | 61 | +0.481 [-1.335, +2.297] | 6.356 | 0.52 | 0.604 | not applied (n < 1000) | 0.915 | +0.1 | -1.8 | -0.7988 | -0.6112 |
| Avg. daily time 54-250 (%) | 61 | +0.312 [-2.064, +2.688] | 9.986 | 0.26 | 0.797 | not applied (n < 1000) | 0.943 | +1.1 | -0.8 | -0.8544 | -0.6112 |
| Time 181-250, pooled (%) | 61 | -0.439 [-1.398, +0.520] | -1.647 | -0.90 | 0.370 | not applied (n < 1000) | 0.915 | +0.3 | -1.6 | -0.6399 | -0.6112 |
| Avg. daily time 181-250 (%) | 61 | -0.169 [-1.214, +0.876] | -0.6179 | -0.32 | 0.752 | not applied (n < 1000) | 0.943 | +1.8 | -0.1 | -0.6978 | -0.6112 |
| Time > 180, pooled (%) | 61 | -0.518 [-1.565, +0.529] | -1.926 | -0.97 | 0.332 | not applied (n < 1000) | 0.915 | -0.4 | -2.3 | -0.6469 | -0.6112 |
| Avg. daily time > 180 (%) | 61 | -0.262 [-1.441, +0.917] | -0.9474 | -0.44 | 0.663 | not applied (n < 1000) | 0.915 | +1.4 | -0.5 | -0.7130 | -0.6112 |

Skipped: Any reading < 54 during wear (0/1) (fewer than 30 participants with any time in band); Time < 54, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time < 54 (%) (fewer than 30 participants with any time in band); Nocturnal time > 180 (%) (fewer than 30 participants with any time in band); Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### CES-D-10 depressive symptoms (0-30)
*n = 61; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 61 | -0.631 [-2.284, +1.022] | -1.749 | -0.75 | 0.454 | not applied (n < 1000) | 0.915 | +1.3 | +0.0 | -0.6099 | -0.4879 |
| Mean glucose (mg/dL) | 61 | +0.391 [-0.821, +1.602] | 0.05391 | 0.63 | 0.527 | not applied (n < 1000) | 0.915 | +1.7 | +0.4 | -0.4944 | -0.4879 |
| GMI (%) | 61 | +0.391 [-0.821, +1.602] | 2.254 | 0.63 | 0.527 | not applied (n < 1000) | 0.915 | +1.7 | +0.4 | -0.4944 | -0.4879 |
| Nocturnal mean 00-06h (mg/dL) | 61 | +0.997 [-0.495, +2.489] | 0.09628 | 1.31 | 0.190 | not applied (n < 1000) | 0.915 | -0.2 | -1.5 | -0.4695 | -0.4879 |
| Glucose SD, pooled (mg/dL) | 61 | +0.541 [-1.625, +2.707] | 0.1701 | 0.49 | 0.625 | not applied (n < 1000) | 0.915 | +1.5 | +0.2 | -0.5814 | -0.4879 |
| Avg. daily SD (mg/dL) | 61 | +1.079 [-0.992, +3.151] | 0.3386 | 1.02 | 0.307 | not applied (n < 1000) | 0.915 | +0.2 | -1.1 | -0.5665 | -0.4879 |
| CV (%) | 61 | +0.328 [-1.744, +2.399] | 0.1204 | 0.31 | 0.757 | not applied (n < 1000) | 0.943 | +1.8 | +0.5 | -0.5610 | -0.4879 |
| Mean / SD ratio | 61 | -0.367 [-2.215, +1.480] | -0.2682 | -0.39 | 0.697 | not applied (n < 1000) | 0.929 | +1.8 | +0.5 | -0.5394 | -0.4879 |
| Avg. daily mean / SD | 61 | -0.807 [-2.662, +1.049] | -0.4137 | -0.85 | 0.394 | not applied (n < 1000) | 0.915 | +0.9 | -0.4 | -0.5071 | -0.4879 |
| MAG (mg/dL/h) | 61 | +0.679 [-1.349, +2.708] | 0.111 | 0.66 | 0.511 | not applied (n < 1000) | 0.915 | +1.1 | -0.2 | -0.5088 | -0.4879 |
| Avg. daily range (mg/dL) | 61 | +0.846 [-1.196, +2.887] | 0.0652 | 0.81 | 0.417 | not applied (n < 1000) | 0.915 | +0.7 | -0.6 | -0.5723 | -0.4879 |
| SD of daily means (mg/dL) | 61 | -0.463 [-2.626, +1.700] | -0.1856 | -0.42 | 0.675 | not applied (n < 1000) | 0.915 | +1.6 | +0.3 | -0.5730 | -0.4879 |
| Time in range 70-180, pooled (%) | 61 | +0.247 [-1.535, +2.029] | 0.7689 | 0.27 | 0.786 | not applied (n < 1000) | 0.943 | +1.9 | +0.6 | -0.5863 | -0.4879 |
| Avg. daily time in range 70-180 (%) | 61 | -0.112 [-2.317, +2.092] | -0.3328 | -0.10 | 0.920 | not applied (n < 1000) | 0.980 | +2.0 | +0.7 | -0.7192 | -0.4879 |
| Time 54-69, pooled (%) | 61 | -0.656 [-2.779, +1.467] | -3.288 | -0.61 | 0.545 | not applied (n < 1000) | 0.915 | +1.1 | -0.2 | -0.5885 | -0.4879 |
| Avg. daily time 54-69 (%) | 61 | -0.303 [-2.848, +2.241] | -1.616 | -0.23 | 0.815 | not applied (n < 1000) | 0.943 | +1.8 | +0.5 | -0.7189 | -0.4879 |
| Time < 70, pooled (%) | 61 | -0.834 [-2.681, +1.013] | -3.659 | -0.89 | 0.376 | not applied (n < 1000) | 0.915 | +0.5 | -0.8 | -0.5219 | -0.4879 |
| Avg. daily time < 70 (%) | 61 | -0.384 [-2.800, +2.032] | -1.968 | -0.31 | 0.755 | not applied (n < 1000) | 0.943 | +1.7 | +0.4 | -0.6960 | -0.4879 |
| Time 54-250, pooled (%) | 61 | +0.807 [-0.235, +1.848] | 10.66 | 1.52 | 0.129 | not applied (n < 1000) | 0.915 | +0.8 | -0.5 | -0.4544 | -0.4879 |
| Avg. daily time 54-250 (%) | 61 | +0.484 [-1.060, +2.027] | 15.5 | 0.61 | 0.539 | not applied (n < 1000) | 0.915 | +1.5 | +0.2 | -0.4888 | -0.4879 |
| Time 181-250, pooled (%) | 61 | +0.423 [-1.340, +2.187] | 1.588 | 0.47 | 0.638 | not applied (n < 1000) | 0.915 | +1.6 | +0.4 | -0.5724 | -0.4879 |
| Avg. daily time 181-250 (%) | 61 | +0.444 [-1.410, +2.298] | 1.625 | 0.47 | 0.639 | not applied (n < 1000) | 0.915 | +1.6 | +0.4 | -0.6126 | -0.4879 |
| Time > 180, pooled (%) | 61 | +0.427 [-1.298, +2.152] | 1.587 | 0.49 | 0.628 | not applied (n < 1000) | 0.915 | +1.6 | +0.4 | -0.5713 | -0.4879 |
| Avg. daily time > 180 (%) | 61 | +0.445 [-1.363, +2.254] | 1.61 | 0.48 | 0.629 | not applied (n < 1000) | 0.915 | +1.6 | +0.3 | -0.6098 | -0.4879 |

Skipped: Any reading < 54 during wear (0/1) (fewer than 30 participants with any time in band); Time < 54, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time < 54 (%) (fewer than 30 participants with any time in band); Nocturnal time > 180 (%) (fewer than 30 participants with any time in band); Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
_no models_ (sample too small (< 60 participants or < 15 events))

#### Indoor PM2.5, log(1 + mean ug/m3)
_no models_ (no data)

#### Indoor temperature, mean (deg C)
_no models_ (no data)

#### Indoor relative humidity, mean (%)
_no models_ (no data)

#### Indoor VOC index, mean
_no models_ (no data)

#### Steps per wear-day
_no models_ (no data)

#### Brisk-cadence minutes per day (>= 100 steps/min)
_no models_ (no data)

#### Resting heart-rate proxy (daily 5th pct, bpm)
_no models_ (no data)

#### Total sleep time per night (min)
*n = 60; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 60 | -5.677 [-27.020, +15.665] | -16.75 | -0.52 | 0.602 | not applied (n < 1000) | 0.915 | +1.8 | +0.0 | -1.1485 | -1.1001 |
| Mean glucose (mg/dL) | 60 | -22.640 [-56.614, +11.334] | -3.113 | -1.31 | 0.192 | not applied (n < 1000) | 0.915 | -2.8 | -4.5 | -0.9597 | -1.1001 |
| GMI (%) | 60 | -22.640 [-56.614, +11.334] | -130.2 | -1.31 | 0.192 | not applied (n < 1000) | 0.915 | -2.8 | -4.5 | -0.9597 | -1.1001 |
| Nocturnal mean 00-06h (mg/dL) | 60 | -19.037 [-47.820, +9.747] | -1.846 | -1.30 | 0.195 | not applied (n < 1000) | 0.915 | -1.3 | -3.0 | -0.9580 | -1.1001 |
| Glucose SD, pooled (mg/dL) | 60 | -8.742 [-44.212, +26.728] | -2.747 | -0.48 | 0.629 | not applied (n < 1000) | 0.915 | +1.5 | -0.3 | -1.5465 | -1.1001 |
| Avg. daily SD (mg/dL) | 60 | -9.500 [-47.699, +28.698] | -2.973 | -0.49 | 0.626 | not applied (n < 1000) | 0.915 | +1.4 | -0.3 | -1.5298 | -1.1001 |
| CV (%) | 60 | +0.882 [-34.028, +35.792] | 0.3226 | 0.05 | 0.961 | not applied (n < 1000) | 0.990 | +2.0 | +0.2 | -1.5233 | -1.1001 |
| Mean / SD ratio | 60 | -0.439 [-34.936, +34.058] | -0.3193 | -0.02 | 0.980 | not applied (n < 1000) | 0.990 | +2.0 | +0.2 | -1.6053 | -1.1001 |
| Avg. daily mean / SD | 60 | +1.498 [-33.314, +36.310] | 0.7631 | 0.08 | 0.933 | not applied (n < 1000) | 0.980 | +2.0 | +0.2 | -1.4449 | -1.1001 |
| MAG (mg/dL/h) | 60 | -23.223 [-53.962, +7.516] | -3.77 | -1.48 | 0.139 | not applied (n < 1000) | 0.915 | -2.3 | -4.0 | -1.1225 | -1.1001 |
| Avg. daily range (mg/dL) | 60 | -16.337 [-50.809, +18.134] | -1.249 | -0.93 | 0.353 | not applied (n < 1000) | 0.915 | +0.1 | -1.7 | -1.4249 | -1.1001 |
| SD of daily means (mg/dL) | 60 | -0.322 [-22.941, +22.298] | -0.129 | -0.03 | 0.978 | not applied (n < 1000) | 0.990 | +2.0 | +0.2 | -1.1937 | -1.1001 |
| Time in range 70-180, pooled (%) | 60 | -0.076 [-30.182, +30.030] | -0.2378 | -0.00 | 0.996 | not applied (n < 1000) | 0.996 | +2.0 | +0.2 | -1.3320 | -1.1001 |
| Avg. daily time in range 70-180 (%) | 60 | +1.691 [-33.964, +37.345] | 5.001 | 0.09 | 0.926 | not applied (n < 1000) | 0.980 | +2.0 | +0.2 | -1.4305 | -1.1001 |
| Time 54-69, pooled (%) | 60 | +19.500 [-5.978, +44.977] | 97.38 | 1.50 | 0.134 | not applied (n < 1000) | 0.915 | -1.4 | -3.1 | -0.9389 | -1.1001 |
| Avg. daily time 54-69 (%) | 60 | +16.020 [-11.613, +43.654] | 84.95 | 1.14 | 0.256 | not applied (n < 1000) | 0.915 | -0.3 | -2.0 | -1.0711 | -1.1001 |
| Time < 70, pooled (%) | 60 | +16.809 [-7.372, +40.990] | 73.5 | 1.36 | 0.173 | not applied (n < 1000) | 0.915 | -0.4 | -2.2 | -0.9566 | -1.1001 |
| Avg. daily time < 70 (%) | 60 | +14.534 [-11.570, +40.638] | 74.12 | 1.09 | 0.275 | not applied (n < 1000) | 0.915 | +0.1 | -1.6 | -1.0769 | -1.1001 |
| Time 54-250, pooled (%) | 60 | +4.539 [-12.982, +22.060] | 59.56 | 0.51 | 0.612 | not applied (n < 1000) | 0.915 | +1.8 | +0.1 | -1.1206 | -1.1001 |
| Avg. daily time 54-250 (%) | 60 | +10.738 [-8.917, +30.393] | 341.4 | 1.07 | 0.284 | not applied (n < 1000) | 0.915 | +1.0 | -0.8 | -1.0884 | -1.1001 |
| Time 181-250, pooled (%) | 60 | -14.615 [-44.312, +15.082] | -54.69 | -0.96 | 0.335 | not applied (n < 1000) | 0.915 | +0.3 | -1.5 | -1.2558 | -1.1001 |
| Avg. daily time 181-250 (%) | 60 | -13.433 [-46.537, +19.672] | -48.97 | -0.80 | 0.426 | not applied (n < 1000) | 0.915 | +0.6 | -1.1 | -1.3186 | -1.1001 |
| Time > 180, pooled (%) | 60 | -14.992 [-44.305, +14.322] | -55.6 | -1.00 | 0.316 | not applied (n < 1000) | 0.915 | +0.2 | -1.6 | -1.2550 | -1.1001 |
| Avg. daily time > 180 (%) | 60 | -13.816 [-46.218, +18.586] | -49.78 | -0.84 | 0.403 | not applied (n < 1000) | 0.915 | +0.5 | -1.2 | -1.3128 | -1.1001 |

Skipped: Any reading < 54 during wear (0/1) (fewer than 30 participants with any time in band); Time < 54, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time < 54 (%) (fewer than 30 participants with any time in band); Nocturnal time > 180 (%) (fewer than 30 participants with any time in band); Any reading > 250 during wear (0/1) (fewer than 30 participants with any time in band); Time > 250, pooled (%) (fewer than 30 participants with any time in band); Avg. daily time > 250 (%) (fewer than 30 participants with any time in band)

#### Garmin stress score, mean (0-100)
_no models_ (no data)


---

## Cohort: Within 54-250: no reading < 54 and none > 250

### Population: Total analysis base

#### MoCA total score (0-30)
*n = 890; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 890 | -0.279 [-0.482, -0.076] | -0.658 | -2.69 | 0.007** | not applied (n < 1000) | 0.087 | -6.4 | +0.0 | 0.0844 | 0.0785 |
| Mean glucose (mg/dL) | 890 | -0.378 [-0.584, -0.172] | -0.03126 | -3.60 | 3.1e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -14.5 | -8.1 | 0.0936 | 0.0785 |
| GMI (%) | 890 | -0.378 [-0.584, -0.172] | -1.307 | -3.60 | 3.1e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -14.5 | -8.1 | 0.0936 | 0.0785 |
| Nocturnal mean 00-06h (mg/dL) | 890 | -0.368 [-0.573, -0.163] | -0.02704 | -3.51 | 4.4e-04*** | not applied (n < 1000) | 0.013 (q<0.05) | -13.3 | -6.9 | 0.0913 | 0.0785 |
| Glucose SD, pooled (mg/dL) | 890 | -0.206 [-0.399, -0.013] | -0.04966 | -2.09 | 0.037* | not applied (n < 1000) | 0.199 | -2.8 | +3.6 | 0.0817 | 0.0785 |
| Avg. daily SD (mg/dL) | 890 | -0.197 [-0.388, -0.006] | -0.04839 | -2.02 | 0.043* | not applied (n < 1000) | 0.200 | -2.4 | +4.0 | 0.0811 | 0.0785 |
| CV (%) | 890 | -0.034 [-0.230, +0.162] | -0.01181 | -0.34 | 0.733 | not applied (n < 1000) | 0.934 | +1.9 | +8.3 | 0.0756 | 0.0785 |
| Mean / SD ratio | 890 | +0.000 [-0.200, +0.201] | 0.0004073 | 0.00 | 0.996 | not applied (n < 1000) | 1.000 | +2.0 | +8.4 | 0.0751 | 0.0785 |
| Avg. daily mean / SD | 890 | +0.020 [-0.172, +0.211] | 0.0136 | 0.20 | 0.841 | not applied (n < 1000) | 0.954 | +2.0 | +8.4 | 0.0747 | 0.0785 |
| MAG (mg/dL/h) | 890 | -0.063 [-0.230, +0.104] | -0.009413 | -0.74 | 0.461 | not applied (n < 1000) | 0.807 | +1.5 | +7.9 | 0.0764 | 0.0785 |
| Avg. daily range (mg/dL) | 890 | -0.158 [-0.341, +0.024] | -0.009319 | -1.70 | 0.089 | not applied (n < 1000) | 0.315 | -1.0 | +5.4 | 0.0790 | 0.0785 |
| SD of daily means (mg/dL) | 890 | -0.183 [-0.370, +0.005] | -0.07756 | -1.91 | 0.056 | not applied (n < 1000) | 0.222 | -1.9 | +4.5 | 0.0800 | 0.0785 |
| Time in range 70-180, pooled (%) | 890 | +0.228 [+0.007, +0.448] | 0.06711 | 2.03 | 0.043* | not applied (n < 1000) | 0.199 | -4.0 | +2.4 | 0.0832 | 0.0785 |
| Avg. daily time in range 70-180 (%) | 890 | +0.225 [+0.008, +0.443] | 0.06785 | 2.03 | 0.042* | not applied (n < 1000) | 0.199 | -3.9 | +2.5 | 0.0830 | 0.0785 |
| Time 54-69, pooled (%) | 890 | +0.117 [-0.029, +0.263] | 0.2444 | 1.57 | 0.116 | not applied (n < 1000) | 0.380 | +0.4 | +6.8 | 0.0780 | 0.0785 |
| Avg. daily time 54-69 (%) | 890 | +0.104 [-0.042, +0.250] | 0.2093 | 1.39 | 0.164 | not applied (n < 1000) | 0.484 | +0.7 | +7.1 | 0.0775 | 0.0785 |
| Time < 70, pooled (%) | 890 | +0.117 [-0.029, +0.263] | 0.2444 | 1.57 | 0.116 | not applied (n < 1000) | 0.380 | +0.4 | +6.8 | 0.0780 | 0.0785 |
| Avg. daily time < 70 (%) | 890 | +0.104 [-0.042, +0.250] | 0.2093 | 1.39 | 0.164 | not applied (n < 1000) | 0.484 | +0.7 | +7.1 | 0.0775 | 0.0785 |
| Time 181-250, pooled (%) | 890 | -0.243 [-0.464, -0.022] | -0.07096 | -2.16 | 0.031* | not applied (n < 1000) | 0.199 | -4.9 | +1.6 | 0.0841 | 0.0785 |
| Avg. daily time 181-250 (%) | 890 | -0.240 [-0.457, -0.022] | -0.07141 | -2.16 | 0.031* | not applied (n < 1000) | 0.199 | -4.6 | +1.8 | 0.0838 | 0.0785 |
| Time > 180, pooled (%) | 890 | -0.243 [-0.464, -0.022] | -0.07096 | -2.16 | 0.031* | not applied (n < 1000) | 0.199 | -4.9 | +1.6 | 0.0841 | 0.0785 |
| Avg. daily time > 180 (%) | 890 | -0.240 [-0.457, -0.022] | -0.07141 | -2.16 | 0.031* | not applied (n < 1000) | 0.199 | -4.6 | +1.8 | 0.0838 | 0.0785 |
| Nocturnal time > 180 (%) | 890 | -0.230 [-0.447, -0.014] | -0.06166 | -2.08 | 0.037* | not applied (n < 1000) | 0.199 | -4.1 | +2.3 | 0.0820 | 0.0785 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 890; events = 336; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 890 | OR 1.172 [1.008, 1.363] | 0.3746 | 2.07 | 0.039* | not applied (n < 1000) | 0.199 | -2.3 | +0.0 | 0.6573 | 0.6558 |
| Mean glucose (mg/dL) | 890 | OR 1.310 [1.130, 1.518] | 0.0223 | 3.57 | 3.5e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -10.9 | -8.6 | 0.6664 | 0.6558 |
| GMI (%) | 890 | OR 1.310 [1.130, 1.518] | 0.9322 | 3.57 | 3.5e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -10.9 | -8.6 | 0.6664 | 0.6558 |
| Nocturnal mean 00-06h (mg/dL) | 890 | OR 1.327 [1.142, 1.541] | 0.02077 | 3.70 | 2.1e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -11.9 | -9.6 | 0.6680 | 0.6558 |
| Glucose SD, pooled (mg/dL) | 890 | OR 1.167 [1.007, 1.352] | 0.03728 | 2.05 | 0.040* | not applied (n < 1000) | 0.199 | -2.2 | +0.1 | 0.6527 | 0.6558 |
| Avg. daily SD (mg/dL) | 890 | OR 1.164 [1.005, 1.349] | 0.03739 | 2.03 | 0.043* | not applied (n < 1000) | 0.199 | -2.1 | +0.2 | 0.6527 | 0.6558 |
| CV (%) | 890 | OR 1.032 [0.893, 1.193] | 0.01102 | 0.43 | 0.668 | not applied (n < 1000) | 0.911 | +1.8 | +4.2 | 0.6508 | 0.6558 |
| Mean / SD ratio | 890 | OR 0.990 [0.856, 1.146] | -0.008747 | -0.14 | 0.892 | not applied (n < 1000) | 0.991 | +2.0 | +4.3 | 0.6500 | 0.6558 |
| Avg. daily mean / SD | 890 | OR 0.963 [0.832, 1.115] | -0.02597 | -0.50 | 0.617 | not applied (n < 1000) | 0.871 | +1.7 | +4.1 | 0.6511 | 0.6558 |
| MAG (mg/dL/h) | 890 | OR 1.072 [0.928, 1.237] | 0.01036 | 0.95 | 0.344 | not applied (n < 1000) | 0.668 | +1.1 | +3.4 | 0.6558 | 0.6558 |
| Avg. daily range (mg/dL) | 890 | OR 1.136 [0.983, 1.313] | 0.007499 | 1.72 | 0.085 | not applied (n < 1000) | 0.304 | -1.0 | +1.4 | 0.6528 | 0.6558 |
| SD of daily means (mg/dL) | 890 | OR 1.150 [0.996, 1.328] | 0.05927 | 1.90 | 0.057 | not applied (n < 1000) | 0.224 | -1.6 | +0.7 | 0.6550 | 0.6558 |
| Time in range 70-180, pooled (%) | 890 | OR 0.868 [0.751, 1.003] | -0.04177 | -1.92 | 0.054 | not applied (n < 1000) | 0.222 | -1.7 | +0.6 | 0.6543 | 0.6558 |
| Avg. daily time in range 70-180 (%) | 890 | OR 0.861 [0.745, 0.994] | -0.04517 | -2.04 | 0.041* | not applied (n < 1000) | 0.199 | -2.2 | +0.2 | 0.6542 | 0.6558 |
| Time 54-69, pooled (%) | 890 | OR 0.911 [0.778, 1.068] | -0.1942 | -1.15 | 0.250 | not applied (n < 1000) | 0.583 | +0.5 | +2.9 | 0.6548 | 0.6558 |
| Avg. daily time 54-69 (%) | 890 | OR 0.923 [0.790, 1.079] | -0.1617 | -1.01 | 0.314 | not applied (n < 1000) | 0.634 | +0.9 | +3.2 | 0.6545 | 0.6558 |
| Time < 70, pooled (%) | 890 | OR 0.911 [0.778, 1.068] | -0.1942 | -1.15 | 0.250 | not applied (n < 1000) | 0.583 | +0.5 | +2.9 | 0.6548 | 0.6558 |
| Avg. daily time < 70 (%) | 890 | OR 0.923 [0.790, 1.079] | -0.1617 | -1.01 | 0.314 | not applied (n < 1000) | 0.634 | +0.9 | +3.2 | 0.6545 | 0.6558 |
| Time 181-250, pooled (%) | 890 | OR 1.166 [1.009, 1.347] | 0.04476 | 2.08 | 0.038* | not applied (n < 1000) | 0.199 | -2.3 | +0.0 | 0.6551 | 0.6558 |
| Avg. daily time 181-250 (%) | 890 | OR 1.174 [1.016, 1.357] | 0.04788 | 2.18 | 0.029* | not applied (n < 1000) | 0.199 | -2.8 | -0.4 | 0.6553 | 0.6558 |
| Time > 180, pooled (%) | 890 | OR 1.166 [1.009, 1.347] | 0.04476 | 2.08 | 0.038* | not applied (n < 1000) | 0.199 | -2.3 | +0.0 | 0.6551 | 0.6558 |
| Avg. daily time > 180 (%) | 890 | OR 1.174 [1.016, 1.357] | 0.04788 | 2.18 | 0.029* | not applied (n < 1000) | 0.199 | -2.8 | -0.4 | 0.6553 | 0.6558 |
| Nocturnal time > 180 (%) | 890 | OR 1.167 [1.006, 1.355] | 0.04146 | 2.03 | 0.042* | not applied (n < 1000) | 0.199 | -2.3 | +0.1 | 0.6561 | 0.6558 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 890; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 890 | -0.020 [-0.204, +0.164] | -0.0468 | -0.21 | 0.832 | not applied (n < 1000) | 0.950 | +2.0 | +0.0 | 0.0305 | 0.0328 |
| Mean glucose (mg/dL) | 890 | -0.221 [-0.443, +0.001] | -0.01829 | -1.95 | 0.051 | not applied (n < 1000) | 0.215 | -4.5 | -6.5 | 0.0369 | 0.0328 |
| GMI (%) | 890 | -0.221 [-0.443, +0.001] | -0.7648 | -1.95 | 0.051 | not applied (n < 1000) | 0.215 | -4.5 | -6.5 | 0.0369 | 0.0328 |
| Nocturnal mean 00-06h (mg/dL) | 890 | -0.259 [-0.469, -0.049] | -0.01903 | -2.42 | 0.016* | not applied (n < 1000) | 0.148 | -6.7 | -8.7 | 0.0392 | 0.0328 |
| Glucose SD, pooled (mg/dL) | 890 | -0.007 [-0.188, +0.174] | -0.001623 | -0.07 | 0.942 | not applied (n < 1000) | 0.993 | +2.0 | +0.0 | 0.0305 | 0.0328 |
| Avg. daily SD (mg/dL) | 890 | -0.020 [-0.199, +0.160] | -0.00486 | -0.22 | 0.829 | not applied (n < 1000) | 0.950 | +1.9 | -0.0 | 0.0306 | 0.0328 |
| CV (%) | 890 | +0.102 [-0.077, +0.280] | 0.03521 | 1.11 | 0.265 | not applied (n < 1000) | 0.604 | +0.6 | -1.3 | 0.0327 | 0.0328 |
| Mean / SD ratio | 890 | -0.117 [-0.307, +0.074] | -0.1009 | -1.20 | 0.230 | not applied (n < 1000) | 0.562 | +0.2 | -1.8 | 0.0331 | 0.0328 |
| Avg. daily mean / SD | 890 | -0.068 [-0.245, +0.109] | -0.04747 | -0.76 | 0.449 | not applied (n < 1000) | 0.800 | +1.4 | -0.6 | 0.0317 | 0.0328 |
| MAG (mg/dL/h) | 890 | +0.013 [-0.143, +0.169] | 0.001957 | 0.16 | 0.870 | not applied (n < 1000) | 0.972 | +2.0 | +0.0 | 0.0301 | 0.0328 |
| Avg. daily range (mg/dL) | 890 | -0.019 [-0.186, +0.149] | -0.001091 | -0.22 | 0.828 | not applied (n < 1000) | 0.950 | +2.0 | +0.0 | 0.0305 | 0.0328 |
| SD of daily means (mg/dL) | 890 | -0.056 [-0.224, +0.113] | -0.02361 | -0.65 | 0.518 | not applied (n < 1000) | 0.836 | +1.6 | -0.4 | 0.0282 | 0.0328 |
| Time in range 70-180, pooled (%) | 890 | +0.153 [-0.099, +0.405] | 0.04506 | 1.19 | 0.234 | not applied (n < 1000) | 0.566 | -1.1 | -3.1 | 0.0337 | 0.0328 |
| Avg. daily time in range 70-180 (%) | 890 | +0.151 [-0.101, +0.403] | 0.04549 | 1.17 | 0.241 | not applied (n < 1000) | 0.570 | -1.1 | -3.0 | 0.0336 | 0.0328 |
| Time 54-69, pooled (%) | 890 | +0.055 [-0.063, +0.173] | 0.1147 | 0.91 | 0.362 | not applied (n < 1000) | 0.672 | +1.6 | -0.4 | 0.0330 | 0.0328 |
| Avg. daily time 54-69 (%) | 890 | +0.057 [-0.064, +0.179] | 0.1158 | 0.93 | 0.355 | not applied (n < 1000) | 0.672 | +1.5 | -0.4 | 0.0328 | 0.0328 |
| Time < 70, pooled (%) | 890 | +0.055 [-0.063, +0.173] | 0.1147 | 0.91 | 0.362 | not applied (n < 1000) | 0.672 | +1.6 | -0.4 | 0.0330 | 0.0328 |
| Avg. daily time < 70 (%) | 890 | +0.057 [-0.064, +0.179] | 0.1158 | 0.93 | 0.355 | not applied (n < 1000) | 0.672 | +1.5 | -0.4 | 0.0328 | 0.0328 |
| Time 181-250, pooled (%) | 890 | -0.160 [-0.412, +0.093] | -0.04664 | -1.24 | 0.215 | not applied (n < 1000) | 0.562 | -1.4 | -3.4 | 0.0340 | 0.0328 |
| Avg. daily time 181-250 (%) | 890 | -0.159 [-0.412, +0.094] | -0.04732 | -1.23 | 0.219 | not applied (n < 1000) | 0.562 | -1.4 | -3.3 | 0.0340 | 0.0328 |
| Time > 180, pooled (%) | 890 | -0.160 [-0.412, +0.093] | -0.04664 | -1.24 | 0.215 | not applied (n < 1000) | 0.562 | -1.4 | -3.4 | 0.0340 | 0.0328 |
| Avg. daily time > 180 (%) | 890 | -0.159 [-0.412, +0.094] | -0.04732 | -1.23 | 0.219 | not applied (n < 1000) | 0.562 | -1.4 | -3.3 | 0.0340 | 0.0328 |
| Nocturnal time > 180 (%) | 890 | -0.100 [-0.305, +0.104] | -0.02688 | -0.96 | 0.335 | not applied (n < 1000) | 0.667 | +0.7 | -1.3 | 0.0317 | 0.0328 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 889; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 889 | -0.123 [-0.467, +0.221] | -0.2907 | -0.70 | 0.483 | not applied (n < 1000) | 0.811 | +1.4 | +0.0 | 0.0485 | 0.0487 |
| Mean glucose (mg/dL) | 889 | -0.167 [-0.482, +0.149] | -0.01377 | -1.04 | 0.300 | not applied (n < 1000) | 0.630 | +0.9 | -0.5 | 0.0495 | 0.0487 |
| GMI (%) | 889 | -0.167 [-0.482, +0.149] | -0.5758 | -1.04 | 0.300 | not applied (n < 1000) | 0.630 | +0.9 | -0.5 | 0.0495 | 0.0487 |
| Nocturnal mean 00-06h (mg/dL) | 889 | -0.030 [-0.355, +0.295] | -0.002207 | -0.18 | 0.856 | not applied (n < 1000) | 0.964 | +2.0 | +0.5 | 0.0480 | 0.0487 |
| Glucose SD, pooled (mg/dL) | 889 | -0.079 [-0.389, +0.232] | -0.01905 | -0.50 | 0.619 | not applied (n < 1000) | 0.871 | +1.8 | +0.3 | 0.0471 | 0.0487 |
| Avg. daily SD (mg/dL) | 889 | -0.099 [-0.409, +0.211] | -0.02429 | -0.62 | 0.533 | not applied (n < 1000) | 0.841 | +1.6 | +0.2 | 0.0478 | 0.0487 |
| CV (%) | 889 | +0.000 [-0.293, +0.293] | 2.846e-05 | 0.00 | 1.000 | not applied (n < 1000) | 1.000 | +2.0 | +0.6 | 0.0466 | 0.0487 |
| Mean / SD ratio | 889 | -0.015 [-0.304, +0.275] | -0.01278 | -0.10 | 0.920 | not applied (n < 1000) | 0.992 | +2.0 | +0.6 | 0.0470 | 0.0487 |
| Avg. daily mean / SD | 889 | +0.050 [-0.255, +0.354] | 0.03455 | 0.32 | 0.749 | not applied (n < 1000) | 0.942 | +1.9 | +0.5 | 0.0476 | 0.0487 |
| MAG (mg/dL/h) | 889 | +0.215 [-0.085, +0.515] | 0.03214 | 1.40 | 0.160 | not applied (n < 1000) | 0.484 | +0.1 | -1.4 | 0.0481 | 0.0487 |
| Avg. daily range (mg/dL) | 889 | -0.038 [-0.334, +0.258] | -0.002236 | -0.25 | 0.802 | not applied (n < 1000) | 0.950 | +1.9 | +0.5 | 0.0476 | 0.0487 |
| SD of daily means (mg/dL) | 889 | +0.071 [-0.237, +0.380] | 0.03028 | 0.45 | 0.650 | not applied (n < 1000) | 0.899 | +1.8 | +0.4 | 0.0472 | 0.0487 |
| Time in range 70-180, pooled (%) | 889 | +0.173 [-0.159, +0.505] | 0.05092 | 1.02 | 0.308 | not applied (n < 1000) | 0.634 | +0.8 | -0.6 | 0.0452 | 0.0487 |
| Avg. daily time in range 70-180 (%) | 889 | +0.198 [-0.129, +0.524] | 0.05951 | 1.19 | 0.235 | not applied (n < 1000) | 0.566 | +0.4 | -1.0 | 0.0460 | 0.0487 |
| Time 54-69, pooled (%) | 889 | -0.094 [-0.377, +0.189] | -0.1954 | -0.65 | 0.516 | not applied (n < 1000) | 0.836 | +1.6 | +0.2 | 0.0476 | 0.0487 |
| Avg. daily time 54-69 (%) | 889 | -0.083 [-0.377, +0.210] | -0.1679 | -0.56 | 0.578 | not applied (n < 1000) | 0.867 | +1.7 | +0.3 | 0.0473 | 0.0487 |
| Time < 70, pooled (%) | 889 | -0.094 [-0.377, +0.189] | -0.1954 | -0.65 | 0.516 | not applied (n < 1000) | 0.836 | +1.6 | +0.2 | 0.0476 | 0.0487 |
| Avg. daily time < 70 (%) | 889 | -0.083 [-0.377, +0.210] | -0.1679 | -0.56 | 0.578 | not applied (n < 1000) | 0.867 | +1.7 | +0.3 | 0.0473 | 0.0487 |
| Time 181-250, pooled (%) | 889 | -0.158 [-0.490, +0.175] | -0.04609 | -0.93 | 0.352 | not applied (n < 1000) | 0.672 | +1.0 | -0.4 | 0.0456 | 0.0487 |
| Avg. daily time 181-250 (%) | 889 | -0.184 [-0.511, +0.144] | -0.05468 | -1.10 | 0.272 | not applied (n < 1000) | 0.604 | +0.7 | -0.8 | 0.0463 | 0.0487 |
| Time > 180, pooled (%) | 889 | -0.158 [-0.490, +0.175] | -0.04609 | -0.93 | 0.352 | not applied (n < 1000) | 0.672 | +1.0 | -0.4 | 0.0456 | 0.0487 |
| Avg. daily time > 180 (%) | 889 | -0.184 [-0.511, +0.144] | -0.05468 | -1.10 | 0.272 | not applied (n < 1000) | 0.604 | +0.7 | -0.8 | 0.0463 | 0.0487 |
| Nocturnal time > 180 (%) | 889 | +0.225 [-0.151, +0.601] | 0.06031 | 1.17 | 0.241 | not applied (n < 1000) | 0.570 | +0.0 | -1.4 | 0.0449 | 0.0487 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 889; events = 155; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 889 | OR 0.950 [0.790, 1.144] | -0.1198 | -0.54 | 0.592 | not applied (n < 1000) | 0.867 | +1.7 | +0.0 | 0.6419 | 0.6430 |
| Mean glucose (mg/dL) | 889 | OR 1.069 [0.892, 1.280] | 0.00548 | 0.72 | 0.472 | not applied (n < 1000) | 0.811 | +1.5 | -0.2 | 0.6411 | 0.6430 |
| GMI (%) | 889 | OR 1.069 [0.892, 1.280] | 0.2291 | 0.72 | 0.472 | not applied (n < 1000) | 0.811 | +1.5 | -0.2 | 0.6411 | 0.6430 |
| Nocturnal mean 00-06h (mg/dL) | 889 | OR 1.205 [1.008, 1.441] | 0.01371 | 2.04 | 0.041* | not applied (n < 1000) | 0.199 | -2.2 | -3.9 | 0.6505 | 0.6430 |
| Glucose SD, pooled (mg/dL) | 889 | OR 1.009 [0.839, 1.214] | 0.002263 | 0.10 | 0.921 | not applied (n < 1000) | 0.992 | +2.0 | +0.3 | 0.6366 | 0.6430 |
| Avg. daily SD (mg/dL) | 889 | OR 1.009 [0.839, 1.215] | 0.00232 | 0.10 | 0.921 | not applied (n < 1000) | 0.992 | +2.0 | +0.3 | 0.6372 | 0.6430 |
| CV (%) | 889 | OR 0.974 [0.810, 1.171] | -0.009156 | -0.28 | 0.779 | not applied (n < 1000) | 0.950 | +1.9 | +0.2 | 0.6350 | 0.6430 |
| Mean / SD ratio | 889 | OR 1.007 [0.837, 1.211] | 0.005965 | 0.07 | 0.942 | not applied (n < 1000) | 0.993 | +2.0 | +0.3 | 0.6354 | 0.6430 |
| Avg. daily mean / SD | 889 | OR 1.023 [0.853, 1.228] | 0.0161 | 0.25 | 0.803 | not applied (n < 1000) | 0.950 | +1.9 | +0.2 | 0.6346 | 0.6430 |
| MAG (mg/dL/h) | 889 | OR 1.176 [0.985, 1.402] | 0.0242 | 1.80 | 0.072 | not applied (n < 1000) | 0.265 | -1.2 | -2.9 | 0.6481 | 0.6430 |
| Avg. daily range (mg/dL) | 889 | OR 1.032 [0.858, 1.241] | 0.001848 | 0.33 | 0.739 | not applied (n < 1000) | 0.937 | +1.9 | +0.2 | 0.6364 | 0.6430 |
| SD of daily means (mg/dL) | 889 | OR 1.069 [0.896, 1.275] | 0.02837 | 0.74 | 0.458 | not applied (n < 1000) | 0.807 | +1.5 | -0.3 | 0.6431 | 0.6430 |
| Time in range 70-180, pooled (%) | 889 | OR 0.960 [0.812, 1.136] | -0.01192 | -0.47 | 0.637 | not applied (n < 1000) | 0.885 | +1.8 | +0.1 | 0.6414 | 0.6430 |
| Avg. daily time in range 70-180 (%) | 889 | OR 0.968 [0.817, 1.147] | -0.009862 | -0.38 | 0.705 | not applied (n < 1000) | 0.934 | +1.9 | +0.1 | 0.6415 | 0.6430 |
| Time 54-69, pooled (%) | 889 | OR 0.962 [0.780, 1.188] | -0.08017 | -0.36 | 0.721 | not applied (n < 1000) | 0.934 | +1.9 | +0.2 | 0.6377 | 0.6430 |
| Avg. daily time 54-69 (%) | 889 | OR 0.968 [0.782, 1.199] | -0.06468 | -0.29 | 0.769 | not applied (n < 1000) | 0.950 | +1.9 | +0.2 | 0.6376 | 0.6430 |
| Time < 70, pooled (%) | 889 | OR 0.962 [0.780, 1.188] | -0.08017 | -0.36 | 0.721 | not applied (n < 1000) | 0.934 | +1.9 | +0.2 | 0.6377 | 0.6430 |
| Avg. daily time < 70 (%) | 889 | OR 0.968 [0.782, 1.199] | -0.06468 | -0.29 | 0.769 | not applied (n < 1000) | 0.950 | +1.9 | +0.2 | 0.6376 | 0.6430 |
| Time 181-250, pooled (%) | 889 | OR 1.045 [0.883, 1.236] | 0.01281 | 0.51 | 0.608 | not applied (n < 1000) | 0.871 | +1.7 | +0.0 | 0.6414 | 0.6430 |
| Avg. daily time 181-250 (%) | 889 | OR 1.036 [0.875, 1.228] | 0.01064 | 0.41 | 0.680 | not applied (n < 1000) | 0.912 | +1.8 | +0.1 | 0.6412 | 0.6430 |
| Time > 180, pooled (%) | 889 | OR 1.045 [0.883, 1.236] | 0.01281 | 0.51 | 0.608 | not applied (n < 1000) | 0.871 | +1.7 | +0.0 | 0.6414 | 0.6430 |
| Avg. daily time > 180 (%) | 889 | OR 1.036 [0.875, 1.228] | 0.01064 | 0.41 | 0.680 | not applied (n < 1000) | 0.912 | +1.8 | +0.1 | 0.6412 | 0.6430 |
| Nocturnal time > 180 (%) | 889 | OR 1.190 [1.025, 1.382] | 0.04666 | 2.28 | 0.023* | not applied (n < 1000) | 0.179 | -3.2 | -5.0 | 0.6499 | 0.6430 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 872; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 872 | +0.016 [-0.041, +0.073] | 0.03749 | 0.54 | 0.589 | not applied (n < 1000) | 0.867 | +1.7 | +0.0 | 0.1142 | 0.1153 |
| Mean glucose (mg/dL) | 872 | -0.035 [-0.091, +0.021] | -0.002882 | -1.21 | 0.226 | not applied (n < 1000) | 0.562 | +0.5 | -1.2 | 0.1138 | 0.1153 |
| GMI (%) | 872 | -0.035 [-0.091, +0.021] | -0.1205 | -1.21 | 0.226 | not applied (n < 1000) | 0.562 | +0.5 | -1.2 | 0.1138 | 0.1153 |
| Nocturnal mean 00-06h (mg/dL) | 872 | -0.033 [-0.091, +0.024] | -0.002444 | -1.13 | 0.259 | not applied (n < 1000) | 0.601 | +0.7 | -1.0 | 0.1137 | 0.1153 |
| Glucose SD, pooled (mg/dL) | 872 | +0.017 [-0.037, +0.071] | 0.004015 | 0.60 | 0.547 | not applied (n < 1000) | 0.852 | +1.7 | -0.1 | 0.1104 | 0.1153 |
| Avg. daily SD (mg/dL) | 872 | +0.009 [-0.044, +0.061] | 0.002149 | 0.32 | 0.746 | not applied (n < 1000) | 0.942 | +1.9 | +0.2 | 0.1099 | 0.1153 |
| CV (%) | 872 | +0.037 [-0.017, +0.092] | 0.01301 | 1.36 | 0.175 | not applied (n < 1000) | 0.500 | +0.2 | -1.5 | 0.1131 | 0.1153 |
| Mean / SD ratio | 872 | -0.029 [-0.082, +0.024] | -0.02526 | -1.07 | 0.283 | not applied (n < 1000) | 0.625 | +0.9 | -0.8 | 0.1124 | 0.1153 |
| Avg. daily mean / SD | 872 | -0.022 [-0.076, +0.031] | -0.01547 | -0.82 | 0.413 | not applied (n < 1000) | 0.743 | +1.4 | -0.3 | 0.1112 | 0.1153 |
| MAG (mg/dL/h) | 872 | +0.034 [-0.021, +0.088] | 0.005037 | 1.21 | 0.227 | not applied (n < 1000) | 0.562 | +0.5 | -1.2 | 0.1150 | 0.1153 |
| Avg. daily range (mg/dL) | 872 | +0.006 [-0.045, +0.057] | 0.0003439 | 0.22 | 0.823 | not applied (n < 1000) | 0.950 | +2.0 | +0.2 | 0.1107 | 0.1153 |
| SD of daily means (mg/dL) | 872 | +0.034 [-0.027, +0.094] | 0.01433 | 1.10 | 0.272 | not applied (n < 1000) | 0.604 | +0.6 | -1.1 | 0.1151 | 0.1153 |
| Time in range 70-180, pooled (%) | 872 | +0.026 [-0.027, +0.079] | 0.007589 | 0.95 | 0.344 | not applied (n < 1000) | 0.668 | +1.2 | -0.5 | 0.1127 | 0.1153 |
| Avg. daily time in range 70-180 (%) | 872 | +0.028 [-0.025, +0.082] | 0.008638 | 1.04 | 0.298 | not applied (n < 1000) | 0.630 | +1.0 | -0.7 | 0.1125 | 0.1153 |
| Time 54-69, pooled (%) | 872 | +0.015 [-0.042, +0.073] | 0.03216 | 0.53 | 0.598 | not applied (n < 1000) | 0.867 | +1.7 | -0.0 | 0.1128 | 0.1153 |
| Avg. daily time 54-69 (%) | 872 | +0.012 [-0.044, +0.068] | 0.02479 | 0.43 | 0.666 | not applied (n < 1000) | 0.911 | +1.8 | +0.1 | 0.1131 | 0.1153 |
| Time < 70, pooled (%) | 872 | +0.015 [-0.042, +0.073] | 0.03216 | 0.53 | 0.598 | not applied (n < 1000) | 0.867 | +1.7 | -0.0 | 0.1128 | 0.1153 |
| Avg. daily time < 70 (%) | 872 | +0.012 [-0.044, +0.068] | 0.02479 | 0.43 | 0.666 | not applied (n < 1000) | 0.911 | +1.8 | +0.1 | 0.1131 | 0.1153 |
| Time 181-250, pooled (%) | 872 | -0.028 [-0.080, +0.025] | -0.008139 | -1.03 | 0.303 | not applied (n < 1000) | 0.630 | +1.1 | -0.7 | 0.1132 | 0.1153 |
| Avg. daily time 181-250 (%) | 872 | -0.030 [-0.084, +0.023] | -0.009068 | -1.10 | 0.269 | not applied (n < 1000) | 0.604 | +0.9 | -0.8 | 0.1130 | 0.1153 |
| Time > 180, pooled (%) | 872 | -0.028 [-0.080, +0.025] | -0.008139 | -1.03 | 0.303 | not applied (n < 1000) | 0.630 | +1.1 | -0.7 | 0.1132 | 0.1153 |
| Avg. daily time > 180 (%) | 872 | -0.030 [-0.084, +0.023] | -0.009068 | -1.10 | 0.269 | not applied (n < 1000) | 0.604 | +0.9 | -0.8 | 0.1130 | 0.1153 |
| Nocturnal time > 180 (%) | 872 | -0.003 [-0.065, +0.058] | -0.0009416 | -0.11 | 0.911 | not applied (n < 1000) | 0.992 | +2.0 | +0.3 | 0.1122 | 0.1153 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 872; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 872 | +0.018 [-0.125, +0.161] | 0.04251 | 0.24 | 0.807 | not applied (n < 1000) | 0.950 | +1.9 | +0.0 | 0.2993 | 0.3009 |
| Mean glucose (mg/dL) | 872 | -0.002 [-0.135, +0.131] | -0.0001849 | -0.03 | 0.974 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.2990 | 0.3009 |
| GMI (%) | 872 | -0.002 [-0.135, +0.131] | -0.007731 | -0.03 | 0.974 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.2990 | 0.3009 |
| Nocturnal mean 00-06h (mg/dL) | 872 | -0.037 [-0.169, +0.095] | -0.002701 | -0.55 | 0.586 | not applied (n < 1000) | 0.867 | +1.7 | -0.2 | 0.2995 | 0.3009 |
| Glucose SD, pooled (mg/dL) | 872 | -0.025 [-0.157, +0.106] | -0.006139 | -0.38 | 0.705 | not applied (n < 1000) | 0.934 | +1.9 | -0.1 | 0.2996 | 0.3009 |
| Avg. daily SD (mg/dL) | 872 | -0.015 [-0.145, +0.115] | -0.003643 | -0.22 | 0.823 | not applied (n < 1000) | 0.950 | +2.0 | +0.0 | 0.2990 | 0.3009 |
| CV (%) | 872 | -0.025 [-0.154, +0.105] | -0.008516 | -0.37 | 0.711 | not applied (n < 1000) | 0.934 | +1.9 | -0.1 | 0.2997 | 0.3009 |
| Mean / SD ratio | 872 | +0.023 [-0.109, +0.155] | 0.01992 | 0.34 | 0.734 | not applied (n < 1000) | 0.934 | +1.9 | -0.1 | 0.2997 | 0.3009 |
| Avg. daily mean / SD | 872 | +0.003 [-0.132, +0.138] | 0.001946 | 0.04 | 0.968 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.2990 | 0.3009 |
| MAG (mg/dL/h) | 872 | +0.024 [-0.114, +0.163] | 0.003659 | 0.35 | 0.729 | not applied (n < 1000) | 0.934 | +1.9 | -0.1 | 0.2997 | 0.3009 |
| Avg. daily range (mg/dL) | 872 | -0.015 [-0.142, +0.113] | -0.0008651 | -0.22 | 0.822 | not applied (n < 1000) | 0.950 | +2.0 | +0.0 | 0.2996 | 0.3009 |
| SD of daily means (mg/dL) | 872 | -0.060 [-0.200, +0.081] | -0.02531 | -0.83 | 0.404 | not applied (n < 1000) | 0.731 | +1.2 | -0.7 | 0.3007 | 0.3009 |
| Time in range 70-180, pooled (%) | 872 | +0.017 [-0.102, +0.136] | 0.005129 | 0.28 | 0.776 | not applied (n < 1000) | 0.950 | +1.9 | -0.0 | 0.2999 | 0.3009 |
| Avg. daily time in range 70-180 (%) | 872 | +0.024 [-0.097, +0.146] | 0.007419 | 0.39 | 0.693 | not applied (n < 1000) | 0.926 | +1.9 | -0.1 | 0.3000 | 0.3009 |
| Time 54-69, pooled (%) | 872 | -0.035 [-0.178, +0.108] | -0.07323 | -0.48 | 0.629 | not applied (n < 1000) | 0.877 | +1.7 | -0.2 | 0.2988 | 0.3009 |
| Avg. daily time 54-69 (%) | 872 | -0.019 [-0.154, +0.117] | -0.03725 | -0.27 | 0.788 | not applied (n < 1000) | 0.950 | +1.9 | -0.0 | 0.2988 | 0.3009 |
| Time < 70, pooled (%) | 872 | -0.035 [-0.178, +0.108] | -0.07323 | -0.48 | 0.629 | not applied (n < 1000) | 0.877 | +1.7 | -0.2 | 0.2988 | 0.3009 |
| Avg. daily time < 70 (%) | 872 | -0.019 [-0.154, +0.117] | -0.03725 | -0.27 | 0.788 | not applied (n < 1000) | 0.950 | +1.9 | -0.0 | 0.2988 | 0.3009 |
| Time 181-250, pooled (%) | 872 | -0.012 [-0.132, +0.108] | -0.003525 | -0.20 | 0.845 | not applied (n < 1000) | 0.954 | +2.0 | +0.0 | 0.2995 | 0.3009 |
| Avg. daily time 181-250 (%) | 872 | -0.021 [-0.144, +0.101] | -0.006432 | -0.34 | 0.732 | not applied (n < 1000) | 0.934 | +1.9 | -0.0 | 0.2996 | 0.3009 |
| Time > 180, pooled (%) | 872 | -0.012 [-0.132, +0.108] | -0.003525 | -0.20 | 0.845 | not applied (n < 1000) | 0.954 | +2.0 | +0.0 | 0.2995 | 0.3009 |
| Avg. daily time > 180 (%) | 872 | -0.021 [-0.144, +0.101] | -0.006432 | -0.34 | 0.732 | not applied (n < 1000) | 0.934 | +1.9 | -0.0 | 0.2996 | 0.3009 |
| Nocturnal time > 180 (%) | 872 | -0.000 [-0.134, +0.134] | -2.325e-05 | -0.00 | 0.999 | not applied (n < 1000) | 1.000 | +2.0 | +0.1 | 0.2995 | 0.3009 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 872; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 872 | +0.175 [-0.291, +0.641] | 0.417 | 0.74 | 0.461 | not applied (n < 1000) | 0.807 | +1.3 | +0.0 | 0.2313 | 0.2364 |
| Mean glucose (mg/dL) | 872 | +0.280 [-0.113, +0.674] | 0.0233 | 1.40 | 0.162 | not applied (n < 1000) | 0.484 | +0.0 | -1.2 | 0.2349 | 0.2364 |
| GMI (%) | 872 | +0.280 [-0.113, +0.674] | 0.974 | 1.40 | 0.162 | not applied (n < 1000) | 0.484 | +0.0 | -1.2 | 0.2349 | 0.2364 |
| Nocturnal mean 00-06h (mg/dL) | 872 | +0.296 [-0.109, +0.701] | 0.02177 | 1.43 | 0.152 | not applied (n < 1000) | 0.481 | -0.1 | -1.4 | 0.2355 | 0.2364 |
| Glucose SD, pooled (mg/dL) | 872 | +0.587 [+0.196, +0.979] | 0.1421 | 2.94 | 0.003** | not applied (n < 1000) | 0.048 (q<0.05) | -6.6 | -7.8 | 0.2421 | 0.2364 |
| Avg. daily SD (mg/dL) | 872 | +0.567 [+0.178, +0.956] | 0.1397 | 2.86 | 0.004** | not applied (n < 1000) | 0.060 | -6.0 | -7.3 | 0.2419 | 0.2364 |
| CV (%) | 872 | +0.502 [+0.106, +0.898] | 0.1745 | 2.49 | 0.013* | not applied (n < 1000) | 0.134 | -4.4 | -5.7 | 0.2401 | 0.2364 |
| Mean / SD ratio | 872 | -0.380 [-0.779, +0.019] | -0.3297 | -1.86 | 0.062 | not applied (n < 1000) | 0.239 | -1.7 | -3.0 | 0.2374 | 0.2364 |
| Avg. daily mean / SD | 872 | -0.412 [-0.825, +0.000] | -0.2862 | -1.96 | 0.050 | not applied (n < 1000) | 0.215 | -2.4 | -3.7 | 0.2382 | 0.2364 |
| MAG (mg/dL/h) | 872 | +0.056 [-0.352, +0.465] | 0.008418 | 0.27 | 0.787 | not applied (n < 1000) | 0.950 | +1.9 | +0.6 | 0.2348 | 0.2364 |
| Avg. daily range (mg/dL) | 872 | +0.401 [+0.014, +0.787] | 0.02366 | 2.03 | 0.042* | not applied (n < 1000) | 0.199 | -2.1 | -3.4 | 0.2382 | 0.2364 |
| SD of daily means (mg/dL) | 872 | +0.357 [-0.071, +0.785] | 0.1511 | 1.64 | 0.102 | not applied (n < 1000) | 0.346 | -1.2 | -2.5 | 0.2316 | 0.2364 |
| Time in range 70-180, pooled (%) | 872 | -0.415 [-0.839, +0.010] | -0.123 | -1.91 | 0.056 | not applied (n < 1000) | 0.222 | -2.3 | -3.6 | 0.2360 | 0.2364 |
| Avg. daily time in range 70-180 (%) | 872 | -0.444 [-0.858, -0.030] | -0.1348 | -2.10 | 0.036* | not applied (n < 1000) | 0.199 | -3.0 | -4.3 | 0.2365 | 0.2364 |
| Time 54-69, pooled (%) | 872 | +0.085 [-0.315, +0.486] | 0.1777 | 0.42 | 0.676 | not applied (n < 1000) | 0.912 | +1.8 | +0.5 | 0.2334 | 0.2364 |
| Avg. daily time 54-69 (%) | 872 | +0.048 [-0.342, +0.439] | 0.09724 | 0.24 | 0.808 | not applied (n < 1000) | 0.950 | +1.9 | +0.6 | 0.2337 | 0.2364 |
| Time < 70, pooled (%) | 872 | +0.085 [-0.315, +0.486] | 0.1777 | 0.42 | 0.676 | not applied (n < 1000) | 0.912 | +1.8 | +0.5 | 0.2334 | 0.2364 |
| Avg. daily time < 70 (%) | 872 | +0.048 [-0.342, +0.439] | 0.09724 | 0.24 | 0.808 | not applied (n < 1000) | 0.950 | +1.9 | +0.6 | 0.2337 | 0.2364 |
| Time 181-250, pooled (%) | 872 | +0.399 [-0.025, +0.823] | 0.1174 | 1.85 | 0.065 | not applied (n < 1000) | 0.243 | -2.0 | -3.3 | 0.2356 | 0.2364 |
| Avg. daily time 181-250 (%) | 872 | +0.434 [+0.019, +0.848] | 0.1303 | 2.05 | 0.040* | not applied (n < 1000) | 0.199 | -2.7 | -4.0 | 0.2361 | 0.2364 |
| Time > 180, pooled (%) | 872 | +0.399 [-0.025, +0.823] | 0.1174 | 1.85 | 0.065 | not applied (n < 1000) | 0.243 | -2.0 | -3.3 | 0.2356 | 0.2364 |
| Avg. daily time > 180 (%) | 872 | +0.434 [+0.019, +0.848] | 0.1303 | 2.05 | 0.040* | not applied (n < 1000) | 0.199 | -2.7 | -4.0 | 0.2361 | 0.2364 |
| Nocturnal time > 180 (%) | 872 | +0.371 [-0.050, +0.791] | 0.09984 | 1.73 | 0.084 | not applied (n < 1000) | 0.304 | -1.4 | -2.7 | 0.2347 | 0.2364 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 872; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 872 | -0.231 [-1.523, +1.061] | -0.5504 | -0.35 | 0.726 | not applied (n < 1000) | 0.934 | +1.8 | +0.0 | 0.0111 | 0.0149 |
| Mean glucose (mg/dL) | 872 | -0.790 [-1.910, +0.331] | -0.06561 | -1.38 | 0.167 | not applied (n < 1000) | 0.484 | -0.1 | -1.9 | 0.0160 | 0.0149 |
| GMI (%) | 872 | -0.790 [-1.910, +0.331] | -2.743 | -1.38 | 0.167 | not applied (n < 1000) | 0.484 | -0.1 | -1.9 | 0.0160 | 0.0149 |
| Nocturnal mean 00-06h (mg/dL) | 872 | -0.756 [-1.829, +0.317] | -0.05564 | -1.38 | 0.168 | not applied (n < 1000) | 0.484 | +0.1 | -1.7 | 0.0154 | 0.0149 |
| Glucose SD, pooled (mg/dL) | 872 | -0.805 [-1.951, +0.340] | -0.1948 | -1.38 | 0.168 | not applied (n < 1000) | 0.484 | -0.2 | -2.0 | 0.0165 | 0.0149 |
| Avg. daily SD (mg/dL) | 872 | -0.772 [-1.903, +0.359] | -0.1903 | -1.34 | 0.181 | not applied (n < 1000) | 0.511 | -0.0 | -1.9 | 0.0161 | 0.0149 |
| CV (%) | 872 | -0.474 [-1.533, +0.585] | -0.1647 | -0.88 | 0.380 | not applied (n < 1000) | 0.697 | +1.2 | -0.6 | 0.0146 | 0.0149 |
| Mean / SD ratio | 872 | +0.479 [-0.606, +1.564] | 0.4158 | 0.87 | 0.387 | not applied (n < 1000) | 0.703 | +1.2 | -0.6 | 0.0139 | 0.0149 |
| Avg. daily mean / SD | 872 | +0.389 [-0.695, +1.474] | 0.2705 | 0.70 | 0.482 | not applied (n < 1000) | 0.811 | +1.5 | -0.4 | 0.0130 | 0.0149 |
| MAG (mg/dL/h) | 872 | +0.185 [-0.883, +1.253] | 0.02775 | 0.34 | 0.734 | not applied (n < 1000) | 0.934 | +1.9 | +0.0 | 0.0121 | 0.0149 |
| Avg. daily range (mg/dL) | 872 | -0.550 [-1.636, +0.535] | -0.03251 | -0.99 | 0.320 | not applied (n < 1000) | 0.641 | +0.9 | -0.9 | 0.0144 | 0.0149 |
| SD of daily means (mg/dL) | 872 | -0.033 [-1.212, +1.147] | -0.01378 | -0.05 | 0.957 | not applied (n < 1000) | 1.000 | +2.0 | +0.2 | 0.0125 | 0.0149 |
| Time in range 70-180, pooled (%) | 872 | +0.350 [-0.926, +1.626] | 0.1038 | 0.54 | 0.591 | not applied (n < 1000) | 0.867 | +1.6 | -0.3 | 0.0138 | 0.0149 |
| Avg. daily time in range 70-180 (%) | 872 | +0.408 [-0.849, +1.664] | 0.1237 | 0.64 | 0.525 | not applied (n < 1000) | 0.837 | +1.4 | -0.4 | 0.0142 | 0.0149 |
| Time 54-69, pooled (%) | 872 | +0.149 [-1.182, +1.480] | 0.3102 | 0.22 | 0.826 | not applied (n < 1000) | 0.950 | +1.9 | +0.1 | 0.0106 | 0.0149 |
| Avg. daily time 54-69 (%) | 872 | +0.051 [-1.274, +1.377] | 0.1034 | 0.08 | 0.939 | not applied (n < 1000) | 0.993 | +2.0 | +0.2 | 0.0103 | 0.0149 |
| Time < 70, pooled (%) | 872 | +0.149 [-1.182, +1.480] | 0.3102 | 0.22 | 0.826 | not applied (n < 1000) | 0.950 | +1.9 | +0.1 | 0.0106 | 0.0149 |
| Avg. daily time < 70 (%) | 872 | +0.051 [-1.274, +1.377] | 0.1034 | 0.08 | 0.939 | not applied (n < 1000) | 0.993 | +2.0 | +0.2 | 0.0103 | 0.0149 |
| Time 181-250, pooled (%) | 872 | -0.370 [-1.652, +0.913] | -0.1087 | -0.56 | 0.572 | not applied (n < 1000) | 0.867 | +1.5 | -0.3 | 0.0136 | 0.0149 |
| Avg. daily time 181-250 (%) | 872 | -0.413 [-1.677, +0.851] | -0.124 | -0.64 | 0.522 | not applied (n < 1000) | 0.836 | +1.4 | -0.4 | 0.0140 | 0.0149 |
| Time > 180, pooled (%) | 872 | -0.370 [-1.652, +0.913] | -0.1087 | -0.56 | 0.572 | not applied (n < 1000) | 0.867 | +1.5 | -0.3 | 0.0136 | 0.0149 |
| Avg. daily time > 180 (%) | 872 | -0.413 [-1.677, +0.851] | -0.124 | -0.64 | 0.522 | not applied (n < 1000) | 0.836 | +1.4 | -0.4 | 0.0140 | 0.0149 |
| Nocturnal time > 180 (%) | 872 | -0.714 [-1.710, +0.282] | -0.1923 | -1.40 | 0.160 | not applied (n < 1000) | 0.484 | +0.3 | -1.6 | 0.0164 | 0.0149 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Steps per wear-day
*n = 771; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 771 | +363.619 [+60.657, +666.581] | 861.6 | 2.35 | 0.019* | not applied (n < 1000) | 0.161 | -3.8 | +0.0 | 0.0834 | 0.0805 |
| Mean glucose (mg/dL) | 771 | +144.727 [-153.710, +443.165] | 11.95 | 0.95 | 0.342 | not applied (n < 1000) | 0.668 | +1.0 | +4.8 | 0.0796 | 0.0805 |
| GMI (%) | 771 | +144.727 [-153.710, +443.165] | 499.7 | 0.95 | 0.342 | not applied (n < 1000) | 0.668 | +1.0 | +4.8 | 0.0796 | 0.0805 |
| Nocturnal mean 00-06h (mg/dL) | 771 | +198.940 [-106.255, +504.135] | 14.5 | 1.28 | 0.201 | not applied (n < 1000) | 0.550 | +0.2 | +3.9 | 0.0800 | 0.0805 |
| Glucose SD, pooled (mg/dL) | 771 | +90.185 [-195.647, +376.017] | 21.65 | 0.62 | 0.536 | not applied (n < 1000) | 0.841 | +1.6 | +5.4 | 0.0797 | 0.0805 |
| Avg. daily SD (mg/dL) | 771 | +72.862 [-214.433, +360.157] | 17.94 | 0.50 | 0.619 | not applied (n < 1000) | 0.871 | +1.8 | +5.5 | 0.0796 | 0.0805 |
| CV (%) | 771 | -13.713 [-278.032, +250.606] | -4.68 | -0.10 | 0.919 | not applied (n < 1000) | 0.992 | +2.0 | +5.8 | 0.0788 | 0.0805 |
| Mean / SD ratio | 771 | -17.050 [-280.888, +246.788] | -14.68 | -0.13 | 0.899 | not applied (n < 1000) | 0.992 | +2.0 | +5.7 | 0.0786 | 0.0805 |
| Avg. daily mean / SD | 771 | -40.932 [-303.538, +221.674] | -28.55 | -0.31 | 0.760 | not applied (n < 1000) | 0.950 | +1.9 | +5.7 | 0.0790 | 0.0805 |
| MAG (mg/dL/h) | 771 | +557.298 [+266.824, +847.773] | 83.19 | 3.76 | 1.7e-04*** | not applied (n < 1000) | 0.011 (q<0.05) | -13.3 | -9.6 | 0.0967 | 0.0805 |
| Avg. daily range (mg/dL) | 771 | +143.180 [-134.438, +420.798] | 8.463 | 1.01 | 0.312 | not applied (n < 1000) | 0.634 | +1.0 | +4.8 | 0.0801 | 0.0805 |
| SD of daily means (mg/dL) | 771 | +251.261 [-62.834, +565.356] | 106.8 | 1.57 | 0.117 | not applied (n < 1000) | 0.380 | -1.0 | +2.8 | 0.0814 | 0.0805 |
| Time in range 70-180, pooled (%) | 771 | +11.423 [-307.687, +330.533] | 3.287 | 0.07 | 0.944 | not applied (n < 1000) | 0.993 | +2.0 | +5.8 | 0.0778 | 0.0805 |
| Avg. daily time in range 70-180 (%) | 771 | -6.785 [-330.893, +317.322] | -1.995 | -0.04 | 0.967 | not applied (n < 1000) | 1.000 | +2.0 | +5.8 | 0.0778 | 0.0805 |
| Time 54-69, pooled (%) | 771 | -167.569 [-438.318, +103.181] | -338.2 | -1.21 | 0.225 | not applied (n < 1000) | 0.562 | +0.6 | +4.4 | 0.0764 | 0.0805 |
| Avg. daily time 54-69 (%) | 771 | -198.615 [-463.902, +66.673] | -388.4 | -1.47 | 0.142 | not applied (n < 1000) | 0.454 | +0.1 | +3.8 | 0.0780 | 0.0805 |
| Time < 70, pooled (%) | 771 | -167.569 [-438.318, +103.181] | -338.2 | -1.21 | 0.225 | not applied (n < 1000) | 0.562 | +0.6 | +4.4 | 0.0764 | 0.0805 |
| Avg. daily time < 70 (%) | 771 | -198.615 [-463.902, +66.673] | -388.4 | -1.47 | 0.142 | not applied (n < 1000) | 0.454 | +0.1 | +3.8 | 0.0780 | 0.0805 |
| Time 181-250, pooled (%) | 771 | +13.307 [-306.545, +333.158] | 3.798 | 0.08 | 0.935 | not applied (n < 1000) | 0.993 | +2.0 | +5.8 | 0.0775 | 0.0805 |
| Avg. daily time 181-250 (%) | 771 | +37.566 [-288.012, +363.143] | 10.94 | 0.23 | 0.821 | not applied (n < 1000) | 0.950 | +1.9 | +5.7 | 0.0775 | 0.0805 |
| Time > 180, pooled (%) | 771 | +13.307 [-306.545, +333.158] | 3.798 | 0.08 | 0.935 | not applied (n < 1000) | 0.993 | +2.0 | +5.8 | 0.0775 | 0.0805 |
| Avg. daily time > 180 (%) | 771 | +37.566 [-288.012, +363.143] | 10.94 | 0.23 | 0.821 | not applied (n < 1000) | 0.950 | +1.9 | +5.7 | 0.0775 | 0.0805 |
| Nocturnal time > 180 (%) | 771 | +43.220 [-293.492, +379.932] | 11.43 | 0.25 | 0.801 | not applied (n < 1000) | 0.950 | +1.9 | +5.7 | 0.0753 | 0.0805 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 771; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 771 | +1.185 [+0.234, +2.136] | 2.809 | 2.44 | 0.015* | not applied (n < 1000) | 0.147 | -4.7 | +0.0 | 0.1159 | 0.1107 |
| Mean glucose (mg/dL) | 771 | +0.584 [-0.299, +1.467] | 0.0482 | 1.30 | 0.195 | not applied (n < 1000) | 0.537 | +0.3 | +4.9 | 0.1104 | 0.1107 |
| GMI (%) | 771 | +0.584 [-0.299, +1.467] | 2.015 | 1.30 | 0.195 | not applied (n < 1000) | 0.537 | +0.3 | +4.9 | 0.1104 | 0.1107 |
| Nocturnal mean 00-06h (mg/dL) | 771 | +0.568 [-0.334, +1.470] | 0.04141 | 1.23 | 0.217 | not applied (n < 1000) | 0.562 | +0.4 | +5.0 | 0.1098 | 0.1107 |
| Glucose SD, pooled (mg/dL) | 771 | +0.588 [-0.292, +1.467] | 0.1412 | 1.31 | 0.190 | not applied (n < 1000) | 0.532 | +0.3 | +4.9 | 0.1120 | 0.1107 |
| Avg. daily SD (mg/dL) | 771 | +0.537 [-0.339, +1.414] | 0.1323 | 1.20 | 0.230 | not applied (n < 1000) | 0.562 | +0.5 | +5.2 | 0.1116 | 0.1107 |
| CV (%) | 771 | +0.229 [-0.612, +1.070] | 0.07821 | 0.53 | 0.593 | not applied (n < 1000) | 0.867 | +1.7 | +6.4 | 0.1095 | 0.1107 |
| Mean / SD ratio | 771 | -0.304 [-1.133, +0.525] | -0.2616 | -0.72 | 0.473 | not applied (n < 1000) | 0.811 | +1.5 | +6.2 | 0.1092 | 0.1107 |
| Avg. daily mean / SD | 771 | -0.328 [-1.140, +0.484] | -0.2288 | -0.79 | 0.428 | not applied (n < 1000) | 0.766 | +1.4 | +6.1 | 0.1098 | 0.1107 |
| MAG (mg/dL/h) | 771 | +1.848 [+0.999, +2.696] | 0.2758 | 4.27 | 2.0e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -16.3 | -11.7 | 0.1309 | 0.1107 |
| Avg. daily range (mg/dL) | 771 | +0.829 [-0.054, +1.711] | 0.04899 | 1.84 | 0.066 | not applied (n < 1000) | 0.243 | -1.6 | +3.1 | 0.1141 | 0.1107 |
| SD of daily means (mg/dL) | 771 | +0.785 [-0.139, +1.708] | 0.3336 | 1.67 | 0.096 | not applied (n < 1000) | 0.328 | -1.2 | +3.5 | 0.1112 | 0.1107 |
| Time in range 70-180, pooled (%) | 771 | -0.223 [-1.096, +0.650] | -0.06424 | -0.50 | 0.616 | not applied (n < 1000) | 0.871 | +1.7 | +6.4 | 0.1091 | 0.1107 |
| Avg. daily time in range 70-180 (%) | 771 | -0.304 [-1.186, +0.578] | -0.08935 | -0.68 | 0.499 | not applied (n < 1000) | 0.833 | +1.5 | +6.2 | 0.1093 | 0.1107 |
| Time 54-69, pooled (%) | 771 | -0.623 [-1.258, +0.013] | -1.257 | -1.92 | 0.055 | not applied (n < 1000) | 0.222 | -0.1 | +4.6 | 0.1109 | 0.1107 |
| Avg. daily time 54-69 (%) | 771 | -0.705 [-1.311, -0.100] | -1.38 | -2.28 | 0.022* | not applied (n < 1000) | 0.179 | -0.6 | +4.0 | 0.1121 | 0.1107 |
| Time < 70, pooled (%) | 771 | -0.623 [-1.258, +0.013] | -1.257 | -1.92 | 0.055 | not applied (n < 1000) | 0.222 | -0.1 | +4.6 | 0.1109 | 0.1107 |
| Avg. daily time < 70 (%) | 771 | -0.705 [-1.311, -0.100] | -1.38 | -2.28 | 0.022* | not applied (n < 1000) | 0.179 | -0.6 | +4.0 | 0.1121 | 0.1107 |
| Time 181-250, pooled (%) | 771 | +0.313 [-0.563, +1.190] | 0.08946 | 0.70 | 0.483 | not applied (n < 1000) | 0.811 | +1.5 | +6.1 | 0.1091 | 0.1107 |
| Avg. daily time 181-250 (%) | 771 | +0.411 [-0.475, +1.298] | 0.1198 | 0.91 | 0.363 | not applied (n < 1000) | 0.672 | +1.1 | +5.8 | 0.1096 | 0.1107 |
| Time > 180, pooled (%) | 771 | +0.313 [-0.563, +1.190] | 0.08946 | 0.70 | 0.483 | not applied (n < 1000) | 0.811 | +1.5 | +6.1 | 0.1091 | 0.1107 |
| Avg. daily time > 180 (%) | 771 | +0.411 [-0.475, +1.298] | 0.1198 | 0.91 | 0.363 | not applied (n < 1000) | 0.672 | +1.1 | +5.8 | 0.1096 | 0.1107 |
| Nocturnal time > 180 (%) | 771 | +0.309 [-0.675, +1.294] | 0.08177 | 0.62 | 0.538 | not applied (n < 1000) | 0.841 | +1.5 | +6.2 | 0.1072 | 0.1107 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 774; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 774 | +1.016 [+0.408, +1.623] | 2.41 | 3.27 | 0.001** | not applied (n < 1000) | 0.024 (q<0.05) | -9.9 | +0.0 | 0.1652 | 0.1535 |
| Mean glucose (mg/dL) | 774 | +1.165 [+0.628, +1.701] | 0.09654 | 4.26 | 2.1e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -14.9 | -5.0 | 0.1713 | 0.1535 |
| GMI (%) | 774 | +1.165 [+0.628, +1.701] | 4.036 | 4.26 | 2.1e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -14.9 | -5.0 | 0.1713 | 0.1535 |
| Nocturnal mean 00-06h (mg/dL) | 774 | +1.152 [+0.620, +1.684] | 0.08388 | 4.24 | 2.2e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -14.2 | -4.3 | 0.1710 | 0.1535 |
| Glucose SD, pooled (mg/dL) | 774 | +0.741 [+0.164, +1.319] | 0.1782 | 2.52 | 0.012* | not applied (n < 1000) | 0.127 | -4.7 | +5.2 | 0.1593 | 0.1535 |
| Avg. daily SD (mg/dL) | 774 | +0.761 [+0.178, +1.344] | 0.1875 | 2.56 | 0.011* | not applied (n < 1000) | 0.121 | -5.1 | +4.8 | 0.1601 | 0.1535 |
| CV (%) | 774 | +0.159 [-0.405, +0.723] | 0.05426 | 0.55 | 0.580 | not applied (n < 1000) | 0.867 | +1.7 | +11.6 | 0.1515 | 0.1535 |
| Mean / SD ratio | 774 | -0.141 [-0.669, +0.387] | -0.1203 | -0.52 | 0.601 | not applied (n < 1000) | 0.867 | +1.8 | +11.7 | 0.1523 | 0.1535 |
| Avg. daily mean / SD | 774 | -0.232 [-0.750, +0.287] | -0.1598 | -0.88 | 0.381 | not applied (n < 1000) | 0.697 | +1.3 | +11.2 | 0.1532 | 0.1535 |
| MAG (mg/dL/h) | 774 | +0.938 [+0.360, +1.517] | 0.1394 | 3.18 | 0.001** | not applied (n < 1000) | 0.032 (q<0.05) | -9.5 | +0.5 | 0.1636 | 0.1535 |
| Avg. daily range (mg/dL) | 774 | +0.728 [+0.164, +1.291] | 0.04296 | 2.53 | 0.011* | not applied (n < 1000) | 0.127 | -4.7 | +5.2 | 0.1594 | 0.1535 |
| SD of daily means (mg/dL) | 774 | +0.735 [+0.121, +1.348] | 0.3126 | 2.35 | 0.019* | not applied (n < 1000) | 0.161 | -4.8 | +5.1 | 0.1569 | 0.1535 |
| Time in range 70-180, pooled (%) | 774 | -0.769 [-1.309, -0.229] | -0.225 | -2.79 | 0.005** | not applied (n < 1000) | 0.071 | -5.4 | +4.5 | 0.1598 | 0.1535 |
| Avg. daily time in range 70-180 (%) | 774 | -0.813 [-1.349, -0.277] | -0.2435 | -2.98 | 0.003** | not applied (n < 1000) | 0.046 (q<0.05) | -6.3 | +3.7 | 0.1607 | 0.1535 |
| Time 54-69, pooled (%) | 774 | -0.804 [-1.467, -0.141] | -1.626 | -2.38 | 0.017* | not applied (n < 1000) | 0.156 | -6.4 | +3.5 | 0.1579 | 0.1535 |
| Avg. daily time 54-69 (%) | 774 | -0.752 [-1.429, -0.074] | -1.472 | -2.17 | 0.030* | not applied (n < 1000) | 0.199 | -5.3 | +4.6 | 0.1576 | 0.1535 |
| Time < 70, pooled (%) | 774 | -0.804 [-1.467, -0.141] | -1.626 | -2.38 | 0.017* | not applied (n < 1000) | 0.156 | -6.4 | +3.5 | 0.1579 | 0.1535 |
| Avg. daily time < 70 (%) | 774 | -0.752 [-1.429, -0.074] | -1.472 | -2.17 | 0.030* | not applied (n < 1000) | 0.199 | -5.3 | +4.6 | 0.1576 | 0.1535 |
| Time 181-250, pooled (%) | 774 | +0.884 [+0.331, +1.436] | 0.2564 | 3.13 | 0.002** | not applied (n < 1000) | 0.033 (q<0.05) | -7.8 | +2.1 | 0.1620 | 0.1535 |
| Avg. daily time 181-250 (%) | 774 | +0.926 [+0.382, +1.470] | 0.2747 | 3.34 | 8.5e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -8.7 | +1.2 | 0.1631 | 0.1535 |
| Time > 180, pooled (%) | 774 | +0.884 [+0.331, +1.436] | 0.2564 | 3.13 | 0.002** | not applied (n < 1000) | 0.033 (q<0.05) | -7.8 | +2.1 | 0.1620 | 0.1535 |
| Avg. daily time > 180 (%) | 774 | +0.926 [+0.382, +1.470] | 0.2747 | 3.34 | 8.5e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -8.7 | +1.2 | 0.1631 | 0.1535 |
| Nocturnal time > 180 (%) | 774 | +0.544 [+0.135, +0.953] | 0.1439 | 2.61 | 0.009** | not applied (n < 1000) | 0.108 | -1.7 | +8.3 | 0.1570 | 0.1535 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 779; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 779 | -7.115 [-12.140, -2.089] | -16.9 | -2.77 | 0.006** | not applied (n < 1000) | 0.071 | -5.6 | +0.0 | 0.0122 | 0.0096 |
| Mean glucose (mg/dL) | 779 | -3.162 [-8.101, +1.776] | -0.2638 | -1.25 | 0.209 | not applied (n < 1000) | 0.562 | +0.4 | +6.0 | 0.0027 | 0.0096 |
| GMI (%) | 779 | -3.162 [-8.101, +1.776] | -11.03 | -1.25 | 0.209 | not applied (n < 1000) | 0.562 | +0.4 | +6.0 | 0.0027 | 0.0096 |
| Nocturnal mean 00-06h (mg/dL) | 779 | -5.434 [-10.488, -0.379] | -0.3983 | -2.11 | 0.035* | not applied (n < 1000) | 0.199 | -2.6 | +3.0 | 0.0088 | 0.0096 |
| Glucose SD, pooled (mg/dL) | 779 | -1.453 [-6.647, +3.741] | -0.3496 | -0.55 | 0.583 | not applied (n < 1000) | 0.867 | +1.7 | +7.3 | 0.0034 | 0.0096 |
| Avg. daily SD (mg/dL) | 779 | -1.535 [-6.652, +3.582] | -0.3773 | -0.59 | 0.557 | not applied (n < 1000) | 0.862 | +1.6 | +7.2 | 0.0029 | 0.0096 |
| CV (%) | 779 | +0.103 [-5.016, +5.222] | 0.03533 | 0.04 | 0.969 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0073 | 0.0096 |
| Mean / SD ratio | 779 | -0.443 [-5.507, +4.620] | -0.3855 | -0.17 | 0.864 | not applied (n < 1000) | 0.969 | +2.0 | +7.6 | 0.0073 | 0.0096 |
| Avg. daily mean / SD | 779 | -0.024 [-5.010, +4.961] | -0.01688 | -0.01 | 0.992 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0065 | 0.0096 |
| MAG (mg/dL/h) | 779 | -7.094 [-12.830, -1.358] | -1.057 | -2.42 | 0.015* | not applied (n < 1000) | 0.148 | -6.5 | -0.9 | 0.0152 | 0.0096 |
| Avg. daily range (mg/dL) | 779 | +0.022 [-5.264, +5.309] | 0.001324 | 0.01 | 0.993 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0023 | 0.0096 |
| SD of daily means (mg/dL) | 779 | -1.634 [-6.588, +3.321] | -0.6839 | -0.65 | 0.518 | not applied (n < 1000) | 0.836 | +1.6 | +7.2 | 0.0070 | 0.0096 |
| Time in range 70-180, pooled (%) | 779 | -0.330 [-4.851, +4.192] | -0.09623 | -0.14 | 0.886 | not applied (n < 1000) | 0.988 | +2.0 | +7.6 | 0.0023 | 0.0096 |
| Avg. daily time in range 70-180 (%) | 779 | +0.054 [-4.506, +4.615] | 0.01615 | 0.02 | 0.981 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0022 | 0.0096 |
| Time 54-69, pooled (%) | 779 | +0.559 [-3.761, +4.878] | 1.146 | 0.25 | 0.800 | not applied (n < 1000) | 0.950 | +1.9 | +7.6 | 0.0065 | 0.0096 |
| Avg. daily time 54-69 (%) | 779 | -0.030 [-4.235, +4.176] | -0.05886 | -0.01 | 0.989 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0068 | 0.0096 |
| Time < 70, pooled (%) | 779 | +0.559 [-3.761, +4.878] | 1.146 | 0.25 | 0.800 | not applied (n < 1000) | 0.950 | +1.9 | +7.6 | 0.0065 | 0.0096 |
| Avg. daily time < 70 (%) | 779 | -0.030 [-4.235, +4.176] | -0.05886 | -0.01 | 0.989 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0068 | 0.0096 |
| Time 181-250, pooled (%) | 779 | +0.245 [-4.327, +4.817] | 0.07093 | 0.10 | 0.916 | not applied (n < 1000) | 0.992 | +2.0 | +7.6 | 0.0016 | 0.0096 |
| Avg. daily time 181-250 (%) | 779 | -0.049 [-4.666, +4.568] | -0.01454 | -0.02 | 0.983 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0015 | 0.0096 |
| Time > 180, pooled (%) | 779 | +0.245 [-4.327, +4.817] | 0.07093 | 0.10 | 0.916 | not applied (n < 1000) | 0.992 | +2.0 | +7.6 | 0.0016 | 0.0096 |
| Avg. daily time > 180 (%) | 779 | -0.049 [-4.666, +4.568] | -0.01454 | -0.02 | 0.983 | not applied (n < 1000) | 1.000 | +2.0 | +7.6 | 0.0015 | 0.0096 |
| Nocturnal time > 180 (%) | 779 | +0.295 [-5.118, +5.708] | 0.07821 | 0.11 | 0.915 | not applied (n < 1000) | 0.992 | +2.0 | +7.6 | 0.0052 | 0.0096 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 775; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 775 | +1.492 [+0.159, +2.825] | 3.533 | 2.19 | 0.028* | not applied (n < 1000) | 0.199 | -3.2 | +0.0 | 0.1110 | 0.1075 |
| Mean glucose (mg/dL) | 775 | +1.875 [+0.635, +3.115] | 0.155 | 2.96 | 0.003** | not applied (n < 1000) | 0.046 (q<0.05) | -6.8 | -3.7 | 0.1159 | 0.1075 |
| GMI (%) | 775 | +1.875 [+0.635, +3.115] | 6.478 | 2.96 | 0.003** | not applied (n < 1000) | 0.046 (q<0.05) | -6.8 | -3.7 | 0.1159 | 0.1075 |
| Nocturnal mean 00-06h (mg/dL) | 775 | +1.944 [+0.697, +3.191] | 0.1415 | 3.06 | 0.002** | not applied (n < 1000) | 0.040 (q<0.05) | -7.3 | -4.1 | 0.1151 | 0.1075 |
| Glucose SD, pooled (mg/dL) | 775 | +1.215 [-0.060, +2.489] | 0.2917 | 1.87 | 0.062 | not applied (n < 1000) | 0.239 | -1.7 | +1.5 | 0.1107 | 0.1075 |
| Avg. daily SD (mg/dL) | 775 | +1.093 [-0.187, +2.373] | 0.2691 | 1.67 | 0.094 | not applied (n < 1000) | 0.326 | -1.0 | +2.2 | 0.1101 | 0.1075 |
| CV (%) | 775 | +0.348 [-0.907, +1.602] | 0.1184 | 0.54 | 0.587 | not applied (n < 1000) | 0.867 | +1.7 | +4.9 | 0.1063 | 0.1075 |
| Mean / SD ratio | 775 | -0.445 [-1.671, +0.781] | -0.3799 | -0.71 | 0.477 | not applied (n < 1000) | 0.811 | +1.5 | +4.7 | 0.1066 | 0.1075 |
| Avg. daily mean / SD | 775 | -0.399 [-1.607, +0.810] | -0.2752 | -0.65 | 0.518 | not applied (n < 1000) | 0.836 | +1.6 | +4.8 | 0.1067 | 0.1075 |
| MAG (mg/dL/h) | 775 | +1.038 [-0.243, +2.319] | 0.1543 | 1.59 | 0.112 | not applied (n < 1000) | 0.377 | -0.8 | +2.4 | 0.1089 | 0.1075 |
| Avg. daily range (mg/dL) | 775 | +1.081 [-0.180, +2.342] | 0.06367 | 1.68 | 0.093 | not applied (n < 1000) | 0.325 | -1.0 | +2.2 | 0.1097 | 0.1075 |
| SD of daily means (mg/dL) | 775 | +1.267 [+0.033, +2.501] | 0.5397 | 2.01 | 0.044* | not applied (n < 1000) | 0.201 | -2.1 | +1.1 | 0.1095 | 0.1075 |
| Time in range 70-180, pooled (%) | 775 | -0.362 [-1.465, +0.741] | -0.106 | -0.64 | 0.520 | not applied (n < 1000) | 0.836 | +1.7 | +4.9 | 0.1067 | 0.1075 |
| Avg. daily time in range 70-180 (%) | 775 | -0.344 [-1.433, +0.744] | -0.1032 | -0.62 | 0.535 | not applied (n < 1000) | 0.841 | +1.7 | +4.9 | 0.1068 | 0.1075 |
| Time 54-69, pooled (%) | 775 | -1.618 [-3.099, -0.137] | -3.232 | -2.14 | 0.032* | not applied (n < 1000) | 0.199 | -4.9 | -1.7 | 0.1126 | 0.1075 |
| Avg. daily time 54-69 (%) | 775 | -1.614 [-3.224, -0.005] | -3.123 | -1.97 | 0.049* | not applied (n < 1000) | 0.215 | -4.8 | -1.6 | 0.1117 | 0.1075 |
| Time < 70, pooled (%) | 775 | -1.618 [-3.099, -0.137] | -3.232 | -2.14 | 0.032* | not applied (n < 1000) | 0.199 | -4.9 | -1.7 | 0.1126 | 0.1075 |
| Avg. daily time < 70 (%) | 775 | -1.614 [-3.224, -0.005] | -3.123 | -1.97 | 0.049* | not applied (n < 1000) | 0.215 | -4.8 | -1.6 | 0.1117 | 0.1075 |
| Time 181-250, pooled (%) | 775 | +0.603 [-0.534, +1.741] | 0.1752 | 1.04 | 0.298 | not applied (n < 1000) | 0.630 | +1.1 | +4.3 | 0.1073 | 0.1075 |
| Avg. daily time 181-250 (%) | 775 | +0.599 [-0.517, +1.715] | 0.1778 | 1.05 | 0.293 | not applied (n < 1000) | 0.630 | +1.1 | +4.3 | 0.1075 | 0.1075 |
| Time > 180, pooled (%) | 775 | +0.603 [-0.534, +1.741] | 0.1752 | 1.04 | 0.298 | not applied (n < 1000) | 0.630 | +1.1 | +4.3 | 0.1073 | 0.1075 |
| Avg. daily time > 180 (%) | 775 | +0.599 [-0.517, +1.715] | 0.1778 | 1.05 | 0.293 | not applied (n < 1000) | 0.630 | +1.1 | +4.3 | 0.1075 | 0.1075 |
| Nocturnal time > 180 (%) | 775 | +0.519 [-0.493, +1.531] | 0.1373 | 1.01 | 0.315 | not applied (n < 1000) | 0.634 | +1.3 | +4.5 | 0.1071 | 0.1075 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

### Population: Healthy group (no diabetes + pre-diabetes / lifestyle)

#### MoCA total score (0-30)
*n = 685; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 685 | -0.240 [-0.457, -0.023] | -0.7219 | -2.17 | 0.030* | not applied (n < 1000) | 0.322 | -3.3 | +0.0 | 0.0914 | 0.0870 |
| Mean glucose (mg/dL) | 685 | -0.290 [-0.543, -0.037] | -0.02586 | -2.25 | 0.025* | not applied (n < 1000) | 0.304 | -5.9 | -2.6 | 0.0914 | 0.0870 |
| GMI (%) | 685 | -0.290 [-0.543, -0.037] | -1.081 | -2.25 | 0.025* | not applied (n < 1000) | 0.304 | -5.9 | -2.6 | 0.0914 | 0.0870 |
| Nocturnal mean 00-06h (mg/dL) | 685 | -0.211 [-0.457, +0.036] | -0.01651 | -1.68 | 0.094 | not applied (n < 1000) | 0.556 | -2.1 | +1.2 | 0.0846 | 0.0870 |
| Glucose SD, pooled (mg/dL) | 685 | -0.063 [-0.273, +0.147] | -0.01669 | -0.59 | 0.557 | not applied (n < 1000) | 0.918 | +1.6 | +4.9 | 0.0854 | 0.0870 |
| Avg. daily SD (mg/dL) | 685 | -0.063 [-0.270, +0.144] | -0.01697 | -0.60 | 0.551 | not applied (n < 1000) | 0.918 | +1.6 | +4.9 | 0.0856 | 0.0870 |
| CV (%) | 685 | +0.073 [-0.143, +0.289] | 0.02637 | 0.66 | 0.509 | not applied (n < 1000) | 0.918 | +1.5 | +4.8 | 0.0845 | 0.0870 |
| Mean / SD ratio | 685 | -0.117 [-0.341, +0.107] | -0.1032 | -1.02 | 0.307 | not applied (n < 1000) | 0.773 | +0.7 | +4.0 | 0.0840 | 0.0870 |
| Avg. daily mean / SD | 685 | -0.101 [-0.316, +0.113] | -0.07267 | -0.93 | 0.355 | not applied (n < 1000) | 0.818 | +1.0 | +4.3 | 0.0838 | 0.0870 |
| MAG (mg/dL/h) | 685 | -0.014 [-0.192, +0.164] | -0.002087 | -0.16 | 0.877 | not applied (n < 1000) | 0.969 | +2.0 | +5.3 | 0.0838 | 0.0870 |
| Avg. daily range (mg/dL) | 685 | -0.048 [-0.245, +0.149] | -0.002955 | -0.48 | 0.633 | not applied (n < 1000) | 0.931 | +1.8 | +5.1 | 0.0848 | 0.0870 |
| SD of daily means (mg/dL) | 685 | -0.104 [-0.316, +0.109] | -0.0462 | -0.96 | 0.338 | not applied (n < 1000) | 0.818 | +1.0 | +4.3 | 0.0850 | 0.0870 |
| Time in range 70-180, pooled (%) | 685 | +0.196 [-0.094, +0.486] | 0.07305 | 1.33 | 0.185 | not applied (n < 1000) | 0.612 | -1.7 | +1.6 | 0.0859 | 0.0870 |
| Avg. daily time in range 70-180 (%) | 685 | +0.207 [-0.080, +0.494] | 0.07889 | 1.41 | 0.157 | not applied (n < 1000) | 0.574 | -2.1 | +1.2 | 0.0865 | 0.0870 |
| Time 54-69, pooled (%) | 685 | +0.064 [-0.100, +0.228] | 0.1228 | 0.76 | 0.444 | not applied (n < 1000) | 0.883 | +1.6 | +4.9 | 0.0839 | 0.0870 |
| Avg. daily time 54-69 (%) | 685 | +0.057 [-0.109, +0.222] | 0.1052 | 0.67 | 0.502 | not applied (n < 1000) | 0.918 | +1.7 | +5.0 | 0.0830 | 0.0870 |
| Time < 70, pooled (%) | 685 | +0.064 [-0.100, +0.228] | 0.1228 | 0.76 | 0.444 | not applied (n < 1000) | 0.883 | +1.6 | +4.9 | 0.0839 | 0.0870 |
| Avg. daily time < 70 (%) | 685 | +0.057 [-0.109, +0.222] | 0.1052 | 0.67 | 0.502 | not applied (n < 1000) | 0.918 | +1.7 | +5.0 | 0.0830 | 0.0870 |
| Time 181-250, pooled (%) | 685 | -0.208 [-0.499, +0.084] | -0.07683 | -1.40 | 0.162 | not applied (n < 1000) | 0.574 | -2.1 | +1.2 | 0.0865 | 0.0870 |
| Avg. daily time 181-250 (%) | 685 | -0.218 [-0.507, +0.070] | -0.08252 | -1.48 | 0.138 | not applied (n < 1000) | 0.557 | -2.5 | +0.8 | 0.0874 | 0.0870 |
| Time > 180, pooled (%) | 685 | -0.208 [-0.499, +0.084] | -0.07683 | -1.40 | 0.162 | not applied (n < 1000) | 0.574 | -2.1 | +1.2 | 0.0865 | 0.0870 |
| Avg. daily time > 180 (%) | 685 | -0.218 [-0.507, +0.070] | -0.08252 | -1.48 | 0.138 | not applied (n < 1000) | 0.557 | -2.5 | +0.8 | 0.0874 | 0.0870 |
| Nocturnal time > 180 (%) | 685 | -0.122 [-0.377, +0.133] | -0.03988 | -0.94 | 0.347 | not applied (n < 1000) | 0.818 | +0.6 | +3.9 | 0.0728 | 0.0870 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 685; events = 242; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 685 | OR 1.098 [0.927, 1.301] | 0.281 | 1.08 | 0.280 | not applied (n < 1000) | 0.740 | +0.8 | +0.0 | 0.6388 | 0.6460 |
| Mean glucose (mg/dL) | 685 | OR 1.208 [1.021, 1.429] | 0.01685 | 2.21 | 0.027* | not applied (n < 1000) | 0.304 | -2.9 | -3.7 | 0.6539 | 0.6460 |
| GMI (%) | 685 | OR 1.208 [1.021, 1.429] | 0.7044 | 2.21 | 0.027* | not applied (n < 1000) | 0.304 | -2.9 | -3.7 | 0.6539 | 0.6460 |
| Nocturnal mean 00-06h (mg/dL) | 685 | OR 1.178 [0.994, 1.395] | 0.01283 | 1.90 | 0.058 | not applied (n < 1000) | 0.467 | -1.6 | -2.4 | 0.6532 | 0.6460 |
| Glucose SD, pooled (mg/dL) | 685 | OR 1.061 [0.898, 1.254] | 0.01573 | 0.70 | 0.487 | not applied (n < 1000) | 0.918 | +1.5 | +0.7 | 0.6444 | 0.6460 |
| Avg. daily SD (mg/dL) | 685 | OR 1.063 [0.900, 1.256] | 0.01654 | 0.72 | 0.470 | not applied (n < 1000) | 0.907 | +1.5 | +0.6 | 0.6437 | 0.6460 |
| CV (%) | 685 | OR 0.971 [0.823, 1.147] | -0.01052 | -0.34 | 0.732 | not applied (n < 1000) | 0.951 | +1.9 | +1.0 | 0.6441 | 0.6460 |
| Mean / SD ratio | 685 | OR 1.052 [0.891, 1.241] | 0.04446 | 0.59 | 0.553 | not applied (n < 1000) | 0.918 | +1.6 | +0.8 | 0.6441 | 0.6460 |
| Avg. daily mean / SD | 685 | OR 1.032 [0.874, 1.218] | 0.02248 | 0.37 | 0.711 | not applied (n < 1000) | 0.951 | +1.9 | +1.0 | 0.6431 | 0.6460 |
| MAG (mg/dL/h) | 685 | OR 1.096 [0.930, 1.292] | 0.01362 | 1.09 | 0.274 | not applied (n < 1000) | 0.739 | +0.8 | -0.0 | 0.6440 | 0.6460 |
| Avg. daily range (mg/dL) | 685 | OR 1.069 [0.906, 1.261] | 0.004093 | 0.79 | 0.431 | not applied (n < 1000) | 0.883 | +1.4 | +0.5 | 0.6436 | 0.6460 |
| SD of daily means (mg/dL) | 685 | OR 1.103 [0.937, 1.297] | 0.04351 | 1.18 | 0.239 | not applied (n < 1000) | 0.739 | +0.6 | -0.2 | 0.6460 | 0.6460 |
| Time in range 70-180, pooled (%) | 685 | OR 0.936 [0.794, 1.102] | -0.02477 | -0.80 | 0.427 | not applied (n < 1000) | 0.883 | +1.4 | +0.5 | 0.6451 | 0.6460 |
| Avg. daily time in range 70-180 (%) | 685 | OR 0.920 [0.782, 1.083] | -0.0317 | -1.00 | 0.317 | not applied (n < 1000) | 0.791 | +1.0 | +0.2 | 0.6452 | 0.6460 |
| Time 54-69, pooled (%) | 685 | OR 0.952 [0.802, 1.130] | -0.09482 | -0.56 | 0.572 | not applied (n < 1000) | 0.918 | +1.7 | +0.8 | 0.6444 | 0.6460 |
| Avg. daily time 54-69 (%) | 685 | OR 0.964 [0.815, 1.141] | -0.06745 | -0.42 | 0.671 | not applied (n < 1000) | 0.947 | +1.8 | +1.0 | 0.6438 | 0.6460 |
| Time < 70, pooled (%) | 685 | OR 0.952 [0.802, 1.130] | -0.09482 | -0.56 | 0.572 | not applied (n < 1000) | 0.918 | +1.7 | +0.8 | 0.6444 | 0.6460 |
| Avg. daily time < 70 (%) | 685 | OR 0.964 [0.815, 1.141] | -0.06745 | -0.42 | 0.671 | not applied (n < 1000) | 0.947 | +1.8 | +1.0 | 0.6438 | 0.6460 |
| Time 181-250, pooled (%) | 685 | OR 1.079 [0.916, 1.270] | 0.02797 | 0.91 | 0.365 | not applied (n < 1000) | 0.822 | +1.2 | +0.4 | 0.6454 | 0.6460 |
| Avg. daily time 181-250 (%) | 685 | OR 1.095 [0.930, 1.289] | 0.03423 | 1.09 | 0.277 | not applied (n < 1000) | 0.739 | +0.8 | +0.0 | 0.6458 | 0.6460 |
| Time > 180, pooled (%) | 685 | OR 1.079 [0.916, 1.270] | 0.02797 | 0.91 | 0.365 | not applied (n < 1000) | 0.822 | +1.2 | +0.4 | 0.6454 | 0.6460 |
| Avg. daily time > 180 (%) | 685 | OR 1.095 [0.930, 1.289] | 0.03423 | 1.09 | 0.277 | not applied (n < 1000) | 0.739 | +0.8 | +0.0 | 0.6458 | 0.6460 |
| Nocturnal time > 180 (%) | 685 | OR 1.054 [0.896, 1.239] | 0.01703 | 0.63 | 0.528 | not applied (n < 1000) | 0.918 | +1.6 | +0.8 | 0.6448 | 0.6460 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 685; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 685 | -0.007 [-0.207, +0.194] | -0.01958 | -0.06 | 0.949 | not applied (n < 1000) | 0.989 | +2.0 | +0.0 | 0.0396 | 0.0422 |
| Mean glucose (mg/dL) | 685 | -0.279 [-0.549, -0.009] | -0.02488 | -2.02 | 0.043* | not applied (n < 1000) | 0.365 | -6.0 | -8.0 | 0.0453 | 0.0422 |
| GMI (%) | 685 | -0.279 [-0.549, -0.009] | -1.04 | -2.02 | 0.043* | not applied (n < 1000) | 0.365 | -6.0 | -8.0 | 0.0453 | 0.0422 |
| Nocturnal mean 00-06h (mg/dL) | 685 | -0.263 [-0.514, -0.013] | -0.02063 | -2.06 | 0.039* | not applied (n < 1000) | 0.361 | -5.0 | -7.0 | 0.0419 | 0.0422 |
| Glucose SD, pooled (mg/dL) | 685 | -0.015 [-0.210, +0.180] | -0.003898 | -0.15 | 0.883 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0395 | 0.0422 |
| Avg. daily SD (mg/dL) | 685 | -0.023 [-0.218, +0.171] | -0.006209 | -0.23 | 0.816 | not applied (n < 1000) | 0.969 | +1.9 | -0.1 | 0.0396 | 0.0422 |
| CV (%) | 685 | +0.112 [-0.090, +0.314] | 0.0406 | 1.09 | 0.278 | not applied (n < 1000) | 0.739 | +0.7 | -1.3 | 0.0403 | 0.0422 |
| Mean / SD ratio | 685 | -0.151 [-0.375, +0.072] | -0.134 | -1.33 | 0.184 | not applied (n < 1000) | 0.612 | -0.4 | -2.4 | 0.0405 | 0.0422 |
| Avg. daily mean / SD | 685 | -0.122 [-0.330, +0.086] | -0.08746 | -1.15 | 0.251 | not applied (n < 1000) | 0.739 | +0.4 | -1.6 | 0.0393 | 0.0422 |
| MAG (mg/dL/h) | 685 | +0.027 [-0.153, +0.207] | 0.003995 | 0.29 | 0.770 | not applied (n < 1000) | 0.968 | +1.9 | -0.1 | 0.0399 | 0.0422 |
| Avg. daily range (mg/dL) | 685 | -0.021 [-0.209, +0.167] | -0.001308 | -0.22 | 0.825 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0394 | 0.0422 |
| SD of daily means (mg/dL) | 685 | -0.072 [-0.255, +0.111] | -0.03211 | -0.77 | 0.440 | not applied (n < 1000) | 0.883 | +1.5 | -0.5 | 0.0410 | 0.0422 |
| Time in range 70-180, pooled (%) | 685 | +0.250 [-0.079, +0.579] | 0.09312 | 1.49 | 0.136 | not applied (n < 1000) | 0.557 | -4.5 | -6.5 | 0.0414 | 0.0422 |
| Avg. daily time in range 70-180 (%) | 685 | +0.255 [-0.071, +0.580] | 0.09708 | 1.53 | 0.125 | not applied (n < 1000) | 0.557 | -4.8 | -6.8 | 0.0421 | 0.0422 |
| Time 54-69, pooled (%) | 685 | +0.040 [-0.088, +0.169] | 0.07737 | 0.62 | 0.538 | not applied (n < 1000) | 0.918 | +1.8 | -0.2 | 0.0419 | 0.0422 |
| Avg. daily time 54-69 (%) | 685 | +0.039 [-0.090, +0.168] | 0.07285 | 0.60 | 0.551 | not applied (n < 1000) | 0.918 | +1.8 | -0.2 | 0.0416 | 0.0422 |
| Time < 70, pooled (%) | 685 | +0.040 [-0.088, +0.169] | 0.07737 | 0.62 | 0.538 | not applied (n < 1000) | 0.918 | +1.8 | -0.2 | 0.0419 | 0.0422 |
| Avg. daily time < 70 (%) | 685 | +0.039 [-0.090, +0.168] | 0.07285 | 0.60 | 0.551 | not applied (n < 1000) | 0.918 | +1.8 | -0.2 | 0.0416 | 0.0422 |
| Time 181-250, pooled (%) | 685 | -0.257 [-0.588, +0.075] | -0.09498 | -1.52 | 0.129 | not applied (n < 1000) | 0.557 | -4.9 | -6.9 | 0.0418 | 0.0422 |
| Avg. daily time 181-250 (%) | 685 | -0.262 [-0.590, +0.066] | -0.09918 | -1.57 | 0.117 | not applied (n < 1000) | 0.556 | -5.2 | -7.2 | 0.0427 | 0.0422 |
| Time > 180, pooled (%) | 685 | -0.257 [-0.588, +0.075] | -0.09498 | -1.52 | 0.129 | not applied (n < 1000) | 0.557 | -4.9 | -6.9 | 0.0418 | 0.0422 |
| Avg. daily time > 180 (%) | 685 | -0.262 [-0.590, +0.066] | -0.09918 | -1.57 | 0.117 | not applied (n < 1000) | 0.556 | -5.2 | -7.2 | 0.0427 | 0.0422 |
| Nocturnal time > 180 (%) | 685 | -0.070 [-0.310, +0.170] | -0.02292 | -0.57 | 0.566 | not applied (n < 1000) | 0.918 | +1.5 | -0.5 | 0.0364 | 0.0422 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 685; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 685 | -0.023 [-0.391, +0.344] | -0.07056 | -0.13 | 0.900 | not applied (n < 1000) | 0.972 | +2.0 | +0.0 | 0.0241 | 0.0250 |
| Mean glucose (mg/dL) | 685 | -0.093 [-0.449, +0.264] | -0.008274 | -0.51 | 0.610 | not applied (n < 1000) | 0.918 | +1.7 | -0.3 | 0.0238 | 0.0250 |
| GMI (%) | 685 | -0.093 [-0.449, +0.264] | -0.3459 | -0.51 | 0.610 | not applied (n < 1000) | 0.918 | +1.7 | -0.3 | 0.0238 | 0.0250 |
| Nocturnal mean 00-06h (mg/dL) | 685 | -0.032 [-0.405, +0.341] | -0.002501 | -0.17 | 0.867 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0233 | 0.0250 |
| Glucose SD, pooled (mg/dL) | 685 | -0.011 [-0.360, +0.338] | -0.002851 | -0.06 | 0.952 | not applied (n < 1000) | 0.989 | +2.0 | +0.0 | 0.0197 | 0.0250 |
| Avg. daily SD (mg/dL) | 685 | -0.062 [-0.414, +0.290] | -0.01663 | -0.34 | 0.731 | not applied (n < 1000) | 0.951 | +1.9 | -0.1 | 0.0202 | 0.0250 |
| CV (%) | 685 | +0.036 [-0.300, +0.371] | 0.01289 | 0.21 | 0.836 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0188 | 0.0250 |
| Mean / SD ratio | 685 | -0.029 [-0.354, +0.296] | -0.0256 | -0.17 | 0.861 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0196 | 0.0250 |
| Avg. daily mean / SD | 685 | +0.086 [-0.254, +0.425] | 0.06146 | 0.49 | 0.621 | not applied (n < 1000) | 0.921 | +1.7 | -0.2 | 0.0205 | 0.0250 |
| MAG (mg/dL/h) | 685 | +0.068 [-0.254, +0.390] | 0.01006 | 0.41 | 0.680 | not applied (n < 1000) | 0.947 | +1.8 | -0.1 | 0.0233 | 0.0250 |
| Avg. daily range (mg/dL) | 685 | -0.054 [-0.383, +0.274] | -0.003353 | -0.32 | 0.745 | not applied (n < 1000) | 0.951 | +1.9 | -0.1 | 0.0190 | 0.0250 |
| SD of daily means (mg/dL) | 685 | +0.089 [-0.238, +0.416] | 0.0395 | 0.53 | 0.595 | not applied (n < 1000) | 0.918 | +1.7 | -0.3 | 0.0208 | 0.0250 |
| Time in range 70-180, pooled (%) | 685 | -0.061 [-0.419, +0.297] | -0.0227 | -0.33 | 0.739 | not applied (n < 1000) | 0.951 | +1.9 | -0.1 | 0.0214 | 0.0250 |
| Avg. daily time in range 70-180 (%) | 685 | -0.020 [-0.381, +0.342] | -0.007433 | -0.11 | 0.916 | not applied (n < 1000) | 0.972 | +2.0 | +0.0 | 0.0216 | 0.0250 |
| Time 54-69, pooled (%) | 685 | -0.078 [-0.415, +0.258] | -0.1499 | -0.46 | 0.649 | not applied (n < 1000) | 0.946 | +1.8 | -0.2 | 0.0219 | 0.0250 |
| Avg. daily time 54-69 (%) | 685 | -0.071 [-0.424, +0.281] | -0.1325 | -0.40 | 0.691 | not applied (n < 1000) | 0.951 | +1.8 | -0.2 | 0.0217 | 0.0250 |
| Time < 70, pooled (%) | 685 | -0.078 [-0.415, +0.258] | -0.1499 | -0.46 | 0.649 | not applied (n < 1000) | 0.946 | +1.8 | -0.2 | 0.0219 | 0.0250 |
| Avg. daily time < 70 (%) | 685 | -0.071 [-0.424, +0.281] | -0.1325 | -0.40 | 0.691 | not applied (n < 1000) | 0.951 | +1.8 | -0.2 | 0.0217 | 0.0250 |
| Time 181-250, pooled (%) | 685 | +0.076 [-0.281, +0.433] | 0.02806 | 0.42 | 0.677 | not applied (n < 1000) | 0.947 | +1.8 | -0.2 | 0.0217 | 0.0250 |
| Avg. daily time 181-250 (%) | 685 | +0.034 [-0.327, +0.396] | 0.01291 | 0.18 | 0.853 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0215 | 0.0250 |
| Time > 180, pooled (%) | 685 | +0.076 [-0.281, +0.433] | 0.02806 | 0.42 | 0.677 | not applied (n < 1000) | 0.947 | +1.8 | -0.2 | 0.0217 | 0.0250 |
| Avg. daily time > 180 (%) | 685 | +0.034 [-0.327, +0.396] | 0.01291 | 0.18 | 0.853 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.0215 | 0.0250 |
| Nocturnal time > 180 (%) | 685 | +0.384 [+0.035, +0.733] | 0.1253 | 2.16 | 0.031* | not applied (n < 1000) | 0.323 | -3.0 | -5.0 | 0.0330 | 0.0250 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 685; events = 105; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 685 | OR 1.011 [0.809, 1.263] | 0.03144 | 0.09 | 0.927 | not applied (n < 1000) | 0.975 | +2.0 | +0.0 | 0.6394 | 0.6413 |
| Mean glucose (mg/dL) | 685 | OR 1.059 [0.854, 1.313] | 0.005113 | 0.52 | 0.601 | not applied (n < 1000) | 0.918 | +1.7 | -0.3 | 0.6352 | 0.6413 |
| GMI (%) | 685 | OR 1.059 [0.854, 1.313] | 0.2137 | 0.52 | 0.601 | not applied (n < 1000) | 0.918 | +1.7 | -0.3 | 0.6352 | 0.6413 |
| Nocturnal mean 00-06h (mg/dL) | 685 | OR 1.191 [0.963, 1.474] | 0.01369 | 1.61 | 0.108 | not applied (n < 1000) | 0.556 | -0.6 | -2.5 | 0.6446 | 0.6413 |
| Glucose SD, pooled (mg/dL) | 685 | OR 1.009 [0.810, 1.256] | 0.00231 | 0.08 | 0.938 | not applied (n < 1000) | 0.981 | +2.0 | +0.0 | 0.6328 | 0.6413 |
| Avg. daily SD (mg/dL) | 685 | OR 0.999 [0.801, 1.246] | -0.0001946 | -0.01 | 0.995 | not applied (n < 1000) | 0.995 | +2.0 | +0.0 | 0.6339 | 0.6413 |
| CV (%) | 685 | OR 0.978 [0.785, 1.219] | -0.008085 | -0.20 | 0.843 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.6317 | 0.6413 |
| Mean / SD ratio | 685 | OR 1.022 [0.820, 1.274] | 0.01943 | 0.20 | 0.845 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.6335 | 0.6413 |
| Avg. daily mean / SD | 685 | OR 1.048 [0.842, 1.304] | 0.03384 | 0.42 | 0.672 | not applied (n < 1000) | 0.947 | +1.8 | -0.2 | 0.6328 | 0.6413 |
| MAG (mg/dL/h) | 685 | OR 1.037 [0.839, 1.282] | 0.005398 | 0.34 | 0.736 | not applied (n < 1000) | 0.951 | +1.9 | -0.1 | 0.6396 | 0.6413 |
| Avg. daily range (mg/dL) | 685 | OR 0.982 [0.786, 1.226] | -0.001121 | -0.16 | 0.872 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.6307 | 0.6413 |
| SD of daily means (mg/dL) | 685 | OR 1.086 [0.881, 1.338] | 0.03657 | 0.77 | 0.441 | not applied (n < 1000) | 0.883 | +1.4 | -0.6 | 0.6382 | 0.6413 |
| Time in range 70-180, pooled (%) | 685 | OR 0.852 [0.708, 1.027] | -0.05948 | -1.68 | 0.093 | not applied (n < 1000) | 0.556 | -0.7 | -2.7 | 0.6428 | 0.6413 |
| Avg. daily time in range 70-180 (%) | 685 | OR 0.858 [0.711, 1.034] | -0.05853 | -1.61 | 0.107 | not applied (n < 1000) | 0.556 | -0.5 | -2.5 | 0.6427 | 0.6413 |
| Time 54-69, pooled (%) | 685 | OR 1.013 [0.806, 1.273] | 0.02493 | 0.11 | 0.911 | not applied (n < 1000) | 0.972 | +2.0 | -0.0 | 0.6401 | 0.6413 |
| Avg. daily time 54-69 (%) | 685 | OR 1.023 [0.816, 1.283] | 0.04235 | 0.20 | 0.843 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.6399 | 0.6413 |
| Time < 70, pooled (%) | 685 | OR 1.013 [0.806, 1.273] | 0.02493 | 0.11 | 0.911 | not applied (n < 1000) | 0.972 | +2.0 | -0.0 | 0.6401 | 0.6413 |
| Avg. daily time < 70 (%) | 685 | OR 1.023 [0.816, 1.283] | 0.04235 | 0.20 | 0.843 | not applied (n < 1000) | 0.969 | +2.0 | -0.0 | 0.6399 | 0.6413 |
| Time 181-250, pooled (%) | 685 | OR 1.170 [0.971, 1.409] | 0.05798 | 1.65 | 0.098 | not applied (n < 1000) | 0.556 | -0.6 | -2.6 | 0.6424 | 0.6413 |
| Avg. daily time 181-250 (%) | 685 | OR 1.161 [0.963, 1.400] | 0.0565 | 1.57 | 0.117 | not applied (n < 1000) | 0.556 | -0.3 | -2.3 | 0.6426 | 0.6413 |
| Time > 180, pooled (%) | 685 | OR 1.170 [0.971, 1.409] | 0.05798 | 1.65 | 0.098 | not applied (n < 1000) | 0.556 | -0.6 | -2.6 | 0.6424 | 0.6413 |
| Avg. daily time > 180 (%) | 685 | OR 1.161 [0.963, 1.400] | 0.0565 | 1.57 | 0.117 | not applied (n < 1000) | 0.556 | -0.3 | -2.3 | 0.6426 | 0.6413 |
| Nocturnal time > 180 (%) | 685 | OR 1.343 [1.096, 1.645] | 0.09613 | 2.84 | 0.004** | not applied (n < 1000) | 0.102 | -8.2 | -10.2 | 0.6528 | 0.6413 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 674; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 674 | +0.028 [-0.039, +0.095] | 0.08395 | 0.82 | 0.413 | not applied (n < 1000) | 0.883 | +1.3 | +0.0 | 0.0953 | 0.0979 |
| Mean glucose (mg/dL) | 674 | -0.035 [-0.098, +0.028] | -0.00313 | -1.10 | 0.273 | not applied (n < 1000) | 0.739 | +0.8 | -0.5 | 0.0975 | 0.0979 |
| GMI (%) | 674 | -0.035 [-0.098, +0.028] | -0.1309 | -1.10 | 0.273 | not applied (n < 1000) | 0.739 | +0.8 | -0.5 | 0.0975 | 0.0979 |
| Nocturnal mean 00-06h (mg/dL) | 674 | -0.032 [-0.096, +0.033] | -0.002492 | -0.97 | 0.333 | not applied (n < 1000) | 0.814 | +1.0 | -0.2 | 0.0969 | 0.0979 |
| Glucose SD, pooled (mg/dL) | 674 | +0.001 [-0.060, +0.063] | 0.0003853 | 0.05 | 0.963 | not applied (n < 1000) | 0.990 | +2.0 | +0.7 | 0.0954 | 0.0979 |
| Avg. daily SD (mg/dL) | 674 | -0.006 [-0.067, +0.055] | -0.00156 | -0.19 | 0.852 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0952 | 0.0979 |
| CV (%) | 674 | +0.018 [-0.044, +0.081] | 0.006705 | 0.58 | 0.564 | not applied (n < 1000) | 0.918 | +1.7 | +0.4 | 0.0945 | 0.0979 |
| Mean / SD ratio | 674 | -0.012 [-0.074, +0.050] | -0.01069 | -0.38 | 0.703 | not applied (n < 1000) | 0.951 | +1.9 | +0.6 | 0.0940 | 0.0979 |
| Avg. daily mean / SD | 674 | -0.005 [-0.067, +0.057] | -0.00357 | -0.16 | 0.875 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0926 | 0.0979 |
| MAG (mg/dL/h) | 674 | +0.025 [-0.041, +0.091] | 0.003735 | 0.75 | 0.453 | not applied (n < 1000) | 0.890 | +1.4 | +0.1 | 0.0957 | 0.0979 |
| Avg. daily range (mg/dL) | 674 | -0.017 [-0.076, +0.041] | -0.00108 | -0.58 | 0.561 | not applied (n < 1000) | 0.918 | +1.7 | +0.4 | 0.0943 | 0.0979 |
| SD of daily means (mg/dL) | 674 | +0.020 [-0.046, +0.085] | 0.008823 | 0.60 | 0.551 | not applied (n < 1000) | 0.918 | +1.6 | +0.3 | 0.0960 | 0.0979 |
| Time in range 70-180, pooled (%) | 674 | +0.025 [-0.035, +0.084] | 0.009145 | 0.82 | 0.415 | not applied (n < 1000) | 0.883 | +1.4 | +0.1 | 0.0966 | 0.0979 |
| Avg. daily time in range 70-180 (%) | 674 | +0.032 [-0.027, +0.090] | 0.0121 | 1.07 | 0.286 | not applied (n < 1000) | 0.748 | +1.0 | -0.3 | 0.0968 | 0.0979 |
| Time 54-69, pooled (%) | 674 | +0.006 [-0.049, +0.061] | 0.01136 | 0.21 | 0.831 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0968 | 0.0979 |
| Avg. daily time 54-69 (%) | 674 | +0.006 [-0.049, +0.062] | 0.01153 | 0.22 | 0.824 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0966 | 0.0979 |
| Time < 70, pooled (%) | 674 | +0.006 [-0.049, +0.061] | 0.01136 | 0.21 | 0.831 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0968 | 0.0979 |
| Avg. daily time < 70 (%) | 674 | +0.006 [-0.049, +0.062] | 0.01153 | 0.22 | 0.824 | not applied (n < 1000) | 0.969 | +2.0 | +0.7 | 0.0966 | 0.0979 |
| Time 181-250, pooled (%) | 674 | -0.026 [-0.085, +0.034] | -0.00948 | -0.85 | 0.398 | not applied (n < 1000) | 0.875 | +1.4 | +0.1 | 0.0966 | 0.0979 |
| Avg. daily time 181-250 (%) | 674 | -0.033 [-0.092, +0.026] | -0.01248 | -1.10 | 0.272 | not applied (n < 1000) | 0.739 | +0.9 | -0.4 | 0.0968 | 0.0979 |
| Time > 180, pooled (%) | 674 | -0.026 [-0.085, +0.034] | -0.00948 | -0.85 | 0.398 | not applied (n < 1000) | 0.875 | +1.4 | +0.1 | 0.0966 | 0.0979 |
| Avg. daily time > 180 (%) | 674 | -0.033 [-0.092, +0.026] | -0.01248 | -1.10 | 0.272 | not applied (n < 1000) | 0.739 | +0.9 | -0.4 | 0.0968 | 0.0979 |
| Nocturnal time > 180 (%) | 674 | +0.019 [-0.053, +0.091] | 0.006129 | 0.51 | 0.608 | not applied (n < 1000) | 0.918 | +1.6 | +0.4 | 0.0924 | 0.0979 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 674; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 674 | +0.045 [-0.099, +0.188] | 0.1341 | 0.61 | 0.542 | not applied (n < 1000) | 0.918 | +1.6 | +0.0 | 0.3082 | 0.3110 |
| Mean glucose (mg/dL) | 674 | +0.036 [-0.105, +0.177] | 0.003223 | 0.50 | 0.616 | not applied (n < 1000) | 0.918 | +1.8 | +0.1 | 0.3104 | 0.3110 |
| GMI (%) | 674 | +0.036 [-0.105, +0.177] | 0.1347 | 0.50 | 0.616 | not applied (n < 1000) | 0.918 | +1.8 | +0.1 | 0.3104 | 0.3110 |
| Nocturnal mean 00-06h (mg/dL) | 674 | +0.013 [-0.123, +0.149] | 0.000999 | 0.18 | 0.854 | not applied (n < 1000) | 0.969 | +2.0 | +0.3 | 0.3102 | 0.3110 |
| Glucose SD, pooled (mg/dL) | 674 | -0.066 [-0.209, +0.076] | -0.01774 | -0.92 | 0.359 | not applied (n < 1000) | 0.821 | +1.1 | -0.5 | 0.3077 | 0.3110 |
| Avg. daily SD (mg/dL) | 674 | -0.067 [-0.208, +0.074] | -0.018 | -0.93 | 0.355 | not applied (n < 1000) | 0.818 | +1.1 | -0.5 | 0.3079 | 0.3110 |
| CV (%) | 674 | -0.091 [-0.226, +0.044] | -0.03317 | -1.32 | 0.186 | not applied (n < 1000) | 0.612 | +0.4 | -1.3 | 0.3060 | 0.3110 |
| Mean / SD ratio | 674 | +0.077 [-0.058, +0.211] | 0.06827 | 1.12 | 0.263 | not applied (n < 1000) | 0.739 | +0.8 | -0.8 | 0.3058 | 0.3110 |
| Avg. daily mean / SD | 674 | +0.063 [-0.068, +0.194] | 0.0453 | 0.94 | 0.345 | not applied (n < 1000) | 0.818 | +1.2 | -0.4 | 0.3056 | 0.3110 |
| MAG (mg/dL/h) | 674 | +0.048 [-0.103, +0.199] | 0.007122 | 0.62 | 0.533 | not applied (n < 1000) | 0.918 | +1.5 | -0.1 | 0.3095 | 0.3110 |
| Avg. daily range (mg/dL) | 674 | -0.051 [-0.191, +0.090] | -0.003149 | -0.71 | 0.478 | not applied (n < 1000) | 0.917 | +1.5 | -0.1 | 0.3071 | 0.3110 |
| SD of daily means (mg/dL) | 674 | -0.020 [-0.175, +0.136] | -0.008743 | -0.25 | 0.803 | not applied (n < 1000) | 0.969 | +1.9 | +0.3 | 0.3074 | 0.3110 |
| Time in range 70-180, pooled (%) | 674 | -0.007 [-0.128, +0.114] | -0.002732 | -0.12 | 0.905 | not applied (n < 1000) | 0.972 | +2.0 | +0.4 | 0.3101 | 0.3110 |
| Avg. daily time in range 70-180 (%) | 674 | -0.002 [-0.127, +0.122] | -0.0007897 | -0.03 | 0.974 | not applied (n < 1000) | 0.990 | +2.0 | +0.4 | 0.3101 | 0.3110 |
| Time 54-69, pooled (%) | 674 | -0.009 [-0.166, +0.147] | -0.01793 | -0.12 | 0.906 | not applied (n < 1000) | 0.972 | +2.0 | +0.3 | 0.3087 | 0.3110 |
| Avg. daily time 54-69 (%) | 674 | +0.001 [-0.149, +0.150] | 0.001215 | 0.01 | 0.993 | not applied (n < 1000) | 0.995 | +2.0 | +0.4 | 0.3089 | 0.3110 |
| Time < 70, pooled (%) | 674 | -0.009 [-0.166, +0.147] | -0.01793 | -0.12 | 0.906 | not applied (n < 1000) | 0.972 | +2.0 | +0.3 | 0.3087 | 0.3110 |
| Avg. daily time < 70 (%) | 674 | +0.001 [-0.149, +0.150] | 0.001215 | 0.01 | 0.993 | not applied (n < 1000) | 0.995 | +2.0 | +0.4 | 0.3089 | 0.3110 |
| Time 181-250, pooled (%) | 674 | +0.009 [-0.115, +0.133] | 0.003383 | 0.15 | 0.885 | not applied (n < 1000) | 0.969 | +2.0 | +0.3 | 0.3099 | 0.3110 |
| Avg. daily time 181-250 (%) | 674 | +0.002 [-0.125, +0.129] | 0.0007314 | 0.03 | 0.976 | not applied (n < 1000) | 0.990 | +2.0 | +0.4 | 0.3099 | 0.3110 |
| Time > 180, pooled (%) | 674 | +0.009 [-0.115, +0.133] | 0.003383 | 0.15 | 0.885 | not applied (n < 1000) | 0.969 | +2.0 | +0.3 | 0.3099 | 0.3110 |
| Avg. daily time > 180 (%) | 674 | +0.002 [-0.125, +0.129] | 0.0007314 | 0.03 | 0.976 | not applied (n < 1000) | 0.990 | +2.0 | +0.4 | 0.3099 | 0.3110 |
| Nocturnal time > 180 (%) | 674 | +0.063 [-0.067, +0.194] | 0.0205 | 0.95 | 0.341 | not applied (n < 1000) | 0.818 | +1.2 | -0.4 | 0.3081 | 0.3110 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 674; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 674 | +0.149 [-0.308, +0.606] | 0.4478 | 0.64 | 0.522 | not applied (n < 1000) | 0.918 | +1.6 | +0.0 | 0.2406 | 0.2411 |
| Mean glucose (mg/dL) | 674 | +0.120 [-0.307, +0.548] | 0.01075 | 0.55 | 0.581 | not applied (n < 1000) | 0.918 | +1.7 | +0.1 | 0.2392 | 0.2411 |
| GMI (%) | 674 | +0.120 [-0.307, +0.548] | 0.4495 | 0.55 | 0.581 | not applied (n < 1000) | 0.918 | +1.7 | +0.1 | 0.2392 | 0.2411 |
| Nocturnal mean 00-06h (mg/dL) | 674 | +0.180 [-0.264, +0.623] | 0.01408 | 0.79 | 0.427 | not applied (n < 1000) | 0.883 | +1.4 | -0.2 | 0.2385 | 0.2411 |
| Glucose SD, pooled (mg/dL) | 674 | +0.408 [-0.028, +0.843] | 0.1088 | 1.83 | 0.067 | not applied (n < 1000) | 0.494 | -1.4 | -3.0 | 0.2429 | 0.2411 |
| Avg. daily SD (mg/dL) | 674 | +0.424 [-0.013, +0.860] | 0.1146 | 1.90 | 0.057 | not applied (n < 1000) | 0.467 | -1.7 | -3.2 | 0.2423 | 0.2411 |
| CV (%) | 674 | +0.397 [-0.046, +0.840] | 0.1447 | 1.76 | 0.079 | not applied (n < 1000) | 0.554 | -1.3 | -2.8 | 0.2432 | 0.2411 |
| Mean / SD ratio | 674 | -0.296 [-0.750, +0.159] | -0.2631 | -1.28 | 0.202 | not applied (n < 1000) | 0.651 | +0.2 | -1.4 | 0.2416 | 0.2411 |
| Avg. daily mean / SD | 674 | -0.395 [-0.866, +0.076] | -0.2842 | -1.64 | 0.100 | not applied (n < 1000) | 0.556 | -1.2 | -2.8 | 0.2423 | 0.2411 |
| MAG (mg/dL/h) | 674 | -0.097 [-0.546, +0.352] | -0.01442 | -0.42 | 0.671 | not applied (n < 1000) | 0.947 | +1.8 | +0.2 | 0.2401 | 0.2411 |
| Avg. daily range (mg/dL) | 674 | +0.250 [-0.196, +0.695] | 0.01546 | 1.10 | 0.272 | not applied (n < 1000) | 0.739 | +0.7 | -0.9 | 0.2404 | 0.2411 |
| SD of daily means (mg/dL) | 674 | +0.246 [-0.220, +0.712] | 0.1088 | 1.03 | 0.301 | not applied (n < 1000) | 0.769 | +0.8 | -0.8 | 0.2423 | 0.2411 |
| Time in range 70-180, pooled (%) | 674 | -0.231 [-0.634, +0.172] | -0.08586 | -1.12 | 0.262 | not applied (n < 1000) | 0.739 | +0.9 | -0.7 | 0.2405 | 0.2411 |
| Avg. daily time in range 70-180 (%) | 674 | -0.250 [-0.653, +0.154] | -0.09498 | -1.21 | 0.225 | not applied (n < 1000) | 0.704 | +0.7 | -0.9 | 0.2409 | 0.2411 |
| Time 54-69, pooled (%) | 674 | +0.084 [-0.377, +0.544] | 0.1591 | 0.36 | 0.722 | not applied (n < 1000) | 0.951 | +1.9 | +0.3 | 0.2380 | 0.2411 |
| Avg. daily time 54-69 (%) | 674 | +0.058 [-0.402, +0.517] | 0.1059 | 0.25 | 0.806 | not applied (n < 1000) | 0.969 | +1.9 | +0.4 | 0.2382 | 0.2411 |
| Time < 70, pooled (%) | 674 | +0.084 [-0.377, +0.544] | 0.1591 | 0.36 | 0.722 | not applied (n < 1000) | 0.951 | +1.9 | +0.3 | 0.2380 | 0.2411 |
| Avg. daily time < 70 (%) | 674 | +0.058 [-0.402, +0.517] | 0.1059 | 0.25 | 0.806 | not applied (n < 1000) | 0.969 | +1.9 | +0.4 | 0.2382 | 0.2411 |
| Time 181-250, pooled (%) | 674 | +0.214 [-0.193, +0.621] | 0.07893 | 1.03 | 0.303 | not applied (n < 1000) | 0.769 | +1.1 | -0.5 | 0.2403 | 0.2411 |
| Avg. daily time 181-250 (%) | 674 | +0.238 [-0.170, +0.645] | 0.08966 | 1.14 | 0.254 | not applied (n < 1000) | 0.739 | +0.8 | -0.7 | 0.2407 | 0.2411 |
| Time > 180, pooled (%) | 674 | +0.214 [-0.193, +0.621] | 0.07893 | 1.03 | 0.303 | not applied (n < 1000) | 0.769 | +1.1 | -0.5 | 0.2403 | 0.2411 |
| Avg. daily time > 180 (%) | 674 | +0.238 [-0.170, +0.645] | 0.08966 | 1.14 | 0.254 | not applied (n < 1000) | 0.739 | +0.8 | -0.7 | 0.2407 | 0.2411 |
| Nocturnal time > 180 (%) | 674 | +0.254 [-0.059, +0.567] | 0.08218 | 1.59 | 0.112 | not applied (n < 1000) | 0.556 | +0.7 | -0.9 | 0.2410 | 0.2411 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 674; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 674 | -0.448 [-1.791, +0.895] | -1.344 | -0.65 | 0.514 | not applied (n < 1000) | 0.918 | +1.5 | +0.0 | -0.0174 | -0.0148 |
| Mean glucose (mg/dL) | 674 | -1.410 [-2.639, -0.182] | -0.1258 | -2.25 | 0.024* | not applied (n < 1000) | 0.304 | -3.5 | -4.9 | -0.0093 | -0.0148 |
| GMI (%) | 674 | -1.410 [-2.639, -0.182] | -5.261 | -2.25 | 0.024* | not applied (n < 1000) | 0.304 | -3.5 | -4.9 | -0.0093 | -0.0148 |
| Nocturnal mean 00-06h (mg/dL) | 674 | -1.086 [-2.250, +0.078] | -0.08502 | -1.83 | 0.067 | not applied (n < 1000) | 0.494 | -1.2 | -2.6 | -0.0139 | -0.0148 |
| Glucose SD, pooled (mg/dL) | 674 | -1.511 [-2.738, -0.283] | -0.4033 | -2.41 | 0.016* | not applied (n < 1000) | 0.268 | -4.4 | -5.8 | -0.0066 | -0.0148 |
| Avg. daily SD (mg/dL) | 674 | -1.538 [-2.757, -0.319] | -0.4158 | -2.47 | 0.013* | not applied (n < 1000) | 0.254 | -4.6 | -6.1 | -0.0053 | -0.0148 |
| CV (%) | 674 | -0.891 [-2.097, +0.314] | -0.3249 | -1.45 | 0.147 | not applied (n < 1000) | 0.558 | -0.2 | -1.7 | -0.0136 | -0.0148 |
| Mean / SD ratio | 674 | +1.035 [-0.183, +2.253] | 0.9203 | 1.67 | 0.096 | not applied (n < 1000) | 0.556 | -1.0 | -2.5 | -0.0131 | -0.0148 |
| Avg. daily mean / SD | 674 | +1.017 [-0.213, +2.246] | 0.7318 | 1.62 | 0.105 | not applied (n < 1000) | 0.556 | -0.9 | -2.4 | -0.0123 | -0.0148 |
| MAG (mg/dL/h) | 674 | +0.073 [-1.100, +1.246] | 0.01085 | 0.12 | 0.903 | not applied (n < 1000) | 0.972 | +2.0 | +0.5 | -0.0178 | -0.0148 |
| Avg. daily range (mg/dL) | 674 | -0.925 [-2.110, +0.259] | -0.05726 | -1.53 | 0.126 | not applied (n < 1000) | 0.557 | -0.4 | -1.9 | -0.0132 | -0.0148 |
| SD of daily means (mg/dL) | 674 | -0.451 [-1.737, +0.836] | -0.1995 | -0.69 | 0.492 | not applied (n < 1000) | 0.918 | +1.4 | -0.0 | -0.0172 | -0.0148 |
| Time in range 70-180, pooled (%) | 674 | +0.868 [-0.386, +2.121] | 0.3227 | 1.36 | 0.175 | not applied (n < 1000) | 0.599 | -0.1 | -1.6 | -0.0169 | -0.0148 |
| Avg. daily time in range 70-180 (%) | 674 | +0.925 [-0.322, +2.172] | 0.3519 | 1.45 | 0.146 | not applied (n < 1000) | 0.558 | -0.4 | -1.9 | -0.0166 | -0.0148 |
| Time 54-69, pooled (%) | 674 | +0.280 [-1.349, +1.909] | 0.5334 | 0.34 | 0.736 | not applied (n < 1000) | 0.951 | +1.8 | +0.3 | -0.0190 | -0.0148 |
| Avg. daily time 54-69 (%) | 674 | +0.134 [-1.472, +1.741] | 0.2475 | 0.16 | 0.870 | not applied (n < 1000) | 0.969 | +1.9 | +0.5 | -0.0197 | -0.0148 |
| Time < 70, pooled (%) | 674 | +0.280 [-1.349, +1.909] | 0.5334 | 0.34 | 0.736 | not applied (n < 1000) | 0.951 | +1.8 | +0.3 | -0.0190 | -0.0148 |
| Avg. daily time < 70 (%) | 674 | +0.134 [-1.472, +1.741] | 0.2475 | 0.16 | 0.870 | not applied (n < 1000) | 0.969 | +1.9 | +0.5 | -0.0197 | -0.0148 |
| Time 181-250, pooled (%) | 674 | -0.920 [-2.182, +0.342] | -0.3396 | -1.43 | 0.153 | not applied (n < 1000) | 0.567 | -0.4 | -1.8 | -0.0160 | -0.0148 |
| Avg. daily time 181-250 (%) | 674 | -0.952 [-2.211, +0.307] | -0.3593 | -1.48 | 0.138 | not applied (n < 1000) | 0.557 | -0.5 | -2.0 | -0.0158 | -0.0148 |
| Time > 180, pooled (%) | 674 | -0.920 [-2.182, +0.342] | -0.3396 | -1.43 | 0.153 | not applied (n < 1000) | 0.567 | -0.4 | -1.8 | -0.0160 | -0.0148 |
| Avg. daily time > 180 (%) | 674 | -0.952 [-2.211, +0.307] | -0.3593 | -1.48 | 0.138 | not applied (n < 1000) | 0.557 | -0.5 | -2.0 | -0.0158 | -0.0148 |
| Nocturnal time > 180 (%) | 674 | -0.819 [-1.964, +0.326] | -0.2651 | -1.40 | 0.161 | not applied (n < 1000) | 0.574 | +0.1 | -1.3 | -0.0197 | -0.0148 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Steps per wear-day
*n = 593; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 593 | +361.065 [+40.298, +681.832] | 1074 | 2.21 | 0.027* | not applied (n < 1000) | 0.304 | -3.3 | +0.0 | 0.0719 | 0.0678 |
| Mean glucose (mg/dL) | 593 | -4.874 [-306.435, +296.686] | -0.4346 | -0.03 | 0.975 | not applied (n < 1000) | 0.990 | +2.0 | +5.3 | 0.0632 | 0.0678 |
| GMI (%) | 593 | -4.874 [-306.435, +296.686] | -18.17 | -0.03 | 0.975 | not applied (n < 1000) | 0.990 | +2.0 | +5.3 | 0.0632 | 0.0678 |
| Nocturnal mean 00-06h (mg/dL) | 593 | +8.905 [-312.947, +330.757] | 0.6873 | 0.05 | 0.957 | not applied (n < 1000) | 0.990 | +2.0 | +5.3 | 0.0620 | 0.0678 |
| Glucose SD, pooled (mg/dL) | 593 | +69.086 [-235.411, +373.582] | 18.35 | 0.44 | 0.657 | not applied (n < 1000) | 0.947 | +1.8 | +5.1 | 0.0649 | 0.0678 |
| Avg. daily SD (mg/dL) | 593 | +32.363 [-269.323, +334.049] | 8.753 | 0.21 | 0.833 | not applied (n < 1000) | 0.969 | +2.0 | +5.2 | 0.0641 | 0.0678 |
| CV (%) | 593 | +36.663 [-254.117, +327.442] | 13.2 | 0.25 | 0.805 | not applied (n < 1000) | 0.969 | +1.9 | +5.2 | 0.0638 | 0.0678 |
| Mean / SD ratio | 593 | -30.800 [-324.926, +263.326] | -27.41 | -0.21 | 0.837 | not applied (n < 1000) | 0.969 | +2.0 | +5.2 | 0.0645 | 0.0678 |
| Avg. daily mean / SD | 593 | -19.795 [-313.803, +274.213] | -14.47 | -0.13 | 0.895 | not applied (n < 1000) | 0.972 | +2.0 | +5.3 | 0.0638 | 0.0678 |
| MAG (mg/dL/h) | 593 | +609.671 [+271.335, +948.006] | 90.83 | 3.53 | 4.1e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -14.2 | -10.9 | 0.0871 | 0.0678 |
| Avg. daily range (mg/dL) | 593 | +139.630 [-153.941, +433.202] | 8.693 | 0.93 | 0.351 | not applied (n < 1000) | 0.818 | +1.2 | +4.5 | 0.0679 | 0.0678 |
| SD of daily means (mg/dL) | 593 | +388.246 [+53.209, +723.283] | 175.1 | 2.27 | 0.023* | not applied (n < 1000) | 0.304 | -4.5 | -1.2 | 0.0757 | 0.0678 |
| Time in range 70-180, pooled (%) | 593 | -4.452 [-323.624, +314.720] | -1.61 | -0.03 | 0.978 | not applied (n < 1000) | 0.990 | +2.0 | +5.3 | 0.0646 | 0.0678 |
| Avg. daily time in range 70-180 (%) | 593 | -12.608 [-325.915, +300.698] | -4.677 | -0.08 | 0.937 | not applied (n < 1000) | 0.981 | +2.0 | +5.3 | 0.0647 | 0.0678 |
| Time 54-69, pooled (%) | 593 | -59.669 [-450.816, +331.477] | -110.8 | -0.30 | 0.765 | not applied (n < 1000) | 0.966 | +1.8 | +5.1 | 0.0645 | 0.0678 |
| Avg. daily time 54-69 (%) | 593 | -79.034 [-480.181, +322.113] | -142.3 | -0.39 | 0.699 | not applied (n < 1000) | 0.951 | +1.7 | +5.0 | 0.0643 | 0.0678 |
| Time < 70, pooled (%) | 593 | -59.669 [-450.816, +331.477] | -110.8 | -0.30 | 0.765 | not applied (n < 1000) | 0.966 | +1.8 | +5.1 | 0.0645 | 0.0678 |
| Avg. daily time < 70 (%) | 593 | -79.034 [-480.181, +322.113] | -142.3 | -0.39 | 0.699 | not applied (n < 1000) | 0.951 | +1.7 | +5.0 | 0.0643 | 0.0678 |
| Time 181-250, pooled (%) | 593 | +16.121 [-300.988, +333.229] | 5.79 | 0.10 | 0.921 | not applied (n < 1000) | 0.972 | +2.0 | +5.3 | 0.0648 | 0.0678 |
| Avg. daily time 181-250 (%) | 593 | +28.965 [-283.517, +341.448] | 10.68 | 0.18 | 0.856 | not applied (n < 1000) | 0.969 | +2.0 | +5.2 | 0.0651 | 0.0678 |
| Time > 180, pooled (%) | 593 | +16.121 [-300.988, +333.229] | 5.79 | 0.10 | 0.921 | not applied (n < 1000) | 0.972 | +2.0 | +5.3 | 0.0648 | 0.0678 |
| Avg. daily time > 180 (%) | 593 | +28.965 [-283.517, +341.448] | 10.68 | 0.18 | 0.856 | not applied (n < 1000) | 0.969 | +2.0 | +5.2 | 0.0651 | 0.0678 |
| Nocturnal time > 180 (%) | 593 | -29.897 [-420.978, +361.184] | -9.357 | -0.15 | 0.881 | not applied (n < 1000) | 0.969 | +2.0 | +5.2 | 0.0618 | 0.0678 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 593; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 593 | +0.933 [-0.103, +1.968] | 2.774 | 1.77 | 0.078 | not applied (n < 1000) | 0.554 | -1.6 | +0.0 | 0.0909 | 0.0887 |
| Mean glucose (mg/dL) | 593 | +0.152 [-0.769, +1.072] | 0.01353 | 0.32 | 0.747 | not applied (n < 1000) | 0.951 | +1.9 | +3.5 | 0.0840 | 0.0887 |
| GMI (%) | 593 | +0.152 [-0.769, +1.072] | 0.5657 | 0.32 | 0.747 | not applied (n < 1000) | 0.951 | +1.9 | +3.5 | 0.0840 | 0.0887 |
| Nocturnal mean 00-06h (mg/dL) | 593 | +0.004 [-0.936, +0.944] | 0.0003139 | 0.01 | 0.993 | not applied (n < 1000) | 0.995 | +2.0 | +3.6 | 0.0830 | 0.0887 |
| Glucose SD, pooled (mg/dL) | 593 | +0.625 [-0.315, +1.565] | 0.1661 | 1.30 | 0.192 | not applied (n < 1000) | 0.625 | +0.3 | +1.9 | 0.0910 | 0.0887 |
| Avg. daily SD (mg/dL) | 593 | +0.565 [-0.384, +1.514] | 0.1528 | 1.17 | 0.243 | not applied (n < 1000) | 0.739 | +0.6 | +2.3 | 0.0900 | 0.0887 |
| CV (%) | 593 | +0.493 [-0.430, +1.416] | 0.1774 | 1.05 | 0.295 | not applied (n < 1000) | 0.766 | +0.9 | +2.6 | 0.0883 | 0.0887 |
| Mean / SD ratio | 593 | -0.469 [-1.407, +0.469] | -0.4172 | -0.98 | 0.327 | not applied (n < 1000) | 0.811 | +1.0 | +2.7 | 0.0886 | 0.0887 |
| Avg. daily mean / SD | 593 | -0.409 [-1.346, +0.528] | -0.2992 | -0.86 | 0.392 | not applied (n < 1000) | 0.875 | +1.3 | +2.9 | 0.0880 | 0.0887 |
| MAG (mg/dL/h) | 593 | +2.150 [+1.155, +3.146] | 0.3204 | 4.23 | 2.3e-05*** | not applied (n < 1000) | 0.004 (q<0.05) | -19.0 | -17.3 | 0.1140 | 0.0887 |
| Avg. daily range (mg/dL) | 593 | +0.988 [+0.031, +1.946] | 0.06153 | 2.02 | 0.043* | not applied (n < 1000) | 0.365 | -2.3 | -0.7 | 0.0946 | 0.0887 |
| SD of daily means (mg/dL) | 593 | +1.056 [+0.080, +2.031] | 0.4762 | 2.12 | 0.034* | not applied (n < 1000) | 0.326 | -3.0 | -1.3 | 0.0943 | 0.0887 |
| Time in range 70-180, pooled (%) | 593 | -0.222 [-1.073, +0.628] | -0.08033 | -0.51 | 0.609 | not applied (n < 1000) | 0.918 | +1.8 | +3.4 | 0.0865 | 0.0887 |
| Avg. daily time in range 70-180 (%) | 593 | -0.293 [-1.162, +0.575] | -0.1088 | -0.66 | 0.508 | not applied (n < 1000) | 0.918 | +1.6 | +3.3 | 0.0868 | 0.0887 |
| Time 54-69, pooled (%) | 593 | -0.349 [-1.267, +0.569] | -0.6485 | -0.75 | 0.456 | not applied (n < 1000) | 0.890 | +1.5 | +3.1 | 0.0853 | 0.0887 |
| Avg. daily time 54-69 (%) | 593 | -0.372 [-1.312, +0.569] | -0.6693 | -0.77 | 0.439 | not applied (n < 1000) | 0.883 | +1.4 | +3.0 | 0.0848 | 0.0887 |
| Time < 70, pooled (%) | 593 | -0.349 [-1.267, +0.569] | -0.6485 | -0.75 | 0.456 | not applied (n < 1000) | 0.890 | +1.5 | +3.1 | 0.0853 | 0.0887 |
| Avg. daily time < 70 (%) | 593 | -0.372 [-1.312, +0.569] | -0.6693 | -0.77 | 0.439 | not applied (n < 1000) | 0.883 | +1.4 | +3.0 | 0.0848 | 0.0887 |
| Time 181-250, pooled (%) | 593 | +0.290 [-0.563, +1.142] | 0.1041 | 0.67 | 0.505 | not applied (n < 1000) | 0.918 | +1.6 | +3.3 | 0.0866 | 0.0887 |
| Avg. daily time 181-250 (%) | 593 | +0.370 [-0.500, +1.240] | 0.1363 | 0.83 | 0.405 | not applied (n < 1000) | 0.875 | +1.4 | +3.1 | 0.0872 | 0.0887 |
| Time > 180, pooled (%) | 593 | +0.290 [-0.563, +1.142] | 0.1041 | 0.67 | 0.505 | not applied (n < 1000) | 0.918 | +1.6 | +3.3 | 0.0866 | 0.0887 |
| Avg. daily time > 180 (%) | 593 | +0.370 [-0.500, +1.240] | 0.1363 | 0.83 | 0.405 | not applied (n < 1000) | 0.875 | +1.4 | +3.1 | 0.0872 | 0.0887 |
| Nocturnal time > 180 (%) | 593 | -0.145 [-1.028, +0.738] | -0.04542 | -0.32 | 0.747 | not applied (n < 1000) | 0.951 | +1.9 | +3.6 | 0.0846 | 0.0887 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 597; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 597 | +0.701 [+0.052, +1.349] | 2.087 | 2.12 | 0.034* | not applied (n < 1000) | 0.326 | -3.0 | +0.0 | 0.1127 | 0.1040 |
| Mean glucose (mg/dL) | 597 | +0.835 [+0.277, +1.393] | 0.0745 | 2.93 | 0.003** | not applied (n < 1000) | 0.083 | -5.4 | -2.4 | 0.1140 | 0.1040 |
| GMI (%) | 597 | +0.835 [+0.277, +1.393] | 3.115 | 2.93 | 0.003** | not applied (n < 1000) | 0.083 | -5.4 | -2.4 | 0.1140 | 0.1040 |
| Nocturnal mean 00-06h (mg/dL) | 597 | +0.975 [+0.407, +1.542] | 0.07498 | 3.37 | 7.6e-04*** | not applied (n < 1000) | 0.025 (q<0.05) | -7.8 | -4.8 | 0.1168 | 0.1040 |
| Glucose SD, pooled (mg/dL) | 597 | +0.562 [-0.088, +1.211] | 0.1485 | 1.69 | 0.090 | not applied (n < 1000) | 0.556 | -1.3 | +1.7 | 0.1049 | 0.1040 |
| Avg. daily SD (mg/dL) | 597 | +0.576 [-0.078, +1.230] | 0.1549 | 1.72 | 0.085 | not applied (n < 1000) | 0.556 | -1.5 | +1.5 | 0.1055 | 0.1040 |
| CV (%) | 597 | +0.131 [-0.513, +0.775] | 0.04695 | 0.40 | 0.690 | not applied (n < 1000) | 0.951 | +1.8 | +4.8 | 0.0982 | 0.1040 |
| Mean / SD ratio | 597 | -0.085 [-0.679, +0.508] | -0.07508 | -0.28 | 0.778 | not applied (n < 1000) | 0.969 | +1.9 | +4.9 | 0.0996 | 0.1040 |
| Avg. daily mean / SD | 597 | -0.168 [-0.757, +0.420] | -0.1212 | -0.56 | 0.575 | not applied (n < 1000) | 0.918 | +1.7 | +4.7 | 0.1012 | 0.1040 |
| MAG (mg/dL/h) | 597 | +0.967 [+0.286, +1.649] | 0.1433 | 2.78 | 0.005** | not applied (n < 1000) | 0.116 | -8.2 | -5.2 | 0.1161 | 0.1040 |
| Avg. daily range (mg/dL) | 597 | +0.522 [-0.107, +1.151] | 0.03235 | 1.63 | 0.104 | not applied (n < 1000) | 0.556 | -0.9 | +2.1 | 0.1044 | 0.1040 |
| SD of daily means (mg/dL) | 597 | +0.842 [+0.158, +1.526] | 0.38 | 2.41 | 0.016* | not applied (n < 1000) | 0.268 | -5.7 | -2.7 | 0.1100 | 0.1040 |
| Time in range 70-180, pooled (%) | 597 | -0.725 [-1.129, -0.322] | -0.2627 | -3.52 | 4.3e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -3.7 | -0.7 | 0.1122 | 0.1040 |
| Avg. daily time in range 70-180 (%) | 597 | -0.760 [-1.177, -0.343] | -0.2823 | -3.57 | 3.6e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -4.2 | -1.2 | 0.1128 | 0.1040 |
| Time 54-69, pooled (%) | 597 | -0.560 [-1.154, +0.033] | -1.044 | -1.85 | 0.064 | not applied (n < 1000) | 0.494 | -1.4 | +1.6 | 0.1015 | 0.1040 |
| Avg. daily time 54-69 (%) | 597 | -0.507 [-1.081, +0.067] | -0.9156 | -1.73 | 0.084 | not applied (n < 1000) | 0.556 | -0.8 | +2.2 | 0.1015 | 0.1040 |
| Time < 70, pooled (%) | 597 | -0.560 [-1.154, +0.033] | -1.044 | -1.85 | 0.064 | not applied (n < 1000) | 0.494 | -1.4 | +1.6 | 0.1015 | 0.1040 |
| Avg. daily time < 70 (%) | 597 | -0.507 [-1.081, +0.067] | -0.9156 | -1.73 | 0.084 | not applied (n < 1000) | 0.556 | -0.8 | +2.2 | 0.1015 | 0.1040 |
| Time 181-250, pooled (%) | 597 | +0.833 [+0.424, +1.241] | 0.2996 | 4.00 | 6.5e-05*** | not applied (n < 1000) | 0.004 (q<0.05) | -5.4 | -2.4 | 0.1152 | 0.1040 |
| Avg. daily time 181-250 (%) | 597 | +0.863 [+0.446, +1.280] | 0.3186 | 4.06 | 4.9e-05*** | not applied (n < 1000) | 0.004 (q<0.05) | -6.0 | -3.0 | 0.1157 | 0.1040 |
| Time > 180, pooled (%) | 597 | +0.833 [+0.424, +1.241] | 0.2996 | 4.00 | 6.5e-05*** | not applied (n < 1000) | 0.004 (q<0.05) | -5.4 | -2.4 | 0.1152 | 0.1040 |
| Avg. daily time > 180 (%) | 597 | +0.863 [+0.446, +1.280] | 0.3186 | 4.06 | 4.9e-05*** | not applied (n < 1000) | 0.004 (q<0.05) | -6.0 | -3.0 | 0.1157 | 0.1040 |
| Nocturnal time > 180 (%) | 597 | +0.581 [+0.242, +0.920] | 0.1805 | 3.36 | 7.9e-04*** | not applied (n < 1000) | 0.025 (q<0.05) | -1.6 | +1.4 | 0.1093 | 0.1040 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 601; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 601 | -7.766 [-13.877, -1.655] | -23.14 | -2.49 | 0.013* | not applied (n < 1000) | 0.254 | -5.6 | +0.0 | -0.0138 | -0.0246 |
| Mean glucose (mg/dL) | 601 | -0.656 [-6.221, +4.908] | -0.05928 | -0.23 | 0.817 | not applied (n < 1000) | 0.969 | +1.9 | +7.5 | -0.0256 | -0.0246 |
| GMI (%) | 601 | -0.656 [-6.221, +4.908] | -2.478 | -0.23 | 0.817 | not applied (n < 1000) | 0.969 | +1.9 | +7.5 | -0.0256 | -0.0246 |
| Nocturnal mean 00-06h (mg/dL) | 601 | -4.259 [-9.836, +1.318] | -0.3309 | -1.50 | 0.134 | not applied (n < 1000) | 0.557 | -0.3 | +5.3 | -0.0218 | -0.0246 |
| Glucose SD, pooled (mg/dL) | 601 | +0.810 [-4.946, +6.566] | 0.216 | 0.28 | 0.783 | not applied (n < 1000) | 0.969 | +1.9 | +7.5 | -0.0293 | -0.0246 |
| Avg. daily SD (mg/dL) | 601 | +1.452 [-4.461, +7.366] | 0.3923 | 0.48 | 0.630 | not applied (n < 1000) | 0.931 | +1.7 | +7.3 | -0.0293 | -0.0246 |
| CV (%) | 601 | +1.225 [-4.258, +6.709] | 0.4452 | 0.44 | 0.661 | not applied (n < 1000) | 0.947 | +1.8 | +7.4 | -0.0289 | -0.0246 |
| Mean / SD ratio | 601 | -1.579 [-6.946, +3.788] | -1.423 | -0.58 | 0.564 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0291 | -0.0246 |
| Avg. daily mean / SD | 601 | -2.098 [-7.669, +3.472] | -1.536 | -0.74 | 0.460 | not applied (n < 1000) | 0.893 | +1.4 | +7.0 | -0.0294 | -0.0246 |
| MAG (mg/dL/h) | 601 | -4.662 [-11.542, +2.218] | -0.6933 | -1.33 | 0.184 | not applied (n < 1000) | 0.612 | -0.9 | +4.7 | -0.0231 | -0.0246 |
| Avg. daily range (mg/dL) | 601 | +2.477 [-3.651, +8.604] | 0.1534 | 0.79 | 0.428 | not applied (n < 1000) | 0.883 | +1.2 | +6.8 | -0.0260 | -0.0246 |
| SD of daily means (mg/dL) | 601 | -2.694 [-8.158, +2.770] | -1.189 | -0.97 | 0.334 | not applied (n < 1000) | 0.814 | +1.0 | +6.6 | -0.0275 | -0.0246 |
| Time in range 70-180, pooled (%) | 601 | -1.633 [-6.785, +3.519] | -0.6079 | -0.62 | 0.534 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0266 | -0.0246 |
| Avg. daily time in range 70-180 (%) | 601 | -1.193 [-6.439, +4.053] | -0.4545 | -0.45 | 0.656 | not applied (n < 1000) | 0.947 | +1.8 | +7.4 | -0.0272 | -0.0246 |
| Time 54-69, pooled (%) | 601 | -0.871 [-5.780, +4.038] | -1.648 | -0.35 | 0.728 | not applied (n < 1000) | 0.951 | +1.9 | +7.5 | -0.0271 | -0.0246 |
| Avg. daily time 54-69 (%) | 601 | -1.396 [-6.488, +3.696] | -2.559 | -0.54 | 0.591 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0268 | -0.0246 |
| Time < 70, pooled (%) | 601 | -0.871 [-5.780, +4.038] | -1.648 | -0.35 | 0.728 | not applied (n < 1000) | 0.951 | +1.9 | +7.5 | -0.0271 | -0.0246 |
| Avg. daily time < 70 (%) | 601 | -1.396 [-6.488, +3.696] | -2.559 | -0.54 | 0.591 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0268 | -0.0246 |
| Time 181-250, pooled (%) | 601 | +1.801 [-3.516, +7.117] | 0.6658 | 0.66 | 0.507 | not applied (n < 1000) | 0.918 | +1.6 | +7.2 | -0.0265 | -0.0246 |
| Avg. daily time 181-250 (%) | 601 | +1.484 [-3.912, +6.879] | 0.5617 | 0.54 | 0.590 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0269 | -0.0246 |
| Time > 180, pooled (%) | 601 | +1.801 [-3.516, +7.117] | 0.6658 | 0.66 | 0.507 | not applied (n < 1000) | 0.918 | +1.6 | +7.2 | -0.0265 | -0.0246 |
| Avg. daily time > 180 (%) | 601 | +1.484 [-3.912, +6.879] | 0.5617 | 0.54 | 0.590 | not applied (n < 1000) | 0.918 | +1.7 | +7.3 | -0.0269 | -0.0246 |
| Nocturnal time > 180 (%) | 601 | -0.754 [-5.130, +3.623] | -0.2364 | -0.34 | 0.736 | not applied (n < 1000) | 0.951 | +1.9 | +7.5 | -0.0259 | -0.0246 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 598; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 598 | +1.231 [-0.249, +2.710] | 3.653 | 1.63 | 0.103 | not applied (n < 1000) | 0.556 | -1.0 | +0.0 | 0.0616 | 0.0599 |
| Mean glucose (mg/dL) | 598 | +1.639 [+0.286, +2.991] | 0.1455 | 2.37 | 0.018* | not applied (n < 1000) | 0.270 | -3.5 | -2.5 | 0.0647 | 0.0599 |
| GMI (%) | 598 | +1.639 [+0.286, +2.991] | 6.084 | 2.37 | 0.018* | not applied (n < 1000) | 0.270 | -3.5 | -2.5 | 0.0647 | 0.0599 |
| Nocturnal mean 00-06h (mg/dL) | 598 | +2.059 [+0.685, +3.433] | 0.1583 | 2.94 | 0.003** | not applied (n < 1000) | 0.083 | -6.4 | -5.5 | 0.0681 | 0.0599 |
| Glucose SD, pooled (mg/dL) | 598 | +1.199 [-0.253, +2.651] | 0.3166 | 1.62 | 0.105 | not applied (n < 1000) | 0.556 | -0.9 | +0.0 | 0.0561 | 0.0599 |
| Avg. daily SD (mg/dL) | 598 | +1.021 [-0.440, +2.482] | 0.2744 | 1.37 | 0.171 | not applied (n < 1000) | 0.591 | -0.1 | +0.8 | 0.0545 | 0.0599 |
| CV (%) | 598 | +0.441 [-1.009, +1.891] | 0.1582 | 0.60 | 0.551 | not applied (n < 1000) | 0.918 | +1.6 | +2.6 | 0.0533 | 0.0599 |
| Mean / SD ratio | 598 | -0.601 [-2.010, +0.807] | -0.5294 | -0.84 | 0.403 | not applied (n < 1000) | 0.875 | +1.3 | +2.2 | 0.0530 | 0.0599 |
| Avg. daily mean / SD | 598 | -0.457 [-1.876, +0.963] | -0.3291 | -0.63 | 0.528 | not applied (n < 1000) | 0.918 | +1.6 | +2.5 | 0.0525 | 0.0599 |
| MAG (mg/dL/h) | 598 | +1.196 [-0.296, +2.687] | 0.1772 | 1.57 | 0.116 | not applied (n < 1000) | 0.556 | -1.0 | -0.0 | 0.0579 | 0.0599 |
| Avg. daily range (mg/dL) | 598 | +1.066 [-0.357, +2.489] | 0.06582 | 1.47 | 0.142 | not applied (n < 1000) | 0.558 | -0.4 | +0.6 | 0.0571 | 0.0599 |
| SD of daily means (mg/dL) | 598 | +1.551 [+0.114, +2.988] | 0.7015 | 2.12 | 0.034* | not applied (n < 1000) | 0.326 | -3.0 | -2.1 | 0.0587 | 0.0599 |
| Time in range 70-180, pooled (%) | 598 | -0.533 [-1.663, +0.597] | -0.1931 | -0.92 | 0.356 | not applied (n < 1000) | 0.818 | +1.4 | +2.4 | 0.0594 | 0.0599 |
| Avg. daily time in range 70-180 (%) | 598 | -0.470 [-1.608, +0.668] | -0.1747 | -0.81 | 0.418 | not applied (n < 1000) | 0.883 | +1.5 | +2.5 | 0.0588 | 0.0599 |
| Time 54-69, pooled (%) | 598 | -1.053 [-2.408, +0.303] | -1.936 | -1.52 | 0.128 | not applied (n < 1000) | 0.557 | -0.3 | +0.7 | 0.0595 | 0.0599 |
| Avg. daily time 54-69 (%) | 598 | -1.053 [-2.466, +0.360] | -1.876 | -1.46 | 0.144 | not applied (n < 1000) | 0.558 | -0.3 | +0.7 | 0.0602 | 0.0599 |
| Time < 70, pooled (%) | 598 | -1.053 [-2.408, +0.303] | -1.936 | -1.52 | 0.128 | not applied (n < 1000) | 0.557 | -0.3 | +0.7 | 0.0595 | 0.0599 |
| Avg. daily time < 70 (%) | 598 | -1.053 [-2.466, +0.360] | -1.876 | -1.46 | 0.144 | not applied (n < 1000) | 0.558 | -0.3 | +0.7 | 0.0602 | 0.0599 |
| Time 181-250, pooled (%) | 598 | +0.739 [-0.426, +1.904] | 0.2662 | 1.24 | 0.214 | not applied (n < 1000) | 0.674 | +0.9 | +1.8 | 0.0604 | 0.0599 |
| Avg. daily time 181-250 (%) | 598 | +0.689 [-0.476, +1.855] | 0.2547 | 1.16 | 0.246 | not applied (n < 1000) | 0.739 | +1.0 | +2.0 | 0.0596 | 0.0599 |
| Time > 180, pooled (%) | 598 | +0.739 [-0.426, +1.904] | 0.2662 | 1.24 | 0.214 | not applied (n < 1000) | 0.674 | +0.9 | +1.8 | 0.0604 | 0.0599 |
| Avg. daily time > 180 (%) | 598 | +0.689 [-0.476, +1.855] | 0.2547 | 1.16 | 0.246 | not applied (n < 1000) | 0.739 | +1.0 | +2.0 | 0.0596 | 0.0599 |
| Nocturnal time > 180 (%) | 598 | +0.730 [-0.307, +1.767] | 0.2272 | 1.38 | 0.168 | not applied (n < 1000) | 0.586 | +0.9 | +1.9 | 0.0595 | 0.0599 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

### Population: Non-healthy group (T2D non-insulin + T2D insulin)

#### MoCA total score (0-30)
*n = 205; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 205 | -0.268 [-0.736, +0.199] | -0.511 | -1.12 | 0.261 | not applied (n < 1000) | 0.786 | +0.3 | +0.0 | 0.0043 | 0.0135 |
| Mean glucose (mg/dL) | 205 | -0.492 [-0.869, -0.114] | -0.03813 | -2.55 | 0.011* | not applied (n < 1000) | 0.310 | -4.1 | -4.4 | 0.0337 | 0.0135 |
| GMI (%) | 205 | -0.492 [-0.869, -0.114] | -1.594 | -2.55 | 0.011* | not applied (n < 1000) | 0.310 | -4.1 | -4.4 | 0.0337 | 0.0135 |
| Nocturnal mean 00-06h (mg/dL) | 205 | -0.736 [-1.143, -0.329] | -0.05106 | -3.54 | 3.9e-04*** | not applied (n < 1000) | 0.096 | -11.9 | -12.3 | 0.0618 | 0.0135 |
| Glucose SD, pooled (mg/dL) | 205 | -0.551 [-0.978, -0.124] | -0.1193 | -2.53 | 0.011* | not applied (n < 1000) | 0.310 | -4.9 | -5.3 | 0.0235 | 0.0135 |
| Avg. daily SD (mg/dL) | 205 | -0.507 [-0.935, -0.079] | -0.1131 | -2.32 | 0.020* | not applied (n < 1000) | 0.316 | -4.0 | -4.4 | 0.0215 | 0.0135 |
| CV (%) | 205 | -0.366 [-0.821, +0.089] | -0.1172 | -1.57 | 0.115 | not applied (n < 1000) | 0.663 | -1.0 | -1.3 | 0.0034 | 0.0135 |
| Mean / SD ratio | 205 | +0.385 [-0.068, +0.838] | 0.3238 | 1.66 | 0.096 | not applied (n < 1000) | 0.627 | -1.4 | -1.7 | 0.0018 | 0.0135 |
| Avg. daily mean / SD | 205 | +0.382 [-0.052, +0.817] | 0.2497 | 1.73 | 0.084 | not applied (n < 1000) | 0.627 | -1.4 | -1.7 | 0.0026 | 0.0135 |
| MAG (mg/dL/h) | 205 | -0.198 [-0.659, +0.263] | -0.03057 | -0.84 | 0.401 | not applied (n < 1000) | 0.822 | +1.0 | +0.7 | -0.0011 | 0.0135 |
| Avg. daily range (mg/dL) | 205 | -0.402 [-0.834, +0.029] | -0.02261 | -1.83 | 0.067 | not applied (n < 1000) | 0.572 | -1.9 | -2.3 | 0.0143 | 0.0135 |
| SD of daily means (mg/dL) | 205 | -0.449 [-0.873, -0.026] | -0.1736 | -2.08 | 0.037* | not applied (n < 1000) | 0.483 | -2.3 | -2.7 | 0.0212 | 0.0135 |
| Time in range 70-180, pooled (%) | 205 | +0.238 [-0.162, +0.639] | 0.05045 | 1.17 | 0.243 | not applied (n < 1000) | 0.761 | +0.6 | +0.3 | 0.0006 | 0.0135 |
| Avg. daily time in range 70-180 (%) | 205 | +0.215 [-0.181, +0.611] | 0.0465 | 1.06 | 0.288 | not applied (n < 1000) | 0.786 | +0.9 | +0.6 | -0.0005 | 0.0135 |
| Time 54-69, pooled (%) | 205 | +0.242 [-0.014, +0.497] | 0.8327 | 1.86 | 0.064 | not applied (n < 1000) | 0.568 | +0.6 | +0.3 | 0.0064 | 0.0135 |
| Avg. daily time 54-69 (%) | 205 | +0.186 [-0.057, +0.430] | 0.619 | 1.50 | 0.133 | not applied (n < 1000) | 0.698 | +1.2 | +0.8 | 0.0070 | 0.0135 |
| Time < 70, pooled (%) | 205 | +0.242 [-0.014, +0.497] | 0.8327 | 1.86 | 0.064 | not applied (n < 1000) | 0.568 | +0.6 | +0.3 | 0.0064 | 0.0135 |
| Avg. daily time < 70 (%) | 205 | +0.186 [-0.057, +0.430] | 0.619 | 1.50 | 0.133 | not applied (n < 1000) | 0.698 | +1.2 | +0.8 | 0.0070 | 0.0135 |
| Time 181-250, pooled (%) | 205 | -0.251 [-0.651, +0.149] | -0.05274 | -1.23 | 0.219 | not applied (n < 1000) | 0.734 | +0.5 | +0.2 | 0.0012 | 0.0135 |
| Avg. daily time 181-250 (%) | 205 | -0.225 [-0.619, +0.170] | -0.04817 | -1.12 | 0.264 | not applied (n < 1000) | 0.786 | +0.8 | +0.5 | 0.0001 | 0.0135 |
| Time > 180, pooled (%) | 205 | -0.251 [-0.651, +0.149] | -0.05274 | -1.23 | 0.219 | not applied (n < 1000) | 0.734 | +0.5 | +0.2 | 0.0012 | 0.0135 |
| Avg. daily time > 180 (%) | 205 | -0.225 [-0.619, +0.170] | -0.04817 | -1.12 | 0.264 | not applied (n < 1000) | 0.786 | +0.8 | +0.5 | 0.0001 | 0.0135 |
| Nocturnal time > 180 (%) | 205 | -0.417 [-0.912, +0.078] | -0.08044 | -1.65 | 0.098 | not applied (n < 1000) | 0.627 | -2.0 | -2.4 | 0.0087 | 0.0135 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 205; events = 94; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 205 | OR 1.276 [0.922, 1.766] | 0.4639 | 1.47 | 0.142 | not applied (n < 1000) | 0.698 | -0.3 | +0.0 | 0.6275 | 0.6274 |
| Mean glucose (mg/dL) | 205 | OR 1.496 [1.091, 2.052] | 0.03123 | 2.50 | 0.012* | not applied (n < 1000) | 0.310 | -4.5 | -4.3 | 0.6382 | 0.6274 |
| GMI (%) | 205 | OR 1.496 [1.091, 2.052] | 1.306 | 2.50 | 0.012* | not applied (n < 1000) | 0.310 | -4.5 | -4.3 | 0.6382 | 0.6274 |
| Nocturnal mean 00-06h (mg/dL) | 205 | OR 1.795 [1.285, 2.507] | 0.04057 | 3.43 | 6.0e-04*** | not applied (n < 1000) | 0.096 | -11.0 | -10.8 | 0.6588 | 0.6274 |
| Glucose SD, pooled (mg/dL) | 205 | OR 1.437 [1.037, 1.990] | 0.07844 | 2.18 | 0.029* | not applied (n < 1000) | 0.427 | -2.9 | -2.6 | 0.6330 | 0.6274 |
| Avg. daily SD (mg/dL) | 205 | OR 1.409 [1.023, 1.942] | 0.07653 | 2.10 | 0.036* | not applied (n < 1000) | 0.483 | -2.5 | -2.2 | 0.6313 | 0.6274 |
| CV (%) | 205 | OR 1.222 [0.882, 1.693] | 0.06432 | 1.21 | 0.228 | not applied (n < 1000) | 0.734 | +0.5 | +0.8 | 0.6212 | 0.6274 |
| Mean / SD ratio | 205 | OR 0.819 [0.587, 1.142] | -0.168 | -1.18 | 0.240 | not applied (n < 1000) | 0.756 | +0.6 | +0.8 | 0.6239 | 0.6274 |
| Avg. daily mean / SD | 205 | OR 0.780 [0.556, 1.093] | -0.1624 | -1.44 | 0.149 | not applied (n < 1000) | 0.705 | -0.2 | +0.1 | 0.6268 | 0.6274 |
| MAG (mg/dL/h) | 205 | OR 0.988 [0.727, 1.342] | -0.001863 | -0.08 | 0.939 | not applied (n < 1000) | 0.991 | +2.0 | +2.3 | 0.6102 | 0.6274 |
| Avg. daily range (mg/dL) | 205 | OR 1.270 [0.930, 1.735] | 0.01344 | 1.50 | 0.133 | not applied (n < 1000) | 0.698 | -0.3 | -0.0 | 0.6210 | 0.6274 |
| SD of daily means (mg/dL) | 205 | OR 1.293 [0.927, 1.803] | 0.09928 | 1.51 | 0.130 | not applied (n < 1000) | 0.698 | -0.3 | -0.1 | 0.6282 | 0.6274 |
| Time in range 70-180, pooled (%) | 205 | OR 0.794 [0.580, 1.088] | -0.0488 | -1.44 | 0.151 | not applied (n < 1000) | 0.705 | -0.1 | +0.1 | 0.6229 | 0.6274 |
| Avg. daily time in range 70-180 (%) | 205 | OR 0.798 [0.584, 1.090] | -0.04881 | -1.42 | 0.156 | not applied (n < 1000) | 0.705 | -0.1 | +0.2 | 0.6241 | 0.6274 |
| Time 54-69, pooled (%) | 205 | OR 0.815 [0.556, 1.195] | -0.7046 | -1.05 | 0.295 | not applied (n < 1000) | 0.786 | +0.7 | +1.0 | 0.6227 | 0.6274 |
| Avg. daily time 54-69 (%) | 205 | OR 0.814 [0.545, 1.214] | -0.6839 | -1.01 | 0.313 | not applied (n < 1000) | 0.787 | +0.8 | +1.1 | 0.6224 | 0.6274 |
| Time < 70, pooled (%) | 205 | OR 0.815 [0.556, 1.195] | -0.7046 | -1.05 | 0.295 | not applied (n < 1000) | 0.786 | +0.7 | +1.0 | 0.6227 | 0.6274 |
| Avg. daily time < 70 (%) | 205 | OR 0.814 [0.545, 1.214] | -0.6839 | -1.01 | 0.313 | not applied (n < 1000) | 0.787 | +0.8 | +1.1 | 0.6224 | 0.6274 |
| Time 181-250, pooled (%) | 205 | OR 1.270 [0.927, 1.739] | 0.05022 | 1.49 | 0.137 | not applied (n < 1000) | 0.698 | -0.3 | -0.0 | 0.6246 | 0.6274 |
| Avg. daily time 181-250 (%) | 205 | OR 1.263 [0.924, 1.727] | 0.05008 | 1.46 | 0.143 | not applied (n < 1000) | 0.698 | -0.2 | +0.0 | 0.6241 | 0.6274 |
| Time > 180, pooled (%) | 205 | OR 1.270 [0.927, 1.739] | 0.05022 | 1.49 | 0.137 | not applied (n < 1000) | 0.698 | -0.3 | -0.0 | 0.6246 | 0.6274 |
| Avg. daily time > 180 (%) | 205 | OR 1.263 [0.924, 1.727] | 0.05008 | 1.46 | 0.143 | not applied (n < 1000) | 0.698 | -0.2 | +0.0 | 0.6241 | 0.6274 |
| Nocturnal time > 180 (%) | 205 | OR 1.476 [0.992, 2.196] | 0.07502 | 1.92 | 0.055 | not applied (n < 1000) | 0.547 | -2.4 | -2.2 | 0.6277 | 0.6274 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 205; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 205 | -0.221 [-0.616, +0.174] | -0.4207 | -1.10 | 0.273 | not applied (n < 1000) | 0.786 | +0.5 | +0.0 | -0.1137 | -0.1022 |
| Mean glucose (mg/dL) | 205 | -0.166 [-0.580, +0.247] | -0.0129 | -0.79 | 0.430 | not applied (n < 1000) | 0.835 | +1.1 | +0.6 | -0.1195 | -0.1022 |
| GMI (%) | 205 | -0.166 [-0.580, +0.247] | -0.5392 | -0.79 | 0.430 | not applied (n < 1000) | 0.835 | +1.1 | +0.6 | -0.1195 | -0.1022 |
| Nocturnal mean 00-06h (mg/dL) | 205 | -0.343 [-0.750, +0.064] | -0.02376 | -1.65 | 0.099 | not applied (n < 1000) | 0.627 | -2.0 | -2.5 | -0.1096 | -0.1022 |
| Glucose SD, pooled (mg/dL) | 205 | -0.143 [-0.536, +0.249] | -0.03104 | -0.72 | 0.474 | not applied (n < 1000) | 0.892 | +1.4 | +0.9 | -0.1201 | -0.1022 |
| Avg. daily SD (mg/dL) | 205 | -0.169 [-0.554, +0.217] | -0.03763 | -0.86 | 0.391 | not applied (n < 1000) | 0.820 | +1.1 | +0.6 | -0.1119 | -0.1022 |
| CV (%) | 205 | -0.055 [-0.431, +0.321] | -0.01777 | -0.29 | 0.773 | not applied (n < 1000) | 0.984 | +1.9 | +1.5 | -0.1187 | -0.1022 |
| Mean / SD ratio | 205 | +0.108 [-0.239, +0.454] | 0.09061 | 0.61 | 0.542 | not applied (n < 1000) | 0.963 | +1.6 | +1.2 | -0.1124 | -0.1022 |
| Avg. daily mean / SD | 205 | +0.206 [-0.109, +0.521] | 0.1343 | 1.28 | 0.201 | not applied (n < 1000) | 0.719 | +0.7 | +0.2 | -0.1022 | -0.1022 |
| MAG (mg/dL/h) | 205 | -0.044 [-0.380, +0.291] | -0.006862 | -0.26 | 0.795 | not applied (n < 1000) | 0.984 | +1.9 | +1.5 | -0.1237 | -0.1022 |
| Avg. daily range (mg/dL) | 205 | -0.121 [-0.493, +0.252] | -0.006785 | -0.64 | 0.525 | not applied (n < 1000) | 0.961 | +1.5 | +1.1 | -0.1118 | -0.1022 |
| SD of daily means (mg/dL) | 205 | -0.117 [-0.525, +0.291] | -0.04523 | -0.56 | 0.573 | not applied (n < 1000) | 0.963 | +1.6 | +1.1 | -0.1263 | -0.1022 |
| Time in range 70-180, pooled (%) | 205 | +0.109 [-0.332, +0.551] | 0.02315 | 0.49 | 0.627 | not applied (n < 1000) | 0.963 | +1.6 | +1.2 | -0.1242 | -0.1022 |
| Avg. daily time in range 70-180 (%) | 205 | +0.098 [-0.349, +0.546] | 0.02125 | 0.43 | 0.667 | not applied (n < 1000) | 0.984 | +1.7 | +1.2 | -0.1243 | -0.1022 |
| Time 54-69, pooled (%) | 205 | +0.150 [-0.196, +0.496] | 0.5174 | 0.85 | 0.395 | not applied (n < 1000) | 0.820 | +1.3 | +0.8 | -0.1105 | -0.1022 |
| Avg. daily time 54-69 (%) | 205 | +0.164 [-0.129, +0.458] | 0.5461 | 1.10 | 0.272 | not applied (n < 1000) | 0.786 | +1.1 | +0.6 | -0.1061 | -0.1022 |
| Time < 70, pooled (%) | 205 | +0.150 [-0.196, +0.496] | 0.5174 | 0.85 | 0.395 | not applied (n < 1000) | 0.820 | +1.3 | +0.8 | -0.1105 | -0.1022 |
| Avg. daily time < 70 (%) | 205 | +0.164 [-0.129, +0.458] | 0.5461 | 1.10 | 0.272 | not applied (n < 1000) | 0.786 | +1.1 | +0.6 | -0.1061 | -0.1022 |
| Time 181-250, pooled (%) | 205 | -0.117 [-0.560, +0.325] | -0.02471 | -0.52 | 0.603 | not applied (n < 1000) | 0.963 | +1.5 | +1.1 | -0.1238 | -0.1022 |
| Avg. daily time 181-250 (%) | 205 | -0.108 [-0.555, +0.340] | -0.02312 | -0.47 | 0.637 | not applied (n < 1000) | 0.963 | +1.6 | +1.2 | -0.1235 | -0.1022 |
| Time > 180, pooled (%) | 205 | -0.117 [-0.560, +0.325] | -0.02471 | -0.52 | 0.603 | not applied (n < 1000) | 0.963 | +1.5 | +1.1 | -0.1238 | -0.1022 |
| Avg. daily time > 180 (%) | 205 | -0.108 [-0.555, +0.340] | -0.02312 | -0.47 | 0.637 | not applied (n < 1000) | 0.963 | +1.6 | +1.2 | -0.1235 | -0.1022 |
| Nocturnal time > 180 (%) | 205 | -0.253 [-0.736, +0.230] | -0.04877 | -1.03 | 0.304 | not applied (n < 1000) | 0.786 | -0.0 | -0.5 | -0.1088 | -0.1022 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 204; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 204 | -0.627 [-1.372, +0.118] | -1.192 | -1.65 | 0.099 | not applied (n < 1000) | 0.627 | -0.8 | +0.0 | 0.0237 | 0.0136 |
| Mean glucose (mg/dL) | 204 | -0.536 [-1.202, +0.131] | -0.04146 | -1.58 | 0.115 | not applied (n < 1000) | 0.663 | -0.2 | +0.6 | 0.0015 | 0.0136 |
| GMI (%) | 204 | -0.536 [-1.202, +0.131] | -1.733 | -1.58 | 0.115 | not applied (n < 1000) | 0.663 | -0.2 | +0.6 | 0.0015 | 0.0136 |
| Nocturnal mean 00-06h (mg/dL) | 204 | -0.136 [-0.824, +0.553] | -0.009399 | -0.39 | 0.699 | not applied (n < 1000) | 0.984 | +1.9 | +2.7 | -0.0042 | 0.0136 |
| Glucose SD, pooled (mg/dL) | 204 | -0.307 [-1.039, +0.425] | -0.06651 | -0.82 | 0.411 | not applied (n < 1000) | 0.822 | +1.4 | +2.2 | -0.0022 | 0.0136 |
| Avg. daily SD (mg/dL) | 204 | -0.228 [-0.945, +0.490] | -0.05072 | -0.62 | 0.534 | not applied (n < 1000) | 0.963 | +1.6 | +2.4 | -0.0030 | 0.0136 |
| CV (%) | 204 | -0.047 [-0.747, +0.653] | -0.01505 | -0.13 | 0.895 | not applied (n < 1000) | 0.986 | +2.0 | +2.8 | 0.0045 | 0.0136 |
| Mean / SD ratio | 204 | -0.072 [-0.796, +0.653] | -0.06044 | -0.19 | 0.846 | not applied (n < 1000) | 0.984 | +2.0 | +2.8 | 0.0026 | 0.0136 |
| Avg. daily mean / SD | 204 | -0.203 [-0.953, +0.547] | -0.1327 | -0.53 | 0.595 | not applied (n < 1000) | 0.963 | +1.7 | +2.5 | 0.0016 | 0.0136 |
| MAG (mg/dL/h) | 204 | +0.819 [+0.126, +1.512] | 0.1266 | 2.32 | 0.021* | not applied (n < 1000) | 0.316 | -3.2 | -2.4 | 0.0338 | 0.0136 |
| Avg. daily range (mg/dL) | 204 | +0.010 [-0.692, +0.712] | 0.0005521 | 0.03 | 0.978 | not applied (n < 1000) | 0.999 | +2.0 | +2.8 | 0.0008 | 0.0136 |
| SD of daily means (mg/dL) | 204 | -0.044 [-0.862, +0.774] | -0.01696 | -0.11 | 0.916 | not applied (n < 1000) | 0.986 | +2.0 | +2.8 | 0.0008 | 0.0136 |
| Time in range 70-180, pooled (%) | 204 | +0.728 [+0.023, +1.432] | 0.1538 | 2.02 | 0.043* | not applied (n < 1000) | 0.483 | -1.9 | -1.1 | 0.0045 | 0.0136 |
| Avg. daily time in range 70-180 (%) | 204 | +0.723 [+0.023, +1.422] | 0.1559 | 2.02 | 0.043* | not applied (n < 1000) | 0.483 | -1.9 | -1.1 | 0.0068 | 0.0136 |
| Time 54-69, pooled (%) | 204 | -0.035 [-0.657, +0.586] | -0.1211 | -0.11 | 0.912 | not applied (n < 1000) | 0.986 | +2.0 | +2.8 | 0.0033 | 0.0136 |
| Avg. daily time 54-69 (%) | 204 | +0.000 [-0.537, +0.537] | 0.0007155 | 0.00 | 0.999 | not applied (n < 1000) | 0.999 | +2.0 | +2.8 | 0.0063 | 0.0136 |
| Time < 70, pooled (%) | 204 | -0.035 [-0.657, +0.586] | -0.1211 | -0.11 | 0.912 | not applied (n < 1000) | 0.986 | +2.0 | +2.8 | 0.0033 | 0.0136 |
| Avg. daily time < 70 (%) | 204 | +0.000 [-0.537, +0.537] | 0.0007155 | 0.00 | 0.999 | not applied (n < 1000) | 0.999 | +2.0 | +2.8 | 0.0063 | 0.0136 |
| Time 181-250, pooled (%) | 204 | -0.719 [-1.421, -0.016] | -0.1508 | -2.00 | 0.045* | not applied (n < 1000) | 0.483 | -1.8 | -1.0 | 0.0038 | 0.0136 |
| Avg. daily time 181-250 (%) | 204 | -0.715 [-1.411, -0.018] | -0.1528 | -2.01 | 0.044* | not applied (n < 1000) | 0.483 | -1.8 | -1.0 | 0.0061 | 0.0136 |
| Time > 180, pooled (%) | 204 | -0.719 [-1.421, -0.016] | -0.1508 | -2.00 | 0.045* | not applied (n < 1000) | 0.483 | -1.8 | -1.0 | 0.0038 | 0.0136 |
| Avg. daily time > 180 (%) | 204 | -0.715 [-1.411, -0.018] | -0.1528 | -2.01 | 0.044* | not applied (n < 1000) | 0.483 | -1.8 | -1.0 | 0.0061 | 0.0136 |
| Nocturnal time > 180 (%) | 204 | -0.164 [-1.072, +0.744] | -0.0316 | -0.35 | 0.723 | not applied (n < 1000) | 0.984 | +1.8 | +2.6 | -0.0272 | 0.0136 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 204; events = 50; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 204 | OR 0.764 [0.524, 1.113] | -0.5128 | -1.40 | 0.161 | not applied (n < 1000) | 0.705 | -0.1 | +0.0 | 0.5403 | 0.5062 |
| Mean glucose (mg/dL) | 204 | OR 0.997 [0.714, 1.393] | -0.0002112 | -0.02 | 0.987 | not applied (n < 1000) | 0.999 | +2.0 | +2.1 | 0.5023 | 0.5062 |
| GMI (%) | 204 | OR 0.997 [0.714, 1.393] | -0.008828 | -0.02 | 0.987 | not applied (n < 1000) | 0.999 | +2.0 | +2.1 | 0.5023 | 0.5062 |
| Nocturnal mean 00-06h (mg/dL) | 204 | OR 1.145 [0.824, 1.591] | 0.009377 | 0.81 | 0.420 | not applied (n < 1000) | 0.828 | +1.3 | +1.5 | 0.5023 | 0.5062 |
| Glucose SD, pooled (mg/dL) | 204 | OR 0.961 [0.676, 1.367] | -0.008507 | -0.22 | 0.827 | not applied (n < 1000) | 0.984 | +2.0 | +2.1 | 0.5010 | 0.5062 |
| Avg. daily SD (mg/dL) | 204 | OR 0.979 [0.692, 1.385] | -0.004765 | -0.12 | 0.904 | not applied (n < 1000) | 0.986 | +2.0 | +2.1 | 0.4974 | 0.5062 |
| CV (%) | 204 | OR 0.958 [0.671, 1.369] | -0.01376 | -0.24 | 0.814 | not applied (n < 1000) | 0.984 | +1.9 | +2.1 | 0.4965 | 0.5062 |
| Mean / SD ratio | 204 | OR 0.956 [0.672, 1.361] | -0.03786 | -0.25 | 0.803 | not applied (n < 1000) | 0.984 | +1.9 | +2.1 | 0.4952 | 0.5062 |
| Avg. daily mean / SD | 204 | OR 0.943 [0.668, 1.331] | -0.03855 | -0.34 | 0.737 | not applied (n < 1000) | 0.984 | +1.9 | +2.0 | 0.4875 | 0.5062 |
| MAG (mg/dL/h) | 204 | OR 1.757 [1.227, 2.517] | 0.08713 | 3.08 | 0.002** | not applied (n < 1000) | 0.225 | -8.3 | -8.2 | 0.5932 | 0.5062 |
| Avg. daily range (mg/dL) | 204 | OR 1.110 [0.786, 1.567] | 0.005865 | 0.59 | 0.553 | not applied (n < 1000) | 0.963 | +1.6 | +1.8 | 0.5003 | 0.5062 |
| SD of daily means (mg/dL) | 204 | OR 0.994 [0.693, 1.426] | -0.002251 | -0.03 | 0.975 | not applied (n < 1000) | 0.999 | +2.0 | +2.1 | 0.4982 | 0.5062 |
| Time in range 70-180, pooled (%) | 204 | OR 1.307 [0.882, 1.936] | 0.05653 | 1.33 | 0.182 | not applied (n < 1000) | 0.705 | -0.0 | +0.1 | 0.5244 | 0.5062 |
| Avg. daily time in range 70-180 (%) | 204 | OR 1.323 [0.892, 1.963] | 0.06042 | 1.39 | 0.164 | not applied (n < 1000) | 0.705 | -0.2 | -0.1 | 0.5270 | 0.5062 |
| Time 54-69, pooled (%) | 204 | OR 0.788 [0.485, 1.281] | -0.8187 | -0.96 | 0.337 | not applied (n < 1000) | 0.805 | +0.9 | +1.0 | 0.5072 | 0.5062 |
| Avg. daily time 54-69 (%) | 204 | OR 0.754 [0.440, 1.292] | -0.9362 | -1.03 | 0.304 | not applied (n < 1000) | 0.786 | +0.6 | +0.7 | 0.5097 | 0.5062 |
| Time < 70, pooled (%) | 204 | OR 0.788 [0.485, 1.281] | -0.8187 | -0.96 | 0.337 | not applied (n < 1000) | 0.805 | +0.9 | +1.0 | 0.5072 | 0.5062 |
| Avg. daily time < 70 (%) | 204 | OR 0.754 [0.440, 1.292] | -0.9362 | -1.03 | 0.304 | not applied (n < 1000) | 0.786 | +0.6 | +0.7 | 0.5097 | 0.5062 |
| Time 181-250, pooled (%) | 204 | OR 0.777 [0.527, 1.146] | -0.05294 | -1.27 | 0.203 | not applied (n < 1000) | 0.719 | +0.2 | +0.3 | 0.5234 | 0.5062 |
| Avg. daily time 181-250 (%) | 204 | OR 0.769 [0.521, 1.135] | -0.05614 | -1.32 | 0.186 | not applied (n < 1000) | 0.705 | +0.0 | +0.1 | 0.5247 | 0.5062 |
| Time > 180, pooled (%) | 204 | OR 0.777 [0.527, 1.146] | -0.05294 | -1.27 | 0.203 | not applied (n < 1000) | 0.719 | +0.2 | +0.3 | 0.5234 | 0.5062 |
| Avg. daily time > 180 (%) | 204 | OR 0.769 [0.521, 1.135] | -0.05614 | -1.32 | 0.186 | not applied (n < 1000) | 0.705 | +0.0 | +0.1 | 0.5247 | 0.5062 |
| Nocturnal time > 180 (%) | 204 | OR 0.948 [0.678, 1.328] | -0.01019 | -0.31 | 0.758 | not applied (n < 1000) | 0.984 | +1.9 | +2.0 | 0.4997 | 0.5062 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 198; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 198 | +0.016 [-0.093, +0.124] | 0.03014 | 0.28 | 0.778 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | -0.1120 | -0.1086 |
| Mean glucose (mg/dL) | 198 | -0.033 [-0.153, +0.087] | -0.002579 | -0.54 | 0.591 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | -0.1174 | -0.1086 |
| GMI (%) | 198 | -0.033 [-0.153, +0.087] | -0.1078 | -0.54 | 0.591 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | -0.1174 | -0.1086 |
| Nocturnal mean 00-06h (mg/dL) | 198 | -0.030 [-0.154, +0.094] | -0.002073 | -0.47 | 0.637 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | -0.1130 | -0.1086 |
| Glucose SD, pooled (mg/dL) | 198 | +0.099 [-0.017, +0.215] | 0.02136 | 1.68 | 0.093 | not applied (n < 1000) | 0.627 | -0.6 | -2.5 | -0.1059 | -0.1086 |
| Avg. daily SD (mg/dL) | 198 | +0.076 [-0.032, +0.183] | 0.01678 | 1.38 | 0.168 | not applied (n < 1000) | 0.705 | +0.5 | -1.5 | -0.1076 | -0.1086 |
| CV (%) | 198 | +0.145 [+0.025, +0.264] | 0.04615 | 2.38 | 0.017* | not applied (n < 1000) | 0.316 | -3.4 | -5.4 | -0.0898 | -0.1086 |
| Mean / SD ratio | 198 | -0.130 [-0.239, -0.020] | -0.1085 | -2.33 | 0.020* | not applied (n < 1000) | 0.316 | -2.4 | -4.4 | -0.0939 | -0.1086 |
| Avg. daily mean / SD | 198 | -0.103 [-0.214, +0.009] | -0.06614 | -1.81 | 0.071 | not applied (n < 1000) | 0.586 | -0.8 | -2.7 | -0.1007 | -0.1086 |
| MAG (mg/dL/h) | 198 | +0.069 [-0.027, +0.166] | 0.01064 | 1.40 | 0.161 | not applied (n < 1000) | 0.705 | +0.6 | -1.4 | -0.0983 | -0.1086 |
| Avg. daily range (mg/dL) | 198 | +0.096 [-0.006, +0.198] | 0.00535 | 1.84 | 0.066 | not applied (n < 1000) | 0.572 | -0.6 | -2.5 | -0.0950 | -0.1086 |
| SD of daily means (mg/dL) | 198 | +0.133 [-0.027, +0.293] | 0.05151 | 1.63 | 0.104 | not applied (n < 1000) | 0.643 | -2.4 | -4.3 | -0.1196 | -0.1086 |
| Time in range 70-180, pooled (%) | 198 | +0.015 [-0.103, +0.133] | 0.003203 | 0.25 | 0.803 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | -0.1183 | -0.1086 |
| Avg. daily time in range 70-180 (%) | 198 | +0.012 [-0.109, +0.133] | 0.002542 | 0.19 | 0.850 | not applied (n < 1000) | 0.984 | +2.0 | +0.0 | -0.1190 | -0.1086 |
| Time 54-69, pooled (%) | 198 | +0.115 [-0.182, +0.412] | 0.4201 | 0.76 | 0.450 | not applied (n < 1000) | 0.862 | -1.7 | -3.7 | -0.1167 | -0.1086 |
| Avg. daily time 54-69 (%) | 198 | +0.084 [-0.205, +0.374] | 0.3017 | 0.57 | 0.568 | not applied (n < 1000) | 0.963 | -0.0 | -2.0 | -0.1297 | -0.1086 |
| Time < 70, pooled (%) | 198 | +0.115 [-0.182, +0.412] | 0.4201 | 0.76 | 0.450 | not applied (n < 1000) | 0.862 | -1.7 | -3.7 | -0.1167 | -0.1086 |
| Avg. daily time < 70 (%) | 198 | +0.084 [-0.205, +0.374] | 0.3017 | 0.57 | 0.568 | not applied (n < 1000) | 0.963 | -0.0 | -2.0 | -0.1297 | -0.1086 |
| Time 181-250, pooled (%) | 198 | -0.021 [-0.138, +0.095] | -0.00456 | -0.36 | 0.717 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | -0.1174 | -0.1086 |
| Avg. daily time 181-250 (%) | 198 | -0.017 [-0.136, +0.103] | -0.003607 | -0.27 | 0.785 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | -0.1185 | -0.1086 |
| Time > 180, pooled (%) | 198 | -0.021 [-0.138, +0.095] | -0.00456 | -0.36 | 0.717 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | -0.1174 | -0.1086 |
| Avg. daily time > 180 (%) | 198 | -0.017 [-0.136, +0.103] | -0.003607 | -0.27 | 0.785 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | -0.1185 | -0.1086 |
| Nocturnal time > 180 (%) | 198 | -0.031 [-0.156, +0.094] | -0.00603 | -0.48 | 0.630 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | -0.1108 | -0.1086 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 198; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 198 | -0.059 [-0.456, +0.337] | -0.1148 | -0.29 | 0.770 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | 0.1411 | 0.1449 |
| Mean glucose (mg/dL) | 198 | -0.158 [-0.484, +0.169] | -0.01237 | -0.95 | 0.345 | not applied (n < 1000) | 0.805 | +0.9 | -0.9 | 0.1473 | 0.1449 |
| GMI (%) | 198 | -0.158 [-0.484, +0.169] | -0.5173 | -0.95 | 0.345 | not applied (n < 1000) | 0.805 | +0.9 | -0.9 | 0.1473 | 0.1449 |
| Nocturnal mean 00-06h (mg/dL) | 198 | -0.217 [-0.537, +0.103] | -0.01507 | -1.33 | 0.184 | not applied (n < 1000) | 0.705 | -0.0 | -1.9 | 0.1494 | 0.1449 |
| Glucose SD, pooled (mg/dL) | 198 | -0.013 [-0.335, +0.309] | -0.002837 | -0.08 | 0.936 | not applied (n < 1000) | 0.991 | +2.0 | +0.1 | 0.1352 | 0.1449 |
| Avg. daily SD (mg/dL) | 198 | +0.037 [-0.274, +0.347] | 0.008173 | 0.23 | 0.816 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | 0.1316 | 0.1449 |
| CV (%) | 198 | +0.091 [-0.268, +0.450] | 0.02894 | 0.50 | 0.620 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | 0.1349 | 0.1449 |
| Mean / SD ratio | 198 | -0.074 [-0.483, +0.336] | -0.06152 | -0.35 | 0.725 | not applied (n < 1000) | 0.984 | +1.8 | -0.1 | 0.1299 | 0.1449 |
| Avg. daily mean / SD | 198 | -0.104 [-0.548, +0.340] | -0.06708 | -0.46 | 0.646 | not applied (n < 1000) | 0.972 | +1.6 | -0.3 | 0.1214 | 0.1449 |
| MAG (mg/dL/h) | 198 | -0.085 [-0.430, +0.259] | -0.01316 | -0.49 | 0.627 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | 0.1303 | 0.1449 |
| Avg. daily range (mg/dL) | 198 | +0.001 [-0.307, +0.309] | 6.546e-05 | 0.01 | 0.994 | not applied (n < 1000) | 0.999 | +2.0 | +0.1 | 0.1295 | 0.1449 |
| SD of daily means (mg/dL) | 198 | -0.262 [-0.628, +0.104] | -0.1016 | -1.40 | 0.160 | not applied (n < 1000) | 0.705 | -0.5 | -2.3 | 0.1395 | 0.1449 |
| Time in range 70-180, pooled (%) | 198 | +0.095 [-0.218, +0.409] | 0.02037 | 0.60 | 0.551 | not applied (n < 1000) | 0.963 | +1.6 | -0.2 | 0.1393 | 0.1449 |
| Avg. daily time in range 70-180 (%) | 198 | +0.102 [-0.219, +0.423] | 0.02223 | 0.62 | 0.534 | not applied (n < 1000) | 0.963 | +1.6 | -0.3 | 0.1382 | 0.1449 |
| Time 54-69, pooled (%) | 198 | -0.194 [-0.480, +0.093] | -0.7097 | -1.32 | 0.186 | not applied (n < 1000) | 0.705 | +0.4 | -1.4 | 0.1430 | 0.1449 |
| Avg. daily time 54-69 (%) | 198 | -0.137 [-0.416, +0.141] | -0.4909 | -0.97 | 0.333 | not applied (n < 1000) | 0.805 | +1.2 | -0.6 | 0.1389 | 0.1449 |
| Time < 70, pooled (%) | 198 | -0.194 [-0.480, +0.093] | -0.7097 | -1.32 | 0.186 | not applied (n < 1000) | 0.705 | +0.4 | -1.4 | 0.1430 | 0.1449 |
| Avg. daily time < 70 (%) | 198 | -0.137 [-0.416, +0.141] | -0.4909 | -0.97 | 0.333 | not applied (n < 1000) | 0.805 | +1.2 | -0.6 | 0.1389 | 0.1449 |
| Time 181-250, pooled (%) | 198 | -0.083 [-0.394, +0.227] | -0.01772 | -0.53 | 0.598 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | 0.1391 | 0.1449 |
| Avg. daily time 181-250 (%) | 198 | -0.092 [-0.411, +0.226] | -0.02003 | -0.57 | 0.569 | not applied (n < 1000) | 0.963 | +1.6 | -0.2 | 0.1382 | 0.1449 |
| Time > 180, pooled (%) | 198 | -0.083 [-0.394, +0.227] | -0.01772 | -0.53 | 0.598 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | 0.1391 | 0.1449 |
| Avg. daily time > 180 (%) | 198 | -0.092 [-0.411, +0.226] | -0.02003 | -0.57 | 0.569 | not applied (n < 1000) | 0.963 | +1.6 | -0.2 | 0.1382 | 0.1449 |
| Nocturnal time > 180 (%) | 198 | -0.161 [-0.535, +0.213] | -0.03158 | -0.84 | 0.398 | not applied (n < 1000) | 0.822 | +1.0 | -0.9 | 0.1422 | 0.1449 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 198; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 198 | -0.101 [-1.202, +1.001] | -0.1948 | -0.18 | 0.858 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | 0.0463 | 0.0582 |
| Mean glucose (mg/dL) | 198 | +0.590 [-0.362, +1.541] | 0.0463 | 1.21 | 0.224 | not applied (n < 1000) | 0.734 | +0.1 | -1.9 | 0.0666 | 0.0582 |
| GMI (%) | 198 | +0.590 [-0.362, +1.541] | 1.935 | 1.21 | 0.224 | not applied (n < 1000) | 0.734 | +0.1 | -1.9 | 0.0666 | 0.0582 |
| Nocturnal mean 00-06h (mg/dL) | 198 | +0.501 [-0.440, +1.442] | 0.03478 | 1.04 | 0.297 | not applied (n < 1000) | 0.786 | +0.6 | -1.3 | 0.0619 | 0.0582 |
| Glucose SD, pooled (mg/dL) | 198 | +0.836 [-0.012, +1.684] | 0.1804 | 1.93 | 0.053 | not applied (n < 1000) | 0.547 | -1.5 | -3.5 | 0.0761 | 0.0582 |
| Avg. daily SD (mg/dL) | 198 | +0.709 [-0.125, +1.543] | 0.1573 | 1.67 | 0.096 | not applied (n < 1000) | 0.627 | -0.6 | -2.5 | 0.0698 | 0.0582 |
| CV (%) | 198 | +0.581 [-0.338, +1.500] | 0.1849 | 1.24 | 0.215 | not applied (n < 1000) | 0.734 | +0.4 | -1.6 | 0.0595 | 0.0582 |
| Mean / SD ratio | 198 | -0.435 [-1.319, +0.449] | -0.3641 | -0.96 | 0.335 | not applied (n < 1000) | 0.805 | +1.1 | -0.9 | 0.0560 | 0.0582 |
| Avg. daily mean / SD | 198 | -0.291 [-1.159, +0.577] | -0.1878 | -0.66 | 0.511 | not applied (n < 1000) | 0.940 | +1.6 | -0.4 | 0.0488 | 0.0582 |
| MAG (mg/dL/h) | 198 | +0.653 [-0.249, +1.555] | 0.1006 | 1.42 | 0.156 | not applied (n < 1000) | 0.705 | -0.4 | -2.4 | 0.0614 | 0.0582 |
| Avg. daily range (mg/dL) | 198 | +0.665 [-0.141, +1.470] | 0.03721 | 1.62 | 0.106 | not applied (n < 1000) | 0.643 | -0.4 | -2.3 | 0.0688 | 0.0582 |
| SD of daily means (mg/dL) | 198 | +0.497 [-0.535, +1.528] | 0.1925 | 0.94 | 0.345 | not applied (n < 1000) | 0.805 | +0.8 | -1.1 | 0.0547 | 0.0582 |
| Time in range 70-180, pooled (%) | 198 | -0.525 [-1.651, +0.601] | -0.1121 | -0.91 | 0.361 | not applied (n < 1000) | 0.820 | +0.5 | -1.4 | 0.0581 | 0.0582 |
| Avg. daily time in range 70-180 (%) | 198 | -0.571 [-1.649, +0.507] | -0.1247 | -1.04 | 0.299 | not applied (n < 1000) | 0.786 | +0.2 | -1.7 | 0.0615 | 0.0582 |
| Time 54-69, pooled (%) | 198 | +0.099 [-1.000, +1.198] | 0.3632 | 0.18 | 0.860 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | 0.0487 | 0.0582 |
| Avg. daily time 54-69 (%) | 198 | -0.041 [-0.930, +0.848] | -0.1469 | -0.09 | 0.928 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0527 | 0.0582 |
| Time < 70, pooled (%) | 198 | +0.099 [-1.000, +1.198] | 0.3632 | 0.18 | 0.860 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | 0.0487 | 0.0582 |
| Avg. daily time < 70 (%) | 198 | -0.041 [-0.930, +0.848] | -0.1469 | -0.09 | 0.928 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.0527 | 0.0582 |
| Time 181-250, pooled (%) | 198 | +0.515 [-0.607, +1.636] | 0.1093 | 0.90 | 0.368 | not applied (n < 1000) | 0.820 | +0.6 | -1.4 | 0.0577 | 0.0582 |
| Avg. daily time 181-250 (%) | 198 | +0.567 [-0.508, +1.643] | 0.123 | 1.03 | 0.301 | not applied (n < 1000) | 0.786 | +0.3 | -1.7 | 0.0613 | 0.0582 |
| Time > 180, pooled (%) | 198 | +0.515 [-0.607, +1.636] | 0.1093 | 0.90 | 0.368 | not applied (n < 1000) | 0.820 | +0.6 | -1.4 | 0.0577 | 0.0582 |
| Avg. daily time > 180 (%) | 198 | +0.567 [-0.508, +1.643] | 0.123 | 1.03 | 0.301 | not applied (n < 1000) | 0.786 | +0.3 | -1.7 | 0.0613 | 0.0582 |
| Nocturnal time > 180 (%) | 198 | +0.444 [-0.823, +1.710] | 0.08691 | 0.69 | 0.492 | not applied (n < 1000) | 0.911 | +1.0 | -1.0 | 0.0562 | 0.0582 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 198; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 198 | +0.243 [-3.091, +3.577] | 0.4709 | 0.14 | 0.886 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | -0.0534 | -0.0421 |
| Mean glucose (mg/dL) | 198 | +1.095 [-1.516, +3.706] | 0.08599 | 0.82 | 0.411 | not applied (n < 1000) | 0.822 | +1.1 | -0.9 | -0.0444 | -0.0421 |
| GMI (%) | 198 | +1.095 [-1.516, +3.706] | 3.595 | 0.82 | 0.411 | not applied (n < 1000) | 0.822 | +1.1 | -0.9 | -0.0444 | -0.0421 |
| Nocturnal mean 00-06h (mg/dL) | 198 | +0.339 [-2.263, +2.942] | 0.02357 | 0.26 | 0.798 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | -0.0475 | -0.0421 |
| Glucose SD, pooled (mg/dL) | 198 | +1.422 [-1.297, +4.141] | 0.3069 | 1.03 | 0.305 | not applied (n < 1000) | 0.786 | +0.6 | -1.3 | -0.0429 | -0.0421 |
| Avg. daily SD (mg/dL) | 198 | +1.525 [-0.988, +4.038] | 0.3383 | 1.19 | 0.234 | not applied (n < 1000) | 0.747 | +0.4 | -1.6 | -0.0375 | -0.0421 |
| CV (%) | 198 | +1.035 [-1.269, +3.338] | 0.3296 | 0.88 | 0.379 | not applied (n < 1000) | 0.820 | +1.3 | -0.7 | -0.0448 | -0.0421 |
| Mean / SD ratio | 198 | -1.632 [-3.806, +0.541] | -1.365 | -1.47 | 0.141 | not applied (n < 1000) | 0.698 | +0.2 | -1.7 | -0.0329 | -0.0421 |
| Avg. daily mean / SD | 198 | -1.754 [-3.729, +0.221] | -1.131 | -1.74 | 0.082 | not applied (n < 1000) | 0.627 | -0.1 | -2.1 | -0.0271 | -0.0421 |
| MAG (mg/dL/h) | 198 | +0.528 [-2.039, +3.094] | 0.08123 | 0.40 | 0.687 | not applied (n < 1000) | 0.984 | +1.8 | -0.2 | -0.0573 | -0.0421 |
| Avg. daily range (mg/dL) | 198 | +0.666 [-1.797, +3.130] | 0.03731 | 0.53 | 0.596 | not applied (n < 1000) | 0.963 | +1.7 | -0.3 | -0.0417 | -0.0421 |
| SD of daily means (mg/dL) | 198 | +1.863 [-1.548, +5.273] | 0.7219 | 1.07 | 0.284 | not applied (n < 1000) | 0.786 | -0.2 | -2.1 | -0.0459 | -0.0421 |
| Time in range 70-180, pooled (%) | 198 | -0.867 [-4.116, +2.383] | -0.185 | -0.52 | 0.601 | not applied (n < 1000) | 0.963 | +1.5 | -0.5 | -0.0542 | -0.0421 |
| Avg. daily time in range 70-180 (%) | 198 | -0.818 [-4.057, +2.421] | -0.1787 | -0.50 | 0.621 | not applied (n < 1000) | 0.963 | +1.5 | -0.4 | -0.0523 | -0.0421 |
| Time 54-69, pooled (%) | 198 | -0.429 [-2.646, +1.788] | -1.572 | -0.38 | 0.705 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | -0.0442 | -0.0421 |
| Avg. daily time 54-69 (%) | 198 | -0.211 [-2.237, +1.814] | -0.7546 | -0.20 | 0.838 | not applied (n < 1000) | 0.984 | +2.0 | +0.0 | -0.0445 | -0.0421 |
| Time < 70, pooled (%) | 198 | -0.429 [-2.646, +1.788] | -1.572 | -0.38 | 0.705 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | -0.0442 | -0.0421 |
| Avg. daily time < 70 (%) | 198 | -0.211 [-2.237, +1.814] | -0.7546 | -0.20 | 0.838 | not applied (n < 1000) | 0.984 | +2.0 | +0.0 | -0.0445 | -0.0421 |
| Time 181-250, pooled (%) | 198 | +0.884 [-2.362, +4.129] | 0.1877 | 0.53 | 0.594 | not applied (n < 1000) | 0.963 | +1.4 | -0.5 | -0.0539 | -0.0421 |
| Avg. daily time 181-250 (%) | 198 | +0.822 [-2.412, +4.056] | 0.1783 | 0.50 | 0.618 | not applied (n < 1000) | 0.963 | +1.5 | -0.4 | -0.0522 | -0.0421 |
| Time > 180, pooled (%) | 198 | +0.884 [-2.362, +4.129] | 0.1877 | 0.53 | 0.594 | not applied (n < 1000) | 0.963 | +1.4 | -0.5 | -0.0539 | -0.0421 |
| Avg. daily time > 180 (%) | 198 | +0.822 [-2.412, +4.056] | 0.1783 | 0.50 | 0.618 | not applied (n < 1000) | 0.963 | +1.5 | -0.4 | -0.0522 | -0.0421 |
| Nocturnal time > 180 (%) | 198 | -0.352 [-2.978, +2.273] | -0.06903 | -0.26 | 0.793 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | -0.0528 | -0.0421 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Steps per wear-day
*n = 178; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 178 | +141.242 [-511.338, +793.822] | 267.8 | 0.42 | 0.671 | not applied (n < 1000) | 0.984 | +1.8 | +0.0 | -0.0025 | 0.0019 |
| Mean glucose (mg/dL) | 178 | +338.866 [-430.895, +1108.628] | 25.74 | 0.86 | 0.388 | not applied (n < 1000) | 0.820 | +1.1 | -0.8 | -0.0132 | 0.0019 |
| GMI (%) | 178 | +338.866 [-430.895, +1108.628] | 1076 | 0.86 | 0.388 | not applied (n < 1000) | 0.820 | +1.1 | -0.8 | -0.0132 | 0.0019 |
| Nocturnal mean 00-06h (mg/dL) | 178 | +612.402 [-91.415, +1316.218] | 41.82 | 1.71 | 0.088 | not applied (n < 1000) | 0.627 | -1.1 | -2.9 | 0.0083 | 0.0019 |
| Glucose SD, pooled (mg/dL) | 178 | +112.723 [-593.119, +818.565] | 23.49 | 0.31 | 0.754 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0040 | 0.0019 |
| Avg. daily SD (mg/dL) | 178 | +117.425 [-579.108, +813.958] | 25.44 | 0.33 | 0.741 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | -0.0039 | 0.0019 |
| CV (%) | 178 | -85.822 [-766.988, +595.344] | -26.21 | -0.25 | 0.805 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0126 | 0.0019 |
| Mean / SD ratio | 178 | -62.778 [-705.169, +579.613] | -50.21 | -0.19 | 0.848 | not applied (n < 1000) | 0.984 | +2.0 | +0.1 | -0.0120 | 0.0019 |
| Avg. daily mean / SD | 178 | -169.684 [-796.167, +456.798] | -105.7 | -0.53 | 0.596 | not applied (n < 1000) | 0.963 | +1.8 | -0.1 | -0.0117 | 0.0019 |
| MAG (mg/dL/h) | 178 | +380.770 [-277.076, +1038.617] | 57.27 | 1.13 | 0.257 | not applied (n < 1000) | 0.786 | +0.8 | -1.1 | -0.0082 | 0.0019 |
| Avg. daily range (mg/dL) | 178 | +82.600 [-616.350, +781.551] | 4.508 | 0.23 | 0.817 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0077 | 0.0019 |
| SD of daily means (mg/dL) | 178 | -85.482 [-933.891, +762.928] | -32.31 | -0.20 | 0.843 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0059 | 0.0019 |
| Time in range 70-180, pooled (%) | 178 | +141.908 [-638.270, +922.085] | 29.3 | 0.36 | 0.721 | not applied (n < 1000) | 0.984 | +1.8 | -0.0 | -0.0166 | 0.0019 |
| Avg. daily time in range 70-180 (%) | 178 | +111.386 [-697.497, +920.269] | 23.45 | 0.27 | 0.787 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0172 | 0.0019 |
| Time 54-69, pooled (%) | 178 | -440.222 [-1081.368, +200.923] | -1439 | -1.35 | 0.178 | not applied (n < 1000) | 0.705 | +0.5 | -1.4 | -0.0046 | 0.0019 |
| Avg. daily time 54-69 (%) | 178 | -559.151 [-1194.178, +75.876] | -1758 | -1.73 | 0.084 | not applied (n < 1000) | 0.627 | -0.5 | -2.3 | 0.0036 | 0.0019 |
| Time < 70, pooled (%) | 178 | -440.222 [-1081.368, +200.923] | -1439 | -1.35 | 0.178 | not applied (n < 1000) | 0.705 | +0.5 | -1.4 | -0.0046 | 0.0019 |
| Avg. daily time < 70 (%) | 178 | -559.151 [-1194.178, +75.876] | -1758 | -1.73 | 0.084 | not applied (n < 1000) | 0.627 | -0.5 | -2.3 | 0.0036 | 0.0019 |
| Time 181-250, pooled (%) | 178 | -112.745 [-892.046, +666.557] | -23.14 | -0.28 | 0.777 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0173 | 0.0019 |
| Avg. daily time 181-250 (%) | 178 | -72.470 [-881.171, +736.231] | -15.13 | -0.18 | 0.861 | not applied (n < 1000) | 0.984 | +2.0 | +0.1 | -0.0180 | 0.0019 |
| Time > 180, pooled (%) | 178 | -112.745 [-892.046, +666.557] | -23.14 | -0.28 | 0.777 | not applied (n < 1000) | 0.984 | +1.9 | +0.1 | -0.0173 | 0.0019 |
| Avg. daily time > 180 (%) | 178 | -72.470 [-881.171, +736.231] | -15.13 | -0.18 | 0.861 | not applied (n < 1000) | 0.984 | +2.0 | +0.1 | -0.0180 | 0.0019 |
| Nocturnal time > 180 (%) | 178 | +174.103 [-594.092, +942.298] | 34.23 | 0.44 | 0.657 | not applied (n < 1000) | 0.984 | +1.8 | -0.1 | -0.0060 | 0.0019 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 178; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 178 | +0.811 [-1.141, +2.763] | 1.538 | 0.81 | 0.415 | not applied (n < 1000) | 0.825 | +1.4 | +0.0 | 0.0292 | 0.0346 |
| Mean glucose (mg/dL) | 178 | +1.049 [-1.111, +3.209] | 0.07966 | 0.95 | 0.341 | not applied (n < 1000) | 0.805 | +0.9 | -0.5 | 0.0193 | 0.0346 |
| GMI (%) | 178 | +1.049 [-1.111, +3.209] | 3.33 | 0.95 | 0.341 | not applied (n < 1000) | 0.805 | +0.9 | -0.5 | 0.0193 | 0.0346 |
| Nocturnal mean 00-06h (mg/dL) | 178 | +1.791 [-0.314, +3.897] | 0.1223 | 1.67 | 0.095 | not applied (n < 1000) | 0.627 | -1.2 | -2.6 | 0.0411 | 0.0346 |
| Glucose SD, pooled (mg/dL) | 178 | +0.172 [-1.915, +2.260] | 0.03594 | 0.16 | 0.871 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0231 | 0.0346 |
| Avg. daily SD (mg/dL) | 178 | +0.125 [-1.885, +2.136] | 0.02716 | 0.12 | 0.903 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0230 | 0.0346 |
| CV (%) | 178 | -0.561 [-2.690, +1.568] | -0.1714 | -0.52 | 0.606 | not applied (n < 1000) | 0.963 | +1.7 | +0.3 | 0.0183 | 0.0346 |
| Mean / SD ratio | 178 | +0.189 [-1.727, +2.105] | 0.1513 | 0.19 | 0.847 | not applied (n < 1000) | 0.984 | +2.0 | +0.6 | 0.0177 | 0.0346 |
| Avg. daily mean / SD | 178 | -0.134 [-1.974, +1.707] | -0.08324 | -0.14 | 0.887 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0173 | 0.0346 |
| MAG (mg/dL/h) | 178 | +0.765 [-1.040, +2.570] | 0.115 | 0.83 | 0.406 | not applied (n < 1000) | 0.822 | +1.4 | +0.0 | 0.0255 | 0.0346 |
| Avg. daily range (mg/dL) | 178 | -0.005 [-2.099, +2.089] | -0.0002722 | -0.00 | 0.996 | not applied (n < 1000) | 0.999 | +2.0 | +0.6 | 0.0180 | 0.0346 |
| SD of daily means (mg/dL) | 178 | -0.035 [-2.570, +2.501] | -0.01304 | -0.03 | 0.979 | not applied (n < 1000) | 0.999 | +2.0 | +0.6 | 0.0234 | 0.0346 |
| Time in range 70-180, pooled (%) | 178 | +0.214 [-1.872, +2.300] | 0.04414 | 0.20 | 0.841 | not applied (n < 1000) | 0.984 | +2.0 | +0.6 | 0.0160 | 0.0346 |
| Avg. daily time in range 70-180 (%) | 178 | +0.109 [-2.004, +2.222] | 0.02295 | 0.10 | 0.919 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0168 | 0.0346 |
| Time 54-69, pooled (%) | 178 | -1.281 [-3.252, +0.690] | -4.188 | -1.27 | 0.203 | not applied (n < 1000) | 0.719 | +0.4 | -1.0 | 0.0268 | 0.0346 |
| Avg. daily time 54-69 (%) | 178 | -1.770 [-3.598, +0.058] | -5.565 | -1.90 | 0.058 | not applied (n < 1000) | 0.547 | -1.0 | -2.4 | 0.0397 | 0.0346 |
| Time < 70, pooled (%) | 178 | -1.281 [-3.252, +0.690] | -4.188 | -1.27 | 0.203 | not applied (n < 1000) | 0.719 | +0.4 | -1.0 | 0.0268 | 0.0346 |
| Avg. daily time < 70 (%) | 178 | -1.770 [-3.598, +0.058] | -5.565 | -1.90 | 0.058 | not applied (n < 1000) | 0.547 | -1.0 | -2.4 | 0.0397 | 0.0346 |
| Time 181-250, pooled (%) | 178 | -0.131 [-2.217, +1.955] | -0.02688 | -0.12 | 0.902 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0151 | 0.0346 |
| Avg. daily time 181-250 (%) | 178 | +0.011 [-2.107, +2.129] | 0.002338 | 0.01 | 0.992 | not applied (n < 1000) | 0.999 | +2.0 | +0.6 | 0.0157 | 0.0346 |
| Time > 180, pooled (%) | 178 | -0.131 [-2.217, +1.955] | -0.02688 | -0.12 | 0.902 | not applied (n < 1000) | 0.986 | +2.0 | +0.6 | 0.0151 | 0.0346 |
| Avg. daily time > 180 (%) | 178 | +0.011 [-2.107, +2.129] | 0.002338 | 0.01 | 0.992 | not applied (n < 1000) | 0.999 | +2.0 | +0.6 | 0.0157 | 0.0346 |
| Nocturnal time > 180 (%) | 178 | +1.023 [-1.472, +3.519] | 0.2012 | 0.80 | 0.422 | not applied (n < 1000) | 0.828 | +1.0 | -0.4 | 0.0241 | 0.0346 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 177; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 177 | +0.216 [-1.126, +1.558] | 0.4085 | 0.32 | 0.753 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | 0.1127 | 0.1209 |
| Mean glucose (mg/dL) | 177 | +0.771 [-0.451, +1.994] | 0.05894 | 1.24 | 0.216 | not applied (n < 1000) | 0.734 | +0.3 | -1.6 | 0.1189 | 0.1209 |
| GMI (%) | 177 | +0.771 [-0.451, +1.994] | 2.464 | 1.24 | 0.216 | not applied (n < 1000) | 0.734 | +0.3 | -1.6 | 0.1189 | 0.1209 |
| Nocturnal mean 00-06h (mg/dL) | 177 | +0.626 [-0.589, +1.841] | 0.04274 | 1.01 | 0.312 | not applied (n < 1000) | 0.787 | +0.9 | -1.0 | 0.1151 | 0.1209 |
| Glucose SD, pooled (mg/dL) | 177 | +0.037 [-1.190, +1.265] | 0.007853 | 0.06 | 0.952 | not applied (n < 1000) | 0.999 | +2.0 | +0.1 | 0.1150 | 0.1209 |
| Avg. daily SD (mg/dL) | 177 | +0.078 [-1.118, +1.275] | 0.01714 | 0.13 | 0.898 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.1157 | 0.1209 |
| CV (%) | 177 | -0.442 [-1.642, +0.757] | -0.1351 | -0.72 | 0.470 | not applied (n < 1000) | 0.890 | +1.5 | -0.4 | 0.1201 | 0.1209 |
| Mean / SD ratio | 177 | +0.193 [-1.022, +1.408] | 0.1544 | 0.31 | 0.755 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | 0.1172 | 0.1209 |
| Avg. daily mean / SD | 177 | +0.043 [-1.179, +1.266] | 0.02686 | 0.07 | 0.945 | not applied (n < 1000) | 0.994 | +2.0 | +0.1 | 0.1153 | 0.1209 |
| MAG (mg/dL/h) | 177 | +0.732 [-0.456, +1.920] | 0.1099 | 1.21 | 0.227 | not applied (n < 1000) | 0.734 | +0.5 | -1.4 | 0.1111 | 0.1209 |
| Avg. daily range (mg/dL) | 177 | +0.347 [-0.906, +1.600] | 0.01903 | 0.54 | 0.587 | not applied (n < 1000) | 0.963 | +1.7 | -0.2 | 0.1153 | 0.1209 |
| SD of daily means (mg/dL) | 177 | -0.306 [-1.681, +1.070] | -0.1155 | -0.44 | 0.663 | not applied (n < 1000) | 0.984 | +1.8 | -0.1 | 0.1107 | 0.1209 |
| Time in range 70-180, pooled (%) | 177 | +0.068 [-1.256, +1.392] | 0.01438 | 0.10 | 0.920 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.1074 | 0.1209 |
| Avg. daily time in range 70-180 (%) | 177 | +0.030 [-1.313, +1.373] | 0.006418 | 0.04 | 0.966 | not applied (n < 1000) | 0.999 | +2.0 | +0.1 | 0.1068 | 0.1209 |
| Time 54-69, pooled (%) | 177 | -1.385 [-2.401, -0.369] | -4.517 | -2.67 | 0.008** | not applied (n < 1000) | 0.310 | -3.3 | -5.1 | 0.1281 | 0.1209 |
| Avg. daily time 54-69 (%) | 177 | -1.375 [-2.534, -0.216] | -4.312 | -2.32 | 0.020* | not applied (n < 1000) | 0.316 | -3.2 | -5.1 | 0.1234 | 0.1209 |
| Time < 70, pooled (%) | 177 | -1.385 [-2.401, -0.369] | -4.517 | -2.67 | 0.008** | not applied (n < 1000) | 0.310 | -3.3 | -5.1 | 0.1281 | 0.1209 |
| Avg. daily time < 70 (%) | 177 | -1.375 [-2.534, -0.216] | -4.312 | -2.32 | 0.020* | not applied (n < 1000) | 0.316 | -3.2 | -5.1 | 0.1234 | 0.1209 |
| Time 181-250, pooled (%) | 177 | +0.021 [-1.308, +1.350] | 0.004427 | 0.03 | 0.975 | not applied (n < 1000) | 0.999 | +2.0 | +0.1 | 0.1076 | 0.1209 |
| Avg. daily time 181-250 (%) | 177 | +0.064 [-1.278, +1.407] | 0.01385 | 0.09 | 0.925 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.1075 | 0.1209 |
| Time > 180, pooled (%) | 177 | +0.021 [-1.308, +1.350] | 0.004427 | 0.03 | 0.975 | not applied (n < 1000) | 0.999 | +2.0 | +0.1 | 0.1076 | 0.1209 |
| Avg. daily time > 180 (%) | 177 | +0.064 [-1.278, +1.407] | 0.01385 | 0.09 | 0.925 | not applied (n < 1000) | 0.986 | +2.0 | +0.1 | 0.1075 | 0.1209 |
| Nocturnal time > 180 (%) | 177 | -0.171 [-1.183, +0.840] | -0.0338 | -0.33 | 0.740 | not applied (n < 1000) | 0.984 | +1.9 | +0.0 | 0.1185 | 0.1209 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 178; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 178 | -3.239 [-13.731, +7.253] | -6.151 | -0.61 | 0.545 | not applied (n < 1000) | 0.963 | +1.7 | +0.0 | -0.1070 | -0.1029 |
| Mean glucose (mg/dL) | 178 | -8.844 [-21.666, +3.979] | -0.6717 | -1.35 | 0.176 | not applied (n < 1000) | 0.705 | -0.8 | -2.4 | -0.1170 | -0.1029 |
| GMI (%) | 178 | -8.844 [-21.666, +3.979] | -28.08 | -1.35 | 0.176 | not applied (n < 1000) | 0.705 | -0.8 | -2.4 | -0.1170 | -0.1029 |
| Nocturnal mean 00-06h (mg/dL) | 178 | -7.712 [-21.080, +5.655] | -0.5295 | -1.13 | 0.258 | not applied (n < 1000) | 0.786 | -0.1 | -1.8 | -0.1224 | -0.1029 |
| Glucose SD, pooled (mg/dL) | 178 | -6.311 [-19.952, +7.330] | -1.306 | -0.91 | 0.365 | not applied (n < 1000) | 0.820 | +0.7 | -0.9 | -0.1141 | -0.1029 |
| Avg. daily SD (mg/dL) | 178 | -8.166 [-20.668, +4.336] | -1.757 | -1.28 | 0.200 | not applied (n < 1000) | 0.719 | -0.2 | -1.8 | -0.1078 | -0.1029 |
| CV (%) | 178 | -2.273 [-15.864, +11.319] | -0.6935 | -0.33 | 0.743 | not applied (n < 1000) | 0.984 | +1.8 | +0.2 | -0.1172 | -0.1029 |
| Mean / SD ratio | 178 | +1.945 [-12.442, +16.333] | 1.555 | 0.26 | 0.791 | not applied (n < 1000) | 0.984 | +1.9 | +0.2 | -0.1137 | -0.1029 |
| Avg. daily mean / SD | 178 | +4.776 [-7.902, +17.454] | 2.971 | 0.74 | 0.460 | not applied (n < 1000) | 0.877 | +1.3 | -0.4 | -0.1095 | -0.1029 |
| MAG (mg/dL/h) | 178 | -13.804 [-23.796, -3.812] | -2.073 | -2.71 | 0.007** | not applied (n < 1000) | 0.310 | -5.0 | -6.7 | -0.0914 | -0.1029 |
| Avg. daily range (mg/dL) | 178 | -5.504 [-18.019, +7.011] | -0.2984 | -0.86 | 0.389 | not applied (n < 1000) | 0.820 | +1.0 | -0.7 | -0.1185 | -0.1029 |
| SD of daily means (mg/dL) | 178 | +1.231 [-11.811, +14.273] | 0.4611 | 0.18 | 0.853 | not applied (n < 1000) | 0.984 | +2.0 | +0.3 | -0.1178 | -0.1029 |
| Time in range 70-180, pooled (%) | 178 | +1.826 [-9.039, +12.691] | 0.3759 | 0.33 | 0.742 | not applied (n < 1000) | 0.984 | +1.9 | +0.2 | -0.1114 | -0.1029 |
| Avg. daily time in range 70-180 (%) | 178 | +2.235 [-8.438, +12.907] | 0.4692 | 0.41 | 0.682 | not applied (n < 1000) | 0.984 | +1.8 | +0.2 | -0.1131 | -0.1029 |
| Time 54-69, pooled (%) | 178 | +6.596 [-8.266, +21.459] | 21.45 | 0.87 | 0.384 | not applied (n < 1000) | 0.820 | +0.5 | -1.2 | -0.1051 | -0.1029 |
| Avg. daily time 54-69 (%) | 178 | +5.620 [-10.095, +21.335] | 17.56 | 0.70 | 0.483 | not applied (n < 1000) | 0.900 | +0.9 | -0.8 | -0.1123 | -0.1029 |
| Time < 70, pooled (%) | 178 | +6.596 [-8.266, +21.459] | 21.45 | 0.87 | 0.384 | not applied (n < 1000) | 0.820 | +0.5 | -1.2 | -0.1051 | -0.1029 |
| Avg. daily time < 70 (%) | 178 | +5.620 [-10.095, +21.335] | 17.56 | 0.70 | 0.483 | not applied (n < 1000) | 0.900 | +0.9 | -0.8 | -0.1123 | -0.1029 |
| Time 181-250, pooled (%) | 178 | -2.229 [-13.094, +8.636] | -0.4559 | -0.40 | 0.688 | not applied (n < 1000) | 0.984 | +1.8 | +0.2 | -0.1108 | -0.1029 |
| Avg. daily time 181-250 (%) | 178 | -2.591 [-13.331, +8.149] | -0.5393 | -0.47 | 0.636 | not applied (n < 1000) | 0.963 | +1.8 | +0.1 | -0.1128 | -0.1029 |
| Time > 180, pooled (%) | 178 | -2.229 [-13.094, +8.636] | -0.4559 | -0.40 | 0.688 | not applied (n < 1000) | 0.984 | +1.8 | +0.2 | -0.1108 | -0.1029 |
| Avg. daily time > 180 (%) | 178 | -2.591 [-13.331, +8.149] | -0.5393 | -0.47 | 0.636 | not applied (n < 1000) | 0.963 | +1.8 | +0.1 | -0.1128 | -0.1029 |
| Nocturnal time > 180 (%) | 178 | +2.777 [-13.838, +19.392] | 0.5457 | 0.33 | 0.743 | not applied (n < 1000) | 0.984 | +1.7 | +0.1 | -0.1380 | -0.1029 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 177; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 177 | -0.149 [-2.873, +2.575] | -0.2822 | -0.11 | 0.915 | not applied (n < 1000) | 0.986 | +2.0 | +0.0 | 0.1346 | 0.1468 |
| Mean glucose (mg/dL) | 177 | +0.313 [-2.220, +2.847] | 0.02394 | 0.24 | 0.809 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | 0.1391 | 0.1468 |
| GMI (%) | 177 | +0.313 [-2.220, +2.847] | 1.001 | 0.24 | 0.809 | not applied (n < 1000) | 0.984 | +1.9 | -0.0 | 0.1391 | 0.1468 |
| Nocturnal mean 00-06h (mg/dL) | 177 | -0.006 [-2.543, +2.530] | -0.0004308 | -0.00 | 0.996 | not applied (n < 1000) | 0.999 | +2.0 | +0.0 | 0.1415 | 0.1468 |
| Glucose SD, pooled (mg/dL) | 177 | -0.263 [-2.911, +2.385] | -0.05526 | -0.19 | 0.846 | not applied (n < 1000) | 0.984 | +2.0 | -0.0 | 0.1453 | 0.1468 |
| Avg. daily SD (mg/dL) | 177 | -0.341 [-2.915, +2.233] | -0.0745 | -0.26 | 0.795 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | 0.1446 | 0.1468 |
| CV (%) | 177 | -0.471 [-3.048, +2.105] | -0.1441 | -0.36 | 0.720 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | 0.1459 | 0.1468 |
| Mean / SD ratio | 177 | +0.393 [-2.156, +2.943] | 0.3146 | 0.30 | 0.762 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | 0.1429 | 0.1468 |
| Avg. daily mean / SD | 177 | +0.193 [-2.323, +2.710] | 0.1204 | 0.15 | 0.880 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.1391 | 0.1468 |
| MAG (mg/dL/h) | 177 | +0.378 [-2.428, +3.184] | 0.05676 | 0.26 | 0.792 | not applied (n < 1000) | 0.984 | +1.9 | -0.1 | 0.1211 | 0.1468 |
| Avg. daily range (mg/dL) | 177 | -0.240 [-2.948, +2.467] | -0.01318 | -0.17 | 0.862 | not applied (n < 1000) | 0.984 | +2.0 | -0.0 | 0.1395 | 0.1468 |
| SD of daily means (mg/dL) | 177 | -0.158 [-2.818, +2.503] | -0.05954 | -0.12 | 0.907 | not applied (n < 1000) | 0.986 | +2.0 | -0.0 | 0.1444 | 0.1468 |
| Time in range 70-180, pooled (%) | 177 | +1.235 [-1.071, +3.541] | 0.2617 | 1.05 | 0.294 | not applied (n < 1000) | 0.786 | +1.1 | -0.9 | 0.1445 | 0.1468 |
| Avg. daily time in range 70-180 (%) | 177 | +1.225 [-1.063, +3.512] | 0.2656 | 1.05 | 0.294 | not applied (n < 1000) | 0.786 | +1.1 | -0.9 | 0.1445 | 0.1468 |
| Time 54-69, pooled (%) | 177 | -2.697 [-4.781, -0.612] | -8.795 | -2.54 | 0.011* | not applied (n < 1000) | 0.310 | -2.4 | -4.4 | 0.1532 | 0.1468 |
| Avg. daily time 54-69 (%) | 177 | -2.731 [-5.003, -0.460] | -8.569 | -2.36 | 0.018* | not applied (n < 1000) | 0.316 | -2.6 | -4.5 | 0.1485 | 0.1468 |
| Time < 70, pooled (%) | 177 | -2.697 [-4.781, -0.612] | -8.795 | -2.54 | 0.011* | not applied (n < 1000) | 0.310 | -2.4 | -4.4 | 0.1532 | 0.1468 |
| Avg. daily time < 70 (%) | 177 | -2.731 [-5.003, -0.460] | -8.569 | -2.36 | 0.018* | not applied (n < 1000) | 0.316 | -2.6 | -4.5 | 0.1485 | 0.1468 |
| Time 181-250, pooled (%) | 177 | -1.051 [-3.384, +1.282] | -0.2214 | -0.88 | 0.377 | not applied (n < 1000) | 0.820 | +1.3 | -0.7 | 0.1433 | 0.1468 |
| Avg. daily time 181-250 (%) | 177 | -1.024 [-3.335, +1.288] | -0.2201 | -0.87 | 0.385 | not applied (n < 1000) | 0.820 | +1.4 | -0.6 | 0.1434 | 0.1468 |
| Time > 180, pooled (%) | 177 | -1.051 [-3.384, +1.282] | -0.2214 | -0.88 | 0.377 | not applied (n < 1000) | 0.820 | +1.3 | -0.7 | 0.1433 | 0.1468 |
| Avg. daily time > 180 (%) | 177 | -1.024 [-3.335, +1.288] | -0.2201 | -0.87 | 0.385 | not applied (n < 1000) | 0.820 | +1.4 | -0.6 | 0.1434 | 0.1468 |
| Nocturnal time > 180 (%) | 177 | -0.563 [-3.274, +2.147] | -0.111 | -0.41 | 0.684 | not applied (n < 1000) | 0.984 | +1.8 | -0.2 | 0.1390 | 0.1468 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort); Time < 54, pooled (%) (predictor constant in this cohort); Avg. daily time < 54 (%) (predictor constant in this cohort); Time 54-250, pooled (%) (predictor constant in this cohort); Avg. daily time 54-250 (%) (predictor constant in this cohort); Any reading > 250 during wear (0/1) (predictor constant in this cohort); Time > 250, pooled (%) (predictor constant in this cohort); Avg. daily time > 250 (%) (predictor constant in this cohort)


---

## Cohort: Hypoglycaemia exposure: at least one reading < 54

### Population: Total analysis base

#### MoCA total score (0-30)
*n = 638; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 638 | -0.523 [-0.761, -0.285] | -0.62 | -4.30 | 1.7e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -17.9 | +0.0 | 0.0911 | 0.0671 |
| Mean glucose (mg/dL) | 638 | -0.435 [-0.690, -0.180] | -0.01795 | -3.34 | 8.3e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -12.1 | +5.7 | 0.0849 | 0.0671 |
| GMI (%) | 638 | -0.435 [-0.690, -0.180] | -0.7503 | -3.34 | 8.3e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -12.1 | +5.7 | 0.0849 | 0.0671 |
| Nocturnal mean 00-06h (mg/dL) | 638 | -0.397 [-0.641, -0.153] | -0.01643 | -3.19 | 0.001** | not applied (n < 1000) | 0.023 (q<0.05) | -9.9 | +8.0 | 0.0814 | 0.0671 |
| Glucose SD, pooled (mg/dL) | 638 | -0.442 [-0.702, -0.182] | -0.03658 | -3.34 | 8.5e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -11.8 | +6.1 | 0.0808 | 0.0671 |
| Avg. daily SD (mg/dL) | 638 | -0.423 [-0.689, -0.157] | -0.04056 | -3.11 | 0.002** | not applied (n < 1000) | 0.026 (q<0.05) | -10.5 | +7.3 | 0.0782 | 0.0671 |
| CV (%) | 638 | -0.326 [-0.561, -0.090] | -0.05333 | -2.71 | 0.007** | not applied (n < 1000) | 0.044 (q<0.05) | -5.4 | +12.5 | 0.0692 | 0.0671 |
| Mean / SD ratio | 638 | +0.349 [+0.121, +0.577] | 0.2686 | 3.00 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -6.8 | +11.1 | 0.0721 | 0.0671 |
| Avg. daily mean / SD | 638 | +0.259 [+0.028, +0.490] | 0.1635 | 2.20 | 0.028* | not applied (n < 1000) | 0.102 | -2.8 | +15.0 | 0.0666 | 0.0671 |
| MAG (mg/dL/h) | 638 | -0.189 [-0.434, +0.056] | -0.01991 | -1.51 | 0.130 | not applied (n < 1000) | 0.289 | -0.7 | +17.1 | 0.0666 | 0.0671 |
| Avg. daily range (mg/dL) | 638 | -0.348 [-0.613, -0.082] | -0.008891 | -2.57 | 0.010* | not applied (n < 1000) | 0.061 | -6.6 | +11.2 | 0.0722 | 0.0671 |
| SD of daily means (mg/dL) | 638 | -0.317 [-0.564, -0.070] | -0.04549 | -2.51 | 0.012* | not applied (n < 1000) | 0.064 | -5.6 | +12.3 | 0.0742 | 0.0671 |
| Time in range 70-180, pooled (%) | 638 | +0.475 [+0.213, +0.736] | 0.03654 | 3.56 | 3.7e-04*** | not applied (n < 1000) | 0.010 (q<0.05) | -14.7 | +3.1 | 0.0872 | 0.0671 |
| Avg. daily time in range 70-180 (%) | 638 | +0.466 [+0.203, +0.729] | 0.03564 | 3.47 | 5.2e-04*** | not applied (n < 1000) | 0.013 (q<0.05) | -14.1 | +3.8 | 0.0860 | 0.0671 |
| Time < 54, pooled (%) | 638 | -0.023 [-0.306, +0.261] | -0.02619 | -0.16 | 0.875 | not applied (n < 1000) | 0.932 | +2.0 | +19.8 | 0.0633 | 0.0671 |
| Avg. daily time < 54 (%) | 638 | -0.030 [-0.285, +0.226] | -0.03931 | -0.23 | 0.821 | not applied (n < 1000) | 0.905 | +1.9 | +19.8 | 0.0631 | 0.0671 |
| Time 54-69, pooled (%) | 638 | -0.125 [-0.336, +0.085] | -0.05524 | -1.17 | 0.244 | not applied (n < 1000) | 0.465 | +0.8 | +18.6 | 0.0680 | 0.0671 |
| Avg. daily time 54-69 (%) | 638 | -0.125 [-0.345, +0.095] | -0.05295 | -1.11 | 0.267 | not applied (n < 1000) | 0.503 | +0.8 | +18.6 | 0.0677 | 0.0671 |
| Time < 70, pooled (%) | 638 | -0.109 [-0.320, +0.102] | -0.03879 | -1.01 | 0.311 | not applied (n < 1000) | 0.543 | +1.1 | +18.9 | 0.0670 | 0.0671 |
| Avg. daily time < 70 (%) | 638 | -0.111 [-0.329, +0.106] | -0.03886 | -1.00 | 0.317 | not applied (n < 1000) | 0.547 | +1.0 | +18.9 | 0.0669 | 0.0671 |
| Time 54-250, pooled (%) | 638 | +0.415 [+0.137, +0.694] | 0.07249 | 2.92 | 0.003** | not applied (n < 1000) | 0.031 (q<0.05) | -11.4 | +6.5 | 0.0827 | 0.0671 |
| Avg. daily time 54-250 (%) | 638 | +0.438 [+0.161, +0.714] | 0.08396 | 3.10 | 0.002** | not applied (n < 1000) | 0.026 (q<0.05) | -12.8 | +5.1 | 0.0850 | 0.0671 |
| Time 181-250, pooled (%) | 638 | -0.374 [-0.633, -0.115] | -0.04126 | -2.83 | 0.005** | not applied (n < 1000) | 0.036 (q<0.05) | -8.2 | +9.6 | 0.0766 | 0.0671 |
| Avg. daily time 181-250 (%) | 638 | -0.365 [-0.619, -0.111] | -0.03923 | -2.81 | 0.005** | not applied (n < 1000) | 0.037 (q<0.05) | -7.8 | +10.1 | 0.0758 | 0.0671 |
| Time > 180, pooled (%) | 638 | -0.449 [-0.717, -0.180] | -0.03461 | -3.28 | 0.001** | not applied (n < 1000) | 0.020 (q<0.05) | -13.0 | +4.9 | 0.0852 | 0.0671 |
| Avg. daily time > 180 (%) | 638 | -0.442 [-0.712, -0.171] | -0.03409 | -3.20 | 0.001** | not applied (n < 1000) | 0.023 (q<0.05) | -12.5 | +5.4 | 0.0844 | 0.0671 |
| Nocturnal time > 180 (%) | 638 | -0.403 [-0.665, -0.140] | -0.03294 | -3.01 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -10.4 | +7.4 | 0.0813 | 0.0671 |
| Any reading > 250 during wear (0/1) | 638 | -0.280 [-0.535, -0.024] | -0.6163 | -2.15 | 0.032* | not applied (n < 1000) | 0.109 | -3.8 | +14.1 | 0.0671 | 0.0671 |
| Time > 250, pooled (%) | 638 | -0.418 [-0.700, -0.135] | -0.07402 | -2.90 | 0.004** | not applied (n < 1000) | 0.032 (q<0.05) | -11.6 | +6.3 | 0.0835 | 0.0671 |
| Avg. daily time > 250 (%) | 638 | -0.441 [-0.723, -0.159] | -0.08631 | -3.06 | 0.002** | not applied (n < 1000) | 0.028 (q<0.05) | -13.1 | +4.8 | 0.0860 | 0.0671 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 638; events = 228; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 638 | OR 1.432 [1.180, 1.737] | 0.4257 | 3.64 | 2.7e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -12.9 | +0.0 | 0.6626 | 0.6412 |
| Mean glucose (mg/dL) | 638 | OR 1.238 [1.038, 1.476] | 0.008797 | 2.37 | 0.018* | not applied (n < 1000) | 0.080 | -3.8 | +9.0 | 0.6473 | 0.6412 |
| GMI (%) | 638 | OR 1.238 [1.038, 1.476] | 0.3678 | 2.37 | 0.018* | not applied (n < 1000) | 0.080 | -3.8 | +9.0 | 0.6473 | 0.6412 |
| Nocturnal mean 00-06h (mg/dL) | 638 | OR 1.186 [0.997, 1.411] | 0.007052 | 1.93 | 0.054 | not applied (n < 1000) | 0.157 | -1.8 | +11.1 | 0.6455 | 0.6412 |
| Glucose SD, pooled (mg/dL) | 638 | OR 1.301 [1.083, 1.562] | 0.02175 | 2.81 | 0.005** | not applied (n < 1000) | 0.037 (q<0.05) | -6.3 | +6.6 | 0.6480 | 0.6412 |
| Avg. daily SD (mg/dL) | 638 | OR 1.263 [1.052, 1.516] | 0.0224 | 2.51 | 0.012* | not applied (n < 1000) | 0.064 | -4.5 | +8.3 | 0.6473 | 0.6412 |
| CV (%) | 638 | OR 1.258 [1.050, 1.507] | 0.03761 | 2.49 | 0.013* | not applied (n < 1000) | 0.064 | -4.3 | +8.6 | 0.6460 | 0.6412 |
| Mean / SD ratio | 638 | OR 0.802 [0.667, 0.964] | -0.1697 | -2.35 | 0.019* | not applied (n < 1000) | 0.084 | -3.6 | +9.2 | 0.6445 | 0.6412 |
| Avg. daily mean / SD | 638 | OR 0.848 [0.706, 1.019] | -0.1041 | -1.76 | 0.078 | not applied (n < 1000) | 0.196 | -1.2 | +11.7 | 0.6433 | 0.6412 |
| MAG (mg/dL/h) | 638 | OR 1.099 [0.927, 1.303] | 0.009928 | 1.08 | 0.278 | not applied (n < 1000) | 0.507 | +0.8 | +13.7 | 0.6383 | 0.6412 |
| Avg. daily range (mg/dL) | 638 | OR 1.199 [1.004, 1.432] | 0.004637 | 2.00 | 0.045* | not applied (n < 1000) | 0.135 | -2.0 | +10.8 | 0.6445 | 0.6412 |
| SD of daily means (mg/dL) | 638 | OR 1.232 [1.025, 1.481] | 0.02997 | 2.23 | 0.026* | not applied (n < 1000) | 0.097 | -3.3 | +9.5 | 0.6430 | 0.6412 |
| Time in range 70-180, pooled (%) | 638 | OR 0.752 [0.628, 0.900] | -0.02197 | -3.10 | 0.002** | not applied (n < 1000) | 0.026 (q<0.05) | -8.2 | +4.6 | 0.6551 | 0.6412 |
| Avg. daily time in range 70-180 (%) | 638 | OR 0.758 [0.634, 0.907] | -0.02115 | -3.03 | 0.002** | not applied (n < 1000) | 0.028 (q<0.05) | -7.7 | +5.2 | 0.6542 | 0.6412 |
| Time < 54, pooled (%) | 638 | OR 1.067 [0.901, 1.264] | 0.07418 | 0.75 | 0.455 | not applied (n < 1000) | 0.687 | +1.4 | +14.3 | 0.6434 | 0.6412 |
| Avg. daily time < 54 (%) | 638 | OR 1.074 [0.910, 1.268] | 0.09517 | 0.84 | 0.399 | not applied (n < 1000) | 0.638 | +1.3 | +14.1 | 0.6408 | 0.6412 |
| Time 54-69, pooled (%) | 638 | OR 1.229 [1.038, 1.456] | 0.09098 | 2.39 | 0.017* | not applied (n < 1000) | 0.080 | -3.8 | +9.0 | 0.6467 | 0.6412 |
| Avg. daily time 54-69 (%) | 638 | OR 1.235 [1.042, 1.463] | 0.08955 | 2.44 | 0.015* | not applied (n < 1000) | 0.072 | -4.1 | +8.8 | 0.6468 | 0.6412 |
| Time < 70, pooled (%) | 638 | OR 1.207 [1.019, 1.431] | 0.06703 | 2.17 | 0.030* | not applied (n < 1000) | 0.107 | -2.8 | +10.1 | 0.6470 | 0.6412 |
| Avg. daily time < 70 (%) | 638 | OR 1.213 [1.024, 1.437] | 0.06757 | 2.23 | 0.026* | not applied (n < 1000) | 0.097 | -3.1 | +9.8 | 0.6465 | 0.6412 |
| Time 54-250, pooled (%) | 638 | OR 0.765 [0.607, 0.965] | -0.0467 | -2.26 | 0.024* | not applied (n < 1000) | 0.093 | -5.3 | +7.5 | 0.6480 | 0.6412 |
| Avg. daily time 54-250 (%) | 638 | OR 0.775 [0.619, 0.970] | -0.04892 | -2.23 | 0.026* | not applied (n < 1000) | 0.097 | -4.7 | +8.2 | 0.6461 | 0.6412 |
| Time 181-250, pooled (%) | 638 | OR 1.219 [1.027, 1.448] | 0.02189 | 2.26 | 0.024* | not applied (n < 1000) | 0.093 | -3.1 | +9.7 | 0.6481 | 0.6412 |
| Avg. daily time 181-250 (%) | 638 | OR 1.221 [1.029, 1.448] | 0.02143 | 2.29 | 0.022* | not applied (n < 1000) | 0.092 | -3.2 | +9.6 | 0.6481 | 0.6412 |
| Time > 180, pooled (%) | 638 | OR 1.269 [1.064, 1.514] | 0.0184 | 2.65 | 0.008** | not applied (n < 1000) | 0.050 | -5.3 | +7.5 | 0.6499 | 0.6412 |
| Avg. daily time > 180 (%) | 638 | OR 1.258 [1.056, 1.500] | 0.01773 | 2.56 | 0.010* | not applied (n < 1000) | 0.061 | -4.8 | +8.0 | 0.6490 | 0.6412 |
| Nocturnal time > 180 (%) | 638 | OR 1.222 [1.027, 1.453] | 0.01636 | 2.26 | 0.024* | not applied (n < 1000) | 0.093 | -3.4 | +9.5 | 0.6486 | 0.6412 |
| Any reading > 250 during wear (0/1) | 638 | OR 1.105 [0.929, 1.313] | 0.2195 | 1.13 | 0.259 | not applied (n < 1000) | 0.492 | +0.7 | +13.6 | 0.6387 | 0.6412 |
| Time > 250, pooled (%) | 638 | OR 1.295 [1.028, 1.631] | 0.04576 | 2.19 | 0.028* | not applied (n < 1000) | 0.102 | -4.9 | +8.0 | 0.6467 | 0.6412 |
| Avg. daily time > 250 (%) | 638 | OR 1.282 [1.023, 1.607] | 0.04863 | 2.16 | 0.031* | not applied (n < 1000) | 0.109 | -4.3 | +8.5 | 0.6454 | 0.6412 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 638; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 638 | -0.288 [-0.492, -0.085] | -0.3421 | -2.78 | 0.005** | not applied (n < 1000) | 0.038 (q<0.05) | -5.5 | +0.0 | 0.0528 | 0.0430 |
| Mean glucose (mg/dL) | 638 | -0.218 [-0.450, +0.014] | -0.008991 | -1.84 | 0.066 | not applied (n < 1000) | 0.173 | -2.4 | +3.1 | 0.0475 | 0.0430 |
| GMI (%) | 638 | -0.218 [-0.450, +0.014] | -0.3759 | -1.84 | 0.066 | not applied (n < 1000) | 0.173 | -2.4 | +3.1 | 0.0475 | 0.0430 |
| Nocturnal mean 00-06h (mg/dL) | 638 | -0.228 [-0.463, +0.007] | -0.009413 | -1.90 | 0.058 | not applied (n < 1000) | 0.162 | -2.8 | +2.6 | 0.0468 | 0.0430 |
| Glucose SD, pooled (mg/dL) | 638 | -0.273 [-0.504, -0.043] | -0.02261 | -2.32 | 0.020* | not applied (n < 1000) | 0.087 | -4.5 | +0.9 | 0.0491 | 0.0430 |
| Avg. daily SD (mg/dL) | 638 | -0.251 [-0.471, -0.031] | -0.02406 | -2.24 | 0.025* | not applied (n < 1000) | 0.097 | -3.5 | +2.0 | 0.0476 | 0.0430 |
| CV (%) | 638 | -0.206 [-0.416, +0.005] | -0.03368 | -1.91 | 0.056 | not applied (n < 1000) | 0.159 | -1.7 | +3.8 | 0.0434 | 0.0430 |
| Mean / SD ratio | 638 | +0.166 [-0.036, +0.367] | 0.1275 | 1.61 | 0.107 | not applied (n < 1000) | 0.252 | -0.5 | +5.0 | 0.0414 | 0.0430 |
| Avg. daily mean / SD | 638 | +0.140 [-0.066, +0.347] | 0.08847 | 1.33 | 0.182 | not applied (n < 1000) | 0.371 | +0.2 | +5.7 | 0.0397 | 0.0430 |
| MAG (mg/dL/h) | 638 | -0.188 [-0.399, +0.024] | -0.01975 | -1.73 | 0.083 | not applied (n < 1000) | 0.206 | -1.4 | +4.1 | 0.0459 | 0.0430 |
| Avg. daily range (mg/dL) | 638 | -0.213 [-0.434, +0.008] | -0.005443 | -1.88 | 0.059 | not applied (n < 1000) | 0.164 | -2.0 | +3.5 | 0.0449 | 0.0430 |
| SD of daily means (mg/dL) | 638 | -0.223 [-0.484, +0.039] | -0.03196 | -1.67 | 0.095 | not applied (n < 1000) | 0.231 | -2.7 | +2.8 | 0.0452 | 0.0430 |
| Time in range 70-180, pooled (%) | 638 | +0.244 [+0.010, +0.478] | 0.01879 | 2.04 | 0.041* | not applied (n < 1000) | 0.128 | -3.5 | +2.0 | 0.0487 | 0.0430 |
| Avg. daily time in range 70-180 (%) | 638 | +0.241 [+0.007, +0.475] | 0.01843 | 2.02 | 0.043* | not applied (n < 1000) | 0.131 | -3.3 | +2.2 | 0.0486 | 0.0430 |
| Time < 54, pooled (%) | 638 | +0.064 [-0.099, +0.227] | 0.07316 | 0.77 | 0.444 | not applied (n < 1000) | 0.679 | +1.6 | +7.1 | 0.0425 | 0.0430 |
| Avg. daily time < 54 (%) | 638 | -0.028 [-0.189, +0.133] | -0.03753 | -0.34 | 0.731 | not applied (n < 1000) | 0.848 | +1.9 | +7.4 | 0.0414 | 0.0430 |
| Time 54-69, pooled (%) | 638 | -0.062 [-0.257, +0.133] | -0.02723 | -0.62 | 0.535 | not applied (n < 1000) | 0.736 | +1.6 | +7.1 | 0.0426 | 0.0430 |
| Avg. daily time 54-69 (%) | 638 | -0.111 [-0.315, +0.092] | -0.04732 | -1.08 | 0.282 | not applied (n < 1000) | 0.507 | +0.8 | +6.3 | 0.0435 | 0.0430 |
| Time < 70, pooled (%) | 638 | -0.031 [-0.211, +0.149] | -0.01091 | -0.33 | 0.739 | not applied (n < 1000) | 0.852 | +1.9 | +7.4 | 0.0421 | 0.0430 |
| Avg. daily time < 70 (%) | 638 | -0.100 [-0.292, +0.093] | -0.03488 | -1.02 | 0.309 | not applied (n < 1000) | 0.543 | +1.0 | +6.5 | 0.0431 | 0.0430 |
| Time 54-250, pooled (%) | 638 | +0.255 [-0.013, +0.522] | 0.04443 | 1.87 | 0.062 | not applied (n < 1000) | 0.166 | -4.2 | +1.2 | 0.0460 | 0.0430 |
| Avg. daily time 54-250 (%) | 638 | +0.255 [-0.022, +0.532] | 0.04896 | 1.81 | 0.071 | not applied (n < 1000) | 0.183 | -4.2 | +1.2 | 0.0457 | 0.0430 |
| Time 181-250, pooled (%) | 638 | -0.165 [-0.379, +0.048] | -0.01826 | -1.52 | 0.129 | not applied (n < 1000) | 0.289 | -0.5 | +5.0 | 0.0454 | 0.0430 |
| Avg. daily time 181-250 (%) | 638 | -0.159 [-0.373, +0.055] | -0.01709 | -1.46 | 0.145 | not applied (n < 1000) | 0.316 | -0.3 | +5.2 | 0.0449 | 0.0430 |
| Time > 180, pooled (%) | 638 | -0.236 [-0.473, -0.000] | -0.01824 | -1.96 | 0.050* | not applied (n < 1000) | 0.145 | -3.2 | +2.3 | 0.0486 | 0.0430 |
| Avg. daily time > 180 (%) | 638 | -0.218 [-0.455, +0.019] | -0.01686 | -1.81 | 0.071 | not applied (n < 1000) | 0.183 | -2.4 | +3.1 | 0.0476 | 0.0430 |
| Nocturnal time > 180 (%) | 638 | -0.241 [-0.488, +0.006] | -0.01971 | -1.91 | 0.056 | not applied (n < 1000) | 0.159 | -3.5 | +2.0 | 0.0469 | 0.0430 |
| Any reading > 250 during wear (0/1) | 638 | -0.161 [-0.387, +0.066] | -0.3536 | -1.39 | 0.165 | not applied (n < 1000) | 0.351 | -0.4 | +5.1 | 0.0431 | 0.0430 |
| Time > 250, pooled (%) | 638 | -0.268 [-0.542, +0.006] | -0.04751 | -1.92 | 0.055 | not applied (n < 1000) | 0.158 | -4.9 | +0.5 | 0.0467 | 0.0430 |
| Avg. daily time > 250 (%) | 638 | -0.256 [-0.539, +0.028] | -0.05 | -1.76 | 0.078 | not applied (n < 1000) | 0.196 | -4.3 | +1.2 | 0.0453 | 0.0430 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 637; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 637 | +0.355 [-0.072, +0.782] | 0.4211 | 1.63 | 0.103 | not applied (n < 1000) | 0.245 | -1.2 | +0.0 | 0.0858 | 0.0834 |
| Mean glucose (mg/dL) | 637 | +0.375 [-0.029, +0.778] | 0.01544 | 1.82 | 0.069 | not applied (n < 1000) | 0.179 | -1.7 | -0.5 | 0.0840 | 0.0834 |
| GMI (%) | 637 | +0.375 [-0.029, +0.778] | 0.6455 | 1.82 | 0.069 | not applied (n < 1000) | 0.179 | -1.7 | -0.5 | 0.0840 | 0.0834 |
| Nocturnal mean 00-06h (mg/dL) | 637 | +0.502 [+0.113, +0.892] | 0.02076 | 2.53 | 0.011* | not applied (n < 1000) | 0.064 | -4.7 | -3.5 | 0.0890 | 0.0834 |
| Glucose SD, pooled (mg/dL) | 637 | +0.547 [+0.157, +0.938] | 0.04529 | 2.75 | 0.006** | not applied (n < 1000) | 0.041 (q<0.05) | -5.5 | -4.3 | 0.0916 | 0.0834 |
| Avg. daily SD (mg/dL) | 637 | +0.493 [+0.108, +0.879] | 0.04734 | 2.51 | 0.012* | not applied (n < 1000) | 0.064 | -4.0 | -2.8 | 0.0899 | 0.0834 |
| CV (%) | 637 | +0.432 [+0.047, +0.816] | 0.07077 | 2.20 | 0.028* | not applied (n < 1000) | 0.102 | -2.6 | -1.4 | 0.0887 | 0.0834 |
| Mean / SD ratio | 637 | -0.453 [-0.830, -0.075] | -0.3484 | -2.35 | 0.019* | not applied (n < 1000) | 0.084 | -3.2 | -2.0 | 0.0893 | 0.0834 |
| Avg. daily mean / SD | 637 | -0.311 [-0.691, +0.070] | -0.196 | -1.60 | 0.110 | not applied (n < 1000) | 0.256 | -0.5 | +0.8 | 0.0854 | 0.0834 |
| MAG (mg/dL/h) | 637 | +0.222 [-0.181, +0.626] | 0.02341 | 1.08 | 0.280 | not applied (n < 1000) | 0.507 | +0.7 | +1.9 | 0.0829 | 0.0834 |
| Avg. daily range (mg/dL) | 637 | +0.432 [+0.038, +0.827] | 0.01105 | 2.15 | 0.032* | not applied (n < 1000) | 0.109 | -2.7 | -1.5 | 0.0877 | 0.0834 |
| SD of daily means (mg/dL) | 637 | +0.596 [+0.205, +0.986] | 0.08549 | 2.99 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -7.5 | -6.3 | 0.0934 | 0.0834 |
| Time in range 70-180, pooled (%) | 637 | -0.549 [-0.917, -0.181] | -0.04226 | -2.93 | 0.003** | not applied (n < 1000) | 0.031 (q<0.05) | -5.9 | -4.7 | 0.0910 | 0.0834 |
| Avg. daily time in range 70-180 (%) | 637 | -0.570 [-0.942, -0.198] | -0.04359 | -3.01 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -6.5 | -5.3 | 0.0918 | 0.0834 |
| Time < 54, pooled (%) | 637 | -0.120 [-0.453, +0.213] | -0.1378 | -0.71 | 0.479 | not applied (n < 1000) | 0.707 | +1.6 | +2.8 | 0.0835 | 0.0834 |
| Avg. daily time < 54 (%) | 637 | -0.034 [-0.402, +0.335] | -0.04462 | -0.18 | 0.858 | not applied (n < 1000) | 0.921 | +2.0 | +3.2 | 0.0816 | 0.0834 |
| Time 54-69, pooled (%) | 637 | +0.134 [-0.231, +0.499] | 0.05904 | 0.72 | 0.472 | not applied (n < 1000) | 0.705 | +1.5 | +2.7 | 0.0821 | 0.0834 |
| Avg. daily time 54-69 (%) | 637 | +0.185 [-0.187, +0.556] | 0.07827 | 0.97 | 0.330 | not applied (n < 1000) | 0.559 | +1.1 | +2.3 | 0.0832 | 0.0834 |
| Time < 70, pooled (%) | 637 | +0.072 [-0.288, +0.432] | 0.02563 | 0.39 | 0.695 | not applied (n < 1000) | 0.829 | +1.9 | +3.1 | 0.0818 | 0.0834 |
| Avg. daily time < 70 (%) | 637 | +0.144 [-0.226, +0.514] | 0.05041 | 0.76 | 0.444 | not applied (n < 1000) | 0.679 | +1.4 | +2.6 | 0.0828 | 0.0834 |
| Time 54-250, pooled (%) | 637 | -0.611 [-0.879, -0.342] | -0.1065 | -4.46 | 8.3e-06*** | not applied (n < 1000) | 0.001 (q<0.05) | -8.3 | -7.1 | 0.0966 | 0.0834 |
| Avg. daily time 54-250 (%) | 637 | -0.614 [-0.929, -0.299] | -0.1177 | -3.82 | 1.3e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -8.3 | -7.1 | 0.0964 | 0.0834 |
| Time 181-250, pooled (%) | 637 | +0.349 [-0.051, +0.748] | 0.03848 | 1.71 | 0.087 | not applied (n < 1000) | 0.213 | -1.2 | +0.1 | 0.0832 | 0.0834 |
| Avg. daily time 181-250 (%) | 637 | +0.392 [-0.014, +0.799] | 0.04216 | 1.89 | 0.058 | not applied (n < 1000) | 0.162 | -2.0 | -0.8 | 0.0842 | 0.0834 |
| Time > 180, pooled (%) | 637 | +0.532 [+0.157, +0.907] | 0.04099 | 2.78 | 0.005** | not applied (n < 1000) | 0.038 (q<0.05) | -5.4 | -4.2 | 0.0900 | 0.0834 |
| Avg. daily time > 180 (%) | 637 | +0.539 [+0.159, +0.918] | 0.04155 | 2.78 | 0.005** | not applied (n < 1000) | 0.038 (q<0.05) | -5.6 | -4.4 | 0.0901 | 0.0834 |
| Nocturnal time > 180 (%) | 637 | +0.744 [+0.388, +1.100] | 0.06076 | 4.09 | 4.2e-05*** | not applied (n < 1000) | 0.003 (q<0.05) | -13.1 | -11.9 | 0.1020 | 0.0834 |
| Any reading > 250 during wear (0/1) | 637 | +0.365 [-0.018, +0.748] | 0.8037 | 1.87 | 0.062 | not applied (n < 1000) | 0.166 | -1.5 | -0.3 | 0.0812 | 0.0834 |
| Time > 250, pooled (%) | 637 | +0.638 [+0.361, +0.916] | 0.113 | 4.51 | 6.5e-06*** | not applied (n < 1000) | 0.001 (q<0.05) | -9.2 | -8.0 | 0.0979 | 0.0834 |
| Avg. daily time > 250 (%) | 637 | +0.630 [+0.297, +0.962] | 0.1231 | 3.71 | 2.1e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -8.9 | -7.6 | 0.0972 | 0.0834 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 637; events = 137; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 637 | OR 1.312 [1.089, 1.582] | 0.3224 | 2.85 | 0.004** | not applied (n < 1000) | 0.035 (q<0.05) | -6.1 | +0.0 | 0.6650 | 0.6587 |
| Mean glucose (mg/dL) | 637 | OR 1.331 [1.106, 1.602] | 0.01179 | 3.03 | 0.002** | not applied (n < 1000) | 0.028 (q<0.05) | -7.2 | -1.1 | 0.6620 | 0.6587 |
| GMI (%) | 637 | OR 1.331 [1.106, 1.602] | 0.4929 | 3.03 | 0.002** | not applied (n < 1000) | 0.028 (q<0.05) | -7.2 | -1.1 | 0.6620 | 0.6587 |
| Nocturnal mean 00-06h (mg/dL) | 637 | OR 1.437 [1.189, 1.736] | 0.01497 | 3.75 | 1.7e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -12.7 | -6.6 | 0.6746 | 0.6587 |
| Glucose SD, pooled (mg/dL) | 637 | OR 1.393 [1.146, 1.693] | 0.02744 | 3.33 | 8.7e-04*** | not applied (n < 1000) | 0.017 (q<0.05) | -9.3 | -3.1 | 0.6698 | 0.6587 |
| Avg. daily SD (mg/dL) | 637 | OR 1.337 [1.099, 1.627] | 0.02789 | 2.90 | 0.004** | not applied (n < 1000) | 0.032 (q<0.05) | -6.6 | -0.4 | 0.6675 | 0.6587 |
| CV (%) | 637 | OR 1.263 [1.032, 1.546] | 0.03827 | 2.26 | 0.024* | not applied (n < 1000) | 0.093 | -3.0 | +3.1 | 0.6669 | 0.6587 |
| Mean / SD ratio | 637 | OR 0.784 [0.634, 0.970] | -0.1873 | -2.24 | 0.025* | not applied (n < 1000) | 0.096 | -3.2 | +3.0 | 0.6659 | 0.6587 |
| Avg. daily mean / SD | 637 | OR 0.857 [0.694, 1.059] | -0.09706 | -1.43 | 0.153 | not applied (n < 1000) | 0.331 | -0.1 | +6.1 | 0.6568 | 0.6587 |
| MAG (mg/dL/h) | 637 | OR 1.079 [0.889, 1.309] | 0.007973 | 0.77 | 0.444 | not applied (n < 1000) | 0.679 | +1.4 | +7.6 | 0.6486 | 0.6587 |
| Avg. daily range (mg/dL) | 637 | OR 1.272 [1.046, 1.546] | 0.006149 | 2.42 | 0.016* | not applied (n < 1000) | 0.076 | -3.8 | +2.3 | 0.6607 | 0.6587 |
| SD of daily means (mg/dL) | 637 | OR 1.430 [1.181, 1.730] | 0.05128 | 3.67 | 2.4e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -12.2 | -6.1 | 0.6752 | 0.6587 |
| Time in range 70-180, pooled (%) | 637 | OR 0.712 [0.593, 0.854] | -0.02618 | -3.65 | 2.6e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -11.6 | -5.5 | 0.6725 | 0.6587 |
| Avg. daily time in range 70-180 (%) | 637 | OR 0.711 [0.593, 0.853] | -0.02605 | -3.67 | 2.5e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -11.7 | -5.6 | 0.6727 | 0.6587 |
| Time < 54, pooled (%) | 637 | OR 0.886 [0.668, 1.175] | -0.1386 | -0.84 | 0.402 | not applied (n < 1000) | 0.638 | +1.2 | +7.3 | 0.6559 | 0.6587 |
| Avg. daily time < 54 (%) | 637 | OR 0.929 [0.727, 1.187] | -0.09803 | -0.59 | 0.556 | not applied (n < 1000) | 0.753 | +1.6 | +7.8 | 0.6540 | 0.6587 |
| Time 54-69, pooled (%) | 637 | OR 1.018 [0.838, 1.235] | 0.007716 | 0.18 | 0.859 | not applied (n < 1000) | 0.921 | +2.0 | +8.1 | 0.6556 | 0.6587 |
| Avg. daily time 54-69 (%) | 637 | OR 1.025 [0.845, 1.243] | 0.01027 | 0.25 | 0.806 | not applied (n < 1000) | 0.899 | +1.9 | +8.1 | 0.6555 | 0.6587 |
| Time < 70, pooled (%) | 637 | OR 0.991 [0.810, 1.212] | -0.003138 | -0.09 | 0.932 | not applied (n < 1000) | 0.977 | +2.0 | +8.1 | 0.6556 | 0.6587 |
| Avg. daily time < 70 (%) | 637 | OR 1.006 [0.826, 1.225] | 0.002034 | 0.06 | 0.954 | not applied (n < 1000) | 0.977 | +2.0 | +8.1 | 0.6556 | 0.6587 |
| Time 54-250, pooled (%) | 637 | OR 0.672 [0.518, 0.871] | -0.06937 | -3.01 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -13.1 | -6.9 | 0.6689 | 0.6587 |
| Avg. daily time 54-250 (%) | 637 | OR 0.673 [0.525, 0.863] | -0.0758 | -3.12 | 0.002** | not applied (n < 1000) | 0.026 (q<0.05) | -13.3 | -7.2 | 0.6677 | 0.6587 |
| Time 181-250, pooled (%) | 637 | OR 1.295 [1.080, 1.554] | 0.02857 | 2.79 | 0.005** | not applied (n < 1000) | 0.038 (q<0.05) | -5.6 | +0.5 | 0.6670 | 0.6587 |
| Avg. daily time 181-250 (%) | 637 | OR 1.312 [1.095, 1.572] | 0.02917 | 2.94 | 0.003** | not applied (n < 1000) | 0.030 (q<0.05) | -6.5 | -0.3 | 0.6679 | 0.6587 |
| Time > 180, pooled (%) | 637 | OR 1.401 [1.169, 1.680] | 0.02601 | 3.65 | 2.7e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -11.6 | -5.5 | 0.6699 | 0.6587 |
| Avg. daily time > 180 (%) | 637 | OR 1.402 [1.170, 1.680] | 0.02606 | 3.66 | 2.5e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -11.7 | -5.5 | 0.6703 | 0.6587 |
| Nocturnal time > 180 (%) | 637 | OR 1.539 [1.271, 1.864] | 0.03522 | 4.41 | 1.0e-05*** | not applied (n < 1000) | 0.001 (q<0.05) | -20.5 | -14.4 | 0.6855 | 0.6587 |
| Any reading > 250 during wear (0/1) | 637 | OR 1.336 [1.097, 1.627] | 0.6383 | 2.88 | 0.004** | not applied (n < 1000) | 0.033 (q<0.05) | -6.2 | -0.0 | 0.6660 | 0.6587 |
| Time > 250, pooled (%) | 637 | OR 1.535 [1.164, 2.024] | 0.07591 | 3.04 | 0.002** | not applied (n < 1000) | 0.028 (q<0.05) | -14.4 | -8.3 | 0.6697 | 0.6587 |
| Avg. daily time > 250 (%) | 637 | OR 1.534 [1.178, 1.997] | 0.08363 | 3.18 | 0.001** | not applied (n < 1000) | 0.023 (q<0.05) | -14.7 | -8.5 | 0.6702 | 0.6587 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 628; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 628 | +0.108 [+0.014, +0.201] | 0.1271 | 2.26 | 0.024* | not applied (n < 1000) | 0.093 | -5.0 | +0.0 | 0.1204 | 0.1141 |
| Mean glucose (mg/dL) | 628 | -0.016 [-0.095, +0.062] | -0.0006767 | -0.41 | 0.682 | not applied (n < 1000) | 0.828 | +1.8 | +6.8 | 0.1093 | 0.1141 |
| GMI (%) | 628 | -0.016 [-0.095, +0.062] | -0.02829 | -0.41 | 0.682 | not applied (n < 1000) | 0.828 | +1.8 | +6.8 | 0.1093 | 0.1141 |
| Nocturnal mean 00-06h (mg/dL) | 628 | -0.010 [-0.094, +0.074] | -0.000417 | -0.24 | 0.814 | not applied (n < 1000) | 0.902 | +1.9 | +6.9 | 0.1081 | 0.1141 |
| Glucose SD, pooled (mg/dL) | 628 | +0.026 [-0.058, +0.109] | 0.002102 | 0.60 | 0.548 | not applied (n < 1000) | 0.747 | +1.6 | +6.6 | 0.1093 | 0.1141 |
| Avg. daily SD (mg/dL) | 628 | +0.017 [-0.065, +0.099] | 0.001636 | 0.41 | 0.682 | not applied (n < 1000) | 0.828 | +1.8 | +6.8 | 0.1097 | 0.1141 |
| CV (%) | 628 | +0.044 [-0.046, +0.133] | 0.007144 | 0.96 | 0.337 | not applied (n < 1000) | 0.566 | +0.9 | +5.9 | 0.1096 | 0.1141 |
| Mean / SD ratio | 628 | -0.044 [-0.125, +0.036] | -0.0341 | -1.08 | 0.279 | not applied (n < 1000) | 0.507 | +0.8 | +5.8 | 0.1096 | 0.1141 |
| Avg. daily mean / SD | 628 | -0.053 [-0.132, +0.026] | -0.03322 | -1.32 | 0.187 | not applied (n < 1000) | 0.377 | +0.3 | +5.3 | 0.1112 | 0.1141 |
| MAG (mg/dL/h) | 628 | +0.007 [-0.065, +0.080] | 0.0007799 | 0.20 | 0.840 | not applied (n < 1000) | 0.919 | +2.0 | +7.0 | 0.1129 | 0.1141 |
| Avg. daily range (mg/dL) | 628 | +0.009 [-0.073, +0.092] | 0.0002303 | 0.21 | 0.830 | not applied (n < 1000) | 0.910 | +2.0 | +7.0 | 0.1100 | 0.1141 |
| SD of daily means (mg/dL) | 628 | +0.046 [-0.036, +0.127] | 0.006505 | 1.10 | 0.272 | not applied (n < 1000) | 0.507 | +0.7 | +5.7 | 0.1103 | 0.1141 |
| Time in range 70-180, pooled (%) | 628 | -0.048 [-0.128, +0.032] | -0.003681 | -1.18 | 0.239 | not applied (n < 1000) | 0.459 | +0.6 | +5.6 | 0.1098 | 0.1141 |
| Avg. daily time in range 70-180 (%) | 628 | -0.051 [-0.131, +0.030] | -0.003844 | -1.23 | 0.219 | not applied (n < 1000) | 0.425 | +0.4 | +5.4 | 0.1101 | 0.1141 |
| Time < 54, pooled (%) | 628 | +0.038 [-0.073, +0.148] | 0.04285 | 0.67 | 0.506 | not applied (n < 1000) | 0.720 | +1.1 | +6.1 | 0.1129 | 0.1141 |
| Avg. daily time < 54 (%) | 628 | +0.065 [-0.054, +0.184] | 0.08637 | 1.07 | 0.283 | not applied (n < 1000) | 0.507 | -0.8 | +4.2 | 0.1151 | 0.1141 |
| Time 54-69, pooled (%) | 628 | +0.084 [-0.017, +0.186] | 0.03694 | 1.63 | 0.103 | not applied (n < 1000) | 0.245 | -2.7 | +2.3 | 0.1143 | 0.1141 |
| Avg. daily time 54-69 (%) | 628 | +0.091 [-0.013, +0.196] | 0.03864 | 1.72 | 0.086 | not applied (n < 1000) | 0.211 | -3.5 | +1.5 | 0.1168 | 0.1141 |
| Time < 70, pooled (%) | 628 | +0.080 [-0.022, +0.182] | 0.02838 | 1.54 | 0.123 | not applied (n < 1000) | 0.277 | -2.2 | +2.8 | 0.1149 | 0.1141 |
| Avg. daily time < 70 (%) | 628 | +0.093 [-0.013, +0.199] | 0.03233 | 1.72 | 0.086 | not applied (n < 1000) | 0.211 | -3.7 | +1.3 | 0.1180 | 0.1141 |
| Time 54-250, pooled (%) | 628 | -0.017 [-0.076, +0.042] | -0.002976 | -0.57 | 0.566 | not applied (n < 1000) | 0.760 | +1.8 | +6.8 | 0.1128 | 0.1141 |
| Avg. daily time 54-250 (%) | 628 | -0.027 [-0.091, +0.037] | -0.005179 | -0.83 | 0.406 | not applied (n < 1000) | 0.638 | +1.5 | +6.5 | 0.1134 | 0.1141 |
| Time 181-250, pooled (%) | 628 | +0.035 [-0.056, +0.126] | 0.003857 | 0.76 | 0.448 | not applied (n < 1000) | 0.682 | +1.2 | +6.2 | 0.1076 | 0.1141 |
| Avg. daily time 181-250 (%) | 628 | +0.030 [-0.059, +0.120] | 0.003242 | 0.67 | 0.505 | not applied (n < 1000) | 0.720 | +1.4 | +6.4 | 0.1073 | 0.1141 |
| Time > 180, pooled (%) | 628 | +0.030 [-0.050, +0.109] | 0.002271 | 0.73 | 0.464 | not applied (n < 1000) | 0.696 | +1.5 | +6.5 | 0.1095 | 0.1141 |
| Avg. daily time > 180 (%) | 628 | +0.029 [-0.050, +0.109] | 0.002231 | 0.72 | 0.473 | not applied (n < 1000) | 0.705 | +1.5 | +6.5 | 0.1093 | 0.1141 |
| Nocturnal time > 180 (%) | 628 | +0.047 [-0.040, +0.134] | 0.003818 | 1.06 | 0.290 | not applied (n < 1000) | 0.518 | +0.6 | +5.6 | 0.1101 | 0.1141 |
| Any reading > 250 during wear (0/1) | 628 | -0.012 [-0.094, +0.070] | -0.0258 | -0.28 | 0.779 | not applied (n < 1000) | 0.885 | +1.9 | +6.9 | 0.1101 | 0.1141 |
| Time > 250, pooled (%) | 628 | +0.012 [-0.043, +0.066] | 0.002042 | 0.42 | 0.677 | not applied (n < 1000) | 0.828 | +1.9 | +6.9 | 0.1130 | 0.1141 |
| Avg. daily time > 250 (%) | 628 | +0.018 [-0.041, +0.077] | 0.003506 | 0.60 | 0.546 | not applied (n < 1000) | 0.747 | +1.8 | +6.8 | 0.1132 | 0.1141 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 628; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 628 | -0.024 [-0.192, +0.143] | -0.02875 | -0.28 | 0.776 | not applied (n < 1000) | 0.883 | +1.9 | +0.0 | 0.2304 | 0.2332 |
| Mean glucose (mg/dL) | 628 | -0.063 [-0.248, +0.122] | -0.002591 | -0.67 | 0.504 | not applied (n < 1000) | 0.720 | +1.4 | -0.5 | 0.2284 | 0.2332 |
| GMI (%) | 628 | -0.063 [-0.248, +0.122] | -0.1083 | -0.67 | 0.504 | not applied (n < 1000) | 0.720 | +1.4 | -0.5 | 0.2284 | 0.2332 |
| Nocturnal mean 00-06h (mg/dL) | 628 | -0.085 [-0.292, +0.122] | -0.003486 | -0.80 | 0.422 | not applied (n < 1000) | 0.659 | +1.0 | -0.9 | 0.2304 | 0.2332 |
| Glucose SD, pooled (mg/dL) | 628 | -0.039 [-0.223, +0.146] | -0.003181 | -0.41 | 0.681 | not applied (n < 1000) | 0.828 | +1.8 | -0.1 | 0.2263 | 0.2332 |
| Avg. daily SD (mg/dL) | 628 | -0.071 [-0.243, +0.100] | -0.006822 | -0.82 | 0.413 | not applied (n < 1000) | 0.647 | +1.3 | -0.6 | 0.2268 | 0.2332 |
| CV (%) | 628 | +0.025 [-0.155, +0.205] | 0.004075 | 0.27 | 0.786 | not applied (n < 1000) | 0.888 | +1.9 | -0.0 | 0.2274 | 0.2332 |
| Mean / SD ratio | 628 | -0.003 [-0.180, +0.175] | -0.002151 | -0.03 | 0.975 | not applied (n < 1000) | 0.989 | +2.0 | +0.1 | 0.2262 | 0.2332 |
| Avg. daily mean / SD | 628 | +0.049 [-0.136, +0.234] | 0.03061 | 0.52 | 0.605 | not applied (n < 1000) | 0.780 | +1.7 | -0.2 | 0.2240 | 0.2332 |
| MAG (mg/dL/h) | 628 | -0.008 [-0.170, +0.154] | -0.0008518 | -0.10 | 0.922 | not applied (n < 1000) | 0.973 | +2.0 | +0.1 | 0.2303 | 0.2332 |
| Avg. daily range (mg/dL) | 628 | -0.072 [-0.243, +0.098] | -0.001844 | -0.83 | 0.406 | not applied (n < 1000) | 0.638 | +1.3 | -0.6 | 0.2270 | 0.2332 |
| SD of daily means (mg/dL) | 628 | -0.004 [-0.243, +0.234] | -0.0006222 | -0.04 | 0.971 | not applied (n < 1000) | 0.988 | +2.0 | +0.1 | 0.2281 | 0.2332 |
| Time in range 70-180, pooled (%) | 628 | +0.017 [-0.167, +0.202] | 0.001338 | 0.19 | 0.852 | not applied (n < 1000) | 0.920 | +2.0 | +0.0 | 0.2264 | 0.2332 |
| Avg. daily time in range 70-180 (%) | 628 | +0.014 [-0.169, +0.198] | 0.001095 | 0.15 | 0.878 | not applied (n < 1000) | 0.933 | +2.0 | +0.1 | 0.2263 | 0.2332 |
| Time < 54, pooled (%) | 628 | +0.175 [+0.024, +0.326] | 0.1996 | 2.27 | 0.023* | not applied (n < 1000) | 0.093 | -2.5 | -4.4 | 0.2381 | 0.2332 |
| Avg. daily time < 54 (%) | 628 | +0.151 [-0.041, +0.342] | 0.1994 | 1.54 | 0.124 | not applied (n < 1000) | 0.278 | -1.3 | -3.2 | 0.2360 | 0.2332 |
| Time 54-69, pooled (%) | 628 | +0.151 [+0.008, +0.294] | 0.06605 | 2.06 | 0.039* | not applied (n < 1000) | 0.125 | -1.4 | -3.3 | 0.2362 | 0.2332 |
| Avg. daily time 54-69 (%) | 628 | +0.172 [+0.027, +0.317] | 0.07256 | 2.32 | 0.020* | not applied (n < 1000) | 0.087 | -2.4 | -4.3 | 0.2383 | 0.2332 |
| Time < 70, pooled (%) | 628 | +0.176 [+0.028, +0.325] | 0.06249 | 2.33 | 0.020* | not applied (n < 1000) | 0.087 | -2.6 | -4.6 | 0.2378 | 0.2332 |
| Avg. daily time < 70 (%) | 628 | +0.182 [+0.028, +0.335] | 0.06325 | 2.32 | 0.020* | not applied (n < 1000) | 0.087 | -2.9 | -4.8 | 0.2387 | 0.2332 |
| Time 54-250, pooled (%) | 628 | -0.002 [-0.223, +0.219] | -0.0003152 | -0.02 | 0.987 | not applied (n < 1000) | 0.992 | +2.0 | +0.1 | 0.2261 | 0.2332 |
| Avg. daily time 54-250 (%) | 628 | +0.002 [-0.230, +0.234] | 0.0003766 | 0.02 | 0.987 | not applied (n < 1000) | 0.992 | +2.0 | +0.1 | 0.2262 | 0.2332 |
| Time 181-250, pooled (%) | 628 | -0.067 [-0.232, +0.098] | -0.007358 | -0.80 | 0.426 | not applied (n < 1000) | 0.663 | +1.4 | -0.5 | 0.2268 | 0.2332 |
| Avg. daily time 181-250 (%) | 628 | -0.065 [-0.230, +0.099] | -0.006995 | -0.78 | 0.435 | not applied (n < 1000) | 0.675 | +1.4 | -0.5 | 0.2267 | 0.2332 |
| Time > 180, pooled (%) | 628 | -0.058 [-0.243, +0.128] | -0.004443 | -0.61 | 0.540 | not applied (n < 1000) | 0.742 | +1.5 | -0.4 | 0.2268 | 0.2332 |
| Avg. daily time > 180 (%) | 628 | -0.057 [-0.243, +0.129] | -0.004356 | -0.60 | 0.550 | not applied (n < 1000) | 0.747 | +1.5 | -0.4 | 0.2267 | 0.2332 |
| Nocturnal time > 180 (%) | 628 | -0.055 [-0.269, +0.159] | -0.004475 | -0.50 | 0.614 | not applied (n < 1000) | 0.788 | +1.6 | -0.4 | 0.2274 | 0.2332 |
| Any reading > 250 during wear (0/1) | 628 | -0.029 [-0.197, +0.138] | -0.06484 | -0.34 | 0.731 | not applied (n < 1000) | 0.848 | +1.9 | -0.0 | 0.2301 | 0.2332 |
| Time > 250, pooled (%) | 628 | -0.025 [-0.253, +0.202] | -0.004458 | -0.22 | 0.827 | not applied (n < 1000) | 0.910 | +1.9 | -0.0 | 0.2262 | 0.2332 |
| Avg. daily time > 250 (%) | 628 | -0.024 [-0.268, +0.219] | -0.004727 | -0.20 | 0.845 | not applied (n < 1000) | 0.919 | +1.9 | -0.0 | 0.2263 | 0.2332 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 628; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 628 | +0.331 [-0.203, +0.865] | 0.391 | 1.21 | 0.224 | not applied (n < 1000) | 0.432 | +0.4 | +0.0 | 0.1902 | 0.1896 |
| Mean glucose (mg/dL) | 628 | +0.163 [-0.334, +0.660] | 0.006697 | 0.64 | 0.520 | not applied (n < 1000) | 0.724 | +1.6 | +1.2 | 0.1863 | 0.1896 |
| GMI (%) | 628 | +0.163 [-0.334, +0.660] | 0.28 | 0.64 | 0.520 | not applied (n < 1000) | 0.724 | +1.6 | +1.2 | 0.1863 | 0.1896 |
| Nocturnal mean 00-06h (mg/dL) | 628 | +0.048 [-0.456, +0.551] | 0.001971 | 0.19 | 0.852 | not applied (n < 1000) | 0.920 | +2.0 | +1.6 | 0.1861 | 0.1896 |
| Glucose SD, pooled (mg/dL) | 628 | -0.121 [-0.623, +0.381] | -0.009953 | -0.47 | 0.637 | not applied (n < 1000) | 0.803 | +1.8 | +1.4 | 0.1873 | 0.1896 |
| Avg. daily SD (mg/dL) | 628 | -0.075 [-0.566, +0.416] | -0.00716 | -0.30 | 0.765 | not applied (n < 1000) | 0.875 | +1.9 | +1.5 | 0.1866 | 0.1896 |
| CV (%) | 628 | -0.358 [-0.881, +0.166] | -0.05835 | -1.34 | 0.181 | not applied (n < 1000) | 0.370 | +0.2 | -0.2 | 0.1918 | 0.1896 |
| Mean / SD ratio | 628 | +0.425 [-0.092, +0.941] | 0.3255 | 1.61 | 0.108 | not applied (n < 1000) | 0.252 | -0.7 | -1.1 | 0.1930 | 0.1896 |
| Avg. daily mean / SD | 628 | +0.353 [-0.164, +0.869] | 0.2215 | 1.34 | 0.181 | not applied (n < 1000) | 0.370 | +0.2 | -0.2 | 0.1910 | 0.1896 |
| MAG (mg/dL/h) | 628 | -0.057 [-0.518, +0.403] | -0.006036 | -0.24 | 0.807 | not applied (n < 1000) | 0.899 | +1.9 | +1.6 | 0.1895 | 0.1896 |
| Avg. daily range (mg/dL) | 628 | -0.095 [-0.580, +0.391] | -0.002412 | -0.38 | 0.702 | not applied (n < 1000) | 0.829 | +1.9 | +1.5 | 0.1876 | 0.1896 |
| SD of daily means (mg/dL) | 628 | -0.107 [-0.628, +0.413] | -0.01531 | -0.40 | 0.686 | not applied (n < 1000) | 0.828 | +1.8 | +1.4 | 0.1886 | 0.1896 |
| Time in range 70-180, pooled (%) | 628 | -0.108 [-0.629, +0.413] | -0.008256 | -0.41 | 0.685 | not applied (n < 1000) | 0.828 | +1.8 | +1.4 | 0.1845 | 0.1896 |
| Avg. daily time in range 70-180 (%) | 628 | -0.104 [-0.637, +0.428] | -0.007941 | -0.38 | 0.701 | not applied (n < 1000) | 0.829 | +1.8 | +1.5 | 0.1846 | 0.1896 |
| Time < 54, pooled (%) | 628 | -0.383 [-0.740, -0.026] | -0.4365 | -2.10 | 0.036* | not applied (n < 1000) | 0.119 | -0.4 | -0.7 | 0.1918 | 0.1896 |
| Avg. daily time < 54 (%) | 628 | -0.462 [-0.902, -0.022] | -0.6116 | -2.06 | 0.040* | not applied (n < 1000) | 0.125 | -1.4 | -1.8 | 0.1930 | 0.1896 |
| Time 54-69, pooled (%) | 628 | -0.215 [-0.680, +0.251] | -0.09408 | -0.90 | 0.366 | not applied (n < 1000) | 0.601 | +1.2 | +0.9 | 0.1893 | 0.1896 |
| Avg. daily time 54-69 (%) | 628 | -0.238 [-0.705, +0.229] | -0.1007 | -1.00 | 0.317 | not applied (n < 1000) | 0.547 | +1.1 | +0.7 | 0.1896 | 0.1896 |
| Time < 70, pooled (%) | 628 | -0.292 [-0.754, +0.169] | -0.1036 | -1.24 | 0.215 | not applied (n < 1000) | 0.421 | +0.6 | +0.2 | 0.1901 | 0.1896 |
| Avg. daily time < 70 (%) | 628 | -0.318 [-0.783, +0.147] | -0.1107 | -1.34 | 0.180 | not applied (n < 1000) | 0.370 | +0.4 | -0.0 | 0.1905 | 0.1896 |
| Time 54-250, pooled (%) | 628 | -0.081 [-0.496, +0.334] | -0.01406 | -0.38 | 0.702 | not applied (n < 1000) | 0.829 | +1.9 | +1.5 | 0.1875 | 0.1896 |
| Avg. daily time 54-250 (%) | 628 | -0.107 [-0.575, +0.360] | -0.02044 | -0.45 | 0.653 | not applied (n < 1000) | 0.809 | +1.8 | +1.4 | 0.1876 | 0.1896 |
| Time 181-250, pooled (%) | 628 | +0.159 [-0.389, +0.707] | 0.01748 | 0.57 | 0.569 | not applied (n < 1000) | 0.761 | +1.6 | +1.2 | 0.1841 | 0.1896 |
| Avg. daily time 181-250 (%) | 628 | +0.148 [-0.400, +0.696] | 0.01585 | 0.53 | 0.596 | not applied (n < 1000) | 0.772 | +1.7 | +1.3 | 0.1842 | 0.1896 |
| Time > 180, pooled (%) | 628 | +0.175 [-0.346, +0.695] | 0.0134 | 0.66 | 0.511 | not applied (n < 1000) | 0.721 | +1.5 | +1.2 | 0.1852 | 0.1896 |
| Avg. daily time > 180 (%) | 628 | +0.179 [-0.355, +0.713] | 0.01372 | 0.66 | 0.511 | not applied (n < 1000) | 0.721 | +1.5 | +1.1 | 0.1854 | 0.1896 |
| Nocturnal time > 180 (%) | 628 | -0.093 [-0.614, +0.427] | -0.007587 | -0.35 | 0.725 | not applied (n < 1000) | 0.848 | +1.9 | +1.5 | 0.1851 | 0.1896 |
| Any reading > 250 during wear (0/1) | 628 | -0.164 [-0.672, +0.344] | -0.3612 | -0.63 | 0.526 | not applied (n < 1000) | 0.729 | +1.6 | +1.2 | 0.1853 | 0.1896 |
| Time > 250, pooled (%) | 628 | +0.142 [-0.291, +0.575] | 0.02496 | 0.64 | 0.521 | not applied (n < 1000) | 0.724 | +1.7 | +1.3 | 0.1881 | 0.1896 |
| Avg. daily time > 250 (%) | 628 | +0.178 [-0.319, +0.675] | 0.03454 | 0.70 | 0.483 | not applied (n < 1000) | 0.707 | +1.5 | +1.1 | 0.1884 | 0.1896 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 628; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 628 | -0.708 [-3.316, +1.899] | -0.8371 | -0.53 | 0.594 | not applied (n < 1000) | 0.772 | +1.0 | +0.0 | 0.0040 | 0.0109 |
| Mean glucose (mg/dL) | 628 | -0.630 [-3.138, +1.879] | -0.02586 | -0.49 | 0.623 | not applied (n < 1000) | 0.788 | +1.2 | +0.2 | 0.0030 | 0.0109 |
| GMI (%) | 628 | -0.630 [-3.138, +1.879] | -1.081 | -0.49 | 0.623 | not applied (n < 1000) | 0.788 | +1.2 | +0.2 | 0.0030 | 0.0109 |
| Nocturnal mean 00-06h (mg/dL) | 628 | -1.152 [-3.863, +1.560] | -0.0474 | -0.83 | 0.405 | not applied (n < 1000) | 0.638 | -0.8 | -1.8 | 0.0036 | 0.0109 |
| Glucose SD, pooled (mg/dL) | 628 | -0.421 [-2.524, +1.681] | -0.03471 | -0.39 | 0.694 | not applied (n < 1000) | 0.829 | +1.7 | +0.7 | 0.0022 | 0.0109 |
| Avg. daily SD (mg/dL) | 628 | -0.030 [-1.726, +1.665] | -0.002909 | -0.04 | 0.972 | not applied (n < 1000) | 0.988 | +2.0 | +1.0 | 0.0051 | 0.0109 |
| CV (%) | 628 | +0.137 [-1.368, +1.642] | 0.0223 | 0.18 | 0.859 | not applied (n < 1000) | 0.921 | +2.0 | +1.0 | 0.0061 | 0.0109 |
| Mean / SD ratio | 628 | -0.345 [-1.806, +1.117] | -0.2642 | -0.46 | 0.644 | not applied (n < 1000) | 0.806 | +1.8 | +0.8 | 0.0064 | 0.0109 |
| Avg. daily mean / SD | 628 | -0.532 [-1.921, +0.856] | -0.3343 | -0.75 | 0.452 | not applied (n < 1000) | 0.686 | +1.4 | +0.4 | 0.0088 | 0.0109 |
| MAG (mg/dL/h) | 628 | +0.963 [-0.590, +2.515] | 0.1011 | 1.21 | 0.224 | not applied (n < 1000) | 0.432 | +0.0 | -1.0 | 0.0110 | 0.0109 |
| Avg. daily range (mg/dL) | 628 | +0.324 [-1.340, +1.988] | 0.008243 | 0.38 | 0.703 | not applied (n < 1000) | 0.829 | +1.8 | +0.8 | 0.0066 | 0.0109 |
| SD of daily means (mg/dL) | 628 | -1.532 [-4.702, +1.638] | -0.2187 | -0.95 | 0.343 | not applied (n < 1000) | 0.572 | -3.0 | -4.0 | -0.0023 | 0.0109 |
| Time in range 70-180, pooled (%) | 628 | +0.012 [-2.808, +2.833] | 0.0009405 | 0.01 | 0.993 | not applied (n < 1000) | 0.994 | +2.0 | +1.0 | -0.0003 | 0.0109 |
| Avg. daily time in range 70-180 (%) | 628 | +0.094 [-2.736, +2.924] | 0.007124 | 0.06 | 0.948 | not applied (n < 1000) | 0.977 | +2.0 | +1.0 | -0.0006 | 0.0109 |
| Time < 54, pooled (%) | 628 | +0.319 [-1.199, +1.836] | 0.3634 | 0.41 | 0.681 | not applied (n < 1000) | 0.828 | +1.8 | +0.8 | 0.0068 | 0.0109 |
| Avg. daily time < 54 (%) | 628 | +0.460 [-0.825, +1.746] | 0.6096 | 0.70 | 0.483 | not applied (n < 1000) | 0.707 | +1.5 | +0.5 | 0.0094 | 0.0109 |
| Time 54-69, pooled (%) | 628 | +0.566 [-0.757, +1.888] | 0.2481 | 0.84 | 0.402 | not applied (n < 1000) | 0.638 | +1.3 | +0.3 | 0.0102 | 0.0109 |
| Avg. daily time 54-69 (%) | 628 | +0.457 [-0.858, +1.771] | 0.1929 | 0.68 | 0.496 | not applied (n < 1000) | 0.716 | +1.5 | +0.5 | 0.0103 | 0.0109 |
| Time < 70, pooled (%) | 628 | +0.559 [-0.736, +1.853] | 0.1978 | 0.85 | 0.398 | not applied (n < 1000) | 0.638 | +1.3 | +0.3 | 0.0100 | 0.0109 |
| Avg. daily time < 70 (%) | 628 | +0.499 [-0.777, +1.775] | 0.1736 | 0.77 | 0.443 | not applied (n < 1000) | 0.679 | +1.5 | +0.5 | 0.0105 | 0.0109 |
| Time 54-250, pooled (%) | 628 | +1.493 [-1.524, +4.509] | 0.2586 | 0.97 | 0.332 | not applied (n < 1000) | 0.560 | -2.8 | -3.8 | 0.0031 | 0.0109 |
| Avg. daily time 54-250 (%) | 628 | +1.611 [-1.510, +4.731] | 0.3068 | 1.01 | 0.312 | not applied (n < 1000) | 0.543 | -3.6 | -4.5 | 0.0020 | 0.0109 |
| Time 181-250, pooled (%) | 628 | +0.825 [-1.957, +3.607] | 0.09055 | 0.58 | 0.561 | not applied (n < 1000) | 0.758 | +0.6 | -0.4 | 0.0010 | 0.0109 |
| Avg. daily time 181-250 (%) | 628 | +0.684 [-2.036, +3.405] | 0.07311 | 0.49 | 0.622 | not applied (n < 1000) | 0.788 | +1.0 | +0.0 | 0.0009 | 0.0109 |
| Time > 180, pooled (%) | 628 | -0.140 [-3.034, +2.754] | -0.01077 | -0.10 | 0.924 | not applied (n < 1000) | 0.973 | +2.0 | +1.0 | -0.0003 | 0.0109 |
| Avg. daily time > 180 (%) | 628 | -0.210 [-3.118, +2.697] | -0.01612 | -0.14 | 0.887 | not applied (n < 1000) | 0.941 | +1.9 | +0.9 | -0.0007 | 0.0109 |
| Nocturnal time > 180 (%) | 628 | -0.598 [-3.999, +2.804] | -0.04854 | -0.34 | 0.730 | not applied (n < 1000) | 0.848 | +1.2 | +0.3 | -0.0036 | 0.0109 |
| Any reading > 250 during wear (0/1) | 628 | +0.884 [-0.691, +2.459] | 1.944 | 1.10 | 0.271 | not applied (n < 1000) | 0.507 | +0.4 | -0.6 | 0.0107 | 0.0109 |
| Time > 250, pooled (%) | 628 | -1.566 [-4.645, +1.514] | -0.2753 | -1.00 | 0.319 | not applied (n < 1000) | 0.547 | -3.3 | -4.3 | 0.0047 | 0.0109 |
| Avg. daily time > 250 (%) | 628 | -1.710 [-4.898, +1.477] | -0.3322 | -1.05 | 0.293 | not applied (n < 1000) | 0.519 | -4.3 | -5.3 | 0.0032 | 0.0109 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 575; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 575 | +312.274 [-183.949, +808.498] | 367.2 | 1.23 | 0.217 | not applied (n < 1000) | 0.425 | -1.0 | +0.0 | 0.1257 | 0.1243 |
| Mean glucose (mg/dL) | 575 | -96.222 [-475.807, +283.363] | -3.915 | -0.50 | 0.619 | not applied (n < 1000) | 0.788 | +1.7 | +2.7 | 0.1211 | 0.1243 |
| GMI (%) | 575 | -96.222 [-475.807, +283.363] | -163.7 | -0.50 | 0.619 | not applied (n < 1000) | 0.788 | +1.7 | +2.7 | 0.1211 | 0.1243 |
| Nocturnal mean 00-06h (mg/dL) | 575 | +30.257 [-345.403, +405.917] | 1.226 | 0.16 | 0.875 | not applied (n < 1000) | 0.932 | +2.0 | +3.0 | 0.1215 | 0.1243 |
| Glucose SD, pooled (mg/dL) | 575 | -254.431 [-615.486, +106.623] | -21.15 | -1.38 | 0.167 | not applied (n < 1000) | 0.351 | +0.1 | +1.1 | 0.1242 | 0.1243 |
| Avg. daily SD (mg/dL) | 575 | -290.456 [-635.893, +54.980] | -27.95 | -1.65 | 0.099 | not applied (n < 1000) | 0.238 | -0.5 | +0.5 | 0.1252 | 0.1243 |
| CV (%) | 575 | -267.695 [-602.869, +67.479] | -44.33 | -1.57 | 0.117 | not applied (n < 1000) | 0.270 | -0.1 | +0.9 | 0.1240 | 0.1243 |
| Mean / SD ratio | 575 | +62.108 [-278.321, +402.538] | 47.71 | 0.36 | 0.721 | not applied (n < 1000) | 0.845 | +1.9 | +2.9 | 0.1209 | 0.1243 |
| Avg. daily mean / SD | 575 | -11.684 [-342.454, +319.085] | -7.361 | -0.07 | 0.945 | not applied (n < 1000) | 0.977 | +2.0 | +3.0 | 0.1210 | 0.1243 |
| MAG (mg/dL/h) | 575 | +166.819 [-211.276, +544.914] | 17.58 | 0.86 | 0.387 | not applied (n < 1000) | 0.633 | +1.1 | +2.1 | 0.1211 | 0.1243 |
| Avg. daily range (mg/dL) | 575 | -193.906 [-557.609, +169.797] | -4.975 | -1.04 | 0.296 | not applied (n < 1000) | 0.522 | +0.9 | +1.9 | 0.1222 | 0.1243 |
| SD of daily means (mg/dL) | 575 | -48.211 [-450.018, +353.596] | -7.001 | -0.24 | 0.814 | not applied (n < 1000) | 0.902 | +1.9 | +2.9 | 0.1213 | 0.1243 |
| Time in range 70-180, pooled (%) | 575 | +240.456 [-123.083, +603.994] | 18.4 | 1.30 | 0.195 | not applied (n < 1000) | 0.386 | +0.2 | +1.2 | 0.1241 | 0.1243 |
| Avg. daily time in range 70-180 (%) | 575 | +234.693 [-129.453, +598.839] | 17.84 | 1.26 | 0.207 | not applied (n < 1000) | 0.407 | +0.3 | +1.3 | 0.1239 | 0.1243 |
| Time < 54, pooled (%) | 575 | -209.825 [-443.563, +23.913] | -230.9 | -1.76 | 0.079 | not applied (n < 1000) | 0.196 | +0.5 | +1.5 | 0.1252 | 0.1243 |
| Avg. daily time < 54 (%) | 575 | -224.802 [-460.211, +10.607] | -285.5 | -1.87 | 0.061 | not applied (n < 1000) | 0.166 | +0.3 | +1.3 | 0.1253 | 0.1243 |
| Time 54-69, pooled (%) | 575 | -183.727 [-517.407, +149.954] | -78.8 | -1.08 | 0.281 | not applied (n < 1000) | 0.507 | +0.9 | +1.9 | 0.1244 | 0.1243 |
| Avg. daily time 54-69 (%) | 575 | -184.483 [-517.110, +148.144] | -75.87 | -1.09 | 0.277 | not applied (n < 1000) | 0.507 | +0.9 | +1.9 | 0.1240 | 0.1243 |
| Time < 70, pooled (%) | 575 | -214.010 [-528.759, +100.739] | -73.69 | -1.33 | 0.183 | not applied (n < 1000) | 0.371 | +0.5 | +1.5 | 0.1253 | 0.1243 |
| Avg. daily time < 70 (%) | 575 | -211.724 [-528.821, +105.374] | -71.42 | -1.31 | 0.191 | not applied (n < 1000) | 0.381 | +0.5 | +1.5 | 0.1246 | 0.1243 |
| Time 54-250, pooled (%) | 575 | +244.787 [-75.435, +565.010] | 41.68 | 1.50 | 0.134 | not applied (n < 1000) | 0.296 | +0.0 | +1.0 | 0.1239 | 0.1243 |
| Avg. daily time 54-250 (%) | 575 | +194.195 [-144.703, +533.092] | 36.68 | 1.12 | 0.261 | not applied (n < 1000) | 0.495 | +0.8 | +1.8 | 0.1224 | 0.1243 |
| Time 181-250, pooled (%) | 575 | -130.774 [-519.431, +257.883] | -14.43 | -0.66 | 0.510 | not applied (n < 1000) | 0.721 | +1.5 | +2.5 | 0.1214 | 0.1243 |
| Avg. daily time 181-250 (%) | 575 | -164.479 [-541.683, +212.724] | -17.64 | -0.85 | 0.393 | not applied (n < 1000) | 0.637 | +1.2 | +2.1 | 0.1221 | 0.1243 |
| Time > 180, pooled (%) | 575 | -189.525 [-561.712, +182.662] | -14.53 | -1.00 | 0.318 | not applied (n < 1000) | 0.547 | +0.9 | +1.9 | 0.1223 | 0.1243 |
| Avg. daily time > 180 (%) | 575 | -184.660 [-554.787, +185.466] | -14.18 | -0.98 | 0.328 | not applied (n < 1000) | 0.558 | +0.9 | +1.9 | 0.1219 | 0.1243 |
| Nocturnal time > 180 (%) | 575 | -209.749 [-591.440, +171.942] | -16.63 | -1.08 | 0.281 | not applied (n < 1000) | 0.507 | +0.6 | +1.6 | 0.1226 | 0.1243 |
| Any reading > 250 during wear (0/1) | 575 | +66.555 [-321.794, +454.904] | 147.3 | 0.34 | 0.737 | not applied (n < 1000) | 0.852 | +1.9 | +2.8 | 0.1212 | 0.1243 |
| Time > 250, pooled (%) | 575 | -215.131 [-539.492, +109.230] | -37.23 | -1.30 | 0.194 | not applied (n < 1000) | 0.385 | +0.5 | +1.5 | 0.1233 | 0.1243 |
| Avg. daily time > 250 (%) | 575 | -163.421 [-498.873, +172.031] | -31.53 | -0.95 | 0.340 | not applied (n < 1000) | 0.568 | +1.1 | +2.1 | 0.1216 | 0.1243 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 575; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 575 | +1.237 [-0.221, +2.695] | 1.454 | 1.66 | 0.096 | not applied (n < 1000) | 0.233 | -3.1 | +0.0 | 0.1471 | 0.1410 |
| Mean glucose (mg/dL) | 575 | -0.037 [-1.221, +1.147] | -0.001511 | -0.06 | 0.951 | not applied (n < 1000) | 0.977 | +2.0 | +5.1 | 0.1375 | 0.1410 |
| GMI (%) | 575 | -0.037 [-1.221, +1.147] | -0.06318 | -0.06 | 0.951 | not applied (n < 1000) | 0.977 | +2.0 | +5.1 | 0.1375 | 0.1410 |
| Nocturnal mean 00-06h (mg/dL) | 575 | +0.324 [-0.851, +1.500] | 0.01314 | 0.54 | 0.589 | not applied (n < 1000) | 0.768 | +1.6 | +4.7 | 0.1388 | 0.1410 |
| Glucose SD, pooled (mg/dL) | 575 | -0.420 [-1.588, +0.748] | -0.03491 | -0.70 | 0.481 | not applied (n < 1000) | 0.707 | +1.4 | +4.5 | 0.1387 | 0.1410 |
| Avg. daily SD (mg/dL) | 575 | -0.613 [-1.715, +0.488] | -0.05903 | -1.09 | 0.275 | not applied (n < 1000) | 0.507 | +0.8 | +3.9 | 0.1402 | 0.1410 |
| CV (%) | 575 | -0.526 [-1.572, +0.521] | -0.08702 | -0.98 | 0.325 | not applied (n < 1000) | 0.555 | +1.1 | +4.2 | 0.1395 | 0.1410 |
| Mean / SD ratio | 575 | -0.035 [-1.075, +1.004] | -0.02714 | -0.07 | 0.947 | not applied (n < 1000) | 0.977 | +2.0 | +5.1 | 0.1387 | 0.1410 |
| Avg. daily mean / SD | 575 | -0.155 [-1.160, +0.850] | -0.09766 | -0.30 | 0.762 | not applied (n < 1000) | 0.875 | +1.9 | +5.0 | 0.1393 | 0.1410 |
| MAG (mg/dL/h) | 575 | +0.505 [-0.659, +1.668] | 0.05318 | 0.85 | 0.395 | not applied (n < 1000) | 0.638 | +1.1 | +4.2 | 0.1387 | 0.1410 |
| Avg. daily range (mg/dL) | 575 | -0.424 [-1.554, +0.706] | -0.01088 | -0.74 | 0.462 | not applied (n < 1000) | 0.696 | +1.4 | +4.5 | 0.1391 | 0.1410 |
| SD of daily means (mg/dL) | 575 | +0.295 [-0.977, +1.567] | 0.04288 | 0.46 | 0.649 | not applied (n < 1000) | 0.807 | +1.7 | +4.8 | 0.1392 | 0.1410 |
| Time in range 70-180, pooled (%) | 575 | +0.335 [-0.858, +1.528] | 0.02563 | 0.55 | 0.582 | not applied (n < 1000) | 0.765 | +1.6 | +4.7 | 0.1376 | 0.1410 |
| Avg. daily time in range 70-180 (%) | 575 | +0.329 [-0.861, +1.519] | 0.02498 | 0.54 | 0.588 | not applied (n < 1000) | 0.768 | +1.6 | +4.7 | 0.1375 | 0.1410 |
| Time < 54, pooled (%) | 575 | -0.487 [-1.174, +0.201] | -0.5354 | -1.39 | 0.165 | not applied (n < 1000) | 0.351 | +1.1 | +4.3 | 0.1407 | 0.1410 |
| Avg. daily time < 54 (%) | 575 | -0.605 [-1.405, +0.195] | -0.7683 | -1.48 | 0.138 | not applied (n < 1000) | 0.303 | +0.7 | +3.8 | 0.1389 | 0.1410 |
| Time 54-69, pooled (%) | 575 | -0.322 [-1.300, +0.656] | -0.138 | -0.64 | 0.519 | not applied (n < 1000) | 0.724 | +1.6 | +4.7 | 0.1395 | 0.1410 |
| Avg. daily time 54-69 (%) | 575 | -0.354 [-1.342, +0.634] | -0.1456 | -0.70 | 0.482 | not applied (n < 1000) | 0.707 | +1.5 | +4.7 | 0.1386 | 0.1410 |
| Time < 70, pooled (%) | 575 | -0.412 [-1.350, +0.526] | -0.1418 | -0.86 | 0.389 | not applied (n < 1000) | 0.634 | +1.4 | +4.5 | 0.1400 | 0.1410 |
| Avg. daily time < 70 (%) | 575 | -0.452 [-1.417, +0.513] | -0.1525 | -0.92 | 0.358 | not applied (n < 1000) | 0.594 | +1.3 | +4.4 | 0.1386 | 0.1410 |
| Time 54-250, pooled (%) | 575 | +0.337 [-0.917, +1.592] | 0.05741 | 0.53 | 0.598 | not applied (n < 1000) | 0.773 | +1.6 | +4.7 | 0.1355 | 0.1410 |
| Avg. daily time 54-250 (%) | 575 | +0.157 [-1.080, +1.395] | 0.02974 | 0.25 | 0.803 | not applied (n < 1000) | 0.899 | +1.9 | +5.0 | 0.1350 | 0.1410 |
| Time 181-250, pooled (%) | 575 | -0.167 [-1.343, +1.009] | -0.01838 | -0.28 | 0.781 | not applied (n < 1000) | 0.885 | +1.9 | +5.0 | 0.1380 | 0.1410 |
| Avg. daily time 181-250 (%) | 575 | -0.272 [-1.425, +0.882] | -0.02913 | -0.46 | 0.644 | not applied (n < 1000) | 0.806 | +1.8 | +4.9 | 0.1383 | 0.1410 |
| Time > 180, pooled (%) | 575 | -0.237 [-1.441, +0.967] | -0.01819 | -0.39 | 0.699 | not applied (n < 1000) | 0.829 | +1.8 | +4.9 | 0.1369 | 0.1410 |
| Avg. daily time > 180 (%) | 575 | -0.221 [-1.416, +0.974] | -0.01699 | -0.36 | 0.717 | not applied (n < 1000) | 0.843 | +1.8 | +4.9 | 0.1365 | 0.1410 |
| Nocturnal time > 180 (%) | 575 | -0.256 [-1.524, +1.013] | -0.02028 | -0.40 | 0.693 | not applied (n < 1000) | 0.829 | +1.8 | +4.9 | 0.1362 | 0.1410 |
| Any reading > 250 during wear (0/1) | 575 | +0.269 [-0.887, +1.426] | 0.5963 | 0.46 | 0.648 | not applied (n < 1000) | 0.807 | +1.8 | +4.9 | 0.1384 | 0.1410 |
| Time > 250, pooled (%) | 575 | -0.265 [-1.528, +0.998] | -0.04588 | -0.41 | 0.681 | not applied (n < 1000) | 0.828 | +1.7 | +4.9 | 0.1357 | 0.1410 |
| Avg. daily time > 250 (%) | 575 | -0.068 [-1.292, +1.156] | -0.01311 | -0.11 | 0.913 | not applied (n < 1000) | 0.966 | +2.0 | +5.1 | 0.1350 | 0.1410 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 576; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 576 | +1.114 [+0.257, +1.971] | 1.297 | 2.55 | 0.011* | not applied (n < 1000) | 0.062 | -8.4 | +0.0 | 0.1547 | 0.1444 |
| Mean glucose (mg/dL) | 576 | +0.941 [+0.167, +1.714] | 0.03772 | 2.38 | 0.017* | not applied (n < 1000) | 0.080 | -5.7 | +2.8 | 0.1494 | 0.1444 |
| GMI (%) | 576 | +0.941 [+0.167, +1.714] | 1.577 | 2.38 | 0.017* | not applied (n < 1000) | 0.080 | -5.7 | +2.8 | 0.1494 | 0.1444 |
| Nocturnal mean 00-06h (mg/dL) | 576 | +0.771 [+0.064, +1.478] | 0.03099 | 2.14 | 0.033* | not applied (n < 1000) | 0.111 | -3.2 | +5.2 | 0.1477 | 0.1444 |
| Glucose SD, pooled (mg/dL) | 576 | +1.015 [+0.175, +1.854] | 0.08321 | 2.37 | 0.018* | not applied (n < 1000) | 0.080 | -6.4 | +2.0 | 0.1491 | 0.1444 |
| Avg. daily SD (mg/dL) | 576 | +0.933 [+0.067, +1.798] | 0.08861 | 2.11 | 0.035* | not applied (n < 1000) | 0.116 | -5.0 | +3.4 | 0.1473 | 0.1444 |
| CV (%) | 576 | +0.892 [+0.195, +1.589] | 0.1473 | 2.51 | 0.012* | not applied (n < 1000) | 0.064 | -4.4 | +4.0 | 0.1498 | 0.1444 |
| Mean / SD ratio | 576 | -1.072 [-1.731, -0.413] | -0.8225 | -3.19 | 0.001** | not applied (n < 1000) | 0.023 (q<0.05) | -7.6 | +0.8 | 0.1549 | 0.1444 |
| Avg. daily mean / SD | 576 | -0.962 [-1.615, -0.310] | -0.606 | -2.89 | 0.004** | not applied (n < 1000) | 0.032 (q<0.05) | -5.7 | +2.7 | 0.1533 | 0.1444 |
| MAG (mg/dL/h) | 576 | +0.515 [-0.162, +1.193] | 0.05402 | 1.49 | 0.136 | not applied (n < 1000) | 0.298 | -0.4 | +8.1 | 0.1417 | 0.1444 |
| Avg. daily range (mg/dL) | 576 | +0.891 [+0.129, +1.652] | 0.02265 | 2.29 | 0.022* | not applied (n < 1000) | 0.092 | -4.5 | +3.9 | 0.1464 | 0.1444 |
| SD of daily means (mg/dL) | 576 | +0.979 [+0.331, +1.627] | 0.1402 | 2.96 | 0.003** | not applied (n < 1000) | 0.029 (q<0.05) | -6.5 | +2.0 | 0.1516 | 0.1444 |
| Time in range 70-180, pooled (%) | 576 | -1.016 [-1.808, -0.223] | -0.07631 | -2.51 | 0.012* | not applied (n < 1000) | 0.064 | -6.9 | +1.6 | 0.1510 | 0.1444 |
| Avg. daily time in range 70-180 (%) | 576 | -1.011 [-1.785, -0.238] | -0.07549 | -2.56 | 0.010* | not applied (n < 1000) | 0.061 | -6.7 | +1.7 | 0.1511 | 0.1444 |
| Time < 54, pooled (%) | 576 | +0.137 [-0.351, +0.625] | 0.1505 | 0.55 | 0.583 | not applied (n < 1000) | 0.765 | +1.8 | +10.2 | 0.1424 | 0.1444 |
| Avg. daily time < 54 (%) | 576 | +0.024 [-0.637, +0.685] | 0.03056 | 0.07 | 0.943 | not applied (n < 1000) | 0.977 | +2.0 | +10.4 | 0.1409 | 0.1444 |
| Time 54-69, pooled (%) | 576 | +0.017 [-0.568, +0.603] | 0.007433 | 0.06 | 0.954 | not applied (n < 1000) | 0.977 | +2.0 | +10.4 | 0.1422 | 0.1444 |
| Avg. daily time 54-69 (%) | 576 | -0.005 [-0.614, +0.604] | -0.001974 | -0.02 | 0.988 | not applied (n < 1000) | 0.992 | +2.0 | +10.4 | 0.1422 | 0.1444 |
| Time < 70, pooled (%) | 576 | +0.057 [-0.518, +0.631] | 0.01951 | 0.19 | 0.847 | not applied (n < 1000) | 0.919 | +2.0 | +10.4 | 0.1418 | 0.1444 |
| Avg. daily time < 70 (%) | 576 | +0.002 [-0.625, +0.630] | 0.0008045 | 0.01 | 0.994 | not applied (n < 1000) | 0.994 | +2.0 | +10.4 | 0.1417 | 0.1444 |
| Time 54-250, pooled (%) | 576 | -0.428 [-1.344, +0.488] | -0.07132 | -0.92 | 0.360 | not applied (n < 1000) | 0.594 | +0.4 | +8.8 | 0.1344 | 0.1444 |
| Avg. daily time 54-250 (%) | 576 | -0.549 [-1.359, +0.261] | -0.1006 | -1.33 | 0.184 | not applied (n < 1000) | 0.371 | -0.7 | +7.7 | 0.1394 | 0.1444 |
| Time 181-250, pooled (%) | 576 | +1.187 [+0.410, +1.965] | 0.1297 | 2.99 | 0.003** | not applied (n < 1000) | 0.028 (q<0.05) | -10.0 | -1.6 | 0.1531 | 0.1444 |
| Avg. daily time 181-250 (%) | 576 | +1.110 [+0.314, +1.907] | 0.118 | 2.73 | 0.006** | not applied (n < 1000) | 0.042 (q<0.05) | -8.6 | -0.1 | 0.1508 | 0.1444 |
| Time > 180, pooled (%) | 576 | +1.000 [+0.215, +1.784] | 0.07518 | 2.50 | 0.012* | not applied (n < 1000) | 0.064 | -6.6 | +1.8 | 0.1497 | 0.1444 |
| Avg. daily time > 180 (%) | 576 | +1.014 [+0.255, +1.772] | 0.07633 | 2.62 | 0.009** | not applied (n < 1000) | 0.055 | -6.8 | +1.6 | 0.1502 | 0.1444 |
| Nocturnal time > 180 (%) | 576 | +0.685 [-0.033, +1.404] | 0.05377 | 1.87 | 0.061 | not applied (n < 1000) | 0.166 | -2.1 | +6.3 | 0.1452 | 0.1444 |
| Any reading > 250 during wear (0/1) | 576 | +0.807 [+0.116, +1.499] | 1.784 | 2.29 | 0.022* | not applied (n < 1000) | 0.092 | -3.6 | +4.8 | 0.1449 | 0.1444 |
| Time > 250, pooled (%) | 576 | +0.413 [-0.481, +1.307] | 0.06983 | 0.91 | 0.365 | not applied (n < 1000) | 0.601 | +0.5 | +8.9 | 0.1349 | 0.1444 |
| Avg. daily time > 250 (%) | 576 | +0.555 [-0.248, +1.359] | 0.1037 | 1.35 | 0.176 | not applied (n < 1000) | 0.366 | -0.7 | +7.7 | 0.1400 | 0.1444 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 588; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 588 | -8.459 [-13.666, -3.252] | -9.895 | -3.18 | 0.001** | not applied (n < 1000) | 0.023 (q<0.05) | -6.9 | +0.0 | -0.0040 | -0.0166 |
| Mean glucose (mg/dL) | 588 | -5.870 [-11.205, -0.534] | -0.2384 | -2.16 | 0.031* | not applied (n < 1000) | 0.109 | -2.4 | +4.5 | -0.0114 | -0.0166 |
| GMI (%) | 588 | -5.870 [-11.205, -0.534] | -9.968 | -2.16 | 0.031* | not applied (n < 1000) | 0.109 | -2.4 | +4.5 | -0.0114 | -0.0166 |
| Nocturnal mean 00-06h (mg/dL) | 588 | -5.828 [-11.473, -0.183] | -0.2371 | -2.02 | 0.043* | not applied (n < 1000) | 0.131 | -2.4 | +4.5 | -0.0119 | -0.0166 |
| Glucose SD, pooled (mg/dL) | 588 | -4.427 [-9.951, +1.098] | -0.3639 | -1.57 | 0.116 | not applied (n < 1000) | 0.270 | -0.4 | +6.6 | -0.0167 | -0.0166 |
| Avg. daily SD (mg/dL) | 588 | -3.807 [-9.124, +1.510] | -0.3622 | -1.40 | 0.161 | not applied (n < 1000) | 0.344 | +0.3 | +7.2 | -0.0180 | -0.0166 |
| CV (%) | 588 | -0.935 [-6.538, +4.667] | -0.1546 | -0.33 | 0.744 | not applied (n < 1000) | 0.856 | +1.9 | +8.8 | -0.0216 | -0.0166 |
| Mean / SD ratio | 588 | +0.699 [-4.706, +6.103] | 0.5381 | 0.25 | 0.800 | not applied (n < 1000) | 0.899 | +1.9 | +8.9 | -0.0219 | -0.0166 |
| Avg. daily mean / SD | 588 | +1.524 [-3.761, +6.810] | 0.9662 | 0.57 | 0.572 | not applied (n < 1000) | 0.762 | +1.7 | +8.6 | -0.0222 | -0.0166 |
| MAG (mg/dL/h) | 588 | -12.146 [-17.766, -6.525] | -1.282 | -4.24 | 2.3e-05*** | not applied (n < 1000) | 0.002 (q<0.05) | -17.8 | -10.9 | 0.0039 | -0.0166 |
| Avg. daily range (mg/dL) | 588 | -4.235 [-9.562, +1.092] | -0.1082 | -1.56 | 0.119 | not applied (n < 1000) | 0.271 | -0.2 | +6.7 | -0.0180 | -0.0166 |
| SD of daily means (mg/dL) | 588 | -5.180 [-10.922, +0.563] | -0.748 | -1.77 | 0.077 | not applied (n < 1000) | 0.196 | -1.5 | +5.4 | -0.0119 | -0.0166 |
| Time in range 70-180, pooled (%) | 588 | +5.680 [+0.023, +11.337] | 0.4312 | 1.97 | 0.049* | not applied (n < 1000) | 0.144 | -2.1 | +4.8 | -0.0116 | -0.0166 |
| Avg. daily time in range 70-180 (%) | 588 | +5.596 [-0.167, +11.358] | 0.4226 | 1.90 | 0.057 | not applied (n < 1000) | 0.161 | -2.0 | +5.0 | -0.0118 | -0.0166 |
| Time < 54, pooled (%) | 588 | -0.060 [-4.718, +4.597] | -0.06687 | -0.03 | 0.980 | not applied (n < 1000) | 0.992 | +2.0 | +8.9 | -0.0181 | -0.0166 |
| Avg. daily time < 54 (%) | 588 | -0.142 [-4.546, +4.263] | -0.1818 | -0.06 | 0.950 | not applied (n < 1000) | 0.977 | +2.0 | +8.9 | -0.0176 | -0.0166 |
| Time 54-69, pooled (%) | 588 | +1.691 [-3.170, +6.552] | 0.7337 | 0.68 | 0.495 | not applied (n < 1000) | 0.716 | +1.6 | +8.5 | -0.0179 | -0.0166 |
| Avg. daily time 54-69 (%) | 588 | +1.374 [-3.460, +6.209] | 0.5716 | 0.56 | 0.577 | not applied (n < 1000) | 0.765 | +1.7 | +8.7 | -0.0178 | -0.0166 |
| Time < 70, pooled (%) | 588 | +1.348 [-3.342, +6.039] | 0.4694 | 0.56 | 0.573 | not applied (n < 1000) | 0.762 | +1.8 | +8.7 | -0.0178 | -0.0166 |
| Avg. daily time < 70 (%) | 588 | +1.098 [-3.527, +5.723] | 0.3746 | 0.47 | 0.642 | not applied (n < 1000) | 0.806 | +1.8 | +8.8 | -0.0177 | -0.0166 |
| Time 54-250, pooled (%) | 588 | +6.596 [+1.491, +11.701] | 1.109 | 2.53 | 0.011* | not applied (n < 1000) | 0.064 | -3.8 | +3.1 | -0.0103 | -0.0166 |
| Avg. daily time 54-250 (%) | 588 | +7.032 [+2.161, +11.903] | 1.301 | 2.83 | 0.005** | not applied (n < 1000) | 0.036 (q<0.05) | -4.6 | +2.4 | -0.0080 | -0.0166 |
| Time 181-250, pooled (%) | 588 | -4.225 [-10.068, +1.617] | -0.4679 | -1.42 | 0.156 | not applied (n < 1000) | 0.337 | -0.3 | +6.7 | -0.0144 | -0.0166 |
| Avg. daily time 181-250 (%) | 588 | -4.098 [-10.035, +1.840] | -0.4422 | -1.35 | 0.176 | not applied (n < 1000) | 0.366 | -0.1 | +6.8 | -0.0148 | -0.0166 |
| Time > 180, pooled (%) | 588 | -5.985 [-11.671, -0.298] | -0.4554 | -2.06 | 0.039* | not applied (n < 1000) | 0.125 | -2.6 | +4.4 | -0.0111 | -0.0166 |
| Avg. daily time > 180 (%) | 588 | -5.881 [-11.727, -0.035] | -0.4488 | -1.97 | 0.049* | not applied (n < 1000) | 0.144 | -2.4 | +4.5 | -0.0113 | -0.0166 |
| Nocturnal time > 180 (%) | 588 | -4.938 [-11.119, +1.242] | -0.3927 | -1.57 | 0.117 | not applied (n < 1000) | 0.270 | -1.2 | +5.7 | -0.0144 | -0.0166 |
| Any reading > 250 during wear (0/1) | 588 | -1.842 [-7.642, +3.957] | -4.074 | -0.62 | 0.534 | not applied (n < 1000) | 0.736 | +1.6 | +8.5 | -0.0186 | -0.0166 |
| Time > 250, pooled (%) | 588 | -6.678 [-11.722, -1.634] | -1.14 | -2.59 | 0.009** | not applied (n < 1000) | 0.058 | -4.0 | +3.0 | -0.0103 | -0.0166 |
| Avg. daily time > 250 (%) | 588 | -7.135 [-12.090, -2.180] | -1.347 | -2.82 | 0.005** | not applied (n < 1000) | 0.036 (q<0.05) | -4.8 | +2.2 | -0.0082 | -0.0166 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 577; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 577 | +2.275 [+0.457, +4.094] | 2.651 | 2.45 | 0.014* | not applied (n < 1000) | 0.071 | -7.6 | +0.0 | 0.0946 | 0.0856 |
| Mean glucose (mg/dL) | 577 | +1.690 [+0.047, +3.334] | 0.06788 | 2.02 | 0.044* | not applied (n < 1000) | 0.131 | -3.5 | +4.1 | 0.0884 | 0.0856 |
| GMI (%) | 577 | +1.690 [+0.047, +3.334] | 2.838 | 2.02 | 0.044* | not applied (n < 1000) | 0.131 | -3.5 | +4.1 | 0.0884 | 0.0856 |
| Nocturnal mean 00-06h (mg/dL) | 577 | +1.225 [-0.316, +2.766] | 0.04926 | 1.56 | 0.119 | not applied (n < 1000) | 0.271 | -0.9 | +6.7 | 0.0856 | 0.0856 |
| Glucose SD, pooled (mg/dL) | 577 | +1.768 [+0.107, +3.430] | 0.1451 | 2.09 | 0.037* | not applied (n < 1000) | 0.121 | -3.6 | +4.0 | 0.0868 | 0.0856 |
| Avg. daily SD (mg/dL) | 577 | +1.594 [-0.147, +3.335] | 0.1514 | 1.79 | 0.073 | not applied (n < 1000) | 0.186 | -2.5 | +5.1 | 0.0848 | 0.0856 |
| CV (%) | 577 | +1.600 [+0.086, +3.113] | 0.264 | 2.07 | 0.038* | not applied (n < 1000) | 0.124 | -2.6 | +5.0 | 0.0882 | 0.0856 |
| Mean / SD ratio | 577 | -2.109 [-3.505, -0.714] | -1.617 | -2.96 | 0.003** | not applied (n < 1000) | 0.029 (q<0.05) | -6.3 | +1.3 | 0.0946 | 0.0856 |
| Avg. daily mean / SD | 577 | -1.752 [-3.159, -0.345] | -1.102 | -2.44 | 0.015* | not applied (n < 1000) | 0.072 | -3.7 | +3.9 | 0.0906 | 0.0856 |
| MAG (mg/dL/h) | 577 | +0.782 [-0.669, +2.234] | 0.08168 | 1.06 | 0.291 | not applied (n < 1000) | 0.518 | +0.8 | +8.4 | 0.0854 | 0.0856 |
| Avg. daily range (mg/dL) | 577 | +1.529 [-0.073, +3.130] | 0.03883 | 1.87 | 0.061 | not applied (n < 1000) | 0.166 | -2.3 | +5.3 | 0.0860 | 0.0856 |
| SD of daily means (mg/dL) | 577 | +1.866 [+0.502, +3.229] | 0.267 | 2.68 | 0.007** | not applied (n < 1000) | 0.047 (q<0.05) | -4.8 | +2.8 | 0.0924 | 0.0856 |
| Time in range 70-180, pooled (%) | 577 | -1.721 [-3.342, -0.099] | -0.1294 | -2.08 | 0.038* | not applied (n < 1000) | 0.122 | -3.6 | +4.0 | 0.0883 | 0.0856 |
| Avg. daily time in range 70-180 (%) | 577 | -1.679 [-3.279, -0.080] | -0.1255 | -2.06 | 0.040* | not applied (n < 1000) | 0.125 | -3.3 | +4.3 | 0.0888 | 0.0856 |
| Time < 54, pooled (%) | 577 | +0.183 [-1.406, +1.773] | 0.2018 | 0.23 | 0.821 | not applied (n < 1000) | 0.905 | +1.9 | +9.5 | 0.0821 | 0.0856 |
| Avg. daily time < 54 (%) | 577 | -0.041 [-1.629, +1.548] | -0.05182 | -0.05 | 0.960 | not applied (n < 1000) | 0.981 | +2.0 | +9.6 | 0.0818 | 0.0856 |
| Time 54-69, pooled (%) | 577 | -0.146 [-1.610, +1.319] | -0.06248 | -0.19 | 0.846 | not applied (n < 1000) | 0.919 | +2.0 | +9.6 | 0.0816 | 0.0856 |
| Avg. daily time 54-69 (%) | 577 | -0.227 [-1.748, +1.294] | -0.0935 | -0.29 | 0.770 | not applied (n < 1000) | 0.879 | +1.9 | +9.5 | 0.0815 | 0.0856 |
| Time < 70, pooled (%) | 577 | -0.061 [-1.511, +1.389] | -0.02088 | -0.08 | 0.935 | not applied (n < 1000) | 0.977 | +2.0 | +9.6 | 0.0821 | 0.0856 |
| Avg. daily time < 70 (%) | 577 | -0.198 [-1.750, +1.353] | -0.06699 | -0.25 | 0.802 | not applied (n < 1000) | 0.899 | +1.9 | +9.5 | 0.0818 | 0.0856 |
| Time 54-250, pooled (%) | 577 | -0.565 [-2.488, +1.358] | -0.09416 | -0.58 | 0.565 | not applied (n < 1000) | 0.760 | +1.4 | +9.0 | 0.0742 | 0.0856 |
| Avg. daily time 54-250 (%) | 577 | -0.707 [-2.736, +1.322] | -0.1295 | -0.68 | 0.495 | not applied (n < 1000) | 0.716 | +1.0 | +8.6 | 0.0771 | 0.0856 |
| Time 181-250, pooled (%) | 577 | +2.169 [+0.584, +3.755] | 0.2372 | 2.68 | 0.007** | not applied (n < 1000) | 0.047 (q<0.05) | -6.9 | +0.7 | 0.0929 | 0.0856 |
| Avg. daily time 181-250 (%) | 577 | +2.027 [+0.439, +3.615] | 0.2157 | 2.50 | 0.012* | not applied (n < 1000) | 0.064 | -5.8 | +1.8 | 0.0914 | 0.0856 |
| Time > 180, pooled (%) | 577 | +1.729 [+0.110, +3.348] | 0.1302 | 2.09 | 0.036* | not applied (n < 1000) | 0.120 | -3.7 | +3.9 | 0.0879 | 0.0856 |
| Avg. daily time > 180 (%) | 577 | +1.730 [+0.138, +3.323] | 0.1304 | 2.13 | 0.033* | not applied (n < 1000) | 0.113 | -3.7 | +3.9 | 0.0885 | 0.0856 |
| Nocturnal time > 180 (%) | 577 | +1.062 [-0.441, +2.564] | 0.08332 | 1.38 | 0.166 | not applied (n < 1000) | 0.351 | -0.2 | +7.4 | 0.0846 | 0.0856 |
| Any reading > 250 during wear (0/1) | 577 | +1.512 [+0.055, +2.969] | 3.343 | 2.03 | 0.042* | not applied (n < 1000) | 0.130 | -2.3 | +5.3 | 0.0869 | 0.0856 |
| Time > 250, pooled (%) | 577 | +0.544 [-1.387, +2.476] | 0.09211 | 0.55 | 0.581 | not applied (n < 1000) | 0.765 | +1.4 | +9.0 | 0.0747 | 0.0856 |
| Avg. daily time > 250 (%) | 577 | +0.725 [-1.362, +2.812] | 0.1356 | 0.68 | 0.496 | not applied (n < 1000) | 0.716 | +1.0 | +8.6 | 0.0774 | 0.0856 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

### Population: Healthy group (no diabetes + pre-diabetes / lifestyle)

#### MoCA total score (0-30)
*n = 408; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 408 | -0.168 [-0.391, +0.054] | -0.3949 | -1.48 | 0.138 | not applied (n < 1000) | 0.943 | +0.3 | +0.0 | 0.0387 | 0.0383 |
| Mean glucose (mg/dL) | 408 | -0.116 [-0.358, +0.125] | -0.008309 | -0.94 | 0.345 | not applied (n < 1000) | 0.987 | +1.1 | +0.9 | 0.0354 | 0.0383 |
| GMI (%) | 408 | -0.116 [-0.358, +0.125] | -0.3474 | -0.94 | 0.345 | not applied (n < 1000) | 0.987 | +1.1 | +0.9 | 0.0354 | 0.0383 |
| Nocturnal mean 00-06h (mg/dL) | 408 | -0.099 [-0.343, +0.144] | -0.006472 | -0.80 | 0.424 | not applied (n < 1000) | 0.987 | +1.4 | +1.1 | 0.0345 | 0.0383 |
| Glucose SD, pooled (mg/dL) | 408 | -0.116 [-0.397, +0.164] | -0.01806 | -0.81 | 0.416 | not applied (n < 1000) | 0.987 | +1.1 | +0.9 | 0.0358 | 0.0383 |
| Avg. daily SD (mg/dL) | 408 | -0.122 [-0.401, +0.158] | -0.02061 | -0.85 | 0.393 | not applied (n < 1000) | 0.987 | +1.1 | +0.8 | 0.0351 | 0.0383 |
| CV (%) | 408 | -0.105 [-0.376, +0.165] | -0.02281 | -0.76 | 0.446 | not applied (n < 1000) | 0.987 | +1.3 | +1.0 | 0.0353 | 0.0383 |
| Mean / SD ratio | 408 | +0.179 [-0.077, +0.435] | 0.1601 | 1.37 | 0.170 | not applied (n < 1000) | 0.967 | -0.1 | -0.3 | 0.0394 | 0.0383 |
| Avg. daily mean / SD | 408 | +0.134 [-0.129, +0.397] | 0.09542 | 1.00 | 0.317 | not applied (n < 1000) | 0.987 | +0.9 | +0.6 | 0.0356 | 0.0383 |
| MAG (mg/dL/h) | 408 | -0.078 [-0.342, +0.186] | -0.009635 | -0.58 | 0.564 | not applied (n < 1000) | 0.987 | +1.6 | +1.3 | 0.0350 | 0.0383 |
| Avg. daily range (mg/dL) | 408 | -0.128 [-0.407, +0.151] | -0.004801 | -0.90 | 0.368 | not applied (n < 1000) | 0.987 | +1.0 | +0.7 | 0.0334 | 0.0383 |
| SD of daily means (mg/dL) | 408 | +0.092 [-0.179, +0.364] | 0.0244 | 0.67 | 0.505 | not applied (n < 1000) | 0.987 | +1.4 | +1.1 | 0.0374 | 0.0383 |
| Time in range 70-180, pooled (%) | 408 | +0.079 [-0.116, +0.274] | 0.01536 | 0.80 | 0.426 | not applied (n < 1000) | 0.987 | +1.6 | +1.3 | 0.0378 | 0.0383 |
| Avg. daily time in range 70-180 (%) | 408 | +0.060 [-0.131, +0.251] | 0.01126 | 0.61 | 0.539 | not applied (n < 1000) | 0.987 | +1.8 | +1.5 | 0.0375 | 0.0383 |
| Time < 54, pooled (%) | 408 | -0.031 [-0.456, +0.394] | -0.03302 | -0.14 | 0.886 | not applied (n < 1000) | 0.987 | +1.9 | +1.6 | 0.0215 | 0.0383 |
| Avg. daily time < 54 (%) | 408 | -0.008 [-0.336, +0.321] | -0.01076 | -0.05 | 0.963 | not applied (n < 1000) | 0.987 | +2.0 | +1.7 | 0.0291 | 0.0383 |
| Time 54-69, pooled (%) | 408 | -0.123 [-0.307, +0.061] | -0.0577 | -1.31 | 0.190 | not applied (n < 1000) | 0.967 | +1.0 | +0.7 | 0.0381 | 0.0383 |
| Avg. daily time 54-69 (%) | 408 | -0.105 [-0.294, +0.083] | -0.04812 | -1.09 | 0.274 | not applied (n < 1000) | 0.987 | +1.3 | +1.0 | 0.0377 | 0.0383 |
| Time < 70, pooled (%) | 408 | -0.109 [-0.316, +0.099] | -0.04045 | -1.03 | 0.304 | not applied (n < 1000) | 0.987 | +1.2 | +1.0 | 0.0360 | 0.0383 |
| Avg. daily time < 70 (%) | 408 | -0.090 [-0.294, +0.114] | -0.03394 | -0.86 | 0.388 | not applied (n < 1000) | 0.987 | +1.5 | +1.2 | 0.0363 | 0.0383 |
| Time 54-250, pooled (%) | 408 | -0.006 [-0.286, +0.274] | -0.004732 | -0.04 | 0.968 | not applied (n < 1000) | 0.987 | +2.0 | +1.7 | 0.0323 | 0.0383 |
| Avg. daily time 54-250 (%) | 408 | -0.057 [-0.280, +0.166] | -0.05348 | -0.50 | 0.616 | not applied (n < 1000) | 0.987 | +1.8 | +1.5 | 0.0356 | 0.0383 |
| Time 181-250, pooled (%) | 408 | -0.037 [-0.242, +0.169] | -0.008816 | -0.35 | 0.726 | not applied (n < 1000) | 0.987 | +1.9 | +1.6 | 0.0362 | 0.0383 |
| Avg. daily time 181-250 (%) | 408 | -0.035 [-0.236, +0.166] | -0.007975 | -0.34 | 0.736 | not applied (n < 1000) | 0.987 | +1.9 | +1.6 | 0.0363 | 0.0383 |
| Time > 180, pooled (%) | 408 | -0.025 [-0.227, +0.177] | -0.005273 | -0.24 | 0.810 | not applied (n < 1000) | 0.987 | +2.0 | +1.7 | 0.0363 | 0.0383 |
| Avg. daily time > 180 (%) | 408 | -0.017 [-0.213, +0.178] | -0.003488 | -0.17 | 0.863 | not applied (n < 1000) | 0.987 | +2.0 | +1.7 | 0.0363 | 0.0383 |
| Nocturnal time > 180 (%) | 408 | +0.019 [-0.176, +0.214] | 0.004169 | 0.19 | 0.848 | not applied (n < 1000) | 0.987 | +2.0 | +1.7 | 0.0361 | 0.0383 |
| Any reading > 250 during wear (0/1) | 408 | -0.048 [-0.337, +0.241] | -0.1306 | -0.33 | 0.744 | not applied (n < 1000) | 0.987 | +1.8 | +1.6 | 0.0330 | 0.0383 |
| Time > 250, pooled (%) | 408 | +0.051 [-0.199, +0.302] | 0.07329 | 0.40 | 0.688 | not applied (n < 1000) | 0.987 | +1.8 | +1.5 | 0.0360 | 0.0383 |
| Avg. daily time > 250 (%) | 408 | +0.087 [-0.206, +0.380] | 0.1153 | 0.58 | 0.560 | not applied (n < 1000) | 0.987 | +1.5 | +1.2 | 0.0372 | 0.0383 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 408; events = 123; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 408 | OR 1.093 [0.870, 1.373] | 0.2095 | 0.77 | 0.443 | not applied (n < 1000) | 0.987 | +1.4 | +0.0 | 0.6239 | 0.6308 |
| Mean glucose (mg/dL) | 408 | OR 0.901 [0.711, 1.143] | -0.007407 | -0.86 | 0.391 | not applied (n < 1000) | 0.987 | +1.3 | -0.2 | 0.6295 | 0.6308 |
| GMI (%) | 408 | OR 0.901 [0.711, 1.143] | -0.3097 | -0.86 | 0.391 | not applied (n < 1000) | 0.987 | +1.3 | -0.2 | 0.6295 | 0.6308 |
| Nocturnal mean 00-06h (mg/dL) | 408 | OR 0.883 [0.696, 1.120] | -0.008074 | -1.02 | 0.306 | not applied (n < 1000) | 0.987 | +0.9 | -0.5 | 0.6310 | 0.6308 |
| Glucose SD, pooled (mg/dL) | 408 | OR 0.991 [0.792, 1.241] | -0.001383 | -0.08 | 0.938 | not applied (n < 1000) | 0.987 | +2.0 | +0.6 | 0.6279 | 0.6308 |
| Avg. daily SD (mg/dL) | 408 | OR 0.987 [0.787, 1.237] | -0.002248 | -0.12 | 0.908 | not applied (n < 1000) | 0.987 | +2.0 | +0.6 | 0.6280 | 0.6308 |
| CV (%) | 408 | OR 1.065 [0.855, 1.328] | 0.01375 | 0.56 | 0.573 | not applied (n < 1000) | 0.987 | +1.7 | +0.3 | 0.6299 | 0.6308 |
| Mean / SD ratio | 408 | OR 0.912 [0.725, 1.146] | -0.08234 | -0.79 | 0.429 | not applied (n < 1000) | 0.987 | +1.4 | -0.1 | 0.6294 | 0.6308 |
| Avg. daily mean / SD | 408 | OR 0.921 [0.732, 1.158] | -0.05854 | -0.70 | 0.481 | not applied (n < 1000) | 0.987 | +1.5 | +0.1 | 0.6271 | 0.6308 |
| MAG (mg/dL/h) | 408 | OR 1.033 [0.828, 1.289] | 0.00404 | 0.29 | 0.772 | not applied (n < 1000) | 0.987 | +1.9 | +0.5 | 0.6257 | 0.6308 |
| Avg. daily range (mg/dL) | 408 | OR 1.009 [0.808, 1.261] | 0.0003406 | 0.08 | 0.936 | not applied (n < 1000) | 0.987 | +2.0 | +0.6 | 0.6267 | 0.6308 |
| SD of daily means (mg/dL) | 408 | OR 0.905 [0.717, 1.141] | -0.02648 | -0.85 | 0.398 | not applied (n < 1000) | 0.987 | +1.3 | -0.2 | 0.6327 | 0.6308 |
| Time in range 70-180, pooled (%) | 408 | OR 0.970 [0.779, 1.209] | -0.005857 | -0.27 | 0.789 | not applied (n < 1000) | 0.987 | +1.9 | +0.5 | 0.6269 | 0.6308 |
| Avg. daily time in range 70-180 (%) | 408 | OR 0.990 [0.792, 1.237] | -0.001911 | -0.09 | 0.929 | not applied (n < 1000) | 0.987 | +2.0 | +0.6 | 0.6262 | 0.6308 |
| Time < 54, pooled (%) | 408 | OR 1.088 [0.875, 1.354] | 0.09017 | 0.76 | 0.448 | not applied (n < 1000) | 0.987 | +1.4 | -0.0 | 0.6314 | 0.6308 |
| Avg. daily time < 54 (%) | 408 | OR 1.074 [0.867, 1.330] | 0.09948 | 0.65 | 0.515 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.6309 | 0.6308 |
| Time 54-69, pooled (%) | 408 | OR 1.309 [1.056, 1.621] | 0.1264 | 2.46 | 0.014* | not applied (n < 1000) | 0.526 | -4.1 | -5.5 | 0.6401 | 0.6308 |
| Avg. daily time 54-69 (%) | 408 | OR 1.291 [1.043, 1.598] | 0.1168 | 2.34 | 0.019* | not applied (n < 1000) | 0.531 | -3.5 | -4.9 | 0.6383 | 0.6308 |
| Time < 70, pooled (%) | 408 | OR 1.278 [1.031, 1.583] | 0.091 | 2.24 | 0.025* | not applied (n < 1000) | 0.608 | -3.0 | -4.4 | 0.6415 | 0.6308 |
| Avg. daily time < 70 (%) | 408 | OR 1.261 [1.019, 1.560] | 0.08761 | 2.14 | 0.033* | not applied (n < 1000) | 0.622 | -2.5 | -3.9 | 0.6378 | 0.6308 |
| Time 54-250, pooled (%) | 408 | OR 0.986 [0.796, 1.222] | -0.0117 | -0.13 | 0.898 | not applied (n < 1000) | 0.987 | +2.0 | +0.6 | 0.6298 | 0.6308 |
| Avg. daily time 54-250 (%) | 408 | OR 1.052 [0.834, 1.327] | 0.04755 | 0.43 | 0.669 | not applied (n < 1000) | 0.987 | +1.8 | +0.4 | 0.6286 | 0.6308 |
| Time 181-250, pooled (%) | 408 | OR 0.876 [0.675, 1.138] | -0.0317 | -0.99 | 0.323 | not applied (n < 1000) | 0.987 | +0.9 | -0.5 | 0.6339 | 0.6308 |
| Avg. daily time 181-250 (%) | 408 | OR 0.875 [0.672, 1.141] | -0.03068 | -0.98 | 0.325 | not applied (n < 1000) | 0.987 | +0.9 | -0.5 | 0.6335 | 0.6308 |
| Time > 180, pooled (%) | 408 | OR 0.873 [0.669, 1.140] | -0.02879 | -1.00 | 0.318 | not applied (n < 1000) | 0.987 | +0.9 | -0.5 | 0.6347 | 0.6308 |
| Avg. daily time > 180 (%) | 408 | OR 0.862 [0.654, 1.136] | -0.0301 | -1.05 | 0.292 | not applied (n < 1000) | 0.987 | +0.7 | -0.7 | 0.6344 | 0.6308 |
| Nocturnal time > 180 (%) | 408 | OR 0.838 [0.620, 1.133] | -0.03873 | -1.15 | 0.250 | not applied (n < 1000) | 0.987 | +0.3 | -1.1 | 0.6350 | 0.6308 |
| Any reading > 250 during wear (0/1) | 408 | OR 0.901 [0.717, 1.132] | -0.2824 | -0.89 | 0.372 | not applied (n < 1000) | 0.987 | +1.2 | -0.2 | 0.6352 | 0.6308 |
| Time > 250, pooled (%) | 408 | OR 0.891 [0.678, 1.172] | -0.1643 | -0.83 | 0.409 | not applied (n < 1000) | 0.987 | +1.2 | -0.2 | 0.6339 | 0.6308 |
| Avg. daily time > 250 (%) | 408 | OR 0.802 [0.558, 1.152] | -0.2924 | -1.19 | 0.233 | not applied (n < 1000) | 0.987 | -0.0 | -1.5 | 0.6356 | 0.6308 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 408; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 408 | -0.001 [-0.219, +0.217] | -0.002196 | -0.01 | 0.993 | not applied (n < 1000) | 0.996 | +2.0 | +0.0 | 0.0307 | 0.0326 |
| Mean glucose (mg/dL) | 408 | +0.008 [-0.232, +0.248] | 0.000592 | 0.07 | 0.946 | not applied (n < 1000) | 0.987 | +2.0 | -0.0 | 0.0291 | 0.0326 |
| GMI (%) | 408 | +0.008 [-0.232, +0.248] | 0.02475 | 0.07 | 0.946 | not applied (n < 1000) | 0.987 | +2.0 | -0.0 | 0.0291 | 0.0326 |
| Nocturnal mean 00-06h (mg/dL) | 408 | -0.034 [-0.273, +0.205] | -0.002227 | -0.28 | 0.779 | not applied (n < 1000) | 0.987 | +1.9 | -0.1 | 0.0280 | 0.0326 |
| Glucose SD, pooled (mg/dL) | 408 | +0.112 [-0.122, +0.346] | 0.01747 | 0.94 | 0.347 | not applied (n < 1000) | 0.987 | +1.2 | -0.8 | 0.0291 | 0.0326 |
| Avg. daily SD (mg/dL) | 408 | +0.082 [-0.150, +0.315] | 0.01391 | 0.69 | 0.488 | not applied (n < 1000) | 0.987 | +1.6 | -0.4 | 0.0284 | 0.0326 |
| CV (%) | 408 | +0.123 [-0.088, +0.335] | 0.02678 | 1.14 | 0.252 | not applied (n < 1000) | 0.987 | +1.0 | -1.0 | 0.0304 | 0.0326 |
| Mean / SD ratio | 408 | -0.067 [-0.286, +0.152] | -0.05993 | -0.60 | 0.548 | not applied (n < 1000) | 0.987 | +1.7 | -0.3 | 0.0286 | 0.0326 |
| Avg. daily mean / SD | 408 | -0.027 [-0.251, +0.198] | -0.01901 | -0.23 | 0.816 | not applied (n < 1000) | 0.987 | +2.0 | -0.0 | 0.0288 | 0.0326 |
| MAG (mg/dL/h) | 408 | -0.144 [-0.389, +0.100] | -0.01789 | -1.16 | 0.247 | not applied (n < 1000) | 0.987 | +0.6 | -1.4 | 0.0338 | 0.0326 |
| Avg. daily range (mg/dL) | 408 | +0.046 [-0.179, +0.270] | 0.001714 | 0.40 | 0.690 | not applied (n < 1000) | 0.987 | +1.9 | -0.1 | 0.0299 | 0.0326 |
| SD of daily means (mg/dL) | 408 | +0.183 [-0.011, +0.378] | 0.04838 | 1.85 | 0.065 | not applied (n < 1000) | 0.637 | -0.4 | -2.4 | 0.0377 | 0.0326 |
| Time in range 70-180, pooled (%) | 408 | -0.122 [-0.358, +0.113] | -0.0238 | -1.02 | 0.309 | not applied (n < 1000) | 0.987 | +1.0 | -1.0 | 0.0304 | 0.0326 |
| Avg. daily time in range 70-180 (%) | 408 | -0.103 [-0.336, +0.129] | -0.01943 | -0.87 | 0.383 | not applied (n < 1000) | 0.987 | +1.3 | -0.7 | 0.0299 | 0.0326 |
| Time < 54, pooled (%) | 408 | +0.137 [-0.216, +0.491] | 0.1463 | 0.76 | 0.447 | not applied (n < 1000) | 0.987 | +0.7 | -1.3 | 0.0333 | 0.0326 |
| Avg. daily time < 54 (%) | 408 | +0.084 [-0.126, +0.294] | 0.1173 | 0.78 | 0.433 | not applied (n < 1000) | 0.987 | +1.5 | -0.5 | 0.0317 | 0.0326 |
| Time 54-69, pooled (%) | 408 | +0.071 [-0.125, +0.267] | 0.03346 | 0.71 | 0.476 | not applied (n < 1000) | 0.987 | +1.7 | -0.3 | 0.0305 | 0.0326 |
| Avg. daily time 54-69 (%) | 408 | +0.041 [-0.154, +0.236] | 0.01893 | 0.42 | 0.677 | not applied (n < 1000) | 0.987 | +1.9 | -0.1 | 0.0309 | 0.0326 |
| Time < 70, pooled (%) | 408 | +0.105 [-0.078, +0.287] | 0.03893 | 1.13 | 0.260 | not applied (n < 1000) | 0.987 | +1.3 | -0.7 | 0.0315 | 0.0326 |
| Avg. daily time < 70 (%) | 408 | +0.057 [-0.125, +0.239] | 0.02158 | 0.62 | 0.538 | not applied (n < 1000) | 0.987 | +1.8 | -0.2 | 0.0311 | 0.0326 |
| Time 54-250, pooled (%) | 408 | -0.118 [-0.363, +0.127] | -0.09821 | -0.95 | 0.344 | not applied (n < 1000) | 0.987 | +1.1 | -0.9 | 0.0337 | 0.0326 |
| Avg. daily time 54-250 (%) | 408 | -0.089 [-0.307, +0.129] | -0.08345 | -0.80 | 0.424 | not applied (n < 1000) | 0.987 | +1.5 | -0.5 | 0.0326 | 0.0326 |
| Time 181-250, pooled (%) | 408 | +0.082 [-0.164, +0.327] | 0.01964 | 0.65 | 0.514 | not applied (n < 1000) | 0.987 | +1.5 | -0.5 | 0.0283 | 0.0326 |
| Avg. daily time 181-250 (%) | 408 | +0.085 [-0.159, +0.330] | 0.0197 | 0.69 | 0.493 | not applied (n < 1000) | 0.987 | +1.5 | -0.5 | 0.0286 | 0.0326 |
| Time > 180, pooled (%) | 408 | +0.075 [-0.176, +0.326] | 0.01594 | 0.59 | 0.558 | not applied (n < 1000) | 0.987 | +1.6 | -0.4 | 0.0279 | 0.0326 |
| Avg. daily time > 180 (%) | 408 | +0.082 [-0.172, +0.337] | 0.01672 | 0.63 | 0.526 | not applied (n < 1000) | 0.987 | +1.5 | -0.5 | 0.0281 | 0.0326 |
| Nocturnal time > 180 (%) | 408 | +0.057 [-0.186, +0.300] | 0.01246 | 0.46 | 0.647 | not applied (n < 1000) | 0.987 | +1.8 | -0.2 | 0.0284 | 0.0326 |
| Any reading > 250 during wear (0/1) | 408 | +0.093 [-0.160, +0.346] | 0.252 | 0.72 | 0.472 | not applied (n < 1000) | 0.987 | +1.4 | -0.6 | 0.0296 | 0.0326 |
| Time > 250, pooled (%) | 408 | +0.018 [-0.241, +0.277] | 0.02566 | 0.14 | 0.892 | not applied (n < 1000) | 0.987 | +2.0 | -0.0 | 0.0283 | 0.0326 |
| Avg. daily time > 250 (%) | 408 | +0.045 [-0.271, +0.361] | 0.05995 | 0.28 | 0.779 | not applied (n < 1000) | 0.987 | +1.9 | -0.1 | 0.0269 | 0.0326 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 408; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 408 | +0.118 [-0.492, +0.728] | 0.2767 | 0.38 | 0.705 | not applied (n < 1000) | 0.987 | +1.8 | +0.0 | 0.0516 | 0.0547 |
| Mean glucose (mg/dL) | 408 | +0.087 [-0.521, +0.696] | 0.006221 | 0.28 | 0.779 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.0479 | 0.0547 |
| GMI (%) | 408 | +0.087 [-0.521, +0.696] | 0.2601 | 0.28 | 0.779 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.0479 | 0.0547 |
| Nocturnal mean 00-06h (mg/dL) | 408 | +0.028 [-0.578, +0.634] | 0.0018 | 0.09 | 0.929 | not applied (n < 1000) | 0.987 | +2.0 | +0.2 | 0.0442 | 0.0547 |
| Glucose SD, pooled (mg/dL) | 408 | +0.329 [-0.174, +0.831] | 0.05107 | 1.28 | 0.200 | not applied (n < 1000) | 0.967 | +0.2 | -1.6 | 0.0558 | 0.0547 |
| Avg. daily SD (mg/dL) | 408 | +0.345 [-0.191, +0.882] | 0.0584 | 1.26 | 0.207 | not applied (n < 1000) | 0.968 | +0.1 | -1.7 | 0.0568 | 0.0547 |
| CV (%) | 408 | +0.296 [-0.158, +0.749] | 0.06416 | 1.28 | 0.201 | not applied (n < 1000) | 0.967 | +0.6 | -1.2 | 0.0545 | 0.0547 |
| Mean / SD ratio | 408 | -0.410 [-0.885, +0.065] | -0.3659 | -1.69 | 0.091 | not applied (n < 1000) | 0.753 | -0.8 | -2.6 | 0.0573 | 0.0547 |
| Avg. daily mean / SD | 408 | -0.333 [-0.826, +0.159] | -0.2369 | -1.33 | 0.185 | not applied (n < 1000) | 0.967 | +0.2 | -1.6 | 0.0550 | 0.0547 |
| MAG (mg/dL/h) | 408 | -0.011 [-0.529, +0.507] | -0.001363 | -0.04 | 0.967 | not applied (n < 1000) | 0.987 | +2.0 | +0.2 | 0.0457 | 0.0547 |
| Avg. daily range (mg/dL) | 408 | +0.237 [-0.276, +0.751] | 0.008908 | 0.91 | 0.365 | not applied (n < 1000) | 0.987 | +1.1 | -0.7 | 0.0527 | 0.0547 |
| SD of daily means (mg/dL) | 408 | +0.225 [-0.178, +0.627] | 0.05926 | 1.09 | 0.274 | not applied (n < 1000) | 0.987 | +1.1 | -0.6 | 0.0545 | 0.0547 |
| Time in range 70-180, pooled (%) | 408 | -0.552 [-1.134, +0.029] | -0.1075 | -1.86 | 0.062 | not applied (n < 1000) | 0.637 | -3.2 | -4.9 | 0.0632 | 0.0547 |
| Avg. daily time in range 70-180 (%) | 408 | -0.610 [-1.219, +0.000] | -0.1145 | -1.96 | 0.050 | not applied (n < 1000) | 0.637 | -4.3 | -6.1 | 0.0653 | 0.0547 |
| Time < 54, pooled (%) | 408 | -0.085 [-0.568, +0.398] | -0.09085 | -0.35 | 0.729 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.0529 | 0.0547 |
| Avg. daily time < 54 (%) | 408 | +0.009 [-0.367, +0.385] | 0.01204 | 0.04 | 0.964 | not applied (n < 1000) | 0.987 | +2.0 | +0.2 | 0.0534 | 0.0547 |
| Time 54-69, pooled (%) | 408 | +0.072 [-0.437, +0.582] | 0.034 | 0.28 | 0.781 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.0530 | 0.0547 |
| Avg. daily time 54-69 (%) | 408 | +0.132 [-0.390, +0.654] | 0.06039 | 0.50 | 0.620 | not applied (n < 1000) | 0.987 | +1.7 | -0.1 | 0.0538 | 0.0547 |
| Time < 70, pooled (%) | 408 | +0.028 [-0.465, +0.521] | 0.0104 | 0.11 | 0.911 | not applied (n < 1000) | 0.987 | +2.0 | +0.2 | 0.0536 | 0.0547 |
| Avg. daily time < 70 (%) | 408 | +0.112 [-0.389, +0.614] | 0.04249 | 0.44 | 0.660 | not applied (n < 1000) | 0.987 | +1.8 | +0.0 | 0.0542 | 0.0547 |
| Time 54-250, pooled (%) | 408 | -0.184 [-0.618, +0.250] | -0.153 | -0.83 | 0.406 | not applied (n < 1000) | 0.987 | +1.4 | -0.3 | 0.0529 | 0.0547 |
| Avg. daily time 54-250 (%) | 408 | -0.326 [-0.799, +0.147] | -0.3059 | -1.35 | 0.177 | not applied (n < 1000) | 0.967 | +0.2 | -1.5 | 0.0551 | 0.0547 |
| Time 181-250, pooled (%) | 408 | +0.599 [-0.030, +1.228] | 0.1439 | 1.87 | 0.062 | not applied (n < 1000) | 0.637 | -4.0 | -5.8 | 0.0655 | 0.0547 |
| Avg. daily time 181-250 (%) | 408 | +0.609 [-0.038, +1.255] | 0.1402 | 1.84 | 0.065 | not applied (n < 1000) | 0.637 | -4.2 | -6.0 | 0.0651 | 0.0547 |
| Time > 180, pooled (%) | 408 | +0.594 [-0.046, +1.235] | 0.1262 | 1.82 | 0.069 | not applied (n < 1000) | 0.659 | -3.9 | -5.7 | 0.0648 | 0.0547 |
| Avg. daily time > 180 (%) | 408 | +0.606 [-0.073, +1.285] | 0.1229 | 1.75 | 0.080 | not applied (n < 1000) | 0.719 | -4.1 | -5.9 | 0.0640 | 0.0547 |
| Nocturnal time > 180 (%) | 408 | +0.813 [+0.323, +1.303] | 0.1784 | 3.25 | 0.001** | not applied (n < 1000) | 0.179 | -9.4 | -11.2 | 0.0780 | 0.0547 |
| Any reading > 250 during wear (0/1) | 408 | +0.202 [-0.294, +0.698] | 0.5488 | 0.80 | 0.424 | not applied (n < 1000) | 0.987 | +1.3 | -0.5 | 0.0554 | 0.0547 |
| Time > 250, pooled (%) | 408 | +0.430 [-0.321, +1.181] | 0.6131 | 1.12 | 0.261 | not applied (n < 1000) | 0.987 | -1.1 | -2.9 | 0.0514 | 0.0547 |
| Avg. daily time > 250 (%) | 408 | +0.448 [-0.501, +1.397] | 0.5937 | 0.93 | 0.355 | not applied (n < 1000) | 0.987 | -1.4 | -3.1 | 0.0437 | 0.0547 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 408; events = 81; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 408 | OR 1.255 [0.978, 1.610] | 0.5325 | 1.79 | 0.074 | not applied (n < 1000) | 0.678 | -1.3 | +0.0 | 0.6177 | 0.6085 |
| Mean glucose (mg/dL) | 408 | OR 1.190 [0.929, 1.526] | 0.01245 | 1.38 | 0.169 | not applied (n < 1000) | 0.967 | +0.2 | +1.5 | 0.6096 | 0.6085 |
| GMI (%) | 408 | OR 1.190 [0.929, 1.526] | 0.5204 | 1.38 | 0.169 | not applied (n < 1000) | 0.967 | +0.2 | +1.5 | 0.6096 | 0.6085 |
| Nocturnal mean 00-06h (mg/dL) | 408 | OR 1.199 [0.936, 1.535] | 0.0118 | 1.44 | 0.151 | not applied (n < 1000) | 0.958 | -0.0 | +1.3 | 0.6109 | 0.6085 |
| Glucose SD, pooled (mg/dL) | 408 | OR 1.290 [1.006, 1.653] | 0.03953 | 2.01 | 0.045* | not applied (n < 1000) | 0.622 | -1.9 | -0.6 | 0.6170 | 0.6085 |
| Avg. daily SD (mg/dL) | 408 | OR 1.293 [1.008, 1.659] | 0.04347 | 2.02 | 0.043* | not applied (n < 1000) | 0.622 | -1.9 | -0.6 | 0.6188 | 0.6085 |
| CV (%) | 408 | OR 1.179 [0.918, 1.515] | 0.03581 | 1.29 | 0.197 | not applied (n < 1000) | 0.967 | +0.4 | +1.7 | 0.6119 | 0.6085 |
| Mean / SD ratio | 408 | OR 0.810 [0.622, 1.056] | -0.1876 | -1.56 | 0.120 | not applied (n < 1000) | 0.882 | -0.4 | +0.9 | 0.6161 | 0.6085 |
| Avg. daily mean / SD | 408 | OR 0.832 [0.635, 1.089] | -0.1311 | -1.34 | 0.180 | not applied (n < 1000) | 0.967 | +0.2 | +1.5 | 0.6099 | 0.6085 |
| MAG (mg/dL/h) | 408 | OR 0.959 [0.738, 1.247] | -0.00515 | -0.31 | 0.756 | not applied (n < 1000) | 0.987 | +1.9 | +3.2 | 0.6041 | 0.6085 |
| Avg. daily range (mg/dL) | 408 | OR 1.175 [0.913, 1.513] | 0.00607 | 1.26 | 0.209 | not applied (n < 1000) | 0.968 | +0.5 | +1.8 | 0.6072 | 0.6085 |
| SD of daily means (mg/dL) | 408 | OR 1.134 [0.890, 1.445] | 0.03311 | 1.01 | 0.310 | not applied (n < 1000) | 0.987 | +1.0 | +2.3 | 0.6045 | 0.6085 |
| Time in range 70-180, pooled (%) | 408 | OR 0.720 [0.572, 0.906] | -0.06385 | -2.80 | 0.005** | not applied (n < 1000) | 0.267 | -6.0 | -4.7 | 0.6329 | 0.6085 |
| Avg. daily time in range 70-180 (%) | 408 | OR 0.725 [0.577, 0.912] | -0.06026 | -2.74 | 0.006** | not applied (n < 1000) | 0.283 | -5.7 | -4.4 | 0.6319 | 0.6085 |
| Time < 54, pooled (%) | 408 | OR 0.886 [0.598, 1.312] | -0.1292 | -0.60 | 0.546 | not applied (n < 1000) | 0.987 | +1.6 | +2.9 | 0.6084 | 0.6085 |
| Avg. daily time < 54 (%) | 408 | OR 0.811 [0.525, 1.252] | -0.2934 | -0.95 | 0.344 | not applied (n < 1000) | 0.987 | +0.9 | +2.2 | 0.6132 | 0.6085 |
| Time 54-69, pooled (%) | 408 | OR 1.002 [0.782, 1.285] | 0.001082 | 0.02 | 0.986 | not applied (n < 1000) | 0.996 | +2.0 | +3.3 | 0.6073 | 0.6085 |
| Avg. daily time 54-69 (%) | 408 | OR 0.993 [0.773, 1.274] | -0.00329 | -0.06 | 0.955 | not applied (n < 1000) | 0.987 | +2.0 | +3.3 | 0.6073 | 0.6085 |
| Time < 70, pooled (%) | 408 | OR 0.979 [0.753, 1.274] | -0.007843 | -0.16 | 0.875 | not applied (n < 1000) | 0.987 | +2.0 | +3.3 | 0.6075 | 0.6085 |
| Avg. daily time < 70 (%) | 408 | OR 0.966 [0.743, 1.257] | -0.01302 | -0.26 | 0.797 | not applied (n < 1000) | 0.987 | +1.9 | +3.2 | 0.6080 | 0.6085 |
| Time 54-250, pooled (%) | 408 | OR 0.846 [0.675, 1.060] | -0.139 | -1.45 | 0.146 | not applied (n < 1000) | 0.943 | +0.2 | +1.5 | 0.6112 | 0.6085 |
| Avg. daily time 54-250 (%) | 408 | OR 0.835 [0.668, 1.043] | -0.1695 | -1.59 | 0.112 | not applied (n < 1000) | 0.856 | -0.2 | +1.1 | 0.6112 | 0.6085 |
| Time 181-250, pooled (%) | 408 | OR 1.427 [1.128, 1.805] | 0.08535 | 2.96 | 0.003** | not applied (n < 1000) | 0.235 | -7.5 | -6.2 | 0.6272 | 0.6085 |
| Avg. daily time 181-250 (%) | 408 | OR 1.427 [1.125, 1.809] | 0.08192 | 2.93 | 0.003** | not applied (n < 1000) | 0.235 | -7.5 | -6.2 | 0.6288 | 0.6085 |
| Time > 180, pooled (%) | 408 | OR 1.432 [1.127, 1.820] | 0.07626 | 2.93 | 0.003** | not applied (n < 1000) | 0.235 | -7.6 | -6.3 | 0.6291 | 0.6085 |
| Avg. daily time > 180 (%) | 408 | OR 1.433 [1.121, 1.831] | 0.07304 | 2.88 | 0.004** | not applied (n < 1000) | 0.241 | -7.6 | -6.3 | 0.6297 | 0.6085 |
| Nocturnal time > 180 (%) | 408 | OR 1.567 [1.192, 2.059] | 0.09856 | 3.22 | 0.001** | not applied (n < 1000) | 0.179 | -11.7 | -10.4 | 0.6339 | 0.6085 |
| Any reading > 250 during wear (0/1) | 408 | OR 1.260 [0.990, 1.604] | 0.6272 | 1.88 | 0.060 | not applied (n < 1000) | 0.637 | -1.4 | -0.0 | 0.6123 | 0.6085 |
| Time > 250, pooled (%) | 408 | OR 1.344 [1.048, 1.723] | 0.4209 | 2.33 | 0.020* | not applied (n < 1000) | 0.531 | -4.6 | -3.3 | 0.6234 | 0.6085 |
| Avg. daily time > 250 (%) | 408 | OR 1.339 [1.031, 1.740] | 0.3868 | 2.19 | 0.029* | not applied (n < 1000) | 0.608 | -4.3 | -3.0 | 0.6254 | 0.6085 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 400; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 400 | +0.016 [-0.087, +0.118] | 0.03675 | 0.30 | 0.765 | not applied (n < 1000) | 0.987 | +1.9 | +0.0 | 0.0707 | 0.0807 |
| Mean glucose (mg/dL) | 400 | -0.116 [-0.213, -0.018] | -0.008259 | -2.32 | 0.020* | not applied (n < 1000) | 0.531 | -3.9 | -5.8 | 0.0859 | 0.0807 |
| GMI (%) | 400 | -0.116 [-0.213, -0.018] | -0.3453 | -2.32 | 0.020* | not applied (n < 1000) | 0.531 | -3.9 | -5.8 | 0.0859 | 0.0807 |
| Nocturnal mean 00-06h (mg/dL) | 400 | -0.082 [-0.179, +0.014] | -0.005352 | -1.67 | 0.095 | not applied (n < 1000) | 0.769 | -1.0 | -2.9 | 0.0798 | 0.0807 |
| Glucose SD, pooled (mg/dL) | 400 | -0.063 [-0.157, +0.030] | -0.009768 | -1.33 | 0.185 | not applied (n < 1000) | 0.967 | +0.2 | -1.7 | 0.0800 | 0.0807 |
| Avg. daily SD (mg/dL) | 400 | -0.060 [-0.161, +0.041] | -0.01001 | -1.16 | 0.248 | not applied (n < 1000) | 0.987 | +0.4 | -1.5 | 0.0804 | 0.0807 |
| CV (%) | 400 | -0.022 [-0.112, +0.067] | -0.004809 | -0.49 | 0.626 | not applied (n < 1000) | 0.987 | +1.8 | -0.1 | 0.0769 | 0.0807 |
| Mean / SD ratio | 400 | +0.008 [-0.083, +0.100] | 0.007492 | 0.18 | 0.857 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.0770 | 0.0807 |
| Avg. daily mean / SD | 400 | -0.006 [-0.097, +0.085] | -0.004188 | -0.13 | 0.898 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.0764 | 0.0807 |
| MAG (mg/dL/h) | 400 | +0.041 [-0.051, +0.133] | 0.005011 | 0.87 | 0.386 | not applied (n < 1000) | 0.987 | +1.2 | -0.7 | 0.0739 | 0.0807 |
| Avg. daily range (mg/dL) | 400 | -0.041 [-0.147, +0.065] | -0.001538 | -0.76 | 0.447 | not applied (n < 1000) | 0.987 | +1.2 | -0.7 | 0.0790 | 0.0807 |
| SD of daily means (mg/dL) | 400 | -0.050 [-0.125, +0.026] | -0.01307 | -1.29 | 0.197 | not applied (n < 1000) | 0.967 | +0.9 | -1.0 | 0.0783 | 0.0807 |
| Time in range 70-180, pooled (%) | 400 | +0.084 [+0.008, +0.160] | 0.01628 | 2.17 | 0.030* | not applied (n < 1000) | 0.608 | -1.2 | -3.1 | 0.0833 | 0.0807 |
| Avg. daily time in range 70-180 (%) | 400 | +0.081 [+0.002, +0.161] | 0.01512 | 2.00 | 0.046* | not applied (n < 1000) | 0.622 | -1.0 | -2.9 | 0.0837 | 0.0807 |
| Time < 54, pooled (%) | 400 | -0.022 [-0.081, +0.037] | -0.02353 | -0.74 | 0.459 | not applied (n < 1000) | 0.987 | +1.8 | -0.1 | 0.0788 | 0.0807 |
| Avg. daily time < 54 (%) | 400 | -0.020 [-0.082, +0.041] | -0.02844 | -0.66 | 0.512 | not applied (n < 1000) | 0.987 | +1.8 | -0.1 | 0.0785 | 0.0807 |
| Time 54-69, pooled (%) | 400 | -0.009 [-0.094, +0.077] | -0.004087 | -0.20 | 0.841 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.0754 | 0.0807 |
| Avg. daily time 54-69 (%) | 400 | -0.006 [-0.096, +0.084] | -0.002651 | -0.13 | 0.899 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.0753 | 0.0807 |
| Time < 70, pooled (%) | 400 | -0.015 [-0.094, +0.064] | -0.005469 | -0.37 | 0.714 | not applied (n < 1000) | 0.987 | +1.9 | +0.0 | 0.0765 | 0.0807 |
| Avg. daily time < 70 (%) | 400 | -0.010 [-0.096, +0.075] | -0.003916 | -0.24 | 0.811 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.0759 | 0.0807 |
| Time 54-250, pooled (%) | 400 | +0.047 [-0.026, +0.121] | 0.03874 | 1.25 | 0.210 | not applied (n < 1000) | 0.968 | +1.0 | -0.9 | 0.0775 | 0.0807 |
| Avg. daily time 54-250 (%) | 400 | +0.045 [-0.024, +0.114] | 0.04211 | 1.29 | 0.198 | not applied (n < 1000) | 0.967 | +1.1 | -0.8 | 0.0791 | 0.0807 |
| Time 181-250, pooled (%) | 400 | -0.088 [-0.170, -0.007] | -0.02106 | -2.12 | 0.034* | not applied (n < 1000) | 0.622 | -1.5 | -3.4 | 0.0831 | 0.0807 |
| Avg. daily time 181-250 (%) | 400 | -0.088 [-0.172, -0.003] | -0.02007 | -2.03 | 0.042* | not applied (n < 1000) | 0.622 | -1.4 | -3.3 | 0.0834 | 0.0807 |
| Time > 180, pooled (%) | 400 | -0.086 [-0.170, -0.002] | -0.01805 | -2.00 | 0.046* | not applied (n < 1000) | 0.622 | -1.3 | -3.2 | 0.0824 | 0.0807 |
| Avg. daily time > 180 (%) | 400 | -0.084 [-0.173, +0.005] | -0.01694 | -1.85 | 0.064 | not applied (n < 1000) | 0.637 | -1.1 | -3.0 | 0.0826 | 0.0807 |
| Nocturnal time > 180 (%) | 400 | -0.070 [-0.144, +0.003] | -0.01526 | -1.87 | 0.061 | not applied (n < 1000) | 0.637 | -0.2 | -2.1 | 0.0815 | 0.0807 |
| Any reading > 250 during wear (0/1) | 400 | -0.048 [-0.138, +0.041] | -0.132 | -1.06 | 0.291 | not applied (n < 1000) | 0.987 | +0.9 | -1.0 | 0.0786 | 0.0807 |
| Time > 250, pooled (%) | 400 | -0.051 [-0.142, +0.040] | -0.07202 | -1.10 | 0.270 | not applied (n < 1000) | 0.987 | +0.8 | -1.1 | 0.0789 | 0.0807 |
| Avg. daily time > 250 (%) | 400 | -0.044 [-0.141, +0.052] | -0.05816 | -0.90 | 0.369 | not applied (n < 1000) | 0.987 | +1.1 | -0.8 | 0.0786 | 0.0807 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 400; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 400 | -0.043 [-0.279, +0.192] | -0.1023 | -0.36 | 0.717 | not applied (n < 1000) | 0.987 | +1.8 | +0.0 | 0.2109 | 0.2134 |
| Mean glucose (mg/dL) | 400 | -0.099 [-0.303, +0.105] | -0.007078 | -0.95 | 0.340 | not applied (n < 1000) | 0.987 | +1.0 | -0.8 | 0.2110 | 0.2134 |
| GMI (%) | 400 | -0.099 [-0.303, +0.105] | -0.2959 | -0.95 | 0.340 | not applied (n < 1000) | 0.987 | +1.0 | -0.8 | 0.2110 | 0.2134 |
| Nocturnal mean 00-06h (mg/dL) | 400 | -0.162 [-0.363, +0.039] | -0.01051 | -1.58 | 0.114 | not applied (n < 1000) | 0.859 | -0.6 | -2.4 | 0.2118 | 0.2134 |
| Glucose SD, pooled (mg/dL) | 400 | -0.018 [-0.239, +0.203] | -0.002829 | -0.16 | 0.871 | not applied (n < 1000) | 0.987 | +2.0 | +0.1 | 0.2063 | 0.2134 |
| Avg. daily SD (mg/dL) | 400 | -0.033 [-0.254, +0.189] | -0.005476 | -0.29 | 0.773 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.2063 | 0.2134 |
| CV (%) | 400 | +0.045 [-0.165, +0.255] | 0.009643 | 0.42 | 0.676 | not applied (n < 1000) | 0.987 | +1.8 | -0.0 | 0.2077 | 0.2134 |
| Mean / SD ratio | 400 | +0.007 [-0.195, +0.208] | 0.005851 | 0.06 | 0.949 | not applied (n < 1000) | 0.987 | +2.0 | +0.2 | 0.2092 | 0.2134 |
| Avg. daily mean / SD | 400 | +0.049 [-0.170, +0.267] | 0.03425 | 0.44 | 0.663 | not applied (n < 1000) | 0.987 | +1.8 | -0.1 | 0.2091 | 0.2134 |
| MAG (mg/dL/h) | 400 | +0.053 [-0.148, +0.254] | 0.00656 | 0.52 | 0.603 | not applied (n < 1000) | 0.987 | +1.7 | -0.1 | 0.2071 | 0.2134 |
| Avg. daily range (mg/dL) | 400 | -0.044 [-0.257, +0.170] | -0.001626 | -0.40 | 0.689 | not applied (n < 1000) | 0.987 | +1.8 | -0.0 | 0.2077 | 0.2134 |
| SD of daily means (mg/dL) | 400 | -0.055 [-0.280, +0.169] | -0.01457 | -0.48 | 0.628 | not applied (n < 1000) | 0.987 | +1.7 | -0.1 | 0.2103 | 0.2134 |
| Time in range 70-180, pooled (%) | 400 | -0.048 [-0.251, +0.155] | -0.009254 | -0.46 | 0.644 | not applied (n < 1000) | 0.987 | +1.8 | -0.1 | 0.2080 | 0.2134 |
| Avg. daily time in range 70-180 (%) | 400 | -0.040 [-0.239, +0.158] | -0.007483 | -0.40 | 0.692 | not applied (n < 1000) | 0.987 | +1.8 | +0.0 | 0.2084 | 0.2134 |
| Time < 54, pooled (%) | 400 | +0.222 [+0.041, +0.403] | 0.2347 | 2.40 | 0.016* | not applied (n < 1000) | 0.531 | -3.0 | -4.8 | 0.2197 | 0.2134 |
| Avg. daily time < 54 (%) | 400 | +0.198 [-0.041, +0.436] | 0.2746 | 1.63 | 0.104 | not applied (n < 1000) | 0.824 | -1.9 | -3.7 | 0.2139 | 0.2134 |
| Time 54-69, pooled (%) | 400 | +0.143 [-0.005, +0.292] | 0.067 | 1.89 | 0.059 | not applied (n < 1000) | 0.637 | -0.1 | -1.9 | 0.2147 | 0.2134 |
| Avg. daily time 54-69 (%) | 400 | +0.159 [+0.005, +0.313] | 0.07236 | 2.02 | 0.043* | not applied (n < 1000) | 0.622 | -0.5 | -2.3 | 0.2156 | 0.2134 |
| Time < 70, pooled (%) | 400 | +0.193 [+0.018, +0.367] | 0.07108 | 2.16 | 0.030* | not applied (n < 1000) | 0.608 | -1.7 | -3.5 | 0.2172 | 0.2134 |
| Avg. daily time < 70 (%) | 400 | +0.186 [+0.010, +0.362] | 0.07004 | 2.07 | 0.039* | not applied (n < 1000) | 0.622 | -1.4 | -3.3 | 0.2163 | 0.2134 |
| Time 54-250, pooled (%) | 400 | -0.157 [-0.406, +0.093] | -0.1289 | -1.23 | 0.219 | not applied (n < 1000) | 0.987 | -0.5 | -2.3 | 0.2089 | 0.2134 |
| Avg. daily time 54-250 (%) | 400 | -0.114 [-0.366, +0.138] | -0.1057 | -0.88 | 0.377 | not applied (n < 1000) | 0.987 | +0.7 | -1.1 | 0.2042 | 0.2134 |
| Time 181-250, pooled (%) | 400 | -0.060 [-0.270, +0.150] | -0.01428 | -0.56 | 0.576 | not applied (n < 1000) | 0.987 | +1.6 | -0.2 | 0.2102 | 0.2134 |
| Avg. daily time 181-250 (%) | 400 | -0.059 [-0.270, +0.152] | -0.01344 | -0.55 | 0.585 | not applied (n < 1000) | 0.987 | +1.7 | -0.2 | 0.2103 | 0.2134 |
| Time > 180, pooled (%) | 400 | -0.057 [-0.272, +0.158] | -0.01204 | -0.52 | 0.602 | not applied (n < 1000) | 0.987 | +1.7 | -0.1 | 0.2099 | 0.2134 |
| Avg. daily time > 180 (%) | 400 | -0.056 [-0.275, +0.163] | -0.0112 | -0.50 | 0.619 | not applied (n < 1000) | 0.987 | +1.7 | -0.1 | 0.2098 | 0.2134 |
| Nocturnal time > 180 (%) | 400 | -0.106 [-0.326, +0.113] | -0.02314 | -0.95 | 0.342 | not applied (n < 1000) | 0.987 | +0.9 | -1.0 | 0.2107 | 0.2134 |
| Any reading > 250 during wear (0/1) | 400 | -0.029 [-0.244, +0.187] | -0.07806 | -0.26 | 0.794 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.2072 | 0.2134 |
| Time > 250, pooled (%) | 400 | -0.028 [-0.268, +0.212] | -0.03978 | -0.23 | 0.818 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.2073 | 0.2134 |
| Avg. daily time > 250 (%) | 400 | -0.025 [-0.292, +0.242] | -0.0332 | -0.19 | 0.853 | not applied (n < 1000) | 0.987 | +1.9 | +0.1 | 0.2058 | 0.2134 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 400; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 400 | +0.625 [-0.011, +1.261] | 1.471 | 1.93 | 0.054 | not applied (n < 1000) | 0.637 | -2.0 | +0.0 | 0.1995 | 0.1981 |
| Mean glucose (mg/dL) | 400 | -0.089 [-0.730, +0.553] | -0.006336 | -0.27 | 0.786 | not applied (n < 1000) | 0.987 | +1.9 | +3.9 | 0.1921 | 0.1981 |
| GMI (%) | 400 | -0.089 [-0.730, +0.553] | -0.2649 | -0.27 | 0.786 | not applied (n < 1000) | 0.987 | +1.9 | +3.9 | 0.1921 | 0.1981 |
| Nocturnal mean 00-06h (mg/dL) | 400 | +0.049 [-0.594, +0.692] | 0.003185 | 0.15 | 0.881 | not applied (n < 1000) | 0.987 | +2.0 | +4.0 | 0.1933 | 0.1981 |
| Glucose SD, pooled (mg/dL) | 400 | -0.487 [-1.127, +0.153] | -0.0753 | -1.49 | 0.136 | not applied (n < 1000) | 0.943 | -0.6 | +1.4 | 0.1972 | 0.1981 |
| Avg. daily SD (mg/dL) | 400 | -0.522 [-1.162, +0.119] | -0.08775 | -1.60 | 0.110 | not applied (n < 1000) | 0.856 | -0.9 | +1.1 | 0.1972 | 0.1981 |
| CV (%) | 400 | -0.547 [-1.182, +0.088] | -0.118 | -1.69 | 0.091 | not applied (n < 1000) | 0.753 | -1.3 | +0.7 | 0.2004 | 0.1981 |
| Mean / SD ratio | 400 | +0.636 [+0.032, +1.241] | 0.5653 | 2.06 | 0.039* | not applied (n < 1000) | 0.622 | -2.5 | -0.5 | 0.2003 | 0.1981 |
| Avg. daily mean / SD | 400 | +0.615 [-0.031, +1.261] | 0.4342 | 1.87 | 0.062 | not applied (n < 1000) | 0.637 | -2.2 | -0.1 | 0.1996 | 0.1981 |
| MAG (mg/dL/h) | 400 | -0.088 [-0.674, +0.498] | -0.01082 | -0.29 | 0.769 | not applied (n < 1000) | 0.987 | +1.9 | +3.9 | 0.1930 | 0.1981 |
| Avg. daily range (mg/dL) | 400 | -0.370 [-0.982, +0.242] | -0.01382 | -1.19 | 0.236 | not applied (n < 1000) | 0.987 | +0.5 | +2.5 | 0.1962 | 0.1981 |
| SD of daily means (mg/dL) | 400 | -0.093 [-0.776, +0.589] | -0.02452 | -0.27 | 0.789 | not applied (n < 1000) | 0.987 | +1.9 | +3.9 | 0.1954 | 0.1981 |
| Time in range 70-180, pooled (%) | 400 | +0.339 [-0.350, +1.027] | 0.06537 | 0.96 | 0.335 | not applied (n < 1000) | 0.987 | +0.7 | +2.7 | 0.1906 | 0.1981 |
| Avg. daily time in range 70-180 (%) | 400 | +0.312 [-0.369, +0.992] | 0.0581 | 0.90 | 0.369 | not applied (n < 1000) | 0.987 | +0.9 | +2.9 | 0.1902 | 0.1981 |
| Time < 54, pooled (%) | 400 | -0.401 [-0.759, -0.044] | -0.4244 | -2.20 | 0.028* | not applied (n < 1000) | 0.608 | +0.2 | +2.2 | 0.1985 | 0.1981 |
| Avg. daily time < 54 (%) | 400 | -0.476 [-0.836, -0.116] | -0.6613 | -2.59 | 0.010** | not applied (n < 1000) | 0.403 | -0.5 | +1.5 | 0.2023 | 0.1981 |
| Time 54-69, pooled (%) | 400 | -0.260 [-0.758, +0.237] | -0.1218 | -1.03 | 0.305 | not applied (n < 1000) | 0.987 | +1.2 | +3.3 | 0.1971 | 0.1981 |
| Avg. daily time 54-69 (%) | 400 | -0.233 [-0.734, +0.268] | -0.1062 | -0.91 | 0.362 | not applied (n < 1000) | 0.987 | +1.4 | +3.4 | 0.1961 | 0.1981 |
| Time < 70, pooled (%) | 400 | -0.349 [-0.858, +0.160] | -0.1289 | -1.34 | 0.179 | not applied (n < 1000) | 0.967 | +0.7 | +2.7 | 0.1978 | 0.1981 |
| Avg. daily time < 70 (%) | 400 | -0.324 [-0.847, +0.200] | -0.1218 | -1.21 | 0.226 | not applied (n < 1000) | 0.987 | +0.9 | +2.9 | 0.1976 | 0.1981 |
| Time 54-250, pooled (%) | 400 | +0.279 [-0.311, +0.869] | 0.2299 | 0.93 | 0.354 | not applied (n < 1000) | 0.987 | +1.1 | +3.2 | 0.1916 | 0.1981 |
| Avg. daily time 54-250 (%) | 400 | +0.245 [-0.384, +0.874] | 0.2279 | 0.76 | 0.446 | not applied (n < 1000) | 0.987 | +1.3 | +3.4 | 0.1910 | 0.1981 |
| Time 181-250, pooled (%) | 400 | -0.211 [-0.923, +0.501] | -0.0503 | -0.58 | 0.562 | not applied (n < 1000) | 0.987 | +1.5 | +3.5 | 0.1891 | 0.1981 |
| Avg. daily time 181-250 (%) | 400 | -0.212 [-0.916, +0.492] | -0.04855 | -0.59 | 0.555 | not applied (n < 1000) | 0.987 | +1.5 | +3.5 | 0.1888 | 0.1981 |
| Time > 180, pooled (%) | 400 | -0.177 [-0.903, +0.548] | -0.03739 | -0.48 | 0.632 | not applied (n < 1000) | 0.987 | +1.7 | +3.7 | 0.1886 | 0.1981 |
| Avg. daily time > 180 (%) | 400 | -0.171 [-0.890, +0.548] | -0.03441 | -0.47 | 0.641 | not applied (n < 1000) | 0.987 | +1.7 | +3.7 | 0.1883 | 0.1981 |
| Nocturnal time > 180 (%) | 400 | -0.165 [-1.010, +0.680] | -0.03586 | -0.38 | 0.702 | not applied (n < 1000) | 0.987 | +1.7 | +3.7 | 0.1826 | 0.1981 |
| Any reading > 250 during wear (0/1) | 400 | -0.191 [-0.815, +0.433] | -0.5203 | -0.60 | 0.548 | not applied (n < 1000) | 0.987 | +1.6 | +3.6 | 0.1956 | 0.1981 |
| Time > 250, pooled (%) | 400 | +0.058 [-0.749, +0.864] | 0.08149 | 0.14 | 0.888 | not applied (n < 1000) | 0.987 | +2.0 | +4.0 | 0.1906 | 0.1981 |
| Avg. daily time > 250 (%) | 400 | +0.101 [-0.819, +1.022] | 0.1328 | 0.22 | 0.829 | not applied (n < 1000) | 0.987 | +1.9 | +3.9 | 0.1898 | 0.1981 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 400; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 400 | +0.468 [-1.119, +2.056] | 1.102 | 0.58 | 0.563 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0605 | -0.0551 |
| Mean glucose (mg/dL) | 400 | -0.422 [-2.102, +1.257] | -0.03013 | -0.49 | 0.622 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0651 | -0.0551 |
| GMI (%) | 400 | -0.422 [-2.102, +1.257] | -1.26 | -0.49 | 0.622 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0651 | -0.0551 |
| Nocturnal mean 00-06h (mg/dL) | 400 | -0.089 [-1.666, +1.489] | -0.005759 | -0.11 | 0.912 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0672 | -0.0551 |
| Glucose SD, pooled (mg/dL) | 400 | -0.180 [-1.910, +1.549] | -0.02788 | -0.20 | 0.838 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0584 | -0.0551 |
| Avg. daily SD (mg/dL) | 400 | -0.368 [-2.193, +1.456] | -0.06197 | -0.40 | 0.692 | not applied (n < 1000) | 0.987 | +1.8 | +0.1 | -0.0594 | -0.0551 |
| CV (%) | 400 | -0.214 [-1.814, +1.386] | -0.04621 | -0.26 | 0.793 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0574 | -0.0551 |
| Mean / SD ratio | 400 | +0.109 [-1.449, +1.668] | 0.09711 | 0.14 | 0.891 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0575 | -0.0551 |
| Avg. daily mean / SD | 400 | +0.327 [-1.313, +1.968] | 0.2311 | 0.39 | 0.696 | not applied (n < 1000) | 0.987 | +1.8 | +0.2 | -0.0587 | -0.0551 |
| MAG (mg/dL/h) | 400 | +0.179 [-1.451, +1.810] | 0.02205 | 0.22 | 0.830 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0588 | -0.0551 |
| Avg. daily range (mg/dL) | 400 | -0.480 [-2.392, +1.432] | -0.0179 | -0.49 | 0.623 | not applied (n < 1000) | 0.987 | +1.6 | -0.0 | -0.0599 | -0.0551 |
| SD of daily means (mg/dL) | 400 | +0.153 [-1.333, +1.639] | 0.04025 | 0.20 | 0.840 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0561 | -0.0551 |
| Time in range 70-180, pooled (%) | 400 | -0.229 [-1.987, +1.529] | -0.04418 | -0.26 | 0.799 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0584 | -0.0551 |
| Avg. daily time in range 70-180 (%) | 400 | -0.194 [-2.036, +1.647] | -0.03623 | -0.21 | 0.836 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0584 | -0.0551 |
| Time < 54, pooled (%) | 400 | +0.145 [-1.577, +1.867] | 0.1534 | 0.17 | 0.869 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0596 | -0.0551 |
| Avg. daily time < 54 (%) | 400 | +0.069 [-1.618, +1.756] | 0.09529 | 0.08 | 0.937 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0614 | -0.0551 |
| Time 54-69, pooled (%) | 400 | +0.004 [-1.583, +1.592] | 0.00197 | 0.01 | 0.996 | not applied (n < 1000) | 0.996 | +2.0 | +0.3 | -0.0624 | -0.0551 |
| Avg. daily time 54-69 (%) | 400 | -0.073 [-1.738, +1.593] | -0.03308 | -0.09 | 0.932 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0632 | -0.0551 |
| Time < 70, pooled (%) | 400 | +0.054 [-1.516, +1.625] | 0.02011 | 0.07 | 0.946 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0625 | -0.0551 |
| Avg. daily time < 70 (%) | 400 | -0.042 [-1.713, +1.629] | -0.01579 | -0.05 | 0.961 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0637 | -0.0551 |
| Time 54-250, pooled (%) | 400 | -0.241 [-1.897, +1.415] | -0.1985 | -0.29 | 0.775 | not applied (n < 1000) | 0.987 | +1.9 | +0.2 | -0.0565 | -0.0551 |
| Avg. daily time 54-250 (%) | 400 | -0.301 [-2.057, +1.455] | -0.2802 | -0.34 | 0.737 | not applied (n < 1000) | 0.987 | +1.8 | +0.2 | -0.0559 | -0.0551 |
| Time 181-250, pooled (%) | 400 | +0.216 [-1.667, +2.099] | 0.0516 | 0.23 | 0.822 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0661 | -0.0551 |
| Avg. daily time 181-250 (%) | 400 | +0.207 [-1.715, +2.128] | 0.04725 | 0.21 | 0.833 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0660 | -0.0551 |
| Time > 180, pooled (%) | 400 | +0.224 [-1.707, +2.155] | 0.04725 | 0.23 | 0.820 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0654 | -0.0551 |
| Avg. daily time > 180 (%) | 400 | +0.237 [-1.751, +2.226] | 0.04784 | 0.23 | 0.815 | not applied (n < 1000) | 0.987 | +1.9 | +0.2 | -0.0657 | -0.0551 |
| Nocturnal time > 180 (%) | 400 | +0.139 [-1.725, +2.002] | 0.03016 | 0.15 | 0.884 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0717 | -0.0551 |
| Any reading > 250 during wear (0/1) | 400 | +0.345 [-1.280, +1.970] | 0.9403 | 0.42 | 0.677 | not applied (n < 1000) | 0.987 | +1.8 | +0.1 | -0.0590 | -0.0551 |
| Time > 250, pooled (%) | 400 | +0.220 [-2.027, +2.467] | 0.3103 | 0.19 | 0.848 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0624 | -0.0551 |
| Avg. daily time > 250 (%) | 400 | +0.358 [-1.981, +2.697] | 0.4698 | 0.30 | 0.764 | not applied (n < 1000) | 0.987 | +1.8 | +0.1 | -0.0622 | -0.0551 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 374; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 374 | +251.559 [-135.415, +638.533] | 577.3 | 1.27 | 0.203 | not applied (n < 1000) | 0.967 | +0.5 | +0.0 | 0.0499 | 0.0549 |
| Mean glucose (mg/dL) | 374 | -49.064 [-438.807, +340.680] | -3.448 | -0.25 | 0.805 | not applied (n < 1000) | 0.987 | +1.9 | +1.5 | 0.0510 | 0.0549 |
| GMI (%) | 374 | -49.064 [-438.807, +340.680] | -144.2 | -0.25 | 0.805 | not applied (n < 1000) | 0.987 | +1.9 | +1.5 | 0.0510 | 0.0549 |
| Nocturnal mean 00-06h (mg/dL) | 374 | +84.399 [-322.959, +491.757] | 5.484 | 0.41 | 0.685 | not applied (n < 1000) | 0.987 | +1.8 | +1.3 | 0.0492 | 0.0549 |
| Glucose SD, pooled (mg/dL) | 374 | -185.948 [-607.060, +235.163] | -29.5 | -0.87 | 0.387 | not applied (n < 1000) | 0.987 | +1.1 | +0.6 | 0.0530 | 0.0549 |
| Avg. daily SD (mg/dL) | 374 | -179.514 [-619.668, +260.639] | -30.47 | -0.80 | 0.424 | not applied (n < 1000) | 0.987 | +1.2 | +0.7 | 0.0513 | 0.0549 |
| CV (%) | 374 | -200.739 [-609.774, +208.297] | -44.4 | -0.96 | 0.336 | not applied (n < 1000) | 0.987 | +1.0 | +0.5 | 0.0545 | 0.0549 |
| Mean / SD ratio | 374 | +57.365 [-342.089, +456.819] | 51.38 | 0.28 | 0.778 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0512 | 0.0549 |
| Avg. daily mean / SD | 374 | -46.096 [-453.834, +361.642] | -32.76 | -0.22 | 0.825 | not applied (n < 1000) | 0.987 | +1.9 | +1.5 | 0.0483 | 0.0549 |
| MAG (mg/dL/h) | 374 | +225.559 [-170.224, +621.342] | 28.37 | 1.12 | 0.264 | not applied (n < 1000) | 0.987 | +0.7 | +0.2 | 0.0529 | 0.0549 |
| Avg. daily range (mg/dL) | 374 | -102.830 [-534.429, +328.769] | -3.886 | -0.47 | 0.641 | not applied (n < 1000) | 0.987 | +1.7 | +1.2 | 0.0485 | 0.0549 |
| SD of daily means (mg/dL) | 374 | -67.470 [-474.151, +339.211] | -18.98 | -0.33 | 0.745 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0513 | 0.0549 |
| Time in range 70-180, pooled (%) | 374 | +167.652 [-136.177, +471.482] | 31.91 | 1.08 | 0.279 | not applied (n < 1000) | 0.987 | +1.3 | +0.8 | 0.0543 | 0.0549 |
| Avg. daily time in range 70-180 (%) | 374 | +147.347 [-161.320, +456.014] | 27.03 | 0.94 | 0.349 | not applied (n < 1000) | 0.987 | +1.4 | +1.0 | 0.0536 | 0.0549 |
| Time < 54, pooled (%) | 374 | -119.304 [-403.268, +164.660] | -122.9 | -0.82 | 0.410 | not applied (n < 1000) | 0.987 | +1.6 | +1.2 | 0.0531 | 0.0549 |
| Avg. daily time < 54 (%) | 374 | -47.465 [-409.791, +314.860] | -63.85 | -0.26 | 0.797 | not applied (n < 1000) | 0.987 | +1.9 | +1.5 | 0.0529 | 0.0549 |
| Time 54-69, pooled (%) | 374 | -73.164 [-530.505, +384.177] | -33.29 | -0.31 | 0.754 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0415 | 0.0549 |
| Avg. daily time 54-69 (%) | 374 | -50.977 [-521.819, +419.865] | -22.61 | -0.21 | 0.832 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0405 | 0.0549 |
| Time < 70, pooled (%) | 374 | -100.186 [-526.349, +325.978] | -35.95 | -0.46 | 0.645 | not applied (n < 1000) | 0.987 | +1.7 | +1.3 | 0.0474 | 0.0549 |
| Avg. daily time < 70 (%) | 374 | -55.345 [-508.973, +398.284] | -20.25 | -0.24 | 0.811 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0446 | 0.0549 |
| Time 54-250, pooled (%) | 374 | +137.682 [-149.076, +424.439] | 112.6 | 0.94 | 0.347 | not applied (n < 1000) | 0.987 | +1.5 | +1.0 | 0.0536 | 0.0549 |
| Avg. daily time 54-250 (%) | 374 | +71.352 [-237.475, +380.178] | 66.28 | 0.45 | 0.651 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0528 | 0.0549 |
| Time 181-250, pooled (%) | 374 | -130.999 [-407.394, +145.396] | -30.68 | -0.93 | 0.353 | not applied (n < 1000) | 0.987 | +1.6 | +1.1 | 0.0531 | 0.0549 |
| Avg. daily time 181-250 (%) | 374 | -138.605 [-420.439, +143.230] | -31.05 | -0.96 | 0.335 | not applied (n < 1000) | 0.987 | +1.5 | +1.0 | 0.0533 | 0.0549 |
| Time > 180, pooled (%) | 374 | -126.834 [-403.487, +149.820] | -26.34 | -0.90 | 0.369 | not applied (n < 1000) | 0.987 | +1.6 | +1.1 | 0.0527 | 0.0549 |
| Avg. daily time > 180 (%) | 374 | -130.582 [-411.418, +150.255] | -25.84 | -0.91 | 0.362 | not applied (n < 1000) | 0.987 | +1.6 | +1.1 | 0.0528 | 0.0549 |
| Nocturnal time > 180 (%) | 374 | -140.244 [-416.805, +136.318] | -30.17 | -0.99 | 0.320 | not applied (n < 1000) | 0.987 | +1.5 | +1.0 | 0.0540 | 0.0549 |
| Any reading > 250 during wear (0/1) | 374 | -30.180 [-399.970, +339.611] | -82.12 | -0.16 | 0.873 | not applied (n < 1000) | 0.987 | +2.0 | +1.5 | 0.0429 | 0.0549 |
| Time > 250, pooled (%) | 374 | -74.697 [-404.354, +254.961] | -109.5 | -0.44 | 0.657 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0509 | 0.0549 |
| Avg. daily time > 250 (%) | 374 | -55.090 [-344.345, +234.165] | -74.69 | -0.37 | 0.709 | not applied (n < 1000) | 0.987 | +1.9 | +1.4 | 0.0515 | 0.0549 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 374; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 374 | +0.718 [-0.472, +1.908] | 1.648 | 1.18 | 0.237 | not applied (n < 1000) | 0.987 | +0.8 | +0.0 | 0.0738 | 0.0776 |
| Mean glucose (mg/dL) | 374 | -0.023 [-1.218, +1.173] | -0.001584 | -0.04 | 0.971 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0744 | 0.0776 |
| GMI (%) | 374 | -0.023 [-1.218, +1.173] | -0.06622 | -0.04 | 0.971 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0744 | 0.0776 |
| Nocturnal mean 00-06h (mg/dL) | 374 | +0.315 [-0.947, +1.578] | 0.02048 | 0.49 | 0.625 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0733 | 0.0776 |
| Glucose SD, pooled (mg/dL) | 374 | -0.353 [-1.679, +0.974] | -0.05596 | -0.52 | 0.602 | not applied (n < 1000) | 0.987 | +1.7 | +0.9 | 0.0717 | 0.0776 |
| Avg. daily SD (mg/dL) | 374 | -0.376 [-1.777, +1.025] | -0.06379 | -0.53 | 0.599 | not applied (n < 1000) | 0.987 | +1.7 | +0.9 | 0.0689 | 0.0776 |
| CV (%) | 374 | -0.453 [-1.769, +0.863] | -0.1002 | -0.67 | 0.500 | not applied (n < 1000) | 0.987 | +1.5 | +0.7 | 0.0727 | 0.0776 |
| Mean / SD ratio | 374 | -0.046 [-1.362, +1.271] | -0.04101 | -0.07 | 0.946 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0704 | 0.0776 |
| Avg. daily mean / SD | 374 | -0.306 [-1.623, +1.011] | -0.2178 | -0.46 | 0.648 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0663 | 0.0776 |
| MAG (mg/dL/h) | 374 | +0.648 [-0.624, +1.919] | 0.08146 | 1.00 | 0.318 | not applied (n < 1000) | 0.987 | +0.9 | +0.2 | 0.0725 | 0.0776 |
| Avg. daily range (mg/dL) | 374 | -0.315 [-1.693, +1.063] | -0.0119 | -0.45 | 0.654 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0675 | 0.0776 |
| SD of daily means (mg/dL) | 374 | +0.069 [-1.229, +1.366] | 0.0193 | 0.10 | 0.917 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0740 | 0.0776 |
| Time in range 70-180, pooled (%) | 374 | +0.359 [-0.630, +1.348] | 0.06836 | 0.71 | 0.477 | not applied (n < 1000) | 0.987 | +1.7 | +0.9 | 0.0756 | 0.0776 |
| Avg. daily time in range 70-180 (%) | 374 | +0.335 [-0.658, +1.328] | 0.06147 | 0.66 | 0.508 | not applied (n < 1000) | 0.987 | +1.7 | +0.9 | 0.0753 | 0.0776 |
| Time < 54, pooled (%) | 374 | -0.282 [-1.506, +0.942] | -0.2903 | -0.45 | 0.652 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0744 | 0.0776 |
| Avg. daily time < 54 (%) | 374 | -0.220 [-1.512, +1.072] | -0.296 | -0.33 | 0.739 | not applied (n < 1000) | 0.987 | +1.9 | +1.1 | 0.0755 | 0.0776 |
| Time 54-69, pooled (%) | 374 | -0.194 [-1.628, +1.240] | -0.08824 | -0.27 | 0.791 | not applied (n < 1000) | 0.987 | +1.9 | +1.1 | 0.0674 | 0.0776 |
| Avg. daily time 54-69 (%) | 374 | -0.194 [-1.658, +1.270] | -0.0861 | -0.26 | 0.795 | not applied (n < 1000) | 0.987 | +1.9 | +1.1 | 0.0659 | 0.0776 |
| Time < 70, pooled (%) | 374 | -0.254 [-1.612, +1.105] | -0.09099 | -0.37 | 0.715 | not applied (n < 1000) | 0.987 | +1.8 | +1.1 | 0.0718 | 0.0776 |
| Avg. daily time < 70 (%) | 374 | -0.221 [-1.650, +1.208] | -0.08098 | -0.30 | 0.761 | not applied (n < 1000) | 0.987 | +1.9 | +1.1 | 0.0687 | 0.0776 |
| Time 54-250, pooled (%) | 374 | +0.292 [-0.798, +1.383] | 0.239 | 0.53 | 0.599 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0755 | 0.0776 |
| Avg. daily time 54-250 (%) | 374 | +0.182 [-0.901, +1.265] | 0.1691 | 0.33 | 0.742 | not applied (n < 1000) | 0.987 | +1.9 | +1.1 | 0.0751 | 0.0776 |
| Time 181-250, pooled (%) | 374 | -0.262 [-1.135, +0.611] | -0.06135 | -0.59 | 0.556 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0753 | 0.0776 |
| Avg. daily time 181-250 (%) | 374 | -0.271 [-1.154, +0.612] | -0.06066 | -0.60 | 0.548 | not applied (n < 1000) | 0.987 | +1.8 | +1.0 | 0.0752 | 0.0776 |
| Time > 180, pooled (%) | 374 | -0.249 [-1.117, +0.618] | -0.05174 | -0.56 | 0.574 | not applied (n < 1000) | 0.987 | +1.8 | +1.1 | 0.0750 | 0.0776 |
| Avg. daily time > 180 (%) | 374 | -0.245 [-1.118, +0.628] | -0.04857 | -0.55 | 0.582 | not applied (n < 1000) | 0.987 | +1.8 | +1.1 | 0.0749 | 0.0776 |
| Nocturnal time > 180 (%) | 374 | -0.252 [-1.134, +0.631] | -0.05413 | -0.56 | 0.576 | not applied (n < 1000) | 0.987 | +1.8 | +1.1 | 0.0757 | 0.0776 |
| Any reading > 250 during wear (0/1) | 374 | -0.052 [-1.300, +1.197] | -0.1403 | -0.08 | 0.935 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0650 | 0.0776 |
| Time > 250, pooled (%) | 374 | -0.118 [-1.043, +0.808] | -0.1724 | -0.25 | 0.803 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0740 | 0.0776 |
| Avg. daily time > 250 (%) | 374 | -0.041 [-0.867, +0.785] | -0.05599 | -0.10 | 0.922 | not applied (n < 1000) | 0.987 | +2.0 | +1.2 | 0.0740 | 0.0776 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 373; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 373 | +0.279 [-0.459, +1.017] | 0.6397 | 0.74 | 0.459 | not applied (n < 1000) | 0.987 | +1.5 | +0.0 | 0.0996 | 0.0998 |
| Mean glucose (mg/dL) | 373 | +0.245 [-0.585, +1.075] | 0.01722 | 0.58 | 0.563 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.0992 | 0.0998 |
| GMI (%) | 373 | +0.245 [-0.585, +1.075] | 0.7199 | 0.58 | 0.563 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.0992 | 0.0998 |
| Nocturnal mean 00-06h (mg/dL) | 373 | +0.186 [-0.625, +0.998] | 0.01216 | 0.45 | 0.653 | not applied (n < 1000) | 0.987 | +1.8 | +0.3 | 0.0970 | 0.0998 |
| Glucose SD, pooled (mg/dL) | 373 | +0.551 [-0.188, +1.291] | 0.08781 | 1.46 | 0.144 | not applied (n < 1000) | 0.943 | +0.1 | -1.5 | 0.1038 | 0.0998 |
| Avg. daily SD (mg/dL) | 373 | +0.503 [-0.245, +1.251] | 0.08556 | 1.32 | 0.188 | not applied (n < 1000) | 0.967 | +0.4 | -1.1 | 0.1023 | 0.0998 |
| CV (%) | 373 | +0.509 [-0.217, +1.235] | 0.1129 | 1.38 | 0.169 | not applied (n < 1000) | 0.967 | +0.3 | -1.2 | 0.1026 | 0.0998 |
| Mean / SD ratio | 373 | -0.681 [-1.424, +0.062] | -0.611 | -1.80 | 0.072 | not applied (n < 1000) | 0.676 | -1.0 | -2.5 | 0.1054 | 0.0998 |
| Avg. daily mean / SD | 373 | -0.671 [-1.436, +0.093] | -0.4777 | -1.72 | 0.085 | not applied (n < 1000) | 0.739 | -0.9 | -2.4 | 0.1037 | 0.0998 |
| MAG (mg/dL/h) | 373 | +0.532 [-0.245, +1.310] | 0.06701 | 1.34 | 0.179 | not applied (n < 1000) | 0.967 | +0.1 | -1.4 | 0.0988 | 0.0998 |
| Avg. daily range (mg/dL) | 373 | +0.403 [-0.345, +1.151] | 0.01527 | 1.06 | 0.291 | not applied (n < 1000) | 0.987 | +1.0 | -0.6 | 0.1021 | 0.0998 |
| SD of daily means (mg/dL) | 373 | +0.626 [-0.188, +1.440] | 0.1776 | 1.51 | 0.132 | not applied (n < 1000) | 0.943 | -0.6 | -2.1 | 0.1044 | 0.0998 |
| Time in range 70-180, pooled (%) | 373 | -0.235 [-1.038, +0.568] | -0.04469 | -0.57 | 0.566 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.0967 | 0.0998 |
| Avg. daily time in range 70-180 (%) | 373 | -0.229 [-1.059, +0.602] | -0.04193 | -0.54 | 0.590 | not applied (n < 1000) | 0.987 | +1.7 | +0.1 | 0.0958 | 0.0998 |
| Time < 54, pooled (%) | 373 | +0.070 [-0.386, +0.526] | 0.07193 | 0.30 | 0.764 | not applied (n < 1000) | 0.987 | +2.0 | +0.4 | 0.0968 | 0.0998 |
| Avg. daily time < 54 (%) | 373 | +0.024 [-0.567, +0.615] | 0.03245 | 0.08 | 0.936 | not applied (n < 1000) | 0.987 | +2.0 | +0.5 | 0.0935 | 0.0998 |
| Time 54-69, pooled (%) | 373 | -0.019 [-0.763, +0.725] | -0.008657 | -0.05 | 0.960 | not applied (n < 1000) | 0.987 | +2.0 | +0.5 | 0.0966 | 0.0998 |
| Avg. daily time 54-69 (%) | 373 | -0.006 [-0.772, +0.760] | -0.002486 | -0.01 | 0.989 | not applied (n < 1000) | 0.996 | +2.0 | +0.5 | 0.0958 | 0.0998 |
| Time < 70, pooled (%) | 373 | +0.009 [-0.690, +0.708] | 0.003322 | 0.03 | 0.979 | not applied (n < 1000) | 0.993 | +2.0 | +0.5 | 0.0961 | 0.0998 |
| Avg. daily time < 70 (%) | 373 | +0.002 [-0.750, +0.754] | 0.0006804 | 0.00 | 0.996 | not applied (n < 1000) | 0.996 | +2.0 | +0.5 | 0.0947 | 0.0998 |
| Time 54-250, pooled (%) | 373 | -0.016 [-0.560, +0.528] | -0.01327 | -0.06 | 0.953 | not applied (n < 1000) | 0.987 | +2.0 | +0.5 | 0.0960 | 0.0998 |
| Avg. daily time 54-250 (%) | 373 | +0.028 [-0.647, +0.704] | 0.02609 | 0.08 | 0.935 | not applied (n < 1000) | 0.987 | +2.0 | +0.5 | 0.0939 | 0.0998 |
| Time 181-250, pooled (%) | 373 | +0.297 [-0.593, +1.188] | 0.06968 | 0.65 | 0.513 | not applied (n < 1000) | 0.987 | +1.4 | -0.1 | 0.0973 | 0.0998 |
| Avg. daily time 181-250 (%) | 373 | +0.292 [-0.601, +1.184] | 0.06539 | 0.64 | 0.522 | not applied (n < 1000) | 0.987 | +1.5 | -0.1 | 0.0971 | 0.0998 |
| Time > 180, pooled (%) | 373 | +0.254 [-0.654, +1.161] | 0.05267 | 0.55 | 0.584 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.0964 | 0.0998 |
| Avg. daily time > 180 (%) | 373 | +0.248 [-0.678, +1.175] | 0.04913 | 0.52 | 0.600 | not applied (n < 1000) | 0.987 | +1.6 | +0.1 | 0.0960 | 0.0998 |
| Nocturnal time > 180 (%) | 373 | -0.136 [-0.902, +0.631] | -0.02944 | -0.35 | 0.729 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | 0.0964 | 0.0998 |
| Any reading > 250 during wear (0/1) | 373 | +0.036 [-0.768, +0.840] | 0.09799 | 0.09 | 0.930 | not applied (n < 1000) | 0.987 | +2.0 | +0.5 | 0.0956 | 0.0998 |
| Time > 250, pooled (%) | 373 | -0.071 [-1.030, +0.888] | -0.104 | -0.15 | 0.884 | not applied (n < 1000) | 0.987 | +2.0 | +0.4 | 0.0924 | 0.0998 |
| Avg. daily time > 250 (%) | 373 | -0.065 [-1.201, +1.072] | -0.0876 | -0.11 | 0.911 | not applied (n < 1000) | 0.987 | +2.0 | +0.4 | 0.0910 | 0.0998 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 383; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 383 | -2.028 [-10.076, +6.020] | -4.685 | -0.49 | 0.621 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0560 | -0.0513 |
| Mean glucose (mg/dL) | 383 | -1.967 [-8.685, +4.752] | -0.1397 | -0.57 | 0.566 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0573 | -0.0513 |
| GMI (%) | 383 | -1.967 [-8.685, +4.752] | -5.84 | -0.57 | 0.566 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0573 | -0.0513 |
| Nocturnal mean 00-06h (mg/dL) | 383 | -3.602 [-10.644, +3.439] | -0.2364 | -1.00 | 0.316 | not applied (n < 1000) | 0.987 | +0.8 | -0.8 | -0.0547 | -0.0513 |
| Glucose SD, pooled (mg/dL) | 383 | +0.025 [-6.963, +7.012] | 0.003964 | 0.01 | 0.994 | not applied (n < 1000) | 0.996 | +2.0 | +0.3 | -0.0657 | -0.0513 |
| Avg. daily SD (mg/dL) | 383 | -0.136 [-7.179, +6.907] | -0.02332 | -0.04 | 0.970 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0639 | -0.0513 |
| CV (%) | 383 | +0.746 [-5.761, +7.253] | 0.167 | 0.22 | 0.822 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0633 | -0.0513 |
| Mean / SD ratio | 383 | -0.425 [-6.571, +5.720] | -0.3841 | -0.14 | 0.892 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0632 | -0.0513 |
| Avg. daily mean / SD | 383 | +1.377 [-4.645, +7.400] | 0.9926 | 0.45 | 0.654 | not applied (n < 1000) | 0.987 | +1.8 | +0.2 | -0.0607 | -0.0513 |
| MAG (mg/dL/h) | 383 | -11.886 [-18.384, -5.388] | -1.518 | -3.58 | 3.4e-04*** | not applied (n < 1000) | 0.142 | -11.2 | -12.9 | -0.0210 | -0.0513 |
| Avg. daily range (mg/dL) | 383 | -1.094 [-7.932, +5.743] | -0.04187 | -0.31 | 0.754 | not applied (n < 1000) | 0.987 | +1.9 | +0.2 | -0.0631 | -0.0513 |
| SD of daily means (mg/dL) | 383 | +0.850 [-5.308, +7.008] | 0.2421 | 0.27 | 0.787 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0656 | -0.0513 |
| Time in range 70-180, pooled (%) | 383 | -2.129 [-9.209, +4.952] | -0.4089 | -0.59 | 0.556 | not applied (n < 1000) | 0.987 | +1.6 | -0.1 | -0.0600 | -0.0513 |
| Avg. daily time in range 70-180 (%) | 383 | -2.376 [-9.445, +4.693] | -0.4403 | -0.66 | 0.510 | not applied (n < 1000) | 0.987 | +1.5 | -0.2 | -0.0596 | -0.0513 |
| Time < 54, pooled (%) | 383 | -2.428 [-6.578, +1.722] | -2.527 | -1.15 | 0.252 | not applied (n < 1000) | 0.987 | +1.5 | -0.2 | -0.0533 | -0.0513 |
| Avg. daily time < 54 (%) | 383 | -2.758 [-6.811, +1.294] | -3.749 | -1.33 | 0.182 | not applied (n < 1000) | 0.967 | +1.3 | -0.3 | -0.0518 | -0.0513 |
| Time 54-69, pooled (%) | 383 | +1.930 [-3.143, +7.002] | 0.8894 | 0.75 | 0.456 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0539 | -0.0513 |
| Avg. daily time 54-69 (%) | 383 | +2.054 [-3.077, +7.185] | 0.9231 | 0.78 | 0.433 | not applied (n < 1000) | 0.987 | +1.6 | -0.0 | -0.0543 | -0.0513 |
| Time < 70, pooled (%) | 383 | +0.691 [-4.279, +5.661] | 0.2509 | 0.27 | 0.785 | not applied (n < 1000) | 0.987 | +2.0 | +0.3 | -0.0555 | -0.0513 |
| Avg. daily time < 70 (%) | 383 | +0.964 [-3.984, +5.913] | 0.3573 | 0.38 | 0.702 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0551 | -0.0513 |
| Time 54-250, pooled (%) | 383 | +1.349 [-4.208, +6.905] | 1.114 | 0.48 | 0.634 | not applied (n < 1000) | 0.987 | +1.8 | +0.2 | -0.0591 | -0.0513 |
| Avg. daily time 54-250 (%) | 383 | +1.254 [-5.061, +7.568] | 1.177 | 0.39 | 0.697 | not applied (n < 1000) | 0.987 | +1.9 | +0.2 | -0.0571 | -0.0513 |
| Time 181-250, pooled (%) | 383 | +2.035 [-5.793, +9.863] | 0.4809 | 0.51 | 0.610 | not applied (n < 1000) | 0.987 | +1.6 | -0.0 | -0.0565 | -0.0513 |
| Avg. daily time 181-250 (%) | 383 | +2.188 [-5.634, +10.010] | 0.4954 | 0.55 | 0.584 | not applied (n < 1000) | 0.987 | +1.6 | -0.1 | -0.0565 | -0.0513 |
| Time > 180, pooled (%) | 383 | +1.956 [-6.010, +9.921] | 0.41 | 0.48 | 0.630 | not applied (n < 1000) | 0.987 | +1.7 | +0.0 | -0.0570 | -0.0513 |
| Avg. daily time > 180 (%) | 383 | +2.073 [-5.880, +10.027] | 0.4148 | 0.51 | 0.609 | not applied (n < 1000) | 0.987 | +1.6 | -0.0 | -0.0570 | -0.0513 |
| Nocturnal time > 180 (%) | 383 | +1.542 [-8.550, +11.633] | 0.3387 | 0.30 | 0.765 | not applied (n < 1000) | 0.987 | +1.8 | +0.1 | -0.0652 | -0.0513 |
| Any reading > 250 during wear (0/1) | 383 | +5.430 [-1.802, +12.661] | 14.72 | 1.47 | 0.141 | not applied (n < 1000) | 0.943 | -0.7 | -2.4 | -0.0570 | -0.0513 |
| Time > 250, pooled (%) | 383 | +1.061 [-7.397, +9.520] | 1.573 | 0.25 | 0.806 | not applied (n < 1000) | 0.987 | +1.9 | +0.2 | -0.0613 | -0.0513 |
| Avg. daily time > 250 (%) | 383 | +0.959 [-7.736, +9.654] | 1.316 | 0.22 | 0.829 | not applied (n < 1000) | 0.987 | +1.9 | +0.3 | -0.0612 | -0.0513 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 374; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 374 | +1.188 [-0.398, +2.773] | 2.725 | 1.47 | 0.142 | not applied (n < 1000) | 0.943 | +0.2 | +0.0 | 0.0339 | 0.0428 |
| Mean glucose (mg/dL) | 374 | +0.387 [-1.390, +2.165] | 0.02723 | 0.43 | 0.669 | not applied (n < 1000) | 0.987 | +1.8 | +1.6 | 0.0329 | 0.0428 |
| GMI (%) | 374 | +0.387 [-1.390, +2.165] | 1.138 | 0.43 | 0.669 | not applied (n < 1000) | 0.987 | +1.8 | +1.6 | 0.0329 | 0.0428 |
| Nocturnal mean 00-06h (mg/dL) | 374 | -0.062 [-1.901, +1.777] | -0.004023 | -0.07 | 0.947 | not applied (n < 1000) | 0.987 | +2.0 | +1.8 | 0.0309 | 0.0428 |
| Glucose SD, pooled (mg/dL) | 374 | +1.207 [-0.523, +2.938] | 0.1916 | 1.37 | 0.171 | not applied (n < 1000) | 0.967 | +0.0 | -0.2 | 0.0405 | 0.0428 |
| Avg. daily SD (mg/dL) | 374 | +1.052 [-0.706, +2.810] | 0.1786 | 1.17 | 0.241 | not applied (n < 1000) | 0.987 | +0.5 | +0.3 | 0.0379 | 0.0428 |
| CV (%) | 374 | +1.244 [-0.666, +3.155] | 0.2753 | 1.28 | 0.202 | not applied (n < 1000) | 0.967 | -0.1 | -0.3 | 0.0384 | 0.0428 |
| Mean / SD ratio | 374 | -1.721 [-3.448, +0.005] | -1.542 | -1.95 | 0.051 | not applied (n < 1000) | 0.637 | -2.1 | -2.3 | 0.0462 | 0.0428 |
| Avg. daily mean / SD | 374 | -1.521 [-3.258, +0.216] | -1.081 | -1.72 | 0.086 | not applied (n < 1000) | 0.739 | -1.1 | -1.3 | 0.0413 | 0.0428 |
| MAG (mg/dL/h) | 374 | +1.250 [-0.505, +3.004] | 0.1572 | 1.40 | 0.163 | not applied (n < 1000) | 0.967 | -0.2 | -0.3 | 0.0395 | 0.0428 |
| Avg. daily range (mg/dL) | 374 | +1.017 [-0.751, +2.785] | 0.03842 | 1.13 | 0.260 | not applied (n < 1000) | 0.987 | +0.6 | +0.4 | 0.0356 | 0.0428 |
| SD of daily means (mg/dL) | 374 | +1.353 [-0.453, +3.160] | 0.3806 | 1.47 | 0.142 | not applied (n < 1000) | 0.943 | -0.6 | -0.8 | 0.0444 | 0.0428 |
| Time in range 70-180, pooled (%) | 374 | -0.055 [-1.891, +1.781] | -0.01049 | -0.06 | 0.953 | not applied (n < 1000) | 0.987 | +2.0 | +1.8 | 0.0345 | 0.0428 |
| Avg. daily time in range 70-180 (%) | 374 | +0.048 [-1.809, +1.906] | 0.008884 | 0.05 | 0.959 | not applied (n < 1000) | 0.987 | +2.0 | +1.8 | 0.0348 | 0.0428 |
| Time < 54, pooled (%) | 374 | -0.285 [-1.989, +1.420] | -0.293 | -0.33 | 0.743 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0415 | 0.0428 |
| Avg. daily time < 54 (%) | 374 | -0.477 [-2.347, +1.394] | -0.6414 | -0.50 | 0.617 | not applied (n < 1000) | 0.987 | +1.7 | +1.5 | 0.0425 | 0.0428 |
| Time 54-69, pooled (%) | 374 | -0.188 [-2.127, +1.750] | -0.08567 | -0.19 | 0.849 | not applied (n < 1000) | 0.987 | +2.0 | +1.8 | 0.0240 | 0.0428 |
| Avg. daily time 54-69 (%) | 374 | -0.253 [-2.294, +1.788] | -0.1124 | -0.24 | 0.808 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0220 | 0.0428 |
| Time < 70, pooled (%) | 374 | -0.250 [-2.135, +1.635] | -0.0897 | -0.26 | 0.795 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0319 | 0.0428 |
| Avg. daily time < 70 (%) | 374 | -0.340 [-2.433, +1.752] | -0.1245 | -0.32 | 0.750 | not applied (n < 1000) | 0.987 | +1.8 | +1.6 | 0.0272 | 0.0428 |
| Time 54-250, pooled (%) | 374 | +0.341 [-1.202, +1.884] | 0.2787 | 0.43 | 0.665 | not applied (n < 1000) | 0.987 | +1.8 | +1.6 | 0.0374 | 0.0428 |
| Avg. daily time 54-250 (%) | 374 | +0.535 [-1.109, +2.180] | 0.4973 | 0.64 | 0.523 | not applied (n < 1000) | 0.987 | +1.6 | +1.4 | 0.0379 | 0.0428 |
| Time 181-250, pooled (%) | 374 | +0.263 [-1.636, +2.162] | 0.06166 | 0.27 | 0.786 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0321 | 0.0428 |
| Avg. daily time 181-250 (%) | 374 | +0.197 [-1.695, +2.088] | 0.04406 | 0.20 | 0.839 | not applied (n < 1000) | 0.987 | +1.9 | +1.8 | 0.0319 | 0.0428 |
| Time > 180, pooled (%) | 374 | +0.205 [-1.717, +2.127] | 0.04263 | 0.21 | 0.834 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0323 | 0.0428 |
| Avg. daily time > 180 (%) | 374 | +0.131 [-1.796, +2.058] | 0.02597 | 0.13 | 0.894 | not applied (n < 1000) | 0.987 | +2.0 | +1.8 | 0.0323 | 0.0428 |
| Nocturnal time > 180 (%) | 374 | -0.754 [-2.534, +1.025] | -0.1623 | -0.83 | 0.406 | not applied (n < 1000) | 0.987 | +1.2 | +1.0 | 0.0426 | 0.0428 |
| Any reading > 250 during wear (0/1) | 374 | +0.214 [-1.587, +2.015] | 0.5834 | 0.23 | 0.816 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0345 | 0.0428 |
| Time > 250, pooled (%) | 374 | -0.201 [-2.348, +1.947] | -0.2938 | -0.18 | 0.855 | not applied (n < 1000) | 0.987 | +1.9 | +1.8 | 0.0318 | 0.0428 |
| Avg. daily time > 250 (%) | 374 | -0.292 [-2.618, +2.033] | -0.3964 | -0.25 | 0.805 | not applied (n < 1000) | 0.987 | +1.9 | +1.7 | 0.0313 | 0.0428 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

### Population: Non-healthy group (T2D non-insulin + T2D insulin)

#### MoCA total score (0-30)
*n = 230; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 230 | -0.543 [-0.979, -0.106] | -0.4864 | -2.44 | 0.015* | not applied (n < 1000) | 0.169 | -4.4 | +0.0 | 0.0302 | 0.0230 |
| Mean glucose (mg/dL) | 230 | -0.470 [-0.937, -0.003] | -0.01495 | -1.97 | 0.049* | not applied (n < 1000) | 0.253 | -2.9 | +1.4 | 0.0229 | 0.0230 |
| GMI (%) | 230 | -0.470 [-0.937, -0.003] | -0.6249 | -1.97 | 0.049* | not applied (n < 1000) | 0.253 | -2.9 | +1.4 | 0.0229 | 0.0230 |
| Nocturnal mean 00-06h (mg/dL) | 230 | -0.487 [-0.922, -0.052] | -0.0153 | -2.19 | 0.028* | not applied (n < 1000) | 0.204 | -3.4 | +1.0 | 0.0209 | 0.0230 |
| Glucose SD, pooled (mg/dL) | 230 | -0.417 [-0.872, +0.038] | -0.02668 | -1.80 | 0.072 | not applied (n < 1000) | 0.284 | -1.5 | +2.9 | 0.0173 | 0.0230 |
| Avg. daily SD (mg/dL) | 230 | -0.374 [-0.844, +0.097] | -0.02804 | -1.56 | 0.119 | not applied (n < 1000) | 0.389 | -0.7 | +3.6 | 0.0128 | 0.0230 |
| CV (%) | 230 | -0.233 [-0.619, +0.153] | -0.0329 | -1.18 | 0.237 | not applied (n < 1000) | 0.562 | +1.0 | +5.4 | 0.0132 | 0.0230 |
| Mean / SD ratio | 230 | +0.229 [-0.160, +0.618] | 0.1666 | 1.16 | 0.248 | not applied (n < 1000) | 0.565 | +1.0 | +5.4 | 0.0153 | 0.0230 |
| Avg. daily mean / SD | 230 | +0.082 [-0.318, +0.481] | 0.04877 | 0.40 | 0.689 | not applied (n < 1000) | 0.867 | +1.9 | +6.2 | 0.0107 | 0.0230 |
| MAG (mg/dL/h) | 230 | -0.077 [-0.544, +0.389] | -0.00706 | -0.32 | 0.745 | not applied (n < 1000) | 0.896 | +1.9 | +6.2 | 0.0042 | 0.0230 |
| Avg. daily range (mg/dL) | 230 | -0.241 [-0.727, +0.245] | -0.005098 | -0.97 | 0.332 | not applied (n < 1000) | 0.639 | +0.9 | +5.2 | 0.0075 | 0.0230 |
| SD of daily means (mg/dL) | 230 | -0.456 [-0.874, -0.037] | -0.04731 | -2.13 | 0.033* | not applied (n < 1000) | 0.213 | -2.4 | +2.0 | 0.0278 | 0.0230 |
| Time in range 70-180, pooled (%) | 230 | +0.553 [+0.085, +1.020] | 0.03047 | 2.32 | 0.021* | not applied (n < 1000) | 0.184 | -4.6 | -0.2 | 0.0251 | 0.0230 |
| Avg. daily time in range 70-180 (%) | 230 | +0.548 [+0.076, +1.020] | 0.03011 | 2.28 | 0.023* | not applied (n < 1000) | 0.188 | -4.5 | -0.1 | 0.0243 | 0.0230 |
| Time < 54, pooled (%) | 230 | -0.042 [-0.777, +0.693] | -0.05671 | -0.11 | 0.911 | not applied (n < 1000) | 0.961 | +2.0 | +6.3 | -0.0013 | 0.0230 |
| Avg. daily time < 54 (%) | 230 | -0.054 [-0.615, +0.506] | -0.0667 | -0.19 | 0.850 | not applied (n < 1000) | 0.925 | +1.9 | +6.3 | -0.0051 | 0.0230 |
| Time 54-69, pooled (%) | 230 | -0.069 [-0.556, +0.417] | -0.02768 | -0.28 | 0.781 | not applied (n < 1000) | 0.908 | +1.9 | +6.3 | 0.0110 | 0.0230 |
| Avg. daily time 54-69 (%) | 230 | -0.058 [-0.567, +0.450] | -0.0222 | -0.22 | 0.822 | not applied (n < 1000) | 0.912 | +1.9 | +6.3 | 0.0099 | 0.0230 |
| Time < 70, pooled (%) | 230 | -0.068 [-0.564, +0.429] | -0.02247 | -0.27 | 0.790 | not applied (n < 1000) | 0.908 | +1.9 | +6.3 | 0.0089 | 0.0230 |
| Avg. daily time < 70 (%) | 230 | -0.061 [-0.557, +0.434] | -0.01922 | -0.24 | 0.808 | not applied (n < 1000) | 0.912 | +1.9 | +6.3 | 0.0079 | 0.0230 |
| Time 54-250, pooled (%) | 230 | +0.556 [+0.053, +1.060] | 0.06122 | 2.17 | 0.030* | not applied (n < 1000) | 0.209 | -4.8 | -0.4 | 0.0226 | 0.0230 |
| Avg. daily time 54-250 (%) | 230 | +0.605 [+0.110, +1.099] | 0.07334 | 2.40 | 0.016* | not applied (n < 1000) | 0.169 | -6.0 | -1.6 | 0.0237 | 0.0230 |
| Time 181-250, pooled (%) | 230 | -0.382 [-0.844, +0.080] | -0.0314 | -1.62 | 0.105 | not applied (n < 1000) | 0.356 | -1.2 | +3.2 | 0.0197 | 0.0230 |
| Avg. daily time 181-250 (%) | 230 | -0.374 [-0.828, +0.080] | -0.02981 | -1.61 | 0.107 | not applied (n < 1000) | 0.359 | -1.0 | +3.3 | 0.0199 | 0.0230 |
| Time > 180, pooled (%) | 230 | -0.527 [-1.002, -0.052] | -0.0287 | -2.18 | 0.030* | not applied (n < 1000) | 0.209 | -4.1 | +0.3 | 0.0231 | 0.0230 |
| Avg. daily time > 180 (%) | 230 | -0.526 [-1.005, -0.046] | -0.02872 | -2.15 | 0.032* | not applied (n < 1000) | 0.209 | -4.0 | +0.3 | 0.0230 | 0.0230 |
| Nocturnal time > 180 (%) | 230 | -0.546 [-1.006, -0.086] | -0.03016 | -2.33 | 0.020* | not applied (n < 1000) | 0.184 | -4.7 | -0.3 | 0.0179 | 0.0230 |
| Any reading > 250 during wear (0/1) | 230 | -0.279 [-0.742, +0.183] | -0.5581 | -1.19 | 0.236 | not applied (n < 1000) | 0.562 | +0.4 | +4.8 | 0.0126 | 0.0230 |
| Time > 250, pooled (%) | 230 | -0.555 [-1.062, -0.048] | -0.06152 | -2.15 | 0.032* | not applied (n < 1000) | 0.209 | -4.8 | -0.4 | 0.0204 | 0.0230 |
| Avg. daily time > 250 (%) | 230 | -0.605 [-1.105, -0.105] | -0.07435 | -2.37 | 0.018* | not applied (n < 1000) | 0.173 | -6.0 | -1.6 | 0.0213 | 0.0230 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 230; events = 105; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 230 | OR 1.518 [1.107, 2.083] | 0.374 | 2.59 | 0.010** | not applied (n < 1000) | 0.131 | -5.5 | +0.0 | 0.6402 | 0.6130 |
| Mean glucose (mg/dL) | 230 | OR 1.333 [0.999, 1.781] | 0.009161 | 1.95 | 0.051 | not applied (n < 1000) | 0.259 | -2.0 | +3.5 | 0.6126 | 0.6130 |
| GMI (%) | 230 | OR 1.333 [0.999, 1.781] | 0.383 | 1.95 | 0.051 | not applied (n < 1000) | 0.259 | -2.0 | +3.5 | 0.6126 | 0.6130 |
| Nocturnal mean 00-06h (mg/dL) | 230 | OR 1.317 [0.989, 1.754] | 0.008649 | 1.88 | 0.060 | not applied (n < 1000) | 0.276 | -1.8 | +3.8 | 0.6070 | 0.6130 |
| Glucose SD, pooled (mg/dL) | 230 | OR 1.378 [1.008, 1.883] | 0.0205 | 2.01 | 0.044* | not applied (n < 1000) | 0.248 | -2.3 | +3.2 | 0.6158 | 0.6130 |
| Avg. daily SD (mg/dL) | 230 | OR 1.306 [0.958, 1.780] | 0.02001 | 1.69 | 0.092 | not applied (n < 1000) | 0.330 | -1.0 | +4.5 | 0.6137 | 0.6130 |
| CV (%) | 230 | OR 1.304 [0.949, 1.792] | 0.03743 | 1.63 | 0.102 | not applied (n < 1000) | 0.354 | -0.7 | +4.8 | 0.6181 | 0.6130 |
| Mean / SD ratio | 230 | OR 0.806 [0.587, 1.107] | -0.1565 | -1.33 | 0.184 | not applied (n < 1000) | 0.508 | +0.2 | +5.7 | 0.6190 | 0.6130 |
| Avg. daily mean / SD | 230 | OR 0.911 [0.668, 1.242] | -0.05582 | -0.59 | 0.555 | not applied (n < 1000) | 0.817 | +1.6 | +7.2 | 0.6135 | 0.6130 |
| MAG (mg/dL/h) | 230 | OR 1.056 [0.795, 1.402] | 0.00493 | 0.37 | 0.709 | not applied (n < 1000) | 0.883 | +1.9 | +7.4 | 0.5970 | 0.6130 |
| Avg. daily range (mg/dL) | 230 | OR 1.191 [0.882, 1.607] | 0.003694 | 1.14 | 0.255 | not applied (n < 1000) | 0.571 | +0.7 | +6.2 | 0.6109 | 0.6130 |
| SD of daily means (mg/dL) | 230 | OR 1.419 [1.024, 1.966] | 0.03635 | 2.10 | 0.035* | not applied (n < 1000) | 0.220 | -3.0 | +2.6 | 0.6223 | 0.6130 |
| Time in range 70-180, pooled (%) | 230 | OR 0.706 [0.524, 0.952] | -0.01917 | -2.28 | 0.022* | not applied (n < 1000) | 0.188 | -3.6 | +2.0 | 0.6225 | 0.6130 |
| Avg. daily time in range 70-180 (%) | 230 | OR 0.709 [0.527, 0.953] | -0.01893 | -2.27 | 0.023* | not applied (n < 1000) | 0.188 | -3.5 | +2.1 | 0.6213 | 0.6130 |
| Time < 54, pooled (%) | 230 | OR 1.063 [0.807, 1.401] | 0.08257 | 0.43 | 0.665 | not applied (n < 1000) | 0.867 | +1.8 | +7.4 | 0.5947 | 0.6130 |
| Avg. daily time < 54 (%) | 230 | OR 1.086 [0.823, 1.434] | 0.1021 | 0.59 | 0.558 | not applied (n < 1000) | 0.817 | +1.6 | +7.2 | 0.6025 | 0.6130 |
| Time 54-69, pooled (%) | 230 | OR 1.147 [0.863, 1.525] | 0.05507 | 0.95 | 0.343 | not applied (n < 1000) | 0.645 | +1.1 | +6.6 | 0.6086 | 0.6130 |
| Avg. daily time 54-69 (%) | 230 | OR 1.166 [0.875, 1.555] | 0.05856 | 1.05 | 0.295 | not applied (n < 1000) | 0.618 | +0.9 | +6.4 | 0.6128 | 0.6130 |
| Time < 70, pooled (%) | 230 | OR 1.137 [0.856, 1.510] | 0.04272 | 0.89 | 0.375 | not applied (n < 1000) | 0.667 | +1.2 | +6.7 | 0.6072 | 0.6130 |
| Avg. daily time < 70 (%) | 230 | OR 1.158 [0.869, 1.541] | 0.04572 | 1.00 | 0.316 | not applied (n < 1000) | 0.636 | +1.0 | +6.5 | 0.6128 | 0.6130 |
| Time 54-250, pooled (%) | 230 | OR 0.706 [0.485, 1.028] | -0.03829 | -1.81 | 0.070 | not applied (n < 1000) | 0.284 | -2.5 | +3.0 | 0.6215 | 0.6130 |
| Avg. daily time 54-250 (%) | 230 | OR 0.707 [0.488, 1.024] | -0.04211 | -1.83 | 0.067 | not applied (n < 1000) | 0.282 | -2.5 | +3.1 | 0.6229 | 0.6130 |
| Time 181-250, pooled (%) | 230 | OR 1.280 [0.967, 1.694] | 0.02028 | 1.72 | 0.085 | not applied (n < 1000) | 0.312 | -1.0 | +4.5 | 0.6156 | 0.6130 |
| Avg. daily time 181-250 (%) | 230 | OR 1.288 [0.974, 1.703] | 0.02017 | 1.77 | 0.076 | not applied (n < 1000) | 0.294 | -1.2 | +4.4 | 0.6147 | 0.6130 |
| Time > 180, pooled (%) | 230 | OR 1.367 [1.021, 1.831] | 0.01705 | 2.10 | 0.036* | not applied (n < 1000) | 0.220 | -2.7 | +2.9 | 0.6189 | 0.6130 |
| Avg. daily time > 180 (%) | 230 | OR 1.361 [1.017, 1.819] | 0.01682 | 2.08 | 0.038* | not applied (n < 1000) | 0.227 | -2.5 | +3.0 | 0.6175 | 0.6130 |
| Nocturnal time > 180 (%) | 230 | OR 1.347 [1.007, 1.803] | 0.01647 | 2.01 | 0.045* | not applied (n < 1000) | 0.248 | -2.3 | +3.2 | 0.6156 | 0.6130 |
| Any reading > 250 during wear (0/1) | 230 | OR 1.184 [0.889, 1.578] | 0.3375 | 1.15 | 0.248 | not applied (n < 1000) | 0.565 | +0.7 | +6.2 | 0.6130 | 0.6130 |
| Time > 250, pooled (%) | 230 | OR 1.406 [0.970, 2.038] | 0.03775 | 1.80 | 0.072 | not applied (n < 1000) | 0.284 | -2.4 | +3.2 | 0.6240 | 0.6130 |
| Avg. daily time > 250 (%) | 230 | OR 1.406 [0.971, 2.035] | 0.04185 | 1.80 | 0.071 | not applied (n < 1000) | 0.284 | -2.3 | +3.2 | 0.6229 | 0.6130 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 230; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 230 | -0.411 [-0.759, -0.064] | -0.3684 | -2.32 | 0.020* | not applied (n < 1000) | 0.184 | -3.3 | +0.0 | 0.0213 | 0.0034 |
| Mean glucose (mg/dL) | 230 | -0.311 [-0.715, +0.094] | -0.009888 | -1.51 | 0.132 | not applied (n < 1000) | 0.413 | -1.1 | +2.2 | 0.0074 | 0.0034 |
| GMI (%) | 230 | -0.311 [-0.715, +0.094] | -0.4134 | -1.51 | 0.132 | not applied (n < 1000) | 0.413 | -1.1 | +2.2 | 0.0074 | 0.0034 |
| Nocturnal mean 00-06h (mg/dL) | 230 | -0.328 [-0.745, +0.090] | -0.0103 | -1.54 | 0.124 | not applied (n < 1000) | 0.398 | -1.5 | +1.8 | 0.0068 | 0.0034 |
| Glucose SD, pooled (mg/dL) | 230 | -0.519 [-0.908, -0.130] | -0.03321 | -2.61 | 0.009** | not applied (n < 1000) | 0.130 | -5.8 | -2.6 | 0.0319 | 0.0034 |
| Avg. daily SD (mg/dL) | 230 | -0.456 [-0.824, -0.088] | -0.03424 | -2.43 | 0.015* | not applied (n < 1000) | 0.169 | -4.0 | -0.7 | 0.0243 | 0.0034 |
| CV (%) | 230 | -0.546 [-0.904, -0.188] | -0.07711 | -2.99 | 0.003** | not applied (n < 1000) | 0.058 | -5.9 | -2.6 | 0.0319 | 0.0034 |
| Mean / SD ratio | 230 | +0.397 [+0.024, +0.770] | 0.2884 | 2.08 | 0.037* | not applied (n < 1000) | 0.226 | -2.3 | +1.0 | 0.0125 | 0.0034 |
| Avg. daily mean / SD | 230 | +0.248 [-0.166, +0.661] | 0.1481 | 1.17 | 0.240 | not applied (n < 1000) | 0.563 | +0.3 | +3.6 | 0.0026 | 0.0034 |
| MAG (mg/dL/h) | 230 | -0.128 [-0.511, +0.255] | -0.01166 | -0.65 | 0.513 | not applied (n < 1000) | 0.770 | +1.5 | +4.8 | -0.0100 | 0.0034 |
| Avg. daily range (mg/dL) | 230 | -0.391 [-0.773, -0.009] | -0.008284 | -2.01 | 0.045* | not applied (n < 1000) | 0.248 | -2.3 | +0.9 | 0.0169 | 0.0034 |
| SD of daily means (mg/dL) | 230 | -0.526 [-0.952, -0.101] | -0.05464 | -2.42 | 0.015* | not applied (n < 1000) | 0.169 | -6.6 | -3.3 | 0.0315 | 0.0034 |
| Time in range 70-180, pooled (%) | 230 | +0.415 [+0.004, +0.826] | 0.02288 | 1.98 | 0.048* | not applied (n < 1000) | 0.253 | -3.4 | -0.1 | 0.0148 | 0.0034 |
| Avg. daily time in range 70-180 (%) | 230 | +0.404 [-0.010, +0.818] | 0.02218 | 1.91 | 0.056 | not applied (n < 1000) | 0.269 | -3.1 | +0.2 | 0.0126 | 0.0034 |
| Time < 54, pooled (%) | 230 | -0.109 [-0.357, +0.139] | -0.1475 | -0.86 | 0.390 | not applied (n < 1000) | 0.685 | +1.6 | +4.9 | -0.0006 | 0.0034 |
| Avg. daily time < 54 (%) | 230 | -0.201 [-0.467, +0.065] | -0.2478 | -1.48 | 0.139 | not applied (n < 1000) | 0.425 | +0.7 | +4.0 | 0.0023 | 0.0034 |
| Time 54-69, pooled (%) | 230 | -0.255 [-0.598, +0.088] | -0.102 | -1.46 | 0.145 | not applied (n < 1000) | 0.435 | -0.0 | +3.2 | 0.0062 | 0.0034 |
| Avg. daily time 54-69 (%) | 230 | -0.317 [-0.667, +0.032] | -0.1209 | -1.78 | 0.075 | not applied (n < 1000) | 0.293 | -1.1 | +2.1 | 0.0097 | 0.0034 |
| Time < 70, pooled (%) | 230 | -0.238 [-0.557, +0.081] | -0.07909 | -1.46 | 0.144 | not applied (n < 1000) | 0.435 | +0.2 | +3.5 | 0.0058 | 0.0034 |
| Avg. daily time < 70 (%) | 230 | -0.311 [-0.639, +0.017] | -0.09719 | -1.86 | 0.063 | not applied (n < 1000) | 0.280 | -1.0 | +2.2 | 0.0098 | 0.0034 |
| Time 54-250, pooled (%) | 230 | +0.419 [-0.068, +0.907] | 0.04615 | 1.69 | 0.092 | not applied (n < 1000) | 0.330 | -3.6 | -0.3 | 0.0213 | 0.0034 |
| Avg. daily time 54-250 (%) | 230 | +0.416 [-0.086, +0.919] | 0.05053 | 1.62 | 0.104 | not applied (n < 1000) | 0.356 | -3.4 | -0.2 | 0.0213 | 0.0034 |
| Time 181-250, pooled (%) | 230 | -0.244 [-0.612, +0.124] | -0.02005 | -1.30 | 0.193 | not applied (n < 1000) | 0.521 | +0.1 | +3.4 | -0.0075 | 0.0034 |
| Avg. daily time 181-250 (%) | 230 | -0.237 [-0.608, +0.134] | -0.01894 | -1.25 | 0.210 | not applied (n < 1000) | 0.537 | +0.2 | +3.5 | -0.0076 | 0.0034 |
| Time > 180, pooled (%) | 230 | -0.365 [-0.777, +0.047] | -0.01988 | -1.74 | 0.082 | not applied (n < 1000) | 0.312 | -2.2 | +1.1 | 0.0106 | 0.0034 |
| Avg. daily time > 180 (%) | 230 | -0.341 [-0.758, +0.075] | -0.01863 | -1.60 | 0.109 | not applied (n < 1000) | 0.359 | -1.6 | +1.6 | 0.0076 | 0.0034 |
| Nocturnal time > 180 (%) | 230 | -0.396 [-0.826, +0.035] | -0.02185 | -1.80 | 0.072 | not applied (n < 1000) | 0.284 | -3.0 | +0.2 | 0.0132 | 0.0034 |
| Any reading > 250 during wear (0/1) | 230 | -0.403 [-0.812, +0.006] | -0.8052 | -1.93 | 0.053 | not applied (n < 1000) | 0.267 | -2.8 | +0.4 | 0.0045 | 0.0034 |
| Time > 250, pooled (%) | 230 | -0.412 [-0.906, +0.082] | -0.04569 | -1.64 | 0.102 | not applied (n < 1000) | 0.354 | -3.4 | -0.1 | 0.0199 | 0.0034 |
| Avg. daily time > 250 (%) | 230 | -0.400 [-0.912, +0.111] | -0.04919 | -1.53 | 0.125 | not applied (n < 1000) | 0.398 | -3.0 | +0.2 | 0.0186 | 0.0034 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 229; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 229 | +0.586 [-0.115, +1.288] | 0.5242 | 1.64 | 0.101 | not applied (n < 1000) | 0.354 | -1.9 | +0.0 | 0.0208 | 0.0289 |
| Mean glucose (mg/dL) | 229 | +0.608 [+0.009, +1.207] | 0.01931 | 1.99 | 0.047* | not applied (n < 1000) | 0.252 | -2.3 | -0.5 | 0.0238 | 0.0289 |
| GMI (%) | 229 | +0.608 [+0.009, +1.207] | 0.8073 | 1.99 | 0.047* | not applied (n < 1000) | 0.252 | -2.3 | -0.5 | 0.0238 | 0.0289 |
| Nocturnal mean 00-06h (mg/dL) | 229 | +0.921 [+0.369, +1.473] | 0.02888 | 3.27 | 0.001** | not applied (n < 1000) | 0.045 (q<0.05) | -8.2 | -6.3 | 0.0379 | 0.0289 |
| Glucose SD, pooled (mg/dL) | 229 | +0.765 [+0.095, +1.434] | 0.04884 | 2.24 | 0.025* | not applied (n < 1000) | 0.195 | -4.2 | -2.3 | 0.0347 | 0.0289 |
| Avg. daily SD (mg/dL) | 229 | +0.635 [-0.038, +1.308] | 0.0476 | 1.85 | 0.064 | not applied (n < 1000) | 0.280 | -2.2 | -0.3 | 0.0249 | 0.0289 |
| CV (%) | 229 | +0.550 [-0.187, +1.287] | 0.07751 | 1.46 | 0.144 | not applied (n < 1000) | 0.435 | -0.9 | +1.0 | 0.0252 | 0.0289 |
| Mean / SD ratio | 229 | -0.465 [-1.169, +0.239] | -0.3374 | -1.29 | 0.196 | not applied (n < 1000) | 0.521 | -0.1 | +1.8 | 0.0232 | 0.0289 |
| Avg. daily mean / SD | 229 | -0.196 [-0.876, +0.483] | -0.1173 | -0.57 | 0.571 | not applied (n < 1000) | 0.827 | +1.6 | +3.5 | 0.0144 | 0.0289 |
| MAG (mg/dL/h) | 229 | +0.529 [-0.116, +1.174] | 0.04826 | 1.61 | 0.108 | not applied (n < 1000) | 0.359 | -1.1 | +0.8 | 0.0252 | 0.0289 |
| Avg. daily range (mg/dL) | 229 | +0.653 [-0.031, +1.338] | 0.01381 | 1.87 | 0.061 | not applied (n < 1000) | 0.278 | -2.4 | -0.5 | 0.0208 | 0.0289 |
| SD of daily means (mg/dL) | 229 | +0.919 [+0.241, +1.596] | 0.09521 | 2.66 | 0.008** | not applied (n < 1000) | 0.124 | -7.5 | -5.6 | 0.0533 | 0.0289 |
| Time in range 70-180, pooled (%) | 229 | -0.673 [-1.284, -0.062] | -0.03703 | -2.16 | 0.031* | not applied (n < 1000) | 0.209 | -3.1 | -1.2 | 0.0323 | 0.0289 |
| Avg. daily time in range 70-180 (%) | 229 | -0.674 [-1.289, -0.059] | -0.03697 | -2.15 | 0.032* | not applied (n < 1000) | 0.209 | -3.1 | -1.2 | 0.0309 | 0.0289 |
| Time < 54, pooled (%) | 229 | -0.195 [-0.777, +0.387] | -0.2639 | -0.66 | 0.511 | not applied (n < 1000) | 0.770 | +1.6 | +3.4 | 0.0123 | 0.0289 |
| Avg. daily time < 54 (%) | 229 | -0.071 [-1.110, +0.967] | -0.08761 | -0.13 | 0.893 | not applied (n < 1000) | 0.952 | +1.9 | +3.8 | 0.0039 | 0.0289 |
| Time 54-69, pooled (%) | 229 | +0.204 [-0.407, +0.814] | 0.08134 | 0.65 | 0.513 | not applied (n < 1000) | 0.770 | +1.5 | +3.4 | 0.0148 | 0.0289 |
| Avg. daily time 54-69 (%) | 229 | +0.247 [-0.383, +0.878] | 0.09411 | 0.77 | 0.442 | not applied (n < 1000) | 0.736 | +1.3 | +3.2 | 0.0149 | 0.0289 |
| Time < 70, pooled (%) | 229 | +0.121 [-0.526, +0.769] | 0.04022 | 0.37 | 0.714 | not applied (n < 1000) | 0.884 | +1.8 | +3.7 | 0.0092 | 0.0289 |
| Avg. daily time < 70 (%) | 229 | +0.184 [-0.508, +0.876] | 0.05742 | 0.52 | 0.602 | not applied (n < 1000) | 0.847 | +1.6 | +3.5 | 0.0104 | 0.0289 |
| Time 54-250, pooled (%) | 229 | -0.980 [-1.425, -0.534] | -0.1076 | -4.31 | 1.6e-05*** | not applied (n < 1000) | 0.003 (q<0.05) | -9.1 | -7.3 | 0.0723 | 0.0289 |
| Avg. daily time 54-250 (%) | 229 | -0.953 [-1.466, -0.439] | -0.1154 | -3.64 | 2.8e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -8.4 | -6.6 | 0.0681 | 0.0289 |
| Time 181-250, pooled (%) | 229 | +0.214 [-0.389, +0.818] | 0.01758 | 0.70 | 0.486 | not applied (n < 1000) | 0.756 | +1.5 | +3.3 | 0.0055 | 0.0289 |
| Avg. daily time 181-250 (%) | 229 | +0.288 [-0.329, +0.905] | 0.02289 | 0.91 | 0.361 | not applied (n < 1000) | 0.659 | +1.1 | +2.9 | 0.0062 | 0.0289 |
| Time > 180, pooled (%) | 229 | +0.635 [+0.027, +1.243] | 0.03452 | 2.05 | 0.041* | not applied (n < 1000) | 0.237 | -2.6 | -0.7 | 0.0286 | 0.0289 |
| Avg. daily time > 180 (%) | 229 | +0.628 [+0.020, +1.236] | 0.03422 | 2.02 | 0.043* | not applied (n < 1000) | 0.247 | -2.5 | -0.6 | 0.0271 | 0.0289 |
| Nocturnal time > 180 (%) | 229 | +0.935 [+0.396, +1.473] | 0.05152 | 3.40 | 6.7e-04*** | not applied (n < 1000) | 0.031 (q<0.05) | -8.3 | -6.5 | 0.0499 | 0.0289 |
| Any reading > 250 during wear (0/1) | 229 | +0.617 [-0.020, +1.253] | 1.231 | 1.90 | 0.058 | not applied (n < 1000) | 0.272 | -2.1 | -0.2 | 0.0366 | 0.0289 |
| Time > 250, pooled (%) | 229 | +0.999 [+0.549, +1.450] | 0.1105 | 4.35 | 1.4e-05*** | not applied (n < 1000) | 0.003 (q<0.05) | -9.6 | -7.8 | 0.0731 | 0.0289 |
| Avg. daily time > 250 (%) | 229 | +0.969 [+0.444, +1.494] | 0.1189 | 3.62 | 3.0e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -8.8 | -7.0 | 0.0684 | 0.0289 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 229; events = 56; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 229 | OR 1.530 [1.119, 2.092] | 0.3802 | 2.67 | 0.008** | not applied (n < 1000) | 0.124 | -5.3 | +0.0 | 0.6788 | 0.6497 |
| Mean glucose (mg/dL) | 229 | OR 1.610 [1.179, 2.197] | 0.01512 | 3.00 | 0.003** | not applied (n < 1000) | 0.058 | -7.5 | -2.2 | 0.6656 | 0.6497 |
| GMI (%) | 229 | OR 1.610 [1.179, 2.197] | 0.6321 | 3.00 | 0.003** | not applied (n < 1000) | 0.058 | -7.5 | -2.2 | 0.6656 | 0.6497 |
| Nocturnal mean 00-06h (mg/dL) | 229 | OR 1.864 [1.339, 2.595] | 0.01952 | 3.69 | 2.2e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -13.5 | -8.3 | 0.6985 | 0.6497 |
| Glucose SD, pooled (mg/dL) | 229 | OR 1.668 [1.195, 2.328] | 0.03266 | 3.01 | 0.003** | not applied (n < 1000) | 0.058 | -7.5 | -2.2 | 0.6771 | 0.6497 |
| Avg. daily SD (mg/dL) | 229 | OR 1.513 [1.088, 2.102] | 0.03102 | 2.46 | 0.014* | not applied (n < 1000) | 0.168 | -4.2 | +1.0 | 0.6587 | 0.6497 |
| CV (%) | 229 | OR 1.411 [0.991, 2.009] | 0.0486 | 1.91 | 0.056 | not applied (n < 1000) | 0.269 | -1.7 | +3.6 | 0.6560 | 0.6497 |
| Mean / SD ratio | 229 | OR 0.716 [0.490, 1.046] | -0.2424 | -1.73 | 0.084 | not applied (n < 1000) | 0.312 | -1.2 | +4.1 | 0.6500 | 0.6497 |
| Avg. daily mean / SD | 229 | OR 0.879 [0.616, 1.254] | -0.07727 | -0.71 | 0.476 | not applied (n < 1000) | 0.754 | +1.5 | +6.8 | 0.6305 | 0.6497 |
| MAG (mg/dL/h) | 229 | OR 1.219 [0.888, 1.673] | 0.01805 | 1.22 | 0.221 | not applied (n < 1000) | 0.552 | +0.5 | +5.8 | 0.6219 | 0.6497 |
| Avg. daily range (mg/dL) | 229 | OR 1.476 [1.059, 2.058] | 0.008237 | 2.30 | 0.021* | not applied (n < 1000) | 0.188 | -3.4 | +1.9 | 0.6518 | 0.6497 |
| SD of daily means (mg/dL) | 229 | OR 1.878 [1.329, 2.652] | 0.06529 | 3.58 | 3.5e-04*** | not applied (n < 1000) | 0.021 (q<0.05) | -12.5 | -7.2 | 0.7024 | 0.6497 |
| Time in range 70-180, pooled (%) | 229 | OR 0.609 [0.447, 0.828] | -0.02732 | -3.16 | 0.002** | not applied (n < 1000) | 0.058 | -8.4 | -3.1 | 0.6795 | 0.6497 |
| Avg. daily time in range 70-180 (%) | 229 | OR 0.610 [0.449, 0.830] | -0.02707 | -3.14 | 0.002** | not applied (n < 1000) | 0.058 | -8.2 | -2.9 | 0.6819 | 0.6497 |
| Time < 54, pooled (%) | 229 | OR 0.861 [0.568, 1.307] | -0.2021 | -0.70 | 0.482 | not applied (n < 1000) | 0.754 | +1.4 | +6.7 | 0.6364 | 0.6497 |
| Avg. daily time < 54 (%) | 229 | OR 1.008 [0.733, 1.386] | 0.009423 | 0.05 | 0.962 | not applied (n < 1000) | 0.976 | +2.0 | +7.3 | 0.6357 | 0.6497 |
| Time 54-69, pooled (%) | 229 | OR 1.018 [0.736, 1.409] | 0.007314 | 0.11 | 0.912 | not applied (n < 1000) | 0.961 | +2.0 | +7.3 | 0.6416 | 0.6497 |
| Avg. daily time 54-69 (%) | 229 | OR 1.052 [0.761, 1.454] | 0.01934 | 0.31 | 0.758 | not applied (n < 1000) | 0.897 | +1.9 | +7.2 | 0.6450 | 0.6497 |
| Time < 70, pooled (%) | 229 | OR 0.986 [0.709, 1.371] | -0.004725 | -0.08 | 0.933 | not applied (n < 1000) | 0.962 | +2.0 | +7.3 | 0.6432 | 0.6497 |
| Avg. daily time < 70 (%) | 229 | OR 1.044 [0.758, 1.438] | 0.01338 | 0.26 | 0.793 | not applied (n < 1000) | 0.908 | +1.9 | +7.2 | 0.6441 | 0.6497 |
| Time 54-250, pooled (%) | 229 | OR 0.524 [0.339, 0.808] | -0.07104 | -2.92 | 0.003** | not applied (n < 1000) | 0.067 | -12.5 | -7.2 | 0.6831 | 0.6497 |
| Avg. daily time 54-250 (%) | 229 | OR 0.523 [0.343, 0.798] | -0.07842 | -3.00 | 0.003** | not applied (n < 1000) | 0.058 | -12.4 | -7.1 | 0.6815 | 0.6497 |
| Time 181-250, pooled (%) | 229 | OR 1.341 [0.989, 1.818] | 0.02405 | 1.89 | 0.059 | not applied (n < 1000) | 0.276 | -1.5 | +3.8 | 0.6577 | 0.6497 |
| Avg. daily time 181-250 (%) | 229 | OR 1.374 [1.014, 1.860] | 0.02527 | 2.05 | 0.040* | not applied (n < 1000) | 0.237 | -2.2 | +3.1 | 0.6641 | 0.6497 |
| Time > 180, pooled (%) | 229 | OR 1.624 [1.197, 2.203] | 0.02636 | 3.12 | 0.002** | not applied (n < 1000) | 0.058 | -8.0 | -2.8 | 0.6748 | 0.6497 |
| Avg. daily time > 180 (%) | 229 | OR 1.611 [1.188, 2.186] | 0.026 | 3.06 | 0.002** | not applied (n < 1000) | 0.058 | -7.7 | -2.4 | 0.6759 | 0.6497 |
| Nocturnal time > 180 (%) | 229 | OR 1.857 [1.353, 2.549] | 0.03413 | 3.83 | 1.3e-04*** | not applied (n < 1000) | 0.018 (q<0.05) | -14.5 | -9.3 | 0.7069 | 0.6497 |
| Any reading > 250 during wear (0/1) | 229 | OR 1.620 [1.133, 2.314] | 0.9626 | 2.65 | 0.008** | not applied (n < 1000) | 0.124 | -5.3 | -0.1 | 0.6745 | 0.6497 |
| Time > 250, pooled (%) | 229 | OR 1.955 [1.252, 3.055] | 0.07419 | 2.95 | 0.003** | not applied (n < 1000) | 0.064 | -13.1 | -7.8 | 0.6869 | 0.6497 |
| Avg. daily time > 250 (%) | 229 | OR 1.960 [1.264, 3.042] | 0.08258 | 3.00 | 0.003** | not applied (n < 1000) | 0.058 | -12.9 | -7.6 | 0.6815 | 0.6497 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 228; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 228 | +0.148 [-0.013, +0.309] | 0.1321 | 1.80 | 0.071 | not applied (n < 1000) | 0.284 | -2.6 | +0.0 | 0.0050 | -0.0010 |
| Mean glucose (mg/dL) | 228 | +0.003 [-0.129, +0.134] | 8.549e-05 | 0.04 | 0.968 | not applied (n < 1000) | 0.977 | +2.0 | +4.6 | -0.0120 | -0.0010 |
| GMI (%) | 228 | +0.003 [-0.129, +0.134] | 0.003574 | 0.04 | 0.968 | not applied (n < 1000) | 0.977 | +2.0 | +4.6 | -0.0120 | -0.0010 |
| Nocturnal mean 00-06h (mg/dL) | 228 | +0.014 [-0.132, +0.160] | 0.0004357 | 0.19 | 0.852 | not applied (n < 1000) | 0.925 | +2.0 | +4.6 | -0.0126 | -0.0010 |
| Glucose SD, pooled (mg/dL) | 228 | +0.037 [-0.108, +0.181] | 0.002346 | 0.50 | 0.619 | not applied (n < 1000) | 0.858 | +1.7 | +4.3 | -0.0188 | -0.0010 |
| Avg. daily SD (mg/dL) | 228 | +0.021 [-0.118, +0.160] | 0.001593 | 0.30 | 0.765 | not applied (n < 1000) | 0.900 | +1.9 | +4.5 | -0.0181 | -0.0010 |
| CV (%) | 228 | +0.070 [-0.102, +0.242] | 0.009908 | 0.80 | 0.425 | not applied (n < 1000) | 0.722 | +1.1 | +3.7 | -0.0284 | -0.0010 |
| Mean / SD ratio | 228 | -0.066 [-0.213, +0.080] | -0.04844 | -0.89 | 0.373 | not applied (n < 1000) | 0.666 | +1.2 | +3.8 | -0.0202 | -0.0010 |
| Avg. daily mean / SD | 228 | -0.064 [-0.206, +0.079] | -0.03817 | -0.88 | 0.381 | not applied (n < 1000) | 0.673 | +1.3 | +3.9 | -0.0171 | -0.0010 |
| MAG (mg/dL/h) | 228 | -0.066 [-0.186, +0.053] | -0.006068 | -1.09 | 0.278 | not applied (n < 1000) | 0.592 | +1.1 | +3.7 | -0.0051 | -0.0010 |
| Avg. daily range (mg/dL) | 228 | +0.001 [-0.135, +0.137] | 2.768e-05 | 0.02 | 0.985 | not applied (n < 1000) | 0.986 | +2.0 | +4.6 | -0.0193 | -0.0010 |
| SD of daily means (mg/dL) | 228 | +0.075 [-0.080, +0.230] | 0.007794 | 0.95 | 0.341 | not applied (n < 1000) | 0.645 | +0.8 | +3.4 | -0.0149 | -0.0010 |
| Time in range 70-180, pooled (%) | 228 | -0.081 [-0.213, +0.050] | -0.004476 | -1.21 | 0.226 | not applied (n < 1000) | 0.556 | +0.6 | +3.2 | -0.0057 | -0.0010 |
| Avg. daily time in range 70-180 (%) | 228 | -0.087 [-0.219, +0.045] | -0.004764 | -1.29 | 0.197 | not applied (n < 1000) | 0.521 | +0.5 | +3.0 | -0.0058 | -0.0010 |
| Time < 54, pooled (%) | 228 | +0.180 [+0.020, +0.340] | 0.2428 | 2.20 | 0.028* | not applied (n < 1000) | 0.204 | -4.9 | -2.3 | 0.0002 | -0.0010 |
| Avg. daily time < 54 (%) | 228 | +0.193 [-0.059, +0.444] | 0.2365 | 1.50 | 0.134 | not applied (n < 1000) | 0.413 | -6.0 | -3.4 | 0.0143 | -0.0010 |
| Time 54-69, pooled (%) | 228 | +0.213 [+0.026, +0.400] | 0.08492 | 2.23 | 0.026* | not applied (n < 1000) | 0.195 | -7.8 | -5.2 | 0.0173 | -0.0010 |
| Avg. daily time 54-69 (%) | 228 | +0.221 [+0.030, +0.411] | 0.08381 | 2.27 | 0.023* | not applied (n < 1000) | 0.188 | -8.4 | -5.8 | 0.0224 | -0.0010 |
| Time < 70, pooled (%) | 228 | +0.221 [+0.045, +0.397] | 0.07313 | 2.46 | 0.014* | not applied (n < 1000) | 0.168 | -8.5 | -5.9 | 0.0205 | -0.0010 |
| Avg. daily time < 70 (%) | 228 | +0.230 [+0.042, +0.418] | 0.0717 | 2.40 | 0.016* | not applied (n < 1000) | 0.169 | -9.4 | -6.8 | 0.0263 | -0.0010 |
| Time 54-250, pooled (%) | 228 | -0.023 [-0.127, +0.080] | -0.002559 | -0.44 | 0.658 | not applied (n < 1000) | 0.867 | +1.9 | +4.5 | -0.0029 | -0.0010 |
| Avg. daily time 54-250 (%) | 228 | -0.040 [-0.152, +0.071] | -0.004878 | -0.71 | 0.478 | not applied (n < 1000) | 0.754 | +1.7 | +4.3 | -0.0017 | -0.0010 |
| Time 181-250, pooled (%) | 228 | +0.058 [-0.097, +0.213] | 0.004746 | 0.73 | 0.464 | not applied (n < 1000) | 0.754 | +1.3 | +3.9 | -0.0186 | -0.0010 |
| Avg. daily time 181-250 (%) | 228 | +0.051 [-0.100, +0.201] | 0.004037 | 0.66 | 0.509 | not applied (n < 1000) | 0.770 | +1.5 | +4.1 | -0.0199 | -0.0010 |
| Time > 180, pooled (%) | 228 | +0.043 [-0.090, +0.175] | 0.002316 | 0.63 | 0.528 | not applied (n < 1000) | 0.786 | +1.6 | +4.2 | -0.0131 | -0.0010 |
| Avg. daily time > 180 (%) | 228 | +0.044 [-0.088, +0.177] | 0.002421 | 0.66 | 0.512 | not applied (n < 1000) | 0.770 | +1.6 | +4.2 | -0.0144 | -0.0010 |
| Nocturnal time > 180 (%) | 228 | +0.084 [-0.062, +0.229] | 0.004599 | 1.12 | 0.261 | not applied (n < 1000) | 0.573 | +0.5 | +3.1 | -0.0050 | -0.0010 |
| Any reading > 250 during wear (0/1) | 228 | -0.030 [-0.184, +0.124] | -0.06021 | -0.38 | 0.701 | not applied (n < 1000) | 0.879 | +1.8 | +4.4 | -0.0289 | -0.0010 |
| Time > 250, pooled (%) | 228 | +0.009 [-0.086, +0.103] | 0.0009529 | 0.18 | 0.858 | not applied (n < 1000) | 0.928 | +2.0 | +4.6 | -0.0040 | -0.0010 |
| Avg. daily time > 250 (%) | 228 | +0.021 [-0.080, +0.122] | 0.002582 | 0.41 | 0.683 | not applied (n < 1000) | 0.867 | +1.9 | +4.5 | -0.0037 | -0.0010 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 228; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 228 | -0.155 [-0.443, +0.132] | -0.1385 | -1.06 | 0.290 | not applied (n < 1000) | 0.616 | +0.8 | +0.0 | 0.1914 | 0.1885 |
| Mean glucose (mg/dL) | 228 | -0.202 [-0.535, +0.131] | -0.00642 | -1.19 | 0.235 | not applied (n < 1000) | 0.562 | -0.1 | -0.9 | 0.1886 | 0.1885 |
| GMI (%) | 228 | -0.202 [-0.535, +0.131] | -0.2684 | -1.19 | 0.235 | not applied (n < 1000) | 0.562 | -0.1 | -0.9 | 0.1886 | 0.1885 |
| Nocturnal mean 00-06h (mg/dL) | 228 | -0.151 [-0.524, +0.222] | -0.004735 | -0.79 | 0.428 | not applied (n < 1000) | 0.722 | +0.8 | +0.0 | 0.1855 | 0.1885 |
| Glucose SD, pooled (mg/dL) | 228 | -0.167 [-0.503, +0.169] | -0.01071 | -0.98 | 0.329 | not applied (n < 1000) | 0.639 | +0.7 | -0.1 | 0.1811 | 0.1885 |
| Avg. daily SD (mg/dL) | 228 | -0.225 [-0.531, +0.081] | -0.01691 | -1.44 | 0.150 | not applied (n < 1000) | 0.446 | -0.3 | -1.1 | 0.1861 | 0.1885 |
| CV (%) | 228 | -0.050 [-0.400, +0.300] | -0.007054 | -0.28 | 0.780 | not applied (n < 1000) | 0.908 | +1.9 | +1.1 | 0.1773 | 0.1885 |
| Mean / SD ratio | 228 | +0.067 [-0.299, +0.433] | 0.04861 | 0.36 | 0.721 | not applied (n < 1000) | 0.888 | +1.8 | +1.0 | 0.1784 | 0.1885 |
| Avg. daily mean / SD | 228 | +0.135 [-0.227, +0.498] | 0.08124 | 0.73 | 0.464 | not applied (n < 1000) | 0.754 | +1.2 | +0.4 | 0.1816 | 0.1885 |
| MAG (mg/dL/h) | 228 | -0.148 [-0.428, +0.132] | -0.01357 | -1.04 | 0.300 | not applied (n < 1000) | 0.624 | +0.9 | +0.1 | 0.1770 | 0.1885 |
| Avg. daily range (mg/dL) | 228 | -0.220 [-0.528, +0.087] | -0.004677 | -1.40 | 0.160 | not applied (n < 1000) | 0.464 | -0.2 | -1.0 | 0.1848 | 0.1885 |
| SD of daily means (mg/dL) | 228 | -0.028 [-0.468, +0.412] | -0.002876 | -0.12 | 0.901 | not applied (n < 1000) | 0.956 | +2.0 | +1.2 | 0.1750 | 0.1885 |
| Time in range 70-180, pooled (%) | 228 | +0.155 [-0.166, +0.476] | 0.00854 | 0.95 | 0.344 | not applied (n < 1000) | 0.645 | +0.8 | +0.0 | 0.1849 | 0.1885 |
| Avg. daily time in range 70-180 (%) | 228 | +0.145 [-0.178, +0.468] | 0.00794 | 0.88 | 0.380 | not applied (n < 1000) | 0.673 | +1.0 | +0.2 | 0.1841 | 0.1885 |
| Time < 54, pooled (%) | 228 | +0.079 [-0.182, +0.341] | 0.1067 | 0.59 | 0.553 | not applied (n < 1000) | 0.817 | +1.7 | +0.9 | 0.1785 | 0.1885 |
| Avg. daily time < 54 (%) | 228 | +0.084 [-0.282, +0.449] | 0.1028 | 0.45 | 0.653 | not applied (n < 1000) | 0.867 | +1.6 | +0.8 | 0.1768 | 0.1885 |
| Time 54-69, pooled (%) | 228 | +0.249 [-0.033, +0.531] | 0.09937 | 1.73 | 0.084 | not applied (n < 1000) | 0.312 | -1.2 | -2.0 | 0.1861 | 0.1885 |
| Avg. daily time 54-69 (%) | 228 | +0.271 [-0.007, +0.549] | 0.1029 | 1.91 | 0.056 | not applied (n < 1000) | 0.269 | -1.7 | -2.5 | 0.1892 | 0.1885 |
| Time < 70, pooled (%) | 228 | +0.226 [-0.062, +0.514] | 0.07489 | 1.54 | 0.124 | not applied (n < 1000) | 0.398 | -0.6 | -1.4 | 0.1831 | 0.1885 |
| Avg. daily time < 70 (%) | 228 | +0.243 [-0.060, +0.546] | 0.07581 | 1.57 | 0.115 | not applied (n < 1000) | 0.378 | -1.0 | -1.8 | 0.1865 | 0.1885 |
| Time 54-250, pooled (%) | 228 | +0.098 [-0.293, +0.489] | 0.01075 | 0.49 | 0.623 | not applied (n < 1000) | 0.858 | +1.5 | +0.7 | 0.1745 | 0.1885 |
| Avg. daily time 54-250 (%) | 228 | +0.089 [-0.323, +0.500] | 0.01071 | 0.42 | 0.673 | not applied (n < 1000) | 0.867 | +1.6 | +0.8 | 0.1720 | 0.1885 |
| Time 181-250, pooled (%) | 228 | -0.206 [-0.489, +0.076] | -0.01694 | -1.43 | 0.152 | not applied (n < 1000) | 0.447 | -0.1 | -0.9 | 0.1920 | 0.1885 |
| Avg. daily time 181-250 (%) | 228 | -0.205 [-0.486, +0.077] | -0.0163 | -1.42 | 0.154 | not applied (n < 1000) | 0.450 | -0.1 | -0.9 | 0.1914 | 0.1885 |
| Time > 180, pooled (%) | 228 | -0.189 [-0.510, +0.133] | -0.01026 | -1.15 | 0.250 | not applied (n < 1000) | 0.565 | +0.2 | -0.6 | 0.1878 | 0.1885 |
| Avg. daily time > 180 (%) | 228 | -0.185 [-0.509, +0.139] | -0.01009 | -1.12 | 0.262 | not applied (n < 1000) | 0.573 | +0.3 | -0.5 | 0.1878 | 0.1885 |
| Nocturnal time > 180 (%) | 228 | -0.133 [-0.496, +0.229] | -0.007347 | -0.72 | 0.470 | not applied (n < 1000) | 0.754 | +1.1 | +0.3 | 0.1811 | 0.1885 |
| Any reading > 250 during wear (0/1) | 228 | -0.108 [-0.408, +0.191] | -0.2161 | -0.71 | 0.479 | not applied (n < 1000) | 0.754 | +1.4 | +0.6 | 0.1823 | 0.1885 |
| Time > 250, pooled (%) | 228 | -0.105 [-0.503, +0.293] | -0.0116 | -0.52 | 0.605 | not applied (n < 1000) | 0.847 | +1.4 | +0.6 | 0.1753 | 0.1885 |
| Avg. daily time > 250 (%) | 228 | -0.098 [-0.522, +0.326] | -0.01203 | -0.45 | 0.649 | not applied (n < 1000) | 0.867 | +1.5 | +0.7 | 0.1720 | 0.1885 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 228; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 228 | +0.465 [-0.493, +1.423] | 0.4154 | 0.95 | 0.341 | not applied (n < 1000) | 0.645 | +0.9 | +0.0 | -0.0074 | -0.0000 |
| Mean glucose (mg/dL) | 228 | +0.567 [-0.302, +1.436] | 0.01802 | 1.28 | 0.201 | not applied (n < 1000) | 0.521 | +0.3 | -0.6 | -0.0032 | -0.0000 |
| GMI (%) | 228 | +0.567 [-0.302, +1.436] | 0.7531 | 1.28 | 0.201 | not applied (n < 1000) | 0.521 | +0.3 | -0.6 | -0.0032 | -0.0000 |
| Nocturnal mean 00-06h (mg/dL) | 228 | +0.192 [-0.666, +1.050] | 0.00601 | 0.44 | 0.662 | not applied (n < 1000) | 0.867 | +1.8 | +0.9 | -0.0125 | -0.0000 |
| Glucose SD, pooled (mg/dL) | 228 | +0.393 [-0.514, +1.300] | 0.02513 | 0.85 | 0.396 | not applied (n < 1000) | 0.693 | +1.3 | +0.4 | -0.0037 | -0.0000 |
| Avg. daily SD (mg/dL) | 228 | +0.540 [-0.333, +1.413] | 0.04053 | 1.21 | 0.226 | not applied (n < 1000) | 0.556 | +0.7 | -0.3 | -0.0001 | -0.0000 |
| CV (%) | 228 | +0.150 [-0.900, +1.200] | 0.02124 | 0.28 | 0.779 | not applied (n < 1000) | 0.908 | +1.9 | +1.0 | -0.0039 | -0.0000 |
| Mean / SD ratio | 228 | -0.161 [-1.176, +0.853] | -0.1176 | -0.31 | 0.755 | not applied (n < 1000) | 0.896 | +1.9 | +1.0 | -0.0071 | -0.0000 |
| Avg. daily mean / SD | 228 | -0.313 [-1.234, +0.608] | -0.1875 | -0.67 | 0.506 | not applied (n < 1000) | 0.770 | +1.6 | +0.7 | -0.0054 | -0.0000 |
| MAG (mg/dL/h) | 228 | +0.106 [-0.707, +0.920] | 0.009714 | 0.26 | 0.798 | not applied (n < 1000) | 0.908 | +1.9 | +1.0 | -0.0053 | -0.0000 |
| Avg. daily range (mg/dL) | 228 | +0.453 [-0.418, +1.325] | 0.009629 | 1.02 | 0.308 | not applied (n < 1000) | 0.625 | +1.1 | +0.1 | -0.0028 | -0.0000 |
| SD of daily means (mg/dL) | 228 | +0.065 [-0.878, +1.009] | 0.00675 | 0.14 | 0.892 | not applied (n < 1000) | 0.952 | +2.0 | +1.1 | -0.0117 | -0.0000 |
| Time in range 70-180, pooled (%) | 228 | -0.595 [-1.506, +0.317] | -0.03275 | -1.28 | 0.201 | not applied (n < 1000) | 0.521 | +0.2 | -0.7 | -0.0049 | -0.0000 |
| Avg. daily time in range 70-180 (%) | 228 | -0.589 [-1.526, +0.349] | -0.03228 | -1.23 | 0.218 | not applied (n < 1000) | 0.549 | +0.3 | -0.6 | -0.0062 | -0.0000 |
| Time < 54, pooled (%) | 228 | -0.321 [-1.784, +1.143] | -0.4329 | -0.43 | 0.667 | not applied (n < 1000) | 0.867 | +1.5 | +0.6 | -0.0121 | -0.0000 |
| Avg. daily time < 54 (%) | 228 | -0.360 [-1.563, +0.843] | -0.4418 | -0.59 | 0.558 | not applied (n < 1000) | 0.817 | +1.3 | +0.4 | -0.0050 | -0.0000 |
| Time 54-69, pooled (%) | 228 | -0.045 [-1.078, +0.988] | -0.01789 | -0.09 | 0.932 | not applied (n < 1000) | 0.962 | +2.0 | +1.1 | -0.0075 | -0.0000 |
| Avg. daily time 54-69 (%) | 228 | -0.131 [-1.145, +0.883] | -0.04978 | -0.25 | 0.800 | not applied (n < 1000) | 0.908 | +1.9 | +1.0 | -0.0065 | -0.0000 |
| Time < 70, pooled (%) | 228 | -0.116 [-1.123, +0.892] | -0.03838 | -0.23 | 0.822 | not applied (n < 1000) | 0.912 | +1.9 | +1.0 | -0.0066 | -0.0000 |
| Avg. daily time < 70 (%) | 228 | -0.200 [-1.174, +0.774] | -0.06219 | -0.40 | 0.688 | not applied (n < 1000) | 0.867 | +1.8 | +0.9 | -0.0048 | -0.0000 |
| Time 54-250, pooled (%) | 228 | -0.348 [-1.099, +0.403] | -0.03818 | -0.91 | 0.364 | not applied (n < 1000) | 0.659 | +1.4 | +0.5 | -0.0040 | -0.0000 |
| Avg. daily time 54-250 (%) | 228 | -0.399 [-1.252, +0.455] | -0.04819 | -0.92 | 0.360 | not applied (n < 1000) | 0.659 | +1.2 | +0.3 | -0.0051 | -0.0000 |
| Time 181-250, pooled (%) | 228 | +0.623 [-0.355, +1.602] | 0.05115 | 1.25 | 0.212 | not applied (n < 1000) | 0.539 | +0.0 | -0.9 | -0.0064 | -0.0000 |
| Avg. daily time 181-250 (%) | 228 | +0.604 [-0.374, +1.581] | 0.04808 | 1.21 | 0.226 | not applied (n < 1000) | 0.556 | +0.1 | -0.8 | -0.0074 | -0.0000 |
| Time > 180, pooled (%) | 228 | +0.599 [-0.311, +1.509] | 0.03257 | 1.29 | 0.197 | not applied (n < 1000) | 0.521 | +0.2 | -0.7 | -0.0055 | -0.0000 |
| Avg. daily time > 180 (%) | 228 | +0.613 [-0.325, +1.550] | 0.0334 | 1.28 | 0.200 | not applied (n < 1000) | 0.521 | +0.1 | -0.8 | -0.0061 | -0.0000 |
| Nocturnal time > 180 (%) | 228 | +0.047 [-0.857, +0.951] | 0.002602 | 0.10 | 0.918 | not applied (n < 1000) | 0.961 | +2.0 | +1.1 | -0.0165 | -0.0000 |
| Any reading > 250 during wear (0/1) | 228 | +0.073 [-0.858, +1.004] | 0.146 | 0.15 | 0.878 | not applied (n < 1000) | 0.948 | +2.0 | +1.1 | -0.0047 | -0.0000 |
| Time > 250, pooled (%) | 228 | +0.376 [-0.391, +1.144] | 0.04155 | 0.96 | 0.337 | not applied (n < 1000) | 0.645 | +1.3 | +0.4 | -0.0036 | -0.0000 |
| Avg. daily time > 250 (%) | 228 | +0.440 [-0.444, +1.325] | 0.05392 | 0.98 | 0.329 | not applied (n < 1000) | 0.639 | +1.0 | +0.1 | -0.0038 | -0.0000 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 228; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 228 | -2.167 [-6.535, +2.201] | -1.935 | -0.97 | 0.331 | not applied (n < 1000) | 0.639 | -0.9 | +0.0 | -0.0662 | -0.0561 |
| Mean glucose (mg/dL) | 228 | -1.459 [-5.651, +2.734] | -0.04635 | -0.68 | 0.495 | not applied (n < 1000) | 0.762 | +0.7 | +1.6 | -0.0938 | -0.0561 |
| GMI (%) | 228 | -1.459 [-5.651, +2.734] | -1.938 | -0.68 | 0.495 | not applied (n < 1000) | 0.762 | +0.7 | +1.6 | -0.0938 | -0.0561 |
| Nocturnal mean 00-06h (mg/dL) | 228 | -2.499 [-7.242, +2.244] | -0.07842 | -1.03 | 0.302 | not applied (n < 1000) | 0.624 | -2.0 | -1.1 | -0.0949 | -0.0561 |
| Glucose SD, pooled (mg/dL) | 228 | -1.481 [-5.025, +2.063] | -0.09481 | -0.82 | 0.413 | not applied (n < 1000) | 0.709 | +0.7 | +1.6 | -0.0736 | -0.0561 |
| Avg. daily SD (mg/dL) | 228 | -0.479 [-3.177, +2.220] | -0.03596 | -0.35 | 0.728 | not applied (n < 1000) | 0.888 | +1.9 | +2.8 | -0.0699 | -0.0561 |
| CV (%) | 228 | -0.153 [-2.965, +2.658] | -0.02168 | -0.11 | 0.915 | not applied (n < 1000) | 0.961 | +2.0 | +2.9 | -0.0600 | -0.0561 |
| Mean / SD ratio | 228 | -0.290 [-3.014, +2.435] | -0.2112 | -0.21 | 0.835 | not applied (n < 1000) | 0.913 | +2.0 | +2.9 | -0.0628 | -0.0561 |
| Avg. daily mean / SD | 228 | -1.159 [-3.709, +1.390] | -0.6956 | -0.89 | 0.373 | not applied (n < 1000) | 0.666 | +1.3 | +2.2 | -0.0618 | -0.0561 |
| MAG (mg/dL/h) | 228 | +1.644 [-1.204, +4.493] | 0.1506 | 1.13 | 0.258 | not applied (n < 1000) | 0.573 | +0.3 | +1.2 | -0.0615 | -0.0561 |
| Avg. daily range (mg/dL) | 228 | +0.575 [-2.193, +3.344] | 0.01221 | 0.41 | 0.684 | not applied (n < 1000) | 0.867 | +1.8 | +2.7 | -0.0623 | -0.0561 |
| SD of daily means (mg/dL) | 228 | -3.785 [-9.233, +1.663] | -0.3916 | -1.36 | 0.173 | not applied (n < 1000) | 0.492 | -6.8 | -5.9 | -0.0627 | -0.0561 |
| Time in range 70-180, pooled (%) | 228 | +0.795 [-3.754, +5.344] | 0.04379 | 0.34 | 0.732 | not applied (n < 1000) | 0.888 | +1.6 | +2.5 | -0.0930 | -0.0561 |
| Avg. daily time in range 70-180 (%) | 228 | +0.956 [-3.625, +5.537] | 0.05244 | 0.41 | 0.683 | not applied (n < 1000) | 0.867 | +1.4 | +2.4 | -0.0946 | -0.0561 |
| Time < 54, pooled (%) | 228 | +0.868 [-0.869, +2.605] | 1.171 | 0.98 | 0.328 | not applied (n < 1000) | 0.639 | +1.5 | +2.4 | -0.0682 | -0.0561 |
| Avg. daily time < 54 (%) | 228 | +1.157 [-0.793, +3.107] | 1.42 | 1.16 | 0.245 | not applied (n < 1000) | 0.565 | +1.2 | +2.1 | -0.0609 | -0.0561 |
| Time 54-69, pooled (%) | 228 | +1.242 [-0.933, +3.417] | 0.4954 | 1.12 | 0.263 | not applied (n < 1000) | 0.573 | +1.0 | +1.9 | -0.0648 | -0.0561 |
| Avg. daily time 54-69 (%) | 228 | +1.052 [-1.062, +3.165] | 0.3992 | 0.98 | 0.329 | not applied (n < 1000) | 0.639 | +1.3 | +2.2 | -0.0641 | -0.0561 |
| Time < 70, pooled (%) | 228 | +1.243 [-0.814, +3.300] | 0.4118 | 1.18 | 0.236 | not applied (n < 1000) | 0.562 | +1.0 | +1.9 | -0.0654 | -0.0561 |
| Avg. daily time < 70 (%) | 228 | +1.158 [-0.812, +3.128] | 0.3606 | 1.15 | 0.249 | not applied (n < 1000) | 0.565 | +1.2 | +2.1 | -0.0630 | -0.0561 |
| Time 54-250, pooled (%) | 228 | +2.933 [-2.123, +7.989] | 0.3217 | 1.14 | 0.256 | not applied (n < 1000) | 0.571 | -3.4 | -2.5 | -0.0977 | -0.0561 |
| Avg. daily time 54-250 (%) | 228 | +3.183 [-2.005, +8.371] | 0.3848 | 1.20 | 0.229 | not applied (n < 1000) | 0.560 | -4.3 | -3.4 | -0.1028 | -0.0561 |
| Time 181-250, pooled (%) | 228 | +0.771 [-3.764, +5.305] | 0.06323 | 0.33 | 0.739 | not applied (n < 1000) | 0.895 | +1.6 | +2.5 | -0.0890 | -0.0561 |
| Avg. daily time 181-250 (%) | 228 | +0.487 [-3.885, +4.860] | 0.03881 | 0.22 | 0.827 | not applied (n < 1000) | 0.912 | +1.9 | +2.8 | -0.0895 | -0.0561 |
| Time > 180, pooled (%) | 228 | -0.982 [-5.553, +3.589] | -0.05339 | -0.42 | 0.674 | not applied (n < 1000) | 0.867 | +1.4 | +2.3 | -0.0949 | -0.0561 |
| Avg. daily time > 180 (%) | 228 | -1.143 [-5.759, +3.472] | -0.06231 | -0.49 | 0.627 | not applied (n < 1000) | 0.858 | +1.2 | +2.1 | -0.0964 | -0.0561 |
| Nocturnal time > 180 (%) | 228 | -1.588 [-7.088, +3.911] | -0.08748 | -0.57 | 0.571 | not applied (n < 1000) | 0.827 | +0.4 | +1.3 | -0.0963 | -0.0561 |
| Any reading > 250 during wear (0/1) | 228 | +1.312 [-1.535, +4.158] | 2.62 | 0.90 | 0.367 | not applied (n < 1000) | 0.661 | +1.0 | +1.9 | -0.0586 | -0.0561 |
| Time > 250, pooled (%) | 228 | -3.019 [-8.121, +2.082] | -0.3334 | -1.16 | 0.246 | not applied (n < 1000) | 0.565 | -3.7 | -2.8 | -0.0994 | -0.0561 |
| Avg. daily time > 250 (%) | 228 | -3.340 [-8.618, +1.937] | -0.409 | -1.24 | 0.215 | not applied (n < 1000) | 0.543 | -4.9 | -4.0 | -0.1039 | -0.0561 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 201; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 201 | +474.032 [-436.998, +1385.062] | 413.3 | 1.02 | 0.308 | not applied (n < 1000) | 0.625 | +0.0 | +0.0 | 0.1015 | 0.1009 |
| Mean glucose (mg/dL) | 201 | -150.775 [-844.651, +543.102] | -4.683 | -0.43 | 0.670 | not applied (n < 1000) | 0.867 | +1.8 | +1.8 | 0.0958 | 0.1009 |
| GMI (%) | 201 | -150.775 [-844.651, +543.102] | -195.8 | -0.43 | 0.670 | not applied (n < 1000) | 0.867 | +1.8 | +1.8 | 0.0958 | 0.1009 |
| Nocturnal mean 00-06h (mg/dL) | 201 | +7.043 [-673.332, +687.418] | 0.2134 | 0.02 | 0.984 | not applied (n < 1000) | 0.986 | +2.0 | +2.0 | 0.0951 | 0.1009 |
| Glucose SD, pooled (mg/dL) | 201 | -358.223 [-1029.834, +313.388] | -22.66 | -1.05 | 0.296 | not applied (n < 1000) | 0.618 | +1.0 | +0.9 | 0.0991 | 0.1009 |
| Avg. daily SD (mg/dL) | 201 | -451.661 [-1085.170, +181.847] | -33.58 | -1.40 | 0.162 | not applied (n < 1000) | 0.467 | +0.4 | +0.3 | 0.1016 | 0.1009 |
| CV (%) | 201 | -361.912 [-1012.707, +288.884] | -50.9 | -1.09 | 0.276 | not applied (n < 1000) | 0.591 | +1.0 | +1.0 | 0.0962 | 0.1009 |
| Mean / SD ratio | 201 | +24.538 [-615.613, +664.690] | 17.56 | 0.08 | 0.940 | not applied (n < 1000) | 0.963 | +2.0 | +2.0 | 0.0897 | 0.1009 |
| Avg. daily mean / SD | 201 | +24.888 [-570.622, +620.398] | 14.7 | 0.08 | 0.935 | not applied (n < 1000) | 0.962 | +2.0 | +2.0 | 0.0897 | 0.1009 |
| MAG (mg/dL/h) | 201 | +123.325 [-650.125, +896.776] | 10.98 | 0.31 | 0.755 | not applied (n < 1000) | 0.896 | +1.9 | +1.8 | 0.0910 | 0.1009 |
| Avg. daily range (mg/dL) | 201 | -320.321 [-1011.669, +371.026] | -6.704 | -0.91 | 0.364 | not applied (n < 1000) | 0.659 | +1.2 | +1.2 | 0.0961 | 0.1009 |
| SD of daily means (mg/dL) | 201 | +31.395 [-711.257, +774.048] | 3.215 | 0.08 | 0.934 | not applied (n < 1000) | 0.962 | +2.0 | +2.0 | 0.0927 | 0.1009 |
| Time in range 70-180, pooled (%) | 201 | +337.085 [-342.861, +1017.031] | 18.25 | 0.97 | 0.331 | not applied (n < 1000) | 0.639 | +1.0 | +1.0 | 0.1019 | 0.1009 |
| Avg. daily time in range 70-180 (%) | 201 | +332.537 [-349.831, +1014.904] | 17.95 | 0.96 | 0.340 | not applied (n < 1000) | 0.645 | +1.0 | +1.0 | 0.1013 | 0.1009 |
| Time < 54, pooled (%) | 201 | -387.135 [-970.462, +196.191] | -495 | -1.30 | 0.193 | not applied (n < 1000) | 0.521 | +0.7 | +0.7 | 0.1023 | 0.1009 |
| Avg. daily time < 54 (%) | 201 | -468.599 [-965.646, +28.447] | -542.2 | -1.85 | 0.065 | not applied (n < 1000) | 0.280 | +0.0 | +0.0 | 0.1051 | 0.1009 |
| Time 54-69, pooled (%) | 201 | -320.453 [-854.823, +213.917] | -125 | -1.18 | 0.240 | not applied (n < 1000) | 0.563 | +1.1 | +1.1 | 0.1014 | 0.1009 |
| Avg. daily time 54-69 (%) | 201 | -353.201 [-869.540, +163.138] | -129.6 | -1.34 | 0.180 | not applied (n < 1000) | 0.506 | +0.9 | +0.9 | 0.1035 | 0.1009 |
| Time < 70, pooled (%) | 201 | -359.963 [-873.345, +153.419] | -115.5 | -1.37 | 0.169 | not applied (n < 1000) | 0.484 | +0.9 | +0.8 | 0.1031 | 0.1009 |
| Avg. daily time < 70 (%) | 201 | -409.278 [-888.526, +69.970] | -122.3 | -1.67 | 0.094 | not applied (n < 1000) | 0.335 | +0.5 | +0.5 | 0.1061 | 0.1009 |
| Time 54-250, pooled (%) | 201 | +363.885 [-275.414, +1003.185] | 38.53 | 1.12 | 0.265 | not applied (n < 1000) | 0.573 | +0.8 | +0.8 | 0.1016 | 0.1009 |
| Avg. daily time 54-250 (%) | 201 | +276.677 [-378.516, +931.871] | 32.58 | 0.83 | 0.408 | not applied (n < 1000) | 0.705 | +1.3 | +1.3 | 0.0986 | 0.1009 |
| Time 181-250, pooled (%) | 201 | -151.624 [-860.712, +557.463] | -12.33 | -0.42 | 0.675 | not applied (n < 1000) | 0.867 | +1.8 | +1.8 | 0.0971 | 0.1009 |
| Avg. daily time 181-250 (%) | 201 | -216.638 [-908.272, +474.995] | -17.08 | -0.61 | 0.539 | not applied (n < 1000) | 0.800 | +1.6 | +1.6 | 0.0979 | 0.1009 |
| Time > 180, pooled (%) | 201 | -267.726 [-952.119, +416.666] | -14.32 | -0.77 | 0.443 | not applied (n < 1000) | 0.736 | +1.4 | +1.3 | 0.0999 | 0.1009 |
| Avg. daily time > 180 (%) | 201 | -251.730 [-935.323, +431.864] | -13.52 | -0.72 | 0.470 | not applied (n < 1000) | 0.754 | +1.4 | +1.4 | 0.0994 | 0.1009 |
| Nocturnal time > 180 (%) | 201 | -281.705 [-993.834, +430.424] | -14.91 | -0.78 | 0.438 | not applied (n < 1000) | 0.736 | +1.3 | +1.3 | 0.0981 | 0.1009 |
| Any reading > 250 during wear (0/1) | 201 | +251.034 [-489.156, +991.224] | 501.1 | 0.66 | 0.506 | not applied (n < 1000) | 0.770 | +1.5 | +1.5 | 0.1028 | 0.1009 |
| Time > 250, pooled (%) | 201 | -333.630 [-973.976, +306.715] | -35.59 | -1.02 | 0.307 | not applied (n < 1000) | 0.625 | +1.0 | +1.0 | 0.1008 | 0.1009 |
| Avg. daily time > 250 (%) | 201 | -231.025 [-874.172, +412.122] | -27.59 | -0.70 | 0.481 | not applied (n < 1000) | 0.754 | +1.5 | +1.5 | 0.0974 | 0.1009 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 201; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 201 | +1.770 [-0.883, +4.424] | 1.543 | 1.31 | 0.191 | not applied (n < 1000) | 0.521 | -1.4 | +0.0 | 0.1241 | 0.1144 |
| Mean glucose (mg/dL) | 201 | -0.239 [-2.436, +1.957] | -0.007433 | -0.21 | 0.831 | not applied (n < 1000) | 0.912 | +1.9 | +3.4 | 0.1081 | 0.1144 |
| GMI (%) | 201 | -0.239 [-2.436, +1.957] | -0.3107 | -0.21 | 0.831 | not applied (n < 1000) | 0.912 | +1.9 | +3.4 | 0.1081 | 0.1144 |
| Nocturnal mean 00-06h (mg/dL) | 201 | +0.295 [-1.883, +2.472] | 0.008929 | 0.27 | 0.791 | not applied (n < 1000) | 0.908 | +1.9 | +3.3 | 0.1101 | 0.1144 |
| Glucose SD, pooled (mg/dL) | 201 | -0.889 [-3.028, +1.250] | -0.05624 | -0.81 | 0.415 | not applied (n < 1000) | 0.709 | +1.2 | +2.6 | 0.1117 | 0.1144 |
| Avg. daily SD (mg/dL) | 201 | -1.321 [-3.256, +0.613] | -0.09821 | -1.34 | 0.181 | not applied (n < 1000) | 0.506 | +0.3 | +1.7 | 0.1171 | 0.1144 |
| CV (%) | 201 | -1.065 [-2.933, +0.803] | -0.1498 | -1.12 | 0.264 | not applied (n < 1000) | 0.573 | +1.0 | +2.4 | 0.1134 | 0.1144 |
| Mean / SD ratio | 201 | +0.274 [-1.493, +2.040] | 0.1959 | 0.30 | 0.761 | not applied (n < 1000) | 0.898 | +1.9 | +3.4 | 0.1065 | 0.1144 |
| Avg. daily mean / SD | 201 | +0.407 [-1.259, +2.074] | 0.2406 | 0.48 | 0.632 | not applied (n < 1000) | 0.859 | +1.8 | +3.3 | 0.1055 | 0.1144 |
| MAG (mg/dL/h) | 201 | +0.108 [-2.232, +2.448] | 0.009633 | 0.09 | 0.928 | not applied (n < 1000) | 0.962 | +2.0 | +3.4 | 0.0972 | 0.1144 |
| Avg. daily range (mg/dL) | 201 | -0.986 [-3.051, +1.078] | -0.02065 | -0.94 | 0.349 | not applied (n < 1000) | 0.646 | +1.0 | +2.5 | 0.1114 | 0.1144 |
| SD of daily means (mg/dL) | 201 | +0.527 [-1.877, +2.930] | 0.05395 | 0.43 | 0.668 | not applied (n < 1000) | 0.867 | +1.7 | +3.1 | 0.1066 | 0.1144 |
| Time in range 70-180, pooled (%) | 201 | +0.626 [-1.595, +2.848] | 0.0339 | 0.55 | 0.581 | not applied (n < 1000) | 0.838 | +1.6 | +3.0 | 0.1096 | 0.1144 |
| Avg. daily time in range 70-180 (%) | 201 | +0.619 [-1.602, +2.840] | 0.03343 | 0.55 | 0.585 | not applied (n < 1000) | 0.840 | +1.6 | +3.0 | 0.1090 | 0.1144 |
| Time < 54, pooled (%) | 201 | -0.915 [-3.266, +1.436] | -1.17 | -0.76 | 0.446 | not applied (n < 1000) | 0.736 | +1.1 | +2.5 | 0.1096 | 0.1144 |
| Avg. daily time < 54 (%) | 201 | -1.183 [-3.285, +0.920] | -1.368 | -1.10 | 0.270 | not applied (n < 1000) | 0.582 | +0.5 | +1.9 | 0.1100 | 0.1144 |
| Time 54-69, pooled (%) | 201 | -0.578 [-1.965, +0.810] | -0.2254 | -0.82 | 0.414 | not applied (n < 1000) | 0.709 | +1.6 | +3.1 | 0.1131 | 0.1144 |
| Avg. daily time 54-69 (%) | 201 | -0.683 [-2.111, +0.746] | -0.2504 | -0.94 | 0.349 | not applied (n < 1000) | 0.646 | +1.5 | +2.9 | 0.1137 | 0.1144 |
| Time < 70, pooled (%) | 201 | -0.703 [-2.123, +0.717] | -0.2257 | -0.97 | 0.332 | not applied (n < 1000) | 0.639 | +1.5 | +2.9 | 0.1134 | 0.1144 |
| Avg. daily time < 70 (%) | 201 | -0.863 [-2.328, +0.602] | -0.2579 | -1.15 | 0.248 | not applied (n < 1000) | 0.565 | +1.2 | +2.6 | 0.1141 | 0.1144 |
| Time 54-250, pooled (%) | 201 | +0.595 [-1.817, +3.006] | 0.06294 | 0.48 | 0.629 | not applied (n < 1000) | 0.858 | +1.6 | +3.0 | 0.1063 | 0.1144 |
| Avg. daily time 54-250 (%) | 201 | +0.284 [-2.075, +2.643] | 0.03342 | 0.24 | 0.814 | not applied (n < 1000) | 0.912 | +1.9 | +3.3 | 0.1042 | 0.1144 |
| Time 181-250, pooled (%) | 201 | -0.349 [-2.485, +1.787] | -0.02839 | -0.32 | 0.749 | not applied (n < 1000) | 0.896 | +1.9 | +3.3 | 0.1073 | 0.1144 |
| Avg. daily time 181-250 (%) | 201 | -0.554 [-2.654, +1.546] | -0.04368 | -0.52 | 0.605 | not applied (n < 1000) | 0.847 | +1.7 | +3.1 | 0.1081 | 0.1144 |
| Time > 180, pooled (%) | 201 | -0.491 [-2.702, +1.719] | -0.02629 | -0.44 | 0.663 | not applied (n < 1000) | 0.867 | +1.7 | +3.2 | 0.1087 | 0.1144 |
| Avg. daily time > 180 (%) | 201 | -0.451 [-2.655, +1.753] | -0.02421 | -0.40 | 0.689 | not applied (n < 1000) | 0.867 | +1.8 | +3.2 | 0.1079 | 0.1144 |
| Nocturnal time > 180 (%) | 201 | -0.419 [-2.781, +1.943] | -0.02219 | -0.35 | 0.728 | not applied (n < 1000) | 0.888 | +1.8 | +3.2 | 0.1070 | 0.1144 |
| Any reading > 250 during wear (0/1) | 201 | +0.560 [-1.554, +2.673] | 1.117 | 0.52 | 0.604 | not applied (n < 1000) | 0.847 | +1.7 | +3.1 | 0.1143 | 0.1144 |
| Time > 250, pooled (%) | 201 | -0.522 [-2.926, +1.882] | -0.05568 | -0.43 | 0.670 | not applied (n < 1000) | 0.867 | +1.7 | +3.1 | 0.1056 | 0.1144 |
| Avg. daily time > 250 (%) | 201 | -0.165 [-2.491, +2.162] | -0.01966 | -0.14 | 0.890 | not applied (n < 1000) | 0.952 | +2.0 | +3.4 | 0.1031 | 0.1144 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 203; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 203 | +0.388 [-0.947, +1.723] | 0.3358 | 0.57 | 0.569 | not applied (n < 1000) | 0.827 | +1.5 | +0.0 | 0.0645 | 0.0742 |
| Mean glucose (mg/dL) | 203 | +0.199 [-1.043, +1.440] | 0.006077 | 0.31 | 0.754 | not applied (n < 1000) | 0.896 | +1.9 | +0.4 | 0.0662 | 0.0742 |
| GMI (%) | 203 | +0.199 [-1.043, +1.440] | 0.2541 | 0.31 | 0.754 | not applied (n < 1000) | 0.896 | +1.9 | +0.4 | 0.0662 | 0.0742 |
| Nocturnal mean 00-06h (mg/dL) | 203 | +0.249 [-0.857, +1.354] | 0.007485 | 0.44 | 0.659 | not applied (n < 1000) | 0.867 | +1.8 | +0.3 | 0.0674 | 0.0742 |
| Glucose SD, pooled (mg/dL) | 203 | -0.247 [-1.654, +1.159] | -0.01541 | -0.34 | 0.730 | not applied (n < 1000) | 0.888 | +1.8 | +0.3 | 0.0608 | 0.0742 |
| Avg. daily SD (mg/dL) | 203 | -0.397 [-1.825, +1.031] | -0.02909 | -0.54 | 0.586 | not applied (n < 1000) | 0.840 | +1.5 | +0.0 | 0.0633 | 0.0742 |
| CV (%) | 203 | -0.493 [-1.911, +0.925] | -0.06917 | -0.68 | 0.496 | not applied (n < 1000) | 0.762 | +1.4 | -0.2 | 0.0651 | 0.0742 |
| Mean / SD ratio | 203 | +0.043 [-1.316, +1.402] | 0.03083 | 0.06 | 0.950 | not applied (n < 1000) | 0.971 | +2.0 | +0.5 | 0.0665 | 0.0742 |
| Avg. daily mean / SD | 203 | +0.152 [-1.203, +1.506] | 0.08965 | 0.22 | 0.826 | not applied (n < 1000) | 0.912 | +1.9 | +0.4 | 0.0678 | 0.0742 |
| MAG (mg/dL/h) | 203 | -0.441 [-1.668, +0.785] | -0.03899 | -0.70 | 0.481 | not applied (n < 1000) | 0.754 | +1.4 | -0.1 | 0.0656 | 0.0742 |
| Avg. daily range (mg/dL) | 203 | -0.356 [-1.742, +1.030] | -0.007378 | -0.50 | 0.615 | not applied (n < 1000) | 0.858 | +1.6 | +0.1 | 0.0670 | 0.0742 |
| SD of daily means (mg/dL) | 203 | +0.245 [-0.799, +1.289] | 0.02474 | 0.46 | 0.645 | not applied (n < 1000) | 0.867 | +1.8 | +0.3 | 0.0638 | 0.0742 |
| Time in range 70-180, pooled (%) | 203 | -0.232 [-1.518, +1.054] | -0.01233 | -0.35 | 0.724 | not applied (n < 1000) | 0.888 | +1.8 | +0.3 | 0.0654 | 0.0742 |
| Avg. daily time in range 70-180 (%) | 203 | -0.237 [-1.487, +1.014] | -0.01256 | -0.37 | 0.711 | not applied (n < 1000) | 0.883 | +1.8 | +0.3 | 0.0658 | 0.0742 |
| Time < 54, pooled (%) | 203 | +0.416 [-0.643, +1.475] | 0.5339 | 0.77 | 0.442 | not applied (n < 1000) | 0.736 | +1.4 | -0.1 | 0.0680 | 0.0742 |
| Avg. daily time < 54 (%) | 203 | -0.100 [-2.062, +1.861] | -0.1165 | -0.10 | 0.920 | not applied (n < 1000) | 0.961 | +2.0 | +0.5 | 0.0497 | 0.0742 |
| Time 54-69, pooled (%) | 203 | -0.239 [-1.409, +0.932] | -0.09346 | -0.40 | 0.689 | not applied (n < 1000) | 0.867 | +1.8 | +0.3 | 0.0676 | 0.0742 |
| Avg. daily time 54-69 (%) | 203 | -0.422 [-1.693, +0.850] | -0.1553 | -0.65 | 0.515 | not applied (n < 1000) | 0.770 | +1.4 | -0.1 | 0.0650 | 0.0742 |
| Time < 70, pooled (%) | 203 | -0.092 [-1.301, +1.118] | -0.02959 | -0.15 | 0.882 | not applied (n < 1000) | 0.949 | +2.0 | +0.5 | 0.0655 | 0.0742 |
| Avg. daily time < 70 (%) | 203 | -0.369 [-1.755, +1.017] | -0.1107 | -0.52 | 0.602 | not applied (n < 1000) | 0.847 | +1.6 | +0.0 | 0.0609 | 0.0742 |
| Time 54-250, pooled (%) | 203 | +0.055 [-1.369, +1.479] | 0.005702 | 0.08 | 0.940 | not applied (n < 1000) | 0.963 | +2.0 | +0.5 | 0.0606 | 0.0742 |
| Avg. daily time 54-250 (%) | 203 | -0.137 [-1.319, +1.046] | -0.01566 | -0.23 | 0.821 | not applied (n < 1000) | 0.912 | +1.9 | +0.4 | 0.0670 | 0.0742 |
| Time 181-250, pooled (%) | 203 | +0.441 [-0.790, +1.672] | 0.03557 | 0.70 | 0.483 | not applied (n < 1000) | 0.754 | +1.4 | -0.1 | 0.0679 | 0.0742 |
| Avg. daily time 181-250 (%) | 203 | +0.340 [-0.909, +1.590] | 0.02665 | 0.53 | 0.593 | not applied (n < 1000) | 0.847 | +1.6 | +0.1 | 0.0655 | 0.0742 |
| Time > 180, pooled (%) | 203 | +0.240 [-1.003, +1.483] | 0.01261 | 0.38 | 0.705 | not applied (n < 1000) | 0.881 | +1.8 | +0.3 | 0.0670 | 0.0742 |
| Avg. daily time > 180 (%) | 203 | +0.296 [-0.900, +1.493] | 0.01561 | 0.48 | 0.628 | not applied (n < 1000) | 0.858 | +1.7 | +0.2 | 0.0677 | 0.0742 |
| Nocturnal time > 180 (%) | 203 | +0.204 [-0.921, +1.329] | 0.01072 | 0.36 | 0.722 | not applied (n < 1000) | 0.888 | +1.9 | +0.3 | 0.0702 | 0.0742 |
| Any reading > 250 during wear (0/1) | 203 | +0.055 [-1.185, +1.296] | 0.1106 | 0.09 | 0.930 | not applied (n < 1000) | 0.962 | +2.0 | +0.5 | 0.0682 | 0.0742 |
| Time > 250, pooled (%) | 203 | -0.088 [-1.461, +1.284] | -0.009266 | -0.13 | 0.899 | not applied (n < 1000) | 0.956 | +2.0 | +0.5 | 0.0613 | 0.0742 |
| Avg. daily time > 250 (%) | 203 | +0.148 [-0.982, +1.278] | 0.01718 | 0.26 | 0.798 | not applied (n < 1000) | 0.908 | +1.9 | +0.4 | 0.0681 | 0.0742 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 205; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 205 | -14.939 [-23.473, -6.405] | -12.94 | -3.43 | 6.0e-04*** | not applied (n < 1000) | 0.031 (q<0.05) | -7.7 | +0.0 | -0.0422 | -0.0799 |
| Mean glucose (mg/dL) | 205 | -10.118 [-19.026, -1.209] | -0.3115 | -2.23 | 0.026* | not applied (n < 1000) | 0.195 | -2.6 | +5.1 | -0.0722 | -0.0799 |
| GMI (%) | 205 | -10.118 [-19.026, -1.209] | -13.02 | -2.23 | 0.026* | not applied (n < 1000) | 0.195 | -2.6 | +5.1 | -0.0722 | -0.0799 |
| Nocturnal mean 00-06h (mg/dL) | 205 | -8.336 [-17.703, +1.030] | -0.2522 | -1.74 | 0.081 | not applied (n < 1000) | 0.310 | -1.1 | +6.5 | -0.0854 | -0.0799 |
| Glucose SD, pooled (mg/dL) | 205 | -8.953 [-18.701, +0.794] | -0.5567 | -1.80 | 0.072 | not applied (n < 1000) | 0.284 | -1.2 | +6.5 | -0.0696 | -0.0799 |
| Avg. daily SD (mg/dL) | 205 | -7.734 [-17.044, +1.576] | -0.5645 | -1.63 | 0.103 | not applied (n < 1000) | 0.356 | -0.3 | +7.3 | -0.0707 | -0.0799 |
| CV (%) | 205 | -2.671 [-13.359, +8.017] | -0.3731 | -0.49 | 0.624 | not applied (n < 1000) | 0.858 | +1.7 | +9.4 | -0.0884 | -0.0799 |
| Mean / SD ratio | 205 | +1.819 [-9.142, +12.781] | 1.301 | 0.33 | 0.745 | not applied (n < 1000) | 0.896 | +1.9 | +9.6 | -0.0930 | -0.0799 |
| Avg. daily mean / SD | 205 | +1.050 [-9.232, +11.332] | 0.6199 | 0.20 | 0.841 | not applied (n < 1000) | 0.918 | +2.0 | +9.6 | -0.0929 | -0.0799 |
| MAG (mg/dL/h) | 205 | -14.317 [-24.946, -3.688] | -1.265 | -2.64 | 0.008** | not applied (n < 1000) | 0.124 | -6.7 | +1.0 | -0.0473 | -0.0799 |
| Avg. daily range (mg/dL) | 205 | -8.555 [-18.323, +1.213] | -0.1768 | -1.72 | 0.086 | not applied (n < 1000) | 0.314 | -0.8 | +6.8 | -0.0692 | -0.0799 |
| SD of daily means (mg/dL) | 205 | -9.935 [-20.050, +0.180] | -1.007 | -1.93 | 0.054 | not applied (n < 1000) | 0.268 | -2.2 | +5.5 | -0.0715 | -0.0799 |
| Time in range 70-180, pooled (%) | 205 | +11.669 [+2.144, +21.194] | 0.6249 | 2.40 | 0.016* | not applied (n < 1000) | 0.169 | -3.8 | +3.8 | -0.0675 | -0.0799 |
| Avg. daily time in range 70-180 (%) | 205 | +11.795 [+2.011, +21.579] | 0.6302 | 2.36 | 0.018* | not applied (n < 1000) | 0.173 | -3.9 | +3.8 | -0.0689 | -0.0799 |
| Time < 54, pooled (%) | 205 | +6.550 [-0.427, +13.526] | 8.43 | 1.84 | 0.066 | not applied (n < 1000) | 0.282 | +0.2 | +7.8 | -0.0779 | -0.0799 |
| Avg. daily time < 54 (%) | 205 | +4.994 [-2.806, +12.794] | 5.832 | 1.25 | 0.210 | not applied (n < 1000) | 0.537 | +0.9 | +8.6 | -0.0827 | -0.0799 |
| Time 54-69, pooled (%) | 205 | +2.492 [-8.513, +13.497] | 0.9819 | 0.44 | 0.657 | not applied (n < 1000) | 0.867 | +1.7 | +9.4 | -0.0940 | -0.0799 |
| Avg. daily time 54-69 (%) | 205 | +1.474 [-9.009, +11.956] | 0.5458 | 0.28 | 0.783 | not applied (n < 1000) | 0.908 | +1.9 | +9.6 | -0.0932 | -0.0799 |
| Time < 70, pooled (%) | 205 | +3.688 [-6.609, +13.986] | 1.195 | 0.70 | 0.483 | not applied (n < 1000) | 0.754 | +1.4 | +9.1 | -0.0901 | -0.0799 |
| Avg. daily time < 70 (%) | 205 | +2.502 [-7.398, +12.401] | 0.7548 | 0.50 | 0.620 | not applied (n < 1000) | 0.858 | +1.7 | +9.4 | -0.0908 | -0.0799 |
| Time 54-250, pooled (%) | 205 | +11.069 [+2.241, +19.898] | 1.157 | 2.46 | 0.014* | not applied (n < 1000) | 0.168 | -3.4 | +4.3 | -0.0606 | -0.0799 |
| Avg. daily time 54-250 (%) | 205 | +11.829 [+3.287, +20.372] | 1.363 | 2.71 | 0.007** | not applied (n < 1000) | 0.116 | -4.1 | +3.6 | -0.0559 | -0.0799 |
| Time 181-250, pooled (%) | 205 | -9.368 [-19.175, +0.439] | -0.7632 | -1.87 | 0.061 | not applied (n < 1000) | 0.278 | -1.8 | +5.9 | -0.0834 | -0.0799 |
| Avg. daily time 181-250 (%) | 205 | -9.351 [-19.462, +0.761] | -0.7408 | -1.81 | 0.070 | not applied (n < 1000) | 0.284 | -1.8 | +5.9 | -0.0844 | -0.0799 |
| Time > 180, pooled (%) | 205 | -11.937 [-21.432, -2.442] | -0.6315 | -2.46 | 0.014* | not applied (n < 1000) | 0.168 | -4.2 | +3.5 | -0.0662 | -0.0799 |
| Avg. daily time > 180 (%) | 205 | -11.968 [-21.796, -2.141] | -0.6365 | -2.39 | 0.017* | not applied (n < 1000) | 0.170 | -4.2 | +3.5 | -0.0684 | -0.0799 |
| Nocturnal time > 180 (%) | 205 | -9.295 [-19.110, +0.519] | -0.4919 | -1.86 | 0.063 | not applied (n < 1000) | 0.280 | -1.8 | +5.9 | -0.0804 | -0.0799 |
| Any reading > 250 during wear (0/1) | 205 | -12.004 [-23.122, -0.887] | -23.96 | -2.12 | 0.034* | not applied (n < 1000) | 0.218 | -3.8 | +3.8 | -0.0662 | -0.0799 |
| Time > 250, pooled (%) | 205 | -11.634 [-20.400, -2.869] | -1.224 | -2.60 | 0.009** | not applied (n < 1000) | 0.130 | -4.0 | +3.7 | -0.0583 | -0.0799 |
| Avg. daily time > 250 (%) | 205 | -12.440 [-21.277, -3.602] | -1.452 | -2.76 | 0.006** | not applied (n < 1000) | 0.106 | -4.8 | +2.9 | -0.0535 | -0.0799 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 203; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 203 | +1.639 [-1.430, +4.708] | 1.419 | 1.05 | 0.295 | not applied (n < 1000) | 0.618 | +0.2 | +0.0 | -0.0381 | -0.0365 |
| Mean glucose (mg/dL) | 203 | +1.184 [-1.596, +3.963] | 0.03623 | 0.83 | 0.404 | not applied (n < 1000) | 0.701 | +1.0 | +0.8 | -0.0383 | -0.0365 |
| GMI (%) | 203 | +1.184 [-1.596, +3.963] | 1.515 | 0.83 | 0.404 | not applied (n < 1000) | 0.701 | +1.0 | +0.8 | -0.0383 | -0.0365 |
| Nocturnal mean 00-06h (mg/dL) | 203 | +1.038 [-1.529, +3.605] | 0.03125 | 0.79 | 0.428 | not applied (n < 1000) | 0.722 | +1.2 | +1.1 | -0.0406 | -0.0365 |
| Glucose SD, pooled (mg/dL) | 203 | +0.326 [-2.575, +3.226] | 0.02031 | 0.22 | 0.826 | not applied (n < 1000) | 0.912 | +1.9 | +1.8 | -0.0458 | -0.0365 |
| Avg. daily SD (mg/dL) | 203 | +0.078 [-2.950, +3.107] | 0.005745 | 0.05 | 0.960 | not applied (n < 1000) | 0.976 | +2.0 | +1.8 | -0.0459 | -0.0365 |
| CV (%) | 203 | -0.206 [-3.075, +2.662] | -0.02895 | -0.14 | 0.888 | not applied (n < 1000) | 0.952 | +2.0 | +1.8 | -0.0471 | -0.0365 |
| Mean / SD ratio | 203 | -0.746 [-3.518, +2.025] | -0.5329 | -0.53 | 0.598 | not applied (n < 1000) | 0.847 | +1.7 | +1.5 | -0.0409 | -0.0365 |
| Avg. daily mean / SD | 203 | -0.312 [-3.192, +2.568] | -0.1843 | -0.21 | 0.832 | not applied (n < 1000) | 0.912 | +1.9 | +1.8 | -0.0444 | -0.0365 |
| MAG (mg/dL/h) | 203 | -1.015 [-3.638, +1.609] | -0.08928 | -0.76 | 0.448 | not applied (n < 1000) | 0.736 | +1.3 | +1.1 | -0.0428 | -0.0365 |
| Avg. daily range (mg/dL) | 203 | -0.026 [-2.976, +2.923] | -0.0005454 | -0.02 | 0.986 | not applied (n < 1000) | 0.986 | +2.0 | +1.8 | -0.0434 | -0.0365 |
| SD of daily means (mg/dL) | 203 | +1.181 [-1.119, +3.482] | 0.1192 | 1.01 | 0.314 | not applied (n < 1000) | 0.634 | +1.1 | +0.9 | -0.0403 | -0.0365 |
| Time in range 70-180, pooled (%) | 203 | -1.301 [-4.016, +1.414] | -0.06929 | -0.94 | 0.348 | not applied (n < 1000) | 0.646 | +0.9 | +0.7 | -0.0374 | -0.0365 |
| Avg. daily time in range 70-180 (%) | 203 | -1.323 [-3.988, +1.342] | -0.07022 | -0.97 | 0.331 | not applied (n < 1000) | 0.639 | +0.8 | +0.6 | -0.0373 | -0.0365 |
| Time < 54, pooled (%) | 203 | +1.435 [-0.438, +3.307] | 1.842 | 1.50 | 0.133 | not applied (n < 1000) | 0.413 | +0.6 | +0.4 | -0.0397 | -0.0365 |
| Avg. daily time < 54 (%) | 203 | +0.524 [-3.037, +4.085] | 0.6086 | 0.29 | 0.773 | not applied (n < 1000) | 0.907 | +1.8 | +1.6 | -0.0608 | -0.0365 |
| Time 54-69, pooled (%) | 203 | -0.356 [-3.052, +2.341] | -0.1393 | -0.26 | 0.796 | not applied (n < 1000) | 0.908 | +1.9 | +1.7 | -0.0436 | -0.0365 |
| Avg. daily time 54-69 (%) | 203 | -0.617 [-3.420, +2.186] | -0.2271 | -0.43 | 0.666 | not applied (n < 1000) | 0.867 | +1.7 | +1.6 | -0.0461 | -0.0365 |
| Time < 70, pooled (%) | 203 | +0.067 [-2.643, +2.777] | 0.02156 | 0.05 | 0.961 | not applied (n < 1000) | 0.976 | +2.0 | +1.8 | -0.0456 | -0.0365 |
| Avg. daily time < 70 (%) | 203 | -0.365 [-3.259, +2.529] | -0.1095 | -0.25 | 0.805 | not applied (n < 1000) | 0.911 | +1.9 | +1.7 | -0.0497 | -0.0365 |
| Time 54-250, pooled (%) | 203 | -0.169 [-3.333, +2.996] | -0.01754 | -0.10 | 0.917 | not applied (n < 1000) | 0.961 | +2.0 | +1.8 | -0.0447 | -0.0365 |
| Avg. daily time 54-250 (%) | 203 | -0.441 [-3.689, +2.808] | -0.05054 | -0.27 | 0.790 | not applied (n < 1000) | 0.908 | +1.9 | +1.7 | -0.0420 | -0.0365 |
| Time 181-250, pooled (%) | 203 | +1.899 [-0.693, +4.492] | 0.1533 | 1.44 | 0.151 | not applied (n < 1000) | 0.446 | -0.5 | -0.6 | -0.0342 | -0.0365 |
| Avg. daily time 181-250 (%) | 203 | +1.751 [-0.832, +4.335] | 0.1374 | 1.33 | 0.184 | not applied (n < 1000) | 0.508 | -0.1 | -0.3 | -0.0364 | -0.0365 |
| Time > 180, pooled (%) | 203 | +1.253 [-1.404, +3.910] | 0.06587 | 0.92 | 0.355 | not applied (n < 1000) | 0.655 | +0.9 | +0.7 | -0.0369 | -0.0365 |
| Avg. daily time > 180 (%) | 203 | +1.357 [-1.247, +3.961] | 0.07161 | 1.02 | 0.307 | not applied (n < 1000) | 0.625 | +0.7 | +0.6 | -0.0368 | -0.0365 |
| Nocturnal time > 180 (%) | 203 | +0.899 [-1.548, +3.345] | 0.0472 | 0.72 | 0.472 | not applied (n < 1000) | 0.754 | +1.4 | +1.3 | -0.0394 | -0.0365 |
| Any reading > 250 during wear (0/1) | 203 | +1.019 [-1.607, +3.645] | 2.035 | 0.76 | 0.447 | not applied (n < 1000) | 0.736 | +1.3 | +1.2 | -0.0460 | -0.0365 |
| Time > 250, pooled (%) | 203 | +0.054 [-3.050, +3.157] | 0.005638 | 0.03 | 0.973 | not applied (n < 1000) | 0.980 | +2.0 | +1.8 | -0.0435 | -0.0365 |
| Avg. daily time > 250 (%) | 203 | +0.392 [-2.858, +3.642] | 0.04556 | 0.24 | 0.813 | not applied (n < 1000) | 0.912 | +1.9 | +1.7 | -0.0412 | -0.0365 |

Skipped: Any reading < 54 during wear (0/1) (predictor constant in this cohort)


---

## Cohort: Hyperglycaemia exposure: at least one reading > 250

### Population: Total analysis base

#### MoCA total score (0-30)
*n = 795; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 795 | -0.299 [-0.545, -0.053] | -0.2192 | -2.38 | 0.017* | not applied (n < 1000) | 0.087 | -3.6 | +0.0 | 0.0518 | 0.0474 |
| Mean glucose (mg/dL) | 795 | -0.365 [-0.619, -0.111] | -0.009004 | -2.82 | 0.005** | not applied (n < 1000) | 0.045 (q<0.05) | -6.6 | -3.0 | 0.0540 | 0.0474 |
| GMI (%) | 795 | -0.365 [-0.619, -0.111] | -0.3764 | -2.82 | 0.005** | not applied (n < 1000) | 0.045 (q<0.05) | -6.6 | -3.0 | 0.0540 | 0.0474 |
| Nocturnal mean 00-06h (mg/dL) | 795 | -0.345 [-0.601, -0.089] | -0.007994 | -2.64 | 0.008** | not applied (n < 1000) | 0.056 | -5.6 | -2.0 | 0.0530 | 0.0474 |
| Glucose SD, pooled (mg/dL) | 795 | -0.360 [-0.606, -0.115] | -0.02935 | -2.87 | 0.004** | not applied (n < 1000) | 0.041 (q<0.05) | -6.1 | -2.4 | 0.0546 | 0.0474 |
| Avg. daily SD (mg/dL) | 795 | -0.341 [-0.588, -0.095] | -0.03174 | -2.72 | 0.007** | not applied (n < 1000) | 0.050 | -5.3 | -1.7 | 0.0536 | 0.0474 |
| CV (%) | 795 | -0.049 [-0.273, +0.175] | -0.008929 | -0.43 | 0.669 | not applied (n < 1000) | 0.788 | +1.8 | +5.5 | 0.0445 | 0.0474 |
| Mean / SD ratio | 795 | +0.089 [-0.138, +0.316] | 0.08948 | 0.77 | 0.443 | not applied (n < 1000) | 0.689 | +1.5 | +5.1 | 0.0455 | 0.0474 |
| Avg. daily mean / SD | 795 | +0.036 [-0.209, +0.281] | 0.0288 | 0.29 | 0.775 | not applied (n < 1000) | 0.863 | +1.9 | +5.5 | 0.0450 | 0.0474 |
| MAG (mg/dL/h) | 795 | -0.253 [-0.508, +0.001] | -0.02614 | -1.95 | 0.051 | not applied (n < 1000) | 0.180 | -2.2 | +1.4 | 0.0526 | 0.0474 |
| Avg. daily range (mg/dL) | 795 | -0.275 [-0.530, -0.020] | -0.007611 | -2.12 | 0.034* | not applied (n < 1000) | 0.141 | -2.8 | +0.8 | 0.0516 | 0.0474 |
| SD of daily means (mg/dL) | 795 | -0.253 [-0.506, -0.000] | -0.03049 | -1.96 | 0.050* | not applied (n < 1000) | 0.178 | -2.1 | +1.6 | 0.0510 | 0.0474 |
| Time in range 70-180, pooled (%) | 795 | +0.360 [+0.106, +0.614] | 0.0141 | 2.77 | 0.006** | not applied (n < 1000) | 0.046 (q<0.05) | -6.2 | -2.6 | 0.0538 | 0.0474 |
| Avg. daily time in range 70-180 (%) | 795 | +0.352 [+0.097, +0.607] | 0.0137 | 2.71 | 0.007** | not applied (n < 1000) | 0.051 | -5.9 | -2.2 | 0.0534 | 0.0474 |
| Any reading < 54 during wear (0/1) | 795 | +0.108 [-0.130, +0.346] | 0.2545 | 0.89 | 0.375 | not applied (n < 1000) | 0.663 | +1.2 | +4.8 | 0.0450 | 0.0474 |
| Time < 54, pooled (%) | 795 | +0.152 [+0.008, +0.296] | 0.2681 | 2.07 | 0.039* | not applied (n < 1000) | 0.156 | +0.4 | +4.0 | 0.0448 | 0.0474 |
| Avg. daily time < 54 (%) | 795 | +0.112 [-0.106, +0.330] | 0.227 | 1.01 | 0.315 | not applied (n < 1000) | 0.609 | +1.1 | +4.8 | 0.0437 | 0.0474 |
| Time 54-69, pooled (%) | 795 | +0.050 [-0.121, +0.222] | 0.04875 | 0.58 | 0.563 | not applied (n < 1000) | 0.741 | +1.8 | +5.5 | 0.0446 | 0.0474 |
| Avg. daily time 54-69 (%) | 795 | +0.047 [-0.128, +0.221] | 0.04284 | 0.52 | 0.600 | not applied (n < 1000) | 0.754 | +1.9 | +5.5 | 0.0436 | 0.0474 |
| Time < 70, pooled (%) | 795 | +0.101 [-0.086, +0.287] | 0.07269 | 1.06 | 0.289 | not applied (n < 1000) | 0.578 | +1.3 | +4.9 | 0.0455 | 0.0474 |
| Avg. daily time < 70 (%) | 795 | +0.074 [-0.119, +0.268] | 0.05177 | 0.75 | 0.451 | not applied (n < 1000) | 0.689 | +1.6 | +5.3 | 0.0431 | 0.0474 |
| Time 54-250, pooled (%) | 795 | +0.319 [+0.063, +0.576] | 0.01893 | 2.44 | 0.015* | not applied (n < 1000) | 0.083 | -4.6 | -1.0 | 0.0532 | 0.0474 |
| Avg. daily time 54-250 (%) | 795 | +0.317 [+0.056, +0.578] | 0.019 | 2.38 | 0.017* | not applied (n < 1000) | 0.087 | -4.5 | -0.9 | 0.0529 | 0.0474 |
| Time 181-250, pooled (%) | 795 | -0.241 [-0.488, +0.006] | -0.01625 | -1.91 | 0.056 | not applied (n < 1000) | 0.180 | -1.8 | +1.8 | 0.0469 | 0.0474 |
| Avg. daily time 181-250 (%) | 795 | -0.234 [-0.483, +0.014] | -0.01548 | -1.85 | 0.064 | not applied (n < 1000) | 0.196 | -1.6 | +2.0 | 0.0466 | 0.0474 |
| Time > 180, pooled (%) | 795 | -0.362 [-0.615, -0.109] | -0.0141 | -2.80 | 0.005** | not applied (n < 1000) | 0.046 (q<0.05) | -6.4 | -2.7 | 0.0539 | 0.0474 |
| Avg. daily time > 180 (%) | 795 | -0.354 [-0.608, -0.099] | -0.01368 | -2.72 | 0.006** | not applied (n < 1000) | 0.050 | -6.0 | -2.3 | 0.0534 | 0.0474 |
| Nocturnal time > 180 (%) | 795 | -0.351 [-0.608, -0.093] | -0.01233 | -2.67 | 0.008** | not applied (n < 1000) | 0.055 | -5.7 | -2.1 | 0.0538 | 0.0474 |
| Time > 250, pooled (%) | 795 | -0.325 [-0.582, -0.068] | -0.01923 | -2.47 | 0.013* | not applied (n < 1000) | 0.078 | -4.9 | -1.2 | 0.0535 | 0.0474 |
| Avg. daily time > 250 (%) | 795 | -0.320 [-0.581, -0.060] | -0.0192 | -2.41 | 0.016* | not applied (n < 1000) | 0.087 | -4.7 | -1.1 | 0.0531 | 0.0474 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 795; events = 371; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 795 | OR 1.190 [1.017, 1.391] | 0.1273 | 2.17 | 0.030* | not applied (n < 1000) | 0.127 | -2.9 | +0.0 | 0.6220 | 0.6214 |
| Mean glucose (mg/dL) | 795 | OR 1.234 [1.057, 1.441] | 0.00519 | 2.67 | 0.008** | not applied (n < 1000) | 0.055 | -5.3 | -2.4 | 0.6234 | 0.6214 |
| GMI (%) | 795 | OR 1.234 [1.057, 1.441] | 0.217 | 2.67 | 0.008** | not applied (n < 1000) | 0.055 | -5.3 | -2.4 | 0.6234 | 0.6214 |
| Nocturnal mean 00-06h (mg/dL) | 795 | OR 1.197 [1.025, 1.397] | 0.004155 | 2.27 | 0.023* | not applied (n < 1000) | 0.106 | -3.3 | -0.4 | 0.6218 | 0.6214 |
| Glucose SD, pooled (mg/dL) | 795 | OR 1.237 [1.057, 1.448] | 0.01731 | 2.65 | 0.008** | not applied (n < 1000) | 0.056 | -5.2 | -2.3 | 0.6262 | 0.6214 |
| Avg. daily SD (mg/dL) | 795 | OR 1.222 [1.045, 1.428] | 0.01864 | 2.52 | 0.012* | not applied (n < 1000) | 0.070 | -4.5 | -1.6 | 0.6252 | 0.6214 |
| CV (%) | 795 | OR 1.047 [0.901, 1.215] | 0.008304 | 0.60 | 0.551 | not applied (n < 1000) | 0.739 | +1.6 | +4.5 | 0.6213 | 0.6214 |
| Mean / SD ratio | 795 | OR 0.961 [0.828, 1.115] | -0.03997 | -0.52 | 0.600 | not applied (n < 1000) | 0.754 | +1.7 | +4.6 | 0.6206 | 0.6214 |
| Avg. daily mean / SD | 795 | OR 0.985 [0.850, 1.142] | -0.01204 | -0.20 | 0.843 | not applied (n < 1000) | 0.899 | +2.0 | +4.8 | 0.6205 | 0.6214 |
| MAG (mg/dL/h) | 795 | OR 1.169 [1.003, 1.362] | 0.01607 | 1.99 | 0.046* | not applied (n < 1000) | 0.171 | -2.0 | +0.8 | 0.6202 | 0.6214 |
| Avg. daily range (mg/dL) | 795 | OR 1.187 [1.018, 1.385] | 0.00475 | 2.19 | 0.029* | not applied (n < 1000) | 0.124 | -2.9 | +0.0 | 0.6246 | 0.6214 |
| SD of daily means (mg/dL) | 795 | OR 1.184 [1.011, 1.385] | 0.02028 | 2.10 | 0.036* | not applied (n < 1000) | 0.146 | -2.5 | +0.3 | 0.6234 | 0.6214 |
| Time in range 70-180, pooled (%) | 795 | OR 0.803 [0.688, 0.936] | -0.008616 | -2.80 | 0.005** | not applied (n < 1000) | 0.046 (q<0.05) | -6.0 | -3.1 | 0.6231 | 0.6214 |
| Avg. daily time in range 70-180 (%) | 795 | OR 0.804 [0.690, 0.938] | -0.008473 | -2.78 | 0.006** | not applied (n < 1000) | 0.046 (q<0.05) | -5.8 | -2.9 | 0.6228 | 0.6214 |
| Any reading < 54 during wear (0/1) | 795 | OR 0.897 [0.774, 1.039] | -0.2575 | -1.45 | 0.147 | not applied (n < 1000) | 0.363 | -0.1 | +2.7 | 0.6246 | 0.6214 |
| Time < 54, pooled (%) | 795 | OR 0.908 [0.742, 1.112] | -0.1695 | -0.93 | 0.352 | not applied (n < 1000) | 0.637 | +0.8 | +3.6 | 0.6222 | 0.6214 |
| Avg. daily time < 54 (%) | 795 | OR 0.969 [0.837, 1.121] | -0.06458 | -0.43 | 0.670 | not applied (n < 1000) | 0.788 | +1.8 | +4.7 | 0.6194 | 0.6214 |
| Time 54-69, pooled (%) | 795 | OR 1.039 [0.899, 1.201] | 0.03673 | 0.51 | 0.607 | not applied (n < 1000) | 0.754 | +1.7 | +4.6 | 0.6172 | 0.6214 |
| Avg. daily time 54-69 (%) | 795 | OR 1.061 [0.916, 1.229] | 0.05428 | 0.79 | 0.431 | not applied (n < 1000) | 0.689 | +1.4 | +4.2 | 0.6183 | 0.6214 |
| Time < 70, pooled (%) | 795 | OR 0.996 [0.862, 1.151] | -0.002902 | -0.05 | 0.956 | not applied (n < 1000) | 0.971 | +2.0 | +4.9 | 0.6185 | 0.6214 |
| Avg. daily time < 70 (%) | 795 | OR 1.034 [0.895, 1.194] | 0.02298 | 0.45 | 0.654 | not applied (n < 1000) | 0.780 | +1.8 | +4.7 | 0.6185 | 0.6214 |
| Time 54-250, pooled (%) | 795 | OR 0.829 [0.709, 0.970] | -0.01108 | -2.34 | 0.019* | not applied (n < 1000) | 0.094 | -3.7 | -0.9 | 0.6208 | 0.6214 |
| Avg. daily time 54-250 (%) | 795 | OR 0.833 [0.712, 0.974] | -0.01097 | -2.29 | 0.022* | not applied (n < 1000) | 0.102 | -3.5 | -0.6 | 0.6203 | 0.6214 |
| Time 181-250, pooled (%) | 795 | OR 1.167 [1.005, 1.356] | 0.01041 | 2.02 | 0.043* | not applied (n < 1000) | 0.162 | -2.1 | +0.8 | 0.6209 | 0.6214 |
| Avg. daily time 181-250 (%) | 795 | OR 1.168 [1.005, 1.357] | 0.01026 | 2.03 | 0.042* | not applied (n < 1000) | 0.162 | -2.1 | +0.7 | 0.6206 | 0.6214 |
| Time > 180, pooled (%) | 795 | OR 1.243 [1.066, 1.449] | 0.008482 | 2.78 | 0.005** | not applied (n < 1000) | 0.046 (q<0.05) | -5.8 | -3.0 | 0.6229 | 0.6214 |
| Avg. daily time > 180 (%) | 795 | OR 1.238 [1.062, 1.444] | 0.00827 | 2.73 | 0.006** | not applied (n < 1000) | 0.050 | -5.5 | -2.7 | 0.6224 | 0.6214 |
| Nocturnal time > 180 (%) | 795 | OR 1.214 [1.040, 1.416] | 0.006813 | 2.46 | 0.014* | not applied (n < 1000) | 0.080 | -4.1 | -1.3 | 0.6239 | 0.6214 |
| Time > 250, pooled (%) | 795 | OR 1.209 [1.034, 1.415] | 0.01126 | 2.38 | 0.017* | not applied (n < 1000) | 0.087 | -3.9 | -1.1 | 0.6211 | 0.6214 |
| Avg. daily time > 250 (%) | 795 | OR 1.202 [1.028, 1.406] | 0.01103 | 2.31 | 0.021* | not applied (n < 1000) | 0.100 | -3.6 | -0.7 | 0.6205 | 0.6214 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 795; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 795 | -0.193 [-0.391, +0.005] | -0.1413 | -1.91 | 0.056 | not applied (n < 1000) | 0.180 | -1.4 | +0.0 | 0.0382 | 0.0354 |
| Mean glucose (mg/dL) | 795 | -0.193 [-0.380, -0.006] | -0.004754 | -2.02 | 0.043* | not applied (n < 1000) | 0.162 | -1.5 | -0.1 | 0.0386 | 0.0354 |
| GMI (%) | 795 | -0.193 [-0.380, -0.006] | -0.1987 | -2.02 | 0.043* | not applied (n < 1000) | 0.162 | -1.5 | -0.1 | 0.0386 | 0.0354 |
| Nocturnal mean 00-06h (mg/dL) | 795 | -0.214 [-0.402, -0.026] | -0.004958 | -2.23 | 0.026* | not applied (n < 1000) | 0.115 | -2.2 | -0.8 | 0.0400 | 0.0354 |
| Glucose SD, pooled (mg/dL) | 795 | -0.246 [-0.447, -0.044] | -0.02 | -2.39 | 0.017* | not applied (n < 1000) | 0.087 | -3.4 | -2.0 | 0.0396 | 0.0354 |
| Avg. daily SD (mg/dL) | 795 | -0.236 [-0.431, -0.040] | -0.02192 | -2.36 | 0.018* | not applied (n < 1000) | 0.090 | -3.1 | -1.7 | 0.0396 | 0.0354 |
| CV (%) | 795 | -0.120 [-0.311, +0.071] | -0.02195 | -1.23 | 0.217 | not applied (n < 1000) | 0.479 | +0.6 | +2.0 | 0.0354 | 0.0354 |
| Mean / SD ratio | 795 | +0.073 [-0.122, +0.268] | 0.07348 | 0.73 | 0.463 | not applied (n < 1000) | 0.689 | +1.5 | +2.9 | 0.0350 | 0.0354 |
| Avg. daily mean / SD | 795 | +0.058 [-0.149, +0.264] | 0.04637 | 0.55 | 0.585 | not applied (n < 1000) | 0.750 | +1.7 | +3.1 | 0.0343 | 0.0354 |
| MAG (mg/dL/h) | 795 | -0.153 [-0.365, +0.058] | -0.01584 | -1.42 | 0.155 | not applied (n < 1000) | 0.377 | -0.2 | +1.2 | 0.0364 | 0.0354 |
| Avg. daily range (mg/dL) | 795 | -0.197 [-0.403, +0.008] | -0.005455 | -1.88 | 0.060 | not applied (n < 1000) | 0.188 | -1.6 | -0.2 | 0.0384 | 0.0354 |
| SD of daily means (mg/dL) | 795 | -0.161 [-0.391, +0.068] | -0.01938 | -1.38 | 0.169 | not applied (n < 1000) | 0.399 | -0.4 | +1.0 | 0.0353 | 0.0354 |
| Time in range 70-180, pooled (%) | 795 | +0.193 [-0.001, +0.386] | 0.007551 | 1.95 | 0.051 | not applied (n < 1000) | 0.180 | -1.4 | -0.0 | 0.0385 | 0.0354 |
| Avg. daily time in range 70-180 (%) | 795 | +0.191 [-0.004, +0.386] | 0.007439 | 1.92 | 0.054 | not applied (n < 1000) | 0.180 | -1.4 | +0.0 | 0.0384 | 0.0354 |
| Any reading < 54 during wear (0/1) | 795 | +0.031 [-0.162, +0.224] | 0.07409 | 0.32 | 0.750 | not applied (n < 1000) | 0.845 | +1.9 | +3.3 | 0.0342 | 0.0354 |
| Time < 54, pooled (%) | 795 | +0.011 [-0.087, +0.109] | 0.01884 | 0.21 | 0.831 | not applied (n < 1000) | 0.890 | +2.0 | +3.4 | 0.0350 | 0.0354 |
| Avg. daily time < 54 (%) | 795 | -0.039 [-0.222, +0.144] | -0.07838 | -0.41 | 0.678 | not applied (n < 1000) | 0.792 | +1.9 | +3.2 | 0.0346 | 0.0354 |
| Time 54-69, pooled (%) | 795 | -0.071 [-0.276, +0.134] | -0.06878 | -0.68 | 0.496 | not applied (n < 1000) | 0.713 | +1.5 | +2.9 | 0.0355 | 0.0354 |
| Avg. daily time 54-69 (%) | 795 | -0.120 [-0.356, +0.115] | -0.1107 | -1.00 | 0.317 | not applied (n < 1000) | 0.611 | +0.6 | +2.0 | 0.0365 | 0.0354 |
| Time < 70, pooled (%) | 795 | -0.049 [-0.221, +0.123] | -0.03522 | -0.56 | 0.576 | not applied (n < 1000) | 0.745 | +1.8 | +3.1 | 0.0353 | 0.0354 |
| Avg. daily time < 70 (%) | 795 | -0.105 [-0.308, +0.098] | -0.07281 | -1.01 | 0.312 | not applied (n < 1000) | 0.607 | +0.9 | +2.3 | 0.0362 | 0.0354 |
| Time 54-250, pooled (%) | 795 | +0.169 [-0.011, +0.350] | 0.01003 | 1.84 | 0.066 | not applied (n < 1000) | 0.201 | -0.7 | +0.7 | 0.0368 | 0.0354 |
| Avg. daily time 54-250 (%) | 795 | +0.162 [-0.017, +0.342] | 0.009716 | 1.77 | 0.077 | not applied (n < 1000) | 0.225 | -0.5 | +0.9 | 0.0365 | 0.0354 |
| Time 181-250, pooled (%) | 795 | -0.124 [-0.316, +0.068] | -0.008349 | -1.27 | 0.205 | not applied (n < 1000) | 0.461 | +0.5 | +1.9 | 0.0349 | 0.0354 |
| Avg. daily time 181-250 (%) | 795 | -0.127 [-0.321, +0.066] | -0.008408 | -1.29 | 0.196 | not applied (n < 1000) | 0.453 | +0.5 | +1.8 | 0.0350 | 0.0354 |
| Time > 180, pooled (%) | 795 | -0.188 [-0.381, +0.005] | -0.007318 | -1.91 | 0.056 | not applied (n < 1000) | 0.180 | -1.3 | +0.1 | 0.0383 | 0.0354 |
| Avg. daily time > 180 (%) | 795 | -0.183 [-0.377, +0.011] | -0.007094 | -1.85 | 0.064 | not applied (n < 1000) | 0.196 | -1.1 | +0.3 | 0.0381 | 0.0354 |
| Nocturnal time > 180 (%) | 795 | -0.194 [-0.389, +0.002] | -0.006807 | -1.94 | 0.052 | not applied (n < 1000) | 0.180 | -1.4 | -0.0 | 0.0391 | 0.0354 |
| Time > 250, pooled (%) | 795 | -0.170 [-0.350, +0.011] | -0.01005 | -1.84 | 0.066 | not applied (n < 1000) | 0.200 | -0.7 | +0.7 | 0.0368 | 0.0354 |
| Avg. daily time > 250 (%) | 795 | -0.161 [-0.340, +0.019] | -0.009639 | -1.76 | 0.079 | not applied (n < 1000) | 0.230 | -0.4 | +0.9 | 0.0364 | 0.0354 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 793; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 793 | +0.254 [-0.157, +0.665] | 0.1862 | 1.21 | 0.225 | not applied (n < 1000) | 0.485 | -0.0 | +0.0 | 0.1058 | 0.1053 |
| Mean glucose (mg/dL) | 793 | +0.164 [-0.228, +0.556] | 0.004042 | 0.82 | 0.413 | not applied (n < 1000) | 0.676 | +1.1 | +1.2 | 0.1043 | 0.1053 |
| GMI (%) | 793 | +0.164 [-0.228, +0.556] | 0.169 | 0.82 | 0.413 | not applied (n < 1000) | 0.676 | +1.1 | +1.2 | 0.1043 | 0.1053 |
| Nocturnal mean 00-06h (mg/dL) | 793 | +0.235 [-0.156, +0.626] | 0.005436 | 1.18 | 0.238 | not applied (n < 1000) | 0.500 | +0.3 | +0.3 | 0.1052 | 0.1053 |
| Glucose SD, pooled (mg/dL) | 793 | +0.273 [-0.107, +0.652] | 0.02217 | 1.41 | 0.159 | not applied (n < 1000) | 0.384 | -0.3 | -0.3 | 0.1071 | 0.1053 |
| Avg. daily SD (mg/dL) | 793 | +0.157 [-0.220, +0.534] | 0.01459 | 0.82 | 0.414 | not applied (n < 1000) | 0.676 | +1.2 | +1.2 | 0.1050 | 0.1053 |
| CV (%) | 793 | +0.098 [-0.252, +0.449] | 0.0179 | 0.55 | 0.583 | not applied (n < 1000) | 0.749 | +1.7 | +1.7 | 0.1038 | 0.1053 |
| Mean / SD ratio | 793 | -0.136 [-0.487, +0.215] | -0.1367 | -0.76 | 0.447 | not applied (n < 1000) | 0.689 | +1.4 | +1.4 | 0.1037 | 0.1053 |
| Avg. daily mean / SD | 793 | -0.008 [-0.360, +0.344] | -0.006117 | -0.04 | 0.966 | not applied (n < 1000) | 0.973 | +2.0 | +2.0 | 0.1031 | 0.1053 |
| MAG (mg/dL/h) | 793 | +0.357 [-0.019, +0.734] | 0.03686 | 1.86 | 0.063 | not applied (n < 1000) | 0.196 | -2.1 | -2.1 | 0.1079 | 0.1053 |
| Avg. daily range (mg/dL) | 793 | +0.124 [-0.247, +0.495] | 0.00343 | 0.66 | 0.512 | not applied (n < 1000) | 0.724 | +1.5 | +1.5 | 0.1044 | 0.1053 |
| SD of daily means (mg/dL) | 793 | +0.552 [+0.184, +0.920] | 0.06641 | 2.94 | 0.003** | not applied (n < 1000) | 0.034 (q<0.05) | -7.6 | -7.6 | 0.1150 | 0.1053 |
| Time in range 70-180, pooled (%) | 793 | -0.205 [-0.596, +0.187] | -0.008015 | -1.02 | 0.306 | not applied (n < 1000) | 0.602 | +0.7 | +0.7 | 0.1053 | 0.1053 |
| Avg. daily time in range 70-180 (%) | 793 | -0.192 [-0.584, +0.201] | -0.007451 | -0.96 | 0.339 | not applied (n < 1000) | 0.630 | +0.9 | +0.9 | 0.1051 | 0.1053 |
| Any reading < 54 during wear (0/1) | 793 | +0.280 [-0.062, +0.622] | 0.6632 | 1.61 | 0.108 | not applied (n < 1000) | 0.284 | -0.7 | -0.7 | 0.1057 | 0.1053 |
| Time < 54, pooled (%) | 793 | -0.009 [-0.196, +0.179] | -0.01513 | -0.09 | 0.928 | not applied (n < 1000) | 0.958 | +2.0 | +2.0 | 0.1051 | 0.1053 |
| Avg. daily time < 54 (%) | 793 | +0.049 [-0.305, +0.402] | 0.09876 | 0.27 | 0.787 | not applied (n < 1000) | 0.863 | +1.9 | +1.9 | 0.1035 | 0.1053 |
| Time 54-69, pooled (%) | 793 | +0.108 [-0.235, +0.450] | 0.1041 | 0.62 | 0.538 | not applied (n < 1000) | 0.739 | +1.6 | +1.6 | 0.1031 | 0.1053 |
| Avg. daily time 54-69 (%) | 793 | +0.153 [-0.213, +0.520] | 0.1411 | 0.82 | 0.412 | not applied (n < 1000) | 0.676 | +1.2 | +1.2 | 0.1027 | 0.1053 |
| Time < 70, pooled (%) | 793 | +0.077 [-0.216, +0.370] | 0.05548 | 0.52 | 0.606 | not applied (n < 1000) | 0.754 | +1.8 | +1.8 | 0.1039 | 0.1053 |
| Avg. daily time < 70 (%) | 793 | +0.133 [-0.206, +0.473] | 0.09263 | 0.77 | 0.442 | not applied (n < 1000) | 0.689 | +1.4 | +1.4 | 0.1031 | 0.1053 |
| Time 54-250, pooled (%) | 793 | -0.133 [-0.555, +0.289] | -0.007888 | -0.62 | 0.536 | not applied (n < 1000) | 0.739 | +1.4 | +1.4 | 0.1042 | 0.1053 |
| Avg. daily time 54-250 (%) | 793 | -0.110 [-0.534, +0.314] | -0.006562 | -0.51 | 0.612 | not applied (n < 1000) | 0.754 | +1.6 | +1.6 | 0.1039 | 0.1053 |
| Time 181-250, pooled (%) | 793 | +0.182 [-0.186, +0.549] | 0.01223 | 0.97 | 0.333 | not applied (n < 1000) | 0.623 | +0.9 | +0.9 | 0.1044 | 0.1053 |
| Avg. daily time 181-250 (%) | 793 | +0.183 [-0.186, +0.552] | 0.01208 | 0.97 | 0.331 | not applied (n < 1000) | 0.623 | +0.9 | +0.9 | 0.1045 | 0.1053 |
| Time > 180, pooled (%) | 793 | +0.198 [-0.191, +0.587] | 0.007713 | 1.00 | 0.319 | not applied (n < 1000) | 0.611 | +0.8 | +0.8 | 0.1051 | 0.1053 |
| Avg. daily time > 180 (%) | 793 | +0.182 [-0.209, +0.573] | 0.007043 | 0.91 | 0.361 | not applied (n < 1000) | 0.648 | +1.0 | +1.0 | 0.1048 | 0.1053 |
| Nocturnal time > 180 (%) | 793 | +0.280 [-0.112, +0.672] | 0.009832 | 1.40 | 0.161 | not applied (n < 1000) | 0.387 | -0.4 | -0.4 | 0.1063 | 0.1053 |
| Time > 250, pooled (%) | 793 | +0.134 [-0.288, +0.555] | 0.0079 | 0.62 | 0.535 | not applied (n < 1000) | 0.739 | +1.4 | +1.4 | 0.1041 | 0.1053 |
| Avg. daily time > 250 (%) | 793 | +0.108 [-0.316, +0.532] | 0.006467 | 0.50 | 0.617 | not applied (n < 1000) | 0.756 | +1.6 | +1.6 | 0.1039 | 0.1053 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 793; events = 165; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 793 | OR 1.157 [0.978, 1.369] | 0.107 | 1.70 | 0.088 | not applied (n < 1000) | 0.240 | -0.8 | +0.0 | 0.6896 | 0.6853 |
| Mean glucose (mg/dL) | 793 | OR 1.109 [0.936, 1.315] | 0.002558 | 1.19 | 0.232 | not applied (n < 1000) | 0.494 | +0.6 | +1.4 | 0.6888 | 0.6853 |
| GMI (%) | 793 | OR 1.109 [0.936, 1.315] | 0.1069 | 1.19 | 0.232 | not applied (n < 1000) | 0.494 | +0.6 | +1.4 | 0.6888 | 0.6853 |
| Nocturnal mean 00-06h (mg/dL) | 793 | OR 1.184 [1.000, 1.402] | 0.003913 | 1.96 | 0.049* | not applied (n < 1000) | 0.178 | -1.8 | -1.0 | 0.6927 | 0.6853 |
| Glucose SD, pooled (mg/dL) | 793 | OR 1.192 [0.994, 1.428] | 0.01426 | 1.90 | 0.058 | not applied (n < 1000) | 0.182 | -1.6 | -0.7 | 0.6913 | 0.6853 |
| Avg. daily SD (mg/dL) | 793 | OR 1.110 [0.926, 1.331] | 0.009705 | 1.13 | 0.259 | not applied (n < 1000) | 0.536 | +0.7 | +1.6 | 0.6883 | 0.6853 |
| CV (%) | 793 | OR 1.057 [0.880, 1.269] | 0.01006 | 0.59 | 0.556 | not applied (n < 1000) | 0.739 | +1.7 | +2.5 | 0.6841 | 0.6853 |
| Mean / SD ratio | 793 | OR 0.966 [0.804, 1.162] | -0.03456 | -0.37 | 0.715 | not applied (n < 1000) | 0.821 | +1.9 | +2.7 | 0.6848 | 0.6853 |
| Avg. daily mean / SD | 793 | OR 1.053 [0.880, 1.261] | 0.04167 | 0.56 | 0.573 | not applied (n < 1000) | 0.743 | +1.7 | +2.5 | 0.6833 | 0.6853 |
| MAG (mg/dL/h) | 793 | OR 1.169 [0.981, 1.395] | 0.01615 | 1.74 | 0.082 | not applied (n < 1000) | 0.233 | -1.0 | -0.2 | 0.6891 | 0.6853 |
| Avg. daily range (mg/dL) | 793 | OR 1.101 [0.917, 1.320] | 0.002646 | 1.03 | 0.303 | not applied (n < 1000) | 0.600 | +0.9 | +1.8 | 0.6879 | 0.6853 |
| SD of daily means (mg/dL) | 793 | OR 1.361 [1.145, 1.618] | 0.03707 | 3.50 | 4.7e-04*** | not applied (n < 1000) | 0.007 (q<0.05) | -10.2 | -9.4 | 0.7042 | 0.6853 |
| Time in range 70-180, pooled (%) | 793 | OR 0.896 [0.751, 1.069] | -0.004304 | -1.22 | 0.223 | not applied (n < 1000) | 0.482 | +0.5 | +1.4 | 0.6883 | 0.6853 |
| Avg. daily time in range 70-180 (%) | 793 | OR 0.903 [0.757, 1.078] | -0.003958 | -1.13 | 0.260 | not applied (n < 1000) | 0.536 | +0.7 | +1.6 | 0.6883 | 0.6853 |
| Any reading < 54 during wear (0/1) | 793 | OR 1.249 [1.054, 1.481] | 0.5266 | 2.56 | 0.010* | not applied (n < 1000) | 0.065 | -4.4 | -3.6 | 0.6848 | 0.6853 |
| Time < 54, pooled (%) | 793 | OR 1.020 [0.829, 1.255] | 0.03455 | 0.19 | 0.853 | not applied (n < 1000) | 0.902 | +2.0 | +2.8 | 0.6838 | 0.6853 |
| Avg. daily time < 54 (%) | 793 | OR 1.036 [0.867, 1.237] | 0.07116 | 0.39 | 0.698 | not applied (n < 1000) | 0.805 | +1.9 | +2.7 | 0.6813 | 0.6853 |
| Time 54-69, pooled (%) | 793 | OR 1.038 [0.878, 1.227] | 0.03572 | 0.43 | 0.665 | not applied (n < 1000) | 0.788 | +1.8 | +2.7 | 0.6840 | 0.6853 |
| Avg. daily time 54-69 (%) | 793 | OR 1.056 [0.897, 1.243] | 0.05 | 0.65 | 0.514 | not applied (n < 1000) | 0.724 | +1.6 | +2.4 | 0.6852 | 0.6853 |
| Time < 70, pooled (%) | 793 | OR 1.037 [0.869, 1.237] | 0.0262 | 0.40 | 0.686 | not applied (n < 1000) | 0.798 | +1.8 | +2.7 | 0.6838 | 0.6853 |
| Avg. daily time < 70 (%) | 793 | OR 1.054 [0.893, 1.245] | 0.03684 | 0.62 | 0.533 | not applied (n < 1000) | 0.739 | +1.6 | +2.5 | 0.6846 | 0.6853 |
| Time 54-250, pooled (%) | 793 | OR 0.943 [0.802, 1.109] | -0.003477 | -0.71 | 0.477 | not applied (n < 1000) | 0.697 | +1.5 | +2.3 | 0.6853 | 0.6853 |
| Avg. daily time 54-250 (%) | 793 | OR 0.958 [0.814, 1.127] | -0.002582 | -0.52 | 0.604 | not applied (n < 1000) | 0.754 | +1.7 | +2.6 | 0.6848 | 0.6853 |
| Time 181-250, pooled (%) | 793 | OR 1.121 [0.934, 1.345] | 0.00767 | 1.22 | 0.222 | not applied (n < 1000) | 0.482 | +0.5 | +1.4 | 0.6868 | 0.6853 |
| Avg. daily time 181-250 (%) | 793 | OR 1.127 [0.938, 1.352] | 0.00786 | 1.28 | 0.201 | not applied (n < 1000) | 0.457 | +0.4 | +1.2 | 0.6864 | 0.6853 |
| Time > 180, pooled (%) | 793 | OR 1.113 [0.933, 1.328] | 0.004165 | 1.19 | 0.234 | not applied (n < 1000) | 0.495 | +0.6 | +1.4 | 0.6883 | 0.6853 |
| Avg. daily time > 180 (%) | 793 | OR 1.103 [0.924, 1.316] | 0.003785 | 1.08 | 0.279 | not applied (n < 1000) | 0.565 | +0.8 | +1.7 | 0.6883 | 0.6853 |
| Nocturnal time > 180 (%) | 793 | OR 1.193 [1.003, 1.419] | 0.006188 | 1.99 | 0.047* | not applied (n < 1000) | 0.171 | -1.9 | -1.0 | 0.6912 | 0.6853 |
| Time > 250, pooled (%) | 793 | OR 1.060 [0.902, 1.246] | 0.003453 | 0.71 | 0.480 | not applied (n < 1000) | 0.699 | +1.5 | +2.3 | 0.6852 | 0.6853 |
| Avg. daily time > 250 (%) | 793 | OR 1.043 [0.886, 1.228] | 0.002534 | 0.51 | 0.611 | not applied (n < 1000) | 0.754 | +1.7 | +2.6 | 0.6848 | 0.6853 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 783; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 783 | +0.122 [+0.038, +0.206] | 0.08911 | 2.84 | 0.004** | not applied (n < 1000) | 0.044 (q<0.05) | -11.1 | +0.0 | 0.1639 | 0.1522 |
| Mean glucose (mg/dL) | 783 | +0.085 [+0.008, +0.162] | 0.002091 | 2.17 | 0.030* | not applied (n < 1000) | 0.127 | -4.5 | +6.6 | 0.1546 | 0.1522 |
| GMI (%) | 783 | +0.085 [+0.008, +0.162] | 0.08742 | 2.17 | 0.030* | not applied (n < 1000) | 0.127 | -4.5 | +6.6 | 0.1546 | 0.1522 |
| Nocturnal mean 00-06h (mg/dL) | 783 | +0.102 [+0.026, +0.179] | 0.002368 | 2.62 | 0.009** | not applied (n < 1000) | 0.060 | -7.3 | +3.8 | 0.1575 | 0.1522 |
| Glucose SD, pooled (mg/dL) | 783 | +0.077 [+0.010, +0.145] | 0.006294 | 2.24 | 0.025* | not applied (n < 1000) | 0.115 | -3.1 | +8.0 | 0.1543 | 0.1522 |
| Avg. daily SD (mg/dL) | 783 | +0.058 [-0.008, +0.123] | 0.005393 | 1.73 | 0.083 | not applied (n < 1000) | 0.235 | -0.9 | +10.2 | 0.1518 | 0.1522 |
| CV (%) | 783 | +0.021 [-0.047, +0.088] | 0.003751 | 0.60 | 0.551 | not applied (n < 1000) | 0.739 | +1.6 | +12.7 | 0.1490 | 0.1522 |
| Mean / SD ratio | 783 | -0.021 [-0.089, +0.047] | -0.02101 | -0.61 | 0.544 | not applied (n < 1000) | 0.739 | +1.6 | +12.7 | 0.1496 | 0.1522 |
| Avg. daily mean / SD | 783 | -0.012 [-0.082, +0.059] | -0.00955 | -0.33 | 0.741 | not applied (n < 1000) | 0.841 | +1.9 | +13.0 | 0.1505 | 0.1522 |
| MAG (mg/dL/h) | 783 | +0.042 [-0.023, +0.107] | 0.004333 | 1.27 | 0.204 | not applied (n < 1000) | 0.460 | +0.4 | +11.5 | 0.1521 | 0.1522 |
| Avg. daily range (mg/dL) | 783 | +0.050 [-0.014, +0.114] | 0.00139 | 1.54 | 0.124 | not applied (n < 1000) | 0.317 | -0.2 | +10.9 | 0.1515 | 0.1522 |
| SD of daily means (mg/dL) | 783 | +0.119 [+0.047, +0.192] | 0.01434 | 3.22 | 0.001** | not applied (n < 1000) | 0.017 (q<0.05) | -10.6 | +0.5 | 0.1604 | 0.1522 |
| Time in range 70-180, pooled (%) | 783 | -0.091 [-0.166, -0.016] | -0.003559 | -2.38 | 0.017* | not applied (n < 1000) | 0.087 | -5.3 | +5.8 | 0.1555 | 0.1522 |
| Avg. daily time in range 70-180 (%) | 783 | -0.091 [-0.166, -0.016] | -0.003533 | -2.38 | 0.017* | not applied (n < 1000) | 0.087 | -5.3 | +5.8 | 0.1555 | 0.1522 |
| Any reading < 54 during wear (0/1) | 783 | +0.016 [-0.050, +0.083] | 0.03828 | 0.48 | 0.633 | not applied (n < 1000) | 0.768 | +1.7 | +12.8 | 0.1496 | 0.1522 |
| Time < 54, pooled (%) | 783 | +0.012 [-0.110, +0.135] | 0.02176 | 0.20 | 0.842 | not applied (n < 1000) | 0.899 | +1.9 | +13.0 | 0.1502 | 0.1522 |
| Avg. daily time < 54 (%) | 783 | +0.026 [-0.064, +0.117] | 0.05307 | 0.57 | 0.568 | not applied (n < 1000) | 0.743 | +1.3 | +12.4 | 0.1447 | 0.1522 |
| Time 54-69, pooled (%) | 783 | +0.015 [-0.092, +0.122] | 0.01434 | 0.27 | 0.785 | not applied (n < 1000) | 0.863 | +1.8 | +12.9 | 0.1472 | 0.1522 |
| Avg. daily time 54-69 (%) | 783 | +0.021 [-0.092, +0.134] | 0.01904 | 0.36 | 0.717 | not applied (n < 1000) | 0.821 | +1.6 | +12.7 | 0.1481 | 0.1522 |
| Time < 70, pooled (%) | 783 | +0.016 [-0.077, +0.110] | 0.01172 | 0.34 | 0.731 | not applied (n < 1000) | 0.834 | +1.7 | +12.8 | 0.1495 | 0.1522 |
| Avg. daily time < 70 (%) | 783 | +0.025 [-0.077, +0.127] | 0.0173 | 0.48 | 0.630 | not applied (n < 1000) | 0.766 | +1.4 | +12.5 | 0.1498 | 0.1522 |
| Time 54-250, pooled (%) | 783 | -0.073 [-0.155, +0.010] | -0.004298 | -1.72 | 0.085 | not applied (n < 1000) | 0.237 | -2.8 | +8.3 | 0.1496 | 0.1522 |
| Avg. daily time 54-250 (%) | 783 | -0.073 [-0.156, +0.009] | -0.004387 | -1.75 | 0.080 | not applied (n < 1000) | 0.233 | -2.9 | +8.2 | 0.1494 | 0.1522 |
| Time 181-250, pooled (%) | 783 | +0.067 [-0.001, +0.135] | 0.004525 | 1.94 | 0.052 | not applied (n < 1000) | 0.180 | -2.2 | +8.9 | 0.1546 | 0.1522 |
| Avg. daily time 181-250 (%) | 783 | +0.067 [-0.001, +0.134] | 0.004396 | 1.93 | 0.053 | not applied (n < 1000) | 0.180 | -2.1 | +9.0 | 0.1550 | 0.1522 |
| Time > 180, pooled (%) | 783 | +0.089 [+0.014, +0.164] | 0.003462 | 2.33 | 0.020* | not applied (n < 1000) | 0.095 | -5.0 | +6.1 | 0.1554 | 0.1522 |
| Avg. daily time > 180 (%) | 783 | +0.089 [+0.014, +0.163] | 0.003424 | 2.32 | 0.020* | not applied (n < 1000) | 0.097 | -4.9 | +6.2 | 0.1553 | 0.1522 |
| Nocturnal time > 180 (%) | 783 | +0.093 [+0.018, +0.168] | 0.003265 | 2.42 | 0.016* | not applied (n < 1000) | 0.087 | -5.5 | +5.6 | 0.1557 | 0.1522 |
| Time > 250, pooled (%) | 783 | +0.072 [-0.011, +0.155] | 0.004267 | 1.71 | 0.087 | not applied (n < 1000) | 0.240 | -2.7 | +8.4 | 0.1496 | 0.1522 |
| Avg. daily time > 250 (%) | 783 | +0.072 [-0.010, +0.155] | 0.004333 | 1.73 | 0.084 | not applied (n < 1000) | 0.237 | -2.8 | +8.3 | 0.1493 | 0.1522 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 783; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 783 | +0.063 [-0.142, +0.268] | 0.04609 | 0.60 | 0.548 | not applied (n < 1000) | 0.739 | +1.3 | +0.0 | 0.2769 | 0.2794 |
| Mean glucose (mg/dL) | 783 | +0.049 [-0.109, +0.208] | 0.001215 | 0.61 | 0.542 | not applied (n < 1000) | 0.739 | +1.6 | +0.3 | 0.2762 | 0.2794 |
| GMI (%) | 783 | +0.049 [-0.109, +0.208] | 0.05078 | 0.61 | 0.542 | not applied (n < 1000) | 0.739 | +1.6 | +0.3 | 0.2762 | 0.2794 |
| Nocturnal mean 00-06h (mg/dL) | 783 | +0.048 [-0.112, +0.209] | 0.001121 | 0.59 | 0.554 | not applied (n < 1000) | 0.739 | +1.6 | +0.3 | 0.2754 | 0.2794 |
| Glucose SD, pooled (mg/dL) | 783 | +0.073 [-0.086, +0.232] | 0.005957 | 0.90 | 0.369 | not applied (n < 1000) | 0.659 | +1.1 | -0.2 | 0.2774 | 0.2794 |
| Avg. daily SD (mg/dL) | 783 | +0.057 [-0.095, +0.208] | 0.005276 | 0.73 | 0.464 | not applied (n < 1000) | 0.689 | +1.4 | +0.1 | 0.2774 | 0.2794 |
| CV (%) | 783 | +0.073 [-0.071, +0.217] | 0.01323 | 0.99 | 0.321 | not applied (n < 1000) | 0.612 | +1.0 | -0.3 | 0.2787 | 0.2794 |
| Mean / SD ratio | 783 | -0.105 [-0.244, +0.034] | -0.1054 | -1.48 | 0.138 | not applied (n < 1000) | 0.348 | -0.1 | -1.4 | 0.2792 | 0.2794 |
| Avg. daily mean / SD | 783 | -0.086 [-0.232, +0.060] | -0.06912 | -1.16 | 0.247 | not applied (n < 1000) | 0.514 | +0.6 | -0.7 | 0.2786 | 0.2794 |
| MAG (mg/dL/h) | 783 | +0.017 [-0.130, +0.163] | 0.001716 | 0.22 | 0.823 | not applied (n < 1000) | 0.885 | +1.9 | +0.6 | 0.2779 | 0.2794 |
| Avg. daily range (mg/dL) | 783 | +0.073 [-0.073, +0.219] | 0.002021 | 0.98 | 0.328 | not applied (n < 1000) | 0.620 | +1.1 | -0.2 | 0.2784 | 0.2794 |
| SD of daily means (mg/dL) | 783 | +0.080 [-0.103, +0.263] | 0.009641 | 0.86 | 0.390 | not applied (n < 1000) | 0.671 | +0.9 | -0.4 | 0.2766 | 0.2794 |
| Time in range 70-180, pooled (%) | 783 | -0.073 [-0.233, +0.087] | -0.002862 | -0.90 | 0.370 | not applied (n < 1000) | 0.659 | +1.1 | -0.2 | 0.2773 | 0.2794 |
| Avg. daily time in range 70-180 (%) | 783 | -0.065 [-0.226, +0.096] | -0.002527 | -0.79 | 0.428 | not applied (n < 1000) | 0.689 | +1.3 | -0.0 | 0.2771 | 0.2794 |
| Any reading < 54 during wear (0/1) | 783 | -0.021 [-0.163, +0.121] | -0.04993 | -0.29 | 0.770 | not applied (n < 1000) | 0.863 | +1.9 | +0.6 | 0.2789 | 0.2794 |
| Time < 54, pooled (%) | 783 | +0.128 [-0.076, +0.332] | 0.223 | 1.23 | 0.220 | not applied (n < 1000) | 0.482 | -1.2 | -2.5 | 0.2808 | 0.2794 |
| Avg. daily time < 54 (%) | 783 | +0.088 [-0.167, +0.343] | 0.176 | 0.67 | 0.501 | not applied (n < 1000) | 0.713 | +0.5 | -0.8 | 0.2795 | 0.2794 |
| Time 54-69, pooled (%) | 783 | +0.051 [-0.121, +0.224] | 0.04934 | 0.59 | 0.558 | not applied (n < 1000) | 0.739 | +1.5 | +0.2 | 0.2792 | 0.2794 |
| Avg. daily time 54-69 (%) | 783 | +0.065 [-0.112, +0.241] | 0.05895 | 0.72 | 0.474 | not applied (n < 1000) | 0.697 | +1.2 | -0.1 | 0.2796 | 0.2794 |
| Time < 70, pooled (%) | 783 | +0.092 [-0.098, +0.281] | 0.0655 | 0.95 | 0.344 | not applied (n < 1000) | 0.633 | +0.4 | -0.9 | 0.2798 | 0.2794 |
| Avg. daily time < 70 (%) | 783 | +0.080 [-0.107, +0.266] | 0.05495 | 0.84 | 0.403 | not applied (n < 1000) | 0.676 | +0.8 | -0.5 | 0.2802 | 0.2794 |
| Time 54-250, pooled (%) | 783 | -0.061 [-0.224, +0.102] | -0.003585 | -0.73 | 0.466 | not applied (n < 1000) | 0.689 | +1.3 | +0.0 | 0.2773 | 0.2794 |
| Avg. daily time 54-250 (%) | 783 | -0.053 [-0.218, +0.111] | -0.003185 | -0.64 | 0.525 | not applied (n < 1000) | 0.735 | +1.5 | +0.2 | 0.2771 | 0.2794 |
| Time 181-250, pooled (%) | 783 | +0.049 [-0.100, +0.197] | 0.003281 | 0.64 | 0.520 | not applied (n < 1000) | 0.731 | +1.6 | +0.3 | 0.2765 | 0.2794 |
| Avg. daily time 181-250 (%) | 783 | +0.043 [-0.106, +0.193] | 0.002842 | 0.57 | 0.572 | not applied (n < 1000) | 0.743 | +1.7 | +0.4 | 0.2764 | 0.2794 |
| Time > 180, pooled (%) | 783 | +0.067 [-0.092, +0.226] | 0.002605 | 0.82 | 0.411 | not applied (n < 1000) | 0.676 | +1.2 | -0.1 | 0.2770 | 0.2794 |
| Avg. daily time > 180 (%) | 783 | +0.060 [-0.100, +0.220] | 0.002306 | 0.73 | 0.465 | not applied (n < 1000) | 0.689 | +1.4 | +0.1 | 0.2769 | 0.2794 |
| Nocturnal time > 180 (%) | 783 | +0.044 [-0.121, +0.208] | 0.00153 | 0.52 | 0.605 | not applied (n < 1000) | 0.754 | +1.7 | +0.4 | 0.2753 | 0.2794 |
| Time > 250, pooled (%) | 783 | +0.056 [-0.107, +0.219] | 0.003308 | 0.67 | 0.501 | not applied (n < 1000) | 0.713 | +1.4 | +0.1 | 0.2771 | 0.2794 |
| Avg. daily time > 250 (%) | 783 | +0.050 [-0.114, +0.215] | 0.003017 | 0.60 | 0.547 | not applied (n < 1000) | 0.739 | +1.5 | +0.2 | 0.2770 | 0.2794 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 783; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 783 | +0.225 [-0.222, +0.673] | 0.1649 | 0.99 | 0.324 | not applied (n < 1000) | 0.616 | +1.0 | +0.0 | 0.2100 | 0.2129 |
| Mean glucose (mg/dL) | 783 | +0.324 [-0.134, +0.782] | 0.007986 | 1.39 | 0.165 | not applied (n < 1000) | 0.392 | -0.1 | -1.1 | 0.2109 | 0.2129 |
| GMI (%) | 783 | +0.324 [-0.134, +0.782] | 0.3339 | 1.39 | 0.165 | not applied (n < 1000) | 0.392 | -0.1 | -1.1 | 0.2109 | 0.2129 |
| Nocturnal mean 00-06h (mg/dL) | 783 | +0.254 [-0.193, +0.701] | 0.005887 | 1.12 | 0.265 | not applied (n < 1000) | 0.542 | +0.7 | -0.3 | 0.2109 | 0.2129 |
| Glucose SD, pooled (mg/dL) | 783 | +0.114 [-0.332, +0.561] | 0.009334 | 0.50 | 0.616 | not applied (n < 1000) | 0.756 | +1.8 | +0.7 | 0.2107 | 0.2129 |
| Avg. daily SD (mg/dL) | 783 | +0.177 [-0.267, +0.621] | 0.01649 | 0.78 | 0.435 | not applied (n < 1000) | 0.689 | +1.4 | +0.4 | 0.2111 | 0.2129 |
| CV (%) | 783 | -0.153 [-0.595, +0.289] | -0.02778 | -0.68 | 0.498 | not applied (n < 1000) | 0.713 | +1.5 | +0.5 | 0.2098 | 0.2129 |
| Mean / SD ratio | 783 | +0.189 [-0.244, +0.622] | 0.1895 | 0.86 | 0.392 | not applied (n < 1000) | 0.671 | +1.3 | +0.2 | 0.2095 | 0.2129 |
| Avg. daily mean / SD | 783 | +0.065 [-0.377, +0.508] | 0.05234 | 0.29 | 0.773 | not applied (n < 1000) | 0.863 | +1.9 | +0.9 | 0.2075 | 0.2129 |
| MAG (mg/dL/h) | 783 | +0.125 [-0.299, +0.548] | 0.0128 | 0.58 | 0.564 | not applied (n < 1000) | 0.741 | +1.7 | +0.7 | 0.2117 | 0.2129 |
| Avg. daily range (mg/dL) | 783 | +0.167 [-0.263, +0.598] | 0.004621 | 0.76 | 0.447 | not applied (n < 1000) | 0.689 | +1.5 | +0.4 | 0.2107 | 0.2129 |
| SD of daily means (mg/dL) | 783 | -0.014 [-0.459, +0.431] | -0.001685 | -0.06 | 0.951 | not applied (n < 1000) | 0.971 | +2.0 | +1.0 | 0.2103 | 0.2129 |
| Time in range 70-180, pooled (%) | 783 | -0.177 [-0.651, +0.297] | -0.006926 | -0.73 | 0.465 | not applied (n < 1000) | 0.689 | +1.4 | +0.4 | 0.2102 | 0.2129 |
| Avg. daily time in range 70-180 (%) | 783 | -0.188 [-0.662, +0.287] | -0.007304 | -0.78 | 0.438 | not applied (n < 1000) | 0.689 | +1.3 | +0.3 | 0.2102 | 0.2129 |
| Any reading < 54 during wear (0/1) | 783 | +0.012 [-0.420, +0.444] | 0.02876 | 0.06 | 0.956 | not applied (n < 1000) | 0.971 | +2.0 | +1.0 | 0.2113 | 0.2129 |
| Time < 54, pooled (%) | 783 | -0.288 [-0.569, -0.008] | -0.5042 | -2.02 | 0.044* | not applied (n < 1000) | 0.163 | +0.2 | -0.8 | 0.2099 | 0.2129 |
| Avg. daily time < 54 (%) | 783 | -0.241 [-0.706, +0.223] | -0.4854 | -1.02 | 0.309 | not applied (n < 1000) | 0.603 | +0.8 | -0.3 | 0.2105 | 0.2129 |
| Time 54-69, pooled (%) | 783 | -0.012 [-0.492, +0.468] | -0.01132 | -0.05 | 0.962 | not applied (n < 1000) | 0.971 | +2.0 | +1.0 | 0.2097 | 0.2129 |
| Avg. daily time 54-69 (%) | 783 | +0.005 [-0.465, +0.475] | 0.004545 | 0.02 | 0.983 | not applied (n < 1000) | 0.986 | +2.0 | +1.0 | 0.2103 | 0.2129 |
| Time < 70, pooled (%) | 783 | -0.129 [-0.642, +0.385] | -0.09209 | -0.49 | 0.623 | not applied (n < 1000) | 0.761 | +1.7 | +0.6 | 0.2083 | 0.2129 |
| Avg. daily time < 70 (%) | 783 | -0.081 [-0.571, +0.410] | -0.05567 | -0.32 | 0.747 | not applied (n < 1000) | 0.845 | +1.9 | +0.9 | 0.2092 | 0.2129 |
| Time 54-250, pooled (%) | 783 | -0.170 [-0.620, +0.281] | -0.01004 | -0.74 | 0.460 | not applied (n < 1000) | 0.689 | +1.4 | +0.4 | 0.2097 | 0.2129 |
| Avg. daily time 54-250 (%) | 783 | -0.172 [-0.629, +0.284] | -0.01031 | -0.74 | 0.459 | not applied (n < 1000) | 0.689 | +1.4 | +0.4 | 0.2095 | 0.2129 |
| Time 181-250, pooled (%) | 783 | +0.102 [-0.355, +0.559] | 0.006875 | 0.44 | 0.661 | not applied (n < 1000) | 0.787 | +1.8 | +0.8 | 0.2095 | 0.2129 |
| Avg. daily time 181-250 (%) | 783 | +0.118 [-0.337, +0.573] | 0.007786 | 0.51 | 0.611 | not applied (n < 1000) | 0.754 | +1.7 | +0.7 | 0.2095 | 0.2129 |
| Time > 180, pooled (%) | 783 | +0.182 [-0.291, +0.656] | 0.007103 | 0.75 | 0.451 | not applied (n < 1000) | 0.689 | +1.3 | +0.3 | 0.2100 | 0.2129 |
| Avg. daily time > 180 (%) | 783 | +0.191 [-0.284, +0.665] | 0.007384 | 0.79 | 0.430 | not applied (n < 1000) | 0.689 | +1.3 | +0.3 | 0.2101 | 0.2129 |
| Nocturnal time > 180 (%) | 783 | +0.033 [-0.433, +0.498] | 0.001153 | 0.14 | 0.890 | not applied (n < 1000) | 0.932 | +2.0 | +1.0 | 0.2107 | 0.2129 |
| Time > 250, pooled (%) | 783 | +0.180 [-0.270, +0.630] | 0.01064 | 0.78 | 0.433 | not applied (n < 1000) | 0.689 | +1.4 | +0.3 | 0.2096 | 0.2129 |
| Avg. daily time > 250 (%) | 783 | +0.180 [-0.277, +0.636] | 0.01076 | 0.77 | 0.440 | not applied (n < 1000) | 0.689 | +1.4 | +0.3 | 0.2094 | 0.2129 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 783; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 783 | -1.812 [-3.185, -0.439] | -1.327 | -2.59 | 0.010** | not applied (n < 1000) | 0.063 | -6.2 | +0.0 | 0.0294 | 0.0243 |
| Mean glucose (mg/dL) | 783 | -1.317 [-2.660, +0.025] | -0.03245 | -1.92 | 0.054 | not applied (n < 1000) | 0.180 | -2.4 | +3.8 | 0.0243 | 0.0243 |
| GMI (%) | 783 | -1.317 [-2.660, +0.025] | -1.357 | -1.92 | 0.054 | not applied (n < 1000) | 0.180 | -2.4 | +3.8 | 0.0243 | 0.0243 |
| Nocturnal mean 00-06h (mg/dL) | 783 | -1.193 [-2.695, +0.309] | -0.02763 | -1.56 | 0.119 | not applied (n < 1000) | 0.310 | -1.5 | +4.6 | 0.0207 | 0.0243 |
| Glucose SD, pooled (mg/dL) | 783 | -1.022 [-2.486, +0.442] | -0.08337 | -1.37 | 0.171 | not applied (n < 1000) | 0.402 | -0.5 | +5.6 | 0.0235 | 0.0243 |
| Avg. daily SD (mg/dL) | 783 | -0.584 [-1.819, +0.650] | -0.05448 | -0.93 | 0.353 | not applied (n < 1000) | 0.637 | +1.2 | +7.3 | 0.0226 | 0.0243 |
| CV (%) | 783 | -0.160 [-1.400, +1.080] | -0.02905 | -0.25 | 0.801 | not applied (n < 1000) | 0.871 | +1.9 | +8.1 | 0.0217 | 0.0243 |
| Mean / SD ratio | 783 | +0.081 [-1.160, +1.322] | 0.08116 | 0.13 | 0.898 | not applied (n < 1000) | 0.936 | +2.0 | +8.1 | 0.0218 | 0.0243 |
| Avg. daily mean / SD | 783 | -0.424 [-1.607, +0.759] | -0.3402 | -0.70 | 0.483 | not applied (n < 1000) | 0.701 | +1.5 | +7.7 | 0.0221 | 0.0243 |
| MAG (mg/dL/h) | 783 | -0.036 [-1.403, +1.331] | -0.003701 | -0.05 | 0.959 | not applied (n < 1000) | 0.971 | +2.0 | +8.2 | 0.0185 | 0.0243 |
| Avg. daily range (mg/dL) | 783 | -0.353 [-1.578, +0.873] | -0.009762 | -0.56 | 0.573 | not applied (n < 1000) | 0.743 | +1.7 | +7.9 | 0.0210 | 0.0243 |
| SD of daily means (mg/dL) | 783 | -1.723 [-3.835, +0.389] | -0.2075 | -1.60 | 0.110 | not applied (n < 1000) | 0.286 | -5.4 | +0.8 | 0.0190 | 0.0243 |
| Time in range 70-180, pooled (%) | 783 | +1.223 [-0.170, +2.616] | 0.04794 | 1.72 | 0.085 | not applied (n < 1000) | 0.238 | -1.7 | +4.4 | 0.0236 | 0.0243 |
| Avg. daily time in range 70-180 (%) | 783 | +1.268 [-0.128, +2.663] | 0.04929 | 1.78 | 0.075 | not applied (n < 1000) | 0.222 | -2.0 | +4.2 | 0.0239 | 0.0243 |
| Any reading < 54 during wear (0/1) | 783 | +0.171 [-1.172, +1.514] | 0.404 | 0.25 | 0.803 | not applied (n < 1000) | 0.871 | +1.9 | +8.1 | 0.0200 | 0.0243 |
| Time < 54, pooled (%) | 783 | -0.492 [-1.951, +0.967] | -0.8603 | -0.66 | 0.509 | not applied (n < 1000) | 0.722 | +1.3 | +7.5 | 0.0226 | 0.0243 |
| Avg. daily time < 54 (%) | 783 | -0.507 [-1.183, +0.168] | -1.02 | -1.47 | 0.141 | not applied (n < 1000) | 0.353 | +1.3 | +7.5 | 0.0237 | 0.0243 |
| Time 54-69, pooled (%) | 783 | -0.509 [-1.788, +0.769] | -0.4886 | -0.78 | 0.435 | not applied (n < 1000) | 0.689 | +1.3 | +7.5 | 0.0234 | 0.0243 |
| Avg. daily time 54-69 (%) | 783 | -0.709 [-1.824, +0.406] | -0.6477 | -1.25 | 0.213 | not applied (n < 1000) | 0.473 | +0.7 | +6.8 | 0.0246 | 0.0243 |
| Time < 70, pooled (%) | 783 | -0.586 [-1.657, +0.485] | -0.4193 | -1.07 | 0.283 | not applied (n < 1000) | 0.569 | +1.1 | +7.2 | 0.0240 | 0.0243 |
| Avg. daily time < 70 (%) | 783 | -0.715 [-1.686, +0.256] | -0.494 | -1.44 | 0.149 | not applied (n < 1000) | 0.366 | +0.6 | +6.8 | 0.0247 | 0.0243 |
| Time 54-250, pooled (%) | 783 | +1.730 [+0.401, +3.059] | 0.1023 | 2.55 | 0.011* | not applied (n < 1000) | 0.065 | -5.6 | +0.5 | 0.0289 | 0.0243 |
| Avg. daily time 54-250 (%) | 783 | +1.780 [+0.428, +3.132] | 0.1065 | 2.58 | 0.010** | not applied (n < 1000) | 0.063 | -6.1 | +0.1 | 0.0296 | 0.0243 |
| Time 181-250, pooled (%) | 783 | -0.044 [-1.622, +1.535] | -0.002943 | -0.05 | 0.957 | not applied (n < 1000) | 0.971 | +2.0 | +8.2 | 0.0187 | 0.0243 |
| Avg. daily time 181-250 (%) | 783 | -0.076 [-1.629, +1.478] | -0.004986 | -0.10 | 0.924 | not applied (n < 1000) | 0.957 | +2.0 | +8.2 | 0.0188 | 0.0243 |
| Time > 180, pooled (%) | 783 | -1.176 [-2.570, +0.217] | -0.0458 | -1.65 | 0.098 | not applied (n < 1000) | 0.259 | -1.5 | +4.7 | 0.0231 | 0.0243 |
| Avg. daily time > 180 (%) | 783 | -1.213 [-2.609, +0.183] | -0.04691 | -1.70 | 0.089 | not applied (n < 1000) | 0.240 | -1.7 | +4.5 | 0.0234 | 0.0243 |
| Nocturnal time > 180 (%) | 783 | -0.815 [-2.379, +0.749] | -0.02867 | -1.02 | 0.307 | not applied (n < 1000) | 0.602 | +0.4 | +6.5 | 0.0197 | 0.0243 |
| Time > 250, pooled (%) | 783 | -1.711 [-3.041, -0.381] | -0.1011 | -2.52 | 0.012* | not applied (n < 1000) | 0.070 | -5.5 | +0.7 | 0.0288 | 0.0243 |
| Avg. daily time > 250 (%) | 783 | -1.763 [-3.116, -0.409] | -0.1054 | -2.55 | 0.011* | not applied (n < 1000) | 0.065 | -5.9 | +0.2 | 0.0295 | 0.0243 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 690; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 690 | +373.534 [-45.898, +792.966] | 270.5 | 1.75 | 0.081 | not applied (n < 1000) | 0.233 | -2.1 | +0.0 | 0.1249 | 0.1276 |
| Mean glucose (mg/dL) | 690 | +159.583 [-258.723, +577.889] | 3.935 | 0.75 | 0.455 | not applied (n < 1000) | 0.689 | +1.2 | +3.3 | 0.1200 | 0.1276 |
| GMI (%) | 690 | +159.583 [-258.723, +577.889] | 164.5 | 0.75 | 0.455 | not applied (n < 1000) | 0.689 | +1.2 | +3.3 | 0.1200 | 0.1276 |
| Nocturnal mean 00-06h (mg/dL) | 690 | +270.753 [-162.931, +704.437] | 6.279 | 1.22 | 0.221 | not applied (n < 1000) | 0.482 | -0.2 | +1.9 | 0.1194 | 0.1276 |
| Glucose SD, pooled (mg/dL) | 690 | +60.235 [-355.260, +475.730] | 4.921 | 0.28 | 0.776 | not applied (n < 1000) | 0.863 | +1.9 | +4.0 | 0.1192 | 0.1276 |
| Avg. daily SD (mg/dL) | 690 | +5.141 [-384.804, +395.085] | 0.4803 | 0.03 | 0.979 | not applied (n < 1000) | 0.984 | +2.0 | +4.1 | 0.1211 | 0.1276 |
| CV (%) | 690 | -143.859 [-475.177, +187.459] | -26.22 | -0.85 | 0.395 | not applied (n < 1000) | 0.671 | +1.4 | +3.5 | 0.1248 | 0.1276 |
| Mean / SD ratio | 690 | -31.689 [-354.002, +290.624] | -31.66 | -0.19 | 0.847 | not applied (n < 1000) | 0.899 | +2.0 | +4.1 | 0.1243 | 0.1276 |
| Avg. daily mean / SD | 690 | -76.187 [-391.857, +239.483] | -61.31 | -0.47 | 0.636 | not applied (n < 1000) | 0.769 | +1.8 | +3.9 | 0.1254 | 0.1276 |
| MAG (mg/dL/h) | 690 | +346.488 [-55.192, +748.168] | 35.81 | 1.69 | 0.091 | not applied (n < 1000) | 0.243 | -1.7 | +0.4 | 0.1250 | 0.1276 |
| Avg. daily range (mg/dL) | 690 | +37.479 [-344.802, +419.760] | 1.046 | 0.19 | 0.848 | not applied (n < 1000) | 0.899 | +2.0 | +4.0 | 0.1213 | 0.1276 |
| SD of daily means (mg/dL) | 690 | +282.038 [-149.834, +713.910] | 34.28 | 1.28 | 0.201 | not applied (n < 1000) | 0.457 | -0.4 | +1.7 | 0.1219 | 0.1276 |
| Time in range 70-180, pooled (%) | 690 | -170.315 [-594.195, +253.565] | -6.708 | -0.79 | 0.431 | not applied (n < 1000) | 0.689 | +1.2 | +3.2 | 0.1188 | 0.1276 |
| Avg. daily time in range 70-180 (%) | 690 | -164.246 [-587.399, +258.907] | -6.417 | -0.76 | 0.447 | not applied (n < 1000) | 0.689 | +1.2 | +3.3 | 0.1189 | 0.1276 |
| Any reading < 54 during wear (0/1) | 690 | -298.026 [-642.856, +46.803] | -699.6 | -1.69 | 0.090 | not applied (n < 1000) | 0.243 | -0.9 | +1.2 | 0.1252 | 0.1276 |
| Time < 54, pooled (%) | 690 | -219.730 [-957.252, +517.792] | -362 | -0.58 | 0.559 | not applied (n < 1000) | 0.739 | +0.4 | +2.5 | 0.1218 | 0.1276 |
| Avg. daily time < 54 (%) | 690 | -273.818 [-619.977, +72.342] | -519.2 | -1.55 | 0.121 | not applied (n < 1000) | 0.310 | -0.4 | +1.7 | 0.1276 | 0.1276 |
| Time 54-69, pooled (%) | 690 | -333.591 [-651.835, -15.347] | -318.1 | -2.05 | 0.040* | not applied (n < 1000) | 0.159 | -1.5 | +0.6 | 0.1294 | 0.1276 |
| Avg. daily time 54-69 (%) | 690 | -352.239 [-662.715, -41.763] | -312 | -2.22 | 0.026* | not applied (n < 1000) | 0.115 | -1.9 | +0.2 | 0.1300 | 0.1276 |
| Time < 70, pooled (%) | 690 | -339.792 [-610.857, -68.727] | -236.9 | -2.46 | 0.014* | not applied (n < 1000) | 0.080 | -1.7 | +0.4 | 0.1297 | 0.1276 |
| Avg. daily time < 70 (%) | 690 | -362.163 [-621.751, -102.575] | -240.5 | -2.73 | 0.006** | not applied (n < 1000) | 0.050 | -2.1 | -0.1 | 0.1305 | 0.1276 |
| Time 54-250, pooled (%) | 690 | -2.200 [-426.136, +421.735] | -0.1303 | -0.01 | 0.992 | not applied (n < 1000) | 0.992 | +2.0 | +4.1 | 0.1207 | 0.1276 |
| Avg. daily time 54-250 (%) | 690 | -10.383 [-419.832, +399.066] | -0.6242 | -0.05 | 0.960 | not applied (n < 1000) | 0.971 | +2.0 | +4.1 | 0.1209 | 0.1276 |
| Time 181-250, pooled (%) | 690 | +302.779 [-79.705, +685.262] | 20.37 | 1.55 | 0.121 | not applied (n < 1000) | 0.310 | -0.8 | +1.3 | 0.1252 | 0.1276 |
| Avg. daily time 181-250 (%) | 690 | +283.276 [-99.613, +666.165] | 18.66 | 1.45 | 0.147 | not applied (n < 1000) | 0.363 | -0.4 | +1.7 | 0.1245 | 0.1276 |
| Time > 180, pooled (%) | 690 | +189.199 [-233.316, +611.715] | 7.402 | 0.88 | 0.380 | not applied (n < 1000) | 0.668 | +1.0 | +3.0 | 0.1191 | 0.1276 |
| Avg. daily time > 180 (%) | 690 | +185.658 [-236.473, +607.789] | 7.215 | 0.86 | 0.389 | not applied (n < 1000) | 0.671 | +1.0 | +3.1 | 0.1191 | 0.1276 |
| Nocturnal time > 180 (%) | 690 | +245.206 [-186.967, +677.380] | 8.665 | 1.11 | 0.266 | not applied (n < 1000) | 0.543 | +0.3 | +2.4 | 0.1181 | 0.1276 |
| Time > 250, pooled (%) | 690 | +10.603 [-413.711, +434.917] | 0.6277 | 0.05 | 0.961 | not applied (n < 1000) | 0.971 | +2.0 | +4.1 | 0.1206 | 0.1276 |
| Avg. daily time > 250 (%) | 690 | +19.587 [-390.235, +429.409] | 1.178 | 0.09 | 0.925 | not applied (n < 1000) | 0.957 | +2.0 | +4.1 | 0.1209 | 0.1276 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 690; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 690 | +1.136 [-0.028, +2.301] | 0.823 | 1.91 | 0.056 | not applied (n < 1000) | 0.180 | -2.4 | +0.0 | 0.1471 | 0.1476 |
| Mean glucose (mg/dL) | 690 | +0.512 [-0.671, +1.696] | 0.01263 | 0.85 | 0.396 | not applied (n < 1000) | 0.671 | +1.1 | +3.5 | 0.1421 | 0.1476 |
| GMI (%) | 690 | +0.512 [-0.671, +1.696] | 0.5282 | 0.85 | 0.396 | not applied (n < 1000) | 0.671 | +1.1 | +3.5 | 0.1421 | 0.1476 |
| Nocturnal mean 00-06h (mg/dL) | 690 | +0.793 [-0.448, +2.034] | 0.0184 | 1.25 | 0.210 | not applied (n < 1000) | 0.470 | -0.1 | +2.2 | 0.1419 | 0.1476 |
| Glucose SD, pooled (mg/dL) | 690 | +0.455 [-0.744, +1.654] | 0.03718 | 0.74 | 0.457 | not applied (n < 1000) | 0.689 | +1.3 | +3.7 | 0.1403 | 0.1476 |
| Avg. daily SD (mg/dL) | 690 | +0.249 [-0.883, +1.380] | 0.02325 | 0.43 | 0.666 | not applied (n < 1000) | 0.788 | +1.8 | +4.2 | 0.1417 | 0.1476 |
| CV (%) | 690 | -0.206 [-1.180, +0.768] | -0.03753 | -0.41 | 0.679 | not applied (n < 1000) | 0.792 | +1.8 | +4.2 | 0.1448 | 0.1476 |
| Mean / SD ratio | 690 | -0.332 [-1.270, +0.606] | -0.3317 | -0.69 | 0.488 | not applied (n < 1000) | 0.707 | +1.6 | +4.0 | 0.1455 | 0.1476 |
| Avg. daily mean / SD | 690 | -0.390 [-1.309, +0.529] | -0.3139 | -0.83 | 0.406 | not applied (n < 1000) | 0.676 | +1.4 | +3.8 | 0.1460 | 0.1476 |
| MAG (mg/dL/h) | 690 | +1.130 [-0.029, +2.290] | 0.1168 | 1.91 | 0.056 | not applied (n < 1000) | 0.180 | -2.6 | -0.2 | 0.1480 | 0.1476 |
| Avg. daily range (mg/dL) | 690 | +0.354 [-0.766, +1.473] | 0.00987 | 0.62 | 0.536 | not applied (n < 1000) | 0.739 | +1.6 | +4.0 | 0.1426 | 0.1476 |
| SD of daily means (mg/dL) | 690 | +0.928 [-0.266, +2.122] | 0.1128 | 1.52 | 0.128 | not applied (n < 1000) | 0.323 | -1.0 | +1.4 | 0.1425 | 0.1476 |
| Time in range 70-180, pooled (%) | 690 | -0.519 [-1.713, +0.674] | -0.02045 | -0.85 | 0.394 | not applied (n < 1000) | 0.671 | +1.1 | +3.5 | 0.1412 | 0.1476 |
| Avg. daily time in range 70-180 (%) | 690 | -0.509 [-1.703, +0.686] | -0.01987 | -0.83 | 0.404 | not applied (n < 1000) | 0.676 | +1.1 | +3.5 | 0.1413 | 0.1476 |
| Any reading < 54 during wear (0/1) | 690 | -0.620 [-1.639, +0.399] | -1.456 | -1.19 | 0.233 | not applied (n < 1000) | 0.494 | +0.5 | +2.9 | 0.1458 | 0.1476 |
| Time < 54, pooled (%) | 690 | -0.592 [-1.940, +0.756] | -0.9754 | -0.86 | 0.389 | not applied (n < 1000) | 0.671 | +0.7 | +3.1 | 0.1460 | 0.1476 |
| Avg. daily time < 54 (%) | 690 | -0.777 [-1.670, +0.116] | -1.473 | -1.71 | 0.088 | not applied (n < 1000) | 0.240 | -0.3 | +2.1 | 0.1483 | 0.1476 |
| Time 54-69, pooled (%) | 690 | -0.842 [-1.745, +0.060] | -0.8032 | -1.83 | 0.067 | not applied (n < 1000) | 0.202 | -0.6 | +1.8 | 0.1488 | 0.1476 |
| Avg. daily time 54-69 (%) | 690 | -0.940 [-1.838, -0.043] | -0.8328 | -2.05 | 0.040* | not applied (n < 1000) | 0.159 | -1.2 | +1.1 | 0.1498 | 0.1476 |
| Time < 70, pooled (%) | 690 | -0.874 [-1.671, -0.077] | -0.6094 | -2.15 | 0.032* | not applied (n < 1000) | 0.131 | -0.8 | +1.6 | 0.1492 | 0.1476 |
| Avg. daily time < 70 (%) | 690 | -0.983 [-1.789, -0.177] | -0.6528 | -2.39 | 0.017* | not applied (n < 1000) | 0.087 | -1.5 | +0.8 | 0.1503 | 0.1476 |
| Time 54-250, pooled (%) | 690 | -0.136 [-1.332, +1.060] | -0.008041 | -0.22 | 0.824 | not applied (n < 1000) | 0.885 | +1.9 | +4.3 | 0.1421 | 0.1476 |
| Avg. daily time 54-250 (%) | 690 | -0.160 [-1.315, +0.996] | -0.009607 | -0.27 | 0.786 | not applied (n < 1000) | 0.863 | +1.9 | +4.3 | 0.1424 | 0.1476 |
| Time 181-250, pooled (%) | 690 | +0.764 [-0.338, +1.866] | 0.05137 | 1.36 | 0.174 | not applied (n < 1000) | 0.407 | -0.1 | +2.3 | 0.1451 | 0.1476 |
| Avg. daily time 181-250 (%) | 690 | +0.726 [-0.379, +1.830] | 0.04779 | 1.29 | 0.198 | not applied (n < 1000) | 0.454 | +0.2 | +2.5 | 0.1445 | 0.1476 |
| Time > 180, pooled (%) | 690 | +0.567 [-0.624, +1.758] | 0.02218 | 0.93 | 0.351 | not applied (n < 1000) | 0.637 | +0.9 | +3.3 | 0.1415 | 0.1476 |
| Avg. daily time > 180 (%) | 690 | +0.566 [-0.626, +1.759] | 0.022 | 0.93 | 0.352 | not applied (n < 1000) | 0.637 | +0.9 | +3.3 | 0.1416 | 0.1476 |
| Nocturnal time > 180 (%) | 690 | +0.671 [-0.552, +1.894] | 0.02372 | 1.08 | 0.282 | not applied (n < 1000) | 0.569 | +0.5 | +2.9 | 0.1410 | 0.1476 |
| Time > 250, pooled (%) | 690 | +0.158 [-1.038, +1.355] | 0.009378 | 0.26 | 0.795 | not applied (n < 1000) | 0.868 | +1.9 | +4.3 | 0.1422 | 0.1476 |
| Avg. daily time > 250 (%) | 690 | +0.186 [-0.971, +1.343] | 0.01118 | 0.31 | 0.753 | not applied (n < 1000) | 0.845 | +1.9 | +4.3 | 0.1424 | 0.1476 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 692; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 692 | +1.726 [+1.083, +2.369] | 1.25 | 5.26 | 1.4e-07*** | not applied (n < 1000) | 9.1e-06 (q<0.05) | -24.4 | +0.0 | 0.1435 | 0.1112 |
| Mean glucose (mg/dL) | 692 | +1.815 [+1.123, +2.508] | 0.04472 | 5.14 | 2.8e-07*** | not applied (n < 1000) | 1.2e-05 (q<0.05) | -28.0 | -3.5 | 0.1473 | 0.1112 |
| GMI (%) | 692 | +1.815 [+1.123, +2.508] | 1.87 | 5.14 | 2.8e-07*** | not applied (n < 1000) | 1.2e-05 (q<0.05) | -28.0 | -3.5 | 0.1473 | 0.1112 |
| Nocturnal mean 00-06h (mg/dL) | 692 | +1.691 [+0.998, +2.384] | 0.03924 | 4.79 | 1.7e-06*** | not applied (n < 1000) | 4.2e-05 (q<0.05) | -23.5 | +0.9 | 0.1414 | 0.1112 |
| Glucose SD, pooled (mg/dL) | 692 | +1.334 [+0.592, +2.076] | 0.1085 | 3.52 | 4.3e-04*** | not applied (n < 1000) | 0.007 (q<0.05) | -13.4 | +11.1 | 0.1268 | 0.1112 |
| Avg. daily SD (mg/dL) | 692 | +1.201 [+0.471, +1.931] | 0.1117 | 3.22 | 0.001** | not applied (n < 1000) | 0.017 (q<0.05) | -10.6 | +13.9 | 0.1239 | 0.1112 |
| CV (%) | 692 | -0.045 [-0.698, +0.608] | -0.008237 | -0.14 | 0.892 | not applied (n < 1000) | 0.932 | +2.0 | +26.4 | 0.1096 | 0.1112 |
| Mean / SD ratio | 692 | -0.037 [-0.696, +0.622] | -0.03695 | -0.11 | 0.913 | not applied (n < 1000) | 0.949 | +2.0 | +26.4 | 0.1094 | 0.1112 |
| Avg. daily mean / SD | 692 | +0.051 [-0.590, +0.692] | 0.04123 | 0.16 | 0.876 | not applied (n < 1000) | 0.924 | +2.0 | +26.4 | 0.1101 | 0.1112 |
| MAG (mg/dL/h) | 692 | +0.787 [+0.095, +1.480] | 0.08107 | 2.23 | 0.026* | not applied (n < 1000) | 0.115 | -3.7 | +20.7 | 0.1099 | 0.1112 |
| Avg. daily range (mg/dL) | 692 | +0.999 [+0.311, +1.688] | 0.02781 | 2.85 | 0.004** | not applied (n < 1000) | 0.044 (q<0.05) | -6.9 | +17.6 | 0.1183 | 0.1112 |
| SD of daily means (mg/dL) | 692 | +1.580 [+0.868, +2.292] | 0.191 | 4.35 | 1.4e-05*** | not applied (n < 1000) | 2.9e-04 (q<0.05) | -20.4 | +4.0 | 0.1312 | 0.1112 |
| Time in range 70-180, pooled (%) | 692 | -1.900 [-2.605, -1.196] | -0.07481 | -5.29 | 1.2e-07*** | not applied (n < 1000) | 9.1e-06 (q<0.05) | -30.2 | -5.8 | 0.1495 | 0.1112 |
| Avg. daily time in range 70-180 (%) | 692 | -1.873 [-2.578, -1.168] | -0.07314 | -5.21 | 1.9e-07*** | not applied (n < 1000) | 1.0e-05 (q<0.05) | -29.3 | -4.8 | 0.1479 | 0.1112 |
| Any reading < 54 during wear (0/1) | 692 | -0.271 [-0.908, +0.366] | -0.635 | -0.83 | 0.405 | not applied (n < 1000) | 0.676 | +1.3 | +25.7 | 0.1103 | 0.1112 |
| Time < 54, pooled (%) | 692 | +0.013 [-0.303, +0.330] | 0.02206 | 0.08 | 0.934 | not applied (n < 1000) | 0.961 | +2.0 | +26.4 | 0.1100 | 0.1112 |
| Avg. daily time < 54 (%) | 692 | -0.169 [-0.791, +0.454] | -0.3203 | -0.53 | 0.595 | not applied (n < 1000) | 0.754 | +1.7 | +26.2 | 0.1090 | 0.1112 |
| Time 54-69, pooled (%) | 692 | -0.280 [-1.029, +0.470] | -0.267 | -0.73 | 0.465 | not applied (n < 1000) | 0.689 | +1.3 | +25.7 | 0.1101 | 0.1112 |
| Avg. daily time 54-69 (%) | 692 | -0.358 [-1.150, +0.434] | -0.3176 | -0.89 | 0.375 | not applied (n < 1000) | 0.663 | +0.8 | +25.2 | 0.1101 | 0.1112 |
| Time < 70, pooled (%) | 692 | -0.200 [-0.779, +0.380] | -0.1393 | -0.68 | 0.499 | not applied (n < 1000) | 0.713 | +1.6 | +26.1 | 0.1100 | 0.1112 |
| Avg. daily time < 70 (%) | 692 | -0.329 [-1.008, +0.350] | -0.2188 | -0.95 | 0.342 | not applied (n < 1000) | 0.633 | +1.0 | +25.4 | 0.1103 | 0.1112 |
| Time 54-250, pooled (%) | 692 | -1.119 [-1.814, -0.423] | -0.06623 | -3.15 | 0.002** | not applied (n < 1000) | 0.021 (q<0.05) | -9.4 | +15.0 | 0.1226 | 0.1112 |
| Avg. daily time 54-250 (%) | 692 | -1.123 [-1.828, -0.419] | -0.0675 | -3.12 | 0.002** | not applied (n < 1000) | 0.021 (q<0.05) | -9.5 | +14.9 | 0.1227 | 0.1112 |
| Time 181-250, pooled (%) | 692 | +1.883 [+1.210, +2.556] | 0.1267 | 5.48 | 4.2e-08*** | not applied (n < 1000) | 8.8e-06 (q<0.05) | -30.9 | -6.4 | 0.1501 | 0.1112 |
| Avg. daily time 181-250 (%) | 692 | +1.844 [+1.171, +2.517] | 0.1215 | 5.37 | 7.8e-08*** | not applied (n < 1000) | 9.1e-06 (q<0.05) | -29.4 | -5.0 | 0.1478 | 0.1112 |
| Time > 180, pooled (%) | 692 | +1.894 [+1.193, +2.595] | 0.07406 | 5.30 | 1.2e-07*** | not applied (n < 1000) | 9.1e-06 (q<0.05) | -30.1 | -5.7 | 0.1495 | 0.1112 |
| Avg. daily time > 180 (%) | 692 | +1.878 [+1.177, +2.579] | 0.07293 | 5.25 | 1.5e-07*** | not applied (n < 1000) | 9.1e-06 (q<0.05) | -29.5 | -5.1 | 0.1484 | 0.1112 |
| Nocturnal time > 180 (%) | 692 | +1.536 [+0.832, +2.241] | 0.05432 | 4.27 | 1.9e-05*** | not applied (n < 1000) | 3.8e-04 (q<0.05) | -18.5 | +5.9 | 0.1344 | 0.1112 |
| Time > 250, pooled (%) | 692 | +1.118 [+0.424, +1.812] | 0.06617 | 3.16 | 0.002** | not applied (n < 1000) | 0.021 (q<0.05) | -9.4 | +15.1 | 0.1226 | 0.1112 |
| Avg. daily time > 250 (%) | 692 | +1.129 [+0.424, +1.833] | 0.06782 | 3.14 | 0.002** | not applied (n < 1000) | 0.021 (q<0.05) | -9.6 | +14.8 | 0.1229 | 0.1112 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 694; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 694 | -6.114 [-10.746, -1.483] | -4.496 | -2.59 | 0.010** | not applied (n < 1000) | 0.063 | -3.3 | +0.0 | 0.0007 | -0.0046 |
| Mean glucose (mg/dL) | 694 | -1.554 [-6.776, +3.669] | -0.03913 | -0.58 | 0.560 | not applied (n < 1000) | 0.739 | +1.7 | +5.0 | -0.0065 | -0.0046 |
| GMI (%) | 694 | -1.554 [-6.776, +3.669] | -1.636 | -0.58 | 0.560 | not applied (n < 1000) | 0.739 | +1.7 | +5.0 | -0.0065 | -0.0046 |
| Nocturnal mean 00-06h (mg/dL) | 694 | -0.370 [-5.650, +4.911] | -0.008754 | -0.14 | 0.891 | not applied (n < 1000) | 0.932 | +2.0 | +5.3 | -0.0071 | -0.0046 |
| Glucose SD, pooled (mg/dL) | 694 | -5.412 [-10.644, -0.180] | -0.4407 | -2.03 | 0.043* | not applied (n < 1000) | 0.162 | -2.1 | +1.3 | -0.0022 | -0.0046 |
| Avg. daily SD (mg/dL) | 694 | -5.048 [-10.212, +0.116] | -0.4709 | -1.92 | 0.055 | not applied (n < 1000) | 0.180 | -1.6 | +1.7 | -0.0019 | -0.0046 |
| CV (%) | 694 | -4.268 [-9.248, +0.713] | -0.7781 | -1.68 | 0.093 | not applied (n < 1000) | 0.247 | -0.7 | +2.6 | -0.0067 | -0.0046 |
| Mean / SD ratio | 694 | +5.434 [+0.646, +10.222] | 5.5 | 2.22 | 0.026* | not applied (n < 1000) | 0.115 | -2.5 | +0.9 | -0.0036 | -0.0046 |
| Avg. daily mean / SD | 694 | +6.421 [+1.547, +11.294] | 5.211 | 2.58 | 0.010** | not applied (n < 1000) | 0.063 | -4.3 | -1.0 | 0.0025 | -0.0046 |
| MAG (mg/dL/h) | 694 | -9.995 [-14.943, -5.048] | -1.036 | -3.96 | 7.5e-05*** | not applied (n < 1000) | 0.001 (q<0.05) | -13.1 | -9.8 | 0.0143 | -0.0046 |
| Avg. daily range (mg/dL) | 694 | -5.278 [-10.360, -0.197] | -0.1475 | -2.04 | 0.042* | not applied (n < 1000) | 0.162 | -2.0 | +1.3 | -0.0006 | -0.0046 |
| SD of daily means (mg/dL) | 694 | -5.236 [-10.555, +0.083] | -0.6333 | -1.93 | 0.054 | not applied (n < 1000) | 0.180 | -1.9 | +1.4 | -0.0047 | -0.0046 |
| Time in range 70-180, pooled (%) | 694 | +1.285 [-4.058, +6.628] | 0.05135 | 0.47 | 0.637 | not applied (n < 1000) | 0.769 | +1.8 | +5.1 | -0.0074 | -0.0046 |
| Avg. daily time in range 70-180 (%) | 694 | +1.101 [-4.265, +6.466] | 0.04362 | 0.40 | 0.688 | not applied (n < 1000) | 0.798 | +1.8 | +5.2 | -0.0074 | -0.0046 |
| Any reading < 54 during wear (0/1) | 694 | +1.859 [-3.164, +6.883] | 4.338 | 0.73 | 0.468 | not applied (n < 1000) | 0.690 | +1.5 | +4.8 | -0.0076 | -0.0046 |
| Time < 54, pooled (%) | 694 | -1.158 [-3.092, +0.776] | -1.911 | -1.17 | 0.241 | not applied (n < 1000) | 0.503 | +1.8 | +5.1 | -0.0046 | -0.0046 |
| Avg. daily time < 54 (%) | 694 | -0.667 [-3.230, +1.895] | -1.266 | -0.51 | 0.610 | not applied (n < 1000) | 0.754 | +1.9 | +5.3 | -0.0050 | -0.0046 |
| Time 54-69, pooled (%) | 694 | +3.821 [-1.473, +9.115] | 3.644 | 1.41 | 0.157 | not applied (n < 1000) | 0.382 | -0.2 | +3.1 | -0.0027 | -0.0046 |
| Avg. daily time 54-69 (%) | 694 | +3.265 [-1.603, +8.133] | 2.894 | 1.31 | 0.189 | not applied (n < 1000) | 0.438 | +0.4 | +3.7 | -0.0036 | -0.0046 |
| Time < 70, pooled (%) | 694 | +2.306 [-2.512, +7.124] | 1.609 | 0.94 | 0.348 | not applied (n < 1000) | 0.637 | +1.2 | +4.5 | -0.0056 | -0.0046 |
| Avg. daily time < 70 (%) | 694 | +2.213 [-1.980, +6.406] | 1.47 | 1.03 | 0.301 | not applied (n < 1000) | 0.599 | +1.3 | +4.6 | -0.0051 | -0.0046 |
| Time 54-250, pooled (%) | 694 | +0.844 [-4.118, +5.806] | 0.05175 | 0.33 | 0.739 | not applied (n < 1000) | 0.841 | +1.9 | +5.2 | -0.0080 | -0.0046 |
| Avg. daily time 54-250 (%) | 694 | +0.712 [-4.276, +5.700] | 0.04433 | 0.28 | 0.780 | not applied (n < 1000) | 0.863 | +1.9 | +5.2 | -0.0081 | -0.0046 |
| Time 181-250, pooled (%) | 694 | -1.452 [-7.015, +4.112] | -0.09795 | -0.51 | 0.609 | not applied (n < 1000) | 0.754 | +1.7 | +5.0 | -0.0073 | -0.0046 |
| Avg. daily time 181-250 (%) | 694 | -1.272 [-6.828, +4.283] | -0.08411 | -0.45 | 0.653 | not applied (n < 1000) | 0.780 | +1.8 | +5.1 | -0.0073 | -0.0046 |
| Time > 180, pooled (%) | 694 | -1.413 [-6.756, +3.930] | -0.05609 | -0.52 | 0.604 | not applied (n < 1000) | 0.754 | +1.7 | +5.0 | -0.0072 | -0.0046 |
| Avg. daily time > 180 (%) | 694 | -1.232 [-6.592, +4.128] | -0.04857 | -0.45 | 0.652 | not applied (n < 1000) | 0.780 | +1.8 | +5.1 | -0.0072 | -0.0046 |
| Nocturnal time > 180 (%) | 694 | +0.616 [-4.739, +5.971] | 0.02206 | 0.23 | 0.822 | not applied (n < 1000) | 0.885 | +1.9 | +5.3 | -0.0071 | -0.0046 |
| Time > 250, pooled (%) | 694 | -0.798 [-5.760, +4.165] | -0.04892 | -0.32 | 0.753 | not applied (n < 1000) | 0.845 | +1.9 | +5.2 | -0.0081 | -0.0046 |
| Avg. daily time > 250 (%) | 694 | -0.688 [-5.675, +4.299] | -0.04288 | -0.27 | 0.787 | not applied (n < 1000) | 0.863 | +1.9 | +5.3 | -0.0082 | -0.0046 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 692; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 692 | +3.977 [+2.673, +5.281] | 2.879 | 5.98 | 2.3e-09*** | not applied (n < 1000) | 9.5e-07 (q<0.05) | -30.9 | +0.0 | 0.1111 | 0.0692 |
| Mean glucose (mg/dL) | 692 | +3.595 [+2.076, +5.114] | 0.08865 | 4.64 | 3.5e-06*** | not applied (n < 1000) | 7.7e-05 (q<0.05) | -25.4 | +5.5 | 0.1005 | 0.0692 |
| GMI (%) | 692 | +3.595 [+2.076, +5.114] | 3.706 | 4.64 | 3.5e-06*** | not applied (n < 1000) | 7.7e-05 (q<0.05) | -25.4 | +5.5 | 0.1005 | 0.0692 |
| Nocturnal mean 00-06h (mg/dL) | 692 | +3.165 [+1.619, +4.712] | 0.0735 | 4.01 | 6.0e-05*** | not applied (n < 1000) | 0.001 (q<0.05) | -18.8 | +12.1 | 0.0922 | 0.0692 |
| Glucose SD, pooled (mg/dL) | 692 | +2.715 [+1.195, +4.236] | 0.2208 | 3.50 | 4.6e-04*** | not applied (n < 1000) | 0.007 (q<0.05) | -12.9 | +18.0 | 0.0828 | 0.0692 |
| Avg. daily SD (mg/dL) | 692 | +2.624 [+1.069, +4.178] | 0.2443 | 3.31 | 9.4e-04*** | not applied (n < 1000) | 0.014 (q<0.05) | -12.1 | +18.8 | 0.0818 | 0.0692 |
| CV (%) | 692 | -0.100 [-1.482, +1.283] | -0.01816 | -0.14 | 0.888 | not applied (n < 1000) | 0.932 | +2.0 | +32.9 | 0.0670 | 0.0692 |
| Mean / SD ratio | 692 | -0.158 [-1.544, +1.227] | -0.1581 | -0.22 | 0.823 | not applied (n < 1000) | 0.885 | +1.9 | +32.8 | 0.0671 | 0.0692 |
| Avg. daily mean / SD | 692 | -0.183 [-1.548, +1.182] | -0.147 | -0.26 | 0.793 | not applied (n < 1000) | 0.867 | +1.9 | +32.8 | 0.0682 | 0.0692 |
| MAG (mg/dL/h) | 692 | +1.278 [-0.116, +2.672] | 0.1313 | 1.80 | 0.072 | not applied (n < 1000) | 0.216 | -1.5 | +29.4 | 0.0672 | 0.0692 |
| Avg. daily range (mg/dL) | 692 | +2.081 [+0.593, +3.570] | 0.05798 | 2.74 | 0.006** | not applied (n < 1000) | 0.050 | -7.0 | +23.9 | 0.0741 | 0.0692 |
| SD of daily means (mg/dL) | 692 | +2.409 [+1.053, +3.766] | 0.2912 | 3.48 | 5.0e-04*** | not applied (n < 1000) | 0.008 (q<0.05) | -10.1 | +20.8 | 0.0797 | 0.0692 |
| Time in range 70-180, pooled (%) | 692 | -3.815 [-5.284, -2.345] | -0.1502 | -5.09 | 3.6e-07*** | not applied (n < 1000) | 1.4e-05 (q<0.05) | -28.3 | +2.6 | 0.1039 | 0.0692 |
| Avg. daily time in range 70-180 (%) | 692 | -3.752 [-5.222, -2.282] | -0.1465 | -5.00 | 5.7e-07*** | not applied (n < 1000) | 1.7e-05 (q<0.05) | -27.2 | +3.6 | 0.1023 | 0.0692 |
| Any reading < 54 during wear (0/1) | 692 | -0.590 [-1.913, +0.734] | -1.383 | -0.87 | 0.382 | not applied (n < 1000) | 0.669 | +1.2 | +32.1 | 0.0680 | 0.0692 |
| Time < 54, pooled (%) | 692 | -0.310 [-1.868, +1.248] | -0.5112 | -0.39 | 0.697 | not applied (n < 1000) | 0.805 | +1.8 | +32.7 | 0.0677 | 0.0692 |
| Avg. daily time < 54 (%) | 692 | -0.527 [-1.594, +0.541] | -0.9999 | -0.97 | 0.334 | not applied (n < 1000) | 0.623 | +1.4 | +32.3 | 0.0677 | 0.0692 |
| Time 54-69, pooled (%) | 692 | -0.420 [-2.687, +1.847] | -0.4015 | -0.36 | 0.716 | not applied (n < 1000) | 0.821 | +1.6 | +32.5 | 0.0643 | 0.0692 |
| Avg. daily time 54-69 (%) | 692 | -0.481 [-2.730, +1.767] | -0.4269 | -0.42 | 0.675 | not applied (n < 1000) | 0.792 | +1.5 | +32.4 | 0.0639 | 0.0692 |
| Time < 70, pooled (%) | 692 | -0.442 [-2.302, +1.417] | -0.3089 | -0.47 | 0.641 | not applied (n < 1000) | 0.771 | +1.6 | +32.5 | 0.0655 | 0.0692 |
| Avg. daily time < 70 (%) | 692 | -0.549 [-2.512, +1.414] | -0.3651 | -0.55 | 0.583 | not applied (n < 1000) | 0.749 | +1.3 | +32.2 | 0.0647 | 0.0692 |
| Time 54-250, pooled (%) | 692 | -2.457 [-4.068, -0.845] | -0.1454 | -2.99 | 0.003** | not applied (n < 1000) | 0.031 (q<0.05) | -10.8 | +20.1 | 0.0806 | 0.0692 |
| Avg. daily time 54-250 (%) | 692 | -2.468 [-4.097, -0.840] | -0.1483 | -2.97 | 0.003** | not applied (n < 1000) | 0.032 (q<0.05) | -11.0 | +19.9 | 0.0804 | 0.0692 |
| Time 181-250, pooled (%) | 692 | +3.537 [+2.146, +4.927] | 0.2381 | 4.98 | 6.2e-07*** | not applied (n < 1000) | 1.7e-05 (q<0.05) | -24.9 | +5.9 | 0.1014 | 0.0692 |
| Avg. daily time 181-250 (%) | 692 | +3.441 [+2.050, +4.831] | 0.2269 | 4.85 | 1.2e-06*** | not applied (n < 1000) | 3.2e-05 (q<0.05) | -23.4 | +7.5 | 0.0993 | 0.0692 |
| Time > 180, pooled (%) | 692 | +3.805 [+2.335, +5.274] | 0.1488 | 5.08 | 3.9e-07*** | not applied (n < 1000) | 1.4e-05 (q<0.05) | -28.2 | +2.7 | 0.1040 | 0.0692 |
| Avg. daily time > 180 (%) | 692 | +3.754 [+2.285, +5.224] | 0.1458 | 5.01 | 5.5e-07*** | not applied (n < 1000) | 1.7e-05 (q<0.05) | -27.4 | +3.5 | 0.1027 | 0.0692 |
| Nocturnal time > 180 (%) | 692 | +2.958 [+1.484, +4.431] | 0.1046 | 3.93 | 8.3e-05*** | not applied (n < 1000) | 0.001 (q<0.05) | -15.7 | +15.1 | 0.0875 | 0.0692 |
| Time > 250, pooled (%) | 692 | +2.468 [+0.857, +4.079] | 0.1461 | 3.00 | 0.003** | not applied (n < 1000) | 0.031 (q<0.05) | -10.9 | +19.9 | 0.0808 | 0.0692 |
| Avg. daily time > 250 (%) | 692 | +2.485 [+0.856, +4.115] | 0.1494 | 2.99 | 0.003** | not applied (n < 1000) | 0.031 (q<0.05) | -11.1 | +19.7 | 0.0807 | 0.0692 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

### Population: Healthy group (no diabetes + pre-diabetes / lifestyle)

#### MoCA total score (0-30)
*n = 244; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 244 | -0.471 [-1.019, +0.077] | -0.5165 | -1.68 | 0.092 | not applied (n < 1000) | 0.503 | -2.9 | +0.0 | -0.0274 | -0.0383 |
| Mean glucose (mg/dL) | 244 | -0.676 [-1.214, -0.138] | -0.02296 | -2.46 | 0.014* | not applied (n < 1000) | 0.214 | -8.2 | -5.3 | -0.0028 | -0.0383 |
| GMI (%) | 244 | -0.676 [-1.214, -0.138] | -0.96 | -2.46 | 0.014* | not applied (n < 1000) | 0.214 | -8.2 | -5.3 | -0.0028 | -0.0383 |
| Nocturnal mean 00-06h (mg/dL) | 244 | -0.573 [-1.101, -0.045] | -0.01764 | -2.13 | 0.033* | not applied (n < 1000) | 0.351 | -5.3 | -2.4 | -0.0149 | -0.0383 |
| Glucose SD, pooled (mg/dL) | 244 | -0.295 [-0.781, +0.192] | -0.03848 | -1.19 | 0.235 | not applied (n < 1000) | 0.700 | +0.1 | +3.0 | -0.0439 | -0.0383 |
| Avg. daily SD (mg/dL) | 244 | -0.333 [-0.772, +0.105] | -0.04586 | -1.49 | 0.136 | not applied (n < 1000) | 0.595 | -0.4 | +2.5 | -0.0382 | -0.0383 |
| CV (%) | 244 | +0.262 [-0.159, +0.683] | 0.05312 | 1.22 | 0.222 | not applied (n < 1000) | 0.700 | +0.5 | +3.4 | -0.0400 | -0.0383 |
| Mean / SD ratio | 244 | -0.262 [-0.693, +0.168] | -0.2756 | -1.19 | 0.232 | not applied (n < 1000) | 0.700 | +0.5 | +3.4 | -0.0405 | -0.0383 |
| Avg. daily mean / SD | 244 | -0.174 [-0.633, +0.286] | -0.1402 | -0.74 | 0.459 | not applied (n < 1000) | 0.837 | +1.3 | +4.2 | -0.0443 | -0.0383 |
| MAG (mg/dL/h) | 244 | -0.023 [-0.479, +0.434] | -0.002465 | -0.10 | 0.923 | not applied (n < 1000) | 0.977 | +2.0 | +4.9 | -0.0596 | -0.0383 |
| Avg. daily range (mg/dL) | 244 | -0.138 [-0.581, +0.304] | -0.004994 | -0.61 | 0.539 | not applied (n < 1000) | 0.867 | +1.6 | +4.5 | -0.0513 | -0.0383 |
| SD of daily means (mg/dL) | 244 | +0.243 [-0.366, +0.852] | 0.05161 | 0.78 | 0.434 | not applied (n < 1000) | 0.837 | +0.6 | +3.5 | -0.0455 | -0.0383 |
| Time in range 70-180, pooled (%) | 244 | +0.587 [+0.067, +1.108] | 0.03567 | 2.21 | 0.027* | not applied (n < 1000) | 0.325 | -5.7 | -2.8 | -0.0110 | -0.0383 |
| Avg. daily time in range 70-180 (%) | 244 | +0.574 [+0.053, +1.095] | 0.03448 | 2.16 | 0.031* | not applied (n < 1000) | 0.348 | -5.4 | -2.5 | -0.0121 | -0.0383 |
| Any reading < 54 during wear (0/1) | 244 | +0.279 [-0.115, +0.673] | 0.6265 | 1.39 | 0.166 | not applied (n < 1000) | 0.638 | +0.2 | +3.1 | -0.0349 | -0.0383 |
| Time < 54, pooled (%) | 244 | +0.278 [-0.017, +0.573] | 0.2925 | 1.85 | 0.065 | not applied (n < 1000) | 0.457 | +0.2 | +3.1 | -0.0362 | -0.0383 |
| Avg. daily time < 54 (%) | 244 | +0.259 [+0.033, +0.485] | 0.3585 | 2.25 | 0.024* | not applied (n < 1000) | 0.312 | +0.5 | +3.4 | -0.0348 | -0.0383 |
| Time 54-69, pooled (%) | 244 | +0.151 [-0.566, +0.867] | 0.1167 | 0.41 | 0.680 | not applied (n < 1000) | 0.896 | +1.5 | +4.4 | -0.0513 | -0.0383 |
| Avg. daily time 54-69 (%) | 244 | +0.142 [-0.572, +0.856] | 0.1047 | 0.39 | 0.697 | not applied (n < 1000) | 0.906 | +1.6 | +4.4 | -0.0501 | -0.0383 |
| Time < 70, pooled (%) | 244 | +0.242 [-0.244, +0.728] | 0.126 | 0.98 | 0.329 | not applied (n < 1000) | 0.794 | +0.7 | +3.6 | -0.0410 | -0.0383 |
| Avg. daily time < 70 (%) | 244 | +0.205 [-0.346, +0.756] | 0.1092 | 0.73 | 0.466 | not applied (n < 1000) | 0.837 | +1.1 | +4.0 | -0.0445 | -0.0383 |
| Time 54-250, pooled (%) | 244 | +0.558 [-0.109, +1.225] | 0.05146 | 1.64 | 0.101 | not applied (n < 1000) | 0.517 | -5.1 | -2.2 | -0.0324 | -0.0383 |
| Avg. daily time 54-250 (%) | 244 | +0.569 [-0.110, +1.249] | 0.05352 | 1.64 | 0.100 | not applied (n < 1000) | 0.517 | -5.3 | -2.4 | -0.0323 | -0.0383 |
| Time 181-250, pooled (%) | 244 | -0.381 [-0.783, +0.022] | -0.03754 | -1.85 | 0.064 | not applied (n < 1000) | 0.457 | -1.1 | +1.8 | -0.0250 | -0.0383 |
| Avg. daily time 181-250 (%) | 244 | -0.359 [-0.761, +0.043] | -0.03453 | -1.75 | 0.080 | not applied (n < 1000) | 0.466 | -0.8 | +2.1 | -0.0270 | -0.0383 |
| Time > 180, pooled (%) | 244 | -0.613 [-1.135, -0.091] | -0.03693 | -2.30 | 0.021* | not applied (n < 1000) | 0.295 | -6.4 | -3.5 | -0.0088 | -0.0383 |
| Avg. daily time > 180 (%) | 244 | -0.595 [-1.117, -0.072] | -0.03548 | -2.23 | 0.026* | not applied (n < 1000) | 0.316 | -5.9 | -3.0 | -0.0107 | -0.0383 |
| Nocturnal time > 180 (%) | 244 | -0.514 [-1.039, +0.011] | -0.02966 | -1.92 | 0.055 | not applied (n < 1000) | 0.434 | -4.0 | -1.1 | -0.0190 | -0.0383 |
| Time > 250, pooled (%) | 244 | -0.585 [-1.260, +0.091] | -0.05403 | -1.70 | 0.090 | not applied (n < 1000) | 0.502 | -5.8 | -2.9 | -0.0325 | -0.0383 |
| Avg. daily time > 250 (%) | 244 | -0.588 [-1.272, +0.095] | -0.05532 | -1.69 | 0.092 | not applied (n < 1000) | 0.503 | -5.8 | -2.9 | -0.0325 | -0.0383 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 244; events = 91; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 244 | OR 1.053 [0.783, 1.416] | 0.05655 | 0.34 | 0.733 | not applied (n < 1000) | 0.919 | +1.9 | +0.0 | 0.6052 | 0.6156 |
| Mean glucose (mg/dL) | 244 | OR 1.197 [0.883, 1.621] | 0.006095 | 1.16 | 0.246 | not applied (n < 1000) | 0.714 | +0.6 | -1.3 | 0.6013 | 0.6156 |
| GMI (%) | 244 | OR 1.197 [0.883, 1.621] | 0.2548 | 1.16 | 0.246 | not applied (n < 1000) | 0.714 | +0.6 | -1.3 | 0.6013 | 0.6156 |
| Nocturnal mean 00-06h (mg/dL) | 244 | OR 1.082 [0.805, 1.453] | 0.002412 | 0.52 | 0.603 | not applied (n < 1000) | 0.873 | +1.7 | -0.2 | 0.6066 | 0.6156 |
| Glucose SD, pooled (mg/dL) | 244 | OR 1.102 [0.823, 1.475] | 0.01266 | 0.65 | 0.515 | not applied (n < 1000) | 0.855 | +1.6 | -0.3 | 0.6032 | 0.6156 |
| Avg. daily SD (mg/dL) | 244 | OR 1.162 [0.867, 1.559] | 0.02071 | 1.01 | 0.315 | not applied (n < 1000) | 0.782 | +1.0 | -0.9 | 0.6056 | 0.6156 |
| CV (%) | 244 | OR 0.958 [0.718, 1.279] | -0.008584 | -0.29 | 0.773 | not applied (n < 1000) | 0.927 | +1.9 | +0.0 | 0.6069 | 0.6156 |
| Mean / SD ratio | 244 | OR 1.082 [0.816, 1.436] | 0.08303 | 0.55 | 0.584 | not applied (n < 1000) | 0.868 | +1.7 | -0.2 | 0.6077 | 0.6156 |
| Avg. daily mean / SD | 244 | OR 1.015 [0.764, 1.347] | 0.01177 | 0.10 | 0.920 | not applied (n < 1000) | 0.977 | +2.0 | +0.1 | 0.6062 | 0.6156 |
| MAG (mg/dL/h) | 244 | OR 0.986 [0.731, 1.330] | -0.001556 | -0.09 | 0.926 | not applied (n < 1000) | 0.977 | +2.0 | +0.1 | 0.5985 | 0.6156 |
| Avg. daily range (mg/dL) | 244 | OR 1.068 [0.799, 1.427] | 0.002375 | 0.45 | 0.656 | not applied (n < 1000) | 0.886 | +1.8 | -0.1 | 0.6077 | 0.6156 |
| SD of daily means (mg/dL) | 244 | OR 0.747 [0.552, 1.010] | -0.06196 | -1.89 | 0.058 | not applied (n < 1000) | 0.449 | -1.8 | -3.7 | 0.6264 | 0.6156 |
| Time in range 70-180, pooled (%) | 244 | OR 0.870 [0.652, 1.162] | -0.00846 | -0.94 | 0.345 | not applied (n < 1000) | 0.796 | +1.1 | -0.8 | 0.5989 | 0.6156 |
| Avg. daily time in range 70-180 (%) | 244 | OR 0.877 [0.657, 1.171] | -0.007858 | -0.89 | 0.375 | not applied (n < 1000) | 0.820 | +1.2 | -0.7 | 0.5985 | 0.6156 |
| Any reading < 54 during wear (0/1) | 244 | OR 0.744 [0.555, 0.997] | -0.6651 | -1.98 | 0.048* | not applied (n < 1000) | 0.417 | -2.1 | -4.0 | 0.6275 | 0.6156 |
| Time < 54, pooled (%) | 244 | OR 0.761 [0.424, 1.366] | -0.2875 | -0.92 | 0.360 | not applied (n < 1000) | 0.809 | +0.0 | -1.9 | 0.6199 | 0.6156 |
| Avg. daily time < 54 (%) | 244 | OR 0.874 [0.638, 1.197] | -0.187 | -0.84 | 0.400 | not applied (n < 1000) | 0.835 | +1.1 | -0.7 | 0.6123 | 0.6156 |
| Time 54-69, pooled (%) | 244 | OR 1.012 [0.764, 1.339] | 0.008937 | 0.08 | 0.936 | not applied (n < 1000) | 0.977 | +2.0 | +0.1 | 0.6020 | 0.6156 |
| Avg. daily time 54-69 (%) | 244 | OR 1.027 [0.780, 1.352] | 0.01966 | 0.19 | 0.849 | not applied (n < 1000) | 0.959 | +2.0 | +0.1 | 0.6016 | 0.6156 |
| Time < 70, pooled (%) | 244 | OR 0.909 [0.672, 1.230] | -0.04973 | -0.62 | 0.536 | not applied (n < 1000) | 0.866 | +1.6 | -0.3 | 0.6063 | 0.6156 |
| Avg. daily time < 70 (%) | 244 | OR 0.966 [0.723, 1.290] | -0.01861 | -0.24 | 0.813 | not applied (n < 1000) | 0.941 | +1.9 | +0.1 | 0.6076 | 0.6156 |
| Time 54-250, pooled (%) | 244 | OR 0.952 [0.709, 1.277] | -0.004572 | -0.33 | 0.741 | not applied (n < 1000) | 0.921 | +1.9 | +0.0 | 0.6021 | 0.6156 |
| Avg. daily time 54-250 (%) | 244 | OR 0.949 [0.707, 1.275] | -0.004911 | -0.35 | 0.729 | not applied (n < 1000) | 0.919 | +1.9 | -0.0 | 0.6025 | 0.6156 |
| Time 181-250, pooled (%) | 244 | OR 1.187 [0.892, 1.579] | 0.01688 | 1.17 | 0.240 | not applied (n < 1000) | 0.705 | +0.6 | -1.2 | 0.6071 | 0.6156 |
| Avg. daily time 181-250 (%) | 244 | OR 1.164 [0.875, 1.547] | 0.01457 | 1.04 | 0.297 | not applied (n < 1000) | 0.770 | +0.9 | -1.0 | 0.6069 | 0.6156 |
| Time > 180, pooled (%) | 244 | OR 1.162 [0.870, 1.553] | 0.009039 | 1.01 | 0.310 | not applied (n < 1000) | 0.782 | +1.0 | -0.9 | 0.5997 | 0.6156 |
| Avg. daily time > 180 (%) | 244 | OR 1.144 [0.856, 1.528] | 0.008021 | 0.91 | 0.363 | not applied (n < 1000) | 0.810 | +1.2 | -0.7 | 0.5990 | 0.6156 |
| Nocturnal time > 180 (%) | 244 | OR 0.994 [0.740, 1.334] | -0.0003621 | -0.04 | 0.967 | not applied (n < 1000) | 0.983 | +2.0 | +0.1 | 0.6011 | 0.6156 |
| Time > 250, pooled (%) | 244 | OR 1.072 [0.796, 1.442] | 0.006399 | 0.46 | 0.648 | not applied (n < 1000) | 0.880 | +1.8 | -0.1 | 0.6033 | 0.6156 |
| Avg. daily time > 250 (%) | 244 | OR 1.065 [0.792, 1.433] | 0.005914 | 0.42 | 0.678 | not applied (n < 1000) | 0.896 | +1.8 | -0.1 | 0.6035 | 0.6156 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 244; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 244 | -0.373 [-0.692, -0.053] | -0.4089 | -2.28 | 0.022* | not applied (n < 1000) | 0.295 | -2.3 | +0.0 | -0.0170 | -0.0389 |
| Mean glucose (mg/dL) | 244 | -0.510 [-0.791, -0.228] | -0.01732 | -3.55 | 3.9e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -6.1 | -3.8 | -0.0022 | -0.0389 |
| GMI (%) | 244 | -0.510 [-0.791, -0.228] | -0.7239 | -3.55 | 3.9e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -6.1 | -3.8 | -0.0022 | -0.0389 |
| Nocturnal mean 00-06h (mg/dL) | 244 | -0.498 [-0.789, -0.207] | -0.01533 | -3.35 | 8.0e-04*** | not applied (n < 1000) | 0.038 (q<0.05) | -5.8 | -3.5 | -0.0050 | -0.0389 |
| Glucose SD, pooled (mg/dL) | 244 | -0.220 [-0.571, +0.131] | -0.02871 | -1.23 | 0.220 | not applied (n < 1000) | 0.700 | +0.5 | +2.9 | -0.0434 | -0.0389 |
| Avg. daily SD (mg/dL) | 244 | -0.255 [-0.619, +0.110] | -0.03505 | -1.37 | 0.171 | not applied (n < 1000) | 0.641 | +0.1 | +2.4 | -0.0413 | -0.0389 |
| CV (%) | 244 | +0.175 [-0.168, +0.518] | 0.03546 | 1.00 | 0.317 | not applied (n < 1000) | 0.782 | +1.1 | +3.4 | -0.0460 | -0.0389 |
| Mean / SD ratio | 244 | -0.237 [-0.595, +0.121] | -0.2491 | -1.30 | 0.194 | not applied (n < 1000) | 0.674 | +0.2 | +2.5 | -0.0416 | -0.0389 |
| Avg. daily mean / SD | 244 | -0.137 [-0.504, +0.230] | -0.1107 | -0.73 | 0.464 | not applied (n < 1000) | 0.837 | +1.4 | +3.7 | -0.0451 | -0.0389 |
| MAG (mg/dL/h) | 244 | -0.218 [-0.645, +0.208] | -0.02383 | -1.00 | 0.316 | not applied (n < 1000) | 0.782 | +0.6 | +2.9 | -0.0508 | -0.0389 |
| Avg. daily range (mg/dL) | 244 | -0.138 [-0.537, +0.261] | -0.004975 | -0.68 | 0.498 | not applied (n < 1000) | 0.852 | +1.4 | +3.7 | -0.0523 | -0.0389 |
| SD of daily means (mg/dL) | 244 | +0.051 [-0.300, +0.402] | 0.01077 | 0.28 | 0.777 | not applied (n < 1000) | 0.927 | +1.9 | +4.2 | -0.0459 | -0.0389 |
| Time in range 70-180, pooled (%) | 244 | +0.441 [+0.150, +0.732] | 0.02678 | 2.97 | 0.003** | not applied (n < 1000) | 0.090 | -4.1 | -1.8 | -0.0120 | -0.0389 |
| Avg. daily time in range 70-180 (%) | 244 | +0.438 [+0.145, +0.731] | 0.02629 | 2.93 | 0.003** | not applied (n < 1000) | 0.095 | -4.0 | -1.7 | -0.0129 | -0.0389 |
| Any reading < 54 during wear (0/1) | 244 | +0.239 [-0.100, +0.577] | 0.5359 | 1.38 | 0.168 | not applied (n < 1000) | 0.640 | +0.1 | +2.5 | -0.0384 | -0.0389 |
| Time < 54, pooled (%) | 244 | +0.066 [-0.577, +0.708] | 0.06907 | 0.20 | 0.841 | not applied (n < 1000) | 0.956 | +1.9 | +4.2 | -0.0599 | -0.0389 |
| Avg. daily time < 54 (%) | 244 | +0.058 [-0.203, +0.319] | 0.08008 | 0.43 | 0.664 | not applied (n < 1000) | 0.890 | +1.9 | +4.2 | -0.0426 | -0.0389 |
| Time 54-69, pooled (%) | 244 | +0.153 [-0.027, +0.334] | 0.1188 | 1.66 | 0.097 | not applied (n < 1000) | 0.512 | +1.3 | +3.6 | -0.0388 | -0.0389 |
| Avg. daily time 54-69 (%) | 244 | +0.131 [-0.028, +0.291] | 0.09667 | 1.61 | 0.107 | not applied (n < 1000) | 0.521 | +1.5 | +3.8 | -0.0394 | -0.0389 |
| Time < 70, pooled (%) | 244 | +0.136 [-0.054, +0.326] | 0.07095 | 1.41 | 0.159 | not applied (n < 1000) | 0.635 | +1.4 | +3.7 | -0.0408 | -0.0389 |
| Avg. daily time < 70 (%) | 244 | +0.118 [-0.053, +0.288] | 0.06273 | 1.35 | 0.176 | not applied (n < 1000) | 0.642 | +1.6 | +3.9 | -0.0405 | -0.0389 |
| Time 54-250, pooled (%) | 244 | +0.442 [+0.192, +0.692] | 0.04073 | 3.46 | 5.4e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -4.2 | -1.9 | -0.0148 | -0.0389 |
| Avg. daily time 54-250 (%) | 244 | +0.446 [+0.196, +0.695] | 0.04187 | 3.50 | 4.7e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -4.3 | -2.0 | -0.0149 | -0.0389 |
| Time 181-250, pooled (%) | 244 | -0.266 [-0.580, +0.049] | -0.02621 | -1.66 | 0.098 | not applied (n < 1000) | 0.512 | -0.1 | +2.2 | -0.0338 | -0.0389 |
| Avg. daily time 181-250 (%) | 244 | -0.265 [-0.579, +0.048] | -0.02548 | -1.66 | 0.097 | not applied (n < 1000) | 0.512 | -0.1 | +2.2 | -0.0340 | -0.0389 |
| Time > 180, pooled (%) | 244 | -0.455 [-0.746, -0.164] | -0.02741 | -3.07 | 0.002** | not applied (n < 1000) | 0.076 | -4.5 | -2.2 | -0.0110 | -0.0389 |
| Avg. daily time > 180 (%) | 244 | -0.449 [-0.742, -0.157] | -0.0268 | -3.01 | 0.003** | not applied (n < 1000) | 0.085 | -4.3 | -2.0 | -0.0123 | -0.0389 |
| Nocturnal time > 180 (%) | 244 | -0.399 [-0.687, -0.110] | -0.023 | -2.71 | 0.007** | not applied (n < 1000) | 0.168 | -3.0 | -0.7 | -0.0186 | -0.0389 |
| Time > 250, pooled (%) | 244 | -0.449 [-0.702, -0.196] | -0.04149 | -3.48 | 4.9e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -4.4 | -2.1 | -0.0151 | -0.0389 |
| Avg. daily time > 250 (%) | 244 | -0.450 [-0.701, -0.199] | -0.04234 | -3.51 | 4.4e-04*** | not applied (n < 1000) | 0.032 (q<0.05) | -4.4 | -2.1 | -0.0152 | -0.0389 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 243; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 243 | -0.184 [-0.844, +0.476] | -0.2016 | -0.55 | 0.585 | not applied (n < 1000) | 0.868 | +1.6 | +0.0 | 0.0551 | 0.0629 |
| Mean glucose (mg/dL) | 243 | -0.062 [-0.790, +0.667] | -0.002098 | -0.17 | 0.868 | not applied (n < 1000) | 0.971 | +2.0 | +0.3 | 0.0524 | 0.0629 |
| GMI (%) | 243 | -0.062 [-0.790, +0.667] | -0.08772 | -0.17 | 0.868 | not applied (n < 1000) | 0.971 | +2.0 | +0.3 | 0.0524 | 0.0629 |
| Nocturnal mean 00-06h (mg/dL) | 243 | +0.054 [-0.713, +0.821] | 0.001657 | 0.14 | 0.891 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | 0.0506 | 0.0629 |
| Glucose SD, pooled (mg/dL) | 243 | -0.397 [-1.023, +0.228] | -0.05205 | -1.25 | 0.213 | not applied (n < 1000) | 0.698 | +0.3 | -1.3 | 0.0646 | 0.0629 |
| Avg. daily SD (mg/dL) | 243 | -0.455 [-1.104, +0.193] | -0.06295 | -1.38 | 0.169 | not applied (n < 1000) | 0.640 | -0.2 | -1.8 | 0.0674 | 0.0629 |
| CV (%) | 243 | -0.446 [-0.985, +0.093] | -0.09013 | -1.62 | 0.105 | not applied (n < 1000) | 0.519 | -0.2 | -1.8 | 0.0681 | 0.0629 |
| Mean / SD ratio | 243 | +0.401 [-0.159, +0.962] | 0.4205 | 1.40 | 0.161 | not applied (n < 1000) | 0.635 | +0.2 | -1.4 | 0.0653 | 0.0629 |
| Avg. daily mean / SD | 243 | +0.498 [-0.111, +1.108] | 0.4021 | 1.60 | 0.109 | not applied (n < 1000) | 0.527 | -0.8 | -2.4 | 0.0683 | 0.0629 |
| MAG (mg/dL/h) | 243 | -0.338 [-1.038, +0.362] | -0.03677 | -0.95 | 0.344 | not applied (n < 1000) | 0.796 | +0.8 | -0.8 | 0.0586 | 0.0629 |
| Avg. daily range (mg/dL) | 243 | -0.443 [-1.098, +0.213] | -0.01603 | -1.32 | 0.185 | not applied (n < 1000) | 0.672 | -0.1 | -1.8 | 0.0664 | 0.0629 |
| SD of daily means (mg/dL) | 243 | +0.015 [-0.523, +0.552] | 0.00309 | 0.05 | 0.958 | not applied (n < 1000) | 0.983 | +2.0 | +0.4 | 0.0550 | 0.0629 |
| Time in range 70-180, pooled (%) | 243 | +0.093 [-0.799, +0.985] | 0.005681 | 0.20 | 0.838 | not applied (n < 1000) | 0.956 | +1.9 | +0.3 | 0.0420 | 0.0629 |
| Avg. daily time in range 70-180 (%) | 243 | +0.073 [-0.815, +0.961] | 0.004432 | 0.16 | 0.871 | not applied (n < 1000) | 0.971 | +1.9 | +0.3 | 0.0424 | 0.0629 |
| Any reading < 54 during wear (0/1) | 243 | +0.133 [-0.509, +0.774] | 0.2978 | 0.41 | 0.685 | not applied (n < 1000) | 0.899 | +1.8 | +0.2 | 0.0456 | 0.0629 |
| Time < 54, pooled (%) | 243 | -0.059 [-0.994, +0.876] | -0.06178 | -0.12 | 0.902 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | 0.0448 | 0.0629 |
| Avg. daily time < 54 (%) | 243 | -0.103 [-0.805, +0.599] | -0.1423 | -0.29 | 0.774 | not applied (n < 1000) | 0.927 | +1.9 | +0.3 | 0.0535 | 0.0629 |
| Time 54-69, pooled (%) | 243 | -0.322 [-0.925, +0.281] | -0.249 | -1.05 | 0.295 | not applied (n < 1000) | 0.770 | +0.8 | -0.8 | 0.0601 | 0.0629 |
| Avg. daily time 54-69 (%) | 243 | -0.310 [-0.891, +0.272] | -0.2279 | -1.04 | 0.296 | not applied (n < 1000) | 0.770 | +0.9 | -0.7 | 0.0601 | 0.0629 |
| Time < 70, pooled (%) | 243 | -0.246 [-0.601, +0.109] | -0.1279 | -1.36 | 0.174 | not applied (n < 1000) | 0.642 | +1.3 | -0.3 | 0.0632 | 0.0629 |
| Avg. daily time < 70 (%) | 243 | -0.265 [-0.596, +0.066] | -0.1408 | -1.57 | 0.117 | not applied (n < 1000) | 0.559 | +1.2 | -0.4 | 0.0639 | 0.0629 |
| Time 54-250, pooled (%) | 243 | +0.497 [-0.037, +1.032] | 0.04583 | 1.82 | 0.068 | not applied (n < 1000) | 0.457 | -0.8 | -2.4 | 0.0669 | 0.0629 |
| Avg. daily time 54-250 (%) | 243 | +0.503 [-0.048, +1.053] | 0.0472 | 1.79 | 0.074 | not applied (n < 1000) | 0.457 | -0.9 | -2.5 | 0.0674 | 0.0629 |
| Time 181-250, pooled (%) | 243 | +0.453 [-0.528, +1.434] | 0.04514 | 0.91 | 0.365 | not applied (n < 1000) | 0.812 | -0.2 | -1.8 | 0.0517 | 0.0629 |
| Avg. daily time 181-250 (%) | 243 | +0.465 [-0.512, +1.443] | 0.04514 | 0.93 | 0.351 | not applied (n < 1000) | 0.796 | -0.3 | -2.0 | 0.0522 | 0.0629 |
| Time > 180, pooled (%) | 243 | -0.064 [-0.961, +0.833] | -0.00386 | -0.14 | 0.889 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | 0.0418 | 0.0629 |
| Avg. daily time > 180 (%) | 243 | -0.043 [-0.937, +0.851] | -0.002592 | -0.09 | 0.925 | not applied (n < 1000) | 0.977 | +2.0 | +0.4 | 0.0423 | 0.0629 |
| Nocturnal time > 180 (%) | 243 | +0.125 [-0.849, +1.100] | 0.007215 | 0.25 | 0.801 | not applied (n < 1000) | 0.940 | +1.8 | +0.2 | 0.0382 | 0.0629 |
| Time > 250, pooled (%) | 243 | -0.494 [-1.031, +0.043] | -0.04559 | -1.80 | 0.072 | not applied (n < 1000) | 0.457 | -0.8 | -2.4 | 0.0671 | 0.0629 |
| Avg. daily time > 250 (%) | 243 | -0.496 [-1.049, +0.057] | -0.04666 | -1.76 | 0.079 | not applied (n < 1000) | 0.466 | -0.8 | -2.4 | 0.0673 | 0.0629 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 243; events = 47; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 243 | OR 1.045 [0.773, 1.412] | 0.04824 | 0.29 | 0.774 | not applied (n < 1000) | 0.927 | +1.9 | +0.0 | 0.6611 | 0.6660 |
| Mean glucose (mg/dL) | 243 | OR 1.118 [0.826, 1.512] | 0.003793 | 0.72 | 0.471 | not applied (n < 1000) | 0.837 | +1.5 | -0.4 | 0.6644 | 0.6660 |
| GMI (%) | 243 | OR 1.118 [0.826, 1.512] | 0.1586 | 0.72 | 0.471 | not applied (n < 1000) | 0.837 | +1.5 | -0.4 | 0.6644 | 0.6660 |
| Nocturnal mean 00-06h (mg/dL) | 243 | OR 1.205 [0.891, 1.629] | 0.005731 | 1.21 | 0.226 | not applied (n < 1000) | 0.700 | +0.6 | -1.4 | 0.6697 | 0.6660 |
| Glucose SD, pooled (mg/dL) | 243 | OR 0.819 [0.569, 1.179] | -0.02621 | -1.08 | 0.282 | not applied (n < 1000) | 0.758 | +0.8 | -1.1 | 0.6632 | 0.6660 |
| Avg. daily SD (mg/dL) | 243 | OR 0.751 [0.515, 1.095] | -0.03962 | -1.49 | 0.136 | not applied (n < 1000) | 0.595 | -0.3 | -2.3 | 0.6710 | 0.6660 |
| CV (%) | 243 | OR 0.636 [0.418, 0.969] | -0.09136 | -2.10 | 0.035* | not applied (n < 1000) | 0.351 | -3.0 | -4.9 | 0.6801 | 0.6660 |
| Mean / SD ratio | 243 | OR 1.500 [1.037, 2.170] | 0.4249 | 2.15 | 0.032* | not applied (n < 1000) | 0.348 | -2.7 | -4.6 | 0.6805 | 0.6660 |
| Avg. daily mean / SD | 243 | OR 1.606 [1.113, 2.316] | 0.3819 | 2.53 | 0.011* | not applied (n < 1000) | 0.206 | -4.5 | -6.5 | 0.6919 | 0.6660 |
| MAG (mg/dL/h) | 243 | OR 0.827 [0.570, 1.200] | -0.02066 | -1.00 | 0.318 | not applied (n < 1000) | 0.782 | +1.0 | -0.9 | 0.6643 | 0.6660 |
| Avg. daily range (mg/dL) | 243 | OR 0.733 [0.503, 1.067] | -0.01126 | -1.62 | 0.105 | not applied (n < 1000) | 0.519 | -0.8 | -2.7 | 0.6786 | 0.6660 |
| SD of daily means (mg/dL) | 243 | OR 1.118 [0.808, 1.545] | 0.02356 | 0.67 | 0.501 | not applied (n < 1000) | 0.852 | +1.6 | -0.4 | 0.6655 | 0.6660 |
| Time in range 70-180, pooled (%) | 243 | OR 0.985 [0.717, 1.353] | -0.0009309 | -0.09 | 0.925 | not applied (n < 1000) | 0.977 | +2.0 | +0.1 | 0.6619 | 0.6660 |
| Avg. daily time in range 70-180 (%) | 243 | OR 0.981 [0.715, 1.347] | -0.001155 | -0.12 | 0.906 | not applied (n < 1000) | 0.977 | +2.0 | +0.1 | 0.6608 | 0.6660 |
| Any reading < 54 during wear (0/1) | 243 | OR 1.228 [0.878, 1.719] | 0.4615 | 1.20 | 0.230 | not applied (n < 1000) | 0.700 | +0.6 | -1.3 | 0.6707 | 0.6660 |
| Time < 54, pooled (%) | 243 | OR 0.676 [0.198, 2.305] | -0.4103 | -0.62 | 0.532 | not applied (n < 1000) | 0.863 | +1.4 | -0.5 | 0.6677 | 0.6660 |
| Avg. daily time < 54 (%) | 243 | OR 0.378 [0.058, 2.439] | -1.345 | -1.02 | 0.306 | not applied (n < 1000) | 0.780 | -0.3 | -2.2 | 0.6789 | 0.6660 |
| Time 54-69, pooled (%) | 243 | OR 0.601 [0.272, 1.329] | -0.3932 | -1.26 | 0.209 | not applied (n < 1000) | 0.698 | -0.7 | -2.7 | 0.6703 | 0.6660 |
| Avg. daily time 54-69 (%) | 243 | OR 0.555 [0.221, 1.397] | -0.4327 | -1.25 | 0.211 | not applied (n < 1000) | 0.698 | -0.9 | -2.9 | 0.6685 | 0.6660 |
| Time < 70, pooled (%) | 243 | OR 0.619 [0.263, 1.459] | -0.249 | -1.10 | 0.273 | not applied (n < 1000) | 0.752 | -0.2 | -2.1 | 0.6707 | 0.6660 |
| Avg. daily time < 70 (%) | 243 | OR 0.508 [0.170, 1.523] | -0.3601 | -1.21 | 0.227 | not applied (n < 1000) | 0.700 | -1.0 | -2.9 | 0.6725 | 0.6660 |
| Time 54-250, pooled (%) | 243 | OR 1.059 [0.768, 1.458] | 0.005243 | 0.35 | 0.728 | not applied (n < 1000) | 0.919 | +1.9 | -0.0 | 0.6495 | 0.6660 |
| Avg. daily time 54-250 (%) | 243 | OR 1.056 [0.769, 1.449] | 0.00509 | 0.34 | 0.737 | not applied (n < 1000) | 0.919 | +1.9 | -0.0 | 0.6486 | 0.6660 |
| Time 181-250, pooled (%) | 243 | OR 1.160 [0.816, 1.649] | 0.01482 | 0.83 | 0.407 | not applied (n < 1000) | 0.837 | +1.3 | -0.6 | 0.6609 | 0.6660 |
| Avg. daily time 181-250 (%) | 243 | OR 1.162 [0.818, 1.652] | 0.01459 | 0.84 | 0.402 | not applied (n < 1000) | 0.835 | +1.3 | -0.6 | 0.6598 | 0.6660 |
| Time > 180, pooled (%) | 243 | OR 1.035 [0.756, 1.418] | 0.0021 | 0.22 | 0.829 | not applied (n < 1000) | 0.951 | +2.0 | +0.0 | 0.6614 | 0.6660 |
| Avg. daily time > 180 (%) | 243 | OR 1.041 [0.761, 1.425] | 0.002428 | 0.25 | 0.801 | not applied (n < 1000) | 0.940 | +1.9 | +0.0 | 0.6609 | 0.6660 |
| Nocturnal time > 180 (%) | 243 | OR 1.155 [0.855, 1.559] | 0.008284 | 0.94 | 0.348 | not applied (n < 1000) | 0.796 | +1.1 | -0.8 | 0.6690 | 0.6660 |
| Time > 250, pooled (%) | 243 | OR 0.949 [0.691, 1.304] | -0.004797 | -0.32 | 0.748 | not applied (n < 1000) | 0.922 | +1.9 | -0.0 | 0.6503 | 0.6660 |
| Avg. daily time > 250 (%) | 243 | OR 0.954 [0.698, 1.305] | -0.004418 | -0.29 | 0.769 | not applied (n < 1000) | 0.927 | +1.9 | -0.0 | 0.6503 | 0.6660 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 241; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 241 | -0.032 [-0.115, +0.052] | -0.03473 | -0.75 | 0.455 | not applied (n < 1000) | 0.837 | +1.7 | +0.0 | 0.0102 | 0.0104 |
| Mean glucose (mg/dL) | 241 | -0.046 [-0.136, +0.045] | -0.001549 | -0.99 | 0.320 | not applied (n < 1000) | 0.782 | +1.3 | -0.4 | 0.0113 | 0.0104 |
| GMI (%) | 241 | -0.046 [-0.136, +0.045] | -0.06477 | -0.99 | 0.320 | not applied (n < 1000) | 0.782 | +1.3 | -0.4 | 0.0113 | 0.0104 |
| Nocturnal mean 00-06h (mg/dL) | 241 | -0.052 [-0.143, +0.039] | -0.001587 | -1.12 | 0.264 | not applied (n < 1000) | 0.740 | +1.1 | -0.5 | 0.0116 | 0.0104 |
| Glucose SD, pooled (mg/dL) | 241 | -0.026 [-0.135, +0.083] | -0.003405 | -0.47 | 0.638 | not applied (n < 1000) | 0.873 | +1.8 | +0.1 | 0.0041 | 0.0104 |
| Avg. daily SD (mg/dL) | 241 | +0.005 [-0.112, +0.121] | 0.0006251 | 0.08 | 0.939 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | -0.0002 | 0.0104 |
| CV (%) | 241 | +0.020 [-0.099, +0.138] | 0.003939 | 0.32 | 0.747 | not applied (n < 1000) | 0.922 | +1.9 | +0.2 | 0.0035 | 0.0104 |
| Mean / SD ratio | 241 | -0.030 [-0.148, +0.087] | -0.03189 | -0.51 | 0.611 | not applied (n < 1000) | 0.873 | +1.7 | +0.0 | 0.0056 | 0.0104 |
| Avg. daily mean / SD | 241 | -0.073 [-0.191, +0.045] | -0.05875 | -1.21 | 0.225 | not applied (n < 1000) | 0.700 | +0.2 | -1.5 | 0.0098 | 0.0104 |
| MAG (mg/dL/h) | 241 | +0.097 [-0.011, +0.205] | 0.01051 | 1.75 | 0.079 | not applied (n < 1000) | 0.466 | -0.9 | -2.5 | 0.0194 | 0.0104 |
| Avg. daily range (mg/dL) | 241 | +0.027 [-0.098, +0.152] | 0.0009776 | 0.43 | 0.670 | not applied (n < 1000) | 0.890 | +1.8 | +0.1 | -0.0015 | 0.0104 |
| SD of daily means (mg/dL) | 241 | -0.070 [-0.172, +0.031] | -0.01489 | -1.36 | 0.173 | not applied (n < 1000) | 0.642 | +0.2 | -1.4 | 0.0145 | 0.0104 |
| Time in range 70-180, pooled (%) | 241 | +0.038 [-0.066, +0.143] | 0.002323 | 0.72 | 0.471 | not applied (n < 1000) | 0.837 | +1.5 | -0.2 | 0.0072 | 0.0104 |
| Avg. daily time in range 70-180 (%) | 241 | +0.035 [-0.069, +0.138] | 0.002067 | 0.65 | 0.513 | not applied (n < 1000) | 0.855 | +1.6 | -0.1 | 0.0069 | 0.0104 |
| Any reading < 54 during wear (0/1) | 241 | -0.024 [-0.143, +0.095] | -0.05426 | -0.40 | 0.692 | not applied (n < 1000) | 0.902 | +1.8 | +0.1 | -0.0125 | 0.0104 |
| Time < 54, pooled (%) | 241 | -0.010 [-0.155, +0.135] | -0.0103 | -0.13 | 0.894 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | -0.0081 | 0.0104 |
| Avg. daily time < 54 (%) | 241 | -0.006 [-0.087, +0.075] | -0.008552 | -0.15 | 0.880 | not applied (n < 1000) | 0.977 | +2.0 | +0.3 | 0.0053 | 0.0104 |
| Time 54-69, pooled (%) | 241 | -0.031 [-0.282, +0.220] | -0.02404 | -0.24 | 0.807 | not applied (n < 1000) | 0.940 | +1.7 | +0.0 | -0.0242 | 0.0104 |
| Avg. daily time 54-69 (%) | 241 | -0.027 [-0.297, +0.243] | -0.01983 | -0.20 | 0.844 | not applied (n < 1000) | 0.956 | +1.8 | +0.1 | -0.0230 | 0.0104 |
| Time < 70, pooled (%) | 241 | -0.026 [-0.178, +0.125] | -0.01347 | -0.34 | 0.736 | not applied (n < 1000) | 0.919 | +1.8 | +0.1 | -0.0025 | 0.0104 |
| Avg. daily time < 70 (%) | 241 | -0.022 [-0.208, +0.164] | -0.01171 | -0.23 | 0.816 | not applied (n < 1000) | 0.942 | +1.8 | +0.2 | -0.0047 | 0.0104 |
| Time 54-250, pooled (%) | 241 | +0.021 [-0.049, +0.092] | 0.00195 | 0.59 | 0.554 | not applied (n < 1000) | 0.868 | +1.8 | +0.2 | 0.0106 | 0.0104 |
| Avg. daily time 54-250 (%) | 241 | +0.020 [-0.050, +0.090] | 0.001878 | 0.56 | 0.574 | not applied (n < 1000) | 0.868 | +1.9 | +0.2 | 0.0103 | 0.0104 |
| Time 181-250, pooled (%) | 241 | -0.036 [-0.181, +0.110] | -0.003523 | -0.48 | 0.629 | not applied (n < 1000) | 0.873 | +1.6 | -0.1 | -0.0015 | 0.0104 |
| Avg. daily time 181-250 (%) | 241 | -0.031 [-0.175, +0.112] | -0.002999 | -0.43 | 0.669 | not applied (n < 1000) | 0.890 | +1.7 | +0.0 | -0.0007 | 0.0104 |
| Time > 180, pooled (%) | 241 | -0.035 [-0.139, +0.069] | -0.002105 | -0.66 | 0.507 | not applied (n < 1000) | 0.855 | +1.6 | -0.1 | 0.0076 | 0.0104 |
| Avg. daily time > 180 (%) | 241 | -0.032 [-0.134, +0.071] | -0.001891 | -0.61 | 0.543 | not applied (n < 1000) | 0.868 | +1.7 | +0.0 | 0.0073 | 0.0104 |
| Nocturnal time > 180 (%) | 241 | -0.046 [-0.150, +0.058] | -0.00264 | -0.86 | 0.387 | not applied (n < 1000) | 0.826 | +1.3 | -0.4 | 0.0077 | 0.0104 |
| Time > 250, pooled (%) | 241 | -0.020 [-0.090, +0.050] | -0.00188 | -0.57 | 0.567 | not applied (n < 1000) | 0.868 | +1.9 | +0.2 | 0.0105 | 0.0104 |
| Avg. daily time > 250 (%) | 241 | -0.020 [-0.089, +0.050] | -0.001842 | -0.55 | 0.579 | not applied (n < 1000) | 0.868 | +1.9 | +0.2 | 0.0104 | 0.0104 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 241; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 241 | +0.152 [-0.139, +0.442] | 0.1655 | 1.02 | 0.306 | not applied (n < 1000) | 0.780 | +0.6 | +0.0 | 0.2389 | 0.2391 |
| Mean glucose (mg/dL) | 241 | +0.215 [-0.022, +0.452] | 0.00726 | 1.78 | 0.075 | not applied (n < 1000) | 0.457 | -0.9 | -1.4 | 0.2457 | 0.2391 |
| GMI (%) | 241 | +0.215 [-0.022, +0.452] | 0.3035 | 1.78 | 0.075 | not applied (n < 1000) | 0.457 | -0.9 | -1.4 | 0.2457 | 0.2391 |
| Nocturnal mean 00-06h (mg/dL) | 241 | +0.177 [-0.057, +0.411] | 0.005422 | 1.49 | 0.137 | not applied (n < 1000) | 0.595 | +0.1 | -0.5 | 0.2415 | 0.2391 |
| Glucose SD, pooled (mg/dL) | 241 | +0.340 [+0.083, +0.598] | 0.04436 | 2.59 | 0.010** | not applied (n < 1000) | 0.201 | -5.2 | -5.8 | 0.2626 | 0.2391 |
| Avg. daily SD (mg/dL) | 241 | +0.336 [+0.085, +0.588] | 0.04619 | 2.62 | 0.009** | not applied (n < 1000) | 0.201 | -5.0 | -5.6 | 0.2600 | 0.2391 |
| CV (%) | 241 | +0.222 [-0.034, +0.479] | 0.04485 | 1.70 | 0.089 | not applied (n < 1000) | 0.502 | -1.1 | -1.7 | 0.2445 | 0.2391 |
| Mean / SD ratio | 241 | -0.226 [-0.473, +0.020] | -0.2368 | -1.80 | 0.072 | not applied (n < 1000) | 0.457 | -1.3 | -1.9 | 0.2484 | 0.2391 |
| Avg. daily mean / SD | 241 | -0.240 [-0.483, +0.003] | -0.1932 | -1.94 | 0.052 | not applied (n < 1000) | 0.434 | -1.7 | -2.3 | 0.2475 | 0.2391 |
| MAG (mg/dL/h) | 241 | +0.229 [-0.047, +0.505] | 0.0249 | 1.63 | 0.104 | not applied (n < 1000) | 0.519 | -1.0 | -1.6 | 0.2427 | 0.2391 |
| Avg. daily range (mg/dL) | 241 | +0.349 [+0.109, +0.589] | 0.01255 | 2.85 | 0.004** | not applied (n < 1000) | 0.113 | -5.7 | -6.3 | 0.2587 | 0.2391 |
| SD of daily means (mg/dL) | 241 | +0.127 [-0.156, +0.409] | 0.02682 | 0.88 | 0.379 | not applied (n < 1000) | 0.820 | +0.9 | +0.4 | 0.2306 | 0.2391 |
| Time in range 70-180, pooled (%) | 241 | -0.317 [-0.566, -0.068] | -0.01916 | -2.49 | 0.013* | not applied (n < 1000) | 0.212 | -4.4 | -4.9 | 0.2558 | 0.2391 |
| Avg. daily time in range 70-180 (%) | 241 | -0.314 [-0.560, -0.068] | -0.01878 | -2.50 | 0.012* | not applied (n < 1000) | 0.212 | -4.2 | -4.8 | 0.2549 | 0.2391 |
| Any reading < 54 during wear (0/1) | 241 | +0.075 [-0.195, +0.345] | 0.1695 | 0.54 | 0.586 | not applied (n < 1000) | 0.868 | +1.6 | +1.1 | 0.2335 | 0.2391 |
| Time < 54, pooled (%) | 241 | +0.288 [-0.019, +0.594] | 0.3008 | 1.84 | 0.066 | not applied (n < 1000) | 0.457 | -3.5 | -4.1 | 0.2554 | 0.2391 |
| Avg. daily time < 54 (%) | 241 | +0.284 [+0.149, +0.420] | 0.3908 | 4.11 | 4.0e-05*** | not applied (n < 1000) | 0.017 (q<0.05) | -3.3 | -3.9 | 0.2567 | 0.2391 |
| Time 54-69, pooled (%) | 241 | +0.116 [-0.519, +0.750] | 0.08903 | 0.36 | 0.721 | not applied (n < 1000) | 0.918 | +1.1 | +0.6 | 0.2101 | 0.2391 |
| Avg. daily time 54-69 (%) | 241 | +0.113 [-0.533, +0.760] | 0.08314 | 0.34 | 0.731 | not applied (n < 1000) | 0.919 | +1.2 | +0.6 | 0.2096 | 0.2391 |
| Time < 70, pooled (%) | 241 | +0.224 [-0.239, +0.688] | 0.1161 | 0.95 | 0.343 | not applied (n < 1000) | 0.796 | -1.2 | -1.8 | 0.2298 | 0.2391 |
| Avg. daily time < 70 (%) | 241 | +0.195 [-0.339, +0.728] | 0.1031 | 0.72 | 0.475 | not applied (n < 1000) | 0.837 | -0.4 | -1.0 | 0.2237 | 0.2391 |
| Time 54-250, pooled (%) | 241 | -0.202 [-0.479, +0.074] | -0.01853 | -1.43 | 0.152 | not applied (n < 1000) | 0.629 | -0.6 | -1.2 | 0.2444 | 0.2391 |
| Avg. daily time 54-250 (%) | 241 | -0.196 [-0.468, +0.076] | -0.0183 | -1.41 | 0.158 | not applied (n < 1000) | 0.635 | -0.5 | -1.0 | 0.2439 | 0.2391 |
| Time 181-250, pooled (%) | 241 | +0.284 [+0.022, +0.546] | 0.02793 | 2.12 | 0.034* | not applied (n < 1000) | 0.351 | -3.0 | -3.5 | 0.2494 | 0.2391 |
| Avg. daily time 181-250 (%) | 241 | +0.288 [+0.027, +0.550] | 0.02761 | 2.16 | 0.031* | not applied (n < 1000) | 0.348 | -3.1 | -3.7 | 0.2491 | 0.2391 |
| Time > 180, pooled (%) | 241 | +0.288 [+0.045, +0.532] | 0.01729 | 2.32 | 0.020* | not applied (n < 1000) | 0.294 | -3.2 | -3.8 | 0.2532 | 0.2391 |
| Avg. daily time > 180 (%) | 241 | +0.290 [+0.048, +0.532] | 0.01722 | 2.35 | 0.019* | not applied (n < 1000) | 0.283 | -3.3 | -3.9 | 0.2527 | 0.2391 |
| Nocturnal time > 180 (%) | 241 | +0.216 [-0.027, +0.459] | 0.01239 | 1.74 | 0.082 | not applied (n < 1000) | 0.471 | -1.0 | -1.5 | 0.2422 | 0.2391 |
| Time > 250, pooled (%) | 241 | +0.177 [-0.090, +0.444] | 0.01626 | 1.30 | 0.193 | not applied (n < 1000) | 0.674 | -0.0 | -0.6 | 0.2432 | 0.2391 |
| Avg. daily time > 250 (%) | 241 | +0.177 [-0.088, +0.441] | 0.01651 | 1.31 | 0.191 | not applied (n < 1000) | 0.674 | -0.0 | -0.6 | 0.2431 | 0.2391 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 241; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 241 | +0.326 [-0.258, +0.910] | 0.3558 | 1.09 | 0.274 | not applied (n < 1000) | 0.752 | +1.3 | +0.0 | 0.0886 | 0.0973 |
| Mean glucose (mg/dL) | 241 | +0.280 [-0.429, +0.989] | 0.009467 | 0.77 | 0.439 | not applied (n < 1000) | 0.837 | +1.5 | +0.2 | 0.0834 | 0.0973 |
| GMI (%) | 241 | +0.280 [-0.429, +0.989] | 0.3958 | 0.77 | 0.439 | not applied (n < 1000) | 0.837 | +1.5 | +0.2 | 0.0834 | 0.0973 |
| Nocturnal mean 00-06h (mg/dL) | 241 | +0.323 [-0.379, +1.025] | 0.009887 | 0.90 | 0.367 | not applied (n < 1000) | 0.812 | +1.3 | +0.0 | 0.0870 | 0.0973 |
| Glucose SD, pooled (mg/dL) | 241 | -0.264 [-1.084, +0.555] | -0.03446 | -0.63 | 0.527 | not applied (n < 1000) | 0.858 | +1.6 | +0.2 | 0.0806 | 0.0973 |
| Avg. daily SD (mg/dL) | 241 | -0.063 [-0.904, +0.777] | -0.008702 | -0.15 | 0.883 | not applied (n < 1000) | 0.977 | +2.0 | +0.7 | 0.0845 | 0.0973 |
| CV (%) | 241 | -0.400 [-1.222, +0.421] | -0.08082 | -0.95 | 0.340 | not applied (n < 1000) | 0.796 | +1.0 | -0.4 | 0.0912 | 0.0973 |
| Mean / SD ratio | 241 | +0.547 [-0.282, +1.375] | 0.5725 | 1.29 | 0.196 | not applied (n < 1000) | 0.675 | +0.0 | -1.3 | 0.0961 | 0.0973 |
| Avg. daily mean / SD | 241 | +0.199 [-0.613, +1.010] | 0.1599 | 0.48 | 0.632 | not applied (n < 1000) | 0.873 | +1.7 | +0.4 | 0.0946 | 0.0973 |
| MAG (mg/dL/h) | 241 | -0.021 [-0.870, +0.829] | -0.002246 | -0.05 | 0.962 | not applied (n < 1000) | 0.983 | +2.0 | +0.7 | 0.0934 | 0.0973 |
| Avg. daily range (mg/dL) | 241 | +0.031 [-0.771, +0.833] | 0.001108 | 0.08 | 0.940 | not applied (n < 1000) | 0.977 | +2.0 | +0.7 | 0.0877 | 0.0973 |
| SD of daily means (mg/dL) | 241 | -0.320 [-1.111, +0.471] | -0.06765 | -0.79 | 0.428 | not applied (n < 1000) | 0.837 | +1.3 | -0.0 | 0.0786 | 0.0973 |
| Time in range 70-180, pooled (%) | 241 | -0.206 [-0.936, +0.524] | -0.01244 | -0.55 | 0.581 | not applied (n < 1000) | 0.868 | +1.7 | +0.4 | 0.0831 | 0.0973 |
| Avg. daily time in range 70-180 (%) | 241 | -0.234 [-0.958, +0.490] | -0.01398 | -0.63 | 0.527 | not applied (n < 1000) | 0.858 | +1.7 | +0.3 | 0.0843 | 0.0973 |
| Any reading < 54 during wear (0/1) | 241 | -0.212 [-1.018, +0.593] | -0.48 | -0.52 | 0.605 | not applied (n < 1000) | 0.873 | +1.7 | +0.4 | 0.0719 | 0.0973 |
| Time < 54, pooled (%) | 241 | -0.503 [-1.048, +0.043] | -0.5257 | -1.81 | 0.071 | not applied (n < 1000) | 0.457 | +0.3 | -1.0 | 0.0944 | 0.0973 |
| Avg. daily time < 54 (%) | 241 | -0.489 [-1.171, +0.193] | -0.6731 | -1.41 | 0.160 | not applied (n < 1000) | 0.635 | +0.4 | -0.9 | 0.0972 | 0.0973 |
| Time 54-69, pooled (%) | 241 | +0.111 [-0.522, +0.745] | 0.08583 | 0.34 | 0.730 | not applied (n < 1000) | 0.919 | +1.9 | +0.6 | 0.0936 | 0.0973 |
| Avg. daily time 54-69 (%) | 241 | +0.205 [-0.411, +0.821] | 0.1502 | 0.65 | 0.515 | not applied (n < 1000) | 0.855 | +1.7 | +0.4 | 0.0931 | 0.0973 |
| Time < 70, pooled (%) | 241 | -0.181 [-1.158, +0.796] | -0.09365 | -0.36 | 0.717 | not applied (n < 1000) | 0.918 | +1.8 | +0.5 | 0.0880 | 0.0973 |
| Avg. daily time < 70 (%) | 241 | -0.045 [-0.942, +0.852] | -0.02368 | -0.10 | 0.922 | not applied (n < 1000) | 0.977 | +2.0 | +0.7 | 0.0909 | 0.0973 |
| Time 54-250, pooled (%) | 241 | -0.332 [-0.961, +0.297] | -0.03045 | -1.03 | 0.301 | not applied (n < 1000) | 0.775 | +1.3 | -0.0 | 0.0877 | 0.0973 |
| Avg. daily time 54-250 (%) | 241 | -0.348 [-0.984, +0.287] | -0.03252 | -1.07 | 0.283 | not applied (n < 1000) | 0.758 | +1.2 | -0.1 | 0.0879 | 0.0973 |
| Time 181-250, pooled (%) | 241 | -0.049 [-0.846, +0.749] | -0.004802 | -0.12 | 0.904 | not applied (n < 1000) | 0.977 | +2.0 | +0.7 | 0.0887 | 0.0973 |
| Avg. daily time 181-250 (%) | 241 | -0.020 [-0.812, +0.772] | -0.001948 | -0.05 | 0.960 | not applied (n < 1000) | 0.983 | +2.0 | +0.7 | 0.0888 | 0.0973 |
| Time > 180, pooled (%) | 241 | +0.226 [-0.498, +0.950] | 0.01355 | 0.61 | 0.541 | not applied (n < 1000) | 0.867 | +1.7 | +0.4 | 0.0836 | 0.0973 |
| Avg. daily time > 180 (%) | 241 | +0.237 [-0.484, +0.959] | 0.01409 | 0.64 | 0.519 | not applied (n < 1000) | 0.858 | +1.6 | +0.3 | 0.0843 | 0.0973 |
| Nocturnal time > 180 (%) | 241 | +0.284 [-0.394, +0.963] | 0.01632 | 0.82 | 0.411 | not applied (n < 1000) | 0.837 | +1.5 | +0.2 | 0.0902 | 0.0973 |
| Time > 250, pooled (%) | 241 | +0.378 [-0.240, +0.997] | 0.03475 | 1.20 | 0.231 | not applied (n < 1000) | 0.700 | +1.1 | -0.3 | 0.0891 | 0.0973 |
| Avg. daily time > 250 (%) | 241 | +0.382 [-0.248, +1.013] | 0.03574 | 1.19 | 0.235 | not applied (n < 1000) | 0.700 | +1.0 | -0.3 | 0.0888 | 0.0973 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 241; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 241 | -1.890 [-3.851, +0.070] | -2.064 | -1.89 | 0.059 | not applied (n < 1000) | 0.449 | -1.9 | +0.0 | -0.0270 | -0.0282 |
| Mean glucose (mg/dL) | 241 | -0.824 [-3.136, +1.488] | -0.02783 | -0.70 | 0.485 | not applied (n < 1000) | 0.842 | +1.3 | +3.2 | -0.0496 | -0.0282 |
| GMI (%) | 241 | -0.824 [-3.136, +1.488] | -1.163 | -0.70 | 0.485 | not applied (n < 1000) | 0.842 | +1.3 | +3.2 | -0.0496 | -0.0282 |
| Nocturnal mean 00-06h (mg/dL) | 241 | -0.840 [-3.197, +1.518] | -0.0257 | -0.70 | 0.485 | not applied (n < 1000) | 0.842 | +1.2 | +3.2 | -0.0543 | -0.0282 |
| Glucose SD, pooled (mg/dL) | 241 | -1.257 [-3.290, +0.776] | -0.1639 | -1.21 | 0.225 | not applied (n < 1000) | 0.700 | +0.3 | +2.2 | -0.0316 | -0.0282 |
| Avg. daily SD (mg/dL) | 241 | -0.900 [-3.049, +1.249] | -0.1236 | -0.82 | 0.412 | not applied (n < 1000) | 0.837 | +1.1 | +3.1 | -0.0385 | -0.0282 |
| CV (%) | 241 | -0.934 [-2.919, +1.051] | -0.1885 | -0.92 | 0.356 | not applied (n < 1000) | 0.805 | +1.0 | +3.0 | -0.0337 | -0.0282 |
| Mean / SD ratio | 241 | +0.630 [-1.475, +2.735] | 0.6601 | 0.59 | 0.557 | not applied (n < 1000) | 0.868 | +1.5 | +3.5 | -0.0389 | -0.0282 |
| Avg. daily mean / SD | 241 | +0.093 [-2.067, +2.253] | 0.07472 | 0.08 | 0.933 | not applied (n < 1000) | 0.977 | +2.0 | +3.9 | -0.0498 | -0.0282 |
| MAG (mg/dL/h) | 241 | -0.866 [-3.145, +1.414] | -0.09412 | -0.74 | 0.457 | not applied (n < 1000) | 0.837 | +1.2 | +3.2 | -0.0293 | -0.0282 |
| Avg. daily range (mg/dL) | 241 | -0.805 [-3.098, +1.489] | -0.02892 | -0.69 | 0.492 | not applied (n < 1000) | 0.847 | +1.3 | +3.2 | -0.0402 | -0.0282 |
| SD of daily means (mg/dL) | 241 | -1.550 [-3.507, +0.406] | -0.3278 | -1.55 | 0.120 | not applied (n < 1000) | 0.559 | -0.8 | +1.2 | -0.0267 | -0.0282 |
| Time in range 70-180, pooled (%) | 241 | +0.895 [-1.540, +3.330] | 0.0541 | 0.72 | 0.471 | not applied (n < 1000) | 0.837 | +1.1 | +3.1 | -0.0509 | -0.0282 |
| Avg. daily time in range 70-180 (%) | 241 | +0.818 [-1.604, +3.239] | 0.04892 | 0.66 | 0.508 | not applied (n < 1000) | 0.855 | +1.3 | +3.2 | -0.0518 | -0.0282 |
| Any reading < 54 during wear (0/1) | 241 | -0.040 [-2.086, +2.007] | -0.08967 | -0.04 | 0.970 | not applied (n < 1000) | 0.984 | +2.0 | +3.9 | -0.0311 | -0.0282 |
| Time < 54, pooled (%) | 241 | -0.952 [-8.723, +6.819] | -0.9952 | -0.24 | 0.810 | not applied (n < 1000) | 0.940 | +1.0 | +2.9 | -0.0951 | -0.0282 |
| Avg. daily time < 54 (%) | 241 | -1.051 [-5.035, +2.932] | -1.446 | -0.52 | 0.605 | not applied (n < 1000) | 0.873 | +0.7 | +2.7 | -0.0430 | -0.0282 |
| Time 54-69, pooled (%) | 241 | -1.803 [-2.940, -0.667] | -1.389 | -3.11 | 0.002** | not applied (n < 1000) | 0.071 | -1.7 | +0.3 | -0.0130 | -0.0282 |
| Avg. daily time 54-69 (%) | 241 | -1.848 [-2.961, -0.736] | -1.354 | -3.26 | 0.001** | not applied (n < 1000) | 0.047 (q<0.05) | -1.8 | +0.1 | -0.0127 | -0.0282 |
| Time < 70, pooled (%) | 241 | -1.699 [-3.294, -0.104] | -0.8793 | -2.09 | 0.037* | not applied (n < 1000) | 0.351 | -1.3 | +0.7 | -0.0156 | -0.0282 |
| Avg. daily time < 70 (%) | 241 | -1.758 [-3.079, -0.437] | -0.9312 | -2.61 | 0.009** | not applied (n < 1000) | 0.201 | -1.4 | +0.5 | -0.0146 | -0.0282 |
| Time 54-250, pooled (%) | 241 | +1.939 [+0.123, +3.755] | 0.1778 | 2.09 | 0.036* | not applied (n < 1000) | 0.351 | -2.3 | -0.3 | -0.0271 | -0.0282 |
| Avg. daily time 54-250 (%) | 241 | +1.936 [+0.096, +3.776] | 0.1809 | 2.06 | 0.039* | not applied (n < 1000) | 0.366 | -2.3 | -0.3 | -0.0271 | -0.0282 |
| Time 181-250, pooled (%) | 241 | +0.953 [-1.817, +3.724] | 0.09372 | 0.67 | 0.500 | not applied (n < 1000) | 0.852 | +1.0 | +3.0 | -0.0380 | -0.0282 |
| Avg. daily time 181-250 (%) | 241 | +1.000 [-1.730, +3.730] | 0.09575 | 0.72 | 0.473 | not applied (n < 1000) | 0.837 | +0.9 | +2.9 | -0.0392 | -0.0282 |
| Time > 180, pooled (%) | 241 | -0.687 [-3.153, +1.778] | -0.04123 | -0.55 | 0.585 | not applied (n < 1000) | 0.868 | +1.5 | +3.4 | -0.0524 | -0.0282 |
| Avg. daily time > 180 (%) | 241 | -0.613 [-3.065, +1.838] | -0.03643 | -0.49 | 0.624 | not applied (n < 1000) | 0.873 | +1.6 | +3.5 | -0.0533 | -0.0282 |
| Nocturnal time > 180 (%) | 241 | -0.888 [-3.421, +1.646] | -0.05095 | -0.69 | 0.492 | not applied (n < 1000) | 0.847 | +1.1 | +3.1 | -0.0595 | -0.0282 |
| Time > 250, pooled (%) | 241 | -1.861 [-3.695, -0.027] | -0.1709 | -1.99 | 0.047* | not applied (n < 1000) | 0.417 | -1.9 | +0.0 | -0.0286 | -0.0282 |
| Avg. daily time > 250 (%) | 241 | -1.867 [-3.713, -0.021] | -0.1746 | -1.98 | 0.047* | not applied (n < 1000) | 0.417 | -2.0 | -0.0 | -0.0284 | -0.0282 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 218; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 218 | +232.325 [-250.461, +715.110] | 259.3 | 0.94 | 0.346 | not applied (n < 1000) | 0.796 | +1.2 | +0.0 | -0.0218 | -0.0165 |
| Mean glucose (mg/dL) | 218 | -23.783 [-653.994, +606.428] | -0.8489 | -0.07 | 0.941 | not applied (n < 1000) | 0.977 | +2.0 | +0.8 | -0.0342 | -0.0165 |
| GMI (%) | 218 | -23.783 [-653.994, +606.428] | -35.49 | -0.07 | 0.941 | not applied (n < 1000) | 0.977 | +2.0 | +0.8 | -0.0342 | -0.0165 |
| Nocturnal mean 00-06h (mg/dL) | 218 | +70.460 [-482.353, +623.274] | 2.255 | 0.25 | 0.803 | not applied (n < 1000) | 0.940 | +1.9 | +0.7 | -0.0289 | -0.0165 |
| Glucose SD, pooled (mg/dL) | 218 | -165.997 [-766.925, +434.931] | -22.7 | -0.54 | 0.588 | not applied (n < 1000) | 0.868 | +1.6 | +0.4 | -0.0284 | -0.0165 |
| Avg. daily SD (mg/dL) | 218 | -149.287 [-757.456, +458.883] | -21 | -0.48 | 0.630 | not applied (n < 1000) | 0.873 | +1.7 | +0.5 | -0.0283 | -0.0165 |
| CV (%) | 218 | -134.679 [-692.036, +422.677] | -28.24 | -0.47 | 0.636 | not applied (n < 1000) | 0.873 | +1.7 | +0.5 | -0.0265 | -0.0165 |
| Mean / SD ratio | 218 | +68.257 [-477.272, +613.787] | 73.42 | 0.25 | 0.806 | not applied (n < 1000) | 0.940 | +1.9 | +0.7 | -0.0297 | -0.0165 |
| Avg. daily mean / SD | 218 | -27.952 [-562.314, +506.411] | -23.35 | -0.10 | 0.918 | not applied (n < 1000) | 0.977 | +2.0 | +0.8 | -0.0247 | -0.0165 |
| MAG (mg/dL/h) | 218 | +338.426 [-183.059, +859.912] | 38.93 | 1.27 | 0.203 | not applied (n < 1000) | 0.689 | +0.4 | -0.8 | -0.0187 | -0.0165 |
| Avg. daily range (mg/dL) | 218 | -59.814 [-654.581, +534.952] | -2.231 | -0.20 | 0.844 | not applied (n < 1000) | 0.956 | +1.9 | +0.7 | -0.0249 | -0.0165 |
| SD of daily means (mg/dL) | 218 | -114.603 [-591.170, +361.965] | -27.26 | -0.47 | 0.637 | not applied (n < 1000) | 0.873 | +1.8 | +0.6 | -0.0290 | -0.0165 |
| Time in range 70-180, pooled (%) | 218 | +157.394 [-517.045, +831.833] | 10.04 | 0.46 | 0.647 | not applied (n < 1000) | 0.880 | +1.6 | +0.4 | -0.0332 | -0.0165 |
| Avg. daily time in range 70-180 (%) | 218 | +172.267 [-502.978, +847.511] | 10.88 | 0.50 | 0.617 | not applied (n < 1000) | 0.873 | +1.6 | +0.4 | -0.0329 | -0.0165 |
| Any reading < 54 during wear (0/1) | 218 | -61.496 [-561.329, +438.337] | -137.4 | -0.24 | 0.809 | not applied (n < 1000) | 0.940 | +1.9 | +0.7 | -0.0327 | -0.0165 |
| Time < 54, pooled (%) | 218 | -103.199 [-514.857, +308.460] | -102.9 | -0.49 | 0.623 | not applied (n < 1000) | 0.873 | +1.8 | +0.6 | -0.0203 | -0.0165 |
| Avg. daily time < 54 (%) | 218 | -113.637 [-411.565, +184.292] | -149.3 | -0.75 | 0.455 | not applied (n < 1000) | 0.837 | +1.8 | +0.6 | -0.0199 | -0.0165 |
| Time 54-69, pooled (%) | 218 | -144.967 [-514.686, +224.753] | -108.6 | -0.77 | 0.442 | not applied (n < 1000) | 0.837 | +1.7 | +0.5 | -0.0356 | -0.0165 |
| Avg. daily time 54-69 (%) | 218 | -127.302 [-521.904, +267.301] | -90.48 | -0.63 | 0.527 | not applied (n < 1000) | 0.858 | +1.8 | +0.6 | -0.0402 | -0.0165 |
| Time < 70, pooled (%) | 218 | -150.060 [-478.809, +178.690] | -74.89 | -0.89 | 0.371 | not applied (n < 1000) | 0.816 | +1.7 | +0.5 | -0.0187 | -0.0165 |
| Avg. daily time < 70 (%) | 218 | -137.158 [-487.187, +212.871] | -70.04 | -0.77 | 0.442 | not applied (n < 1000) | 0.837 | +1.7 | +0.5 | -0.0225 | -0.0165 |
| Time 54-250, pooled (%) | 218 | -137.845 [-671.095, +395.406] | -13.82 | -0.51 | 0.612 | not applied (n < 1000) | 0.873 | +1.7 | +0.5 | -0.0245 | -0.0165 |
| Avg. daily time 54-250 (%) | 218 | -139.141 [-667.144, +388.861] | -14.46 | -0.52 | 0.606 | not applied (n < 1000) | 0.873 | +1.7 | +0.5 | -0.0243 | -0.0165 |
| Time 181-250, pooled (%) | 218 | -405.616 [-973.868, +162.636] | -41.42 | -1.40 | 0.162 | not applied (n < 1000) | 0.635 | -0.3 | -1.5 | -0.0192 | -0.0165 |
| Avg. daily time 181-250 (%) | 218 | -419.367 [-983.134, +144.400] | -41.71 | -1.46 | 0.145 | not applied (n < 1000) | 0.621 | -0.4 | -1.6 | -0.0195 | -0.0165 |
| Time > 180, pooled (%) | 218 | -137.858 [-808.964, +533.248] | -8.725 | -0.40 | 0.687 | not applied (n < 1000) | 0.899 | +1.7 | +0.5 | -0.0337 | -0.0165 |
| Avg. daily time > 180 (%) | 218 | -155.062 [-826.947, +516.822] | -9.725 | -0.45 | 0.651 | not applied (n < 1000) | 0.882 | +1.6 | +0.4 | -0.0335 | -0.0165 |
| Nocturnal time > 180 (%) | 218 | -18.606 [-603.770, +566.558] | -1.131 | -0.06 | 0.950 | not applied (n < 1000) | 0.981 | +2.0 | +0.8 | -0.0254 | -0.0165 |
| Time > 250, pooled (%) | 218 | +148.708 [-376.747, +674.164] | 14.96 | 0.55 | 0.579 | not applied (n < 1000) | 0.868 | +1.7 | +0.5 | -0.0234 | -0.0165 |
| Avg. daily time > 250 (%) | 218 | +148.280 [-372.449, +669.008] | 15.43 | 0.56 | 0.577 | not applied (n < 1000) | 0.868 | +1.7 | +0.5 | -0.0235 | -0.0165 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 218; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 218 | +0.875 [-0.940, +2.690] | 0.9766 | 0.95 | 0.345 | not applied (n < 1000) | 0.796 | +0.9 | +0.0 | 0.0170 | 0.0283 |
| Mean glucose (mg/dL) | 218 | +0.262 [-1.782, +2.305] | 0.00935 | 0.25 | 0.802 | not applied (n < 1000) | 0.940 | +1.9 | +1.0 | 0.0103 | 0.0283 |
| GMI (%) | 218 | +0.262 [-1.782, +2.305] | 0.3909 | 0.25 | 0.802 | not applied (n < 1000) | 0.940 | +1.9 | +1.0 | 0.0103 | 0.0283 |
| Nocturnal mean 00-06h (mg/dL) | 218 | +0.468 [-1.405, +2.341] | 0.01499 | 0.49 | 0.624 | not applied (n < 1000) | 0.873 | +1.7 | +0.8 | 0.0152 | 0.0283 |
| Glucose SD, pooled (mg/dL) | 218 | -0.318 [-2.241, +1.604] | -0.04351 | -0.32 | 0.746 | not applied (n < 1000) | 0.922 | +1.9 | +1.0 | 0.0111 | 0.0283 |
| Avg. daily SD (mg/dL) | 218 | -0.297 [-2.230, +1.636] | -0.04183 | -0.30 | 0.763 | not applied (n < 1000) | 0.927 | +1.9 | +1.0 | 0.0120 | 0.0283 |
| CV (%) | 218 | -0.520 [-2.324, +1.283] | -0.1091 | -0.57 | 0.572 | not applied (n < 1000) | 0.868 | +1.6 | +0.7 | 0.0211 | 0.0283 |
| Mean / SD ratio | 218 | +0.236 [-1.599, +2.072] | 0.254 | 0.25 | 0.801 | not applied (n < 1000) | 0.940 | +1.9 | +1.0 | 0.0167 | 0.0283 |
| Avg. daily mean / SD | 218 | -0.020 [-1.801, +1.761] | -0.01636 | -0.02 | 0.983 | not applied (n < 1000) | 0.992 | +2.0 | +1.1 | 0.0189 | 0.0283 |
| MAG (mg/dL/h) | 218 | +0.857 [-0.873, +2.587] | 0.09861 | 0.97 | 0.331 | not applied (n < 1000) | 0.795 | +1.0 | +0.1 | 0.0227 | 0.0283 |
| Avg. daily range (mg/dL) | 218 | -0.120 [-2.025, +1.785] | -0.004466 | -0.12 | 0.902 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0163 | 0.0283 |
| SD of daily means (mg/dL) | 218 | -0.088 [-1.709, +1.532] | -0.02102 | -0.11 | 0.915 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0127 | 0.0283 |
| Time in range 70-180, pooled (%) | 218 | +0.111 [-2.050, +2.272] | 0.0071 | 0.10 | 0.920 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0100 | 0.0283 |
| Avg. daily time in range 70-180 (%) | 218 | +0.162 [-2.007, +2.331] | 0.01022 | 0.15 | 0.884 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0109 | 0.0283 |
| Any reading < 54 during wear (0/1) | 218 | -0.305 [-1.963, +1.353] | -0.6813 | -0.36 | 0.719 | not applied (n < 1000) | 0.918 | +1.9 | +1.0 | 0.0175 | 0.0283 |
| Time < 54, pooled (%) | 218 | -0.216 [-2.622, +2.189] | -0.2156 | -0.18 | 0.860 | not applied (n < 1000) | 0.968 | +1.9 | +1.0 | 0.0173 | 0.0283 |
| Avg. daily time < 54 (%) | 218 | -0.280 [-1.549, +0.989] | -0.3678 | -0.43 | 0.665 | not applied (n < 1000) | 0.890 | +1.9 | +1.0 | 0.0227 | 0.0283 |
| Time 54-69, pooled (%) | 218 | -0.520 [-1.772, +0.732] | -0.3894 | -0.81 | 0.416 | not applied (n < 1000) | 0.837 | +1.6 | +0.7 | 0.0070 | 0.0283 |
| Avg. daily time 54-69 (%) | 218 | -0.538 [-1.755, +0.679] | -0.3825 | -0.87 | 0.386 | not applied (n < 1000) | 0.826 | +1.6 | +0.7 | 0.0065 | 0.0283 |
| Time < 70, pooled (%) | 218 | -0.460 [-1.641, +0.722] | -0.2294 | -0.76 | 0.446 | not applied (n < 1000) | 0.837 | +1.7 | +0.8 | 0.0238 | 0.0283 |
| Avg. daily time < 70 (%) | 218 | -0.500 [-1.767, +0.766] | -0.2555 | -0.77 | 0.439 | not applied (n < 1000) | 0.837 | +1.6 | +0.7 | 0.0203 | 0.0283 |
| Time 54-250, pooled (%) | 218 | -0.696 [-2.592, +1.201] | -0.06976 | -0.72 | 0.472 | not applied (n < 1000) | 0.837 | +1.3 | +0.4 | 0.0151 | 0.0283 |
| Avg. daily time 54-250 (%) | 218 | -0.694 [-2.578, +1.190] | -0.07214 | -0.72 | 0.470 | not applied (n < 1000) | 0.837 | +1.3 | +0.4 | 0.0153 | 0.0283 |
| Time 181-250, pooled (%) | 218 | -0.908 [-2.782, +0.965] | -0.09277 | -0.95 | 0.342 | not applied (n < 1000) | 0.796 | +0.9 | -0.0 | 0.0237 | 0.0283 |
| Avg. daily time 181-250 (%) | 218 | -0.935 [-2.797, +0.928] | -0.09295 | -0.98 | 0.325 | not applied (n < 1000) | 0.790 | +0.8 | -0.1 | 0.0235 | 0.0283 |
| Time > 180, pooled (%) | 218 | -0.053 [-2.205, +2.100] | -0.00333 | -0.05 | 0.962 | not applied (n < 1000) | 0.983 | +2.0 | +1.1 | 0.0096 | 0.0283 |
| Avg. daily time > 180 (%) | 218 | -0.100 [-2.256, +2.056] | -0.006289 | -0.09 | 0.927 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0102 | 0.0283 |
| Nocturnal time > 180 (%) | 218 | +0.073 [-1.914, +2.061] | 0.004457 | 0.07 | 0.942 | not applied (n < 1000) | 0.977 | +2.0 | +1.1 | 0.0150 | 0.0283 |
| Time > 250, pooled (%) | 218 | +0.721 [-1.170, +2.612] | 0.07247 | 0.75 | 0.455 | not applied (n < 1000) | 0.837 | +1.2 | +0.3 | 0.0162 | 0.0283 |
| Avg. daily time > 250 (%) | 218 | +0.718 [-1.155, +2.591] | 0.07469 | 0.75 | 0.452 | not applied (n < 1000) | 0.837 | +1.2 | +0.3 | 0.0162 | 0.0283 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 218; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 218 | +1.157 [+0.083, +2.231] | 1.292 | 2.11 | 0.035* | not applied (n < 1000) | 0.351 | -3.5 | +0.0 | -0.0645 | -0.0790 |
| Mean glucose (mg/dL) | 218 | +1.235 [-0.020, +2.490] | 0.04403 | 1.93 | 0.054 | not applied (n < 1000) | 0.434 | -4.3 | -0.8 | -0.0601 | -0.0790 |
| GMI (%) | 218 | +1.235 [-0.020, +2.490] | 1.841 | 1.93 | 0.054 | not applied (n < 1000) | 0.434 | -4.3 | -0.8 | -0.0601 | -0.0790 |
| Nocturnal mean 00-06h (mg/dL) | 218 | +0.988 [-0.261, +2.237] | 0.03161 | 1.55 | 0.121 | not applied (n < 1000) | 0.559 | -2.0 | +1.5 | -0.0695 | -0.0790 |
| Glucose SD, pooled (mg/dL) | 218 | +1.266 [+0.007, +2.525] | 0.1733 | 1.97 | 0.049* | not applied (n < 1000) | 0.418 | -4.5 | -1.0 | -0.0622 | -0.0790 |
| Avg. daily SD (mg/dL) | 218 | +1.111 [-0.101, +2.323] | 0.1563 | 1.80 | 0.072 | not applied (n < 1000) | 0.457 | -3.0 | +0.5 | -0.0644 | -0.0790 |
| CV (%) | 218 | +0.488 [-0.534, +1.511] | 0.1025 | 0.94 | 0.350 | not applied (n < 1000) | 0.796 | +1.0 | +4.6 | -0.0803 | -0.0790 |
| Mean / SD ratio | 218 | -0.563 [-1.596, +0.471] | -0.6063 | -1.07 | 0.286 | not applied (n < 1000) | 0.758 | +0.7 | +4.2 | -0.0759 | -0.0790 |
| Avg. daily mean / SD | 218 | -0.449 [-1.448, +0.550] | -0.3754 | -0.88 | 0.378 | not applied (n < 1000) | 0.820 | +1.2 | +4.7 | -0.0788 | -0.0790 |
| MAG (mg/dL/h) | 218 | +0.458 [-0.579, +1.496] | 0.05267 | 0.87 | 0.386 | not applied (n < 1000) | 0.826 | +1.2 | +4.7 | -0.0818 | -0.0790 |
| Avg. daily range (mg/dL) | 218 | +0.854 [-0.229, +1.937] | 0.0318 | 1.54 | 0.122 | not applied (n < 1000) | 0.559 | -1.0 | +2.5 | -0.0692 | -0.0790 |
| SD of daily means (mg/dL) | 218 | +1.383 [+0.316, +2.450] | 0.329 | 2.54 | 0.011* | not applied (n < 1000) | 0.206 | -6.5 | -3.0 | -0.0576 | -0.0790 |
| Time in range 70-180, pooled (%) | 218 | -1.153 [-2.612, +0.306] | -0.07355 | -1.55 | 0.121 | not applied (n < 1000) | 0.559 | -3.5 | +0.1 | -0.0728 | -0.0790 |
| Avg. daily time in range 70-180 (%) | 218 | -1.116 [-2.579, +0.348] | -0.07043 | -1.49 | 0.135 | not applied (n < 1000) | 0.595 | -3.1 | +0.4 | -0.0739 | -0.0790 |
| Any reading < 54 during wear (0/1) | 218 | -0.095 [-1.233, +1.044] | -0.2112 | -0.16 | 0.871 | not applied (n < 1000) | 0.971 | +2.0 | +5.5 | -0.0977 | -0.0790 |
| Time < 54, pooled (%) | 218 | +0.450 [-3.400, +4.299] | 0.4482 | 0.23 | 0.819 | not applied (n < 1000) | 0.942 | +1.2 | +4.7 | -0.1751 | -0.0790 |
| Avg. daily time < 54 (%) | 218 | +0.425 [-1.122, +1.971] | 0.558 | 0.54 | 0.590 | not applied (n < 1000) | 0.868 | +1.3 | +4.8 | -0.1014 | -0.0790 |
| Time 54-69, pooled (%) | 218 | +0.606 [-0.402, +1.614] | 0.4543 | 1.18 | 0.238 | not applied (n < 1000) | 0.705 | +0.5 | +4.0 | -0.0793 | -0.0790 |
| Avg. daily time 54-69 (%) | 218 | +0.616 [-0.353, +1.586] | 0.4382 | 1.25 | 0.213 | not applied (n < 1000) | 0.698 | +0.4 | +4.0 | -0.0793 | -0.0790 |
| Time < 70, pooled (%) | 218 | +0.637 [-0.201, +1.475] | 0.3179 | 1.49 | 0.136 | not applied (n < 1000) | 0.595 | +0.3 | +3.9 | -0.0787 | -0.0790 |
| Avg. daily time < 70 (%) | 218 | +0.614 [-0.228, +1.456] | 0.3137 | 1.43 | 0.153 | not applied (n < 1000) | 0.629 | +0.5 | +4.0 | -0.0786 | -0.0790 |
| Time 54-250, pooled (%) | 218 | -0.913 [-2.283, +0.458] | -0.09152 | -1.31 | 0.192 | not applied (n < 1000) | 0.674 | -1.6 | +1.9 | -0.0817 | -0.0790 |
| Avg. daily time 54-250 (%) | 218 | -0.911 [-2.310, +0.488] | -0.09465 | -1.28 | 0.202 | not applied (n < 1000) | 0.689 | -1.6 | +2.0 | -0.0819 | -0.0790 |
| Time 181-250, pooled (%) | 218 | +0.839 [-0.591, +2.268] | 0.08565 | 1.15 | 0.250 | not applied (n < 1000) | 0.715 | -0.7 | +2.8 | -0.0838 | -0.0790 |
| Avg. daily time 181-250 (%) | 218 | +0.804 [-0.630, +2.237] | 0.07992 | 1.10 | 0.272 | not applied (n < 1000) | 0.752 | -0.5 | +3.1 | -0.0834 | -0.0790 |
| Time > 180, pooled (%) | 218 | +1.068 [-0.396, +2.532] | 0.06759 | 1.43 | 0.153 | not applied (n < 1000) | 0.629 | -2.7 | +0.9 | -0.0742 | -0.0790 |
| Avg. daily time > 180 (%) | 218 | +1.037 [-0.429, +2.503] | 0.06504 | 1.39 | 0.166 | not applied (n < 1000) | 0.638 | -2.4 | +1.1 | -0.0749 | -0.0790 |
| Nocturnal time > 180 (%) | 218 | +0.293 [-1.226, +1.813] | 0.01783 | 0.38 | 0.705 | not applied (n < 1000) | 0.914 | +1.7 | +5.2 | -0.0945 | -0.0790 |
| Time > 250, pooled (%) | 218 | +0.873 [-0.533, +2.279] | 0.08782 | 1.22 | 0.224 | not applied (n < 1000) | 0.700 | -1.3 | +2.3 | -0.0832 | -0.0790 |
| Avg. daily time > 250 (%) | 218 | +0.881 [-0.543, +2.306] | 0.0917 | 1.21 | 0.225 | not applied (n < 1000) | 0.700 | -1.3 | +2.2 | -0.0829 | -0.0790 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 215; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 215 | -6.743 [-14.082, +0.595] | -7.752 | -1.80 | 0.072 | not applied (n < 1000) | 0.457 | -0.2 | +0.0 | -0.1124 | -0.1092 |
| Mean glucose (mg/dL) | 215 | -2.606 [-12.173, +6.962] | -0.09854 | -0.53 | 0.593 | not applied (n < 1000) | 0.868 | +1.7 | +1.9 | -0.1342 | -0.1092 |
| GMI (%) | 215 | -2.606 [-12.173, +6.962] | -4.119 | -0.53 | 0.593 | not applied (n < 1000) | 0.868 | +1.7 | +1.9 | -0.1342 | -0.1092 |
| Nocturnal mean 00-06h (mg/dL) | 215 | -2.189 [-11.314, +6.936] | -0.07476 | -0.47 | 0.638 | not applied (n < 1000) | 0.873 | +1.8 | +2.0 | -0.1313 | -0.1092 |
| Glucose SD, pooled (mg/dL) | 215 | -5.710 [-16.135, +4.715] | -0.7848 | -1.07 | 0.283 | not applied (n < 1000) | 0.758 | +0.4 | +0.6 | -0.1304 | -0.1092 |
| Avg. daily SD (mg/dL) | 215 | -7.935 [-18.742, +2.873] | -1.13 | -1.44 | 0.150 | not applied (n < 1000) | 0.629 | -1.1 | -0.9 | -0.1226 | -0.1092 |
| CV (%) | 215 | -4.086 [-13.561, +5.388] | -0.857 | -0.85 | 0.398 | not applied (n < 1000) | 0.835 | +1.2 | +1.4 | -0.1300 | -0.1092 |
| Mean / SD ratio | 215 | +5.174 [-3.642, +13.990] | 5.59 | 1.15 | 0.250 | not applied (n < 1000) | 0.715 | +0.6 | +0.9 | -0.1191 | -0.1092 |
| Avg. daily mean / SD | 215 | +12.077 [+2.775, +21.378] | 10.09 | 2.54 | 0.011* | not applied (n < 1000) | 0.206 | -5.5 | -5.3 | -0.0997 | -0.1092 |
| MAG (mg/dL/h) | 215 | -15.094 [-23.750, -6.437] | -1.735 | -3.42 | 6.3e-04*** | not applied (n < 1000) | 0.033 (q<0.05) | -9.2 | -9.0 | -0.0682 | -0.1092 |
| Avg. daily range (mg/dL) | 215 | -9.732 [-20.395, +0.932] | -0.3631 | -1.79 | 0.074 | not applied (n < 1000) | 0.457 | -2.9 | -2.6 | -0.1152 | -0.1092 |
| SD of daily means (mg/dL) | 215 | -1.988 [-9.883, +5.907] | -0.4698 | -0.49 | 0.622 | not applied (n < 1000) | 0.873 | +1.8 | +2.0 | -0.1149 | -0.1092 |
| Time in range 70-180, pooled (%) | 215 | +0.238 [-10.509, +10.986] | 0.01631 | 0.04 | 0.965 | not applied (n < 1000) | 0.983 | +2.0 | +2.2 | -0.1416 | -0.1092 |
| Avg. daily time in range 70-180 (%) | 215 | +0.049 [-10.767, +10.865] | 0.003331 | 0.01 | 0.993 | not applied (n < 1000) | 0.995 | +2.0 | +2.2 | -0.1410 | -0.1092 |
| Any reading < 54 during wear (0/1) | 215 | +8.534 [-0.824, +17.892] | 18.79 | 1.79 | 0.074 | not applied (n < 1000) | 0.457 | -1.8 | -1.5 | -0.1025 | -0.1092 |
| Time < 54, pooled (%) | 215 | -1.418 [-10.282, +7.447] | -1.403 | -0.31 | 0.754 | not applied (n < 1000) | 0.926 | +1.9 | +2.1 | -0.1446 | -0.1092 |
| Avg. daily time < 54 (%) | 215 | -1.792 [-5.907, +2.324] | -2.333 | -0.85 | 0.393 | not applied (n < 1000) | 0.835 | +1.8 | +2.1 | -0.1194 | -0.1092 |
| Time 54-69, pooled (%) | 215 | +2.579 [-6.786, +11.944] | 1.921 | 0.54 | 0.589 | not applied (n < 1000) | 0.868 | +1.7 | +1.9 | -0.1295 | -0.1092 |
| Avg. daily time 54-69 (%) | 215 | +1.069 [-4.554, +6.691] | 0.7555 | 0.37 | 0.709 | not applied (n < 1000) | 0.916 | +1.9 | +2.2 | -0.1199 | -0.1092 |
| Time < 70, pooled (%) | 215 | +1.006 [-5.458, +7.471] | 0.4991 | 0.31 | 0.760 | not applied (n < 1000) | 0.927 | +1.9 | +2.2 | -0.1211 | -0.1092 |
| Avg. daily time < 70 (%) | 215 | +0.062 [-5.099, +5.223] | 0.03153 | 0.02 | 0.981 | not applied (n < 1000) | 0.992 | +2.0 | +2.2 | -0.1183 | -0.1092 |
| Time 54-250, pooled (%) | 215 | +2.605 [-4.663, +9.873] | 0.293 | 0.70 | 0.482 | not applied (n < 1000) | 0.842 | +1.7 | +1.9 | -0.1173 | -0.1092 |
| Avg. daily time 54-250 (%) | 215 | +2.649 [-4.504, +9.802] | 0.3101 | 0.73 | 0.468 | not applied (n < 1000) | 0.837 | +1.6 | +1.9 | -0.1178 | -0.1092 |
| Time 181-250, pooled (%) | 215 | +1.820 [-9.991, +13.631] | 0.1867 | 0.30 | 0.763 | not applied (n < 1000) | 0.927 | +1.8 | +2.1 | -0.1513 | -0.1092 |
| Avg. daily time 181-250 (%) | 215 | +2.210 [-9.477, +13.896] | 0.2209 | 0.37 | 0.711 | not applied (n < 1000) | 0.916 | +1.8 | +2.0 | -0.1488 | -0.1092 |
| Time > 180, pooled (%) | 215 | -0.377 [-11.220, +10.465] | -0.02561 | -0.07 | 0.946 | not applied (n < 1000) | 0.978 | +2.0 | +2.2 | -0.1434 | -0.1092 |
| Avg. daily time > 180 (%) | 215 | -0.057 [-10.932, +10.817] | -0.003858 | -0.01 | 0.992 | not applied (n < 1000) | 0.995 | +2.0 | +2.2 | -0.1425 | -0.1092 |
| Nocturnal time > 180 (%) | 215 | +1.506 [-8.797, +11.808] | 0.0985 | 0.29 | 0.775 | not applied (n < 1000) | 0.927 | +1.9 | +2.1 | -0.1263 | -0.1092 |
| Time > 250, pooled (%) | 215 | -2.455 [-10.019, +5.108] | -0.2773 | -0.64 | 0.525 | not applied (n < 1000) | 0.858 | +1.7 | +1.9 | -0.1172 | -0.1092 |
| Avg. daily time > 250 (%) | 215 | -2.495 [-9.898, +4.907] | -0.2928 | -0.66 | 0.509 | not applied (n < 1000) | 0.855 | +1.7 | +1.9 | -0.1178 | -0.1092 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 218; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 218 | +2.649 [+0.375, +4.923] | 2.957 | 2.28 | 0.022* | not applied (n < 1000) | 0.295 | -3.6 | +0.0 | -0.0927 | -0.1079 |
| Mean glucose (mg/dL) | 218 | +1.354 [-2.011, +4.720] | 0.04833 | 0.79 | 0.430 | not applied (n < 1000) | 0.837 | +0.5 | +4.1 | -0.1138 | -0.1079 |
| GMI (%) | 218 | +1.354 [-2.011, +4.720] | 2.021 | 0.79 | 0.430 | not applied (n < 1000) | 0.837 | +0.5 | +4.1 | -0.1138 | -0.1079 |
| Nocturnal mean 00-06h (mg/dL) | 218 | +0.652 [-2.901, +4.205] | 0.02089 | 0.36 | 0.719 | not applied (n < 1000) | 0.918 | +1.7 | +5.3 | -0.1204 | -0.1079 |
| Glucose SD, pooled (mg/dL) | 218 | +1.583 [-1.319, +4.485] | 0.2165 | 1.07 | 0.285 | not applied (n < 1000) | 0.758 | +0.0 | +3.6 | -0.1177 | -0.1079 |
| Avg. daily SD (mg/dL) | 218 | +1.595 [-1.206, +4.395] | 0.2244 | 1.12 | 0.264 | not applied (n < 1000) | 0.740 | +0.0 | +3.6 | -0.1113 | -0.1079 |
| CV (%) | 218 | +0.994 [-1.562, +3.550] | 0.2084 | 0.76 | 0.446 | not applied (n < 1000) | 0.837 | +1.2 | +4.8 | -0.1113 | -0.1079 |
| Mean / SD ratio | 218 | -1.320 [-3.749, +1.109] | -1.42 | -1.06 | 0.287 | not applied (n < 1000) | 0.758 | +0.6 | +4.2 | -0.1072 | -0.1079 |
| Avg. daily mean / SD | 218 | -1.579 [-3.927, +0.770] | -1.319 | -1.32 | 0.188 | not applied (n < 1000) | 0.674 | -0.0 | +3.6 | -0.1017 | -0.1079 |
| MAG (mg/dL/h) | 218 | +0.361 [-2.029, +2.751] | 0.04142 | 0.30 | 0.767 | not applied (n < 1000) | 0.927 | +1.9 | +5.5 | -0.1127 | -0.1079 |
| Avg. daily range (mg/dL) | 218 | +1.436 [-1.039, +3.911] | 0.05349 | 1.14 | 0.256 | not applied (n < 1000) | 0.725 | +0.3 | +3.9 | -0.1061 | -0.1079 |
| SD of daily means (mg/dL) | 218 | +1.066 [-1.506, +3.638] | 0.2537 | 0.81 | 0.417 | not applied (n < 1000) | 0.837 | +1.0 | +4.6 | -0.1212 | -0.1079 |
| Time in range 70-180, pooled (%) | 218 | -1.468 [-4.898, +1.963] | -0.09361 | -0.84 | 0.402 | not applied (n < 1000) | 0.835 | +0.3 | +3.9 | -0.1223 | -0.1079 |
| Avg. daily time in range 70-180 (%) | 218 | -1.394 [-4.809, +2.022] | -0.08798 | -0.80 | 0.424 | not applied (n < 1000) | 0.837 | +0.5 | +4.1 | -0.1214 | -0.1079 |
| Any reading < 54 during wear (0/1) | 218 | +0.165 [-2.224, +2.554] | 0.3686 | 0.14 | 0.892 | not applied (n < 1000) | 0.977 | +2.0 | +5.6 | -0.1146 | -0.1079 |
| Time < 54, pooled (%) | 218 | -0.012 [-11.679, +11.654] | -0.01226 | -0.00 | 0.998 | not applied (n < 1000) | 0.998 | +2.0 | +5.6 | -0.2785 | -0.1079 |
| Avg. daily time < 54 (%) | 218 | +0.044 [-6.157, +6.245] | 0.05743 | 0.01 | 0.989 | not applied (n < 1000) | 0.995 | +2.0 | +5.6 | -0.1683 | -0.1079 |
| Time 54-69, pooled (%) | 218 | +1.397 [-3.987, +6.780] | 1.046 | 0.51 | 0.611 | not applied (n < 1000) | 0.873 | +0.5 | +4.0 | -0.1088 | -0.1079 |
| Avg. daily time 54-69 (%) | 218 | +1.410 [-4.066, +6.885] | 1.002 | 0.50 | 0.614 | not applied (n < 1000) | 0.873 | +0.4 | +4.0 | -0.1096 | -0.1079 |
| Time < 70, pooled (%) | 218 | +0.931 [-3.489, +5.352] | 0.4647 | 0.41 | 0.680 | not applied (n < 1000) | 0.896 | +1.3 | +4.9 | -0.1219 | -0.1079 |
| Avg. daily time < 70 (%) | 218 | +1.037 [-3.646, +5.720] | 0.5296 | 0.43 | 0.664 | not applied (n < 1000) | 0.890 | +1.2 | +4.7 | -0.1171 | -0.1079 |
| Time 54-250, pooled (%) | 218 | -1.243 [-5.383, +2.898] | -0.1246 | -0.59 | 0.556 | not applied (n < 1000) | 0.868 | +0.7 | +4.3 | -0.1318 | -0.1079 |
| Avg. daily time 54-250 (%) | 218 | -1.243 [-5.411, +2.924] | -0.1292 | -0.58 | 0.559 | not applied (n < 1000) | 0.868 | +0.7 | +4.3 | -0.1317 | -0.1079 |
| Time 181-250, pooled (%) | 218 | +0.890 [-2.051, +3.831] | 0.09089 | 0.59 | 0.553 | not applied (n < 1000) | 0.868 | +1.4 | +5.0 | -0.1218 | -0.1079 |
| Avg. daily time 181-250 (%) | 218 | +0.802 [-2.105, +3.708] | 0.0797 | 0.54 | 0.589 | not applied (n < 1000) | 0.868 | +1.5 | +5.1 | -0.1203 | -0.1079 |
| Time > 180, pooled (%) | 218 | +1.345 [-2.112, +4.802] | 0.08512 | 0.76 | 0.446 | not applied (n < 1000) | 0.837 | +0.6 | +4.2 | -0.1203 | -0.1079 |
| Avg. daily time > 180 (%) | 218 | +1.263 [-2.174, +4.701] | 0.07923 | 0.72 | 0.471 | not applied (n < 1000) | 0.837 | +0.7 | +4.3 | -0.1195 | -0.1079 |
| Nocturnal time > 180 (%) | 218 | -0.391 [-4.201, +3.418] | -0.0238 | -0.20 | 0.840 | not applied (n < 1000) | 0.956 | +1.9 | +5.5 | -0.1302 | -0.1079 |
| Time > 250, pooled (%) | 218 | +1.250 [-2.921, +5.422] | 0.1258 | 0.59 | 0.557 | not applied (n < 1000) | 0.868 | +0.7 | +4.3 | -0.1310 | -0.1079 |
| Avg. daily time > 250 (%) | 218 | +1.244 [-2.948, +5.436] | 0.1294 | 0.58 | 0.561 | not applied (n < 1000) | 0.868 | +0.7 | +4.3 | -0.1308 | -0.1079 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

### Population: Non-healthy group (T2D non-insulin + T2D insulin)

#### MoCA total score (0-30)
*n = 551; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 551 | -0.161 [-0.441, +0.119] | -0.1165 | -1.13 | 0.260 | not applied (n < 1000) | 0.535 | +0.9 | +0.0 | 0.0223 | 0.0218 |
| Mean glucose (mg/dL) | 551 | -0.199 [-0.492, +0.094] | -0.004822 | -1.33 | 0.183 | not applied (n < 1000) | 0.415 | +0.2 | -0.6 | 0.0238 | 0.0218 |
| GMI (%) | 551 | -0.199 [-0.492, +0.094] | -0.2016 | -1.33 | 0.183 | not applied (n < 1000) | 0.415 | +0.2 | -0.6 | 0.0238 | 0.0218 |
| Nocturnal mean 00-06h (mg/dL) | 551 | -0.207 [-0.503, +0.089] | -0.004641 | -1.37 | 0.170 | not applied (n < 1000) | 0.404 | +0.1 | -0.7 | 0.0238 | 0.0218 |
| Glucose SD, pooled (mg/dL) | 551 | -0.308 [-0.595, -0.020] | -0.02474 | -2.10 | 0.036* | not applied (n < 1000) | 0.275 | -2.2 | -3.0 | 0.0274 | 0.0218 |
| Avg. daily SD (mg/dL) | 551 | -0.276 [-0.571, +0.019] | -0.02549 | -1.83 | 0.067 | not applied (n < 1000) | 0.289 | -1.4 | -2.2 | 0.0263 | 0.0218 |
| CV (%) | 551 | -0.128 [-0.382, +0.127] | -0.02308 | -0.98 | 0.325 | not applied (n < 1000) | 0.596 | +1.3 | +0.4 | 0.0206 | 0.0218 |
| Mean / SD ratio | 551 | +0.189 [-0.070, +0.449] | 0.193 | 1.43 | 0.153 | not applied (n < 1000) | 0.389 | +0.4 | -0.5 | 0.0219 | 0.0218 |
| Avg. daily mean / SD | 551 | +0.085 [-0.206, +0.375] | 0.0697 | 0.57 | 0.568 | not applied (n < 1000) | 0.803 | +1.7 | +0.8 | 0.0192 | 0.0218 |
| MAG (mg/dL/h) | 551 | -0.340 [-0.649, -0.031] | -0.03441 | -2.15 | 0.031* | not applied (n < 1000) | 0.247 | -3.1 | -4.0 | 0.0295 | 0.0218 |
| Avg. daily range (mg/dL) | 551 | -0.255 [-0.566, +0.056] | -0.006974 | -1.61 | 0.108 | not applied (n < 1000) | 0.343 | -0.9 | -1.7 | 0.0254 | 0.0218 |
| SD of daily means (mg/dL) | 551 | -0.323 [-0.613, -0.033] | -0.03639 | -2.18 | 0.029* | not applied (n < 1000) | 0.244 | -2.5 | -3.4 | 0.0260 | 0.0218 |
| Time in range 70-180, pooled (%) | 551 | +0.224 [-0.075, +0.524] | 0.008627 | 1.47 | 0.142 | not applied (n < 1000) | 0.382 | -0.2 | -1.1 | 0.0235 | 0.0218 |
| Avg. daily time in range 70-180 (%) | 551 | +0.219 [-0.082, +0.519] | 0.00833 | 1.42 | 0.154 | not applied (n < 1000) | 0.389 | -0.1 | -1.0 | 0.0233 | 0.0218 |
| Any reading < 54 during wear (0/1) | 551 | -0.017 [-0.315, +0.281] | -0.04161 | -0.11 | 0.910 | not applied (n < 1000) | 0.949 | +2.0 | +1.1 | 0.0190 | 0.0218 |
| Time < 54, pooled (%) | 551 | +0.041 [-0.213, +0.295] | 0.1627 | 0.32 | 0.751 | not applied (n < 1000) | 0.861 | +1.9 | +1.1 | 0.0191 | 0.0218 |
| Avg. daily time < 54 (%) | 551 | +0.002 [-0.479, +0.482] | 0.004503 | 0.01 | 0.995 | not applied (n < 1000) | 1.000 | +2.0 | +1.1 | 0.0095 | 0.0218 |
| Time 54-69, pooled (%) | 551 | -0.044 [-0.248, +0.161] | -0.04833 | -0.42 | 0.677 | not applied (n < 1000) | 0.849 | +1.9 | +1.1 | 0.0196 | 0.0218 |
| Avg. daily time 54-69 (%) | 551 | -0.038 [-0.243, +0.167] | -0.04006 | -0.36 | 0.717 | not applied (n < 1000) | 0.853 | +1.9 | +1.1 | 0.0198 | 0.0218 |
| Time < 70, pooled (%) | 551 | -0.027 [-0.236, +0.182] | -0.02539 | -0.25 | 0.799 | not applied (n < 1000) | 0.884 | +2.0 | +1.1 | 0.0193 | 0.0218 |
| Avg. daily time < 70 (%) | 551 | -0.030 [-0.238, +0.179] | -0.02477 | -0.28 | 0.782 | not applied (n < 1000) | 0.873 | +2.0 | +1.1 | 0.0193 | 0.0218 |
| Time 54-250, pooled (%) | 551 | +0.218 [-0.069, +0.505] | 0.01183 | 1.49 | 0.136 | not applied (n < 1000) | 0.378 | -0.1 | -1.0 | 0.0251 | 0.0218 |
| Avg. daily time 54-250 (%) | 551 | +0.214 [-0.075, +0.503] | 0.01172 | 1.45 | 0.146 | not applied (n < 1000) | 0.382 | -0.0 | -0.9 | 0.0250 | 0.0218 |
| Time 181-250, pooled (%) | 551 | -0.119 [-0.420, +0.182] | -0.008121 | -0.78 | 0.438 | not applied (n < 1000) | 0.730 | +1.3 | +0.5 | 0.0180 | 0.0218 |
| Avg. daily time 181-250 (%) | 551 | -0.116 [-0.418, +0.185] | -0.007774 | -0.76 | 0.449 | not applied (n < 1000) | 0.734 | +1.4 | +0.5 | 0.0178 | 0.0218 |
| Time > 180, pooled (%) | 551 | -0.221 [-0.520, +0.077] | -0.008455 | -1.45 | 0.146 | not applied (n < 1000) | 0.382 | -0.2 | -1.0 | 0.0235 | 0.0218 |
| Avg. daily time > 180 (%) | 551 | -0.216 [-0.515, +0.084] | -0.00817 | -1.41 | 0.159 | not applied (n < 1000) | 0.392 | -0.1 | -0.9 | 0.0232 | 0.0218 |
| Nocturnal time > 180 (%) | 551 | -0.251 [-0.558, +0.057] | -0.008299 | -1.60 | 0.110 | not applied (n < 1000) | 0.346 | -0.7 | -1.6 | 0.0241 | 0.0218 |
| Time > 250, pooled (%) | 551 | -0.219 [-0.506, +0.068] | -0.01185 | -1.49 | 0.135 | not applied (n < 1000) | 0.378 | -0.1 | -1.0 | 0.0252 | 0.0218 |
| Avg. daily time > 250 (%) | 551 | -0.214 [-0.503, +0.075] | -0.01172 | -1.45 | 0.146 | not applied (n < 1000) | 0.382 | -0.0 | -0.9 | 0.0250 | 0.0218 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Cognitive impairment (MoCA < 26)
*n = 551; events = 280; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 551 | OR 1.131 [0.943, 1.357] | 0.08935 | 1.33 | 0.184 | not applied (n < 1000) | 0.415 | +0.2 | +0.0 | 0.6019 | 0.5990 |
| Mean glucose (mg/dL) | 551 | OR 1.171 [0.977, 1.403] | 0.00383 | 1.71 | 0.087 | not applied (n < 1000) | 0.323 | -1.0 | -1.2 | 0.6033 | 0.5990 |
| GMI (%) | 551 | OR 1.171 [0.977, 1.403] | 0.1601 | 1.71 | 0.087 | not applied (n < 1000) | 0.323 | -1.0 | -1.2 | 0.6033 | 0.5990 |
| Nocturnal mean 00-06h (mg/dL) | 551 | OR 1.164 [0.969, 1.398] | 0.003399 | 1.62 | 0.105 | not applied (n < 1000) | 0.337 | -0.7 | -0.9 | 0.6038 | 0.5990 |
| Glucose SD, pooled (mg/dL) | 551 | OR 1.194 [0.993, 1.436] | 0.01424 | 1.88 | 0.060 | not applied (n < 1000) | 0.289 | -1.6 | -1.8 | 0.6031 | 0.5990 |
| Avg. daily SD (mg/dL) | 551 | OR 1.169 [0.974, 1.404] | 0.01445 | 1.68 | 0.093 | not applied (n < 1000) | 0.327 | -0.9 | -1.1 | 0.6028 | 0.5990 |
| CV (%) | 551 | OR 1.051 [0.879, 1.257] | 0.00895 | 0.54 | 0.587 | not applied (n < 1000) | 0.815 | +1.7 | +1.5 | 0.5960 | 0.5990 |
| Mean / SD ratio | 551 | OR 0.948 [0.794, 1.132] | -0.05418 | -0.59 | 0.556 | not applied (n < 1000) | 0.803 | +1.7 | +1.5 | 0.5971 | 0.5990 |
| Avg. daily mean / SD | 551 | OR 0.996 [0.835, 1.188] | -0.003255 | -0.04 | 0.965 | not applied (n < 1000) | 0.986 | +2.0 | +1.8 | 0.5952 | 0.5990 |
| MAG (mg/dL/h) | 551 | OR 1.265 [1.047, 1.528] | 0.0238 | 2.44 | 0.015* | not applied (n < 1000) | 0.164 | -4.2 | -4.4 | 0.6059 | 0.5990 |
| Avg. daily range (mg/dL) | 551 | OR 1.170 [0.974, 1.405] | 0.004289 | 1.68 | 0.093 | not applied (n < 1000) | 0.327 | -0.9 | -1.1 | 0.6031 | 0.5990 |
| SD of daily means (mg/dL) | 551 | OR 1.242 [1.025, 1.505] | 0.02443 | 2.21 | 0.027* | not applied (n < 1000) | 0.244 | -3.1 | -3.3 | 0.6069 | 0.5990 |
| Time in range 70-180, pooled (%) | 551 | OR 0.838 [0.700, 1.003] | -0.006802 | -1.92 | 0.055 | not applied (n < 1000) | 0.289 | -1.7 | -1.9 | 0.6052 | 0.5990 |
| Avg. daily time in range 70-180 (%) | 551 | OR 0.838 [0.699, 1.004] | -0.006746 | -1.92 | 0.055 | not applied (n < 1000) | 0.289 | -1.7 | -1.9 | 0.6049 | 0.5990 |
| Any reading < 54 during wear (0/1) | 551 | OR 0.998 [0.837, 1.190] | -0.004561 | -0.02 | 0.983 | not applied (n < 1000) | 0.992 | +2.0 | +1.8 | 0.5956 | 0.5990 |
| Time < 54, pooled (%) | 551 | OR 1.036 [0.870, 1.235] | 0.1418 | 0.40 | 0.689 | not applied (n < 1000) | 0.850 | +1.8 | +1.6 | 0.5934 | 0.5990 |
| Avg. daily time < 54 (%) | 551 | OR 1.049 [0.874, 1.260] | 0.1385 | 0.51 | 0.607 | not applied (n < 1000) | 0.823 | +1.7 | +1.5 | 0.5959 | 0.5990 |
| Time 54-69, pooled (%) | 551 | OR 1.111 [0.925, 1.334] | 0.1165 | 1.12 | 0.262 | not applied (n < 1000) | 0.535 | +0.7 | +0.5 | 0.5956 | 0.5990 |
| Avg. daily time 54-69 (%) | 551 | OR 1.137 [0.940, 1.375] | 0.1358 | 1.32 | 0.187 | not applied (n < 1000) | 0.419 | +0.1 | -0.1 | 0.5967 | 0.5990 |
| Time < 70, pooled (%) | 551 | OR 1.101 [0.918, 1.320] | 0.09018 | 1.04 | 0.298 | not applied (n < 1000) | 0.567 | +0.9 | +0.7 | 0.5960 | 0.5990 |
| Avg. daily time < 70 (%) | 551 | OR 1.124 [0.927, 1.363] | 0.09792 | 1.19 | 0.236 | not applied (n < 1000) | 0.503 | +0.5 | +0.3 | 0.5968 | 0.5990 |
| Time 54-250, pooled (%) | 551 | OR 0.835 [0.693, 1.006] | -0.009758 | -1.89 | 0.058 | not applied (n < 1000) | 0.289 | -1.7 | -1.9 | 0.6039 | 0.5990 |
| Avg. daily time 54-250 (%) | 551 | OR 0.840 [0.697, 1.011] | -0.009576 | -1.84 | 0.065 | not applied (n < 1000) | 0.289 | -1.5 | -1.7 | 0.6039 | 0.5990 |
| Time 181-250, pooled (%) | 551 | OR 1.087 [0.911, 1.296] | 0.005678 | 0.93 | 0.354 | not applied (n < 1000) | 0.628 | +1.1 | +0.9 | 0.5991 | 0.5990 |
| Avg. daily time 181-250 (%) | 551 | OR 1.094 [0.917, 1.305] | 0.005982 | 1.00 | 0.320 | not applied (n < 1000) | 0.594 | +1.0 | +0.8 | 0.5988 | 0.5990 |
| Time > 180, pooled (%) | 551 | OR 1.187 [0.991, 1.421] | 0.006546 | 1.87 | 0.062 | not applied (n < 1000) | 0.289 | -1.5 | -1.7 | 0.6041 | 0.5990 |
| Avg. daily time > 180 (%) | 551 | OR 1.186 [0.990, 1.420] | 0.006461 | 1.85 | 0.064 | not applied (n < 1000) | 0.289 | -1.5 | -1.7 | 0.6038 | 0.5990 |
| Nocturnal time > 180 (%) | 551 | OR 1.199 [0.998, 1.441] | 0.006025 | 1.94 | 0.052 | not applied (n < 1000) | 0.289 | -1.8 | -2.0 | 0.6057 | 0.5990 |
| Time > 250, pooled (%) | 551 | OR 1.197 [0.993, 1.441] | 0.009722 | 1.89 | 0.059 | not applied (n < 1000) | 0.289 | -1.7 | -1.9 | 0.6041 | 0.5990 |
| Avg. daily time > 250 (%) | 551 | OR 1.190 [0.988, 1.433] | 0.00952 | 1.83 | 0.067 | not applied (n < 1000) | 0.289 | -1.5 | -1.7 | 0.6040 | 0.5990 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### MoCA memory index score (0-15)
*n = 551; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 551 | -0.083 [-0.306, +0.140] | -0.06035 | -0.73 | 0.463 | not applied (n < 1000) | 0.746 | +1.6 | +0.0 | 0.0152 | 0.0168 |
| Mean glucose (mg/dL) | 551 | -0.041 [-0.268, +0.186] | -0.0009991 | -0.36 | 0.722 | not applied (n < 1000) | 0.853 | +1.9 | +0.3 | 0.0153 | 0.0168 |
| GMI (%) | 551 | -0.041 [-0.268, +0.186] | -0.04177 | -0.36 | 0.722 | not applied (n < 1000) | 0.853 | +1.9 | +0.3 | 0.0153 | 0.0168 |
| Nocturnal mean 00-06h (mg/dL) | 551 | -0.076 [-0.306, +0.153] | -0.001713 | -0.65 | 0.514 | not applied (n < 1000) | 0.794 | +1.6 | +0.1 | 0.0155 | 0.0168 |
| Glucose SD, pooled (mg/dL) | 551 | -0.201 [-0.444, +0.042] | -0.01617 | -1.62 | 0.105 | not applied (n < 1000) | 0.337 | -0.6 | -2.2 | 0.0173 | 0.0168 |
| Avg. daily SD (mg/dL) | 551 | -0.177 [-0.415, +0.062] | -0.01634 | -1.45 | 0.146 | not applied (n < 1000) | 0.382 | -0.0 | -1.6 | 0.0169 | 0.0168 |
| CV (%) | 551 | -0.207 [-0.435, +0.022] | -0.03728 | -1.77 | 0.076 | not applied (n < 1000) | 0.315 | -0.8 | -2.4 | 0.0165 | 0.0168 |
| Mean / SD ratio | 551 | +0.166 [-0.070, +0.403] | 0.1696 | 1.38 | 0.168 | not applied (n < 1000) | 0.402 | +0.1 | -1.4 | 0.0163 | 0.0168 |
| Avg. daily mean / SD | 551 | +0.103 [-0.159, +0.365] | 0.08479 | 0.77 | 0.442 | not applied (n < 1000) | 0.731 | +1.3 | -0.3 | 0.0135 | 0.0168 |
| MAG (mg/dL/h) | 551 | -0.133 [-0.386, +0.120] | -0.01347 | -1.03 | 0.303 | not applied (n < 1000) | 0.570 | +0.9 | -0.7 | 0.0181 | 0.0168 |
| Avg. daily range (mg/dL) | 551 | -0.169 [-0.420, +0.083] | -0.004613 | -1.31 | 0.189 | not applied (n < 1000) | 0.423 | +0.2 | -1.4 | 0.0165 | 0.0168 |
| SD of daily means (mg/dL) | 551 | -0.181 [-0.456, +0.093] | -0.02043 | -1.29 | 0.196 | not applied (n < 1000) | 0.433 | -0.1 | -1.6 | 0.0156 | 0.0168 |
| Time in range 70-180, pooled (%) | 551 | +0.062 [-0.174, +0.297] | 0.002374 | 0.51 | 0.607 | not applied (n < 1000) | 0.823 | +1.8 | +0.2 | 0.0153 | 0.0168 |
| Avg. daily time in range 70-180 (%) | 551 | +0.061 [-0.176, +0.298] | 0.002327 | 0.50 | 0.614 | not applied (n < 1000) | 0.823 | +1.8 | +0.2 | 0.0154 | 0.0168 |
| Any reading < 54 during wear (0/1) | 551 | -0.100 [-0.340, +0.140] | -0.2432 | -0.82 | 0.414 | not applied (n < 1000) | 0.704 | +1.3 | -0.2 | 0.0138 | 0.0168 |
| Time < 54, pooled (%) | 551 | -0.100 [-0.359, +0.160] | -0.3951 | -0.75 | 0.451 | not applied (n < 1000) | 0.735 | +1.3 | -0.2 | 0.0138 | 0.0168 |
| Avg. daily time < 54 (%) | 551 | -0.144 [-0.353, +0.066] | -0.4143 | -1.35 | 0.178 | not applied (n < 1000) | 0.412 | +0.6 | -1.0 | 0.0166 | 0.0168 |
| Time 54-69, pooled (%) | 551 | -0.233 [-0.477, +0.010] | -0.2594 | -1.88 | 0.060 | not applied (n < 1000) | 0.289 | -1.7 | -3.2 | 0.0195 | 0.0168 |
| Avg. daily time 54-69 (%) | 551 | -0.298 [-0.511, -0.084] | -0.3153 | -2.74 | 0.006** | not applied (n < 1000) | 0.107 | -4.0 | -5.5 | 0.0250 | 0.0168 |
| Time < 70, pooled (%) | 551 | -0.221 [-0.455, +0.012] | -0.2067 | -1.86 | 0.063 | not applied (n < 1000) | 0.289 | -1.3 | -2.8 | 0.0186 | 0.0168 |
| Avg. daily time < 70 (%) | 551 | -0.278 [-0.469, -0.088] | -0.2335 | -2.86 | 0.004** | not applied (n < 1000) | 0.099 | -3.2 | -4.8 | 0.0233 | 0.0168 |
| Time 54-250, pooled (%) | 551 | +0.081 [-0.132, +0.295] | 0.004404 | 0.75 | 0.455 | not applied (n < 1000) | 0.738 | +1.6 | +0.0 | 0.0162 | 0.0168 |
| Avg. daily time 54-250 (%) | 551 | +0.072 [-0.139, +0.283] | 0.00395 | 0.67 | 0.502 | not applied (n < 1000) | 0.787 | +1.7 | +0.1 | 0.0162 | 0.0168 |
| Time 181-250, pooled (%) | 551 | +0.007 [-0.234, +0.248] | 0.0004475 | 0.05 | 0.957 | not applied (n < 1000) | 0.981 | +2.0 | +0.4 | 0.0140 | 0.0168 |
| Avg. daily time 181-250 (%) | 551 | +0.000 [-0.243, +0.243] | 1.143e-05 | 0.00 | 0.999 | not applied (n < 1000) | 1.000 | +2.0 | +0.4 | 0.0141 | 0.0168 |
| Time > 180, pooled (%) | 551 | -0.052 [-0.287, +0.183] | -0.001985 | -0.43 | 0.665 | not applied (n < 1000) | 0.847 | +1.8 | +0.3 | 0.0152 | 0.0168 |
| Avg. daily time > 180 (%) | 551 | -0.048 [-0.284, +0.189] | -0.001806 | -0.39 | 0.693 | not applied (n < 1000) | 0.851 | +1.9 | +0.3 | 0.0153 | 0.0168 |
| Nocturnal time > 180 (%) | 551 | -0.093 [-0.331, +0.146] | -0.003068 | -0.76 | 0.446 | not applied (n < 1000) | 0.732 | +1.5 | -0.1 | 0.0156 | 0.0168 |
| Time > 250, pooled (%) | 551 | -0.080 [-0.293, +0.133] | -0.004324 | -0.73 | 0.463 | not applied (n < 1000) | 0.746 | +1.6 | +0.0 | 0.0162 | 0.0168 |
| Avg. daily time > 250 (%) | 551 | -0.069 [-0.280, +0.141] | -0.003793 | -0.64 | 0.519 | not applied (n < 1000) | 0.797 | +1.7 | +0.1 | 0.0162 | 0.0168 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### CES-D-10 depressive symptoms (0-30)
*n = 550; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 550 | +0.485 [-0.001, +0.970] | 0.3505 | 1.96 | 0.050 | not applied (n < 1000) | 0.289 | -3.1 | +0.0 | 0.0824 | 0.0804 |
| Mean glucose (mg/dL) | 550 | +0.283 [-0.189, +0.754] | 0.006853 | 1.18 | 0.240 | not applied (n < 1000) | 0.506 | +0.2 | +3.4 | 0.0809 | 0.0804 |
| GMI (%) | 550 | +0.283 [-0.189, +0.754] | 0.2865 | 1.18 | 0.240 | not applied (n < 1000) | 0.506 | +0.2 | +3.4 | 0.0809 | 0.0804 |
| Nocturnal mean 00-06h (mg/dL) | 550 | +0.337 [-0.127, +0.802] | 0.007555 | 1.42 | 0.155 | not applied (n < 1000) | 0.389 | -0.5 | +2.7 | 0.0810 | 0.0804 |
| Glucose SD, pooled (mg/dL) | 550 | +0.546 [+0.114, +0.977] | 0.04386 | 2.48 | 0.013* | not applied (n < 1000) | 0.158 | -4.5 | -1.4 | 0.0868 | 0.0804 |
| Avg. daily SD (mg/dL) | 550 | +0.402 [-0.030, +0.834] | 0.03711 | 1.82 | 0.068 | not applied (n < 1000) | 0.289 | -1.6 | +1.6 | 0.0819 | 0.0804 |
| CV (%) | 550 | +0.365 [-0.063, +0.793] | 0.06591 | 1.67 | 0.095 | not applied (n < 1000) | 0.328 | -1.0 | +2.2 | 0.0827 | 0.0804 |
| Mean / SD ratio | 550 | -0.402 [-0.831, +0.026] | -0.41 | -1.84 | 0.066 | not applied (n < 1000) | 0.289 | -1.7 | +1.5 | 0.0828 | 0.0804 |
| Avg. daily mean / SD | 550 | -0.238 [-0.658, +0.183] | -0.1958 | -1.11 | 0.268 | not applied (n < 1000) | 0.538 | +0.7 | +3.9 | 0.0782 | 0.0804 |
| MAG (mg/dL/h) | 550 | +0.632 [+0.175, +1.089] | 0.06405 | 2.71 | 0.007** | not applied (n < 1000) | 0.107 | -6.8 | -3.7 | 0.0898 | 0.0804 |
| Avg. daily range (mg/dL) | 550 | +0.363 [-0.073, +0.799] | 0.009916 | 1.63 | 0.103 | not applied (n < 1000) | 0.337 | -0.9 | +2.3 | 0.0802 | 0.0804 |
| SD of daily means (mg/dL) | 550 | +0.793 [+0.360, +1.226] | 0.08936 | 3.59 | 3.3e-04*** | not applied (n < 1000) | 0.034 (q<0.05) | -11.7 | -8.5 | 0.0977 | 0.0804 |
| Time in range 70-180, pooled (%) | 550 | -0.359 [-0.804, +0.085] | -0.01381 | -1.59 | 0.113 | not applied (n < 1000) | 0.348 | -0.8 | +2.3 | 0.0825 | 0.0804 |
| Avg. daily time in range 70-180 (%) | 550 | -0.338 [-0.785, +0.109] | -0.01286 | -1.48 | 0.139 | not applied (n < 1000) | 0.379 | -0.5 | +2.6 | 0.0819 | 0.0804 |
| Any reading < 54 during wear (0/1) | 550 | +0.357 [-0.058, +0.771] | 0.868 | 1.69 | 0.092 | not applied (n < 1000) | 0.327 | -0.9 | +2.2 | 0.0833 | 0.0804 |
| Time < 54, pooled (%) | 550 | +0.176 [-0.307, +0.660] | 0.6991 | 0.72 | 0.474 | not applied (n < 1000) | 0.752 | +1.3 | +4.4 | 0.0793 | 0.0804 |
| Avg. daily time < 54 (%) | 550 | +0.251 [-0.395, +0.897] | 0.7242 | 0.76 | 0.446 | not applied (n < 1000) | 0.732 | +0.5 | +3.7 | 0.0795 | 0.0804 |
| Time 54-69, pooled (%) | 550 | +0.389 [-0.079, +0.857] | 0.4327 | 1.63 | 0.104 | not applied (n < 1000) | 0.337 | -1.4 | +1.7 | 0.0842 | 0.0804 |
| Avg. daily time 54-69 (%) | 550 | +0.468 [+0.067, +0.869] | 0.4969 | 2.29 | 0.022* | not applied (n < 1000) | 0.221 | -3.0 | +0.2 | 0.0876 | 0.0804 |
| Time < 70, pooled (%) | 550 | +0.371 [-0.082, +0.824] | 0.3467 | 1.60 | 0.109 | not applied (n < 1000) | 0.344 | -1.1 | +2.0 | 0.0831 | 0.0804 |
| Avg. daily time < 70 (%) | 550 | +0.445 [+0.064, +0.826] | 0.3737 | 2.29 | 0.022* | not applied (n < 1000) | 0.221 | -2.5 | +0.6 | 0.0856 | 0.0804 |
| Time 54-250, pooled (%) | 550 | -0.357 [-0.870, +0.157] | -0.01932 | -1.36 | 0.174 | not applied (n < 1000) | 0.410 | -0.8 | +2.3 | 0.0810 | 0.0804 |
| Avg. daily time 54-250 (%) | 550 | -0.324 [-0.842, +0.194] | -0.01771 | -1.23 | 0.220 | not applied (n < 1000) | 0.485 | -0.3 | +2.8 | 0.0802 | 0.0804 |
| Time 181-250, pooled (%) | 550 | +0.162 [-0.243, +0.567] | 0.01106 | 0.79 | 0.432 | not applied (n < 1000) | 0.726 | +1.4 | +4.5 | 0.0765 | 0.0804 |
| Avg. daily time 181-250 (%) | 550 | +0.162 [-0.245, +0.569] | 0.01081 | 0.78 | 0.435 | not applied (n < 1000) | 0.728 | +1.4 | +4.5 | 0.0767 | 0.0804 |
| Time > 180, pooled (%) | 550 | +0.341 [-0.103, +0.785] | 0.01302 | 1.51 | 0.132 | not applied (n < 1000) | 0.375 | -0.6 | +2.6 | 0.0820 | 0.0804 |
| Avg. daily time > 180 (%) | 550 | +0.314 [-0.132, +0.761] | 0.01191 | 1.38 | 0.167 | not applied (n < 1000) | 0.402 | -0.2 | +3.0 | 0.0814 | 0.0804 |
| Nocturnal time > 180 (%) | 550 | +0.395 [-0.049, +0.839] | 0.01308 | 1.74 | 0.081 | not applied (n < 1000) | 0.320 | -1.3 | +1.8 | 0.0814 | 0.0804 |
| Time > 250, pooled (%) | 550 | +0.354 [-0.159, +0.867] | 0.01917 | 1.35 | 0.177 | not applied (n < 1000) | 0.411 | -0.7 | +2.4 | 0.0810 | 0.0804 |
| Avg. daily time > 250 (%) | 550 | +0.319 [-0.198, +0.836] | 0.01743 | 1.21 | 0.227 | not applied (n < 1000) | 0.492 | -0.2 | +2.9 | 0.0801 | 0.0804 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Clinically relevant depressive symptoms (CES-D-10 >= 10)
*n = 550; events = 118; logistic (Wald)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 550 | OR 1.265 [1.040, 1.539] | 0.1702 | 2.36 | 0.019* | not applied (n < 1000) | 0.194 | -3.4 | +0.0 | 0.6637 | 0.6501 |
| Mean glucose (mg/dL) | 550 | OR 1.151 [0.943, 1.406] | 0.003413 | 1.38 | 0.167 | not applied (n < 1000) | 0.402 | +0.1 | +3.6 | 0.6538 | 0.6501 |
| GMI (%) | 550 | OR 1.151 [0.943, 1.406] | 0.1427 | 1.38 | 0.167 | not applied (n < 1000) | 0.402 | +0.1 | +3.6 | 0.6538 | 0.6501 |
| Nocturnal mean 00-06h (mg/dL) | 550 | OR 1.221 [0.999, 1.492] | 0.004469 | 1.95 | 0.052 | not applied (n < 1000) | 0.289 | -1.7 | +1.7 | 0.6579 | 0.6501 |
| Glucose SD, pooled (mg/dL) | 550 | OR 1.385 [1.119, 1.713] | 0.02614 | 3.00 | 0.003** | not applied (n < 1000) | 0.077 | -7.0 | -3.6 | 0.6699 | 0.6501 |
| Avg. daily SD (mg/dL) | 550 | OR 1.271 [1.030, 1.570] | 0.02218 | 2.23 | 0.025* | not applied (n < 1000) | 0.243 | -3.0 | +0.5 | 0.6610 | 0.6501 |
| CV (%) | 550 | OR 1.252 [1.009, 1.554] | 0.04061 | 2.04 | 0.041* | not applied (n < 1000) | 0.289 | -2.2 | +1.3 | 0.6533 | 0.6501 |
| Mean / SD ratio | 550 | OR 0.809 [0.644, 1.017] | -0.2158 | -1.82 | 0.069 | not applied (n < 1000) | 0.290 | -1.5 | +2.0 | 0.6489 | 0.6501 |
| Avg. daily mean / SD | 550 | OR 0.910 [0.732, 1.133] | -0.07732 | -0.84 | 0.400 | not applied (n < 1000) | 0.689 | +1.3 | +4.7 | 0.6437 | 0.6501 |
| MAG (mg/dL/h) | 550 | OR 1.297 [1.054, 1.597] | 0.02639 | 2.46 | 0.014* | not applied (n < 1000) | 0.164 | -4.0 | -0.6 | 0.6559 | 0.6501 |
| Avg. daily range (mg/dL) | 550 | OR 1.270 [1.025, 1.573] | 0.006523 | 2.19 | 0.029* | not applied (n < 1000) | 0.244 | -2.8 | +0.7 | 0.6597 | 0.6501 |
| SD of daily means (mg/dL) | 550 | OR 1.550 [1.256, 1.913] | 0.04939 | 4.09 | 4.4e-05*** | not applied (n < 1000) | 0.006 (q<0.05) | -15.0 | -11.6 | 0.6878 | 0.6501 |
| Time in range 70-180, pooled (%) | 550 | OR 0.829 [0.674, 1.020] | -0.007208 | -1.77 | 0.077 | not applied (n < 1000) | 0.315 | -1.1 | +2.3 | 0.6584 | 0.6501 |
| Avg. daily time in range 70-180 (%) | 550 | OR 0.838 [0.681, 1.033] | -0.006713 | -1.66 | 0.098 | not applied (n < 1000) | 0.331 | -0.7 | +2.7 | 0.6576 | 0.6501 |
| Any reading < 54 during wear (0/1) | 550 | OR 1.253 [1.025, 1.530] | 0.5481 | 2.20 | 0.028* | not applied (n < 1000) | 0.244 | -2.7 | +0.7 | 0.6617 | 0.6501 |
| Time < 54, pooled (%) | 550 | OR 1.124 [0.927, 1.363] | 0.4642 | 1.19 | 0.233 | not applied (n < 1000) | 0.500 | +0.6 | +4.0 | 0.6527 | 0.6501 |
| Avg. daily time < 54 (%) | 550 | OR 1.142 [0.913, 1.428] | 0.3815 | 1.16 | 0.246 | not applied (n < 1000) | 0.517 | +0.2 | +3.7 | 0.6513 | 0.6501 |
| Time 54-69, pooled (%) | 550 | OR 1.179 [0.974, 1.427] | 0.1833 | 1.69 | 0.090 | not applied (n < 1000) | 0.327 | -0.7 | +2.7 | 0.6536 | 0.6501 |
| Avg. daily time 54-69 (%) | 550 | OR 1.215 [1.003, 1.472] | 0.207 | 1.99 | 0.046* | not applied (n < 1000) | 0.289 | -1.9 | +1.6 | 0.6549 | 0.6501 |
| Time < 70, pooled (%) | 550 | OR 1.183 [0.977, 1.433] | 0.1572 | 1.72 | 0.086 | not applied (n < 1000) | 0.323 | -0.8 | +2.6 | 0.6549 | 0.6501 |
| Avg. daily time < 70 (%) | 550 | OR 1.217 [0.991, 1.494] | 0.1649 | 1.88 | 0.060 | not applied (n < 1000) | 0.289 | -1.8 | +1.7 | 0.6540 | 0.6501 |
| Time 54-250, pooled (%) | 550 | OR 0.889 [0.734, 1.076] | -0.0064 | -1.21 | 0.226 | not applied (n < 1000) | 0.492 | +0.6 | +4.0 | 0.6521 | 0.6501 |
| Avg. daily time 54-250 (%) | 550 | OR 0.907 [0.749, 1.100] | -0.005315 | -0.99 | 0.322 | not applied (n < 1000) | 0.596 | +1.0 | +4.5 | 0.6505 | 0.6501 |
| Time 181-250, pooled (%) | 550 | OR 1.172 [0.946, 1.453] | 0.01084 | 1.45 | 0.147 | not applied (n < 1000) | 0.382 | -0.1 | +3.4 | 0.6520 | 0.6501 |
| Avg. daily time 181-250 (%) | 550 | OR 1.182 [0.953, 1.466] | 0.01114 | 1.52 | 0.129 | not applied (n < 1000) | 0.371 | -0.3 | +3.2 | 0.6531 | 0.6501 |
| Time > 180, pooled (%) | 550 | OR 1.196 [0.972, 1.471] | 0.006825 | 1.69 | 0.091 | not applied (n < 1000) | 0.327 | -0.8 | +2.6 | 0.6580 | 0.6501 |
| Avg. daily time > 180 (%) | 550 | OR 1.180 [0.958, 1.453] | 0.006257 | 1.55 | 0.121 | not applied (n < 1000) | 0.362 | -0.4 | +3.1 | 0.6567 | 0.6501 |
| Nocturnal time > 180 (%) | 550 | OR 1.270 [1.031, 1.566] | 0.007922 | 2.24 | 0.025* | not applied (n < 1000) | 0.243 | -2.9 | +0.5 | 0.6588 | 0.6501 |
| Time > 250, pooled (%) | 550 | OR 1.124 [0.928, 1.361] | 0.006312 | 1.19 | 0.233 | not applied (n < 1000) | 0.500 | +0.6 | +4.1 | 0.6521 | 0.6501 |
| Avg. daily time > 250 (%) | 550 | OR 1.099 [0.907, 1.332] | 0.005173 | 0.96 | 0.336 | not applied (n < 1000) | 0.611 | +1.1 | +4.5 | 0.6504 | 0.6501 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor PM2.5, log(1 + mean ug/m3)
*n = 542; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 542 | +0.134 [+0.025, +0.243] | 0.09671 | 2.42 | 0.016* | not applied (n < 1000) | 0.167 | -8.9 | +0.0 | 0.1505 | 0.1470 |
| Mean glucose (mg/dL) | 542 | +0.091 [-0.005, +0.187] | 0.002202 | 1.86 | 0.063 | not applied (n < 1000) | 0.289 | -3.1 | +5.8 | 0.1482 | 0.1470 |
| GMI (%) | 542 | +0.091 [-0.005, +0.187] | 0.09207 | 1.86 | 0.063 | not applied (n < 1000) | 0.289 | -3.1 | +5.8 | 0.1482 | 0.1470 |
| Nocturnal mean 00-06h (mg/dL) | 542 | +0.122 [+0.026, +0.218] | 0.00273 | 2.49 | 0.013* | not applied (n < 1000) | 0.158 | -6.8 | +2.1 | 0.1559 | 0.1470 |
| Glucose SD, pooled (mg/dL) | 542 | +0.070 [-0.008, +0.148] | 0.005637 | 1.75 | 0.079 | not applied (n < 1000) | 0.320 | -0.9 | +8.0 | 0.1523 | 0.1470 |
| Avg. daily SD (mg/dL) | 542 | +0.037 [-0.040, +0.113] | 0.003385 | 0.93 | 0.351 | not applied (n < 1000) | 0.626 | +1.2 | +10.1 | 0.1478 | 0.1470 |
| CV (%) | 542 | +0.008 [-0.079, +0.095] | 0.001388 | 0.17 | 0.862 | not applied (n < 1000) | 0.923 | +2.0 | +10.9 | 0.1459 | 0.1470 |
| Mean / SD ratio | 542 | -0.004 [-0.092, +0.083] | -0.004458 | -0.10 | 0.921 | not applied (n < 1000) | 0.958 | +2.0 | +10.9 | 0.1441 | 0.1470 |
| Avg. daily mean / SD | 542 | +0.027 [-0.065, +0.120] | 0.02247 | 0.58 | 0.562 | not applied (n < 1000) | 0.803 | +1.5 | +10.4 | 0.1424 | 0.1470 |
| MAG (mg/dL/h) | 542 | +0.007 [-0.073, +0.088] | 0.0007514 | 0.18 | 0.857 | not applied (n < 1000) | 0.920 | +2.0 | +10.9 | 0.1447 | 0.1470 |
| Avg. daily range (mg/dL) | 542 | +0.026 [-0.051, +0.102] | 0.0007002 | 0.66 | 0.512 | not applied (n < 1000) | 0.794 | +1.6 | +10.5 | 0.1464 | 0.1470 |
| SD of daily means (mg/dL) | 542 | +0.142 [+0.056, +0.229] | 0.01607 | 3.24 | 0.001** | not applied (n < 1000) | 0.053 | -10.1 | -1.2 | 0.1656 | 0.1470 |
| Time in range 70-180, pooled (%) | 542 | -0.095 [-0.185, -0.005] | -0.003642 | -2.06 | 0.039* | not applied (n < 1000) | 0.289 | -3.5 | +5.4 | 0.1506 | 0.1470 |
| Avg. daily time in range 70-180 (%) | 542 | -0.094 [-0.184, -0.004] | -0.003584 | -2.05 | 0.040* | not applied (n < 1000) | 0.289 | -3.4 | +5.5 | 0.1509 | 0.1470 |
| Any reading < 54 during wear (0/1) | 542 | +0.043 [-0.041, +0.127] | 0.1034 | 1.00 | 0.319 | not applied (n < 1000) | 0.594 | +0.8 | +9.7 | 0.1459 | 0.1470 |
| Time < 54, pooled (%) | 542 | +0.081 [-0.068, +0.230] | 0.3179 | 1.06 | 0.288 | not applied (n < 1000) | 0.557 | -2.1 | +6.8 | 0.1399 | 0.1470 |
| Avg. daily time < 54 (%) | 542 | +0.072 [-0.317, +0.461] | 0.2053 | 0.36 | 0.718 | not applied (n < 1000) | 0.853 | -1.3 | +7.6 | 0.0856 | 0.1470 |
| Time 54-69, pooled (%) | 542 | +0.053 [-0.052, +0.158] | 0.05818 | 0.99 | 0.324 | not applied (n < 1000) | 0.596 | +0.2 | +9.1 | 0.1478 | 0.1470 |
| Avg. daily time 54-69 (%) | 542 | +0.060 [-0.046, +0.167] | 0.06324 | 1.11 | 0.269 | not applied (n < 1000) | 0.538 | -0.3 | +8.6 | 0.1467 | 0.1470 |
| Time < 70, pooled (%) | 542 | +0.064 [-0.047, +0.174] | 0.05918 | 1.13 | 0.258 | not applied (n < 1000) | 0.534 | -0.5 | +8.4 | 0.1477 | 0.1470 |
| Avg. daily time < 70 (%) | 542 | +0.069 [-0.059, +0.197] | 0.0574 | 1.05 | 0.292 | not applied (n < 1000) | 0.562 | -1.0 | +7.9 | 0.1423 | 0.1470 |
| Time 54-250, pooled (%) | 542 | -0.079 [-0.183, +0.025] | -0.004267 | -1.48 | 0.138 | not applied (n < 1000) | 0.379 | -1.7 | +7.2 | 0.1420 | 0.1470 |
| Avg. daily time 54-250 (%) | 542 | -0.080 [-0.183, +0.024] | -0.00436 | -1.51 | 0.130 | not applied (n < 1000) | 0.372 | -1.8 | +7.1 | 0.1416 | 0.1470 |
| Time 181-250, pooled (%) | 542 | +0.064 [-0.016, +0.144] | 0.004352 | 1.56 | 0.118 | not applied (n < 1000) | 0.358 | -0.6 | +8.3 | 0.1505 | 0.1470 |
| Avg. daily time 181-250 (%) | 542 | +0.062 [-0.018, +0.141] | 0.004104 | 1.52 | 0.129 | not applied (n < 1000) | 0.371 | -0.4 | +8.5 | 0.1503 | 0.1470 |
| Time > 180, pooled (%) | 542 | +0.091 [+0.001, +0.182] | 0.003484 | 1.98 | 0.048* | not applied (n < 1000) | 0.289 | -3.1 | +5.8 | 0.1501 | 0.1470 |
| Avg. daily time > 180 (%) | 542 | +0.090 [-0.000, +0.180] | 0.003415 | 1.96 | 0.050 | not applied (n < 1000) | 0.289 | -2.9 | +6.0 | 0.1502 | 0.1470 |
| Nocturnal time > 180 (%) | 542 | +0.101 [+0.010, +0.192] | 0.003358 | 2.18 | 0.029* | not applied (n < 1000) | 0.244 | -4.0 | +4.9 | 0.1525 | 0.1470 |
| Time > 250, pooled (%) | 542 | +0.078 [-0.027, +0.182] | 0.0042 | 1.46 | 0.145 | not applied (n < 1000) | 0.382 | -1.6 | +7.3 | 0.1418 | 0.1470 |
| Avg. daily time > 250 (%) | 542 | +0.078 [-0.025, +0.182] | 0.00428 | 1.48 | 0.138 | not applied (n < 1000) | 0.379 | -1.7 | +7.2 | 0.1414 | 0.1470 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor temperature, mean (deg C)
*n = 542; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 542 | -0.017 [-0.272, +0.238] | -0.01229 | -0.13 | 0.896 | not applied (n < 1000) | 0.948 | +2.0 | +0.0 | 0.2167 | 0.2218 |
| Mean glucose (mg/dL) | 542 | -0.048 [-0.240, +0.144] | -0.001159 | -0.49 | 0.626 | not applied (n < 1000) | 0.823 | +1.7 | -0.2 | 0.2177 | 0.2218 |
| GMI (%) | 542 | -0.048 [-0.240, +0.144] | -0.04845 | -0.49 | 0.626 | not applied (n < 1000) | 0.823 | +1.7 | -0.2 | 0.2177 | 0.2218 |
| Nocturnal mean 00-06h (mg/dL) | 542 | -0.028 [-0.228, +0.172] | -0.000629 | -0.27 | 0.784 | not applied (n < 1000) | 0.873 | +1.9 | -0.1 | 0.2174 | 0.2218 |
| Glucose SD, pooled (mg/dL) | 542 | -0.056 [-0.245, +0.133] | -0.004512 | -0.58 | 0.560 | not applied (n < 1000) | 0.803 | +1.6 | -0.3 | 0.2192 | 0.2218 |
| Avg. daily SD (mg/dL) | 542 | -0.079 [-0.259, +0.101] | -0.007311 | -0.86 | 0.391 | not applied (n < 1000) | 0.681 | +1.2 | -0.7 | 0.2198 | 0.2218 |
| CV (%) | 542 | -0.012 [-0.184, +0.160] | -0.002101 | -0.13 | 0.894 | not applied (n < 1000) | 0.948 | +2.0 | +0.0 | 0.2182 | 0.2218 |
| Mean / SD ratio | 542 | -0.027 [-0.196, +0.142] | -0.02739 | -0.31 | 0.754 | not applied (n < 1000) | 0.861 | +1.9 | -0.1 | 0.2185 | 0.2218 |
| Avg. daily mean / SD | 542 | +0.006 [-0.182, +0.193] | 0.004739 | 0.06 | 0.952 | not applied (n < 1000) | 0.980 | +2.0 | +0.0 | 0.2174 | 0.2218 |
| MAG (mg/dL/h) | 542 | -0.053 [-0.228, +0.122] | -0.005353 | -0.60 | 0.551 | not applied (n < 1000) | 0.801 | +1.7 | -0.3 | 0.2195 | 0.2218 |
| Avg. daily range (mg/dL) | 542 | -0.054 [-0.228, +0.120] | -0.00147 | -0.60 | 0.545 | not applied (n < 1000) | 0.798 | +1.6 | -0.3 | 0.2190 | 0.2218 |
| SD of daily means (mg/dL) | 542 | +0.024 [-0.203, +0.250] | 0.002659 | 0.20 | 0.838 | not applied (n < 1000) | 0.903 | +1.9 | -0.0 | 0.2174 | 0.2218 |
| Time in range 70-180, pooled (%) | 542 | +0.050 [-0.142, +0.242] | 0.001925 | 0.51 | 0.608 | not applied (n < 1000) | 0.823 | +1.7 | -0.3 | 0.2180 | 0.2218 |
| Avg. daily time in range 70-180 (%) | 542 | +0.060 [-0.133, +0.253] | 0.002284 | 0.61 | 0.542 | not applied (n < 1000) | 0.798 | +1.6 | -0.4 | 0.2184 | 0.2218 |
| Any reading < 54 during wear (0/1) | 542 | -0.066 [-0.233, +0.102] | -0.1586 | -0.77 | 0.442 | not applied (n < 1000) | 0.731 | +1.4 | -0.5 | 0.2191 | 0.2218 |
| Time < 54, pooled (%) | 542 | -0.044 [-0.186, +0.098] | -0.173 | -0.60 | 0.545 | not applied (n < 1000) | 0.798 | +1.8 | -0.2 | 0.2210 | 0.2218 |
| Avg. daily time < 54 (%) | 542 | -0.061 [-0.225, +0.103] | -0.1739 | -0.73 | 0.467 | not applied (n < 1000) | 0.746 | +1.5 | -0.4 | 0.2204 | 0.2218 |
| Time 54-69, pooled (%) | 542 | +0.039 [-0.161, +0.238] | 0.04267 | 0.38 | 0.704 | not applied (n < 1000) | 0.853 | +1.8 | -0.2 | 0.2179 | 0.2218 |
| Avg. daily time 54-69 (%) | 542 | +0.061 [-0.129, +0.251] | 0.06376 | 0.63 | 0.531 | not applied (n < 1000) | 0.797 | +1.5 | -0.4 | 0.2181 | 0.2218 |
| Time < 70, pooled (%) | 542 | +0.022 [-0.164, +0.208] | 0.02076 | 0.24 | 0.814 | not applied (n < 1000) | 0.887 | +1.9 | -0.0 | 0.2184 | 0.2218 |
| Avg. daily time < 70 (%) | 542 | +0.030 [-0.176, +0.236] | 0.02517 | 0.29 | 0.774 | not applied (n < 1000) | 0.869 | +1.9 | -0.1 | 0.2176 | 0.2218 |
| Time 54-250, pooled (%) | 542 | -0.002 [-0.203, +0.198] | -0.0001211 | -0.02 | 0.983 | not applied (n < 1000) | 0.992 | +2.0 | +0.0 | 0.2172 | 0.2218 |
| Avg. daily time 54-250 (%) | 542 | +0.003 [-0.199, +0.205] | 0.000171 | 0.03 | 0.976 | not applied (n < 1000) | 0.992 | +2.0 | +0.0 | 0.2171 | 0.2218 |
| Time 181-250, pooled (%) | 542 | -0.091 [-0.263, +0.082] | -0.006182 | -1.03 | 0.302 | not applied (n < 1000) | 0.570 | +0.9 | -1.0 | 0.2190 | 0.2218 |
| Avg. daily time 181-250 (%) | 542 | -0.101 [-0.276, +0.073] | -0.006768 | -1.14 | 0.254 | not applied (n < 1000) | 0.527 | +0.7 | -1.3 | 0.2197 | 0.2218 |
| Time > 180, pooled (%) | 542 | -0.051 [-0.242, +0.141] | -0.001932 | -0.52 | 0.604 | not applied (n < 1000) | 0.823 | +1.7 | -0.3 | 0.2179 | 0.2218 |
| Avg. daily time > 180 (%) | 542 | -0.061 [-0.253, +0.131] | -0.002308 | -0.62 | 0.535 | not applied (n < 1000) | 0.798 | +1.5 | -0.4 | 0.2183 | 0.2218 |
| Nocturnal time > 180 (%) | 542 | -0.048 [-0.250, +0.155] | -0.001576 | -0.46 | 0.645 | not applied (n < 1000) | 0.831 | +1.7 | -0.2 | 0.2178 | 0.2218 |
| Time > 250, pooled (%) | 542 | +0.003 [-0.198, +0.203] | 0.0001551 | 0.03 | 0.978 | not applied (n < 1000) | 0.992 | +2.0 | +0.0 | 0.2172 | 0.2218 |
| Avg. daily time > 250 (%) | 542 | -0.002 [-0.204, +0.200] | -0.0001041 | -0.02 | 0.985 | not applied (n < 1000) | 0.992 | +2.0 | +0.0 | 0.2171 | 0.2218 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor relative humidity, mean (%)
*n = 542; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 542 | +0.159 [-0.384, +0.702] | 0.1149 | 0.57 | 0.566 | not applied (n < 1000) | 0.803 | +1.6 | +0.0 | 0.1882 | 0.1926 |
| Mean glucose (mg/dL) | 542 | +0.304 [-0.246, +0.854] | 0.007369 | 1.08 | 0.278 | not applied (n < 1000) | 0.546 | +0.7 | -1.0 | 0.1930 | 0.1926 |
| GMI (%) | 542 | +0.304 [-0.246, +0.854] | 0.3081 | 1.08 | 0.278 | not applied (n < 1000) | 0.546 | +0.7 | -1.0 | 0.1930 | 0.1926 |
| Nocturnal mean 00-06h (mg/dL) | 542 | +0.195 [-0.343, +0.733] | 0.004381 | 0.71 | 0.477 | not applied (n < 1000) | 0.753 | +1.5 | -0.2 | 0.1919 | 0.1926 |
| Glucose SD, pooled (mg/dL) | 542 | +0.144 [-0.382, +0.671] | 0.01163 | 0.54 | 0.591 | not applied (n < 1000) | 0.816 | +1.7 | +0.1 | 0.1904 | 0.1926 |
| Avg. daily SD (mg/dL) | 542 | +0.150 [-0.376, +0.677] | 0.01393 | 0.56 | 0.576 | not applied (n < 1000) | 0.809 | +1.7 | +0.0 | 0.1895 | 0.1926 |
| CV (%) | 542 | -0.128 [-0.659, +0.402] | -0.02303 | -0.47 | 0.635 | not applied (n < 1000) | 0.826 | +1.8 | +0.1 | 0.1908 | 0.1926 |
| Mean / SD ratio | 542 | +0.112 [-0.409, +0.634] | 0.1139 | 0.42 | 0.672 | not applied (n < 1000) | 0.849 | +1.8 | +0.2 | 0.1907 | 0.1926 |
| Avg. daily mean / SD | 542 | +0.099 [-0.452, +0.651] | 0.08141 | 0.35 | 0.724 | not applied (n < 1000) | 0.853 | +1.9 | +0.2 | 0.1890 | 0.1926 |
| MAG (mg/dL/h) | 542 | +0.065 [-0.446, +0.576] | 0.006544 | 0.25 | 0.804 | not applied (n < 1000) | 0.885 | +1.9 | +0.3 | 0.1898 | 0.1926 |
| Avg. daily range (mg/dL) | 542 | +0.097 [-0.416, +0.609] | 0.002641 | 0.37 | 0.712 | not applied (n < 1000) | 0.853 | +1.9 | +0.2 | 0.1887 | 0.1926 |
| SD of daily means (mg/dL) | 542 | +0.064 [-0.469, +0.596] | 0.007178 | 0.23 | 0.815 | not applied (n < 1000) | 0.887 | +1.9 | +0.3 | 0.1906 | 0.1926 |
| Time in range 70-180, pooled (%) | 542 | -0.134 [-0.699, +0.431] | -0.005147 | -0.46 | 0.642 | not applied (n < 1000) | 0.830 | +1.7 | +0.1 | 0.1916 | 0.1926 |
| Avg. daily time in range 70-180 (%) | 542 | -0.143 [-0.708, +0.423] | -0.00543 | -0.49 | 0.621 | not applied (n < 1000) | 0.823 | +1.7 | +0.1 | 0.1917 | 0.1926 |
| Any reading < 54 during wear (0/1) | 542 | +0.163 [-0.363, +0.690] | 0.3943 | 0.61 | 0.543 | not applied (n < 1000) | 0.798 | +1.6 | -0.0 | 0.1863 | 0.1926 |
| Time < 54, pooled (%) | 542 | -0.097 [-0.725, +0.532] | -0.3803 | -0.30 | 0.763 | not applied (n < 1000) | 0.863 | +1.9 | +0.2 | 0.1885 | 0.1926 |
| Avg. daily time < 54 (%) | 542 | -0.063 [-1.097, +0.970] | -0.1804 | -0.12 | 0.905 | not applied (n < 1000) | 0.949 | +1.9 | +0.3 | 0.1845 | 0.1926 |
| Time 54-69, pooled (%) | 542 | -0.133 [-0.809, +0.542] | -0.1471 | -0.39 | 0.699 | not applied (n < 1000) | 0.853 | +1.7 | +0.1 | 0.1909 | 0.1926 |
| Avg. daily time 54-69 (%) | 542 | -0.156 [-0.835, +0.523] | -0.1637 | -0.45 | 0.653 | not applied (n < 1000) | 0.834 | +1.6 | +0.0 | 0.1911 | 0.1926 |
| Time < 70, pooled (%) | 542 | -0.136 [-0.792, +0.521] | -0.126 | -0.41 | 0.685 | not applied (n < 1000) | 0.850 | +1.7 | +0.1 | 0.1906 | 0.1926 |
| Avg. daily time < 70 (%) | 542 | -0.142 [-0.809, +0.524] | -0.1184 | -0.42 | 0.676 | not applied (n < 1000) | 0.849 | +1.7 | +0.1 | 0.1902 | 0.1926 |
| Time 54-250, pooled (%) | 542 | -0.116 [-0.669, +0.438] | -0.006254 | -0.41 | 0.682 | not applied (n < 1000) | 0.850 | +1.8 | +0.2 | 0.1900 | 0.1926 |
| Avg. daily time 54-250 (%) | 542 | -0.114 [-0.675, +0.447] | -0.006239 | -0.40 | 0.690 | not applied (n < 1000) | 0.850 | +1.8 | +0.2 | 0.1898 | 0.1926 |
| Time 181-250, pooled (%) | 542 | +0.098 [-0.448, +0.645] | 0.006686 | 0.35 | 0.725 | not applied (n < 1000) | 0.853 | +1.9 | +0.2 | 0.1883 | 0.1926 |
| Avg. daily time 181-250 (%) | 542 | +0.117 [-0.427, +0.660] | 0.007789 | 0.42 | 0.674 | not applied (n < 1000) | 0.849 | +1.8 | +0.2 | 0.1884 | 0.1926 |
| Time > 180, pooled (%) | 542 | +0.138 [-0.427, +0.704] | 0.005289 | 0.48 | 0.631 | not applied (n < 1000) | 0.826 | +1.7 | +0.1 | 0.1916 | 0.1926 |
| Avg. daily time > 180 (%) | 542 | +0.148 [-0.417, +0.714] | 0.005612 | 0.51 | 0.608 | not applied (n < 1000) | 0.823 | +1.7 | +0.0 | 0.1917 | 0.1926 |
| Nocturnal time > 180 (%) | 542 | -0.059 [-0.618, +0.500] | -0.001946 | -0.21 | 0.837 | not applied (n < 1000) | 0.903 | +2.0 | +0.3 | 0.1909 | 0.1926 |
| Time > 250, pooled (%) | 542 | +0.117 [-0.437, +0.670] | 0.006324 | 0.41 | 0.679 | not applied (n < 1000) | 0.849 | +1.8 | +0.2 | 0.1900 | 0.1926 |
| Avg. daily time > 250 (%) | 542 | +0.115 [-0.446, +0.676] | 0.006305 | 0.40 | 0.687 | not applied (n < 1000) | 0.850 | +1.8 | +0.2 | 0.1899 | 0.1926 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Indoor VOC index, mean
*n = 542; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 542 | -1.878 [-3.545, -0.210] | -1.355 | -2.21 | 0.027* | not applied (n < 1000) | 0.244 | -3.7 | +0.0 | -0.0115 | -0.0184 |
| Mean glucose (mg/dL) | 542 | -1.633 [-3.273, +0.006] | -0.03958 | -1.95 | 0.051 | not applied (n < 1000) | 0.289 | -2.3 | +1.3 | -0.0144 | -0.0184 |
| GMI (%) | 542 | -1.633 [-3.273, +0.006] | -1.655 | -1.95 | 0.051 | not applied (n < 1000) | 0.289 | -2.3 | +1.3 | -0.0144 | -0.0184 |
| Nocturnal mean 00-06h (mg/dL) | 542 | -1.461 [-3.333, +0.412] | -0.03278 | -1.53 | 0.126 | not applied (n < 1000) | 0.371 | -1.4 | +2.3 | -0.0175 | -0.0184 |
| Glucose SD, pooled (mg/dL) | 542 | -1.036 [-2.855, +0.783] | -0.08337 | -1.12 | 0.264 | not applied (n < 1000) | 0.535 | +0.3 | +4.0 | -0.0208 | -0.0184 |
| Avg. daily SD (mg/dL) | 542 | -0.511 [-2.046, +1.024] | -0.04731 | -0.65 | 0.514 | not applied (n < 1000) | 0.794 | +1.6 | +5.3 | -0.0214 | -0.0184 |
| CV (%) | 542 | +0.162 [-1.387, +1.712] | 0.02914 | 0.21 | 0.837 | not applied (n < 1000) | 0.903 | +2.0 | +5.6 | -0.0209 | -0.0184 |
| Mean / SD ratio | 542 | -0.183 [-1.731, +1.366] | -0.185 | -0.23 | 0.817 | not applied (n < 1000) | 0.887 | +1.9 | +5.6 | -0.0210 | -0.0184 |
| Avg. daily mean / SD | 542 | -0.720 [-2.178, +0.738] | -0.5898 | -0.97 | 0.333 | not applied (n < 1000) | 0.608 | +1.1 | +4.8 | -0.0208 | -0.0184 |
| MAG (mg/dL/h) | 542 | +0.105 [-1.609, +1.818] | 0.01054 | 0.12 | 0.905 | not applied (n < 1000) | 0.949 | +2.0 | +5.7 | -0.0247 | -0.0184 |
| Avg. daily range (mg/dL) | 542 | -0.291 [-1.816, +1.233] | -0.00797 | -0.37 | 0.708 | not applied (n < 1000) | 0.853 | +1.9 | +5.5 | -0.0210 | -0.0184 |
| SD of daily means (mg/dL) | 542 | -1.952 [-4.631, +0.727] | -0.2203 | -1.43 | 0.153 | not applied (n < 1000) | 0.389 | -4.0 | -0.4 | -0.0219 | -0.0184 |
| Time in range 70-180, pooled (%) | 542 | +1.458 [-0.184, +3.100] | 0.05604 | 1.74 | 0.082 | not applied (n < 1000) | 0.320 | -1.4 | +2.2 | -0.0155 | -0.0184 |
| Avg. daily time in range 70-180 (%) | 542 | +1.547 [-0.098, +3.193] | 0.05895 | 1.84 | 0.065 | not applied (n < 1000) | 0.289 | -1.9 | +1.8 | -0.0149 | -0.0184 |
| Any reading < 54 during wear (0/1) | 542 | +0.323 [-1.484, +2.129] | 0.7789 | 0.35 | 0.726 | not applied (n < 1000) | 0.853 | +1.8 | +5.5 | -0.0223 | -0.0184 |
| Time < 54, pooled (%) | 542 | +0.201 [-1.112, +1.513] | 0.7908 | 0.30 | 0.764 | not applied (n < 1000) | 0.863 | +1.9 | +5.6 | -0.0217 | -0.0184 |
| Avg. daily time < 54 (%) | 542 | +0.043 [-1.052, +1.138] | 0.1231 | 0.08 | 0.939 | not applied (n < 1000) | 0.969 | +2.0 | +5.7 | -0.0206 | -0.0184 |
| Time 54-69, pooled (%) | 542 | +0.227 [-1.196, +1.650] | 0.2506 | 0.31 | 0.754 | not applied (n < 1000) | 0.861 | +1.9 | +5.6 | -0.0208 | -0.0184 |
| Avg. daily time 54-69 (%) | 542 | -0.056 [-1.390, +1.277] | -0.05928 | -0.08 | 0.934 | not applied (n < 1000) | 0.966 | +2.0 | +5.7 | -0.0218 | -0.0184 |
| Time < 70, pooled (%) | 542 | +0.240 [-1.143, +1.623] | 0.2226 | 0.34 | 0.734 | not applied (n < 1000) | 0.854 | +1.9 | +5.6 | -0.0206 | -0.0184 |
| Avg. daily time < 70 (%) | 542 | -0.032 [-1.211, +1.147] | -0.02671 | -0.05 | 0.957 | not applied (n < 1000) | 0.981 | +2.0 | +5.7 | -0.0215 | -0.0184 |
| Time 54-250, pooled (%) | 542 | +1.697 [+0.000, +3.394] | 0.09178 | 1.96 | 0.050* | not applied (n < 1000) | 0.289 | -2.6 | +1.1 | -0.0129 | -0.0184 |
| Avg. daily time 54-250 (%) | 542 | +1.774 [+0.051, +3.497] | 0.09697 | 2.02 | 0.044* | not applied (n < 1000) | 0.289 | -3.1 | +0.6 | -0.0120 | -0.0184 |
| Time 181-250, pooled (%) | 542 | -0.466 [-2.313, +1.381] | -0.03176 | -0.49 | 0.621 | not applied (n < 1000) | 0.823 | +1.6 | +5.3 | -0.0232 | -0.0184 |
| Avg. daily time 181-250 (%) | 542 | -0.529 [-2.334, +1.276] | -0.03528 | -0.57 | 0.566 | not applied (n < 1000) | 0.803 | +1.5 | +5.2 | -0.0229 | -0.0184 |
| Time > 180, pooled (%) | 542 | -1.456 [-3.095, +0.184] | -0.05558 | -1.74 | 0.082 | not applied (n < 1000) | 0.320 | -1.4 | +2.2 | -0.0155 | -0.0184 |
| Avg. daily time > 180 (%) | 542 | -1.534 [-3.177, +0.110] | -0.05812 | -1.83 | 0.067 | not applied (n < 1000) | 0.289 | -1.8 | +1.9 | -0.0150 | -0.0184 |
| Nocturnal time > 180 (%) | 542 | -0.877 [-2.758, +1.004] | -0.02906 | -0.91 | 0.361 | not applied (n < 1000) | 0.634 | +0.8 | +4.5 | -0.0220 | -0.0184 |
| Time > 250, pooled (%) | 542 | -1.698 [-3.396, -0.001] | -0.09186 | -1.96 | 0.050* | not applied (n < 1000) | 0.289 | -2.6 | +1.0 | -0.0128 | -0.0184 |
| Avg. daily time > 250 (%) | 542 | -1.774 [-3.498, -0.050] | -0.09698 | -2.02 | 0.044* | not applied (n < 1000) | 0.289 | -3.1 | +0.6 | -0.0120 | -0.0184 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Steps per wear-day
*n = 472; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 472 | +200.435 [-299.041, +699.910] | 142.7 | 0.79 | 0.432 | not applied (n < 1000) | 0.726 | +1.3 | +0.0 | 0.1221 | 0.1311 |
| Mean glucose (mg/dL) | 472 | +29.030 [-474.532, +532.592] | 0.6974 | 0.11 | 0.910 | not applied (n < 1000) | 0.949 | +2.0 | +0.7 | 0.1285 | 0.1311 |
| GMI (%) | 472 | +29.030 [-474.532, +532.592] | 29.16 | 0.11 | 0.910 | not applied (n < 1000) | 0.949 | +2.0 | +0.7 | 0.1285 | 0.1311 |
| Nocturnal mean 00-06h (mg/dL) | 472 | +173.395 [-363.443, +710.232] | 3.877 | 0.63 | 0.527 | not applied (n < 1000) | 0.797 | +1.4 | +0.2 | 0.1284 | 0.1311 |
| Glucose SD, pooled (mg/dL) | 472 | -61.931 [-553.152, +429.291] | -4.955 | -0.25 | 0.805 | not applied (n < 1000) | 0.885 | +1.9 | +0.7 | 0.1246 | 0.1311 |
| Avg. daily SD (mg/dL) | 472 | -123.328 [-581.783, +335.127] | -11.38 | -0.53 | 0.598 | not applied (n < 1000) | 0.823 | +1.7 | +0.5 | 0.1257 | 0.1311 |
| CV (%) | 472 | -205.034 [-627.641, +217.572] | -36.44 | -0.95 | 0.342 | not applied (n < 1000) | 0.616 | +1.2 | -0.1 | 0.1260 | 0.1311 |
| Mean / SD ratio | 472 | -18.176 [-425.294, +388.942] | -18.09 | -0.09 | 0.930 | not applied (n < 1000) | 0.965 | +2.0 | +0.7 | 0.1268 | 0.1311 |
| Avg. daily mean / SD | 472 | -49.295 [-445.875, +347.284] | -39.76 | -0.24 | 0.808 | not applied (n < 1000) | 0.886 | +2.0 | +0.7 | 0.1278 | 0.1311 |
| MAG (mg/dL/h) | 472 | +362.889 [-153.383, +879.162] | 36.12 | 1.38 | 0.168 | not applied (n < 1000) | 0.402 | -0.5 | -1.8 | 0.1308 | 0.1311 |
| Avg. daily range (mg/dL) | 472 | -54.159 [-512.295, +403.977] | -1.479 | -0.23 | 0.817 | not applied (n < 1000) | 0.887 | +1.9 | +0.7 | 0.1255 | 0.1311 |
| SD of daily means (mg/dL) | 472 | +226.057 [-294.483, +746.596] | 25.5 | 0.85 | 0.395 | not applied (n < 1000) | 0.682 | +1.0 | -0.2 | 0.1267 | 0.1311 |
| Time in range 70-180, pooled (%) | 472 | -65.101 [-568.362, +438.160] | -2.499 | -0.25 | 0.800 | not applied (n < 1000) | 0.884 | +1.9 | +0.7 | 0.1270 | 0.1311 |
| Avg. daily time in range 70-180 (%) | 472 | -66.034 [-567.143, +435.076] | -2.513 | -0.26 | 0.796 | not applied (n < 1000) | 0.884 | +1.9 | +0.7 | 0.1272 | 0.1311 |
| Any reading < 54 during wear (0/1) | 472 | -386.212 [-847.921, +75.497] | -930.8 | -1.64 | 0.101 | not applied (n < 1000) | 0.336 | -1.0 | -2.2 | 0.1331 | 0.1311 |
| Time < 54, pooled (%) | 472 | -442.032 [-698.459, -185.606] | -1643 | -3.38 | 7.3e-04*** | not applied (n < 1000) | 0.053 | -1.8 | -3.1 | 0.1356 | 0.1311 |
| Avg. daily time < 54 (%) | 472 | -400.045 [-565.794, -234.296] | -1074 | -4.73 | 2.2e-06*** | not applied (n < 1000) | 4.7e-04 (q<0.05) | -1.2 | -2.4 | 0.1359 | 0.1311 |
| Time 54-69, pooled (%) | 472 | -423.153 [-928.168, +81.862] | -477.2 | -1.64 | 0.101 | not applied (n < 1000) | 0.336 | -1.5 | -2.7 | 0.1325 | 0.1311 |
| Avg. daily time 54-69 (%) | 472 | -461.859 [-934.695, +10.978] | -473.4 | -1.91 | 0.056 | not applied (n < 1000) | 0.289 | -2.2 | -3.4 | 0.1338 | 0.1311 |
| Time < 70, pooled (%) | 472 | -463.474 [-921.425, -5.523] | -432 | -1.98 | 0.047* | not applied (n < 1000) | 0.289 | -2.2 | -3.4 | 0.1343 | 0.1311 |
| Avg. daily time < 70 (%) | 472 | -484.019 [-851.308, -116.731] | -389 | -2.58 | 0.010** | not applied (n < 1000) | 0.129 | -2.6 | -3.8 | 0.1360 | 0.1311 |
| Time 54-250, pooled (%) | 472 | +130.385 [-383.483, +644.253] | 6.964 | 0.50 | 0.619 | not applied (n < 1000) | 0.823 | +1.7 | +0.4 | 0.1293 | 0.1311 |
| Avg. daily time 54-250 (%) | 472 | +112.703 [-378.518, +603.925] | 6.096 | 0.45 | 0.653 | not applied (n < 1000) | 0.834 | +1.8 | +0.5 | 0.1294 | 0.1311 |
| Time 181-250, pooled (%) | 472 | +296.365 [-149.686, +742.416] | 20.03 | 1.30 | 0.193 | not applied (n < 1000) | 0.429 | +0.3 | -1.0 | 0.1308 | 0.1311 |
| Avg. daily time 181-250 (%) | 472 | +275.305 [-170.633, +721.244] | 18.2 | 1.21 | 0.226 | not applied (n < 1000) | 0.492 | +0.5 | -0.7 | 0.1302 | 0.1311 |
| Time > 180, pooled (%) | 472 | +83.937 [-418.096, +585.969] | 3.202 | 0.33 | 0.743 | not applied (n < 1000) | 0.861 | +1.9 | +0.6 | 0.1274 | 0.1311 |
| Avg. daily time > 180 (%) | 472 | +89.040 [-411.423, +589.503] | 3.371 | 0.35 | 0.727 | not applied (n < 1000) | 0.853 | +1.9 | +0.6 | 0.1277 | 0.1311 |
| Nocturnal time > 180 (%) | 472 | +165.952 [-353.889, +685.793] | 5.503 | 0.63 | 0.532 | not applied (n < 1000) | 0.797 | +1.5 | +0.3 | 0.1279 | 0.1311 |
| Time > 250, pooled (%) | 472 | -123.714 [-637.755, +390.327] | -6.608 | -0.47 | 0.637 | not applied (n < 1000) | 0.826 | +1.7 | +0.5 | 0.1293 | 0.1311 |
| Avg. daily time > 250 (%) | 472 | -104.179 [-595.657, +387.298] | -5.637 | -0.42 | 0.678 | not applied (n < 1000) | 0.849 | +1.8 | +0.5 | 0.1294 | 0.1311 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Brisk-cadence minutes per day (>= 100 steps/min)
*n = 472; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 472 | +0.709 [-0.626, +2.044] | 0.5048 | 1.04 | 0.298 | not applied (n < 1000) | 0.567 | +0.9 | +0.0 | 0.1406 | 0.1463 |
| Mean glucose (mg/dL) | 472 | +0.112 [-1.266, +1.491] | 0.002702 | 0.16 | 0.873 | not applied (n < 1000) | 0.928 | +2.0 | +1.1 | 0.1437 | 0.1463 |
| GMI (%) | 472 | +0.112 [-1.266, +1.491] | 0.113 | 0.16 | 0.873 | not applied (n < 1000) | 0.928 | +2.0 | +1.1 | 0.1437 | 0.1463 |
| Nocturnal mean 00-06h (mg/dL) | 472 | +0.480 [-1.013, +1.972] | 0.01072 | 0.63 | 0.529 | not applied (n < 1000) | 0.797 | +1.5 | +0.6 | 0.1437 | 0.1463 |
| Glucose SD, pooled (mg/dL) | 472 | +0.241 [-1.150, +1.631] | 0.01926 | 0.34 | 0.734 | not applied (n < 1000) | 0.854 | +1.9 | +1.0 | 0.1406 | 0.1463 |
| Avg. daily SD (mg/dL) | 472 | -0.000 [-1.308, +1.308] | -9.221e-06 | -0.00 | 1.000 | not applied (n < 1000) | 1.000 | +2.0 | +1.1 | 0.1409 | 0.1463 |
| CV (%) | 472 | -0.186 [-1.369, +0.998] | -0.03298 | -0.31 | 0.759 | not applied (n < 1000) | 0.861 | +1.9 | +1.1 | 0.1419 | 0.1463 |
| Mean / SD ratio | 472 | -0.478 [-1.576, +0.619] | -0.476 | -0.85 | 0.393 | not applied (n < 1000) | 0.682 | +1.5 | +0.6 | 0.1441 | 0.1463 |
| Avg. daily mean / SD | 472 | -0.460 [-1.541, +0.622] | -0.3708 | -0.83 | 0.405 | not applied (n < 1000) | 0.694 | +1.5 | +0.6 | 0.1444 | 0.1463 |
| MAG (mg/dL/h) | 472 | +1.275 [-0.179, +2.730] | 0.1269 | 1.72 | 0.086 | not applied (n < 1000) | 0.323 | -1.8 | -2.7 | 0.1483 | 0.1463 |
| Avg. daily range (mg/dL) | 472 | +0.241 [-1.079, +1.561] | 0.006578 | 0.36 | 0.721 | not applied (n < 1000) | 0.853 | +1.9 | +1.0 | 0.1411 | 0.1463 |
| SD of daily means (mg/dL) | 472 | +0.809 [-0.610, +2.228] | 0.09128 | 1.12 | 0.264 | not applied (n < 1000) | 0.535 | +0.5 | -0.3 | 0.1440 | 0.1463 |
| Time in range 70-180, pooled (%) | 472 | -0.205 [-1.579, +1.169] | -0.007865 | -0.29 | 0.770 | not applied (n < 1000) | 0.867 | +1.9 | +1.0 | 0.1427 | 0.1463 |
| Avg. daily time in range 70-180 (%) | 472 | -0.217 [-1.589, +1.155] | -0.008251 | -0.31 | 0.757 | not applied (n < 1000) | 0.861 | +1.9 | +1.0 | 0.1429 | 0.1463 |
| Any reading < 54 during wear (0/1) | 472 | -0.713 [-2.021, +0.595] | -1.719 | -1.07 | 0.285 | not applied (n < 1000) | 0.555 | +0.8 | -0.1 | 0.1454 | 0.1463 |
| Time < 54, pooled (%) | 472 | -1.124 [-1.951, -0.298] | -4.178 | -2.67 | 0.008** | not applied (n < 1000) | 0.115 | -1.0 | -1.9 | 0.1489 | 0.1463 |
| Avg. daily time < 54 (%) | 472 | -1.097 [-1.528, -0.665] | -2.945 | -4.98 | 6.4e-07*** | not applied (n < 1000) | 2.7e-04 (q<0.05) | -0.9 | -1.8 | 0.1504 | 0.1463 |
| Time 54-69, pooled (%) | 472 | -0.943 [-2.325, +0.438] | -1.064 | -1.34 | 0.181 | not applied (n < 1000) | 0.415 | -0.1 | -1.0 | 0.1471 | 0.1463 |
| Avg. daily time 54-69 (%) | 472 | -1.087 [-2.436, +0.261] | -1.114 | -1.58 | 0.114 | not applied (n < 1000) | 0.349 | -0.8 | -1.7 | 0.1480 | 0.1463 |
| Time < 70, pooled (%) | 472 | -1.068 [-2.347, +0.211] | -0.9958 | -1.64 | 0.102 | not applied (n < 1000) | 0.336 | -0.7 | -1.5 | 0.1481 | 0.1463 |
| Avg. daily time < 70 (%) | 472 | -1.187 [-2.289, -0.085] | -0.9537 | -2.11 | 0.035* | not applied (n < 1000) | 0.270 | -1.3 | -2.2 | 0.1497 | 0.1463 |
| Time 54-250, pooled (%) | 472 | +0.266 [-1.153, +1.685] | 0.0142 | 0.37 | 0.714 | not applied (n < 1000) | 0.853 | +1.8 | +1.0 | 0.1431 | 0.1463 |
| Avg. daily time 54-250 (%) | 472 | +0.215 [-1.143, +1.573] | 0.01163 | 0.31 | 0.756 | not applied (n < 1000) | 0.861 | +1.9 | +1.0 | 0.1434 | 0.1463 |
| Time 181-250, pooled (%) | 472 | +0.733 [-0.509, +1.974] | 0.04952 | 1.16 | 0.247 | not applied (n < 1000) | 0.517 | +0.7 | -0.1 | 0.1448 | 0.1463 |
| Avg. daily time 181-250 (%) | 472 | +0.692 [-0.548, +1.932] | 0.04575 | 1.09 | 0.274 | not applied (n < 1000) | 0.543 | +0.9 | +0.0 | 0.1446 | 0.1463 |
| Time > 180, pooled (%) | 472 | +0.248 [-1.122, +1.617] | 0.009455 | 0.35 | 0.723 | not applied (n < 1000) | 0.853 | +1.9 | +1.0 | 0.1430 | 0.1463 |
| Avg. daily time > 180 (%) | 472 | +0.273 [-1.097, +1.642] | 0.01033 | 0.39 | 0.696 | not applied (n < 1000) | 0.853 | +1.8 | +1.0 | 0.1432 | 0.1463 |
| Nocturnal time > 180 (%) | 472 | +0.449 [-0.993, +1.891] | 0.01488 | 0.61 | 0.542 | not applied (n < 1000) | 0.798 | +1.6 | +0.7 | 0.1429 | 0.1463 |
| Time > 250, pooled (%) | 472 | -0.249 [-1.668, +1.170] | -0.01329 | -0.34 | 0.731 | not applied (n < 1000) | 0.854 | +1.9 | +1.0 | 0.1431 | 0.1463 |
| Avg. daily time > 250 (%) | 472 | -0.192 [-1.550, +1.167] | -0.01037 | -0.28 | 0.782 | not applied (n < 1000) | 0.873 | +1.9 | +1.1 | 0.1434 | 0.1463 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Resting heart-rate proxy (daily 5th pct, bpm)
*n = 474; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 474 | +0.783 [+0.078, +1.489] | 0.5581 | 2.18 | 0.030* | not applied (n < 1000) | 0.244 | -1.9 | +0.0 | 0.1255 | 0.1229 |
| Mean glucose (mg/dL) | 474 | +1.054 [+0.267, +1.841] | 0.02532 | 2.63 | 0.009** | not applied (n < 1000) | 0.117 | -5.2 | -3.3 | 0.1306 | 0.1229 |
| GMI (%) | 474 | +1.054 [+0.267, +1.841] | 1.059 | 2.63 | 0.009** | not applied (n < 1000) | 0.117 | -5.2 | -3.3 | 0.1306 | 0.1229 |
| Nocturnal mean 00-06h (mg/dL) | 474 | +1.040 [+0.232, +1.848] | 0.02328 | 2.52 | 0.012* | not applied (n < 1000) | 0.148 | -4.8 | -2.9 | 0.1288 | 0.1229 |
| Glucose SD, pooled (mg/dL) | 474 | +0.365 [-0.449, +1.179] | 0.02906 | 0.88 | 0.379 | not applied (n < 1000) | 0.663 | +1.2 | +3.0 | 0.1163 | 0.1229 |
| Avg. daily SD (mg/dL) | 474 | +0.252 [-0.546, +1.049] | 0.02313 | 0.62 | 0.536 | not applied (n < 1000) | 0.798 | +1.6 | +3.5 | 0.1171 | 0.1229 |
| CV (%) | 474 | -0.641 [-1.441, +0.160] | -0.1138 | -1.57 | 0.117 | not applied (n < 1000) | 0.356 | -0.7 | +1.2 | 0.1253 | 0.1229 |
| Mean / SD ratio | 474 | +0.593 [-0.185, +1.372] | 0.5904 | 1.49 | 0.135 | not applied (n < 1000) | 0.378 | -0.3 | +1.6 | 0.1248 | 0.1229 |
| Avg. daily mean / SD | 474 | +0.662 [-0.098, +1.421] | 0.5336 | 1.71 | 0.088 | not applied (n < 1000) | 0.323 | -0.9 | +1.0 | 0.1258 | 0.1229 |
| MAG (mg/dL/h) | 474 | +0.826 [-0.014, +1.665] | 0.08184 | 1.93 | 0.054 | not applied (n < 1000) | 0.289 | -2.4 | -0.5 | 0.1231 | 0.1229 |
| Avg. daily range (mg/dL) | 474 | +0.253 [-0.531, +1.036] | 0.006876 | 0.63 | 0.528 | not applied (n < 1000) | 0.797 | +1.6 | +3.5 | 0.1166 | 0.1229 |
| SD of daily means (mg/dL) | 474 | +0.884 [+0.082, +1.685] | 0.09912 | 2.16 | 0.031* | not applied (n < 1000) | 0.247 | -2.9 | -1.1 | 0.1250 | 0.1229 |
| Time in range 70-180, pooled (%) | 474 | -1.114 [-1.913, -0.315] | -0.04275 | -2.73 | 0.006** | not applied (n < 1000) | 0.107 | -6.0 | -4.1 | 0.1295 | 0.1229 |
| Avg. daily time in range 70-180 (%) | 474 | -1.099 [-1.895, -0.302] | -0.0418 | -2.70 | 0.007** | not applied (n < 1000) | 0.107 | -5.7 | -3.9 | 0.1293 | 0.1229 |
| Any reading < 54 during wear (0/1) | 474 | -0.120 [-0.864, +0.623] | -0.2888 | -0.32 | 0.752 | not applied (n < 1000) | 0.861 | +1.9 | +3.8 | 0.1202 | 0.1229 |
| Time < 54, pooled (%) | 474 | -0.167 [-1.195, +0.861] | -0.6227 | -0.32 | 0.750 | not applied (n < 1000) | 0.861 | +1.8 | +3.7 | 0.1169 | 0.1229 |
| Avg. daily time < 54 (%) | 474 | -0.453 [-1.955, +1.049] | -1.219 | -0.59 | 0.554 | not applied (n < 1000) | 0.803 | +0.6 | +2.5 | 0.1096 | 0.1229 |
| Time 54-69, pooled (%) | 474 | -0.618 [-1.381, +0.145] | -0.6985 | -1.59 | 0.112 | not applied (n < 1000) | 0.348 | -0.5 | +1.4 | 0.1248 | 0.1229 |
| Avg. daily time 54-69 (%) | 474 | -0.766 [-1.554, +0.022] | -0.7865 | -1.91 | 0.057 | not applied (n < 1000) | 0.289 | -1.9 | +0.0 | 0.1268 | 0.1229 |
| Time < 70, pooled (%) | 474 | -0.556 [-1.306, +0.195] | -0.519 | -1.45 | 0.147 | not applied (n < 1000) | 0.382 | -0.0 | +1.9 | 0.1232 | 0.1229 |
| Avg. daily time < 70 (%) | 474 | -0.739 [-1.464, -0.014] | -0.5947 | -2.00 | 0.046* | not applied (n < 1000) | 0.289 | -1.6 | +0.3 | 0.1256 | 0.1229 |
| Time 54-250, pooled (%) | 474 | -0.690 [-1.505, +0.126] | -0.03685 | -1.66 | 0.097 | not applied (n < 1000) | 0.331 | -1.0 | +0.9 | 0.1235 | 0.1229 |
| Avg. daily time 54-250 (%) | 474 | -0.715 [-1.533, +0.103] | -0.03868 | -1.71 | 0.087 | not applied (n < 1000) | 0.323 | -1.3 | +0.6 | 0.1241 | 0.1229 |
| Time 181-250, pooled (%) | 474 | +1.101 [+0.355, +1.846] | 0.07448 | 2.89 | 0.004** | not applied (n < 1000) | 0.094 | -6.0 | -4.1 | 0.1310 | 0.1229 |
| Avg. daily time 181-250 (%) | 474 | +1.058 [+0.319, +1.797] | 0.07001 | 2.81 | 0.005** | not applied (n < 1000) | 0.107 | -5.4 | -3.5 | 0.1297 | 0.1229 |
| Time > 180, pooled (%) | 474 | +1.128 [+0.334, +1.922] | 0.04302 | 2.79 | 0.005** | not applied (n < 1000) | 0.107 | -6.2 | -4.3 | 0.1302 | 0.1229 |
| Avg. daily time > 180 (%) | 474 | +1.126 [+0.335, +1.918] | 0.04263 | 2.79 | 0.005** | not applied (n < 1000) | 0.107 | -6.2 | -4.3 | 0.1304 | 0.1229 |
| Nocturnal time > 180 (%) | 474 | +1.003 [+0.196, +1.809] | 0.03329 | 2.44 | 0.015* | not applied (n < 1000) | 0.164 | -4.2 | -2.3 | 0.1255 | 0.1229 |
| Time > 250, pooled (%) | 474 | +0.692 [-0.121, +1.505] | 0.03696 | 1.67 | 0.095 | not applied (n < 1000) | 0.328 | -1.0 | +0.8 | 0.1236 | 0.1229 |
| Avg. daily time > 250 (%) | 474 | +0.724 [-0.093, +1.542] | 0.03921 | 1.74 | 0.082 | not applied (n < 1000) | 0.320 | -1.3 | +0.5 | 0.1244 | 0.1229 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Total sleep time per night (min)
*n = 479; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 479 | -3.027 [-8.351, +2.296] | -2.196 | -1.11 | 0.265 | not applied (n < 1000) | 0.535 | +1.1 | +0.0 | -0.0202 | -0.0179 |
| Mean glucose (mg/dL) | 479 | +1.535 [-4.537, +7.606] | 0.03762 | 0.50 | 0.620 | not applied (n < 1000) | 0.823 | +1.8 | +0.7 | -0.0202 | -0.0179 |
| GMI (%) | 479 | +1.535 [-4.537, +7.606] | 1.573 | 0.50 | 0.620 | not applied (n < 1000) | 0.823 | +1.8 | +0.7 | -0.0202 | -0.0179 |
| Nocturnal mean 00-06h (mg/dL) | 479 | +2.613 [-3.649, +8.876] | 0.0594 | 0.82 | 0.413 | not applied (n < 1000) | 0.704 | +1.3 | +0.2 | -0.0196 | -0.0179 |
| Glucose SD, pooled (mg/dL) | 479 | -2.447 [-8.341, +3.446] | -0.1953 | -0.81 | 0.416 | not applied (n < 1000) | 0.704 | +1.4 | +0.3 | -0.0191 | -0.0179 |
| Avg. daily SD (mg/dL) | 479 | -1.758 [-7.499, +3.983] | -0.162 | -0.60 | 0.548 | not applied (n < 1000) | 0.800 | +1.7 | +0.6 | -0.0202 | -0.0179 |
| CV (%) | 479 | -2.871 [-8.910, +3.168] | -0.5111 | -0.93 | 0.351 | not applied (n < 1000) | 0.626 | +1.1 | +0.1 | -0.0188 | -0.0179 |
| Mean / SD ratio | 479 | +4.200 [-1.629, +10.029] | 4.255 | 1.41 | 0.158 | not applied (n < 1000) | 0.392 | +0.1 | -0.9 | -0.0164 | -0.0179 |
| Avg. daily mean / SD | 479 | +3.178 [-2.494, +8.850] | 2.597 | 1.10 | 0.272 | not applied (n < 1000) | 0.542 | +0.9 | -0.1 | -0.0181 | -0.0179 |
| MAG (mg/dL/h) | 479 | -7.920 [-13.826, -2.014] | -0.7922 | -2.63 | 0.009** | not applied (n < 1000) | 0.117 | -4.6 | -5.6 | -0.0065 | -0.0179 |
| Avg. daily range (mg/dL) | 479 | -1.872 [-7.583, +3.839] | -0.05131 | -0.64 | 0.521 | not applied (n < 1000) | 0.797 | +1.6 | +0.6 | -0.0203 | -0.0179 |
| SD of daily means (mg/dL) | 479 | -2.973 [-9.344, +3.398] | -0.3342 | -0.91 | 0.360 | not applied (n < 1000) | 0.634 | +1.1 | +0.0 | -0.0193 | -0.0179 |
| Time in range 70-180, pooled (%) | 479 | -1.536 [-7.638, +4.565] | -0.05966 | -0.49 | 0.622 | not applied (n < 1000) | 0.823 | +1.8 | +0.7 | -0.0203 | -0.0179 |
| Avg. daily time in range 70-180 (%) | 479 | -1.690 [-7.801, +4.421] | -0.06505 | -0.54 | 0.588 | not applied (n < 1000) | 0.815 | +1.7 | +0.6 | -0.0202 | -0.0179 |
| Any reading < 54 during wear (0/1) | 479 | -1.903 [-7.860, +4.053] | -4.581 | -0.63 | 0.531 | not applied (n < 1000) | 0.797 | +1.6 | +0.5 | -0.0227 | -0.0179 |
| Time < 54, pooled (%) | 479 | -1.697 [-6.300, +2.906] | -6.329 | -0.72 | 0.470 | not applied (n < 1000) | 0.748 | +1.7 | +0.6 | -0.0213 | -0.0179 |
| Avg. daily time < 54 (%) | 479 | -0.047 [-4.795, +4.700] | -0.1279 | -0.02 | 0.984 | not applied (n < 1000) | 0.992 | +2.0 | +0.9 | -0.0225 | -0.0179 |
| Time 54-69, pooled (%) | 479 | +3.963 [-4.325, +12.251] | 4.472 | 0.94 | 0.349 | not applied (n < 1000) | 0.626 | +0.3 | -0.7 | -0.0211 | -0.0179 |
| Avg. daily time 54-69 (%) | 479 | +4.160 [-3.470, +11.790] | 4.27 | 1.07 | 0.285 | not applied (n < 1000) | 0.555 | +0.2 | -0.9 | -0.0190 | -0.0179 |
| Time < 70, pooled (%) | 479 | +2.862 [-4.853, +10.577] | 2.669 | 0.73 | 0.467 | not applied (n < 1000) | 0.746 | +1.1 | +0.1 | -0.0222 | -0.0179 |
| Avg. daily time < 70 (%) | 479 | +3.249 [-3.409, +9.907] | 2.617 | 0.96 | 0.339 | not applied (n < 1000) | 0.613 | +0.9 | -0.2 | -0.0192 | -0.0179 |
| Time 54-250, pooled (%) | 479 | -1.656 [-7.641, +4.328] | -0.09126 | -0.54 | 0.587 | not applied (n < 1000) | 0.815 | +1.7 | +0.7 | -0.0198 | -0.0179 |
| Avg. daily time 54-250 (%) | 479 | -1.736 [-7.718, +4.247] | -0.09684 | -0.57 | 0.570 | not applied (n < 1000) | 0.803 | +1.7 | +0.6 | -0.0195 | -0.0179 |
| Time 181-250, pooled (%) | 479 | +0.396 [-5.966, +6.758] | 0.02694 | 0.12 | 0.903 | not applied (n < 1000) | 0.949 | +2.0 | +0.9 | -0.0215 | -0.0179 |
| Avg. daily time 181-250 (%) | 479 | +0.557 [-5.786, +6.901] | 0.03709 | 0.17 | 0.863 | not applied (n < 1000) | 0.923 | +2.0 | +0.9 | -0.0213 | -0.0179 |
| Time > 180, pooled (%) | 479 | +1.402 [-4.705, +7.510] | 0.05412 | 0.45 | 0.653 | not applied (n < 1000) | 0.834 | +1.8 | +0.7 | -0.0204 | -0.0179 |
| Avg. daily time > 180 (%) | 479 | +1.518 [-4.600, +7.636] | 0.05814 | 0.49 | 0.627 | not applied (n < 1000) | 0.823 | +1.8 | +0.7 | -0.0203 | -0.0179 |
| Nocturnal time > 180 (%) | 479 | +3.237 [-2.981, +9.456] | 0.1084 | 1.02 | 0.308 | not applied (n < 1000) | 0.577 | +1.0 | -0.1 | -0.0179 | -0.0179 |
| Time > 250, pooled (%) | 479 | +1.681 [-4.302, +7.665] | 0.09265 | 0.55 | 0.582 | not applied (n < 1000) | 0.815 | +1.7 | +0.6 | -0.0198 | -0.0179 |
| Avg. daily time > 250 (%) | 479 | +1.736 [-4.246, +7.718] | 0.0969 | 0.57 | 0.570 | not applied (n < 1000) | 0.803 | +1.7 | +0.6 | -0.0195 | -0.0179 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)

#### Garmin stress score, mean (0-100)
*n = 474; OLS (HC3)*

| Predictor (entered alone) | n | Effect per 1 SD (95% CI) | Raw slope | t / z | p (raw) | q (BH, rule: n >= 1000) | q (BH, informational, all tests in population) | dAIC vs covariates | dAIC vs HbA1c-only | CV R2/AUC (pred | covs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HbA1c (%) | 474 | +2.522 [+0.957, +4.087] | 1.797 | 3.16 | 0.002** | not applied (n < 1000) | 0.061 | -7.6 | +0.0 | 0.1048 | 0.0898 |
| Mean glucose (mg/dL) | 474 | +2.701 [+0.958, +4.445] | 0.06495 | 3.04 | 0.002** | not applied (n < 1000) | 0.072 | -9.2 | -1.7 | 0.1074 | 0.0898 |
| GMI (%) | 474 | +2.701 [+0.958, +4.445] | 2.715 | 3.04 | 0.002** | not applied (n < 1000) | 0.072 | -9.2 | -1.7 | 0.1074 | 0.0898 |
| Nocturnal mean 00-06h (mg/dL) | 474 | +2.513 [+0.712, +4.315] | 0.05628 | 2.73 | 0.006** | not applied (n < 1000) | 0.107 | -7.4 | +0.2 | 0.1028 | 0.0898 |
| Glucose SD, pooled (mg/dL) | 474 | +1.271 [-0.476, +3.018] | 0.1012 | 1.43 | 0.154 | not applied (n < 1000) | 0.389 | -0.4 | +7.2 | 0.0902 | 0.0898 |
| Avg. daily SD (mg/dL) | 474 | +1.283 [-0.526, +3.091] | 0.118 | 1.39 | 0.164 | not applied (n < 1000) | 0.402 | -0.5 | +7.1 | 0.0907 | 0.0898 |
| CV (%) | 474 | -1.304 [-2.954, +0.346] | -0.2316 | -1.55 | 0.121 | not applied (n < 1000) | 0.362 | -0.6 | +7.0 | 0.0910 | 0.0898 |
| Mean / SD ratio | 474 | +1.103 [-0.499, +2.704] | 1.097 | 1.35 | 0.177 | not applied (n < 1000) | 0.411 | +0.1 | +7.7 | 0.0892 | 0.0898 |
| Avg. daily mean / SD | 474 | +1.067 [-0.473, +2.608] | 0.8603 | 1.36 | 0.175 | not applied (n < 1000) | 0.410 | +0.2 | +7.8 | 0.0896 | 0.0898 |
| MAG (mg/dL/h) | 474 | +1.440 [-0.229, +3.109] | 0.1425 | 1.69 | 0.091 | not applied (n < 1000) | 0.327 | -1.2 | +6.4 | 0.0924 | 0.0898 |
| Avg. daily range (mg/dL) | 474 | +0.943 [-0.833, +2.720] | 0.02575 | 1.04 | 0.298 | not applied (n < 1000) | 0.567 | +0.7 | +8.2 | 0.0870 | 0.0898 |
| SD of daily means (mg/dL) | 474 | +1.214 [-0.338, +2.765] | 0.1361 | 1.53 | 0.125 | not applied (n < 1000) | 0.371 | -0.2 | +7.4 | 0.0919 | 0.0898 |
| Time in range 70-180, pooled (%) | 474 | -2.774 [-4.431, -1.116] | -0.1065 | -3.28 | 0.001** | not applied (n < 1000) | 0.053 | -9.8 | -2.2 | 0.1089 | 0.0898 |
| Avg. daily time in range 70-180 (%) | 474 | -2.727 [-4.385, -1.070] | -0.1038 | -3.22 | 0.001** | not applied (n < 1000) | 0.053 | -9.4 | -1.8 | 0.1082 | 0.0898 |
| Any reading < 54 during wear (0/1) | 474 | -0.520 [-2.074, +1.034] | -1.252 | -0.66 | 0.512 | not applied (n < 1000) | 0.794 | +1.6 | +9.1 | 0.0881 | 0.0898 |
| Time < 54, pooled (%) | 474 | -0.435 [-2.240, +1.369] | -1.621 | -0.47 | 0.636 | not applied (n < 1000) | 0.826 | +1.7 | +9.3 | 0.0857 | 0.0898 |
| Avg. daily time < 54 (%) | 474 | -0.808 [-3.110, +1.494] | -2.175 | -0.69 | 0.491 | not applied (n < 1000) | 0.773 | +1.0 | +8.5 | 0.0815 | 0.0898 |
| Time 54-69, pooled (%) | 474 | -1.160 [-2.658, +0.338] | -1.312 | -1.52 | 0.129 | not applied (n < 1000) | 0.371 | -0.1 | +7.5 | 0.0917 | 0.0898 |
| Avg. daily time 54-69 (%) | 474 | -1.308 [-2.785, +0.168] | -1.344 | -1.74 | 0.082 | not applied (n < 1000) | 0.320 | -0.7 | +6.9 | 0.0928 | 0.0898 |
| Time < 70, pooled (%) | 474 | -1.074 [-2.555, +0.408] | -1.003 | -1.42 | 0.155 | not applied (n < 1000) | 0.389 | +0.2 | +7.8 | 0.0904 | 0.0898 |
| Avg. daily time < 70 (%) | 474 | -1.272 [-2.613, +0.069] | -1.025 | -1.86 | 0.063 | not applied (n < 1000) | 0.289 | -0.5 | +7.1 | 0.0917 | 0.0898 |
| Time 54-250, pooled (%) | 474 | -1.887 [-3.770, -0.004] | -0.1008 | -1.96 | 0.050* | not applied (n < 1000) | 0.289 | -3.4 | +4.2 | 0.0941 | 0.0898 |
| Avg. daily time 54-250 (%) | 474 | -1.932 [-3.827, -0.037] | -0.1045 | -2.00 | 0.046* | not applied (n < 1000) | 0.289 | -3.6 | +3.9 | 0.0944 | 0.0898 |
| Time 181-250, pooled (%) | 474 | +2.512 [+0.931, +4.093] | 0.1701 | 3.11 | 0.002** | not applied (n < 1000) | 0.065 | -7.9 | -0.3 | 0.1082 | 0.0898 |
| Avg. daily time 181-250 (%) | 474 | +2.403 [+0.821, +3.985] | 0.1592 | 2.98 | 0.003** | not applied (n < 1000) | 0.077 | -7.1 | +0.5 | 0.1064 | 0.0898 |
| Time > 180, pooled (%) | 474 | +2.796 [+1.145, +4.446] | 0.1067 | 3.32 | 9.0e-04*** | not applied (n < 1000) | 0.053 | -10.0 | -2.4 | 0.1093 | 0.0898 |
| Avg. daily time > 180 (%) | 474 | +2.769 [+1.118, +4.421] | 0.1049 | 3.29 | 0.001** | not applied (n < 1000) | 0.053 | -9.7 | -2.1 | 0.1090 | 0.0898 |
| Nocturnal time > 180 (%) | 474 | +2.324 [+0.653, +3.995] | 0.07717 | 2.73 | 0.006** | not applied (n < 1000) | 0.107 | -5.9 | +1.7 | 0.0992 | 0.0898 |
| Time > 250, pooled (%) | 474 | +1.892 [+0.012, +3.772] | 0.1011 | 1.97 | 0.049* | not applied (n < 1000) | 0.289 | -3.4 | +4.2 | 0.0942 | 0.0898 |
| Avg. daily time > 250 (%) | 474 | +1.948 [+0.053, +3.843] | 0.1054 | 2.02 | 0.044* | not applied (n < 1000) | 0.289 | -3.7 | +3.8 | 0.0946 | 0.0898 |

Skipped: Any reading > 250 during wear (0/1) (predictor constant in this cohort)
