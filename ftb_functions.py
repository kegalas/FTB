import pygame
import sys
import os
import player as Player

def mouse_check_event(playerA):      #检测鼠标按下
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #判断有无关闭
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #点击左键
                playerA.moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:       #放开左键
                playerA.moving = False
