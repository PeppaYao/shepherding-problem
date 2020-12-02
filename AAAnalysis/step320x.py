import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
step = 320
sheep = np.array(
    [[401, 383], [378, 406], [436, 394], [421, 416], [378, 395], [400, 409], [426, 438], [398, 410], [415, 459],
     [411, 442], [391, 370], [353, 418], [411, 403], [427, 382], [381, 435], [401, 458], [377, 416], [390, 397],
     [392, 429], [411, 391], [408, 423], [371, 448], [433, 421], [338, 446], [412, 419], [377, 428], [396, 449],
     [363, 425], [448, 401], [422, 428], [386, 424], [360, 408], [419, 402], [350, 465], [360, 446], [388, 404],
     [379, 378], [432, 456], [434, 414], [469, 401], [398, 396], [482, 385], [364, 436], [399, 442], [398, 418],
     [367, 458], [381, 458], [384, 469], [365, 391], [351, 434]])
shepherd = np.array([311.13327777, 315.04755436])
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

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\step{}.pdf".format(step), dpi=600, format='pdf')
