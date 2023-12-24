import sys

import pygame

from scripts.tilemap import Tilemap
from scripts.rules import ConwayUpdator

GAME_RATE = 15

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640,480), flags=pygame.RESIZABLE)

        self.offset = [0,0]
        
        self.live_color = (0,0,0)

        self.tilemap = Tilemap(self, tile_size=8)
        self.tilemap.import_tiles('thing1')
        self.updator = ConwayUpdator(self.tilemap)

        self.m_buttons_held = {'left':False, 'right':False}
        self.keys_held = {'up':False, 'right':False, 'down':False, 'left':False}
        self.motion = [0,0]
        self.pan_speed = 1

        self.game_running = False
        self.game_timer = 0

        self.tile_colors = {
            'dead':(255,255,255),
            'live':(0,0,0)
        }

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            if self.game_running:
                self.game_timer += 1
                if self.game_timer % GAME_RATE == 0:
                    self.tilemap.increment(self.updator)

            self.tilemap.render(self.screen, offset=self.offset)

            #handle camera motion to view other parts of grid -- CURRENTLY DISABLED
            self.motion = [self.keys_held['left']-self.keys_held['right'], self.keys_held['up']-self.keys_held['down']]
            self.offset = [self.offset[0]+self.motion[0]*self.pan_speed, self.offset[1]+self.motion[1]*self.pan_speed]

            #handle placing and removing tiles from grid
            if self.m_buttons_held['left']:
                m_pos = pygame.mouse.get_pos()
                grid_x, grid_y = m_pos[0]//(self.tilemap.tile_size+1), m_pos[1]//(self.tilemap.tile_size+1)
                self.tilemap.add_tile((grid_x, grid_y))
            elif self.m_buttons_held['right']:
                m_pos = pygame.mouse.get_pos()
                grid_x, grid_y = m_pos[0]//(self.tilemap.tile_size+1), m_pos[1]//(self.tilemap.tile_size+1)
                if self.tilemap.tiles.get(str(grid_x)+';'+str(grid_y), False):
                    self.tilemap.rem_tile((grid_x, grid_y))


            """-----------------------EVENT LOOP-------------------------"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_running = False
                    if event.button == 1:
                        self.m_buttons_held['left'] = True
                    if event.button == 3:
                        self.m_buttons_held['right'] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.m_buttons_held['left'] = False
                    if event.button == 3:
                        self.m_buttons_held['right'] = False

                if event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.keys_held['up'] = True
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.keys_held['right'] = True
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = True
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.keys_held['left'] = True
                    
                    if not self.game_running and event.key == pygame.K_SPACE: #start
                        self.game_running = True
                    if event.key == pygame.K_p: #pause
                        self.game_running = False
                    if event.key == pygame.K_r: #reset
                        self.game_running = False
                        self.game_timer = 0
                        self.tilemap.tiles = {}
                    
                    if event.key == pygame.K_o:
                        self.tilemap.export_tiles('thing1')
                    if event.key == pygame.K_i:
                        self.tilemap.import_tiles('thing1')
                if event.type == pygame.KEYUP:
                    if event.key in {pygame.K_w, pygame.K_UP}:
                        self.keys_held['up'] = False
                    if event.key in {pygame.K_d, pygame.K_RIGHT}:
                        self.keys_held['right'] = False
                    if event.key in {pygame.K_s, pygame.K_DOWN}:
                        self.keys_held['down'] = False
                    if event.key in {pygame.K_a, pygame.K_LEFT}:
                        self.keys_held['left'] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()