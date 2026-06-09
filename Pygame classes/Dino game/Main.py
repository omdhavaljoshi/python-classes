import pygame
pygame.init()
import Player as p
import settings as s
import Authentication as Auth
import Obstacles as o
import database as d
import render_screen as r
import os
# pygame.mixer.music.load(r"Pygame classes/Dino game/dino music.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.5)

DIR = os.path.dirname(__file__)
score_font = pygame.font.Font(None,30)
bg = pygame.image.load(os.path.join(DIR,r"image assets/bg (1).png"))
ground_img = pygame.image.load(os.path.join(DIR,r"image assets/ground.png"))
s.dino = p.Dino()
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
player_group.add(s.dino)
s.screen  = pygame.display.set_mode((s.w,s.h))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
        if event.type == s.spawn_obstacle and s.game_on_pause == False:
            obstacle_group.add(o.Obstacles())
            
    if s.current_screen == s.AUTHSCREEN:
        # authenticate()
        r.draw_button("Login",s.login_button)
        r.draw_button("Sign Up", s.signup_button)
        s.screen.fill("Green")
        print(s.current_screen,"*****")

    # if current_screen == "loged_in":
    #     # continue
    # Collision -->
    if pygame.sprite.spritecollide(s.dino,obstacle_group,False,pygame.sprite.collide_mask):
        s.game_on_pause = True
        s.dino.dino_state = "dead"
        d.save_score(s.current_user)

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
    
    s.screen.blit(bg,(0,0))
    s.screen.blit(ground_img,(s.groundx,s.h-150))
    player_group.draw(s.screen)
    player_group.update()
    obstacle_group.draw(s.screen)
    obstacle_group.update()
    score_text = score_font.render(f"Score : {s.score}",False,"BLACK")
    s.screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()