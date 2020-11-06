from p5 import *
from star import Star

stars = []


def setup():
    size(600, 600)
    stars.extend((Star() for _ in range(800)))


def draw():
    background(0)
    translate(width / 2, height / 2)
    for s in stars:
        s.update()
        s.show()


if __name__ == '__main__':
    run()
