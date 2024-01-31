import sys

import pygame

from scripts.board import Board

THEMES = {
    "evil light":{},
    "dark":{
        "board_background":(30,30,30),
        "gui_background":(60,60,60),
        "borders":(30,30,30),
        "numbers":(60,80,240),
        "selected_num":(40,60,200),
        "invalid_num":(200,0,0),
        "num_background":(60,60,60),
        "selected_num_background":(90,90,90),
        "selected_num_type_background":(75,75,75),
    },
    "sunset":{} 
}

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.FRAMERATE = 60

        #PGScreen's size must be (x,y) where x > y by a decent amount ~5/4ths
        self.PGScreen = pygame.display.set_mode((960,640))
        self.board_screen = pygame.Surface((self.PGScreen.get_height(), self.PGScreen.get_height()))
        self.GUI_screen = pygame.Surface((self.PGScreen.get_width()-self.PGScreen.get_height(), self.PGScreen.get_height()))

        self.theme = THEMES["dark"]
        
        self.board = Board(self.board_screen.get_size(), 20)
        #self.GUI = None


    def run(self):
        while True:
            self.board.render(self.board_screen, self.theme)
            self.GUI_screen.fill(self.theme["gui_background"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_LEFT:
                        self.board.shift_selection((-1,0))
                    if event.key == pygame.K_UP:
                        self.board.shift_selection((0,1))
                    if event.key == pygame.K_RIGHT:
                        self.board.shift_selection((1,0))
                    if event.key == pygame.K_DOWN:
                        self.board.shift_selection((0,-1))
                    
                    if event.key == pygame.K_1:
                        self.board.set_tile(1)
                    if event.key == pygame.K_2:
                        self.board.set_tile(2)
                    if event.key == pygame.K_3:
                        self.board.set_tile(3)
                    if event.key == pygame.K_4:
                        self.board.set_tile(4)
                    if event.key == pygame.K_5:
                        self.board.set_tile(5)
                    if event.key == pygame.K_6:
                        self.board.set_tile(6)
                    if event.key == pygame.K_7:
                        self.board.set_tile(7)
                    if event.key == pygame.K_8:
                        self.board.set_tile(8)
                    if event.key == pygame.K_9:
                        self.board.set_tile(9)
                    if event.key == pygame.K_0:
                        self.board.set_tile("")
                    
                    if event.key == pygame.K_z:
                        self.board.gen_board()
                    #if event.key == pygame.K_x:
                    #    self.board.prep_board()
            
            self.PGScreen.blit(self.board_screen, (0,0))
            self.PGScreen.blit(self.GUI_screen, (self.PGScreen.get_height(),0))
            pygame.display.update()
            self.clock.tick(self.FRAMERATE)

Game().run()