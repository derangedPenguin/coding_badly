import pygame

def draw_text(surf, text, pos, font_name='Helvetica', font_size=(16), color=(255,255,255)):
    font = pygame.font.SysFont(font_name, font_size)
    text_render = font.render(text, True, color)
    rect = text_render.get_rect()
    rect.center = pos

    surf.blit(text_render, rect)

class Button:
    def __init__(self, action, c_pos, size, text, font_name='helvetica') -> None:
        self.action = action
        self.rect = pygame.Rect(c_pos[0] - size[0]//2, c_pos[1] - size[1]//2, *size)
        self.text = text
        self.font = font_name

    def render(self, surf):
        pygame.draw.rect(surf, (255,255,255), self.rect, width=2)
        draw_text(surf, self.text, self.rect.center, font_size=self.rect.height//2, font_name=self.font)
        