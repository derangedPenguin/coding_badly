import turtle

import math
import random

class Painter(turtle.Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed(10)
    
    def draw_reg_poly(self, sides, side_length, turn_left):
        for side in range(sides):
            self.forward(side_length)
            if turn_left:
                self.left(360/sides)
            else:
                self.right(360/sides)
    
    def idk_but_cool(self):
        self.left(40)

        for i in range(1000):
            self.forward(100 - i)
            self.left(90 - i)
    
    def poly_spiral(self, turns, sides, dir, fill=False):
        if fill: self.begin_fill()

        match dir:
            case 'down':
                for i in range(turns):
                    self.forward(turns - i)
                    self.left((360/sides) + 1)
            case 'up':
                for i in range(turns):
                    self.forward(i)
                    self.left((360/sides) + 1)
            case 'down-up':
                for i in range(turns * 2):
                    self.forward(turns - i)
                    self.left((360/sides) + 1)
            case 'up-down': # doesn't work idk
                for i in range(0,-turns * 2, -1):
                    self.forward(turns - i)
                    self.left((360/sides) + 1)
                    
        if fill: self.end_fill()
    
    def torus(self): # ???
        for i in range(-300, 300):
            self.forward(10)
            self.left(i % 20)
    
    def other_torus(self):
        for i in range(-600,600):
            self.forward(2)
            self.left(i%26)


bud = Painter()

#bud.poly_spiral(200, 3, 'down-up', fill=True)
bud.idk_but_cool()

screen = turtle.Screen()
screen.mainloop()