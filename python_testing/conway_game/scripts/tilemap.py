import pygame, json

class Tilemap:
    def __init__(self, game, tile_size=8) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}

        for i in range(-100,100):
            self.tiles[str(i + 3) + ';10'] = True
            self.tiles['10;'+str(i + 5)] = True
        #print(json.dumps(self.tiles, indent=4))
        self.establish_edges()
    
    def __getitem__(self, item):
        return self.tiles[item]
        
    def establish_edges(self):
        """
        find outermost defined edges.

        loops through all tiles, don't run repeatedly.
        """
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        for tile in self.tiles:
            x, y = [int(i) for i in tile.split(';')]
            if x < self.left:
                self.left = x
            elif x > self.right:
                self.right = x
            if y < self.top:
                self.top = y
            elif y > self.bottom:
                self.bottom = y
        #print(f'{self.left}\n{self.right}\n{self.top}\n{self.bottom}\n\n')
    
    def check_edge_change(self, tile: tuple[int, int]):
        """checks if argument tile changes edges of board"""
        x, y = tile
        if x < self.left:
            self.left = x
        elif x > self.right:
            self.right = x
        if y < self.top:
            self.top = y
        elif y > self.bottom:
            self.bottom = y

    def render(self, surf: pygame.Surface, offset: tuple[int, int]=(0,0)):
        for x in range(self.left, self.right):
            for y in range(self.top, self.bottom):
                screen_pos = x*self.tile_size - offset[0], y*self.tile_size - offset[1]
                #if surf.get_rect().collidepoint(screen_pos) or True:
                #print(f'screen: {screen_pos}\ngrid: {str(x) + ';' + str(y)}')
                if (str(x) + ';' + str(y)) in self.tiles:
                    pygame.draw.rect(surf, self.game.tile_colors['live'], (*screen_pos, self.tile_size, self.tile_size))
                else: 
                    pygame.draw.rect(surf, self.game.tile_colors['dead'], (*screen_pos, self.tile_size, self.tile_size))