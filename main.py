import pygame
import sys
import os
import player as Player
import ftb_functions as ftb

pygame.init()
screen = pygame.display.set_mode((530,800))         #窗口大小
pygame.display.set_caption("足球战术板")        #设置标题

localtion = os.path.dirname(__file__) + '/images/soccer-field-s.jpg'    #背景图片位置

backgroundimg = pygame.image.load(localtion)           #加载背景图片


screen.fill((230,230,230))        #背景颜色
pygame.display.flip()               #绘制屏幕

allplyr = []
for i in range(0,11):
    allplyr.append(Player.Player(screen))

plyrpos = ((200,230),(330,230),(80,380),(200,400),(330,400),\
    (450,380),(80,580),(200,600),(330,600),(450,580),(265,780))

for i in range(0,11):
    allplyr[i].rect.centerx = plyrpos[i][0]
    allplyr[i].rect.centery = plyrpos[i][1]
    allplyr[i].img_centerx = float(plyrpos[i][0])
    allplyr[i].img_centery = float(plyrpos[i][1])
    allplyr[i].img_x = float(allplyr[i].rect.x)
    allplyr[i].img_y = float(allplyr[i].rect.y)

#

#player1 = Player.Player(screen)

class Checkclick():
    def __init__(self):
        self.ifc = False

ifclick = Checkclick()

while True:
    ftb.mouse_check_event(ifclick)
    for i in range(0,11):
        if ifclick.ifc == True:
            allplyr[i].mov() 
    
    #ftb.mouse_check_event(player1)
    
    #if player1.moving == True:
    #    player1.mov()                   #移动球员
    
    screen.fill((230,230,230))        #背景颜色
    screen.blit(backgroundimg,(0,0))       #刷新背景

    for i in range(0,11):
        allplyr[i].blitme()

    #player1.blitme()                #绘制球员
    pygame.display.update()               #刷新屏幕


