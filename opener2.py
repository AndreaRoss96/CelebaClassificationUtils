import matplotlib.pyplot as plt
import matplotlib.image as img
import game_funct as gf
from singleton import ImageGetterSingleton
import os
import time
import pygame
from setting import Settings
from background import Background

mypath = "Hey\\img_align_celeba\\img_align_celeba"
def run_game():

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
            (settings.screen_width,settings.screen_height))

    while True:
        gf.check_events(settings, screen)
        gf.update_screen(screen, screen)


#BackGround = Background('background_image.png', [0,0])
#screen.fill([255, 255, 255])
#screen.blit(BackGround.image, BackGround.rect)


run_game()
