import numpy as np
import matplotlib.pyplot as plt
import math
fig, ax = plt.subplots()
PI = 180
X = np.array([PI/18, PI/9, PI/6, PI/4.5, PI/3.6, PI/3])


Y = np.array([471.000, 687.000, 725.000, 725.000, 725.000, 725.000])
Y0 = np.array([593.000, 540.000, 690.000, 721.000, 741.000, 741.000])
Y1 = np.array([511.000, 587.000, 777.000, 780.000, 780.000, 780.000])
Y2 = np.array([563.000, 569.000, 838.000, 1072.000, 2001.000, 2001.000])
Y3 = np.array([531.000, 509.000, 922.000, 1182.000, 2001.000, 2001.000])

plt.plot(X, Y,  label="N=20")
plt.plot(X, Y0,  label="N=30")
plt.plot(X, Y1,  label="N=40")
plt.plot(X, Y2,  label="N=50")
plt.plot(X, Y3,  label="N=60")


plt.xlabel("Angle(degrees)")
plt.ylabel("Time(steps)")
plt.legend()
plt.grid()
plt.show()
fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\theta10to60.pdf", dpi=600, format='pdf')