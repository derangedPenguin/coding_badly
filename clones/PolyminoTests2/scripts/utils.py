import os

import pygame

BASE_IMG_PATH = 'data/images/'

#image handling
def load_image(path, scale: tuple|None = None, colorkey: tuple | None = None, **flags):
    #get image
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()

    #scale image
    if not scale is None:
        img = pygame.transform.scale(img, (img.get_width() * scale[0], img.get_height() * scale[1]))
    
    #manage colorkey
    try:
        if len(colorkey) == 2: # use pixel at coord as color key
            colorkey = img.get_at(colorkey)
    except:
        pass
    if colorkey is not None:
        img.set_colorkey(colorkey)

    #flags
    if flags.get('shift_col', False):
        img = shift_col(img, flags['shift_col'])
    if flags.get('set_alpha', False):
        img.set_alpha(flags['set_alpha'])

    return img

def load_images(path):
    images = []
    for file in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + file))
    return images

def shift_col(img: pygame.Surface, color: tuple = (255, 255, 255)):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            old_col = img.get_at((x,y))
            new_col = ((old_col.r+color[0])/2,(old_col.g+color[1])/2,(old_col.b+color[2])/2, old_col[3])
            img.set_at((x,y),new_col)
    return img