import numpy as np
from numpy import linalg as la


def collecting(herd, all_sheep, speed):
    speeds = speed * 1.5
    herd_point = herd.position2point()

    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    far_a = find_max_angle_sheep(herd_point, all_sheep)
    gt_dist_a = la.norm(far_a - g_mean)
    pc_a = (far_a - g_mean) / gt_dist_a * 65 + far_a
    rd_a = (pc_a - herd_point) / la.norm(pc_a - herd_point) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]

    herd.draw()


def driving(herd, all_sheep, speed, target):
    speeds = speed * 1.5
    herd_point = herd.position2point()
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    gt_dist = la.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * 65 + g_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()


def check(my_sheep):
    n = len(my_sheep)
    radius = n + 50
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [la.norm(sheep - global_mean) for sheep in my_sheep]
    D = np.array(d)
    return np.all(D <= radius)


def is_all_in_target(my_sheep):
    for p in my_sheep:
        if p[0] < 455 or p[1] < 455:
            return False
    return True


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