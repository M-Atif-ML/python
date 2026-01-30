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

start = (0,0)
end= (0,0)
size = (0,0)
drawing = False
rect_list =  []

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			start = event.pos
			size = 0,0
			drawing = True
		elif event.type == pygame.MOUSEBUTTONUP:
			end = event.pos
			size = end[0] -start[0],end[1]-start[1]
			rect = pygame.Rect(start,size)
			rect_list.append(rect)
			drawing = False
		elif event.type == pygame.MOUSEMOTION and drawing:
			end = event.pos
			size = end[0]-start[0] , end[1]-start[1]

	# print(drawing)
	screen.fill((127,127,127))

	for rect in rect_list:	
		pygame.draw.rect(screen, RED, rect, 2)
	pygame.draw.rect(screen, BLUE, (start, size), 1)
	pygame.display.update()

pygame.quit()