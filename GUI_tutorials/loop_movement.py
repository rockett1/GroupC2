"""
Basic Robot Moving round arena using Python and TKinter
"""
# Get TKinter ready to go
from tkinter import *
import time
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
canvas.pack(padx=10,pady=10)
# The velocity, or distance moved per time step
vx = 10.0 # x velocity
vy = 5.0 # y velocity
id1=canvas.create_rectangle(3,7,3+10,7+10)
# Generate robot movement 200 timesteps
for t in range(1, 200):
    x1,y1,x2,y2=canvas.coords(id1)
    # Reposition the robot
    canvas.coords(id1,x1,y1+vy,x2,y2+vy)
    canvas.update()
    # Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)
window.mainloop() 
