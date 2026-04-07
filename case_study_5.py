import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('1-Nikola Jokic.csv')
'''
#Task 1
df_sorted = df.sort_values(by=['Game_ID'])

fig = px.line(df_sorted, x='Game_ID', y='points', title='Nikola Jokic Points Per Game Over Time')

fig.show()'''

'''#Task 2
df_clean = df.dropna(subset=['points', 'assists', 'totReb'])
avg_stats = {
    "Average Points": df_clean['points'].mean(),
    "Average Assists": df_clean['assists'].mean(),
    "Average Rebounds": df_clean['totReb'].mean()
}

fig = go.Figure(data=[
    go.Bar(name='Average Points', x=list(avg_stats.keys()), y=[avg_stats["Average Points"]]),
    go.Bar(name='Average Assists', x=list(avg_stats.keys()), y=[avg_stats["Average Assists"]]),
    go.Bar(name='Average Rebounds', x=list(avg_stats.keys()), y=[avg_stats["Average Rebounds"]])
])

fig.update_layout(barmode='group', title='Nikola Jokic Average Stats Per Game')

fig.show()'''

#Task 3
df_clean = df.dropna(subset=['points'])

fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df_clean['points'], xbins=dict(start=0, end=df_clean['points'].max(), size=5), marker_color='#EB89B5', opacity=0.75))

# Add range slider to the layout
fig.update_layout(
    title_text='Distribution of Points Scored by Nikola Jokic',
    xaxis=dict(
        title='Points Scored',
        rangeslider=dict(visible=True),
        type='linear'
    ),
    yaxis=dict(title='Count'),
    bargap=0.1  # Gap between bars of adjacent location coordinates
)

# Display the figure
fig.show()