"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_04_02 Распространённые форматы текстовых файлов: CSV, JSON
"""

"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется 
явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2
"""

import json


data = json.loads(input())

# interpolate input data format for dfs algorithm
relations = dict()
for relation in data:
    for parent in relation.get('parents'):
        if parent not in relations:
            relations[parent] = list()
        relations[parent].append(relation.get('name'))


# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs(vertex, visited):
    count = 1
    visited.add(vertex)
    if vertex in relations:
        for child in relations[vertex]:
            if child not in visited:
                count += dfs(child, visited)
    return count


counted = {relation.get('name'): dfs(relation.get('name'), set()) for relation in data}
for class_name in sorted(counted):
    print(f'{class_name} : {counted[class_name]}')
