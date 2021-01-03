# 装饰器
import time


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def calc_time(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("总耗时：{:.3f}".format(end - start))
        return result
    return inner


@calc_time
def prime_nums(maxNumber):
    count = 0
    for i in range(2, maxNumber):
        if is_prime(i):
            count += 1
    return count


print(prime_nums(5000))