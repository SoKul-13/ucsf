# Phase 6 - Glycaemic measures entered one at a time, in the total cohort and in "healthy" vs "non-healthy" groups, with raw and FDR-adjusted p-values and glucose-band analyses

**Phase 6 research report** · AI-READI v3.0.0 · 2026-09-07
**Companion files**: [full single-predictor tables](research_report_02_full_single_predictor_tables.md) · [glucose-band analyses](research_report_03_glucose_band_analyses.md) · [methods and sample log](research_report_04_methods_and_sample_log.md) · result CSVs in `data/` · figures in `figures/`
**Code**: `src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py` (shared) → `src/6_subgroup_single_predictor_analysis/run_phase6_analysis.py` → `generate_phase6_reports.py`

---

## What was asked and what was done

| Request | Implementation |
| :--- | :--- |
| #1 Run by total, "healthy" (healthy + pre-diabetes) and "non-healthy" (oral/non-insulin + insulin) | Three populations from the Phase 5 analysis base: total N = 2,138; healthy N = 1,271 (739 no diabetes + 532 pre-diabetes / lifestyle); non-healthy N = 867 (639 T2D non-insulin + 228 insulin). Same per-outcome complete-case rule as Phase 5. |
| #1 p-values with and without FDR | Every test reports the raw p and two Benjamini-Hochberg q-values (family = all tests in the population; family = all predictors for that outcome). |
| #2 Each measure individually, not together | 31 predictors, each fitted as `outcome ~ covariates + predictor`: HbA1c; CGM level (mean, GMI, nocturnal mean); CGM variability (pooled SD, daily SD, CV, mean/SD, daily mean/SD, MAG, daily range, SD of daily means); time in range 70-180 (pooled and daily); and every glucose band (see #4). No combined models. |
| #3 BH-FDR only on large datasets | Rule implemented: FDR is applied only when the sample behind the test has **n ≥ 1,000**. That is the case for the total and healthy populations (n = 1,872-2,138 and 1,125-1,271) and never for the non-healthy population (n = 747-867), whose results are therefore raw-p only and marked as such. **This threshold is my interpretation of "large" - change `FDR_MIN_N` in the script if you meant something else.** |
| #4 Enough people outside 54-250? Separate versions for 54-70, 54-250, > 180 | Feasibility table below; band metrics (% of CGM time in < 54, 54-69, < 70, 70-180, 181-250, > 180, > 250, 54-250; pooled and day-averaged; plus 0/1 "any reading" indicators for < 54 and > 250) each tested alone in all three populations. Full tables in report 03. |

Covariates, estimators (OLS with HC3 t-tests; logistic with Wald z), effect scaling (per 1 SD of the predictor) and cross-validation follow Phase 5. 434 tests were run per population (1,302 in total); none were skipped.

---

## 1. Are there enough people outside 54-250 mg/dL? (request #4)

| Band | Total (n = 2,138): any time / ≥ 1 % / ≥ 5 % of time | Healthy (1,271) | Non-healthy (867) | Verdict |
| :--- | :---: | :---: | :---: | :--- |
| < 54 | 638 / 56 / 3 | 408 / 35 / 2 | 230 / 21 / 1 | **Marginal.** Many people have a few readings below 54 (median exposure among them is a handful of readings), but fewer than 60 have ≥ 1 % of their time there. The % time metric is nearly all zeros; the 0/1 "any reading < 54" indicator is the usable form. |
| 54-69 | 1,251 / 326 / 42 | 828 / 221 / 22 | 423 / 105 / 20 | Feasible as % time (326 with ≥ 1 %). |
| < 70 (54-69 plus < 54) | 1,259 / 377 / 57 | 831 / 253 / 34 | 428 / 124 / 23 | Feasible. |
| 181-250 | 1,927 / 1,407 / 826 | 1,094 / 641 / 234 | 833 / 766 / 592 | Feasible everywhere. |
| > 180 | 1,927 / 1,410 / 837 | 1,094 / 643 / 240 | 833 / 767 / 597 | Feasible everywhere. |
| > 250 | 795 / 461 / 240 | 244 / 69 / 18 | 551 / 392 / 222 | Feasible in total and non-healthy; **marginal in healthy** (69 with ≥ 1 %). |
| 54-250 (wide band) | 2,138 / 2,138 / 2,134 | all | all | Feasible, but it is nearly the complement of "> 250" (median 100 %), so it mostly re-tests severe hyperglycaemia with the sign reversed. |
| 70-180 (usual) | 2,135 / 2,125 / 2,110 | all | all | Reference range. |

