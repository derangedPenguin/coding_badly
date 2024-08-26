import pygame as pg

class Board:

    TILE_COLORS = ((240,240,220),(30,30,40)) #Ivory & very dark brown

    WIDTH = 8

    def __init__(self, board_size_px) -> None:
        self.tw = self.tile_width = board_size_px/self.WIDTH

        self.assets = {
            'pawn': load_image(),
            # 'bishop',
            # 'rook',
            # 'knight',
            # 'queen',
            # 'king'
        }

    def render(self, surf, offset):
        for y in range(self.WIDTH):
            for x in range(self.WIDTH):
                pg.draw.rect(surf,self.TILE_COLORS[((y+x)%2)-1], (y*self.tw, x*self.tw, self.tw, self.tw))