from tkinter import *
import numpy as np
import time
import math

tk = Tk()
tk.title('shepherd')
tk.wm_attributes("-topmost", 1)

Width = 600
Height = 600
canvas = Canvas(tk, width=Width, height=Height, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_line(Height - 150, Height - 150, Height - 150, Height, Height - 150, Height - 150, Height, Height - 150)
tk.update()
X = []

sheep_view_distance = 200
repulsion_distance = 12

speed = 5
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
        """"返回目标当前的位置"""
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


def sheeps_move(shepherd_farthest, shepherd_max_angle, all_sheep, k_nearest,
                sheep_view_distance, repulsion_distance, speed):
    """
    羊根据牧羊犬的位置的移动情况,如果两者之间的距离大于视野距离，则羊只进行简单的随机运动，
    否则牧羊犬会受到五个不同方向的线性合力，作为下一次位置的计算方法
    """
    number_of_sheep = len(all_sheep)
    new_displacement_of_all_sheep = np.zeros((number_of_sheep, 2), dtype=np.float64)
    for i in range(number_of_sheep):
        per_sheep = agent['sheep' + str(i)].position2point()
        centroid_to_sheep_distance_angle = np.linalg.norm(per_sheep - shepherd_max_angle)

        # 获取到局部中心点和靠太近的排斥力
        local_mean, ra = knn(per_sheep, all_sheep, k_nearest, repulsion_distance)
        centroid_to_sheep_distance_farthest = np.linalg.norm(per_sheep - shepherd_farthest)

        current_vector = 2 * ra
        judge_generate_repulsion = False
        if centroid_to_sheep_distance_angle <= sheep_view_distance:
            repulsion_force_1 = (per_sheep - shepherd_max_angle) / centroid_to_sheep_distance_angle
            current_vector += 0.7*repulsion_force_1
            judge_generate_repulsion = True
        elif centroid_to_sheep_distance_farthest <= sheep_view_distance:
            repulsion_force_2 = (per_sheep - shepherd_farthest) / centroid_to_sheep_distance_farthest
            print("repulsion_force_2", repulsion_force_2)
            print("before", current_vector)
            current_vector += repulsion_force_2
            print("after", current_vector)
            judge_generate_repulsion = True
        if judge_generate_repulsion:
            local_force = (local_mean - per_sheep) / np.linalg.norm(local_mean - per_sheep)
            current_vector += 1.05*local_force
        current_unit_vector = current_vector / np.linalg.norm(current_vector)

        displacement_of_sheep = current_unit_vector * speed
        agent['sheep' + str(i)].x = displacement_of_sheep[0]
        agent['sheep' + str(i)].y = displacement_of_sheep[1]
        agent['sheep' + str(i)].draw()
        new_displacement_of_all_sheep[i] = displacement_of_sheep

    for i in range(number_of_sheep):
        per_sheep = agent['sheep' + str(i)].position2point()
        all_sheep[i] = new_displacement_of_all_sheep[i] + per_sheep

    return all_sheep


def driving(shepherd_2, shepherd_1, target, array, g_mean):
    """把羊往目标点驱赶"""
    shepherd_farthest = shepherd_1.position2point()
    shepherd_max_angle = shepherd_2.position2point()


    sheeps_move(shep, array)
    gt_dist = np.linalg.norm(target - g_mean)
    Pd = (g_mean - target) / gt_dist * approach + g_mean
    rd = (Pd - herd) / np.linalg.norm(Pd - herd) * speeds
    shepherd.x = rd[0]
    shepherd.y = rd[1]
    rd = rd + herd
    g_mean = np.array([np.mean(array[:, 0]), np.mean(array[:, 1])])
    shepherd.draw()
    return array, g_mean, rd


def collecting(shepherd_1, shepherd_2, all_sheep, global_mean, k_nearest, sheep_view_distance,
               repulsion_distance, speed):
    """
    目标：把远离中心的羊聚集起来
    1、找到最大距离的羊
    2、找到最大角度的羊
    3、计算两个牧羊犬下一次的位置
    4、计算羊的下一次的位置
    5、返回中心值和牧羊犬与羊的新位置

    """
    shepherd_farthest = shepherd_1.position2point()
    shepherd_max_angle = shepherd_2.position2point()
    # 找到最远距离的羊
    farthest_index = find_farthest_sheep(all_sheep, global_mean)
    farthest_sheep = agent['sheep' + str(farthest_index)].position2point()
    # 找到最大角度的羊
    max_angle_sheep_index = find_max_angle_sheep(shepherd_max_angle, global_mean, all_sheep)
    max_angle_sheep = agent['sheep' + str(max_angle_sheep_index)].position2point()

    speeds = speed * 1.5
    # 最大距离牧羊犬的下一次的位置
    centroid_to_sheep_distance_1 = np.linalg.norm(shepherd_farthest - global_mean)
    target_position_1 = (shepherd_farthest - global_mean) / centroid_to_sheep_distance_1 * 100 + farthest_sheep
    displacement_of_farthest_shepherd = (target_position_1 - shepherd_farthest) \
                                        / np.linalg.norm(target_position_1 - shepherd_farthest) * speeds

    # 最大角度牧羊犬的下一次的位置
    centroid_to_sheep_distance_2 = np.linalg.norm(max_angle_sheep - global_mean)
    target_position_2 = (max_angle_sheep - global_mean) / centroid_to_sheep_distance_2 * 100 + max_angle_sheep
    displacement_of_max_angle_shepherd = (target_position_2 - shepherd_max_angle) \
                                         / np.linalg.norm(target_position_2 - shepherd_max_angle) * speeds

    all_sheep = sheeps_move(shepherd_farthest, shepherd_max_angle, all_sheep, k_nearest, sheep_view_distance,
                            repulsion_distance, speed)

    shepherd_1.x = displacement_of_farthest_shepherd[0]
    shepherd_1.y = displacement_of_farthest_shepherd[1]

    shepherd_2.x = displacement_of_max_angle_shepherd[0]
    shepherd_2.y = displacement_of_max_angle_shepherd[1]
    # 计算新中心值
    global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    shepherd_1.draw()
    shepherd_2.draw()
    return all_sheep, global_mean, shepherd_1, shepherd_2


def find_nerest_dist(arrv, herd):
    """找离牧羊犬最近的羊"""
    d = [np.linalg.norm(x - herd) for x in arrv]
    near = np.argsort(d)
    ner = arrv[near[0]]
    gt_dist = np.linalg.norm(ner - herd)
    return gt_dist


def find_max_angle_sheep(p, center, all_sheep):
    """找到最大角度的羊，作为目标点"""
    d = [math.sqrt(np.sum((x - p) ** 2)) for x in all_sheep]
    dx = math.sqrt(np.sum((center - p) ** 2))
    OA = center - p
    OB = all_sheep - p
    m = len(all_sheep)
    t = [OA.dot(OB[i, :]) / dx / d[i] for i in range(m)]
    far = np.argsort(t)
    return far[0]


def knn(per_sheep, all_sheep, k, repulsion_distance):
    """根据给出的坐标，计算出与该坐标最近的k个点,并返回局部中心点和羊内部作用力的合力方向"""
    d = [np.linalg.norm(per_sheep - sheep) for sheep in all_sheep]
    near = np.argsort(d)
    top = [all_sheep[v] for v in near[1:k + 1]]
    t = np.array(top)
    local_m = [np.mean(t[:, 0]), np.mean(t[:, 1])]
    local_m = np.array(local_m, np.float64)
    ra = np.zeros(2, dtype=np.float64)
    for p in near[1:k + 1]:
        if d[p] <= repulsion_distance:
            ra += (per_sheep - all_sheep[p]) / np.linalg.norm(per_sheep - all_sheep[p])
    return local_m, ra

def check(lst, g_mean):
    """对所有的羊检查是否都在全局中心点的Fn半径范围内"""
    d = [np.linalg.norm(x - g_mean) for x in lst]
    D = np.array(d)
    return np.all(D <= Fn)


def find_farthest_sheep(all_sheep, g_m):
    """找到离中心最远的羊"""
    d = [np.linalg.norm(x - g_m) for x in all_sheep]
    return np.argmax(d)



def all_sheeps_in(arrx):
    """判断是否所有羊都到达了目标范围"""
    for p in arrx:
        if p[0] < Height - 145 or p[1] < Height - 145:
            return False
    return True


target = np.array([Height - 40, Height - 40])
N = 80
X = []
k_nearest = N // 2 + 5
Fn = N + 30
agent = {}

for i in range(N):
    np.random.seed(i)
    x = np.random.randint(50, 500)
    y = np.random.randint(50, 500)
    X.append([x, y])
    agent['sheep' + str(i)] = Agent(x - 5, y - 5, x + 5, y + 5, 'green')
X = np.array(X)

shepherd_1 = Agent(550, 550, 560, 560, 'black')
shepherd_2 = Agent(0, 0, 10, 10, 'red')

shepherd_point_1 = shepherd_1.position2point()
shepherd_point_2 = shepherd_2.position2point()
global_mean = np.array([np.mean(X[:, 0]), np.mean(X[:, 1])])


step = 0
while True:
    if check(X, global_mean):
        break
        # X, global_mean, shepherd_1, shepherd_2 = driving(shepherd_1, shepherd_2, target, X, global_mean
        #                                                  , sheep_view_distance, repulsion_distance)
    else:
        X, global_mean, shepherd_1, shepherd_2 = collecting(shepherd_1, shepherd_2, X, global_mean,
                                                                      k_nearest, sheep_view_distance,
                                                                      repulsion_distance, speed)
    if all_sheeps_in(X) or step > 4000:
        break
    tk.update()
    time.sleep(0.01)
    step += 1


label = Label(tk, text="游戏结束!", font=('楷体', 40), fg='red')
label.place(x=175, y=285)
tk.mainloop()
