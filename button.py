import pygame
import sys
import os
import player as Player
import ftb_functions as ftbf
import json

save_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav'+os.sep+'save.json' 

class Button_save():
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'save.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 10
    def blitme(self):
        self.screen.blit(self.image,(self.x,self.y))
    def save(self, plyrList, plyrList2):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=10 and self.position[1]<=60):
            allPos = []
            allPos2 = []
            for i in range(0,11):
                onePos = []
                onePos.append(plyrList[i].rect.centerx)
                onePos.append(plyrList[i].rect.centery)
                allPos.append(onePos)
            for i in range(0,11):
                onePos = []
                onePos.append(plyrList2[i].rect.centerx)
                onePos.append(plyrList2[i].rect.centery)
                allPos2.append(onePos)
            with open(save_dir,'w') as f_obj:
                json.dump([allPos,allPos2], f_obj)
            return 1



class Button_load(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'load.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 70
    def load(self, plyrList, plyrList2):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=70 and self.position[1]<=120):
            global all
            all = []
            with open(save_dir,'r') as f_obj:
                all = json.load(f_obj)
            posList = all[0]
            posList2 = all[1]
            for i in range(0,11):
                plyrList[i].rect.centerx = posList[i][0]
                plyrList[i].rect.centery = posList[i][1]
                plyrList[i].img_centerx = float(posList[i][0])
                plyrList[i].img_centery = float(posList[i][1])
                plyrList[i].img_x = float(plyrList[i].rect.x)
                plyrList[i].img_y = float(plyrList[i].rect.y)
            for i in range(0,11):
                plyrList2[i].rect.centerx = posList2[i][0]
                plyrList2[i].rect.centery = posList2[i][1]
                plyrList2[i].img_centerx = float(posList2[i][0])
                plyrList2[i].img_centery = float(posList2[i][1])
                plyrList2[i].img_x = float(plyrList2[i].rect.x)
                plyrList2[i].img_y = float(plyrList2[i].rect.y)
            return 1






