import pygame as pg
from sys import exit
import math

def update_screen():
    #doesn't work very well, just opening the output image is best
    real_screen.blit(pg.transform.scale(screen, (real_screen.get_width(), screen.get_height()*(real_screen.get_width()/screen.get_width()))), (0,0))
    pg.display.update()

pg.init()
real_screen = pg.display.set_mode((640,640))

img = pg.image.load('arch.jpg').convert()

screen = pg.Surface((img.get_width()*2 + 5, img.get_height()))

#draw original image
screen.blit(img, (0,0))
update_screen()

#handle image
for x in range(img.get_width()):
    for y in range(img.get_height()):
        #get original color
        base = img.get_at((x, y))

        #do modifications
        new = ((math.sin(x+y)+math.pi)/(math.pi*2)*255, (y/img.get_height())*255, base.b)

        #set modifies color
        try:
            img.set_at((x,y), new)
        except ValueError:
            print(new)

#draw modified image
screen.blit(img, (img.get_width()+5, 0))
update_screen()

#save modified image
pg.image.save(img, 'modified.jpg')

#wait for user before closing window
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                pg.quit()
                exit()