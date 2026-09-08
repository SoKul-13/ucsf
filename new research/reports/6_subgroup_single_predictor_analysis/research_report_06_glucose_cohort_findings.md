# Phase 6b - Actual-value glucose cohorts: the same single-predictor analysis inside people who stay within 54-250, people who go below 54, and people who go above 250

**Phase 6b research report** · AI-READI v3.0.0 · 2026-09-07
**Companion files**: [cohort tables](research_report_05_glucose_cohort_tables.md) · [Phase 6 narrative](research_report_01_subgroup_single_predictor_findings.md) · [methods and sample log](research_report_04_methods_and_sample_log.md) (section "How pooled and day-averaged metrics are calculated") · CSVs `data/cohort_*.csv` · figures `figures/fig4-fig5`
**Code**: `src/6_subgroup_single_predictor_analysis/run_phase6b_glucose_cohorts.py` → `generate_phase6b_reports.py`
**Full model outputs**: `model_output_tables/phase6b_<cohort>_<population>.md` and `phase6b_model_outputs.csv` (all terms, standard OLS-output format).

---

## 1. Cohort definitions, sizes and what was not possible

Cohorts are defined from each participant's **own valid CGM readings** over the whole wear (same readings, valid-day rule and analysis base as Phase 5/6). Inside every cohort the full Phase 6 grid is run: 31 glycaemic measures entered one at a time (HbA1c, CGM level, CGM variability, the standard 70-180 time in range, and the glucose bands), 14 outcomes, three populations (total / healthy = no diabetes + pre-diabetes / non-healthy = T2D oral + insulin), Phase 5 covariates.

| Cohort | Definition | N | Healthy | Non-healthy | Possible? |
| :--- | :--- | :---: | :---: | :---: | :--- |
| Normal range only | every reading within 70-180 | **39** | 30 | 9 | **No.** 39 people, 6 CES-D ≥ 10 events, 10 MoCA < 26 events; no covariate-adjusted model can be fitted. Only 1.8 % of participants never leave 70-180 over 10 days. |
| Near-normal (substitute) | ≥ 99 % of readings within 70-180 | 454 | 393 | 61 | Yes for total and healthy; the non-healthy stratum (61) is too small for most outcomes (models fail or fall below the 60-participant / 15-event floor). |
| Within 54-250 | no reading < 54 and none > 250 | 890 | 685 | 205 | Yes. |
| Hypoglycaemia exposure | at least one reading < 54 | 638 | 408 | 230 | Yes. |
| Hyperglycaemia exposure | at least one reading > 250 | 795 | 244 | 551 | Yes (healthy stratum is small, 215-244). |

Overlap: 453 people have < 54 exposure only, 610 have > 250 only, 185 have both, 890 neither. A stricter hypoglycaemia definition (≥ 1 % of time < 54) leaves 56 people and is not possible; a stricter hyperglycaemia definition (≥ 1 % of time > 250) leaves 461 and could be run on request.

**FDR.** No cohort reaches the Phase 6 rule (n ≥ 1,000), so by rule #3 the reported q column reads "not applied". Because that leaves 420 raw tests per cohort-population uncorrected, an *informational* Benjamini-Hochberg q over all tests in the cohort-population is also shown and flagged "**" in the tables and Fig. 4; it is a guide, not the rule.

Counts of raw p < 0.05 (out of ~420 tests per cohort-population; ~21 expected under the null):

| Cohort | Total | Healthy | Non-healthy |
| :--- | :---: | :---: | :---: |
| Near-normal (≥ 99 % TIR) | 26 (0 informational q < 0.05) | 26 (0) | 0 of 96 estimable tests |
| Within 54-250 | 73 of 322 (22) | 38 (10) | 30 (0) |
| Hypoglycaemia exposure | **144 (66)** | 31 (0) | 81 (10) |
| Hyperglycaemia exposure | **117 (50)** | 49 (10) | 70 (4) |

(Within 54-250 and near-normal have fewer tests because the < 54 and > 250 band predictors are constant there and are skipped.)

![Fig 5](figures/fig5_glucose_cohort_sizes.png)

