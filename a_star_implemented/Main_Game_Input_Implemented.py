# Main game file

import pygame
import tkinter as tk
from tkinter import *
import sys
import time
from random import randint
from obj import Object
from obj import Triangle
from obj import Circle
from obj import Square
from obj import Rectangle
from a_star import A_star

class MyPyGame():
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
        self.FPS=5
        self.clock=pygame.time.Clock()
        pygame.display.update()

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
        pygame.display.update()

    def search(self,start,end,Glist):
        a=A_star(start,end,Glist)
        self.path=a.solve()
        exitGame=False
        pos_x=self.start_point_x
        pos_y=self.start_point_y
        self.de_occupy_grid(pos_x,pos_y)
        self.screen.blit(self.ship,(pos_x,pos_y))
        pygame.display.update()

        while not exitGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            for x,y in self.path:
            
                self.screen.blit(self.held_image,(0,0))

                for i in self.objects:
                    i.print_obj()
                for i in self.obstacles:
                    i.print_obj()
                self.screen.blit(self.ship,(pos_x,pos_y))
                pos_x=x
                pos_y=y
                #head=pygame.transform.rotate(self.ship,270) if it goes to right
                pygame.display.update()
                self.clock.tick(self.FPS)
            exitGame=True
        pygame.display.update()

    def game(self,x,y):
        
        exitGame=False
        while not exitGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            self.start_point_x=x+30
            self.start_point_y=y+15
            self.ship=pygame.image.load('ship.png')
            self.random_object_generator(6)
            print(self.start_point_x)
            print(self.start_point_y)
            #call the search function

            self.search((840,150),(60,60),self.Glist)
            exitGame=True
        pygame.display.update()
    def create_grid(self):
        nri=0
        nrj=0
        for i in range(30,self.display_width-30,30):
            nri=nri+1
            for j in range(30,self.display_height-30,30):
                self.Glist[(i,j)]=True
                nrj=nrj+1
