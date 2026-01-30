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
size = 640, 320
width, height = size


pygame.init()

screen = pygame.display.set_mode((640, 240))


ball = pygame.image.load(r"ball.gif")
rect= ball.get_rect()
speed = [2,2]


background = GRAY
running = True

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

print(key_dict)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEMOTION:
			print(event.pos, event.rel)
		if event.type == pygame.KEYDOWN:
			if event.key in key_dict:
				background = key_dict[event.key]

				caption = "Color: "+str(background)
				pygame.display.set_caption(caption)


	screen.fill(background)
	pygame.display.update()

pygame.quit()