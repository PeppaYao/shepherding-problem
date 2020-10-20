import numpy as np


def sheeps_move(shepherd_max_angle, all_sheep,
                sheep_view_distance, repulsion_distance, speed, sheep_dict):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """
    number_of_sheep = len(all_sheep)
    new_displacement_of_all_sheep = np.zeros((number_of_sheep, 2), dtype=np.float64)
    displacement_of_sheep = np.array([.0, 0.000001])
    # 计算每只羊下次的位置
    for i in range(number_of_sheep):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        centroid_to_sheep_distance_angle = np.linalg.norm(per_sheep - shepherd_max_angle)
        # 获取到局部中心点和靠太近的排斥力
        local_mean = get_local_attractive(per_sheep, all_sheep, sheep_view_distance)
        ra = get_sheep_repulsion_to_neighbor(per_sheep, all_sheep, repulsion_distance)
        # 内部排斥作用力
        current_vector = 2 * ra
        # 牧羊犬的驱赶作用力
        if centroid_to_sheep_distance_angle <= sheep_view_distance:
            repulsion_force_1 = (per_sheep - shepherd_max_angle) / centroid_to_sheep_distance_angle
            current_vector += repulsion_force_1
            local_force = (local_mean - per_sheep) / np.linalg.norm(local_mean - per_sheep)
            # 局部中心点靠拢的吸引力
            current_vector += 1.1*local_force
        if np.linalg.norm(current_vector) != 0:
            current_unit_vector = current_vector / np.linalg.norm(current_vector)
        else:
            current_unit_vector = np.array([0.1, 0.1])
        displacement_of_sheep = current_unit_vector * speed

        sheep_dict['sheep' + str(i)].x = displacement_of_sheep[0]
        sheep_dict['sheep' + str(i)].y = displacement_of_sheep[1]
        sheep_dict['sheep' + str(i)].draw()
        # 使用临时变量记录更新的位移信息，暂时不做更新，当所有羊的位置计算完成后，统一更新
        new_displacement_of_all_sheep[i] = displacement_of_sheep

    for i in range(number_of_sheep):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_displacement_of_all_sheep[i] + per_sheep

    return all_sheep


def get_local_attractive(cur_sheep, all_sheep, sheep_view_dist):
    """
    sheep_view_dist,然后以该羊为圆心，寻找整个羊群中在该羊形成的Rs的圆内的圆心
    """
    dist = [np.linalg.norm(sheep - cur_sheep) for sheep in all_sheep]
    neighbor_sheep = np.array([all_sheep[i] for i in range(1, len(all_sheep)) if dist[i] < sheep_view_dist])
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
