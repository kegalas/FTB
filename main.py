import pygame
import sys
import os
import player as Player
import ftb_functions as ftbf
import button as Button 
import time

pygame.init()
screen = pygame.display.set_mode((600,800))         #窗口大小
pygame.display.set_caption("足球战术板")        #设置标题
location = os.path.dirname(os.path.abspath(__file__)) + \
    os.sep+'images'+os.sep+'soccer-field-s.jpg'    #背景图片位置

#print('the location: '+location)
#print('2:'+os.path.dirname(os.path.abspath(__file__)))


backgroundimg = pygame.image.load(location)           #加载背景图片


screen.fill((230,230,230))        #背景颜色
pygame.display.flip()               #绘制屏幕

plyrpos = [(200,230),(330,230),(80,380),(200,400),(330,400),\
    (450,380),(80,580),(200,600),(330,600),(450,580),(265,780)]

plyrpos2 = [(265,180),(155,180),(375,180),(80,280),(450,280),\
    (265,365),(155,365),(200,540),(330,540),(375,365),(265,20)]

allplyr = Player.initPlyrPosition(plyrpos,screen)
allplyr2 = Player.initPlyr2Position(plyrpos2,screen)


buttonList = []

buttonList.append(Button.Button_save(screen))
buttonList.append(Button.Button_load(screen))

class Checkclick():
    def __init__(self):
        self.ifc = False

ifclick = Checkclick()

while True:
    ftbf.mouse_check_event(ifclick)
    if ifclick.ifc:
        buttonList[0].save(allplyr,allplyr2)
        buttonList[1].load(allplyr,allplyr2)
        for i in range(0,11):
            allplyr[i].mov(allplyr,allplyr2,i) 
            allplyr2[i].mov(allplyr,allplyr2,i) 
            
    
    #ftbf.mouse_check_event(player1)
    
    #if player1.moving == True:
    #    player1.mov()                   #移动球员
    
    screen.fill((230,230,230))        #背景颜色
    screen.blit(backgroundimg,(0,0))       #刷新背景

    for i in range(0,11):
        allplyr[i].blitme()
        allplyr2[i].blitme()
    
    buttonList[0].blitme()
    buttonList[1].blitme()

    #player1.blitme()                #绘制球员
    pygame.display.update()               #刷新屏幕

    time.sleep(0.004)            #保持250hz的刷新

