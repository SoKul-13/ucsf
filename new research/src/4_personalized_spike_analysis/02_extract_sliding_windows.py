import os
import json
import glob
import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count

# Set paths relative to new research structure
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
WORKSPACE_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, ".."))
CGM_DIR = os.path.join(WORKSPACE_ROOT, "dataset", "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
CLINICAL_EXT_PATH = os.path.join(PROJECT_ROOT, "data", "master_extended_dataset.csv")

REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "4_personalized_spike_analysis")
DATA_OUT_DIR = os.path.join(REPORTS_DIR, "data")
MASTER_DATA_DIR = os.path.join(PROJECT_ROOT, "data")

os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(MASTER_DATA_DIR, exist_ok=True)

def parse_glucose_val(raw_val):
    if raw_val is None:
        return None
    if isinstance(raw_val, (int, float)):
        return float(raw_val)
    val_str = str(raw_val).strip()
    if val_str.lower() == 'high':
        return 400.0
    if val_str.lower() == 'low':
        return 40.0
    try:
        return float(val_str)
    except ValueError:
        return None

def process_single_patient(args):
    pdir, person_meta, stride_minutes = args
    pid = int(pdir.replace('AIREADI-', '')) if 'AIREADI-' in pdir else int(pdir)
    if pid not in person_meta:
        return []
        
    p_info = person_meta[pid]
    json_files = glob.glob(os.path.join(CGM_DIR, pdir, "*.json"))
    if not json_files:
        return []
        
    try:
        with open(json_files[0], 'r') as f:
            data = json.load(f)
        readings = data.get('body', {}).get('cgm', [])
        if not readings:
            return []
            
        records = []
        for r in readings:
            v = parse_glucose_val(r.get('blood_glucose', {}).get('value'))
            t_str = r.get('effective_time_frame', {}).get('time_interval', {}).get('start_date_time') or r.get('effective_time_frame', {}).get('time_interval', {}).get('start_time') or r.get('start_time')
            if v is not None and t_str is not None:
                records.append({'time': pd.to_datetime(t_str), 'glucose': v})
                
        if len(records) < 864:
            return []
            
        df_p = pd.DataFrame(records).sort_values('time').drop_duplicates(subset=['time']).reset_index(drop=True)
        
        # Resample to 5-minute grid
        df_p.set_index('time', inplace=True)
        df_p = df_p.resample('5min').mean()
        df_p['glucose'] = df_p['glucose'].interpolate(method='linear', limit=3)
        df_p.dropna(subset=['glucose'], inplace=True)
        
        g_vals = df_p['glucose'].values
        times = df_p.index
        n_len = len(g_vals)
        if n_len < 30:
            return []
            
        p_mean = float(np.mean(g_vals))
        p_sd = float(np.std(g_vals, ddof=1)) if n_len > 1 else 1.0
        p_sd = max(p_sd, 0.001)
        thresh_2sd = p_mean + 2.0 * p_sd
        
        stride_steps = max(1, stride_minutes // 5)
        samples = []
        
        for t_idx in range(12, n_len - 12, stride_steps):
            hist_window = g_vals[t_idx-12:t_idx+1]
            t_curr = times[t_idx]
            
            g_curr = float(hist_window[-1])
            g_lag5 = float(hist_window[-2])
            g_lag10 = float(hist_window[-3])
            g_lag15 = float(hist_window[-4])
            g_lag30 = float(hist_window[-7])
            g_lag60 = float(hist_window[0])
            
            vel_15 = (g_curr - g_lag15) / 15.0
            vel_30 = (g_curr - g_lag30) / 30.0
            vel_60 = (g_curr - g_lag60) / 60.0
            acc_15 = (vel_15 - ((g_lag15 - float(hist_window[-7])) / 15.0)) / 15.0
            
            roll_mean_30 = float(np.mean(hist_window[-7:]))
            roll_std_30 = float(np.std(hist_window[-7:], ddof=1)) if len(hist_window[-7:]) > 1 else 0.0
            roll_min_30 = float(np.min(hist_window[-7:]))
            roll_max_30 = float(np.max(hist_window[-7:]))
            
            roll_mean_60 = float(np.mean(hist_window))
            roll_std_60 = float(np.std(hist_window, ddof=1))
            roll_min_60 = float(np.min(hist_window))
            roll_max_60 = float(np.max(hist_window))
            
            hour = t_curr.hour
            dow = t_curr.dayofweek
            is_weekend = int(dow in [5, 6])
            sin_hour = float(np.sin(2 * np.pi * hour / 24.0))
            cos_hour = float(np.cos(2 * np.pi * hour / 24.0))
            
            fut_15 = g_vals[t_idx+1:t_idx+4]
            fut_30 = g_vals[t_idx+1:t_idx+7]
            fut_60 = g_vals[t_idx+1:t_idx+13]
            
            max_15 = float(np.max(fut_15)) if len(fut_15) > 0 else g_curr
            max_30 = float(np.max(fut_30)) if len(fut_30) > 0 else g_curr
            max_60 = float(np.max(fut_60)) if len(fut_60) > 0 else g_curr
            
            samples.append({
                'person_id': pid,
                'time': t_curr,
                'g_current': g_curr,
                'z_current': (g_curr - p_mean) / p_sd,
                'g_lag5': g_lag5,
                'g_lag10': g_lag10,
                'g_lag15': g_lag15,
                'g_lag30': g_lag30,
                'g_lag60': g_lag60,
                'vel_15': vel_15,
                'vel_30': vel_30,
                'vel_60': vel_60,
                'acc_15': acc_15,
                'roll_mean_30': roll_mean_30,
                'roll_std_30': roll_std_30,
                'roll_min_30': roll_min_30,
                'roll_max_30': roll_max_30,
                'roll_mean_60': roll_mean_60,
                'roll_std_60': roll_std_60,
                'roll_min_60': roll_min_60,
                'roll_max_60': roll_max_60,
                'hour': hour,
                'day_of_week': dow,
                'is_weekend': is_weekend,
                'sin_hour': sin_hour,
                'cos_hour': cos_hour,
                'patient_mean': p_mean,
                'patient_sd': p_sd,
                'age': p_info.get('age', 60),
                'bmi': p_info.get('bmi', 28.0),
                'years_of_education': p_info.get('years_of_education', 14.0),
                'is_diabetic': p_info.get('is_diabetic', 0),
                'target_140_15m': int(max_15 >= 140.0),
                'target_140_30m': int(max_30 >= 140.0),
                'target_140_60m': int(max_60 >= 140.0),
                'target_2sd_15m': int(max_15 >= thresh_2sd),
                'target_2sd_30m': int(max_30 >= thresh_2sd),
                'target_2sd_60m': int(max_60 >= thresh_2sd),
            })
        return samples
    except Exception as e:
        return []

def build_sliding_window_dataset_parallel(stride_minutes=30):
    print(f"Parallel extracting sliding window features (stride={stride_minutes} mins)...")
    df_ext = pd.read_csv(CLINICAL_EXT_PATH)
    def is_diabetic_fn(sg):
        sg_l = str(sg).lower()
        if 'oral' in sg_l or 'insulin' in sg_l:
            return 1
        return 0
    df_ext['is_diabetic'] = df_ext['study_group'].apply(is_diabetic_fn)
    person_meta = df_ext.set_index('person_id').to_dict(orient='index')
    
    person_dirs = [d for d in os.listdir(CGM_DIR) if os.path.isdir(os.path.join(CGM_DIR, d))]
    tasks = [(pdir, person_meta, stride_minutes) for pdir in person_dirs]
    
    n_workers = min(cpu_count(), 8)
    print(f"Using {n_workers} CPU workers for parallel extraction...")
    
    with Pool(n_workers) as pool:
        results = pool.map(process_single_patient, tasks)
        
    all_window_samples = [item for sublist in results for item in sublist]
    df_windows = pd.DataFrame(all_window_samples)
    print(f"Extracted {len(df_windows)} sliding window samples across {df_windows['person_id'].nunique()} patients.")
    
    out_parquet = os.path.join(DATA_OUT_DIR, "cgm_sliding_window_features.parquet")
    df_windows.to_parquet(out_parquet, index=False)
    print(f"Saved sliding window features to {out_parquet}")
    return df_windows

if __name__ == "__main__":
    build_sliding_window_dataset_parallel(stride_minutes=30)
