import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 60
idx = 23
sheep = np.array(
    [[276, 239], [188, 248], [274, 539], [412, 293], [235, 216], [407, 253], [446, 274], [287, 255], [510, 385],
     [436, 392], [309, 173], [457, 127], [387, 447], [392, 220], [268, 351], [499, 430], [297, 281], [258, 269],
     [353, 330], [252, 358], [397, 527], [520, 265], [414, 177], [149, 84], [466, 245], [289, 326], [349, 366],
     [175, 290], [306, 564], [519, 419], [336, 463], [255, 71], [314, 315], [171, 392], [464, 164], [315, 301],
     [245, 204], [438, 422], [464, 93], [432, 163], [371, 286], [503, 120], [262, 436], [371, 363], [319, 467],
     [508, 478], [312, 341], [296, 338], [146, 320], [470, 472], ]
)
shepherd = np.array([63.3235962, 315.14925913])

# 计算最远距离
target_map = np.array([550, 550])
g_mean = np.array([np.mean(sheep[:, 0]), np.mean(sheep[:, 1])])
d = [la.norm(x - target_map) + la.norm(x - g_mean) for x in sheep]
idx = np.argmax(d)
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
plt.text(10, 20, 'time steps: {}/554'.format(step), fontsize=15)
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(0, 600)
plt.ylim(0, 600)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend(loc='upper right')
# plt.grid()
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\stepAngle{}x.pdf".format(step), dpi=600, format='pdf')
