from ACshepherd import tkinterGUI
from ACshepherd import agent
import numpy as np
import time
from ACshepherd import shepherdRules


def init_sheep(canvas, N):
    agents = {}
    X = list()
    for i in range(N):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = agent.Agent(canvas, x - 5, y - 5, x + 5, y + 5, 'green', 'oval')

    shepherd = agent.Agent(canvas, 560, 560, 560 + 10, 560 + 10, 'red', 'oval')

    return np.array(X), agents, shepherd


def run_animation(all_sheep, sheep_dict, shepherd):
    step = 0
    N = len(all_sheep)
    target = np.array([560, 560])
    k_nearest = N//2+5
    sheep_view_distance = 300
    repulsion_distance = 12
    speed = 3
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    while True:
        if shepherdRules.check(all_sheep, global_mean):
            all_sheep, global_mean, shepherd = shepherdRules.driving(shepherd, all_sheep, global_mean,
                                                                      k_nearest, sheep_view_distance,
                                                                      repulsion_distance, speed, sheep_dict, target)
        else:
            all_sheep, global_mean, shepherd, = shepherdRules.collecting(shepherd, all_sheep, global_mean,
                                                                      k_nearest, sheep_view_distance,
                                                                      repulsion_distance, speed, sheep_dict)
        if shepherdRules.all_sheeps_in(all_sheep) or step > 8000:
            break
        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 60
    all_sheep, sheep_dict, shepherd= init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd)
    print("animation over!", step)
    tk.mainloop()
