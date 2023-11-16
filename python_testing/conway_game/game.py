import sys

import pygame

from scripts.tilemap import Tilemap

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640,480))

        self.offset = [0,0]
        
        self.live_color = (0,0,0)

        self.tilemap = Tilemap(self, tile_size=8)

        self.tile_colors = {
            'dead':(255,255,255),
            'live':(0,0,0)
        }

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            self.tilemap.render(self.screen, offset=(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
            
            self.clock.tick(60)

Game().run()