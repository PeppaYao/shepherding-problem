import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 0
idx = 62
sheep = np.array(
    [[224, 576], [85, 255], [221, 546], [413, 267], [170, 195], [403, 225], [442, 246], [223, 217], [499, 358],
     [433, 366], [316, 144], [457, 98], [381, 411], [388, 197], [160, 361], [507, 403], [218, 256], [159, 260],
     [349, 293], [145, 371], [403, 492], [505, 225], [421, 153], [133, 61], [469, 211], [180, 336], [360, 337],
     [72, 561], [307, 535], [520, 392], [341, 442], [259, 37], [268, 572], [72, 407], [468, 143], [249, 290],
     [183, 179], [450, 381], [467, 74], [441, 123], [374, 237], [496, 98], [154, 452], [375, 341], [326, 437],
     [509, 432], [242, 570], [188, 349], [53, 354], [476, 442], [228, 497], [110, 502], [203, 541], [77, 437],
     [164, 343], [509, 316], [391, 505], [514, 24], [339, 565], [229, 445], [255, 83], [152, 547], [69, 43], [95, 135],
     [501, 140], [350, 137], [71, 72], [371, 473], [367, 517], [103, 221], ]
)
shepherd = np.array([ 54.57434431, 551.02271233])
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
