import json

import pygame

from scripts.characters import *
from scripts.utils import *

class Tilemap:
    def __init__(self, game) -> None:
        self.game = game

        self.map = {}
        self.chars_data = {}
        self.player_data = {}

        self.imgs = {}
        self.tile_width = 64

    def __getitem__(self, item):
        return self.map[item]
    def __setitem__(self, item, value):
        self.map[item] = value

    def import_tilemap(self, path):
        '''
        
        '''
        data = json.load(open(path, 'r'))
        self.map = {i['pos']:i for i in data['map']}
        self.chars_data = data['chars']
        self.player_data = data['player']
    def export_tilemap(self, path):
        '''
        unfinished
        '''
        file = open(path, 'w')
        data = {
            'map':{data + {'pos':pos} for pos, data in self.map.items()}
        }
        file.write(json.dumps())
    
    def load_chars_data(self):
        chars = []
        for character in self.chars_data:
            chars.append(NPC([i*self.tile_width for i in conv_coord(character['pos'])], character['img_path'], self, character['update_data']))
        return chars
    def load_player_data(self):
        return Player(conv_coord(self.player_data['pos']), (self.game.screen.get_width()//2,self.game.screen.get_height()//2), self.player_data['img_path'], self)
    def load_tile_data(self):
        '''
        converts necessary tile data into python objects, loads all tile images
        '''
        for tile in self.map.values():
            tile['draw_pos'] = tuple(i*self.tile_width for i in conv_coord(tile['pos']))
            if tile['type'] not in self.imgs:
                self.imgs[tile['type']] = load_img(f'data/images/tiles/{tile['type']}.png', size=(self.tile_width, self.tile_width))
    
    def render(self, surf:pygame.Surface, cam_offset:tuple[float,float]=(0,0)):
        '''
        draws all tiles in tilemap to :param surf:
        :param cam_offset: camera position in pixels
        '''
        for data in self.map.values():
            real_pos = (data['draw_pos'][0]-cam_offset[0], data['draw_pos'][1]-cam_offset[1])
            surf.blit(self.imgs[data['type']], real_pos)