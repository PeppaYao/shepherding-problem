import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 466
sheep = np.array(
 [[551, 493], [458, 519], [526, 501], [509, 473], [520, 461], [517, 481], [508, 509], [491, 470], [515, 518],
  [494, 496], [551, 512], [501, 552], [523, 491], [539, 508], [470, 542], [484, 532], [467, 566], [534, 459],
  [478, 504], [536, 500], [483, 484], [487, 524], [509, 504], [523, 545], [497, 505], [464, 524], [479, 519],
  [458, 553], [539, 524], [482, 515], [469, 507], [486, 567], [502, 493], [497, 541], [485, 547], [529, 478],
  [544, 480], [536, 541], [501, 511], [520, 514], [534, 490], [524, 531], [472, 557], [496, 486], [467, 494],
  [500, 531], [503, 516], [512, 537], [456, 538], [514, 554]])
shepherd = np.array([427.48232424, 445.85210883])
ticks = np.arange(0, 700, 100)
plt.scatter(sheep[:, 0], 600-sheep[:, 1], c='g', label='sheep')
plt.scatter(shepherd[0], 600-shepherd[1], c='r', marker='p', label='shepherd')
line = np.array([[450, 0], [450, 150], [600, 150]])
plt.plot(line[:, 0], line[:, 1])
# plt.text(480, 80, 'target area')
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

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\step{}.pdf".format(step), dpi=600, format='pdf')
