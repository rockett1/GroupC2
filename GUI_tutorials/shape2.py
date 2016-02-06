from tkinter import *
window = Tk()
canvas = Canvas(window, width=600, height=600, bg='white')
canvas.pack()
#Create a black line at co-ordinates x1=30, y1=60, x2=130, y2=90. The line is black.
canvas.create_line(30,60,130,60,fill="black",width=20)
# Create a polygon (the coordinates are x1, y1 … xn,yn.
#The outline is brown and is 6 pixels thick and the fill is lightblue. X1=40, y1=40
canvas.create_polygon(60,100,140,140,150,180,fill="lightblue",outline="brown",width=6)
window.mainloop()
