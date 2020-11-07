from p5 import *


class Node:

    def __init__(self, val, x=0, y=0):
        self.value = val
        self.left = None
        self.right = None
        self.x = x
        self.y = y

    def __str__(self):
        return "Node {val='" + str(self.value) + "', " + \
               "x='" + str(self.x) + "', " + \
               "y='" + str(self.y) + "'}"

    __repr__ = __str__

    def search(self, val):
        if self.value == val:
            return self
        elif val < self.value and self.left is not None:
            return self.left.search(val)
        elif val > self.value and self.right is not None:
            return self.right.search(val)

        return None

    def visit(self, parent):
        if self.left is not None:
            self.left.visit(self)

        stroke(255)
        fill(51)
        line(parent.x, parent.y, self.x, self.y)
        ellipse(self.x, self.y, 25, 25)
        fill(255)
        no_stroke()
        text_align(CENTER)
        text(str(self.value), self.x, self.y)

        if self.right is not None:
            self.right.visit(self)

    def add_node(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
                self.left.x = self.x - 50
                self.left.y = self.y + 20
            else:
                self.left.add_node(node)
        elif node.value > self.value:
            if self.right is None:
                self.right = node
                self.right.x = self.x + 50
                self.right.y = self.y + 20
            else:
                self.right.add_node(node)
