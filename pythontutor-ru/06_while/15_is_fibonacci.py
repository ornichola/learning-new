"""
http://pythontutor.ru/lessons/while/problems/is_fibonacci/
Дано натуральное число A.
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
Если А не является числом Фибоначчи, выведите число -1.
"""

a = int(input())

b = 0
c = 1
n = 1
while c != a:
    b, c = c, b + c
    n += 1
    if c > a:
        n = -1
        break

print(n)
