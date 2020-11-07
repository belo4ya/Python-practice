from p5 import *
from planet import Planet


class Sketch:
    sun = Planet(50, 0, 0, random_uniform(TWO_PI))

    @classmethod
    def setup(cls):
        size(600, 600)
        cls.sun.spawn_moons(5, 1)

    @classmethod
    def draw(cls):
        background(51)
        translate(width / 2, height / 2)
        cls.sun.show()
        cls.sun.orbit()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
