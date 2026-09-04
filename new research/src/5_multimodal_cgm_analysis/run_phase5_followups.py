"""
Phase 5b - follow-up analyses recommended in research_report_01 (section 5.5)
============================================================================

A. Parsimonious CGM pair (mean glucose + average daily SD) vs the four-metric block
   and vs HbA1c; TIR as the alternative second metric.
B. HbA1c-CGM discordance: haemoglobin glycation index (HGI = HbA1c residualised on
   mean glucose) and the glycation gap (HbA1c - GMI) as predictors of every outcome,
   with and without adjustment for red-cell indices.
C. Depression: pre-specified replication of the between-day-variability signal
   (SD of daily means, nocturnal mean) using the AI-READI recommended split
   (train = discovery, val + test = hold-out), plus sleep-regularity metrics and a
   bootstrap mediation analysis.
D. Diabetes-status interactions and restricted-cubic-spline dose-response curves for
   cognition and autonomic outcomes; non-diabetic-range slopes.
E. Within-window temporal check (first vs second half of the CGM wear): split-half
   reliability of the metrics and whether recency matters for prediction.

Outputs: reports/5_multimodal_cgm_analysis/data/followup_*.csv, figures/fig7-fig10.
"""

import os
import json
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor
from concurrent.futures import ProcessPoolExecutor, as_completed

from run_multimodal_cgm_models import (fit, fit_ml, nested_test, slope_row, cross_validate, delong_test,
                                       COV_FORMULA, BASE_COVS, OUTCOMES, PRED_LABEL, HBA1C, CORE_CGM,
                                       DATA_DIR, OUT_DATA, OUT_FIG)
import extract_multimodal_dataset as EX

warnings.filterwarnings("ignore")
np.random.seed(20260904)

PAIR = ["mean_glucose", "avg_daily_sd"]
PAIR_TIR = ["mean_glucose", "avg_daily_tir"]
LABEL = dict(PRED_LABEL)
LABEL.update({"hgi": "HGI (HbA1c residual on mean glucose, %)", "glycation_gap": "Glycation gap (HbA1c - GMI, %)",
              "sd_of_daily_means": "SD of daily means (mg/dL)", "nocturnal_mean": "Nocturnal mean 00-06h (mg/dL)",
              "sleep_midpoint_sd_h": "Sleep-midpoint SD across nights (h)", "sleep_onset_sd_h": "Sleep-onset SD (h)",
              "sleep_tst_sd_min": "Sleep-duration SD (min)", "sleep_efficiency_pct": "Sleep efficiency (%)",
              "sleep_tst_min": "Sleep duration (min)", "steps_cv_between_days": "Step-count CV between days (%)"})
BLUE, ORANGE, AQUA, GREY, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#8a8987", "#4a3aa7"


def vif(df, cols):
    X = sm.add_constant(df[cols].astype(float))
    return {c: float(variance_inflation_factor(X.values, i + 1)) for i, c in enumerate(cols)}


def per_sd(model, term, sd, kind):
    r = slope_row(model, term, sd, kind)
    r["term"] = term
    return r


