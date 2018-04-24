"""
http://pythontutor.ru/lessons/2d_arrays/problems/chessboard/
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""


n, m = [int(i) for i in input().split()]
lst = [['.'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
            lst[i][j] = '*'

for line in lst:
    print(' '.join(line))

"""
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
"""
