import pygame
import sys
import os
import player as Player
import ftb_functions as ftbf
import json
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk


save_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav' 

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

            #调用windows的打开文件窗口
            window = tk.Tk()
            file = filedialog.asksaveasfilename(initialdir=save_dir)
            if not file: #防止点开窗口而又不保存
                window.destroy()
                return 0
            file += ".json"
            with open(file,'w') as f_obj:
                json.dump([allPos,allPos2], f_obj)
            window.destroy()
        
            return 1

class Button_load(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'load.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 70
    def load_all(self, plyrList, plyrList2):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=70 and self.position[1]<=120):
            global all
            all = []

            #调用windows的打开文件窗口
            window = tk.Tk()
            file = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__))+ os.sep+'sav')
            if not file: #防止点开窗口而又不保存
                window.destroy()
                return 0
            with open(file,'r') as f_obj:
                all = json.load(f_obj)
            window.destroy()

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

class Button_tactics(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'tactics.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 130
        self.bTacticsDir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav'+os.sep+'blueTeam'+os.sep
        self.yTacticsDir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'sav'+os.sep+'yellowTeam'+os.sep
    def load(self,plyrList,plyrList2):#黄队，蓝队
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=130 and self.position[1]<=180):
            window = tk.Tk()
            window.title("选取预设战术")
            window.geometry("280x70")
            label  = tk.Label(window,text="黄队战术")
            label2 = tk.Label(window,text="蓝队战术")
            label.grid(column=0,row=0)
            label2.grid(column=0,row=1)

            combo  = ttk.Combobox(window)
            combo2 = ttk.Combobox(window)
            combo['values'] = ('442','352','4321','433')
            combo2['values'] = ('352','442','4321','433')
            combo.current(0)
            combo2.current(0)
            combo.grid(column=1,row=0)
            combo2.grid(column=1,row=1)

            def clicked():
                tmpDir = self.yTacticsDir+combo.get()+'.json'
                global tmpPos
                with open(tmpDir,'r') as f_obj:
                    tmpPos = json.load(f_obj)
                for i in range(0,11):
                    plyrList[i].rect.centerx = tmpPos[i][0]
                    plyrList[i].rect.centery = tmpPos[i][1]
                    plyrList[i].img_centerx = float(tmpPos[i][0])
                    plyrList[i].img_centery = float(tmpPos[i][1])
                    plyrList[i].img_x = float(plyrList[i].rect.x)
                    plyrList[i].img_y = float(plyrList[i].rect.y)
                window.destroy()
                 
            def clicked2():
                tmpDir = self.bTacticsDir+combo2.get()+'.json'
                global tmpPos2
                with open(tmpDir,'r') as f_obj:
                    tmpPos2 = json.load(f_obj)
                for i in range(0,11):
                    plyrList2[i].rect.centerx = tmpPos2[i][0]
                    plyrList2[i].rect.centery = tmpPos2[i][1]
                    plyrList2[i].img_centerx = float(tmpPos2[i][0])
                    plyrList2[i].img_centery = float(tmpPos2[i][1])
                    plyrList2[i].img_x = float(plyrList2[i].rect.x)
                    plyrList2[i].img_y = float(plyrList2[i].rect.y)
                window.destroy()
                

            btn = tk.Button(window, text="确定", command=clicked)
            btn2 = tk.Button(window, text="确定", command=clicked2)
            
            btn.grid(column=2,row=0)
            btn2.grid(column=2,row=1)

            window.mainloop()







