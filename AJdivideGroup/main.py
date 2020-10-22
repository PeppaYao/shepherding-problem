from AJdivideGroup import tkinterGUI
from AJdivideGroup import sheep
import numpy as np
import time
from AJdivideGroup import shepherdR


def init_sheep(canvas_local, N):
    agents = {}
    X = list()
    for i in range(N):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        if i % 2 == 0:
            color = "green"
        else:
            color = "blue"
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, color)

    shepherd_a = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')

    return np.array(X), agents, shepherd_a


def run_animation(all_sheep, sheep_dict, shepherd_A):
    step = 0
    target = np.array([560, 560])
    R_dist = 200
    R_rep = 12
    speed = 2
    N = len(all_sheep)
    last_vector = np.zeros((N, 2), dtype=np.float32)

    while True:
        set_a = []
        for per_sheep in sheep_dict.values():
            temp = per_sheep.position2point()
            if per_sheep.color == 'green' and per_sheep.status:
                set_a.append([temp[0], temp[1]])
        set_A = np.array(set_a)
        if shepherdR.check(set_A, all_sheep):
            shepherdR.driving(shepherd_A, set_A, all_sheep, R_dist, R_rep, speed, sheep_dict, target, last_vector)
        else:
            shepherdR.collecting(shepherd_A, set_A, all_sheep, R_dist, R_rep, speed, sheep_dict, last_vector)

        if shepherdR.is_all_in_target(set_A) or step > 4000:
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 30
    all_sheep, sheep_dict, shepherd_A = init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd_A)
    print("animation over!", step)
    tk.mainloop()
