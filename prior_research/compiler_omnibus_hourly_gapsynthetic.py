import pandas as pd
import json
import glob
import os
import numpy as np

# --- CONFIGURATION ---
BASE_PATH = os.path.abspath("../dataset") 
OUTPUT_FOLDER = os.path.abspath("../output_omnibus_hourly")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# --- 1. STATIC METADATA EXTRACTORS ---

def get_clinical_conditions(p_str):
    files = glob.glob(os.path.join(BASE_PATH, "clinical_data", "**", "condition_occurrence.csv"), recursive=True)
    if files:
        try:
            df = pd.read_csv(files[0], low_memory=False)
            p_conds = df[df['person_id'].astype(str) == p_str]
            if not p_conds.empty and 'condition_source_value' in p_conds.columns:
                return " | ".join(p_conds['condition_source_value'].dropna().astype(str).unique())
        except: pass
    return None

def get_cardiac_metrics(p_str):
    files = glob.glob(os.path.join(BASE_PATH, "cardiac_ecg", "**", f"*{p_str}*.hea"), recursive=True)
    metrics = {}
    if files:
        try:
            with open(files[0], 'r') as file:
                file_text = file.read()
                if f"participant_id: {p_str}" in file_text:
                    file.seek(0)
                    for line in file:
                        if line.startswith('#'):
                            parts = line.strip().lstrip('# ').split(':', 1)
                            if len(parts) == 2:
                                k, v = parts[0].strip(), parts[1].strip()
                                if k in ['Rate', 'PR', 'QRSD', 'QT', 'QTc', 'P', 'QRS', 'T']:
                                    try: metrics[f"ecg_{k}"] = float(v)
                                    except ValueError: metrics[f"ecg_{k}"] = v
        except: pass
    return metrics

def get_env_location(p_str):
    files = glob.glob(os.path.join(BASE_PATH, "environment", "**", "manifest.tsv"), recursive=True)
    if files:
        try:
            df = pd.read_csv(files[0], sep='\t', low_memory=False)
            p_data = df[df['person_id'].astype(str) == p_str]
            if not p_data.empty and 'sensor_location' in p_data.columns:
                return p_data.iloc[0]['sensor_location']
        except: pass
    return None

def get_wearable_metadata(p_str):
    files = glob.glob(os.path.join(BASE_PATH, "wearable_activity_monitor", "**", "manifest.tsv"), recursive=True)
    meta = {}
    if files:
        try:
            df = pd.read_csv(files[0], sep='\t', low_memory=False)
            p_data = df[df['person_id'].astype(str) == p_str]
            if not p_data.empty:
                if 'wrist_worn_on' in p_data.columns: meta['meta_wrist_worn'] = p_data.iloc[0]['wrist_worn_on']
                if 'dominant_hand' in p_data.columns: meta['meta_dominant_hand'] = p_data.iloc[0]['dominant_hand']
        except: pass
    return meta

def get_cgm_metadata(p_str):
    files = glob.glob(os.path.join(BASE_PATH, "wearable_blood_glucose", "**", "manifest.tsv"), recursive=True)
    meta = {}
    if files:
        try:
            df = pd.read_csv(files[0], sep='\t', low_memory=False)
            p_data = df[df['person_id'].astype(str) == p_str]
            if not p_data.empty:
                if 'manufacturer' in p_data.columns: meta['meta_cgm_device'] = p_data.iloc[0]['manufacturer']
                if 'manufacturer_model_name' in p_data.columns: meta['meta_cgm_model'] = p_data.iloc[0]['manufacturer_model_name']
        except: pass
    return meta

def load_participants_tsv():
    parts_path = os.path.join(BASE_PATH, "participants.tsv")
    meta_dict = {}
    if os.path.exists(parts_path):
        try:
            df = pd.read_csv(parts_path, sep='\t', low_memory=False)
            for _, row in df.iterrows():
                if pd.notna(row.get('person_id')):
                    p_id = str(int(row['person_id']))
                    meta_dict[p_id] = row.dropna().to_dict()
        except Exception as e:
            print(f"Warning: Could not load participants.tsv -> {e}")
    return meta_dict

# --- 2. MAIN COMPILER ENGINE ---

