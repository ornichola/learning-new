"""
http://pythontutor.ru/lessons/while/problems/powers_of_two/
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя!
"""

n = int(input())

powered = 1
power = 0
while powered * 2 <= n:
    powered *= 2
    power += 1

print(power, powered)
