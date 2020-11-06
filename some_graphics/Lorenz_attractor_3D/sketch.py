from p5 import *

x = 0.01
y = 0
z = 0

a = 10
b = 28
c = 8 / 3

points = []


def setup():
    size(800, 600)
    color_mode("HSB")


def draw():
    global x, y, z

    background(0)

    dt = 0.01
    dx = a * (y - x) * dt
    dy = (x * (b - z) - y) * dt
    dz = (x * y - c * z) * dt
    x += dx
    y += dy
    z += dz

    points.append(Vector(x, y, z))

    translate(0, 0, -80)
    cam_x = remap(mouse_x, (0, width), (-200, 200))
    cam_y = remap(mouse_y, (0, height), (-200, 200))
    camera((cam_x, cam_y, height / 2 / tan((PI * 30) / 180)), (0, 0, 0), (0, 1, 0))
    scale(5)
    stroke(255)
    no_fill()

    hu = 0
    begin_shape()

    vertex(points[0].x, points[0].y, points[0].z)
    for v in points:
        stroke(hu, 255, 255)
        vertex(v.x, v.y, v.z)

        hu = (hu + 1) % 255

    end_shape()


if __name__ == '__main__':
    run(mode="P3D")
