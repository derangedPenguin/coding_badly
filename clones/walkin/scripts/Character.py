import typing

import random
import math

import pygame

from scripts.utils import *
from scripts.Animation import Animation

class Character:
    def __init__(self, world_pos:typing.Sequence, imgs_path:str, tilemap) -> None:
        self.world_pos = list(world_pos) #in tilemap coords
        self.img = load_img(imgs_path)
        self.tilemap = tilemap
        self.motion = [0,0]
        self.speed_mult = 1
    
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
    
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(*self.world_pos, *self.img.get_size())
    
    def move(self, dirs: tuple[int, int]):
        '''
        :input dirs: x and y directions to move
        will move only one tile
        '''
        #kicks off motion and sets proper direction, full motion handled in update function
        if self.motion == [0,0]:
            self.motion = [dirs[0]/10, -dirs[1]/10]
            self.world_pos[0] += self.motion[0] * self.speed_mult
            self.world_pos[1] += self.motion[1] * self.speed_mult
    def move_to(self, pos:tuple):
        '''kinda bad rn'''
        self.world_pos = pos
    
    def get_px_pos(self):
        '''get on-screen position in pixels'''
        return self.world_pos[0] * self.tilemap.tile_width, self.world_pos[1] * self.tilemap.tile_width