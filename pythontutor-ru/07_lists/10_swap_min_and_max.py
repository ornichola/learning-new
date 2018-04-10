"""
http://pythontutor.ru/lessons/lists/problems/swap_min_and_max/
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""

lst = [int(i) for i in input().split()]

index_el_max = lst.index(max(lst))
index_el_min = lst.index(min(lst))

lst[index_el_max], lst[index_el_min] = lst[index_el_min], lst[index_el_max]

print(' '.join([str(i) for i in lst]))
