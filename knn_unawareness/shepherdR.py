import numpy as np
from knn_unawareness import sheepR
import math
from numpy import linalg as la


def collecting(herd, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    """
    firstly, find the sheep of farthest distance.
    Secondly, calculate the sheep position according the herd current position.
    Thirdly, calculate the herd position.
    """
    speeds = speed * 1.5
    shepherd_a_position = herd.position2point()
    green_array = all_sheep[green_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])
    far_a = find_farthest_sheep(green_array)
    sheepR.sheeps_move(shepherd_a_position, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

    gt_dist_a = la.norm(far_a - green_mean)
    pc_a = (far_a - green_mean) / gt_dist_a * 65 + far_a
    rd_a = (pc_a - shepherd_a_position) / la.norm(pc_a - shepherd_a_position) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]

    herd.draw()


def driving(herd, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector):
    """
    Only consider sheep with green color
    """
    speeds = speed * 1.5
    green_array = all_sheep[green_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])
    herd_point = herd.position2point()

    sheepR.sheeps_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

    gt_dist = la.norm(target - green_mean)
    Pd = (green_mean - target) / gt_dist * 65 + green_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()


def find_farthest_sheep(my_sheep):
    """
    找到离中心最远的羊
    """
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(x - global_mean) for x in my_sheep]
    return my_sheep[np.argmax(d)]


def check(my_sheep):
    """
    To check whether all sheep in certain radius
    """
    n = len(my_sheep)
    radius = n + 70
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [la.norm(sheep - global_mean) for sheep in my_sheep]
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


def get_green_proportion(all_sheep, green_index):
    """
    :param all_sheep: all sheep postion
    :param green_index: green sheep index
    :return: proportion of green sheep in target area
    """
    green_count = 0
    other_count = 0
    n = len(all_sheep)
    for i in range(n):
        sheep = all_sheep[i]
        if sheep[0] >= 455 and sheep[1] >= 455:
            if i in green_index:
                green_count += 1
            else:
                other_count += 1

    return green_count, other_count