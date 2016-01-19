import time
from tkinter import *
#Move robot to left
def leftKey(event):
    print ("Left key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1-10,y1,x2-10,y2)
#Move robot to right
def rightKey(event):
    print ("Right key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1+10,y1,x2+10,y2)
#Move robot up
def upKey(event):
    print ("Up key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1-5,x2,y2-5)
#Move robot to down
def downKey(event):
    print ("Down key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1+5,x2,y2+5)
main = Tk()
#Create canvas
canvas = Canvas(main, width=400, height=300)
canvas.pack()
#Create user controlled robot
id1=canvas.create_rectangle(120,120,100, 100, width=2)
#move robot using keys
canvas.bind('<Left>', leftKey)
canvas.bind('<Right>', rightKey)
canvas.bind('<Up>', upKey)
canvas.bind('<Down>', downKey)
canvas.focus_set()
#Amount move root by
vx = 10.0 # x velocity
vy = 5.0 # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 400.0
y_max = 300.0
# Create computer controlled robot
id2=canvas.create_rectangle(3,7,3+10,7+10)
# Move robot around
for t in range(1, 500):
    X1,Y1,X2,Y2=canvas.coords(id2)
    # Change direction if near edge
    if X1 >= x_max:
        vx = -10.0
    if Y1 <= y_min:
        vy = 5.0
    if Y2 >= y_max:
        vy = -5.0
    if X1 <= x_min:
        vx = 10.0
    # Move robot a fixed amount
    canvas.coords(id2,X1+vx,Y1+vy,X2+vx,Y2+vy)
    canvas.update()
    # Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)
main.mainloop()
