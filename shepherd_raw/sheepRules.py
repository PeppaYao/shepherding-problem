import numpy as np


def sheeps_move(herd, array, agent):
    """羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于100米，则羊只进行简单的随机运动，否则牧羊犬会受到五个不同方向的线性合力"""
    n = len(array)
    last = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        point = agent['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(point - herd)
        l_mean, ra = knn(point, array, 20)
        if ps_dist > 250:
            H = np.random.uniform(-1, 1, size=2)  # H为-1到1随机运动的大小
            H = H / np.linalg.norm(H)  # 把数据归一化
            last[i] = H
        else:
            rs = (point - herd) / ps_dist
            C = (l_mean - point) / np.linalg.norm(l_mean - point)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.5 * last[i] + 1.05 * C + rs + 2 * 1.0 * ra + 0.3 * e / np.linalg.norm(e)
            H = H / np.linalg.norm(H)
            last[i] = H
            H = H * 5
        agent['sheep' + str(i)].x = H[0]
        agent['sheep' + str(i)].y = H[1]
        agent['sheep' + str(i)].draw()
        array[i] = last[i] + point


def knn(x, others, k):  # 用在sheeps_move这个函数中
    """根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向"""
    d = [np.linalg.norm(x - x_) for x_ in others]
    near = np.argsort(d)
    top = [others[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float32)
    ra = np.zeros(2, dtype=np.float32)
    for p in near[1:k + 1]:
        if d[p] <= 14:
            ra += (x - others[p]) / np.linalg.norm(x - others[p])
    return local_m, ra
