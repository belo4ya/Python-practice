import pyglet
from walker import Walker

window = pyglet.window.Window(400, 400)
pyglet.gl.glClearColor(0.2, 0.2, 0.2, 1.0)
walker = Walker(200, 200)


@window.event
def on_draw():
    pyglet.shapes.Rectangle(walker.x, walker.y, 2, 2, (224, 30, 130)).draw()


def update(dt):
    walker.step()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
