"""
http://pythontutor.ru/lessons/lists/problems/increasing_neighbours/
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""

l = input().split()

prev = int(l[0])
for i in l:
    if int(i) > prev:
        print(i)
    prev = int(i)
