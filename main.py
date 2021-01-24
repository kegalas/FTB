import pygame
import sys
import os
import player as Player
import ftb_functions as ftb
import time

pygame.init()
screen = pygame.display.set_mode((530,800))         #窗口大小
pygame.display.set_caption("足球战术板")        #设置标题
localtion = os.path.dirname(os.path.abspath(__file__)) + \
    os.sep+'images'+os.sep+'soccer-field-s.jpg'    #背景图片位置

#print('the localtion: '+localtion)
#print('2:'+os.path.dirname(os.path.abspath(__file__)))


backgroundimg = pygame.image.load(localtion)           #加载背景图片


screen.fill((230,230,230))        #背景颜色
pygame.display.flip()               #绘制屏幕

allplyr = []
allplyr2 = []
for i in range(0,11):
    allplyr.append(Player.Player(screen))

for i in range(0,11):
    allplyr2.append(Player.Player2(screen))


plyrpos = ((200,230),(330,230),(80,380),(200,400),(330,400),\
    (450,380),(80,580),(200,600),(330,600),(450,580),(265,780))

plyrpos2 = ((265,180),(155,180),(375,180),(80,280),(450,280),\
    (265,365),(155,365),(200,540),(330,540),(375,365),(265,20))

for i in range(0,11):
    allplyr[i].rect.centerx = plyrpos[i][0]
    allplyr[i].rect.centery = plyrpos[i][1]
    allplyr[i].img_centerx = float(plyrpos[i][0])
    allplyr[i].img_centery = float(plyrpos[i][1])
    allplyr[i].img_x = float(allplyr[i].rect.x)
    allplyr[i].img_y = float(allplyr[i].rect.y)

for i in range(0,11):
    allplyr2[i].rect.centerx = plyrpos2[i][0]
    allplyr2[i].rect.centery = plyrpos2[i][1]
    allplyr2[i].img_centerx = float(plyrpos2[i][0])
    allplyr2[i].img_centery = float(plyrpos2[i][1])
    allplyr2[i].img_x = float(allplyr2[i].rect.x)
    allplyr2[i].img_y = float(allplyr2[i].rect.y)



class Checkclick():
    def __init__(self):
        self.ifc = False

ifclick = Checkclick()

while True:
    ftb.mouse_check_event(ifclick)
    for i in range(0,11):
        if ifclick.ifc:
            allplyr[i].mov(allplyr,allplyr2,i) 
            allplyr2[i].mov(allplyr,allplyr2,i) 
    
    #ftb.mouse_check_event(player1)
    
    #if player1.moving == True:
    #    player1.mov()                   #移动球员
    

    screen.fill((230,230,230))        #背景颜色
    screen.blit(backgroundimg,(0,0))       #刷新背景

    for i in range(0,11):
        allplyr[i].blitme()
        allplyr2[i].blitme()

    #player1.blitme()                #绘制球员
    pygame.display.update()               #刷新屏幕

    time.sleep(0.004)            #保持250hz的刷新

