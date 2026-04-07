import pandas as pd

df_jb = pd.read_csv('1-Jimmy Butler.csv')
df_nj = pd.read_csv('1-Nikola Jokic.csv')

df_jb.fillna(0, inplace=True)
df_nj.fillna(0, inplace=True)

#Task 1
# Merging Datasets
# Merge on 'Game_ID' to compare statistics in the same games
merged_df = pd.merge(df_jb, df_nj, on='Game_ID', suffixes=('_Butler', '_Jokic'))

# Basic Time-Series Analysis
# Calculate the moving average of points scored over the last 5 games
merged_df['MA_Points_Butler'] = merged_df['points_Butler'].rolling(window=5).mean()
merged_df['MA_Points_Jokic'] = merged_df['points_Jokic'].rolling(window=5).mean()

# Display the first few rows of the merged dataset
print("Task 1:")
print(merged_df.head())
print()

#Task 2
#Average
average_df_jb = df_jb.groupby('Team').mean(numeric_only=True)
average_df_nj = df_nj.groupby('Team').mean(numeric_only=True)

#Data Filtering
high_score_jb = df_jb[df_jb['points'] > 20]
high_score_nj = df_nj[df_nj['points'] > 20]

#Data Sorting
sorted_jb = df_jb.sort_values(by='points', ascending=False)
sorted_nj = df_nj.sort_values(by='points', ascending=False)

# Display the average stats
print("Task 2:")
print("Average stats for Jimmy Butler:")
print(average_df_jb)
print("\nAverage stats for Nikola Jokic:")
print(average_df_nj)

# Display a few high scoring games
print("\nHigh scoring games for Jimmy Butler:")
print(high_score_jb.head())
print("\nHigh scoring games for Nikola Jokic:")
print(high_score_nj.head())
print()

#Task 3
def categorize_performance(points):
    if points <= 10:
        return 'Low'
    elif points <= 20:
        return 'Medium'
    elif points <= 30:
        return 'High'
    else:
        return 'Very High'


# Data Manipulation: Applying Functions
# Use apply() to calculate efficiency and categorize performance
df_nj['efficiency'] = df_nj.apply(lambda row: row['points'] / row['min'] if row['min'] > 0 else 0, axis=1)
df_nj['Performance_Label'] = df_nj['points'].apply(categorize_performance)

df_jb['efficiency'] = df_jb.apply(lambda row: row['points'] / row['min'] if row['min'] > 0 else 0, axis=1)
df_jb['Performance_Label'] = df_jb['points'].apply(categorize_performance)

# Use map() on a DataFrame to transform the 'Team' column based on a predefined dictionary
team_mapping = {'Heat': 'Miami Heat', 'Nuggets': 'Denver Nuggets'}
df_jb['Team'] = df_jb['Team'].map(team_mapping)
df_nj['Team'] = df_nj['Team'].map(team_mapping)

# Grouping Data: Group by 'Performance_Label' and calculate mean stats, specifying numeric_only=True
grouped_df_jb = df_jb.groupby('Performance_Label').mean(numeric_only=True)
grouped_df_nj = df_nj.groupby('Performance_Label').mean(numeric_only=True)

# Display the grouped statistics
print("Task 3:")
print("Grouped Stats for Jimmy Butler:")
print(grouped_df_jb)

print("\nGrouped Stats for Nikola Jokic:")
print(grouped_df_nj)
print()