# ======================================================================================
# A. parsimonious pair
# ======================================================================================
def part_a(base):
    rows, fits = [], []
    for dom, y, kind, lab, ef, ec in OUTCOMES:
        covf = COV_FORMULA + ef
        d = base.dropna(subset=[y, HBA1C] + list(CORE_CGM) + BASE_COVS + ec).copy()
        if kind == "logit":
            d[y] = d[y].astype(int)
        specs = {"M0": f"{y} ~ {covf}", "M1": f"{y} ~ {covf} + {HBA1C}",
                 "P2": f"{y} ~ {covf} + " + " + ".join(PAIR),
                 "P2T": f"{y} ~ {covf} + " + " + ".join(PAIR_TIR),
                 "P3": f"{y} ~ {covf} + {HBA1C} + " + " + ".join(PAIR),
                 "M2": f"{y} ~ {covf} + " + " + ".join(CORE_CGM),
                 "M3": f"{y} ~ {covf} + {HBA1C} + " + " + ".join(CORE_CGM)}
        ml = {k: fit_ml(f, d, kind) for k, f in specs.items()}
        rb = {k: fit(f, d, kind) for k, f in specs.items()}
        sds = {p: float(d[p].std(ddof=1)) for p in [HBA1C] + list(CORE_CGM)}
        for k in specs:
            row = {"outcome": y, "label": lab, "kind": kind, "spec": k, "n": len(d), "aic": float(ml[k].aic),
                   "bic": float(ml[k].bic), "k_params": int(ml[k].df_model + 1)}
            if kind == "ols":
                row["adj_r2"] = float(ml[k].rsquared_adj)
            cvr = cross_validate(specs[k], d, y, kind)
            row.update(cvr)
            fits.append(row)
        tests = [("P3", "M1", "pair adds beyond HbA1c"), ("P3", "P2", "HbA1c adds beyond pair"),
                 ("M3", "P3", "other two metrics add beyond pair + HbA1c"), ("M2", "P2", "other two metrics add beyond pair"),
                 ("P2", "M0", "pair adds to covariates")]
        for full, red, q in tests:
            s, dfree, p, lab_t = nested_test(ml[full], ml[red], kind)
            rows.append({"outcome": y, "label": lab, "kind": kind, "full": full, "reduced": red, "question": q,
                         "stat": s, "df": dfree, "p": p, "test": lab_t, "delta_aic": float(ml[full].aic - ml[red].aic), "n": len(d)})
        # slopes in P3 and in P2 / P2T
        for spec in ["P2", "P2T", "P3"]:
            for term in rb[spec].params.index:
                if term in sds:
                    r = per_sd(rb[spec], term, sds[term], kind)
                    r.update({"outcome": y, "label": lab, "kind": kind, "spec": spec, "n": len(d)})
                    fits.append({**{"outcome": y, "label": lab, "kind": kind, "spec": spec + "_slope_" + term, "n": len(d)},
                                 **{f"slope_{kk}": vv for kk, vv in r.items() if kk in ("beta_per_sd", "ci_low_per_sd", "ci_high_per_sd", "p", "or_per_sd")}})
        v = vif(d, [HBA1C] + PAIR)
        rows.append({"outcome": y, "label": lab, "kind": kind, "full": "P3", "reduced": "-", "question": "VIF in P3",
                     "stat": np.nan, "df": 0, "p": np.nan, "test": "; ".join(f"{k}={vv:.2f}" for k, vv in v.items()),
                     "delta_aic": np.nan, "n": len(d)})
    nested = pd.DataFrame(rows)
    fam = nested[nested["question"] == "pair adds beyond HbA1c"].copy()
    fam["q_bh"] = multipletests(fam["p"], method="fdr_bh")[1]
    fam2 = nested[nested["question"] == "HbA1c adds beyond pair"].copy()
    fam2["q_bh"] = multipletests(fam2["p"], method="fdr_bh")[1]
    nested = nested.merge(pd.concat([fam, fam2])[["outcome", "question", "q_bh"]], on=["outcome", "question"], how="left")
    nested.to_csv(os.path.join(OUT_DATA, "followup_A_pair_nested_tests.csv"), index=False)
    pd.DataFrame(fits).to_csv(os.path.join(OUT_DATA, "followup_A_pair_fit_and_slopes.csv"), index=False)
    return nested, pd.DataFrame(fits)


# ======================================================================================
# B. discordance
# ======================================================================================
def part_b(base):
    d = base.copy()
    hgi_model = smf.ols(f"{HBA1C} ~ mean_glucose", d).fit()
    d["hgi"] = hgi_model.resid
    d["glycation_gap"] = d[HBA1C] - d["gmi"]
    info = {"hgi_model_intercept": float(hgi_model.params["Intercept"]), "hgi_model_slope_per_mg_dl": float(hgi_model.params["mean_glucose"]),
            "hgi_model_r2": float(hgi_model.rsquared), "hgi_sd": float(d["hgi"].std()), "gap_sd": float(d["glycation_gap"].std()),
            "corr_hgi_gap": float(d[["hgi", "glycation_gap"]].corr().iloc[0, 1]), "n": int(len(d))}
    # determinants of HGI
    det_cols = ["age", "bmi", "hemoglobin_g_dl", "mcv_fl", "rdw_pct", "hematocrit_pct", "creatinine", "kidney_disease",
                "any_diabetes", "insulin_use", "clinical_site", "years_of_education"]
    dd = d.dropna(subset=det_cols).copy()
    det = smf.ols("hgi ~ age + bmi + hemoglobin_g_dl + mcv_fl + rdw_pct + hematocrit_pct + creatinine + kidney_disease + "
                  "any_diabetes + insulin_use + C(clinical_site) + years_of_education", dd).fit(cov_type="HC3")
    det_rows = []
    for t in det.params.index:
        if t == "Intercept":
            continue
        sd_x = float(dd[t].std(ddof=1)) if t in dd.columns else np.nan
        det_rows.append({"term": t, "beta": float(det.params[t]), "se": float(det.bse[t]), "p": float(det.pvalues[t]),
                         "beta_per_sd": float(det.params[t] * sd_x) if np.isfinite(sd_x) else np.nan, "n": len(dd), "r2": float(det.rsquared)})
    pd.DataFrame(det_rows).to_csv(os.path.join(OUT_DATA, "followup_B_hgi_determinants.csv"), index=False)
    info["hgi_determinants_r2"] = float(det.rsquared)
    # HGI vs univariate correlates
    corr_rows = []
    for c in ["age", "bmi", "hemoglobin_g_dl", "mcv_fl", "rdw_pct", "hematocrit_pct", "creatinine", "years_of_education", "avg_daily_sd", "cgm_valid_days"]:
        s = d[[c, "hgi"]].dropna()
        rho, p = stats.spearmanr(s[c], s["hgi"])
        corr_rows.append({"variable": c, "spearman_rho_with_hgi": float(rho), "p": float(p), "n": len(s)})
    pd.DataFrame(corr_rows).to_csv(os.path.join(OUT_DATA, "followup_B_hgi_correlates.csv"), index=False)

    rows = []
    for dom, y, kind, lab, ef, ec in OUTCOMES:
        covf = COV_FORMULA + ef
        for disc in ["hgi", "glycation_gap"]:
            need = [y, disc, "mean_glucose"] + BASE_COVS + ec
            dsub = d.dropna(subset=need).copy()
            if kind == "logit":
                dsub[y] = dsub[y].astype(int)
            sd_d = float(dsub[disc].std(ddof=1)); sd_g = float(dsub["mean_glucose"].std(ddof=1))
            # model 1: mean glucose + discordance
            m = fit(f"{y} ~ {covf} + mean_glucose + {disc}", dsub, kind)
            r = per_sd(m, disc, sd_d, kind); g = per_sd(m, "mean_glucose", sd_g, kind)
            rows.append({"outcome": y, "label": lab, "kind": kind, "discordance": disc, "adjustment": "covariates + mean glucose",
                         "n": len(dsub), **{f"disc_{k}": v for k, v in r.items() if k != "term"},
                         **{f"glu_{k}": v for k, v in g.items() if k in ("beta_per_sd", "p", "or_per_sd")}})
            # model 2: + red-cell indices
            need2 = need + ["hemoglobin_g_dl", "mcv_fl", "rdw_pct"]
            dsub2 = d.dropna(subset=need2).copy()
            if kind == "logit":
                dsub2[y] = dsub2[y].astype(int)
            m2 = fit(f"{y} ~ {covf} + mean_glucose + {disc} + hemoglobin_g_dl + mcv_fl + rdw_pct", dsub2, kind)
            r2 = per_sd(m2, disc, float(dsub2[disc].std(ddof=1)), kind)
            rows.append({"outcome": y, "label": lab, "kind": kind, "discordance": disc, "adjustment": "+ haemoglobin, MCV, RDW",
                         "n": len(dsub2), **{f"disc_{k}": v for k, v in r2.items() if k != "term"}})
    res = pd.DataFrame(rows)
    for disc in ["hgi", "glycation_gap"]:
        for adj in res["adjustment"].unique():
            msk = (res["discordance"] == disc) & (res["adjustment"] == adj)
            res.loc[msk, "q_bh"] = multipletests(res.loc[msk, "disc_p"], method="fdr_bh")[1]
    res.to_csv(os.path.join(OUT_DATA, "followup_B_discordance_effects.csv"), index=False)
    with open(os.path.join(OUT_DATA, "followup_B_hgi_info.json"), "w") as f:
        json.dump(info, f, indent=1)
    return res, info, d


