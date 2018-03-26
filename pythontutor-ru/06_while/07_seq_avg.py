"""
http://pythontutor.ru/lessons/while/problems/seq_avg/
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""

total = 0
count = 0
inp = int(input())
while inp != 0:
    total += inp
    count += 1
    inp = int(input())

print(total / count)
