from tkinter import *
# create the canvas, size in pixels
canvas = Canvas(width = 300, height = 200, bg = 'white')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# Create line that curves using different points
canvas.create_line(40,170,100,140,130,60,40,120,fill="blue",smooth="true")
# run it ...
canvas.create_line(200,170,250,180,330,180,400,200,fill="blue",smooth="true")
mainloop()
