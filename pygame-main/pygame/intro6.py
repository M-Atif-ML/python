import pygame 
from pygame.locals import *
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
size = 1040, 820
width, height = size


pygame.init()

screen = pygame.display.set_mode(size)


ball = pygame.image.load(r"ball.gif")
rect= ball.get_rect()
speed = [0,1]


background = GRAY
running = True

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

print(key_dict)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(background)

    rect = rect.move(speed)

    if rect.bottom > height:
        speed = [0,-1]
    if rect.top < 0:
        speed = [0,1]
 

    
    pygame.draw.circle(screen, RED, rect, 1)
    # pygame.draw.rect)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()