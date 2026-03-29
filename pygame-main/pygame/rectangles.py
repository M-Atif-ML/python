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


width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

dir = {K_LEFT: (-10, 0), K_RIGHT: (10, 0), K_UP: (0, -10), K_DOWN: (0, 10)}



points = [(random.randint(0,width) , random.randint(0,height)) for _ in range(300)]
print(points)

print(points)

rect = Rect(50, 60, 200, 80)
rect1 = Rect(100, 20, 100, 140)
moving_rect = Rect(30,50,200,80)
self_moving_rect = Rect(100, 50, 50, 50)
colliding_rect = Rect(200,80,200,100)
v = [1,1]

moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN :
            moving = True
        if event.type == MOUSEBUTTONUP:
            moving = False

        if event.type == MOUSEMOTION and moving:
        
            colliding_rect.move_ip(event.rel)


    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, colliding_rect,1)


    for point in points:
        if colliding_rect.collidepoint(point):
            pygame.draw.circle(screen,RED,point,4,0)
        else:
            pygame.draw.circle(screen,BLUE,point,4,0)





    pygame.display.flip()

pygame.quit()