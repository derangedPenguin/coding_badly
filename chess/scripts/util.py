import pygame as pg

def load_image(path):
    img = pg.image.load(path).convert()

    img.set_colorkey((0,0,0))

    return img