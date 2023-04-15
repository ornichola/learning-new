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


def task_05():
    """
    Написать бесконечно работающий калькулятор. Детали реализации:
    1. Пользователю предлагается выбрать действие (список действий предварительно выводится на экран):
    ввод "1" - сложение (+)
    ввод "2" - вычитание (-)
    ввод "3" - умножение (*)
    ввод "4" - деление (/)
    2. Если пользователь выбирает недопустимое действие - выводится ошибка и пользователю предлагается выбрать
    действие повторно
    3. Если выбрано существующее действие, пользователю предлагается ввести сначала первое число, затем второе
    4. Если пользователем вводится не число хотя бы в одно из двух значений - выдается ошибка и программа возвращается
    к п.1
    5. Если введены корректные числа - выполняем действие, выводим результат на экран и переходим к п.1
    """

    while True:
        command = input('Выберите действие: 1 (+), 2 (-), 3 (*), 4 (/): ')
        match command:
            case '1':
                a, b = input('Введите первое число: '), input('Введите второе число: ')
                try:
                    a, b = float(a), float(b)
                except ValueError:
                    print('На ввод принимаются только числовые значения')
                print(f'{a} + {b} = {a + b}')
            case '2':
                a, b = input('Введите первое число: '), input('Введите второе число: ')
                try:
                    a, b = float(a), float(b)
                except ValueError:
                    print('На ввод принимаются только числовые значения')
                print(f'{a} - {b} = {a - b}')
            case '3':
                a, b = input('Введите первое число: '), input('Введите второе число: ')
                try:
                    a, b = float(a), float(b)
                except ValueError:
                    print('На ввод принимаются только числовые значения')
                print(f'{a} * {b} = {a * b}')
            case '4':
                a, b = input('Введите первое число: '), input('Введите второе число: ')
                try:
                    a, b = float(a), float(b)
                except ValueError:
                    print('На ввод принимаются только числовые значения')

                try:
                    r = a / b
                    print(f'{a} / {b} = {r}')
                except ZeroDivisionError:
                    print('На ноль делить нельзя')
            case _:
                print('Ошибка. Выберите значения: 1 (+), 2 (-), 3 (*), 4 (/)')

if __name__ == '__main__':
    # task_01(NUMS)
    # task_02(1234567890)
    # task_03({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20})
    # task_04([1, 4, 6, 9, 2, 3, 5])
    task_05()
