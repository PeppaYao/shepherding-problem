import numpy as np
from numpy import linalg as la
import math


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


def inv(x, s):
    epsilon = 1
    return (x/s + epsilon)**(-2)


def find_target_farthest_sheep(target, all_sheep):
    d = [np.linalg.norm(x - target) for x in all_sheep]
    return all_sheep[np.argmax(d)]


def find_max_double_dist_sheep(target, all_sheep):
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    d = [la.norm(x - target) + la.norm(x - global_mean) for x in all_sheep]
    return all_sheep[np.argmax(d)]


def check_sector(all_sheep, theta, target):
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])

    d = [la.norm(sheep - target) for sheep in all_sheep]
    dx = la.norm(g_mean - target)
    OA = g_mean - target
    OB = all_sheep - target
    m = len(all_sheep)
    t = np.array([OA.dot(OB[i, :]) / dx / d[i] for i in range(m)])

    return all(t > math.cos(theta))


def get_repulsive(cur_sheep, all_sheep, r_rep):
    repulsion = np.zeros(2, dtype=np.float32)
    n = len(all_sheep)
    count_neighbor = 0
    for i in range(n):
        if all(all_sheep[i] == cur_sheep):
            continue
        d = la.norm(cur_sheep - all_sheep[i])
        if r_rep >= d > 0.1:
            repulsion += (cur_sheep - all_sheep[i]) / d * inv(d, 1)
            count_neighbor += 1
    return repulsion / count_neighbor if count_neighbor > 0 else repulsion


def get_alignment(cur_sheep, all_sheep, r_dist):
    alignment = np.zeros(2, dtype=np.float32)
    n = len(all_sheep)
    count_neighbor = 0
    for i in range(n):
        if all(all_sheep[i] == cur_sheep):
            continue
        d = la.norm(cur_sheep - all_sheep[i])
        if r_dist >= d > 0.1:
            alignment += (all_sheep[i]) / la.norm(all_sheep[i])
            count_neighbor += 1
    return alignment / count_neighbor if count_neighbor > 0 else alignment


def get_attractive(cur_sheep, all_sheep, r_dist):
    attractive = np.zeros(2, dtype=np.float32)
    n = len(all_sheep)
    count_neighbor = 0
    for i in range(n):
        if all(all_sheep[i] == cur_sheep):
            continue
        d = la.norm(all_sheep[i] - cur_sheep)
        if r_dist >= d > 0.1:
            attractive += (all_sheep[i] - cur_sheep) / d
            count_neighbor += 1
    return attractive / count_neighbor if count_neighbor > 0 else attractive


def get_escape(herd_pos, cur_sheep, r_dist):
    escape = np.zeros(2, dtype=np.float32)
    d = la.norm(cur_sheep - herd_pos)
    if r_dist >= d >= 0.1:
        escape += (cur_sheep - herd_pos) / d * inv(d, 30)
    return escape


def check_dist(all_sheep, target, fn):
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    d = [la.norm(sheep - target) for sheep in all_sheep]
    gcm2target = la.norm(g_mean - target)
    return all(d < gcm2target + fn)