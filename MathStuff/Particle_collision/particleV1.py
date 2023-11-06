import math
from typing import Any
import numpy as np

import pygame

INFLUENCE_RADIUS =  20

EDGE_COLLISION_DAMPING = 0.8

class Particle:
    """a class representing a 2d circular particle"""

    def __init__(self, sim, pos, radius, elasticity) -> None:
        self.sim = sim
        self.pos = list(pos)
        self.radius = radius
        self.velocity = pygame.Vector2(0,0)
        self.elasticity = elasticity
        self.mass = 1
    
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
    
    def update(self, dt):
        """runs motion and collision physics on particle"""
        #first attempt at applying velocity to frame movement
        '''if self.radius < self.x + self.vel_x < self.sim.display.get_width() - self.radius:
            self.x += self.velocity.x * dt
        else:
            #self.x = self.radius if self.x <= self.radius else self.sim.display.get_width() - self.radius
            self.vel_x *= -1 * EDGE_COLLISION_DAMPING
        self.vel_x += self.sim.hori_grav

        if self.radius < self.y + self.velocity.y < self.sim.display.get_height() - self.radius:
            self.y += self.velocity.y * dt
        else:
            #self.y = self.radius if self.y <= self.radius else self.sim.display.get_height() - self.radius
            self.vel_y *= -1 * EDGE_COLLISION_DAMPING
        self.vel_y += self.sim.vert_grav'''

        #general application of gravity, frame movement from velocity, and wall collisions
        if self.x <= self.radius:
            self.x = self.radius
            self.vel_x *= -1 * EDGE_COLLISION_DAMPING
        elif self.x >= self.sim.display.get_width() - self.radius:
            self.x = self.sim.display.get_width() - self.radius
            self.vel_x *= -1 * EDGE_COLLISION_DAMPING
        else:
            self.x += self.vel_x
        self.vel_x += self.sim.hori_grav

        if self.y <= self.radius:
            self.y = self.radius
            self.vel_y *= -1 * EDGE_COLLISION_DAMPING
        elif self.y >= self.sim.display.get_height() - self.radius:
            self.y = self.sim.display.get_height() - self.radius
            self.vel_y *= -1 * EDGE_COLLISION_DAMPING
        else:
            self.y += self.vel_y
        self.vel_y += self.sim.vert_grav

        #runs collision on other particles
        for particle in self.sim.particles:
            if self is particle or self.pos == particle.pos: # dont collide with self or particles in exact same pos
                continue
            squared_dist = (particle.x - self.x) ** 2 + (particle.y - self.y) ** 2
            if squared_dist < (self.radius + particle.radius) ** 2:
                #snap both particles to be non-intersecting before bounce calcs
                angle = math.atan(abs(particle.x - self.x) / abs(particle.y - self.y))
                move_dist = (self.radius + particle.radius) - math.sqrt(squared_dist)
                
                self.x += math.cos(angle) * move_dist / 2
                self.y += math.sin(angle) * move_dist / 2
                particle.x -= math.cos(angle) * move_dist / 2
                particle.y -= math.sin(angle) * move_dist / 2

                #print(f'velocity before: {sum(self.velocity)}')
                # adapted from internet source, works pretty well when i turn off snapping (but w/out snap, they will intersect and get stuck together)
                r1 = pygame.Vector2(self.pos)
                r2 = pygame.Vector2(particle.pos)
                total_mass = self.mass + particle.mass
                #avg_elasticity = (self.elasticity + particle.elasticity) / 2 -- would like to apply, if only i could do the math :/
                try:
                    u1 = self.velocity - 2*particle.mass / total_mass * pygame.Vector2.dot(self.velocity-particle.velocity, r1-r2) / squared_dist * (r1 - r2)
                    u2 = particle.velocity - 2*self.mass / total_mass * pygame.Vector2.dot(particle.velocity-self.velocity, r2-r1) / squared_dist * (r2 - r1)
                    self.velocity = u1
                    particle.velocity = u2
                except ZeroDivisionError:
                    self.x += self.radius
            
                #original bounce calcs, i understand a bit better, i think it worked too, but confuzzlement
                '''
                #bounce
                tan_vect = pygame.Vector2(-(particle.y - self.y), particle.x - self.x).normalize()
                rel_velocity = pygame.Vector2(particle.velocity.x - self.velocity.x, particle.velocity.y - self.velocity.y)
                length = pygame.Vector2.dot(rel_velocity, tan_vect)
                velocity_component_on_tan = tan_vect * length
                velocity_perp_to_tan = rel_velocity - velocity_component_on_tan

                avg_elasticity = (self.elasticity + particle.elasticity) / 2
                self.velocity.x -= velocity_perp_to_tan.x * avg_elasticity
                self.velocity.y -= velocity_perp_to_tan.y * avg_elasticity
                particle.velocity.x += velocity_perp_to_tan.x * avg_elasticity
                particle.velocity.y += velocity_perp_to_tan.y * avg_elasticity'''
                #print(f'velocity after: {sum(self.velocity)}')
                
    
    def render(self, surf):
        """Draws particle onto pygame Surface arg"""
        vel = abs(sum(self.velocity))
        scale = min(vel, 25.5) / 25.5
        #attempt at color change based on velocity
        try:
            color = (int(scale * 255), 0, int(255 - (scale * 255)))
        except ValueError:
            print(vel)
        #surf.set_at((int(self.x), int(self.y)), color)
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), self.radius)