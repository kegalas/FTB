import pygame
import player as Player
import ftb_functions as ftbf
import button as Button 

def printArrow(screen, arrowArr):
    for i in range(0,530):
        for j in range(0,800):
            if(arrowArr[i][j]==1):
                pygame.draw.rect(screen,[255,0,0],[i,j,4,4],3)
    
def eraseArrow(screen, arrowArr, x, y):
    for i in range(-8,9):
        for j in range(-8,9):
            arrowArr[x+i][y+j]=0
    
        


