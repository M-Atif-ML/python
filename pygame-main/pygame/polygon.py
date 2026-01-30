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

pygame.init()



screen = pygame.display.set_mode((640, 240))


running = True


drawing = False
points = []

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			points.append(event.pos)
			drawing = True
		if event.type == pygame.MOUSEBUTTONUP:
			drawing = False
		if event.type == pygame.MOUSEMOTION and drawing:
			points[-1] = event.pos

	# print(drawing)
	screen.fill((127,127,127))
	if len(points)>1:
		pygame.draw.lines(screen,RED,True,points,3)
		# pygame.draw.rect(screen,GREEN,rect,1)

	pygame.display.update()

pygame.quit()