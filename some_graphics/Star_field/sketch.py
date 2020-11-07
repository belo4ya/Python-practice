from p5 import *
from star import Star


class Sketch:
    stars = []

    @classmethod
    def setup(cls):
        size(600, 600)
        cls.stars.extend((Star() for _ in range(800)))

    @classmethod
    def draw(cls):
        background(0)
        translate(width / 2, height / 2)
        for s in cls.stars:
            s.update()
            s.show()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
