import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
PI = 180
X = np.array([PI/18, PI/9, PI/6, PI/4.5, PI/3.6, PI/3])


Y = np.array([471.000, 687.000, 725.000, 725.000, 725.000, 725.000])


plt.plot(X, Y,  label="N=20")



plt.xlabel("Angle(degrees)")
plt.ylabel("Time(steps)")
plt.legend()
plt.grid()
plt.show()
# fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\theta10to60.pdf", dpi=600, format='pdf')