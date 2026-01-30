import pygame
# from rect import *
from pygame.locals import *
import random

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
pygame.init()

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
        'midtop', 'midright', 'midbottom', 'midleft', 'center')


width = 640
height = 220
screen = pygame.display.set_mode((640,220))

dir = {K_LEFT: (-10, 0), K_RIGHT: (10, 0), K_UP: (0, -10), K_DOWN: (0, 10)}



points = [(random.randint(0,width) , random.randint(0,height)) for _ in range(100)]
print(points)

print(points)

rect = Rect(50, 60, 200, 80)
rect1 = Rect(100, 20, 100, 140)
moving_rect = Rect(30,50,200,80)
self_moving_rect = Rect(100, 50, 50, 50)
# colliding_rect = 
v = [1,1]

moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN :
            if moving_rect.collidepoint(event.pos):
                moving = True
        if event.type == MOUSEBUTTONUP:
            moving = False

        if event.type == MOUSEMOTION and moving:
        
            moving_rect.move_ip(event.rel)

    # self_moving_rect.move_ip(v)
    # if self_moving_rect.left < 0:
    #     v[0] *= -1
    # if self_moving_rect.right > width:
    #     v[0] *= -1
    # if self_moving_rect.top < 0:
    #     v[1] *= -1
    # if self_moving_rect.bottom > height:
    #     v[1] *= -1
   
    screen.fill(GRAY)
    # pygame.draw.rect(screen, BLUE, self_moving_rect)


    for point in points:
        # print()
        pygame.draw.circle(screen,BLUE,point,4,0)



    # pygame.draw.rect(screen, RED, moving_rect)
    # if rect.colliderect(moving_rect):
    #     pygame.draw.rect(screen, GREEN, rect)

    # if moving:
    #     pygame.draw.rect(screen, BLUE, moving_rect, 4)

    pygame.display.flip()

pygame.quit()