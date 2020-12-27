import pygame
import sys
import os
import ftb_functions as fft
from pygame.sprite import Sprite

class Player():
    """储存球员信息的类"""
    def __init__(self,screen):
        """储存一些基本信息"""
        self.screen = screen

        self.localtion = os.path.dirname(__file__) + '/images/player-s.png'      #球员图片位置

        self.image = pygame.image.load(self.localtion)
        self.rect = self.image.get_rect()       #获取球员矩形
        self.screen_rect = screen.get_rect()


        #将球员开始时放在屏幕最下方正中间
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.top
        #使球员的位置可以储存小数
        self.img_centerx = float(self.rect.centerx)
        self.img_centery = float(self.rect.centery)
        self.img_x = float(self.rect.x)
        self.img_y = float(self.rect.y)
        self.moving = False

    def mov(self):
        """让球员随着鼠标移动"""
        self.position = pygame.mouse.get_pos()
        if(self.position[0]>=self.img_x and self.position[0]<=self.img_x+self.rect.w\
            and self.position[1]>=self.img_y and self.position[1]<=self.img_y+self.rect.h
            ):
            self.img_centerx = self.position[0]
            self.img_centery = self.position[1]
            self.rect.centerx = self.img_centerx
            self.rect.centery = self.img_centery
            self.img_x = self.rect.x
            self.img_y = self.rect.y
        
    def blitme(self):
        """绘制球员"""
        self.screen.blit(self.image,self.rect)







        


        

