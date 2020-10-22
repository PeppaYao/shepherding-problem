from tkinter import *
import numpy as np
import time
import math

tk = Tk()
tk.title('ADshepherd_raw')
tk.wm_attributes("-topmost", 1)
Width = 600
Height = 600
canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
tk.update()

Rs = 250
Ra = 14

speed = 5
speed_of_herd = 1.5 * speed
approach = 65


class Agent:
    def __init__(self, canvas, x, y, u, v, color, shape):
        """对目标对象进行初始化"""
        self.canvas = canvas
        self.color = color
        self.id = None
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.shape = shape
        self.color = color
        self.id = self.create_agent()
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)
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


    def position(self):
        """返回目标当前的位置"""
        pos = self.canvas.coords(self.id)
        return pos

    def draw(self):
        """绘制目标对象的运动状态"""
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
        """把目标的两个坐标转换为中心的一个坐标"""
        pos = self.position()
        point = [0.0, 0.0]
        point[0] = (pos[0] + pos[2]) / 2
        point[1] = (pos[1] + pos[3]) / 2
        return np.array(point)

    def delete(self):
        """删除目标对象"""
        self.canvas.delete(self.id)

    def stop(self):
        """当目标对象到达指定区域则停止运动"""
        self.tag = False


def sheeps_move(herd, array):
    """羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于100米，则羊只进行简单的随机运动，否则牧羊犬会受到五个不同方向的线性合力"""
    n = len(array)
    last = np.zeros((n, 2), dtype=np.float32)
    for i in range(n):
        point = agent['sheep' + str(i)].position2point()
        ps_dist = np.linalg.norm(point - herd)
        if ps_dist > Rs:
            h = np.random.uniform(-1, 1, size=2)  # H为-1到1随机运动的大小
            h = h / np.linalg.norm(h)  # 把数据归一化
            last[i] = h
        else:
            rs = (point - herd) / ps_dist
            l_mean = local(point, array)
            ra = repulsion(point, array)
            c = (l_mean - point) / np.linalg.norm(l_mean - point)
            h = 0.5 * last[i] + 1.05 * c + rs + 2 * ra + 0.5 * np.random.uniform(-0.5, 0.5, size=2)
            h = h / np.linalg.norm(h)
            last[i] = h
            h = h * speed
        agent['sheep' + str(i)].x = h[0]
        agent['sheep' + str(i)].y = h[1]
        array[i] = last[i] + point
        agent['sheep' + str(i)].draw()


def driving(herd, target, array, g_mean):
    """把羊往目标点驱赶"""
    text = canvas.create_text(190, 20, text="驱赶", font=('楷体', 20))
    canvas.pack()
    sheeps_move(herd, array)
    gt_dist = np.linalg.norm(target - g_mean)
    pd = (g_mean - target) / gt_dist * approach + g_mean
    rd = (pd - herd) / np.linalg.norm(pd - herd) * speed_of_herd
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd, text


def collecting(herd, array, g_mean):
    """把远离中心的羊聚集起来"""
    text = canvas.create_text(190, 20, text="聚集", font=('楷体', 20))
    canvas.pack()
    far = find_farest(array, g_mean)
    sheeps_move(herd, array)
    gt_dist = np.linalg.norm(far - g_mean)
    pc = (far - g_mean) / gt_dist * approach + far
    rd = (pc - herd) / np.linalg.norm(pc - herd) * speed_of_herd
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd, text


def local(x, array):
    """
    羊和狼的视野距离差值和速度差值
    给出羊的视距范围Rs,然后以该羊为圆心，寻找整个羊群中在该羊形成的Rs的圆内的圆心
    """
    d = [np.linalg.norm(x_ - x) for x_ in array]
    L = [array[i] for i in range(1, len(array)) if d[i] < Rs]
    lcm = np.array(L)
    if len(lcm) > 0:
        Lmean = np.array([np.mean(lcm[:, 0]), np.mean(lcm[:, 1])])
    else:
        Lmean = np.zeros(2)
    return Lmean


def repulsion(x, array):
    d = [math.sqrt(np.sum((x_ - x) ** 2)) for x_ in array]
    r = np.zeros(2, dtype=np.float32)
    for i in range(1, len(array)):
        if d[i] <= Ra:
            r += (x - array[i]) / (math.sqrt(np.sum((x - array[i]) ** 2)))
    return r


def check(lst, g_mean):
    """对所有的羊检查是否都在全局中心点的Fn半径范围内"""
    d = [np.linalg.norm(x - g_mean) for x in lst]
    D = np.array(d)
    return np.all(D <= Fn)


def find_farest(arrv, g_m):
    """找到离中心最远的羊"""
    d = [np.linalg.norm(x - g_m) for x in arrv]
    nearr = np.argsort(d)
    return arrv[nearr[-1]]


def all_sheeps_in(arrx):
    """判断是否所有羊都到达了目标范围"""
    for p in arrx:
        if p[0] < Height - 145 or p[1] < Height - 145:
            return False
    return True


'''初始化的羊群'''
target = np.array([Height - 40, Height - 40])
colors = ['black', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple']
Y1 = []
X1 = []
N = 46
Fn = N + 40
agent = {}
X = list()
for i in range(N):
    np.random.seed(i)
    if i % 2 == 0:
        x = np.random.randint(10, 590)
        y = np.random.randint(10, 590)
        agent['sheep' + str(i)] = Agent(canvas, x - 5, y - 5, x + 5, y + 5, colors[1], 'oval')  # 绿色
        X.append([x, y])
    else:
        x = np.random.randint(10, 590)
        y = np.random.randint(10, 590)
        agent['sheep' + str(i)] = Agent(canvas, x - 5, y - 5, x + 5, y + 5, colors[2], 'rectangle')  # 蓝色
        X.append([x, y])

X = np.array(X)
shepherd = Agent(canvas, 560, 560, 560 + 10, 560 + 10, 'red', 'oval')
shepherd_point = shepherd.position2point()
step = 0
global_mean = np.array([np.mean(X[:, 0]), np.mean(X[:, 1])])

while True:
    if check(X, global_mean):
        X, global_mean, shepherd_point = driving(shepherd_point, target, X, global_mean)
    else:
        X, global_mean, shepherd_point, = collecting(shepherd_point, X, global_mean)
    if all_sheeps_in(X) or step > 8000:
        break
    tk.update()
    time.sleep(0.01)
    step += 1




'''动画结束'''
print("结束")
# label = Label(tk, text="动画结束!", font=('楷体', 20), fg='red')
# label.place(x=225, y=285)
tk.mainloop()
