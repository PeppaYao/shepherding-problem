import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 160
idx = 48
sheep = np.array(
    [[339, 186], [272, 263], [326, 150], [413, 203], [296, 245], [404, 255], [434, 241], [297, 258], [394, 427],
     [439, 397], [352, 195], [331, 201], [385, 194], [384, 212], [257, 323], [306, 454], [274, 282], [288, 271],
     [355, 319], [313, 237], [412, 341], [286, 351], [428, 178], [258, 279], [419, 240], [258, 289], [346, 370],
     [280, 255], [349, 112], [409, 295], [338, 344], [327, 212], [342, 174], [216, 377], [250, 333], [287, 314],
     [317, 226], [450, 432], [379, 123], [452, 144], [395, 272], [441, 133], [242, 305], [366, 371], [333, 278],
     [260, 351], [282, 327], [274, 374], [225, 137], [286, 242]])
shepherd = np.array([161.37072934, 62.08922441])
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

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\step{}.pdf".format(step), dpi=600, format='pdf')
