from AItwoClusterDistance import tkinterGUI
from AItwoClusterDistance import sheep
import numpy as np
import time
from AItwoClusterDistance import shepherdR


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

    shepherd_local = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')

    return np.array(X), agents, shepherd_local


def run_animation(all_sheep, sheep_dict, shepherd):
    step = 0
    target = np.array([560, 560])
    sheep_view_distance = 200
    repulsion_distance = 12
    speed = 2
    N = len(all_sheep)
    radius = N + 36
    last_vector = np.zeros((N, 2), dtype=np.float32)
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    while True:
        if shepherdR.check(all_sheep, global_mean, radius):
            all_sheep, global_mean, shepherd = shepherdR.driving(shepherd, all_sheep, global_mean,
                                                                     sheep_view_distance,
                                                                     repulsion_distance, speed, sheep_dict, target, last_vector)
        else:
            all_sheep, global_mean, shepherd = shepherdR.collecting(shepherd, all_sheep, global_mean,
                                                                         sheep_view_distance,
                                                                         repulsion_distance, speed, sheep_dict, target, last_vector)
        if shepherdR.all_sheeps_in(all_sheep) or step > 8000:
            break
        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 40
    all_sheep, sheep_dict, shepherd = init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd)
    print("animation over!", step)
    tk.mainloop()
