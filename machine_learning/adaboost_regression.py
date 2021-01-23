from sklearn.ensemble import AdaBoostRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = AdaBoostRegressor(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))