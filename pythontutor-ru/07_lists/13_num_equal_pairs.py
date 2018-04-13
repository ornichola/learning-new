"""
http://pythontutor.ru/lessons/lists/problems/num_equal_pairs/
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

lst = [int(i) for i in input().split()]

count = 0
for i in range(len(lst)-1):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            count += 1
        j += 1

print(count)

"""
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
"""
