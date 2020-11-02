import numpy as np

A = np.array([3, 4, 5, 6])
print("1-范数:", np.linalg.norm(A, ord=1))
print("2-范数:", np.linalg.norm(A, ord=2))
print("无穷范数:", np.linalg.norm(A, ord=np.inf))
