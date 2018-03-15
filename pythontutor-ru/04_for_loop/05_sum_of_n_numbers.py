'''
http://pythontutor.ru/lessons/for_loop/problems/sum_of_n_numbers/
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N,
затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
'''

inp = int(input())
s = 0
for _ in range(inp):
    s += int(input())
print(s)
