import pygame

import json

from typing import Self

SURROUNDING_OFFSETS = {
            (-1,-1):False,(0,-1):False,(1,-1):False,
            (-1,0):False,             (1,0):False,
            (-1,1):False,(0,1):False,(1,1):False,
        }

BORDER_SIZE = 1

class Tilemap:
    def __init__(self, game, tile_size=8) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}

        self.establish_edges()
    
    def __getitem__(self, key):
        return self.tiles.get(key, False)
    
    def __setitem__(self, key, value):
        self.tiles[key] = value

    def export_tiles(self, filename):
        with open(f'data/stored_maps/{filename}.json', 'w') as file:
            file.write(json.dumps(self.tiles))
    def import_tiles(self, filename):
        with open(f'data/stored_maps/{filename}.json', 'r') as file:
            self.tiles = json.load(file)
        self.establish_edges()
    
    def copy(self, include_tiles: bool = True) -> Self:
        board = Tilemap(self.game, self.tile_size)
        if include_tiles:
            board.tiles = self.tiles.copy()
        else:
            board.tiles = {}
        return board
    
    def add_tile(self, coord: str | tuple):
        if type(coord) is str:
            self.tiles[coord] = True
        else:
            self.tiles[str(coord[0])+';'+str(coord[1])] = True
    def rem_tile(self, coord: str | tuple):
        try:
            if type(coord) is str:
                del self.tiles[coord]
            else:
                    del self.tiles[str(coord[0])+';'+str(coord[1])]
        except KeyError:
            pass

    def get_surrounding(self, tile_coord):
        surrounding = SURROUNDING_OFFSETS.copy()
        for offset in surrounding:
            off_loc_string = f'{tile_coord[0]+offset[0]};{tile_coord[1]+offset[1]}'
            if self.tiles.get(off_loc_string, False):
                surrounding[offset] = True
        return surrounding
        
    def establish_edges(self):
        """
        find outermost defined edges.

        loops through all tiles, don't run repeatedly.
        """
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        for tile in self.tiles:
            x, y = [int(i) for i in tile.split(';')]
            if x < self.left:
                self.left = x
            elif x > self.right:
                self.right = x
            if y < self.top:
                self.top = y
            elif y > self.bottom:
                self.bottom = y
        #print(f'{self.left}\n{self.right}\n{self.top}\n{self.bottom}\n\n')
    
    def check_edge_change(self, tile: tuple[int, int]):
        """checks if argument tile extends edges of board"""
        x, y = tile
        if x < self.left:
            self.left = x
        elif x > self.right:
            self.right = x
        if y < self.top:
            self.top = y
        elif y > self.bottom:
            self.bottom = y
    
    def increment(self, updator):
        self.tiles = updator.mono_board_update().tiles

    def render(self, surf: pygame.Surface, offset: tuple[int, int]=(0,0)):
        """render"""
        """for grid_x, screen_x in enumerate(range(0, surf.get_width(), self.tile_size+1)):
            for grid_y, screen_y in enumerate(range(0, surf.get_height(), self.tile_size+1)):
                grid_x, grid_y = grid_x+offset[0], grid_y+offset[1]#grid_x+(offset[0]//(self.tile_size+1)), grid_y+(offset[1]//(self.tile_size+1))
                if str(grid_x)+';'+str(grid_y) in self.tiles.keys():
                    pygame.draw.rect(surf, (0,0,0), pygame.Rect((screen_x, screen_y, self.tile_size, self.tile_size)))
                else:
                    pygame.draw.rect(surf, (255,255,255), pygame.Rect((screen_x, screen_y, self.tile_size, self.tile_size)))"""
        TTW = self.tile_size+BORDER_SIZE
        #start at first tile--occurs before screen edge-end at screen edge at farthest, increment by total tile width
        for grid_x, screen_x in enumerate(range(-offset[0]//self.tile_size, surf.get_width(), TTW)):
            for grid_y, screen_y in enumerate(range(-offset[1]//self.tile_size, surf.get_height(), TTW)):
                grid_x, grid_y = grid_x + (offset[0]//TTW), grid_y + (offset[1]//TTW)
                if self[f'{grid_x};{grid_y}']:
                    pygame.draw.rect(surf, (0,0,0), pygame.Rect((screen_x, screen_y, self.tile_size, self.tile_size)))
                else:
                    pygame.draw.rect(surf, (255,255,255), pygame.Rect((screen_x, screen_y, self.tile_size, self.tile_size)))
