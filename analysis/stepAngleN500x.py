import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 500
sheep = np.array(
    [[419, 547], [431, 562], [428, 531], [464, 474], [451, 463], [412, 487], [434, 500], [423, 477], [447, 525],
     [439, 478], [440, 504], [449, 494], [421, 496], [466, 490], [467, 540], [488, 511], [493, 495], [478, 495],
     [431, 551], [393, 520], [433, 526], [427, 512], [440, 509], [470, 508], [414, 516], [428, 466], [441, 537],
     [453, 565], [472, 527], [513, 519], [477, 482], [458, 503], [461, 553], [457, 531], [435, 524], [418, 530],
     [433, 485], [419, 521], [457, 512], [432, 509], [401, 498], [470, 517], [401, 531], [449, 487], [409, 507],
     [483, 521], [400, 543], [447, 551], [450, 535], [487, 542]])
shepherd = np.array([301.50865066, 473.73544102])
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
plt.scatter(g_mean[0], g_mean[1], marker='^', c='orange', label='center')
# plt.scatter(sheep[idx][0], sheep[idx][1], c='b', label='outermost sheep')
line = np.array([[450, 0], [450, 150], [600, 150]])

plt.plot(line[:, 0], line[:, 1], 'c')
# plt.text(460, 20, 'target area', fontsize=15)
plt.text(10, 570, 'driving', fontsize=15)
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
