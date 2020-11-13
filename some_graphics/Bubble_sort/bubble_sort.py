import numpy as np
import time
import pyglet
import p5


class BubbleSort:

    def __init__(self, batch: pyglet.graphics.Batch):
        self.width = 2
        self.values = np.random.random(400 // (2 * self.width)) * 400
        self.i = 0
        self.j = 0

        self._batch = batch
        self._lines = []
        for i in range(0, 400, self.width * 2):
            self._lines.append(pyglet.shapes.Line(i, 0, i, self.values[i // (2 * self.width)],
                                                  width=self.width, batch=self._batch))

    def update(self):
        if self.i < len(self.values) - self.j - 1:
            self._lines[self.i - 1].color = (255, 255, 255)
            self._lines[self.i].color = (255, 0, 0)
            if self.values[self.i] > self.values[self.i + 1]:
                self.values[self.i], self.values[self.i + 1] = self.values[self.i + 1], self.values[self.i]

                self._lines[self.i].x, self._lines[self.i + 1].x = self._lines[self.i + 1].x, self._lines[self.i].x
                self._lines[self.i].x2, self._lines[self.i + 1].x2 = self._lines[self.i + 1].x2, self._lines[self.i].x2
                self._lines[self.i], self._lines[self.i + 1] = self._lines[self.i + 1], self._lines[self.i]

            self.i += 1
        else:
            self.j += 1
            self.i = 0

        if np.array_equal(np.sort(self.values), self.values):
            print(self.values)
            time.sleep(5)
            self._reset()

    def _reset(self):
        self.i = 0
        self.j = 0
        self.values = np.random.random(400 // self.width) * 400

        for i in range(0, 400, self.width):
            self._lines[i // self.width].delete()

        self._lines = []
        for i in range(0, 400, self.width):
            self._lines.append(pyglet.shapes.Line(i, 0, i, self.values[i // self.width], width=2, batch=self._batch))


if __name__ == '__main__':
    print(p5.remap(0.1, (0, 1), (0, 255)))