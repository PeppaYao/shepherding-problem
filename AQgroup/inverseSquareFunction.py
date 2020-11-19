import numpy as np
import matplotlib.pyplot as plt


def inv(x, s):
    epsilon = 1
    return (x/s + epsilon)**(-2)


fig, ax = plt.subplots()
T = np.arange(0, 100, 0.01)
Y = inv(T, 1)
Y2 = inv(T, 30)
plt.plot(T, Y, label="s = 1")
plt.plot(T, Y2, label="s = 30")
plt.xlabel("distance(pixels)")
plt.ylabel("function value")
plt.legend()
plt.show()
fig.savefig('inverseSquareFunction.pdf', dpi=600, format='pdf')

