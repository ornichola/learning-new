"""
Напишите функцию, которая при заданном целом числе n складывает цифры этого числа и выводит результат.
"""

def task_02(num: int):
    _sum = 0
    while num:
        _sum += num % 10
        num //= 10
    return _sum


print(task_02(1234567890))
