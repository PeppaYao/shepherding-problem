import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(5, 105, 5)

Y = np.array([804.000, 709.000, 605.000, 759.000, 989.000, 881.000, 1012.000, 531.000, 926.000, 1179.000, 1262.000, 1345.000, 1237.000, 1297.000, 1550.000, 1819.000, 1527.000, 1772.000, 1727.000, 1575.000])
Y1 = np.array([713.000, 604.000, 548.000, 1128.000, 550.000, 585.000, 586.000, 593.000, 593.000, 655.000, 1277.000, 728.000, 1618.000, 1457.000, 1627.000, 1336.000, 898.000, 901.000, 1476.000, 938.000, ])
plt.plot(X, Y, '-o', label="distance")
plt.plot(X, Y1, '-o', label="angle")
plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()