import pygame
import random
from random import randrange

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    #screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), 
       (randrange(0, 800), randrange(0, 600), randrange(10, 90), randrange(10, 90)))
    pygame.display.flip()
    #clock.tick(24)
