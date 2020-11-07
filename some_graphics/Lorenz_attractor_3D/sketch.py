from p5 import *


class Sketch:
    x = 0.01
    y = 0
    z = 0

    a = 10
    b = 28
    c = 8 / 3

    points = []

    @classmethod
    def setup(cls):
        size(800, 600)
        color_mode("HSB")

    @classmethod
    def draw(cls):
        background(0)

        dt = 0.01
        dx = cls.a * (cls.y - cls.x) * dt
        dy = (cls.x * (cls.b - cls.z) - cls.y) * dt
        dz = (cls.x * cls.y - cls.c * cls.z) * dt
        cls.x += dx
        cls.y += dy
        cls.z += dz

        cls.points.append(Vector(cls.x, cls.y, cls.z))

        translate(0, 0, -80)
        cam_x = remap(mouse_x, (0, width), (-200, 200))
        cam_y = remap(mouse_y, (0, height), (-200, 200))
        camera((cam_x, cam_y, height / 2 / tan((PI * 30) / 180)), (0, 0, 0), (0, 1, 0))
        scale(5)
        stroke(255)
        no_fill()

        hu = 0
        begin_shape()

        vertex(cls.points[0].x, cls.points[0].y, cls.points[0].z)
        for v in cls.points:
            stroke(hu, 255, 255)
            vertex(v.x, v.y, v.z)

            hu = (hu + 1) % 255

        end_shape()


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.draw, mode="P3D")
