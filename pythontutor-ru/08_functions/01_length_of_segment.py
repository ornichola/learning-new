"""
http://pythontutor.ru/lessons/functions/problems/length_of_segment/
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора.
Попробуйте прочитать о ней на Википедии.
"""


def distance(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return (x ** 2 + y ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
