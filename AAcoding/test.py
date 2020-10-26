import numpy as np


if __name__ == '__main__':
    x = np.array([[1,2],[3,4]])
    y = x.copy()
    z = x
    y[0][1] = 33
    z[0][1] = 55
    print(x)
    print(y)
    print(z)
