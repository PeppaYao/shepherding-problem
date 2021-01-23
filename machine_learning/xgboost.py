import numpy as np
from sklearn.tree import DecisionTreeRegressor

# 建议一个最大为 1 层的回归树弱学习器
weak_learner = DecisionTreeRegressor(max_depth=1)

x = np.array([[2], [-2], [-1], [3], [7]])  # 输入值
y = np.array([-1, 13, 5, 2, 9])  # 真实值

weak_learner.fit(x, y)  # F(x) 回归树
y_ = weak_learner.predict(x)  # 预测
print(y_)