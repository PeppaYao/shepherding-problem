import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ratio = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
X = np.array(ratio)
Y1 = np.array([779.000, 1032.000, 609.000, 730.000, 654.000, 628.000, ])
Y2 = np.array([802.000, 852.000, 818.000, 804.000, 1147.000, 867.000, ])
Y3 = np.array([862.000, 927.000, 932.000, 1090.000, 980.000, 692.000, ])
plt.plot(X, Y1, '-o', label="$N=50$")
plt.plot(X, Y2, '-o', label="$N=60$")
plt.plot(X, Y3, '-o', label="$N=70$")
plt.xlabel("speed ratio")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()