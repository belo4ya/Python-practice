"""
Реализация быстрой сортировки на чистом Python.
https://ru.wikipedia.org/wiki/Быстрая_сортировка
"""


def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array.pop()
    greater = []
    lesser = []
    for el in array:
        if el > pivot:
            greater.append(el)
        else:
            lesser.append(el)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
