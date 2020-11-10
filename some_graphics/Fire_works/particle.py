import pyglet
import p5


class Particle(pyglet.shapes.Circle):

    def __init__(self, x, y, hu, batch):
        super(Particle, self).__init__(x, y, 4, 50, (hu, 255, 255), batch)
        self.opacity = 255

    def update(self):
        self.y += 1
        self.opacity -= 4