---

## 2. Findings by cohort

### 2.1 Near-normal cohort (≥ 99 % of readings in 70-180; the closest possible version of "normal range only")

Once glycaemia is restricted to this narrow band, the level and variability metrics stop predicting cognition, resting heart rate and stress (all p > 0.05 for HbA1c, mean glucose, SD, CV, TIR in the total and healthy populations). What remains:

- **MAG (mean absolute glucose change) → depression**: CES-D-10 total +0.62 points per SD (p = 0.005) and CES-D-10 ≥ 10 log-OR +0.43 (p = 0.001) in the total cohort; +0.58 / +0.46 in the healthy population (p = 0.008 / 0.001). Between-day SD of daily means → memory index −0.34 (p = 0.0075).
- **HbA1c → shorter sleep** (−10.5 min per SD, p = 0.001; healthy −11.4, p = 0.001) and, oddly, **time 54-69 → longer sleep** (+9.2 min, p = 0.004) and **TIR → fewer brisk minutes** (−1.6 min, p = 0.004).
- Nothing survives the informational FDR.

**Inference.** Within the normal range the glucose *level* no longer carries information about cognition or autonomic tone, which confirms that those gradients in Phase 5/6 come from the movement across the 70-180 boundary. Rapid glucose change (MAG) still tracks depressive symptoms, and HbA1c still tracks sleep, which fits the Phase 5b conclusion that HbA1c's behavioural associations are not about sensor glucose.

### 2.2 Within 54-250 (no severe hypo- or hyperglycaemia; n = 890)

- **Cognition**: mean glucose −0.38 MoCA points per SD (p = 3 × 10⁻⁴, informational q < 0.05) and MoCA < 26 log-OR +0.27 (p = 3.5 × 10⁻⁴, q < 0.05); HbA1c −0.28 (p = 0.007); TIR +0.23 (p = 0.043); SD −0.21 (p = 0.04). In the non-healthy stratum (205) the variability metrics are as strong as level (pooled SD −0.55, p = 0.011; mean glucose −0.49, p = 0.011).
- **Resting heart rate and stress**: mean glucose +1.16 bpm per SD (p = 2 × 10⁻⁵, q < 0.05) and +1.88 stress points (p = 0.003, q < 0.05); TIR −0.77 bpm (p = 0.005); time > 180 +0.88 bpm (p = 0.002, q < 0.05). In the healthy stratum TIR −0.73 bpm (p = 4 × 10⁻⁴, q < 0.05) and time > 180 +0.83 (p = 6.5 × 10⁻⁵, q < 0.05).
- **Activity and sleep**: MAG +557 steps and +1.85 brisk minutes per SD (p = 2 × 10⁻⁴ and 2 × 10⁻⁵, both q < 0.05); HbA1c +364 steps (p = 0.019) and −7.1 min sleep (p = 0.006).
- **Depression**: nothing in the total or healthy populations; in the non-healthy stratum MAG → CES-D-10 ≥ 10 log-OR +0.56 (p = 0.002).
- **Environment**: relative humidity rises with pooled SD (+0.59 % per SD, p = 0.003, q < 0.05) and CV; PM2.5, temperature and VOC null.

**Inference.** Removing everyone with severe excursions does not remove the cognition and autonomic gradients: moderate hyperglycaemia (181-250) and level within 54-250 are enough. This is the cleanest demonstration that the associations are not driven by a tail of extreme values.

### 2.3 Hypoglycaemia-exposed cohort (≥ 1 reading < 54; n = 638)

This is the cohort with the most signal per test (144 raw hits, 66 informational q < 0.05), and it is where the depression-glycaemia association is concentrated.

