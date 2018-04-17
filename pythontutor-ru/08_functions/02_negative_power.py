"""
http://pythontutor.ru/lessons/functions/problems/negative_power/
Дано действительное положительное число a и целоe число n.
Вычислите a**n. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
"""


def power(a, n):
    res = 1
    for _ in range(abs(n)):
        res *= a
    if n < 0:
        return 1 / res
    return res


a = float(input())
n = int(input())

print(power(a, n))
