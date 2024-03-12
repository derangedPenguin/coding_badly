import pygame

TEXT_DEFAULTS = {'font_name':'San Francisco', 'font_size':16, 'color':(255,255,255)}

def draw_text(surf, text, pos, text_data):
    """basic procedure to construct text and draw to pygame surfaces"""
    for arg in TEXT_DEFAULTS:
        if arg not in text_data:
            text_data[arg] = TEXT_DEFAULTS[arg]

    font = pygame.font.SysFont(text_data['font_name'],text_data['font_size'])
    text_render = font.render(text,True,text_data['color'])
    rect = text_render.get_rect()
    rect.center = pos#(pos[0]+rect.width/2,pos[1]+rect.height/2)
    surf.blit(text_render,rect)

class PGText:
    '''
    class to handle text with basic convenience methods
    '''
    def __init__(self, value, pos:tuple[int,int], prefix:str='', suffix:str='', text_data={}) -> None:
        self.prefix = prefix
        self.suffix = suffix
        self.value = value
        self.pos = pos
        self.text_data = text_data

    def update(self, val):
        self.value = str(val)

    def render(self, surf):
        draw_text(surf, self.prefix+self.value+self.suffix, self.pos, self.text_data)