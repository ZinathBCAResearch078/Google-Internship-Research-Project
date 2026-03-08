import pandas as pd
import os

# This script points to the exact file you just renamed
file_path = '/sdcard/Download/research_data.csv'

if not os.path.exists(file_path):
    # Secondary path check for different Android versions
    file_path = '/storage/emulated/0/Download/research_data.csv'

if os.path.exists(file_path):
    print("✅ Research Data Found. Starting Analysis...")
    
    # We load only column 7 (Country Code) to keep mobile performance high
    df = pd.read_csv(file_path, sep='\t', header=None, usecols=[10], names=['CountryCode'])
    
    # Calculate the percentage of total news coverage for each country
    bias_metrics = df['CountryCode'].value_counts(normalize=True) * 100
    
    print("\n--- 🔍 DATA BIAS INVESTIGATOR: GEOGRAPHIC RESULTS ---")
    print(bias_metrics.head(10).to_string())
    
    # Specific comparison for your research log
    india = bias_metrics.get('IND', 0)
    usa = bias_metrics.get('USA', 0)
    print(f"\nIndia (IND) Representation: {india:.2f}%")
    print(f"United States (USA) Representation: {usa:.2f}%")
    print("\n--- ANALYSIS COMPLETE ---")
else:
    print("❌ Error: Still cannot see 'research_data.csv' in Download.")
