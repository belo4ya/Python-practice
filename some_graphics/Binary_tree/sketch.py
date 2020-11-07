from p5 import *
from tree import Tree
import time


class Sketch:
    tree = None

    @classmethod
    def setup(cls):
        size(700, 300)
        background(51)
        cls.tree = Tree()
        for i in range(100):
            cls.tree.add_value(floor(random_uniform(0, 100)))

        cls.tree.traverse()

        result = cls.tree.search(10)
        if result is None:
            print("10 not found")
        else:
            print(result)
            fill(139, 0, 255)
            ellipse(result.x, result.y, 25, 25)
            fill(255)
            no_stroke()
            text(str(result.value), result.x, result.y)

        save_frame("gif/anim.png")
        time.sleep(0.5)


if __name__ == '__main__':
    run(sketch_setup=Sketch.setup, sketch_draw=Sketch.setup)
