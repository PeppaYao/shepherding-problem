import numpy as np
from numpy import linalg as la


def collecting(herd_point, all_sheep, speed, my_index):
    speeds = speed * 1.5

    green_array = all_sheep[my_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])
    far = find_farthest_sheep(green_array)

    gt_dist_a = la.norm(far - green_mean)
    pc = (far - green_mean) / gt_dist_a * 65 + far
    rd = (pc - herd_point) / la.norm(pc - herd_point) * speeds
    herd_point += rd


def driving(herd_point, all_sheep, speed, target, my_index):
    speeds = speed * 1.5
    green_array = all_sheep[my_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])

    gt_dist = la.norm(target - green_mean)
    Pd = (green_mean - target) / gt_dist * 65 + green_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds
    herd_point += rd


def find_farthest_sheep(my_sheep):
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(x - global_mean) for x in my_sheep]
    return my_sheep[np.argmax(d)]


def check(my_sheep, all_sheep):
    n = len(all_sheep)
    radius = n + 40
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [la.norm(sheep - global_mean) for sheep in my_sheep]
    D = np.array(d)
    return np.all(D <= radius)


def is_all_in_target(my_sheep):
    for p in my_sheep:
        if p[0] < 455 or p[1] < 455:
            return False
    return True


def get_success_number(all_sheep):
    count = 0
    for sheep in all_sheep:
        if sheep[0] >= 450 and sheep[1] >= 450:
            count += 1

    return count