### 策略说明 
2020.10.22
- 一只牧羊犬
- 两类羊
- 基于KNN
- 羊无组别意识
- 最远距离
### 补充内容
- 聚集部分羊之后，没有识别到离群点的羊。2020.10.24已修复
- 新增统计聚集完绿色羊之后所占比例。2020.10.25实现
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
