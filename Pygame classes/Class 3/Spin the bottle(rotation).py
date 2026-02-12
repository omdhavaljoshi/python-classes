import pygame


pygame.init()


h,w = 500,500

screen  = pygame.display.set_mode((w,h))
pygame.display.set_caption("Truth and dare")

class Bottle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.loadedImage =  pygame.image.load(r"Pygame classes/Class 3/green bottle.png")
        self.loadedImage = pygame.transform.scale(self.loadedImage,(80,120))
        
        
        self.image = self.loadedImage
        self.rect = self.image.get_rect(center=(w//2,h//2))
       
        self.center = (self.rect.x,self.rect.y)
        self.angle = 1
        
    def update(self):
        self.angle = (self.angle+1)%360
        self.image = pygame.transform.rotate(self.loadedImage,self.angle)
        
        self.rect = self.image.get_rect(center=self.center)
        

runninStatus = True


bottle = Bottle()
clock = pygame.time.Clock()
bottle_group = pygame.sprite.Group()
bottle_group.add(bottle)

while runninStatus:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninStatus = False
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX,mousey)= pygame.mouse.get_pos()
            print(mouseX,mousey) 
    screen.fill("red")
    bottle_group.draw(screen)
    bottle_group.update()
    pygame.display.update()


pygame.quit()