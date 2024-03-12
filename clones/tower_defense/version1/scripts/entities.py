import pygame

import math

from scripts.utils import load_image

FRAME_RATE = 60

ATTACKER_SPEEDS = [10, 30] # must be <= framerate

class Tower:
    def __init__(self, game, t_type, pos) -> None:
        self.game = game
        self.type = t_type
        self.pos = list(pos)
        self.orientation = 90
        self.target = 0
    
    def update(self):
        pass

    def render(self, surf):
        surf.blit(pygame.transform.rotate(self.game.assets['tower'][self.type], self.orientation), self.pos)

class Attacker:
    def __init__(self, game, a_type, path) -> None:
        self.game = game
        self.pos = list(path.points[0]).copy()
        self.type = a_type
        self.speed = ATTACKER_SPEEDS[self.type] / FRAME_RATE # / framerate makes the input pixels per sec
        self.frame_mvmt = (0,0)

        self.img = self.game.assets['attacker'][a_type]#load_image('attackers/'+str(a_type)+'.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.points_passed = 1
        self.path = path
        self.next_pos = self.path.points[0].copy()
        
    def update(self):
        if self.points_passed == len(self.path.points):
            return True

        distance = math.sqrt((self.next_pos[0] - self.pos[0]) ** 2 + (self.next_pos[1] - self.pos[1]) ** 2)
        if distance <= self.speed:
            self.pos = self.next_pos
            self.points_passed += 1
            try:
                self.next_pos = self.path.points[self.points_passed].copy()
            except IndexError:
                return True

            
            
        else:
            x_total_dist = abs(self.next_pos[0] - self.pos[0])
            y_total_dist = abs(self.next_pos[1] - self.pos[1])
            try:
                angle = math.atan(y_total_dist / x_total_dist)
            except ZeroDivisionError:
                angle = 0 if y_total_dist > 0 else 180
            self.frame_mvmt = (self.speed * math.cos(angle) * (-1 if self.next_pos[0] - self.pos[0] < 0 else 1), self.speed * math.sin(angle) * (-1 if self.next_pos[1] - self.pos[1] < 0 else 1))

            self.pos[0] += self.frame_mvmt[0]
            self.pos[1] += self.frame_mvmt[1]

    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0]-self.width//2, self.pos[1]-self.height//2))