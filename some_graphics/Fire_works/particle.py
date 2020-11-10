import pyglet
import p5


class Particle(pyglet.shapes.Circle):

    def __init__(self, x, y, hu, firework, batch=None):
        super().__init__(x, y, 4, 500, (hu, 255, 255), batch)
        self.pos = p5.Vector(x, y)
        self.hu = hu
        self.firework = firework
        self.opacity = 255
        self.acc = p5.Vector(0, 0)

        if self.firework:
            self.vel = p5.Vector(0, p5.random_uniform(-12, -8))
        else:
            self.vel = p5.Vector.random_2D() * p5.random_uniform(2, 10)

    def update(self):
        self.acc += p5.Vector(0, 0.2)

        if not self.firework:
            self.vel *= 0.9
            self.radius = 2
            if self.opacity > 4:
                self.opacity -= 4
            else:
                self.opacity = 0

        self.vel += self.acc
        self.pos += self.vel

        self.x = self.pos.x
        self.y = self.pos.y

        self.acc *= 0

    def done(self):
        if self.opacity < 1:
            return True
        else:
            return False
