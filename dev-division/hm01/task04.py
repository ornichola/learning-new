"""
Дан произвольный список. Необходимо написать минимум 4 способа развернуть данный список в обратную сторону.
Один из способов должен быть реализован самостоятельно, без использования встроенных возможностей списка.
"""

def task_04(lst: list):

    print('original', lst)

    # first
    r_01 = list(reversed(lst))
    print('first', r_01)

    # second
    r_02 = lst[::-1]
    print('second', r_02)

    # third
    # lst.reverse()
    # print('third', lst)

    # fourth
    r_04, index = list(), -1
    for _ in range(len(lst)):
        r_04.append(lst[index])
        index -= 1
    print('fourth', r_04)

    # fifth
    r_05 = list()
    for i in lst:
        r_05.insert(0, i)
    print('fifth', r_05)

    # sixth
    r_06 = list()
    for _ in range(len(lst)):
        r_06.append(lst.pop())
    print('n', r_06)


task_04([1, 4, 6, 9, 2, 3, 5])
