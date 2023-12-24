import pygame

import numpy as np

class Arc:
    def __init__(self, grid, start_point: tuple[int, int], step_count, step_length, surface, width=1, color=(255,0,0)) -> None:
        self.grid = grid
        self.start_point = start_point
        self.step_count = step_count
        self.step_length = step_length
        self.surf = surface
        self.vertex_radius = width / 2
        self.color = color
    
    def draw_vertex(self, x, y):
        pygame.draw.circle(self.surf, self.color, (x,y), self.vertex_radius)
    
    def draw_curve(self):
        screen_x, screen_y = self.start_point
        for step_num in range(self.step_count):
            self.draw_vertex(screen_x,screen_y)
            try:
                direction = self.grid.get_at_screen((screen_x, screen_y))['angle']
            except:
                direction=0
                print('off-screen')
            screen_x += self.step_length*np.cos(direction)
            screen_y += self.step_length*np.sin(direction)
            
'''
# starting point x = 500 y = 100
begin_curve:
    for n in range(num_steps):
        draw_vertex(x, y)
        x_offset = x - left_x
        y_offset = y - top_y

        grid_angle = grid[int(x_offset / resolution)][int(y_offset / resolution)]

        x += step_length * np.cos(grid_angle)
        y += step_length * np.sin(grid_angle)
'''