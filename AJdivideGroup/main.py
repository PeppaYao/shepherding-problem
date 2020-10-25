from AJdivideGroup import tkinterGUI
from AJdivideGroup import sheep
import numpy as np
import time
from AJdivideGroup import shepherdR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
    green_index = []
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        index = np.random.randint(1, 1000) % 2
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, colors[index])
        if index == 0:
            green_index.append(i)

    shepherd_a = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')

    return np.array(X), agents, shepherd_a, green_index


def run_animation(all_sheep, sheep_dict, shepherd_A, green_index):
    step = 0
    target = np.array([560, 560])
    r_dist = 200
    r_rep = 12
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    green_array = all_sheep[green_index]
    while True:

        if shepherdR.check(green_array):
            print("driving...")
            shepherdR.driving(shepherd_A, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector)
        else:
            print("collecting...")
            shepherdR.collecting(shepherd_A, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        green_array = all_sheep[green_index]
        if shepherdR.is_all_in_target(green_array) or step > 4000:
            proportion = shepherdR.get_green_proportion(all_sheep, green_index)
            print("proportion of green sheep: ", proportion)
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step, proportion


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    n = 40
    all_sheep, sheep_dict, shepherd_a, green_index = init_sheep(canvas, n)
    step, proportion = run_animation(all_sheep, sheep_dict, shepherd_a, green_index)
    print("animation over!", step)
    tk.mainloop()
