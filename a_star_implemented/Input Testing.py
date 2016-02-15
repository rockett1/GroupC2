
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
textbox_frame=Frame(window)
textbox_frame.pack(side=TOP)
minutes=Entry(textbox_frame,bd = 3)
minutes.pack(side=LEFT,expand=True,fill=BOTH)
buttonStart = Button(canvas, text="START", command=lambda: getTextValue(), background = "green", width=20)
buttonStart.pack(side=LEFT)


def getTextValue(): 
    inputs = minutes.get()
    print(inputs)
    Use = int(inputs)
    the = Use + 4
    print(the)







