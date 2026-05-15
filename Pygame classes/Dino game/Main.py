import pygame
pygame.init()
from Player import Dino
import settings as s
from Authentication import *
from Obstacles import *
from database import *
pygame.mixer.music.load(r"Pygame classes/Dino game/dino music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

score_font = pygame.font.Font(None,30)
bg = pygame.image.load(r"/Users/omjoshi/Library/CloudStorage/OneDrive-Personal/Coding/Python coding class/Pygame classes/Class 1/bg (1).png")
ground_img = pygame.image.load(r"Pygame classes/Dino game/ground.png")
s.dino = Dino()
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
player_group.add(s.dino)
screen  = pygame.display.set_mode((s.w,s.h))
pygame.time.set_timer(s.spawn_obstacle,1500)

runninStatus = True
while runninStatus:
    s.clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninStatus = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                s.dino.dino_state = "run"
                s.game_on_pause = False
            if event.key == pygame.K_SPACE:
                s.dino.start_jump()
                s.game_on_pause = False
            # if event.key == pygame.K_d:
            #     dino.dino_state = "dead"
            #     game_on_pause = True
        if event.type == s.spawn_obstacle and s.game_on_pause == False:
            obstacle_group.add(Obstacles())
            
    if s.current_screen == s.LOGINSCREEN:
        authenticate()
        print(s.current_screen,"*****")

    # if current_screen == "loged_in":
    #     # continue
    # Collision -->
    if pygame.sprite.spritecollide(s.dino,obstacle_group,False,pygame.sprite.collide_mask):
        s.game_on_pause = True
        s.dino.dino_state = "dead"
        save_score(s.current_user)

    # Scroll Logic -->
    if s.game_on_pause == False:
        if s.dino.dino_on_ground == True:
            s.groundx -= s.groundSpeed
            if s.groundx <= -102:
                s.groundx = 0
        else:
            s.groundx -= s.groundSpeed+0.7
            if s.groundx <= -102:
                s.groundx = 0
    
    screen.blit(bg,(0,0))
    screen.blit(ground_img,(s.groundx,s.h-150))
    player_group.draw(screen)
    player_group.update()
    obstacle_group.draw(screen)
    obstacle_group.update()
    score_text = score_font.render(f"Score : {s.score}",False,"BLACK")
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()