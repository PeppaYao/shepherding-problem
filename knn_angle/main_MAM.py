from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from knn_angle import shepherdR_MAM
from knn_distance import sheepR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

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
    radius = math.sqrt(n) * r_rep
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        herd_point = herd.position2point().copy()
        if common.check(all_sheep, radius):
            shepherdR_MAM.driving(herd, all_sheep, speed, target, app_dist)
        else:
            shepherdR_MAM.collecting(herd, all_sheep, speed, app_dist)

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
    # 随机最大角度
    tk, canvas = gui.init_tkinter()
    steps = []
    for n in range(10, 101):
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, shepherd_a)
        steps.append(step)
    print("随机最大角度 animation over!")
    common.print_list(steps)
    tk.mainloop()
