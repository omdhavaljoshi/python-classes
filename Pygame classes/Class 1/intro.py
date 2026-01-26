# Pygame ->
import pygame,random

# Create a window ->
pygame.init()
height = 500
width = 500
screen = pygame.display.set_mode((height,width))
posX = 100
posY = 100
speedX = random.randint(-5,5)
speedY = random.randint(-5,5)
clock = pygame.time.Clock()
bg = pygame.image.load(r"/Users/omjoshi/Library/CloudStorage/OneDrive-Personal/Coding/Python coding class/Pygame classes/Class 1/night 2.png")
bgImage = pygame.transform.scale(bg,(width,height))

class Ball(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.image.load(r"/Users/omjoshi/Library/CloudStorage/OneDrive-Personal/Coding/Python coding class/Pygame classes/Class 1/lan3.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(center=(posX,posY))
        self.Ypos = posY
        self.speed = random.randint(1,3)
    
    def update(self):
        self.Ypos -= self.speed
        self.rect.y = self.Ypos

balls = []
sprite_ball_group = pygame.sprite.Group()
for i in range(10):
    ball = Ball(random.randint(10,width-10), height-100)
    balls.append(ball)

for ball in balls: 
    sprite_ball_group.add(ball)

# Loop ->
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speedX += 2
                if speedY >= -2:
                    speedY += 1
            elif event.key == pygame.K_DOWN:
                speedX -= 2
                speedY -= 2
            elif event.key == pygame.K_LEFT:
                posX -= 2
            elif event.key == pygame.K_RIGHT:
                posX += 2
    posX += speedX
    posY += speedY
    if posX >= 500 or posX <= 0:
        speedX = -speedX
    if posY >= 500 or posY <= 0:
        speedY = -speedY
    screen.fill("White")
    # pygame.draw.rect(screen,"green",(posX,posY,100,100))
    screen.blit(bgImage,(0,0))
    pygame.draw.circle(screen,"Red",(posX,posY),30)
    sprite_ball_group.draw(screen)
    sprite_ball_group.update()
    pygame.display.flip()