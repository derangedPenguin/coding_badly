import pygame as pg

class GamePiece:
    def __init__(self, board_pos, type:str) -> None:
        self.board_pos = list(board_pos) #x,y coords w/ origin at bot-left for white
        self.screen_pos = [0,0]
        self.type = type