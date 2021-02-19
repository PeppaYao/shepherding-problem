from utils import common
import numpy as np


def sheep_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict):
    n = len(all_sheep)
    new_position = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()

        repulsive = common.get_repulsive(per_sheep, all_sheep, r_rep)
        alignment = common.get_alignment(per_sheep, all_sheep, r_dist)
        attractive = common.get_attractive(per_sheep, all_sheep, r_dist)
        escape = common.get_escape(herd_a_pos, per_sheep, r_dist)

        print("repulsive", repulsive)
        print("alignment", alignment)
        print("attractive", attractive)
        print("escape", escape)

        cur_velocity = (2*repulsive + 0.5*alignment + 1.3*attractive + 20*escape) * speed
        print(cur_velocity)

        sheep_dict['sheep' + str(i)].x = cur_velocity[0]
        sheep_dict['sheep' + str(i)].y = cur_velocity[1]
        sheep_dict['sheep' + str(i)].draw()
        new_position[i] = cur_velocity

    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()
        all_sheep[i] = new_position[i] + per_sheep



