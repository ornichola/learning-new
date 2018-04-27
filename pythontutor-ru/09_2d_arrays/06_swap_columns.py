"""
http://pythontutor.ru/lessons/2d_arrays/problems/swap_columns/
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
"""

n, m = [int(i) for i in input().split()]
lst = [[int(i) for i in input().split()] for j in range(n)]
i, j = [int(i) for i in input().split()]


def swap_columns(lst, i, j):
    if i == j or i > m or j > m:
        return lst
    col_i = []
    col_j = []
    for k in range(n):
        for l in range(m):
            if l == i:
                col_i.append(lst[k][l])
            elif l == j:
                col_j.append(lst[k][l])
    for k in range(n):
        for l in range(m):
            if l == i:
                lst[k][l] = col_j[k]
            elif l == j:
                lst[k][l] = col_i[k]
    return lst


for line in swap_columns(lst, i, j):
    print(' '.join([str(c) for c in line]))

"""
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
"""
