import numpy as np
import math


def calculate_angle(sheep_position, shepherd):
    local_centroid = np.array([np.mean(sheep_position[:, 0]), np.mean(sheep_position[:, 1])])
    d = [math.sqrt(np.sum((sheep - shepherd) ** 2)) for sheep in sheep_position]  # 牧羊犬到每只羊的距离
    dx = math.sqrt(np.sum((local_centroid - shepherd) ** 2))  # 牧羊犬到中心点的距离
    oa = local_centroid - shepherd
    ob = sheep_position - shepherd
    number_of_sheep = len(X)
    print(d)
    print(dx)

    shepherd_to_sheep_angle = [oa.dot(ob[i, :]) / dx / d[i] for i in range(number_of_sheep)]
    print(shepherd_to_sheep_angle)
    return 0


if __name__ == '__main__':
    X = np.array([[1, -1],
                  [3, 5]])
    shepherd = np.array([[0, 0]])
    color_of_X = ['green', 'blue', 'blue', 'green']

    result = calculate_angle(X, shepherd)
    print(result)
