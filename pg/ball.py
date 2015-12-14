import pygame
import random
from random import randrange

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
ball = [[randrange(800), randrange(600)], [randrange(255), randrange(255), randrange(255)], randrange(10,20), [randrange(-10, 10), randrange(-10, 10)]]
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, ball[1], (int(ball[0][0]), int(ball[0][1])),  ball[2])
    ball[0][0] += ball[3][0]
    ball[0][1] += ball[3][1]
    if ball[0][0] > 800 - ball[2] or ball[0][0] < ball[2]:
        ball[3][0] *= -1
    if ball[0][1] > 600 - ball[2]  or ball[0][1] < ball[2]:
        ball[3][1] *= -1
    #ball[3][1] += .2 # add gravity!
    if ball[0][1] > 600 - ball[2]:
        ball[0][1] = 600 - ball[2]
    pygame.display.flip()
    clock.tick(24)
