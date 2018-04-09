"""
http://pythontutor.ru/lessons/lists/problems/swap_neighbours/
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""

lst = input().split()

for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

for el in lst:
    print(el, end=' ')