# ======================================================================================
# C. depression replication + sleep regularity + mediation
# ======================================================================================
def part_c(base):
    d = base.copy()
    d["split"] = np.where(d["recommended_split"] == "train", "discovery (train)", "hold-out (val + test)")
    preds = ["sd_of_daily_means", "nocturnal_mean", "avg_daily_sd", "mean_glucose", HBA1C,
             "sleep_midpoint_sd_h", "sleep_onset_sd_h", "sleep_tst_sd_min", "sleep_efficiency_pct", "sleep_tst_min", "steps_cv_between_days"]
    rows = []
    for y, kind in [("cesd10_total", "ols"), ("cesd10_ge10", "logit")]:
        for split in ["discovery (train)", "hold-out (val + test)", "all"]:
            dd = d if split == "all" else d[d["split"] == split]
            for pr in preds:
                s = dd.dropna(subset=[y, pr] + BASE_COVS).copy()
                if kind == "logit":
                    s[y] = s[y].astype(int)
                if len(s) < 100:
                    continue
                m = fit(f"{y} ~ {COV_FORMULA} + {pr}", s, kind)
                r = per_sd(m, pr, float(s[pr].std(ddof=1)), kind)
                rows.append({"outcome": y, "kind": kind, "split": split, "predictor": pr, "n": len(s),
                             **{k: v for k, v in r.items() if k != "term"}})
    rep = pd.DataFrame(rows)
    # replication verdict for the two pre-specified CGM predictors
    verdict = []
    for y in ["cesd10_total", "cesd10_ge10"]:
        for pr in ["sd_of_daily_means", "nocturnal_mean"]:
            a = rep[(rep.outcome == y) & (rep.predictor == pr) & (rep.split == "discovery (train)")].iloc[0]
            b = rep[(rep.outcome == y) & (rep.predictor == pr) & (rep.split == "hold-out (val + test)")].iloc[0]
            same_sign = np.sign(a["beta_per_sd"]) == np.sign(b["beta_per_sd"])
            p_one_sided = b["p"] / 2 if same_sign else 1 - b["p"] / 2
            verdict.append({"outcome": y, "predictor": pr, "discovery_beta_per_sd": a["beta_per_sd"], "discovery_p": a["p"], "discovery_n": a["n"],
                            "holdout_beta_per_sd": b["beta_per_sd"], "holdout_p_two_sided": b["p"], "holdout_p_one_sided": p_one_sided,
                            "holdout_n": b["n"], "replicated_one_sided_0.05": bool(same_sign and p_one_sided < 0.05)})
    verdict = pd.DataFrame(verdict)
    rep.to_csv(os.path.join(OUT_DATA, "followup_C_depression_split_replication.csv"), index=False)
    verdict.to_csv(os.path.join(OUT_DATA, "followup_C_depression_replication_verdict.csv"), index=False)

    # joint models on the full sample: does between-day variability add beyond HbA1c and mean glucose, and beyond sleep regularity?
    joint_rows = []
    for y, kind in [("cesd10_total", "ols"), ("cesd10_ge10", "logit")]:
        s = d.dropna(subset=[y, "sd_of_daily_means", "nocturnal_mean", HBA1C, "mean_glucose", "avg_daily_sd",
                             "sleep_midpoint_sd_h", "sleep_tst_sd_min", "sleep_tst_min", "sleep_efficiency_pct"] + BASE_COVS).copy()
        if kind == "logit":
            s[y] = s[y].astype(int)
        sd_v = float(s["sd_of_daily_means"].std(ddof=1))
        specs = {"J0: + SD of daily means": f"{y} ~ {COV_FORMULA} + sd_of_daily_means",
                 "J1: + HbA1c + mean glucose": f"{y} ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose",
                 "J2: + within-day SD": f"{y} ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose + avg_daily_sd",
                 "J3: + sleep regularity & duration": f"{y} ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose + avg_daily_sd + sleep_midpoint_sd_h + sleep_tst_sd_min + sleep_tst_min + sleep_efficiency_pct",
                 "J4: + nocturnal mean": f"{y} ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose + avg_daily_sd + sleep_midpoint_sd_h + sleep_tst_sd_min + sleep_tst_min + sleep_efficiency_pct + nocturnal_mean"}
        for name, f in specs.items():
            m = fit(f, s, kind)
            r = per_sd(m, "sd_of_daily_means", sd_v, kind)
            joint_rows.append({"outcome": y, "kind": kind, "spec": name, "n": len(s), **{k: v for k, v in r.items() if k != "term"},
                               "aic": float(fit_ml(f, s, kind).aic)})
            if "sleep_midpoint_sd_h" in m.params.index:
                for t in ["sleep_midpoint_sd_h", "sleep_tst_sd_min", "sleep_tst_min", "sleep_efficiency_pct", "nocturnal_mean"]:
                    if t in m.params.index:
                        rr = per_sd(m, t, float(s[t].std(ddof=1)), kind)
                        joint_rows.append({"outcome": y, "kind": kind, "spec": name + f" [{t}]", "n": len(s), **{k: v for k, v in rr.items() if k != "term"}, "aic": np.nan})
    joint = pd.DataFrame(joint_rows)
    joint.to_csv(os.path.join(OUT_DATA, "followup_C_depression_joint_models.csv"), index=False)

    # mediation: sd_of_daily_means -> sleep regularity -> CES-D (bootstrap indirect effect), OLS on CES-D total
    med_rows = []
    s = d.dropna(subset=["cesd10_total", "sd_of_daily_means", "sleep_midpoint_sd_h", "sleep_tst_sd_min", HBA1C, "mean_glucose"] + BASE_COVS).copy()
    for med in ["sleep_midpoint_sd_h", "sleep_tst_sd_min"]:
        def indirect(df):
            a = smf.ols(f"{med} ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose", df).fit().params["sd_of_daily_means"]
            mb = smf.ols(f"cesd10_total ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose + {med}", df).fit()
            return a * mb.params[med], mb.params["sd_of_daily_means"]
        ind, direct = indirect(s)
        total = smf.ols(f"cesd10_total ~ {COV_FORMULA} + sd_of_daily_means + {HBA1C} + mean_glucose", s).fit().params["sd_of_daily_means"]
        boots = []
        rng = np.random.default_rng(3)
        for _ in range(500):
            b = s.sample(n=len(s), replace=True, random_state=int(rng.integers(1e9)))
            try:
                boots.append(indirect(b)[0])
            except Exception:
                pass
        lo, hi = np.percentile(boots, [2.5, 97.5])
        sd_v = float(s["sd_of_daily_means"].std(ddof=1))
        med_rows.append({"mediator": med, "n": len(s), "total_effect_per_sd": total * sd_v, "direct_effect_per_sd": direct * sd_v,
                         "indirect_effect_per_sd": ind * sd_v, "indirect_ci_low": lo * sd_v, "indirect_ci_high": hi * sd_v,
                         "pct_mediated": 100 * ind / total if total != 0 else np.nan})
    med = pd.DataFrame(med_rows)
    med.to_csv(os.path.join(OUT_DATA, "followup_C_depression_mediation.csv"), index=False)

    # what explains between-day variability itself?
    s = d.dropna(subset=["sd_of_daily_means", "sleep_midpoint_sd_h", "sleep_tst_sd_min", "steps_cv_between_days", "mean_glucose", "avg_daily_sd"] + BASE_COVS).copy()
    m = fit(f"sd_of_daily_means ~ {COV_FORMULA} + mean_glucose + avg_daily_sd + sleep_midpoint_sd_h + sleep_tst_sd_min + steps_cv_between_days + any_diabetes", s, "ols")
    expl = []
    for t in ["mean_glucose", "avg_daily_sd", "sleep_midpoint_sd_h", "sleep_tst_sd_min", "steps_cv_between_days", "any_diabetes"]:
        r = per_sd(m, t, float(s[t].std(ddof=1)), "ols")
        expl.append({"term": t, "n": len(s), "r2": float(m.rsquared), **{k: v for k, v in r.items() if k != "term"}})
    pd.DataFrame(expl).to_csv(os.path.join(OUT_DATA, "followup_C_between_day_variability_determinants.csv"), index=False)
    return rep, verdict, joint, med


