"""
Phase 6 - report generator (same table format as Phase 5)
Writes:
  reports/6_subgroup_single_predictor_analysis/research_report_02_full_single_predictor_tables.md
  reports/6_subgroup_single_predictor_analysis/research_report_03_glucose_band_analyses.md
  reports/6_subgroup_single_predictor_analysis/research_report_04_methods_and_sample_log.md
The narrative (research_report_01_*.md) is written separately.
"""

import os
import sys
import json
import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from run_phase6_analysis import (PREDICTORS, GROUPS, BANDS, OUT_DATA, REPORT_DIR, FDR_MIN_N, OUTCOMES, HBA1C)  # noqa: E402


def fmt_p(p):
    if pd.isna(p):
        return "-"
    return f"{p:.1e}" if p < 0.001 else f"{p:.3f}"


def stars(p):
    return "" if pd.isna(p) else ("***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "")


def md_table(df, cols, headers=None):
    headers = headers or cols
    esc = lambda v: str(v).replace("|", "\\|") if "\\|" not in str(v) else str(v)
    out = ["| " + " | ".join(esc(h) for h in headers) + " |", "| " + " | ".join([":---"] + [":---:"] * (len(cols) - 1)) + " |"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(esc(r[c]) for c in cols) + " |")
    return "\n".join(out)


def eff(r):
    if r["kind"] == "logit":
        return f"OR {r['or_per_sd']:.3f} [{r['or_ci_low']:.3f}, {r['or_ci_high']:.3f}]"
    return f"{r['beta_per_sd']:+.3f} [{r['ci_low_per_sd']:+.3f}, {r['ci_high_per_sd']:+.3f}]"


def qcell(r, col):
    if not r["fdr_applied"]:
        return f"not applied (n < {FDR_MIN_N})"
    q = r[col]
    return fmt_p(q) + (" (FDR<0.05)" if q < 0.05 else "")


def load():
    res = pd.read_csv(os.path.join(OUT_DATA, "single_predictor_results_all_groups.csv"))
    fe = pd.read_csv(os.path.join(OUT_DATA, "band_feasibility.csv"))
    counts = pd.read_csv(os.path.join(OUT_DATA, "significance_counts_by_group.csv"))
    cfg = json.load(open(os.path.join(OUT_DATA, "config.json")))
    return res, fe, counts, cfg


def prep(res):
    r = res.copy()
    ok = r["skipped_reason"].fillna("") == ""
    r.loc[ok, "Effect per 1 SD (95% CI)"] = r[ok].apply(eff, axis=1)
    r.loc[ok, "raw slope"] = r[ok].apply(lambda x: f"{x['beta_raw']:.4g}", axis=1)
    r.loc[ok, "t / z"] = r[ok]["stat"].map(lambda v: f"{v:.2f}")
    r.loc[ok, "p (raw)"] = r[ok]["p"].map(lambda v: fmt_p(v) + stars(v))
    r.loc[ok, "q (BH, all tests in population)"] = r[ok].apply(lambda x: qcell(x, "q_bh_group_all_tests"), axis=1)
    r.loc[ok, "q (BH, within outcome)"] = r[ok].apply(lambda x: qcell(x, "q_bh_group_outcome"), axis=1)
    r.loc[ok, "dAIC vs covariates"] = r[ok]["delta_aic_vs_covariates"].map(lambda v: f"{v:+.1f}")
    r.loc[ok, "dAIC vs HbA1c model"] = r[ok]["delta_aic_vs_hba1c_model"].map(lambda v: "-" if pd.isna(v) else f"{v:+.1f}")
    r.loc[ok, "CV R2/AUC (pred | covs only)"] = r[ok].apply(lambda x: f"{x['cv_score']:.4f} | {x['cv_score_covariates_only']:.4f}", axis=1)
    r.loc[ok, "coef"] = r[ok]["beta_raw"].map(lambda v: f"{v:+.4g}")
    r.loc[ok, "se"] = r[ok]["se_raw"].map(lambda v: f"{v:.4g}")
    r.loc[ok, "ci"] = r[ok].apply(lambda x: f"[{x['ci_low_raw']:.4g}, {x['ci_high_raw']:.4g}]", axis=1)
    r.loc[ok, "sig"] = r[ok]["p"].map(stars)
    r.loc[ok, "fit"] = r[ok].apply(lambda x: f"{x['adj_r2']:.4f}" if x["kind"] == "ols" else f"{x['auc_in_sample']:.4f}", axis=1)
    r["Predictor"] = r["predictor"].map(lambda p: SHORT.get(p, PREDICTORS.get(p, (p,))[0]))
    r["_po"] = r["predictor"].map({p: i for i, p in enumerate(PREDICTORS)}).fillna(999)
    r["_oo"] = r["outcome"].map({c: i for i, (_, c, *_) in enumerate(OUTCOMES)})
    return r


def two_tables(okk, extra_cols=None, extra_hdr=None):
    """model-output table (A) followed by effect-size / multiplicity / fit table (B)"""
    ca, ha = COLS_A, HDR_A
    if extra_cols:
        ca = ca[:2] + extra_cols + ca[2:]; ha = ha[:2] + extra_hdr + ha[2:]
    return ("**(A) Model output, raw scale (each row = one covariate-adjusted model with that predictor alone)**\n\n" + md_table(okk, ca, ha) +
            "\n\n**(B) Standardised effect, multiplicity and fit**\n\n" + md_table(okk, COLS_B, HDR_B))


SHORT = {"hba1c": "HbA1c", "mean_glucose": "Mean glucose", "gmi": "GMI", "nocturnal_mean": "Nocturnal mean", "glucose_sd": "SD (pooled)",
         "avg_daily_sd": "SD (daily avg)", "glucose_cv": "CV", "mean_to_sd_ratio": "Mean/SD", "avg_daily_mean_to_sd": "Mean/SD (daily avg)",
         "mag_mg_dl_per_h": "MAG", "avg_daily_range": "Daily range", "sd_of_daily_means": "SD of daily means", "tir_overall": "TIR 70-180 (pooled)",
         "avg_daily_tir": "TIR 70-180 (daily avg)", "any_below_54": "Any <54 (0/1)", "pct_severe_hypo": "%<54 (pooled)", "avg_daily_pct_below_54": "%<54 (daily avg)",
         "pct_mod_hypo": "%54-69 (pooled)", "avg_daily_pct_54_69": "%54-69 (daily avg)", "tbr_below_70": "%<70 (pooled)", "avg_daily_tbr": "%<70 (daily avg)",
         "pct_54_250": "%54-250 (pooled)", "avg_daily_pct_54_250": "%54-250 (daily avg)", "pct_mod_hyper": "%181-250 (pooled)", "avg_daily_pct_181_250": "%181-250 (daily avg)",
         "tar_above_180": "%>180 (pooled)", "avg_daily_tar": "%>180 (daily avg)", "nocturnal_tar": "%>180 nocturnal", "any_above_250": "Any >250 (0/1)",
         "pct_severe_hyper": "%>250 (pooled)", "avg_daily_pct_above_250": "%>250 (daily avg)"}
# Table A = model output (raw scale, one row per single-predictor model); Table B = effect size, multiplicity and fit
COLS_A = ["Predictor", "n", "coef", "se", "ci", "t / z", "p (raw)", "sig"]
HDR_A = ["Predictor (alone)", "N", "Coef (β)", "Std. Err.", "95% CI", "t / z", "Pr(>\\|t\\|)", "Signif"]
COLS_B = ["Predictor", "Effect per 1 SD (95% CI)", "q (BH, all tests in population)", "q (BH, within outcome)", "fit", "dAIC vs covariates", "dAIC vs HbA1c model", "CV R2/AUC (pred | covs only)"]
HDR_B = ["Predictor (alone)", "β per 1 SD (95% CI)", "q, all tests in population", "q, this outcome", "Adj R² / AUC", "ΔAIC vs covs", "ΔAIC vs HbA1c", "CV R²/AUC (predictor vs covariates-only)"]
COLS, HDR = COLS_A, HDR_A


def write_full(res, fe, counts, cfg):
    r = prep(res)
    L = ["# Phase 6 - Full single-predictor tables by population (total / healthy / non-healthy)", "",
         "Generated by `src/6_subgroup_single_predictor_analysis/generate_phase6_reports.py` from `data/single_predictor_results_all_groups.csv`.",
         "",
         "**Table layout.** For every outcome two tables are given: (A) the model output on the raw scale, one row per single-predictor model (coefficient per unit of the predictor, HC3 standard error, 95% CI, t or z, p, significance stars); (B) the standardised effect per 1 SD, BH q-values, adjusted R² (or AUC), AIC differences and cross-validated performance. Complete term-by-term output for every model (intercept and covariates included) is in `model_output_tables/` (index: `model_output_tables/README.md`, split by population and domain) and `phase6_model_outputs.csv`.",
         "",
         "**Design.** Every glycaemic measure is entered on its own: `outcome ~ covariates + predictor`. Covariates are identical to Phase 5 "
         "(age, BMI, education level, clinical site, hypertension, high cholesterol, kidney disease, circulatory disease; season of visit for home-environment outcomes). "
         "Continuous outcomes: OLS with HC3-robust t-tests; binary outcomes: logistic regression with Wald z-tests. Effects are per 1 SD of the predictor, "
         "with the SD computed in the population and outcome sample shown. dAIC compares the predictor model with the covariates-only model and with the HbA1c-only model fitted on the same rows "
         "(negative = better than the comparator). CV = repeated 3 x 10-fold out-of-sample R2 (continuous) or AUC (binary).",
         "",
         f"**FDR policy.** Benjamini-Hochberg adjustment is reported only when the sample behind the test has n >= {FDR_MIN_N} participants (rule #3, 'FDR only on large datasets'). "
         "Two families are shown: (i) all tests in the population (every predictor x every outcome), the most conservative; (ii) all predictors for one outcome. Raw p-values are always shown.",
         "", "**Populations.**", ""]
    for g, (glabel, _) in GROUPS.items():
        L.append(f"- `{g}`: {glabel}")
    L += ["", f"Analysis base N = {cfg['n_base']:,}: healthy {cfg['n_healthy']:,}, non-healthy {cfg['n_non_healthy']:,} (same base and per-outcome complete-case rule as Phase 5).", "",
          "## Significance counts", ""]
    c = counts.copy(); c["group"] = c["group"].map(lambda g: GROUPS[g][0])
    L.append(md_table(c, ["group", "tests", "n_min", "n_max", "sig_raw", "fdr_applied", "sig_fdr_all", "sig_fdr_outcome"],
                      ["Population", "Tests run", "n min", "n max", "Significant raw p < 0.05", "Tests with FDR applied", "Significant q < 0.05 (all-tests family)", "Significant q < 0.05 (within-outcome family)"]))
    for g, (glabel, _) in GROUPS.items():
        L += ["", "---", "", f"## Population: {glabel}", ""]
        for dom in ["Cognition", "Depression", "Home environment", "Wearable activity"]:
            L.append(f"### Domain: {dom}\n")
            for d, y, kind, lab, _, _ in OUTCOMES:
                if d != dom:
                    continue
                sub = r[(r.group == g) & (r.outcome == y)].sort_values("_po")
                okk = sub[sub["skipped_reason"].fillna("") == ""]
                if len(okk) == 0:
                    L.append(f"#### {lab}\n_no models (insufficient sample or events)_\n"); continue
                n = int(okk["n"].max()); ev = okk["events"].dropna()
                L.append(f"#### {lab}\n*n = {n:,}" + (f"; events = {int(ev.iloc[0])}" if len(ev) else "") + f"; estimator = {'OLS (HC3)' if kind == 'ols' else 'logistic (Wald)'}; FDR {'applied' if okk['fdr_applied'].any() else 'not applied (n < ' + str(FDR_MIN_N) + ')'}*\n")
                L.append(two_tables(okk))
                sk = sub[sub["skipped_reason"].fillna("") != ""]
                if len(sk):
                    L.append("\nSkipped: " + "; ".join(f"{PREDICTORS[p][0]} ({why})" for p, why in zip(sk["predictor"], sk["skipped_reason"])))
                L.append("")
    with open(os.path.join(REPORT_DIR, "research_report_02_full_single_predictor_tables.md"), "w") as f:
        f.write("\n".join(L))


def write_bands(res, fe, cfg):
    r = prep(res)
    L = ["# Phase 6 - Glucose-band analyses (54-69, 54-250, > 180 and the other bands) vs the usual 70-180 range", "",
         "Glucose categories: severe hypo < 54; moderate hypo 54-69; normal / TIR 70-180; moderate hyper 181-250; severe hyper > 250 (mg/dL). "
         "Each band metric is the percentage of CGM time in the band (pooled over all valid readings, and the mean of the daily percentages over valid days), entered alone with the Phase 5 covariates. "
         "For the sparse bands < 54 and > 250 a 0/1 indicator (any reading in the band during wear) is also tested.", "",
         "## 1. Are there enough people outside 54-250?", "",
         "A band is called *feasible* when at least 100 participants in the population have >= 1 % of their CGM time in it; *marginal* when >= 100 have any time but fewer than 100 have >= 1 %.", ""]
    f2 = fe.copy(); f2["group"] = f2["group"].map(lambda g: GROUPS[g][0])
    for c in ["pct_any_time", "mean_pct_time", "median_pct_time", "p90_pct_time", "max_pct_time", "median_pct_time_among_exposed"]:
        f2[c] = f2[c].map(lambda v: f"{v:.2f}")
    L.append(md_table(f2, ["group", "band", "n", "n_any_time", "pct_any_time", "n_ge_1pct", "n_ge_5pct", "n_ge_10pct", "mean_pct_time", "median_pct_time", "p90_pct_time", "max_pct_time", "median_pct_time_among_exposed", "enough_for_regression"],
                      ["Population", "Band", "n", "Any time in band", "% of participants", ">= 1% time", ">= 5% time", ">= 10% time", "Mean % time", "Median % time", "90th pct % time", "Max % time", "Median % time among exposed", "Feasible?"]))
    tot = fe[fe.group == "total"]
    L += ["", f"Total CGM readings below 54 mg/dL across the base: {int(tot.loc[tot.band == '<54', 'n_readings_below_54_total'].iloc[0]):,}; above 250: {int(tot.loc[tot.band == '>250', 'n_readings_above_250_total'].iloc[0]):,}.", ""]
    for band in ["70-180", "54-69", "<70", "54-250", ">180", "181-250", ">250", "<54"]:
        L += ["", "---", "", f"## Band {band}", ""]
        for g, (glabel, _) in GROUPS.items():
            L.append(f"### {glabel}\n")
            sub = r[(r.group == g) & (r.band == band)].sort_values(["_oo", "_po"])
            okk = sub[sub["skipped_reason"].fillna("") == ""]
            if len(okk) == 0:
                L.append("_no models_\n"); continue
            okk = okk.copy(); okk["Outcome"] = okk["label"].map(lambda l: l.split(" (")[0])
            okk["exposed"] = okk["n_exposed_gt0"].map(lambda v: "-" if pd.isna(v) else f"{int(v)}")
            okk["Predictor"] = okk["Outcome"] + " ~ " + okk["Predictor"]
            L.append(two_tables(okk, ["exposed"], ["N with time in band"]))
            sk = sub[sub["skipped_reason"].fillna("") != ""]
            if len(sk):
                L.append("\nSkipped: " + "; ".join(f"{lab}: {PREDICTORS[p][0]} ({why})" for lab, p, why in zip(sk["label"], sk["predictor"], sk["skipped_reason"])))
            L.append("")
    with open(os.path.join(REPORT_DIR, "research_report_03_glucose_band_analyses.md"), "w") as f:
        f.write("\n".join(L))


def write_methods(res, cfg):
    L = ["# Phase 6 - Methods, sample construction and execution log", "",
         "## Execution", "", "```bash", 'source "new research/.venv/bin/activate"',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/extract_phase6_dataset.py"   # Phase 5 extractor + glucose-band metrics -> data/master_phase6_dataset.csv',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/run_phase6_analysis.py"     # ~10 min',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/generate_phase6_reports.py"',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/run_phase6b_glucose_cohorts.py"',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/generate_phase6b_reports.py"',
         'python3 "new research/src/6_subgroup_single_predictor_analysis/export_model_output_tables.py"   # full term-by-term model outputs', "```", "",
         "## Sample construction (identical to Phase 5)", "",
         "1. `master_phase6_dataset.csv` (2,280 rows) from `extract_phase6_dataset.py` (the Phase 5 extractor plus band metrics); CGM readings 39-401 mg/dL, site-local time, valid day = >= 70 % of 288 readings, no truncation of the wear period.",
         f"2. Analysis base = >= 3 valid CGM days, laboratory HbA1c present, four core CGM metrics present, complete covariates -> N = {cfg['n_base']:,}.",
         f"3. Populations: total ({cfg['n_base']:,}); healthy = study groups `healthy` + `pre_diabetes_lifestyle_controlled` ({cfg['n_healthy']:,}); non-healthy = `oral_medication_and_or_non_insulin_injectable_medication_controlled` + `insulin_dependent` ({cfg['n_non_healthy']:,}).",
         "4. For each population and outcome: complete cases on the outcome and covariates (season for environmental outcomes). For each predictor: the outcome sample minus participants missing that predictor (day-level band metrics can be missing only for very short wear). Every predictor for a given population x outcome is therefore fitted on the same rows except for those rare predictor-specific losses, which are visible in the `n` column.",
         "5. Band predictors are skipped when fewer than 30 participants in the sample have any time in the band (recorded in the tables as 'skipped').", "",
         "## Models and tests", "",
         "- `outcome ~ covariates + predictor`, one predictor at a time (rule #2). No combined HbA1c + CGM models in this phase.",
         "- OLS with HC3-robust standard errors (t-test) for continuous outcomes; logistic regression with Wald z for binary outcomes.",
         "- Effects per 1 SD of the predictor (SD in that population and outcome sample); raw slope per unit also reported.",
         "- AIC of the predictor model minus AIC of (a) the covariates-only model and (b) the HbA1c-only model on the same rows.",
         "- Out-of-sample R2 / AUC from repeated 3 x 10-fold cross-validation for the predictor model and the covariates-only model.",
         f"- FDR (rule #3): Benjamini-Hochberg applied only to tests whose sample has n >= {FDR_MIN_N}; families = (i) all tests in the population, (ii) all predictors within one outcome, (iii) all outcomes within one predictor, (iv) all tests within one band. Raw p-values are always reported alongside.", "",
         "## How 'pooled' and 'day-averaged' metrics are calculated", "",
         "Let g_1 ... g_N be every valid Dexcom reading of a participant over the whole wear (all days concatenated, 5-min sampling, values 39-401 mg/dL, site-local time; N is typically ~2,850 for 10 days). "
         "Let D be the set of *valid* calendar days (days holding >= 70 % of the expected 288 readings) and g_{d,1} ... g_{d,n_d} the readings on day d.", "",
         "- **Pooled** metric = one statistic computed over all N readings at once, ignoring day boundaries. Examples: mean glucose = (1/N) sum g_i; pooled SD = sqrt( sum (g_i - mean)^2 / (N-1) ); pooled time in 70-180 = 100 x #{i : 70 <= g_i <= 180} / N; pooled time > 250 = 100 x #{i : g_i > 250} / N. Every reading counts equally, so days with more readings weigh more, and partial days are included.",
         "- **Day-averaged** metric = compute the statistic separately on each valid day, then take the unweighted mean over valid days: avg. daily SD = (1/|D|) sum_d SD(g_{d,.}); avg. daily time in 70-180 = (1/|D|) sum_d [100 x #{j : 70 <= g_{d,j} <= 180} / n_d]; likewise for every band. Each day counts equally, partial days (< 70 % complete) are excluded, and the within-day SD is not inflated by day-to-day drift in the mean.",
         "- The two versions correlate at rho ~ 0.98-0.99 for TIR and SD in this cohort and give the same conclusions; the day-averaged form is the one the collaborator asked for ('average daily TIR', 'average daily SD'), the pooled form matches Phase 1-4 and the international consensus reporting.",
         "- Related between-day metric: SD of daily means = SD over valid days of the daily mean glucose (captures day-to-day drift rather than within-day swings).",
         "- 'Any reading < 54' / 'any reading > 250' = 1 if at least one valid reading falls in the band during the wear, else 0.", "",
         "## Predictors", "", "| Column | Label | Family | Band |", "| :--- | :--- | :--- | :--- |"]
    for p, (lab, fam, band) in PREDICTORS.items():
        L.append(f"| `{p}` | {lab} | {fam} | {band} |")
    L += ["", "## Outcomes (as in Phase 5)", "", "| Domain | Column | Type | Label |", "| :--- | :--- | :--- | :--- |"]
    for d, y, kind, lab, _, _ in OUTCOMES:
        L.append(f"| {d} | `{y}` | {'OLS' if kind == 'ols' else 'logistic'} | {lab} |")
    sc = os.path.join(OUT_DATA, "analysis_sample_construction.json")
    if os.path.exists(sc):
        S = json.load(open(sc)); fu = S["funnel"]; po = S["per_outcome"]
        L += ["", "## Exact sample construction (how the 'same-size' samples are made; shared with Phase 5)", "",
              "No participant was truncated to a fixed number of days and no outcome sample was trimmed to match another. 'Same size' means one rule applied within each outcome: "
              "every model for that outcome is fitted on the identical participants, obtained by list-wise deletion on the union of the variables it uses. "
              "Person-level membership is in `data/analysis_sample_membership_by_outcome.csv` (one row per participant, one 0/1 column per step and per outcome); counts are in `data/analysis_sample_construction.json`.", "",
              "| Step | Rule | Participants |", "| :--- | :--- | :---: |",
              f"| 0 | AI-READI v3.0.0 participants | {fu['0_all_participants']:,} |",
              f"| 1 | >= 3 valid CGM days (valid day = >= 70% of 288 readings; all valid readings used, 3-12 days, median 9) | {fu['1_cgm_ge3_valid_days']:,} |",
              f"| 2 | + laboratory HbA1c present | {fu['2_plus_hba1c']:,} |",
              f"| 3 | + four core CGM metrics present | {fu['3_plus_4_core_cgm_metrics']:,} |",
              f"| 4 | + complete covariates (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease) | **{fu['4_plus_complete_covariates_(analysis_base)']:,}** (analysis base) |", "",
              "Per-outcome samples (base minus participants missing that outcome; season of visit was never missing):", "",
              "| Outcome | N | Lost from base (missing outcome) |", "| :--- | :---: | :---: |"]
        for k, v in po.items():
            L.append(f"| {v['label']} | {v['n']:,}" + (f" ({v['events']} events)" if v.get("events") else "") + f" | {v['lost_from_base_due_to_missing_outcome']} |")
        L += ["", "Covariate losses at step 4: BMI 4, education 11. Wearable losses: 248 with no Garmin record plus 18 with < 3 wear-days. Environment losses: 38 without >= 1 h of sensor data "
              "(84 participants with sensor data but < 3 sensor days were retained for the environmental outcomes, as in Phase 5). Populations: healthy = no diabetes + pre-diabetes/lifestyle; non-healthy = T2D oral/non-insulin + insulin."]
    with open(os.path.join(REPORT_DIR, "research_report_04_methods_and_sample_log.md"), "w") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    res, fe, counts, cfg = load()
    write_full(res, fe, counts, cfg)
    write_bands(res, fe, cfg)
    write_methods(res, cfg)
    print("reports written to", REPORT_DIR)
