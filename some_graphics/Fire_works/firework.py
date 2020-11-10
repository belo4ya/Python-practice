import p5
import random
from particle import Particle


class Firework:

    def __init__(self, batch):
        self.color = tuple(random.randint(0, 255) for _ in range(3))
        self.firework = Particle(p5.random_uniform(400), 0, self.color, True, batch=batch)
        self.bach = batch
        self._exploded = False
        self.particles = []

    def done(self):
        if self._exploded and len(self.particles) == 0:
            return True
        else:
            return False

    def explode(self):
        for _ in range(70):
            p = Particle(self.firework.x, self.firework.y, self.color, False, batch=self.firework.batch)
            self.particles.append(p)

    def update(self):
        if not self._exploded:
            self.firework.update()

            if self.firework.vel.y < 0:
                self._exploded = True
                self.explode()
                self.firework.delete()

        for p in self.particles:
            p.update()

            if p.done():
                self.particles.remove(p)
                p.delete()
