"""
Реализация алгоритма двоичного поиска на чистом Python.
"""


def binary_search(a_list, item):
    """
    >>> test_list = [1, 5, 10, 11, 12, 15]
    >>> binary_search(test_list, 20)
    False
    >>> binary_search(test_list, 11)
    True
    """
    if len(a_list) == 0:
        return False

    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1:], item)
