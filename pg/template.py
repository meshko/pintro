import pygame
 
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
