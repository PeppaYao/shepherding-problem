import numpy as np
from AEviewAngle import sheepRules
import math


def collecting(shepherd, all_sheep, global_mean, sheep_view_distance,
               repulsion_distance, speed, sheep_dict):
    """
    目标：把远离中心的羊聚集起来
    """
    shepherd_max_angle = shepherd.position2point()

    max_angle_sheep_index = find_max_angle_sheep(shepherd_max_angle, global_mean, all_sheep)
    max_angle_sheep = sheep_dict['sheep' + str(max_angle_sheep_index)].position2point()

    speeds = speed * 1.2
    # 最大角度牧羊犬的下一次的位置
    centroid_to_sheep_distance_1 = np.linalg.norm(max_angle_sheep - global_mean)
    target_position_2 = (max_angle_sheep - global_mean) / centroid_to_sheep_distance_1 * 65 + max_angle_sheep
    displacement_of_max_angle_shepherd = (target_position_2 - shepherd_max_angle) \
                                         / np.linalg.norm(target_position_2 - shepherd_max_angle) * speeds

    # 此时的羊群位置是更新过了的
    all_sheep = sheepRules.sheeps_move(shepherd_max_angle, all_sheep, sheep_view_distance,
                                       repulsion_distance, speed,  sheep_dict)

    shepherd.x = displacement_of_max_angle_shepherd[0]
    shepherd.y = displacement_of_max_angle_shepherd[1]
    # 计算新中心值
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    shepherd.draw()
    return all_sheep, global_mean, shepherd


def driving(shepherd, all_sheep, global_mean, sheep_view_distance, repulsion_distance, speed, sheep_dict, target):
    """把羊往目标点驱赶"""
    shepherd_max_angle = shepherd.position2point()
    speeds = speed*1.5
    all_sheep = sheepRules.sheeps_move(shepherd_max_angle, all_sheep, sheep_view_distance,
                                       repulsion_distance, speed,  sheep_dict)
    gt_dist = np.linalg.norm(target - global_mean)
    Pd = (global_mean - target) / gt_dist * 65 + global_mean
    rd = (Pd - shepherd_max_angle) / np.linalg.norm(Pd - shepherd_max_angle) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    shepherd.draw()
    return all_sheep, global_mean, shepherd


def find_max_angle_sheep(p, center, all_sheep):
    """找到最大角度的羊，作为目标点"""
    d = [math.sqrt(np.sum((x - p) ** 2)) for x in all_sheep]
    dx = math.sqrt(np.sum((center - p) ** 2))
    OA = center - p
    OB = all_sheep - p
    m = len(all_sheep)
    t = [OA.dot(OB[i, :]) / dx / d[i] for i in range(m)]
    far = np.argsort(t)
    return far[0]


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