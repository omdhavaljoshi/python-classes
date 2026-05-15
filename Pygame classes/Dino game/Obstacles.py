import pygame,random
import settings as s

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(s.obstacle_list))
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect(center = (s.obstacle_x,s.obstacle_y))
        self.speed = 4

    def move_left(self,dino):
        print(dino.dino_on_ground)
        if dino.dino_on_ground == True:
            self.rect.x -= self.speed
            if self.rect.right< dino.rect.left:
                self.kill()
                s.score +=1
        else:
            self.rect.x -= self.speed+0.7
            if self.rect.right< dino.rect.left:
                self.kill()
                s.score +=1

    def update(self):
        if s.game_on_pause == False:
            self.move_left(s.dino)