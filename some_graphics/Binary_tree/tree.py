from p5 import *
from node import Node


class Tree:

    def __init__(self):
        self.root = None

    def traverse(self):
        self.root.visit(self.root)

    def search(self, val):
        return self.root.search(val)

    def add_value(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            self.root.x = width / 2
            self.root.y = 16
        else:
            self.root.add_node(node)
