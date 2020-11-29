import pygame
import sys
import os

def mouse_check_event(event):      #检测鼠标按下
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:       #点击左键
            return True
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:       #放开左键
            return False
