"""
Реализация сортировки слиянием на чистом Python.
https://ru.wikipedia.org/wiki/Сортировка_слиянием
"""


def merge_sort(array):
    if len(array) < 2:
        return array

    def merge(left, right):

        def _merge():
            while left and right:
                if left[0] < right[0]:
                    yield left.pop(0)
                else:
                    yield right.pop(0)
            yield from left
            yield from right

        return list(_merge())

    midpoint = len(array) // 2
    return merge(merge_sort(array[:midpoint]),  merge_sort(array[midpoint:]))
