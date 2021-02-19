import numpy as np
import matplotlib.pyplot as plt
"""
沿着主对角线上的两个子群
"""
fig, ax = plt.subplots()
n = 50
X = list()
Y = list()
for i in range(n):
    # np.random.seed(i+20)
    np.random.seed(i)
    if i % 2 == 0:
        x = np.random.randint(150, 250)
        y = np.random.randint(150, 250)
        X.append([x, y])
    else:
        x = np.random.randint(380, 480)
        y = np.random.randint(380, 480)
        Y.append([x, y])


# 离群点的特殊的一只羊,在目标区域
X = np.array(X)
Y = np.array(Y)

plt.scatter(X[:, 0], 600 - X[:, 1], label="group A")
plt.scatter(Y[:, 0], 600 - Y[:, 1], label="group B")
rangex = np.arange(0, 700, 100)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.xticks(rangex)
plt.yticks(rangex)
plt.grid()
U = np.arange(0, 100)
plt.plot(U, U, label="fasdf")
plt.legend()
plt.show()
# fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\subgroup_init.pdf", dpi=600, format='pdf')