import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
PI = 180
X = np.array([PI/18, PI/9, PI/6, PI/4.5, PI/3.6, PI/3])

Y0 = np.array([593.000, 570.000, 570.000, 570.000, 570.000, 570.000])
Y1 = np.array([511.000, 587.000, 399.000, 399.000, 399.000, 399.000])
Y2 = np.array([563.000, 569.000, 618.000, 516.000, 516.000, 516.000])
Y3 = np.array([531.000, 509.000, 566.000, 578.000, 578.000, 578.000])
Y4 = np.array([637.000, 604.000, 533.000, 531.000, 531.000, 531.000])

plt.plot(X, Y0,  label="N=30")
plt.plot(X, Y1,  label="N=40")
plt.plot(X, Y2,  label="N=50")
plt.plot(X, Y3,  label="N=60")
plt.plot(X, Y4,  label="N=70")


plt.xlabel("degrees")
plt.ylabel("time steps")
plt.legend()
plt.xlim(10, 65)
plt.ylim(300, 700)
plt.grid()
plt.show()
fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\theta10to60_improved.pdf", dpi=600, format='pdf')