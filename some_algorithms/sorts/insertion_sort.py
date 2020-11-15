"""
Реализация сортировки вставками на чистом Python.
https://ru.wikipedia.org/wiki/Сортировка_вставками
"""


def insertion_sort(array):
    for i, v in enumerate(array[1:]):
        tmp = i
        while i >= 0 and v < array[i]:
            array[i + 1] = array[i]
            i -= 1
        if i != tmp:
            array[i + 1] = v

    return array
