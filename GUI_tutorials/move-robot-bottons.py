from tkinter import *
#Functions that move the robot left when left button pressed. Gets the current coordinates of
#the robot and move it 20-pixels to left (x1 and x2 both reduced by 20)
def leftKey():
    print ("Left button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1-20,y1,x2-20,y2)
#Functions that move the robot right when right button pressed. Gets the current coordinates of
#the robot and move it 20-pixels to right (x1 and x2 both increased by 20)
def rightKey():
    print ("Right button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1+20,y1,x2+20,y2)
def topKey():
    print ("Top button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1-20,x2,y2-20)
def downKey():
    print ("Down button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1+20,x2,y2+20)
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
buttonL=Button(window,text='Left', command=leftKey)
buttonL.pack(side=LEFT)
buttonR=Button(window,text='Right', command=rightKey)
buttonR.pack(side=RIGHT)
buttonT=Button(window,text='Top', command=topKey)
buttonT.pack(side=TOP)
buttonD=Button(window,text='Down', command=downKey)
buttonD.pack(side=BOTTOM)
canvas.pack(padx=10,pady=10)
id1=canvas.create_rectangle(120,120,100, 100, width=2)
window.mainloop()
