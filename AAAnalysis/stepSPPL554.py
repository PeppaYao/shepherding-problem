import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 554

sheep = np.array(
    [[101, 140], [69, 116], [121, 191], [109, 165], [104, 154], [89, 190], [128, 177], [78, 198], [129, 133], [62, 203],
     [77, 166], [93, 165], [117, 155], [86, 116], [45, 122], [153, 162], [89, 167], [105, 196], [66, 189], [66, 135],
     [128, 163], [98, 120], [83, 140], [92, 105], [80, 160], [76, 128], [116, 172], [86, 155], [92, 204], [134, 148],
     [53, 172], [100, 176], [55, 188], [53, 143], [95, 179], [82, 177], [117, 143], [91, 130], [133, 120], [92, 148],
     [65, 172], [111, 128], [74, 147], [64, 148], [56, 164], [142, 171], [80, 180], [110, 183], [55, 127], [137, 186], ]
)
# 计算最远的羊
g_mean = np.array([np.mean(sheep[:, 0]), np.mean(sheep[:, 1])])
d = [np.linalg.norm(x - g_mean) for x in sheep]
idx = np.argmax(d)

shepherd = np.array([126.82785944, 294.93691162])
shepherd[1] = 600 - shepherd[1]


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
plt.legend(loc='upper right')
# plt.grid()
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\stepSPPL{}x.pdf".format(step), dpi=600, format='pdf')
