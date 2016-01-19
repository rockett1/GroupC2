from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()
# Create a rectangle on the arena at the coordinates x1=50, y1=80, x2=100 and y2=120. The
#rectangle is red.
objectrectangle=canvas.create_rectangle(80, 185, 180,240, fill="red")
#Create an oval at coordinates s x1=100, y1=10, x2=210 and y2=80. The oval is yellow.
objectoval=canvas.create_oval(100, 10, 210, 80, fill='yellow')
window.mainloop()
