import typing

import random

import pygame

from scripts.utils import *
from scripts.Animation import Animation

class Character:
    def __init__(self, world_pos:typing.Sequence, imgs_path:str, tilemap) -> None:
        self.world_pos = list(world_pos)
        self.imgs = load_img(imgs_path)
        self.tilemap = tilemap
        #self.rect = pygame.Rect(*self.pos, *self.img.get_size())
    
    @property
    def x(self):
        return self.world_pos[0]
    @x.setter
    def x(self, value):
        self.world_pos[0] = value
    @property
    def y(self):
        return self.world_pos[1]
    @y.setter
    def y(self, value):
        self.world_pos[1] = value
    
    def move(self, translation:tuple):
        self.x += translation[0] * self.tilemap.tile_width
        self.y -= translation[1] * self.tilemap.tile_width
    def move_to(self, pos:tuple):
        self.world_pos = pos

    def render(self, surf:pygame.Surface):
        surf.blit(self.img, self.world_pos)

class Player(Character):
    def __init__(self, world_pos: typing.Sequence, screen_pos:typing.Sequence, img_src: pygame.Surface, tilemap) -> None:
        super().__init__(world_pos, img_src, tilemap)
        self.screen_pos = screen_pos
        self.is_moving = False
        self.motion = [0,0]
    
    def move(self, dirs: tuple):
        if self.motion == [0,0]:
            self.motion = dirs[0]/10, dirs[1]/10
    
    def update_motion(self):
        for i in range(2):
            if self.motion[i]:
                if self.motion[i] >= 1:
                    self.world_pos[i] += to_1(self.motion[i])
                    self.motion[i] = 0
                else:
                    self.motion[i] += to_1(self.motion[i])/10
    
    def render(self, surf: pygame.Surface):
        surf.blit(self.imgs, self.screen_pos)

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
            new_pos = self.base_pos[0]+(new_move[0]*self.tilemap.tile_width), self.base_pos[1]-(new_move[1]*self.tilemap.tile_width)
            self.move_to(new_pos)
            self.crnt_move = (self.crnt_move+1)%len(self.update_data['motion'])
    
    def render(self, surf: pygame.Surface, cam_offset: tuple[int,int]=(0,0)):
        surf.blit(self.imgs, (self.world_pos[0]-cam_offset[0], self.world_pos[1]-cam_offset[1]))