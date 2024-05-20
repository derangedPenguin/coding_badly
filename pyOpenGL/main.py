from sys import exit
import numpy as np 

import pygame as pg 

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
   (1, -1, -1),
   (1, 1, -1),
   (-1, 1, -1),
   (-1, -1, -1),
   (1, -1, 1),
   (1, 1, 1),
   (-1, -1, 1),
   (-1, 1, 1)
)
edges = (
   (0,1),
   (0,3),
   (0,4),
   (2,1),
   (2,3),
   (2,7),
   (6,3),
   (6,4),
   (6,7),
   (5,1),
   (5,4),
   (5,7)
)
def Cube():
   glBegin(GL_LINES)
   for edge in edges:
      for vertex in edge:
         glVertex3fv(verticies[vertex])
   glEnd()


class Main:

    FPS = 60

    SCREEN_SIZE = (800,600)

    def __init__(self) -> None:
        '''---------------pg inits---------------'''
        pg.init()
        self.screen = pg.display.set_mode(self.SCREEN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF, vsync=True)
        pg.display.set_caption('Py OpenGL')
        self.clock = pg.time.Clock()

        '''---------------gl inits---------------'''
        gluPerspective(45, (self.SCREEN_SIZE[0]/self.SCREEN_SIZE[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -5)
    
    def run(self):
        while True:
            '''---------------pg/input events---------------'''
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            
            '''---------------frame updates---------------'''
            # glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            Cube()


            '''---------------render / pg handling---------------'''
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    Main().run()