"""
http://pythontutor.ru/lessons/sets/problems/polyglotes/

Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков.
Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков,
которое он знает, а затем - названия языков, по одному в строке.

В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""

students = []
for i in range(int(input())):
    languages = set()
    for j in range(int(input())):
        languages.add(input())
    students.append(languages)

all_languages = set()
knows_all = students[0]
for s in students:
    knows_all &= s
    all_languages |= s

print(len(knows_all))
print('\n'.join([l for l in sorted(knows_all)]))
print(len(all_languages))
print('\n'.join([l for l in sorted(all_languages)]))

"""
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
"""
