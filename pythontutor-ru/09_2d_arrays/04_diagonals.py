"""
http://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.
"""

n = int(input())
lst = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        lst[i][j] = abs(i - j)

for line in lst:
    print(' '.join([str(i) for i in line]))

"""
a = [[abs(i - j) for j in range(n)] for i in range(n)]
"""
