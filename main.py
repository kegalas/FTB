import pygame
import sys
import os
import player as Player

pygame.init()
screen = pygame.display.set_mode((530,800))         #窗口大小
pygame.display.set_caption("足球战术板")        #设置标题

localtion = os.path.dirname(__file__) + '/images/soccer-field-s.jpg'    #背景图片位置

backgroundimg = pygame.image.load(localtion)           #加载背景图片


screen.fill((230,230,230))        #背景颜色
pygame.display.flip()               #绘制屏幕

player1 = Player.Player(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #判断有无关闭
            sys.exit()
        player1.mov(event)                   #移动球员
    
    screen.fill((230,230,230))        #背景颜色
    screen.blit(backgroundimg,(0,0))       #刷新背景



    player1.blitme()                #绘制球员
    pygame.display.update()               #刷新屏幕


