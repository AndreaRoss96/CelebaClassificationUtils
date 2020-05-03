import sys
import pygame
from background import Background
from singleton import ImageGetterSingleton
from setting import Settings

def check_events(settings, screen):
    """respond to keypress or mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            key_down_events(event,settings, screen)

def key_down_events(event, settings, screen):
    imggetter = ImageGetterSingleton()
    if event.key == pygame.K_RIGHT:
        print("You chose RIGHT")
        text = imggetter.set_params(2)
    elif event.key == pygame.K_LEFT:
        print("You chose LEFT")
        text = imggetter.set_params(0)
    elif event.key == pygame.K_SPACE:
        print("you skipped this image")
        text = imggetter.pop()
    elif event.key == pygame.K_DOWN:
        print("You chose CENTER")
        text = imggetter.set_params(1)
    elif event.key == pygame.K_q:
        quit()
    else:
        return
    update_screen(settings, screen, text)

def quit():
    imggetter = ImageGetterSingleton()
    imggetter.quit()
    sys.exit()

def update_screen(settings, screen, text = ""):
    imggetter = ImageGetterSingleton()
    settings = Settings()
    imggetter.quit()
    if imggetter.background_changed:
        BackGround = Background(imggetter.current_img, [0,0], screen)
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        imggetter.background_changed = False
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, (0,0,0),(255,255,255))
    textRect = text.get_rect()
    textRect.center = (settings.screen_width/2,settings.screen_height/2)

    pygame.display.flip()
    pygame.display.update()  
