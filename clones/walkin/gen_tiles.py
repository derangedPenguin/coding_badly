import json

from scripts.utils import conv_coord

tiles = []

def make_tile(pos:list, path):
    return {'pos':conv_coord(pos), 'type':path}

low_x = int(input('low_x: '))
high_x = int(input('high_x: '))
low_y = int(input('low_y: '))
high_y = int(input('high_y: '))

type = input('type: ')

for x in range(low_x, high_x+1):
    for y in range(low_y, high_y+1):
        tiles.append(make_tile((x,y), type))

print(json.dumps(list(tiles)))