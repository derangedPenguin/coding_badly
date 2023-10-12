import pygame

class Tilemap:
    def __init__(self, game, tile_size=8) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}

        for i in range(10):
            self.tiles[str(i + 3) + ';10'] = True
            self.tiles['10;'+str(i + 5)] = True

    def render(self, surf, offset=(0,0)):
        for x in range(surf.get_width() // self.tile_size):
            for y in range(surf.get_height() // self.tile_size):
                print(x - offset[0], y - offset[1], self.tile_size, self.tile_size)
                if str(x) + ';' + str(y) in self.tiles:
                    pygame.draw.rect(surf, self.game.tile_colors['live'], pygame.Rect(x - offset[0], y - offset[1], self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(surf, self.game.tile_colors['dead'], pygame.Rect(x - offset[0] + 1, y - offset[1] + 1, self.tile_size, self.tile_size))
