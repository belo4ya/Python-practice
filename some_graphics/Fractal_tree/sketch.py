from p5 import *


def setup():
    size(400, 400)


def draw():
    background(51)
    stroke(255)
    translate(200, height)
    branch(100)


def branch(length):
    angle = remap(mouse_x, (0, 2 * width), (0, TWO_PI))
    line(0, 0, 0, -length)
    translate(0, -length)
    if length > 4:
        push_matrix()
        rotate(angle)
        branch(length * 0.67)
        pop_matrix()
        push_matrix()
        rotate(-angle)
        branch(length * 0.67)
        pop_matrix()


if __name__ == '__main__':
    run()
