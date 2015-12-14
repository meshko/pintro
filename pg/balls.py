import pygame
import random
from random import randrange
from math import sqrt

import coll

def ball_distance(ball1, ball2):
   xd = ball1[0][0] - ball2[0][0]
   yd = ball1[0][1] - ball2[0][1]
   return sqrt(xd*xd + yd*yd)

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
balls = []
for _ in range(0, 20):
     ball = [[randrange(800), randrange(600)], [randrange(255), randrange(255), randrange(255)], randrange(10,20), [randrange(-10, 10), randrange(-10, 10)]]
     balls.append(ball)

#balls.append([[100, 200],[255,255,255],20,[10,1]])
#balls.append([[200, 200],[255,255,255],20,[-5,-1]])

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    for ball in balls:
        pygame.draw.circle(screen, ball[1], (int(ball[0][0]), int(ball[0][1])),  ball[2])
        ball[0][0] += ball[3][0]
        ball[0][1] += ball[3][1]
        if ball[0][0] > 800 - ball[2] or ball[0][0] < ball[2]:
            ball[3][0] *= -1
        if ball[0][1] > 600 - ball[2]  or ball[0][1] < ball[2]:
            ball[3][1] *= -1
        #ball[3][1] += .2
        if ball[0][1] > 600 - ball[2]:
           ball[0][1] = 600 - ball[2]
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if ball_distance(balls[i], balls[j]) <= balls[i][2] + balls[j][2]:
                #print "collision: ", balls[i], balls[j]
                vs = coll.collide(balls[i], balls[j])
                balls[i][3] = vs[0]
                balls[j][3] = vs[1]
    pygame.display.flip()
    clock.tick(20)


