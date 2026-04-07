import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_bucks = pd.read_csv('Player Data-bucks-clippers 2 April.csv')
data_hawks = pd.read_csv('Player Data-hawks-nets 2 April.csv')

df = pd.concat([data_bucks, data_hawks])

'''#Task 1
sns.set_style('whitegrid')

avg_points = df.groupby('Team')['points'].mean().reset_index()
plt.figure(figsize = (10, 6))
bar_plot = sns.barplot(x = 'Team', y = 'points', data = avg_points)

bar_plot.set_title('Average Points per Team')
bar_plot.set_xlabel('Team')
bar_plot.set_ylabel('Average Points')

plt.show()'''

'''#Task 2
sns.set_style('darkgrid')

avg_fgp = df.groupby('Team')['fgp'].mean().reset_index()
plt.figure(figsize = (10, 6))
scatter_plot = sns.regplot(x = 'fgp', y = 'points', data = df)

scatter_plot.set_title('FGP over Points')
scatter_plot.set_xlabel('FGP')
scatter_plot.set_ylabel('Points')

plt.show()'''

#Task 3
key_var = ['points', 'assists', 'steals', 'blocks', 'totReb', 'fgp', 'tpp', 'ftm']
corr_matrix = df[key_var].corr()

plt.figure(figsize = (12, 8))
heatmap =sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)

heatmap.set_title('Correlation Matrix of Basketball Game Statistics')

plt.show()
