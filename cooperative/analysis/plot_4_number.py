import numpy as np
import matplotlib.pyplot as plt

# 四种最大角度策略
fig, ax = plt.subplots()
X = np.arange(20, 71)
# 随机
Y1 = np.array([1086.000, 432.000, 364.000, 792.000, 934.000, 1362.000, 1357.000, 772.000, 602.000, 1039.000, 1093.000, 451.000, 935.000, 1364.000, 1833.000, 1890.000, 1497.000, 1562.000, 1501.000, 1398.000, 1442.000, 1191.000, 1495.000, 1266.000, 1110.000, 563.000, 594.000, 545.000, 533.000, 641.000, 676.000, 632.000, 669.000, 632.000, 687.000, 890.000, 706.000, 688.000, 1003.000, 986.000, 1150.000, 924.000, 1183.000, 848.000, 1229.000, 1354.000, 1574.000, 1801.000, 1413.000, 728.000, 2455.000, ])
# 顺时针
Y2 = np.array([726.000, 596.000, 595.000, 588.000, 597.000, 588.000, 763.000, 620.000, 624.000, 756.000, 670.000, 641.000, 761.000, 830.000, 797.000, 858.000, 835.000, 815.000, 818.000, 848.000, 830.000, 865.000, 891.000, 867.000, 858.000, 873.000, 865.000, 727.000, 861.000, 947.000, 932.000, 795.000, 931.000, 935.000, 954.000, 945.000, 959.000, 1168.000, 975.000, 1022.000, 1167.000, 1192.000, 1189.000, 1192.000, 1234.000, 1288.000, 1254.000, 1303.000, 1322.000, 1280.000, 1302.000, ])


# 方向性
Y3 = np.array([334.000, 318.000, 308.000, 327.000, 321.000, 310.000, 342.000, 331.000, 341.000, 362.000, 372.000, 359.000, 379.000, 390.000, 394.000, 401.000, 406.000, 417.000, 405.000, 406.000, 401.000, 403.000, 407.000, 419.000, 410.000, 396.000, 401.000, 400.000, 384.000, 485.000, 473.000, 466.000, 475.000, 479.000, 494.000, 489.000, 489.000, 505.000, 503.000, 508.000, 509.000, 521.000, 521.000, 531.000, 557.000, 570.000, 553.000, 582.000, 563.000, 570.000, 578.000, ])

# 最大周长
Y4 = np.array([351.000, 342.000, 355.000, 374.000, 373.000, 394.000, 365.000, 389.000, 335.000, 383.000, 384.000, 447.000, 395.000, 393.000, 381.000, 408.000, 396.000, 406.000, 410.000, 425.000, 398.000, 402.000, 426.000, 405.000, 397.000, 380.000, 403.000, 404.000, 420.000, 491.000, 497.000, 488.000, 483.000, 501.000, 508.000, 507.000, 510.000, 503.000, 524.000, 540.000, 542.000, 531.000, 535.000, 569.000, 567.000, 614.000, 622.000, 600.000, 627.000, 597.000, 606.000, ])


plt.plot(X, Y1,  label="C1")
plt.plot(X, Y2,  label="C2")
plt.plot(X, Y3,  label="C3")
plt.plot(X, Y4,  label="C4")


plt.xlabel("the number of sheep")
plt.ylabel("steps")
# plt.xticks(np.arange(0, 100, 10))
plt.legend()
plt.xlim(20, 75)
plt.ylim(0, 2500)
plt.grid()
plt.show()