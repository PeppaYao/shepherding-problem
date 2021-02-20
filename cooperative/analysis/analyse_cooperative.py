import numpy as np
import matplotlib.pyplot as plt

# 合作：最远距离+驱赶
# 合作：最大角度+驱赶
fig, ax = plt.subplots()
X = np.arange(40, 51)

Y = np.array([1442.000, 1191.000, 1495.000, 1266.000, 1110.000, 563.000, 594.000, 545.000, 533.000, 641.000, 676.000, ])
Y2 = np.array([4001.000, 2179.000, 2610.000, 4001.000, 4001.000, 2017.000, 1599.000, 3604.000, 1222.000, 2871.000, 4001.000, ])

plt.plot(X, Y, 'purple', label="mam")
plt.plot(X, Y2, 'darkcyan', label="sppl")


plt.xlabel("the number of sheep")
plt.ylabel("dispersion")
# plt.xticks(np.arange(0, 100, 10))
plt.legend()
plt.xlim(40, 51)
plt.ylim(0, 4200)
plt.grid()
plt.show()