import pygame

import sys

from scripts.utils import Button

class Hub:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))

        self.clicking = False

        self.buttons = []
        self.buttons.append(Button('game-select_1', (self.screen.get_width()//2, self.screen.get_height()//2), (120, 60), 'hello'))

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            for button in self.buttons:
                button.render(self.screen)
            
            if self.clicking:
                pass  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        mouse_pos = pygame.mouse.get_pos()
                        for button in self.buttons:
                            if button.rect.collidepoint(mouse_pos):
                                self.actions(button.action)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False

            pygame.display.update()
    
    def actions(self, action):
        type, key = action.split('_')
        match type:
            case 'game-select':
                match key:
                    case 1:
                        print('pressed')

Hub().run()