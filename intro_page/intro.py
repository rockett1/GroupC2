import pygame

pygame.init()
green=(0,190,0)
red=(200,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
display_width=800
display_height=600
white=(255,255,255)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Hunter')
gameDisplay.fill(white)
pygame.display.update()
def text_objects(text,font):
    black=(0,0,0)
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def button(msg,x,y,img1,img,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+100>=mouse[0]>=x and y+70>=mouse[1]>y:
        gameDisplay.blit(img1,(x,y))
        if click[0]==1 and action!=None:
            if action=="play":
                #run game
                pass
            elif action=="quit":
                pygame.quit()
                quit()   
    else:
        gameDisplay.blit(img,(x,y))    


    pygame.display.update()
def message_display(text):

    largeText=pygame.font.Font('freesansbold.ttf',40)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
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
            button("Start Game",180,350,startimg1,startimg,"play")
            button("Quit",540,350,quitimg1,quitimg,"quit")
            #pygame.draw.circle(gameDisplay,green,(200,400),(40))
            pygame.display.update()

runIntroWindow()


    
