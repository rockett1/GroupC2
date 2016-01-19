"""
Basic Robot Moving round arena using Python and TKinter
"""
import time
from random import random
# Get TKinter ready to go
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
canvas.pack(padx=10,pady=10)
# The velocity, or distance moved per time step
vx = 10.0 # x velocity
vy = 5.0 # y velocity
id1=canvas.create_rectangle(3,7,3+10,7+10)
x1,y1,x2,y2=canvas.coords(id1)
canvas.coords(id1,x1,y1+vy,x2,y2+vy)
canvas.update()
# Pause for 0.1 seconds, then delete the image
time.sleep(1)
x1,y1,x2,y2=canvas.coords(id1)
# Reposition the robot
canvas.coords(id1,x1,y1+vy,x2,y2+vy)
canvas.update()
time.sleep(1)
x1,y1,x2,y2=canvas.coords(id1)
# Reposition the robot
canvas.coords(id1,x1,y1+vy,x2,y2+vy)
canvas.update()
# Reposition the robot
canvas.coords(id1,x1+vx,y1,x2+vx,y2)
canvas.update()
time.sleep(1)
x1,y1,x2,y2=canvas.coords(id1)
# Reposition the robot
canvas.coords(id1,x1+vx,y1,x2+vx,y2)
canvas.update()
for i in range (10):
    if i%2==0:
        canvas.coords(id1,x1+vx,y1,x2+vx,y2)
        canvas.update()
        time.sleep(0.5)
        x1,y1,x2,y2=canvas.coords(id1)
    else:
        canvas.coords(id1,x1,y1+vy,x2,y2+vy)
        canvas.update()
        time.sleep(0.5)
        x1,y1,x2,y2=canvas.coords(id1)
window.mainloop()
