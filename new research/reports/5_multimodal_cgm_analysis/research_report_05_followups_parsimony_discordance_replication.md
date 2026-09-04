# Follow-up analyses: a parsimonious CGM pair, HbA1c-CGM discordance, split-sample replication of the depression signal, dose-response across the glycaemic spectrum, and the stability of 10-day CGM metrics

**Phase 5b research report** · builds on [research_report_01](research_report_01_cgm_vs_hba1c_comorbidity_prediction.md) section 5.5 · AI-READI v3.0.0 · 2026-09-04
**Code**: `src/5_multimodal_cgm_analysis/run_phase5_followups.py` (after `extract_multimodal_dataset.py`) · result CSVs `data/followup_*.csv` · figures `figures/fig7-fig10`
**Sample**: the same analysis base as report 01 (N = 2,138; ≥ 3 valid CGM days, HbA1c, complete covariates); depression models N = 2,135; wearable models N = 1,872-1,893; environment N = 2,100.

---

## Abstract

Report 01 concluded that CGM and HbA1c carry partly different information and recommended five follow-ups. Four were feasible in the cross-sectional data and are reported here; the fifth (lagged CGM) is approximated by a within-window split-half analysis.

**(A) A two-metric CGM summary is enough.** Mean glucose plus average daily SD (VIF ≤ 3.8, versus up to 11.4 in the four-metric block) reproduces every result of the four-metric block: it adds to HbA1c for MoCA total (F(2) = 7.1, p = 8.2 × 10⁻⁴, q = 0.006) and resting heart rate (p = 9.1 × 10⁻⁴, q = 0.006), and cross-validated performance is indistinguishable from the block (MoCA R² 0.105 vs 0.105; resting HR 0.184 vs 0.185). Substituting TIR for daily SD gives the same answers. The remaining two metrics add small in-sample increments for resting heart rate and stress (p = 0.02-0.04) that do not survive cross-validation.

**(B) Discordance is the active ingredient of HbA1c's "extra" information.** The haemoglobin glycation index (HGI: HbA1c residualised on mean glucose; SD 0.63%; r = 0.999 with HbA1c − GMI) predicted, holding mean glucose constant, indoor PM2.5 (+0.084 log units per SD, q = 0.003), shorter sleep (−5.0 min per SD, q = 0.003), higher Garmin stress (+1.26, q = 0.003), higher resting heart rate (+0.48 bpm, q = 0.028), more steps (+295, q = 0.04) and more brisk minutes (q = 0.028), but not cognition (q ≥ 0.7) or depression (q ≥ 0.3). Red-cell indices (haemoglobin, MCV, RDW, haematocrit) explain only 8% of HGI variance and adjusting for them leaves every HGI effect intact. Exactly as predicted in report 01, glycaemic level (mean glucose) owns cognition and the autonomic signals, whereas the non-glucose component of HbA1c owns the behavioural and exposure outcomes.

**(C) The between-day variability → depression signal replicates.** Using the AI-READI recommended split as a discovery/hold-out partition (n = 1,483 / 652), the SD of daily mean glucose predicted CES-D-10 ≥ 10 in discovery (log-OR 0.21 per SD, p = 0.0013) and in hold-out (0.22 per SD, p = 0.020; OR 1.25). For the continuous score the hold-out estimate was the same size (0.35 vs 0.39 points per SD) but only borderline (p = 0.10 two-sided). The effect strengthens when HbA1c, mean glucose and within-day SD are held constant (0.51 points per SD, p = 8 × 10⁻⁴) and is not explained by sleep regularity (≈ 5% mediated). Nocturnal mean glucose did not replicate convincingly.

**(D) The gradients are a phenomenon of the non-diabetic range.** With four diabetes groups, the mean-glucose slope on MoCA was −1.10 points per pooled SD in participants without diabetes (p = 4 × 10⁻⁶) and 0.00 in insulin-treated diabetes (interaction p = 4 × 10⁻⁴); restricted to no diabetes and HbA1c < 6.5% (n = 1,227) the slope was −0.79 (p = 3.5 × 10⁻⁴). Splines show MoCA falling steeply up to HbA1c ≈ 7% and mean glucose ≈ 175 mg/dL and flat beyond (non-linearity p = 0.014 for HbA1c), and resting heart rate rising to a plateau above ≈ 200 mg/dL (p ≤ 0.0025 for all three predictors).

