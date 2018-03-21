'''
http://pythontutor.ru/lessons/while/problems/list_of_squares/
По данному целому числу N распечатайте все квадраты натуральных чисел,
не превосходящие N, в порядке возрастания.
'''

n = int(input())

i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
