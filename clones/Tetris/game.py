import sys

import pygame

from scripts.board import Board
from scripts.tile import FallingTile
from scripts.utils import load_image

BOARD_DIMS = (10, 20)

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
    
    def new_tile(self):
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), 1)
    
    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.board_display.fill((20,20,20))

            self.board.render(self.board_display)

            kill = self.active_tile.update()
            self.active_tile.render(self.board_display)
            if kill:
                self.new_tile()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.board_display, (320,0))
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()
