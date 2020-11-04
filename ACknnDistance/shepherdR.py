import numpy as np
from numpy import linalg as la


def collecting(herd, all_sheep, speed, app_dist):
    speeds = speed * 2
    herd_point = herd.position2point()

    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    far_a = find_farthest_sheep(all_sheep)

    gt_dist_a = la.norm(far_a - g_mean)
    pc_a = (far_a - g_mean) / gt_dist_a * app_dist + far_a
    rd_a = (pc_a - herd_point) / la.norm(pc_a - herd_point) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]

    herd.draw()


def driving(herd, all_sheep, speed, target, app_dist):
    speeds = speed * 1.0
    herd_point = herd.position2point()
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])

    gt_dist = la.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * app_dist + g_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()


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
