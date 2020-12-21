import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X1 = np.arange(5,150,5)
Y1 = np.array([581,894,693,824,677,884,723,731,439,654,1124,1229,1299,1208,1261,1219,1225,1329,950,1030,1224,1886,1377,1864,1421,2030,1970,1376,1718])
Y2 = np.array([651,545,494,550,529,583,653,568,498,490,522,531,764,672,659,847,673,667,693,644,811,796,736,883,787,813,996,1038,886])
Y3 = np.array([546,435,444,523,454,493,500,463,514,558,531,573,649,638,608,541,675,683,705,753,730,748,771,778,806,780,730,781,856])

plt.plot(X1, Y1,'-o',label='SPPL')
plt.plot(X1, Y2,'-p',label='MAM')
plt.plot(X1, Y3,'-v',label='DMAM')

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(5,150,10))
plt.show()