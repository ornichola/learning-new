"""
http://pythontutor.ru/lessons/lists/problems/unique_elements/
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

lst = [int(i) for i in input().split()]
unique = None

for i in range(len(lst)):
    for j in range(len(lst)):
        unique = True
        if lst[i] == lst[j] and not i == j:
            unique = False
            break
    if unique:
        print(lst[i])

"""
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
"""
