# Main game file
#importing necessary
import pygame
import copy
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

class MyPyGame(object):
    def __init__(self):
        #define grid
        self.Glist={}
        
        #initialising pygame
        
        pygame.display.init()
        
        #defining the colours in the RGB(red,green,blue) system
        self.green=(0,190,0)
        self.red=(200,0,0)
        self.blue=(63,72,204)
        self.white=(255,255,255)
        self.yellow=(254,216,1)
        self.black=(0,0,0)
        #defining the screen dimensions
        self.display_width=1266
        self.display_height=650
        #defining the screen
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        #naming the window
        pygame.display.set_caption('Space Hunter')
        #uploading the background image
        self.background=pygame.image.load('space.jpg')
        #blit the image on the screen
        self.screen.blit(self.background,(0,0))
        #setting fps
        self.FPS=8
        self.clock=pygame.time.Clock()
        #updateting pygame window
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
    
    def find_best_obj(self,start):
        minim=10000
        
        find_list={}
        for i in self.good_list:
            distance=self.cost(start,i.get_coord())
            price=i.get_price()
            find_list[i]=distance
            if (find_list[i]/price)<minim:
                minim=find_list[i]
                position=i.get_coord()
                x=i
        return(position)
    def cost(self,start,goal):
        
        dx=abs(start[0]-goal[0])
        dy=abs(goal[1]-start[1])
        D=abs(dx-dy)
        E=min(dx,dy)
        return ( round( (((E*14)+(D*10))/30),0) )
        
        

    def search(self,start,end,Glist):
        
        exitGame=False
        pos_x=self.start_point_x
        pos_y=self.start_point_y
        self.de_occupy_grid(pos_x,pos_y)

        
        for i in range(end[0]-30,end[0]+30,30):
                for j in range(end[1]-30,end[1]+30,30):
                    self.de_occupy_grid(i,j)
        a=A_star(end,start,Glist)
        self.path=a.solve()
        first_x,first_y=self.path[0]
        

        while not exitGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            for x,y in self.path:
                if x>first_x and y>first_y:
                    #direction='down_right'
                    ship=pygame.transform.rotate(self.ship,225)
                elif x>first_x and y==first_y:
                    #direction=='right'
                    ship=pygame.transform.rotate(self.ship,270)
                elif x>first_x and y<first_y:
                    #direction='up_right'
                    ship=pygame.transform.rotate(self.ship,315)
                elif x==first_x and y<first_y:
                    ship=self.ship
                elif x==first_x and y==first_y:
                    ship=self.ship
                elif x==first_x and y>first_y:
                    #direction='down'
                    ship=pygame.transform.rotate(self.ship,180)
                elif x<first_x and y>first_y:
                    #direction='down_left'
                    ship=pygame.transform.rotate(self.ship,135)
                if x<first_x and y==first_y:
                    #direction='left'
                    ship=pygame.transform.rotate(self.ship,90)
                if x<first_x and y<first_y:
                    #direction='up_left'
                    ship=pygame.transform.rotate(self.ship,45)
                self.screen.blit(self.held_image,(0,0))
                first_x=x
                first_y=y
                for i in self.objects:
                    i.print_obj()
                for i in self.obstacles:
                    i.print_obj()
                pos_x=x
                pos_y=y
                self.screen.blit(ship,(pos_x,pos_y))
                pygame.display.update()
                self.clock.tick(self.FPS)
            
            for i in self.good_list:
                if end==i.get_coord(): 
                    x=i
            self.good_list.remove(x)
            self.objects.remove(x)
            exitGame=True
        pygame.display.update()
    def obj_to_found(self,Alist):
        ok=1
        self.good_list=[]
        self.minutes=user_input[0]
        self.seconds=user_input[1]
        self.sort_type=user_input[9]
        self.sort_order=user_input[8]
        red_i=user_input[6]
        blue_i=user_input[5]
        green_i=user_input[7]
        square_i=user_input[3]
        rect_i=user_input[4]
        tri_i=user_input[2]
        

        for i in self.objects:
            
            if i.get_colour()==self.red and (red_i)==1:
                ok=0
            if i.get_colour()==self.blue and (blue_i)==1:
                ok=0
            if i.get_colour()==self.green and (green_i)==1:
                ok=0
            if i.get_shape()=='T' and (tri_i)==1:
                ok=0
            if i.get_shape()=='R' and (rect_i)==1:
                ok=0
            if i.get_shape()=='S' and (square_i)==1:
                ok=0
            if ok==0:
                self.good_list.append(i)
            ok=1
        return (self.good_list)
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
            self.random_object_generator(10)
            self.good_list=self.obj_to_found(self.objects)
            
            self.start_pos=(self.start_point_x,self.start_point_y)
            #call the search function
            
            while self.good_list:
                current_to_be_found=self.find_best_obj((self.start_pos))
                self.search((self.start_pos),(current_to_be_found),self.Glist)
                self.start_pos=current_to_be_found
                
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
        rand_obst=randint(2,3)
        while rand_obst!=0:
        
            rand_dimension=randint(45,60)

            i=randint(0,len(self.Glist)-1)

            pos=list(self.Glist)[i]


            rand_x=pos[0]
            rand_y=pos[1]
            ok=1
            #checking if the position is available
            for x in range(rand_x-60,rand_x+61,30):
                for y in range(rand_y-60,rand_y+61,30):
                    if  (x,y)in self.Glist and self.Glist[(x,y)]==True:
                        pass
                    else:
                        ok=0
            if ok:
                for x in range(rand_x-60,rand_x+61,30):
                    for y in range(rand_y-60,rand_y+61,30):
                        self.Glist=self.occupy_grid(x,y)
                ob4=Circle(rand_x,rand_y,rand_dimension,self.screen,self.yellow)
                rand_obst=rand_obst-1
                self.obstacles.append(ob4)


        while nr>0:
                
                rand_shape=randint(1,3)
                rand_colour=randint(1,3)
                colours={1:self.red,2:self.blue,3:self.green}
                if rand_colour==1:
                    price=randint(4,6)
                elif rand_colour==2:
                    price=randint(7,9)
                elif rand_colour==3:
                    price=randint(1,3)
                j=randint(0,len(self.Glist)-1)
                pos=list(self.Glist)[j]
                rand_x=pos[0]
                rand_y=pos[1]
                if rand_shape==1:
                    ok=1
                    for x in range(rand_x,rand_x+31,30):
                        for y in range(rand_y,rand_y+31,30):
                            if  (x,y)in self.Glist and self.Glist[(x,y)]==True:
                                pass
                            else:
                                ok=0
                    if ok:
                        for x in range(rand_x,rand_x+31,30):
                            for y in range(rand_y,rand_y+31,30):
                                self.Glist=self.occupy_grid(x,y)
                        ob1=Square(rand_x,rand_y,price,45,self.screen,colours[rand_colour])
                        self.objects.append(ob1)
                        nr=nr-1
                elif rand_shape==2:
                    ok=1
                    for x in range(rand_x,rand_x+31,30):
                        for y in range(rand_y,rand_y+31,30):
                            
                            if  (x,y)in self.Glist and self.Glist[(x,y)]==True:
                                pass
                            else:
                                ok=0
                                
                    if ok:
                        for x in range(rand_x,rand_x+31,30):
                            for y in range(rand_y,rand_y+31,30):
                                self.Glist=self.occupy_grid(x,y)
                        ob2=Triangle(rand_x,rand_y,price,45,self.screen,colours[rand_colour])
                        self.objects.append(ob2)
                        nr=nr-1
                elif rand_shape==3:
                    ok=1
                    for x in range(rand_x,rand_x+31,30):
                        for y in range(rand_y,rand_y+31,30):
                            if  (x,y)in self.Glist and self.Glist[(x,y)]==True:
                                pass
                            else:
                                ok=0
                    if ok:
                        for x in range(rand_x,rand_x+31,30):
                            for y in range(rand_y,rand_y+31,30):
                                self.Glist=self.occupy_grid(x,y)
                        ob3=Rectangle(rand_x,rand_y,price,45,self.screen,colours[rand_colour])
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
                self.button(330,135,spawn1,spawn,"spawn")
                self.button(810,135,spawn1,spawn,"spawn")
                self.button(330,405,spawn1,spawn,"spawn")
                self.button(810,405,spawn1,spawn,"spawn")
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

        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()
        self.CheckVar5 = IntVar()
        self.CheckVar6 = IntVar()

        L5=Label(checkbox_frame1,text='Shapes to be found:')
        L5.pack(side=TOP)

        C1 = Checkbutton(checkbox_frame1, text = "Triangles", variable = self.CheckVar1, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C2 = Checkbutton(checkbox_frame1, text = "Squares", variable = self.CheckVar2, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C3 = Checkbutton(checkbox_frame1, text = "Rectangles", variable = self.CheckVar3, onvalue = 1, offvalue = 0, height=3,  width = 20)

        # Start button.
        buttonStart = Button(startframe, text="START", command=lambda a=self.mpg: self.mpg.spawn_ship(), background = "green", width=20)
        buttonStart.pack(side=LEFT)
        buttonMinutes = Button(startframe, text = "Enter inputs", command=lambda: self.getTextBoxInput(), background = "blue", width=20)
        buttonMinutes.pack(side = LEFT)


        # Set up shape select drop down menu.
        labelShapeSelect = Label(option_frame1, text="Sort by: ")
        labelShapeSelect.pack(side=TOP)

        self.shapeVar = StringVar()
        self.shapeVar.set("Shape")
        shapeSelect = OptionMenu(option_frame1, self.shapeVar, "Shape", "Colour")
        shapeSelect.config(width=35)
        shapeSelect.pack(side = TOP)

        labelSortAorD = Label(option_frame2, text="Sort in order of: ")
        labelSortAorD.pack()

        self.sortVar = StringVar()
        self.sortVar.set("Ascending")
        sortAorD = OptionMenu(option_frame2, self.sortVar, "Ascending", "Descending")
        sortAorD.config(width=35)
        sortAorD.pack(side = TOP)

       
        
        L6=Label(checkbox_frame2,text='Colours to be found:')
        L6.pack(side=TOP)
        
        C4 = Checkbutton(checkbox_frame2, text = "Blue", variable = self.CheckVar4, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C5 = Checkbutton(checkbox_frame2, text = "Red", variable = self.CheckVar5, onvalue = 1, offvalue = 0, height=3,  width = 20)
        C6 = Checkbutton(checkbox_frame2, text = "Green", variable = self.CheckVar6, onvalue = 1, offvalue = 0, height=3,  width = 20)
        
        C1.pack(side=TOP)
        C2.pack(side=TOP)
        C3.pack(side=TOP)
        C4.pack(side=TOP)
        C5.pack(side=TOP)
        C6.pack(side=TOP)
        
        self.minutes=Entry(time_frame,bd=3)
        self.seconds=Entry(time_frame1,bd=3)
        self.minutes.pack(side=LEFT,expand=True,fill=BOTH)
        self.seconds.pack(side=LEFT,expand=True,fill=BOTH)
       
    def getTextBoxInput(self):
        inputs=self.minutes.get()
        inputs2=self.seconds.get()
        TriInput=self.CheckVar1.get()
        SquareInput=self.CheckVar2.get()
        RectInput=self.CheckVar3.get()
        BlueInput=self.CheckVar4.get()
        RedInput=self.CheckVar5.get()
        GreenInput=self.CheckVar6.get()
        SortInput=self.sortVar.get()
        ShapeInput=self.shapeVar.get()
        self.CheckInput(inputs,inputs2)
        global user_input
        user_input= (inputs,inputs2,TriInput,SquareInput,RectInput,BlueInput,RedInput,GreenInput,SortInput,ShapeInput)
    def CheckInput(self,minutes,sec):
        try:
            IntMins=int(minutes)
            if IntMins<0:
                raise ValueError('Must be positive')
            IntSec=int(sec)
            if IntSec<0 or IntSec>60:
                raise ValueError('Seconds must be between 0-60')
        except TypeError:
            print('Wrong Input!')
    	
def main():
    pgame=MyPyGame()
    pgame.runIntroWindow()
if __name__=='__main__':
    sys.exit(main())
