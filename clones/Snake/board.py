import pygame

class Board:
    
    def __init__(self, width, height, tile_width, color1, color2) -> None:
        self.width = width
        self.height = height
        self.tile_width = tile_width

        self.color1 = color1
        self.color2 = color2
    
    def render(self, surf):
        odd_x = False
        odd_y = False
        for screen_x in range(0, self.width*self.tile_width, self.tile_width):
            odd_x = not odd_x
            for screen_y in range(0, self.height*self.tile_width, self.tile_width):
                odd_y = not odd_y
                pygame.draw.rect(surf, self.color1 if (odd_y - odd_x) else self.color2, (screen_x, screen_y, self.tile_width, self.tile_width))
