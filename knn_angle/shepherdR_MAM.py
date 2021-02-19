import numpy as np
from utils import common
from numpy import linalg as la


def collecting(herd, all_sheep, speed, app_dist):
    speeds = speed * 1.5
    herd_point = herd.position2point()

    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    far_a = common.find_max_angle_sheep(herd_point, all_sheep)
    gt_dist_a = la.norm(far_a - g_mean)
    pc_a = (far_a - g_mean) / gt_dist_a * app_dist + far_a
    rd_a = (pc_a - herd_point) / la.norm(pc_a - herd_point) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]

    herd.draw()


def driving(herd, all_sheep, speed, target, app_dist):
    speeds = speed
    herd_point = herd.position2point()
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    gt_dist = la.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * app_dist + g_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()