**(E) Ten-day CGM metrics are stable.** Split-half ICC(2,1) was 0.92 for mean glucose, 0.87 for daily SD and 0.89 for TIR; the first and second halves of the wear predicted outcomes equally well, so the window, not recency, is what the metrics capture.

---

## A. A parsimonious CGM pair

**Question.** Can mean glucose + average daily SD replace the four-metric block without losing information, and does TIR work as the second metric?

**Expected.** Report 01 found the four metrics highly collinear (VIF up to 11.4) and that only mean glucose and daily SD added to HbA1c individually.

**Results.** Specifications (all on the same sample per outcome): M1 HbA1c; P2 mean glucose + daily SD; P2T mean glucose + daily TIR; P3 HbA1c + pair; M2 four metrics; M3 HbA1c + four metrics. VIF in P3 was 2.9 (HbA1c), 3.8 (mean glucose) and 2.5 (daily SD) for every outcome.

| Outcome | Pair adds beyond HbA1c (P3 vs M1) | HbA1c adds beyond pair (P3 vs P2) | Other two metrics add beyond pair (M2 vs P2) | CV R²/AUC: M1 / P2 / P2T / M2 |
| :--- | :---: | :---: | :---: | :---: |
| MoCA total | **p = 8.2 × 10⁻⁴, q = 0.006, ΔAIC −10.3** | p = 0.79 | p = 0.09 | 0.100 / 0.105 / 0.105 / 0.105 |
| MoCA < 26 | p = 0.026, q = 0.12 | p = 0.74 | p = 0.35 | 0.667 / 0.669 / 0.669 / 0.668 |
| MoCA memory index | p = 0.11 | p = 1.0 | p = 0.25 | 0.065 / 0.065 / 0.065 / 0.064 |
| CES-D-10 total | p = 0.72 | p = 0.14 | p = 0.20 | 0.092 / 0.090 / 0.092 / 0.090 |
| CES-D-10 ≥ 10 | p = 0.95 | p = 0.21 | p = 0.69 | 0.668 / 0.668 / 0.667 / 0.665 |
| Indoor PM2.5 (log) | p = 0.034, q = 0.12 | **p = 2.7 × 10⁻⁵, q = 4 × 10⁻⁴, ΔAIC −15.8** | p = 0.007 | 0.144 / 0.138 / 0.142 / 0.140 |
| Indoor temperature | p = 0.84 | p = 0.41 | p = 0.63 | 0.287 / 0.286 / 0.287 / 0.285 |
| Indoor humidity | p = 0.56 | p = 0.72 | p = 0.15 | 0.231 / 0.231 / 0.232 / 0.231 |
| Indoor VOC | p = 0.26 | p = 0.25 | p = 0.31 | 0.029 / 0.029 / 0.028 / 0.028 |
| Steps / day | p = 0.30 | **p = 0.002, q = 0.009** | p = 0.053 | 0.128 / 0.123 / 0.123 / 0.123 |
| Brisk minutes | p = 0.43 | **p = 0.003, q = 0.009** | p = 0.024 | 0.150 / 0.145 / 0.145 / 0.146 |
| Resting heart rate | **p = 9.1 × 10⁻⁴, q = 0.006, ΔAIC −10.1** | p = 0.020, q = 0.046 | p = 0.026 | 0.181 / 0.184 / 0.183 / 0.185 |
| Sleep duration | p = 0.15 | **p = 0.003, q = 0.009** | p = 0.28 | 0.027 / 0.023 / 0.022 / 0.022 |
| Garmin stress | p = 0.052 | **p = 0.003, q = 0.009** | p = 0.019 | 0.121 / 0.119 / 0.118 / 0.121 |

