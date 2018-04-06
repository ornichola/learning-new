"""
http://pythontutor.ru/lessons/lists/problems/maximal_element/
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""

_l = input().split()
l = [int(i) for i in _l]
maximum = l[0]
for i in range(len(l)):
    if l[i] > maximum:
        maximum = l[i]

print(maximum, l.index(maximum))
