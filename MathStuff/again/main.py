from sys import exit
import pygame as pg

from particle import *
from collideable import *

class Main:

    FPS = 60

    def __init__(self) -> None:
        # Pygame Inits
        pg.init()
        self.window = pg.display.set_mode((960,640), vsync=True, flags=pg.RESIZABLE)
        self.clock = pg.time.Clock()

        # My Inits
        self.display = pg.Surface(self.window.get_size())

        self.border = Border((0,0), *self.display.get_size(), 0.8)

        self.particles = set()

        self.slow_mode = False

    def run(self):
        while True:
            # Event Loop
            for event in pg.event.get():
                # Quit
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
                # Keydowns
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.slow_mode = not self.slow_mode
                
                # Keyups
                if event.type == pg.KEYUP:
                    pass
                
                # Mousedowns
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.particles.add(Particle(pg.mouse.get_pos(), 10, self.border))

                # Mouseups
                if event.type == pg.MOUSEBUTTONUP:
                    pass
            # Updates
            self.display.fill((0,0,0))
            
            for particle in self.particles:
                particle.check_collisions(self.particles)
                particle.update()
                particle.draw(self.display)
                
            # Display & Pygame Updates
            self.window.blit(self.display, (0,0))
            pg.display.update()
            self.clock.tick(self.FPS / (self.slow_mode + 1))

if __name__ == '__main__':
    Main().run()