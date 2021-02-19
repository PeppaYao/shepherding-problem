import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(10, 70, 10)

Y = np.array([741.000, 700.000, 1056.000, 533.000, 1387.000, 1299.000])
Y2 = np.array([426.000, 500.000, 611.000, 643.000, 3556.000, 3562.000])
plt.plot(X, Y, '-o', label="center distance")
plt.plot(X, Y2, '-o', label="target distance")

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()