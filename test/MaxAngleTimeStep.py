import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(40, 51)
Y1 = np.array([671.000, 1032.000, 896.000, 1106.000, 1194.000, 553.000, 1155.000, 1137.000, 726.000, 599.000, 923.000, ])
Y2 = np.array([1210.000, 601.000, 574.000, 573.000, 447.000, 1072.000, 1121.000, 1079.000, 1028.000, 1029.000, 988.000, ])
Y3 = np.array([479.000, 398.000, 783.000, 456.000, 598.000, 443.000, 443.000, 541.000, 430.000, 415.000, 437.000, ])


plt.plot(X, Y1, '-o', label="max distance")
plt.plot(X, Y2, '-o', label="max angle")
plt.plot(X, Y3, '-o', label="max perimeter")

plt.xlabel("displacement of target")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()