# ======================================================================================
# D. interactions and splines
# ======================================================================================
D_OUTCOMES = [("moca_total", "ols", "MoCA total score (0-30)"), ("cognitive_impairment", "logit", "Cognitive impairment (MoCA < 26)"),
              ("hr_resting_proxy", "ols", "Resting heart-rate proxy (bpm)"), ("stress_mean", "ols", "Garmin stress score (0-100)")]
D_PREDS = [HBA1C, "mean_glucose", "avg_daily_sd"]
GROUP_ORDER = ["No diabetes", "Pre-diabetes / lifestyle", "T2D non-insulin", "T2D insulin"]


def part_d(base):
    rows, spline_rows, curve_rows = [], [], []
    for y, kind, lab in D_OUTCOMES:
        for pr in D_PREDS:
            s = base.dropna(subset=[y, pr] + BASE_COVS).copy()
            if kind == "logit":
                s[y] = s[y].astype(int)
            sd_x = float(s[pr].std(ddof=1)); s["_z"] = (s[pr] - s[pr].mean()) / sd_x
            # 4-level interaction test
            m_int = fit_ml(f"{y} ~ {COV_FORMULA} + _z * C(diabetes_status)", s, kind)
            m_no = fit_ml(f"{y} ~ {COV_FORMULA} + _z + C(diabetes_status)", s, kind)
            st, dfree, p, lab_t = nested_test(m_int, m_no, kind)
            for g in GROUP_ORDER:
                sub = s[s["diabetes_status"] == g]
                if len(sub) < 60 or (kind == "logit" and sub[y].sum() < 10):
                    continue
                mg = fit(f"{y} ~ {COV_FORMULA} + _z", sub, kind)
                ci = mg.conf_int().loc["_z"]
                rows.append({"outcome": y, "label": lab, "predictor": pr, "group": g, "n": len(sub), "slope_per_pooled_sd": float(mg.params["_z"]),
                             "ci_low": float(ci[0]), "ci_high": float(ci[1]), "p": float(mg.pvalues["_z"]),
                             "interaction_stat": st, "interaction_df": dfree, "interaction_p": p, "interaction_test": lab_t})
            # non-diabetic range: no diabetes group AND HbA1c < 6.5
            sub = s[(s["any_diabetes"] == 0) & (s[HBA1C] < 6.5)]
            mg = fit(f"{y} ~ {COV_FORMULA} + _z", sub, kind)
            ci = mg.conf_int().loc["_z"]
            rows.append({"outcome": y, "label": lab, "predictor": pr, "group": "Non-diabetic range (no T2D & HbA1c < 6.5)", "n": len(sub),
                         "slope_per_pooled_sd": float(mg.params["_z"]), "ci_low": float(ci[0]), "ci_high": float(ci[1]), "p": float(mg.pvalues["_z"]),
                         "interaction_stat": np.nan, "interaction_df": 0, "interaction_p": np.nan, "interaction_test": ""})
            # restricted cubic spline (natural cubic, 4 df) vs linear
            m_lin = fit_ml(f"{y} ~ {COV_FORMULA} + {pr}", s, kind)
            m_spl = fit_ml(f"{y} ~ {COV_FORMULA} + cr({pr}, df=4)", s, kind)
            st2, df2, p2, lab2 = nested_test(m_spl, m_lin, kind)
            spline_rows.append({"outcome": y, "label": lab, "predictor": pr, "n": len(s), "nonlinearity_stat": st2, "df": df2, "p_nonlinear": p2,
                                "test": lab2, "aic_linear": float(m_lin.aic), "aic_spline": float(m_spl.aic)})
            # predicted curve at covariate means / modal categories
            grid = np.linspace(s[pr].quantile(0.01), s[pr].quantile(0.99), 60)
            ref = {}
            for c in BASE_COVS:
                ref[c] = float(s[c].mean()) if pd.api.types.is_numeric_dtype(s[c]) else s[c].mode().iloc[0]
            newd = pd.DataFrame({**{k: [v] * len(grid) for k, v in ref.items()}, pr: grid})
            pred = m_spl.get_prediction(newd)
            sf = pred.summary_frame(alpha=0.05)
            mean_col = "mean" if "mean" in sf.columns else "predicted"
            lo_col = "mean_ci_lower" if "mean_ci_lower" in sf.columns else "ci_lower"
            hi_col = "mean_ci_upper" if "mean_ci_upper" in sf.columns else "ci_upper"
            for xg, mu, lo, hi in zip(grid, sf[mean_col], sf[lo_col], sf[hi_col]):
                curve_rows.append({"outcome": y, "label": lab, "predictor": pr, "x": float(xg), "fit": float(mu), "lo": float(lo), "hi": float(hi)})
    strat = pd.DataFrame(rows); spl = pd.DataFrame(spline_rows); curves = pd.DataFrame(curve_rows)
    strat.to_csv(os.path.join(OUT_DATA, "followup_D_group_slopes_and_interactions.csv"), index=False)
    spl.to_csv(os.path.join(OUT_DATA, "followup_D_spline_nonlinearity.csv"), index=False)
    curves.to_csv(os.path.join(OUT_DATA, "followup_D_spline_curves.csv"), index=False)
    return strat, spl, curves


