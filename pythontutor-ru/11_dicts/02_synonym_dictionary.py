"""
http://pythontutor.ru/lessons/dicts/problems/synonym_dictionary/
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
"""

d = {}
for _ in range(int(input())):
    linked = input().split()
    d[linked[0]] = linked[1]

word = input()

for item in d.items():
    if word in item:
        print(item[1] if word == item[0] else item[0])

"""
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
"""