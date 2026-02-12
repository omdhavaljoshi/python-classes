import pygame
pygame.init()

width,height = 600,400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background_img = pygame.image.load(r"Pygame classes/Class 4/background image.png")
b_img = pygame.transform.scale(background_img, (width,height))

class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.original_img = pygame.image.load(r"Pygame classes/Class 4/sun.png")
        self.original_img = pygame.transform.scale(self.original_img, (50,50))
        self.image = self.original_img
        self.rect = self.image.get_rect(center = (80,80))
        self.angle = 0

    def update(self):
        old_center = (self.rect.center)
        self.angle = (self.angle + 1)%360
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect(center = old_center)

class Earth(pygame.sprite.Sprite):
    pass

sun = Sun()
star_group = pygame.sprite.Group()
star_group.add(sun)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.blit(b_img,(0,0))
    star_group.draw(screen)
    star_group.update()
    pygame.display.flip()
    clock.tick(60)
