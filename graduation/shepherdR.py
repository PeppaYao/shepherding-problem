import numpy as np
from numpy import linalg as la


class Shepherd:
    def __init__(self, b, k=2.0):
        self.behavior = b
        self.ratio_c = k

    def collecting(self, herd, all_sheep, speed, app_dist, target):
        speeds = speed * self.ratio_c
        herd_point = herd.position2point()

        g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
        """根据策略的不同产生多态的行为"""
        far_a = self.behavior.find(all_sheep, target, herd_point)

        gt_dist_a = la.norm(far_a - g_mean)
        pc_a = (far_a - g_mean) / gt_dist_a * app_dist + far_a
        rd_a = (pc_a - herd_point) / la.norm(pc_a - herd_point) * speeds

        herd.x = rd_a[0]
        herd.y = rd_a[1]

        herd.draw()

    def driving(self, herd, all_sheep, speed, target, app_dist):
        speeds = speed * 1.0
        herd_point = herd.position2point()
        g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])

        gt_dist = la.norm(target - g_mean)
        Pd = (g_mean - target) / gt_dist * app_dist + g_mean
        rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

        herd.x = rd[0]
        herd.y = rd[1]
        herd.draw()

    def switch(self, all_sheep, target, fn, theta):
        return self.behavior.check(all_sheep, target, fn, theta)
