"""
Реализация сортировки Шелла на чистом Python.
https://ru.wikipedia.org/wiki/Сортировка_Шелла
"""


def shell_sort(array):
    """
    Классический вариант. Последовательность длин промежутков:
    d_1 = N / 2, d_i = d_(i-1) / 2, d_k = 1
    """
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            tmp = array[i]
            j = i
            while j >= 0 and j-gap >= 0 and array[j - gap] > tmp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = tmp
        gap //= 2
    return array
