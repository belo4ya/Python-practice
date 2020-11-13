import pyglet
from bubble_sort import BubbleSort

window = pyglet.window.Window(400, 400)
pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1.0)
main_batch = pyglet.graphics.Batch()

bubble_sort = BubbleSort(main_batch)


@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    bubble_sort.update()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
