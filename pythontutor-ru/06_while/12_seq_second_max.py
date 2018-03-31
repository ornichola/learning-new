"""
http://pythontutor.ru/lessons/while/problems/seq_second_max/
Последовательность состоит из различных натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
"""

max_prev = 0
max_curr = 0
inp = -1
while inp != 0:
    if inp > max_curr:
        max_prev = max_curr
        max_curr = inp
    elif inp > max_prev:
        max_prev = inp
    inp = int(input())

print(max_prev)
