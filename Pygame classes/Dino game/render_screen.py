import pygame
import settings as s
def draw_button(text,rectButton):
    pygame.draw.rect(s.screen,s.button_colour,rectButton)
    label = s.font.render(text,True,"White")
    coordinates = label.get_rect(center = rectButton.center)
    s.screen.blit(label,coordinates)

def set_screen(mouspos):
    pass