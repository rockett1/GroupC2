import pygame

pygame.init()
green=(0,190,0)
red=(200,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
display_width=1266
display_height=650
white=(255,255,255)
black=(0,0,0)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Hunter')
gameDisplay.fill(white)
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
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        background=pygame.image.load('space.jpg')
        gameDisplay.blit(background,(0,0))
        spawn=pygame.image.load('spawn.png')
        spawn1=pygame.image.load('spawn1.png')
        button(200,120,spawn1,spawn,"spawn")
        button(700,120,spawn1,spawn,"spawn")
        button(200,400,spawn1,spawn,"spawn")
        button(700,400,spawn1,spawn,"spawn")
        
        pygame.draw.rect(gameDisplay,white,[1000,0,5,700])
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
            ship=pygame.image.load('ship.png')
            gameDisplay.blit(ship,(x+30,y+35))
            #head=pygame.transform.rotate(ship,270) if it goes to right
            pygame.display.update()
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

runIntroWindow()


    
