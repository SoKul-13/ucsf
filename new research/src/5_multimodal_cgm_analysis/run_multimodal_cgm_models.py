"""
Phase 5 - CGM-derived metrics vs HbA1c as predictors of comorbidity / lifestyle domains
=======================================================================================

For every outcome (cognition, depression, home environment, wearable activity) the
script fits, on ONE identical complete-case sample:

    M0  covariates only
    M1  covariates + HbA1c
    M2k covariates + one CGM feature (k = mean glucose, mean/SD, avg daily TIR, avg daily SD)
    M2  covariates + all four CGM features
    M3k covariates + HbA1c + one CGM feature
    M3  covariates + HbA1c + all four CGM features

Continuous outcomes: OLS with HC3 heteroskedasticity-robust t-tests.
Binary outcomes:     logistic regression with Wald z-tests.

Incremental value / redundancy is tested with nested likelihood-ratio (logistic) or
F-tests (OLS) plus HC3-robust Wald tests, and quantified out-of-sample with repeated
10-fold cross-validation (R^2 / AUC / Brier).  Benjamini-Hochberg FDR is applied within
the pre-registered primary family.  Secondary analyses: diabetes-stratified slopes with
interaction tests, quadratic non-linearity checks, >=7-valid-day sensitivity, insulin
exclusion, rank-based partial correlations, and an exploratory (FDR-controlled) sweep of
additional CGM metrics.
"""

import os
import json
import warnings
from itertools import product

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.model_selection import RepeatedKFold, RepeatedStratifiedKFold
from sklearn.metrics import roc_auc_score, brier_score_loss, r2_score
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor

warnings.filterwarnings("ignore")
np.random.seed(20260904)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports", "5_multimodal_cgm_analysis")
OUT_DATA = os.path.join(REPORT_DIR, "data")
OUT_FIG = os.path.join(REPORT_DIR, "figures")
for d in (OUT_DATA, OUT_FIG):
    os.makedirs(d, exist_ok=True)

# --------------------------------------------------------------------------------------
# Specification
# --------------------------------------------------------------------------------------
CORE_CGM = {
    "mean_glucose": "Mean glucose (mg/dL)",
    "mean_to_sd_ratio": "Mean / SD ratio",
    "avg_daily_tir": "Avg. daily TIR 70-180 (%)",
    "avg_daily_sd": "Avg. daily SD (mg/dL)",
}
HBA1C = "hba1c"
PRED_LABEL = {HBA1C: "HbA1c (%)", **CORE_CGM}

EXPLORATORY_CGM = {
    "gmi": "GMI (%)",
    "glucose_cv": "CV (%)",
    "tar_above_180": "Time > 180 (%)",
    "pct_severe_hyper": "Time > 250 (%)",
    "tbr_below_70": "Time < 70 (%)",
    "pct_severe_hypo": "Time < 54 (%)",
    "mag_mg_dl_per_h": "MAG (mg/dL/h)",
    "avg_daily_range": "Avg. daily range (mg/dL)",
    "sd_of_daily_means": "SD of daily means (mg/dL)",
    "nocturnal_mean": "Nocturnal mean 00-06h (mg/dL)",
    "avg_daily_mean_to_sd": "Avg. daily mean/SD",
}

BASE_COVS = ["age", "bmi", "education_level", "clinical_site",
             "hypertension", "high_cholesterol", "kidney_disease", "circulatory_problems"]
COV_FORMULA = ("age + bmi + C(education_level) + C(clinical_site) + hypertension + "
               "high_cholesterol + kidney_disease + circulatory_problems")
ENV_EXTRA = " + C(visit_season)"

# (domain, column, model type, label, extra covariate formula, extra covariate columns)
OUTCOMES = [
    ("Cognition", "moca_total", "ols", "MoCA total score (0-30)", "", []),
    ("Cognition", "cognitive_impairment", "logit", "Cognitive impairment (MoCA < 26)", "", []),
    ("Cognition", "moca_memory_index", "ols", "MoCA memory index score (0-15)", "", []),
    ("Depression", "cesd10_total", "ols", "CES-D-10 depressive symptoms (0-30)", "", []),
    ("Depression", "cesd10_ge10", "logit", "Clinically relevant depressive symptoms (CES-D-10 >= 10)", "", []),
    ("Home environment", "log_pm25_mean", "ols", "Indoor PM2.5, log(1 + mean ug/m3)", ENV_EXTRA, ["visit_season"]),
    ("Home environment", "env_temp_mean", "ols", "Indoor temperature, mean (deg C)", ENV_EXTRA, ["visit_season"]),
    ("Home environment", "env_hum_mean", "ols", "Indoor relative humidity, mean (%)", ENV_EXTRA, ["visit_season"]),
    ("Home environment", "env_voc_mean", "ols", "Indoor VOC index, mean", ENV_EXTRA, ["visit_season"]),
    ("Wearable activity", "steps_per_day", "ols", "Steps per wear-day", "", []),
    ("Wearable activity", "mvpa_min_per_day", "ols", "Brisk-cadence minutes per day (>= 100 steps/min)", "", []),
    ("Wearable activity", "hr_resting_proxy", "ols", "Resting heart-rate proxy (daily 5th pct, bpm)", "", []),
    ("Wearable activity", "sleep_tst_min", "ols", "Total sleep time per night (min)", "", []),
    ("Wearable activity", "stress_mean", "ols", "Garmin stress score, mean (0-100)", "", []),
]