Within P3, the pair's contribution to MoCA is shared (mean glucose −0.26 per SD, p = 0.06; daily SD −0.17, p = 0.14; HbA1c −0.03, p = 0.79), which is why the joint test, not the individual terms, is the right summary. For resting heart rate all three terms retain independent information (HbA1c +0.74 bpm per SD, p = 0.016; mean glucose +0.84, p = 0.029; daily SD +0.40, p = 0.20). For sleep duration the pair reveals a suppression pattern: with HbA1c held constant, mean glucose is associated with *longer* sleep (+5.8 min per SD, p = 0.049) while HbA1c predicts shorter sleep (−7.9 min, p = 9 × 10⁻⁴), which foreshadows the discordance analysis below.

**Interpretation.** The two-metric summary loses nothing that matters, removes the collinearity that made the four-metric coefficients uninterpretable, and can be used as the default CGM block in future comorbidity models. TIR is an acceptable substitute for daily SD (near-identical fit) but not an addition. The small in-sample increments of the mean/SD ratio and TIR beyond the pair for heart rate and stress (p ≈ 0.02-0.04) do not appear out of sample (Fig. 10) and should not be chased.

![Fig 10](figures/fig10_pair_vs_block_cv.png)

---

## B. HbA1c-CGM discordance as a predictor

**Question.** Is the information HbA1c holds beyond CGM (for activity, sleep and PM2.5) carried by the part of HbA1c that CGM does *not* explain?

**Expected.** Report 01 predicted that discordance would be the active ingredient for behavioural and exposure outcomes and irrelevant for cognition and autonomic outcomes.

**Definition.** HGI = HbA1c − (2.75 + 0.0249 × mean glucose), the residual of the cohort regression (R² = 0.64). Its SD is 0.63 HbA1c-percentage points, and it is interchangeable with the glycation gap HbA1c − GMI (r = 0.999).

**What HGI is made of.** Rank correlations: RDW +0.21, MCV −0.17, education −0.11, BMI +0.10, age +0.07, haemoglobin −0.05; within-day glucose SD 0.01 and CGM wear days −0.04 (so HGI is not a CGM-quality artefact). A multivariable model of HGI on age, BMI, haemoglobin, MCV, RDW, haematocrit, creatinine, kidney disease, diabetes status, insulin use, site and education explained only 8.4% of its variance (haematocrit +0.22 SD per SD, haemoglobin −0.19, MCV −0.06, diabetes +0.17 points, kidney disease −0.14 points, BMI and age small positives). Most of the discordance is therefore unexplained by the red-cell indices available here.

**Results.** Each outcome was regressed on covariates + mean glucose + HGI, then additionally on haemoglobin, MCV and RDW (Fig. 8; `followup_B_discordance_effects.csv`).

| Outcome | HGI effect per SD (covariates + mean glucose) | q | After red-cell adjustment | Mean glucose in the same model |
| :--- | :---: | :---: | :---: | :---: |
| MoCA total | −0.03 points | 0.71 | −0.02 (q = 0.96) | −0.41 per SD, p < 10⁻⁴ |
| MoCA < 26 | log-OR +0.03 | 0.71 | +0.02 (q = 0.96) | +0.22, p < 10⁻⁴ |
| MoCA memory index | −0.01 | 0.92 | 0.00 | −0.20, p = 6 × 10⁻⁴ |
| CES-D-10 total | +0.16 | 0.32 | +0.16 (q = 0.30) | +0.08, p = 0.50 |
| CES-D-10 ≥ 10 | log-OR +0.07 | 0.33 | +0.07 (q = 0.30) | +0.09, p = 0.08 |
| Indoor PM2.5 (log) | **+0.084** | **0.003** | +0.086 (q = 0.005) | +0.03, p = 0.25 |
| Steps / day | **+295** | **0.04** | +283 (q = 0.053) | +182, p = 0.16 |
| Brisk minutes | **+0.89** | **0.028** | +0.87 (q = 0.048) | +0.55, p = 0.13 |
| Resting heart rate | **+0.48 bpm** | **0.028** | +0.43 (q = 0.051) | +1.73, p < 10⁻⁴ |
| Sleep duration | **−5.0 min** | **0.003** | −4.6 (q = 0.007) | −2.8, p = 0.08 |
| Garmin stress | **+1.26** | **0.003** | +1.17 (q = 0.009) | +3.17, p < 10⁻⁴ |
| Temperature / humidity / VOC | null | ≥ 0.57 | null | null |

