import os

import pygame

BASE_IMG_PATH = 'data/images/'

#image handling
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

def shift_col(img: pygame.Surface, color: tuple = (255, 255, 255)):
    '''norm_color = (color[0]/255, color[1]/255, color[2]/255)
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            old_color = img.get_at((x,y))
            new_color = [old_color[i] * norm_color[i] for i in range(3)]
            #print(new_color)
            try:
                img.set_at((x,y), new_color)
            except TypeError:
                print()'''
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            old_col = img.get_at((x,y))
            new_col = ((old_col.r+color[0])/2,(old_col.g+color[1])/2,(old_col.b+color[2])/2)
            img.set_at((x,y),new_col)
    return img