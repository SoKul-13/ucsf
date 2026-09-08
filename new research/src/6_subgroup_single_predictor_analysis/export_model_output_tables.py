"""
Export every fitted model of Phases 6 and 6b in the repository's standard
"OLS model output" table format (the format used in Phase 4):

    **Regression Call / Formula**: `outcome ~ ...`
    **Model Diagnostics**: N, R2, Adj R2, F-statistic (p), Residual SE, AIC, BIC   (OLS)
                           N, events, McFadden R2, LLR chi2 (p), AUC, AIC, BIC       (logistic)
    | Term / Variable | Coef Estimate (b) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>|t|) | Signif |

Every term (intercept, covariates and the glycaemic predictor) is listed.  OLS standard errors are
HC3 heteroskedasticity-robust, as in the reports; logistic tables show z, and an odds-ratio column.
Nothing is re-analysed: the same formulas, samples and estimators are re-fitted (without the
cross-validation / bootstrap steps) to recover the full coefficient tables.

Outputs
  reports/6_subgroup_single_predictor_analysis/model_output_tables/phase6_<group>.md + phase6_model_outputs.csv
  reports/6_subgroup_single_predictor_analysis/model_output_tables/phase6b_<cohort>_<group>.md + phase6b_model_outputs.csv
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.metrics import roc_auc_score

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src", "5_multimodal_cgm_analysis"))   # unchanged Phase 5 model helpers
from run_multimodal_cgm_models import (COV_FORMULA, BASE_COVS, OUTCOMES, CORE_CGM, HBA1C, PRED_LABEL, DATA_DIR)  # noqa: E402
import run_phase6_analysis as P6  # noqa: E402
import run_phase6b_glucose_cohorts as P6B  # noqa: E402

warnings.filterwarnings("ignore")

R6 = os.path.join(PROJECT_ROOT, "reports", "6_subgroup_single_predictor_analysis", "model_output_tables")
os.makedirs(R6, exist_ok=True)

TERM_LABEL = {
    "Intercept": "Intercept", "age": "Age (years)", "bmi": "BMI (kg/m2)",
    "C(education_level)[T.Graduate level]": "Education: graduate level (vs college)",
    "C(education_level)[T.High school or below]": "Education: high school or below (vs college)",
    "C(clinical_site)[T.UCSD]": "Site: UCSD (vs UAB)", "C(clinical_site)[T.UW]": "Site: UW (vs UAB)",
    "hypertension": "Hypertension", "high_cholesterol": "High cholesterol", "kidney_disease": "Kidney disease",
    "circulatory_problems": "Circulatory disease", "C(visit_season)[T.spring]": "Season: spring (vs autumn)",
    "C(visit_season)[T.summer]": "Season: summer (vs autumn)", "C(visit_season)[T.winter]": "Season: winter (vs autumn)",
    "any_diabetes": "Type 2 diabetes (0/1)", "hgi": "HGI (HbA1c residual on mean glucose)", "glycation_gap": "Glycation gap (HbA1c - GMI)",
    "hemoglobin_g_dl": "Haemoglobin (g/dL)", "mcv_fl": "MCV (fL)", "rdw_pct": "RDW (%)",
}
TERM_LABEL.update({k: v for k, v in PRED_LABEL.items()})
TERM_LABEL.update({k: v[0] for k, v in P6.PREDICTORS.items()})
TERM_LABEL.update({"gmi": "GMI (%)", "glucose_cv": "CV (%)", "tar_above_180": "Time > 180 (%)", "pct_severe_hyper": "Time > 250 (%)",
                   "tbr_below_70": "Time < 70 (%)", "pct_severe_hypo": "Time < 54 (%)", "mag_mg_dl_per_h": "MAG (mg/dL/h)",
                   "avg_daily_range": "Avg. daily range (mg/dL)", "sd_of_daily_means": "SD of daily means (mg/dL)",
                   "nocturnal_mean": "Nocturnal mean 00-06h (mg/dL)", "avg_daily_mean_to_sd": "Avg. daily mean/SD"})


def sig(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "." if p < 0.1 else ""


def fmt_p(p):
    return f"{p:.2e}" if p < 0.001 else f"{p:.4f}"


def fit_full(formula, d, kind):
    """returns (robust fit for the table, ML fit for diagnostics)"""
    if kind == "ols":
        ml = smf.ols(formula, data=d).fit()
        rb = smf.ols(formula, data=d).fit(cov_type="HC3")
    else:
        ml = smf.logit(formula, data=d).fit(disp=0, maxiter=200)
        rb = ml
    return rb, ml


def model_rows(rb, ml, d, y, kind, meta):
    rows = []
    ci = rb.conf_int()
    if kind == "ols":
        diag = {"N_obs": int(ml.nobs), "R_squared": float(ml.rsquared), "Adj_R_squared": float(ml.rsquared_adj),
                "F_stat": float(ml.fvalue), "F_pvalue": float(ml.f_pvalue), "RSE": float(np.sqrt(ml.mse_resid)),
                "df_resid": int(ml.df_resid), "AIC": float(ml.aic), "BIC": float(ml.bic), "LogLik": float(ml.llf),
                "Events": np.nan, "McFadden_R2": np.nan, "LLR_chi2": np.nan, "LLR_pvalue": np.nan, "AUC": np.nan}
    else:
        pred = np.asarray(ml.predict(d))
        diag = {"N_obs": int(ml.nobs), "R_squared": np.nan, "Adj_R_squared": np.nan, "F_stat": np.nan, "F_pvalue": np.nan,
                "RSE": np.nan, "df_resid": int(ml.df_resid), "AIC": float(ml.aic), "BIC": float(ml.bic), "LogLik": float(ml.llf),
                "Events": int(d[y].sum()), "McFadden_R2": float(ml.prsquared), "LLR_chi2": float(ml.llr), "LLR_pvalue": float(ml.llr_pvalue),
                "AUC": float(roc_auc_score(d[y], pred))}
    for t in rb.params.index:
        b = float(rb.params[t]); se = float(rb.bse[t]); st = float(rb.tvalues[t]); p = float(rb.pvalues[t])
        rows.append({**meta, "Term": t, "Term_Label": TERM_LABEL.get(t, t), "Coefficient": b, "Std_Error": se, "Margin_2SE": 2 * se,
                     "t_or_z": st, "p_value": p, "CI_low": float(ci.loc[t, 0]), "CI_high": float(ci.loc[t, 1]),
                     "Odds_Ratio": float(np.exp(b)) if kind == "logit" else np.nan, "Significance": sig(p), **diag})
    return rows


def md_model_block(rows, kind, title):
    r0 = rows[0]
    L = [f"#### {title}", f"**Regression Call / Formula**: `{r0['Formula']}`  "]
    if kind == "ols":
        L.append(f"**Model Diagnostics**: N = **{r0['N_obs']}**, R² = **{r0['R_squared']:.4f}**, Adj R² = **{r0['Adj_R_squared']:.4f}**, "
                 f"F-statistic = **{r0['F_stat']:.2f}** (p = **{fmt_p(r0['F_pvalue'])}**), Residual SE = **{r0['RSE']:.3f}** on **{r0['df_resid']}** df, "
                 f"AIC = **{r0['AIC']:.1f}**, BIC = **{r0['BIC']:.1f}**  (standard errors: HC3-robust)")
        L += ["", "| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\\|t\\|) | Signif |",
              "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |"]
        for r in rows:
            bold = r["p_value"] < 0.05
            b = (lambda s: f"**{s}**") if bold else (lambda s: s)
            coef = f"{r['Coefficient']:+.4f}"; tz = f"{r['t_or_z']:+.3f}"
            L.append(f"| {b(r['Term_Label'])} | {b(coef)} | {r['Std_Error']:.4f} | ±{r['Margin_2SE']:.4f} | {b(tz)} | {b(fmt_p(r['p_value']))} | {r['Significance']} |")
    else:
        L.append(f"**Model Diagnostics**: N = **{r0['N_obs']}**, events = **{r0['Events']}**, McFadden pseudo-R² = **{r0['McFadden_R2']:.4f}**, "
                 f"LLR χ² = **{r0['LLR_chi2']:.2f}** (p = **{fmt_p(r0['LLR_pvalue'])}**), AUC = **{r0['AUC']:.4f}**, AIC = **{r0['AIC']:.1f}**, BIC = **{r0['BIC']:.1f}**")
        L += ["", "| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\\|z\\|) | Odds Ratio | Signif |",
              "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"]
        for r in rows:
            bold = r["p_value"] < 0.05
            b = (lambda s: f"**{s}**") if bold else (lambda s: s)
            coef = f"{r['Coefficient']:+.4f}"; tz = f"{r['t_or_z']:+.3f}"
            L.append(f"| {b(r['Term_Label'])} | {b(coef)} | {r['Std_Error']:.4f} | ±{r['Margin_2SE']:.4f} | {b(tz)} | {b(fmt_p(r['p_value']))} | {np.exp(r['Coefficient']):.4f} | {r['Significance']} |")
    L += ["", "*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*", ""]
    return "\n".join(L)


def write_md(path, header_lines, blocks):
    with open(path, "w") as f:
        f.write("\n".join(header_lines) + "\n\n" + "\n".join(blocks))


# ======================================================================================
DOMAINS = ["Cognition", "Depression", "Home environment", "Wearable activity"]
INDEX = []   # (phase, cohort, population, domain, relative path)


def single_predictor_tables(base, phase_tag, out_dir, csv_name, cohort_key="all", cohort_label="All (analysis base)", md_prefix="phase6"):
    all_rows = []
    for gkey, (glabel, gsel) in P6.GROUPS.items():
        dg = gsel(base)
        blocks_by_domain = {d: [] for d in DOMAINS}
        for dom, y, kind, lab, ef, ec in OUTCOMES:
            blocks = blocks_by_domain[dom]
            covf = COV_FORMULA + ef
            d_out = dg.dropna(subset=[y] + BASE_COVS + ec).copy()
            if kind == "logit":
                d_out[y] = d_out[y].astype(int)
            if len(d_out) < 60 or (kind == "logit" and d_out[y].nunique() < 2):
                continue
            blocks.append(f"\n---\n\n### {lab}  (domain: {dom}; outcome sample N = {len(d_out):,}; {'OLS, HC3 SEs' if kind == 'ols' else 'logistic regression'})\n")
            # covariates-only reference first
            try:
                rb, ml = fit_full(f"{y} ~ {covf}", d_out, kind)
                meta = {"Phase": phase_tag, "Cohort": cohort_key, "Cohort_Label": cohort_label, "Group": gkey, "Group_Label": glabel, "Domain": dom,
                        "Outcome": y, "Outcome_Label": lab, "Model_Type": "OLS (HC3)" if kind == "ols" else "Logistic", "Model": "covariates only",
                        "Predictor": "(none)", "Formula": f"{y} ~ {covf}"}
                rows = model_rows(rb, ml, d_out, y, kind, meta); all_rows += rows
                blocks.append(md_model_block(rows, kind, "Reference: covariates only"))
            except Exception as e:
                blocks.append(f"#### Reference: covariates only\n_could not be fitted ({type(e).__name__})_\n")
            for pr, (plab, fam, band) in P6.PREDICTORS.items():
                if pr not in d_out.columns:
                    continue
                d = d_out.dropna(subset=[pr])
                if len(d) < 60 or (kind == "logit" and d[y].sum() < 15) or d[pr].std(ddof=1) == 0 or (band != "-" and (d[pr] > 0).sum() < 30):
                    continue
                f = f"{y} ~ {covf} + {pr}"
                try:
                    rb, ml = fit_full(f, d, kind)
                except Exception as e:
                    blocks.append(f"#### {plab}\n_could not be fitted ({type(e).__name__})_\n"); continue
                meta = {"Phase": phase_tag, "Cohort": cohort_key, "Cohort_Label": cohort_label, "Group": gkey, "Group_Label": glabel, "Domain": dom,
                        "Outcome": y, "Outcome_Label": lab, "Model_Type": "OLS (HC3)" if kind == "ols" else "Logistic", "Model": f"covariates + {pr}",
                        "Predictor": pr, "Formula": f}
                rows = model_rows(rb, ml, d, y, kind, meta); all_rows += rows
                blocks.append(md_model_block(rows, kind, f"Predictor entered alone: {plab}  (N = {len(d):,})"))
        sub_dir = os.path.join(out_dir, md_prefix if cohort_key == "all" else os.path.join(md_prefix, cohort_key), gkey)
        os.makedirs(sub_dir, exist_ok=True)
        for dom in DOMAINS:
            blocks = blocks_by_domain[dom]
            if not blocks:
                continue
            fname = dom.lower().replace(" ", "_") + ".md"
            write_md(os.path.join(sub_dir, fname),
                     [f"# {phase_tag} model output tables - {cohort_label} - {glabel} - {dom}", "",
                      "Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format "
                      "(HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. "
                      "[Index of all model-output files](../../README.md)" if cohort_key == "all" else
                      "Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format "
                      "(HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)"],
                     blocks)
            INDEX.append((phase_tag, cohort_label, glabel, dom, os.path.relpath(os.path.join(sub_dir, fname), out_dir)))
        print(f"  {phase_tag} {cohort_key} {gkey}: written")
    return all_rows


def main():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_phase6_dataset.csv"), low_memory=False)
    base = df[df["has_cgm"] == 1].dropna(subset=[HBA1C] + list(CORE_CGM) + BASE_COVS).copy()
    print(f"analysis base n = {len(base)}")
    which = sys.argv[1:] or ["6", "6b"]
    if "6" in which:
        rows = single_predictor_tables(base, "Phase 6", R6, "phase6_model_outputs.csv")
        pd.DataFrame(rows).to_csv(os.path.join(R6, "phase6_model_outputs.csv"), index=False)
    if "6b" in which:
        rows = []
        for ck, (clabel, csel) in P6B.COHORTS.items():
            d = csel(base)
            if len(d) < P6B.MIN_COHORT_N:
                print(f"  cohort {ck}: n = {len(d)} -> not possible"); continue
            rows += single_predictor_tables(d, "Phase 6b", R6, None, cohort_key=ck, cohort_label=clabel, md_prefix="phase6b")
        pd.DataFrame(rows).to_csv(os.path.join(R6, "phase6b_model_outputs.csv"), index=False)
    # index
    L = ["# Model output tables (Phases 6 and 6b)", "",
         "Every fitted model with all terms (intercept, covariates, glycaemic predictor) in the standard OLS-output format: formula; N, R², adj R², F-test, residual SE, AIC, BIC "
         "(logistic: N, events, McFadden R², LLR test, AUC); Coef, Std. Error, ±2 SE, t or z, p, significance codes (odds ratios for logistic models). "
         "Files are split by population and outcome domain so that each renders in GitHub / VS Code. Machine-readable: `phase6_model_outputs.csv`, `phase6b_model_outputs.csv`.", ""]
    cur = None
    for phase_tag, clabel, glabel, dom, rel in INDEX:
        head = f"## {phase_tag} - {clabel}"
        if head != cur:
            L += ["", head, ""]; cur = head
        L.append(f"- [{glabel} - {dom}]({rel})")
    with open(os.path.join(R6, "README.md"), "w") as f:
        f.write("\n".join(L))
    print("done")


if __name__ == "__main__":
    main()
