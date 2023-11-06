import sys
import random

import pygame

from scripts.board import Board
from scripts.tile import FallingTile
from scripts.utils import load_image
from scripts.constructor import Polymino_Set

BOARD_DIMS = (10, 20)

NUM_OF_TILES = 2

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((960, 640))
        self.board_display = pygame.Surface((320,640))

        self.assets = {
            0:load_image('dead.png', scale=(4,4)),
            1:load_image('0.png', scale=(4,4))
        }

        self.board = Board(self, BOARD_DIMS, 32)

        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), 1)
    
    def new_tile(self, type: int | None = None):
        if type is None:
            final_type = random.randint(1,NUM_OF_TILES)
        else:
            final_type = type
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, self.board.height//2), final_type)
    
    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.board_display.fill((20,20,20))

            self.board.render(self.board_display)

            mouse_pos = pygame.mouse.get_pos()
            

            kill = self.active_tile.update()
            self.active_tile.render(self.board_display)
            if kill:
                self.new_tile()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print('pressed')
                        if self.board_display.get_bounding_rect().collidepoint(mouse_pos):
                            self.board[mouse_pos[1]/self.board.tile_size][mouse_pos[0]/self.board.tile_size] = 1

                if event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.shift((-1,0))
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.shift((1,0))
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.active_tile.shift((0,1))
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.active_tile.shift((0,-1))
                    if event.key == pygame.K_f:
                        self.active_tile.freeze()
                    if event.key == pygame.K_c:
                        self.new_tile((self.active_tile.type + 1) % NUM_OF_TILES)

            self.screen.blit(self.board_display, (self.screen.get_width()/2-self.board_display.get_width()/2,0))
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()