def compile_individual(p_id, global_meta):
    p_str = str(p_id)
    all_dfs = []

    # A. JSON PARSER
    json_files = glob.glob(os.path.join(BASE_PATH, "wearable*", "**", f"*{p_str}*.json"), recursive=True)
    for f in json_files:
        try:
            with open(f, 'r') as j:
                data = json.load(j)
                body = data.get('body', {})
                
                df = pd.DataFrame()
                if isinstance(body, dict):
                    for key, val in body.items():
                        if isinstance(val, list):
                            df = pd.json_normalize(val)
                            break
                elif isinstance(body, list):
                    df = pd.json_normalize(body)
                
                if not df.empty:
                    val_cols = [c for c in df.columns if 'value' in c.lower()]
                    for vc in val_cols:
                        df[vc] = pd.to_numeric(df[vc], errors='coerce')

                    t_col = next((c for c in df.columns if 'end_date_time' in c.lower()), None)
                    if not t_col:
                        t_col = next((c for c in df.columns if 'date_time' in c.lower()), None)
                    
                    if t_col:
                        df['timestamp'] = pd.to_datetime(df[t_col], utc=True, errors='coerce')
                        df = df.dropna(subset=['timestamp']).set_index('timestamp')
                        all_dfs.append(df)
        except: continue

    # B. CSV PARSER 
    env_files = glob.glob(os.path.join(BASE_PATH, "environment", "**", f"*{p_str}*ENV.csv"), recursive=True)
    for f in env_files:
        try:
            df = pd.read_csv(f, comment='#', low_memory=False, on_bad_lines='skip')
            t_col = next((c for c in df.columns if c.lower() == 'ts' or 'time' in c.lower()), None)
            if t_col:
                df['timestamp'] = pd.to_datetime(df[t_col], utc=True, errors='coerce')
                df = df.dropna(subset=['timestamp']).set_index('timestamp')
                
                sensor_cols = [c for c in df.columns if any(x in c.lower() for x in ['pm', 'temp', 'hum', 'voc', 'nox', 'lch'])]
                for col in sensor_cols:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                
                all_dfs.append(df)
        except: continue

    if not all_dfs: return None

    # C. MASTER MERGE
    combined = pd.concat(all_dfs, axis=0).sort_index()

    vitals = [c for c in combined.columns if 'value' in c.lower() and any(x in c.lower() for x in ['heart', 'oxygen', 'glucose', 'respiratory', 'stress'])]
    for v in vitals:
        combined[v] = combined[v].where(combined[v] > 0, np.nan)

    # DYNAMIC AGGREGATION RULES FOR HOURLY GRID
    agg_rules = {}
    for col in combined.columns:
        if pd.api.types.is_numeric_dtype(combined[col]):
            c_low = col.lower()
            if any(x in c_low for x in ['calor', 'step']):
                agg_rules[col] = 'sum'  
            elif any(x in c_low for x in ['stress', 'score']):
                agg_rules[col] = 'max'  
            else:
                agg_rules[col] = 'mean' 
        else:
            agg_rules[col] = 'first'    

    # 1. CREATE THE STRICT HOURLY GRID ('1h')
    resampled = combined.resample('1h').agg(agg_rules)

    # --- THE IMPUTATION ENGINE (Hourly Scale) ---
    
    # 2. Zero-Fill Burst Metrics
    burst_cols = [c for c in resampled.columns if any(x in c.lower() for x in ['step', 'calor'])]
    if burst_cols:
        resampled[burst_cols] = resampled[burst_cols].fillna(0)

    # 3. Interpolate Continuous Vitals (Limit is 2 HOURS)
    continuous_cols = [c for c in resampled.columns if pd.api.types.is_numeric_dtype(resampled[c]) and c not in burst_cols]
    if continuous_cols:
        resampled[continuous_cols] = resampled[continuous_cols].interpolate(method='linear', limit=2)

    # 4. Forward-Fill Categorical Data
    cat_cols = [c for c in resampled.columns if not pd.api.types.is_numeric_dtype(resampled[c])]
    if cat_cols:
        resampled[cat_cols] = resampled[cat_cols].ffill(limit=2)

    # 5. Final Trim
    sensor_cols = [c for c in resampled.columns if 'meta' not in c and 'clinical' not in c]
    if sensor_cols:
        resampled = resampled.dropna(how='all', subset=sensor_cols)

    # D. BROADCAST STATIC METADATA
    conds = get_clinical_conditions(p_str)
    if conds: resampled['clinical_conditions'] = conds
        
    env_loc = get_env_location(p_str)
    if env_loc: resampled['env_sensor_location'] = env_loc
        
    cardiac = get_cardiac_metrics(p_str)
    for k, v in cardiac.items(): resampled[k] = v
        
    wearable_meta = get_wearable_metadata(p_str)
    for k, v in wearable_meta.items(): resampled[k] = v

    cgm_meta = get_cgm_metadata(p_str)
    for k, v in cgm_meta.items(): resampled[k] = v
        
    for k, v in global_meta.get(p_str, {}).items():
        if k != 'person_id':  
            resampled[f"meta_{k}"] = v

    return resampled

# --- 3. EXECUTION ---
print("Initializing OMNIBUS Compiler (HOURLY Imputation Scale)...")
global_metadata = load_participants_tsv()

success_count = 0
target_ids = sorted([int(k) for k in global_metadata.keys() if str(k).isdigit()])
for i in target_ids:
    out_path = os.path.join(OUTPUT_FOLDER, f"AIREADI_P{i}_OMNIBUS_HOURLY.csv")
    if os.path.exists(out_path):
        print(f"SKIP: P{i} already processed (file exists)")
        continue

    try:
        result = compile_individual(i, global_metadata)
        if result is not None and not result.empty:
            result.to_csv(out_path)
            print(f"SUCCESS: P{i} | {len(result)} HOURS | {len(result.columns)} columns")
            success_count += 1
        else:
            print(f"SKIP: No valid time-series data found for P{i}")
    except Exception as e:
        print(f"ERROR on Participant {i}: {e}")

print(f"--- FINISHED. Compiled {success_count} participants into {OUTPUT_FOLDER} ---")
