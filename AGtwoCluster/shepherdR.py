import numpy as np
from AGtwoCluster import sheepR
import math


def collecting(shepherd, all_sheep, global_mean, sheep_view_distance,
               repulsion_distance, speed, sheep_dict, target, last_vector):
    """
    把远离中心的羊聚集起来
    方向性最大角度 + KNN
    首先找到最大角度的羊，获取到这只羊的位置。
    根据牧羊犬当前的位置，计算羊群下一个时间步的位置，返回一个最新的羊群位置。
    """
    speeds = speed * 1.5
    shepherd_position = shepherd.position2point()
    index = find_max_angle_sheep(shepherd_position, global_mean, all_sheep)
    far = sheep_dict['sheep' + str(index)].position2point()
    all_sheep = sheepR.sheeps_move(shepherd_position, all_sheep, sheep_view_distance,
                                       repulsion_distance, speed,  sheep_dict, last_vector)
    gt_dist = np.linalg.norm(far - global_mean)
    pc = (far - global_mean) / gt_dist * 65 + far
    rd = (pc - shepherd_position) / np.linalg.norm(pc - shepherd_position) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    shepherd.draw()
    return all_sheep, global_mean, shepherd


def driving(shepherd, all_sheep, global_mean, sheep_view_distance,
            repulsion_distance, speed, sheep_dict, target, last_vector):
    """
    把羊往目标点驱赶
    """
    speeds = speed * 1.5
    shepherd_position = shepherd.position2point()
    all_sheep = sheepR.sheeps_move(shepherd_position, all_sheep, sheep_view_distance,
                                   repulsion_distance, speed, sheep_dict, last_vector)
    gt_dist = np.linalg.norm(target - global_mean)
    Pd = (global_mean - target) / gt_dist * 65 + global_mean
    rd = (Pd - shepherd_position) / np.linalg.norm(Pd - shepherd_position) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    shepherd.draw()
    return all_sheep, global_mean, shepherd


def find_max_angle_sheep(p, center, all_sheep):
    """
    传过来的是牧羊犬的位置和中心坐标的位置
    先计算羊的点是否在中心点的左边，若不是则cos(t)设置为1
    由于要找出最大的角度[0,90]范围内，cos(t)值越小，角度越大
    """
    d = [math.sqrt(np.sum((x - p) ** 2)) for x in all_sheep]
    dx = math.sqrt(np.sum((center - p) ** 2))
    OA = center - p
    OB = all_sheep - p
    m = len(all_sheep)
    t = [OA.dot(OB[i, :]) / dx / d[i] for i in range(m)]
    return np.argmin(t)


def check(all_sheep, global_mean, radius):
    """对所有的羊检查是否都在全局中心点的radius半径范围内"""
    d = [np.linalg.norm(sheep - global_mean) for sheep in all_sheep]
    D = np.array(d)
    return np.all(D <= radius)


def all_sheeps_in(all_sheep):
    """判断是否所有羊都到达了目标范围"""
    for p in all_sheep:
        if p[0] < 455 or p[1] < 455:
            return False
    return True
