### 说明
- 两只牧羊犬
- 基于最远距离
- 进行分类
- 最开始各自负责对应颜色的羊群
- 当附近羊的数量超过一半时，当前牧羊犬停止运动。身份转换为协调犬，将颜色错误的分类剔除。
### 评测机制
- 时间步数
- 分类结果
- 路径和轨迹
### 新规则
- 先各自聚集
- 一个在驱赶的时候，另一个必须静止。
- 两只犬之间有排斥
- 每只牧羊犬都单独的调用聚集和驱赶两种策略
### 2020.10.22
- 一只牧羊犬
- 基于KNN
- 羊无组别意识
- 最远距离
### bug
- 聚集部分羊之后，没有识别到离群点的羊。
### 2020.10.25
- 新增聚集完绿色羊之后所占比例
### 实验结果
- steps
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 60, 2)
steps = np.array([605.000, 592.000, 493.000, 603.000, 729.000, 541.000, 523.000, 506.000, 476.000, 478.000, 460.000,
                  502.000, 493.000, 488.000, 481.000, 514.000, 519.000, 522.000, 556.000, 1081.000, 2477.000, 690.000,
                  2242.000, 777.000, 820.000])

plt.plot(sheep, steps)

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.grid()
plt.xticks(np.arange(10, 60, 2))
plt.show()
fig.savefig('stepOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')
```
- proportions
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 60, 2)
proportions = np.array([0.556, 0.500, 0.538, 0.533, 0.529, 0.526, 0.524, 0.632, 0.542, 0.560, 0.625, 0.571, 0.548,
                        0.581, 0.576, 0.541, 0.538, 0.550, 0.535, 0.545, 0.510, 0.510, 0.529, 0.509, 0.500])
plt.plot(sheep, proportions)

plt.xlabel("the number of sheep")
plt.ylabel("proportion")
plt.grid()
plt.xticks(np.arange(10, 60, 2))
plt.show()
fig.savefig('proportionOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')

```
