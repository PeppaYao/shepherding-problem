import numpy as np
from APnoAnimation import shepherdR
from APnoAnimation import sheepR
import time


def run_animation(n, k):
    X = []
    for i in range(n):
        np.random.seed(i)
        x = np.random.randint(50, 500)
        y = np.random.randint(50, 500)
        X.append([x, y])
    step = 0
    target = np.array([560, 560])
    all_sheep = np.array(X, dtype=np.float64)
    r_dist = 250
    r_rep = 14
    speed = 2
    my_index = np.random.choice(np.arange(n), size=k, replace=False)
    my_array = all_sheep[my_index]
    herd = np.array([555, 555], dtype=np.float64)
    last_vector = np.zeros((n, 2), dtype=np.float32)
    while True:
        herd_point = herd.copy()
        if shepherdR.check(my_array, all_sheep):
            shepherdR.driving(herd, all_sheep, speed, target, my_index)
        else:
            shepherdR.collecting(herd, all_sheep, speed, my_index)

        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, last_vector)
        step += 1
        my_array = all_sheep[my_index]
        if shepherdR.is_all_in_target(my_array) or step > 4000:
            my_count = shepherdR.get_success_number(all_sheep)
            break

    return step, my_count


if __name__ == '__main__':
    start = time.time()
    steps = []
    counts = []
    n = 100
    for k in range(5, n+5, 5):
        step, count = run_animation(n, k)
        print(step, count)
        steps.append(step)
        counts.append(count)
    end = time.time()
    print("animation over! cost time:{:.2f}s".format(end - start))
    print(steps)
    print(counts)

