import sys

import pygame

from scripts.Tilemap import *
from scripts.characters import *
from scripts.utils import *

class Game:
    '''does everything'''
    #Consts
    FPS = 60

    TILEMAP_PATH = 'data/maps/map.json'

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((960,640))
        self.clock = pygame.time.Clock()

        self.tilemap = Tilemap(self)
        self.tilemap.import_tilemap(self.TILEMAP_PATH)

        self.chars:list[NPC] = self.tilemap.load_chars_data()

        self.player = self.tilemap.load_player_data()

        self.tilemap.load_tile_data()
    
    def run(self):
        '''do everything'''
        while True:
            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move((0,1))
                    if event.key == pygame.K_a:
                        self.player.move((-1,0))
                    if event.key == pygame.K_s:
                        self.player.move((0,-1))
                    if event.key == pygame.K_d:
                        self.player.move((1,0))

            #frame updates
            self.screen.fill((0,0,0))

            self.tilemap.render(self.screen, self.player.world_pos)

            for char in self.chars:
                char.update1()
                char.render(self.screen, self.player.world_pos)

            self.player.render(self.screen)

            #screen update and ticks
            pygame.display.update()
            self.clock.tick(self.FPS)

Game().run()