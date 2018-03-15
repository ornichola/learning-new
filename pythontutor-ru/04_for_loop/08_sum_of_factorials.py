'''
http://pythontutor.ru/lessons/for_loop/problems/sum_of_factorials/
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.
'''

n = int(input())
s = 0
f = 1
for i in range(1, n+1):
    f *= i
    s += f
print(s)
