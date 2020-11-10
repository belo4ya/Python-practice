import pyglet
import random
from firework import Firework


window = pyglet.window.Window(400, 400)
main_batch = pyglet.graphics.Batch()

fireworks = [Firework(main_batch)]


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    if random.random() < 0.03:
        fireworks.append(Firework(main_batch))

    for f in fireworks:
        f.update()
        if f.done():
            fireworks.remove(f)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
