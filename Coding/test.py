import numpy as np

a = 10
dicts = {"hello": "world"}
X = np.array([100, 200])


def hello(dicts):
    dicts["hello"] = "tencent"
    print("before", dicts)


def testX(X):
    X[0] = 300


if __name__ == '__main__':
    # hello(dicts)
    testX(X)
    print("after", X)