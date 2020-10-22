from AFviewDistance import tkinterGUI
from AFviewDistance import agent
import numpy as np
import time
from AFviewDistance import shepherdRules


def init_sheep(canvas, N):
    agents = {}
    X = list()
    for i in range(N):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = agent.Agent(canvas, x - 5, y - 5, x + 5, y + 5, 'green', 'oval')

    shepherd = agent.Agent(canvas, 590, 590, 600, 600, 'red', 'oval')

    return np.array(X), agents, shepherd


def run_animation(all_sheep, sheep_dict, shepherd):
    step = 0
    target = np.array([560, 560])
    sheep_view_distance = 300
    repulsion_distance = 14
    speed = 1.5
    N = len(all_sheep)
    radius = N + 36
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    while True:
        if shepherdRules.check(all_sheep, global_mean, radius):
            all_sheep, global_mean, shepherd = shepherdRules.driving(shepherd, all_sheep, global_mean,
                                                                     sheep_view_distance,
                                                                     repulsion_distance, speed, sheep_dict, target)
        else:
            all_sheep, global_mean, shepherd, = shepherdRules.collecting(shepherd, all_sheep, global_mean,
                                                                         sheep_view_distance,
                                                                         repulsion_distance, speed, sheep_dict)
        if shepherdRules.all_sheeps_in(all_sheep) or step > 8000:
            break
        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 20
    all_sheep, sheep_dict, shepherd= init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd)
    print("animation over!", step)
    tk.mainloop()
