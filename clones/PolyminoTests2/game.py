import sys
import random

import pygame

from scripts.board import Board
from scripts.tile import FallingTile
from scripts.utils import load_image, shift_col

BOARD_DIMS = (10, 20)

SPEED_MOD = 4

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((960, 640))
        self.board_display = pygame.Surface((320,640))

        self.minoes = []

        self.assets = {
            'circle':load_image('circle.png', scale=(1,1), shift_col=(254,254,254), set_alpha=125),
            0:load_image('gray.png', scale=(4,4)), #gray
        }
        for shape in self.minoes:
            self.assets[shape] = shift_col(self.assets[0].copy(), self.ttm_colors[shape])#(255*self.rng.random(), 255*self.rng.random(), 255*self.rng.random()))

        self.board = Board(self, BOARD_DIMS, 32)

        self.keys_held = {'left':False,'right':False,'down':False, 'shift':False}

        self.new_game()

    def new_game(self):
        self.board.clear()
        self.time_played = 0
        self.new_tile()
    
    def new_tile(self):
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 5), self.minoes.index(self.active_tile.shape_id)+1, speed=1)

    def run(self):
        while True:
            self.screen.fill((200,200,200))
            self.board_display.fill((220,220,220))

            self.board.render(self.board_display)

            #handle held movement inputs
            if self.keys_held['left']:
                self.active_tile.timed_shift(-1)
            elif self.keys_held['right']:
                self.active_tile.timed_shift(1)

            #update and render current falling tile
            kill = self.active_tile.update()
            self.active_tile.render(self.board_display)
            if kill:
                self.new_tile() 

            #event loop for input handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.shift((-1,0))
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.shift((1,0))
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.active_tile.shift((0,1))
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.active_tile.shift((0,-1))
                    if event.key == pygame.K_r:
                        self.active_tile.rotate(not self.keys_held['shift'])
                    if event.key == pygame.K_SPACE:
                        self.cycle_tile()
                    if event.key in {pygame.K_LSHIFT, pygame.K_RSHIFT}:
                        self.keys_held['shift'] = True

                if event.type == pygame.KEYUP:
                    if event.key in {pygame.K_LSHIFT, pygame.K_RSHIFT}:
                        self.keys_held['shift'] = True


            self.screen.blit(self.board_display, (self.screen.get_width()/2-self.board_display.get_width()/2,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
