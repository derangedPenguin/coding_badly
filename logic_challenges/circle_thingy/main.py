"""
All code written by Benjamin McCann

pygame library used to handle graphics and inputs
"""
#Imports
import pygame

import sys

import random

from funcs import *
from entities import Player, Enemy, Entity
from gui import PGText

#Do Everything
class Game:
    #CONSTS
    FPS = 60

    BCKGRND_COLOR = (0,0,0)

    BASE_PLAYER_SIZE = 10
    BASE_PLAYER_SPEED = 5

    MIN_ENEMY_RADIUS = 5
    MAX_ENEMY_RADIUS = 80
    MIN_ENEMY_SPEED = 3
    MAX_ENEMY_SPEED = 8
    BASE_ENEMY_COLOR = (255,255,255)
    ENEMY_COLOR_VARIATION = 55

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((960,640), flags=pygame.RESIZABLE, vsync=True)
        self.clock = pygame.time.Clock()

        self.timer = 0

        self.player = Player(self, (self.screen.get_width()//2, self.screen.get_height()//2), (0,0), self.BASE_PLAYER_SIZE, (255,255,0), self.BASE_PLAYER_SPEED)

        self.spawn_line = ((-self.MAX_ENEMY_RADIUS,-self.MAX_ENEMY_RADIUS),(self.screen.get_width()+self.MAX_ENEMY_RADIUS, -self.MAX_ENEMY_RADIUS), (self.screen.get_width()+self.MAX_ENEMY_RADIUS, self.screen.get_height()+self.MAX_ENEMY_RADIUS), (-self.MAX_ENEMY_RADIUS, self.screen.get_height()+self.MAX_ENEMY_RADIUS))
        self.game_rect = pygame.Rect(*self.spawn_line[0], self.screen.get_width()+(2*self.MAX_ENEMY_RADIUS), self.screen.get_height()+(2*self.MAX_ENEMY_RADIUS))

        self.enemies = []

        self.text = {
            'time':PGText(self.timer, (self.screen.get_width()/2, 20), 'Time: '),
            'e_count':(PGText(len(self.enemies), (self.screen.get_width()/2+40, 20), 'Entities: '))
        }
    
    def lose(self):
        self.player.radius = self.BASE_PLAYER_SIZE
        self.player.speed = self.BASE_PLAYER_SPEED
        self.player.pos = [self.screen.get_width()//2, self.screen.get_height()//2]

        self.enemies.clear()
        self.timer = 0

    def spawn_enemies(self, num):
        for i in range(num):
            radius = (random.random() * (self.MAX_ENEMY_RADIUS-self.MIN_ENEMY_RADIUS+self.player.radius)) + self.MIN_ENEMY_RADIUS
            pos, target = far_points_on_poly(self.spawn_line, self.screen.get_width()*1.25)
            dir = pygame.Vector2((pos[0] - target[0]), (pos[1] - target[1])).normalize()
            color = [val-random.randint(0,self.ENEMY_COLOR_VARIATION) for val in self.BASE_ENEMY_COLOR]
            speed = (random.random() * (self.MAX_ENEMY_SPEED-self.MIN_ENEMY_SPEED)) + self.MIN_ENEMY_SPEED

            self.enemies.append(Enemy(self, pos, dir, radius, color, speed))

    def run(self):
        while True:
            #------------EVENT LOOP------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.VIDEORESIZE:
                    self.spawn_line = ((-self.MAX_ENEMY_RADIUS,-self.MAX_ENEMY_RADIUS),(self.screen.get_width()+self.MAX_ENEMY_RADIUS, -self.MAX_ENEMY_RADIUS), (self.screen.get_width()+self.MAX_ENEMY_RADIUS, self.screen.get_height()+self.MAX_ENEMY_RADIUS), (-self.MAX_ENEMY_RADIUS, self.screen.get_height()+self.MAX_ENEMY_RADIUS))
                    self.game_rect = pygame.Rect(*self.spawn_line[0], self.screen.get_width()+(2*self.MAX_ENEMY_RADIUS), self.screen.get_height()+(2*self.MAX_ENEMY_RADIUS))
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.dir[1] += -1
                    if event.key == pygame.K_a:
                        self.player.dir[0] += -1
                    if event.key == pygame.K_s:
                        self.player.dir[1] += 1
                    if event.key == pygame.K_d:
                        self.player.dir[0] += 1
                    
                    if event.key == pygame.K_SPACE:
                        self.spawn_enemies(2)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.dir[1] -= -1
                    if event.key == pygame.K_a:
                        self.player.dir[0] -= -1
                    if event.key == pygame.K_s:
                        self.player.dir[1] -= 1
                    if event.key == pygame.K_d:
                        self.player.dir[0] -= 1

            #--------------BODY---------------------
            self.timer += 1

            self.screen.fill(self.BCKGRND_COLOR)

            self.player.update()
            self.player.check_collide(self.enemies)
            self.player.render(self.screen)
            
            if random.random() <= 0.3:
                self.spawn_enemies(2)

            for enemy in self.enemies:
                enemy.update()
                kill = enemy.render(self.screen)
                if kill:
                    del enemy
                

            self.text['time'].update(self.timer//60)
            self.text['e_count'].update(len(self.enemies))
            for text in self.text.values():
                text.render(self.screen)

            pygame.display.update()
            self.clock.tick(self.FPS)

Game().run()

pygame.quit()
sys.exit()