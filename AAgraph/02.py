import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(34, 62, 2)
steps_2 = np.array([867.000, 716.000, 747.000, 744.000, 736.000, 782.000, 743.000, 738.000, 897.000, 987.000, 1123.000,
                    1142.000, 1142.000, 1417.000])
steps_3 = np.array([809.000, 713.000, 743.000, 746.000, 745.000, 737.000, 780.000, 756.000, 905.000, 1481.000, 1516.000,
                    1146.000, 1387.000, 1477.000])

plt.plot(sheep, steps_2,  label='restricted view')
plt.plot(sheep, steps_3,  label='new restricted view')

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(34, 62, 4))
plt.show()