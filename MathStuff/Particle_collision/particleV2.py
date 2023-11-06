import math
import numpy as np

import pygame

EDGE_COLLISION_DAMPING = 0.8

GRAVITY = 0.2

class Particle:
    """class to represent 2d circular particles"""

    def __init__(self, sim, pos, radius, elasticity) -> None:
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.elasticity = elasticity
        self.velocity = pygame.Vector2(0,0)
        self.mass = 1

        self.sim = sim

        self.edges = {'xmin':0, 'ymin':0, 'xmax':sim.display.get_width(), 'ymax':sim.display.get_height()}

    """getter and setter funcs to improve readability when referring to position and velocity"""
    @property
    def x(self):
        return self.pos[0]
    @x.setter
    def x(self, value):
        self.pos[0] = value
    @property
    def y(self):
        return self.pos[1]
    @y.setter
    def y(self, value):
        self.pos[1] = value
    @property
    def vel_x(self):
        return self.velocity[0]
    @x.setter
    def vel_x(self, value):
        self.velocity[0] = value
    @property
    def vel_y(self):
        return self.velocity[1]
    @y.setter
    def vel_y(self, value):
        self.velocity[1] = value

    def update(self):
        #gravity
        self.vel_y += GRAVITY

        #collision
        for particle2 in self.sim.particles:
            if self is particle2: continue

            squared_dist = ((self.x - particle2.x) ** 2 + (self.y - particle2.y) ** 2)
            if squared_dist < (self.radius + particle2.radius) ** 2:
                #snap
                angle = math.atan(abs(particle2.pos[0] - self.pos[0]) / abs(particle2.pos[1] - self.pos[1]))
                move_dist = (self.radius + particle2.radius) - math.sqrt(squared_dist)
                
                self.pos[0] += math.cos(angle) * move_dist / 2
                self.pos[1] += math.sin(angle) * move_dist / 2
                particle2.pos[0] -= math.cos(angle) * move_dist / 2
                particle2.pos[1] -= math.sin(angle) * move_dist / 2

        #apply velocity
        # checks edges only, other objects collide differently
        # else handles edge bounce
        if not (self.x + self.vel_x < self.edges['xmin'] or self.x + self.vel_x > self.edges['xmax']):    
            self.x += self.vel_x
        else:
            self.vel_x *= -1 * EDGE_COLLISION_DAMPING
        if not (self.y + self.vel_y < self.edges['xmin'] or self.y + self.vel_y > self.edges['ymax']):    
            self.y += self.vel_y
        else:
            self.vel_y *= -1 * EDGE_COLLISION_DAMPING
            
    def render(self, surf):
        pygame.draw.circle(surf, (255,255,255), self.pos, self.radius)