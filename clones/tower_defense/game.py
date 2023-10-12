import pygame

import sys

from scripts.utils import load_image, load_images
from scripts.entities import Tower, Attacker
from scripts.paths import EntityPath

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))

        self.assets = {
            'tower': load_images('towers'),
            'attacker': load_images('attackers')
        }

        self.towers = []
        self.towers.append(Tower(self, 0, (50,50)))

        self.path = EntityPath(self)
        self.path.import_level('0.json')
        
        self.rounds = [{'timer':0, 'active':False}]

        self.rnd_attackers = []
    
    def run(self):
        while True:
            self.screen.fill((0,175,75))

            pygame.draw.lines(self.screen, (0,0,0), False, (*self.path.points, ))

            if self.rnd_active:
                self.rnd_timer += 1
                self.path.update()

            for tower in self.towers:
                tower.render(self.screen)

            for attacker in self.rnd_attackers:
                exit = attacker.update()
                attacker.render(self.screen)
                if exit:
                    self.rnd_attackers.remove(attacker)

                    if self.rnd_attackers == []:
                        self.rnd_active = False
                        #print(f'round ended')
                        self.rnd_timer = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.path.next_round()
            
            pygame.display.update()

Game().run()