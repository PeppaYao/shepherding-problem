import numpy as np


def sheeps_move(shepherd_max_angle, all_sheep, k_nearest,
                sheep_view_distance, repulsion_distance, speed, sheep_dict):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """
    number_of_sheep = len(all_sheep)
    new_displacement_of_all_sheep = np.zeros((number_of_sheep, 2), dtype=np.float64)
    for i in range(number_of_sheep):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        centroid_to_sheep_distance_angle = np.linalg.norm(per_sheep - shepherd_max_angle)
        # 获取到局部中心点和靠太近的排斥力
        local_mean, ra = knn(per_sheep, all_sheep, k_nearest, repulsion_distance)
        current_vector = 2 * ra
        if centroid_to_sheep_distance_angle <= sheep_view_distance:
            repulsion_force_1 = (per_sheep - shepherd_max_angle) / centroid_to_sheep_distance_angle
            current_vector += repulsion_force_1
            local_force = (local_mean - per_sheep) / np.linalg.norm(local_mean - per_sheep)
            current_vector += 1.05*local_force
        current_unit_vector = current_vector / np.linalg.norm(current_vector)

        displacement_of_sheep = current_unit_vector * speed
        sheep_dict['sheep' + str(i)].x = displacement_of_sheep[0]
        sheep_dict['sheep' + str(i)].y = displacement_of_sheep[1]
        sheep_dict['sheep' + str(i)].draw()
        new_displacement_of_all_sheep[i] = displacement_of_sheep

    for i in range(number_of_sheep):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_displacement_of_all_sheep[i] + per_sheep

    return all_sheep


def knn(per_sheep, all_sheep, k, repulsion_distance):
    """根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向"""
    d = [np.linalg.norm(per_sheep - sheep) for sheep in all_sheep]
    near = np.argsort(d)
    top = [all_sheep[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float64)
    ra = np.zeros(2, dtype=np.float64)
    for p in near[1:k + 1]:
        if d[p] <= repulsion_distance:
            ra += (per_sheep - all_sheep[p]) / np.linalg.norm(per_sheep - all_sheep[p])
    return local_m, ra
