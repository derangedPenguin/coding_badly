import pygame

class Animation:
    def __init__(self, images, frame_dur, pos_shift=0,loop=False) -> None:
        self.images = images
        self.frame_dur = frame_dur
        self.loops = loop
        self.frame = 0
        self.time = 0
        self.pos_shift = pos_shift
    
    def next(self):
        self.time += 1

        frame_img = self.images[self.frame]

        self.frame = self.time // self.frame_dur

        return frame_img

    def get_anim_pos(self):
        return self.frame * self.pos_shift