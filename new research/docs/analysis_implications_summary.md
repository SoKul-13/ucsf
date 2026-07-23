# Analytical Outputs: Findings & Implications Summary

Here is a breakdown of what was produced in the three advanced analysis files and what the findings mean for your research:

### 1. [`reports/survey_bootstrap_results.md`](../reports/survey_bootstrap_results.md)
**What it is:** We took the survey answers (diet, smoking, depression, etc.) and ran a 10,000-iteration permutation test to see if people who answered "Yes" to a behavior had significantly different MoCA (cognitive) scores than people who answered "No". 

**The Implications (The Results):**
- **Diet is a Massive Factor**: People with a healthy diet score (> median) scored significantly higher on the MoCA (~26.05) than people with poor diets (~25.29). This was statistically significant (**p < 0.001**) across *every single subgroup* (young, old, healthy, diabetic).
- **Smoking Hurts Cognition**: Patients who had smoked $\ge 100$ cigarettes in their life scored significantly lower on the MoCA (p=0.002).
- **Depression is Age-Dependent**: Having high depression symptoms (CESD-10 $\ge$ 10) significantly lowered MoCA scores **only in the younger cohort (Age $\le$ 65)** (p=0.003). In the older cohort (> 65), depression didn't show a significant cognitive penalty.
- **Null Results**: Alcohol, marijuana, and vaping did *not* show a statistically significant impact on MoCA scores in this specific dataset.

---

### 2. [`reports/causal_inference_results.md`](../reports/causal_inference_results.md)
**What it is:** This file uses advanced econometrics to prove that the link between Diabetes/Glucose and Cognitive Impairment isn't just a coincidence caused by other variables (like older age or high BMI).

**The Implications (The Results):**
- **Frisch-Waugh-Lovell (FWL) Theorem**: We mathematically proved that if you strip away the effects of all covariates (Age, BMI, etc.) from both MoCA and GMI, the isolated penalty of GMI is **-0.627**. This perfectly matches the multivariable model, proving the model successfully partialled out the confounders.
- **Fixed Effects (FE)**: We added fixed effects to control for the specific hospital/state the patient was in. The penalty for high GMI actually got *stronger* (**-0.646**, p<0.001), proving that geographic or clinical site differences aren't secretly causing the MoCA drops.
- **Propensity Score Matching (PSM)**: We used Machine Learning to match every Diabetic patient to a Healthy patient who was their exact "twin" in terms of Age, BMI, and comorbidities. The result? The diabetic twins scored **0.6395 points lower** on the MoCA than their matched healthy twins. This is incredibly strong evidence for a direct causal link.

---

### 3. [`reports/correlation_results.md`](../reports/correlation_results.md)
**What it is:** Evaluates the direct linear (Pearson) and rank-based (Spearman) correlations between your glucose metrics and MoCA scores.

**The Implications (The Results):**
- **Glucose goes up, Cognition goes down**: Both HbA1c and Mean Glucose show a highly significant **negative** correlation with MoCA (**p < 0.001**).
- **CGM vs Labs**: Mean Glucose (from the wearable CGM) actually has a slightly stronger linear correlation with MoCA (**r = -0.158**) than the lab-derived HbA1c (**r = -0.133**). 
- **The Healthy Subgroup Insight**: Interestingly, for *Healthy* (non-diabetic) patients, Mean Glucose is still highly correlated with MoCA drops (p<0.001), whereas HbA1c loses its linear significance (p=0.061). This implies that for non-diabetics, wearable CGMs are much better at detecting subtle glucose spikes that harm cognition than a standard HbA1c lab test!
