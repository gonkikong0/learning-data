#Program simulates rolling a D6 die (x number of times), tracks the frequency of results and visualizes it on a Histogram. 
#Action -> Data Collection -> Analysis -> Visualization

from plotly.graph_objs import Bar, Layout
from plotly import offline 
from die import Die

#Creating a D6
dice_1 = Die()
dice_2 = Die()
#Rolling and storing results in a list.
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#ANALYZING THE RESULTS
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
 
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results -

x_values = list(range(2, max_result+ 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename = 'd6_d6.html')