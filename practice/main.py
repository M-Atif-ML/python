import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Project")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# floor rectanglge 
width_floor = WIDTH
height_floor = 50
floor = pygame.Rect(0,HEIGHT-25,width_floor,height_floor)

# player rectangle

width_player = 20
height_player= 60

player = pygame.Rect(WIDTH//2,HEIGHT//2,width_player,height_player)


# Game loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here
    

    # Drawing
    screen.fill(BLACK)  # Clear screen

    pygame.draw.rect(screen,(0,255,0),floor)
    
    pygame.draw.rect(screen,(255,0,0),player)
    player.x += 1
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

