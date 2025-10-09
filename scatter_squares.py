import matplotlib.pyplot as plt


x_values = range(1,1001)
y_values = [x**2 for x in x_values]

# plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values ,c = y_values, cmap=plt.cm.Blues , s = 3) #s = markersize (x,y) [data positions]
# The color ('c') can also be passed using RGB Color Model, example : c = (0, 0.9, 0) [ranging from 0 - 1]

#Set chart title and label Axes.

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square Value", fontsize = 14)

#Set size of tick labels.
ax.tick_params(axis='both', which = 'major', labelsize = 14)

#Set the range for each axis.
ax.axis([0, 1100, 0, 1100000]) 

# plt.show() #This only shows the plots
plt.savefig('first_plot.png', bbox_inches ='tight')