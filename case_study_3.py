import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1-Game Data-celtics-warriors 17 June.csv')

team_names = df['Team'].values
points = df['points'].values
rebounds = df['totReb'].values
fgp = df['fgp'].values

'''#Task 1
plt.figure(figsize=(10, 6))
plt.bar(team_names, points, color=['darkblue', 'green'])

plt.xlabel('Team')
plt.ylabel('Points')
plt.title("Total Points by Team")
#lt.grid(axis='y')
plt.show()

#Task 2
plt.figure(figsize=(10, 6))
plt.pie(rebounds, labels=team_names, explode=(0, 0.05), autopct='%1.1f%%', startangle=140, colors=['darkblue', 'green'],
        textprops={'color': 'white', 'fontsize': 12},
        wedgeprops={'edgecolor':'black'})

plt.title("Total Rebounds Distribution")
plt.show()'''

#Task 3
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].bar(team_names, fgp, color=['orange', 'lightblue'])
ax[0].set_xlabel("Team")
ax[0].set_ylabel("Field Goal Percentage (%)")
ax[0].set_title("Field Goal Percentage by Team")
ax[0].grid(axis='y')

colors=['blue', 'red']
for i, team in enumerate(team_names):
    ax[1].scatter(rebounds[i], points[i], color=colors[i], label=team, s=100)

ax[1].set_xlabel("Total Rebounds")
ax[1].set_ylabel("Points")
ax[1].set_title("Total Rebounds vs. Points")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()