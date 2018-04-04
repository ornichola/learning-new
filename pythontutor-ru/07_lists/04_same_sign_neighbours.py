"""
http://pythontutor.ru/lessons/lists/problems/same_sign_neighbours/
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""

_l = input().split()
l = [int(i) for i in _l]

for i in range(len(l) - 1):
    if l[i] < 0 and l[i + 1] < 0 or l[i] > 0 and l[i + 1] > 0:
        print(l[i], l[i + 1])
        break
