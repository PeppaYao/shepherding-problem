import numpy as np
import matplotlib.pyplot as plt
"""
离群羊在目标区域
"""
fig, ax = plt.subplots()
n = 50
X = list()
for i in range(n-1):
    np.random.seed(i)
    x = np.random.randint(100, 300)
    y = np.random.randint(100, 300)
    X.append([x, y])

# 离群点的特殊的一只羊,在目标区域
Y = np.array([550, 50])

X = np.array(X)
plt.scatter(X[:, 0], X[:, 1], label="normal sheep")
plt.scatter(Y[0], Y[1], label="outlier sheep")
rangex = np.arange(0, 700, 100)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.xticks(rangex)
plt.yticks(rangex)
plt.grid()
plt.show()
# fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\outlier_sheep_target_init.pdf", dpi=600, format='pdf')