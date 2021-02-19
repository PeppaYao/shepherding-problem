import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(10, 80, 10)
Y0 = np.array([942.000, 703.000, 1441.000, 756.000, 1345.000, 938.000, 768.000, ])
Y1 = np.array([1008.000, 607.000, 620.000, 630.000, 641.000, 628.000, 633.000, ])
Y2 = np.array([1291.000, 1063.000, 1054.000, 901.000, 1162.000, 867.000, 989.000, ])
Y3 = np.array([858.000, 796.000, 965.000, 999.000, 741.000, 692.000, 720.000, ])
# plt.plot(X, Y0, '-o', label="$N=40$")
plt.plot(X, Y1, '-o', label="$N=50$")
plt.plot(X, Y2, '-o', label="$N=60$")
plt.plot(X, Y3, '-o', label="$N=70$")
plt.xlabel("displacement of target")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()