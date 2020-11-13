import pyglet
import numpy as np


class Sketch:
    window = pyglet.window.Window(400, 400)
    pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1.0)
    main_batch = pyglet.graphics.Batch()

    def __init__(self):
        values = np.random.random(400) * 400
        i = 0

    @staticmethod
    @window.event
    def on_draw():
        print(1)
        cls.window.clear()
        cls.main_batch.draw()

    def update(self):
        pass

    # @classmethod
    # def draw(cls):
    #     background(0)
    #
    #     if cls.i < len(cls.values):
    #         stroke(255)
    #         for j in range(len(cls.values) - 1 - cls.i):
    #             if cls.values[j] > cls.values[j + 1]:
    #                 cls.values[j], cls.values[j + 1] = cls.values[j + 1], cls.values[j]
    #     else:
    #         no_loop()
    #
    #     cls.i += 1
    #
    #     for n in range(len(cls.values)):
    #         stroke(255)
    #         line(n, height, n, height - cls.values[n])


if __name__ == '__main__':
    pyglet.clock.schedule_interval(Sketch().update, 1 / 120.0)
    pyglet.app.run()
