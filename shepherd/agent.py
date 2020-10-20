import numpy as np


class Agent:
    def __init__(self, canvas, x, y, u, v, color, shape):
        """对目标对象进行初始化"""
        self.canvas = canvas
        self.color = color
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.shape = shape
        self.id = self.create_agent()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.tag = True

    def create_agent(self):
        if self.shape == 'oval':
            return self.canvas.create_oval(self.x, self.y, self.u, self.v, fill=self.color)
        elif self.shape == 'rectangle':
            return self.canvas.create_rectangle(self.x, self.y, self.u, self.v, fill=self.color)
        elif self.shape == 'polygon':
            return self.canvas.create_rectangle(self.x, self.y, self.u, self.v, fill=self.color)
        else:
            return 0

    def position2point(self):
        """把目标的两个坐标转换为中心的一个坐标"""
        pos = self.position()
        point = [0.0, 0.0]
        point[0] = (pos[0] + pos[2]) / 2
        point[1] = (pos[1] + pos[3]) / 2
        return np.array(point)
