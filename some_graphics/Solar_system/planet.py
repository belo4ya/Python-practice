from p5 import *
import math


class Planet:

    def __init__(self, radius, distance, orbit_speed, angle):
        self.radius = radius
        self.distance = distance
        self.orbit_speed = orbit_speed
        self.angle = angle
        self.planets = []

    def orbit(self):
        self.angle += self.orbit_speed
        for planet in self.planets:
            planet.orbit()

    def spawn_moons(self, total, level):
        for i in range(total):
            r = self.radius / level / 2
            d = random_uniform(50, 150)
            o = random_uniform(-0.1, 0.1)
            a = random_uniform(TWO_PI)
            self.planets.append(Planet(r, d / level, o, a))
            if level < 3:
                num = math.floor(random_uniform(0, 4))
                self.planets[i].spawn_moons(num, level + 1)

    def show(self):
        push_matrix()
        fill(255, 100)
        rotate(self.angle)
        translate(self.distance, 0)
        ellipse(0, 0, self.radius * 2, self.radius * 2)
        for planet in self.planets:
            planet.show()
        pop_matrix()
