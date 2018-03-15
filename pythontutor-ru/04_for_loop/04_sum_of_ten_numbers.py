'''
http://pythontutor.ru/lessons/for_loop/problems/sum_of_ten_numbers/
Дано 10 целых чисел. Вычислите их сумму.
Напишите программу, использующую наименьшее число переменных.
'''

s = 0
for _ in range(10):
    s += int(input())
print(s)
