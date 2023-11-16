import pygame

TEXT_DEFAULTS = {'font_name':'San Francisco', 'font_size':16, 'color':(255,255,255)}

def draw_text(surf, text, pos, kwargs):
    for arg in TEXT_DEFAULTS:
        if arg not in kwargs:
            kwargs[arg] = TEXT_DEFAULTS[arg]

    font = pygame.font.SysFont(kwargs['font_name'],kwargs['font_size'])
    text_render = font.render(text,True,kwargs['color'])
    rect = text_render.get_rect()
    rect.center = pos#(pos[0]+rect.width/2,pos[1]+rect.height/2)
    surf.blit(text_render,rect)

class GUI:
    def __init__(self, items:dict={}) -> None:
        self.items = items
        #format {'score':{'pos':(x,y),'text':'42', 'text_args':{stuff}}}
    
    def __getitem__(self, item):
        return self.items[item]
    
    def render(self, surf):
        for item in self.items.values():
            draw_text(surf, item['text'], item['pos'], item['text_args'])

class Button:
    def __init__(self, pos, size, text_data) -> None:
        self.pos = list(pos)
        self.size = size
        self.text = text_data[0]
        self.text_args = text_data[1]

        self.rect = pygame.Rect(*self.pos, *self.size)
        self.centered_rect = pygame.Rect(self.pos[0] - self.size[0]//2, self.pos[1] - self.size[1]//2, *self.size)

        self.hovered = False
    
    def render(self, surf):
        fill_color = [180 if not self.hovered else 220]*3

        pygame.draw.rect(surf, fill_color, self.centered_rect)
        pygame.draw.rect(surf, (0,0,0), self.centered_rect, width=5)
        draw_text(surf, self.text, self.pos, self.text_args)
