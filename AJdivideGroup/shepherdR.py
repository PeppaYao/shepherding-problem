import numpy as np
from AJdivideGroup import sheepR
import math


def collecting(herd_A, set_A, all_sheep, R_dist, R_rep, speed, sheep_dict, last_vector):
    """
    首先找到最远距离的羊，获取到这只羊的位置。
    根据牧羊犬当前的位置，计算羊群下一个时间步的位置，返回一个最新的羊群位置。
    """
    speeds = speed * 1.5
    shepherd_a_position = herd_A.position2point()
    global_mean_a = np.array([np.mean(set_A[:, 0]), np.mean(set_A[:, 1])])

    index_a = find_farthest_sheep(set_A)
    far_a = sheep_dict['sheep' + str(index_a)].position2point()

    sheepR.sheeps_move(shepherd_a_position, all_sheep, R_dist, R_rep, speed, sheep_dict, last_vector)

    gt_dist_a = np.linalg.norm(far_a - global_mean_a)
    pc_a = (far_a - global_mean_a) / gt_dist_a * 65 + far_a
    rd_a = (pc_a - shepherd_a_position) / np.linalg.norm(pc_a - shepherd_a_position) * speeds

    herd_A.x = rd_a[0]
    herd_A.y = rd_a[1]

    herd_A.draw()


def driving(shepherd, set_A, all_sheep, sheep_view_distance,
            repulsion_distance, speed, sheep_dict, target, last_vector):
    """
    Only consider sheep with green color
    """
    speeds = speed * 1.5
    global_mean_a = np.array([np.mean(set_A[:, 0]), np.mean(set_A[:, 1])])
    shepherd_position = shepherd.position2point()
    all_sheep = sheepR.sheeps_move(shepherd_position, all_sheep, sheep_view_distance,
                                   repulsion_distance, speed, sheep_dict, last_vector)
    gt_dist = np.linalg.norm(target - global_mean_a)
    Pd = (global_mean_a - target) / gt_dist * 65 + global_mean_a
    rd = (Pd - shepherd_position) / np.linalg.norm(Pd - shepherd_position) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    shepherd.draw()

def find_farthest_sheep(my_sheep):
    """
    找到离中心最远的羊
    """
    global_mean = np.array([np.mean(my_sheep[:, 0]), np.mean(my_sheep[:, 1])])
    d = [np.linalg.norm(x - global_mean) for x in my_sheep]
    return np.argmax(d)


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