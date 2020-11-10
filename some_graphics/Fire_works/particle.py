import p5
import pyglet


class Particle(pyglet.shapes.Circle):

    def __init__(self, x, y, color, firework, batch=None):
        radius = 2
        if firework:
            radius = 4
        super().__init__(x, y, radius, radius * 5, color, batch)

        self.color = color
        self.firework = firework
        self.opacity = 255
        self._done = False

        self.acc = p5.Vector(0, 0)
        if self.firework:
            self.vel = p5.Vector(0, p5.random_uniform(8, 12))
        else:
            self.vel = p5.Vector.random_2D() * p5.random_uniform(-10, -2)

    @property
    def batch(self):
        return self._batch

    def update(self):
        self.acc += p5.Vector(0, -0.2)

        if not self.firework:
            self.vel *= 0.9
            if self.opacity > 4:
                self.opacity -= 4
            else:
                self._done = True
                self.opacity = 0

        self.vel += self.acc
        pos = p5.Vector(self.x, self.y) + self.vel

        self.x = pos.x
        self.y = pos.y

        self.acc *= 0

    def done(self):
        return self._done
