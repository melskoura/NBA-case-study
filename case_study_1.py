import pandas as pd

df = pd.read_csv('1-Game Data-cavaliers-pistons 20 March.csv')

team_names = df['Team'].values
points = df['points'].values
rebounds = df['totReb'].values
assists = df['assists'].values
turnovers = df['turnovers'].values
steals = df['steals'].values
blocks = df['blocks'].values

#Task 1
'''
#sum of statistics
total_points = np.sum(points)
total_rebounds = np.sum(rebounds)
total_assists = np.sum(assists)
total_turnovers = np.sum(turnovers)
total_steals = np.sum(steals)
total_blocks = np.sum(blocks)

#average of statistics
average_points = np.mean(points)
average_rebounds = np.mean(rebounds)
average_assists = np.mean(assists)
average_turnovers = np.mean(turnovers)
average_steals = np.mean(steals)
average_blocks = np.mean(blocks)

# Displaying the results
results = {
    "Total Points": total_points,
    "Total Rebounds": total_rebounds,
    "Total Assists": total_assists,
    "Total Turnovers": total_turnovers,
    "Total Steals": total_steals,
    "Total Blocks": total_blocks,
    "Average Points": average_points,
    "Average Rebounds": average_rebounds,
    "Average Assists": average_assists,
    "Average Turnovers": average_turnovers,
    "Average Steals": average_steals,
    "Average Blocks": average_blocks,
}
print(results)'''

stats = ['points', 'totReb', 'assists', 'turnovers', 'steals', 'blocks']

totals = df[stats].sum()
averages = df[stats].mean()

results = pd.DataFrame({
    'Total': totals,
    'Average': averages
})

print("Task 1: ")
print(results)
print()

#Task 2

def compare_teams(statistic_array, team_names, stat_name):
    if statistic_array[0] > statistic_array[1]:
        winner = team_names[0]
        loser = team_names[1]
        difference = statistic_array[0] - statistic_array[1]
    else:
        winner = team_names[1]
        loser = team_names[0]
        difference = statistic_array[1] - statistic_array[0]

    return f"In {stat_name}, {winner} outperformed {loser} by {difference}."

# Comparisons in points, rebounds, and assists
comparison_points = compare_teams(points, team_names, "points")
comparison_rebounds = compare_teams(rebounds, team_names, "rebounds")
comparison_assists = compare_teams(assists, team_names, "assists")

# Printing the comparison results
comparisons = {
    "Points Comparison": comparison_points,
    "Rebounds Comparison": comparison_rebounds,
    "Assists Comparison": comparison_assists
}

print("Task 2: ")
for key, value in comparisons.items():
    print(f"{key}: {value}")
print()

#Task 3

def shooting_efficiency(fgm, fga, tpm, tpa, ftm, fta, points):
    efg = ((fgm + 0.5 * tpm) / fga) * 100

    if fta != 0:
        ft = (ftm / fta) * 100
    else:
        ft = 0

    if (fga + 0.44 * fta) != 0:
        ts = (points / (2 * (fga + 0.44 * fta))) * 100
    else:
        ts = 0

    return efg, ft, ts

# Extracting shooting data from the dataframe
fgm = df['fgm'].values  # Field goals made
fga = df['fga'].values  # Field goal attempts
tpm = df['tpm'].values  # Three-point field goals made
tpa = df['tpa'].values  # Three-point field goal attempts
ftm = df['ftm'].values  # Free throws made
fta = df['fta'].values  # Free throw attempts

# Calculating shooting efficiency for both teams
team1_efg, team1_ftp, team1_ts = shooting_efficiency(fgm[0], fga[0], tpm[0], tpa[0], ftm[0], fta[0], points[0])
team2_efg, team2_ftp, team2_ts = shooting_efficiency(fgm[1], fga[1], tpm[1], tpa[1], ftm[1], fta[1], points[1])

# Storing the results
shooting_efficiency_results = {
    team_names[0]: {
        "eFG%": team1_efg,
        "FT%": team1_ftp,
        "TS%": team1_ts
    },
    team_names[1]: {
        "eFG%": team2_efg,
        "FT%": team2_ftp,
        "TS%": team2_ts
    }
}

print("Task 3: ")
for team, stats in shooting_efficiency_results.items():
    print(f"{team}:")
    for k, v in stats.items():
        print(f"  {k:<4} : {v:.2f}%")
    print()

