"""
http://pythontutor.ru/lessons/sets/problems/sets_intersection/
Даны два списка чисел.
Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""

print(' '.join([str(i) for i in sorted(list((set([int(i) for i in input().split()])).intersection(set([int(i) for i in input().split()]))))]))

"""print(*sorted(set(input().split()) & set(input().split()), key=int))"""
