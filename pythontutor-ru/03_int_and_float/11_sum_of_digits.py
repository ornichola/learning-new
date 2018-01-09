'''
http://pythontutor.ru/lessons/int_and_float/problems/sum_of_digits/
Дано трехзначное число. Найдите сумму его цифр.
'''

num = int(input())

print(num // 100 + num // 10 % 10 + num % 10)
