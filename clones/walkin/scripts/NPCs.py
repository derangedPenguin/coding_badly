import typing

import pygame

from scripts.Character import *

class NPC(Character):
    def __init__(self, world_pos: typing.Sequence, img_src: pygame.Surface, tilemap, update_data=None) -> None:
        super().__init__(world_pos, img_src, tilemap)
        #if its not gonna update, nullify the function - else setup motion
        if update_data is None or update_data == 'None':
            self.update = lambda : None
        else:
            self.base_pos = world_pos
            self.update_data = update_data
            self.crnt_move = 0
        
    def update1(self):
        if random.random() < 0.01:
            new_move = self.update_data['motion'][self.crnt_move]
            new_pos = self.base_pos[0]+new_move[0], self.base_pos[1]-new_move[1]
            self.move_to(new_pos)
            self.crnt_move = (self.crnt_move+1)%len(self.update_data['motion'])
    
    def render(self, surf: pygame.Surface, cam_offset: tuple[int,int]=(0,0)):
        surf.blit(self.img, ((self.world_pos[0]*self.tilemap.tile_width)-cam_offset[0], (self.world_pos[1]*self.tilemap.tile_width)-cam_offset[1]))