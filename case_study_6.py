import pandas as pd
import scipy.stats as stats
from scipy.stats import ttest_ind, linregress

df = pd.read_csv('2-Milwaukee Bucks.csv')

'''#Task 1
points = df['points']
minutes_played = df['min']

correlation, p_value = stats.pearsonr(points.dropna(), minutes_played.dropna())

print(f"Correlation coefficient between Points Scored and Minutes Played: {correlation}")
print(f"P-value: {p_value}")'''

'''#Task 2
even_game_points = df[df['Game_ID'] % 2 == 0]['points']
odd_game_points = df[df['Game_ID'] % 2 != 0]['points']

t_statistic, p_value = ttest_ind(even_game_points, odd_game_points, nan_policy='omit')

print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")'''

#Task 3
cleaned_df = df.dropna(subset=['min', 'points'])

slope, intercept, r_value, p_value, std_err = linregress(cleaned_df['min'], cleaned_df['points'])

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-Value: {p_value}")
print(f"Standard Error: {std_err}")

predicted_points_30_min = slope * 30 + intercept
print(f"Predicted Points for 30 minutes played: {predicted_points_30_min}")