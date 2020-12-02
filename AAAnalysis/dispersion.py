import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(2, 91)

Y = np.array([36.000, 67.778, 108.000, 144.000, 171.694, 280.163, 270.859, 320.765, 384.260, 390.893, 396.965, 445.598, 470.168, 457.271, 573.273, 605.619, 728.262, 635.152, 740.320, 706.263, 625.240, 740.552, 809.116, 803.450, 772.917, 881.468, 822.203, 948.535, 844.569, 958.799, 993.062, 1122.766, 991.067, 1075.443, 1105.840, 1206.465, 1341.801, 1224.074, 1290.147, 1216.682, 1156.847, 1180.818, 1284.328, 1262.049, 1322.021, 1366.406, 1388.708, 1445.665, 1436.876, 1395.827, 1382.905, 1462.482, 1434.309, 1454.723, 1420.571, 1518.132, 1624.990, 1562.117, 1576.389, 1646.830, 1578.349, 1648.853, 1604.666, 1708.324, 1706.637, 1665.814, 1598.572, 1645.794, 1685.139, 1725.051, 1693.332, 1733.994, 1582.962, 1734.227, 1789.928, 1783.333, 1819.940, 1826.789, 1819.339, 1866.246, 1969.663, 1873.466, 1941.127, 1934.335, 1897.869, 1966.702, 1883.585, 1864.269, 1914.189])

Y2 = np.array([48.250, 60.222, 124.688, 172.800, 255.222, 208.163, 281.250, 309.975, 358.170, 391.917, 378.493, 451.716, 466.883, 463.431, 539.871, 614.443, 678.645, 705.795, 759.600, 664.195, 744.822, 652.900, 741.623, 911.331, 792.854, 855.133, 1002.494, 1021.765, 874.694, 990.874, 1010.428, 1031.286, 1035.396, 1159.414, 1145.064, 1287.908, 1188.057, 1213.709, 1202.100, 1241.580, 1277.751, 1347.527, 1346.730, 1401.922, 1378.905, 1325.847, 1529.388, 1322.907, 1379.920, 1305.164, 1324.612, 1437.102, 1435.095, 1512.210, 1543.694, 1464.630, 1511.001, 1463.459, 1607.994, 1533.787, 1596.700, 1639.620, 1717.412, 1691.858, 1657.061, 1688.285, 1689.780, 1619.966, 1779.852, 1744.437, 1770.671, 1848.562, 1834.849, 1845.714, 1753.228, 1781.221, 1828.023, 1871.644, 1858.835, 1925.933, 1849.809, 1911.713, 1966.090, 1965.792, 1906.027, 1989.688, 1884.147, 2087.601, 1980.448])


plt.plot(X, Y, 'darkcyan', label="MDAF")
plt.plot(X, Y2, 'silver', label="SPPL")


plt.xlabel("the number of sheep")
plt.ylabel("dispersion")
plt.xticks(np.arange(0, 100, 10))
plt.legend()
plt.xlim(0, 95)
plt.ylim(0, 2200)
plt.grid()
plt.show()
fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\dispersion_sheep2to90.pdf", dpi=600, format='pdf')