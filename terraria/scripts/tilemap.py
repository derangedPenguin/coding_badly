import json

import pygame

NEIGHBOR_OFFSETS = [(-1,-1),(0,-1),(1,-1),(2,-1),
                   (-1,0),(0,0),(1,0),(2,0),
                   (-1,1),(0,1),(1,1),(2,1),
                   (-1,2),(0,2),(1,2),(2,2),
                   (-1,3),(0,3),(1,3),(2,3)]

PHYSICS_TILES = {'0'}

class Tilemap:
    def __init__(self, game, tile_size=24) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        #self.new_world(self.game)
        for i in range(len(tiles := self.game.assets['0'])):
            self.tilemap[str(i + (2*i)) + ';10'] = {'id':'0','variant':i,'pos':[i + (2*i), 10]}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['id'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def render(self, surf, cam_offset=(0,0)):
        for x in range(cam_offset[0] // self.tile_size, (cam_offset[0] + surf.get_width()) // self.tile_size + 1):
            for y in range(cam_offset[1] // self.tile_size, (cam_offset[1] + surf.get_height()) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['id']][tile['variant']], (tile['pos'][0] * self.tile_size - cam_offset[0], tile['pos'][1] * self.tile_size - cam_offset[1]))

    def new_world(self, game):
        for x in range(-50,50):
            for y in range(10,20):
                self.tilemap[str(x) + ';' + str(y)] = {'id':'0','variant':76,'pos':[x, y]}
            for y in range(20,40):
                self.tilemap[str(x) + ';' + str(y)] = {'id':'0','variant':1,'pos':[x, y]}