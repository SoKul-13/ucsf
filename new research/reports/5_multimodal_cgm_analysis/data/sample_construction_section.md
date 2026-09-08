
## 8. Exact sample construction (how "same-size" samples were made)

No participant was truncated to a fixed number of days, and no outcome sample was trimmed to match another. "Same size" refers to one rule applied **within each outcome**: every specification for that outcome (M0, M1, M2[x], M2, M3[x], M3) is fitted on the identical set of participants, obtained by list-wise deletion on the union of every variable used by any of those specifications. The person-level membership of every sample is in `data/analysis_sample_membership_by_outcome.csv` (one row per participant, one 0/1 column per step and per outcome), and the counts below are in `data/analysis_sample_construction.json`.

**Step 1 - CGM stream.** All Dexcom G6 readings of type EGV with a numeric value between 39 and 401 mg/dL were kept and converted to site-local time. Duplicate timestamps were dropped. A calendar day was *valid* if it held at least 70 % of the expected 288 readings (>= 202). Overall metrics use every valid reading (not only valid days); day-averaged metrics (`avg_daily_*`) use valid days only. Participants needed >= 3 valid days; in the analysis base the number of valid days ranges 3-12 (median 9, mean 8.8), i.e. the wear period was **not** cut to a common length.

**Step 2 - funnel to the analysis base.**

| Step | Rule | Participants |
| :--- | :--- | :---: |
| 0 | AI-READI v3.0.0 participants | 2,280 |
| 1 | >= 3 valid CGM days | 2,216 |
| 2 | + laboratory HbA1c present (`import_hba1c`) | 2,153 |
| 3 | + all four core CGM metrics present (none missing at this step) | 2,153 |
| 4 | + complete covariates: age, BMI (4 missing), education level (11 missing), site, hypertension, high cholesterol, kidney disease, circulatory disease | **2,138** (analysis base) |

Analysis base by group: No diabetes 739, Pre-diabetes / lifestyle 532, T2D non-insulin 639, T2D insulin 228; by site UW 774, UAB 744, UCSD 620.

**Step 3 - per-outcome complete cases.** From the analysis base, an outcome's sample is every participant with a non-missing outcome (plus season of visit for environmental outcomes, which was never missing). Because HbA1c, the four CGM metrics and the covariates are already complete in the base, the only source of loss at this step is the outcome itself:

| Outcome | N used by every specification | Lost from base (missing outcome) |
| :--- | :---: | :---: |
| MoCA total score (0-30) | 2,138 | 0 |
| Cognitive impairment (MoCA < 26) | 2,138 (857 events) | 0 |
| MoCA memory index score (0-15) | 2,138 | 0 |
| CES-D-10 depressive symptoms (0-30) | 2,135 | 3 |
| Clinically relevant depressive symptoms (CES-D-10 >= 10) | 2,135 (403 events) | 3 |
| Indoor PM2.5, log(1 + mean ug/m3) | 2,100 | 38 |
| Indoor temperature, mean (deg C) | 2,100 | 38 |
| Indoor relative humidity, mean (%) | 2,100 | 38 |
| Indoor VOC index, mean | 2,100 | 38 |
| Steps per wear-day | 1,872 | 266 |
| Brisk-cadence minutes per day (>= 100 steps/min) | 1,872 | 266 |
| Resting heart-rate proxy (daily 5th pct, bpm) | 1,877 | 261 |
| Total sleep time per night (min) | 1,893 | 245 |
| Garmin stress score, mean (0-100) | 1,879 | 259 |
| MoCA delayed recall (0-5) | 2,138 | 0 |
| PAID-5 diabetes distress (0-20) | 2,093 | 45 |
| Indoor NOx index, mean | 2,100 | 38 |
| % time indoor PM2.5 > 15 ug/m3 | 2,100 | 38 |
| Sedentary time (% of labelled minutes) | 1,872 | 266 |
| Sleep efficiency (%) | 1,893 | 245 |
| Nocturnal SpO2, mean (%) | 1,510 | 628 |
| Mean heart rate (bpm) | 1,877 | 261 |
| % time high stress (> 50) | 1,879 | 259 |

Notes on the losses: the 266 participants without step data are 248 with no Garmin record at all plus 18 with < 3 wear-days (a wear-day needs >= 10 h of valid heart-rate contact, excluding the first and last partial days); there were no participants with wear-days but zero steps after the zero-step-day rule. The 38 without environmental outcomes had no sensor file with >= 1 h of valid data; 84 participants with sensor data but < 3 sensor days **were retained** for the environmental outcomes (the >= 3-day flag `has_env` was computed but not applied as an exclusion), which is a documented deviation from the CGM/wearable rules. SpO2 has the largest loss (628) because Garmin records it only during sleep for a subset of nights.

**Step 4 - within-outcome identity of samples.** For each outcome the same rows feed M0, M1, all M2[x], M2, all M3[x] and M3; the predictor SDs used to express effects "per 1 SD" are computed on that same sample. Sensitivity samples (>= 7 valid CGM days, insulin users excluded, T2D only, no-T2D only) are subsets of the same per-outcome samples, and the exploratory sweep of 11 extra CGM metrics uses the outcome's sample minus any participant missing that metric (only `nocturnal_mean` and the day-level metrics can be missing, and only for participants with very short wear).
