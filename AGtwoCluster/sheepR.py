import numpy as np


def sheeps_move(shepherd_position, all_sheep,
                sheep_view_distance, repulsion_distance, speed, sheep_dict, last_vector):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        point = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(point - shepherd_position)
        l_mean, ra = knn(point, all_sheep, n//2+5, repulsion_distance)
        if ps_dist > sheep_view_distance:
            H = np.random.uniform(-1, 1, size=2)  # H为-1到1随机运动的大小
            H = H / np.linalg.norm(H)  # 把数据归一化
            H = 0.1 * last_vector[i] + 2 * ra + 0.3 * H
            H = H / np.linalg.norm(H)
        else:
            rs = (point - shepherd_position) / ps_dist
            C = (l_mean - point) / np.linalg.norm(l_mean - point)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + rs + 2 * ra + 0.3 * e / np.linalg.norm(e)
            H = H / np.linalg.norm(H)
            H = H * speed

        last_vector[i] = H
        sheep_dict['sheep' + str(i)].x = H[0]
        sheep_dict['sheep' + str(i)].y = H[1]
        sheep_dict['sheep' + str(i)].draw()
        new_position[i] = H
    for i in range(n):
        point = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_position[i] + point

    return all_sheep


def knn(x, others, k, Ra):
    """根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向"""
    d = [np.linalg.norm(x - x_) for x_ in others]
    near = np.argsort(d)
    top = [others[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float32)
    ra = np.zeros(2, dtype=np.float32)
    for p in near[1:k + 1]:
        if d[p] <= Ra:
            ra += (x - others[p]) / np.linalg.norm(x - others[p])
    return local_m, ra