import pandas as pd
import glob
import os

files = glob.glob('/Users/guardian/Documents/ucsf/eda_advanced_outputs/bootstraps/factorial_bootstrap_*.csv')

output_lines = []
output_lines.append("COMPREHENSIVE BOOTSTRAP INSIGHTS & SIGNIFICANT FINDINGS")
output_lines.append("=====================================================\n")
output_lines.append("Note: 'Significant' implies the 95% Confidence Interval (CI) does not cross zero.\n")

for f in files:
    var_name = os.path.basename(f).replace('factorial_bootstrap_', '').replace('.csv', '')
    df = pd.read_csv(f)
    
    # Check for significance
    # A result is significant if both CI bounds are > 0 OR both are < 0
    df['significant'] = ((df['2.5% CI'] > 0) & (df['97.5% CI'] > 0)) | ((df['2.5% CI'] < 0) & (df['97.5% CI'] < 0))
    df['abs_diff'] = df['Mean Diff'].abs()
    
    # Sort by absolute mean difference to find the "biggest" effects
    df_sorted = df.sort_values(by='abs_diff', ascending=False)
    
    output_lines.append(f"--- VARIABLE: {var_name.upper()} ---")
    
    sig_df = df_sorted[df_sorted['significant']]
    
    if sig_df.empty:
        output_lines.append("No statistically significant group differences found at the 95% confidence level.\n")
        continue
        
    output_lines.append(f"Found {len(sig_df)} significant group comparisons. Top findings by effect size:")
    
    for _, row in sig_df.head(5).iterrows():
        g1 = row['Group 1']
        g2 = row['Group 2']
        diff = row['Mean Diff']
        ci_low = row['2.5% CI']
        ci_high = row['97.5% CI']
        
        direction = "higher" if diff > 0 else "lower"
        
        output_lines.append(f"  • {g1} vs {g2}:")
        output_lines.append(f"      -> {g1} is {abs(diff):.2f} units {direction} than {g2}.")
        output_lines.append(f"      -> 95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
        
    output_lines.append("")

with open('/Users/guardian/Documents/ucsf/eda_advanced_outputs/bootstraps/bootstrap_comprehensive_insights.txt', 'w') as out:
    out.write('\n'.join(output_lines))
    
print("Summary generated.")