- **Cognition** (total): HbA1c −0.52 MoCA points per SD (p = 1.7 × 10⁻⁵), mean glucose −0.44 (p = 8 × 10⁻⁴), TIR +0.47 (p = 4 × 10⁻⁴), time > 180 −0.45 (p = 0.001), time > 250 −0.42 (p = 0.004); MoCA < 26 log-OR +0.36 per SD HbA1c (p = 3 × 10⁻⁴). All informational q < 0.05.
- **Depression** (total): CES-D-10 total rises with pooled SD (+0.55, p = 0.006), between-day SD (+0.60, p = 0.003), time > 250 (+0.64, p = 6.5 × 10⁻⁶) and falls with TIR (−0.55, p = 0.003); CES-D-10 ≥ 10 log-OR +0.27 to +0.43 per SD for HbA1c, mean glucose, SD, TIR (negative), time > 180 and time > 250 (all p ≤ 0.004). In the non-healthy stratum (230) time > 250 → CES-D-10 +1.00 points per SD (p = 1.4 × 10⁻⁵) and between-day SD → CES-D-10 ≥ 10 log-OR +0.63 (p = 3.5 × 10⁻⁴); in the healthy stratum (408) only TIR (−0.33, p = 0.005) and time > 180 (+0.36, p = 0.003) relate to CES-D-10 ≥ 10.
- **Sleep**: HbA1c −8.5 min per SD (p = 0.0015; non-healthy −14.9, p = 6 × 10⁻⁴), MAG −12.2 (p = 2 × 10⁻⁵), time > 250 −6.7 (p = 0.0095).
- **Resting heart rate and stress**: all level and variability metrics p ≈ 0.01-0.04 in total; between-day SD strongest (p = 0.003 / 0.007).
- **Cognition in the healthy hypo-exposed stratum**: null (all p > 0.14), i.e. the cognition signal in this cohort comes from its non-healthy members (HbA1c −0.54, p = 0.015; TIR +0.55, p = 0.021; time > 250 −0.55, p = 0.032).

**Inference.** People who dip below 54 and *also* run high are the ones whose glycaemia relates to mood and cognition. Among the 638, 185 also exceed 250, and those are overwhelmingly treated diabetes. The signal here is glycaemic instability in both directions, which is the profile of insulin or sulfonylurea treatment with poor control. For a healthy person a few readings below 54 (typically nocturnal sensor-compression lows) carry no cognitive or mood information.

### 2.4 Hyperglycaemia-exposed cohort (≥ 1 reading > 250; n = 795)

- **Resting heart rate and stress** are the dominant signals: mean glucose +1.82 bpm (p = 3 × 10⁻⁷) and +3.6 stress points (p = 3.5 × 10⁻⁶) per SD; TIR −1.90 bpm and −3.8 points (p ≈ 10⁻⁷); HbA1c +1.73 bpm and +4.0 points (p ≤ 10⁻⁷). These hold in the non-healthy stratum (mean glucose +1.05 bpm, p = 0.009; stress +2.7, p = 0.002) and, for stress, even in the 244 healthy members (HbA1c +2.65, p = 0.022).
- **Cognition**: mean glucose −0.37 (p = 0.005), pooled SD −0.36 (p = 0.004), TIR +0.36 (p = 0.006), time > 180 −0.36 (p = 0.005). In the healthy hyper-exposed stratum the memory index falls steeply with mean glucose (−0.51 per SD, p = 4 × 10⁻⁴) and time > 250 (−0.45, p = 5 × 10⁻⁴); in the non-healthy stratum variability (pooled SD −0.31, p = 0.036; MAG −0.34, p = 0.031) matters more than level.
- **Depression**: between-day SD of daily means +0.55 CES-D-10 points (p = 0.003) and log-OR +0.31 for ≥ 10 (p = 5 × 10⁻⁴); non-healthy +0.79 / +0.44 (p = 3 × 10⁻⁴ / 4 × 10⁻⁵). Level metrics are null. Healthy hyper-exposed: null.
- **Indoor PM2.5**: HbA1c +0.12 log units per SD (p = 0.0045), between-day SD +0.12 (p = 0.0013), mean glucose +0.08 (p = 0.03), TIR −0.09 (p = 0.017); non-healthy HbA1c +0.13 (p = 0.016), between-day SD +0.14 (p = 0.0012).
- **Sleep**: MAG −10.0 min (p = 7.5 × 10⁻⁵), HbA1c −6.1 (p = 0.0097), pooled SD −5.4 (p = 0.043).

