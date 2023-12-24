import sys

import random
import numpy as np
import time

import pygame

from grid import Grid
from arc import Arc

BACKGROUND = (255,255,255)
INVERSE_GROUND = (255-BACKGROUND[0], 255-BACKGROUND[1], 255-BACKGROUND[2])

a = np.array((0.66, 0.56, 0.68))
b = np.array((0.71, 0.43, 0.72))
c = np.array((0.52, 0.8, 0.52))
d = np.array((-0.43, 0.39, 0.083))

def palatte(val):
    color = a + b * np.cos(6.28318*(c*val*d))
    return ((color[0]+1)*88, (color[1]+1)*88, (color[2]+1)*88)
def idk(val):
    color = a + b * np.cos(6.28318*(c*val*d))
    return sum(color)/len(color)/255

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.framerate = 30

        self.screen = pygame.display.set_mode((960,640), flags=pygame.RESIZABLE)

        self.gui = pygame.Surface((self.screen.get_width()/5, self.screen.get_height()))
        self.canvas = pygame.Surface((self.screen.get_width()*4/5, self.screen.get_height()))
        self.arc_display = pygame.Surface(self.screen.get_size())
        self.arc_display.set_colorkey((0,0,0))
        self.display_arcs = False

        self.timer = 0

        self.spacing = 20

        self.cycling = True
        self.timer_inc = 1

        self.current_operation = 0

        self.keys_held = {'shift':False}

        #refer to coord with self[x][y]
        self.grid = Grid(self.canvas.get_width(), self.canvas.get_height(), self.spacing, 0, base_color=INVERSE_GROUND)
        #self.test_idk()

        self.drawer = Arc(self.grid, (0,0), 400, 2, self.arc_display, width=10)
    
    def calc_frame(self, mod_case=0) -> float:
        '''
        runs operation across all points for one frame
        returns operation time for performance measuring
        '''
        start_time = time.perf_counter()
        match mod_case:
            case 0:# angle based on y-pos and time
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        data['angle'] = x/-len(row) * np.pi
            case 1:# angle based on dist from center and time
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        dist = np.sqrt((x-len(self.grid)/2)**2+(y-len(self.grid[0])/2)**2)
                        data['angle'] = dist * np.pi * (self.timer/600)
            case 2: #anglee, amgnitude, & color based on dist from center and time
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        # /1000 instead of sqrt for perf, weird and wrong but works
                        dist = ((x-len(self.grid)/2)**2+(y-len(self.grid[0])/2)**2) / 1000
                        #data['magnitude'] = ((dist-10)/2)+15
                        data['angle'] = dist * np.pi * (self.timer/1000)
                        data['magnitude'] = idk(dist+self.timer*0.2) * 10000
                        data['color'] = palatte(dist+self.timer*0.2)
            #now for other than messing with colors and stuffs:
            case 3: # angle based on dist from mosue
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        screen_x, screen_y = data['pos'][0]/2, data['pos'][1]/2 # pos/2 because of resolution maybe?
                        m_pos = pygame.mouse.get_pos()
                        x_dist, y_dist = screen_x-m_pos[0], screen_y-m_pos[1]
                        dist = np.sqrt((x_dist)**2 + (y_dist)**2)
                        try:
                            angle_towards_mouse = np.tanh((screen_y+y_dist)/(screen_x+x_dist))
                        except ZeroDivisionError:
                            angle_towards_mouse = data['angle']
                        applied_dist = np.tanh(dist)
                        data['angle'] = ((data['angle']+(angle_towards_mouse)) / 2)#/(np.pi*2)
            case 4: #do something when in range of mouse, on top of case 0
                for x, row in enumerate(self.grid):
                    for y, data in enumerate(row):
                        screen_x, screen_y = data['pos'][0], data['pos'][1] # pos/2 because of resolution maybe?
                        m_pos = pygame.mouse.get_pos()
                        x_dist, y_dist = screen_x-m_pos[0], screen_y-m_pos[1]
                        dist = np.sqrt((x_dist)**2 + (y_dist)**2)
                        barrier_dist = 80
                        if dist < barrier_dist:
                            data['angle'] = dist / (np.pi*2) * (self.timer%200)/100
                            data['color'] = palatte(dist*self.timer/100)
                        elif barrier_dist <= dist <= barrier_dist*4/5:
                            data['angle'] = dist / (np.pi*2)
                        else:
                            data['angle'] = y/len(self.grid) * np.pi*2 * (self.timer/100)
                            #data['color'] = palatte(y*self.timer/100)



        return time.perf_counter() - start_time
                    
    def run(self):
        while True:
            self.gui.fill(INVERSE_GROUND)
            self.canvas.fill(BACKGROUND)

            self.timer += self.timer_inc
            '''            if abs(self.timer) > 200:
                self.timer_inc *= -1'''

            if self.cycling:
                self.calc_frame(mod_case=self.current_operation)

            self.grid.render(self.canvas, antialiasing=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #time control
                    if event.key == pygame.K_SPACE:
                        self.cycling = not self.cycling
                    if event.key == pygame.K_LEFT: # change by 1 or 10 depending on shift held
                        self.timer_inc -= 1 + (self.keys_held['shift'] * 9)
                    if event.key == pygame.K_RIGHT:
                        self.timer_inc += 1 + (self.keys_held['shift'] * 9)
                    if event.key == pygame.K_t:
                        print(self.timer)
                    #operation cases
                    if event.key == pygame.K_0:
                        self.grid.reset()
                        self.current_operation = 0
                    if event.key == pygame.K_1:
                        self.grid.reset()
                        self.current_operation = 1
                    if event.key == pygame.K_2:
                        self.grid.reset()
                        self.current_operation = 2
                    if event.key == pygame.K_3:
                        self.grid.reset()
                        self.current_operation = 3
                    if event.key == pygame.K_4:
                        self.grid.reset()
                        self.current_operation = 4
                    #check held
                    if event.key == pygame.K_LSHIFT:
                        self.keys_held['shift'] = True
                    #handle arcs & stuff
                    if event.key == pygame.K_d:
                        self.display_arcs = not self.display_arcs
                    if event.key == pygame.K_x:
                        self.arc_display.fill(BACKGROUND)

                if event.type == pygame.KEYUP:
                    #check held
                    if event.key == pygame.K_LSHIFT:
                        self.keys_held['shift'] = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.drawer.start_point = pygame.mouse.get_pos()
                        self.drawer.draw_curve()

            if self.display_arcs:
                self.canvas.blit(self.arc_display, (0,0))
            self.screen.blit(self.canvas, (0,0))
            self.screen.blit(self.gui, (self.screen.get_width()*4/5, 0))

            pygame.display.update()
            self.clock.tick(self.framerate)

Main().run()