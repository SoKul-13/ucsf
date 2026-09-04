"""
Phase 5 - Multimodal master dataset extraction
==============================================

Builds `data/master_multimodal_dataset.csv`, one row per AI-READI participant, by
merging five raw sources:

  1. Dexcom G6 CGM streams          -> overall + day-level glycaemic metrics
  2. OMOP clinical tables           -> demographics, HbA1c, comorbidities, MoCA, CES-D-10, PAID-5, ...
  3. LeeLab Anura home sensor       -> indoor PM2.5 / PM10 / temperature / humidity / VOC / NOx
  4. Garmin Vivosmart 5 wearable    -> steps, MVPA, sedentary time, heart rate, stress, sleep, SpO2, RR
  5. participants.tsv               -> site, study group, age, visit date

Glucose category cut-offs (mg/dL) used throughout:
  severe hypoglycaemia   < 54  (strict)
  moderate hypoglycaemia 54-69 (inclusive)
  normal / TIR           70-180 (inclusive)
  moderate hyperglycaemia 181-250 (inclusive)
  severe hyperglycaemia  > 250 (strict)

All device timestamps are stored in UTC in the raw files; they are converted to the
clinical site's local time zone before day / night aggregation.
"""

import os
import json
import warnings
from concurrent.futures import ProcessPoolExecutor, as_completed
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
CGM_DIR = os.path.join(BASE_DIR, "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
ENV_DIR = os.path.join(BASE_DIR, "environment", "environmental_sensor", "leelab_anura")
WEAR_DIR = os.path.join(BASE_DIR, "wearable_activity_monitor")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

N_WORKERS = max(1, min(8, (os.cpu_count() or 4)))

SITE_TZ = {"UW": "America/Los_Angeles", "UCSD": "America/Los_Angeles", "UAB": "America/Chicago"}

# Glucose category boundaries (mg/dL)
SEV_HYPO = 54.0
TIR_LOW = 70.0
TIR_HIGH = 180.0
SEV_HYPER = 250.0

# CGM data-sufficiency rules
READINGS_PER_DAY = 288                 # 5-min sampling
DAY_COMPLETENESS = 0.70                # a day counts if >= 70 % of expected readings are present
MIN_VALID_DAYS = 3                     # participant-level inclusion threshold (sensitivity: 7)

# Sentinel / missing codes used in the REDCap-derived OMOP tables
SENTINELS = {555.0, 777.0, 888.0, 999.0}


# --------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------
def _to_local(ts_utc, tz):
    """Vectorised UTC -> local conversion for pandas Series of ISO strings."""
    t = pd.to_datetime(ts_utc, utc=True, errors="coerce")
    return t.dt.tz_convert(ZoneInfo(tz))


def _pid_from_folder(name):
    try:
        return int(str(name).replace("AIREADI-", ""))
    except ValueError:
        return None


def _load_site_map():
    parts = pd.read_csv(os.path.join(BASE_DIR, "participants.tsv"), sep="\t")
    return dict(zip(parts["person_id"].astype(int), parts["clinical_site"].map(SITE_TZ).fillna("America/Los_Angeles")))


# --------------------------------------------------------------------------------------
# 1. CGM
# --------------------------------------------------------------------------------------
def parse_cgm(args):
    pid, folder, tz = args
    files = [f for f in os.listdir(folder) if f.endswith(".json")]
    if not files:
        return None
    try:
        with open(os.path.join(folder, files[0])) as f:
            body = json.load(f).get("body", {}).get("cgm", [])
        rows = []
        for r in body:
            bg = r.get("blood_glucose", {})
            v = bg.get("value")
            if v is None or r.get("event_type", "EGV") != "EGV":
                continue
            try:
                v = float(v)
            except (TypeError, ValueError):
                continue
            ts = r.get("effective_time_frame", {}).get("time_interval", {}).get("start_date_time")
            if ts is None:
                ts = r.get("effective_time_frame", {}).get("date_time")
            rows.append((ts, v))
        if len(rows) < READINGS_PER_DAY:
            return None
        df = pd.DataFrame(rows, columns=["ts", "glucose"])
        df["t"] = _to_local(df["ts"], tz)
        df = df.dropna(subset=["t"]).sort_values("t").drop_duplicates("t")
        # Dexcom G6 reports 40-400 mg/dL; anything else is a transmission artefact
        df = df[(df["glucose"] >= 39) & (df["glucose"] <= 401)]
        if len(df) < READINGS_PER_DAY:
            return None

        g = df["glucose"].to_numpy()
        n = len(g)
        rec = {
            "person_id": pid,
            "cgm_n_readings": n,
            "cgm_first_day": df["t"].iloc[0].date().isoformat(),
            "cgm_last_day": df["t"].iloc[-1].date().isoformat(),
            "cgm_span_days": (df["t"].iloc[-1] - df["t"].iloc[0]).total_seconds() / 86400.0,
            # ---- overall (pooled) metrics ----
            "mean_glucose": float(g.mean()),
            "glucose_sd": float(g.std(ddof=1)),
            "gmi": float(3.31 + 0.02392 * g.mean()),
            "tir_overall": float(((g >= TIR_LOW) & (g <= TIR_HIGH)).mean() * 100),
            "pct_severe_hypo": float((g < SEV_HYPO).mean() * 100),
            "pct_mod_hypo": float(((g >= SEV_HYPO) & (g < TIR_LOW)).mean() * 100),
            "pct_mod_hyper": float(((g > TIR_HIGH) & (g <= SEV_HYPER)).mean() * 100),
            "pct_severe_hyper": float((g > SEV_HYPER).mean() * 100),
        }
        rec["glucose_cv"] = rec["glucose_sd"] / rec["mean_glucose"] * 100.0
        rec["mean_to_sd_ratio"] = rec["mean_glucose"] / rec["glucose_sd"] if rec["glucose_sd"] > 0 else np.nan
        rec["tbr_below_70"] = rec["pct_severe_hypo"] + rec["pct_mod_hypo"]
        rec["tar_above_180"] = rec["pct_mod_hyper"] + rec["pct_severe_hyper"]
        # mean absolute glucose change per hour (MAG)
        dt_h = df["t"].diff().dt.total_seconds().to_numpy()[1:] / 3600.0
        dg = np.abs(np.diff(g))
        ok = (dt_h > 0) & (dt_h < 0.5)
        rec["mag_mg_dl_per_h"] = float(dg[ok].sum() / dt_h[ok].sum()) if ok.sum() > 0 else np.nan

        # ---- day-level metrics (local calendar day) ----
        df["day"] = df["t"].dt.date
        df["hour"] = df["t"].dt.hour
        daily = df.groupby("day")["glucose"].agg(
            n="size", mean="mean", sd=lambda s: s.std(ddof=1),
            tir=lambda s: ((s >= TIR_LOW) & (s <= TIR_HIGH)).mean() * 100,
            tar=lambda s: (s > TIR_HIGH).mean() * 100,
            tbr=lambda s: (s < TIR_LOW).mean() * 100,
            sev_hyper=lambda s: (s > SEV_HYPER).mean() * 100,
            rng=lambda s: s.max() - s.min(),
        )
        valid = daily[daily["n"] >= DAY_COMPLETENESS * READINGS_PER_DAY]
        rec["cgm_days_total"] = int(len(daily))
        rec["cgm_valid_days"] = int(len(valid))
        rec["cgm_completeness"] = float(n / max(1.0, rec["cgm_span_days"] * READINGS_PER_DAY))
        if len(valid) >= 1:
            rec["avg_daily_mean"] = float(valid["mean"].mean())
            rec["avg_daily_sd"] = float(valid["sd"].mean())
            rec["avg_daily_tir"] = float(valid["tir"].mean())
            rec["avg_daily_tar"] = float(valid["tar"].mean())
            rec["avg_daily_tbr"] = float(valid["tbr"].mean())
            rec["avg_daily_range"] = float(valid["rng"].mean())
            rec["sd_of_daily_means"] = float(valid["mean"].std(ddof=1)) if len(valid) > 1 else np.nan
            rec["avg_daily_mean_to_sd"] = float((valid["mean"] / valid["sd"]).replace([np.inf, -np.inf], np.nan).mean())
        # nocturnal (00:00-05:59) and daytime means
        night = df[(df["hour"] >= 0) & (df["hour"] < 6)]["glucose"]
        rec["nocturnal_mean"] = float(night.mean()) if len(night) > 50 else np.nan
        rec["nocturnal_tar"] = float((night > TIR_HIGH).mean() * 100) if len(night) > 50 else np.nan
        return rec
    except Exception as e:  # pragma: no cover
        return {"person_id": pid, "cgm_error": str(e)[:80]}


def extract_cgm(site_map):
    print("[1/5] CGM: parsing Dexcom G6 streams ...")
    tasks = []
    for name in os.listdir(CGM_DIR):
        pid = _pid_from_folder(name)
        folder = os.path.join(CGM_DIR, name)
        if pid is None or not os.path.isdir(folder):
            continue
        tasks.append((pid, folder, site_map.get(pid, "America/Los_Angeles")))
    out = []
    with ProcessPoolExecutor(N_WORKERS) as ex:
        for fut in as_completed([ex.submit(parse_cgm, t) for t in tasks]):
            r = fut.result()
            if r and "cgm_error" not in r:
                out.append(r)
    df = pd.DataFrame(out)
    print(f"      {len(df)} participants with >= 1 day of CGM; "
          f"{(df['cgm_valid_days'] >= MIN_VALID_DAYS).sum()} with >= {MIN_VALID_DAYS} valid days")
    return df


# --------------------------------------------------------------------------------------
# 2. Clinical / survey (OMOP)
# --------------------------------------------------------------------------------------
def _clean_num(s):
    s = pd.to_numeric(s, errors="coerce")
    return s.where(~s.isin(SENTINELS))


def extract_clinical():
    print("[2/5] Clinical: OMOP measurement / observation / condition tables ...")
    parts = pd.read_csv(os.path.join(BASE_DIR, "participants.tsv"), sep="\t")
    parts = parts[["person_id", "clinical_site", "study_group", "age", "study_visit_date", "recommended_split"]].copy()
    parts["visit_date"] = pd.to_datetime(parts["study_visit_date"], errors="coerce")
    parts["visit_month"] = parts["visit_date"].dt.month
    parts["visit_season"] = parts["visit_month"].map(
        {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
         6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn"})
    parts.drop(columns=["study_visit_date"], inplace=True)

    # ---- measurements ----
    meas = pd.read_csv(os.path.join(CLINICAL_DIR, "measurement.csv"),
                       usecols=["person_id", "measurement_source_value", "value_as_number"], low_memory=False)
    meas["key"] = meas["measurement_source_value"].astype(str).str.split(",").str[0].str.strip()
    meas["value_as_number"] = _clean_num(meas["value_as_number"])

    def take(key, agg="mean", newname=None):
        sub = meas[meas["key"] == key].dropna(subset=["value_as_number"])
        return sub.groupby("person_id")["value_as_number"].agg(agg).rename(newname or key)

    clin = parts.set_index("person_id")
    clin = clin.join(take("bmi_vsorres", "mean", "bmi"))
    clin = clin.join(take("waist_vsorres", "mean", "waist_cm"))
    clin = clin.join(take("bp1_sysbp_vsorres", "mean", "systolic_bp"))
    clin = clin.join(take("import_hba1c", "mean", "hba1c"))
    clin = clin.join(take("import_glucose", "mean", "fasting_glucose_lab"))
    clin = clin.join(take("import_crp_hs", "mean", "crp_hs"))
    clin = clin.join(take("import_creatinine", "mean", "creatinine"))
    clin = clin.join(take("import_ldl_cholesterol", "mean", "ldl"))
    # red-cell indices (note: the OMOP label `lbscat_a1c` is haemoglobin in g/dL, NOT HbA1c)
    clin = clin.join(take("lbscat_a1c", "mean", "hemoglobin_g_dl"))
    clin = clin.join(take("lbscat_mcv", "mean", "mcv_fl"))
    clin = clin.join(take("lbscat_rdw", "mean", "rdw_pct"))
    clin = clin.join(take("lbscat_hct", "mean", "hematocrit_pct"))
    clin = clin.join(take("import_c_peptide", "mean", "c_peptide"))
    clin = clin.join(take("moca_total_score", "max", "moca_total"))
    clin = clin.join(take("moca_combined_mis_score", "max", "moca_memory_index"))
    clin = clin.join(take("moca_orientation", "max", "moca_orientation"))
    clin = clin.join(take("moca_abstraction", "max", "moca_abstraction"))
    clin = clin.join(take("delayed_recall_with_no_clue", "max", "moca_delayed_recall"))
    clin = clin.join(take("trails_visuospatial_executive", "max", "moca_trails"))
    clin = clin.join(take("digitspan", "max", "moca_digitspan"))
    clin = clin.join(take("fluency_language", "max", "moca_fluency"))
    clin = clin.join(take("naming", "max", "moca_naming"))
    clin = clin.join(take("plcsodlog", "mean", "contrast_sens_od"))

    # ---- observations ----
    obs = pd.read_csv(os.path.join(CLINICAL_DIR, "observation.csv"),
                      usecols=["person_id", "observation_source_value", "value_as_number", "value_as_string"],
                      low_memory=False)
    obs["key"] = obs["observation_source_value"].astype(str).str.split(",").str[0].str.strip()
    obs["num"] = _clean_num(obs["value_as_number"])

    def obs_take(key, agg="max", newname=None):
        sub = obs[obs["key"] == key].dropna(subset=["num"])
        return sub.groupby("person_id")["num"].agg(agg).rename(newname or key)

    clin = clin.join(obs_take("years_of_education", "max"))
    clin = clin.join(obs_take("cestl", "max", "cesd10_total"))
    for i in range(1, 11):
        clin = clin.join(obs_take(f"ces{i}", "max", f"cesd_item{i}"))
    clin = clin.join(obs_take("paidscore", "max", "paid5_total"))
    clin = clin.join(obs_take("dietscore", "max", "diet_score_raw"))
    clin = clin.join(obs_take("cmtrt_insln", "max", "insulin_use"))
    clin = clin.join(obs_take("cmtrt_a1c", "max", "oral_glucose_meds"))
    clin = clin.join(obs_take("cmtrt_glcs", "max", "other_glucose_injectables"))
    clin = clin.join(obs_take("susmkncf", "max", "ever_smoked_100"))
    clin = clin.join(obs_take("susmkcdur", "max", "current_smoker_raw"))
    clin = clin.join(obs_take("sualckncf", "max", "ever_alcohol"))
    clin = clin.join(obs_take("cm_slp", "max", "sleeping_pills_2wk_raw"))
    clin = clin.join(obs_take("mh_dm_age", "max", "diabetes_dx_age"))
    clin = clin.join(obs_take("dmlvex", "max", "self_report_vigorous_exercise"))
    clin = clin.join(obs_take("dmlact", "max", "self_report_activity_level"))
    clin = clin.join(obs_take("pxfi1", "max", "food_insecurity_item1"))
    clin = clin.join(obs_take("pxhi1", "max", "housing_situation"))
    clin = clin.join(obs_take("mhoccur_fall", "max", "fell_last_12mo"))
    clin = clin.join(obs_take("cage", "max", "age_survey"))

    # derived survey variables
    clin["current_smoker"] = np.where(clin["ever_smoked_100"] == 1,
                                      (clin["current_smoker_raw"] == 1).astype(float), 0.0)
    clin.loc[clin["ever_smoked_100"].isna(), "current_smoker"] = np.nan
    clin["sleeping_pills_2wk"] = (clin["sleeping_pills_2wk_raw"].fillna(0) > 0).astype(float)
    clin.loc[clin["sleeping_pills_2wk_raw"].isna(), "sleeping_pills_2wk"] = np.nan
    clin["insulin_use"] = clin["insulin_use"].fillna(0.0)          # not asked of non-diabetic participants
    clin["oral_glucose_meds"] = clin["oral_glucose_meds"].fillna(0.0)
    clin["cesd10_ge10"] = (clin["cesd10_total"] >= 10).astype(float)
    clin.loc[clin["cesd10_total"].isna(), "cesd10_ge10"] = np.nan
    clin["cognitive_impairment"] = (clin["moca_total"] < 26).astype(float)
    clin.loc[clin["moca_total"].isna(), "cognitive_impairment"] = np.nan
    clin["moca_education_adj"] = clin["moca_total"] + np.where(clin["years_of_education"] <= 12, 1, 0)
    clin.loc[clin["moca_total"].isna(), "moca_education_adj"] = np.nan
    clin["food_insecure"] = clin["food_insecurity_item1"].isin([1, 2]).astype(float)
    clin.loc[clin["food_insecurity_item1"].isna(), "food_insecure"] = np.nan

    def map_edu(y):
        if pd.isna(y):
            return np.nan
        if y <= 12:
            return "High school or below"
        if y <= 16:
            return "College level"
        return "Graduate level"
    clin["education_level"] = clin["years_of_education"].apply(map_edu)

    # ---- conditions (self-reported medical history) ----
    cond = pd.read_csv(os.path.join(CLINICAL_DIR, "condition_occurrence.csv"),
                       usecols=["person_id", "condition_source_value"], low_memory=False)
    cond["key"] = cond["condition_source_value"].astype(str).str.split(",").str[0].str.strip()
    has = cond.groupby("key")["person_id"].apply(set).to_dict()

    def flag(keys):
        ids = set()
        for k in keys:
            ids |= has.get(k, set())
        return clin.index.to_series().isin(ids).astype(int)

    clin["hypertension"] = flag(["mhoccur_hbp"])
    clin["high_cholesterol"] = flag(["mhoccur_clsh"])
    clin["kidney_disease"] = flag(["mhoccur_rnl"])
    clin["circulatory_problems"] = flag(["mhoccur_circ", "mhoccur_strk", "mhoccur_mi"])
    clin["cardiovascular_any"] = flag(["mhoccur_circ", "mhoccur_strk", "mhoccur_mi", "mhoccur_cvdot"])
    clin["neurodegenerative"] = flag(["mhoccur_pd", "mhoccur_ad", "mhoccur_cogn", "mhoccur_ms", "mhoccur_cns"])
    clin["pulmonary_disease"] = flag(["mhoccur_plm"])
    clin["arthritis"] = flag(["mhoccur_ra"])
    clin["cancer"] = flag(["mhoccur_ca"])
    clin["diabetic_retinopathy"] = flag(["mhoccur_pdr"])
    clin["obesity_dx"] = flag(["mhoccur_obs"])
    clin["hearing_impairment"] = flag(["mhoccur_ear"])
    clin["type2_diabetes_dx"] = flag(["mhterm_dm2"])
    clin["prediabetes_dx"] = flag(["mhterm_predm"])
    clin["comorbidity_count"] = clin[["hypertension", "high_cholesterol", "kidney_disease",
                                     "cardiovascular_any", "pulmonary_disease", "arthritis", "cancer"]].sum(axis=1)

    clin["diabetes_status"] = clin["study_group"].map({
        "healthy": "No diabetes",
        "pre_diabetes_lifestyle_controlled": "Pre-diabetes / lifestyle",
        "oral_medication_and_or_non_insulin_injectable_medication_controlled": "T2D non-insulin",
        "insulin_dependent": "T2D insulin"})
    clin["any_diabetes"] = clin["study_group"].isin(
        ["oral_medication_and_or_non_insulin_injectable_medication_controlled", "insulin_dependent"]).astype(int)
    clin = clin.reset_index()
    print(f"      {len(clin)} participants; HbA1c available for {clin['hba1c'].notna().sum()}, "
          f"MoCA {clin['moca_total'].notna().sum()}, CES-D-10 {clin['cesd10_total'].notna().sum()}")
    return clin


# --------------------------------------------------------------------------------------
# 3. Environmental sensor
# --------------------------------------------------------------------------------------
ENV_COLS = ["ts", "pm1", "pm2.5", "pm10", "hum", "temp", "voc", "nox", "screen"]


def parse_env(args):
    pid, folder, tz = args
    files = [f for f in os.listdir(folder) if f.endswith(".csv")]
    if not files:
        return None
    try:
        df = pd.read_csv(os.path.join(folder, files[0]), comment="#", usecols=lambda c: c.strip() in ENV_COLS)
        df.columns = [c.strip() for c in df.columns]
        df["t"] = _to_local(df["ts"], tz)
        df = df.dropna(subset=["t"]).sort_values("t")
        for c in ["pm1", "pm2.5", "pm10", "hum", "temp", "voc", "nox", "screen"]:
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors="coerce")
        # physical plausibility filters (sensor spec ranges; 65535 = uint16 sentinel)
        df.loc[(df["temp"] < -10) | (df["temp"] > 50), "temp"] = np.nan
        df.loc[(df["hum"] < 0) | (df["hum"] > 100), "hum"] = np.nan
        for c in ["pm1", "pm2.5", "pm10"]:
            df.loc[(df[c] < 0) | (df[c] >= 5000), c] = np.nan
        # VOC / NOx index: 1-500 valid; 0 = sensor warm-up
        for c in ["voc", "nox"]:
            df.loc[(df[c] < 1) | (df[c] > 500), c] = np.nan
        # aggregate to 1-minute means to remove the 5-s micro-structure before summarising
        m = df.set_index("t")[["pm1", "pm2.5", "pm10", "hum", "temp", "voc", "nox"]].resample("1min").mean()
        m = m.dropna(how="all")
        if len(m) < 60:
            return None
        hours = len(m) / 60.0
        hr = m.index.hour
        night = (hr >= 22) | (hr < 6)
        rec = {
            "person_id": pid,
            "env_hours": hours,
            "env_days": hours / 24.0,
            "env_first_day": m.index[0].date().isoformat(),
            "env_last_day": m.index[-1].date().isoformat(),
            "env_pm25_mean": m["pm2.5"].mean(),
            "env_pm25_median": m["pm2.5"].median(),
            "env_pm25_p95": m["pm2.5"].quantile(0.95),
            "env_pm25_pct_gt15": (m["pm2.5"] > 15).mean() * 100,     # WHO 2021 24-h guideline
            "env_pm25_pct_gt35": (m["pm2.5"] > 35).mean() * 100,     # US EPA 24-h standard
            "env_pm10_mean": m["pm10"].mean(),
            "env_pm10_median": m["pm10"].median(),
            "env_pm1_mean": m["pm1"].mean(),
            "env_temp_mean": m["temp"].mean(),
            "env_temp_sd": m["temp"].std(),
            "env_temp_night_mean": m.loc[night, "temp"].mean(),
            "env_temp_pct_lt18": (m["temp"] < 18).mean() * 100,      # WHO cold-home threshold
            "env_temp_pct_gt26": (m["temp"] > 26).mean() * 100,
            "env_hum_mean": m["hum"].mean(),
            "env_hum_sd": m["hum"].std(),
            "env_hum_pct_gt60": (m["hum"] > 60).mean() * 100,        # mould / dust-mite risk band
            "env_hum_pct_lt30": (m["hum"] < 30).mean() * 100,
            "env_voc_mean": m["voc"].mean(),
            "env_voc_median": m["voc"].median(),
            "env_voc_pct_gt250": (m["voc"] > 250).mean() * 100,
            "env_nox_mean": m["nox"].mean(),
            "env_nox_median": m["nox"].median(),
            "env_nox_pct_gt20": (m["nox"] > 20).mean() * 100,
        }
        # daily-mean based variability of PM2.5 (captures episodic cooking / smoking events)
        daily = m["pm2.5"].resample("1D").mean().dropna()
        rec["env_pm25_daily_max"] = daily.max() if len(daily) else np.nan
        return rec
    except Exception as e:  # pragma: no cover
        return {"person_id": pid, "env_error": str(e)[:80]}


def extract_env(site_map):
    print("[3/5] Environment: parsing LeeLab Anura sensor CSVs (full files) ...")
    if not os.path.exists(ENV_DIR):
        return pd.DataFrame()
    tasks = []
    for name in os.listdir(ENV_DIR):
        pid = _pid_from_folder(name)
        folder = os.path.join(ENV_DIR, name)
        if pid is None or not os.path.isdir(folder):
            continue
        tasks.append((pid, folder, site_map.get(pid, "America/Los_Angeles")))
    out, errs = [], 0
    with ProcessPoolExecutor(N_WORKERS) as ex:
        for fut in as_completed([ex.submit(parse_env, t) for t in tasks]):
            r = fut.result()
            if r is None:
                continue
            if "env_error" in r:
                errs += 1
                continue
            out.append(r)
    df = pd.DataFrame(out)
    print(f"      {len(df)} participants with sensor data ({errs} parse errors)")
    return df


# --------------------------------------------------------------------------------------
# 4. Wearable (Garmin Vivosmart 5)
# --------------------------------------------------------------------------------------
def _load_json_list(domain, pid, key):
    folder = os.path.join(WEAR_DIR, domain, "garmin_vivosmart5", str(pid))
    if not os.path.isdir(folder):
        return None
    files = [f for f in os.listdir(folder) if f.endswith(".json")]
    if not files:
        return None
    with open(os.path.join(folder, files[0])) as f:
        return json.load(f).get("body", {}).get(key, [])


def parse_wearable(args):
    pid, tz = args
    rec = {"person_id": pid}
    try:
        # ---------------- heart rate: defines "wear days" ----------------
        hr = _load_json_list("heart_rate", pid, "heart_rate")
        wear_days = set()
        if hr:
            h = pd.DataFrame({
                "ts": [r.get("effective_time_frame", {}).get("date_time") for r in hr],
                "v": [r.get("heart_rate", {}).get("value") for r in hr]})
            h["v"] = pd.to_numeric(h["v"], errors="coerce")
            h["t"] = _to_local(h["ts"], tz)
            h = h.dropna(subset=["t"])
            h = h[(h["v"] >= 30) & (h["v"] <= 220)]           # 0 = no contact
            if len(h):
                h["day"] = h["t"].dt.date
                h["hour"] = h["t"].dt.hour
                per_day = h.groupby("day").agg(n=("v", "size"), hours=("hour", "nunique"),
                                               mean=("v", "mean"), p05=("v", lambda s: s.quantile(0.05)))
                # drop the (partial) first and last calendar days, then require >= 10 h of contact
                if len(per_day) > 2:
                    per_day = per_day.iloc[1:-1]
                good = per_day[per_day["hours"] >= 10]
                wear_days = set(good.index)
                rec["wear_days_hr"] = int(len(good))
                if len(good):
                    rec["hr_mean"] = float(good["mean"].mean())
                    rec["hr_resting_proxy"] = float(good["p05"].mean())
                    night = h[(h["hour"] >= 0) & (h["hour"] < 5) & (h["day"].isin(wear_days))]
                    rec["hr_night_mean"] = float(night["v"].mean()) if len(night) > 30 else np.nan

        # ---------------- steps / activity intervals ----------------
        acts = _load_json_list("physical_activity", pid, "activity")
        if acts:
            a = pd.DataFrame({
                "name": [r.get("activity_name") for r in acts],
                "steps": [r.get("base_movement_quantity", {}).get("value") for r in acts],
                "s": [r.get("effective_time_frame", {}).get("time_interval", {}).get("start_date_time") for r in acts],
                "e": [r.get("effective_time_frame", {}).get("time_interval", {}).get("end_date_time") for r in acts]})
            a["steps"] = pd.to_numeric(a["steps"], errors="coerce")
            a["ts"] = _to_local(a["s"], tz)
            a["te"] = _to_local(a["e"], tz)
            a = a.dropna(subset=["ts", "te"])
            a["dur_min"] = (a["te"] - a["ts"]).dt.total_seconds() / 60.0
            a = a[(a["dur_min"] >= 0) & (a["dur_min"] <= 24 * 60)]
            a["day"] = a["ts"].dt.date
            a["cadence"] = a["steps"] / a["dur_min"].replace(0, np.nan)
            a["active"] = (a["name"] != "sedentary") * a["dur_min"]                 # any non-sedentary epoch
            a["mvpa"] = ((a["cadence"] >= 100) & (a["name"] != "sedentary")) * a["dur_min"]  # >=100 steps/min ~ moderate intensity
            a["sed"] = (a["name"] == "sedentary") * a["dur_min"]
            days = a.groupby("day").agg(steps=("steps", "sum"), mvpa=("mvpa", "sum"), active=("active", "sum"),
                                        sed=("sed", "sum"), total=("dur_min", "sum"))
            if wear_days:
                days = days[days.index.isin(wear_days)]
            else:  # fall back: full days with >= 12 h of labelled intervals
                days = days[days["total"] >= 12 * 60]
            # a wear-day with zero recorded steps means the device was not worn / not counting
            days = days[days["steps"] > 0]
            if len(days) >= 2:
                rec["wear_days_activity"] = int(len(days))
                rec["steps_per_day"] = float(days["steps"].mean())
                rec["mvpa_min_per_day"] = float(days["mvpa"].mean())
                rec["active_min_per_day"] = float(days["active"].mean())
                rec["sedentary_pct"] = float((days["sed"].sum() / max(1.0, days["total"].sum())) * 100)
                rec["steps_cv_between_days"] = float(days["steps"].std(ddof=1) / days["steps"].mean() * 100) \
                    if len(days) > 1 and days["steps"].mean() > 0 else np.nan

        # ---------------- active calories ----------------
        cal = _load_json_list("physical_activity_calorie", pid, "activity")
        if cal:
            c = pd.DataFrame({
                "v": [r.get("calories_value", {}).get("value") for r in cal],
                "ts": [r.get("effective_time_frame", {}).get("date_time") for r in cal]})
            c["v"] = pd.to_numeric(c["v"], errors="coerce")
            c["t"] = _to_local(c["ts"], tz)
            c = c.dropna(subset=["t", "v"]).sort_values("t")
            c["day"] = c["t"].dt.date
            # the Garmin export interleaves a running daily cumulative total with small
            # per-bout increments, so the daily active-kcal total is the daily maximum
            days = c.groupby("day")["v"].max()
            if wear_days:
                days = days[days.index.isin(wear_days)]
            if len(days):
                rec["active_kcal_per_day"] = float(days.mean())

        # ---------------- stress (Garmin: -1 = insufficient data, -2 = too active) ----------------
        st = _load_json_list("stress", pid, "stress")
        if st:
            s = pd.DataFrame({
                "v": [r.get("stress", {}).get("value") for r in st],
                "ts": [r.get("effective_time_frame", {}).get("date_time") for r in st]})
            s["v"] = pd.to_numeric(s["v"], errors="coerce")
            s["t"] = _to_local(s["ts"], tz)
            s = s.dropna(subset=["t"])
            s["day"] = s["t"].dt.date
            if wear_days:
                s = s[s["day"].isin(wear_days)]
            valid = s[(s["v"] >= 0) & (s["v"] <= 100)]
            if len(valid) > 100:
                rec["stress_mean"] = float(valid["v"].mean())
                rec["stress_pct_high"] = float((valid["v"] > 50).mean() * 100)   # Garmin "high stress" band
                rec["stress_pct_rest"] = float((valid["v"] <= 25).mean() * 100)
                rec["stress_valid_frac"] = float(len(valid) / len(s))

        # ---------------- sleep stages ----------------
        sl = _load_json_list("sleep", pid, "sleep")
        if sl:
            z = pd.DataFrame({
                "stage": [r.get("sleep_stage_state") for r in sl],
                "s": [r.get("effective_time_frame", {}).get("time_interval", {}).get("start_date_time") for r in sl],
                "e": [r.get("effective_time_frame", {}).get("time_interval", {}).get("end_date_time") for r in sl]})
            z["ts"] = _to_local(z["s"], tz)
            z["te"] = _to_local(z["e"], tz)
            z = z.dropna(subset=["ts", "te"])
            z["dur"] = (z["te"] - z["ts"]).dt.total_seconds() / 60.0
            z = z[(z["dur"] > 0) & (z["dur"] <= 12 * 60)]
            # the export contains exact duplicate stage intervals -> keep one copy
            z = z.drop_duplicates(subset=["ts", "te", "stage"]).sort_values("ts")
            # remove residual overlaps (interval starting before the previous one ended)
            z = z[~(z["ts"] < z["te"].shift())]
            # assign each interval to a "night" = date of (start - 12h)
            z["night"] = (z["ts"] - pd.Timedelta(hours=12)).dt.date
            z["asleep"] = z["stage"].isin(["light", "deep", "rem"]) * z["dur"]
            z["deep"] = (z["stage"] == "deep") * z["dur"]
            z["rem"] = (z["stage"] == "rem") * z["dur"]
            z["awake"] = (z["stage"] == "awake") * z["dur"]
            # hours since local noon of the night-date for onset / offset / midpoint
            noon = pd.to_datetime(z["night"].astype(str)) + pd.Timedelta(hours=12)
            noon = noon.dt.tz_localize(z["ts"].dt.tz, nonexistent="shift_forward", ambiguous="NaT")
            z["onset_h"] = (z["ts"].dt.tz_convert("UTC") - noon.dt.tz_convert("UTC")).dt.total_seconds() / 3600.0
            z["offset_h"] = (z["te"].dt.tz_convert("UTC") - noon.dt.tz_convert("UTC")).dt.total_seconds() / 3600.0
            nights = z.groupby("night").agg(tst=("asleep", "sum"), deep=("deep", "sum"),
                                            rem=("rem", "sum"), awake=("awake", "sum"),
                                            onset=("onset_h", "min"), offset=("offset_h", "max"))
            nights["midpoint"] = (nights["onset"] + nights["offset"]) / 2.0
            nights = nights[(nights["tst"] >= 120) & (nights["tst"] <= 16 * 60)]   # drop fragments (< 2 h) and artefacts (> 16 h)
            if len(nights) >= 2:
                rec["sleep_nights"] = int(len(nights))
                rec["sleep_tst_min"] = float(nights["tst"].mean())
                rec["sleep_efficiency_pct"] = float((nights["tst"] / (nights["tst"] + nights["awake"])).mean() * 100)
                rec["sleep_deep_pct"] = float((nights["deep"] / nights["tst"]).mean() * 100)
                rec["sleep_rem_pct"] = float((nights["rem"] / nights["tst"]).mean() * 100)
                rec["sleep_tst_sd_min"] = float(nights["tst"].std(ddof=1))
                rec["sleep_onset_sd_h"] = float(nights["onset"].std(ddof=1))
                rec["sleep_midpoint_sd_h"] = float(nights["midpoint"].std(ddof=1))
                rec["sleep_midpoint_mean_h"] = float(nights["midpoint"].mean())      # hours after local noon (e.g. 15 = 03:00)
                rec["sleep_onset_mean_h"] = float(nights["onset"].mean())

        # ---------------- SpO2 ----------------
        ox = _load_json_list("oxygen_saturation", pid, "breathing")
        if ox:
            o = pd.to_numeric(pd.Series([r.get("oxygen_saturation", {}).get("value") for r in ox]), errors="coerce")
            o = o[(o >= 70) & (o <= 100)]
            if len(o) > 30:
                rec["spo2_mean"] = float(o.mean())
                rec["spo2_pct_lt90"] = float((o < 90).mean() * 100)

        # ---------------- respiratory rate ----------------
        rr = _load_json_list("respiratory_rate", pid, "breathing")
        if rr:
            r_ = pd.to_numeric(pd.Series([r.get("respiratory_rate", {}).get("value") for r in rr]), errors="coerce")
            r_ = r_[(r_ >= 4) & (r_ <= 40)]
            if len(r_) > 100:
                rec["resp_rate_mean"] = float(r_.mean())
        return rec
    except Exception as e:  # pragma: no cover
        rec["wear_error"] = str(e)[:80]
        return rec


def extract_wearable(site_map):
    print("[4/5] Wearable: parsing Garmin Vivosmart 5 JSON streams ...")
    pids = set()
    for dom in ["heart_rate", "physical_activity", "stress", "sleep"]:
        d = os.path.join(WEAR_DIR, dom, "garmin_vivosmart5")
        if os.path.isdir(d):
            for name in os.listdir(d):
                pid = _pid_from_folder(name)
                if pid is not None and os.path.isdir(os.path.join(d, name)):
                    pids.add(pid)
    tasks = [(pid, site_map.get(pid, "America/Los_Angeles")) for pid in sorted(pids)]
    out, errs = [], 0
    with ProcessPoolExecutor(N_WORKERS) as ex:
        for fut in as_completed([ex.submit(parse_wearable, t) for t in tasks]):
            r = fut.result()
            if r is None:
                continue
            if "wear_error" in r:
                errs += 1
                r.pop("wear_error")
            out.append(r)
    df = pd.DataFrame(out)
    print(f"      {len(df)} participants with wearable data ({errs} partial parse errors); "
          f"steps available for {df['steps_per_day'].notna().sum() if 'steps_per_day' in df else 0}")
    return df


# --------------------------------------------------------------------------------------
# 5. merge
# --------------------------------------------------------------------------------------
def main():
    site_map = _load_site_map()
    clin = extract_clinical()
    cgm = extract_cgm(site_map)
    env = extract_env(site_map)
    wear = extract_wearable(site_map)

    print("[5/5] Merging ...")
    df = clin.merge(cgm, on="person_id", how="left")
    if not env.empty:
        df = df.merge(env, on="person_id", how="left")
    if not wear.empty:
        df = df.merge(wear, on="person_id", how="left")

    df["has_cgm"] = df["cgm_valid_days"].fillna(0).ge(MIN_VALID_DAYS).astype(int)
    df["has_env"] = df["env_days"].fillna(0).ge(3).astype(int) if "env_days" in df else 0
    df["has_wearable"] = df["wear_days_hr"].fillna(0).ge(3).astype(int) if "wear_days_hr" in df else 0
    df["log_pm25_mean"] = np.log1p(df["env_pm25_mean"]) if "env_pm25_mean" in df else np.nan

    out = os.path.join(DATA_DIR, "master_multimodal_dataset.csv")
    df.to_csv(out, index=False)
    print(f"Saved {out}: {len(df)} rows x {df.shape[1]} columns")
    print("Coverage: CGM>=3 valid days:", int(df["has_cgm"].sum()),
          "| env>=3 days:", int(df["has_env"].sum()),
          "| wearable>=3 wear-days:", int(df["has_wearable"].sum()),
          "| HbA1c:", int(df["hba1c"].notna().sum()))


if __name__ == "__main__":
    main()
