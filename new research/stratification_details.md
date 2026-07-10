# Stratification & Methodology Details

This document provides a ground-up explanation of exactly how our analytical cohorts and subgroups were defined to ensure the precision and reproducibility of the exact CSV results.

## 1. Primary Stratification: Diabetes Severity

The central independent variable is **Diabetes Severity**. We stratified our patients into four mutually exclusive groups exactly mirroring the original AI-READI study design:

1. **Controls (`1_Controls`)**: Patients with no diagnosis of diabetes or pre-diabetes, and normal glycemic markers.
2. **Pre-diabetes / Lifestyle Controlled (`2_Pre-diabetes`)**: Patients diagnosed with pre-diabetes, or those with Type 2 Diabetes (T2DM) who manage their condition through lifestyle interventions (diet/exercise) without active pharmaceutical treatment.
3. **Medication-controlled (`3_Medication-controlled`)**: Patients with T2DM who use oral medications (e.g., Metformin) and/or non-insulin injectable medications (e.g., GLP-1 agonists like Ozempic/Mounjaro).
4. **Insulin-dependent (`4_Insulin-dependent`)**: Patients with T2DM who require exogenous insulin therapy, representing the most advanced and severe progression of the disease.

## 2. Outcome Variables (Cognitive Impairment)

We split cognitive impairment into two layers of granularity:

### A. Total Cognitive Impairment
Defined purely quantitatively through the Montreal Cognitive Assessment (MoCA). A total score of **< 26** is the universally accepted clinical cutoff for mild cognitive impairment (MCI). 

### B. Specific Clinical Cognitive Impairments
Defined by extracting specific conditions from the `condition_occurrence.csv` table via OMOP strings. This isolates specific pathological trajectories:
- **Alzheimer's Disease**: Extracted using the `mhoccur_ad` string flag.
- **Parkinson's Disease**: Extracted using the `mhoccur_pd` string flag.
- **Clinical Cognitive Impairment / Dementia**: Extracted using the `mhoccur_cogn` string flag.
- **Multiple Sclerosis**: Extracted using the `mhoccur_ms` string flag.
- **CNS Disease**: Extracted using the `mhoccur_cns` string flag.

## 3. Glycemic Metrics (The Comparison)

We compared two competing clinical markers of average blood glucose:

- **HbA1c (Hemoglobin A1c)**: The traditional lab measurement. It binds glucose to hemoglobin in red blood cells, effectively providing a 3-month retrospective average of blood glucose. It is extracted from the `measurement.csv` table.
- **GMI (Glucose Management Indicator)**: The modern wearable equivalent. It is mathematically derived exclusively from Continuous Glucose Monitoring (CGM) interstitial fluid readings over a minimum of 3 continuous days. Extracted from the raw `dexcom_g6` JSON files.

## 4. Covariate Adjustments
To ensure we are testing the true independent effect of diabetes severity, our logistic regressions rigorously stratify and adjust for:
- **Demographics**: `Age` and `Education Level` (Categorical: High school or below, College, Graduate).
- **Physical**: `BMI`.
- **Comorbidities**: `Hypertension`, `High Cholesterol`, `Kidney Disease`, and `Circulatory Problems` (all as binary flags).
*Note: We excluded neurodegenerative diseases as a covariate when predicting specific cognitive impairments, as they are collinear/identical to the outcome.*
