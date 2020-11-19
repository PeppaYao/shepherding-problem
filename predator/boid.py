from utils import common


def sheep_move(herd_a_pos, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector):
    n = len(all_sheep)
    for i in range(n):
        per_sheep = sheep_dict['sheep' + str(i)].position2point()

        repulsive = common.get_repulsive(per_sheep, all_sheep, r_rep)
        alignment = common.get_alignment(per_sheep, all_sheep, r_dist)
        attractive = common.get_attractive(per_sheep, all_sheep, r_dist)
        escape = common.get_escape(herd_a_pos, per_sheep, r_dist)

        cur_velocity = (50*repulsive + 0.5*alignment + 2*attractive + 500*escape) * speed

        sheep_dict['sheep' + str(i)].x = cur_velocity[0]
        sheep_dict['sheep' + str(i)].y = cur_velocity[1]
        sheep_dict['sheep' + str(i)].draw()
