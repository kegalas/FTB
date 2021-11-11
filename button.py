import pygame
import sys
import os
import player as Player
import ftb_functions as ftbf
import arrow as Arrow
import json
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import time


save_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'data' + os.sep + 'save'

#Classes

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
            file = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__))+ os.sep+'data'+ os.sep+'save')
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
        self.bTacticsDir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'data'+os.sep+'blueTeam'+os.sep
        self.yTacticsDir = os.path.dirname(os.path.abspath(__file__)) + os.sep+'data'+os.sep+'yellowTeam'+os.sep
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

class Button_draw_arrow(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'arrow.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 190
    def draw(self,arrowArr,allplyr,allplyr2,buttonList):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=190 and self.position[1]<=240):
            buttonList[3].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'arrow_on.png'
            buttonList[3].image = pygame.image.load(buttonList[3].location)
            buttonList[3].blitme()            
            pygame.display.update() 
            while True:
                class Checkclick():
                    def __init__(self):
                        self.ifc = False
                ifclick = Checkclick()
                ftbf.mouse_check_event(ifclick)
                self.position2 = pygame.mouse.get_pos()
                if ifclick.ifc:
                    if (self.position2[0]>=540 and self.position2[0]<=590 and self.position2[1]>=190 and self.position2[1]<=240):
                        buttonList[3].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'arrow.png'
                        buttonList[3].image = pygame.image.load(buttonList[3].location)
                        buttonList[3].blitme()
                        pygame.display.update() 
                        break
                    elif(self.position2[0]<530 and self.position2[1]<800):
                        while(ifclick.ifc):
                            ftbf.mouse_check_event(ifclick)
                            self.position2 = pygame.mouse.get_pos()
                            if(self.position2[0]>=530):
                                break
                            arrowArr[self.position2[0]][self.position2[1]] = 1
                            Arrow.printArrow(self.screen,arrowArr)
                            pygame.display.update() 
                        
                
                backgroundimg = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'soccer-field-s.jpg')
                self.screen.fill((230,230,230))        #背景颜色
                self.screen.blit(backgroundimg,(0,0))       #刷新背景

                for i in range(0,11):
                    allplyr[i].blitme()
                    allplyr2[i].blitme()
                for i in range(0,7):#0保存，1读取，2战术，3箭头，4擦除，5录制，6播放
                    buttonList[i].blitme()
                Arrow.printArrow(self.screen,arrowArr)
                

                pygame.display.update()               #刷新屏幕

                time.sleep(0.004)            #保持250hz的刷新


                

    


class Button_erase(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'erase.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 250
    def erase(self,arrowArr,allplyr,allplyr2,buttonList):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=250 and self.position[1]<=300):
            buttonList[4].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'erase_on.png'
            buttonList[4].image = pygame.image.load(buttonList[4].location)
            buttonList[4].blitme()            
            pygame.display.update() 
            while True:
                class Checkclick():
                    def __init__(self):
                        self.ifc = False
                ifclick = Checkclick()
                ftbf.mouse_check_event(ifclick)
                self.position2 = pygame.mouse.get_pos()
                if ifclick.ifc:
                    if (self.position2[0]>=540 and self.position2[0]<=590 and self.position2[1]>=250 and self.position2[1]<=300):
                        buttonList[4].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'erase.png'
                        buttonList[4].image = pygame.image.load(buttonList[4].location)
                        buttonList[4].blitme()
                        pygame.display.update() 
                        break
                    elif(self.position2[0]<530 and self.position2[1]<800):
                        while(ifclick.ifc):
                            ftbf.mouse_check_event(ifclick)
                            self.position2 = pygame.mouse.get_pos()
                            if(self.position2[0]>=530):
                                break
                            Arrow.eraseArrow(self.screen,arrowArr,self.position2[0],self.position2[1])
                            arrowArr[self.position2[0]][self.position2[1]] = 0
                            self.screen.blit(backgroundimg,(0,0))
                            for i in range(0,11):
                                allplyr[i].blitme()
                                allplyr2[i].blitme()
                            Arrow.printArrow(self.screen,arrowArr)
                              
                            pygame.display.update() 
                        
                
                backgroundimg = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'soccer-field-s.jpg')
                self.screen.fill((230,230,230))        #背景颜色
                self.screen.blit(backgroundimg,(0,0))       #刷新背景

                for i in range(0,11):
                    allplyr[i].blitme()
                    allplyr2[i].blitme()
                for i in range(0,7):#0保存，1读取，2战术，3箭头，4擦除，5录制，6播放
                    buttonList[i].blitme()
                Arrow.printArrow(self.screen,arrowArr)
                

                pygame.display.update()               #刷新屏幕

                time.sleep(0.004)            #保持250hz的刷新


