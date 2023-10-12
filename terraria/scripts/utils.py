import pygame

import os
import numpy as np

from scripts.sheets import SpriteSheet

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH+path).convert()
    img.set_colorkey((255,255,255))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH+path)):
        images.append(load_image(path + '/' + img_name))
    return images

def load_sheet(path, tile_size=(16,16)):
    sheet = SpriteSheet(path)
    tiles = []
    for y in range(sheet.sheet.get_height() // (tile_size[1] + 2)):
        tiles += sheet.load_strip((0, y * (tile_size[1] + 2), *tile_size), 16, border_pxls=2, colorkey=(0,0,0))
    
    print(pygame.surfarray.pixels_alpha(tiles[-1]))
    empty_tiles = []
    for i in range(len(tiles)):
        if not np.any(pygame.surfarray.pixels_alpha(tiles[i])):
            empty_tiles.append(tiles[i])
    tiles = [i for i in tiles if i not in empty_tiles]

    for i in range(len(tiles)):
        tiles[i] = pygame.transform.scale(tiles[i], (24,24))

    return tiles