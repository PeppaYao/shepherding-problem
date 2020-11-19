from utils import gui
from utils import common
from utils import sheep
import numpy as np
from numpy import linalg as la
from predator import predatorM
from predator import sheepR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    herd = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')
    return np.array(X), agents, herd


def run_animation(all_sheep, sheep_dict, pred):
    step = 0
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])

    while True:
        herd_point = pred.position2point()
        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)
        predatorM.move(pred, g_mean, speed)
        g_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
        tk.update()
        if la.norm(g_mean - herd_point) < 6.0:
            break
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = gui.init_tkinter()
    steps = []
    for n in range(20, 21):
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, shepherd_a)
        steps.append(step)
    print("AC animation over!")
    common.print_list(steps)
    tk.mainloop()
