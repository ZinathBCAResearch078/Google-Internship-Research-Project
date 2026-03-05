import pandas as pd

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
  
