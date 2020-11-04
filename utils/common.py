import numpy as np
from numpy import linalg as la


def find_farthest_sheep(my_sheep):

    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(x - global_mean) for x in my_sheep]
    return my_sheep[np.argmax(d)]


def check(my_sheep, radius):
    n = len(my_sheep)
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [la.norm(sheep - global_mean) for sheep in my_sheep]
    D = np.array(d)
    return np.all(D <= radius)


def is_all_in_target(my_sheep):
    for p in my_sheep:
        if p[0] < 455 or p[1] < 455:
            return False
    return True


def knn(x, others, k, r_rep):
    d = [np.linalg.norm(x - x_) for x_ in others]
    near = np.argsort(d)
    top = [others[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float32)
    ra = np.zeros(2, dtype=np.float32)
    for p in near[1:k + 1]:
        if d[p] <= r_rep:
            ra += (x - others[p]) / np.linalg.norm(x - others[p])
    return local_m, ra


def print_list(lists):
    print("[", end="")
    for item in lists:
        print("{:.3f}".format(item), end=", ")
    print("]")


def find_max_angle_sheep(herd_point, all_sheep):
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    d = [la.norm(sheep - herd_point) for sheep in all_sheep]
    dx = la.norm(g_mean - herd_point)
    OA = g_mean - herd_point
    OB = all_sheep - herd_point
    m = len(all_sheep)
    t = [OA.dot(OB[i, :]) / dx / d[i] for i in range(m)]
    far = np.argsort(t)
    return all_sheep[far[0]]


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