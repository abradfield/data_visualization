import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# The following sets a color using a name, but you can use an RGB(x, x, x) value
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# Can also set a gradient using a colormap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=13)

# Set the size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

# Use the following to save to a file
#plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()