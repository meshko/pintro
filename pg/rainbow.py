import pygame
import random
import math
import colorsys

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
hue = 0
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    hue += 1.0 / 7.0 / 10
    if hue > 1:
       hue = 0 
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    screen.fill((int(r * 255), int(g * 255), int(b * 255)))
    pygame.display.flip()
    clock.tick(10)
