# Do CGM-derived glycaemic metrics predict cognition, depression, the home environment and wearable physiology better than HbA1c? A pre-specified comparison in the AI-READI cohort

**Phase 5 research report** · AI-READI flagship dataset v3.0.0 · analysis date 2026-09-04
**Companion files**: [full regression tables](research_report_02_full_regression_tables.md) · [sensitivity and exploratory tables](research_report_03_sensitivity_and_exploratory_tables.md) · [data dictionary and methods log](research_report_04_data_dictionary_and_methods_log.md) · result CSVs in `data/` · figures in `figures/`
**Code**: `src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py` → `run_multimodal_cgm_models.py` → `generate_reports.py`
**Follow-up**: the recommendations in section 5.5 are carried out in [research_report_05](research_report_05_followups_parsimony_discordance_replication.md) (parsimonious CGM pair, HbA1c-CGM discordance, split-sample replication of the depression signal, dose-response splines, split-half stability).

---

## Abstract

**Background.** HbA1c integrates glycaemia over 8-12 weeks but is blind to short-term glucose dynamics and is influenced by non-glycaemic factors. Continuous glucose monitoring (CGM) captures mean level, variability and time in range (TIR) over days. Whether CGM metrics carry information about diabetes-related comorbidities and behaviours that HbA1c does not is unresolved.

**Methods.** We analysed 2,138 AI-READI participants (739 without diabetes, 532 pre-diabetes/lifestyle-controlled, 639 type 2 diabetes on non-insulin therapy, 228 insulin-treated) with ≥3 valid days of Dexcom G6 data (≥70% of readings per day), a laboratory HbA1c and complete covariates. Four pre-specified CGM metrics were tested: mean glucose, mean/SD ratio, average daily TIR (70-180 mg/dL, inclusive) and average daily SD. Fourteen primary outcomes spanned cognition (MoCA total, MoCA < 26, memory index), depression (CES-D-10 total, CES-D-10 ≥ 10), the home environment (10-day LeeLab Anura sensor: PM2.5, temperature, humidity, VOC) and Garmin wearable physiology (steps, brisk-cadence minutes, resting heart-rate proxy, sleep duration, HRV-based stress). For each outcome we fitted, on one identical sample, covariate-only, HbA1c-only, single-CGM-metric, four-CGM-metric and combined (HbA1c + CGM) models adjusted for age, BMI, education, clinical site and four comorbidities (plus season for environmental outcomes). Slopes were tested with HC3-robust t-tests (OLS) or Wald z-tests (logistic); incremental information with nested F / likelihood-ratio tests; out-of-sample performance with 5 × 10-fold cross-validation and DeLong tests; multiplicity with Benjamini-Hochberg FDR within pre-defined families.

**Results.** *Cognition*: every glycaemic measure predicted lower MoCA and higher odds of impairment (all q < 0.05; mean glucose −0.41 points per SD [34 mg/dL], HbA1c −0.35 per SD [1.05%]). The four CGM metrics added information beyond HbA1c for MoCA total (F(4) = 4.83, p = 7.0 × 10⁻⁴, q = 0.006; ΔAIC −11.4) whereas HbA1c added nothing beyond CGM (p = 0.57). Out-of-sample R² rose from 0.100 (HbA1c) to 0.105 (CGM); the bootstrap CI for the adjusted-R² difference excluded zero. Associations were 2-3 times stronger in participants without diabetes than in those with type 2 diabetes (interaction p = 0.009 for mean glucose). *Depression*: no glycaemic measure predicted CES-D-10 after FDR control; an exploratory sweep implicated between-day variability (SD of daily means: q = 0.005 for CES-D-10 total, q = 5 × 10⁻⁴ for CES-D-10 ≥ 10). *Home environment*: only indoor PM2.5 showed a signal, and only for HbA1c (+7.6% per SD, q = 0.010), which retained information beyond CGM (p = 2.2 × 10⁻⁴). Temperature, humidity and VOC were unrelated to glycaemia. *Wearables*: resting heart rate and stress index were strongly related to every glycaemic measure (p < 10⁻⁶); CGM added information beyond HbA1c for resting heart rate (F(4) = 5.16, p = 3.9 × 10⁻⁴, q = 0.005) with HbA1c contributing little in return (p = 0.031, q = 0.087). Conversely, for steps, brisk minutes and sleep duration only HbA1c was informative (higher HbA1c → more steps and shorter sleep), and it remained so after adjusting for CGM (p ≤ 0.002), while CGM metrics were null.

