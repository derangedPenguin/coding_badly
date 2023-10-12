import math

import pygame

INFLUENCE_RADIUS =  20

EDGE_COLLISION_DAMPING = 0.8

class Particle:
    def __init__(self, sim, pos, radius, elasticity) -> None:
        self.sim = sim
        self.pos = list(pos)
        self.radius = radius
        self.velocity = pygame.Vector2(0,0)
        self.elasticity = elasticity
    
    def update(self):
        if 0 < self.pos[0] + self.velocity[0] < self.sim.display.get_width():
            self.pos[0] += self.velocity.x
        else:
            self.velocity[0] *= -1 * EDGE_COLLISION_DAMPING
        self.velocity[0] += self.sim.hori_grav

        if 0 < self.pos[1] + self.velocity.y < self.sim.display.get_height():
            self.pos[1] += self.velocity.y
        else:
            #self.pos[1] = (self.sim.display.get_height() - self.radius) if 
            self.velocity[1] *= -1 * EDGE_COLLISION_DAMPING
        self.velocity[1] += self.sim.vert_grav

        for particle in self.sim.particles:
            if self is particle:
                continue
            squared_dist = (particle.pos[0] - self.pos[0]) ** 2 + (particle.pos[1] - self.pos[1]) ** 2
            if squared_dist < (self.radius + particle.radius) ** 2:
                #snap
                angle = math.atan(particle.pos[0] - self.pos[0] / particle.pos[1] - self.pos[1])
                move_dist = (self.radius + particle.radius) - math.sqrt(squared_dist)

                self.pos[0] += math.cos(angle) * move_dist / 2
                self.pos[1] += math.sin(angle) * move_dist / 2
                particle.pos[0] -= math.cos(angle) * move_dist / 2
                particle.pos[1] -= math.sin(angle) * move_dist / 2
                
                #bounce
                tan_vect = pygame.Vector2(-(particle.pos[1] - self.pos[1]), particle.pos[0] - self.pos[0]).normalize()
                rel_velocity = pygame.Vector2(particle.velocity.x - self.velocity.x, particle.velocity.y - self.velocity.y)
                length = pygame.Vector2.dot(rel_velocity, tan_vect)
                velocity_component_on_tan = tan_vect * length
                velocity_perp_to_tan = rel_velocity - velocity_component_on_tan

                avg_elasticity = (self.elasticity + particle.elasticity) / 2
                self.velocity.x -= velocity_perp_to_tan.x * avg_elasticity
                self.velocity.y -= velocity_perp_to_tan.y * avg_elasticity
                particle.velocity.x += velocity_perp_to_tan.x * avg_elasticity
                particle.velocity.y += velocity_perp_to_tan.y * avg_elasticity
                
    
    def render(self, surf):
        avg_velocity = abs(self.velocity[0] + self.velocity[1]) // 2
        color = (max(avg_velocity + 255 // 255, 255), 0, max(abs(avg_velocity - 255 // 255), 255))
        #surf.set_at((int(self.pos[0]), int(self.pos[1])), color)
        pygame.draw.circle(surf, (255,255,255), (int(self.pos[0]), int(self.pos[1])), self.radius)