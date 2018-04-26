"""
http://pythontutor.ru/lessons/2d_arrays/problems/secondary_diagonal/
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

n = int(input())
lst = [[0] * n for i in range(n)]

_i = 0
_j = n - 1
for i in range(n):
    for j in range(n):
        if j < _j:
            lst[i][j] = 0
        elif i == _i and j == _j:
            lst[i][j] = 1
            _i = _i + 1
            _j = _j - 1
        else:
            lst[i][j] = 2


for line in lst:
    print(' '.join([str(i) for i in line]))

"""
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
"""
