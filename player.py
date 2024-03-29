import pygame
import sys
import os
import ftb_functions as ftbf
import button as Button 
from pygame.sprite import Sprite

#Classes

class Player():
    """储存球员信息的类"""
    def __init__(self,screen):
        """储存一些基本信息"""
        self.screen = screen

        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'player-s.png'      #球员图片位置
        #print(self.location)
        self.image = pygame.image.load(self.location)
        self.rect = self.image.get_rect()       #获取球员矩形
        self.screen_rect = screen.get_rect()

        self.group = 1 #设置球员所处队伍

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

    def mov(self,allplyr,allplyr2,number):
        """让球员随着鼠标移动"""
        self.position = pygame.mouse.get_pos()
        self.text_intersect = False
        for i in range(0,11):   #判断是否与1队球员重叠
            if i==number and self.group == 1:
                continue
            else:
                if(self.position[0]>=allplyr[i].img_x and \
                    self.position[0]<=allplyr[i].img_x+allplyr[i].rect.w\
                    and self.position[1]>=allplyr[i].img_y and \
                    self.position[1]<=allplyr[i].img_y+allplyr[i].rect.h):
                    self.text_intersect = True
                    break
        for i in range(0,11):   #判断是否与2队球员重叠
            if i==number and self.group == 2:
                continue
            else:
                if(self.position[0]>=allplyr2[i].img_x and \
                    self.position[0]<=allplyr2[i].img_x+allplyr2[i].rect.w\
                    and self.position[1]>=allplyr2[i].img_y and \
                    self.position[1]<=allplyr2[i].img_y+allplyr2[i].rect.h):
                    self.text_intersect = True
                    break

        if(self.position[0]>=self.img_x and self.position[0]<=self.img_x+self.rect.w\
            and self.position[1]>=self.img_y and self.position[1]<=self.img_y+self.rect.h\
            and self.text_intersect==False):    #移动球员到指针处
            self.img_centerx = self.position[0]
            self.img_centery = self.position[1]
            self.rect.centerx = self.img_centerx
            self.rect.centery = self.img_centery
            self.img_x = self.rect.x
            self.img_y = self.rect.y
        
    def blitme(self):
        """绘制球员"""
        self.screen.blit(self.image,self.rect)

class Player2(Player):            
    """储存对方球员信息的类"""
    def __init__(self,screen):
        """储存一些基本信息"""
        self.screen = screen

        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'player-1-s.png'      #球员图片位置
        #print(self.location)
        self.image = pygame.image.load(self.location)
        self.rect = self.image.get_rect()       #获取球员矩形
        self.screen_rect = screen.get_rect()

        self.group = 2 #设置球员所处队伍

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

#Functions

def initPlyrPosition(posList,screen):
    plyrList = []
    for i in range(0,11):
        plyrList.append(Player(screen))
    for i in range(0,11):
        plyrList[i].rect.centerx = posList[i][0]
        plyrList[i].rect.centery = posList[i][1]
        plyrList[i].img_centerx = float(posList[i][0])
        plyrList[i].img_centery = float(posList[i][1])
        plyrList[i].img_x = float(plyrList[i].rect.x)
        plyrList[i].img_y = float(plyrList[i].rect.y)
    return plyrList

def initPlyr2Position(posList,screen):
    plyrList = []
    for i in range(0,11):
        plyrList.append(Player2(screen))
    for i in range(0,11):
        plyrList[i].rect.centerx = posList[i][0]
        plyrList[i].rect.centery = posList[i][1]
        plyrList[i].img_centerx = float(posList[i][0])
        plyrList[i].img_centery = float(posList[i][1])
        plyrList[i].img_x = float(plyrList[i].rect.x)
        plyrList[i].img_y = float(plyrList[i].rect.y)
    return plyrList
    