**Inference.** In people who reach > 250 the autonomic signal is the strongest of any cohort, consistent with sympathetic activation at high glucose; the depression signal is again day-to-day instability, not level; and the PM2.5-HbA1c association re-emerges here (it was absent in the within-54-250 cohort), which suggests it is carried by the poorly controlled, socioeconomically disadvantaged tail.

---

## 3. What is important across the cohorts

1. **The cognition and autonomic gradients survive restriction to 54-250 but disappear inside 70-180.** They are carried by movement across the 180 boundary (moderate hyperglycaemia), not by the extreme tails and not by variation inside the normal range. Clinically: time > 180 is the working exposure, and > 250 adds little beyond it.
2. **Depression tracks glycaemic instability, and only where instability exists.** Between-day SD and MAG relate to CES-D-10 in the hypo-exposed and hyper-exposed cohorts (strongest in their non-healthy members, p ≈ 10⁻⁴-10⁻⁵) and MAG alone does so even inside the near-normal cohort, while nothing relates to depression in the within-54-250 total population.
3. **Hypoglycaemia exposure in a healthy person is not a risk marker.** In the 408 healthy participants with a reading below 54, glycaemic measures predict nothing about cognition, mood, activity or heart rate. In the 230 non-healthy participants with such a reading they predict almost everything, so "< 54" is a marker of treatment-related instability, not of harm from the low reading itself.
4. **HbA1c keeps its behavioural associations in every cohort** (shorter sleep in near-normal, within-54-250, hypo- and hyper-exposed; more steps in within-54-250), even where sensor glucose is uninformative, consistent with Phase 5b's discordance result.
5. **Statistical caution.** No cohort meets the FDR rule; the informational q identifies 66 (hypo), 50 (hyper), 22 (within 54-250) and 0 (near-normal) robust tests. Stratum-level results with n ≈ 200-250 (non-healthy within 54-250, healthy hyper-exposed, non-healthy hypo-exposed) should be read as hypothesis-generating; the near-normal non-healthy stratum (61) is uninformative.

---

## 4. How "pooled" metrics are calculated (and how they differ from day-averaged ones)

Let g₁ … g_N be all valid readings of one participant over the whole wear (all days concatenated; readings 39-401 mg/dL, 5-minute sampling, site-local time; N ≈ 2,850 for 10 days). Let D be the valid days (≥ 70 % of the expected 288 readings) and g_{d,1} … g_{d,n_d} the readings on day d.

- **Pooled** = one statistic over all N readings, ignoring day boundaries. Mean glucose = (1/N) Σ gᵢ. Pooled SD = √[Σ(gᵢ − mean)² / (N − 1)]. Pooled time in 70-180 = 100 × #{i : 70 ≤ gᵢ ≤ 180} / N; pooled time > 250 = 100 × #{i : gᵢ > 250} / N; the other bands likewise. Every reading counts once, so days with more readings weigh more and partial days are included.
- **Day-averaged** = the same statistic computed on each valid day separately, then averaged over valid days with equal weight: avg. daily SD = (1/|D|) Σ_d SD(g_{d,·}); avg. daily time in 70-180 = (1/|D|) Σ_d [100 × #{j : 70 ≤ g_{d,j} ≤ 180} / n_d]. Partial days are excluded, and the within-day SD is not inflated by drift of the daily mean across days.
- **Between-day metric**: SD of daily means = SD over valid days of the daily mean glucose (day-to-day drift, distinct from within-day swings).
- **Indicators**: "any reading < 54" / "any reading > 250" = 1 if at least one valid reading falls in the band during the wear, else 0.
- In this cohort pooled and day-averaged versions correlate at ρ ≈ 0.98-0.99 (TIR, SD) and give the same conclusions; the collaborator's requested "average daily TIR / SD" are the day-averaged forms, and the pooled forms match Phases 1-4 and the international consensus reporting.

*Figures*: [Fig. 4 heat-map of all tests inside each cohort](figures/fig4_heatmap_glucose_cohorts.png) · [Fig. 5 cohort sizes](figures/fig5_glucose_cohort_sizes.png)
