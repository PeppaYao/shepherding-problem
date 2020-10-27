from AFviewDistance import tkinterGUI
from AFviewDistance import sheep
import numpy as np
import time
from AFviewDistance import shepherdR


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


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([560, 560])
    r_dist = 300
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        if shepherdR.check(all_sheep):
            print("driving...")
            shepherdR.driving(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector)
        else:
            print("collecting...")
            shepherdR.collecting(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        if shepherdR.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()

    n = 40
    all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
    step = run_animation(all_sheep, sheep_dict, shepherd_a)
    print("animation over!")
    print(step)
    tk.mainloop()
