'''
http://pythontutor.ru/lessons/int_and_float/problems/tens_digit/
Дано натуральное число. Найдите число десятков в его десятичной записи.
'''

num = int(input())

print(num % 100 // 10)
#print(num // 10 % 10)