# ======================================================================================
# E. split-half temporal check
# ======================================================================================
def _half_metrics(args):
    pid, folder, tz = args
    files = [f for f in os.listdir(folder) if f.endswith(".json")]
    if not files:
        return None
    try:
        with open(os.path.join(folder, files[0])) as f:
            body = json.load(f).get("body", {}).get("cgm", [])
        rows = []
        for r in body:
            v = r.get("blood_glucose", {}).get("value")
            ts = r.get("effective_time_frame", {}).get("time_interval", {}).get("start_date_time")
            if v is None or ts is None:
                continue
            rows.append((ts, float(v)))
        df = pd.DataFrame(rows, columns=["ts", "g"])
        df["t"] = EX._to_local(df["ts"], tz)
        df = df.dropna().sort_values("t")
        df = df[(df["g"] >= 39) & (df["g"] <= 401)]
        if len(df) < 2 * 288 * 3:
            return None
        mid = df["t"].iloc[0] + (df["t"].iloc[-1] - df["t"].iloc[0]) / 2
        out = {"person_id": pid}
        for name, part in (("h1", df[df["t"] < mid]), ("h2", df[df["t"] >= mid])):
            part = part.copy(); part["day"] = part["t"].dt.date
            daily = part.groupby("day")["g"].agg(n="size", sd=lambda x: x.std(ddof=1), tir=lambda x: ((x >= 70) & (x <= 180)).mean() * 100)
            valid = daily[daily["n"] >= 0.7 * 288]
            if len(valid) < 2:
                return None
            out[f"{name}_mean"] = float(part["g"].mean()); out[f"{name}_sd"] = float(valid["sd"].mean())
            out[f"{name}_tir"] = float(valid["tir"].mean()); out[f"{name}_days"] = int(len(valid))
        return out
    except Exception:
        return None


