import numpy as np
from AHtwoClusterView import sheepR
import math


def collecting(shepherd, all_sheep, global_mean, sheep_view_distance,
               repulsion_distance, speed, sheep_dict, target, last_vector):
    """
    把远离中心的羊聚集起来
    随机最大角度 + view
    首先找到最大角度的羊，获取到这只羊的位置。
    根据牧羊犬当前的位置，计算羊群下一个时间步的位置，返回一个最新的羊群位置。
    """
    speeds = speed * 1.5
    shepherd_position = shepherd.position2point()
    index = rotate(shepherd_position, global_mean, target, all_sheep)
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


def get_local_attractive(cur_sheep, all_sheep, sheep_view_dist):
    """
    sheep_view_dist,然后以该羊为圆心，寻找整个羊群中在该羊形成的Rs的圆内的圆心
    """
    dist = [np.linalg.norm(sheep - cur_sheep) for sheep in all_sheep]
    neighbor_sheep = np.array([all_sheep[i] for i in range(0, len(all_sheep)) if dist[i] < sheep_view_dist and dist[i] != 0])
    local_center = np.zeros(2)
    if len(neighbor_sheep) > 0:
        local_center = np.array([np.mean(neighbor_sheep[:, 0]), np.mean(neighbor_sheep[:, 1])])
    return local_center


def get_sheep_repulsion_to_neighbor(cur_sheep, all_sheep, repulsion_dist):
    """
    获取羊内部距离过近的排斥力，当两只羊之间的距离小于repulsion_dist时产生一个作用力
    """
    dist = [np.linalg.norm(sheep - cur_sheep) for sheep in all_sheep]
    repulsion = np.zeros(2, dtype=np.float32)
    for i in range(1, len(all_sheep)):
        d = np.linalg.norm(cur_sheep - all_sheep[i])
        if dist[i] <= repulsion_dist and d != 0:
            repulsion += (cur_sheep - all_sheep[i]) / d
    return repulsion


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