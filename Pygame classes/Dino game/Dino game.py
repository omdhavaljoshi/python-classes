import pygame
pygame.init()
pygame.mixer.music.load(r"Pygame classes/Dino game/dino music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

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
ground = h-150

# Sprites -->
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_image = []
        self.idle_image = []
        self.jump_image = []
        self.dead_image = []
        self.load_images()
        self.index = 0
        self.image = self.idle_image[0]
        self.rect = self.image.get_rect(center = (dinoX,dinoY))
        self.counter = 0
        self.dino_state = "idle"
        self.dino_on_ground = True
        self.dino_velocity_y = 0
        self.gravity = 1
        self.jump_power = -20
    
    def load_images(self):
        for i in range(1,9):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Run "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.run_image.append(self.image)

        for i in range(1,11):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Idle "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.idle_image.append(self.image)

        for i in range(1,13):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Jump "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.jump_image.append(self.image)
        
        for i in range(1,9):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Dead "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.dead_image.append(self.image)
    
    def track_counter(self):
        self.counter+=1
        if self.counter >= 8:
            self.counter = 0
            self.index += 1

    def run(self):
            self.track_counter()
            if self.index > len(self.run_image)-1:
                self.index = 0
            self.image = self.run_image[self.index]

    def idle_(self):
        self.track_counter()
        if self.index > len(self.idle_image)-1:
            self.index = 0
        self.image = self.idle_image[self.index]
    
    def gravity_handle(self):
        self.rect.y += self.dino_velocity_y 
        self.dino_velocity_y += self.gravity 
        if self.rect.y >= 510:
            self.dino_state = "run"
            self.dino_velocity_y = 0
            self.rect.y = 510
            self.dino_on_ground = True

    def start_jump(self):
        if self.dino_on_ground == True:
            self.dino_on_ground = False
            self.dino_velocity_y = self.jump_power
            self.dino_state = "jump"

    def jump(self):
        self.track_counter()
        if self.index >= len(self.jump_image):
            self.index = 0
        self.image = self.jump_image[self.index]
        self.gravity_handle()
    
    def death(self):
        self.track_counter()
        if self.index > len(self.dead_image)-1:
            self.index = 0
        if self.index >= len(self.dead_image)-1:
            self.dino_state = "idle"
        self.image = self.dead_image[self.index]
    
    
    def update(self):
        if self.dino_state == "idle":
            self.idle_()
        elif self.dino_state == "run":
            self.run()
        elif self.dino_state == "jump":
            self.jump()
        elif self.dino_state == "dead":
            self.death()
    
    
dino = Dino()
player_group = pygame.sprite.Group()
player_group.add(dino)

runninStatus = True
while runninStatus:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninStatus = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                dino.dino_state = "run"
            if event.key == pygame.K_SPACE:
                dino.start_jump()
            if event.key == pygame.K_d:
                dino.dino_state = "dead"
    # Scroll Logic -->
    if dino.dino_state != "idle":
        groundx -= groundSpeed
        if groundx <= -102:
            groundx = 0
    
    screen.blit(bg,(0,0))
    screen.blit(ground_img,(groundx,h-150))
    player_group.draw(screen)
    player_group.update()

    pygame.display.update()

pygame.quit()