# Use the Tkinter library to create GUI
from tkinter import *
#Set up a GUI called window.
window = Tk()
#Create the arena for the robot with a width of 400 pixels, a height of 300 pixels and background
#colour white
canvas = Canvas(window, width=400, height=300, bg='white')
# Change the bar name to Robot Arena
window.title("RobotArena")
# Ensure that the arena is shown
canvas.pack()
#Complete the GUI
window.mainloop()
