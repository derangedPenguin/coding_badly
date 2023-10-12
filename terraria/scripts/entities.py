import pygame

from math import sqrt

TERMINAL_VELOCITY = 86.9425 * 24 / 60

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size) -> None:
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {'up':False, 'right':False, 'down':False, 'left':False}

        self.flip = False

    def rect(self):
        return pygame.Rect(*self.pos, *self.size)
    
    def jump(self, power):
        self.velocity[1] = -1 * (self.size[1] / 5) * power
    
    def update(self, tilemap, movement=(0,0)):
        self.collisions = {'up':False, 'right':False, 'down':False, 'left':False}

        frame_movement = (movement[0] * 6 + self.velocity[0], movement[1] * 6 + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for tile_rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(tile_rect):
                if frame_movement[0] > 0:
                    entity_rect.right = tile_rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = tile_rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for tile_rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(tile_rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = tile_rect.top
                    self.collisions['down'] = True
                    self.velocity[1] = 0
                if frame_movement[1] < 0:
                    entity_rect.top = tile_rect.bottom
                    self.collisions['up'] = True
                    self.velocity[1] = 0
                self.pos[1] = entity_rect.y
            
        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        '''if self.velocity[1] == 0:
            self.velocity[1] += 0.5
        elif self.velocity[1] > 0:
            self.velocity[1] = self.velocity[1] / 2
        elif self.velocity[1] > 0:
            self.velocity[1] = self.velocity[1] * 2
        print(self.velocity[1])'''
        
        self.velocity[1] = min(TERMINAL_VELOCITY, self.velocity[1] + 0.5)
        #print(self.velocity[1])

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, surf, cam_offset=(0,0)):
        surf.blit(pygame.transform.flip(self.game.assets['player'], self.flip, False), (self.pos[0] - cam_offset[0], self.pos[1] - cam_offset[1]))

class Player(PhysicsEntity):
    def __init__(self, game, pos) -> None:
        super().__init__(game, 'player', pos, (48,72))

    def update(self, tilemap, movement=(0,0)):
        super().update(tilemap, movement=movement)
    
    def render(self, surf, cam_offset=(0,0)):
        super().render(surf, cam_offset=cam_offset)