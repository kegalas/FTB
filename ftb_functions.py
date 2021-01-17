import pygame
import sys
import os
import player as Player
#import main as Main

def mouse_check_event(ifclick):      #检测鼠标按下
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #判断有无关闭
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #点击左键
                ifclick.ifc = True
                #position1 = pygame.mouse.get_pos()
                #print(position1[0]," ",position1[1])
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:       #放开左键
                ifclick.ifc = False

