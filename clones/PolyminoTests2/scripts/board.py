from typing import Any
import pygame
import json


class Board:
    def __init__(self, game, dims, tile_size) -> None:
        self.width = dims[0]
        self.height = dims[1]
        self.tile_size = tile_size
        self.game = game

        self.tiles = {
            j:{i:0 for i in range(self.width)} for j in range(-1,self.height)
        }
    
    def __getitem__(self, item) -> Any:
        return self.tiles[item]

    def clear(self): #creates a new empty board
        self.tiles = {
            j:{i:0 for i in range(self.width)} for j in range(-1,self.height)
        }
    
    def check_filled(self):
        #check and move full rows
        for row in self.tiles:
            if all(self.tiles[row].values()): # if all values are 1
                self.game.score += 1
                for row_ in range(row, 0, -1):
                    self.tiles[row_] = self.tiles[row_-1].copy()
        #check for any items in top row
        if any(self.tiles[0].values()):
            #lose
            return True #self.clear()
    
    def render(self, surf):
        #print(json.dumps(self.tiles, indent=4))
        for y_cor in self.tiles:
            for x_cor in self.tiles[y_cor]:
                state = self.tiles[y_cor][x_cor]
                if state == 0:
                    continue
                surf.blit(self.game.assets[state], (x_cor * self.tile_size, y_cor * self.tile_size))