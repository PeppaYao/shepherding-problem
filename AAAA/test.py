import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5, 55, 5)
y = np.array([43, 46, 50, 48, 46, 49, 48, 49, 50, 50])

plt.plot(x, y)
plt.grid()
plt.show()