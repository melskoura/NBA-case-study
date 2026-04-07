import pandas as pd
import plotly.express as px

df_la = pd.read_csv('2-Los Angeles Lakers.csv')
df_mb = pd.read_csv('4-Milwaukee Bucks.csv')

df = pd.concat([df_la, df_mb])
colors = {'Lakers': 'purple', 'Bucks': 'green'}

'''#Task 1
avg_points = df.groupby('Team')['points'].mean().reset_index()
fig = px.bar(avg_points, x='Team', y='points', title='Average Points Scored by Team', color='Team', color_discrete_map=colors)

fig.show()'''

'''#Task 2
fig = px.histogram(df, x='min', color='Team', barmode='overlay', title='Distribution of Minutes Played by Lakers and Bucks Players', color_discrete_map=colors)
fig.update_layout(barmode='overlay', xaxis_title='Minutes Played', yaxis_title='Count', legend_title='Team')

fig.show()'''

#Task 3
filtered_df = df[(df['fga'] > 10) & (df['tpa'] > 5)]

fig = px.scatter(filtered_df, x='fgp', y='tpp', color='Team', hover_name='Player', title='Shooting Efficiency: FGP vs TPP',
                 color_discrete_map=colors, labels={'fgp': 'Field Goal Percentage', 'tpp': 'Three-Point Percentage'},
                 width=800, height=600)  # Adjusting chart size

fig.update_layout(xaxis_title='Field Goal Percentage', yaxis_title='Three-Point Percentage', legend_title='Team')

fig.update_traces(marker=dict(size=8, opacity=0.8),
                  hoverinfo='text+name')

fig.show()