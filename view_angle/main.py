from view_angle import tkinterGUI
from view_angle import sheep
import numpy as np
import time
from view_angle import shepherdR
from view_angle import sheepR


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
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        herd_point = herd.position2point().copy()
        if shepherdR.check(all_sheep):
            print("driving...")
            shepherdR.driving(herd, all_sheep, speed, target)
        else:
            print("collecting...")
            shepherdR.collecting(herd, all_sheep, speed)

        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        tk.update()
        time.sleep(0.01)
        if shepherdR.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break
        step += 1
    return step


def print_list(lists):
    print("[", end="")
    for item in lists:
        print("{:.3f}".format(item), end=", ")
    print("]")


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    steps = []
    for n in range(10, 62, 2):
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, shepherd_a)
        steps.append(step)
    print("AE_ animation over!")
    print_list(steps)
    tk.mainloop()
