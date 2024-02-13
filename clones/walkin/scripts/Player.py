import typing

import pygame

from scripts.Character import *

class Player(Character):
    '''main player'''
    def __init__(self, world_pos: typing.Sequence, screen_pos:typing.Sequence, img_src: pygame.Surface, tilemap) -> None:
        super().__init__(world_pos, img_src, tilemap)
        self.screen_pos = screen_pos
        self.motion = [0,0]
        
    def update_motion(self, keys={}):
        if math.isclose(self.x, round(self.x)) and math.isclose(self.y, round(self.y)):
            self.motion = [0,0]
        else:
            self.x = round(self.x + self.motion[0] * self.speed_mult, 1)
            self.y = round(self.y + self.motion[1] * self.speed_mult, 1)
    
    def render(self, surf: pygame.Surface):
        surf.blit(self.img, self.screen_pos)