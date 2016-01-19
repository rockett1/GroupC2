# Allow the GUI to include time functions
import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=300, bg='white')
canvas.pack()
id1=canvas.create_rectangle(40,40,140,140,fill="lightblue",outline="brown",width=6)
# Update to display the square on the arena
canvas.update()
#Do nothing for 2 seconds
time.sleep(2)
#Access the coordinates at which the rectangle is found (id1)
x1,y1,x2,y2=canvas.coords(id1)
#Reposition the square using the coordinates we collected and adding 30 onto each one.
canvas.coords(id1,x1+30,y1+30,x2+30,y2+30)
canvas.update()
canvas.coords(id1,x1,y1,x2,y2)
time.sleep(3)
canvas.update()
window.mainloop()
