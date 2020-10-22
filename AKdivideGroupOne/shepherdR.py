import numpy as np
from AKdivideGroupOne import sheepR
from numpy import linalg as la
import math


def collecting(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, index_g):
    """
    首先找到最远距离的羊，获取到这只羊的位置。
    根据牧羊犬当前的位置，计算羊群下一个时间步的位置，返回一个最新的羊群位置。
    """
    speeds = speed * 1.5
    herd_point = herd.position2point()
    g_sh_array = all_sheep[index_g]
    green_g_mean = np.array([np.mean(g_sh_array[:, 0]), np.mean(g_sh_array[:, 1])])

    far_point = find_farthest_sheep(g_sh_array)

    sheepR.sheeps_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, index_g)

    pc_a = (far_point - green_g_mean) / la.norm(far_point - green_g_mean) * 65 + far_point
    rd_a = (pc_a - herd_point) / la.norm(pc_a - herd_point) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]
    herd.draw()


def driving(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector, index_b, index_g):
    """
    Only consider sheep with green color
    """
    speeds = speed * 1.5
    g_sh_array = all_sheep[index_g]
    global_mean_a = np.array([np.mean(g_sh_array[:, 0]), np.mean(g_sh_array[:, 1])])
    herd_point = herd.position2point()
    sheepR.sheeps_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, index_g)

    Pd = (global_mean_a - target) / la.norm(target - global_mean_a) * 85 + global_mean_a
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds
    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()


def find_farthest_sheep(my_sheep):
    """
    the index indicts given array index
    """
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [la.norm(x - global_mean) for x in my_sheep]
    return my_sheep[np.argmax(d)]


def check(my_sheep, all_sheep):
    """
    对所有的羊检查是否都在全局中心点的radius半径范围内
    """
    n = len(my_sheep)
    radius = n + 50
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(sheep - global_mean) for sheep in my_sheep]
    D = np.array(d)
    return np.all(D <= radius)


def is_all_in_target(my_sheep):
    """
    判断是否所有羊都到达了目标范围
    """
    for p in my_sheep:
        if p[0] < 455 or p[1] < 455:
            return False
    return True


def rotate(cen, center, target, X):
    """
    传过来的是牧羊犬的位置和中心坐标的位置
    先计算羊的点是否在中心点的左边，若不是则cos(t)设置为1
    由于要找出最大的角度[0,90]范围内，cos(t)值越小，角度越大
    """
    d = [math.sqrt(np.sum((x - cen) ** 2)) for x in X]
    dx = math.sqrt(np.sum((center - cen) ** 2))
    OA = center - cen
    OB = X - cen

    m = len(X)
    T = [OA.dot(OB[i, :]) / dx / d[i] for i in range(m)]
    return np.argmin(T)