import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 150
idx = 28
sheep = np.array(
    [[388, 302], [344, 315], [284, 543], [414, 300], [369, 295], [401, 290], [439, 273], [372, 309], [510, 398],
     [447, 401], [392, 275], [456, 131], [398, 439], [408, 266], [310, 355], [502, 434], [373, 320], [359, 317],
     [352, 345], [292, 366], [403, 532], [514, 269], [432, 214], [317, 127], [473, 242], [342, 334], [343, 359],
     [323, 339], [304, 561], [523, 408], [342, 462], [370, 143], [354, 333], [233, 407], [477, 164], [367, 328],
     [385, 285], [429, 419], [477, 79], [441, 186], [384, 312], [506, 124], [275, 437], [377, 362], [320, 474],
     [493, 473], [326, 354], [334, 342], [271, 368], [480, 482], ]
)
shepherd = np.array([235.71462219, 111.62548576])
shepherd[1] = 600 - shepherd[1]
# 计算最远的羊
g_mean = np.array([np.mean(sheep[:, 0]), np.mean(sheep[:, 1])])
d = [np.linalg.norm(x - g_mean) for x in sheep]
idx = np.argmax(d)
# 计算中心线的直线方程
sheep[:, 1] = 600-sheep[:, 1]
target = np.array([560, 40])
g_mean = np.array([np.mean(sheep[:, 0]), np.mean(sheep[:, 1])])




k = (g_mean[1] - target[1]) / (g_mean[0] - target[0])
b = g_mean[1] - k*g_mean[0]
x = np.arange(0, 560)
y = k*x + b
# plt.plot(x, y, '-.', c='lightgray')

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
b2 = ((k*x0 - y0)*(1-math.cos(theta2)) - (x0+k*y0)*math.sin(theta2)+b)/(math.cos(theta2)-k*math.sin(theta2))

yy = kk*x + bb
y2 = k2*x + b2

# plt.plot(x, yy, '-.', c='lightgray')
# plt.plot(x, y2, '-.', c='lightgray')

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
plt.scatter(sheep[idx][0], sheep[idx][1], c='b', label='target sheep')
plt.scatter(g_mean[0], g_mean[1], marker='^', c='orange', label='center')
line = np.array([[450, 0], [450, 150], [600, 150]])

plt.plot(line[:, 0], line[:, 1], 'c')
plt.text(455, 50, 'destination', fontsize=15)
plt.text(455, 20, 'region', fontsize=15)
plt.text(10, 570, 'collecting', fontsize=15)
plt.text(10, 20, 'time steps: {}/1395'.format(step), fontsize=15)
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(0, 600)
plt.ylim(0, 600)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend(loc='center left')
# plt.grid()
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\stepSPPL{}x.pdf".format(step), dpi=600, format='pdf')
