import pygame
from random import randint
import time
class Object:
    def __init__(self,x1,y1,obst,screen,colour):
        self.x1=x1
        self.y1=y1
        self.obst=obst
        self.colour=colour
        self.screen=screen
    def print_obj(self):
        pass
class Triangle(Object):
    def __init__(self,x1,y1,obst,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,obst,screen,colour)
        self.x2=x1+dimension
        self.y2=y1
        self.x3=x1+(dimension/2)
        self.y3=y1+dimension
        self.price=price

    def print_obj(self):
        return(pygame.draw.polygon(self.screen,self.colour,((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3))))
class Quadrilater(Object):
    def __init__(self,x1,y1,obst,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,obst,screen,colour)
        self.price=price
    def print_obj(self):
        pass
class Square(Quadrilater):
    def __init__(self,x1,y1,obst,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,obst,price,dimension,screen,colour)
        self.heigth=dimension
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
class Rectangle(Quadrilater):
    def __init__(self,x1,y1,obst,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,obst,price,dimension,screen,colour)
        self.heigth=dimension+15
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
class Circle(Object):
    def __init__(self,x1,y1,obst,dimension,screen,colour):
        Object.__init__(self,x1,y1,obst,screen,colour)
        self.diameter=dimension
    def print_obj(self):
        return(pygame.draw.circle(self.screen,self.colour,(self.x1,self.y1),self.diameter))

##pygame.init()
##green=(0,190,0)
##red=(200,0,0)
##blue=(63,72,204)
##bright_red=(255,0,0)
##bright_green=(0,255,0)
##display_width=1266
##display_height=650
##white=(255,255,255)
##yellow=(254,216,1)
##black=(0,0,0)
##gameDisplay=pygame.display.set_mode((display_width,display_height))

def random_object_generator(nr):
    rand_obst=randint(3,4)
    while rand_obst!=0:
        
        occupied_x=[]
        occupied_y=[]
        rand_x=randint(0,970)
        rand_dimension=randint(10,30)
        rand_y=randint(0,620)
        if (rand_x not in occupied_x)and (rand_y not in occupied_y):
            ob4=Circle(rand_x,rand_y,True,rand_dimension,gameDisplay,yellow)
            for i in range(rand_x,rand_x+rand_dimension):
                    occupied_x.append(i)
            for i in range(rand_y,rand_y+rand_dimension):
                    occupied_y.append(i)
            ob4.print_obj()
            rand_obst=rand_obst-1
        
    while nr!=0:
        rand_x=randint(0,970)
        rand_dimension=randint(10,30)
        rand_y=randint(0,620)
        rand_shape=randint(1,3)
        rand_colour=randint(1,3)
        colours={1:red,2:blue,3:green}
        if (rand_x not in occupied_x)and (rand_y not in occupied_y):
            if rand_shape==1:
                ob1=Square(rand_x,rand_y,False,1,rand_dimension,gameDisplay,colours[rand_colour])
                for i in range(rand_x,rand_x+rand_dimension):
                    occupied_x.append(i)
                for i in range(rand_y,rand_y+rand_dimension):
                    occupied_y.append(i)
                ob1.print_obj()
            elif rand_shape==2:
                ob2=Rectangle(rand_x,rand_y,False,1,rand_dimension,gameDisplay,colours[rand_colour])
                for i in range(rand_x,rand_x+rand_dimension+15):
                    occupied_x.append(i)
                for i in range(rand_y,rand_y+rand_dimension):
                    occupied_y.append(i)
                ob2.print_obj()
            elif rand_shape==3:
                ob3=Triangle(rand_x,rand_y,False,1,rand_dimension,gameDisplay,colours[rand_colour])
                for i in range(rand_x,rand_x+rand_dimension):
                    occupied_x.append(i)
                for i in range(rand_y,rand_y+rand_dimension):
                    occupied_y.append(i)
                ob3.print_obj()
            nr=nr-1
    pygame.display.update()



def text_objects(text,font):
    black=(0,0,0)
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def button(x,y,img1,img,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+150>=mouse[0]>=x and y+80>=mouse[1]>y:
        gameDisplay.blit(img1,(x,y))
        if click[0]==1 and action!=None:
            if action=="play":
                spawn_ship()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="spawn":
                game(x,y)
                
    else:
        gameDisplay.blit(img,(x,y))    


def message_display(text):

    largeText=pygame.font.Font('freesansbold.ttf',40)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
def spawn_ship():
    exitW=False
    while not exitW:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        background=pygame.image.load('space.jpg')
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))
        spawn=pygame.image.load('spawn.png')
        spawn1=pygame.image.load('spawn1.png')
        button(200,120,spawn1,spawn,"spawn")
        button(700,120,spawn1,spawn,"spawn")
        button(200,400,spawn1,spawn,"spawn")
        button(700,400,spawn1,spawn,"spawn")
        pygame.draw.rect(gameDisplay,white,[1000,0,5,650])

    pygame.display.update()



def game(x,y):
    exitGame=False
    background=pygame.image.load('space.jpg')
    gameDisplay.blit(background,(0,0))
    pygame.draw.rect(gameDisplay,white,[1000,0,5,700])
    while not exitGame:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            random_object_generator(4)
            ship=pygame.image.load('ship.png')
            gameDisplay.blit(ship,(x+30,y+35))
            #head=pygame.transform.rotate(ship,270) if it goes to right
            exitGame=True
    pygame.display.update()
    time.sleep(5)


def runIntroWindow():

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
            message_display("Welcome to Space Hunter!")
            button(400,350,startimg1,startimg,"play")
            button(760,350,quitimg1,quitimg,"quit")
            
    pygame.display.update()
pygame.init()
green=(0,190,0)
red=(200,0,0)
blue=(63,72,204)
bright_red=(255,0,0)
bright_green=(0,255,0)
display_width=1266
display_height=650
white=(255,255,255)
yellow=(254,216,1)
black=(0,0,0)
gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Space Hunter')
gameDisplay.fill(white)
pygame.display.update()
runIntroWindow()


    

    
   
        
