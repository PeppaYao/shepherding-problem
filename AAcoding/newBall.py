# import pygame
#
# pygame.init()
# # 宽高
# screen = pygame.display.set_mode((600, 600))
# # 绘制背景图片
# bg_img = pygame.image.load("balls.gif")
# screen.blit(bg_img, (100, 100))
# pygame.display.update()
# while True:
#     pass


# import pygame
# pygame.init()
# screen = pygame.display.set_mode((600, 400))
# condition = True
# while condition:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             condition = False
# pygame.quit()


import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 400))
ball = pygame.image.load("balls.gif")
ball_rect = ball.get_rect()
print(ball_rect)
speed = [1, 1]
clock = pygame.time.Clock()
while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > 600:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > 400:
        speed[1] = -speed[1]
    screen.fill((255, 255, 255))
    screen.blit(ball, ball_rect)
    pygame.display.flip()
pygame.quit()