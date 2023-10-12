import pygame

import sys

from scripts.utils import load_image, load_images, load_sheet
from scripts.tilemap import Tilemap
from scripts.entities import Player

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Worse Than Terraria')

        self.clock = pygame.time.Clock()

        self.assets = {
            'player': pygame.transform.scale(load_image('player.png'), (48,72)), 
            '0': load_sheet('data/images/sheets/Tiles_0.png')
        }

        self.tilemap = Tilemap(self, tile_size=24)

        self.player = Player(self, (3,3))
        self.player_movement = [False, False]

        self.cam_offset = [0,0]

    def run(self):
        while True:
            self.screen.fill((0,200,255))

            self.cam_offset[0] += (self.player.rect().centerx - self.screen.get_width()//2 -  self.cam_offset[0]) // 30
            self.cam_offset[1] += (self.player.rect().centery - self.screen.get_height()//2 -  self.cam_offset[1]) // 30

            self.tilemap.render(self.screen, cam_offset=self.cam_offset)

            self.player.update(self.tilemap, (self.player_movement[1] - self.player_movement[0],0))
            self.player.render(self.screen, cam_offset=self.cam_offset)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_a,pygame.K_LEFT):
                        self.player_movement[0] = True
                    if event.key in (pygame.K_d,pygame.K_RIGHT):
                        self.player_movement[1] = True
                    if event.key in (pygame.K_w,pygame.K_UP,pygame.K_SPACE):
                        self.player.jump(1)
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_a,pygame.K_LEFT):
                        self.player_movement[0] = False
                    if event.key in (pygame.K_d,pygame.K_RIGHT):
                        self.player_movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)
    
Game().run()