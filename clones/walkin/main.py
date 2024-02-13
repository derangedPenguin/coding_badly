import sys

import pygame

from scripts.Tilemap import *
from scripts.Character import *
from scripts.utils import *
from scripts.Player import *
from scripts.NPCs import *

class Game:
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

        self.player:Player = self.tilemap.load_player_data()

        self.tilemap.load_tile_data()

        self.held_keys = {
            'up':False,
            'left':False,
            'down':False,
            'right':False,
            'shift':False,
        }
    
    def run(self):
        '''do everything'''
        while True:
            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.held_keys['up'] = True
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.held_keys['left'] = True
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.held_keys['down'] = True
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.held_keys['right'] = True
                    if event.key in {pygame.K_LSHIFT}:
                        self.held_keys['shift'] = True
                
                if event.type == pygame.KEYUP:
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.held_keys['up'] = False
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.held_keys['left'] = False
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.held_keys['down'] = False
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.held_keys['right'] = False
                    if event.key in {pygame.K_LSHIFT}:
                        self.held_keys['shift'] = False

            #frame updates
            self.screen.fill((0,0,0))

            self.tilemap.render(self.screen, self.player.get_px_pos())

            for char in self.chars:
                char.update1()
                char.render(self.screen, self.player.get_px_pos())

            
            #update player motion, handling keyboard inputs
            if self.held_keys['shift']:
                self.player.speed_mult = 2
            else:
                self.player.speed_mult = 1
            
            if self.held_keys['up']:
                self.player.move((0,1))
            if self.held_keys['left']:
                self.player.move((-1,0))
            if self.held_keys['down']:
                self.player.move((0,-1))
            if self.held_keys['right']:
                self.player.move((1,0))
            
            self.player.update_motion(keys=self.held_keys)

            self.player.render(self.screen)

            #screen update and ticks
            pygame.display.update()
            self.clock.tick(self.FPS)

Game().run()