def icc_2_1(x, y):
    """two-way random, absolute agreement, single measure ICC(2,1)"""
    data = np.vstack([x, y]).T
    n, k = data.shape
    mean_r = data.mean(axis=1); mean_c = data.mean(axis=0); gm = data.mean()
    ss_r = k * ((mean_r - gm) ** 2).sum(); ss_c = n * ((mean_c - gm) ** 2).sum()
    ss_e = ((data - mean_r[:, None] - mean_c[None, :] + gm) ** 2).sum()
    ms_r = ss_r / (n - 1); ms_c = ss_c / (k - 1); ms_e = ss_e / ((n - 1) * (k - 1))
    return float((ms_r - ms_e) / (ms_r + (k - 1) * ms_e + k * (ms_c - ms_e) / n))


def part_e(base):
    site_map = EX._load_site_map()
    tasks = []
    for pid in base["person_id"]:
        folder = os.path.join(EX.CGM_DIR, str(int(pid)))
        if os.path.isdir(folder):
            tasks.append((int(pid), folder, site_map.get(int(pid), "America/Los_Angeles")))
    out = []
    with ProcessPoolExecutor(EX.N_WORKERS) as ex:
        for fut in as_completed([ex.submit(_half_metrics, t) for t in tasks]):
            r = fut.result()
            if r:
                out.append(r)
    h = pd.DataFrame(out)
    rel = []
    for m in ["mean", "sd", "tir"]:
        rel.append({"metric": m, "n": len(h), "pearson_r": float(h[[f"h1_{m}", f"h2_{m}"]].corr().iloc[0, 1]),
                    "icc_2_1": icc_2_1(h[f"h1_{m}"].to_numpy(), h[f"h2_{m}"].to_numpy()),
                    "mean_abs_diff": float((h[f"h1_{m}"] - h[f"h2_{m}"]).abs().mean()),
                    "mean_h1": float(h[f"h1_{m}"].mean()), "mean_h2": float(h[f"h2_{m}"].mean()),
                    "paired_t_p": float(stats.ttest_rel(h[f"h1_{m}"], h[f"h2_{m}"]).pvalue)})
    rel = pd.DataFrame(rel)
    rel.to_csv(os.path.join(OUT_DATA, "followup_E_split_half_reliability.csv"), index=False)
    # does the half closer to the visit predict better?  (CGM starts at the visit, so h1 = closer to the clinic assessments)
    d = base.merge(h, on="person_id", how="inner")
    rows = []
    for y, kind, lab in D_OUTCOMES + [("cesd10_total", "ols", "CES-D-10"), ("steps_per_day", "ols", "Steps per wear-day"), ("sleep_tst_min", "ols", "Sleep duration")]:
        s = d.dropna(subset=[y, "h1_mean", "h2_mean", HBA1C] + BASE_COVS).copy()
        if kind == "logit":
            s[y] = s[y].astype(int)
        for half in ["h1", "h2"]:
            m = fit(f"{y} ~ {COV_FORMULA} + {half}_mean", s, kind)
            r = per_sd(m, f"{half}_mean", float(s[f"{half}_mean"].std(ddof=1)), kind)
            rows.append({"outcome": y, "label": lab, "half": {"h1": "first half (days 1-5, nearest the visit)", "h2": "second half (days 6-10)"}[half],
                         "n": len(s), **{k: v for k, v in r.items() if k != "term"}, "aic": float(fit_ml(f"{y} ~ {COV_FORMULA} + {half}_mean", s, kind).aic)})
        m = fit(f"{y} ~ {COV_FORMULA} + h1_mean + h2_mean", s, kind)
        for half in ["h1", "h2"]:
            r = per_sd(m, f"{half}_mean", float(s[f"{half}_mean"].std(ddof=1)), kind)
            rows.append({"outcome": y, "label": lab, "half": f"{half} (joint model with both halves)", "n": len(s), **{k: v for k, v in r.items() if k != "term"}, "aic": np.nan})
    rec = pd.DataFrame(rows)
    rec.to_csv(os.path.join(OUT_DATA, "followup_E_recency_models.csv"), index=False)
    return rel, rec


