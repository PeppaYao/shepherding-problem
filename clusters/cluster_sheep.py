import matplotlib.pyplot as plt
from tkinter import *
from sklearn.cluster import KMeans
import numpy as np
import time
from numpy import linalg as la

tk = Tk()
tk.title('羊群数量从40到120的时间步数')
tk.wm_attributes("-topmost", 1)
Width = 600
Height = 600
canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_line(Width / 2, 0, Width / 2, Height)
canvas.create_line(0, Height / 2, Height, Height / 2)
canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
tk.update()

r_dist = 250
r_rep = 14

N = 40
k = N//2 + 5
Fn = N + 36
speed = 3
speeds = 1.5 * speed
approach = 60


class Agent:
    def __init__(self, x, y, u, v, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_oval(x, y, u, v, fill=self.color)
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.tag = True

    def position(self):
        pos = self.canvas.coords(self.id)
        return pos

    def draw(self):
        if self.tag:
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
        pos = self.position()
        point = [0.0, 0.0]
        point[0] = (pos[0] + pos[2]) / 2
        point[1] = (pos[1] + pos[3]) / 2
        return np.array(point)

    def delete(self):
        self.canvas.delete(self.id)

    def stop(self):
        self.tag = False


def knn(herd, others):
    d = [la.norm(herd - per) for per in others]
    near = np.argsort(d)
    top = [others[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float32)
    ra = np.zeros(2, dtype=np.float32)
    for p in near[1:k + 1]:
        if d[p] <= r_rep:
            ra += (herd - others[p]) / np.linalg.norm(herd - others[p])
    return local_m, ra


def check(lst, g_mean):
    d = [np.linalg.norm(per - g_mean) for per in lst]
    D = np.array(d)
    return np.all(D <= Fn)


def find_farest(arr, g_m):
    dist = [np.linalg.norm(u - g_m) for u in arr]
    near = np.argsort(dist)
    return arr[near[-1]]


def move(herd, array, arrt):
    n = len(arrt)
    for i in range(n):
        point = agent['sheep' + str(arrt[i])].position2point()
        ps_dist = np.linalg.norm(point - herd)

        if ps_dist > r_dist:
            h = np.random.uniform(-2, 2, size=2)
        else:
            rs = (point - herd) / ps_dist
            l_mean, ra = knn(point, array)
            c = (l_mean - point) / np.linalg.norm(l_mean - point)
            h = 1.05 * c + rs + 2 * ra
            h = h / np.linalg.norm(h)
            h = h * speed
        agent['sheep' + str(arrt[i])].x = h[0]
        agent['sheep' + str(arrt[i])].y = h[1]
        array[i] = h + point
        agent['sheep' + str(arrt[i])].draw()

    # 对于另一类羊
    arry = [i for i in range(len(X)) if i not in arrt]
    past = np.zeros((len(arry), 2), dtype=np.float32)
    Y = X[arry]
    for i in range(len(arry)):
        point = agent['sheep' + str(arry[i])].position2point()
        ps_dist = np.linalg.norm(point - herd)
        if ps_dist > r_dist:
            h = np.random.uniform(-1, 1, size=2)
        else:
            rs = (point - herd) / ps_dist
            l_mean, ra = knn(point, Y)
            c = (l_mean - point) / np.linalg.norm(l_mean - point)
            h = 0.5 * past[i] + 1.2 * c + rs + 2 * ra
            h = h / np.linalg.norm(h)
            past[i] = h
            h = h * speed

        agent['sheep' + str(arry[i])].x = h[0]
        agent['sheep' + str(arry[i])].y = h[1]
        Y[i] = past[i] + point
        agent['sheep' + str(arry[i])].draw()


def driving(herd, target, array, g_mean, arrt):
    move(herd, array, arrt)  # 羊的移动状况
    gt_dist = np.linalg.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * approach + g_mean
    rd = (Pd - herd) / np.linalg.norm(Pd - herd) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


def collecting(herd, array, g_mean, arrt):
    """把远离中心的羊聚集起来"""
    far = find_farest(array, g_mean)  # 返回最远的羊的位置
    move(herd, array, arrt)  # 羊的移动状况
    gt_dist = np.linalg.norm(far - g_mean)  # 最远的羊与中心的距离
    Pc = (far - g_mean) / gt_dist * approach + far
    rd = (Pc - herd) / np.linalg.norm(Pc - herd) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


def all_sheeps_in(arrx):
    for p in arrx:
        if p[0] < Height - 145 or p[1] < Height - 145:
            return False
    return True


def sheeps_move0(herd, array):
    n = len(array)
    last = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        point = agent['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(point - herd)
        if ps_dist > r_dist:
            H = np.random.uniform(-1, 1, size=2)
            H = H / np.linalg.norm(H)
            last[i] = H
        else:
            rs = (point - herd) / ps_dist
            l_mean, ra = knn(point, array)
            C = (l_mean - point) / np.linalg.norm(l_mean - point)

            H = 0.5 * last[i] + 1.05 * C + rs + 2 * ra + 0.5 * np.random.uniform(-0.5, 0.5, size=2)
            H = H / np.linalg.norm(H)
            last[i] = H
            H = H * speed
        agent['sheep' + str(i)].x = H[0]
        agent['sheep' + str(i)].y = H[1]
        array[i] = last[i] + point
        agent['sheep' + str(i)].draw()


def driving0(herd, target, array, g_mean):
    sheeps_move0(herd, array)
    gt_dist = np.linalg.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * approach + g_mean
    rd = (Pd - herd) / np.linalg.norm(Pd - herd) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


def collecting0(herd, array, g_mean):
    far = find_farest(array, g_mean)
    sheeps_move0(herd, array)
    gt_dist = np.linalg.norm(far - g_mean)
    Pc = (far - g_mean) / gt_dist * approach + far
    rd = (Pc - herd) / np.linalg.norm(Pc - herd) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


Xs = []
Ys = []
Nx = 200
colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
# 40到120的时间步数
for N in range(40, 125, 5):
    k = N // 2 + 5
    Fn = N + 36
    X = []
    agent = {}
    for i in range(N):
        np.random.seed(i)
        if i % 2 == 0:
            x = np.random.randint(50, 250)
            y = np.random.randint(350, 550)
        else:
            x = np.random.randint(350, 550)
            y = np.random.randint(50, 250)
        X.append([x, y])
        agent['sheep' + str(i)] = Agent(x, y, x + 10, y + 10, "green")
    X = np.array(X)
    shepherd = Agent(560, 560, 560 + 10, 560 + 10, 'red')
    target = np.array([Height, Height])
    shepherd_point = shepherd.position2point()
    tk.update()
    time.sleep(0.01)
    tag = []
    step = 0
    out = 1
    first = 1

    while out == 1:
        mean = KMeans(n_clusters=2, random_state=666).fit(X)
        labels = mean.labels_  # [0,1,0,0,1,1,1]
        cluster_centers = mean.cluster_centers_
        center_distance = np.linalg.norm(cluster_centers[0] - cluster_centers[1])  # 计算两个质心的距离
        d0 = np.linalg.norm(cluster_centers[0] - target)    # 计算到目标点的距离
        d1 = np.linalg.norm(cluster_centers[1] - target)
        if d0 < d1:
            flag = 0   # 用于标记当前驱赶哪一个类别
        else:
            flag = 1
        # 修改羊的颜色
        for sh in range(N):
            pos = agent['sheep' + str(sh)].position()
            if len(pos) == 0:
                pos = [295.0, 295.0, 305.0, 305.0]
            agent['sheep' + str(sh)].delete()
            if labels[sh] == flag:
                agent['sheep' + str(sh)] = Agent(pos[0], pos[1], pos[2], pos[3], colors[1])  # 需要处理的类 永远为蓝色
            else:
                agent['sheep' + str(sh)] = Agent(pos[0], pos[1], pos[2], pos[3], colors[2])  # 聚类之后的

        # 如果两个类中心之间的距离大于了Nx，则将类别0驱赶一段距离，然后再判断

        if center_distance > Nx:
            array0 = X[labels == flag]  # X的一个子集
            tag = [i for i in range(len(labels)) if labels[i] == flag]  # 满足标签为flag的索引
            g_mean0 = cluster_centers[flag]
            for _ in range(50):   # 50步之后，再次判断
                if check(array0, g_mean0):
                    array0, g_mean0, shepherd_point = driving(shepherd_point, target, array0, g_mean0, tag)
                else:
                    array0, g_mean0, shepherd_point = collecting(shepherd_point, array0, g_mean0, tag)
                step += 1
                tk.update()
                time.sleep(0.01)
                if all_sheeps_in(array0):
                    for i in range(len(array0)):
                        agent['sheep' + str(tag[i])].stop()
                    first = 0
                    break
            if first == 0:
                array1 = X[labels != flag]
                tag1 = [i for i in range(len(labels)) if labels[i] != flag]
                if flag == 0:
                    g_mean1 = cluster_centers[1]
                else:
                    g_mean1 = cluster_centers[0]
                while True:
                    if check(array1, g_mean1):
                        array1, g_mean1, shepherd_point = driving(shepherd_point, target, array1, g_mean1, tag1)
                    else:
                        array1, g_mean1, shepherd_point = collecting(shepherd_point, array1, g_mean1, tag1)
                    step += 1
                    tk.update()
                    time.sleep(0.01)
                    if all_sheeps_in(array1):
                        out = 0
                        break
        else:
            for sh in range(len(X)):
                pos = agent['sheep' + str(sh)].position()
                agent['sheep' + str(sh)].delete()
                agent['sheep' + str(sh)] = Agent(pos[0], pos[1], pos[2], pos[3], colors[0])  # 整体处理都变为绿色
            tk.update()
            time.sleep(0.01)
            global_mean = np.array([np.mean(X[:, 0]), np.mean(X[:, 1])])
            while True:
                if check(X, global_mean):
                    X, global_mean, shepherd_point = driving0(shepherd_point, target, X, global_mean)
                else:
                    X, global_mean, shepherd_point, = collecting0(shepherd_point, X, global_mean)
                if all_sheeps_in(X):
                    out = 0
                    break
                tk.update()
                time.sleep(0.01)
                step += 1
    for i in range(N):
        agent['sheep' + str(i)].delete()
    shepherd.delete()
    Ys.append(step)
    Xs.append(Nx)

YS = np.array(Ys)
print("[", end="")
for y in YS:
    print(", ", end="")
    print(y, end="")
print("]")

label = Label(tk, text="游戏结束!", font=('楷体', 40), fg='red')
label.place(x=180, y=280)
tk.mainloop()
