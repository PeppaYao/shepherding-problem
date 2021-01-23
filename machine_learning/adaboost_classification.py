# AdaBoost算法既能做分类分析，也能做回归分析
from sklearn.ensemble import AdaBoostClassifier
# 这里做分类
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]

model = AdaBoostClassifier(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))

