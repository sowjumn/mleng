import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y, label='Sin(x)')
plt.title('Matplotlib Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
plt.savefig('plot.png')
