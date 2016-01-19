from tkinter import *
main = Tk()
#Function to print “Left key pressed” if left arrow pressed
def leftKey(event):
    print ("Left key pressed")
#Function to print “Right key pressed” if right arrow pressed
def rightKey(event):
    print ("Right key pressed")
#Function to print “Up key pressed” if up arrow pressed
def upKey(event):
    print ("Up key pressed")
#Function to print “Down key pressed” if down arrow pressed
def downKey(event):
    print("Downkey pressed")
canvas = Canvas(main, width=100, height=100)
canvas.pack()
#Recognise keys in keyboard
canvas.bind('<Left>', leftKey)
canvas.bind('<Right>', rightKey)
canvas.bind('<Up>', upKey)
canvas.bind('<Down>', downKey)
# Create focus for keyboard
canvas.focus_set()
main.mainloop()