**Interpretation.** The prediction holds. Cognition is entirely a function of glycaemic level (mean glucose) and has no discordance component; the behavioural and exposure outcomes (activity, sleep duration, PM2.5) are a function of discordance and not of level; the autonomic outcomes respond to both, with level dominant. Because red-cell indices explain little of HGI and do not attenuate its effects, the discordance signal is unlikely to be a haematological artefact. The two leading candidates are (i) a longer integration window (HbA1c reflects the months before the visit, during which activity, sleep and air quality varied) and (ii) shared upstream determinants, notably socioeconomic position, of which HGI's negative correlation with education (ρ = −0.11) is a hint. A direct income or neighbourhood-deprivation measure, or a second CGM wear months later, would separate these. Practically, studies using HbA1c as a marker of "glycaemia" in relation to lifestyle exposures should be aware that a substantial part of what they detect is not glucose.

![Fig 8](figures/fig8_hgi_discordance_effects.png)

---

## C. Depression: replication of the between-day variability signal and the role of sleep regularity

**Question.** Does the exploratory finding that the SD of daily mean glucose predicts depressive symptoms replicate in a held-out sample, and is it explained by irregular sleep?

**Design.** Discovery = the AI-READI *train* split (n = 1,483 with CES-D-10), hold-out = *val* + *test* (n = 652). Pre-specified predictors: SD of daily means and nocturnal mean (from the exploratory sweep). Sleep-regularity metrics (SD across nights of sleep midpoint, sleep onset and sleep duration; sleep efficiency; duration) and between-day step variability were added as candidate explanations. Same covariates as the primary analysis.

**Results.**

| Predictor | CES-D-10 ≥ 10: discovery | hold-out | Verdict | CES-D-10 total: discovery | hold-out | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| SD of daily means | log-OR +0.21 (p = 0.0013) | **+0.22 (p = 0.020)** | replicated | +0.39 pts (p = 0.002) | +0.35 (p = 0.10) | same size, underpowered |
| Nocturnal mean | +0.13 (p = 0.039) | +0.16 (p = 0.094) | borderline | +0.20 (p = 0.14) | +0.04 (p = 0.87) | no |
| Sleep-duration SD | +0.14 (p = 0.047) | +0.21 (p = 0.037) | replicated | +0.43 (p = 0.001) | +0.23 (p = 0.26) | partial |
| Sleep-onset SD | +0.07 (p = 0.35) | +0.21 (p = 0.042) | – | +0.36 (p = 0.011) | +0.23 (p = 0.25) | partial |
| Sleep-midpoint SD | +0.09 (p = 0.18) | +0.15 (p = 0.13) | – | +0.29 (p = 0.033) | +0.14 (p = 0.51) | no |
| HbA1c, mean glucose, within-day SD | all p > 0.2 | all p > 0.06 | null | all p > 0.28 | all p > 0.4 | null |

Full-sample joint models (n = 1,890 with wearable sleep): the SD-of-daily-means effect on CES-D-10 total *increased* from +0.36 to +0.50 points per SD (p = 0.001) when HbA1c and mean glucose were added, to +0.51 (p = 8 × 10⁻⁴) with within-day SD, and was +0.48 (p = 0.0016) after sleep regularity, duration and efficiency were added; the log-OR for CES-D-10 ≥ 10 went 0.21 → 0.26 → 0.27 → 0.26 (all p ≤ 0.0013). Bootstrap mediation through sleep-midpoint SD or sleep-duration SD accounted for about 5% of the total effect (indirect 0.024 points per SD, 95% CI 0.0005-0.059). Between-day glucose variability itself is explained mostly by glycaemic level and within-day SD (R² 0.51); sleep-midpoint irregularity adds a small independent contribution (+0.34 mg/dL per SD, p = 0.021) and step-count irregularity none.