EXPLORATORY_OUTCOMES = [
    ("Cognition", "moca_delayed_recall", "ols", "MoCA delayed recall (0-5)", "", []),
    ("Depression", "paid5_total", "ols", "PAID-5 diabetes distress (0-20)", "", []),
    ("Home environment", "env_nox_mean", "ols", "Indoor NOx index, mean", ENV_EXTRA, ["visit_season"]),
    ("Home environment", "env_pm25_pct_gt15", "ols", "% time indoor PM2.5 > 15 ug/m3", ENV_EXTRA, ["visit_season"]),
    ("Wearable activity", "sedentary_pct", "ols", "Sedentary time (% of labelled minutes)", "", []),
    ("Wearable activity", "sleep_efficiency_pct", "ols", "Sleep efficiency (%)", "", []),
    ("Wearable activity", "spo2_mean", "ols", "Nocturnal SpO2, mean (%)", "", []),
    ("Wearable activity", "hr_mean", "ols", "Mean heart rate (bpm)", "", []),
    ("Wearable activity", "stress_pct_high", "ols", "% time high stress (> 50)", "", []),
]

CV_SPLITS, CV_REPEATS = 10, 5
BOOT_N = 400

# --------------------------------------------------------------------------------------
# utilities
# --------------------------------------------------------------------------------------
def fit(formula, df, kind):
    if kind == "ols":
        return smf.ols(formula, data=df).fit(cov_type="HC3")
    return smf.logit(formula, data=df).fit(disp=0, maxiter=200)


def fit_ml(formula, df, kind):
    """non-robust fit (needed for nested F / LR tests)"""
    if kind == "ols":
        return smf.ols(formula, data=df).fit()
    return smf.logit(formula, data=df).fit(disp=0, maxiter=200)


def nested_test(full, reduced, kind):
    """returns (statistic, df, p, label)"""
    if kind == "ols":
        f, p, df = full.compare_f_test(reduced)
        return float(f), int(df), float(p), "F"
    lr = 2 * (full.llf - reduced.llf)
    df = int(full.df_model - reduced.df_model)
    return float(lr), df, float(stats.chi2.sf(lr, df)), "LR chi2"


def robust_block_wald(model, terms):
    """HC3 (OLS) or observed-information (logit) Wald test that all `terms` are zero."""
    names = list(model.params.index)
    R = np.zeros((len(terms), len(names)))
    for i, t in enumerate(terms):
        R[i, names.index(t)] = 1.0
    w = model.wald_test(R, scalar=True, use_f=False)
    return float(np.squeeze(w.statistic)), int(len(terms)), float(np.squeeze(w.pvalue))


def slope_row(model, term, sd_x, kind):
    b = float(model.params[term]); se = float(model.bse[term])
    ci = model.conf_int().loc[term]
    row = {"beta_raw": b, "se_raw": se, "stat": float(model.tvalues[term]),
           "p": float(model.pvalues[term]), "ci_low_raw": float(ci[0]), "ci_high_raw": float(ci[1]),
           "beta_per_sd": b * sd_x, "ci_low_per_sd": float(ci[0]) * sd_x, "ci_high_per_sd": float(ci[1]) * sd_x}
    if kind == "logit":
        row.update({"or_per_sd": float(np.exp(b * sd_x)), "or_ci_low": float(np.exp(ci[0] * sd_x)),
                    "or_ci_high": float(np.exp(ci[1] * sd_x)), "or_raw": float(np.exp(b))})
    return row


def mcfadden(model, null_llf):
    return 1 - model.llf / null_llf


def nagelkerke(model, null_llf, n):
    cs = 1 - np.exp(2 * (null_llf - model.llf) / n)
    return cs / (1 - np.exp(2 * null_llf / n))


def delong_test(y, p1, p2):
    """DeLong paired test for two correlated AUCs (Sun & Xu 2014 fast implementation)."""
    y = np.asarray(y).astype(int)
    pos, neg = np.where(y == 1)[0], np.where(y == 0)[0]
    m, n = len(pos), len(neg)

    def structural(pred):
        x, yv = pred[pos], pred[neg]
        tx = stats.rankdata(np.concatenate([x, yv]))
        tx_x, tx_y = stats.rankdata(x), stats.rankdata(yv)
        auc = (tx[:m].sum() - m * (m + 1) / 2) / (m * n)
        v10 = (tx[:m] - tx_x) / n
        v01 = 1 - (tx[m:] - tx_y) / m
        return auc, v10, v01

    a1, v10_1, v01_1 = structural(np.asarray(p1))
    a2, v10_2, v01_2 = structural(np.asarray(p2))
    s10 = np.cov(np.vstack([v10_1, v10_2]))
    s01 = np.cov(np.vstack([v01_1, v01_2]))
    S = s10 / m + s01 / n
    var = S[0, 0] + S[1, 1] - 2 * S[0, 1]
    z = (a1 - a2) / np.sqrt(var) if var > 0 else np.nan
    p = 2 * stats.norm.sf(abs(z)) if np.isfinite(z) else np.nan
    return float(a1), float(a2), float(z), float(p)


def cross_validate(formula, df, y, kind):
    """repeated k-fold; returns mean out-of-sample R2 (OLS) or AUC + Brier (logit)."""
    if kind == "ols":
        splitter = RepeatedKFold(n_splits=CV_SPLITS, n_repeats=CV_REPEATS, random_state=7)
        idx_iter = splitter.split(df)
    else:
        splitter = RepeatedStratifiedKFold(n_splits=CV_SPLITS, n_repeats=CV_REPEATS, random_state=7)
        idx_iter = splitter.split(df, df[y])
    r2s, aucs, briers = [], [], []
    for tr, te in idx_iter:
        dtr, dte = df.iloc[tr], df.iloc[te]
        try:
            m = fit_ml(formula, dtr, kind)
            pred = np.asarray(m.predict(dte))
        except Exception:
            continue
        if kind == "ols":
            r2s.append(r2_score(dte[y], pred))
        else:
            if dte[y].nunique() == 2:
                aucs.append(roc_auc_score(dte[y], pred))
            briers.append(brier_score_loss(dte[y], pred))
    if kind == "ols":
        return {"cv_r2_mean": float(np.mean(r2s)), "cv_r2_sd": float(np.std(r2s))}
    return {"cv_auc_mean": float(np.mean(aucs)), "cv_auc_sd": float(np.std(aucs)),
            "cv_brier_mean": float(np.mean(briers))}


