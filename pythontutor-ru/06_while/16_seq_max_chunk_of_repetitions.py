"""
http://pythontutor.ru/lessons/while/problems/seq_max_chunk_of_repetitions/
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""

inp = -1
count = 0
streak = 0
while inp != 0:
    prev = inp
    inp = int(input())
    if inp == prev:
        count += 1
    else:
        if streak < count:
            streak = count
        count = 1

print(streak)
