from p5 import *


class Sketch:
    values = []
    i = 0

    @classmethod
    def setup(cls):
        size(600, 600)
        cls.values.extend((random_uniform(height) for _ in range(width)))

    @classmethod
    def draw(cls):
        background(0)

        if cls.i < len(cls.values):
            stroke(255)
            for j in range(len(cls.values) - 1 - cls.i):
                if cls.values[j] > cls.values[j + 1]:
                    cls.values[j], cls.values[j + 1] = cls.values[j + 1], cls.values[j]
        else:
            no_loop()

        cls.i += 1

        for n in range(len(cls.values)):
            stroke(255)
            line(n, height, n, height - cls.values[n])


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
