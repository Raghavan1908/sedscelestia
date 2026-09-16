import numpy as np
import pygame

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

center = np.array([W / 2, H / 2])

# Radius of circular boundary
R = 250

# Radius of each ball
r = 12

# Gravity
g = np.array([0, 500])

# Number of balls
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

    # -------------------------
    # CHECK EVENTS
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # -------------------------
    # GRAVITY
    # -------------------------

    vel += g * dt

    # -------------------------
    # MOVE ALL BALLS
    # -------------------------

    pos += vel * dt

    # -------------------------
    # BOUNDARY COLLISION
    # -------------------------

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

    # -------------------------
    # BALL-BALL COLLISION
    # -------------------------

    for i in range(N):

        for j in range(i + 1, N):

            # Vector from ball i to ball j
            d = pos[j] - pos[i]

            distance = np.linalg.norm(d)

            # Check if balls are touching
            if distance < 2 * r and distance != 0:

                # Collision direction
                n = d / distance

                # Relative velocity
                relative_velocity = vel[j] - vel[i]

                # Only collide if moving towards each other
                if np.dot(relative_velocity, n) < 0:

                    # Elastic collision
                    impulse = np.dot(relative_velocity, n)

                    vel[i] += impulse * n
                    vel[j] -= impulse * n

                # Calculate overlap
                overlap = 2 * r - distance

                # Push balls apart
                pos[i] -= n * (overlap / 2)
                pos[j] += n * (overlap / 2)

    # -------------------------
    # DRAW
    # -------------------------

    screen.fill("black")

    # Draw circular boundary
    pygame.draw.circle(
        screen,
        "white",
        center.astype(int),
        R,
        2
    )

    # Draw balls
    for i in range(N):

        pygame.draw.circle(
            screen,
            colors[i],
            pos[i].astype(int),
            r
        )

    pygame.display.flip()

pygame.quit()