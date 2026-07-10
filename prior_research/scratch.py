import pandas as pd
import numpy as np

meas_df = pd.read_csv('/Volumes/Extreme SSD/Documents/ucsf/dataset/clinical_data/measurement.csv', low_memory=False)
moca_df = meas_df[meas_df['measurement_source_value'] == 'moca_total_score'].copy()

print(f"Found {len(moca_df)} total MOCA score records.")
print(f"Unique patients with MOCA scores: {moca_df['person_id'].nunique()}")
print(moca_df[['person_id', 'measurement_date', 'value_source_value']].head())

