from p5 import *
from drop import Drop

drops = []
i = 0


def setup():
    size(640, 360)
    drops.extend((Drop() for _ in range(400)))


def draw():
    background(230, 230, 230)
    for drop in drops:
        drop.fall()
        drop.show()

    global i
    if i > 180:
        no_loop()
        return
    i += 1
    save_frame("gif/anim.png")


if __name__ == '__main__':
    run()