**Conclusions.** CGM and HbA1c are not interchangeable. For physiologically proximal outcomes (cognition, autonomic tone) the 10-day CGM profile, especially mean glucose and daily SD, is at least as informative as HbA1c and adds to it; HbA1c becomes redundant. For behavioural and environmental exposures (activity, sleep duration, indoor PM2.5) HbA1c carries information that a 10-day CGM window does not, plausibly reflecting its longer integration period and non-glycaemic determinants. Depression is essentially unrelated to glycaemic level once education, site and comorbidity are controlled, with a tentative signal for day-to-day instability. All incremental effects are small (ΔR² ≤ 0.02) and none of the models is clinically predictive on its own.

---

## 1. Background and the questions asked

### 1.1 Why compare CGM with HbA1c at all?

HbA1c is the reference biomarker for glycaemic control, but it is a 2-3-month weighted average that (i) cannot distinguish stable from highly variable glycaemia, (ii) is affected by haemoglobin turnover, anaemia, kidney disease and ancestry, and (iii) shows within-person discordance with mean glucose of ±0.5-1.0% in a substantial minority of individuals (Beck et al., 2017; Bergenstal et al., 2017). CGM provides a direct measurement of interstitial glucose every 5 minutes, from which mean glucose, glucose management indicator (GMI), variability (SD, CV) and time in range (TIR) can be derived (Battelino et al., 2019 international consensus). The clinical literature suggests that variability and TIR relate to microvascular complications, hypoglycaemia risk and possibly cognition independently of HbA1c (Lu et al., 2018; Beck et al., 2019), but most evidence comes from diabetes-only cohorts with short CGM wear and rarely includes non-glycaemic comorbidities.

AI-READI is unusual in offering, for the same 2,280 people across the glycaemic spectrum, 10 days of Dexcom G6 data, a laboratory HbA1c, a MoCA, a CES-D-10, 10 days of an indoor environmental sensor and 10 days of a Garmin wearable. This makes it possible to ask, with identical samples and covariates, whether CGM metrics predict any of these domains and whether they add to or replace HbA1c.

### 1.2 What the earlier AI-READI notebooks (Dylan's Notion series) established

The 23 prior notebooks on this cohort provide the context this analysis builds on (summarised in the companion methods log):

- Diabetes stage dominates every glycaemic outcome (Spearman ρ with study group: HbA1c 0.63, CGM mean glucose 0.54); most psychosocial correlates vanish once group is controlled.
- Depression (CES-D-10 ≥ 10, ≈20% of the cohort) is concentrated in insulin users; after adjustment for age and group, depressed participants had HbA1c +0.15% and mean glucose +3.8 mg/dL (NB30), and higher wearable heart rate and stress (NB31). Continuous CES-D was, however, essentially uncorrelated with HbA1c (ρ = 0.02).
- MoCA < 26 (≈41%) tracked diabetes stage and age; education was flagged as an unmeasured confounder (NB33).
- Among CGM metrics, time above 180 and mean glucose were the best HbA1c proxies (ρ ≈ 0.68-0.69); variability metrics (CV, MAGE, SD) formed a separate cluster (NB17, NB13).
- Those notebooks adjusted only for age and diabetes group, never for education or site, and used 140-based or "% of daily means > 180" metrics in places.

The present analysis therefore (a) moves to the consensus 70-180 mg/dL range and the requested four core metrics, (b) adds education, site, BMI and comorbidity adjustment, (c) treats HbA1c and CGM symmetrically in nested models, and (d) controls the false-discovery rate explicitly.

### 1.3 Pre-specified questions

| # | Question | Test |
| :--- | :--- | :--- |
| Q1 | Does each glycaemic measure (HbA1c; mean glucose; mean/SD; average daily TIR; average daily SD) have a non-zero adjusted slope on each outcome? | HC3 t-test (OLS) / Wald z (logistic); BH-FDR over the 14 × 5 family |
| Q2 | Do the four CGM metrics jointly add information beyond HbA1c? Does HbA1c add information beyond the four CGM metrics? | Nested F / LR tests, M3 vs M1 and M3 vs M2; BH-FDR over the 14 × 2 family |
| Q3 | Which single CGM metric adds most beyond HbA1c? | M3[x] vs M1; BH-FDR over the 14 × 4 family |
| Q4 | Is any gain real out of sample? | Repeated 10-fold CV R² / AUC; bootstrap CI for ΔadjR²; DeLong test for ΔAUC |
| Q5 | Are the relationships robust to CGM wear length, insulin use, diabetes status, non-linearity and distributional assumptions? | Sensitivity samples, quadratic terms, rank-based partial correlations |