##        print(self.Glist)

        return(self.Glist)
    def occupy_grid(self,x,y):
        self.Glist[(x,y)]=False
        return (self.Glist)
    def de_occupy_grid(self,x,y):
        self.Glist[(x,y)]=True
        return (self.Glist)
    def random_object_generator(self,nr):
        self.objects=[]
        self.obstacles=[]
        self.Glist=self.create_grid()
        rand_obst=randint(1,3)
        while rand_obst!=0:
        
            rand_dimension=randint(15,60)

            i=randint(0,len(self.Glist)-1)

            pos=list(self.Glist)[i]


            rand_x=pos[0]
            rand_y=pos[1]
            
            #checking if the position is available
            if (((rand_x-30,rand_y-30)in self.Glist)and ((rand_x-30,rand_y)in self.Glist)and((rand_x,rand_y-30)in self.Glist)
            and(rand_dimension<30)and(self.Glist[list(self.Glist)[i]]==True) and (self.Glist[rand_x-30,rand_y-30]==True)
            and (self.Glist[rand_x-30,rand_y]==True)and(self.Glist[rand_x,rand_y-30]==True)):

                ob4=Circle(rand_x,rand_y,rand_dimension,self.screen,self.yellow)
                self.obstacles.append(ob4)
                self.Glist=self.occupy_grid(rand_x,rand_y)
                self.Glist=self.occupy_grid(rand_x-30,rand_y-30)
                self.Glist=self.occupy_grid(rand_x-30,rand_y)
                self.Glist=self.occupy_grid(rand_x,rand_y-30)
                rand_obst=rand_obst-1
            elif (((rand_x-30,rand_y-30)in self.Glist)
            and ((rand_x-30,rand_y)in self.Glist)and((rand_x,rand_y-30)in self.Glist)and((rand_x+30,rand_y-30)in self.Glist)
            and((rand_x+30,rand_y)in self.Glist)and((rand_x,rand_y+30)in self.Glist)and((rand_x-30,rand_y+30)in self.Glist)
            and((rand_x-60,rand_y)in self.Glist)and((rand_x-60,rand_y-30)in self.Glist)and((rand_x,rand_y-60)in self.Glist)
            and((rand_x-30,rand_y-60)in self.Glist)and(rand_dimension>30) and (rand_dimension<=44)and(self.Glist[list(self.Glist)[i]]==True)
            and (self.Glist[rand_x-30,rand_y-30]==True)
            and (self.Glist[rand_x-30,rand_y]==True)and(self.Glist[rand_x,rand_y-30]==True)and(self.Glist[rand_x+30,rand_y-30]==True)
            and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x,rand_y+30]==True)and(self.Glist[rand_x-30,rand_y+30]==True)
            and(self.Glist[rand_x-60,rand_y]==True)and(self.Glist[rand_x-60,rand_y-30]==True)and(self.Glist[rand_x,rand_y-60]==True)
            and(self.Glist[rand_x-30,rand_y-60]==True)):
                ob4=Circle(rand_x,rand_y,rand_dimension,self.screen,self.yellow)
                self.Glist=self.occupy_grid(rand_x,rand_y)
                self.Glist=self.occupy_grid(rand_x-30,rand_y-30)
                self.Glist=self.occupy_grid(rand_x-30,rand_y)
                self.Glist=self.occupy_grid(rand_x,rand_y-30)
                self.Glist=self.occupy_grid(rand_x+30,rand_y-30)
                self.Glist=self.occupy_grid(rand_x+30,rand_y)
                self.Glist=self.occupy_grid(rand_x,rand_y+30)
                self.Glist=self.occupy_grid(rand_x-30,rand_y+30)
                self.Glist=self.occupy_grid(rand_x-60,rand_y)
                self.Glist=self.occupy_grid(rand_x-60,rand_y-30)
                self.Glist=self.occupy_grid(rand_x,rand_y-60)
                self.Glist=self.occupy_grid(rand_x-30,rand_y-60)
                rand_obst=rand_obst-1
                self.obstacles.append(ob4)

            elif (((rand_x-30,rand_y-30)in self.Glist)
            and ((rand_x-30,rand_y)in self.Glist)and((rand_x,rand_y-30)in self.Glist)and((rand_x+30,rand_y-30)in self.Glist)
            and((rand_x+30,rand_y)in self.Glist)and((rand_x,rand_y+30)in self.Glist)and((rand_x-30,rand_y+30)in self.Glist)
            and((rand_x-60,rand_y)in self.Glist)and((rand_x-60,rand_y-30)in self.Glist)and((rand_x,rand_y-60)in self.Glist)
            and((rand_x-30,rand_y-60)in self.Glist)and((rand_x-60,rand_y-60)in self.Glist)and((rand_x+30,rand_y-60)in self.Glist)
            and((rand_x+30,rand_y+30)in self.Glist)and((rand_x-60,rand_y+30)in self.Glist))and((rand_dimension>44)
            and(self.Glist[list(self.Glist)[i]]==True) and (self.Glist[rand_x-30,rand_y-30]==True)
            and (self.Glist[rand_x-30,rand_y]==True)and(self.Glist[rand_x,rand_y-30]==True)and(self.Glist[rand_x+30,rand_y-30]==True)
            and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x,rand_y+30]==True)and(self.Glist[rand_x-30,rand_y+30]==True)
            and(self.Glist[rand_x-60,rand_y]==True)and(self.Glist[rand_x-60,rand_y-30]==True)and(self.Glist[rand_x,rand_y-60]==True)
            and(self.Glist[rand_x-30,rand_y-60]==True)and(self.Glist[rand_x-60,rand_y-60]==True)and(self.Glist[rand_x+30,rand_y-60]==True)
            and(self.Glist[rand_x+30,rand_y+30]==True)
            and(self.Glist[rand_x-60,rand_y+30]==True)):
                ob4=Circle(rand_x,rand_y,rand_dimension,self.screen,self.yellow)
                self.Glist=self.occupy_grid(rand_x,rand_y)
                self.Glist=self.occupy_grid(rand_x-30,rand_y-30)
                self.Glist=self.occupy_grid(rand_x-30,rand_y)
                self.Glist=self.occupy_grid(rand_x,rand_y-30)
                self.Glist=self.occupy_grid(rand_x+30,rand_y-30)
                self.Glist=self.occupy_grid(rand_x+30,rand_y)
                self.Glist=self.occupy_grid(rand_x,rand_y+30)
                self.Glist=self.occupy_grid(rand_x-30,rand_y+30)
                self.Glist=self.occupy_grid(rand_x-60,rand_y)
                self.Glist=self.occupy_grid(rand_x-60,rand_y-30)
                self.Glist=self.occupy_grid(rand_x,rand_y-60)
                self.Glist=self.occupy_grid(rand_x-30,rand_y-60)
                self.Glist=self.occupy_grid(rand_x-60,rand_y-60)
                self.Glist=self.occupy_grid(rand_x+30,rand_y-60)
                self.Glist=self.occupy_grid(rand_x+30,rand_y+30)
                self.Glist=self.occupy_grid(rand_x-60,rand_y+30)
                rand_obst=rand_obst-1
                self.obstacles.append(ob4)

        while nr!=0:
                rand_dimension=randint(15,60)
                rand_shape=randint(1,3)
                rand_colour=randint(1,3)
                colours={1:self.red,2:self.blue,3:self.green}
                j=randint(0,len(self.Glist)-1)
                pos=list(self.Glist)[j]
                rand_x=pos[0]
                rand_y=pos[1]
                if rand_shape==1:
                    if((rand_dimension<30)and(self.Glist[rand_x,rand_y]==True)):
                        ob1=Square(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob1)
                        self.Glist=self.occupy_grid(rand_x,rand_y)
                        nr=nr-1
                    elif (((rand_x+30,rand_y)in self.Glist)and((rand_x+30,rand_y+30)in self.Glist)
                    and((rand_x,rand_y+30)in self.Glist))and((rand_dimension>30)and(self.Glist[rand_x,rand_y]==True)
                    and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x+30,rand_y+30]==True)
                    and(self.Glist[rand_x,rand_y+30]==True)):
                        self.Glist=self.occupy_grid(rand_x+30,rand_y)
                        self.Glist=self.occupy_grid(rand_x+30,rand_y+30)
                        self.Glist=self.occupy_grid(rand_x,rand_y+30)
                        ob1=Square(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob1)
                        nr=nr-1
                elif rand_shape==2:
                    if ((rand_dimension<30)and(self.Glist[rand_x,rand_y]==True)):
                        ob2=Rectangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob2)
                        nr=nr-1
                        self.Glist=self.occupy_grid(rand_x,rand_y)
                    elif (((rand_x+30,rand_y)in self.Glist)and((rand_x+30,rand_y+30)in self.Glist)
                    and((rand_x,rand_y+30)in self.Glist))and((rand_dimension>30) and (rand_dimension<=45)
                    and(self.Glist[rand_x,rand_y]==True)and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x+30,rand_y+30]==True)
                    and(self.Glist[rand_x,rand_y+30]==True)):
                        self.Glist=self.occupy_grid(rand_x+30,rand_y)
                        self.Glist=self.occupy_grid(rand_x+30,rand_y+30)
                        self.Glist=self.occupy_grid(rand_x,rand_y+30)
                        ob2=Rectangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob2)
                        nr=nr-1
                    elif (((rand_x+30,rand_y)in self.Glist)and((rand_x+30,rand_y+30)in self.Glist)
                    and((rand_x,rand_y+30)in self.Glist)and((rand_x+30,rand_y+60)in self.Glist)and((rand_x,rand_y+60)in self.Glist)
                    and(rand_dimension>45)and(self.Glist[rand_x,rand_y]==True)and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x+30,rand_y+30]==True)
                    and(self.Glist[rand_x,rand_y+30]==True)and((rand_x+30,rand_y+60)==True)and(self.Glist[rand_x,rand_y+60]==True)):
                        self.Glist=self.occupy_grid(rand_x+30,rand_y)
                        self.Glist=self.occupy_grid(rand_x+30,rand_y+30)
                        self.Glist=self.occupy_grid(rand_x,rand_y+30)
                        self.Glist=self.occupy_grid(rand_x+30,rand_y+60)
                        self.Glist=self.occupy_grid(rand_x,rand_y+60)
                        ob2=Rectangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob2)        
                        nr=nr-1
                elif rand_shape==3:
                    if ((rand_dimension<30)and(self.Glist[rand_x,rand_y]==True)):
                        ob3=Triangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob3)
                        self.Glist=self.occupy_grid(rand_x,rand_y)
                        nr=nr-1
                    elif (((rand_x+30,rand_y)in self.Glist)and((rand_x,rand_y+30)in self.Glist)and(rand_dimension>30)
                    and(self.Glist[rand_x,rand_y]==True)and (rand_dimension<=45)and(self.Glist[rand_x+30,rand_y]==True)
                    and(self.Glist[rand_x,rand_y+30]==True)):
                        self.Glist=self.occupy_grid(rand_x+30,rand_y)
                        self.Glist=self.occupy_grid(rand_x,rand_y+30)
                        ob3=Triangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob3)
                        nr=nr-1
                    elif (((rand_x+30,rand_y)in self.Glist)and((rand_x+30,rand_y+30)in self.Glist)
                    and((rand_x,rand_y+30)in self.Glist))and((rand_dimension>45)and(self.Glist[rand_x,rand_y]==True)
                    and(self.Glist[rand_x+30,rand_y]==True)and(self.Glist[rand_x+30,rand_y+30]==True)
                    and(self.Glist[rand_x,rand_y+30]==True)):
                        self.Glist=self.occupy_grid(rand_x+30,rand_y)
                        self.Glist=self.occupy_grid(rand_x,rand_y+30)
                        self.Glist=self.occupy_grid(rand_x+30,rand_y+30)
                        ob3=Triangle(rand_x,rand_y,1,rand_dimension,self.screen,colours[rand_colour])
                        self.objects.append(ob3)
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
                    self.gui=Gui(root)
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
            self.button(330,135,spawn1,spawn,"spawn")
            self.button(810,135,spawn1,spawn,"spawn")
            self.button(330,395,spawn1,spawn,"spawn")
            self.button(810,395,spawn1,spawn,"spawn")
            pygame.display.update()



class Gui():
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
        buttonMinutes = Button(startframe, text = "press me", command=lambda: getTextboxInput(), background = "blue", width=20)
        buttonMinutes.pack(side = LEFT)


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
       

        def getTextboxInput():
            inputs = minutes.get()
            print(inputs)
            inputs2 = seconds.get()
            print(inputs2)
      
def main():
    pgame=MyPyGame()
    pgame.runIntroWindow()
if __name__=='__main__':
    sys.exit(main())