**Interpretation.** Day-to-day instability of glucose, net of its level and of within-day variability, is a replicable correlate of clinically relevant depressive symptoms, with an odds ratio of about 1.25 per SD (6.5 mg/dL of between-day SD). It is not a proxy for irregular sleep. Because CES-D-10 and CGM were measured in the same fortnight, the direction is open: low mood can disorganise eating and medication routines, and unstable glycaemia can affect mood. The signal is modest and should be reported as a replicated association, not a screening tool.

![Fig 9](figures/fig9_depression_replication.png)

---

## D. Diabetes-status interactions and dose-response

**Question.** Where along the glycaemic spectrum do the cognition and autonomic gradients live?

**Results (slopes per pooled SD; Fig. 7; `followup_D_*.csv`).**

| Outcome / predictor | No diabetes (n ≈ 739) | Pre-diabetes (532) | T2D non-insulin (639) | T2D insulin (228) | Interaction p (4 groups) | Non-diabetic range* (n = 1,227) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| MoCA / mean glucose | **−1.10 (p = 4 × 10⁻⁶)** | −0.37 (p = 0.10) | −0.18 (p = 0.17) | 0.00 (p = 0.99) | **4 × 10⁻⁴** | −0.79 (p = 3.5 × 10⁻⁴) |
| MoCA / HbA1c | −0.69 (p = 0.011) | −0.45 (p = 0.23) | −0.12 (p = 0.37) | +0.02 (p = 0.91) | 0.039 | −0.70 (p = 0.009) |
| MoCA / daily SD | −0.66 (p = 0.006) | −0.15 | −0.14 | −0.13 | 0.24 | −0.32 (p = 0.065) |
| MoCA < 26 / mean glucose | +0.47 (p = 0.021) | +0.06 | +0.12 | +0.09 | 0.31 | +0.40 (p = 0.009) |
| Resting HR / mean glucose | +1.61 (p = 0.015) | +1.37 (p = 0.044) | +0.70 (p = 0.047) | +0.70 (p = 0.11) | 0.40 | +1.92 (p = 1.7 × 10⁻⁴) |
| Resting HR / HbA1c | +1.53 (p = 0.022) | +2.03 (p = 0.004) | +1.08 (p = 0.006) | +0.14 (p = 0.68) | 0.016 | +1.93 (p = 0.011) |
| Stress / HbA1c | +4.05 (p = 3 × 10⁻⁴) | +2.62 (p = 0.17) | +2.89 (p = 7 × 10⁻⁵) | +1.08 (p = 0.26) | 0.12 | +4.27 (p = 0.010) |

*no diabetes diagnosis and HbA1c < 6.5%.

Restricted cubic splines (4 df) rejected linearity for MoCA vs HbA1c (p = 0.014; steep decline to ≈ 7%, flat thereafter), for resting heart rate vs all three predictors (p ≤ 0.0025; rise to a plateau at ≈ 200 mg/dL or 8%), and for stress (p ≈ 0.02). MoCA vs mean glucose and vs daily SD were adequately linear (p = 0.10 and 0.66).

**Interpretation.** The cognition-glucose association is confined to people without diabetes: one pooled SD of mean glucose (34 mg/dL) inside the normal range corresponds to about one MoCA point, and there is no gradient at all among insulin users. Two readings are compatible with this. A biological one: glucose in the high-normal range indexes early insulin resistance and cerebrovascular risk, whereas in established diabetes treatment, disease duration and complications dominate and measured glucose no longer ranks people by cumulative exposure. A methodological one: in treated diabetes, glucose reflects the intensity of treatment as much as underlying disease (confounding by indication), which flattens or even reverses gradients. Either way, CGM metrics are most informative about cognition and autonomic tone as continuous risk markers in the general population, not as management targets in treated diabetes, and future models should include the interaction or restrict to the non-diabetic range.

![Fig 7](figures/fig7_spline_dose_response.png)

---

## E. Stability of 10-day CGM metrics and the recency question

**Question.** Report 01 could not distinguish "HbA1c integrates longer" from "CGM is more recent". A lagged CGM is unavailable, so: how stable are the metrics within the 10-day window, and does the half nearer the clinic visit predict better?

