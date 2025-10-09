import matplotlib.pyplot as plt


x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values , s = 3) #s = markersize (x,y) [data positions]

#Set chart title and label Axes.

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square Value", fontsize = 14)

#Set size of tick labels.
ax.tick_params(axis='both', which = 'major', labelsize = 14)

plt.show()  