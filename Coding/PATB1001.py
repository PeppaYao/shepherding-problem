if __name__ == '__main__':
    n = int(input())
    step = 0
    while n != 1:
        if n % 2 == 1:
            n = (3*n + 1)//2
        else:
            n >>= 1
        step += 1
    print(step)