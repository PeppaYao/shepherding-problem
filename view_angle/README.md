### 策略说明
- 一只犬
- 一类羊
- 视野距离
- 最大角度
### 补充说明
### 实验结果
- 时间步数四种模型
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
steps_1 = np.array([622.000, 606.000, 679.000, 648.000, 632.000, 613.000, 615.000, 618.000, 620.000, 629.000, 640.000, 633.000, 866.000, 736.000, 758.000, 760.000, 713.000, 753.000, 709.000, 729.000, 913.000, 950.000, 920.000, 1122.000, 1172.000, 1442.000])
steps_2 = np.array([636.000, 625.000, 693.000, 665.000, 652.000, 627.000, 655.000, 905.000, 880.000, 728.000, 641.000, 925.000, 835.000, 716.000, 734.000, 783.000, 746.000, 719.000, 743.000, 791.000, 653.000, 627.000, 671.000, 775.000, 1271.000, 1360.000])
steps_3 = np.array([632.000, 595.000, 624.000, 586.000, 602.000, 620.000, 653.000, 880.000, 959.000, 959.000, 968.000, 1021.000, 692.000, 707.000, 707.000, 703.000, 894.000, 843.000, 883.000, 1048.000, 1662.000, 1400.000, 1175.000, 1494.000, 1200.000, 1238.000])
steps_4 = np.array([655.000, 600.000, 636.000, 566.000, 586.000, 614.000, 1001.000, 581.000, 929.000, 767.000, 602.000, 906.000, 697.000, 718.000, 716.000, 713.000, 896.000, 737.000, 793.000, 772.000, 711.000, 643.000, 768.000, 827.000, 754.000, 702.000])

plt.plot(sheep, steps_1,  label='knn+distance')
plt.plot(sheep, steps_2,  label='knn+angle')
plt.plot(sheep, steps_3,  label='view+distance')
plt.plot(sheep, steps_4,  label='view+angle')

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(10, 62, 4))
plt.show()
```