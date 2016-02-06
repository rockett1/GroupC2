import pygame
import tkinter as tk
from tkinter import *
import sys
import os
import copy
import time
from random import randint

class Object:
    def __init__(self,x1,y1,screen,colour):
        self.x1=x1
        self.y1=y1

        self.colour=colour
        self.screen=screen
    def print_obj(self):
        pass
class Triangle(Object):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.x2=x1+dimension
        self.y2=y1
        self.x3=x1+(dimension/2)
        self.y3=y1+dimension
        self.price=price

    def print_obj(self):
        return(pygame.draw.polygon(self.screen,self.colour,((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3))))
class Quadrilater(Object):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.price=price
    def print_obj(self):
        pass
class Square(Quadrilater):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,price,dimension,screen,colour)
        self.heigth=dimension
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
class Rectangle(Quadrilater):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,price,dimension,screen,colour)
        self.heigth=dimension+15
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
class Circle(Object):
    def __init__(self,x1,y1,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.diameter=dimension
    def print_obj(self):
        return(pygame.draw.circle(self.screen,self.colour,(self.x1,self.y1),self.diameter))





class MyPyGame(object):
    def __init__(self):
        self.Glist={}
        pygame.display.init()
        self.green=(0,190,0)
        self.red=(200,0,0)
        self.blue=(63,72,204)
        self.white=(255,255,255)
        self.yellow=(254,216,1)
        self.black=(0,0,0)
        self.display_width=1266
        self.display_height=650
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption('Space Hunter')
        self.background=pygame.image.load('space.jpg')
        self.screen.blit(self.background,(0,0))

        pygame.display.update()

        self._radius = 125
        
    def runIntroWindow(self):

        exitWindow=False
        while not exitWindow:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            startimg=pygame.image.load('start.png')
            startimg1=pygame.image.load('start1.png')
            quitimg=pygame.image.load('quit.png')
            quitimg1=pygame.image.load('quit1.png')
            self.message_display("Welcome to Space Hunter!")
            self.button(400,350,startimg1,startimg,"play")
            self.button(760,350,quitimg1,quitimg,"quit")
        pygame.display.update()
    def update(self):
##        pygame.draw.circle(self.screen, (0,0,0), (250,250), self._radius)
        pygame.display.update()

    def game(self,x,y):
        exitGame=False
        self.screen.blit(self.held_image,(0,0))
        while not exitGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            self.random_object_generator(6)
            ship=pygame.image.load('ship.png')

            self.screen.blit(ship,(x+30,y+35))

            self.Glist=self.occupy_grid(x+30,y+35)

            
            #head=pygame.transform.rotate(ship,270) if it goes to right
            exitGame=True
        pygame.display.update()
        time.sleep(3)
    def create_grid(self):
        nri=0
        nrj=0
        for i in range(30,self.display_width-30,30):
            nri=nri+1
            for j in range(40,self.display_height-30,30):
                self.Glist[(i,j)]=True
                nrj=nrj+1

        return(self.Glist)
    def occupy_grid(self,x,y):
        self.Glist[(x,y)]=False
        return (self.Glist)
    def random_object_generator(self,nr):
        self.objects=[]
        self.obstacles=[]
        self.Glist=self.create_grid()
        rand_obst=randint(3,4)
        while rand_obst!=0:
        
            rand_dimension=randint(15,30)

            i=randint(0,len(self.Glist)-1)

            pos=list(self.Glist)[i]

            rand_x=pos[0]
            rand_y=pos[1]

            r_x=rand_x+30
            r_y=rand_y+30
          

            if self.Glist[list(self.Glist)[i]]==True:
                ob4=Circle(rand_x,rand_y,rand_dimension,self.screen,self.yellow)
                self.obstacles.append(ob4)
                self.Glist=self.occupy_grid(rand_x,rand_y)
                if rand_dimension>15:
                    self.Glist=self.occupy_grid(r_x,r_y)

                ob4.print_obj()
                rand_obst=rand_obst-1
        
        while nr!=0:
            rand_dimension=randint(15,45)
            rand_shape=randint(1,3)
            rand_colour=randint(1,3)
            colours={1:self.red,2:self.blue,3:self.green}
            j=randint(0,len(self.Glist)-1)
            pos=list(self.Glist)[j]
            rand_x=pos[0]
            rand_y=pos[1]
            r_x=rand_x+30
            r_y=rand_y+30
            if self.Glist[list(self.Glist)[j]]==True:
                if rand_shape==1:
                    ob1=Square(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                    self.objects.append(ob1)
                    self.Glist=self.occupy_grid(rand_x,rand_y)
                    if rand_dimension>30:
                        self.Glist=self.occupy_grid(r_x,r_y)

                    ob1.print_obj()
                elif rand_shape==2:
                    ob2=Rectangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                    self.objects.append(ob2)
                    self.Glist=self.occupy_grid(rand_x,rand_y)
                    if rand_dimension>30:
                        self.Glist=self.occupy_grid(r_x,r_y)
                    ob2.print_obj()
                elif rand_shape==3:
                    ob3=Triangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                    self.objects.append(ob3)
                    self.Glist=self.occupy_grid(rand_x,rand_y)
                    if rand_dimension>30:
                        self.Glist=self.occupy_grid(r_x,r_y)
                    ob3.print_obj()
                nr=nr-1
        pygame.display.update()


    def button(self,x,y,img1,img,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+150>=mouse[0]>=x and y+80>=mouse[1]>y:
            self.screen.blit(img1,(x,y))
            if click[0]==1 and action!=None:
                if action=="play":
                    root=tk.Tk()
                    g=Gui(root)
                    root.mainloop()
                elif action=="quit":
                    pygame.quit()
                    quit()
                elif action=="spawn":
                    self.game(x,y)
                
        else:
            self.screen.blit(img,(x,y))

    def text_objects(self,text,font):
        textSurface=font.render(text,True,self.white)
        return textSurface,textSurface.get_rect()
    def message_display(self,text):
        pygame.font.init()
        self.largeText=pygame.font.Font('freesansbold.ttf',40)
        TextSurf,TextRect=self.text_objects(text,self.largeText)
        TextRect.center=((self.display_width/2),(self.display_height/2))
        self.screen.blit(TextSurf,TextRect)
        pygame.display.update()

    def spawn_ship(self):
        
            exitW=False
            while not exitW:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                self.background=pygame.image.load('space.jpg')
                self.held_image=self.background
                self.screen.blit(self.background,(0,0))
                spawn=pygame.image.load('spawn.png')
                spawn1=pygame.image.load('spawn1.png')
                self.button(330,125,spawn1,spawn,"spawn")
                self.button(810,125,spawn1,spawn,"spawn")
                self.button(330,395,spawn1,spawn,"spawn")
                self.button(810,395,spawn1,spawn,"spawn")
                pygame.display.update()


class Gui(object):
    def __init__(self, root):
        self.root = root
        root.title('Space Hunter')
        root.wm_title("Space Hunter")

        self.mpg=MyPyGame()
        
        title_frame=Frame(self.root)
        textbox_frame=Frame(self.root)
        time_frame=Frame(self.root)
        time_frame1=Frame(self.root)
        checkboxframe=Frame(self.root)
        optionframe=Frame(self.root)
        startframe=Frame(self.root)

        checkbox_frame1=Frame(checkboxframe)
        checkbox_frame2=Frame(checkboxframe)
        option_frame1=Frame(optionframe)
        option_frame2=Frame(optionframe)

        
        title_frame.pack(side=TOP)
        textbox_frame.pack(side=TOP)
        time_frame.pack(side=TOP)
        time_frame1.pack(side=TOP)
        checkboxframe.pack(side=TOP)
        optionframe.pack(side=TOP)
        startframe.pack(side=TOP)
        
        checkbox_frame1.pack(side=LEFT)
        checkbox_frame2.pack(side=LEFT)
        option_frame1.pack(side=LEFT)
        option_frame2.pack(side=LEFT)

        
        L1 = Label(title_frame, text="Chose what to search for and how much time is it given ")
        L1.pack(side=TOP)
        L2 = Label(textbox_frame,text='Time')
        L2.pack(side=LEFT)
        L3 = Label(time_frame,text='Minutes:')
        L3.pack(side=LEFT)
        L4 = Label(time_frame1,text='Seconds:')
        L4.pack(side=LEFT)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()

        L5=Label(checkbox_frame1,text='Shapes to be found:')
        L5.pack(side=TOP)

        C1 = Checkbutton(checkbox_frame1, text = "Triangles", variable = CheckVar1, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C2 = Checkbutton(checkbox_frame1, text = "Squares", variable = CheckVar2, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C3 = Checkbutton(checkbox_frame1, text = "Rectangles", variable = CheckVar3, onvalue = 1, offvalue = 0, height=3,  width = 20)

        # Start button.
        buttonStart = Button(startframe, text="START", command=lambda a=self.mpg: self.mpg.spawn_ship(), background = "green", width=20)
        buttonStart.pack(side=LEFT)


        # Set up shape select drop down menu.
        labelShapeSelect = Label(option_frame1, text="Sort by: ")
        labelShapeSelect.pack(side=TOP)

        shapeVar = StringVar()
        shapeVar.set("Shape")
        shapeSelect = OptionMenu(option_frame1, shapeVar, "Shape", "Colour")
        shapeSelect.config(width=35)
        shapeSelect.pack(side = TOP)

        labelSortAorD = Label(option_frame2, text="Sort in order of: ")
        labelSortAorD.pack()

        sortVar = StringVar()
        sortVar.set("Ascending")
        sortAorD = OptionMenu(option_frame2, sortVar, "Ascending", "Descending")
        sortAorD.config(width=35)
        sortAorD.pack(side = TOP)

       
        
        L6=Label(checkbox_frame2,text='Colours to be found:')
        L6.pack(side=TOP)
        
        C4 = Checkbutton(checkbox_frame2, text = "Blue", variable = CheckVar4, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C5 = Checkbutton(checkbox_frame2, text = "Red", variable = CheckVar5, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C6 = Checkbutton(checkbox_frame2, text = "Green", variable = CheckVar6, onvalue = 1, offvalue = 0, height=3,  width = 20)
        
        C1.pack(side=TOP)
        C2.pack(side=TOP)
        C3.pack(side=TOP)
        C4.pack(side=TOP)
        C5.pack(side=TOP)
        C6.pack(side=TOP)
        
        minutes=Entry(time_frame,bd=3)
        seconds=Entry(time_frame1,bd=3)
        minutes.pack(side=LEFT,expand=True,fill=BOTH)
        seconds.pack(side=LEFT,expand=True,fill=BOTH)

        



    def draw(self):
        self.mpg._radius += 10
def main():
    pgame=MyPyGame()
    pgame.runIntroWindow()
if __name__=='__main__':
    sys.exit(main())
