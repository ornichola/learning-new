"""
http://pythontutor.ru/lessons/while/problems/seq_increasing_neighbours/
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""

count = 0
inp = int(input())
curr_el = inp
while inp != 0:
    inp = int(input())
    if inp > curr_el:
        count += 1
    curr_el = inp

print(count)
