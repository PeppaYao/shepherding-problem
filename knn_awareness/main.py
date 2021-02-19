from knn_awareness import tkinterGUI
from knn_awareness import sheep
import numpy as np
import time
from knn_awareness import shepherdR


def init_sheep(canvas_local, n):
    agents = {}
    colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
    X = list()
    for i in range(n):
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
    last_vector = np.zeros((n, 2), dtype=np.float32)
    green_index = np.array([i for i in range(n) if i % 2 == 0])  # only index
    index_b = np.array([i for i in range(n) if i % 2 == 1])
    g_sh_array = all_sheep[green_index]

    while True:

        if shepherdR.check(g_sh_array, all_sheep):
            print("driving...")
            shepherdR.driving(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, target, last_vector, index_b, green_index)
        else:
            print("collecting...")
            shepherdR.collecting(herd, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, index_b, green_index)

        g_sh_array = all_sheep[green_index]
        if shepherdR.is_all_in_target(g_sh_array) or step > 4000:
            green, blue = shepherdR.get_green_proportion(all_sheep, green_index)
            print("proportion of green sheep: ", green/(green + blue))
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break

        tk.update()
        time.sleep(0.01)
        step += 1
    return step, green, blue


def print_list(lists):
    """
    :param lists: list
    :return: void
    show list and retain three decimal places
    """
    print("[", end="")
    for item in lists:
        print("{:.3f}".format(item), end=", ")
    print("]")


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    steps = []
    greens = []
    blues = []
    for n in range(30, 32, 2):
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step, green, blue = run_animation(all_sheep, sheep_dict, shepherd_a)
        steps.append(step)
        greens.append(green)
        blues.append(blue)
    print("animation over!")
    print_list(steps)
    print_list(greens)
    print_list(blues)
    tk.mainloop()
