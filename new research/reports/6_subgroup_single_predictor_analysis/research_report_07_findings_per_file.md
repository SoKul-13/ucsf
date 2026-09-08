# Phase 6 - Consolidated findings, one section per report file

**Phase 6 / 6b consolidated findings** · AI-READI v3.0.0 · 2026-09-08
**Purpose**: a single file that collects the findings of every Phase 6 report, kept separate by source file so that each section can be read, cited or copied on its own. Nothing here is new analysis; every number is taken from the file named in the section heading. Where a section is a table-only file (02, 03, 05), the findings are drawn from that file's auto-generated interpretation blocks.

**Reading order of the underlying files**: 01 (Phase 6 narrative) → 02 (full tables by population) → 03 (band analyses) → 04 (methods and sample log) → 05 index + four cohort files (Phase 6b tables) → 06 (Phase 6b narrative).

**Common design (applies to every section)**: 31 glycaemic predictors entered one at a time as `outcome ~ covariates + predictor`; 14 outcomes in four domains (cognition, depression, home environment, wearables); Phase 5 covariates (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes); OLS with HC3 for continuous outcomes, logistic with Wald z for binary; effects per 1 SD of the predictor; repeated 3 × 10-fold cross-validation; Benjamini-Hochberg FDR applied only when the test's sample has n ≥ 500, raw p always shown alongside.

---

## File 01 - `research_report_01_subgroup_single_predictor_findings.md` (Phase 6 narrative)

### What the file is
The main Phase 6 write-up. It answers the four collaborator requests: (1) run by total / healthy / non-healthy with and without FDR, (2) each glycaemic measure entered alone, (3) FDR only on large samples, (4) whether there are enough people outside 54-250 to run band-specific versions.

### Populations

| Population | N | Composition |
| :--- | :---: | :--- |
| Total | 2,138 | Phase 5 analysis base |
| Healthy | 1,271 | 739 no diabetes + 532 pre-diabetes / lifestyle |
| Non-healthy | 867 | 639 T2D oral / non-insulin + 228 insulin |

### Findings