class Button_record(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'record.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 310
    def record(self,allplyr,allplyr2,buttonList):
        self.position = pygame.mouse.get_pos()
        
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=310 and self.position[1]<=360):
            buttonList[5].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'record_on.png'
            buttonList[5].image = pygame.image.load(buttonList[5].location)
            buttonList[5].blitme()            
            pygame.display.update() 
            demoList = []
            file = os.path.dirname(os.path.abspath(__file__)) + os.sep+'data'+os.sep+'demo'+os.sep
            localtime = time.localtime(time.time())
            file += str(localtime.tm_year)+'_'+str(localtime.tm_mon)+'_'+str(localtime.tm_mday)+'_'+str(localtime.tm_hour)+'_'+str(localtime.tm_min)+'_'+str(localtime.tm_sec)+ ".json"

            count = 0
            class Checkclick():
                    def __init__(self):
                        self.ifc = False
            ifclick = Checkclick()
            while True:
                
                ftbf.mouse_check_event(ifclick)
                self.position2 = pygame.mouse.get_pos()
                if ifclick.ifc:
                    if (self.position2[0]>=540 and self.position2[0]<=590 and self.position2[1]>=310 and self.position2[1]<=360):
                        buttonList[5].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'record.png'
                        buttonList[5].image = pygame.image.load(buttonList[5].location)
                        buttonList[5].blitme()
                        pygame.display.update() 
                        with open(file,'w') as f_obj:
                            json.dump(demoList, f_obj)
                        break
                    else:
                        for i in range(0,11):
                            allplyr[i]. mov(allplyr,allplyr2,i) 
                            allplyr2[i].mov(allplyr,allplyr2,i)
                
                backgroundimg = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'soccer-field-s.jpg')
                self.screen.fill((230,230,230))        #背景颜色
                self.screen.blit(backgroundimg,(0,0))       #刷新背景

                for i in range(0,11):
                    allplyr[i].blitme()
                    allplyr2[i].blitme()
                for i in range(0,7):#0保存，1读取，2战术，3箭头，4擦除，5录制，6播放
                    buttonList[i].blitme()
                pygame.display.update()               #刷新屏幕

                if(count==0):
                    allPos = []
                    allPos2 = []
                    for i in range(0,11):
                        onePos = []
                        onePos.append(allplyr[i].rect.centerx)
                        onePos.append(allplyr[i].rect.centery)
                        allPos.append(onePos)
                    for i in range(0,11):
                        onePos = []
                        onePos.append(allplyr2[i].rect.centerx)
                        onePos.append(allplyr2[i].rect.centery)
                        allPos2.append(onePos)
                    tmpList = [allPos,allPos2]
                    demoList.append(tmpList)
                count+=1
                count%=5                
                time.sleep(0.004)            #保持250hz的刷新   


class Button_display(Button_save):
    def __init__(self,screen):
        self.screen = screen
        self.location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'display.png'      #保存按钮图片位置
        self.image = pygame.image.load(self.location)
        self.x = 540
        self.y = 370
    def display(self, plyrList, plyrList2,buttonList):
        self.position = pygame.mouse.get_pos()
        if (self.position[0]>=540 and self.position[0]<=590 and self.position[1]>=370 and self.position[1]<=420):
            buttonList[6].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'display_on.png'
            buttonList[6].image = pygame.image.load(buttonList[6].location)
            buttonList[6].blitme()            
            pygame.display.update() 
            
            
            global demoList
            demoList = []

            #调用windows的打开文件窗口
            window = tk.Tk()
            file = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__))+ os.sep+'data'+ os.sep+'demo')
            if not file: #防止点开窗口而又不保存
                window.destroy()
                return 0
            with open(file,'r') as f_obj:
                demoList = json.load(f_obj)
            window.destroy()
            for all in demoList:
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
                
                backgroundimg = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'soccer-field-s.jpg')    
                self.screen.fill((230,230,230))        #背景颜色
                self.screen.blit(backgroundimg,(0,0))       #刷新背景

                for i in range(0,11):
                    plyrList[i].blitme()
                    plyrList2[i].blitme()
                for i in range(0,7):#0保存，1读取，2战术，3箭头，4擦除，5录制，6播放
                    buttonList[i].blitme()
                pygame.display.update()
                time.sleep(0.02)
            
            buttonList[6].location = os.path.dirname(os.path.abspath(__file__)) + os.sep+'images'+os.sep+'display.png'
            buttonList[6].image = pygame.image.load(buttonList[6].location)
            buttonList[6].blitme()            
            pygame.display.update() 
            
            return 1



#function

def createButton(screen):
    buttonList = []
    buttonList.append(Button_save(screen))
    buttonList.append(Button_load(screen))
    buttonList.append(Button_tactics(screen))
    buttonList.append(Button_draw_arrow(screen))
    buttonList.append(Button_erase(screen))
    buttonList.append(Button_record(screen))
    buttonList.append(Button_display(screen))
    return buttonList







