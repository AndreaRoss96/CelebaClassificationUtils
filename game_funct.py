import sys
import pygame
from background import Background
from singleton import ImageGetterSingleton

def check_events(settings, screen):
    """respond to keypress or mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_events(event,settings, screen)

def key_down_events(event, settings, screen):
    imggetter = ImageGetterSingleton()
    if event.key == pygame.K_RIGHT:
        imggetter.set_params(2)
    elif event.key == pygame.K_LEFT:
        imggetter.set_params(2)
    elif event.key == pygame.K_SPACE:
        imggetter.pop()
    elif event.key == pygame.K_q:
        quit()

def quit():
    imggetter = ImageGetterSingleton()
    imggetter.quit()
    sys.exit()

def update_screen(settings, screen):
    imggetter = ImageGetterSingleton()
    imggetter.quit()
    if imggetter.background_changed:
        BackGround = Background(imggetter.current_img, [0,0], screen)
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        imggetter.background_changed = False
    pygame.display.flip()