**F01.1 Band feasibility (request #4).** Hyperglycaemic bands are well populated (1,927 people have any time > 180; 1,407 have ≥ 1 %). Hypoglycaemia < 54 is marginal: 638 have any reading but only 56 have ≥ 1 % of time there, so only the 0/1 "any reading < 54" indicator is usable. The 54-69 band is the workable hypoglycaemia band (326 with ≥ 1 %). The 54-250 wide band is feasible but is almost the complement of > 250 (median 100 %). Over the base, 0.12 % of readings are < 54 and 2.8 % are > 250; 890 participants never leave 54-250.

**F01.2 Signal counts.** Out of 434 tests per population (about 22 expected by chance):

| Population | Raw p < 0.05 | q < 0.05 (all-tests family) | q < 0.05 (within-outcome family) |
| :--- | :---: | :---: | :---: |
| Total | 157 | 126 | 121 |
| Healthy | 73 | 18 | 47 |
| Non-healthy | 110 | 39 | 58 |

The non-healthy group carries more raw and more FDR-robust hits than the healthy group despite being smaller.

**F01.3 Cognition splits by group: level in healthy, variability in non-healthy.**
- Total: mean glucose / GMI −0.41 MoCA points per SD (q < 0.001); pooled SD −0.40; TIR +0.36; HbA1c −0.35 (all q < 0.001).
- Healthy: mean glucose −0.41 (p = 8 × 10⁻⁵, q < 0.05) and nocturnal mean −0.36 (q < 0.05) survive FDR; CV, mean/SD and SD of daily means are null.
- Non-healthy: pooled SD −0.35 (q = 0.035), daily SD −0.33 (q = 0.046), mean/SD +0.30 (q = 0.043), SD of daily means −0.34 (q = 0.040) survive FDR; no level metric does; HbA1c is borderline (p = 0.049).
- Same pattern on the memory index (healthy: mean and nocturnal glucose q < 0.05; non-healthy: SD, CV, daily SD, mean/SD all q < 0.05).
- Inference: in the healthy range cognition tracks glucose *level*; in treated diabetes it tracks *variability*. CGM SD/CV should be reported alongside mean glucose in people with diabetes; high-normal glucose is a cognitive risk marker in people without.

**F01.4 Depression is a non-healthy, instability phenomenon.**
- Total: no level or TIR metric predicts CES-D-10 total (all p > 0.2); SD of daily means +0.36 points per SD (q < 0.05) and log-OR +0.21 for CES-D-10 ≥ 10 (q < 0.001).
- Healthy: nothing (2 of 62 depression tests at raw p < 0.05, which is chance).
- Non-healthy: SD of daily means +0.59 (p = 8 × 10⁻⁴, q = 0.022) and log-OR +0.33 for ≥ 10 (p = 5 × 10⁻⁵, q = 0.007); MAG +0.53 / +0.23 (q = 0.040 for total score). The ≥ 10 result would survive Bonferroni over all 434 tests.

**F01.5 Home environment is not a function of glycaemic level.**
- Total: PM2.5 relates to HbA1c (+0.07 log units per SD, q < 0.05) and SD of daily means (+0.06, q < 0.05). Temperature, humidity, VOC: nothing.
- Healthy: PM2.5 goes weakly the other way with mean glucose (−0.05, p = 0.016); nothing survives FDR.
- Non-healthy: PM2.5 relates to HbA1c (+0.11, p = 0.009), SD of daily means (+0.11, q = 0.035) and the hypoglycaemia bands (time < 70 +0.14, q = 0.040; time 54-69 +0.13, p = 0.006). A shared socioeconomic pathway is the working explanation; an income or deprivation covariate is needed before further interpretation.

**F01.6 Wearables.**
- Resting heart rate and Garmin stress respond to glucose level in every population (total: mean glucose +1.7 bpm and +3.1 stress points per SD; TIR −1.7 / −3.0, all q < 0.001; non-healthy: 11 level/band metrics survive FDR for each).
- Steps and brisk minutes: MAG positive everywhere (+428 steps per SD, q < 0.001 total); HbA1c positive (total q < 0.05); level and TIR null; hypoglycaemia bands negative (time < 70 −231 steps in total, q < 0.05; non-healthy any reading < 54 −502 steps, p = 0.005; day-averaged time < 70 −424, q = 0.024).
- Sleep: MAG −9.0 min per SD (q < 0.001 total and healthy; non-healthy −9.3, q = 0.013); HbA1c −5.3 (total q < 0.05); pooled/daily SD ≈ −4 to −5 (q < 0.05 total).

**F01.7 Band-specific versions.**
- > 180, 181-250, > 250 mirror mean glucose (cognition, heart rate, stress all q < 0.001 in total); no new information; > 250 too sparse in healthy.
- 54-250 is nearly the complement of > 250; adds nothing.
- 54-69 and < 70 carry *different* information: no cognition / heart-rate / stress signal, but fewer steps (total q < 0.05) and, in non-healthy, higher indoor PM2.5.
- < 54: only the 0/1 indicator is usable; its *positive* MoCA association in total and healthy (raw p ≈ 0.03-0.04) is most likely a sensor-compression artefact and must not be read as protective.

**F01.8 What is important (file's own summary).**
1. 70-180 and mean glucose carry the same information for cognition and autonomic outcomes; hypoglycaemia bands carry different information and only in treated diabetes. If one band is added to the standard set, it should be 54-69 or < 70.
2. Level vs variability splits by group; any CGM-vs-HbA1c claim should be made within group.
3. Depression is a non-healthy, instability phenomenon.
4. HbA1c entered alone is never the strongest single predictor for cognition, heart rate or stress, but is the only level-type measure that relates to steps, sleep and PM2.5.
5. Multiplicity matters most in the healthy group (73 → 18).
6. Out-of-sample gains are small (largest +0.034 R² for resting heart rate); these are markers of information content, not screening tools.

**F01.9 Limitations and open clarifications.** 1,302 tests; "healthy" pools no-diabetes and pre-diabetes (dilutes the cognition gradient seen in Phase 5b); near-duplicate predictors make FDR families conservative; band metrics are zero-inflated; cross-sectional. Open items listed in the file: FDR threshold set to n ≥ 500 at user instruction; "54-250" was first implemented as a % time band, and the restriction-to-cohort reading became Phase 6b; pooled vs day-averaged headline version still to be chosen; no-diabetes-only split not repeated here.

---

## File 02 - `research_report_02_full_single_predictor_tables.md` (full tables by population)

### What the file is
Every single-predictor model for the three populations, two tables per outcome: (A) raw-scale coefficient, HC3 SE, 95 % CI, t/z, p; (B) effect per SD, both BH q families, adjusted R²/AUC, ΔAIC vs covariates-only and vs HbA1c-only, cross-validated R²/AUC. Ends with an auto-generated interpretation per population, from which these findings are taken.

### Findings

**F02.1 Total population (434 tests, 157 raw, 126 FDR-robust).**
- Best out-of-sample predictor per outcome: MoCA total → mean glucose (CV R² gain +0.015; −0.41 per SD, q = 6 × 10⁻⁷; 24 FDR-robust predictors); MoCA < 26 → GMI (OR 1.25, 23 FDR-robust); memory index → nocturnal mean (−0.21, 14 FDR-robust); CES-D-10 total → SD of daily means (only FDR-robust predictor, +0.36); CES-D-10 ≥ 10 → SD of daily means (OR 1.23) plus nocturnal time > 180 and nocturnal mean; PM2.5 → HbA1c (+0.07) and SD of daily means; steps → MAG (+428) with the < 54 / < 70 bands negative and HbA1c positive; brisk minutes → MAG and HbA1c; resting HR → % 181-250 pooled (+1.75 bpm, q = 7 × 10⁻¹⁴, 24 FDR-robust); sleep → MAG (−9.0 min, q = 2 × 10⁻⁷) with HbA1c and SD; stress → HbA1c (+3.3, 24 FDR-robust).
- Not predictable from glycaemia: indoor temperature, humidity, VOC.
- Most predictable outcomes by CV gain: resting HR +0.035, stress +0.029, sleep +0.015, MoCA +0.015.
- Families carrying the signal: CGM variability 42 FDR-robust of 112; band > 180 16 of 42; CGM level 16 of 42; HbA1c 9 of 14.
- A CGM metric beats HbA1c by > 2 AIC for 12 outcomes; the largest margins are sleep (MAG, ΔAIC −22.4), brisk minutes (MAG, −11.6), MoCA (mean glucose, −11.3), CES-D-10 ≥ 10 (SD of daily means, −10.2).

**F02.2 Healthy population (434 tests, 73 raw, 18 FDR-robust).**
- FDR-robust associations: MoCA total → GMI / mean glucose (−0.41, q = 0.007), nocturnal mean (−0.36); memory index → nocturnal mean (−0.27), GMI, mean glucose; humidity → daily % < 54 (−0.32, q = 0.036); steps and brisk minutes → MAG (+432 steps, +1.53 min); resting HR → SD of daily means (+0.93), HbA1c (+0.82), pooled SD, MAG, mean glucose, GMI (7 in all); sleep → MAG (−8.3 min); stress → HbA1c (+1.58).
- Nothing survives FDR for MoCA < 26, either depression outcome, PM2.5, temperature, VOC.
- Families: CGM level 8 FDR-robust of 42; variability 7 of 112; HbA1c 2 of 14.

**F02.3 Non-healthy population (434 tests, 110 raw, 39 FDR-robust).**
- FDR-robust associations: MoCA total → pooled SD (−0.35), SD of daily means, mean/SD, daily SD; memory index → pooled SD, CV, daily SD, mean/SD; CES-D-10 total → SD of daily means (+0.59) and MAG; CES-D-10 ≥ 10 → SD of daily means (OR 1.39, q = 0.007; the largest CV gain in the file, +0.023 AUC); PM2.5 → SD of daily means, % < 70 pooled and daily; steps → daily % < 70 (−424), daily % 54-69 (−401); resting HR → 11 level/band metrics led by % 181-250 (+1.09); sleep → MAG (−9.3); stress → 11 metrics led by HbA1c and the > 180 bands (≈ +2.5).
- Nothing survives FDR for MoCA < 26 (nominal: SD of daily means, nocturnal mean, pooled SD, mean glucose), brisk minutes, temperature, humidity, VOC.
- Families: variability 13 FDR-robust of 112; level 6 of 42; band > 180 6 of 42; HbA1c 2 of 14.

---

## File 03 - `research_report_03_glucose_band_analyses.md` (band analyses)

### What the file is
The band metrics only (% time in < 54, 54-69, < 70, 70-180, 181-250, > 180, > 250, 54-250; pooled and day-averaged; plus 0/1 indicators for < 54 and > 250), each entered alone, in all three populations, with a feasibility table per band. Interpretation blocks pool the three populations in their counts.

### Findings

**F03.1 Feasibility.** A band is feasible when ≥ 100 participants have ≥ 1 % of time in it. Feasible everywhere: 54-69, < 70, 70-180, 181-250, > 180, 54-250. Marginal: < 54 in every population (56 with ≥ 1 % in total, 35 healthy, 21 non-healthy); > 250 in the healthy group (69 with ≥ 1 %).

**F03.2 Signal per band (tests pooled over populations).**

| Band | Tests | Raw p < 0.05 | FDR-robust | Where the signal is |
| :--- | :---: | :---: | :---: | :--- |
| 70-180 (TIR) | 84 | 28 | 14 | MoCA total, MoCA < 26, memory index, resting HR (−1.68 bpm per SD, q = 6 × 10⁻¹³), stress (−3.0) |
| 54-69 | 84 | 7 | 1 | Steps only (daily % 54-69 −401 per SD, q = 0.043); PM2.5 nominal (p ≈ 0.006) |
| < 70 | 84 | 8 | 5 | Steps (daily −424, pooled −231) and PM2.5 (+0.14, q = 0.047) |
| 54-250 | 84 | 16 | 8 | MoCA total, MoCA < 26, resting HR (−1.01), stress (−1.93); the mirror image of > 250 |
| > 180 | 126 | 40 | 22 | MoCA total, MoCA < 26, memory index, CES-D-10 ≥ 10 (nocturnal > 180 only, OR 1.17), resting HR (+1.67), stress (+3.01) |
| 181-250 | 84 | 19 | 14 | MoCA total (−0.32), MoCA < 26, memory index, resting HR (+1.75, the best out-of-sample predictor in the whole phase, CV gain +0.035), stress (+3.02) |
| > 250 | 126 | 27 | 12 | MoCA total (any > 250 −0.30), MoCA < 26, resting HR (+1.28), stress (+2.27) |
| < 54 | 126 | 17 | 2 | Humidity (daily % < 54 −0.32, q = 0.036) and steps (daily % < 54 −187, q = 0.028) |

**F03.3 Interpretation.** The hyperglycaemic bands (> 180, 181-250, > 250) and TIR carry the cognition and autonomic signal and are interchangeable with mean glucose. The hypoglycaemic bands (54-69, < 70, < 54) carry none of that signal and instead relate to activity and indoor air quality. The 54-250 band re-tests > 250 with the sign reversed. No band predicts indoor temperature or VOC. The nocturnal > 180 metric is the only band metric that reaches FDR for depression (≥ 10 threshold) in the total population.

---

## File 04 - `research_report_04_methods_and_sample_log.md` (methods and sample log)

### What the file is
The execution log, sample construction, model specification, predictor and outcome dictionaries, and the definition of pooled vs day-averaged metrics. It contains no results; its findings are the design facts that condition every other file.

### Findings

**F04.1 Sample construction (identical to Phase 5).** 2,280 AI-READI participants → 2,216 with ≥ 3 valid CGM days (valid day = ≥ 70 % of 288 readings; 3-12 days, median 9) → 2,153 with laboratory HbA1c → 2,153 with the four core CGM metrics → **2,138** with complete covariates. Covariate losses: BMI 4, education 11. Wearable losses: 248 with no Garmin record plus 18 with < 3 wear-days. Environmental losses: 38 without ≥ 1 h of sensor data.

**F04.2 Per-outcome N.** Cognition 2,138 (857 MoCA < 26 events); depression 2,135 (403 CES-D-10 ≥ 10 events); environment 2,100; steps and brisk minutes 1,872; resting HR 1,877; sleep 1,893; stress 1,879. Every model for a given outcome is fitted on the same participants (list-wise deletion on the union of variables used); predictor-specific losses are rare and visible in the n column. Membership per participant per outcome is in `data/analysis_sample_membership_by_outcome.csv`.

**F04.3 Model rules.** One predictor at a time; no combined HbA1c + CGM models in this phase. Band predictors are skipped when fewer than 30 participants in the sample have any time in the band. ΔAIC vs covariates-only and vs HbA1c-only on the same rows. Repeated 3 × 10-fold CV. Four FDR families stored: all tests in the population, all predictors within one outcome, all outcomes within one predictor, all tests within one band. Informational q stored for tests below the n ≥ 500 rule.

**F04.4 Pooled vs day-averaged.** Pooled = one statistic over all valid readings of the wear (days with more readings weigh more; partial days included). Day-averaged = statistic per valid day, then unweighted mean over valid days (partial days excluded; within-day SD not inflated by day-to-day drift). The two correlate at ρ ≈ 0.98-0.99 for TIR and SD and give the same conclusions. SD of daily means is the between-day metric. "Any reading < 54 / > 250" are 0/1 indicators over the whole wear.

**F04.5 Predictor and outcome dictionaries.** 31 predictors: HbA1c; 3 level metrics (mean, GMI, nocturnal mean); 8 variability metrics (pooled SD, daily SD, CV, mean/SD, daily mean/SD, MAG, daily range, SD of daily means); 2 TIR forms; 17 band metrics. 14 outcomes across cognition (3), depression (2), home environment (4), wearables (5). Column names are listed in the file for joining to the CSVs.

**F04.6 How to read result files.** Table A bold = raw p < 0.05; table B bold = q < 0.05 under the rule. A predictor matters for *prediction* only when the CV gain is positive; a gain below ~0.01 is negligible.

---

## File 05 (index) - `research_report_05_glucose_cohort_tables.md` (Phase 6b cohort index)

### What the file is
The entry point for Phase 6b. It defines the actual-value cohorts, gives their sizes and feasibility, the significance counts per cohort × population, links to the four per-cohort table files, and holds the auto-generated interpretation for the *total* population of each cohort.

### Findings

**F05.1 Cohort definitions and feasibility.**

| Cohort | Definition | N | Healthy | Non-healthy | Feasible? |
| :--- | :--- | :---: | :---: | :---: | :--- |
| normal_70_180 | every reading within 70-180 | 39 | 30 | 9 | **No** (fewer than 100; 6 CES-D ≥ 10 and 10 MoCA < 26 events) |
| near_normal_99 | ≥ 99 % of readings within 70-180 | 454 | 393 | 61 | Yes (substitute for the above; non-healthy stratum too small) |
| within_54_250 | no reading < 54 and none > 250 | 890 | 685 | 205 | Yes |
| hypo_below_54 | ≥ 1 reading < 54 | 638 | 408 | 230 | Yes |
| hyper_above_250 | ≥ 1 reading > 250 | 795 | 244 | 551 | Yes |

Overlap: 453 hypo-only, 610 hyper-only, 185 both, 890 neither. Only 1.8 % of participants never leave 70-180 over the wear. Stricter definitions: ≥ 1 % of time < 54 leaves 56 (not possible); ≥ 1 % of time > 250 leaves 461 (possible on request).

**F05.2 Significance counts (raw p < 0.05 / q < 0.05; bold q = rule-based where n ≥ 500, *i* = informational only).**

| Cohort | Tests | Total | Healthy | Non-healthy |
| :--- | :---: | :---: | :---: | :---: |
| near_normal_99 | 392 (96 in non-healthy) | 26 / 0 *i* | 26 / 0 *i* | 0 / 0 |
| within_54_250 | 322 | 73 / **22** | 38 / **10** | 30 / 0 *i* |
| hypo_below_54 | 420 | 144 / **66** | 31 / 0 *i* | 81 / 10 *i* |
| hyper_above_250 | 420 | 117 / **50** | 49 / 10 *i* | 70 / **2** rule-based, 4 *i* |

Within 54-250 and near-normal have fewer tests because the < 54 and > 250 band predictors are constant there and are skipped. Only cohort-populations with n ≥ 500 meet the FDR rule (within-54-250 total and healthy, hypo total, hyper total, and the hyper non-healthy outcomes whose sample reaches 500); the others show an informational q only. Same convention as the counts table in file 06.

**F05.3 Total-population interpretation per cohort** (details in the per-cohort sections below): near-normal has no FDR-robust test and only 26 raw hits (about 20 expected); within-54-250 keeps the level→cognition and level→autonomic signal (12 of 15 level-metric hits FDR-robust); hypo-exposed has the most signal per test (66 FDR-robust) with HbA1c the best out-of-sample predictor for all three cognition outcomes; hyper-exposed has the strongest autonomic signal of any cohort (stress CV gain +0.042 via HbA1c, resting HR +0.039 via % 181-250).

---

## File 05a - `research_report_05_cohort_near_normal_99.md` (≥ 99 % of readings within 70-180; N = 454)

### Findings

**F05a.1 Total (392 tests, 26 raw, 0 FDR-robust).** Level metrics stop predicting cognition, heart rate and stress (HbA1c, mean glucose, SD, CV, TIR all p > 0.05 for MoCA total and MoCA < 26). What remains at raw p < 0.05: MAG → CES-D-10 ≥ 10 (OR 1.53 per SD, p = 0.001, CV AUC gain +0.037) and CES-D-10 total (p = 0.005); SD of daily means → memory index (−0.34, p = 0.007); HbA1c → sleep (−10.5 min, p = 0.001, CV gain +0.027); time 54-69 → longer sleep (+9.2 min, p = 0.004); TIR → fewer brisk minutes (−1.6, p = 0.004); pooled % < 54 → resting HR (+0.72, p = 0.011); daily range → indoor temperature (−0.24, p = 0.012).

**F05a.2 Healthy stratum (393; 392 tests, 26 raw, 0 FDR-robust).** Same picture as total: MAG → CES-D-10 ≥ 10 (CV gain +0.045); HbA1c → sleep (−11.4, p = 0.001); TIR → brisk minutes; nothing for cognition.

**F05a.3 Non-healthy stratum (61; 96 estimable tests, 0 raw).** Uninformative; most models fail or fall below the participant / event floor.

**F05a.4 Inference.** Inside the near-normal range glucose *level* carries no information about cognition or autonomic tone, so those gradients in Phases 5/6 come from movement across the 70-180 boundary. Rapid glucose change (MAG) still tracks depressive symptoms and HbA1c still tracks sleep, consistent with Phase 5b's conclusion that HbA1c's behavioural associations are not about sensor glucose. No result here survives the informational FDR.

---

## File 05b - `research_report_05_cohort_within_54_250.md` (no reading < 54 and none > 250; N = 890)

### Findings

**F05b.1 Total (322 tests, 73 raw, 22 FDR-robust).**
- Cognition: mean glucose / GMI −0.38 MoCA points per SD (p = 3 × 10⁻⁴, q = 0.011), nocturnal mean −0.37 (q = 0.013); MoCA < 26 OR 1.33 per SD nocturnal mean (q = 0.011), 1.31 for mean glucose and GMI; HbA1c −0.28 (p = 0.007); TIR +0.23 (p = 0.043); memory index nominal only.
- Resting HR: 10 FDR-robust predictors led by mean glucose / GMI +1.16 bpm (q = 0.002), nocturnal mean +1.15, daily % 181-250 and % > 180 +0.93, HbA1c +1.02 (q = 0.024). Stress: nocturnal mean +1.94, mean glucose / GMI +1.88 (q ≈ 0.04).
- Activity: MAG +557 steps (q = 0.011) and +1.85 brisk minutes (q = 0.002); HbA1c +364 steps (p = 0.019).
- Sleep: HbA1c −7.1 min (p = 0.006), MAG −7.1 (p = 0.015); nothing FDR-robust.
- Depression: nothing in total (CES-D-10 total all p > 0.05; ≥ 10 nominal only for nocturnal > 180 and nocturnal mean).
- Environment: relative humidity rises with pooled SD (+0.59 % per SD, q = 0.048); PM2.5, temperature, VOC null.
- Families: CGM level 12 FDR-robust of 42; variability 4 of 112; band > 180 2 of 42; HbA1c 1 of 14. Largest CV gains: brisk minutes +0.020 (MAG), resting HR +0.018 (GMI), steps +0.016 (MAG), MoCA +0.015 (GMI).

**F05b.2 Healthy stratum (685; 322 tests, 38 raw, 10 FDR-robust).** TIR −0.73 bpm (q < 0.05) and time > 180 +0.83 bpm (p = 6.5 × 10⁻⁵, q < 0.05) for resting HR; MAG for brisk minutes (CV gain +0.025) and steps (+0.019); nocturnal > 180 for CES-D-10 ≥ 10 (CV gain +0.012). Families: band > 180 3 FDR-robust of 42; variability 2 of 112; TIR 2 of 28.

**F05b.3 Non-healthy stratum (205; 322 tests, 30 raw, 0 under the rule).** Variability is as strong as level for cognition: pooled SD −0.55 (p = 0.011), mean glucose −0.49 (p = 0.011); nocturnal mean is the best out-of-sample predictor for MoCA total (CV gain +0.048) and MoCA < 26 (+0.031). MAG → CES-D-10 ≥ 10 log-OR +0.56 (p = 0.002; CV AUC gain +0.087, the largest in Phase 6b). Hypothesis-generating only.

**F05b.4 Inference.** Removing everyone with a severe excursion does not remove the cognition and autonomic gradients; moderate hyperglycaemia (181-250) and level within 54-250 are enough. This is the cleanest demonstration that the Phase 5/6 associations are not driven by a tail of extreme values.

---

## File 05c - `research_report_05_cohort_hypo_below_54.md` (≥ 1 reading < 54; N = 638)

### Findings

**F05c.1 Total (420 tests, 144 raw, 66 FDR-robust; the most signal per test of any cohort).**
- Cognition: HbA1c is the best out-of-sample predictor for all three outcomes (MoCA total −0.52 per SD, p = 1.7 × 10⁻⁵, q = 0.002, CV gain +0.024; MoCA < 26 OR 1.43, q = 0.008; memory index −0.29, q = 0.038). 19 FDR-robust predictors for MoCA total, including TIR +0.47, mean glucose −0.44, pooled SD −0.44, time > 180 −0.45, time > 250 −0.42.
- Depression: 11 FDR-robust predictors for CES-D-10 total and 19 for CES-D-10 ≥ 10. Nocturnal > 180 is the best out of sample (+0.74 points, q = 0.003; OR 1.54, q = 0.001, CV AUC gain +0.027); time > 250 +0.64 (q = 0.001); time 54-250 −0.61; TIR −0.57; SD of daily means OR 1.43; nocturnal mean OR 1.44.
- Sleep: MAG −12.1 min (q = 0.002), HbA1c −8.5 (q = 0.023), daily % > 250 −7.1 (q = 0.036).
- Resting HR: mean/SD −1.07 (q = 0.023), % 181-250 +1.19, SD of daily means +0.98. Stress: mean/SD −2.11, SD of daily means +1.87, % 181-250 +2.17 (all q < 0.05).
- Activity: nothing (steps and brisk minutes all p > 0.05). Environment: PM2.5 nominal for HbA1c (p = 0.024); temperature nominal for the hypoglycaemia bands; humidity nominal for % < 54.
- Families: variability 16 FDR-robust of 112; band > 180 9 of 42; TIR 8 of 28; HbA1c 5 of 14.

**F05c.2 Healthy stratum (408; 420 tests, 31 raw, 0 under the rule).** Cognition null (MoCA total all p > 0.14). Nocturnal > 180 → CES-D-10 total +0.81 (p = 0.001) and ≥ 10 OR 1.57 (p = 0.001); the > 180 / 181-250 bands p ≈ 0.003 for ≥ 10. MAG → sleep −11.9 min (p = 3.4 × 10⁻⁴). Mean glucose → *lower* PM2.5 (p = 0.020). Steps, brisk minutes, resting HR, stress: nothing.

**F05c.3 Non-healthy stratum (230; 420 tests, 81 raw, 0 under the rule).** Almost everything moves. Cognition: HbA1c −0.54 (p = 0.015), OR 1.52 for MoCA < 26 (p = 0.010); CV −0.52 on the memory index (p = 0.003, CV gain +0.028). Depression: time > 250 → CES-D-10 +1.00 per SD (p = 1.4 × 10⁻⁵, CV gain +0.044); nocturnal > 180 → ≥ 10 OR 1.86 (p = 1.3 × 10⁻⁴, CV AUC gain +0.057); SD of daily means log-OR +0.63 (p = 3.5 × 10⁻⁴). PM2.5 rises with the hypoglycaemia bands (daily % < 70 +0.23, p = 0.016). Sleep: HbA1c −14.9 min (p = 6 × 10⁻⁴).

**F05c.4 Inference.** People who dip below 54 *and* also run high are the ones whose glycaemia relates to mood and cognition; 185 of the 638 also exceed 250 and are overwhelmingly treated diabetes. The signal is two-directional instability, the profile of insulin or sulfonylurea treatment with poor control. For a healthy person, a few readings below 54 (typically nocturnal compression lows) carry no cognitive or mood information.

---

## File 05d - `research_report_05_cohort_hyper_above_250.md` (≥ 1 reading > 250; N = 795)

### Findings

**F05d.1 Total (420 tests, 117 raw, 50 FDR-robust).**
- Resting HR and stress dominate: 19 FDR-robust predictors for resting HR led by % 181-250 +1.88 bpm (q = 9 × 10⁻⁶, CV gain +0.039), TIR −1.90, HbA1c +1.73, mean glucose +1.82 (p = 3 × 10⁻⁷); 18 for stress led by HbA1c +3.98 (q = 9.5 × 10⁻⁷, CV gain +0.042), TIR −3.81, time > 180 +3.80.
- Cognition: MoCA total → pooled SD −0.36 (q = 0.041), mean glucose / GMI −0.37, time > 180 −0.36, TIR +0.36 (all q < 0.05); MoCA < 26 → TIR (OR 0.80), time > 180 (OR 1.24); memory index nominal only.
- Depression: SD of daily means is the only FDR-robust predictor (CES-D-10 total +0.55, q = 0.034; ≥ 10 OR 1.36, q = 0.007, CV AUC gain +0.019). Level metrics null.
- PM2.5: SD of daily means +0.12 (q = 0.017) and HbA1c +0.12 (q = 0.044); mean glucose and TIR nominal.
- Sleep: MAG −10.0 min (q = 0.001); HbA1c −6.1 and pooled SD −5.4 nominal.
- Activity: hypoglycaemia bands nominally negative for steps (daily % < 70 −362, p = 0.006, q = 0.050) and brisk minutes; nothing FDR-robust.
- Families: variability 12 FDR-robust of 112; level 8 of 42; band > 180 8 of 42; HbA1c 3 of 14.

**F05d.2 Healthy stratum (244; 420 tests, 49 raw, 0 under the rule).** The memory index falls steeply with mean glucose (−0.51 per SD, p = 4 × 10⁻⁴, CV gain +0.037) and time > 250 (−0.45, p = 5 × 10⁻⁴); MoCA total with mean glucose (CV gain +0.036). Stress rises with HbA1c (+2.65, p = 0.022). MAG → sleep (CV gain +0.041). Depression null. Small stratum (215-244); hypothesis-generating.

**F05d.3 Non-healthy stratum (551; 420 tests, 70 raw, 2 FDR-robust under the rule).** The two rule-robust tests are SD of daily means for both depression outcomes (CES-D-10 +0.79, p = 3 × 10⁻⁴; ≥ 10 log-OR +0.44, p = 4 × 10⁻⁵, CV AUC gain +0.038). Also: mean glucose +1.05 bpm (p = 0.009); stress +2.7 (p = 0.002); PM2.5 with SD of daily means +0.14 (p = 0.0012) and HbA1c +0.13 (p = 0.016); cognition tracks variability (pooled SD −0.31, p = 0.036; MAG −0.34, p = 0.031) more than level.

**F05d.4 Inference.** In people who reach > 250 the autonomic signal is the strongest of any cohort, consistent with sympathetic activation at high glucose. The depression signal is again day-to-day instability rather than level. The PM2.5-HbA1c association, absent in the within-54-250 cohort, re-emerges here, which points to the poorly controlled, socioeconomically disadvantaged tail as its carrier.

---

## File 06 - `research_report_06_glucose_cohort_findings.md` (Phase 6b narrative)

### What the file is
The interpretation of the Phase 6b cohort tables (files 05, 05a-05d): why the cohorts exist, which were and were not possible, the findings by cohort, and the cross-cohort conclusions. It also repeats the pooled vs day-averaged definitions.

### Why the cohorts exist
Phase 6 could show *that* glucose level, variability and TIR relate to cognition, autonomic tone and mood, but not *where* on the glucose scale the signal lives, because the band metrics used as predictors are zero-inflated (% time < 54 is unusable). Phase 6b flips the design: the bands define *who is in the sample*, and the full Phase 6 grid is rerun inside each group. This isolates one part of the glucose range at a time and tests whether the Phase 6 gradients survive the removal of the tails.

### Findings

**F06.1 What was not possible.** The planned "normal range only" cohort (every reading within 70-180) has 39 people, 6 CES-D ≥ 10 events and 10 MoCA < 26 events; no covariate-adjusted model can be fitted. The ≥ 99 % TIR cohort (454) is the substitute, and its non-healthy stratum (61) is uninformative. A stricter hypoglycaemia cohort (≥ 1 % of time < 54) has 56 people and was not run; a stricter hyperglycaemia cohort (≥ 1 % of time > 250, 461 people) could be run on request.

**F06.2 Per-cohort headline.** Near-normal: level stops predicting cognition and autonomic tone; MAG still tracks depression; HbA1c still tracks sleep; nothing FDR-robust. Within 54-250: cognition and autonomic gradients intact (mean glucose −0.38 MoCA, +1.16 bpm, +1.88 stress, all q < 0.05); MAG → activity; no depression signal in total. Hypo-exposed: most signal per test (144 raw, 66 robust); depression concentrated here and in its non-healthy members; cognition signal comes only from the non-healthy members. Hyper-exposed: strongest autonomic signal of any cohort; depression = between-day SD; PM2.5-HbA1c re-emerges.

**F06.3 Cross-cohort conclusions (the file's section 3).**
1. The cognition and autonomic gradients survive restriction to 54-250 but disappear inside 70-180. They are carried by movement across the 180 boundary, not by the extreme tails and not by variation inside the normal range. Time > 180 is the working exposure; > 250 adds little.
2. Depression tracks glycaemic instability, and only where instability exists: between-day SD and MAG in the hypo- and hyper-exposed cohorts (strongest in their non-healthy members, p ≈ 10⁻⁴-10⁻⁵); MAG alone even inside the near-normal cohort; nothing in the within-54-250 total population.
3. Hypoglycaemia exposure in a healthy person is not a risk marker. In the 408 healthy participants with a reading < 54, glycaemic measures predict nothing; in the 230 non-healthy participants with such a reading they predict almost everything. "< 54" marks treatment-related instability, not harm from the low reading itself.
4. HbA1c keeps its behavioural associations in every cohort (shorter sleep in all four; more steps within 54-250) even where sensor glucose is uninformative, consistent with the Phase 5b discordance result.
5. Statistical caution: FDR-robust counts under the n ≥ 500 rule are 66 (hypo total), 50 (hyper total), 22 (within-54-250 total), 10 (within-54-250 healthy), 2 (hyper non-healthy) and 0 (near-normal). Strata of n ≈ 200-250 are hypothesis-generating; the near-normal non-healthy stratum is uninformative.

**F06.4 FDR rule statement (checked 2026-09-08).** Section 1 of file 06 states the rule as BH when the test's sample has n ≥ 500, lists the cohort-populations that meet it (within-54-250 total and healthy; hypo total; hyper total; part of the hyper non-healthy stratum) and marks the others as informational q only. This matches section 3 of the same file, the file 05 index, files 01-04 and the generated tables. An earlier draft of section 1 gave the rule as n ≥ 1,000 with "not applied" everywhere; that wording is gone.

---

## Cross-file synthesis (what the Phase 6 set says as a whole)

- **Where the signal lives on the glucose scale.** Crossing 180 into moderate hyperglycaemia carries the cognition and autonomic signal (files 01, 03, 05b, 06). Variation inside 70-180 carries none of it (05a, 06). The > 250 tail adds nothing beyond > 180 (01, 03, 05d).
- **Level vs variability by group.** Healthy: level → cognition and heart rate. Non-healthy: variability → cognition and depression; level → heart rate and stress (01, 02). The cohorts reproduce this split inside each glucose range (05b non-healthy, 05d non-healthy).
- **Depression.** Instability (SD of daily means, MAG), non-healthy, and only where instability exists (01, 02, 05c, 05d, 06). Survives Bonferroni within the non-healthy group (01).
- **Hypoglycaemia.** The 54-69 / < 70 bands relate to fewer steps and higher indoor PM2.5 in treated diabetes, not to cognition (01, 03). A reading < 54 in a healthy person carries no information (05c, 06); in a treated person it marks two-directional instability.
- **HbA1c.** Never the strongest predictor of cognition, heart rate or stress when entered alone, but the one measure that relates to sleep, steps and PM2.5 in every population and every cohort (01, 02, 05a-05d, 06).
- **Prediction.** Out-of-sample gains never exceed about +0.04 R² (resting HR, stress); these are markers of information content, not screening tools (01, 02, 04).
- **Multiplicity.** Raw hits shrink most in the healthy group (73 → 18). Cohort strata under 500 have no rule-based q and should be read as hypothesis-generating (05, 06). All files now state the same n ≥ 500 rule.

*Source files*: [01](research_report_01_subgroup_single_predictor_findings.md) · [02](research_report_02_full_single_predictor_tables.md) · [03](research_report_03_glucose_band_analyses.md) · [04](research_report_04_methods_and_sample_log.md) · [05 index](research_report_05_glucose_cohort_tables.md) · [05a near-normal](research_report_05_cohort_near_normal_99.md) · [05b within 54-250](research_report_05_cohort_within_54_250.md) · [05c hypo < 54](research_report_05_cohort_hypo_below_54.md) · [05d hyper > 250](research_report_05_cohort_hyper_above_250.md) · [06](research_report_06_glucose_cohort_findings.md)
