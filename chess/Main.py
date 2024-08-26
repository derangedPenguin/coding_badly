import pygame as pg
import numpy as np
import sys

from scripts.Board import Board

class Main:

    FPS = 60

    SCREEN_SIZE = (920,640)

    BOARD_SIZE_PX = (640,640)

    BACKGROUND_COLOR = (60,60,60)

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(self.SCREEN_SIZE, flags=pg.RESIZABLE)
        self.clock = pg.time.Clock()

        self.board_surf = pg.Surface(self.BOARD_SIZE_PX)
        self.cam_pos = [(self.screen.get_width()-self.board_surf.get_width())/2,0]

        self.board = Board(self.BOARD_SIZE_PX[0])

        self.pressed_keys = {
            'left':False,
            'right':False,
            'up':False,
            'down':False,
        }
    
    def run(self):
        while True:
            '''Inputs'''
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.pressed_keys['left'] = True
                    if event.key == pg.K_RIGHT:
                        self.pressed_keys['right'] = True
                    if event.key == pg.K_UP:
                        self.pressed_keys['up'] = True
                    if event.key == pg.K_DOWN:
                        self.pressed_keys['down'] = True
                
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.pressed_keys['left'] = False
                    if event.key == pg.K_RIGHT:
                        self.pressed_keys['right'] = False
                    if event.key == pg.K_UP:
                        self.pressed_keys['up'] = False
                    if event.key == pg.K_DOWN:
                        self.pressed_keys['down'] = False
            '''Logic'''
            if self.pressed_keys['left']:
                self.cam_pos[0] -= 10
            if self.pressed_keys['up']:
                self.cam_pos[1] -= 10
            if self.pressed_keys['right']:
                self.cam_pos[0] += 10
            if self.pressed_keys['down']:
                self.cam_pos[1] += 10

            '''Rendering'''

            self.screen.fill(self.BACKGROUND_COLOR)

            self.board.render(self.board_surf, self.cam_pos)
            
            self.screen.blit(self.board_surf, self.cam_pos)
            pg.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    Main().run()