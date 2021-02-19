from partial_sheep import tkinterGUI
from partial_sheep import sheep
import numpy as np
import time
from partial_sheep import shepherdR
from partial_sheep import sheepR


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
    return np.array(X, dtype=np.float64), agents, herd


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([560, 560])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    my_index = np.random.choice(np.arange(n), size=n//2, replace=False)
    my_array = all_sheep[my_index]

    while True:
        herd_point = herd.position2point().copy()
        if shepherdR.check(my_array, all_sheep):
            shepherdR.driving(herd, all_sheep, speed, target, my_index)
        else:
            shepherdR.collecting(herd, all_sheep, speed, my_index)

        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)
        my_array = all_sheep[my_index]
        step += 1
        if shepherdR.is_all_in_target(my_array) or step > 4000:
            my_count = shepherdR.get_success_number(all_sheep)
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break
        tk.update()

    return step, my_count


def print_list(lists):
    print("[", end="")
    for item in lists:
        print("{:.3f}".format(item), end=", ")
    print("]")


if __name__ == '__main__':
    start = time.time()
    tk, canvas = tkinterGUI.init_tkinter()
    steps = []
    counts = []
    for n in range(10, 100, 5):
        all_sheep, sheep_dict, herd = init_sheep(canvas, n)
        step, count = run_animation(all_sheep, sheep_dict, herd)
        print(step, count)
        steps.append(step)
        counts.append(count)
    end = time.time()
    print("animation over! cost time: {:.2f}s".format(end - start))
    print(steps)
    print(counts)
    tk.mainloop()
