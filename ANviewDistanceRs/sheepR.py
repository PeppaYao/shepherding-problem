import numpy as np
from numpy import linalg as la


def sheep_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        ps_dist = la.norm(per_sheep - herd_a_pos)

        l_mean = get_local_attractive(per_sheep, all_sheep, r_dist)
        ra = get_sheep_repulsion(per_sheep, all_sheep, r_rep)

        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)
            H = H / la.norm(H)
            H = 0.1 * last_vector[i] + 1.3 * ra + 0.3 * H
            H = H / la.norm(H)
        else:
            rs = (per_sheep - herd_a_pos) / ps_dist
            C = (l_mean - per_sheep) / la.norm(l_mean - per_sheep)
            e = np.random.uniform(-1, 1, size=2)
            H = 0.1 * last_vector[i] + 1.05 * C + 1.5 * rs + 1.1 * ra + 0.3 * e / la.norm(e)
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


def get_local_attractive(cur_sheep, all_sheep, r_dist):

    dist = [np.linalg.norm(sheep - cur_sheep) for sheep in all_sheep]
    neighbor_sheep = np.array([all_sheep[i] for i in range(1, len(all_sheep)) if dist[i] < r_dist])
    local_center = np.zeros(2)
    if len(neighbor_sheep) > 0:
        local_center = np.array([np.mean(neighbor_sheep[:, 0]), np.mean(neighbor_sheep[:, 1])])
    return local_center


def get_sheep_repulsion(cur_sheep, all_sheep, r_rep):
    dist = [la.norm(sheep - cur_sheep) for sheep in all_sheep]
    repulsion = np.zeros(2, dtype=np.float32)
    n = len(all_sheep)
    for i in range(n):
        d = la.norm(cur_sheep - all_sheep[i])
        if dist[i] <= r_rep and d > 1:
            repulsion += (cur_sheep - all_sheep[i]) / d
    return repulsion