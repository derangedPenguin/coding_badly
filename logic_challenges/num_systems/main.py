import sys

import pygame

from bitmap import *

class Main:
    FPS = 60
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((960,640))
        self.map_display = pygame.Surface((640,640))

        self.bits = 0x0101010101010
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    ...
            
            self.screen.fill((0,0,0))

            render_bitmap(bin(self.bits), 8, 80, self.map_display, (0,0,125))

            self.screen.blit(self.map_display, (0,0))
            pygame.display.update()
            self.clock.tick(self.FPS)

Main().run()