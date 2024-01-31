import math

import pygame

from scripts.board_gen import MagicBoard

def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def draw_num(surf, text, center_pos, font_size=48, color=(30,50,150)):
    """draws a number"""

    font = pygame.font.SysFont('San Francisco', int(font_size))
    text_render = font.render(str(text), True, color)
    rect = text_render.get_rect()
    rect.center = center_pos
    surf.blit(text_render,rect)

class Board:
    """*incomplete* intended to store various board elements and handle all updating and rendering"""
    def __init__(self, size, margin) -> None:
        self.board = [[1 for x in range(9)] for y in range(9)]

        self.tile_width = math.ceil((size[0]-(margin*2))/9)
        self.margin = margin

        self.selected_tile = [0,0]
    
    def __getitem__(self, item):
        return self.board[item]
    def __setitem__(self, key, value):
        self.board[key] = value

    def gen_board(self):
        generator = MagicBoard()
        generator.fill_board()
        self.board = generator.board.copy()
    def prep_board(self):
        generator = MagicBoard()
        generator.board = self.board.copy()
        generator.setup_board()
        self.board = generator.board.copy()

    def shift_selection(self, dir):
        self.selected_tile[0] = clamp(self.selected_tile[0] + dir[0], 0, 8)
        self.selected_tile[1] = clamp(self.selected_tile[1] - dir[1], 0, 8)
    
    def set_tile(self, value):
        self[self.selected_tile[0]][self.selected_tile[1]] = value
        
    def render(self, surf, theme):
        selected_num = self.board[self.selected_tile[0]][self.selected_tile[1]]

        for x in range(9):
            for y in range(9):
                value = self[x][y]
                #BACKGROUND
                color = ()
                pygame.draw.rect(surface=surf,
                                 color=theme['selected_num_background'] if ([x,y] == self.selected_tile) else theme['num_background'],
                                 rect=((x*self.tile_width) + self.margin + 1, (y*self.tile_width) + self.margin + 1, self.tile_width - 1 - ((x+1)%3==0)*3, self.tile_width - 1 - ((y+1)%3==0)*3)
                                 )
                #NUMBER
                color = theme['numbers']
                if value == 0:
                    color = theme['invalid_num']
                if [x,y] == self.selected_tile:
                    color = theme['selected_num']
                draw_num(surf=surf, 
                         text=value, 
                         center_pos=((x*self.tile_width) + self.margin + (self.tile_width/2), (y*self.tile_width) + self.margin + (self.tile_width/2)),
                         font_size=self.tile_width*0.8,
                         color=color
                         )