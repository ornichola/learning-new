"""
http://pythontutor.ru/lessons/while/problems/seq_num_maximal/
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""

inp = -1
maximum = 0
count = 1
while inp != 0:
    if inp > maximum:
        maximum = inp
        count = 1
    elif inp == maximum:
        count += 1
    inp = int(input())

print(count)
