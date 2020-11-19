import numpy as np
from numpy import linalg as la
from utils import common


def move(pred, g_mean, speed):
    pred_speed = speed * 2
    pred_point = pred.position2point()
    dist = la.norm(pred_point - g_mean)
    rd_a = (g_mean - pred_point) / dist * pred_speed

    pred.x = rd_a[0]
    pred.y = rd_a[1]

    pred.draw()



