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
cd "/Users/guardian/Documents/GitHub/bcc/ucsf"

# Create virtual environment (if not already created)
python3 -m venv "new research/.venv"

# Activate environment & install dependencies
source "new research/.venv/bin/activate"
pip install -r requirements.txt
```

### Complete 3-Phase Execution Sequence

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
```

---

## 2. Research Architecture & 3-Phase Framework

The project is structured into three unified research phases:

| Phase | Purpose & Methodology | Source Scripts Directory | Output Reports Directory |
| :--- | :--- | :--- | :--- |
| **Phase 1: Baseline Replication** | Compares CGM (GMI/TIR) vs lab HbA1c to predict MoCA cognitive impairment ($\text{MoCA} < 26$). Validates construct validity and baseline ML models. | [`src/1_baseline_replication/`](new%20research/src/1_baseline_replication) | [`reports/1_baseline_replication/`](new%20research/reports/1_baseline_replication) |
| **Phase 2: Econometrics & Causal Inference** | Controls for confounding variables and lifestyle factors. Applies FWL partialling out, Fixed Effects, PSM, IV-2SLS, and 10,000-iter survey permutation tests. | [`src/2_advanced_causal_and_survey/`](new%20research/src/2_advanced_causal_and_survey) | [`reports/2_advanced_causal_and_survey/`](new%20research/reports/2_advanced_causal_and_survey) |
| **Phase 3: Spikes & Stratifications** | Models continuous glucose surge dynamics ($>180\text{ mg/dL}$), $3 \times 4$ Age x Diabetes grid stratifications, item-level PAID-5 distress, Welch's t-tests (SE), and non-linear interactions ($\text{Age}_{>65} \times \text{Diabetic}$). | [`src/3_spikes_surveys_and_interactions/`](new%20research/src/3_spikes_surveys_and_interactions) | [`reports/3_spikes_surveys_and_interactions/`](new%20research/reports/3_spikes_surveys_and_interactions) |

For complete documentation, variable dictionaries, and report indexes, refer to **[`new research/README.md`](new%20research/README.md)**.