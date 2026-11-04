# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

year = np.array([1990, 2000, 2010, 2020])
pop = np.array([10000, 15000, 32000, 71000])

# Make a scatter plot: year on the x-axis, pop on the y-axis
plt.scatter(year, pop)

# Display the plot with plt.show()
plt.show()