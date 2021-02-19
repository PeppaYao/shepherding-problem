import numpy as np
from numpy import linalg as LA


def sheeps_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, index_g):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    g_sh_array = all_sheep[index_g]
    b_sh_array = all_sheep[index_b]
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(per_sheep - herd_a_pos)
        if per_sheep in g_sh_array:
            l_mean, ra = knn(per_sheep, g_sh_array, n // 2 + 5, r_rep)
        else:
            l_mean, ra = knn(per_sheep, b_sh_array, n // 2 + 5, r_rep)

        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)  # H为-1到1随机运动的大小
            H = H / np.linalg.norm(H)  # 把数据归一化
            H = 0.1 * last_vector[i] + 2 * ra + 0.3 * H
            H = H / np.linalg.norm(H)
        else:
            rs = (per_sheep - herd_a_pos) / ps_dist
            C = (l_mean - per_sheep) / np.linalg.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.5 * last_vector[i] + 5 * C + rs + 2 * ra + 0.3 * e / np.linalg.norm(e)
            H = H / np.linalg.norm(H)
            H = H * speed

        last_vector[i] = H
        sheep_dict['sheep' + str(i)].x = H[0]
        sheep_dict['sheep' + str(i)].y = H[1]
        sheep_dict['sheep' + str(i)].draw()
        new_position[i] = H

    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_position[i] + per_sheep


def knn(per_sheep, all_sheep, k, repulsion_distance):
    """
    根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向
    """
    d = [LA.norm(per_sheep - sheep) for sheep in all_sheep]
    near = np.argsort(d)
    top = [all_sheep[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float64)
    ra = np.zeros(2, dtype=np.float64)
    for p in near[1:k + 1]:
        if d[p] <= repulsion_distance:
            ra += (per_sheep - all_sheep[p]) / LA.norm(per_sheep - all_sheep[p])
    return local_m, ra