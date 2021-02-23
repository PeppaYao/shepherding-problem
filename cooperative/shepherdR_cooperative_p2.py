import numpy as np
from utils import common
from numpy import linalg as la


def collecting(herd_a, herd_b, all_sheep, speed, app_dist, left, right, target):
    # A-左半边 最远距离
    # B-右半边 最大周长
    speeds = speed * 1.5
    herd_point_a = herd_a.position2point()
    herd_point_b = herd_b.position2point()

    g_mean_a = np.array([np.mean(left[:, 0]), np.mean(left[:, 1])])
    g_mean_b = np.array([np.mean(right[:, 0]), np.mean(right[:, 1])])

    far_a = common.find_farthest_sheep(left)
    gt_dist_a = la.norm(far_a - g_mean_a)

    far_b = common.find_max_double_dist_sheep(target, all_sheep)
    gt_dist_b = la.norm(far_b - g_mean_b)

    pc_a = (far_a - g_mean_a) / gt_dist_a * app_dist + far_a
    rd_a = (pc_a - herd_point_a) / la.norm(pc_a - herd_point_a) * speeds

    pc_b = (far_b - g_mean_b) / gt_dist_b * app_dist + far_b
    rd_b = (pc_b - herd_point_b) / la.norm(pc_a - herd_point_b) * speeds

    herd_a.x = rd_a[0]
    herd_a.y = rd_a[1]

    herd_b.x = rd_b[0]
    herd_b.y = rd_b[1]

    herd_a.draw()
    herd_b.draw()


def driving(herd_a, herd_b, all_sheep, speed, target, app_dist):
    speeds = speed * 1.5
    herd_point_a = herd_a.position2point()
    herd_point_b = herd_b.position2point()

    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    gt_dist = la.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * app_dist + g_mean

    rd_a = (Pd - herd_point_a) / np.linalg.norm(Pd - herd_point_a) * speeds
    rd_b = (Pd - herd_point_b) / np.linalg.norm(Pd - herd_point_b) * speeds

    herd_a.x = rd_a[0]
    herd_a.y = rd_a[1]

    herd_b.x = rd_b[0]
    herd_b.y = rd_b[1]

    herd_a.draw()
    herd_b.draw()




