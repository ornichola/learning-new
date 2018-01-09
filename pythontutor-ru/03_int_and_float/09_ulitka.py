'''
http://pythontutor.ru/lessons/int_and_float/problems/ulitka/
Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров. На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. Гарантируется, что a>b.
'''

h = int(input())
a = int(input())
b = int(input())

pos = 0
days = 0

while True:
    max_pos = pos + a
    pos += a - b
    days += 1
    if max_pos >= h:
        break
print(days)

#print(math.ceil((h - a) / (a - b)) + 1)
