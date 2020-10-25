from ALdivideGroup import tkinterGUI
from ALdivideGroup import sheep
import numpy as np
import time
from ALdivideGroup import shepherdR


def init_sheep(canvas_local, N):
    agents = {}
    colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
    X = list()
    for i in range(N):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, colors[i % 2])

    shepherd_a = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')

    return np.array(X), agents, shepherd_a


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([560, 560])
    r_dist = 200
    r_rep = 12
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((N, 2), dtype=np.float32)
    index_g = np.array([i for i in range(n) if i % 2 == 0])  # only index
    index_b = np.array([i for i in range(n) if i % 2 == 1])
    g_sh_array = all_sheep[index_g]

    while True:

        if shepherdR.check(g_sh_array, all_sheep):
            print("driving...")
            shepherdR.driving(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector, index_b, index_g)
        else:
            print("collecting...")
            shepherdR.collecting(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, index_g)

        g_sh_array = all_sheep[index_g]
        if shepherdR.is_all_in_target(g_sh_array) or step > 4000:
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 60
    all_sheep, sheep_dict, shepherd_A = init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd_A)
    print("animation over!", step)
    tk.mainloop()
