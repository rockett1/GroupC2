import time
from tkinter import *
import random
import pygame

window = Tk()
window.wm_title("Blind robot")
# Main game frame.
frame1 = Frame(window)
frame1.pack(side = LEFT)
# Settings menu frame.
frame2 = Frame(window)
frame2.pack(side = LEFT)
# Top section of settings.
frame3 = Frame(frame2)
frame3.pack(side = TOP)
# 2nd from top section of settings.
frame4 = Frame(frame2)
frame4.pack(side = TOP)
# 3rd from top section of settings.
frame5 = Frame(frame2)
frame5.pack(side = TOP)
def getScreenSize():
    # NOT WORKING
    wwidth = canvas.winfo_reqwidth()
    wheight = canvas.winfo_reqheight()
    return wwidth, wheight

canvas = Canvas(frame1, width=1200, height=800, bg="black")
canvas.pack(expand = YES, fill = BOTH)
vx = 10.0
vy = 5.0
ovx = 2.0
ovy = 1.0
pvx = 0.0
pvy = 0.0
x_min = 0.0
y_min = 0.0
playerCrash = False


x_max, y_max = getScreenSize()
    
def id1Random(x_max, y_max, size):
    # Used to get the random spawn position for x and y.
    startx1 = random.randint(size,x_max-size)
    starty1 = random.randint(size,y_max-size)
    return startx1, starty1
    
startx1, starty1 = id1Random(x_max, y_max, 50)
Obx1, Oby1 = id1Random(x_max, y_max, 150)
Obx2 = Obx1+150
Oby2 = Oby1+150
px1, py1 = id1Random(x_max, y_max, 25)
countx = 0
county = 0

# Sun
id2 = canvas.create_rectangle(Obx1, Oby1, Obx2, Oby2, fill = "yellow", outline = "red", width = "15")
#Earth
id1 = canvas.create_rectangle(startx1,starty1,startx1+10,starty1+10, fill = "green", outline = "blue", width = "1")
#Player
id3 = canvas.create_rectangle(px1, py1, px1+25, py1+25, fill = "purple")

def setName():
    canvas.focus_set()
def Right():
    print("Right")
def Up():
    print("Up")
def Down():
    print("Down")

# Functions for changing velocity of player.
def leftKey(event):
    print("Left key pressed.")
    global pvx
    pvx = pvx - 1.0
def rightKey(event):
    print("Right key pressed.")
    global pvx
    pvx = pvx + 1.0
def upKey(event):
    print("Up key pressed.")
    global pvy
    pvy = pvy - 1.0
def downKey(event):
    print("Down key pressed.")
    global pvy
    pvy = pvy + 1.0
def returnKey(event):
    print("Return key pressed.")
    canvas.focus_set()

# Set up text input for ship name.
itemListLabel = Label(frame3, text="ITEM LIST")
itemListLabel.pack(side = TOP)
L1 = Label(frame5, text="Ship Name")
L1.pack(side = LEFT)
E1 = Entry(frame5, bd = 2)
E1.pack(side = LEFT)
buttonL = Button(frame5, text="Ok", command=setName)
buttonL.pack(side=LEFT)
#buttonR = Button(frame2, text="Right", command=Right)
#buttonR.pack(side=RIGHT)
#buttonU = Button(frame2, text="Up", command=Up)
#buttonU.pack(side=TOP)
#buttonD = Button(frame2, text="Down", command=Down)
#buttonD.pack(side=BOTTOM)
# Set up shape select drop down menu.


# Setting up frame for drop down menus.

shapeVar = StringVar()
shapeVar.set("Triangle")
shapeSelect = OptionMenu(frame3, shapeVar, "Triangle", "Square", "Pentagon", "Hexagon")
shapeSelect.pack(side = TOP)

sortVar = StringVar()
sortVar.set("Ascending")
sortAorD = OptionMenu(frame4, sortVar, "Ascending", "Descending")
sortAorD.pack(side = TOP)

canvas.pack(padx=10, pady=10)

# Bind all key presses to functions.
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Down>", downKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Return>", returnKey)
canvas.focus_set()

#canvas.create_line(40,170,100,800,230,60,40,120,fill="blue",smooth="true")

for t in range(1,5000):
    x_max,y_max = getScreenSize()
    x1,y1,x2,y2 = canvas.coords(id1)
    Obx1,Oby1,Obx2,Oby2 = canvas.coords(id2)
    px1, py1, px2, py2 = canvas.coords(id3)

    # Collision between Earth and Sun
    if x1 > (Obx2) and x1 < (Obx2 + 15) and y1 >= Oby1 and y1 <= Oby2:
        countx = 3
        print("Object detected left side.")
    if x2 < (Obx1) and x2 > (Obx1 - 15) and y1 >= Oby1 and y1 <= Oby2:
        print("Object detected right side.")
        countx = -3
    if y1 > (Oby2) and y1 < (Oby2 + 15) and x2 >= Obx1 and x1 <= Obx2:
        print("Object detected above.")
        county = 3
    if y2 < (Oby1) and y2 > (Oby1 - 15) and x2 >= Obx1 and x1 <= Obx2:
        print("Object detected below.")
        county = -3

    # Change direction if collision.    
    if countx>0:
        vx = 10.0
        countx = countx-1
    elif countx <0:
        vx = -10.0
        countx = countx+1
    if county>0:
        vy = 5.0
        county = county-1
    elif county<0:
        vy = -5.0
        county = county+1

    # Boundry collision detection for Earth object.
    if x1 >= x_max-10:
        vx = -10.0
    if y1 <= y_min+5:
        vy = 5.0
    if y2 >= y_max-5:
        vy = -5.0
    if x2 <= x_min+10:
        vx = 10.0

    # Boundry collision detection for Sun object.
    if Obx1 >= x_max-160:
        ovx = -2.0
    elif Obx2 <= x_min+160:
        ovx = 2.0
    if Oby1 <= y_min+10:
        ovy = 1.0
    elif Oby2 >= y_max-10:
        ovy = -1.0

    # Collision between Sun and player objects.
    if playerCrash == False:
        if px1 <= (Obx2) and px1 >= (Obx1) and py1 >= Oby1 and py1 <= Oby2:
            playerCrash = True
        elif py1 <= (Oby2) and py1 >= (Oby1) and px1 >= Obx1 and px1 <= Obx2:
            playerCrash = True
        if playerCrash == True:
            shipName = E1.get()
            print("The ship \"" + shipName + "\" has crashed!")

    # Update positions for objects.
    canvas.coords(id2,Obx1+ovx,Oby1+ovy,Obx2+ovx,Oby2+ovy)
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    if playerCrash == False:
        canvas.coords(id3,px1+pvx,py1+pvy,px2+pvx,py2+pvy)
    canvas.update()
    time.sleep(0.025)

window.mainloop()
    
