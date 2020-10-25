# 装饰器：本质是一个函数
# 正月点灯笼视频：https://www.bilibili.com/video/BV11s411V7Dt
# 千锋教育视频：https://www.bilibili.com/video/BV12e411p79T?p=131
# 1. 把demo函数传给func函数
# 2. 再次调用demo()不再是原来的函数了，而是inner()函数的返回值
# 3. 也就是说加上装饰器后，实际执行的内容是内部类函数。

import time


def cal_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("time cost:", end-start)
    return inner()


@cal_time
def demo():
    x = 0
    for i in range(10000000):
        x += 1
    print(x)


demo()