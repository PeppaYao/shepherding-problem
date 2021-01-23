from sklearn.ensemble import RandomForestClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = RandomForestClassifier(n_estimators=10, random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))