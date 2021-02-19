import numpy as np
from numpy import linalg as la


def sheep_move(herd_1_point, herd_2_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, p, q):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """

    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        cur_sheep = sheep_dict['sheep' + str(i)]
        if not cur_sheep.status:
            continue

        per_sheep = cur_sheep.position2point()
        ps_dist_1 = la.norm(per_sheep - herd_1_point)
        ps_dist_2 = la.norm(per_sheep - herd_2_point)

        l_mean, ra = knn(per_sheep, all_sheep, n // 2 + 1, r_rep)
        rs_1 = np.array([0, 0])
        rs_2 = np.array([0, 0])
        tag = 0
        if p != 0 and ps_dist_1 <= r_dist:
            rs_1 = (per_sheep - herd_1_point) / ps_dist_1
            tag += 1

        if q != 0 and ps_dist_2 <= r_dist:
            rs_2 = (per_sheep - herd_2_point) / ps_dist_2
            tag += 1

        # print(per_sheep)
        if tag == 0:
            H = np.random.uniform(-1, 1, size=2)
            H = H / la.norm(H)
            H = 0.1 * last_vector[i] + 2 * ra + 0.3 * H
            H = H / la.norm(H)
        else:
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 0.5 * C + 0.4*p*rs_1 + 0.4*q*rs_2 + 2 * ra + 0.3*e / la.norm(e)
            H = H / la.norm(H)
            H = H * speed

        last_vector[i] = H
        sheep_dict['sheep' + str(i)].x = H[0]
        sheep_dict['sheep' + str(i)].y = H[1]
        sheep_dict['sheep' + str(i)].draw()
        new_position[i] = H

    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_position[i] + per_sheep


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


def sheep_move_2(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """

    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(per_sheep - herd_a_pos)

        l_mean, ra = knn(per_sheep, all_sheep, n // 2 + 1, r_rep)
        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)  # H为-1到1随机运动的大小
            H = H / np.linalg.norm(H)  # 把数据归一化
            H = 0.15 * last_vector[i] + 1.5 * ra + 0.3 * H
            H = H / np.linalg.norm(H)
        else:
            rs = (per_sheep - herd_a_pos) / ps_dist
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.15 * last_vector[i] + 1.05 * C + rs + 2 * ra + 0.3*e / np.linalg.norm(e)
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