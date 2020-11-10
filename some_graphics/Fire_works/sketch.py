import pyglet
import random
from particle import Particle


def load_particles(batch):
    particles = []
    x = 0
    for i in range(3):
        p = Particle(x + 50, 0, random.randint(0, 255), batch)
        particles.append(p)

    return particles


window = pyglet.window.Window(400, 400)

main_batch = pyglet.graphics.Batch()
particles = load_particles(main_batch)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    for p in particles:
        p.update()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
