import numpy as np

x = np.array([1, 4, 5, 9, 0])
color = ['green', 'blue', 'blue', 'green', 'blue']
y = np.argsort(x)  # 返回从小到大排序后的下标
green_proportion = list()
count_green = 0
count_blue = 0
for index in y:
    if color[index] == 'blue':
        count_blue += 1
    else:
        count_green += 1
    if count_blue == 0:
        green_proportion.append(0)
    else:
        green_proportion.append(count_green/count_blue)  # 目标类别占比越高 越可能作为分割点
print(green_proportion)
np_green_proportion = np.array(green_proportion)
max_green_proportion = np.argmax(green_proportion)  # 最大值的下标
print(max_green_proportion)
