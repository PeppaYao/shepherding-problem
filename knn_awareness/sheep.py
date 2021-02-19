import numpy as np


class Agent:
    def __init__(self, canvas, x, y, u, v, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_oval(x, y, u, v, fill=self.color)
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.status = True

    def position(self):
        """"返回目标当前的位置"""
        pos = self.canvas.coords(self.id)
        return pos

    def draw(self):
        """绘制目标对象的运动状态"""
        if self.status:
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 10
            if pos[1] <= 0:
                self.y = 10
            if pos[2] > self.canvas_width:
                self.x = -10
            if pos[3] > self.canvas_height:
                self.y = -10
        else:
            self.x = 0
            self.y = 0
        self.canvas.move(self.id, self.x, self.y)

    def position2point(self):
        """把目标的两个坐标转换为中心的一个坐标"""
        pos = self.position()
        point = [0.0, 0.0]
        point[0] = (pos[0] + pos[2]) / 2
        point[1] = (pos[1] + pos[3]) / 2
        return np.array(point)

    def delete(self):
        """删除目标对象"""
        self.canvas.delete(self.id)
