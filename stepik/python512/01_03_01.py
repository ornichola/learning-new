"""
[STEPIK]
Python: основы и применение https://stepik.org/512
01_02_01 Функции и стек вызовов
"""

"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x 
и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
"""

import math


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return math.ceil(x / 5) * 5


"""
def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)
"""

"""
def closest_mod_5(x):
    return (x + 4) // 5 * 5
"""
