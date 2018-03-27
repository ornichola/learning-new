"""
http://pythontutor.ru/lessons/while/problems/seq_max/
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
"""

maximum = 0

inp = int(input())
while inp != 0:
    if inp > maximum:
        maximum = inp
    inp = int(input())

print(maximum)
