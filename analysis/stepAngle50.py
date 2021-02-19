import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 50
idx = 62
sheep = np.array(
    [[264, 551], [152, 229], [271, 518], [422, 271], [195, 191], [402, 229], [447, 246], [234, 208], [500, 357],
     [431, 365], [313, 144], [450, 95], [386, 409], [378, 198], [255, 347], [504, 402], [258, 256], [221, 247],
     [349, 298], [238, 346], [414, 494], [503, 216], [422, 153], [130, 58], [479, 208], [277, 332], [359, 339],
     [169, 561], [301, 537], [518, 387], [348, 443], [260, 26], [296, 552], [156, 364], [466, 147], [278, 302],
     [197, 174], [445, 377], [459, 74], [444, 128], [368, 233], [490, 101], [243, 415], [377, 335], [328, 437],
     [503, 429], [278, 544], [284, 347], [134, 304], [486, 445], [281, 460], [202, 475], [262, 501], [160, 395],
     [259, 331], [515, 311], [389, 516], [504, 19], [336, 572], [291, 410], [249, 76], [234, 522], [65, 40], [103, 127],
     [498, 144], [355, 137], [76, 68], [370, 479], [366, 517], [153, 199] ]
)
shepherd = np.array([ 32.29967847, 356.29679251])
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
