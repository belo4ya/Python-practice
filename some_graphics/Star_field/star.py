from p5 import *


class Star:

    def __init__(self):
        self.x = random_uniform(-width, width)
        self.y = random_uniform(-height, height)
        self.z = random_uniform(width)
        self.pz = self.z

    def update(self):
        speed = remap(mouse_x, (0, width), (0, 50))
        self.z -= speed
        if self.z < 1:
            self.z = width
            self.x = random_uniform(-width, width)
            self.y = random_uniform(-height, height)
            self.pz = self.z

    def show(self):
        fill(255)
        no_stroke()

        sx = remap(self.x / self.z, (0, 1), (0, width))
        sy = remap(self.y / self.z, (0, 1), (0, height))

        r = remap(self.z, (0, width), (16, 0))
        ellipse(sx, sy, r, r)

        px = remap(self.x / self.pz, (0, 1), (0, width))
        py = remap(self.y / self.pz, (0, 1), (0, height))

        self.pz = self.z

        stroke(255)
        line(px, py, sx, sy)
