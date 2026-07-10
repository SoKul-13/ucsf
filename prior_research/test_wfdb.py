import pandas as pd
import wfdb
import os
import time

manifest = pd.read_csv('/Users/guardian/Documents/ucsf/dataset/cardiac_ecg/manifest.tsv', sep='\t')
print(f"Total ECG records: {len(manifest)}")

start = time.time()
sample_file = manifest['wfdb_hea_filepath'].iloc[0]
sample_path = os.path.join('/Users/guardian/Documents/ucsf/dataset', sample_file.lstrip('/'))
sample_path_base = sample_path.replace('.hea', '')

record = wfdb.rdrecord(sample_path_base)
print(f"Signals shape: {record.p_signal.shape}")
print(f"Sample frequency: {record.fs}")
print(f"Signal names: {record.sig_name}")
print(f"Time to read 1 record: {time.time() - start:.3f}s")
