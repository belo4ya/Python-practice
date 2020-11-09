# Задача:
# вывести все положительные целочисленные решения уравнения a3 + b3 = c3 + d3,
# где a, b, c и d - целые числа в диапазоне от 1 до 1000.


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
                map_[res] = []
            map_[res].append((c, d))

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            lst = map_[a ** 3 + b ** 3]
            for pair in lst:
                # print(a, b, pair[0], pair[1])
                result.append((a, b, pair[0], pair[1]))
    return result


def solution_5(n=1000):
    """
    но если мы построили хеш со всеми парами (с, d), генерировать пары (а, b)
    не нужно - каждая пара (а, b) уже присутствует в хеше
    """
    result = []
    map_ = {}
    for c in range(1, n + 1):
        for d in range(1, n + 1):
            res = c ** 3 + d ** 3

            if map_.get(res) is None:
                map_[res] = []
            map_[res].append((c, d))

    for pairs in map_.values():
        for pair_ab in pairs:
            for pair_cd in pairs:
                # print(pair_ab[0], pair_ab[1], pair_cd[0], pair_cd[1])
                result.append((pair_ab[0], pair_ab[1], pair_cd[0], pair_cd[1]))

    return result
