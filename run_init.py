# -*- coding: utf-8 -*-
import sys
import pygame
from setting import Settings
from ship import Ship

def run_game():
    pygame.init()
    #初始化设置
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('外星人')
    #初始化飞船
    ship=Ship(screen)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次循环都绘制屏幕
        screen.fill(ai_setting.bg_color)
        #绘制飞船
        ship.blitme()
        #然最近绘制的屏幕可见
        pygame.display.flip()

run_game()
