import pygame as pg

import typing as tp
from scripts.types import *

from scripts.Renderable import Renderable

class Collideable(Renderable):
    def __init__(self,
                 pos: SupportsVector2,
                 width:float,
                 height:float,
                 img:pg.Surface|None=None,
                 renderOverride: tp.Callable[[pg.Surface, pg.Vector2], None]|None=None,
                 flipX:tp.Callable[[], bool]=lambda:False,
                 flipY:tp.Callable[[], bool]=lambda:False,
                 ):
        super().__init__(pos, img, flipX=flipX, flipY=flipY, renderOverride=renderOverride)
        self.width = width
        self.height = height
    
    def getRect(self) -> pg.Rect:
        return pg.Rect(*self.pos, self.width, self.height)
    
    def collidesWith(self, obj:pg.Rect) -> bool:
        return self.getRect().colliderect(obj)

class Dynamic(Collideable):
    def __init__(self,
                 pos: SupportsVector2,
                 width:float,
                 height:float,
                 img:pg.Surface|None=None,
                 renderOverride: tp.Callable[[pg.Surface, pg.Vector2], None]|None=None
                 ):
        self.vel = pg.Vector2(0,0)
        super().__init__(pos, width, height, img=img, flipX=lambda:(self.vel[0] < 0), renderOverride=renderOverride)
    
    @property
    def vx(self):
        return self.vel.x
    @property.setter
    def vx(self, val):
        self.vel.x = val
    @property
    def vy(self):
        return self.vel.y
    @property.setter
    def vy(self, val):
        self.vel.y = val
    
    def applyVel(self, collideables:tp.Collection[Collideable]) -> None:
        #test & move X
        new_rect = pg.Rect(self.x+self.vx, self.y, self.width, self.height)

        for obj in collideables:
            r = obj.getRect()
            if obj.collidesWith(new_rect):
                if self
                


class NPC(Dynamic):
    pass

class Player(Dynamic):
    pass