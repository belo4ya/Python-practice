import unittest
import random

from bubble_sort import bubble_sort_1, bubble_sort_2, bubble_sort_3


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.n = 1_000
        self.data_int = [random.randint(-100, 100) for _ in range(self.n)]
        self.data_float = [random.random() * 100 for _ in range(self.n)]
        self.data_str = [
            chr(random.randint(97, 122)) +
            chr(random.randint(97, 122)) +
            chr(random.randint(97, 122)) for _ in range(self.n)
        ]
        self.data = [self.data_int, self.data_float, self.data_str]

    def test_bubble_sort_1(self):
        for data in self.data:
            result = sorted(data)
            self.assertEqual(bubble_sort_1(data), result, f"Should be {result}")

    def test_bubble_sort_2(self):
        for data in self.data:
            result = sorted(data)
            self.assertEqual(bubble_sort_2(data), result, f"Should be {result}")

    def test_bubble_sort_3(self):
        for data in self.data:
            result = sorted(data)
            self.assertEqual(bubble_sort_3(data), result, f"Should be {result}")


if __name__ == '__main__':
    unittest.main()
