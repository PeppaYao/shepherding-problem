import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
steps_1 = np.array([675.000, 658.000, 692.000, 657.000, 686.000, 666.000, 660.000, 664.000, 721.000, 684.000, 683.000,
                    712.000, 996.000, 2010.000, 963.000, 816.000, 1028.000, 857.000, 1014.000, 895.000, 3059.000,
                    2232.000, 2967.000, 2147.000, 1889.000, 3508.000])
steps_2 = np.array([713.000, 767.000, 748.000, 762.000, 719.000, 771.000, 910.000, 965.000, 964.000, 787.000, 959.000,
                    967.000, 1128.000, 1062.000, 1069.000, 1115.000, 1272.000, 1224.000, 1375.000, 1288.000, 1250.000,
                    1238.000, 1857.000, 1177.000, 1516.000, 1321.000])

steps_3 = np.array([653.000, 664.000, 698.000, 661.000, 676.000, 677.000, 681.000, 670.000, 707.000, 681.000, 693.000,
                    704.000, 969.000, 951.000, 2748.000, 4001.000, 4001.000, 3421.000, 863.000, 1038.000, 2547.000,
                    1723.000, 2795.000, 1760.000, 1962.000, 1873.000])

plt.plot(sheep, steps_1,  label='k neighbor')
plt.plot(sheep, steps_2,  label='restricted view')
plt.plot(sheep, steps_3,  label='new restricted view')

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(10, 62, 4))
plt.show()
# fig.savefig('contrastStepsOfBasicModel.pdf', dpi=600, format='pdf')