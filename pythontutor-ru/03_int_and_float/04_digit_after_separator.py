'''
http://pythontutor.ru/lessons/int_and_float/problems/digit_after_separator/
Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
'''

num = float(input())

print(int(((num - int(num)) - ((num - int(num)) % 0.1)) * 10))
#print(int(num * 10) % 10)
