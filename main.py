import pygame
import sys
import os
import player as Player
import ftb_functions as ftbf
import button as Button 
import time
import json

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

yTeamDefaultPos = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav' + \
                    os.sep + 'yellowTeam' + os.sep + '442.json'
bTeamDefaultPos = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav' + \
                    os.sep + 'blueTeam' + os.sep + '352.json'
#默认站位读取

global plyrpos
global plyrpos2
with open(yTeamDefaultPos,'r') as f_obj:
    plyrpos = json.load(f_obj)
with open(bTeamDefaultPos,'r') as f_obj:
    plyrpos2 = json.load(f_obj)

allplyr = Player.initPlyrPosition(plyrpos,screen)
allplyr2 = Player.initPlyr2Position(plyrpos2,screen)


buttonList = []
buttonList.append(Button.Button_save(screen))
buttonList.append(Button.Button_load(screen))
buttonList.append(Button.Button_tactics(screen))

class Checkclick():
    def __init__(self):
        self.ifc = False

ifclick = Checkclick()

##############################
###Main，真正的主循环开始的位置###
##############################


while True:
    ftbf.mouse_check_event(ifclick)
    if ifclick.ifc:
        buttonList[0].save(allplyr,allplyr2)
        buttonList[1].load_all(allplyr,allplyr2)
        buttonList[2].load(allplyr,allplyr2)
        for i in range(0,11):
            allplyr[i].mov(allplyr,allplyr2,i) 
            allplyr2[i].mov(allplyr,allplyr2,i)

    
    
    screen.fill((230,230,230))        #背景颜色
    screen.blit(backgroundimg,(0,0))       #刷新背景

    for i in range(0,11):
        allplyr[i].blitme()
        allplyr2[i].blitme()
    
    buttonList[0].blitme()
    buttonList[1].blitme()
    buttonList[2].blitme()

    pygame.display.update()               #刷新屏幕

    time.sleep(0.004)            #保持250hz的刷新

