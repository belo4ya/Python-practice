from p5 import *
from curve import Curve


class Sketch:
    WIDTH = 600
    HEIGHT = 600

    angle = 0
    w = 120
    cols = WIDTH // w - 1
    rows = HEIGHT // w - 1
    curves = []

    @classmethod
    def setup(cls):
        size(cls.HEIGHT, cls.WIDTH)

        for j in range(cls.rows):
            cls.curves.append(list())
            for i in range(cls.cols):
                cls.curves[j].append(Curve())

    @classmethod
    def draw(cls):
        background(51)
        d = cls.w - 0.2 * cls.w
        r = d / 2

        no_fill()
        stroke(255)
        for i in range(cls.cols):
            cx = cls.w + i * cls.w +cls. w / 2
            cy = cls.w / 2
            stroke_weight(1)
            stroke(255)
            ellipse(cx, cy, d, d)
            x = r * cos(cls.angle * (i + 1) - HALF_PI)
            y = r * sin(cls.angle * (i + 1) - HALF_PI)
            stroke_weight(8)
            stroke(255)
            point(cx + x, cy + y)
            stroke(255, 150)
            stroke_weight(1)
            line(cx + x, 0, cx + x, height)

            for j in range(cls.rows):
                cls.curves[j][i].x = cx + x

        no_fill()
        stroke(255)
        for j in range(cls.rows):
            cx = cls.w / 2
            cy = cls.w + j * cls.w + cls.w / 2
            stroke_weight(1)
            stroke(255)
            ellipse(cx, cy, d, d)
            x = r * cos(cls.angle * (j + 1) - HALF_PI)
            y = r * sin(cls.angle * (j + 1) - HALF_PI)
            stroke_weight(8)
            stroke(255)
            point(cx + x, cy + y)
            stroke(255, 150)
            stroke_weight(1)
            line(0, cy + y, width, cy + y)

            for i in range(cls.cols):
                cls.curves[j][i].y = cy + y

        for j in range(cls.rows):
            for i in range(cls.cols):
                cls.curves[j][i].add_point()
                cls.curves[j][i].show()

        cls.angle -= 0.05
        if cls.angle < - TWO_PI:
            for j in range(cls.rows):
                for i in range(cls.cols):
                    cls.curves[j][i].reset()

            cls.angle = 0
            clear()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw)
