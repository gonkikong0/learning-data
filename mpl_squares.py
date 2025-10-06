import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4 ,5]
squares = [1,4,9,16,25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(input_values ,squares, linewidth = 3)


#Set up Chart titles and label Axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of the value", fontsize = 14)

#Set size of tick labels #Mainly for styling (tick_parms)
ax.tick_params(axis= 'both', labelsize= 14)

plt.show()