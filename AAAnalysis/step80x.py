import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 80
idx = 48
sheep = np.array(
    [[221, 101], [225, 236], [212, 64], [405, 199], [259, 210], [408, 259], [445, 248], [264, 239], [385, 421],
     [428, 398], [314, 177], [245, 139], [387, 208], [384, 225], [261, 325], [301, 453], [260, 269], [266, 257],
     [352, 319], [207, 152], [402, 336], [279, 349], [419, 181], [255, 247], [427, 235], [266, 298], [349, 368],
     [181, 193], [301, 55], [413, 285], [330, 339], [259, 152], [246, 91], [204, 372], [256, 342], [271, 313],
     [226, 144], [456, 412], [373, 88], [458, 144], [399, 279], [441, 125], [259, 308], [373, 374], [321, 291],
     [269, 360], [275, 335], [272, 374], [87, 78], [259, 222]])
shepherd = np.array([14.57785861, 239.39961625])
ticks = np.arange(0, 700, 100)

plt.scatter(sheep[:, 0], 600-sheep[:, 1], c='g', label='sheep')
plt.scatter(shepherd[0], 600-shepherd[1], c='r', marker='p', label='shepherd')
plt.scatter(sheep[idx][0], 600-sheep[idx][1], c='b', label='outermost sheep')
line = np.array([[450, 0], [450, 150], [600, 150]])
plt.plot(line[:, 0], line[:, 1])
plt.text(460, 50, 'target area', fontsize=15)
plt.text(10, 570, 'collecting', fontsize=15)
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

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\step80.pdf", dpi=600, format='pdf')
