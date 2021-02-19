import numpy as np
import matplotlib.pyplot as plt
"""
沿着主对角线呈直线分布
"""
fig, ax = plt.subplots()
n = 50
X = list()

X = list()
Y = list()
for i in range(n):
    x = 120 + np.random.randint(5) + 8*i
    y = 550 - np.random.randint(5) - 8*i
    X.append([x, y])



# 离群点的特殊的一只羊,在目标区域
X = np.array(X)
# Y = np.array(Y)

plt.scatter(X[:, 0], X[:, 1], label="group A")
# plt.scatter(Y[:, 0], Y[:, 1], label="group B")
rangex = np.arange(0, 700, 100)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.xticks(rangex)
plt.yticks(rangex)
plt.grid()
plt.show()
#fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\line_init.pdf", dpi=600, format='pdf')