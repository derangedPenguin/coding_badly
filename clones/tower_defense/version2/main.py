import sys

from pygame import *

class Game:

    FPS = 60
    
    def __init__(self) -> None:
        init()
        self.screen = display.set_mode((960,640))
        self.clock = time.Clock()

    def run(self):
        while True:
            for event_ in event.get():
                if event_.type == QUIT:
                    quit()
                    sys.exit()
            
            

            display.update()
            self.clock.tick(self.FPS)

Game().run()