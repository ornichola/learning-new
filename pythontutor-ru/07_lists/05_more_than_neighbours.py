"""
http://pythontutor.ru/lessons/lists/problems/more_than_neighbours/
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
поскольку у них недостаточно соседей.
"""

_l = input().split()
l = [int(i) for i in _l]

counter = 0
for i in range(1, len(l) - 1):
    if l[i] > l[i - 1] and l[i] > l[i + 1]:
        counter += 1

print(counter)

# if a[i - 1] < a[i] > a[i + 1]:
