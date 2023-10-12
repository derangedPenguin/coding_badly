import pygame

import sys

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((9*40,16*40))
        pygame.display.set_caption('')

        self.player_movement = [False, False]

    def run(self):
        while True:
            self.screen.fill((0,200,255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

Game().run()