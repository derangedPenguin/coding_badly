import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path, scale: tuple|None = None):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    img.set_colorkey(img.get_at((0,0)))
    if scale != None:
        img = pygame.transform.scale(img, (img.get_width() * scale[0], img.get_height() * scale[1]))
    return img

def load_images(path):
    images = []
    for file in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + file))
    return images