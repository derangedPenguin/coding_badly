import sys

import pygame

import random

SHAPES = {
    'square':((0,200),(100,100),(200,0),(100,-100),(0,-200),(-100,-100),(-200,0),(-100,100))
}

def next_rand(start, shape, factor = (2,3)):
    chosen = random.choice(shape)
    print(chosen)

    new_point = (int((start[0] + chosen[0])*factor[0]/factor[1]), int((start[1] + chosen[1])*factor[0]/factor[1]))

    return new_point

class main:
    def __init__(self) -> None:
        pygame.init()
        #self.display = pygame.display.set_mode((1280,640))
        self.screen = pygame.display.set_mode((1280,640))
        self.clock = pygame.time.Clock()

        self.shape = SHAPES['square']

        self.points = set()

        self.crnt = (20,20)

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            pygame.draw.lines(self.screen, (255,255,255), True, [(point[0]+self.screen.get_width()//2, point[1]+self.screen.get_height()//2) for point in self.shape])

            self.points.add(next_rand(self.crnt, self.shape))

            for point in self.points:
                self.screen.set_at((point[0]+self.screen.get_width()//2, point[1]+self.screen.get_height()//2), (255,255,255))

            print(len(self.points))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #self.display.blit(self.screen,(self.display.get_width()//2, self.display.get_height()//2))
            pygame.display.update()
            self.clock.tick(60)

main().run()