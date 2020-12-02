import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 0
idx = 48
sheep = np.array(
    [[223, 95], [88, 286], [219, 63], [410, 201], [171, 222], [404, 254], [445, 252], [224, 247], [389, 412],
     [433, 396], [313, 174], [239, 131], [379, 206], [386, 227], [160, 391], [295, 444], [220, 288], [162, 292],
     [349, 323], [142, 158], [406, 322], [257, 360], [423, 180], [134, 280], [435, 240], [184, 364], [360, 368],
     [67, 233], [308, 55], [422, 287], [341, 352], [258, 138], [263, 91], [72, 437], [174, 407], [250, 319], [183, 146],
     [450, 411], [380, 101], [444, 153], [377, 269], [447, 128], [152, 394], [372, 368], [327, 289], [181, 426],
     [240, 374], [188, 441], [48, 99], [221, 231]])
shepherd = np.array([54.33802546, 551.05515657])
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
