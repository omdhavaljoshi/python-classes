import pygame,random
pygame.init()

width,height = 600,400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background_img = pygame.image.load(r"Pygame classes/Class 4/background image.png")
b_img = pygame.transform.scale(background_img, (width,height))
stars =[]
count = 0

class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.original_img = pygame.image.load(r"Pygame classes/Class 4/sun.png")
        self.original_img = pygame.transform.scale(self.original_img, (25,25))
        self.image = self.original_img
        self.rect = self.image.get_rect(center = (80,80))
        self.angle = 0

    def update(self):
        old_center = (self.rect.center)
        self.angle = (self.angle + 1)%360
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect(center = old_center)

class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.original_img = pygame.image.load(r"Pygame classes/Class 4/earth.png")
        self.original_img = pygame.transform.scale(self.original_img, (150,150))
        self.image = self.original_img
        self.rect = self.image.get_rect(center = (300,170))
        self.angle = 0

    def update(self):
        old_center = (self.rect.center)
        self.angle = (self.angle + 1)%360
        self.image = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect(center = old_center)

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.image = pygame.image.load(r"Pygame classes/Class 4/star.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(center = (random.randint(0,600),random.randint(0,400)))
        self.speedX = 1
        self.speedY = 1

    def update(self):
        global count
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if count == 120:
            for i in range(5):
                star = Star()
                stars.append(star)
            for star in stars:
                star_group.add(star)
            count = 0
        
        
sun = Sun()
earth = Earth()
for i in range(5):
    star = Star()
    stars.append(star)
star_group = pygame.sprite.Group()
planet_group = pygame.sprite.Group()
star_group.add(sun)
planet_group.add(earth)
for star in stars:
    star_group.add(star)

running = True
while running:
    count += 1
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.blit(b_img,(0,0))
    star_group.draw(screen)
    star_group.update()
    planet_group.draw(screen)
    planet_group.update()
    pygame.display.flip()
    clock.tick(60)
