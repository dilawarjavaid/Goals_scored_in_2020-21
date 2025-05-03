import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io

# Step 1: Data Collection
url = 'https://www.football-data.co.uk/mmz4281/2021/E0.csv'
response = requests.get(url)
data = pd.read_csv(io.StringIO(response.text))

# Step 2: Data Cleaning
# Inspect the first few rows of the dataset
print(data.head())

# Select relevant columns for analysis
# HomeTeam, AwayTeam, FTHG (Full Time Home Goals), FTAG (Full Time Away Goals)
data = data[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]

# Step 3: Data Analysis
# Calculate total goals scored by each team (home and away)
data['TotalHomeGoals'] = data.groupby('HomeTeam')['FTHG'].transform('sum')
data['TotalAwayGoals'] = data.groupby('AwayTeam')['FTAG'].transform('sum')