"""
http://pythontutor.ru/lessons/while/problems/kth_fibonacci/
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

По данному числу n определите n-е число Фибоначчи φn.

Эту задачу можно решать и циклом for.
"""

n = int(input())

a = 0
b = 1

for _ in range(n):
    a, b = b, a + b

print(a)
