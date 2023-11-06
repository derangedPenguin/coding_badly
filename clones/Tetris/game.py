import sys
import numpy as np
import random

import pygame

from scripts.board import Board
from scripts.tile import FallingTile
from scripts.utils import load_image, shift_col
from scripts.text import TextBox

BOARD_DIMS = (10, 20)

SPEED_MOD = 6

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((960, 640))
        self.board_display = pygame.Surface((320,640))

        self.rng = np.random.default_rng(10)
        self.rng.random()

        self.tetrominoes = {'I':((0,0),(1,0),(2,0),(3,0)),
               'O':((0,0),(1,0),(0,1),(1,1)),'T':((-1,0),(0,0),(1,0),(0,1)),
               'L':((0,0),(0,1),(0,2),(1,2)),'J':((1,0),(1,1),(1,2),(0,2)),
               'S':((0,0),(1,0),(0,1),(-1,1)),'Z':((0,0),(1,0),(1,1),(1,2))}
        self.ttm_colors = {'I':(0,255,255),'O':(255,255,0),'T':(127,255,0),'L':(255,127,0),'J':(0,0,255),'S':(0,255,0),'Z':(255,0,0)}

        self.assets = {
            0:load_image('gray.png', scale=(4,4)), #gray
        }
        for shape in self.tetrominoes:
            self.assets[shape] = shift_col(self.assets[0], self.ttm_colors[shape])#(255*self.rng.random(), 255*self.rng.random(), 255*self.rng.random()))

        self.board = Board(self, BOARD_DIMS, 32)

        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), random.choice(list(self.tetrominoes.keys())))

        self.keys_held = {'left':False,'right':False,'down':False}

        self.text_area = TextBox((640,240), {'thing':{'offset':(0,0),'text':''}})
    
    def new_tile(self):
        #prev_speed = self.active_tile.speed
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), random.choice(list(self.tetrominoes.keys())), speed=self.active_tile.speed*1.02)
        self.active_tile.speed_mod = self.keys_held['down'] * SPEED_MOD
    
    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.board_display.fill((20,20,20))

            self.board.render(self.board_display)
            #draw info
            self.text_area.update({'thing':{'text':f'speed: {self.active_tile.speed}'}})

            if self.keys_held['left']:
                self.active_tile.timed_shift(-1)
            elif self.keys_held['right']:
                self.active_tile.timed_shift(1)

            kill = self.active_tile.update()
            self.active_tile.render(self.board_display)
            if kill:
                self.new_tile()
            
            self.board.check_filled()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.start_timer('left')
                        self.keys_held['left'] = True
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.start_timer('right')
                        self.keys_held['right'] = True
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = True
                        self.active_tile.speed_mod = SPEED_MOD
                if event.type == pygame.KEYUP:
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.reset_timer('left')
                        self.keys_held['left'] = False
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.reset_timer('right')
                        self.keys_held['right'] = False
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = False
                        self.active_tile.speed_mod = 0

            self.screen.blit(self.board_display, (self.screen.get_width()/2-self.board_display.get_width()/2,0))
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()
