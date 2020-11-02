import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.arange(5, 55, 5)
y = np.array([43, 46, 50, 48, 46, 49, 48, 49, 50, 50])
y1 = np.full(len(x), 50)

plt.bar(x, y1, color='red', label="total")
plt.bar(x, y, color='blue', label="partial")
plt.legend()
plt.xlabel("number of choice")
plt.ylabel("number of success")
plt.xticks(x)
plt.show()

fig.savefig('choose50.pdf', dpi=600, format='pdf')