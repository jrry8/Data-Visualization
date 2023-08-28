import matplotlib.pyplot as plt

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

x_vals = list(range(1, 51))
y_vals = [x**2 for x in x_vals]
# s: marker size
# colormap is a series of colors in a gradient
# colormaps can be used to emphasize a pattern in the data
# e.g. here we make low values a light blue and high values a dark blue
plt.scatter(x_vals, y_vals, s=10, edgecolors='none', c=y_vals, cmap=plt.cm.Blues)

# at the end of show(), the figure is closed and unregistered from pyplot
# if we called savefig() after show(), we would save a new and empty figure
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
