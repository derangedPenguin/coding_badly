import pygame

import sys

from scripts.utils import load_image, load_images
from scripts.entities import Attacker
from scripts.paths import EntityPath

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))

        self.assets = {
            'attacker': load_images('attackers')
        }   

        self.path = EntityPath(self)
        self.path.import_level('0.json')
        self.path.rounds = [
            {"0":10},
            {"0":5, "1":10}
        ]

        self.attackers = []
    
    def run(self):
        while True:
            self.screen.fill((0,175,75))

            mouse_pos = pygame.mouse.get_pos()

            pygame.draw.circle(self.screen, (255,255,255), self.path.nearest_point(mouse_pos), 3)

            try:
                pygame.draw.lines(self.screen, (0,0,0), False, (*self.path.points, mouse_pos))
            except ValueError:
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.path.points.append(mouse_pos)
                    if event.button == 3:
                        del self.path.points[self.path.points.index(self.path.nearest_point(mouse_pos))]

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        self.path.export_level('0.json')
            
            pygame.display.update()

Game().run()