Across the base there were 7,215 readings below 54 and 165,251 above 250, out of 5.92 million valid readings (0.12 % and 2.8 %); 1,248 of the 2,138 participants had at least one reading outside 54-250 and 890 never left that band. So: hyperglycaemic bands are well populated; hypoglycaemia below 54 is rare enough that only presence/absence can be modelled, and 54-69 is the workable hypoglycaemia band.

![Fig 3](figures/fig3_band_feasibility.png)

---

## 2. Headline results by population (requests #1-#3)

Counts of significant tests (434 per population):

| Population | Raw p < 0.05 | FDR applied? | q < 0.05, family = all 434 tests | q < 0.05, family = within outcome |
| :--- | :---: | :---: | :---: | :---: |
| Total (n 1,872-2,138) | 157 | yes | **126** | 121 |
| Healthy (n 1,125-1,271) | 73 | yes | **18** | 47 |
| Non-healthy (n 747-867) | **110** | no (n < 1,000) | - | - |

Under the null, 5 % of 434 tests ≈ 22 would reach raw p < 0.05, so all three populations carry real signal; the non-healthy group shows more raw hits than the healthy group despite being smaller.

### 2.1 Cognition

| Predictor (alone) | Total: MoCA total per SD | Healthy | Non-healthy (raw only) |
| :--- | :---: | :---: | :---: |
| HbA1c | −0.35 (q < 0.001) | −0.31 (p = 0.005, q > 0.05) | −0.21 (p = 0.049) |
| Mean glucose / GMI | **−0.41 (q < 0.001)** | **−0.41 (p = 8 × 10⁻⁵, q < 0.05)** | −0.27 (p = 0.021) |
| Nocturnal mean | −0.39 (q < 0.001) | **−0.36 (p = 7 × 10⁻⁴, q < 0.05)** | −0.27 (p = 0.018) |
| Glucose SD, pooled | −0.40 (q < 0.001) | −0.24 (p = 0.011) | **−0.35 (p = 0.002)** |
| Avg. daily SD | −0.39 (q < 0.001) | −0.23 (p = 0.008) | **−0.33 (p = 0.004)** |
| CV | −0.23 (q < 0.05) | −0.03 (p = 0.68) | −0.24 (p = 0.021) |
| Mean / SD ratio | +0.22 (q < 0.05) | +0.02 (p = 0.82) | **+0.30 (p = 0.0035)** |
| SD of daily means | −0.31 (q < 0.001) | −0.07 (p = 0.51) | **−0.34 (p = 0.003)** |
| TIR 70-180 (pooled / daily) | +0.36 / +0.35 (q < 0.001) | +0.33 / +0.32 (p = 0.003) | +0.25 / +0.25 (p = 0.03) |

The same pattern holds for MoCA < 26 and the memory index (healthy: mean glucose −0.26 and nocturnal mean −0.27 on the memory index, both q < 0.05; non-healthy: pooled SD −0.28, CV −0.28, mean/SD +0.26, all p ≈ 0.002-0.003).

**Inference.** The two groups are driven by different aspects of glycaemia. In the healthy/pre-diabetic range, cognition tracks glucose *level* (mean, nocturnal, GMI) and not variability (CV, mean/SD and between-day SD are null). In treated diabetes, cognition tracks glucose *variability* (SD, CV, mean/SD, day-to-day SD) more strongly than level, and HbA1c is only borderline. This is a sharper statement than Phase 5's "gradient is steeper outside diabetes": the level-cognition gradient flattens in diabetes, but a variability-cognition gradient appears. Clinically this argues for reporting SD/CV alongside mean glucose when CGM is used in people with diabetes, and for treating high-normal glucose as a cognitive risk marker in people without diabetes.

### 2.2 Depression

- **Total**: no level or TIR metric predicts CES-D-10 total (all p > 0.2). Between-day SD of daily means does (+0.36 points per SD, q < 0.05; CES-D-10 ≥ 10 log-OR +0.21, q < 0.001), with nocturnal mean (q < 0.05) and MAG (raw) also positive for the ≥ 10 threshold. HbA1c reaches raw p = 0.028 for ≥ 10 only.
- **Healthy**: nothing of note. Of the 62 depression tests, two reach raw p < 0.05 (the smallest is nocturnal time > 180 for CES-D-10 ≥ 10, p = 0.016), which is what 62 null tests would produce by chance; none survives FDR.
- **Non-healthy**: SD of daily means +0.59 points per SD (p = 8 × 10⁻⁴) and log-OR +0.33 for CES-D-10 ≥ 10 (p = 5 × 10⁻⁵); MAG +0.53 / +0.23 (p = 0.003 / 0.005); HbA1c +0.31 (p = 0.12) / log-OR +0.18 (p = 0.024); pooled SD log-OR +0.20 (p = 0.02).