---

## 2. Data and methods (summary; full detail in the [methods log](research_report_04_data_dictionary_and_methods_log.md))

### 2.1 Glucose category cut-offs

| Category | Rule (mg/dL) |
| :--- | :--- |
| Severe hypoglycaemia | < 54 |
| Moderate hypoglycaemia | 54-69 |
| Normal / time in range | 70-180 |
| Moderate hyperglycaemia | 181-250 |
| Severe hyperglycaemia | > 250 |

### 2.2 CGM processing

All 5-minute Dexcom G6 readings were converted to site-local time (UW and UCSD: Pacific; UAB: Central). A calendar day was *valid* if it contained ≥ 70% of the expected 288 readings; participants needed ≥ 3 valid days (median 9). The four core metrics are:

- **Mean glucose**: mean of all readings.
- **Mean/SD ratio**: mean divided by the sample SD of all readings (the inverse of the coefficient of variation).
- **Average daily TIR**: mean over valid days of the daily percentage of readings in 70-180 mg/dL.
- **Average daily SD**: mean over valid days of the within-day SD.

Eleven further metrics (GMI, CV, time > 180, > 250, < 70, < 54, mean absolute glucose change, daily range, between-day SD of daily means, nocturnal mean, daily mean/SD) were reserved for a labelled exploratory sweep.

### 2.3 Outcomes

- **Cognition**: MoCA total (0-30), impairment (MoCA < 26), MoCA memory index (0-15).
- **Depression**: CES-D-10 total (0-30) and the standard ≥ 10 screening cut-off.
- **Home environment** (LeeLab Anura, 5-s sampling, full 10-day file, physically implausible values removed, 1-min averaging): log(1 + mean PM2.5), mean temperature, mean relative humidity, mean VOC index.
- **Wearable** (Garmin Vivosmart 5, wear-days defined by ≥ 10 h of valid heart-rate contact, first and last partial days dropped): steps per wear-day, brisk-cadence minutes (≥ 100 steps/min, a moderate-intensity proxy), resting heart-rate proxy (mean of the daily 5th percentile), total sleep time per night (duplicate stage intervals removed), Garmin HRV-based stress index (invalid −1/−2 codes removed).

Exploratory outcomes: MoCA delayed recall, PAID-5, NOx, % time PM2.5 > 15 µg/m³, sedentary %, sleep efficiency, nocturnal SpO₂, mean heart rate, % time high stress.

### 2.4 Models

For each outcome, on one complete-case sample: M0 (covariates), M1 (+ HbA1c), M2[x] (+ one CGM metric), M2 (+ all four), M3[x] (+ HbA1c + one metric), M3 (+ HbA1c + all four). Covariates: age, BMI, education (≤ 12 / 13-16 / > 16 years), clinical site, hypertension, high cholesterol, kidney disease, circulatory disease; season of visit for environmental outcomes. Sex and race are not released at individual level in this dataset version and could not be adjusted for. Effects are reported per 1 SD of the predictor so that HbA1c and CGM metrics are comparable.

---

## 3. Cohort

