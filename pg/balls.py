import pygame
import random
from random import randrange
from math import sqrt

import coll

def make_test_balls():
   balls.append([[100, 200],[100,100,100],20,[10,1]])
   balls.append([[200, 200],[100,100,100],20,[-10,-1]])
   balls.append([[300, 200],[100,100,100],20,[10,1]])
   balls.append([[400, 200],[100,100,100],20,[-10,-1]])
   balls.append([[100, 250],[100,100,100],20,[10,1]])
   balls.append([[200, 250],[100,100,100],20,[-10,-1]])
   balls.append([[300, 250],[100,100,100],20,[10,1]])
   balls.append([[400, 250],[100,100,100],20,[-10,-1]])
   balls.append([[100, 300],[100,100,100],20,[10,1]])
   balls.append([[200, 300],[100,100,100],20,[-10,-1]])
   balls.append([[300, 300],[100,100,100],20,[10,1]])
   balls.append([[400, 300],[100,100,100],20,[-10,-1]])
   balls.append([[100, 350],[100,100,100],20,[10,1]])
   balls.append([[200, 350],[100,100,100],20,[-10,-1]])
   balls.append([[300, 350],[100,100,100],20,[10,1]])
   balls.append([[400, 350],[100,100,100],20,[-10,-1]])
   balls.append([[100, 400],[100,100,100],20,[10,1]])
   balls.append([[200, 400],[100,100,100],20,[-10,-1]])
   balls.append([[300, 400],[100,100,100],20,[10,1]])
   balls.append([[400, 400],[100,100,100],20,[-10,-1]])
   balls.append([[100, 450],[100,100,100],20,[10,1]])
   balls.append([[200, 450],[100,100,100],20,[-10,-1]])
   balls.append([[300, 450],[100,100,100],20,[10,1]])
   balls.append([[400, 450],[100,100,100],20,[-10,-1]])


def ball_distance(ball1, ball2):
   xd = ball1[0][0] - ball2[0][0]
   yd = ball1[0][1] - ball2[0][1]
   return sqrt(xd*xd + yd*yd)

screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
balls = []
for _ in range(0, 20):
     radius = randrange(10,20)
     ball = [[randrange(radius, 800-radius), randrange(radius, 600-radius)], [randrange(255), randrange(255), randrange(255)], radius, [randrange(-5, 5), randrange(-5, 5)]]
     #balls.append(ball)

#balls = []
make_test_balls()

colliding = set()
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 40, 0))
    for i in range(0, len(balls)):
        ball = balls[i]
        pygame.draw.circle(screen, ball[1], (int(ball[0][0]), int(ball[0][1])),  ball[2])
        newx = ball[0][0] + ball[3][0]
        newy = ball[0][1] + ball[3][1]
        if newx > 800 - ball[2] or newx < ball[2]:
            ball[3][0] *= -1
        if newy > 600 - ball[2] or newy < ball[2]:
            ball[3][1] *= -1
        #ball[3][1] += .2
        #new_ball = [[min(800-radius,max(radius,newx)), min(600-radius,max(radius,newy))], [], ball[2], ball[3]]
        #move = True
        #for j in range(i+1, len(balls)):
        #    other_ball = balls[j]
        #    dist = ball_distance(new_ball, other_ball)
        #    if dist <= ball[2] + other_ball[2]:
        #        print "collision", balls
        #        vs = coll.collide(ball, other_ball)
        #        ball[3] = vs[1]
        #        other_ball[3] = vs[0]
        #        newx += vs[1][0]
        #        newy += vs[1][1]
        #        break
        #if move:
        ball[0] = [min(800-radius,max(radius,newx)), min(600-radius,max(radius,newy))]

    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            dist = ball_distance(balls[i], balls[j]) 
            if dist <= balls[i][2] + balls[j][2]:                
                if (i,j) not in colliding:
                    #print "collision: ", balls[i], balls[j]
                    colliding.add((i,j))
                    vs = coll.collide(balls[i], balls[j])
                    balls[i][3] = vs[0]
                    balls[j][3] = vs[1]
            elif (i,j) in colliding:
              colliding.remove((i,j))
    #colliding = new_colliding
    pygame.display.flip()
    clock.tick(20)