**Inference.** The depression-glycaemia association in this cohort is located entirely in people with treated diabetes and is about *instability* (day-to-day swings, rate of change), not average level or time in range. Even though FDR could not be applied in that group by rule #3, an effect with p = 5 × 10⁻⁵ among 434 tests would survive a Bonferroni correction (0.05 / 434 = 1.2 × 10⁻⁴), so it is not a multiplicity artefact. This is consistent with the Phase 5b replication and points to disorganised routines or treatment burden as the pathway.

### 2.3 Home environment

- **Total**: indoor PM2.5 relates to HbA1c (+0.07 log units per SD, q < 0.05) and to SD of daily means (+0.06, q < 0.05); no level or TIR metric. Temperature, humidity and VOC: no glycaemic predictor at any threshold.
- **Healthy**: PM2.5 goes weakly the *other* way with mean glucose (−0.05, raw p = 0.016) and nocturnal mean (−0.05, p = 0.035); nothing survives FDR.
- **Non-healthy**: PM2.5 relates to HbA1c (+0.11, p = 0.009), SD of daily means (+0.11, p = 0.002), and to the hypoglycaemia bands (time < 70: +0.14, p = 0.003; time < 54: +0.11, p = 0.006; time 54-69: +0.13, p = 0.006); TIR −0.07 (p = 0.043).

**Inference.** The home environment is not a function of glycaemic level. The PM2.5 signal is carried by HbA1c and by glycaemic instability, and it is a diabetes-group phenomenon. The link between low-glucose exposure and higher indoor PM2.5 in treated diabetes is new and could reflect a shared socioeconomic pathway (poorer housing, more variable food access, more hypoglycaemia); it needs an income or deprivation covariate before it is interpreted further.

### 2.4 Wearables

- **Resting heart rate and Garmin stress**: every level and variability metric is significant after FDR in the total cohort (mean glucose +1.7 bpm and +3.1 stress points per SD; TIR −1.7 and −3.0). In the healthy group all metrics remain significant (HbA1c +0.82 bpm, q < 0.05; SD of daily means +0.93, q < 0.05; the others at raw p < 0.03). In the non-healthy group level metrics dominate (mean glucose +1.04 bpm, p = 0.001; TIR −1.07, p = 0.001; HbA1c +0.88, p = 0.003; stress +2.6 per SD of mean glucose or TIR, p ≈ 10⁻⁴) while CV and mean/SD are null.
- **Steps and brisk minutes**: HbA1c positive in total (q < 0.05) and healthy (+263 steps per SD, raw p = 0.012); MAG positive everywhere (+428 steps per SD, q < 0.001 in total; +432 in healthy, q < 0.05; +376 in non-healthy, p = 0.07). Level and TIR metrics are null. Hypoglycaemia bands are *negative* for steps: time < 70 −231 steps per SD in total (q < 0.05) and, in the non-healthy group, any reading < 54 −502 steps (p = 0.005), time 54-69 −383 (p = 0.006), time < 70 −412 (p = 0.005); the healthy group shows no such relation.
- **Sleep duration**: HbA1c −5.3 min per SD (total, q < 0.05; non-healthy −5.6, p = 0.012; healthy −4.0, p = 0.035), MAG −9.0 (q < 0.001 in total and healthy; −9.3 in non-healthy, p = 3 × 10⁻⁴), pooled and daily SD ≈ −4 to −5 min (q < 0.05 total; p ≈ 0.04 non-healthy); any reading > 250 −6.7 min (non-healthy, p = 0.014).

**Inference.** Autonomic signals (resting heart rate, HRV-based stress) respond to glucose level in both groups, with the gradient still present in the healthy range. Activity and sleep do not respond to level; the metrics that move with them are HbA1c, MAG (which largely reflects meal- and exercise-driven excursions) and, in treated diabetes, hypoglycaemia exposure, where people with more time below 70 walk 400-500 fewer steps a day. Whether hypoglycaemia limits activity or activity provokes hypoglycaemia cannot be decided cross-sectionally, but the association is confined to the medicated group, which fits treatment-related hypoglycaemia.

### 2.5 Band-specific versions (request #4)

