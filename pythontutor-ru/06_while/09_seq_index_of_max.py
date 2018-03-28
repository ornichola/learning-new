"""
http://pythontutor.ru/lessons/while/problems/seq_index_of_max/
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите индекс наибольшего элемента последовательности.
Если наибольших элементов несколько, выведите индекс первого из них.
Нумерация элементов начинается с нуля.
"""

_index = -1
maximum = -1
inp = -1
while inp != 0:
    inp = int(input())
    _index += 1
    if inp > maximum:
        maximum = inp
        index = _index

print(index)
