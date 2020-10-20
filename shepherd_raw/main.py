from shepherd_raw import tkinterGUI
from shepherd_raw import agent
import numpy as np
import time
from shepherd_raw import shepherdRules


def init_sheep(canvas, N):
    agents = {}
    X = list()
    for i in range(N):
        np.random.seed(i)
        if i % 2 == 0:
            x = np.random.randint(10, 590)
            y = np.random.randint(10, 590)
            agents['sheep' + str(i)] = agent.Agent(canvas, x - 5, y - 5, x + 5, y + 5, 'green', 'oval')  # 绿色
            X.append([x, y])
        else:
            x = np.random.randint(10, 590)
            y = np.random.randint(10, 590)
            agents['sheep' + str(i)] = agent.Agent(canvas, x - 5, y - 5, x + 5, y + 5, 'blue', 'rectangle')  # 蓝色
            X.append([x, y])
    shepherd = agent.Agent(canvas, 560, 560, 560 + 10, 560 + 10, 'red', 'oval')
    shepherd_point = shepherd.position2point()
    return np.array(X), agents, shepherd_point


def run_animation(all_sheep, sheep_dict, shepherd, target):
    step = 0
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    while True:
        if shepherdRules.check(X, global_mean):
            X, global_mean, shepherd_point = shepherdRules.driving(shepherd_point, target, all_sheep, global_mean)
        else:
            X, global_mean, shepherd_point, = shepherdRules.collecting(shepherd_point, all_sheep, global_mean)
        if shepherdRules.all_sheeps_in(X) or step > 8000:
            break
        tk.update()
        time.sleep(0.01)
        step += 1
    return step


if __name__ == '__main__':
    tk, canvas = tkinterGUI.init_tkinter()
    N = 46
    all_sheep, sheep_dict, shepherd = init_sheep(canvas, N)
    step = run_animation(all_sheep, sheep_dict, shepherd)
    print("animation over!", step)
    tk.mainloop()
