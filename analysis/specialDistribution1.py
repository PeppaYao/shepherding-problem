import numpy as np
import matplotlib.pyplot as plt
"""
离群羊不在目标区域
"""
fig, ax = plt.subplots()
n = 50
X = list()
for i in range(n-1):
    np.random.seed(i)
    x = np.random.randint(300, 400)
    y = np.random.randint(200, 350)
    X.append([x, y])

# outlier sheep
Y = np.array([50, 550])

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
# fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\outlier_sheep_init.pdf", dpi=600, format='pdf')