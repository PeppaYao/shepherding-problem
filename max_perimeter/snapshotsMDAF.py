from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from max_perimeter import shepherdRR
from knn_distance import sheepR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 550)
        y = np.random.randint(50, 580)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    # 牧羊犬的初始位置
    herd = sheep.Agent(canvas_local, 50, 550, 60, 560, 'red')
    return np.array(X), agents, herd


def run_animation(all_sheep, sheep_dict, herd, canvas):
    step = 0
    target = np.array([550, 550])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
    theta = math.pi/6
    fn = math.sqrt(n) * r_rep
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        herd_point = herd.position2point().copy()
        whichmode = ""
        if common.check_sector(all_sheep, theta, target) and common.check_dist(all_sheep, target, fn):
            shepherdRR.driving(herd, all_sheep, speed, target, app_dist)
            text = canvas.create_text(220, 20, text="driving", font=("宋体", 18))
            whichmode = "driving"
            canvas.pack()
        else:
            idx = shepherdRR.collecting(herd, all_sheep, speed, app_dist, target)
            text = canvas.create_text(220, 20, text="collecting", font=("宋体", 18))
            whichmode = "collecting"
            canvas.pack()
        step += 1
        step_txt = canvas.create_text(420, 20, text="steps: {}/2000".format(step), font=("宋体", 18))
        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)
        tk.update()
        time.sleep(0.01)
        canvas.delete(text)
        canvas.delete(step_txt)
        if step == 100:
            print("[", end="")
            for per in all_sheep:
                print("[{}, {}], ".format(per[0], per[1]), end="")
            print("]")
            print(herd.position2point())
            print(idx)
            print(whichmode)
            break

        if common.is_all_in_target(all_sheep) or step > 4000:

            print("[", end="")
            for per in all_sheep:
                print("[{}, {}], ".format(per[0], per[1]), end="")
            print("]")
            print(herd.position2point())
            print(whichmode)
            print(idx)
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            break

    return step


if __name__ == '__main__':
    tk, canvas = gui.init_tkinter()
    n = 50
    all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
    step = run_animation(all_sheep, sheep_dict, shepherd_a, canvas)
    print(step)
    print("MDAF animation over!")
    tk.mainloop()
