import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 60, 2)
steps = np.array([605.000, 592.000, 493.000, 603.000, 729.000, 541.000, 523.000, 506.000, 476.000, 478.000, 460.000,
                  502.000, 493.000, 488.000, 481.000, 514.000, 519.000, 522.000, 556.000, 1081.000, 2477.000, 690.000,
                  2242.000, 777.000, 820.000])

plt.plot(sheep, steps)

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.grid()
plt.xticks(np.arange(10, 60, 2))
plt.show()
fig.savefig('stepOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')
