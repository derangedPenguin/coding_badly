import os

import pygame

def conv_coord(coord):
    if type(coord) is str:
        return [int(i) for i in coord.split(',')]
    else:
        return f'{coord[0]},{coord[1]}'

def to_1(num):
    try:
        return num/abs(num)
    except ZeroDivisionError:
        return 0


def load_img(path, colorkey=None, dilation=None, size=None):
    img = pygame.image.load(path).convert()
    if not colorkey is None:
        img.set_colorkey(colorkey)
    if not dilation is None:
        pygame.transform.scale(img,(img.get_width()*dilation[0], img.get_height()*dilation[1]))
    if not size is None:
        pygame.transform.scale(img,size)
    return img

def load_imgs(dirpath, colorkey=None, dilation=None, size=None):
    images = []
    for img_name in os.listdir(dirpath):
        images.append(load_img(f'{dirpath}/{img_name}', colorkey, dilation, size))
    return images