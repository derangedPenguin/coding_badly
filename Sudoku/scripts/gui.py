import pygame as pg

TEXT_DEFAULTS = {'font_name':'sfnsmono', 'font_size':20, 'color':(255,255,255), 'background':None}

def draw_text(surf:pg.Surface, text:str, pos:tuple[int], font:pg.font.Font, data:dict[str]={}):
    """
    basic procedure to construct text and draw to pygame surfaces
    takes top-left position
    """
    text_render = font.render(text,True,data['color'])
    rect = text_render.get_rect()
    rect.topleft = pos
    
    surf.blit(text_render,rect)

#{'prefix':'thingy:','suffix':' units','updatable':98,'pos':(342,96),'text_args':{}}
class GUI:

    BASE_LIST_DATA = {'pos':(0,0),'item_offset':(0,0)}

    BASE_LABEL_DATA = {'prefix':'','suffix':'','updatable':'','pos':(0,0),'text_args':{}}

    def __init__(self, font_args:dict=TEXT_DEFAULTS, **elems:dict) -> None:
        self.elements = {}

        #create font object
        for arg in TEXT_DEFAULTS:
            if arg not in font_args:
                font_args[arg] = TEXT_DEFAULTS[arg]
        self.game_font = pg.font.SysFont(font_args['font_name'], font_args['font_size'])

        #load visible gui elements
        for id, data in elems.items():
            # print(id, data)
            self.fix_elem(data)
            self.elements[id] = data
    
    def fix_elem(self, data):
        # print(data)
        if data['type']=='label':
            for key in self.BASE_LABEL_DATA:
                if key not in data:
                    data[key] = self.BASE_LABEL_DATA[key]
        elif data['type']=='list':
            for elem in data['elems']:
                # print(elem)
                self.fix_elem(elem)
    
    def add_elem(self, id, data:dict):
        for elem in data:
            # print(elem)
            self.fix_elem(elem)
            # print('finished')

        self.elements[id] = data
    
    # def update_elems(self, **data):
    #     for id, updatable in data.items():
    #         self.elements[id]['updatable'] = updatable
    
    def draw_item(self, data, surf, **overrides):
        match data['type']:
                case 'label':
                    draw_text(surf,
                            f'{data['prefix']}{data['updatable']()}{data['suffix']}',
                            data['pos'] if not overrides.get('pos', False) else overrides['pos'],
                            font=self.game_font,
                            data=data['text_args'])
                case 'list':
                    for i, item in enumerate(data['elems']):
                        self.draw_item(item, surf,
                                       pos=(data['pos'][0]+(data['item_offset'][0] * i), data['pos'][1]+(data['item_offset'][1] * i))
                                       )
    
    def render(self, surf):
        for elem in self.elements.values():
            self.draw_item(elem, surf)

