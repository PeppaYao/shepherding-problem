import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 240
sheep = np.array(
    [[368, 315], [345, 349], [381, 297], [394, 313], [361, 334], [386, 338], [412, 323], [367, 354], [395, 438],
     [452, 406], [355, 319], [348, 320], [380, 324], [374, 328], [325, 371], [319, 450], [356, 354], [362, 340],
     [379, 364], [371, 334], [390, 367], [306, 374], [423, 295], [326, 335], [400, 325], [337, 356], [353, 381],
     [336, 344], [411, 255], [392, 351], [365, 369], [347, 334], [379, 311], [229, 389], [308, 360], [352, 363],
     [362, 328], [452, 429], [416, 275], [468, 244], [377, 339], [469, 228], [321, 354], [370, 383], [382, 356],
     [288, 375], [339, 375], [296, 388], [305, 273], [337, 333], ])
shepherd = np.array([288.09367028, 156.88233009])
ticks = np.arange(0, 700, 100)
plt.scatter(sheep[:, 0], 600-sheep[:, 1], c='g', label='sheep')
plt.scatter(shepherd[0], 600-shepherd[1], c='r', marker='p', label='shepherd')
line = np.array([[450, 0], [450, 150], [600, 150]])
plt.plot(line[:, 0], line[:, 1])
plt.text(460, 50, 'target area', fontsize=15)
plt.text(10, 570, 'driving', fontsize=15)
plt.text(10, 20, 'time steps: {}/2000'.format(step), fontsize=15)
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(0, 600)
plt.ylim(0, 600)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid()
plt.show()

#fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\step{}.pdf".format(step), dpi=600, format='pdf')
