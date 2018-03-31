"""
http://pythontutor.ru/lessons/while/problems/std_dev/
Дана последовательность натуральных чисел x1, x2, ..., xn. Стандартным отклонением называется величина
σ = SQRT( ((x1−s)^2 + (x2−s)^2 + … + (xn−s)^2) / (n−1) ).
где s = (x1+x2+…+xn) / n — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""

sum_of_squares = 0
sum_of_inputs = 0
count = 0
inp = int(input())
while inp != 0:
    count += 1
    sum_of_squares += inp ** 2
    sum_of_inputs += inp
    inp = int(input())

avg = sum_of_inputs / count

sd_numerator = sum_of_squares + count * (avg ** 2) - 2 * avg * sum_of_inputs
sd = (sd_numerator / (count - 1)) ** 0.5

print(sd)