| Band | What it adds beyond the 70-180 range |
| :--- | :--- |
| > 180, 181-250, > 250 | Mirror mean glucose almost exactly (cognition, resting heart rate, stress all q < 0.001 in total; same signs in both groups). > 250 as % time or as a 0/1 indicator is significant for cognition, heart rate and stress in total, and for sleep (−6.7 min) and stress in non-healthy. No new information, and in the healthy group > 250 is too sparse to rely on. |
| 54-250 (wide band) | Nearly the complement of > 250 (positive for MoCA q < 0.05; negative for heart rate and stress q < 0.001 in total). Adds nothing that > 250 does not already say. |
| 54-69 and < 70 | **Different information.** No association with cognition, heart rate or stress in any population; instead associated with fewer steps (total q < 0.05; non-healthy p ≈ 0.005) and, in non-healthy, with higher indoor PM2.5 (p ≈ 0.003-0.006). |
| < 54 | Only the 0/1 indicator is usable. It shows a *positive* MoCA association in total and healthy (raw p ≈ 0.03-0.04, not FDR-significant) that is most likely an artefact: brief readings below 54 in healthy people are typically nocturnal sensor-compression lows, which are more common in younger, leaner, better-sleeping participants. It should not be read as "hypoglycaemia protects cognition". In non-healthy it is associated with fewer steps (−502, p = 0.005) and fewer brisk minutes (p = 0.038). |

---

## 3. What is important

1. **The 70-180 range and mean glucose carry the same information for cognition and autonomic outcomes; the hypoglycaemia bands carry different information (activity, air quality) and only in treated diabetes.** If one band beyond 70-180 is to be added to the standard set, it should be 54-69 (or < 70), not 54-250 or > 250.
2. **Level vs variability splits by group.** Healthy: level predicts cognition and heart rate; variability does not. Non-healthy: variability predicts cognition and depression; level predicts heart rate and stress. Any "CGM vs HbA1c" claim should therefore be made within group.
3. **Depression is a non-healthy, instability phenomenon** (between-day SD, MAG), with an effect size that survives even Bonferroni within the group.
4. **HbA1c, entered alone, is never the strongest single predictor for cognition, heart rate or stress** (mean glucose, nocturnal mean or SD beat it in every population), but it is the only level-type measure that relates to steps, sleep and PM2.5 - the same split as in Phase 5.
5. **Multiplicity matters most in the healthy group**: 73 raw hits shrink to 18 under the strictest family; the survivors are mean/nocturnal glucose for cognition and the heart-rate/stress set. The non-healthy group's strongest findings (variability-cognition p ≈ 0.002-0.004; instability-depression p ≈ 10⁻⁵-10⁻⁴; level-heart-rate p ≈ 10⁻³) would survive FDR had it been applied.
6. **Out-of-sample gains remain small** (largest: +0.034 R² for resting heart rate from mean glucose; +0.015 for MoCA), so these are markers of information content, not screening tools.

## 4. Limitations

| Limitation | Why it matters |
| :--- | :--- |
| 31 predictors × 14 outcomes × 3 populations = 1,302 tests | Raw p-values in the non-healthy group are uncorrected by rule #3; treat p between 0.01 and 0.05 there as suggestive only. |
| "Healthy" pools no-diabetes and pre-diabetes | Phase 5b showed the cognition gradient is strongest in the no-diabetes subgroup alone; pooling dilutes it. |
| Many predictors are near-duplicates (mean glucose ≡ GMI; pooled ≡ daily versions; > 180 ≈ 181-250) | The FDR families are therefore conservative; correlated tests inflate the apparent number of "hits". |
| Band metrics are zero-inflated | % time < 54 is uninformative; 0/1 indicators were used but remain crude. |
| Same cross-sectional design, covariate set and proxies as Phase 5 | No sex/race; MoCA and CES-D-10 are screening instruments; wearable metrics are proxies. |

## 5. Clarifications I need from you

1. **FDR threshold**: I applied BH only when n ≥ 1,000. If "large" meant something else (e.g. the total cohort only, or a number-of-tests rule), tell me and I will re-run; it is one constant.
2. **"54 to 250"**: I treated it as *percentage of CGM time between 54 and 250 inclusive* (a wide time-in-range). If you meant *restricting the analysis to people whose glucose never leaves 54-250*, that is a different analysis (it would drop the 1,248 participants with any excursion and keep 890) and I can add it.
3. **Pooled vs day-averaged metrics**: both are reported; say which you want as the headline version in the write-up.
4. **Healthy definition**: implemented as instructed (no diabetes + pre-diabetes/lifestyle). If you also want the no-diabetes-only split from Phase 5b repeated here, it is a one-line change.

*Figures*: [Fig. 1 heat-map of all tests by population](figures/fig1_heatmap_single_predictor_by_group.png) · [Fig. 2 headline predictors by population](figures/fig2_forest_headline_predictors_by_group.png) · [Fig. 3 band feasibility](figures/fig3_band_feasibility.png)
