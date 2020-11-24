from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from MaxDistSum import shepherdR
from ACknnDistance import sheepR


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


def run_animation(all_sheep, sheep_dict, herd, theta):
    step = 0
    target = np.array([600, 600])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
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

        if common.is_all_in_target(all_sheep) or step > 2000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break
        step += 1
    return step


if __name__ == '__main__':
    """
    选择不同的角度：10, 20, 30, 40, 50, 60, 70
    羊群规模设定为：50只
    结果分析：当某个离群羊处于夹角范围内但是离GCM很远时，很难完成牧羊犬任务。
    """
    tk, canvas = gui.init_tkinter()
    steps = []
    n = 50
    thetas = [math.pi/18, math.pi/9, math.pi/6, math.pi/4.5, math.pi/3.6, math.pi/3]
    for theta in thetas:
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, shepherd_a, theta)
        steps.append(step)
        print(step)
    print("max double distance animation over!")
    common.print_list(steps)
    tk.mainloop()
