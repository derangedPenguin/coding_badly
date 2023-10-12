import pygame

class Board:
    def __init__(self, game, dims, tile_size) -> None:
        self.width = dims[0]
        self.height = dims[1]
        self.tile_size = tile_size
        self.game = game

        self.tiles = [
            {i:0 for i in range(self.width)} for j in range(self.height)
        ]

    def clear(self):
        self.tiles = [
            {i:0 for i in range(self.width)} for j in range(self.height)
        ]
    
    def render(self, surf):
        for y_cor in range(len(self.tiles)):
            for x_cor in self.tiles[y_cor]:
                state = self.tiles[y_cor][x_cor]
                if state == 0:
                    continue
                surf.blit(self.game.assets[state], (x_cor * self.tile_size, y_cor * self.tile_size))