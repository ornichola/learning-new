"""
http://pythontutor.ru/lessons/while/problems/seq_num_even/
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""

count = 0
inp = int(input())
while inp != 0:
    if inp % 2 == 0:
        count += 1
    inp = int(input())

print(count)
