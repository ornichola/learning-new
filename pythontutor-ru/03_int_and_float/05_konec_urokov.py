'''
http://pythontutor.ru/lessons/int_and_float/problems/konec_urokov/
В некоторой школе занятия начинаются в 9:00.
Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.
'''

# it's 3 AM and this code smells

# 09 00
h_start = 9
m_start = 0

# brakes
small_brake = 5
big_brake = 15

num = int(input())

import math
if num % 2 == 0:
    total_brake = math.ceil((num - 1) / 2) * small_brake + math.floor((num -1) / 2) * big_brake
elif num % 2 != 0:
    total_brake = (num - 1) / 2 * small_brake + (num -1) / 2 * big_brake
else:
    print('DEBUG - this should not happened')

minutes = (m_start + (45 * num % 60) + (total_brake % 60))
hours = h_start + (45 * num // 60) + (total_brake // 60)
print(int(hours + minutes // 60), int(minutes % 60))

'''
a = int(input())
a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
print(a//60 + 9, a%60)
'''
