import numpy as np
import pygame

pygame.init()

W, H = 300, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60
x = W // 2
y = 100.0
v = 300.0
r = 20
g = 500
running = True

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        y+= v*dt
        if(y>H):
            offset = y+r -H
            y-= offset
            v*= -1
        v+= g*dt


    screen.fill("black")
    pygame.draw.circle(screen, "red", (x, int(y)), r)
    pygame.display.flip()

pygame.quit()