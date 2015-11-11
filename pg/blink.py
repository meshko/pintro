import pygame
 
screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()
r=0
g=0
b=0
d=5
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((r, g, b))
    r=r+d
    g=g+d
    b=b+d
    if r==255:
        d= d * (-1)
    if r==0:
        d= d * (-1)
    pygame.display.flip()
   # clock.tick(240)