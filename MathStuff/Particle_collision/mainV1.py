'''
resources include:
- https://flatredball.com/documentation/tutorials/math/circle-collision/
- https://github.com/xnx/collision/blob/master/collision.py
- https://ericleong.me/research/circle-circle/#dynamic-circle-circle-collision
'''
import sys

import pygame

from particleV1 import Particle

class Sim:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.display = pygame.Surface((640, 360))

        self.clock = pygame.time.Clock()
        self.dt = 0.0

        self.vert_grav = 20
        self.hori_grav = 0

        self.particles = []

    
    def run(self):
        while True:
            self.display.fill((0,0,0))

            for particle in self.particles:
                particle.update(self.dt)
                particle.render(self.display)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = (mouse_pos[0] // (self.screen.get_width() // self.display.get_width()), mouse_pos[1] // (self.screen.get_height() // self.display.get_height()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.particles.append(Particle(self, (mouse_pos[0], mouse_pos[1]), 5, 0.8))
                    if event.key == pygame.K_UP:
                        self.vert_grav -= 5
                    if event.key == pygame.K_DOWN:
                        self.vert_grav += 5
                    if event.key == pygame.K_RIGHT:
                        self.hori_grav += 5
                    if event.key == pygame.K_LEFT:
                        self.hori_grav -= 5
                    if event.key == pygame.K_r:
                        self.vert_grav = 20
                        self.hori_grav = 0
                        self.particles.clear()
            
            self.screen.blit(pygame.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height())), (0,0))
            pygame.display.update()
            self.dt = self.clock.tick(60) / 1000 #in milliseconds

Sim().run()