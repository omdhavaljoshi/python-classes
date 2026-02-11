import pygame,random

pygame.init()
height , width = 500,500
screen = pygame.display.set_mode((width,height))
bg = pygame.image.load(r"Pygame classes/Class 1/bg (1).png")
background_img = pygame.transform.scale(bg, (width,height))
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("monospace",20)
count = 0
balls_caught = 0
ball_speed = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.image = pygame.image.load(r"Pygame classes/Class 2/basket ball.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center = (posX,posY))
        self.Ypos = posY


    def update(self):
        self.Ypos += ball_speed
        self.rect.y = self.Ypos

class Basket(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.image = pygame.image.load(r"Pygame classes/Class 2/basketball_hoop_clipart_image-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect(center = (posX,posY))
        self.speed = 5
    
    def move_right(self):
        if self.rect.right < width:
            self.rect.x += self.speed
 
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

ball = Ball(random.randint(50,width-50),50)
basket = Basket(width//2,height-60)
basket_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
basket_group.add(basket)
ball_group.add(ball)

running = True
while running:
    count += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.sprite.spritecollide(basket,ball_group,True):
        score += 1
        balls_caught += 1
        if balls_caught % 10 == 0:
            ball_speed += 1

    if count > 200:
        ball = Ball(random.randint(50,width-50),50)
        ball_group.add(ball)
        count = 0

    screen.blit(background_img, (0,0))
    scoreText = font.render(f"Score:{score}",True,"black")
    screen.blit(scoreText,(10,10))
    basket_group.draw(screen)
    ball_group.draw(screen)
    ball_group.update()
    basket_group.update()
    pygame.display.update()