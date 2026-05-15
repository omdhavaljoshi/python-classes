import pygame
import settings as s

def setScreenLogic(mousePos):
    if s.gameButton.collidepoint(mousePos):
        print("test")
        s.current_screen = s.GAME
        print(s.current_screen)
    if s.quitButton.collidepoint(mousePos):
        s.running = False
    if s.game_menuButton.collidepoint(mousePos):
        s.current_screen = s.MENU
    if s.game_overButton.collidepoint(mousePos):
        s.current_screen = s.GAME_OVER

def draw_button(text,rectButton):
    pygame.draw.rect(s.screen,s.button_colour,rectButton)
    label = s.font.render(text,True,"White")
    coordinates = label.get_rect(center = rectButton.center)
    s.screen.blit(label,coordinates)

def menuRender():
    #1. text
        title = s.font.render("DINO GAME",False,"Red")
        s.screen.blit(title,(250,150))
        #2. draw button
        draw_button("Start",s.gameButton)
        draw_button("Quit",s.quitButton)

def gameRender():
    score = s.font.render(f"Score: {s.score}",False,"Black")
    s.screen.blit(score,(10,10))
    draw_button("Game Menu",s.game_menuButton)
    draw_button("Game Over",s.game_overButton)

def game_overRender():
    game_over_text = s.font.render("GAME OVER", False, "Red")
    s.screen.blit(game_over_text, (250, 150))
    draw_button("Quit", s.quitButton)
    draw_button("Game Menu", s.game_menuButton)

def render_screen():
    if s.current_screen == s.MENU:
        menuRender()
    if s.current_screen == s.GAME:
        gameRender()
    if s.current_screen == s.GAME_OVER:
        game_overRender()