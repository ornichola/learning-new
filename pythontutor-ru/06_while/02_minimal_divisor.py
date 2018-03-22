'''
http://pythontutor.ru/lessons/while/problems/minimal_divisor/
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
'''

num = int(input())

div = num
while divisor > 1:
    if num % div == 0:
        divisor = div
    div -= 1

print(divisor)

'''
i = 2
while n % i != 0:
    i += 1
'''
