import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 60, 2)
proportions = np.array([0.556, 0.500, 0.538, 0.533, 0.529, 0.526, 0.524, 0.632, 0.542, 0.560, 0.625, 0.571, 0.548,
                        0.581, 0.576, 0.541, 0.538, 0.550, 0.535, 0.545, 0.510, 0.510, 0.529, 0.509, 0.500])
plt.plot(sheep, proportions)

plt.xlabel("the number of sheep")
plt.ylabel("proportion")
plt.grid()
plt.xticks(np.arange(10, 60, 2))
plt.show()
fig.savefig('proportionOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')

