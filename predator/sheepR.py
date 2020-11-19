import numpy as np
from numpy import linalg as la
from utils import common


def sheep_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = la.norm(per_sheep - herd_a_pos)
        l_mean, ra = common.knn(per_sheep, all_sheep, n // 2 + 5, r_rep)
        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)
            H = H / la.norm(H)
            H = 0.1 * last_vector[i] + 2 * ra + 0.5 * H
            H = H / la.norm(H)
        else:
            rs = (per_sheep - herd_a_pos) / ps_dist
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 50*common.inv(ps_dist, 30) * rs + 2 * ra + 0.3 * e / la.norm(e)
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
