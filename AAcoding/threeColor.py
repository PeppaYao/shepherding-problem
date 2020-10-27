"""
There are two bugs:
firstly, the sheep in common circumstance has a down move tendency
secondly, the sheep lack of mutual repulsion
"""
from tkinter import *
import numpy as np
from numpy import linalg as LA
import time
import math

tk = Tk()
tk.title('my_shepherd')
tk.wm_attributes("-topmost", 1)
Width = 750
Height = 750
canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_line(Width / 2, 0, Width / 2, Height)
canvas.create_line(0, Height / 2, Height, Height / 2)
canvas.create_line(610, 610, 610, 750, 610, 610, 750, 610)

tk.update()
Rs = 500
Ra = 12
Fn = 50
k = 30
X = []
speed = 2
speed_of_herd = speed * 1.5
n_sheeps = 40


class Sheep:
    def __init__(self, canvas, x, y, u, v, color):
        '''对目标对象进行初始化'''
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_oval(x, y, u, v, fill=self.color)
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.tag = True

    def position(self):
        '''返回目标当前的位置'''
        pos = self.canvas.coords(self.id)
        return pos

    def draw(self):
        '''绘制目标对象的运动状态'''
        if (self.tag == True):
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
        '''把目标的两个坐标转换为中心的一个坐标'''
        pos = self.position()
        point = np.zeros((2), np.float32)
        point[0] = (pos[0] + pos[2]) / 2
        point[1] = (pos[1] + pos[3]) / 2
        return point

    def delete(self):
        '''删除目标对象'''
        self.canvas.delete(self.id)

    def stop(self):
        '''当目标对象到达指定区域则停止运动'''
        self.tag = False


sheeps = {}
colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple']
for i in range(n_sheeps):
    np.random.seed(i)
    x = np.random.randint(35, 630)
    y = np.random.randint(35, 630)
    X.append([x, y])
    sheeps['sheep' + str(i)] = Sheep(canvas, x, y, x + 10, y + 10, colors[i % 2])  # wonderful
X = np.array(X)
shepherd = Sheep(canvas, 660, 660, 660 + 10, 660 + 10, 'red')

index_g = np.array([i for i in range(n_sheeps) if i % 2 == 0])  # only index
index_b = np.array([i for i in range(n_sheeps) if i % 2 == 1])

'''数据准备工作'''


def position_point(pos):
    '''将两个坐标点取平均值后集中为1个点'''
    point = np.zeros((2), np.float32)
    point[0] = (pos[0] + pos[2]) / 2
    point[1] = (pos[1] + pos[3]) / 2
    return point


