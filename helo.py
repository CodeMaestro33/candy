import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Circle Animation")

x, y = 100, 100
radius = 20
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    x += speed
    if x > 800 - radius or x < radius:
        speed = -speed

    pygame.display.flip()  # Update the screen
    pygame.time.delay(30)

pygame.quit()
