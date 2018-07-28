"""
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B,
при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.

Формат входных данных аналогичен предыдущей задаче

Для каждого запроса выведите наименьшего общего предка данных элементов.
"""


def get_ancestors(offspring, d):
    ancestors = list()
    ancestors.append(offspring)
    while offspring in d:
        offspring = d[offspring]
        ancestors.append(offspring)
    return ancestors


d = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    d[child] = parent

m = int(input())
for i in range(m):
    offspring_1, offspring_2 = input().split()
    ancestors_1 = set(get_ancestors(offspring_1, d))
    for ancestor in get_ancestors(offspring_2, d):
        if ancestor in ancestors_1:
            print(ancestor)
            break
