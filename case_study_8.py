import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_la = pd.read_csv('1-Los Angeles Lakers.csv')
df_mb = pd.read_csv('3-Milwaukee Bucks.csv')

df = pd.concat([df_la, df_mb])
df = df.fillna(0)

df_la = df_la.fillna(0)
df_mb = df_mb.fillna(0)

'''#Task 1
avg_points_player = df.groupby('Player')['points'].mean().reset_index()

top_ten = avg_points_player.sort_values(by='points', ascending=False).head(10)

sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.barplot(x='Player', y='points', data=top_ten, hue='Player', palette='viridis', legend=False)
plt.xticks(rotation=45)
plt.title('Top 10 Players by Average Points')
plt.xlabel('Player')
plt.ylabel('Average Points')
plt.tight_layout()
plt.show()'''

'''#Task 2
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
sns.boxplot(x='Team', y='assists', data=df, hue='Team', palette='coolwarm', legend=False)
plt.title('Distribution of Assists Between Lakers and Bucks')
plt.xlabel('Team')
plt.ylabel('Assists')
plt.tight_layout()
plt.show()'''

#Task 3
def calculate_efficiency_metrics(fgm, fga, tpm, ftm, fta, points):
    efg = (fgm + 0.5 * tpm) / fga if fga != 0 else 0
    ft = ftm / fta if fta != 0 else 0
    ts = points / (2 * (fga + 0.44 * fta)) if (fga + 0.44 * fta) != 0 else 0
    return efg, ft, ts

def extract_team_totals(df):
    fgm = df["fgm"].sum()
    fga = df["fga"].sum()
    tpm = df["tpm"].sum()
    ftm = df["ftm"].sum()
    fta = df["fta"].sum()
    points = df["points"].sum()
    return fgm, fga, tpm, ftm, fta, points

lakers_stats = extract_team_totals(df_la)
bucks_stats = extract_team_totals(df_mb)

lakers_eff = calculate_efficiency_metrics(*lakers_stats)
bucks_eff = calculate_efficiency_metrics(*bucks_stats)

results = pd.DataFrame({
    "Team": ["Los Angeles Lakers", "Milwaukee Bucks"],
    "eFG%": [lakers_eff[0], bucks_eff[0]],
    "FT%": [lakers_eff[1], bucks_eff[1]],
    "TS%": [lakers_eff[2], bucks_eff[2]]
})

print(results)

total_points_lakers = df_la['points'].sum()
total_points_bucks = df_mb['points'].sum()

# Data for pie chart
teams = ['Lakers', 'Bucks']
points = [total_points_lakers, total_points_bucks]
colors = ['#552583', '#00471B'] # Lakers purple and Bucks green
explode = (0.1, 0)  # explode 1st slice (Lakers)

# Plotting a pie chart
plt.figure(figsize=(8, 8))
plt.pie(points, explode=explode, labels=teams, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total Points Contribution by Team')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()