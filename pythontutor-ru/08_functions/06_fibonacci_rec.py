"""
http://pythontutor.ru/lessons/functions/problems/fibonacci_rec/
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
