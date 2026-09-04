# UCSF / AI-READI Data Compilation & Cognitive Impairment Analysis

- **Repository**: `ucsf-data-project`
- **Author**: Soham Kulkarni
- **Primary Module**: [`new research/`](new%20research/README.md)

This repository contains data parsing, statistical replication, econometrics, and machine learning pipelines analyzing the relationship between **diabetes severity (CGM vs. HbA1c)**, **glycemic surge dynamics**, **SDOH survey factors**, and **cognitive function (MoCA scores)** across the AI-READI cohort ($N = 2,226$).

---

## 1. Quick Start & Execution Guide

### Environment Setup
```bash
# Clone repository and navigate to root directory
cd ucsf

# Create virtual environment (if not already created)
python3 -m venv "new research/.venv"

# Activate environment & install dependencies
source "new research/.venv/bin/activate"
pip install -r requirements.txt
```

### Complete 5-Phase Execution Sequence

Run all research scripts in order from the repository root:

```bash
source "new research/.venv/bin/activate"

# ─── PHASE 1: BASELINE REPLICATION & VALIDATION ────────────────────────────
python3 "new research/src/1_baseline_replication/extract_data.py"
python3 "new research/src/1_baseline_replication/analyze_side_by_side.py"
python3 "new research/src/1_baseline_replication/moca_validity.py"
python3 "new research/src/1_baseline_replication/gridsearch_ml.py"
python3 "new research/src/1_baseline_replication/export_exact_results.py"

# ─── PHASE 2: ADVANCED ECONOMETRICS & SURVEY ANALYSIS ────────────────────
python3 "new research/src/2_advanced_causal_and_survey/extract_extended_data.py"
python3 "new research/src/2_advanced_causal_and_survey/survey_bootstrap.py"
python3 "new research/src/2_advanced_causal_and_survey/causal_inference.py"
python3 "new research/src/2_advanced_causal_and_survey/correlation_analysis.py"

# ─── PHASE 3: SPIKES, STRATIFICATIONS & INTERACTIONS ────────────────────
python3 "new research/src/3_spikes_surveys_and_interactions/cgm_spike_extraction.py"
python3 "new research/src/3_spikes_surveys_and_interactions/model_moca_spikes.py"
python3 "new research/src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py"
python3 "new research/src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py"
python3 "new research/src/3_spikes_surveys_and_interactions/paid_moca_analysis.py"
python3 "new research/src/3_spikes_surveys_and_interactions/interaction_stratified_models.py"

# ─── PHASE 4: PERSONALIZED SPIKES & ML FORECASTING ──────────────────────
python3 "new research/src/4_personalized_spike_analysis/01_personalized_spike_evaluation.py"
python3 "new research/src/4_personalized_spike_analysis/02_extract_sliding_windows.py"
python3 "new research/src/4_personalized_spike_analysis/03_predictive_spike_models.py"
python3 "new research/src/4_personalized_spike_analysis/04_diurnal_weekly_management.py"

# ─── PHASE 5: MULTIMODAL OUTCOME PREDICTION & COMORBIDITIES ─────────────
python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"   # CGM (54/70/180/250 cut-offs), OMOP, home sensor, Garmin
python3 "new research/src/5_multimodal_cgm_analysis/run_multimodal_cgm_models.py"     # nested HbA1c / CGM / combined models, CV, FDR, figures
python3 "new research/src/5_multimodal_cgm_analysis/generate_reports.py"              # markdown tables (research_report_02..04)
python3 "new research/src/5_multimodal_cgm_analysis/run_phase5_followups.py"          # follow-ups: CGM pair, HGI discordance, replication, splines (research_report_05)
```

---

## 2. Research Architecture & 5-Phase Framework

The project is structured into five unified research phases:

| Phase | Purpose & Methodology | Source Scripts Directory | Output Reports Directory |
| :--- | :--- | :--- | :--- |
| **Phase 1: Baseline Replication** | Compares CGM (GMI/TIR) vs lab HbA1c to predict MoCA cognitive impairment ($\text{MoCA} < 26$). Validates construct validity and baseline ML models. | [`src/1_baseline_replication/`](new%20research/src/1_baseline_replication) | [`reports/1_baseline_replication/`](new%20research/reports/1_baseline_replication) |
| **Phase 2: Econometrics & Causal Inference** | Controls for confounding variables and lifestyle factors. Applies FWL partialling out, Fixed Effects, PSM, IV-2SLS, and 10,000-iter survey permutation tests. | [`src/2_advanced_causal_and_survey/`](new%20research/src/2_advanced_causal_and_survey) | [`reports/2_advanced_causal_and_survey/`](new%20research/reports/2_advanced_causal_and_survey) |
| **Phase 3: Spikes & Stratifications** | Models continuous glucose surge dynamics ($>180\text{ mg/dL}$), $3 \times 4$ Age x Diabetes grid stratifications, item-level PAID-5 distress, Welch's t-tests (SE), and non-linear interactions ($\text{Age}_{>65} \times \text{Diabetic}$). | [`src/3_spikes_surveys_and_interactions/`](new%20research/src/3_spikes_surveys_and_interactions) | [`reports/3_spikes_surveys_and_interactions/`](new%20research/reports/3_spikes_surveys_and_interactions) |
| **Phase 4: Personalized Spike ML** | Standardizes patient baselines ($Z_{i,t} \ge 2.0$), trains 15m/30m/60m GroupKFold forecasting models, and evaluates 168-hr weekly glycemic management. | [`src/4_personalized_spike_analysis/`](new%20research/src/4_personalized_spike_analysis) | [`reports/4_personalized_spike_analysis/`](new%20research/reports/4_personalized_spike_analysis) |
| **Phase 5: CGM vs HbA1c for Comorbidity Prediction** | Tests whether four pre-specified CGM metrics (mean glucose, mean/SD, average daily TIR 70-180, average daily SD) predict cognition (MoCA), depression (CES-D-10), the home environment (LeeLab Anura) and wearable physiology (Garmin) better than HbA1c. Identical-sample nested models (covariates / HbA1c / CGM / combined), HC3 t and Wald z slope tests, nested F/LR tests, repeated 10-fold CV, DeLong, bootstrap, BH-FDR, diabetes-stratified and non-linearity checks. Main narrative: [`research_report_01_cgm_vs_hba1c_comorbidity_prediction.md`](new%20research/reports/5_multimodal_cgm_analysis/research_report_01_cgm_vs_hba1c_comorbidity_prediction.md); follow-ups (two-metric CGM pair, HbA1c-CGM discordance, split-sample replication, dose-response splines, split-half stability): [`research_report_05_followups_parsimony_discordance_replication.md`](new%20research/reports/5_multimodal_cgm_analysis/research_report_05_followups_parsimony_discordance_replication.md). | [`src/5_multimodal_cgm_analysis/`](new%20research/src/5_multimodal_cgm_analysis) | [`reports/5_multimodal_cgm_analysis/`](new%20research/reports/5_multimodal_cgm_analysis) |

For complete documentation, variable dictionaries, and report indexes, refer to **[`new research/README.md`](new%20research/README.md)**.