from utils import gui
from utils import common
from utils import sheep
import numpy as np
import math
from graduation import shepherdR
from graduation import sheepR
from graduation import behaviors as cb


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 550)
        y = np.random.randint(50, 580)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    herd = sheep.Agent(canvas_local, 50, 550, 60, 560, 'red')
    return np.array(X, np.float64), agents, herd


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([550, 550], np.float64)
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
    fn = math.sqrt(n) * r_rep
    last_vector = np.zeros((n, 2), dtype=np.float32)
    theta = math.pi / 6
    """设定新旧行为策略"""
    herd_instance = shepherdR.Shepherd(cb.OldCBehavior())
    # herd_instance = shepherdR.Shepherd(cb.NewCBehavior())
    # herd_instance = shepherdR.Shepherd(cb.MaxAngleCBehavior())

    while True:
        herd_point = herd.position2point().copy()
        if herd_instance.switch(all_sheep, target, fn, theta):
            herd_instance.driving(herd, all_sheep, speed, target, app_dist)
            text = canvas.create_text(220, 20, text="driving", font=("宋体", 18))
            canvas.pack()
        else:

            herd_instance.collecting(herd, all_sheep, speed, app_dist, target)
            text = canvas.create_text(220, 20, text="collecting", font=("宋体", 18))
            canvas.pack()

        step += 1
        step_txt = canvas.create_text(420, 20, text="steps: {}/2000".format(step), font=("宋体", 18))
        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)
        tk.update()
        canvas.delete(text)
        canvas.delete(step_txt)

        if common.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break
    return step


if __name__ == '__main__':
    tk, canvas = gui.init_tkinter()
    steps = []
    for n in range(40, 51):
        all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
        step = run_animation(all_sheep, sheep_dict, shepherd_a)
        print("current n: {}, step {}:".format(n, step))
        steps.append(step)
    print("animation over!")
    common.print_list(steps)
    tk.mainloop()
