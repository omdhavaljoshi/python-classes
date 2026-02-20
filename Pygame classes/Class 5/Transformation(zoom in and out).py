import pygame,math
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(r"path")
# pygame.mixer.music.play()
# pygame.mixer.music.set_volume() #0-1
h,w=400,600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

bg = pygame.image.load(r"Pygame classes/Class 5/soccer feild.jpg")
bg_img = pygame.transform.scale(bg,(w,h))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.orgImage = pygame.image.load(r"Pygame classes/Class 5/Soccerball.png")
        self.orgImage = pygame.transform.scale(self.orgImage,(100,100))
        self.image = self.orgImage
        self.rect = self.image.get_rect(center=(w//2,h//2))
        self.ballHeight = 100
        self.ballWidth = 100
        self.angle = 1
        self.scale_ = 1
        self.flyingUpState = False
        self.count = 0.0
        self.maginifier = 5
    def update(self):
        # scale
        self.count += 0.05 
        old_center = self.rect.center
        keys = pygame.key.get_pressed()
        scaleValue = self.scale_ + self.maginifier* math.sin(self.count) 
        self.image = pygame.transform.rotozoom(self.orgImage,self.angle,scaleValue)
        self.rect = self.image.get_rect(center=old_center)
        # if self.scale_<=2 and self.flyingUpState == False:
        #     print(self.scale_,self.flyingUpState)
        #     self.scale_ +=0.02
        #     self.angle +=1
        #     self.ballHeight += 10
        #     self.ballWidth +=10
        #     self.image = pygame.transform.rotozoom(self.orgImage,self.angle,self.scale_)
        #     self.rect = self.image.get_rect(center=old_center)
        #     if self.scale_ >= 2:
        #         self.flyingUpState = True
        # if  self.flyingUpState == True:
        #     print(self.scale_,self.flyingUpState)
        #     self.angle +=2
        #     self.ballHeight -= 10
        #     self.ballWidth -=10
        #     self.scale_ -=0.02
        #     self.image = pygame.transform.rotozoom(self.orgImage,self.angle,self.scale_)
        #     self.rect = self.image.get_rect(center=old_center)
        #     if self.scale_<=1:
        #         self.flyingUpState = False
            
        
        
ball = Ball()
ballG = pygame.sprite.Group()
ballG.add(ball)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(bg_img,(0,0))
    ballG.draw(screen)
    ballG.update()

    pygame.display.flip()
    clock.tick(60)
