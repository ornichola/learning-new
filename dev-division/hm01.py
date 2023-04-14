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

    if len(dictionary) < 2:
        raise ValueError(f'В словаре {dictionary} меньше двух ключей')
    d = dict()
    biggest = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:2]
    d[biggest[0][0]], d[biggest[1][0]] = biggest[0][1], biggest[1][1]
    print(d)
    # print(sorted(dictionary, key=dictionary.get)[-2:])


if __name__ == '__main__':
    # task_01(NUMS)
    # task_02(1234567890)
    task_03({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20})