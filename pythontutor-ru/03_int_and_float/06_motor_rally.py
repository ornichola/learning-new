'''
http://pythontutor.ru/lessons/int_and_float/problems/motor_rally/
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
'''

import math

n = int(input())
m = int(input())

print(math.ceil(m / n))

'''
n=int(input())
m=int(input())
print(((m-1)//n)+1)
'''