**Results** (n = 1,674 with ≥ 2 valid days in each half). Split-half agreement: mean glucose ICC(2,1) = 0.92 (mean absolute difference 7.2 mg/dL), daily SD 0.87 (3.4 mg/dL), TIR 0.89 (3.9 percentage points). The first half had slightly higher SD (23.6 vs 22.8 mg/dL, p < 10⁻⁴) and lower TIR (90.1 vs 90.6%, p = 0.007), consistent with a small early-wear or post-visit effect. First- and second-half mean glucose predicted resting heart rate, stress, cognitive impairment, CES-D-10, steps and sleep equally well (AIC differences ≤ 1.4). For MoCA total the first half fitted better (AIC 8370 vs 8376) and in a joint model only the first half retained a slope (−0.48 vs +0.12 per SD; p = 0.02 vs 0.55), but the two halves are collinear (r = 0.92) so this is weak evidence.

**Interpretation.** Ten days of CGM yields person-level metrics with test-retest reliability comparable to a laboratory HbA1c, and the associations do not depend on which five days are used. The residual "extra" information in HbA1c (section B) is therefore not a recency artefact of the CGM window; a longer integration period or non-glycaemic determinants remain the explanations.

---

## Key numbers to cite

- Pair VIF: HbA1c 2.9, mean glucose 3.8, daily SD 2.5 (four-metric block: 3.0 / 11.4 / 4.1 / 9.2 / 9.0).
- Pair beyond HbA1c: MoCA F(2) = 7.1, p = 8.2 × 10⁻⁴; resting HR p = 9.1 × 10⁻⁴. HbA1c beyond pair: PM2.5 p = 2.7 × 10⁻⁵; steps, brisk minutes, sleep, stress p ≈ 0.002-0.003.
- HGI SD 0.63%; red-cell indices explain 8.4%; HGI effects per SD: PM2.5 +0.084 log units, sleep −5.0 min, stress +1.26, resting HR +0.48 bpm, steps +295; cognition null.
- Depression: SD of daily means → CES-D-10 ≥ 10, hold-out log-OR 0.22 per SD (p = 0.020), OR 1.25; net of HbA1c/mean glucose/within-day SD +0.51 points per SD (p = 8 × 10⁻⁴); 5% mediated by sleep regularity.
- MoCA vs mean glucose: −1.10 per pooled SD without diabetes, 0.00 with insulin-treated diabetes, interaction p = 4 × 10⁻⁴; non-diabetic range −0.79 (p = 3.5 × 10⁻⁴).
- Split-half ICC: mean 0.92, daily SD 0.87, TIR 0.89.

## Limitations specific to this report

| Limitation | Why it matters |
| :--- | :--- |
| Hold-out sample of 652 gives ~50% power for the continuous CES-D effect | The continuous-score replication is inconclusive rather than negative. |
| HGI defined by a linear cohort regression | A non-linear or group-specific calibration changes HGI slightly; the glycation-gap definition gave identical results. |
| Red-cell indices limited to haemoglobin, MCV, RDW, haematocrit | Reticulocytes, ferritin and haemoglobinopathy status, the classic HGI determinants, are unavailable. |
| Splines fitted at covariate means | Curves illustrate shape; group medians are shown for orientation only. |
| Split-half analysis uses consecutive halves of one wear | It tests stability, not seasonal or long-term variation. |
| Same limitations as report 01 | Cross-sectional design, no sex/race adjustment, screening instruments, proxy wearable metrics. |

## What to do next

1. Adopt **mean glucose + average daily SD** (or TIR) as the CGM block; report HGI alongside HbA1c when the outcome is behavioural or environmental.
2. Pre-register **SD of daily means → CES-D-10 ≥ 10** for the next AI-READI release and add sleep-regularity indices from the raw Garmin epochs (a true Sleep Regularity Index rather than midpoint SD).
3. Obtain an **income or area-deprivation** variable (PhenX SDOH items are in `observation.csv`: `pxpa*`, `pxji1`, `pxhic*`) to test whether HGI's behavioural associations are socioeconomic.
4. When longitudinal visits exist, repeat section E with a **months-apart CGM** to close the integration-window question.
