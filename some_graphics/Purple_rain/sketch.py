from p5 import *
from drop import Drop

drops = []


def setup():
    size(640, 360)
    drops.extend((Drop() for _ in range(400)))


def draw():
    background(230, 230, 230)
    for drop in drops:
        drop.fall()
        drop.show()


if __name__ == '__main__':
    run()
