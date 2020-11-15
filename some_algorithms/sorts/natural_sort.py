"""
Реализация естественной сортировки строк на чистом Python.
Лексикографический порядок: "file1, file10, file2, file3"
Естественный порядок: "file1, file2, file3, file10"
"""
import re


def natural_sort(array):
    return sorted(array, key=lambda x: [int(s) if s.isdigit() else s.lower() for s in re.split("([0-9]+)", x)])
