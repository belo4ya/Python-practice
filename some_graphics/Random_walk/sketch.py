import pyglet
import random


window = pyglet.window.Window(400, 400)
pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1.0)


def on_draw():
    pass


def update(dt):
    pass


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