def knn(x, others, k):
    '''根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向'''
    d = [math.sqrt(np.sum((x_ - x) ** 2)) for x_ in others]
    near = np.argsort(d)
    top = [others[i] for i in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    ra = np.zeros(2, dtype=np.float32)
    for p in near[1:k + 1]:
        if d[p] <= Ra:
            ra += (x - others[p]) / (math.sqrt(np.sum((x - others[p]) ** 2)))
    return np.array(local_m, np.float32), ra


def check(sheep_lst, g_mean):
    '''对所有的羊检查是否都在全局中心点的Fn半径范围内'''
    n = len(sheep_lst)
    dist = [math.sqrt(np.sum(x - g_mean) ** 2) for x in sheep_lst]
    nearest_dist = np.sort(dist)
    for i in range(n - 1, -1, -1):
        if nearest_dist[i] > Fn:
            return False
    return True


def find_farest(arrv, g_m):
    '''找到离中心最远的羊'''
    dist = [math.sqrt(np.sum(x - g_m) ** 2) for x in arrv]
    nearr = np.argsort(dist)
    return g_sh_array[nearr[-1]]


def driving(herd, target, ar, g_mean, k, arrt):
    '''把羊往目标点驱赶'''
    # 对每只羊进行计算下一步运动位置
    last = np.zeros((len(arrt), 2), dtype=np.float32)
    for i in range(len(arrt)):
        position = sheeps['sheep' + str(arrt[i])].position()
        point = position_point(position)
        ps_dist = math.sqrt(np.sum((point - herd) ** 2))
        pg_dist = math.sqrt(np.sum((point - g_mean) ** 2))
        rg = (g_mean - point) / pg_dist
        g = pg_dist * 0.001 + 0.3
        if ps_dist > Rs / 5:
            H = np.random.uniform(-1, 1, size=2) + g * rg
            H = H / math.sqrt(H[0] * H[0] + H[1] * H[1])
            last[i] = H
        else:
            rs = (point - herd) / ps_dist
            l_mean, ra = knn(point, ar, k)
            C = (l_mean - point) / math.sqrt(np.sum((l_mean - point) ** 2))
            if ps_dist < 3 * Ra:
                p = 0
            else:
                p = 200 / (100 + ps_dist)
            H = 0.5 * last[i] + 1.05 * C + p * rs + 2 * ra + g * rg
            H = H / math.sqrt(H[0] * H[0] + H[1] * H[1])
            last[i] = H
            H = H * 6.6
        last[i] = last[i] / math.sqrt(last[i, 0] * last[i, 0] + last[i, 1] * last[i, 1])
        sheeps['sheep' + str(arrt[i])].x = H[0]
        sheeps['sheep' + str(arrt[i])].y = H[1]
        ar[i] = H + point
        sheeps['sheep' + str(arrt[i])].draw()
    # 其他类羊的下一步运动位置
    arry = [i for i in range(len(X)) if i not in arrt]
    past = np.zeros((len(arry), 2), dtype=np.float32)
    Y = X[arry]
    for i in range(len(arry)):
        position = sheeps['sheep' + str(arry[i])].position()
        point = position_point(position)
        ps_dist = math.sqrt(np.sum((point - herd) ** 2))
        pg_dist = math.sqrt(np.sum((point - g_mean) ** 2))
        rg = (g_mean - point) / pg_dist
        g = pg_dist * 0.001 + 0.3
        if ps_dist > Rs / 5:
            H = np.random.uniform(-1, 1, size=2) + g * rg
            H = H / math.sqrt(H[0] * H[0] + H[1] * H[1])
            past[i] = H
        else:
            rs = (point - herd) / ps_dist
            l_mean, ra = knn(point, Y, k)
            C = (l_mean - point) / math.sqrt(np.sum((l_mean - point) ** 2))
            if ps_dist < 3 * Ra:
                p = 0
            else:
                p = 200 / (100 + ps_dist)
            H = 0.5 * past[i] + 1.05 * C + p * rs + 2 * ra + g * rg
            H = H / math.sqrt(H[0] * H[0] + H[1] * H[1])
            past[i] = H
            H = H * 6.6
        past[i] = past[i] / math.sqrt(past[i, 0] * past[i, 0] + past[i, 1] * past[i, 1])
        sheeps['sheep' + str(arry[i])].x = H[0]
        sheeps['sheep' + str(arry[i])].y = H[1]
        sheeps['sheep' + str(arry[i])].draw()

    # 对于牧羊犬的下一步运动位置
    gt_dist = math.sqrt(np.sum((target - g_mean) ** 2))
    Pd = (g_mean - target) / gt_dist * 80 + g_mean
    rd = (Pd - herd) / math.sqrt(np.sum((Pd - herd) ** 2)) * 10
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(ar[:, 0]), np.mean(ar[:, 1])])
    shepherd.draw()
    return ar, g_mean, rd


def collecting(herd, g_sh_array, g_g_mean, k, b_sh_array, all_sheep):
    """
    only deal with sheep in green
    """
    far = find_farest(g_sh_array, g_g_mean)
    # calculate sheep next position
    for i in range(n_sheeps):
        position = sheeps['sheep' + str(i)].position()
        per_sh_point = position_point(position)
        ps_dist = LA.norm(per_sh_point - herd)
        H = np.random.uniform(-1, 1, size=2)
        H = H / np.linalg.norm(H)

        if ps_dist <= Rs//2:
            rs = (per_sh_point - herd) / ps_dist
            if per_sh_point in g_sh_array:
                l_mean, ra = knn(per_sh_point, g_sh_array, k)
            else:
                l_mean, ra = knn(per_sh_point, b_sh_array, k)
            C = (l_mean - per_sh_point) / LA.norm(l_mean - per_sh_point)
            H = 1.05 * C + 1 * rs + 2 * ra
            H = H / LA.norm(H)

        H = H * speed
        sheeps['sheep' + str(i)].x = H[0]
        sheeps['sheep' + str(i)].y = H[1]
        sheeps['sheep' + str(i)].draw()
        all_sheep[i] = H + per_sh_point

    # calculate ACknnDistance next position
    Pc = (far - g_g_mean) / LA.norm(far - g_g_mean) * 65 + far
    rd = (Pc - herd) / LA.norm(Pc - herd) * speed_of_herd
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    shepherd.draw()

    return all_sheep
def all_sheeps_in(my_sheep):
    for p in my_sheep:
        if p[0] > 700 and p[1] > 700:
            return True
    return False


'''准备数据补充'''
target = np.array([750, 750])


shepherd_point = position_point(shepherd.position())

'''集群和驱赶交替进行'''

while True:
    g_sh_array = X[index_g]
    b_sh_array = X[index_b]
    g_g_mean = np.array([np.mean(g_sh_array[:, 0]), np.mean(g_sh_array[:, 1])])
    if check(g_sh_array, g_g_mean):
        break
        driving(shepherd_point, target, g_sh_array, g_g_mean, k, index_g)
    else:
        X = collecting(shepherd_point, g_sh_array, g_g_mean, k, b_sh_array, X)
    g_sh_array = X[index_g]
    if all_sheeps_in(g_sh_array):
        break
    tk.update()
    time.sleep(0.01)

label = Label(tk, text="游戏结束!", font=('楷体', 40), fg='red')
label.pack()
tk.mainloop()