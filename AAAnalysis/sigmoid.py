import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 20, 0.1)
y = 1/(1 + np.exp(-(x - 10)))

plt.plot(x, y)
plt.show()
