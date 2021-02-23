import numpy as np
from numpy import linalg as la
from utils import common


def sheep_move(herd_a_pos, herd_b_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, left, right):

    # 这是对具体的每只羊的运动计算
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()

        ps_dist_a = la.norm(per_sheep - herd_a_pos)
        ps_dist_b = la.norm(per_sheep - herd_b_pos)
        # 求得局部吸引力和个体排斥力
        l_mean, ra = common.knn(per_sheep, all_sheep, int(n*0.7), r_rep)
        # 计算两只牧羊犬作用的合力
        if ps_dist_a > r_dist and ps_dist_b > r_dist:
            H = np.random.uniform(-1, 1, size=2)
            H = H / la.norm(H)
            H = 0.1 * last_vector[i] + 2 * ra + 0.5 * H
            H = H / la.norm(H)
        elif ps_dist_a > r_dist:
            rs = (per_sheep - herd_a_pos) / ps_dist_a
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 0.5 * rs + 2 * ra + 0.3 * e / la.norm(e)
            H = H / la.norm(H)
            H = H * speed
        elif ps_dist_b > r_dist:
            rs = (per_sheep - herd_b_pos) / ps_dist_b
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 0.5 * rs + 2 * ra + 0.3 * e / la.norm(e)
            H = H / la.norm(H)
            H = H * speed
        else:
            rs_a = (per_sheep - herd_a_pos) / ps_dist_a
            rs_b = (per_sheep - herd_b_pos) / ps_dist_b
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 0.5 * rs_a + 0.5 * rs_b + 2 * ra + 0.3 * e / la.norm(e)
            H = H / la.norm(H)
            H = H * speed

        last_vector[i] = H
        sheep_dict['sheep' + str(i)].x = H[0]
        sheep_dict['sheep' + str(i)].y = H[1]
        sheep_dict['sheep' + str(i)].draw()
        new_position[i] = H
    u = 0
    v = 0
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        if i % 2 == 0:
            left[u] = new_position[i] + per_sheep
            u += 1
        else:
            right[v] = new_position[i] + per_sheep
            v += 1
        all_sheep[i] = new_position[i] + per_sheep


