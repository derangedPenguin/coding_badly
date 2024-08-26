import sys

import pygame as pg

from scripts.GameBoard import GameBoard
from scripts.gui import GUI

THEMES = {
    "light":{},
    "dark":{
        # "board_background":(30,30,30),
        "gui_background":(60,60,60),
        # "borders":(30,30,30),
        "number":(160,160,160),
        "selected_num":(40,60,200),
        "invalid_num":(200,0,0),
        "num_background":(60,60,60),
        "selected_num_background":(90,90,90),
        "selected_num_type_background":(75,75,75),
        "note":(120,120,120)
    },
    "sunset":{
        # "board_background":(220,200,180),
        "gui_background":(220,215,190),
        # "borders":(220,200,180),
        "number":(80,80,80),
        "selected_num":(40,60,200),
        "invalid_num":(200,0,0),
        "num_background":(220,215,190),
        "selected_num_background":(180,170,150),
        "selected_num_type_background":(170,160,140),
        "affected_area_background":(200,190,170),
        "note":(80,80,80),
        "note_bold":(0,0,0)
    } 
}

class Game:
    def __init__(self) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        self.FRAMERATE = 60

        #PGScreen's size must be (x,y) where x > y by a decent amount ~5/4ths
        self.PGScreen = pg.display.set_mode((960,640), pg.HWSURFACE|pg.DOUBLEBUF)
        self.board_screen = pg.Surface((self.PGScreen.get_height(), self.PGScreen.get_height()))
        self.GUI_screen = pg.Surface((self.PGScreen.get_width()-self.PGScreen.get_height(), self.PGScreen.get_height()))

        self.theme = THEMES["sunset"]
        
        self.board = GameBoard(self.board_screen.get_size(), 10)
        self.GUI = GUI(
            note_label={
                'type':'label','prefix':'Notes: ','pos':(40,40),'text_args':{'color':self.theme['number']},'updatable':lambda:(self.noting_enabled)
                }   
        )

        self.noting_enabled = False

        self.frames = 0


    def run(self):
        while True:
            self.board.render(self.board_screen, self.theme, not self.frames)
            self.GUI_screen.fill(self.theme["gui_background"])

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

                    if event.key == pg.K_LEFT:
                        self.board.shift_selection((-1,0))
                    if event.key == pg.K_UP:
                        self.board.shift_selection((0,1))
                    if event.key == pg.K_RIGHT:
                        self.board.shift_selection((1,0))
                    if event.key == pg.K_DOWN:
                        self.board.shift_selection((0,-1))
                    
                    if event.key == pg.K_1:
                        self.board.set_tile(1, self.noting_enabled)
                    if event.key == pg.K_2:
                        self.board.set_tile(2, self.noting_enabled)
                    if event.key == pg.K_3:
                        self.board.set_tile(3, self.noting_enabled)
                    if event.key == pg.K_4:
                        self.board.set_tile(4, self.noting_enabled)
                    if event.key == pg.K_5:
                        self.board.set_tile(5, self.noting_enabled)
                    if event.key == pg.K_6:
                        self.board.set_tile(6, self.noting_enabled)
                    if event.key == pg.K_7:
                        self.board.set_tile(7, self.noting_enabled)
                    if event.key == pg.K_8:
                        self.board.set_tile(8, self.noting_enabled)
                    if event.key == pg.K_9:
                        self.board.set_tile(9, self.noting_enabled)
                    if event.key in {pg.K_DELETE, pg.K_BACKSPACE, pg.K_0}:
                        self.board.set_tile(0, self.noting_enabled)
                    
                    if event.key == pg.K_z:
                        self.board.gen_board()
                        self.frames = -1
                    if event.key == pg.K_x:
                       self.board.drain_board()
                    if event.key == pg.K_c:
                       self.board.gen_all_notes()
                    
                    if event.key == pg.K_n:
                        self.noting_enabled = not self.noting_enabled
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1: #l click
                        mouse_pos = pg.mouse.get_pos()
                        board_pos = self.board.screen_to_local(mouse_pos)
                        if board_pos:
                            self.board.selected_tile = list(board_pos)
            
            self.frames += 1

            self.GUI.render(self.GUI_screen)

            
            
            self.PGScreen.blit(self.board_screen, (0,0))
            self.PGScreen.blit(self.GUI_screen, (self.PGScreen.get_height(),0))
            pg.display.update()
            self.clock.tick(self.FRAMERATE)

Game().run()