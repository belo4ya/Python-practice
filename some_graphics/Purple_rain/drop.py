from p5 import *


class Drop:

    def __init__(self):
        self.x = random_uniform(width)
        self.y = random_uniform(-500, -50)
        self.z = random_uniform(0, 20)
        self.length = remap(self.z, (0, 20), (10, 20))
        self.y_speed = remap(self.z, (0, 20), (1, 20))

    def fall(self):
        self.y += self.y_speed
        grav = remap(self.z, (0, 20), (0, 0.2))
        self.y_speed += grav

        if self.y > height:
            self.y = random_uniform(-200, -100)
            self.y_speed = remap(self.z, (0, 20), (4, 10))

    def show(self):
        thick = remap(self.z, (0, 20), (1, 3))
        stroke_weight(thick)
        stroke(138, 43, 226)
        line(self.x, self.y, self.x, self.y + self.length)
