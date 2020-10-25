
import pygame, sys
pygame.init()
size = width, height = 480, 600  # 窗口大小
speed = [1, 1]
BLACK = 255, 170, 180  # 窗口背景色RGB值
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Ball")
ball = pygame.image.load("balls.gif")  # 引入壁球
ballrect = ball.get_rect()  # 获取壁球大小
fps = 300
fclock = pygame.time.Clock()

# 三、获取事件并逐类响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 横向减速 减一个像素
                if speed[0] <= 0:
                    speed[0] = speed[0]
                else:
                    speed[0] = speed[0] - 1
            elif event.key == pygame.K_RIGHT:
                if speed[0] > 0:
                    speed[0] = speed[0] + 1
                else:
                    speed[0] = speed[0] - 1  # 负号表示方向
            elif event.key == pygame.K_UP:
                if speed[1] > 0:
                    speed[1] = speed[1] + 1
                else:
                    speed[1] = speed[1] - 1
            elif event.key == pygame.K_DOWN:
                if speed[1] <= 0:
                    speed[1] = speed[1]
                else:
                    speed[1] = speed[1] - 1
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    # 四、刷新屏幕
    pygame.display.update()
    fclock.tick(fps)



