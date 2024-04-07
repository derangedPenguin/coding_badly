import pygame as pg
import numpy as np
import typing

from collideable import *

def sqaured_dist(point1:typing.Sequence[float],point2:typing.Sequence[float]):
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

class Particle:

    GRAVITY = 0.3

    mass = 1

    def __init__(self, pos:typing.Sequence[float], radius:int, border:Border, color:tuple[int]=(255,255,255)) -> None:
        self.color = color
        self.pos = np.array([float(i) for i in pos])
        self.radius = radius
        self.border = border
        self.velocity = np.array((0.0,0.0))
    
    @property
    def x(self):
        return self.pos[0]
    @x.setter
    def x(self, val):
        self.pos[0] = val

    @property
    def y(self):
        return self.pos[1]
    @y.setter
    def y(self, val):
        self.pos[1] = val
    
    @property
    def vx(self):
        return self.velocity[0]
    @vx.setter
    def vx(self, val):
        self.velocity[0] = val

    @property
    def vy(self):
        return self.velocity[1]
    @vy.setter
    def vy(self, val):
        self.velocity[1] = val

    def update(self):
        # apply gravity
        self.vy += self.GRAVITY

        # position to check collision with
        new_pos = self.pos + self.velocity

        # Handle border collisions (elastic)
        if self.radius > new_pos[0]:
            new_pos[0] = 0
            self.vx *= -self.border.elasticity
        if self.border.width - self.radius < new_pos[0]:
            new_pos[0] = self.border.width
            self.vx *= -1

        if self.radius > new_pos[1]:
            new_pos[1] = 0
            self.vy *= -self.border.elasticity
        if self.border.height + self.radius < new_pos[1]:
            new_pos[1] = self.border.height
            self.vy *= -self.border.elasticity
        
        # Apply motion
        self.pos = new_pos
    
    def check_collisions(self, other_particles:typing.Collection[typing.Self]):
        #check all given particles
        for oth_p in other_particles:
            #dont collide with self
            if oth_p is self: continue
            #explode if in same pos
            #if oth_p.pos == self.pos: print('explosion')
            #check collision
            sq_dist = sqaured_dist(self.pos, oth_p.pos)
            if sq_dist <= (self.radius + oth_p.radius)**2:
                #handle collision
                self.color = (255,0,0)

                ##Snap apart
                goal_dist = self.radius + oth_p.radius # how far apart should they be
                snap_distance = (goal_dist - np.sqrt(sq_dist)) / 2 # how far does each need to move to not intersect
                angle = np.tan( abs(self.y - oth_p.y) / abs(self.x - oth_p.x) ) # angle of the line between their centerpoints

                shift = np.array((np.cos(angle), np.sin(angle))) # x and y shift to apply to each circle

                self.pos += shift * snap_distance
                oth_p.pos -= shift * snap_distance

                ##Transfer velocity
                mass1, mass2 = self.mass, oth_p.mass
                M = mass1 + mass2
                r1, r2 = self.radius, oth_p.radius
                d = np.linalg.norm(r1 - r2)**2
                v1, v2 = self.velocity, oth_p.velocity
                u1 = v1 - 2*mass2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
                u2 = v2 - 2*mass1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
                self.velocity = u1
                oth_p.velocity = u2


    def draw(self, surf:pg.Surface):
        pg.draw.circle(surf, self.color, self.pos, self.radius)