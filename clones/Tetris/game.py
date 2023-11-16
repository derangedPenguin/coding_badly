import sys
import numpy as np
import random

import pygame

from scripts.board import Board
from scripts.tile import FallingTile, VisualTile
from scripts.utils import load_image, shift_col
from scripts.gui import GUI, Button

BOARD_DIMS = (10, 20)

SPEED_MOD = 4

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption('Not Tetris')
        self.drawn_screen = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.board_display = pygame.Surface((320,640))

        self.rng = np.random.default_rng(10)
        self.rng.random()

        self.tetrominoes = {'I':((0.5,0.5),(-1.5,-0.5),(-0.5,-0.5),(0.5,-0.5),(1.5,-0.5)),
               'O':((0.5,0.5),(-0.5,-0.5),(0.5,-0.5),(-0.5,0.5),(0.5,0.5)),'T':((0,0),(-1,0),(0,0),(1,0),(0,1)),
               'L':((0,0),(-1,0),(0,0),(1,0),(1,-1)),'J':((0,0),(-1,-1),(-1,0),(0,0),(1,0)),
               'S':((0,0),(-1,0),(0,0),(0,-1),(1,-1)),'Z':((0,0),(-1,-1),(0,-1),(0,0),(1,0))}
        self.ttm_colors = {'I':(0,255,255),'O':(255,255,0),'T':(127,255,0),'L':(255,127,0),'J':(0,0,255),'S':(0,255,0),'Z':(255,0,0)}

        self.assets = {
            'circle':load_image('circle.png', scale=(1,1), shift_col=(254,254,254), set_alpha=125),
            0:load_image('gray.png', scale=(4,4)), #gray
        }
        for shape in self.tetrominoes:
            self.assets[shape] = shift_col(self.assets[0].copy(), self.ttm_colors[shape])#(255*self.rng.random(), 255*self.rng.random(), 255*self.rng.random()))

        self.board = Board(self, BOARD_DIMS, 32)

        self.keys_held = {'left':False,'right':False,'down':False, 'shift':False}

        self.gui = GUI({'score':{'pos':(self.screen.get_width()*4/5,300), 'text':'0', 'text_args':{'font_size':48,'color':(255,200,200)}}})
        self.menu_buttons = (Button((self.screen.get_width()//2, self.screen.get_height()//2), (160,80), ('Start', {'font_size':48, 'color':(0,0,0)})), )

        self.new_game()

    def handle_button(self, id):
        match id:
            case 'Start':
                self.new_game()
                self.run_game()
    
    def new_game(self):
        self.board.clear()
        self.score = 0
        self.time_played = 0
        self.tile_sequence = [VisualTile(self, (), random.choice(list(self.tetrominoes.keys()))) for i in range(1)]
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), self.pop_tile())
    
    def new_tile(self):
        prev_speed = self.active_tile.speed
        self.active_tile = FallingTile(self.board, self, (self.board.width//2, 0), self.pop_tile(), speed=min(max(self.score//20, 1), 5))
        self.active_tile.speed_mod = self.keys_held['down'] * SPEED_MOD #transfer speed boost to new tile if applicable
    
    def pop_tile(self):
        #print(self.tile_sequence)
        self.tile_sequence.append(VisualTile(self, (), random.choice(list(self.tetrominoes.keys()))))
        return self.tile_sequence.pop(0).shape_id

    def run_game(self):
        while True:
            self.screen.fill((200,200,200))
            self.board_display.fill((220,220,220))
            
            self.time_played += 1

            self.board.render(self.board_display)

            #handle held movement inputs
            if self.keys_held['left']:
                self.active_tile.timed_shift(-1)
            elif self.keys_held['right']:
                self.active_tile.timed_shift(1)

            #update and render current falling tile
            kill = self.active_tile.update()
            self.active_tile.render(self.board_display)
            if kill:
                self.new_tile()

            self.gui['score']['text'] = f'score: {str(self.score)}'
            self.gui.render(self.screen)

            #render upcoming tile(s)
            for i, tile in enumerate(self.tile_sequence): #for each upcoming tile to be displayed
                tile.render(self.screen, (self.screen.get_width()*4/5, 50+(self.board.tile_size*i*3)))
            
            if self.board.check_filled():
                self.new_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.start_timer('left')
                        self.keys_held['left'] = True
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.start_timer('right')
                        self.keys_held['right'] = True
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = True
                        self.active_tile.speed_mod = SPEED_MOD
                    if event.key in {pygame.K_LSHIFT, pygame.K_RSHIFT}:
                        self.keys_held['shift'] = True
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.active_tile.rotate(not self.keys_held['shift'])
                    if event.key == pygame.K_SPACE:
                        self.active_tile.drop()
                    if event.key == pygame.K_p:
                        self.run_paused()
                if event.type == pygame.KEYUP:
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.active_tile.reset_timer('left')
                        self.keys_held['left'] = False
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.active_tile.reset_timer('right')
                        self.keys_held['right'] = False
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = False
                        self.active_tile.speed_mod = 0
                    if event.key in {pygame.K_LSHIFT, pygame.K_RSHIFT}:
                        self.keys_held['shift'] = True

            self.screen.blit(self.board_display, (self.screen.get_width()/2-self.board_display.get_width()/2,0))
            
            pygame.display.update()
            self.clock.tick(60)
    
    def run_paused(self):
        self.screen.fill((255,255,255, 127))
        while True:
            should_break = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        should_break = True
            if should_break: break

    
    def run_menu(self):
        while True:
            self.drawn_screen.fill((200,200,200))

            mouse_pos = pygame.mouse.get_pos()

            for button in self.menu_buttons:
                button.hovered = button.centered_rect.collidepoint(mouse_pos)
                button.render(self.drawn_screen)

            #draw little bubble around mouse
            self.drawn_screen.blit(self.assets['circle'], (mouse_pos[0]-self.assets['circle'].get_width()//2, mouse_pos[1]-self.assets['circle'].get_height()//2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.menu_buttons:
                            if button.hovered:
                                self.handle_button(button.text)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            self.screen.blit(self.drawn_screen, (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run_menu()
