from divide_group_two import tkinterGUI
from divide_group_two import sheep
import numpy as np
import time
from divide_group_two import sheepR
from divide_group_two import shepherdR


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, colors[i % 2])

    herd_1 = sheep.Agent(canvas_local, 550, 550, 560, 560, 'red')
    herd_2 = sheep.Agent(canvas_local, 50, 50, 60, 60, 'orange')

    return np.array(X), agents, herd_1, herd_2


def run_animation(all_sheep, sheep_dict, herd_1, herd_2):
    step = 0
    target_1 = np.array([560, 560])
    target_2 = np.array([50, 560])
    r_dist = 200
    r_rep = 12
    speed = 2
    n = len(all_sheep)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    green_index = [i for i in range(n) if i % 2 == 0]
    blue_index = [i for i in range(n) if i % 2 == 1]
    green_array = all_sheep[green_index]
    blue_array = all_sheep[blue_index]
    green_run = True
    blue_run = True
    while True:
        herd_1_point = herd_1.position2point().copy()
        herd_2_point = herd_2.position2point().copy()
        p = 1
        q = 1
        green_status_driving = False
        if green_run:
            if shepherdR.check(green_array):
                print("green driving...")
                green_status_driving = True
                shepherdR.driving(herd_1, green_index, all_sheep, speed, target_1)
            else:
                print("green collecting...")
                shepherdR.collecting(herd_1, green_index, all_sheep, speed)
        else:
            p = 0
            q = 2

        if blue_run:
            if shepherdR.check(blue_array) and not green_status_driving:
                print("blue driving...")
                shepherdR.driving(herd_2, blue_index, all_sheep, speed, target_2)
            else:
                print("blue collecting...")
                shepherdR.collecting(herd_2, blue_index, all_sheep, speed)
        else:
            p = 2
            q = 0

        if p == 1 and q == 1:
            sheepR.sheep_move(herd_1_point, herd_2_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector, p, q)
        elif p == 0:
            sheepR.sheep_move_2(herd_2_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)
        elif q == 0:
            sheepR.sheep_move_2(herd_1_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        green_array = all_sheep[green_index]
        blue_array = all_sheep[blue_index]

        if green_run and shepherdR.is_all_in_target(green_array):
            print("green over")
            break
            for ind in green_index:
                sheep_dict['sheep'+str(ind)].status = False
            herd_1.status = False
            green_run = False

        if blue_run and shepherdR.is_all_in_target_blue(blue_array):
            print("blue over")
            break
            for ind in blue_index:
                sheep_dict['sheep'+str(ind)].status = False
            herd_2.status = False
            blue_run = False

        tk.update()
        time.sleep(0.01)
        step += 1
        if not green_run and not blue_run:
            break
    return step


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
    n = 20
    all_sheep, sheep_dict, herd_1, herd_2 = init_sheep(canvas, n);
    step = run_animation(all_sheep, sheep_dict, herd_1, herd_2)
    print("animation over!")
    print(step)
    tk.mainloop()
