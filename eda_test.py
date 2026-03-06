import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignore seaborn warnings for cleaner output
warnings.filterwarnings('ignore')

# --- CONFIGURATION ---
INPUT_FOLDER = os.path.abspath("./output_omnibus_final")
OUTPUT_FOLDER = os.path.abspath("./edatest_outputs")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Set global plotting style
sns.set_theme(style="whitegrid", palette="muted")

def extract_participant_id(filename):
    """Extracts ID like 'P1001' from 'AIREADI_P1001_OMNIBUS_FINAL.csv'."""
    base = os.path.basename(filename)
    parts = base.split('_')
    for part in parts:
        if part.startswith('P') and part[1:].isdigit():
            return part
    return base.split('_')[1] if len(base.split('_')) > 1 else "Unknown"

def process_file_logic(df):
    """Ensures all columns exist (filling missing ones with NaN) before aggregating."""
    # 1. Setup Time Features
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    
    # 2. Define the EXACT Master Schema
    # Every column listed here WILL appear in the final CSV, no matter what.
    desired_aggregations = {
        # Continuous Metrics
        'heart_rate.value': ['mean', 'min', 'max', 'std'],
        'oxygen_saturation.value': ['mean', 'min'],
        'stress.value': ['mean', 'max'],
        'blood_glucose.value': ['mean', 'std', 'max'],
        'respiratory_rate.value': ['mean'],
        'temp': ['mean'],
        
        # Burst / Accumulation Metrics
        'base_movement_quantity.value': ['sum'],
        'calories_value.value': ['sum'],
        
        # Metadata
        'meta_study_group': ['first'],
        'meta_age': ['first']
    }
    
    # 3. CRITICAL FIX: Inject missing columns with NaN so they are never skipped
    for col in desired_aggregations.keys():
        if col not in df.columns:
            df[col] = np.nan

    # 4. Generate Daily Summary (Interday)
    # Pandas automatically ignores NaN rows when calculating mean, std, max, etc.
    daily = df.groupby('date').agg(desired_aggregations)
    
    # Flatten the multi-level columns (e.g., 'heart_rate.value' & 'mean' -> 'heart_rate.value_mean')
    daily.columns = [f"{col}_{stat}" for col, stat in daily.columns]
    daily = daily.reset_index()

    # 5. Generate Hourly Summary (Intraday / Circadian)
    hourly_cols = ['heart_rate.value', 'blood_glucose.value', 'stress.value']
    # Ensure hourly columns exist
    for col in hourly_cols:
        if col not in df.columns:
            df[col] = np.nan
            
    hourly = df.groupby(['date', 'hour'])[hourly_cols].mean().reset_index()
        
    return daily, hourly

def aggregate_data():
    """Reads all 5-min Omnibus CSVs and compiles master datasets."""
    print("Loading 5-minute interval data and aggregating...")
    files = glob.glob(os.path.join(INPUT_FOLDER, "*_OMNIBUS_FINAL.csv"))
    
    if not files:
        print(f"ERROR: No files found in {INPUT_FOLDER}")
        return pd.DataFrame(), pd.DataFrame()

    all_daily = []
    all_hourly = []
    
    for f in files:
        try:
            df = pd.read_csv(f, parse_dates=['timestamp'], low_memory=False)
            if df.empty:
                continue
                
            p_id = extract_participant_id(f)
            
            daily_df, hourly_df = process_file_logic(df)
            
            daily_df['participant_id'] = p_id
            all_daily.append(daily_df)
            
            if not hourly_df.empty:
                hourly_df['participant_id'] = p_id
                all_hourly.append(hourly_df)
                
            print(f"Processed: {p_id}")
            
        except Exception as e:
            print(f"Error processing {os.path.basename(f)}: {e}")
            
    # Concatenate all participant dataframes
    master_daily = pd.concat(all_daily, ignore_index=True) if all_daily else pd.DataFrame()
    master_hourly = pd.concat(all_hourly, ignore_index=True) if all_hourly else pd.DataFrame()
    
    # Reorder participant_id to the front for readability
    if not master_daily.empty:
        cols = ['participant_id', 'date'] + [c for c in master_daily.columns if c not in ['participant_id', 'date']]
        master_daily = master_daily[cols]
        
    if not master_hourly.empty:
        cols = ['participant_id', 'date', 'hour'] + [c for c in master_hourly.columns if c not in ['participant_id', 'date', 'hour']]
        master_hourly = master_hourly[cols]
    
    return master_daily, master_hourly

