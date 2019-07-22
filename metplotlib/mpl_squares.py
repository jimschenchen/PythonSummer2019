import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_value = [value for value in range(1, 6)]
plt.plot(input_value, squares, linewidth = 5)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 24)
plt.ylabel("Square of value", fontsize = 24)

#plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
