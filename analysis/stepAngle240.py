import matplotlib.pyplot as plt
import numpy as np
import math
np.seterr(invalid='ignore')
fig, ax = plt.subplots()
step = 240
sheep = np.array(
    [[368, 315], [345, 349], [381, 297], [394, 313], [361, 334], [386, 338], [412, 323], [367, 354], [395, 438],
     [452, 406], [355, 319], [348, 320], [380, 324], [374, 328], [325, 371], [319, 450], [356, 354], [362, 340],
     [379, 364], [371, 334], [390, 367], [306, 374], [423, 295], [326, 335], [400, 325], [337, 356], [353, 381],
     [336, 344], [411, 255], [392, 351], [365, 369], [347, 334], [379, 311], [229, 389], [308, 360], [352, 363],
     [362, 328], [452, 429], [416, 275], [468, 244], [377, 339], [469, 228], [321, 354], [370, 383], [382, 356],
     [288, 375], [339, 375], [296, 388], [305, 273], [337, 333], ])
shepherd = np.array([288.09367028, 600-156.88233009])

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
line = np.array([[450, 0], [450, 150], [600, 150]])

plt.plot(line[:, 0], line[:, 1], 'c')
plt.text(460, 20, 'target area', fontsize=15)
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

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\stepAngle{}.pdf".format(step), dpi=600, format='pdf')
