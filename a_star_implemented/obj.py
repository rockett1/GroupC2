
# Object to be collected file
import pygame
import tkinter as tk
from tkinter import *
import sys
import time
from random import randint


class Object:
    def __init__(self,x1,y1,screen,colour):
        self.x1=x1
        self.y1=y1

        self.colour=colour
        self.screen=screen
    def print_obj(self):
        pass
	def get_coord(self):
		return((self.x1,self.x2))
class Triangle(Object):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.x2=x1+dimension
        self.y2=y1
        self.x3=x1+(dimension/2)
        self.y3=y1+dimension
        self.price=price

    def print_obj(self):
        return(pygame.draw.polygon(self.screen,self.colour,((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3))))
    def __str__(self):
        return(__class__.__name__ + " with a price of " + str(self.price))
    
class Quadrilater(Object):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.price=price
    def print_obj(self):
        pass
class Square(Quadrilater):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,price,dimension,screen,colour)
        self.heigth=dimension
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
    def __str__(self):
        return(__class__.__name__ + " with a price of " + str(self.price))
    
class Rectangle(Quadrilater):
    def __init__(self,x1,y1,price,dimension,screen,colour):
        Quadrilater.__init__(self,x1,y1,price,dimension,screen,colour)
        self.heigth=dimension+15
        self.weight=dimension
    def print_obj(self):
        return(pygame.draw.rect(self.screen,self.colour,(self.x1,self.y1,self.heigth,self.weight)))
    def __str__(self):
        return(__class__.__name__ + " with a price of " + str(self.price))
    
class Circle(Object):
    def __init__(self,x1,y1,dimension,screen,colour):
        Object.__init__(self,x1,y1,screen,colour)
        self.diameter=dimension
    def print_obj(self):
        return(pygame.draw.circle(self.screen,self.colour,(self.x1,self.y1),self.diameter))

