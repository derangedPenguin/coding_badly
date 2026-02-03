import pygame as pg

import typing as tp
from scripts.types import *

class Renderable:
    def __init__(self,
                 pos: SupportsVector2,
                 img:pg.Surface|None=None,
                 flipX:tp.Callable[[], bool]=lambda:False,
                 flipY:tp.Callable[[], bool]=lambda:False,
                 renderOverride: tp.Callable[[pg.Surface, pg.Vector2], None]|None=None
                 ):
        """
        :param renderOverride: takes a function in the form (pygame Surface to draw on, pygame Vector2 as cam offset, bool debug) => None, which should render the obj to given surf
        """
        if img is None and renderOverride is None:
            raise Exception("Didn't include any valid render method to Renderable. Please include either an img or renderOverride arg")
        self.pos = pg.Vector2(pos)
        self.img = img
        self.flipX = flipX
        self.flipY = flipY

        self.render = renderOverride
    
    @property
    def x(self):
        return self.pos.x
    @property.setter
    def x(self, val):
        self.pos.x = val
    @property
    def y(self):
        return self.pos.y
    @property.setter
    def y(self, val):
        self.pos.y = val
    
    def render(self, surf:pg.Surface, cam_offset:pg.Vector2, debug:bool=False) -> None:
        surf.blit(
            pg.transform.flip(self.img, self.flipX, self.flipY),
            self.pos + cam_offset
        )