# --- VISUALIZATION FUNCTIONS ---

def plot_missingness(df):
    """Visualizes missing data to see exactly which columns are empty for which rows."""
    plt.figure(figsize=(14, 8))
    # Drop identifier columns for the heatmap
    plot_df = df.drop(columns=['participant_id', 'date', 'meta_study_group_first', 'meta_age_first'], errors='ignore')
    
    # If a sum was calculated on all NaNs, pandas returns 0.0. Let's convert 0.0 in movement/calories to NaN for the map if it's deceptive.
    # (Optional, but good for pure missingness visualization)
    
    sns.heatmap(plot_df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
    plt.title("Daily Data Completeness Map (Yellow = Missing Data)", fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "00_missing_data_map.png"), dpi=300)
    plt.close()

def plot_temporal_trends(df):
    """Plots cohort-level average trends over the days of the study (Interday)."""
    df['day_index'] = df.groupby('participant_id').cumcount() + 1
    
    metrics = ['heart_rate.value_mean', 'blood_glucose.value_mean', 'stress.value_mean', 'oxygen_saturation.value_mean']
    available_metrics = [m for m in metrics if m in df.columns and df[m].notna().any()]
    
    if not available_metrics: return

    plt.figure(figsize=(14, 8))
    for metric in available_metrics:
        sns.lineplot(data=df, x='day_index', y=metric, label=metric.split('.')[0].replace('_', ' ').title(), errorbar=None, marker='o')
        
    plt.title("Cohort Average Trends Over Time (Interday)", fontsize=16)
    plt.xlabel("Study Day")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "01_cohort_temporal_trends.png"), dpi=300)
    plt.close()

def plot_intraday_circadian(hourly_df):
    """Plots the average 24-hour cycle across the cohort (Intraday)."""
    if 'heart_rate.value' not in hourly_df.columns or hourly_df['heart_rate.value'].isna().all(): 
        return
    
    plt.figure(figsize=(12, 6))
    
    if 'meta_study_group_first' in hourly_df.columns and not hourly_df['meta_study_group_first'].isna().all():
        sns.lineplot(data=hourly_df, x='hour', y='heart_rate.value', hue='meta_study_group_first', errorbar='sd')
    else:
        sns.lineplot(data=hourly_df, x='hour', y='heart_rate.value', errorbar='sd', color='teal')
        
    plt.title("Average Circadian Heart Rate Rhythm (Intraday)")
    plt.xlabel("Hour of Day (24h)")
    plt.ylabel("Heart Rate (BPM)")
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "02_circadian_hr_rhythm.png"), dpi=300)
    plt.close()

# --- EXECUTION ---
if __name__ == "__main__":
    master_daily, master_hourly = aggregate_data()
    
    if not master_daily.empty:
        print("\nAggregations complete. Generating visual reports...")
        
        # Generate Plots
        plot_missingness(master_daily)
        plot_temporal_trends(master_daily)
        
        if not master_hourly.empty:
            plot_intraday_circadian(master_hourly)
        
        # Save Outputs
        daily_csv = os.path.join(OUTPUT_FOLDER, "MASTER_DAILY_AGGREGATE.csv")
        hourly_csv = os.path.join(OUTPUT_FOLDER, "MASTER_HOURLY_INTRADAY.csv")
        
        master_daily.to_csv(daily_csv, index=False)
        master_hourly.to_csv(hourly_csv, index=False)
        
        print(f"\n--- EDA COMPLETE ---")
        print(f"Data saved to: {daily_csv}")
    else:
        print("Could not generate EDA: No valid data aggregated.")