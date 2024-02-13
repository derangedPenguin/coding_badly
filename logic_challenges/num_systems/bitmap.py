'''len of bin(2**n) is n+1'''
import pygame

import typing

def render_bitmap(map:typing.Sequence[typing.Sequence[bool]], map_width:int, tile_width:float, surf:pygame.Surface, color0:pygame.Color, color1:pygame.Color):
    for map_y in range(len(map)):
        for map_x in range(map_width):
            if map[map_x][map_y]:
                pygame.draw.rect(surf, color1, (map_x*tile_width, map_y*tile_width, tile_width, tile_width))
            else:
                pygame.draw.rect(surf, color0, (map_x*tile_width, map_y*tile_width, tile_width, tile_width))

def int_to_map(num:int)->list[list[bool]]:
    
