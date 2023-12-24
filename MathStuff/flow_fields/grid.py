import numpy as np
import pygame

class Grid:
    def __init__(self, width, height, spacing, margin, base_color=(255,255,255)) -> None:
        self.width = width
        self.height = height
        self.spacing = spacing
        self.margin = margin
        self.base_color = base_color

        self.grid = [
            [{'angle':np.pi*2/3, 'magnitude':8, 'color':base_color, 'pos':(x,y)} 
             for x in range(int(width * -margin), int(width * (margin+1)), self.spacing)
             ] for y in range(int(height * -(margin)), int(height * (margin+1)), self.spacing)
        ]
    
    def __getitem__(self, key):
        return self.grid[key]
    def __setitem__(self, key, value):
        self.grid[key] = value
    
    def __sizeof__(self) -> int:
        return len(self.grid)
    def __len__(self) -> int:
        return len(self.grid)
    
    def get_at_screen(self, coord=tuple[int, int]):
        """
        takes coordinate on surface and returns corresponding point data
        """
        #(coord[0]-self.margin*self.width)      -self.margin*self.width
        #print(f'{coord} - {self.grid[int(coord[0]/self.spacing)][int(coord[1]/self.spacing)]['pos']}')
        return self.grid[int((coord[0]+self.width*self.margin)/self.spacing)][int((coord[1]+self.height*self.margin)/self.spacing)]
    
    def reset(self):
        """
        sets each point back to default values
        """
        for row in self.grid:
            for data in row:
                update_to = {'angle':np.pi*2/3, 'magnitude':10, 'color':self.base_color}
                data.update(update_to)

    def render(self, surf, alpha=1, antialiasing=False, fancy_extension=False):
        """
        renders all points to pygame surface by included data

        alpha represents transparency values of all drawn lines

        antialiasing will blend better across surface, but likely slower in complex situations

        fancy_extension gives similar effect to apple screensaver (wait 2 min to see)
        fancy_extension requires surface arg to support alpha values for proper function
        """
        if not fancy_extension:
            for x, row in enumerate(self.grid):
                for  y, point_data in enumerate(row):
                    screen_x, screen_y = point_data['pos']
                    try:
                        color = pygame.Color((*point_data['color'], alpha))
                    except ValueError:
                        print((*point_data['color'], alpha))
                    pygame.draw.circle(surf, color, (screen_x,screen_y), 1)
                    if antialiasing:
                        pygame.draw.aaline(surf, color, (screen_x,screen_y), (screen_x+point_data['magnitude']*np.cos(point_data['angle']), screen_y+point_data['magnitude']*np.sin(point_data['angle'])))
                    else:
                        pygame.draw.line(surf, color, (screen_x,screen_y), (screen_x+point_data['magnitude']*np.cos(point_data['angle']), screen_y+point_data['magnitude']*np.sin(point_data['angle'])))
        else:
            print('why are you doing this? its not even close to implemented')