import pygame

background_path = r"Pygame classes/Class 1/bg (1).png"
ground_img_path = r"Pygame classes/Dino game/ground.png"
h,w = 800,800
clock = pygame.time.Clock()
groundx = 0
groundSpeed = 4
pygame.display.set_caption("Dino game")
dinoY = h-210
dinoX = 100
ground = h-150
obstacle_list = [r"Pygame classes/Dino game/cactus.png", r"Pygame classes/Dino game/spikes.png"]
obstacle_x = w-10
obstacle_y = ground-50
game_on_pause = True
spawn_obstacle = pygame.USEREVENT + 1
score = 0
LOGINSCREEN = "login screen"
current_screen = LOGINSCREEN
current_user = ""
dino = None