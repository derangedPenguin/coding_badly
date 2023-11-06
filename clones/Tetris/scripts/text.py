import pygame

def draw_text(surf, text, pos, font_name='San Francisco', font_size=(16), color=(255,255,255)):
    font = pygame.font.SysFont(font_name,font_size)
    text_render = font.render(text,True,color)
    rect = text_render.get_rect()
    rect.center = (pos[0]+rect.width/2,pos[1])
    surf.blit(text_render,rect)

class TextBox:
    def __init__(self, pos, items) -> None:
        self.pos = pos
        self.items = items
        # {'offset':(x,y), 'text':message_str}
    
    def update(self, new_items, text_only=True):
        if text_only:
            for item in self.items:
                self.items[item]['text'] = new_items[item]


    def render(self, surf):
        for item in self.items:
            draw_text(surf, self.items[item]['text'], (self.pos[0]+self.items[item]['offset'][0], self.pos[1]+self.items[item]['offset'][1]))