import pygame
import os

w,h = 700,700
screen = None
running = True
fps = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None,40)
score = 0

MENU = "menu"
GAME = "game"
GAME_OVER = "game over"
current_screen = MENU

# Rectangle for button -->
gameButton = pygame.Rect(250,250,200,60)
quitButton = pygame.Rect(250,320,200,60)
game_menuButton = pygame.Rect(250,250,200,60)
game_overButton = pygame.Rect(250,320,200,60)

button_colour = "BLUE"