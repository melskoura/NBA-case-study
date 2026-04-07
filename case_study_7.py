import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('1-Game Data-grizzlies-knicks 12 March.csv')

team_names = df['Team'].values
points = df['points'].values
assists = df['assists'].values
rebounds = df['totReb'].values
steals = df['steals'].values
blocks = df['blocks'].values
fga = df['fga'].values
fgm = df['fgm'].values
fta = df['fta'].values
ftm = df['ftm'].values
turnovers = df['turnovers'].values

unique_teams = np.unique(team_names)

'''#Task 1
avg_points_per_team = np.zeros(len(unique_teams))

for i, team in enumerate(unique_teams):
    team_points = points[team_names == team]
    avg_points_per_team[i] = np.nanmean(team_points)  

plt.bar(unique_teams, avg_points_per_team, color=['blue', 'orange'])
plt.xlabel('Team')
plt.ylabel('Average Points')
plt.title('Average Points Scored by Team')
plt.show()'''

'''#Task 2
total_assists = np.zeros(len(unique_teams))

for i, team in enumerate(unique_teams):
    total_assists[i] = np.nansum(assists[team_names == team])

avg_assists = total_assists / np.array([np.sum(team_names == team) for team in unique_teams])

plt.pie(avg_assists, labels=unique_teams, autopct='%1.1f%%', startangle=140, colors=['blue', 'orange'])
plt.title('Average Assists per Player by Team')
plt.show()'''

#Task 3
efficiency = points + rebounds + assists + steals + blocks - (fga - fgm) - (fta - ftm) - turnovers

df['efficiency'] = efficiency

avg_efficiency = np.zeros(len(unique_teams))
for i, team in enumerate(unique_teams):
    team_efficiency = efficiency[team_names == team]
    avg_efficiency[i] = np.nanmean(team_efficiency)

plt.bar(unique_teams, avg_efficiency, color=['blue', 'orange'])
plt.xlabel('Team')
plt.ylabel('Average Efficiency')
plt.title('Average Player Efficiency by Team')
plt.show()