# Pygame ->
import pygame

# Create a window ->
pygame.init()
height = 500
width = 500
screen = pygame.display.set_mode((height,width))
posX = 100
posY = 100

# Loop ->
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posY -= 2
            elif event.key == pygame.K_DOWN:
                posY += 2
            elif event.key == pygame.K_LEFT:
                posX -= 2
            elif event.key == pygame.K_RIGHT:
                posX += 2

    screen.fill("RED")
    pygame.draw.rect(screen,"green",(posX,posY,100,100))
    pygame.display.flip()