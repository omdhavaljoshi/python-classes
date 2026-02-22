import pygame
pygame.init()

# Background Images -->
bg = pygame.image.load(r"Pygame classes/Class 1/bg (1).png")
ground_img = pygame.image.load(r"Pygame classes/Dino game/ground.png")

# Variables -->
h,w = 800,800
clock = pygame.time.Clock()
groundx = 0
groundSpeed = 4
screen  = pygame.display.set_mode((w,h))
pygame.display.set_caption("Dino game")
dinoY = h-210
dinoX = 100

# Sprites -->
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.index = 0
        for i in range(1,9):
            self.image = pygame.image.load(r"/Users/omjoshi/Library/CloudStorage/OneDrive-Personal/Coding/Python coding class/Pygame classes/Dino game/Run "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.images.append(self.image)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (dinoX,dinoY))
        self.counter = 0
    
    def run(self):
        self.counter+=1
        if self.counter >= 8:
            self.counter = 0
            self.index += 1
            if self.index > len(self.images)-1:
                self.index = 0
            self.image = self.images[self.index]
    
    def update(self):
        self.run()
    
dino = Dino()
player_group = pygame.sprite.Group()
player_group.add(dino)

runninStatus = True
while runninStatus:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninStatus = False
    # Scroll Logic -->
    groundx -= groundSpeed
    if groundx <= -102:
        groundx = 0
    
    screen.blit(bg,(0,0))
    screen.blit(ground_img,(groundx,h-150))
    player_group.draw(screen)
    player_group.update()

    pygame.display.update()

pygame.quit()