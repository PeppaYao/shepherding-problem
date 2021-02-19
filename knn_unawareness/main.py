from knn_unawareness import tkinterGUI
from knn_unawareness import sheep
import numpy as np
import time
from knn_unawareness import shepherdR


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
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, colors[i % 2])
        if i % 2 == 0:
            green_index.append(i)

    herd = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')

    return np.array(X), agents, herd, green_index


def run_animation(all_sheep, sheep_dict, herd, green_index):
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
            shepherdR.driving(herd, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector)
        else:
            print("collecting...")
            shepherdR.collecting(herd, green_index, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        green_array = all_sheep[green_index]
        if shepherdR.is_all_in_target(green_array) or step > 4000:
            green, blue = shepherdR.get_green_proportion(all_sheep, green_index)
            print("proportion of green sheep: ", green / (green + blue))
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step, green, blue


def print_list(lists):
    print("[", end="")
    for item in lists:
        print("{:.3f}".format(item), end=", ")
    print("]")


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    steps = []
    greens = []
    blues = []
    for n in range(10, 62, 2):
        all_sheep, sheep_dict, shepherd_a, green_index = init_sheep(canvas, n)
        step, green, blue = run_animation(all_sheep, sheep_dict, shepherd_a, green_index)
        steps.append(step)
        greens.append(green)
        blues.append(blue)
    print("animation over!")
    print_list(steps)
    print_list(greens)
    print_list(blues)
    tk.mainloop()
