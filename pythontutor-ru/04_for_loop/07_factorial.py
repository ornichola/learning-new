'''
http://pythontutor.ru/lessons/for_loop/problems/factorial/
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!.
Пользоваться математической библиотекой math в этой задаче запрещено.
'''

n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)
