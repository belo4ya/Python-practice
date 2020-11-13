import numpy as np
import time
import pyglet


class BubbleSort:

    def __init__(self, batch, total=400, max_=400, width=5, slow=0.01):
        self.total = total
        self.max_ = max_
        self.width = width
        self.slow = slow

        self.values = np.random.random(self.total // (2 * self.width)) * self.max_
        self.i = 0
        self.j = 0
        self._end = False
        self._mode = 0

        self._batch = batch
        self._lines = []
        for i in range(0, self.total, self.width * 2):
            self._lines.append(pyglet.shapes.Line(i, 0, i, self.values[i // (2 * self.width)],
                                                  width=self.width, batch=self._batch))

    def update(self):
        if self.i < len(self.values) - self.j - 1:
            if self.values[self.i] > self.values[self.i + 1]:

                time.sleep(0.01)
                if self._mode == 0:
                    self._lines[self.i].color = (255, 0, 0)
                    self._lines[self.i + 1].color = (0, 0, 255)
                    self._mode = 2
                    return

                time.sleep(0.01)
                if self._mode == 1:
                    for j in range(0, self.total, self.width * 2):
                        self._lines[j // (2 * self.width)].color = [255, 255, 255]
                    self._lines[self.i].color = [255, 0, 0]
                    self._mode = 0
                    return

                time.sleep(0.01)
                self._mode = 1
                self.values[self.i], self.values[self.i + 1] = self.values[self.i + 1], self.values[self.i]

                self._lines[self.i].x, self._lines[self.i + 1].x = self._lines[self.i + 1].x, self._lines[self.i].x
                self._lines[self.i].x2, self._lines[self.i + 1].x2 = self._lines[self.i + 1].x2, self._lines[self.i].x2
                self._lines[self.i], self._lines[self.i + 1] = self._lines[self.i + 1], self._lines[self.i]

            self.i += 1
        else:
            self.j += 1
            self._lines[self.i].color = (255, 255, 255)
            self.i = 0

        if np.array_equal(np.sort(self.values), self.values):
            for j in range(0, self.total, self.width * 2):
                self._lines[j // (2 * self.width)].color = (0, 255, 0)

            if not self._end:
                self._end = True
                return

            time.sleep(3)
            self._reset()

    def _reset(self):
        self.i = 0
        self.j = 0
        self.values = np.random.random(self.total // (2 * self.width)) * self.max_

        for i in range(0, self.total, self.width * 2):
            self._lines[i // (2 * self.width)].delete()

        self._lines = []
        for i in range(0, self.total, self.width * 2):
            self._lines.append(pyglet.shapes.Line(i, 0, i, self.values[i // (2 * self.width)],
                                                  width=self.width, batch=self._batch))
