import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 400
idx = 62
sheep = np.array(
    [[292, 417], [258, 450], [334, 499], [339, 466], [263, 440], [352, 435], [308, 445], [270, 425], [432, 459],
     [343, 475], [289, 402], [312, 431], [322, 463], [325, 414], [284, 462], [508, 437], [270, 420], [267, 463],
     [281, 419], [278, 438], [439, 521], [331, 454], [328, 430], [306, 390], [315, 433], [286, 441], [302, 448],
     [275, 450], [330, 567], [509, 406], [329, 484], [334, 400], [281, 421], [299, 478], [333, 443], [294, 422],
     [278, 414], [379, 468], [346, 449], [296, 434], [296, 436], [355, 462], [315, 490], [305, 436], [316, 456],
     [504, 461], [296, 467], [296, 445], [281, 471], [470, 456], [346, 491], [299, 512], [320, 511], [309, 470],
     [283, 443], [471, 427], [384, 560], [437, 384], [342, 424], [310, 461], [308, 414], [296, 388], [266, 408],
     [305, 405], [323, 440], [319, 407], [278, 395], [368, 502], [364, 539], [248, 425], ]
)
shepherd = np.array([139.25848586, 379.00584878])
shepherd[1] = 600 - shepherd[1]

# 计算中心线的直线方程
sheep[:, 1] = 600-sheep[:, 1]
target = np.array([600, 0])
g_mean = np.array([np.mean(sheep[:, 0]), np.mean(sheep[:, 1])])

plt.scatter(g_mean[0], g_mean[1], marker='^', c='orange', label='center')


k = (g_mean[1] - target[1]) / (g_mean[0] - target[0])
b = g_mean[1] - k*g_mean[0]
x = np.arange(100, 560)
y = k*x + b
plt.plot(x, y, '-.')

#绕(600, 0)进行旋转
x0 = 560
y0 = 40
#逆时针旋转30度
theta = math.pi/6

#顺时针旋转30度
theta2 = 2*math.pi - theta

kk = (k*math.cos(theta) + math.sin(theta)) / (math.cos(theta) - k*math.sin(theta))
bb = ((k*x0 - y0)*(1-math.cos(theta)) - (x0+k*y0)*math.sin(theta)+b)/(math.cos(theta)-k*math.sin(theta))

k2 = (k*math.cos(theta2) + math.sin(theta2)) / (math.cos(theta2) - k*math.sin(theta2))
b2 = ((k*x0 - y0)*(1-math.cos(theta2)) - (x0+k*y0)*math.sin(theta2)+b)/(math.cos(theta)-k*math.sin(theta2))

yy = kk*x + bb
y2 = k2*x + b2

plt.plot(x, yy, '-.')
plt.plot(x, y2, '-.')

# # 画圆
# fn = 60.0
# xc = np.linspace(0, 600, 3000)
# x1 = np.linspace(g_mean[0], g_mean[1], 3000)
#
# yc1 = g_mean[1] + np.sqrt(fn**2 -(xc - g_mean[0])**2)
# yc2 = g_mean[1] - np.sqrt(fn**2 -(xc - g_mean[0])**2)
#
# plt.plot(xc, yc1, 'y')
# plt.plot(xc, yc2, 'y')


ticks = np.arange(0, 700, 100)
plt.scatter(sheep[:, 0], sheep[:, 1], c='g', label='sheep')
plt.scatter(shepherd[0], shepherd[1], c='r', marker='p', label='shepherd')
plt.scatter(sheep[idx][0], sheep[idx][1], c='b', label='outermost sheep')
line = np.array([[450, 0], [450, 150], [600, 150]])

plt.plot(line[:, 0], line[:, 1], 'c')
plt.text(460, 20, 'target area', fontsize=15)
plt.text(10, 570, 'collecting', fontsize=15)
plt.text(10, 20, 'time steps: {}/2000'.format(step), fontsize=15)
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(0, 600)
plt.ylim(0, 600)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend(loc='upper right')
plt.grid()
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\stepAngle{}.pdf".format(step), dpi=600, format='pdf')
