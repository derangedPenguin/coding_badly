import json

from pygame import *

class Level:

    BASE_FILE_PATH = 'data/maps/'

    def __init__(self) -> None:
        ...

    def import_level(self, name):
        with open(self.BASE_FILE_PATH+name) as file:
            