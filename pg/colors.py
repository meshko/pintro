import pygame
import random
import math

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
i = 0
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    rr = math.radians(i % 180)
    rg = math.radians((i + 30) % 180)
    rb = math.radians((i + 60) % 180)
    screen.fill((255 * math.sin(rr), 255 * math.sin(rg), 255 * math.sin(rb)))
    i = i + 5
    pygame.display.flip()
    #clock.tick(1)
