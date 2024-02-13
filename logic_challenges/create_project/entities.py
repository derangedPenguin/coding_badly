import pygame

import typing

from funcs import *

class Entity:
    """
    Parent class for basic entities with 
    """
    def __init__(self, game, pos: tuple[int, int], dir: tuple[float,float], radius: float, color: tuple[int, int, int], speed: int, type: str) -> None:
        self.game = game #reference to Game object for grabbing data
        self.pos = list(pos) #x,y coords in pixels
        self.radius = radius #body radius in pixels
        self.color = color #rgb body color
        self.speed = speed #speed in pixels/sec
        self.dir = list(dir) #normalized direction vector
        self.type = type #type of entity (player, enemy, etc.)

    def update(self):
        #apply current motion
        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed

    def render(self, surf):
        pygame.draw.circle(surf, self.color, self.pos, self.radius)

class Player(Entity):
    def __init__(self, game, pos: tuple[int, int], dir: tuple[float, float], radius: float, color: tuple[int, int, int], speed: int) -> None:
        super().__init__(game, pos, dir, radius, color, speed, 'player')   
        
    def check_collide(self, enemies: list[typing.Self]):
        '''
        '''
        for enemy in enemies:
            if distance((self.pos, enemy.pos)) < self.radius + enemy.radius:
                if self.radius < enemy.radius:
                    self.game.lose()
                else:
                    self.radius += 1#enemy.radius
                    self.game.enemies.remove(enemy)
    
    def update(self):
        if self.radius-1 < self.pos[0] + (self.dir[0] * self.speed) < self.game.screen.get_width() - self.radius+1:
            self.pos[0] += self.dir[0] * self.speed
        if self.radius-1 < self.pos[1] + (self.dir[1] * self.speed) < self.game.screen.get_height() - self.radius+1:
            self.pos[1] += self.dir[1] * self.speed

class Enemy(Entity):
    def __init__(self, game, pos: tuple[int, int], dir: tuple[float, float], radius: float, color: tuple[int, int, int], speed: int) -> None:
        super().__init__(game, pos, dir, radius, color, speed, 'enemy')
    
    def update(self):
        super().update()
        #extra 3 is margin
        '''if not pygame.Rect.collidepoint(self.game.game_rect, self.pos):
            return True'''
        return False
    
    def render(self, surf):
        if pygame.Rect.collidepoint(self.game.game_rect, self.pos):
            super().render(surf)
        else:
            return True