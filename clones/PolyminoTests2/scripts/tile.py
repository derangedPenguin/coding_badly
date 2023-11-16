import random
import pygame

FRAMERATE = 20

class FallingTile:
    def __init__(self, board, game, pos, shape_id, speed=1) -> None:
        pos_offset = list(game.tetrominoes[shape_id][0])
        self.pos = [pos[0]+pos_offset[0], pos[1]+pos_offset[1]]
        self.board = board
        self.shape_id = shape_id
        self.game = game
        self.timers_active = {'main':True, 'left':False, 'right':False}
        self.timers = {'main':0, 'left':0, 'right':0}
        """time in frames since each timer started"""
        self.speed = speed
        self.speed_mod = 0

        self.freezing = 0

        self.own_offsets = self.game.tetrominoes[self.shape_id][1:]

        #stuff for overall rect collision with more complex shapes
        self.left = self.own_offsets[0][0]
        self.top = self.own_offsets[0][1]
        self.right = self.own_offsets[-1][0]
        self.bottom = self.own_offsets[-1][0]

    def freeze(self):
        for offset in self.own_offsets:
            self.board[self.pos[1] + offset[1]][self.pos[0] + offset[0]] = self.shape_id
        self.freezing = 0
    
    def shape_collide(self, pos, offsets) -> bool:
        try:
            for offset in offsets:
                if self.board.tiles[pos[1]+offset[1]][pos[0]+offset[0]] != 0:
                    return True
        except KeyError:
            return True
        return False

    def shift(self, shift: tuple = (0,0)):
        if moved := (not self.shape_collide((self.pos[0]+shift[0], self.pos[1]+shift[1]), self.own_offsets)):
            self.pos[0] += shift[0]
            self.pos[1] += shift[1]
        return moved
    
    def timed_shift(self, shift):
        shift_dir = 'left' if shift == -1 else 'right'
        if self.timers[shift_dir] % (FRAMERATE / 4) == 0 or self.timers[shift_dir] == 0: #if current time aligns with allowed motion
            self.shift((shift, 0))
    
    def start_timer(self, timer_name):
        self.timers_active[timer_name] = True
    
    def reset_timer(self, timer_name):
        self.timers_active[timer_name] = False
        self.timers[timer_name] = 0

    def rotate(self, clockwise):
        new_offsets = []
        for offset in self.own_offsets:
            vectored = pygame.Vector2(offset)
            new_offsets.append(pygame.Vector2.rotate(vectored, (90 if clockwise else -90)))
        if not self.shape_collide(self.pos, new_offsets):
            self.own_offsets = new_offsets
        
    def drop(self):
        moving = True
        while moving:
            moving = self.shift((0,1))
        self.freezing = 25

    def update(self):
        for timer in self.timers:
            if self.timers_active[timer]:
                self.timers[timer] += 1

    def render(self, surf):
        for offset in self.own_offsets:
            pos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
            surf.blit(self.game.assets[self.shape_id], (pos[0] * self.board.tile_size, pos[1] * self.board.tile_size))