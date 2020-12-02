import math

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(600)
y = -x + 600
k = -1
b = 600
#绕(600, 0)进行旋转
x0 = 600
y0 = 0
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

plt.plot(x, y)
plt.plot(x, yy)
plt.plot(x, y2)

plt.xlim(0, 600)
plt.ylim(0, 600)
plt.show()