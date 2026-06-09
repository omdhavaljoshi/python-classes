import pygame
# pygame.init()
import os

DIR = os.path.dirname(__file__)
# print(DIR)
background_path = os.path.join(DIR, r"Dino game/image assets/bg (1).png")
print(background_path)
ground_img_path = os.path.join(DIR,r"Pygame classes/Dino game/ground.png")
h,w = 800,800
clock = pygame.time.Clock()
groundx = 0
groundSpeed = 4
pygame.display.set_caption("Dino game")
dinoY = h-210
dinoX = 100
ground = h-150
obstacle_list = [os.path.join(DIR,r"image assets/cactus.png"), os.path.join(DIR,r"image assets/spikes.png")]
obstacle_x = w-10
obstacle_y = ground-50
game_on_pause = True
spawn_obstacle = pygame.USEREVENT + 1 
score = 0
AUTHSCREEN = "authenticate"
MENUSCREEN = 'menu'
GAMESCREEN = 'game'
GAMEOVERSCREEN = 'game over'
current_screen = AUTHSCREEN
current_user = ""
dino = None
screen = None
start_button = pygame.Rect(300,300,200,60)
quit_button = pygame.Rect(300,380,200,60)
login_button = pygame.Rect(300,460,200,60)
signup_button = pygame.Rect(250,540,200,60)
font = pygame.font.Font(None,40)
button_colour = "orange"