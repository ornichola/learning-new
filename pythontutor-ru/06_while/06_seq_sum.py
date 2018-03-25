"""
http://pythontutor.ru/lessons/while/problems/seq_sum/
Определите сумму всех элементов последовательности, завершающейся числом 0.
В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""

total = 0
inp = int(input())
while inp != 0:
    total += inp
    inp = int(input())

print(total)
