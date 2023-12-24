from sys import exit as sys_exit

import pygame

from snake import Snake
from board import Board

FRAMERATE = 60

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        #self.timer = 0

        self.screen = pygame.display.set_mode((960,640))
        self.canvas = pygame.Surface((640,640))
        
        self.board = Board(18, 18, 35, (23, 153, 58), (33, 173, 71))

        self.snake = Snake(self, 5, (4,9), 1)

    
    def run(self):
        while True:
            #self.timer += 1
            self.screen.fill((0,0,0))
            self.canvas.fill((30,30,30))

            self.board.render(self.canvas)

            self.snake.update()

            self.snake.render(self.canvas, self.board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys_exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.dir = (1,0)
                    if event.key == pygame.K_LEFT:
                        self.snake.dir = (-1,0)
                    if event.key == pygame.K_UP:
                        self.snake.dir = (0,-1)
                    if event.key == pygame.K_DOWN:
                        self.snake.dir = (0,1)

                    if event.key == pygame.K_i:
                        self.snake.len += 2

            self.screen.blit(self.canvas, (0,0))
            pygame.display.update()
            self.clock.tick(FRAMERATE)

Game().run()