import numpy as np
from shepherd_raw import sheepRules
import math


def check(lst, g_mean, fn):
    """对所有的羊检查是否都在全局中心点的Fn半径范围内"""
    d = [np.linalg.norm(x - g_mean) for x in lst]
    D = np.array(d)
    return np.all(D <= fn)


def find_farest(arrv, g_m):
    """找到离中心最远的羊"""
    d = [np.linalg.norm(x - g_m) for x in arrv]
    near = np.argsort(d)
    return arrv[near[-1]]


def all_sheeps_in(arrx, Height):
    """判断是否所有羊都到达了目标区域"""
    for p in arrx:
        if p[0] < Height - 145 or p[1] < Height - 145:
            return False
    return True


def driving(herd, target, array, g_mean, shepherd):
    """把羊往目标点驱赶"""
    sheepRules.sheeps_move(herd, array)
    gt_dist = np.linalg.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * (14 * math.sqrt(46) + 20) + g_mean
    rd = (Pd - herd) / np.linalg.norm(Pd - herd) * 7.5
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


def collecting(herd, array, g_mean, shepherd):
    """把远离中心的羊聚集起来"""
    far = find_farest(array, g_mean)
    sheepRules.sheeps_move(herd, array)
    gt_dist = np.linalg.norm(far - g_mean)
    pc = (far - g_mean) / gt_dist * (14 + 10) + far
    rd = (pc - herd) / np.linalg.norm(pc - herd) * 7.5
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd
