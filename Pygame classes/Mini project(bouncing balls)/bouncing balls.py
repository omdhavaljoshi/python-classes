import pygame, random
pygame.init()

width,height = 500,500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
ball_img1 = r"Pygame classes/Mini project(bouncing balls)/bb_.png"
ball_img2 = r"Pygame classes/Mini project(bouncing balls)/gb_.png"
ball_img3 = r"Pygame classes/Mini project(bouncing balls)/rb_.png"
ball_img4 = r"Pygame classes/Mini project(bouncing balls)/yb_.png"
ball_list = [ball_img1, ball_img2, ball_img3, ball_img4]
balls = []

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.ball = random.choice(ball_list)
        self.image = pygame.image.load(self.ball)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(center = pos)
        self.speedX = random.randint(-5,5)
        self.speedY = random.randint(-5,5)
    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if  self.rect.right >= 500 or  self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= 500 or  self.rect.top<= 0:
            self.speedY = -self.speedY

ball_group = pygame.sprite.Group()
for i in range(7):
    position = (random.randint(50,450), random.randint(50,450))
    ball = Ball(position)
    balls.append(ball)

for ball in balls:
    ball_group.add(ball)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            ball_group.add(Ball(mouse_pos))


    screen.fill("light blue")
    ball_group.draw(screen)
    ball_group.update()
    pygame.display.flip()
    clock.tick(60)
