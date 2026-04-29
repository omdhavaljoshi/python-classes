import pygame
from Player import Dino
from settings import *
from Authentication import *
from Obstacles import *
from database import *
pygame.init()

score_font = pygame.font.Font(None,30)
bg = pygame.image.load(r"Pygame classes/Class 1/bg (1).png")
ground_img = pygame.image.load(r"Pygame classes/Dino game/ground.png")
dino = Dino()
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
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
                game_on_pause = False
            if event.key == pygame.K_SPACE:
                dino.start_jump()
                game_on_pause = False
            # if event.key == pygame.K_d:
            #     dino.dino_state = "dead"
            #     game_on_pause = True
        if event.type == spawn_obstacle and game_on_pause == False:
            obstacle_group.add(Obstacles())
            
    if current_screen == LOGINSCREEN:
        authenticate()
        print("test")

    # if current_screen == "loged_in":
    #     # continue
    # Collision -->
    if pygame.sprite.spritecollide(dino,obstacle_group,False,pygame.sprite.collide_mask):
        game_on_pause = True
        dino.dino_state = "dead"
        save_score(current_user)

    # Scroll Logic -->
    if game_on_pause == False:
        if dino.dino_on_ground == True:
            groundx -= groundSpeed
            if groundx <= -102:
                groundx = 0
        else:
            groundx -= groundSpeed+0.7
            if groundx <= -102:
                groundx = 0
    
    screen.blit(bg,(0,0))
    screen.blit(ground_img,(groundx,h-150))
    player_group.draw(screen)
    player_group.update()
    obstacle_group.draw(screen)
    obstacle_group.update()
    score_text = score_font.render(f"Score : {score}",False,"BLACK")
    screen.blit(score_text,(10,10))

    pygame.display.update(dino)

pygame.quit()