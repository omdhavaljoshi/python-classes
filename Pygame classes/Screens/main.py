import pygame
pygame.init()
import settings as s
import renderScreen as r

s.screen = pygame.display.set_mode((s.w,s.h))

while s.running:
    s.clock.tick(s.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            print(s.current_screen)
            r.setScreenLogic(mousePos)

    s.screen.fill("white") 
    r.render_screen()
    pygame.display.update()