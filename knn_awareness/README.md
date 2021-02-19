### 策略说明
2020.10.22 
- 一只犬
- 两类羊
- 羊有组别意识
- 基于KNN
- 最远距离
### 补充内容
- 统计完成牧羊犬任务时最终到达目标区域的羊数量占初始羊群数量的比例
- 统计完成牧羊犬任务时的时间步数
### 实验结果
- 统计时间步数
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
steps = np.array([688.000, 717.000, 506.000, 818.000, 705.000, 567.000, 680.000, 871.000, 807.000, 789.000, 851.000,
                  760.000, 772.000, 770.000, 821.000, 760.000, 908.000, 996.000, 873.000, 749.000, 1131.000, 872.000,
                  895.000, 543.000, 549.000, 772.000])

plt.plot(sheep, steps)

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.grid()
plt.xticks(np.arange(10, 62, 2))
plt.show()
fig.savefig('stepOfConsciousSheepOneHerd.pdf', dpi=600, format='pdf')

```
- 统计最终成功率
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
greens = np.array([5.000, 6.000, 7.000, 8.000, 9.000, 10.000, 11.000, 12.000, 13.000, 14.000, 15.000, 16.000, 17.000,
                   18.000, 19.000, 20.000, 21.000, 22.000, 23.000, 24.000, 25.000, 26.000, 27.000, 28.000, 29.000,
                   30.000])
blues = np.array([3.000, 6.000, 7.000, 8.000, 9.000, 10.000, 10.000, 11.000, 11.000, 12.000, 15.000, 14.000, 17.000,
                  15.000, 19.000, 19.000, 19.000, 21.000, 19.000, 24.000, 24.000, 25.000, 23.000, 24.000, 27.000,
                  29.000])
sheepRates = (greens + blues) / (2 * greens)

plt.plot(sheep, sheepRates)

plt.xlabel("the number of sheep")
plt.ylabel("successful rate")
plt.grid()
plt.xticks(np.arange(10, 62, 2))
plt.show()
fig.savefig('successfulRateOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')
```
- 有意识和无意识的对比成功率
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
greens = np.array([5.000, 6.000, 7.000, 8.000, 9.000, 10.000, 11.000, 12.000, 13.000, 14.000, 15.000, 16.000, 17.000,
                   18.000, 19.000, 20.000, 21.000, 22.000, 23.000, 24.000, 25.000, 26.000, 27.000, 28.000, 29.000,
                   30.000])
blues = np.array([3.000, 6.000, 7.000, 8.000, 9.000, 10.000, 10.000, 11.000, 11.000, 12.000, 15.000, 14.000, 17.000,
                  15.000, 19.000, 19.000, 19.000, 21.000, 19.000, 24.000, 24.000, 25.000, 23.000, 24.000, 27.000,
                  29.000])
sheepRates = (greens + blues) / (2 * greens)

greens_1 = np.array([5.000, 6.000, 7.000, 8.000, 9.000, 10.000, 11.000, 12.000, 13.000, 14.000, 15.000, 16.000, 17.000,
                     18.000, 19.000, 20.000, 21.000, 22.000, 23.000, 24.000, 25.000, 26.000, 27.000, 28.000, 29.000,
                     30.000])
blues_1 = np.array([4.000, 6.000, 6.000, 7.000, 8.000, 9.000, 10.000, 7.000, 11.000, 11.000, 9.000, 12.000, 14.000,
                    13.000, 14.000, 17.000, 18.000, 18.000, 20.000, 20.000, 24.000, 25.000, 24.000, 27.000, 29.000,
                    30.000])
sheepRates_1 = (greens_1 + blues_1) / (2 * greens_1)


plt.plot(sheep, sheepRates_1, '-o', label='unconscious')
plt.plot(sheep, sheepRates, '-o', label='conscious')

plt.xlabel("the number of sheep")
plt.ylabel("successful rate")
plt.legend()
plt.grid()
plt.xticks(np.arange(10, 62, 2))
plt.show()
fig.savefig('successfulRateOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')
```
- 时间步数对比
```py
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sheep = np.arange(10, 62, 2)
steps_1 = np.array([605.000, 592.000, 493.000, 603.000, 729.000, 541.000, 523.000, 506.000,
                    476.000, 478.000, 460.000, 502.000, 493.000, 488.000, 481.000, 514.000,
                    519.000, 522.000, 556.000, 1081.000, 2477.000, 690.000, 2242.000, 777.000,
                    820.000, 948.000])
steps_2 = np.array([688.000, 717.000, 506.000, 818.000, 705.000, 567.000, 680.000, 871.000, 807.000, 789.000, 851.000,
                    760.000, 772.000, 770.000, 821.000, 760.000, 908.000, 996.000, 873.000, 749.000, 1131.000, 872.000,
                    895.000, 543.000, 549.000, 772.000])
plt.plot(sheep, steps_1, '-o', label='unconscious')
plt.plot(sheep, steps_2, '-o', label='conscious')

plt.xlabel("the number of sheep")
plt.ylabel("time steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(10, 62, 2))
plt.show()
fig.savefig('stepsOfGreenSheepOneHerd.pdf', dpi=600, format='pdf')
```
