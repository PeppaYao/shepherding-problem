from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from max_perimeter import shepherdR
from knn_distance import sheepR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n-1):
        np.random.seed(i)
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    # 离群点的特殊的一只羊,在目标区域
    X.append([550, 550])
    agents['sheep' + str(n-1)] = sheep.Agent(canvas_local, 550 - 5, 550 - 5, 550 + 5, 550 + 5, 'green')
    # 牧羊犬的初始位置
    herd = sheep.Agent(canvas_local, 50, 550, 60, 560, 'red')
    return np.array(X), agents, herd


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([600, 600])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
    theta = math.pi/4.5
    radius = math.sqrt(n) * r_rep
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        herd_point = herd.position2point().copy()
        if common.check_sector(all_sheep, theta, target):
            shepherdR.driving(herd, all_sheep, speed, target, app_dist)
        else:
            shepherdR.collecting(herd, all_sheep, speed, app_dist, target)

        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        tk.update()
        time.sleep(0.01)

        if common.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = gui.init_tkinter()
    n = 50
    all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
    step = run_animation(all_sheep, sheep_dict, shepherd_a)
    print(step)
    print("MDA animation over!")
    tk.mainloop()
