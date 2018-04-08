"""
http://pythontutor.ru/lessons/lists/problems/num_distinct/
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""

lst = [int(i) for i in input().split()]
counter = 1
for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:
        counter += 1

print(counter)
