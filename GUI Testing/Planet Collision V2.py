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
frame2 = Frame(window, width = 50)
frame2.pack(side = LEFT)
# Section for the list box.
frameListBox = Frame(frame2)
frameListBox.pack(side = TOP)
# Top section of settings. (Item list label)
frame3 = Frame(frame2)
frame3.pack(side = TOP)
# 2nd from top section of settings. (Used for drop down menus)
frame4 = Frame(frame2)
frame4.pack(side = TOP)
# 3rd from top section of settings.
frame5 = Frame(frame2)
frame5.pack(side = TOP)
# 4th from top section of settings.
frame6 = Frame(frame2)
frame6.pack(side = BOTTOM)

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
#startGame = False

x_max, y_max = getScreenSize()
    
def id1Random(x_max, y_max, size):
    # Used to get the random spawn position for x and y.
    """
    This functions takes the maximum x and y values as well as the size of the object
    and return a random x and y position for the object to be created within the borders.
    """
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

# Functions for buttons.
def setName():
    canvas.focus_set()
def Right():
    print("Right")
def Up():
    print("Up")
def Down():
    print("Down")
def startGame():
    print("Start game!")
    global startGame
    startGame = True
def stopGame():
    print("Stop game!")
    global startGame
    startGame = False
    
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
itemListLabel = Label(frameListBox, text="ITEM LIST")
itemListLabel.pack(side = TOP)
L1 = Label(frame5, text="Ship Name: ")
L1.pack(side = LEFT)
E1 = Entry(frame5, bd = 2)
E1.pack(side = LEFT)
buttonL = Button(frame5, text="Ok", command=setName)
buttonL.pack(side=LEFT)


# List box to display list of shapes/colours.
shapeListBox = Listbox(frameListBox, height = 4)
shapeListBox.pack(side = BOTTOM)
shapeListBox.insert(1, "Triangles ")
shapeListBox.insert(2, "Squares ")
shapeListBox.insert(3, "Pentagons ")
#shapeTreeBox = Treeview(frameListBox)
#shapeTreeBox.insert("Triangles: ", "Squares: ", "Pentagons: ")

# Start and stop buttons.
buttonStart = Button(frame6, text="START", command=startGame, background = "green", width=20)
buttonStart.pack(side=LEFT)
buttonStop = Button(frame6, text="STOP", command=stopGame, background = "red", width=20)
buttonStop.pack(side=LEFT)

# Set up shape select drop down menu.
labelShapeSelect = Label(frame4, text="Sort by: ")
labelShapeSelect.pack()

shapeVar = StringVar()
shapeVar.set("Shape")
shapeSelect = OptionMenu(frame4, shapeVar, "Shape", "Colour")
shapeSelect.config(width=35)
shapeSelect.pack(side = TOP)

labelSortAorD = Label(frame4, text="Sort in order of: ", justify=LEFT, font=("Helvetica", 14))
labelSortAorD.pack()

sortVar = StringVar()
sortVar.set("Ascending")
sortAorD = OptionMenu(frame4, sortVar, "Ascending", "Descending")
sortAorD.config(width=35)
sortAorD.pack(side = TOP)

canvas.pack(padx=10, pady=10)


window.mainloop()
    
