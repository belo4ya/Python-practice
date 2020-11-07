# алгоритму 0 лет
def bubble_sort_1(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# алгоритму 5 лет
def bubble_sort_2(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# это все еще сортировка пузырьком
def bubble_sort_3(array):
    for i in range(len(array) - 1):
        f = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                f = True

        if not f:
            break

    return array
