import numpy as np
import pygame

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

center = np.array([W / 2, H / 2])


R = 250


r = 12


g = np.array([0, 500])


N = 8

# Position of all balls
pos = np.array([
    [300, 150],
    [400, 200],
    [200, 200],
    [350, 300],
    [250, 350],
    [400, 400],
    [200, 400],
    [300, 450]
], dtype=float)

# Velocity of all balls
vel = np.random.uniform(-200, 200, (N, 2))

# Colours
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "cyan"
]

running = True

while running:

    dt = clock.tick(60) / 1000

   

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False



    vel += g * dt



    pos += vel * dt



    for i in range(N):

        d = pos[i] - center

        distance = np.linalg.norm(d)

        if distance + r > R:

            # Direction from centre to ball
            n = d / distance

            # Push ball back inside
            offset = distance + r - R

            pos[i] -= n * offset

            # Bounce off boundary
            vel[i] = vel[i] - 2 * np.dot(vel[i], n) * n



    for i in range(N):

        for j in range(i + 1, N):

           
            d = pos[j] - pos[i]

            distance = np.linalg.norm(d)

            # Check if balls are touching
            if distance < 2 * r and distance != 0:

                # Collision direction
                n = d / distance

                # Relative velocity
                relative_velocity = vel[j] - vel[i]

                
                if np.dot(relative_velocity, n) < 0:

                    # Elastic collision
                    impulse = np.dot(relative_velocity, n)

                    vel[i] += impulse * n
                    vel[j] -= impulse * n

               
                overlap = 2 * r - distance

                
                pos[i] -= n * (overlap / 2)
                pos[j] += n * (overlap / 2)



    screen.fill("black")

    
    pygame.draw.circle(
        screen,
        "white",
        center.astype(int),
        R,
        2
    )

    
    for i in range(N):

        pygame.draw.circle(
            screen,
            colors[i],
            pos[i].astype(int),
            r
        )

    pygame.display.flip()

pygame.quit()
