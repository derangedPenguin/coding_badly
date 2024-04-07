import sys

import numpy as np

import pygame

from ctypes import *
from cython import *

MARGIN = 1

a = np.array((0.66, 0.56, 0.68))
b = np.array((0.71, 0.43, 0.72))
c = np.array((0.52, 0.8, 0.52))
d = np.array((-0.43, 0.39, 0.083))

def palatte(val):
    global a, b, c, d
    color = a + b * np.cos(6.28318*(c*val*d))
    return ((color[0]+1)*88, (color[1]+1)*88, (color[2]+1)*88)
def idk(val):
    global a, b, c, d
    color = a + b * np.cos(6.28318*(c*val*d))
    return sum(color)/len(color)/255

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((640,640), flags=pygame.RESIZABLE)
        #self.fancy_screen = pygame.display.se
        self.clock = pygame.time.Clock()

        self.timer = 0

        self.spacing = 10

        self.cycling = True
        self.timer_inc = 1

        #refer to coord with self[x][y]
        self.grid = [
            [[np.pi*2/3,10,(255,255,255)] 
             for __ in range(int(self.screen.get_width()*-(MARGIN-1)), int(self.screen.get_width()*MARGIN), self.spacing)
             ] for _ in range(int(self.screen.get_height()*-(MARGIN-1)), int(self.screen.get_height()*MARGIN), self.spacing)
            ]
        #self.test_idk()

    def __getitem__(self, key):
        return self.grid[key]
    def __setitem__(self, key, value):
        self.grid[key] = value

    def test_idk(self, thing=0):
        # match thing:
        #     case 0:
        #         for y, row in enumerate(self.grid):
        #             for x, data in enumerate(row):
        #                 pass
        #                 #self[x][y] = y/len(self.grid) * np.pi*2
        #     case 1:
        #         for y, row in enumerate(self.grid):
        #             for x, data in enumerate(row):
        #                 dist = np.sqrt((x-len(self.grid)/2)**2+(y-len(self.grid[0])/2)**2)
        #                 self[x][y][0] = dist * np.pi * (self.timer/600%20)
        #     case 2:
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        dist = np.sqrt((x-len(self.grid)/2)**2+(y-len(self.grid[0])/2)**2)
                        data[1] = ((dist-10)/2)+15
                        self[x][y][0] = dist * np.pi * (self.timer/1000)
                        self[x][y][1] = idk(dist+self.timer*0.2) * 20000
                        self[x][y][2] = palatte(dist+self.timer*0.2)
            # #now for other than messing with colors and stuffs:
            # case 3:
            #     for x, row in enumerate(self.grid):
            #         for y, data in enumerate(row):
            #             pass
                    
    def run(self):
        while True:
            self.screen.fill((0,0,0))

            self.timer += self.timer_inc

            if self.cycling:
                self.test_idk(thing=2)

            for y_, row in enumerate(self.grid):
                for x_, data in enumerate(row):
                    point_angle, magnitude, color = data
                    x, y = x_*self.spacing, y_*self.spacing
                    try:
                        pygame.draw.aaline(self.screen, color, (x,y), (x+magnitude*np.cos(point_angle), y+magnitude*np.sin(point_angle))) #have angle(radians) and hypotenuse length, trig from there
                    except ValueError:
                        print(color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.cycling = not self.cycling
                    if event.key == pygame.K_LEFT:
                        self.timer_inc -= 1
                    if event.key == pygame.K_RIGHT:
                        self.timer_inc += 1
                    if event.key == pygame.K_t:
                        print(self.timer)

            pygame.display.update()
            print(self.clock.tick(60))

Main().run()