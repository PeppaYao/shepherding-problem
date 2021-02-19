import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 0
idx = 23
sheep = np.array(
    [[220, 240], [85, 286], [221, 575], [411, 297], [170, 223], [403, 255], [442, 277], [226, 247], [502, 389],
     [433, 399], [313, 173], [458, 128], [382, 438], [389, 224], [160, 391], [506, 435], [217, 289], [162, 292],
     [349, 326], [145, 400], [403, 525], [508, 257], [421, 182], [131, 91], [468, 243], [183, 364], [360, 368],
     [71, 339], [306, 568], [520, 422], [344, 469], [261, 64], [266, 358], [72, 437], [467, 173], [249, 320],
     [181, 211], [447, 413], [465, 101], [441, 156], [374, 270], [498, 131], [155, 482], [375, 369], [325, 470],
     [507, 462], [241, 418], [188, 378], [52, 383], [474, 473]]
)
shepherd = np.array([55.11663925, 551.00170095])
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
# plt.text(455, 40, 'destination region', fontsize=10)
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
