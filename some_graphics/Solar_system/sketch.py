from p5 import *
from planet import Planet

sun = Planet(50, 0, 0, random_uniform(TWO_PI))


def setup():
    size(600, 600)
    sun.spawn_moons(5, 1)


def draw():
    background(51)
    translate(width / 2, height / 2)
    sun.show()
    sun.orbit()


if __name__ == '__main__':
    run()