def vif_table(df, cols):
    X = sm.add_constant(df[cols].astype(float))
    return {c: float(variance_inflation_factor(X.values, i + 1)) for i, c in enumerate(cols)}


def q_label(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""


# --------------------------------------------------------------------------------------
# core routine for one outcome
# --------------------------------------------------------------------------------------
def analyse_outcome(df, domain, y, kind, label, extra_f, extra_cols, sample_tag="primary",
                    cgm_feats=None, do_cv=True, do_boot=True):
    cgm_feats = cgm_feats or list(CORE_CGM)
    covf = COV_FORMULA + extra_f
    need = [y, HBA1C] + cgm_feats + BASE_COVS + extra_cols
    d = df.dropna(subset=need).copy()
    if kind == "logit":
        d[y] = d[y].astype(int)
        if d[y].nunique() < 2 or d[y].sum() < 20:
            return None
    if len(d) < 100:
        return None

    sds = {p: float(d[p].std(ddof=1)) for p in [HBA1C] + cgm_feats}
    specs = {
        "M0": f"{y} ~ {covf}",
        "M1": f"{y} ~ {covf} + {HBA1C}",
        "M2": f"{y} ~ {covf} + " + " + ".join(cgm_feats),
        "M3": f"{y} ~ {covf} + {HBA1C} + " + " + ".join(cgm_feats),
    }
    for k in cgm_feats:
        specs[f"M2_{k}"] = f"{y} ~ {covf} + {k}"
        specs[f"M3_{k}"] = f"{y} ~ {covf} + {HBA1C} + {k}"

    robust, ml = {}, {}
    for name, f in specs.items():
        robust[name] = fit(f, d, kind)
        ml[name] = fit_ml(f, d, kind)

    null_llf = ml["M0"].llf
    n = len(d)
    out = {"domain": domain, "outcome": y, "label": label, "kind": kind, "n": n,
           "sample": sample_tag, "events": int(d[y].sum()) if kind == "logit" else np.nan}

    # ---- fit statistics per spec ----
    fit_rows = []
    for name, m in ml.items():
        row = {"domain": domain, "outcome": y, "label": label, "kind": kind, "sample": sample_tag,
               "spec": name, "n": n, "k_params": int(m.df_model + 1), "llf": float(m.llf),
               "aic": float(m.aic), "bic": float(m.bic)}
        if kind == "ols":
            row.update({"r2": float(m.rsquared), "adj_r2": float(m.rsquared_adj),
                        "delta_r2_vs_M0": float(m.rsquared - ml["M0"].rsquared)})
        else:
            pred = np.asarray(m.predict(d))
            row.update({"mcfadden_r2": float(mcfadden(m, null_llf)),
                        "nagelkerke_r2": float(nagelkerke(m, null_llf, n)),
                        "auc_in_sample": float(roc_auc_score(d[y], pred)),
                        "brier_in_sample": float(brier_score_loss(d[y], pred))})
        if do_cv and name in ("M0", "M1", "M2", "M3") or (do_cv and name.startswith("M2_")):
            row.update(cross_validate(specs[name], d, y, kind))
        fit_rows.append(row)

    # ---- slope tests ----
    slope_rows = []
    for name, m in robust.items():
        for term in [HBA1C] + cgm_feats:
            if term in m.params.index:
                r = slope_row(m, term, sds[term], kind)
                r.update({"domain": domain, "outcome": y, "label": label, "kind": kind, "sample": sample_tag,
                          "spec": name, "predictor": term, "predictor_label": PRED_LABEL.get(term, term),
                          "sd_x": sds[term], "n": n, "test": "HC3 t" if kind == "ols" else "Wald z"})
                slope_rows.append(r)

    # ---- nested tests ----
    nested_rows = []
    def add_nested(full, red, question):
        s, dfree, p, lab = nested_test(ml[full], ml[red], kind)
        terms = [t for t in ml[full].params.index if t not in ml[red].params.index]
        ws, wdf, wp = robust_block_wald(robust[full], terms)
        nested_rows.append({"domain": domain, "outcome": y, "label": label, "kind": kind, "sample": sample_tag,
                            "full": full, "reduced": red, "question": question, "stat": s, "df": dfree, "p": p,
                            "test": lab, "robust_wald": ws, "robust_wald_p": wp,
                            "delta_aic": float(ml[full].aic - ml[red].aic),
                            "delta_bic": float(ml[full].bic - ml[red].bic)})
    add_nested("M1", "M0", "Does HbA1c add to covariates?")
    add_nested("M2", "M0", "Do the 4 CGM features add to covariates?")
    add_nested("M3", "M1", "Do CGM features add beyond HbA1c?")
    add_nested("M3", "M2", "Does HbA1c add beyond CGM features?")
    for k in cgm_feats:
        add_nested(f"M2_{k}", "M0", f"Does {k} alone add to covariates?")
        add_nested(f"M3_{k}", "M1", f"Does {k} add beyond HbA1c?")
        add_nested(f"M3_{k}", f"M2_{k}", f"Does HbA1c add beyond {k}?")

    # ---- head-to-head: HbA1c-only vs CGM-only (non-nested) ----
    h2h = {"domain": domain, "outcome": y, "label": label, "kind": kind, "sample": sample_tag, "n": n,
           "aic_M1": float(ml["M1"].aic), "aic_M2": float(ml["M2"].aic), "aic_M3": float(ml["M3"].aic),
           "bic_M1": float(ml["M1"].bic), "bic_M2": float(ml["M2"].bic), "bic_M3": float(ml["M3"].bic)}
    best_single = min(cgm_feats, key=lambda k: ml[f"M2_{k}"].aic)
    h2h["best_single_cgm"] = best_single
    h2h["aic_best_single_cgm"] = float(ml[f"M2_{best_single}"].aic)
    h2h["aic_diff_bestCGM_minus_HbA1c"] = float(ml[f"M2_{best_single}"].aic - ml["M1"].aic)
    if kind == "ols":
        h2h["adj_r2_M1"], h2h["adj_r2_M2"], h2h["adj_r2_M3"] = (float(ml[s].rsquared_adj) for s in ("M1", "M2", "M3"))
        h2h["adj_r2_best_single_cgm"] = float(ml[f"M2_{best_single}"].rsquared_adj)
        if do_boot:
            # bootstrap CI for adj-R2(M2) - adj-R2(M1) and adj-R2(best single CGM) - adj-R2(M1)
            diffs, diffs_b = [], []
            rng = np.random.default_rng(11)
            for _ in range(BOOT_N):
                b = d.sample(n=n, replace=True, random_state=int(rng.integers(1e9)))
                try:
                    a1 = smf.ols(specs["M1"], b).fit().rsquared_adj
                    a2 = smf.ols(specs["M2"], b).fit().rsquared_adj
                    ab = smf.ols(specs[f"M2_{best_single}"], b).fit().rsquared_adj
                    diffs.append(a2 - a1); diffs_b.append(ab - a1)
                except Exception:
                    pass
            h2h["boot_dAdjR2_M2_minus_M1_ci_low"], h2h["boot_dAdjR2_M2_minus_M1_ci_high"] = np.percentile(diffs, [2.5, 97.5])
            h2h["boot_dAdjR2_best_minus_M1_ci_low"], h2h["boot_dAdjR2_best_minus_M1_ci_high"] = np.percentile(diffs_b, [2.5, 97.5])
    else:
        p1, p2, p3 = (np.asarray(ml[s].predict(d)) for s in ("M1", "M2", "M3"))
        pb = np.asarray(ml[f"M2_{best_single}"].predict(d))
        a1, a2, z, p = delong_test(d[y], p1, p2)
        h2h.update({"auc_M1": a1, "auc_M2": a2, "delong_z_M2_vs_M1": z, "delong_p_M2_vs_M1": p})
        a1, a3, z, p = delong_test(d[y], p1, p3)
        h2h.update({"auc_M3": a3, "delong_z_M3_vs_M1": z, "delong_p_M3_vs_M1": p})
        a1, ab, z, p = delong_test(d[y], p1, pb)
        h2h.update({"auc_best_single_cgm": ab, "delong_z_best_vs_M1": z, "delong_p_best_vs_M1": p})

    # ---- collinearity in M3 ----
    vifs = vif_table(d, [HBA1C] + cgm_feats)
    vif_rows = [{"domain": domain, "outcome": y, "sample": sample_tag, "predictor": k, "vif": v} for k, v in vifs.items()]

    # ---- rank-based partial correlations (robustness to distributional form) ----
    partial_rows = []
    if kind == "ols":
        res_y = smf.ols(specs["M0"], d).fit().resid
        for term in [HBA1C] + cgm_feats:
            res_x = smf.ols(f"{term} ~ {covf}", d).fit().resid
            rho, p = stats.spearmanr(res_y, res_x)
            partial_rows.append({"domain": domain, "outcome": y, "label": label, "sample": sample_tag,
                                 "predictor": term, "partial_spearman_rho": float(rho), "p": float(p), "n": n})

    # ---- non-linearity: quadratic term for each predictor (single-feature models) ----
    nonlin_rows = []
    for term in [HBA1C] + cgm_feats:
        d["_z"] = (d[term] - d[term].mean()) / d[term].std(ddof=1)
        try:
            mq = fit(f"{y} ~ {covf} + _z + I(_z**2)", d, kind)
            nonlin_rows.append({"domain": domain, "outcome": y, "label": label, "sample": sample_tag,
                                "predictor": term, "beta_linear_z": float(mq.params["_z"]),
                                "beta_quadratic_z": float(mq.params["I(_z ** 2)"]),
                                "p_quadratic": float(mq.pvalues["I(_z ** 2)"]), "n": n})
        except Exception:
            pass
    d.drop(columns="_z", inplace=True)

    # ---- diabetes-stratified slopes + interaction (single-feature models) ----
    strat_rows = []
    for term in [HBA1C] + cgm_feats:
        d["_z"] = (d[term] - d[term].mean()) / d[term].std(ddof=1)
        try:
            mi = fit(f"{y} ~ {covf} + _z * any_diabetes", d, kind)
            p_int = float(mi.pvalues["_z:any_diabetes"])
        except Exception:
            p_int = np.nan
        for grp, gname in ((0, "No diabetes / pre-diabetes"), (1, "Type 2 diabetes")):
            sub = d[d["any_diabetes"] == grp]
            if len(sub) < 80 or (kind == "logit" and sub[y].sum() < 15):
                continue
            try:
                ms = fit(f"{y} ~ {covf} + _z", sub, kind)
                ci = ms.conf_int().loc["_z"]
                strat_rows.append({"domain": domain, "outcome": y, "label": label, "sample": sample_tag,
                                   "predictor": term, "stratum": gname, "n": len(sub),
                                   "beta_per_pooled_sd": float(ms.params["_z"]), "ci_low": float(ci[0]),
                                   "ci_high": float(ci[1]), "p": float(ms.pvalues["_z"]), "p_interaction": p_int})
            except Exception:
                pass
    d.drop(columns="_z", inplace=True)

    return {"summary": out, "fit": fit_rows, "slopes": slope_rows, "nested": nested_rows, "h2h": h2h,
            "vif": vif_rows, "partial": partial_rows, "nonlin": nonlin_rows, "strat": strat_rows}


def run_exploratory_sweep(base):
    """single-metric models for the extended CGM metric set; BH-FDR within the sweep"""
    expl_rows, errors = [], []
    for dom, y, kind, lab, ef, ec in OUTCOMES:
        covf = COV_FORMULA + ef
        for k, klab in EXPLORATORY_CGM.items():
            need = [y, k] + BASE_COVS + ec
            d = base.dropna(subset=need).copy()
            if kind == "logit":
                d[y] = d[y].astype(int)
                if d[y].sum() < 20:
                    continue
            if len(d) < 100 or d[k].std() == 0:
                continue
            try:
                m = fit(f"{y} ~ {covf} + {k}", d, kind)
                r = slope_row(m, k, float(d[k].std(ddof=1)), kind)
                r.update({"domain": dom, "outcome": y, "label": lab, "kind": kind, "predictor": k,
                          "predictor_label": klab, "n": len(d)})
                expl_rows.append(r)
            except Exception as e:
                errors.append(f"{y} ~ {k}: {e!r}")
    expl = pd.DataFrame(expl_rows)
    if errors:
        print(f"  exploratory sweep: {len(errors)} model failures, e.g. {errors[0]}")
    if len(expl):
        expl["q_bh"] = multipletests(expl["p"], method="fdr_bh")[1]
        expl.to_csv(os.path.join(OUT_DATA, "exploratory_cgm_metric_sweep_with_fdr.csv"), index=False)
        print(f"  exploratory sweep: {len(expl)} tests, {(expl['q_bh'] < 0.05).sum()} significant at FDR 0.05")
    return expl


# --------------------------------------------------------------------------------------
# descriptives
# --------------------------------------------------------------------------------------
def table_one(df):
    groups = ["No diabetes", "Pre-diabetes / lifestyle", "T2D non-insulin", "T2D insulin"]
    cont = [("age", "Age (years)"), ("bmi", "BMI (kg/m2)"), ("years_of_education", "Education (years)"),
            ("hba1c", "HbA1c (%)"), ("mean_glucose", "Mean glucose (mg/dL)"), ("glucose_sd", "Glucose SD (mg/dL)"),
            ("mean_to_sd_ratio", "Mean/SD ratio"), ("avg_daily_tir", "Avg daily TIR 70-180 (%)"),
            ("avg_daily_sd", "Avg daily SD (mg/dL)"), ("tar_above_180", "Time > 180 (%)"),
            ("tbr_below_70", "Time < 70 (%)"), ("cgm_valid_days", "Valid CGM days"),
            ("moca_total", "MoCA total"), ("cesd10_total", "CES-D-10"), ("paid5_total", "PAID-5"),
            ("env_pm25_mean", "Indoor PM2.5 mean (ug/m3)"), ("env_temp_mean", "Indoor temp (C)"),
            ("env_hum_mean", "Indoor RH (%)"), ("env_voc_mean", "Indoor VOC index"),
            ("steps_per_day", "Steps / day"), ("mvpa_min_per_day", "Brisk minutes / day"),
            ("hr_resting_proxy", "Resting HR proxy (bpm)"), ("sleep_tst_min", "Sleep / night (min)"),
            ("stress_mean", "Garmin stress")]
    binary = [("cognitive_impairment", "MoCA < 26"), ("cesd10_ge10", "CES-D-10 >= 10"),
              ("hypertension", "Hypertension"), ("high_cholesterol", "High cholesterol"),
              ("kidney_disease", "Kidney disease"), ("circulatory_problems", "Circulatory disease"),
              ("insulin_use", "Insulin use")]
    rows = []
    for col, lab in cont:
        if col not in df:
            continue
        r = {"variable": lab, "type": "mean (SD) [n]"}
        for g in groups:
            s = df.loc[df["diabetes_status"] == g, col].dropna()
            r[g] = f"{s.mean():.2f} ({s.std():.2f}) [{len(s)}]" if len(s) else "-"
        s = df[col].dropna(); r["All"] = f"{s.mean():.2f} ({s.std():.2f}) [{len(s)}]"
        # Kruskal-Wallis across groups
        arrs = [df.loc[df["diabetes_status"] == g, col].dropna() for g in groups]
        arrs = [a for a in arrs if len(a) > 1]
        r["p_across_groups"] = f"{stats.kruskal(*arrs).pvalue:.2e}" if len(arrs) > 1 else ""
        rows.append(r)
    for col, lab in binary:
        if col not in df:
            continue
        r = {"variable": lab, "type": "n (%)"}
        for g in groups:
            s = df.loc[df["diabetes_status"] == g, col].dropna()
            r[g] = f"{int(s.sum())} ({s.mean()*100:.1f}%)" if len(s) else "-"
        s = df[col].dropna(); r["All"] = f"{int(s.sum())} ({s.mean()*100:.1f}%)"
        ct = pd.crosstab(df["diabetes_status"], df[col])
        r["p_across_groups"] = f"{stats.chi2_contingency(ct)[1]:.2e}" if ct.shape == (4, 2) else ""
        rows.append(r)
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------------
# figures
# --------------------------------------------------------------------------------------
BLUE, ORANGE, AQUA, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#8a8987"


def make_figures(slopes, nested, h2h, fit, strat, corr, coverage):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": "#b5b4b0", "axes.labelcolor": "#0b0b0b", "xtick.color": "#52514e",
                         "ytick.color": "#52514e", "figure.facecolor": "white"})

    # ---- Fig 1: forest plot of standardized effects, single-predictor models ----
    prim = slopes[(slopes["sample"] == "primary") &
                  (slopes["spec"].isin(["M1"] + [f"M2_{k}" for k in CORE_CGM]))].copy()
    prim = prim[prim.apply(lambda r: r["spec"] == "M1" and r["predictor"] == HBA1C or r["spec"] == f"M2_{r['predictor']}", axis=1)]
    outs = [o for o in [c for _, c, *_ in OUTCOMES] if o in prim["outcome"].unique()]
    n_out = len(outs)
    fig, axes = plt.subplots(nrows=(n_out + 2) // 3, ncols=3, figsize=(13, 3.0 * ((n_out + 2) // 3)))
    axes = axes.ravel()
    preds = [HBA1C] + list(CORE_CGM)
    for ax, o in zip(axes, outs):
        sub = prim[prim["outcome"] == o].set_index("predictor").reindex(preds)
        kind = sub["kind"].iloc[0]
        ys = np.arange(len(preds))[::-1]
        for yy, pr in zip(ys, preds):
            r = sub.loc[pr]
            if kind == "logit":
                est, lo, hi = np.log(r["or_per_sd"]), np.log(r["or_ci_low"]), np.log(r["or_ci_high"])
            else:
                sd_y = 1.0
                est, lo, hi = r["beta_per_sd"], r["ci_low_per_sd"], r["ci_high_per_sd"]
            col = BLUE if pr == HBA1C else ORANGE
            ax.plot([lo, hi], [yy, yy], color=col, lw=2, solid_capstyle="round")
            ax.plot(est, yy, "o", color=col, ms=6, mec="white", mew=1)
            ax.text(ax.get_xlim()[1] if False else hi, yy, f"  p={r['p']:.3g}{q_label(r['p'])}", va="center", fontsize=7, color="#52514e")
        ax.axvline(0, color="#b5b4b0", lw=1, ls="--")
        ax.set_yticks(ys); ax.set_yticklabels([PRED_LABEL[p] for p in preds], fontsize=8)
        ax.set_title(sub["label"].iloc[0] + f"\n(n = {int(sub['n'].iloc[0]):,})", fontsize=8.5, loc="left")
        ax.set_xlabel("log-OR per 1 SD" if kind == "logit" else "change in outcome per 1 SD of predictor", fontsize=8)
        xl = ax.get_xlim(); ax.set_xlim(xl[0], xl[1] + (xl[1] - xl[0]) * 0.45)
    for ax in axes[n_out:]:
        ax.axis("off")
    fig.suptitle("Fig. 1  Covariate-adjusted association of HbA1c (blue) and each core CGM metric (orange) with every primary outcome\n"
                 "Single-predictor models; HC3-robust 95% CI (OLS) or Wald 95% CI (logistic). Unadjusted p-values shown.", fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(os.path.join(OUT_FIG, "fig1_forest_single_predictor_effects.png"), dpi=180)
    plt.close(fig)

    # ---- Fig 2: incremental-value heatmap (-log10 p of nested tests) ----
    nn = nested[(nested["sample"] == "primary") & (nested["full"].isin(["M1", "M2", "M3"]))].copy()
    piv = nn.pivot_table(index="label", columns="question", values="p")
    order = ["Does HbA1c add to covariates?", "Do the 4 CGM features add to covariates?",
             "Do CGM features add beyond HbA1c?", "Does HbA1c add beyond CGM features?"]
    piv = piv.reindex(columns=order)
    labs = [l for _, _, _, l, _, _ in OUTCOMES if l in piv.index]
    piv = piv.reindex(labs)
    fig, ax = plt.subplots(figsize=(10, 0.42 * len(piv) + 2.2))
    mat = -np.log10(piv.values.astype(float))
    im = ax.imshow(mat, cmap="Blues", vmin=0, vmax=6, aspect="auto")
    ax.set_xticks(range(len(order))); ax.set_xticklabels(["HbA1c | covs", "CGM(4) | covs", "CGM(4) | HbA1c", "HbA1c | CGM(4)"], fontsize=8.5)
    ax.set_yticks(range(len(piv))); ax.set_yticklabels(piv.index, fontsize=8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            p = piv.values[i, j]
            ax.text(j, i, f"{p:.2g}", ha="center", va="center", fontsize=7.5,
                    color="white" if mat[i, j] > 3.2 else "#0b0b0b")
    cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02); cb.set_label("-log10 p (nested F / LR test)", fontsize=8)
    ax.set_title("Fig. 2  Nested-model tests: does each predictor block add information\nbeyond the other? (cell text = p-value; 'A | B' = A added to a model already containing B)", fontsize=9, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig2_nested_test_heatmap.png"), dpi=180); plt.close(fig)

    # ---- Fig 3: out-of-sample performance M0 / M1 / M2 / M3 ----
    ff = fit[(fit["sample"] == "primary") & (fit["spec"].isin(["M0", "M1", "M2", "M3"]))].copy()
    ff["metric"] = np.where(ff["kind"] == "ols", ff.get("cv_r2_mean"), ff.get("cv_auc_mean"))
    piv = ff.pivot_table(index="label", columns="spec", values="metric").reindex(labs)
    fig, ax = plt.subplots(figsize=(10, 0.45 * len(piv) + 1.5))
    yy = np.arange(len(piv))[::-1]
    cols = {"M0": GREY, "M1": BLUE, "M2": ORANGE, "M3": AQUA}
    h = 0.2
    for i, s in enumerate(["M0", "M1", "M2", "M3"]):
        ax.barh(yy + (1.5 - i) * h, piv[s], height=h * 0.9, color=cols[s], label={"M0": "Covariates only", "M1": "+ HbA1c", "M2": "+ 4 CGM metrics", "M3": "+ HbA1c + 4 CGM"}[s])
    ax.set_yticks(yy); ax.set_yticklabels(piv.index, fontsize=8)
    ax.set_xlabel("Repeated 10-fold CV: out-of-sample R^2 (continuous) or AUC (binary)", fontsize=8.5)
    ax.legend(fontsize=8, frameon=False, loc="lower right")
    ax.set_title("Fig. 3  Out-of-sample predictive performance by specification (5 x 10-fold cross-validation)", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig3_cv_performance.png"), dpi=180); plt.close(fig)

    # ---- Fig 4: predictor correlation heatmap ----
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr))); ax.set_xticklabels([PRED_LABEL.get(c, c) for c in corr.columns], rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(corr))); ax.set_yticklabels([PRED_LABEL.get(c, c) for c in corr.index], fontsize=8)
    for i in range(len(corr)):
        for j in range(len(corr)):
            ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=8,
                    color="white" if abs(corr.values[i, j]) > 0.6 else "#0b0b0b")
    fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02).set_label("Spearman rho", fontsize=8)
    ax.set_title("Fig. 4  Rank correlations among HbA1c and CGM metrics (analysis sample)", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig4_predictor_correlations.png"), dpi=180); plt.close(fig)

    # ---- Fig 5: diabetes-stratified slopes ----
    st = strat[strat["sample"] == "primary"].copy()
    if len(st):
        outs_s = [o for o in outs if o in st["outcome"].unique()]
        fig, axes = plt.subplots(nrows=(len(outs_s) + 2) // 3, ncols=3, figsize=(13, 3.0 * ((len(outs_s) + 2) // 3)))
        axes = axes.ravel()
        for ax, o in zip(axes, outs_s):
            sub = st[st["outcome"] == o]
            ys = np.arange(len(preds))[::-1]
            for yy, pr in zip(ys, preds):
                for off, (gname, col, mk) in zip((0.18, -0.18), (("No diabetes / pre-diabetes", AQUA, "s"), ("Type 2 diabetes", ORANGE, "o"))):
                    r = sub[(sub["predictor"] == pr) & (sub["stratum"] == gname)]
                    if len(r) == 0:
                        continue
                    r = r.iloc[0]
                    ax.plot([r["ci_low"], r["ci_high"]], [yy + off, yy + off], color=col, lw=1.8)
                    ax.plot(r["beta_per_pooled_sd"], yy + off, mk, color=col, ms=5, mec="white", mew=0.8)
                pint = sub[sub["predictor"] == pr]["p_interaction"].dropna()
                if len(pint):
                    ax.text(ax.get_xlim()[1], yy, f" p_int={pint.iloc[0]:.2g}", fontsize=7, va="center", color="#52514e")
            ax.axvline(0, color="#b5b4b0", lw=1, ls="--")
            ax.set_yticks(ys); ax.set_yticklabels([PRED_LABEL[p] for p in preds], fontsize=8)
            ax.set_title(sub["label"].iloc[0], fontsize=8.5, loc="left")
            xl = ax.get_xlim(); ax.set_xlim(xl[0], xl[1] + (xl[1] - xl[0]) * 0.4)
        for ax in axes[len(outs_s):]:
            ax.axis("off")
        from matplotlib.lines import Line2D
        handles = [Line2D([], [], marker="s", color=AQUA, ls="", label="No diabetes / pre-diabetes (n varies by outcome)"),
                   Line2D([], [], marker="o", color=ORANGE, ls="", label="Type 2 diabetes")]
        fig.legend(handles=handles, fontsize=8.5, frameon=False, loc="upper right", bbox_to_anchor=(0.99, 0.995))
        fig.suptitle("Fig. 5  Diabetes-stratified single-predictor slopes (per pooled SD) with interaction p-values", fontsize=9.5, x=0.01, ha="left")
        fig.tight_layout(rect=[0, 0, 1, 0.96]); fig.savefig(os.path.join(OUT_FIG, "fig5_diabetes_stratified.png"), dpi=180); plt.close(fig)

    # ---- Fig 6: sample flow / coverage ----
    fig, ax = plt.subplots(figsize=(8, 3.6))
    labels_c = list(coverage.keys()); vals = list(coverage.values())
    ax.barh(range(len(vals))[::-1], vals, color=BLUE, height=0.6)
    for i, v in zip(range(len(vals))[::-1], vals):
        ax.text(v + 15, i, f"{v:,}", va="center", fontsize=8.5)
    ax.set_yticks(range(len(vals))[::-1]); ax.set_yticklabels(labels_c, fontsize=8.5)
    ax.set_xlim(0, max(vals) * 1.15); ax.set_xlabel("Participants", fontsize=8.5)
    ax.set_title("Fig. 6  Data availability and analysis-sample construction", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig6_sample_flow.png"), dpi=180); plt.close(fig)


# --------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------
def collect(results, key):
    rows = []
    for r in results:
        if r is None:
            continue
        v = r[key]
        rows.extend(v if isinstance(v, list) else [v])
    return pd.DataFrame(rows)


def main():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_multimodal_dataset.csv"), low_memory=False)
    print(f"Loaded {len(df)} participants")

    # analysis base: >= 3 valid CGM days, HbA1c, and full covariates
    base = df[(df["has_cgm"] == 1)].dropna(subset=[HBA1C] + list(CORE_CGM) + BASE_COVS).copy()
    coverage = {
        "AI-READI participants": int(len(df)),
        "CGM >= 3 valid days (>= 70% of 288 readings/day)": int(df["has_cgm"].sum()),
        "+ HbA1c and complete covariates (analysis base)": int(len(base)),
        "  with MoCA": int(base["moca_total"].notna().sum()),
        "  with CES-D-10": int(base["cesd10_total"].notna().sum()),
        "  with home sensor >= 3 days": int(base["has_env"].sum()),
        "  with wearable >= 3 wear-days": int(base["has_wearable"].sum()),
    }
    print(json.dumps(coverage, indent=1))
    base.to_csv(os.path.join(OUT_DATA, "analysis_base_sample.csv"), index=False)

    # descriptives
    t1 = table_one(base)
    t1.to_csv(os.path.join(OUT_DATA, "table1_descriptives_by_diabetes_status.csv"), index=False)
    corr = base[[HBA1C] + list(CORE_CGM)].corr(method="spearman")
    corr.to_csv(os.path.join(OUT_DATA, "predictor_spearman_correlations.csv"))

    # ------------------ primary analyses ------------------
    results = []
    for dom, y, kind, lab, ef, ec in OUTCOMES:
        print(f"  primary: {lab}")
        results.append(analyse_outcome(base, dom, y, kind, lab, ef, ec, "primary"))

    # ------------------ sensitivity samples ------------------
    sens_samples = {
        "cgm_ge7_days": base[base["cgm_valid_days"] >= 7],
        "no_insulin": base[base["insulin_use"] != 1],
        "diabetes_only": base[base["any_diabetes"] == 1],
        "no_diabetes_only": base[base["any_diabetes"] == 0],
    }
    for tag, sdf in sens_samples.items():
        for dom, y, kind, lab, ef, ec in OUTCOMES:
            print(f"  sensitivity [{tag}]: {lab}")
            results.append(analyse_outcome(sdf, dom, y, kind, lab, ef, ec, tag, do_cv=False, do_boot=False))

    # ------------------ exploratory outcomes (core features) ------------------
    for dom, y, kind, lab, ef, ec in EXPLORATORY_OUTCOMES:
        if y in base.columns:
            print(f"  exploratory outcome: {lab}")
            results.append(analyse_outcome(base, dom, y, kind, lab, ef, ec, "exploratory_outcome", do_cv=False, do_boot=False))

    summary = collect(results, "summary")
    fit = collect(results, "fit")
    slopes = collect(results, "slopes")
    nested = collect(results, "nested")
    h2h = collect(results, "h2h")
    vif = collect(results, "vif")
    partial = collect(results, "partial")
    nonlin = collect(results, "nonlin")
    strat = collect(results, "strat")

    # ------------------ multiplicity control (primary family) ------------------
    fam = slopes[(slopes["sample"] == "primary") &
                 (((slopes["spec"] == "M1") & (slopes["predictor"] == HBA1C)) |
                  slopes.apply(lambda r: r["spec"] == f"M2_{r['predictor']}", axis=1))].copy()
    fam["q_bh"] = multipletests(fam["p"], method="fdr_bh")[1]
    fam["family"] = "primary single-predictor slopes"
    fam["sig_fdr05"] = fam["q_bh"] < 0.05
    fam.to_csv(os.path.join(OUT_DATA, "primary_slope_tests_with_fdr.csv"), index=False)

    fam2 = nested[(nested["sample"] == "primary") & (nested["full"].isin(["M3"])) & (nested["reduced"].isin(["M1", "M2"]))].copy()
    fam2["q_bh"] = multipletests(fam2["p"], method="fdr_bh")[1]
    fam2.to_csv(os.path.join(OUT_DATA, "primary_incremental_tests_with_fdr.csv"), index=False)

    # M3_k: does each single CGM feature add beyond HbA1c (per outcome)?
    fam3 = nested[(nested["sample"] == "primary") & nested["full"].str.startswith("M3_") & (nested["reduced"] == "M1")].copy()
    fam3["q_bh"] = multipletests(fam3["p"], method="fdr_bh")[1]
    fam3.to_csv(os.path.join(OUT_DATA, "primary_single_cgm_beyond_hba1c_with_fdr.csv"), index=False)

    # ------------------ exploratory CGM metrics (single-feature sweep, FDR) ------------------
    run_exploratory_sweep(base)

    # ------------------ save everything ------------------
    summary.to_csv(os.path.join(OUT_DATA, "outcome_summary.csv"), index=False)
    fit.to_csv(os.path.join(OUT_DATA, "model_fit_all_specs.csv"), index=False)
    slopes.to_csv(os.path.join(OUT_DATA, "slope_tests_all_specs.csv"), index=False)
    nested.to_csv(os.path.join(OUT_DATA, "nested_tests_all.csv"), index=False)
    h2h.to_csv(os.path.join(OUT_DATA, "head_to_head_hba1c_vs_cgm.csv"), index=False)
    vif.to_csv(os.path.join(OUT_DATA, "vif_combined_model.csv"), index=False)
    partial.to_csv(os.path.join(OUT_DATA, "partial_spearman_correlations.csv"), index=False)
    nonlin.to_csv(os.path.join(OUT_DATA, "nonlinearity_quadratic_tests.csv"), index=False)
    strat.to_csv(os.path.join(OUT_DATA, "diabetes_stratified_slopes.csv"), index=False)
    with open(os.path.join(OUT_DATA, "coverage.json"), "w") as f:
        json.dump(coverage, f, indent=1)

    make_figures(slopes, nested, h2h, fit, strat, corr, coverage)
    print("Done. Outputs in", OUT_DATA, "and", OUT_FIG)


def figures_only():
    """re-draw figures from the saved CSVs without re-fitting anything"""
    g = lambda n: pd.read_csv(os.path.join(OUT_DATA, n))
    with open(os.path.join(OUT_DATA, "coverage.json")) as f:
        coverage = json.load(f)
    corr = pd.read_csv(os.path.join(OUT_DATA, "predictor_spearman_correlations.csv"), index_col=0)
    make_figures(g("slope_tests_all_specs.csv"), g("nested_tests_all.csv"), g("head_to_head_hba1c_vs_cgm.csv"),
                 g("model_fit_all_specs.csv"), g("diabetes_stratified_slopes.csv"), corr, coverage)


if __name__ == "__main__":
    import sys
    if "--figures-only" in sys.argv:
        figures_only()
    else:
        main()
