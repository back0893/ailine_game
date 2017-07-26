import pygame


class Ship:
    """飞船的控制类"""
    def __init__(self,screen):
        """飞船的初始化及其位置"""
        self.screen=screen

        #从本地加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def blitme(self):
        """在制定位置描绘飞船"""
        self.screen.blit(self.image,self.rect)