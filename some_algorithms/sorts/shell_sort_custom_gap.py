"""
Реализация сортировки Шелла на чистом Python.
https://ru.wikipedia.org/wiki/Сортировка_Шелла
"""


def shell_sort(array):
    """
    Эмпирическая последовательность Марцина Циура:
    701, 301, 132, 57, 23, 10, 4, 1
    """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i
            while j >= gap and array[j] < array[j - gap]:
                array[j], array[j - gap] = array[j - gap], array[j]
                j -= gap
    return array
