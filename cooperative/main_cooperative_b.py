from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from cooperative import shepherdR_cooperative_b as R1
from cooperative import sheepR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    herd_1 = sheep.Agent(canvas_local, 50, 550, 60, 560, 'red')
    herd_2 = sheep.Agent(canvas_local, 550, 50, 560, 60, 'blue')

    return np.array(X), agents, herd_1, herd_2


def run_animation(all_sheep, sheep_dict, herd_a, herd_b):
    step = 0
    target = np.array([560, 560])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
    last_vector = np.zeros((n, 2), dtype=np.float32)
    radius = math.sqrt(n) * r_rep
    while True:
        herd_point_a = herd_a.position2point().copy()
        herd_point_b = herd_b.position2point().copy()
        # A-聚集 + 驱赶
        # B-驱赶
        if common.check(all_sheep, radius):
            R1.driving(herd_a, all_sheep, speed, target, app_dist)
        else:
            R1.collecting(herd_a, all_sheep, speed, app_dist, target)
        R1.driving(herd_b, all_sheep, speed, target, app_dist)

        sheepR.sheep_move(herd_point_a, herd_point_b, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        tk.update()
        time.sleep(0.01)

        if common.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd_a.delete()
            herd_b.delete()
            break
        step += 1
    return step


if __name__ == '__main__':
    # 合作：一只专门聚集，一只专门驱赶。
    # 聚集：最大角度
    tk, canvas = gui.init_tkinter()
    steps = []
    for n in range(20, 71):
        all_sheep, sheep_dict, herd_a, herd_b = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, herd_a, herd_b)
        steps.append(step)
    print("knn farthest angle animation over!")
    common.print_list(steps)
    tk.mainloop()
