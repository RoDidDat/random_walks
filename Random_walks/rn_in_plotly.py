from plotly.graph_objs import Bar, Layout
from plotly import offline
from random_walk import RandomWalk


# Make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()


data = [Bar(x=rw.x_values, y=rw.y_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of Random Walks',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='ranwalk.html')


