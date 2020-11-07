from p5 import *
from drop import Drop


class Sketch:
    drops = []

    @classmethod
    def setup(cls):
        size(640, 360)
        cls.drops.extend((Drop() for _ in range(400)))

    @classmethod
    def draw(cls):
        background(230, 230, 230)
        for drop in cls.drops:
            drop.fall()
            drop.show()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
