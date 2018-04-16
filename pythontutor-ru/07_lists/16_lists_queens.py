"""
http://pythontutor.ru/lessons/lists/problems/lists_queens/
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""

# 16 апреля

coords = []
for _ in range(8):
    x, y = [int(i) for i in input().split()]
    coords.append([x, y])

hit_flag = False
for xy in coords:
    for i in range(len(coords)):
        self_pos = coords.index(xy) == i
        if xy[0] == coords[i][0] and not self_pos:
            hit_flag = True
            break
        elif xy[1] == coords[i][1] and not self_pos:
            hit_flag = True
            break
        elif abs(xy[0] - coords[i][0]) == (abs(xy[1] - coords[i][1])) and not self_pos:
            hit_flag = True
            break
    if hit_flag:
        print('YES')
        break
if not hit_flag:
    print('NO')

"""
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
"""
