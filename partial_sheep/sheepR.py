import numpy as np
from numpy import linalg as la


def sheep_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = la.norm(per_sheep - herd_a_pos)
        l_mean, ra = knn(per_sheep, all_sheep, n // 2 + 5, r_rep)
        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)
            H = H / la.norm(H)
            H = 0.1 * last_vector[i] + 1.2 * ra + 0.3 * H
            H = H / la.norm(H)
        else:
            rs = (per_sheep - herd_a_pos) / ps_dist
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 1 * rs + 1.2 * ra + 0.3 * e / la.norm(e)
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