"""
Реализация сортировки пузырьком на чистом Python.
https://ru.wikipedia.org/wiki/Сортировка_пузырьком
"""


def bubble_sort(array):
    for i in range(len(array) - 1):
        f = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                f = True

        if not f:
            break

    return array
