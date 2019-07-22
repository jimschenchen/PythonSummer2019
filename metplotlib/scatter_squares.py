import matplotlib.pyplot as plt



x_value = [value for value in range(1, 1000)]
y_value = [value**2 for value in x_value]
plt.scatter(x_value, y_value, c = y_value, cmap = plt.cm.Blues, edgecolor='none', s = 10)

plt.axis([0, 1100, 0, 1100000])

plt.savefig("square_plot.png", bbox_inches = 'tight')