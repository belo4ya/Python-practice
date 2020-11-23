import random


class Walker:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self):
        rnd = random.randint(0, 3)
        step = 2
        if rnd == 0:
            self.x += step
        elif rnd == 1:
            self.x -= step
        elif rnd == 2:
            self.y += step
        else:
            self.y -= step

        return self.x, self.y
