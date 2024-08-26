import math

import pygame as pg

from scripts.MagicBoard import MagicBoard, MagicBoard2
from scripts.Board import Board

NOTE_OFFSETS = {
    1:(0.2,0.2),2:(0.5,0.2),3:(0.8,0.2),
    4:(0.2,0.5),5:(0.5,0.5),6:(0.8,0.5),
    7:(0.2,0.8),8:(0.5,0.8),9:(0.8,0.8),
}

def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def draw_num(surf, text, center_pos, font:pg.font.Font, color=(30,50,150)):
    """draws a number"""
    text_render = font.render(str(text), True, color)
    rect = text_render.get_rect()
    rect.center = center_pos
    surf.blit(text_render,rect)

class GameBoard:
    """*incomplete* intended to store various board elements and handle all updating and rendering"""
    def __init__(self, size, margin) -> None:
        self.board = Board()
        # self.initial_board = Board()

        self.tile_width = math.ceil((size[0]-(margin*2))/9)
        self.margin = margin

        self.tile_rects = {
            (i//9,i%9):pg.Rect((i//9*self.tile_width) + self.margin + 1, (i%9*self.tile_width) + self.margin + 1, self.tile_width - 1 - ((i//9+1)%3==0)*3, self.tile_width - 1 - ((i%9+1)%3==0)*3) for i in range(81)
        }

        self.selected_tile = [0,0]

        self.num_font = pg.font.SysFont('sfnsmono', int(self.tile_width*0.65))
        self.note_font = pg.font.SysFont('sfnsmono', int(self.tile_width*0.25))
        self.note_font_bold = pg.font.SysFont('sfnsmono', int(self.tile_width*0.25), True)
    
    def screen_to_local(self, x_y):
        for pos, rect in self.tile_rects.items():
            if rect.collidepoint(x_y): return pos

    def gen_board(self):
        generator = MagicBoard()
        generator.fill_board()
        self.board = generator.board.copy()
        # self.initial_board = generator.board.copy()
    def drain_board(self):
        generator = MagicBoard()
        generator.board = self.board.copy()
        
        self.board = generator.drain_board()

    def gen_possibilities_at_selection(self):
        MagicBoard().gen_possibilities_at(self.selected_tile,self.board)
    def gen_all_notes(self):
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                MagicBoard.gen_possibilities_at((x,y), self.board)

    def shift_selection(self, dir):
        self.selected_tile[0] = clamp(self.selected_tile[0] + dir[0], 0, 8)
        self.selected_tile[1] = clamp(self.selected_tile[1] - dir[1], 0, 8)
    
    def set_tile(self, value, noting=False):
        if noting:
            self.board.set_note(value, self.selected_tile)
        else:
            self.board.set_tile(value, self.selected_tile)
        
    def render(self, surf, theme, debug=False):
        selected_num = self.board[self.selected_tile[0]][self.selected_tile[1]]

        for x in range(9):
            for y in range(9):
                value = self.board[x][y]
                #BACKGROUNDS
                pg.draw.rect(surface=surf,
                                 color=theme['selected_num_background'] if ([x,y] == self.selected_tile) else ( theme['affected_area_background'] if (x==self.selected_tile[0] or y==self.selected_tile[1] or self.board.get_box_coord((x,y))==self.board.get_box_coord(self.selected_tile)) else (theme['selected_num_type_background'] if (value == selected_num and selected_num != 0) else theme['num_background'])),
                                 rect=self.tile_rects[(x,y)]
                                 )
                #NUMBER
                if value == 0:
                    color = theme['note']
                    notes = self.board.get_notes_at(x,y)
                    for note in notes:
                        draw_num(surf=surf, 
                         text=note, 
                         center_pos=((x*self.tile_width) + self.margin + (NOTE_OFFSETS[note][0]*self.tile_width), (y*self.tile_width) + self.margin + (NOTE_OFFSETS[note][1]*self.tile_width)),
                         font=self.note_font_bold if note == selected_num else self.note_font,
                         color=theme['note_bold'] if note == selected_num else theme['note'],
                         )
                else:
                    color = theme['number']
                    if [x,y] == self.selected_tile:
                        color = theme['selected_num']
                    # if value != self.initial_board[x][y]:
                    #     color = theme['invalid_num']
                    # value = str(self.get_box((x,y)))
                    draw_num(surf=surf, 
                            text=value, 
                            center_pos=((x*self.tile_width) + self.margin + (self.tile_width/2), (y*self.tile_width) + self.margin + (self.tile_width/2)),
                            font=self.num_font,
                            color=color if self.board.is_val_valid_at_coord_in_place(value, (x,y)) else theme['invalid_num']
                            )