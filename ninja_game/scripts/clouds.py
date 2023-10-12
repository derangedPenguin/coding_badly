import random as rand

class Cloud:
    def __init__(self, pos, img, speed, depth) -> None:
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, cam_offset):
        render_pos = (self.pos[0] - cam_offset[0] * self.depth, self.pos[1] - cam_offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

class Clouds:
    def __init__(self, cloud_images, count = 16) -> None:
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud((rand.random() * 99999, rand.random() * 99999), rand.choice(cloud_images), rand.random() * 0.05 + 0.05, rand.random() * 0.6 + 0.2))

        self.clouds.sort(key=lambda x: x.depth)

    def update(self):
        for cloud in self.clouds:
            cloud.update()
    
    def render(self, surf, cam_offset=(0,0)):
        for cloud in self.clouds:
            cloud.render(surf, cam_offset=cam_offset)