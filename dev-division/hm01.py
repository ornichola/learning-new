NUMS = [
    849, 200, 809, 164, 926, 84, 892, 666, 880, 869, 775, 707, 874, 195, 120, 275, 328, 228, 43, 445, 421, 246, 666,
    324, 107, 455, 632, 666, 468, 603, 500
]


def task_01(nums: [int]):
    """
    Дан некоторый список чисел.
    Необходимо написать код, который последовательно выводит нечетные числа данного списка,
    а встретив число 666 - останавливает вывод.
    Если мы встречаем число 666 повторно - снова начинаем вывод, только уже четных чисел.
    И так далее.
    """

    print_flag, parity = True, True
    for num in nums:
        if num == 666:
            print_flag = not print_flag
            if print_flag:
                parity = not parity
        else:
            if print_flag and num % 2 == parity:
                print(num)


def task_02(num: int):
    """
    Напишите функцию, которая при заданном целом числе n складывает цифры этого числа и выводит результат.
    """

    _sum = 0
    while num:
        _sum += num % 10
        num //= 10
    print(_sum)


def task_03(dictionary: dict):
    """
    Найдите два ключа с самыми большими значениями в словаре.
    """
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

    if len(dictionary) < 2:
        raise ValueError(f'В словаре {dictionary} меньше двух ключей')
    d = dict()
    biggest = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:2]
    d[biggest[0][0]], d[biggest[1][0]] = biggest[0][1], biggest[1][1]
    print(d)

    # https://stackoverflow.com/questions/39496096/understanding-dictionary-get-in-python
    # print(sorted(dictionary, key=dictionary.get)[-2:])


def task_04(lst: list):
    """
    Дан произвольный список. Необходимо написать минимум 4 способа развернуть данный список в обратную сторону.
    Один из способов должен быть реализован самостоятельно, без использования встроенных возможностей списка.
    """
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


if __name__ == '__main__':
    # task_01(NUMS)
    # task_02(1234567890)
    # task_03({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20})
    task_04([1, 4, 6, 9, 2, 3, 5])