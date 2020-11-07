from p5 import *


class Sketch:

    @classmethod
    def setup(cls):
        size(400, 400)

    @classmethod
    def draw(cls):
        background(51)
        stroke(255)
        translate(200, height)
        cls.branch(100)

    @classmethod
    def branch(cls, length):
        angle = remap(mouse_x, (0, 2 * width), (0, TWO_PI))
        line(0, 0, 0, -length)
        translate(0, -length)
        if length > 4:
            push_matrix()
            rotate(angle)
            cls.branch(length * 0.67)
            pop_matrix()
            push_matrix()
            rotate(-angle)
            cls.branch(length * 0.67)
            pop_matrix()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
