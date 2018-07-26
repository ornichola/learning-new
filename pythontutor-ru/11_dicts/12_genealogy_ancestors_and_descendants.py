"""
Даны два элемента в дереве. Определите, является ли один из них потомком другого.

Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K.
В каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2,
если второй является предком первого или 0, если ни один из них не является предком другого.
"""


def is_ancestor(offspring, elder):
    if offspring == elder:
        return True
    while offspring in d:
        offspring = d[offspring]
        if offspring == elder:
            return True
    return False


d = {}
for _ in range(int(input()) - 1):
    child, parent = input().split()
    d[child] = parent

for v in d.values():
    if v not in d:
        d.update({v: None})
        break

for _ in range(int(input())):
    first, second = input().split()
    if is_ancestor(second, first):
        print(1, end=' ')
    elif is_ancestor(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')
