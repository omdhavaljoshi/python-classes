import pygame,random
from Dino_game import obstacle_list, obstacle_x, obstacle_y, dino, game_on_pause

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(obstacle_list))
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect(center = (obstacle_x,obstacle_y))
        self.speed = 4

    def move_left(self):
        global score
        if dino.dino_on_ground == True:
            self.rect.x -= self.speed
            if self.rect.right< dino.rect.left:
                self.kill()
                score +=1
        else:
            self.rect.x -= self.speed+0.7
            if self.rect.right< dino.rect.left:
                self.kill()
                score +=1

    def update(self):
        if game_on_pause == False:
            self.move_left()