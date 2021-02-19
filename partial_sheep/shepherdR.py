import numpy as np
from numpy import linalg as la


def collecting(herd, all_sheep, speed, my_index):
    speeds = speed * 1.5
    shepherd_a_position = herd.position2point()
    green_array = all_sheep[my_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])
    far_a = find_farthest_sheep(green_array)

    gt_dist_a = la.norm(far_a - green_mean)
    pc_a = (far_a - green_mean) / gt_dist_a * 65 + far_a
    rd_a = (pc_a - shepherd_a_position) / la.norm(pc_a - shepherd_a_position) * speeds

    herd.x = rd_a[0]
    herd.y = rd_a[1]

    herd.draw()


def driving(herd, all_sheep, speed, target, my_index):
    speeds = speed * 1.5
    green_array = all_sheep[my_index]
    green_mean = np.array([np.mean(green_array[:, 0]), np.mean(green_array[:, 1])])
    herd_point = herd.position2point()
    gt_dist = la.norm(target - green_mean)
    Pd = (green_mean - target) / gt_dist * 65 + green_mean
    rd = (Pd - herd_point) / np.linalg.norm(Pd - herd_point) * speeds

    herd.x = rd[0]
    herd.y = rd[1]
    herd.draw()


def find_farthest_sheep(my_sheep):
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(x - global_mean) for x in my_sheep]
    return my_sheep[np.argmax(d)]


def check(my_sheep, all_sheep):
    n = len(all_sheep)
    radius = n + 100
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