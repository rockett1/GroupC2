from tkinter import *
#Functions that print left and right. Called when press button
def Left():
    print ("Left")
def Right():
    print ("Right")
def Up():
    print ("Up")
def Down():
    print ("Down")
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
#Create left button and call function to print left
buttonL=Button(window,text='Left', command=Left)
buttonL.pack(side=LEFT)
# Create right button and call function to print right
buttonR=Button(window,text='Right', command=Right)
buttonR.pack(side=RIGHT)

buttonU=Button(window,text='Up', command=Up)
buttonU.pack(side=TOP)

buttonD=Button(window,text='Down', command=Down)
buttonD.pack(side=BOTTOM)
#Create padding at button of the screen
canvas.pack(padx=10,pady=10)
window.mainloop()