The analysis base contained 2,138 participants (Table 1 in the [full tables](research_report_02_full_regression_tables.md#table-1-cohort-characteristics-of-the-analysis-base-by-diabetes-status)). Mean age was 60.8 years; 40.1% scored MoCA < 26 and 18.9% CES-D-10 ≥ 10. Glycaemic measures rose monotonically across the four groups (HbA1c 5.5 → 5.8 → 6.5 → 7.3%; mean glucose 118 → 126 → 147 → 174 mg/dL; average daily TIR 97 → 94 → 81 → 62%). Resting heart rate and Garmin stress rose across groups (60 → 68 bpm; 48 → 60 points) while steps and brisk minutes did not differ (p = 0.43 and 0.99), an early hint that activity is not tracking glycaemia in this cohort.

The five candidate predictors are strongly inter-correlated (Fig. 4): HbA1c with mean glucose ρ = 0.67, with average daily TIR −0.66 and with average daily SD 0.66; average daily SD with TIR −0.89 and with mean/SD ratio −0.85. Variance inflation factors in the combined four-metric model reached 11.4 for mean glucose and ~9 for TIR and SD. Joint-block coefficients are therefore unstable and inference about individual metrics is drawn from the single-metric models (M2[x], M3[x]), with the four-metric block used only for the block-level nested tests.

![Fig 6](figures/fig6_sample_flow.png)

---

## 4. Results

### 4.1 Cognition — CGM adds to HbA1c; HbA1c is redundant given CGM

**Question.** Do glycaemic measures predict MoCA performance after adjusting for age, education, site and comorbidity, and does CGM add to HbA1c?

**Expected.** Prior notebooks found MoCA tracked diabetes stage; the literature links both HbA1c and glucose variability to cognitive decline.

**Results.** All five measures were associated with all three cognitive outcomes (Table 3; Fig. 1), the only exception being mean/SD ratio for the memory index. Effect sizes per SD of predictor:

| Predictor | MoCA total (points) | MoCA < 26 (OR) | Memory index (points) |
| :--- | :---: | :---: | :---: |
| HbA1c | −0.35 [−0.50, −0.20] | 1.21 [1.10, 1.33] | −0.16 [−0.28, −0.05] |
| Mean glucose | **−0.41 [−0.56, −0.26]** | **1.25 [1.13, 1.37]** | **−0.20 [−0.31, −0.09]** |
| Mean/SD ratio | +0.22 [+0.09, +0.36] | 0.89 [0.81, 0.97] | +0.04 (ns) |
| Avg daily TIR | +0.35 [+0.20, +0.50] | 0.83 [0.75, 0.91] | +0.17 [+0.05, +0.28] |
| Avg daily SD | −0.39 [−0.53, −0.25] | 1.23 [1.12, 1.35] | −0.18 [−0.30, −0.06] |

All bold and non-bold entries except the memory-index mean/SD term survive FDR at 0.05. In natural units, 10 mg/dL higher mean glucose corresponds to 0.12 fewer MoCA points and 1% higher HbA1c to 0.33 fewer points.

Incremental information (Table 4, Fig. 2): the four CGM metrics added to HbA1c for MoCA total (F(4, 2122) = 4.83, p = 7.0 × 10⁻⁴, q = 0.006; ΔAIC −11.4) and marginally for MoCA < 26 (LR χ²(4) = 9.54, p = 0.049, q = 0.11); HbA1c added nothing beyond CGM for any cognitive outcome (p = 0.57-0.80; ΔAIC +1.7 to +1.9). Among single metrics (Table 5), mean glucose (p = 6.8 × 10⁻⁴, q = 0.019) and average daily SD (p = 0.002, q = 0.027) each added to HbA1c for MoCA total.

Out of sample (Fig. 3): cross-validated R² for MoCA total was 0.091 (covariates), 0.100 (+ HbA1c), 0.105 (+ four CGM metrics), 0.104 (combined). The bootstrap 95% CI for adjusted-R²(CGM) − adjusted-R²(HbA1c) was [+0.0006, +0.0169], excluding zero. For MoCA < 26, AUC was 0.675 (HbA1c) vs 0.679 (CGM), DeLong p = 0.19; discrimination is driven by age and education, not glycaemia.

Stratification (Fig. 5): associations were markedly stronger in participants without diabetes or with pre-diabetes than in those with type 2 diabetes (mean glucose −0.73 vs −0.22 MoCA points per pooled SD, interaction p = 0.009; TIR +0.74 vs +0.19, p = 0.029; HbA1c −0.61 vs −0.17, p = 0.049). A convex quadratic term for HbA1c (p = 0.003) tells the same story: the slope is steepest in the normal range and flattens at high HbA1c. Results were unchanged when restricting to ≥ 7 valid CGM days or excluding insulin users (companion sensitivity tables), and rank-based partial correlations agreed in sign and significance.

**Interpretation.** Cognition is the clearest case where the 10-day CGM profile is at least as informative as HbA1c and adds to it, whereas HbA1c becomes redundant once mean glucose or daily SD is in the model. The stronger gradient below the diabetic range echoes the finding of Crane et al. (2013) that higher glucose is associated with dementia risk even without diabetes, and suggests that a ceiling/treatment effect (medication, established complications, already-low MoCA) compresses the gradient in treated diabetes. The MoCA is a screening instrument and the absolute effects are small (roughly one MoCA point across 3 SD of mean glucose), so the finding is about information content, not clinical prediction.

### 4.2 Depression — no relationship with glycaemic level; a tentative signal for day-to-day instability

**Question.** Do glycaemic measures predict CES-D-10 depressive symptoms, continuously or at the ≥ 10 threshold?

**Expected.** NB30 reported adjusted differences of +0.15% HbA1c and +3.8 mg/dL for CES-D-10 ≥ 10 after age and group adjustment; NB13 found continuous CES-D uncorrelated with HbA1c.

**Results.** No measure predicted the continuous score (all p > 0.20). For CES-D-10 ≥ 10, HbA1c (OR 1.12 per SD, p = 0.028) and average daily TIR (OR 0.90, p = 0.047) were nominally associated but did not survive FDR (q = 0.064 and 0.10). Neither block added information to the other (all nested p > 0.24), cross-validated performance did not improve over covariates (AUC ≈ 0.667 throughout), and estimates were similar within and outside diabetes (interaction p > 0.38). Exploratory outcome PAID-5 (diabetes distress) was, as expected, strongly related to every glycaemic measure (all p < 0.003).

In the exploratory metric sweep, the between-day SD of daily means was associated with both CES-D-10 total (+0.36 points per SD, q = 0.005) and CES-D-10 ≥ 10 (log-OR +0.21 per SD, q = 5 × 10⁻⁴), and nocturnal mean glucose with CES-D-10 ≥ 10 (q = 0.024). None of the four core metrics, which are within-day or pooled measures, showed this.

**Interpretation.** Once education, site and comorbidity are controlled, depressive symptoms are not a function of how high glucose is, consistent with the null continuous correlations in the earlier notebooks and with the view that the depression-diabetes link runs through distress, burden of illness and socioeconomic pathways rather than glycaemia itself. The between-day instability signal is biologically plausible (irregular routines, sleep and eating patterns accompany low mood and also destabilise glucose) but is an exploratory finding that needs confirmation in an independent sample before it is used.

### 4.3 Home environment — HbA1c, not CGM, tracks indoor PM2.5; nothing else is related

**Question.** Are glycaemic measures associated with the indoor environment recorded over the same 10 days?

**Expected.** Air-pollution epidemiology links PM2.5 exposure to higher HbA1c and insulin resistance; temperature and humidity were expected to be site- and season-driven with no glycaemic signal.

**Results.** Indoor PM2.5 was associated with HbA1c (+0.073 log-units per SD, i.e. ≈ 7.6% higher PM2.5 per 1.05% HbA1c, q = 0.010) but with none of the four CGM metrics (p ≥ 0.057). HbA1c retained information beyond the CGM block (F(1) = 13.7, p = 2.2 × 10⁻⁴, q = 0.005; ΔAIC −11.8). The CGM block also passed the nested test in the other direction (p = 0.013, q = 0.039), but this reflects a suppression pattern rather than an independent signal: within participants without diabetes, higher mean glucose was associated with *lower* PM2.5 (−0.09 per pooled SD, p = 0.016) while in type 2 diabetes the slope was positive (interaction p = 0.021), and no single CGM metric added to HbA1c after FDR (Table 5). Cross-validated R² rose only from 0.140 (covariates) to 0.144 (HbA1c). Temperature, humidity and VOC showed no association with any measure (all p > 0.23); their models were dominated by site and season (R² 0.24-0.30) and covariate-only performance was not improved by any glycaemic block.

**Interpretation.** A 10-day sensor record of the home is, by construction, a measure of exposure rather than a health outcome, so the question becomes whether glycaemic biomarkers mark the environments people live in. HbA1c does, weakly, in the direction reported by cohort studies of ambient PM2.5 and glycaemia (e.g. Yang et al., 2018; Chen et al., 2016); the 10-day CGM does not. Two non-exclusive explanations fit: HbA1c integrates months of exposure whereas the CGM window is short, and HbA1c is partly a socioeconomic marker (education-adjusted but not income-adjusted) that co-varies with housing quality and indoor combustion sources. The effect is small and should be read as hypothesis-generating.

### 4.4 Wearable physiology and behaviour — a split verdict

**Question.** Do glycaemic measures predict autonomic (resting heart rate, HRV-based stress) and behavioural (steps, brisk minutes, sleep) signals from the wearable, and which biomarker is more informative?

**Expected.** Cardiac autonomic neuropathy raises resting heart rate and lowers HRV in dysglycaemia; NB31 found depression, not activity, related to heart rate and stress; NB23 found steps unrelated to mean glucose.

**Results — autonomic outcomes.** Resting heart-rate proxy and Garmin stress were strongly related to every measure (Fig. 1): per SD, HbA1c +1.67 bpm and mean glucose +1.71 bpm (both p < 10⁻¹⁴); stress +3.3 and +3.1 points (p < 10⁻¹¹). For resting heart rate the CGM block added substantially to HbA1c (F(4) = 5.16, p = 3.9 × 10⁻⁴, q = 0.005; ΔAIC −12.7) while HbA1c added little to CGM (p = 0.031, q = 0.087; ΔAIC −2.7); mean glucose (q = 0.019), TIR (q = 0.027) and daily SD (q = 0.039) each added individually. Cross-validated R² for resting heart rate: 0.149 (covariates) → 0.181 (HbA1c) → 0.185 (CGM) → 0.186 (combined). For stress both blocks added to each other (p = 0.009 and 0.004), with CV R² 0.092 → 0.121 → 0.121 → 0.124. The heart-rate slopes were about twice as steep outside diabetes as within (HbA1c interaction p = 0.017; daily SD p = 0.032), and quadratic terms were negative (p ≤ 0.008), i.e. the relation flattens at high glycaemia.

**Results — behavioural outcomes.** Only HbA1c predicted steps (+325 per SD, q = 0.033), brisk minutes (+0.98 min per SD, q = 0.019) and sleep duration (−5.3 min per SD, q = 6 × 10⁻⁴); average daily SD also predicted shorter sleep (−3.9 min, q = 0.033). HbA1c retained information beyond the CGM block for all three (p = 0.002, 0.002 and 8 × 10⁻⁴; all q < 0.02), whereas the CGM block added nothing to HbA1c after FDR. The positive HbA1c-activity slopes were inverted-U shaped (quadratic p = 0.01-0.03): activity increased with HbA1c within the normal range and turned down at high values, and the effect was carried by participants without diabetes (+523 steps per pooled SD, p = 0.012; type 2 diabetes +211, p = 0.21). Cross-validated gains were negligible (steps 0.124 → 0.128; sleep 0.022 → 0.027). In the exploratory sweep, mean absolute glucose change (MAG) was the strongest CGM correlate of brisk minutes (+1.39 min per SD, q = 3 × 10⁻⁴) and of shorter sleep (−9.0 min per SD, q < 10⁻⁴).

**Interpretation.** The autonomic findings are the strongest in the report and behave like the cognition findings: glucose level and within-day variability measured over 10 days explain resting heart rate and HRV-based stress better than HbA1c, in keeping with a direct physiological pathway (sympathetic activation and early autonomic neuropathy) that responds to current rather than average glycaemia. The behavioural findings run the other way. The positive HbA1c-activity association is unexpected under a simple "hyperglycaemia causes inactivity" model; it is confined to the non-diabetic range, is inverted-U, and is consistent with earlier AI-READI observations that more-disadvantaged subgroups walk more (NB22) and that steps correlate positively with depressive symptoms (NB31). Occupational or transport walking associated with lower socioeconomic position, which also raises HbA1c through diet and access pathways, is the most parsimonious explanation; sensor glucose over 10 days does not carry this signal because activity itself lowers interstitial glucose. Sleep duration follows the same logic: shorter sleep raises HbA1c over months through insulin resistance (Spiegel et al., 2005), while the 10-day CGM mean is buffered. MAG, which rises with exercise-driven excursions, is a useful reminder that some CGM metrics capture activity rather than dysglycaemia.

### 4.5 Summary across domains

| Domain / outcome | Any glycaemic signal (FDR)? | CGM adds beyond HbA1c? | HbA1c adds beyond CGM? | Most informative single measure | Verdict |
| :--- | :---: | :---: | :---: | :--- | :--- |
| MoCA total | yes, all 5 | **yes** (q = 0.006) | no | mean glucose | CGM ≥ HbA1c |
| MoCA < 26 | yes, all 5 | marginal (q = 0.11) | no | mean glucose | CGM ≈ HbA1c |
| MoCA memory index | yes, 4 of 5 | no | no | mean glucose | equivalent |
| CES-D-10 total | no | no | no | – | null |
| CES-D-10 ≥ 10 | no (nominal HbA1c, TIR) | no | no | – | null |
| Indoor PM2.5 | HbA1c only | suppression only | **yes** (q = 0.005) | HbA1c | HbA1c > CGM |
| Indoor temperature / humidity / VOC | no | no | no | – | null |
| Steps per day | HbA1c only | no | **yes** (q = 0.009) | HbA1c | HbA1c > CGM |
| Brisk minutes | HbA1c only | no | **yes** (q = 0.010) | HbA1c | HbA1c > CGM |
| Resting heart rate | yes, all 5 | **yes** (q = 0.005) | weak (q = 0.087) | mean glucose | CGM > HbA1c |
| Sleep duration | HbA1c, daily SD | no | **yes** (q = 0.006) | HbA1c | HbA1c > CGM |
| Garmin stress | yes, all 5 | **yes** (q = 0.030) | **yes** (q = 0.015) | HbA1c ≈ mean glucose | complementary |

Across the four core CGM metrics, mean glucose was the most informative in every domain where CGM mattered; average daily SD was a close second and added to HbA1c for cognition and resting heart rate; average daily TIR behaved as a near-mirror of daily SD (ρ = −0.89) and rarely added beyond it; the mean/SD ratio was the weakest and, being the inverse CV, is almost collinear with daily SD.

---

## 5. Discussion

### 5.1 The overall story

1. **HbA1c and 10-day CGM metrics carry partly different information, and the difference is systematic.** Where the outcome is a proximal physiological state (cognitive performance, resting heart rate, HRV-based stress), current glycaemic level and within-day variability out-inform HbA1c, and HbA1c is redundant once they are in the model. Where the outcome is a behaviour or an exposure integrated over months (habitual activity, sleep duration, indoor particulate exposure), HbA1c retains information that a 10-day sensor window does not.
2. **Mean glucose and average daily SD are the CGM metrics to keep.** They were the only metrics that added to HbA1c after FDR, and they did so for the two outcomes with the strongest overall signal. TIR (70-180) is a monotone transform of the same information in this cohort where 58% of participants have average daily TIR > 95%, and the mean/SD ratio adds nothing.
3. **The glycaemia-cognition and glycaemia-autonomic gradients are steepest below the diabetic range.** Interaction and quadratic tests agree. In treated diabetes the gradient flattens, which limits what CGM can add in the very population where it is used clinically, and which argues for studying CGM metrics as continuous risk markers across the whole population rather than as management targets only.
4. **Depression is not a glycaemic-level phenomenon in this cohort.** With education, site and comorbidity controlled, neither HbA1c nor CGM level predicted CES-D-10; the only signal was day-to-day instability, which is exploratory.
5. **Effect sizes are small.** No block raised cross-validated R² by more than 0.02 or AUC by more than 0.01. The findings concern information content and mechanism, not individual-level prediction.

### 5.2 Relation to the earlier AI-READI notebooks

- The depression-glycaemia association reported in NB30 (+0.15% HbA1c after age and group adjustment) shrinks to a non-significant OR of 1.12 per SD once education, site and comorbidities are added and multiplicity is controlled. The earlier result was probably partly confounded by education and site.
- NB33's MoCA-diabetes link, obtained without education adjustment, survives education adjustment here and is attributable to glycaemia itself, with CGM mean glucose the best marker.
- NB31's finding that heart rate and stress carry a depression signature and NB19's HbA1c-heart-rate correlation (ρ = 0.12) are extended: the autonomic signal is primarily glycaemic and is better captured by CGM.
- NB23's null for steps versus mean glucose is replicated; the new observation is that HbA1c, unlike sensor glucose, is positively related to activity in the non-diabetic range.

### 5.3 Key numbers to cite

- Analysis base N = 2,138; cognition N = 2,138; depression N = 2,135; environment N = 2,100; wearable N = 1,872-1,893.
- MoCA total: mean glucose −0.41 points per SD (34 mg/dL), q = 4 × 10⁻⁷; CGM beyond HbA1c F(4) = 4.83, p = 7.0 × 10⁻⁴; HbA1c beyond CGM p = 0.57; CV R² 0.100 → 0.105.
- MoCA < 26: OR per SD mean glucose 1.25 [1.13, 1.37]; HbA1c 1.21 [1.10, 1.33]; AUC 0.675 vs 0.679 (DeLong p = 0.19).
- CES-D-10 ≥ 10: HbA1c OR 1.12 [1.01, 1.24], q = 0.064; no CGM metric significant; exploratory SD of daily means log-OR +0.21 per SD, q = 5 × 10⁻⁴.
- Indoor PM2.5: HbA1c +7.6% per SD, q = 0.010; HbA1c beyond CGM p = 2.2 × 10⁻⁴.
- Resting heart rate: mean glucose +1.71 bpm per SD, p = 3 × 10⁻¹⁵; CGM beyond HbA1c p = 3.9 × 10⁻⁴; HbA1c beyond CGM p = 0.031.
- Steps: HbA1c +325 per SD, q = 0.033; HbA1c beyond CGM p = 0.002; CGM beyond HbA1c p = 0.06.
- Sleep: HbA1c −5.3 min per SD, q = 6 × 10⁻⁴; HbA1c beyond CGM p = 8 × 10⁻⁴.

### 5.4 Limitations

| Limitation | Why it matters |
| :--- | :--- |
| Cross-sectional, single visit | Direction of effect cannot be established; the PM2.5 and activity findings in particular admit reverse and confounded explanations. |
| 10-day CGM vs 8-12-week HbA1c | The two biomarkers integrate different time windows; part of the "extra information" in HbA1c may simply be longer averaging, and part of the CGM advantage may be recency. |
| No sex or race/ethnicity at individual level | Both affect HbA1c-glucose discordance and several outcomes; residual confounding is possible. Income was not adjusted (education only). |
| Self-reported comorbidities; MoCA and CES-D-10 are screening instruments | Measurement error attenuates effects and inflates the covariate-only baseline. |
| Wearable metrics are proxies | Resting heart rate is the daily 5th percentile, not Garmin's proprietary resting HR; the stress index is a proprietary HRV transform; steps depend on wear-day selection (means here are higher than the manifest averages used in NB31, which included non-wear days). |
| Single-room environmental sensor | Records one location for 10 days; exposure misclassification is likely and site/season dominate the variance. |
| Strong collinearity among CGM metrics (VIF up to 11) | Coefficients of individual metrics inside the four-metric block are unstable; single-metric models were used for inference. |
| Multiple outcomes and metrics | Controlled by BH-FDR within pre-defined families; the exploratory sweep (154 tests) is hypothesis-generating only. |
| Small incremental R² | Neither biomarker predicts any outcome usefully on its own; conclusions are about information content. |

### 5.5 Recommendations for the next iteration

1. Use **mean glucose and average daily SD** as the CGM pair in downstream comorbidity models; drop the mean/SD ratio; treat TIR as an alternative to daily SD, not an addition.
2. For depression, test the **between-day SD of daily means** (and nocturnal mean) as pre-specified predictors in a replication sample, together with sleep-regularity metrics from the wearable.
3. Model **HbA1c-CGM discordance** (e.g. HbA1c residualised on mean glucose, or HbA1c − GMI) directly as a predictor of activity, sleep and PM2.5; the present results predict it will be the active ingredient.
4. Add **interaction terms with diabetes status** (or restrict to the non-diabetic range) when studying cognition and autonomic outcomes, where the gradient is steepest.
5. If longitudinal AI-READI visits become available, re-estimate with **lagged CGM** to separate recency from window length.

---

## 6. References

- Battelino T, et al. Clinical targets for continuous glucose monitoring data interpretation: recommendations from the international consensus on time in range. *Diabetes Care* 2019;42:1593-1603.
- Beck RW, et al. The fallacy of average: how using HbA1c alone to assess glycemic control can be misleading. *Diabetes Care* 2017;40:994-999.
- Beck RW, et al. Validation of time in range as an outcome measure for diabetes clinical trials. *Diabetes Care* 2019;42:400-405.
- Bergenstal RM, et al. Racial differences in the relationship of glucose concentrations and hemoglobin A1c levels. *Ann Intern Med* 2017;167:95-102.
- Chen Z, et al. Ambient air pollutants have adverse effects on insulin and glucose homeostasis in Mexican Americans. *Diabetes Care* 2016;39:547-554.
- Crane PK, et al. Glucose levels and risk of dementia. *N Engl J Med* 2013;369:540-548.
- Lu J, et al. Association of time in range, as assessed by continuous glucose monitoring, with diabetic retinopathy in type 2 diabetes. *Diabetes Care* 2018;41:2370-2376.
- Spiegel K, Knutson K, Leproult R, Tasali E, Van Cauter E. Sleep loss: a novel risk factor for insulin resistance and type 2 diabetes. *J Appl Physiol* 2005;99:2008-2019.
- Yang B-Y, et al. Ambient air pollution in relation to diabetes and glucose-homoeostasis markers in China: a cross-sectional study with findings from the 33 Communities Chinese Health Study. *Lancet Planet Health* 2018;2:e64-e73.
- AI-READI Consortium. Flagship dataset of type 2 diabetes from the AI-READI project, v3.0.0. https://doi.org/10.60775/fairhub.3

*Figures*: [Fig. 1 forest plot](figures/fig1_forest_single_predictor_effects.png) · [Fig. 2 nested tests](figures/fig2_nested_test_heatmap.png) · [Fig. 3 cross-validated performance](figures/fig3_cv_performance.png) · [Fig. 4 predictor correlations](figures/fig4_predictor_correlations.png) · [Fig. 5 diabetes-stratified slopes](figures/fig5_diabetes_stratified.png) · [Fig. 6 sample flow](figures/fig6_sample_flow.png)
