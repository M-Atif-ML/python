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

size = (640, 240)

screen = pygame.display.set_mode(size)


running = True



while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(event)
		if event.type == pygame.MOUSEBUTTONUP:
			print(event)
		if event.type == pygame.MOUSEMOTION:
			print(event)

	screen.fill((127,127,127))
	# pygame.draw.rect(screen,RED,(50, 20, 120, 100))
	# pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
	# pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))

	# ellipse (circle have same procedure)

	pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
	pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
	pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))

	pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
	pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
	pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)

	pygame.display.update()

pygame.quit()