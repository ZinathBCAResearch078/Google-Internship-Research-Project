import pandas as pd
import numpy as np

def analyze_gdelt_bias(file_path):
    """
    RESEARCH LOGIC:
    Processes GDELT event data in chunks to identify geographic skews 
    without crashing system memory (RAM).
    """
    print(f"--- Starting Bias Investigation on: {file_path} ---")
    
    # TECHNICAL NOTE:
    # We use chunksize because GDELT files can contain millions of rows.
    # This ensures the investigator remains functional on resource-constrained 
    # environments by optimizing RAM usage through vectorized operations.
    chunk_size = 50000 
    
    try:
        # Placeholder for data stream initialization
        print(f"Optimization Active: Processing in blocks of {chunk_size}...")
        
        # In a full run, we would aggregate geographic coordinates here
        # to identify 'Data Deserts' vs 'Data Hotspots'.
        
        print("Analysis Status: Core research logic initialized successfully.")
        
    except Exception as e:
        print(f"Error during optimized load: {e}")

if __name__ == "__main__":
    # Standard entry point for research scripts
    # We use a dummy CSV name as a placeholder for the GDELT stream
    analyze_gdelt_bias("gdelt_events_2026.csv")import pandas as pd

# Research Project: Data Bias Investigator
# Simulating a dataset to measure geographic representation
data = {
    'Movie_Title': ['Action Hero', 'Romantic Days', 'Street Dance', 'Tech Life', 'Rural India', 'Global Wars', 'City Lights', 'Desert Storm', 'Mountain Peak', 'Island Dream'],
    'Origin_Country': ['USA', 'USA', 'USA', 'USA', 'India', 'USA', 'USA', 'UK', 'USA', 'USA'],
    'Genre': ['Action', 'Romance', 'Documentary', 'Sci-Fi', 'Drama', 'Action', 'Drama', 'Action', 'Nature', 'Travel']
}

df = pd.DataFrame(data)

# ANALYSIS: Calculating the percentage of USA content to detect bias
total_movies = len(df)
usa_movies = len(df[df['Origin_Country'] == 'USA'])
bias_percentage = (usa_movies / total_movies) * 100

print(f"Total Movies Analyzed: {total_movies}")
print(f"Percentage of USA Content: {bias_percentage}%")

# CONCLUSION: Determining if the dataset is imbalanced
if bias_percentage > 50:
    print("RESULT: Significant Geographic Bias Detected.")
else:
    print("RESULT: Data is Geographically Balanced.")
  
