# Задача:
# вывести все положительные целочисленные решения уравнения a3 + b3 = c3 + d3,
# где a, b, c и d - целые числа в диапазоне от 1 до 1000.

import math


def solution_1(n=1000):
    """
    решение методом "грубой силы"
    """
    result = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        # print(a, b, c, d)
                        result.append((a, b, c, d))
    return result


def solution_2(n=1000):
    """
    значение d единственное для каждой комбинации a, b, c,
    поэтому продолжать проверку для других значений d не нужно
    """
    result = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        # print(a, b, c, d)
                        result.append((a, b, c, d))
                        break
    return result


def solution_3(n=1000):
    result = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                left = a ** 3 + b ** 3 - c ** 3
                if 0 < left <= n ** 3:
                    d = round(pow(left, 1 / 3))
                    if left == d ** 3:
                        # print(a, b, c, d)
                        result.append((a, b, c, d))
    return result


def solution_4(n=1000):
    """
    вместо того чтобы вычислять все пары (с, d) для каждой пары (а, b), список
    пар (c, d) достаточно построить всего один раз. Тогда для каждой пары (а, b) поиск
    будет вестись по списку (с , d)
    """
    result = []
    map_ = {}
    for c in range(1, n + 1):
        for d in range(1, n + 1):
            res = c ** 3 + d ** 3

            if map_.get(res) is None:
                map_[res] = [(c, d)]
            else:
                map_[res].append((c, d))

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            lst = map_[a ** 3 + b ** 3]
            for pair in lst:
                # print(a, b, pair[0], pair[1])
                result.append((a, b, pair[0], pair[1]))
    return result


def solution_5(n=1000):
    result = []
    map_ = {}


if __name__ == '__main__':
    n = 30
    a = solution_1(n)
    b = solution_2(n)
    c = solution_3(n)
    d = solution_4(n)

    print("\nlen(a) =", len(a), "\nlen(b) =", len(b),
          "\nlen(c) =", len(c), "\nlen(d) =", len(d))

    a = set(a)
    b = set(b)
    c = set(c)
    d = set(d)
    print("\nlen(set(a)) =", len(a), "\nlen(set(b)) =", len(b),
          "\nlen(set(c)) =", len(c), "\nlen(set(d)) =", len(d))

    print("\na ^ b = ", a ^ b)
    print("a ^ c = ", a ^ c)
    print("b ^ c = ", b ^ c)
    print("d ^ c = ", d ^ c)
    for i in a ^ c:
        print(i[0] ** 3 + i[1] ** 3 == i[2] ** 3 + i[3] ** 3)
