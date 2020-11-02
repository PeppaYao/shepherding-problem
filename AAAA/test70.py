import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.arange(5, 55, 5)
y = np.array([1506, 1186, 1337, 1289, 1040, 977, 981, 1117, 1225, 1246, 1604, 1778, 1548, 1015])
y1 = np.full(len(x), 50)

plt.bar(x, y1, color='red', label="total")
plt.bar(x, y, color='blue', label="partial")
plt.legend()
plt.xlabel("number of choice")
plt.ylabel("number of success")
plt.xticks(x)
plt.show()

fig.savefig('choose50.pdf', dpi=600, format='pdf')