# ======================================================================================
# figures
# ======================================================================================
def figures(nestedA, fitsA, discB, repC, verdictC, stratD, curvesD, base):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#b5b4b0",
                         "xtick.color": "#52514e", "ytick.color": "#52514e", "figure.facecolor": "white"})
    labs = [l for _, _, _, l, _, _ in OUTCOMES]

    # Fig 7: spline dose-response curves
    fig, axes = plt.subplots(len(D_OUTCOMES), len(D_PREDS), figsize=(13, 3.1 * len(D_OUTCOMES)))
    for i, (y, kind, lab) in enumerate(D_OUTCOMES):
        for j, pr in enumerate(D_PREDS):
            ax = axes[i, j]
            c = curvesD[(curvesD.outcome == y) & (curvesD.predictor == pr)]
            ax.fill_between(c["x"], c["lo"], c["hi"], color=BLUE if pr == HBA1C else ORANGE, alpha=0.18, lw=0)
            ax.plot(c["x"], c["fit"], color=BLUE if pr == HBA1C else ORANGE, lw=2)
            # group medians as reference ticks
            for g, col in zip(GROUP_ORDER, [AQUA, AQUA, ORANGE, VIOLET]):
                med = base.loc[base["diabetes_status"] == g, pr].median()
                ax.axvline(med, color=GREY, lw=0.8, ls=":")
                ax.text(med, ax.get_ylim()[1] if False else c["hi"].max(), g.split(" /")[0].replace("T2D ", "T2D\n"), fontsize=6, rotation=90, va="top", ha="right", color="#52514e")
            if pr == HBA1C:
                ax.axvline(6.5, color="#e34948", lw=1, ls="--")
            ax.set_xlabel(PRED_LABEL[pr], fontsize=8)
            ax.set_ylabel(("log-odds of " if kind == "logit" else "") + lab.split(" (")[0], fontsize=8)
            ax.set_title(f"{lab.split(' (')[0]} vs {PRED_LABEL[pr]}", fontsize=8.5, loc="left")
    fig.suptitle("Fig. 7  Restricted-cubic-spline dose-response (4 df, covariate-adjusted, 95% CI); dotted lines = group medians, red dashed = HbA1c 6.5%",
                 fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.97]); fig.savefig(os.path.join(OUT_FIG, "fig7_spline_dose_response.png"), dpi=180); plt.close(fig)

    # Fig 8: discordance (HGI) effects per outcome, with/without red-cell adjustment, next to mean-glucose effect
    dh = discB[discB["discordance"] == "hgi"].copy()
    fig, ax = plt.subplots(figsize=(10, 0.5 * len(labs) + 1.8))
    yy = np.arange(len(labs))[::-1]
    for off, adj, col in ((0.18, "covariates + mean glucose", BLUE), (-0.18, "+ haemoglobin, MCV, RDW", VIOLET)):
        sub = dh[dh["adjustment"] == adj].set_index("label").reindex(labs)
        # standardise: use t-statistic so outcomes on different scales share an axis
        ax.barh(yy + off, sub["disc_stat"], height=0.34, color=col, label=f"HGI: {adj}")
    sub = dh[dh["adjustment"] == "covariates + mean glucose"].set_index("label").reindex(labs)
    ax.plot(sub["glu_p"].map(lambda p: np.nan), yy, alpha=0)  # placeholder
    for yv, (lab, r) in zip(yy, sub.iterrows()):
        ax.text(ax.get_xlim()[1] if False else max(r["disc_stat"], 0) + 0.3, yv + 0.18, f"q={r['q_bh']:.2g}", fontsize=7, va="center", color="#52514e")
    for xv in (-1.96, 1.96):
        ax.axvline(xv, color="#b5b4b0", lw=1, ls="--")
    ax.axvline(0, color="#52514e", lw=1)
    ax.set_yticks(yy); ax.set_yticklabels(labs, fontsize=8)
    ax.set_xlabel("t / z statistic of the HGI slope (positive = higher outcome with higher-than-expected HbA1c)", fontsize=8.5)
    ax.legend(fontsize=8, frameon=False, loc="lower right")
    ax.set_title("Fig. 8  HbA1c-CGM discordance (HGI) as a predictor, holding mean glucose constant", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig8_hgi_discordance_effects.png"), dpi=180); plt.close(fig)

    # Fig 9: depression replication forest
    preds = ["sd_of_daily_means", "nocturnal_mean", "avg_daily_sd", "mean_glucose", HBA1C, "sleep_midpoint_sd_h", "sleep_onset_sd_h",
             "sleep_tst_sd_min", "sleep_efficiency_pct", "sleep_tst_min", "steps_cv_between_days"]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    for ax, (y, kind, ttl) in zip(axes, [("cesd10_total", "ols", "CES-D-10 total (points per SD)"), ("cesd10_ge10", "logit", "CES-D-10 >= 10 (log-OR per SD)")]):
        yy = np.arange(len(preds))[::-1]
        for off, split, col, mk in ((0.2, "discovery (train)", AQUA, "s"), (0.0, "hold-out (val + test)", ORANGE, "o"), (-0.2, "all", GREY, "D")):
            sub = repC[(repC.outcome == y) & (repC.split == split)].set_index("predictor").reindex(preds)
            if kind == "logit":
                est, lo, hi = np.log(sub["or_per_sd"]), np.log(sub["or_ci_low"]), np.log(sub["or_ci_high"])
            else:
                est, lo, hi = sub["beta_per_sd"], sub["ci_low_per_sd"], sub["ci_high_per_sd"]
            for yv, e, l, h in zip(yy, est, lo, hi):
                ax.plot([l, h], [yv + off, yv + off], color=col, lw=1.6)
                ax.plot(e, yv + off, mk, color=col, ms=4.5, mec="white", mew=0.7, label=split if yv == yy[0] else None)
        ax.axvline(0, color="#b5b4b0", lw=1, ls="--")
        ax.set_yticks(yy); ax.set_yticklabels([LABEL.get(p, p) for p in preds], fontsize=8)
        ax.set_title(ttl, fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False, loc="lower right")
    fig.suptitle("Fig. 9  Depression: single-predictor adjusted effects in the discovery split, the hold-out split and the full sample", fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.95]); fig.savefig(os.path.join(OUT_FIG, "fig9_depression_replication.png"), dpi=180); plt.close(fig)

    # Fig 10: parsimonious pair vs 4-metric block vs HbA1c, cross-validated
    fa = fitsA[fitsA["spec"].isin(["M0", "M1", "P2", "P2T", "P3", "M2", "M3"])].copy()
    fa["metric"] = np.where(fa["kind"] == "ols", fa["cv_r2_mean"], fa["cv_auc_mean"])
    piv = fa.pivot_table(index="label", columns="spec", values="metric").reindex(labs)
    fig, ax = plt.subplots(figsize=(10, 0.5 * len(labs) + 1.8))
    yy = np.arange(len(piv))[::-1]; h = 0.13
    cols = {"M0": GREY, "M1": BLUE, "P2": ORANGE, "P2T": "#eda100", "P3": AQUA, "M2": "#e87ba4", "M3": VIOLET}
    names = {"M0": "Covariates only", "M1": "+ HbA1c", "P2": "+ mean glucose + daily SD", "P2T": "+ mean glucose + daily TIR",
             "P3": "+ HbA1c + mean glucose + daily SD", "M2": "+ 4 CGM metrics", "M3": "+ HbA1c + 4 CGM metrics"}
    for i, s in enumerate(["M0", "M1", "P2", "P2T", "P3", "M2", "M3"]):
        ax.barh(yy + (3 - i) * h, piv[s], height=h * 0.9, color=cols[s], label=names[s])
    ax.set_yticks(yy); ax.set_yticklabels(piv.index, fontsize=8)
    ax.set_xlabel("Repeated 10-fold CV: out-of-sample R^2 (continuous) or AUC (binary)", fontsize=8.5)
    ax.legend(fontsize=7.5, frameon=False, loc="lower right", ncol=2)
    ax.set_title("Fig. 10  Parsimonious CGM pair vs four-metric block vs HbA1c (cross-validated)", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_FIG, "fig10_pair_vs_block_cv.png"), dpi=180); plt.close(fig)


def main():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_multimodal_dataset.csv"), low_memory=False)
    base = df[df["has_cgm"] == 1].dropna(subset=[HBA1C] + list(CORE_CGM) + BASE_COVS).copy()
    print(f"analysis base n = {len(base)}")
    print("A. parsimonious pair ..."); nestedA, fitsA = part_a(base)
    print("B. discordance ..."); discB, infoB, _ = part_b(base)
    print("C. depression replication ..."); repC, verdictC, jointC, medC = part_c(base)
    print("D. interactions & splines ..."); stratD, splD, curvesD = part_d(base)
    print("E. split-half temporal check ..."); relE, recE = part_e(base)
    print("figures ..."); figures(nestedA, fitsA, discB, repC, verdictC, stratD, curvesD, base)
    print("done")


if __name__ == "__main__":
    main()
